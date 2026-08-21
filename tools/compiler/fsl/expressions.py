"""S04 Stage 2 Pure Deterministic Expressions evaluator adhering to S04#10.1–S04#10.7."""

from dataclasses import dataclass
import math
from typing import Any

from tools.compiler.fsl.models import Diagnostic, DiagnosticCode


class EvaluationError(Exception):
    """Internal exception raised during expression evaluation carrying a Diagnostic."""

    def __init__(self, diagnostic: Diagnostic) -> None:
        super().__init__(diagnostic.message)
        self.diagnostic = diagnostic


def evaluate_static_expression(
    expr_ast: Any,
    context: dict[str, Any] | None = None,
    path: str = "expression",
) -> tuple[Any, list[Diagnostic]]:
    """Statically evaluate a pure deterministic expression AST node adhering to S04#10.1–S04#10.7."""
    ctx = context or {}
    try:
        val = _eval_node(expr_ast, ctx, path)
        return val, []
    except EvaluationError as err:
        return None, [err.diagnostic]
    except Exception as exc:
        return None, [
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#10.1",
                message=f"Static evaluation error: {str(exc)}",
                path=path,
            )
        ]


def _eval_node(node: Any, ctx: dict[str, Any], path: str) -> Any:
    # 1. Raw literal primitives or collections (for convenience or direct values)
    if isinstance(node, (int, float, str, bool)):
        if isinstance(node, float) and (math.isnan(node) or math.isinf(node)):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.1",
                    message=f"Non-finite float value '{node}' is not permitted.",
                    path=path,
                )
            )
        return node

    if isinstance(node, list):
        return [_eval_node(elem, ctx, f"{path}[{i}]") for i, elem in enumerate(node)]

    if not isinstance(node, dict):
        raise EvaluationError(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#10.7",
                message=f"Expression node must be a JSON object, got {type(node).__name__}.",
                path=path,
            )
        )

    # 2. JSON AST Nodes per S04#10.7
    kind = node.get("kind")
    if not kind or not isinstance(kind, str):
        # Plain dictionary treated as raw map literal
        return {k: _eval_node(v, ctx, f"{path}.{k}") for k, v in node.items()}

    if kind == "literal":
        if "value" not in node:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.7",
                    message="Literal expression node missing 'value' field.",
                    path=f"{path}.value" if path else "value",
                )
            )
        val = node["value"]
        if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.1",
                    message="Literal float value must be finite IEEE 754.",
                    path=f"{path}.value" if path else "value",
                )
            )
        return val

    elif kind in ("ref", "identifier", "var"):
        name = node.get("name")
        if not name or not isinstance(name, str):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.7",
                    message="Reference node missing non-empty string 'name' field.",
                    path=f"{path}.name" if path else "name",
                )
            )
        if name not in ctx:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.1",
                    message=f"Unresolved reference identifier '{name}' in expression context.",
                    path=path,
                )
            )
        return ctx[name]

    elif kind in ("unary_op", "unary"):
        op = node.get("op")
        if "operand" not in node:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.7",
                    message="Unary operation missing 'operand' node.",
                    path=f"{path}.operand" if path else "operand",
                )
            )
        operand = _eval_node(node["operand"], ctx, f"{path}.operand")

        if op == "not":
            if not isinstance(operand, bool):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator 'not' requires boolean operand, got {type(operand).__name__}.",
                        path=path,
                    )
                )
            return not operand
        elif op == "-":
            if isinstance(operand, bool) or not isinstance(operand, (int, float)):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Unary negation '-' requires numeric operand, got {type(operand).__name__}.",
                        path=path,
                    )
                )
            return -operand
        else:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.2",
                    message=f"Unrecognized unary operator '{op}'.",
                    path=f"{path}.op" if path else "op",
                )
            )

    elif kind in ("binary_op", "binary"):
        op = node.get("op")
        if "left" not in node or "right" not in node:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.7",
                    message="Binary operation requires both 'left' and 'right' operand nodes.",
                    path=path,
                )
            )
        left = _eval_node(node["left"], ctx, f"{path}.left")
        right = _eval_node(node["right"], ctx, f"{path}.right")

        # Arithmetic & Boolean & Relational Operators per S04#10.2
        if op == "+":
            # String concatenation (S04#10.3) or numeric addition (S04#10.2)
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            elif not isinstance(left, bool) and not isinstance(right, bool) and isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            elif isinstance(left, list) and isinstance(right, list):
                return left + right
            else:
                clause = "S04#10.3" if isinstance(left, (str, list)) or isinstance(right, (str, list)) else "S04#10.2"
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id=clause,
                        message=f"Operator '+' incompatible operand types: {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )

        elif op == "-":
            if isinstance(left, bool) or isinstance(right, bool) or not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator '-' requires numeric operands, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
            return left - right

        elif op == "*":
            if isinstance(left, bool) or isinstance(right, bool) or not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator '*' requires numeric operands, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
            return left * right

        elif op == "/":
            if isinstance(left, bool) or isinstance(right, bool) or not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator '/' requires numeric operands, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
            if right == 0:
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message="Division by zero in pure arithmetic expression.",
                        path=path,
                    )
                )
            if isinstance(left, int) and isinstance(right, int) and left % right == 0:
                return left // right
            return left / right

        elif op == "%":
            if isinstance(left, bool) or isinstance(right, bool) or not isinstance(left, int) or not isinstance(right, int):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator '%' requires integer operands, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
            if right == 0:
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message="Modulo by zero in pure arithmetic expression.",
                        path=path,
                    )
                )
            return left % right

        elif op == "and":
            if not isinstance(left, bool) or not isinstance(right, bool):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator 'and' requires boolean operands, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
            return left and right

        elif op == "or":
            if not isinstance(left, bool) or not isinstance(right, bool):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Operator 'or' requires boolean operands, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
            return left or right

        elif op == "==":
            return left == right

        elif op == "!=":
            return left != right

        elif op in ("<", "<=", ">", ">="):
            # Numeric comparisons or string lexicographical comparisons
            if isinstance(left, bool) or isinstance(right, bool):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Relational operator '{op}' does not permit boolean operands.",
                        path=path,
                    )
                )
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if op == "<":
                    return left < right
                elif op == "<=":
                    return left <= right
                elif op == ">":
                    return left > right
                elif op == ">=":
                    return left >= right
            elif isinstance(left, str) and isinstance(right, str):
                if op == "<":
                    return left < right
                elif op == "<=":
                    return left <= right
                elif op == ">":
                    return left > right
                elif op == ">=":
                    return left >= right
            else:
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.2",
                        message=f"Relational operator '{op}' requires comparable operands of matching type, got {type(left).__name__} and {type(right).__name__}.",
                        path=path,
                    )
                )
        else:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.2",
                    message=f"Unrecognized binary operator '{op}'.",
                    path=f"{path}.op" if path else "op",
                )
            )

    # 3. Conditional Expressions per S04#10.4
    elif kind in ("conditional", "if"):
        cond_node = node.get("condition") or node.get("if")
        then_node = node.get("then") or node.get("consequent")
        else_node = node.get("else") or node.get("alternate")

        if cond_node is None or then_node is None or else_node is None:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.4",
                    message="Conditional expression must specify 'condition', 'then', and 'else' branches.",
                    path=path,
                )
            )
        cond_val = _eval_node(cond_node, ctx, f"{path}.condition")
        if not isinstance(cond_val, bool):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.4",
                    message=f"Conditional expression condition must evaluate to boolean, got {type(cond_val).__name__}.",
                    path=f"{path}.condition",
                )
            )
        if cond_val is True:
            return _eval_node(then_node, ctx, f"{path}.then")
        else:
            return _eval_node(else_node, ctx, f"{path}.else")

    # 4. String & Collection Operations per S04#10.3
    elif kind in ("concat", "string_concat"):
        left_node = node.get("left")
        right_node = node.get("right")
        args_node = node.get("args")

        if args_node is not None and isinstance(args_node, list):
            parts = [_eval_node(a, ctx, f"{path}.args[{i}]") for i, a in enumerate(args_node)]
            for i, p in enumerate(parts):
                if not isinstance(p, str):
                    raise EvaluationError(
                        Diagnostic(
                            code=DiagnosticCode.VALIDATION_ERROR,
                            clause_id="S04#10.3",
                            message=f"String concat argument at index {i} must be string, got {type(p).__name__}.",
                            path=f"{path}.args[{i}]",
                        )
                    )
            return "".join(parts)
        elif left_node is not None and right_node is not None:
            left_val = _eval_node(left_node, ctx, f"{path}.left")
            right_val = _eval_node(right_node, ctx, f"{path}.right")
            if not isinstance(left_val, str) or not isinstance(right_val, str):
                raise EvaluationError(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.3",
                        message=f"String concat requires string operands, got {type(left_val).__name__} and {type(right_val).__name__}.",
                        path=path,
                    )
                )
            return left_val + right_val
        else:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message="Concat node requires 'left'/'right' operands or 'args' array.",
                    path=path,
                )
            )

    elif kind in ("length", "collection_length"):
        target_node = node.get("operand") or node.get("target")
        if target_node is None:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message="Length operation missing target 'operand'.",
                    path=path,
                )
            )
        target_val = _eval_node(target_node, ctx, f"{path}.operand")
        if not isinstance(target_val, (str, list, dict)):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"Length operation requires string, list, or map, got {type(target_val).__name__}.",
                    path=path,
                )
            )
        return len(target_val)

    elif kind in ("index", "list_index"):
        target_node = node.get("target")
        idx_node = node.get("index")
        if target_node is None or idx_node is None:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message="Index operation requires 'target' and 'index' nodes.",
                    path=path,
                )
            )
        target_val = _eval_node(target_node, ctx, f"{path}.target")
        idx_val = _eval_node(idx_node, ctx, f"{path}.index")

        if not isinstance(target_val, list):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"Index operation target must be a list, got {type(target_val).__name__}.",
                    path=f"{path}.target",
                )
            )
        if isinstance(idx_val, bool) or not isinstance(idx_val, int):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"Index operand must be integer, got {type(idx_val).__name__}.",
                    path=f"{path}.index",
                )
            )
        if idx_val < 0 or idx_val >= len(target_val):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"List index {idx_val} out of bounds (length {len(target_val)}).",
                    path=path,
                )
            )
        return target_val[idx_val]

    elif kind in ("lookup", "map_lookup"):
        target_node = node.get("target")
        key_node = node.get("key")
        if target_node is None or key_node is None:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message="Lookup operation requires 'target' and 'key' nodes.",
                    path=path,
                )
            )
        target_val = _eval_node(target_node, ctx, f"{path}.target")
        key_val = _eval_node(key_node, ctx, f"{path}.key")

        if not isinstance(target_val, dict):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"Lookup target must be map or record object, got {type(target_val).__name__}.",
                    path=f"{path}.target",
                )
            )
        if not isinstance(key_val, str):
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"Lookup key must be string, got {type(key_val).__name__}.",
                    path=f"{path}.key",
                )
            )
        if key_val not in target_val:
            raise EvaluationError(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.3",
                    message=f"Key '{key_val}' not found in target object.",
                    path=path,
                )
            )
        return target_val[key_val]

    else:
        raise EvaluationError(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#10.7",
                message=f"Unrecognized expression node kind '{kind}'.",
                path=f"{path}.kind" if path else "kind",
            )
        )


def evaluate_declarative_invariants(
    invariants: list[Any],
    context: dict[str, Any] | None = None,
    path_prefix: str = "invariants",
) -> list[Diagnostic]:
    """Evaluate declarative invariant assertions adhering to S04#10.5 & S04#10.6."""
    diagnostics: list[Diagnostic] = []
    ctx = context or {}

    for idx, inv in enumerate(invariants):
        inv_path = f"{path_prefix}[{idx}]"
        inv_name = f"invariant_{idx}"
        expr_node = inv

        if isinstance(inv, dict):
            if "name" in inv and isinstance(inv["name"], str):
                inv_name = inv["name"]
                inv_path = f"{path_prefix}.{inv_name}"
            if "expr" in inv:
                expr_node = inv["expr"]
            elif "assertion" in inv:
                expr_node = inv["assertion"]

        val, eval_diags = evaluate_static_expression(expr_node, ctx, inv_path)
        if eval_diags:
            diagnostics.extend(eval_diags)
        else:
            if not isinstance(val, bool):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.5",
                        message=f"Invariant '{inv_name}' must evaluate to boolean, got {type(val).__name__}.",
                        path=inv_path,
                    )
                )
            elif val is False:
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#10.5",
                        message=f"Declarative invariant assertion '{inv_name}' evaluated to false.",
                        path=inv_path,
                    )
                )

    return diagnostics
