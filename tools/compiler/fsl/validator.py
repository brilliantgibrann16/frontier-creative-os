"""S04 Stage 1 W-B and Stage 2 schema and semantic boundary validator adhering to S04#5.1–S04#10.7 and S05#2.1–S05#2.4."""

from typing import Any

from tools.compiler.fsl.diagnostics import sort_diagnostics
from tools.compiler.fsl.expressions import (
    evaluate_declarative_invariants,
    evaluate_static_expression,
)
from tools.compiler.fsl.models import (
    Diagnostic,
    DiagnosticCode,
    ValidationOutcome,
    ValidationStatus,
)
from tools.compiler.fsl.types import (
    validate_type_annotation,
    validate_value_conformance,
)


def evaluate_artifact_validity(data: dict[str, Any]) -> ValidationOutcome:
    """Evaluate structural validity (S04#6.1, S04#9.4), validity closure (S04#6.2), and outcome (S04#7.1)."""
    diagnostics: list[Diagnostic] = []
    is_structurally_valid = True
    is_closure_valid = True

    # S04#8.1, S04#8.2, S04#8.3, S05#1.2: Schema version validation (Interchange Form)
    schema_version = data.get("schema_version")
    if schema_version is None:
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message="Missing required top-level 'schema_version' field.",
                path="schema_version",
            )
        )
    elif schema_version != "fsl/1.0":
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message=f"Expected schema_version 'fsl/1.0', got '{schema_version}'.",
                path="schema_version",
            )
        )

    # S04#5.1 & S04#6.1: Single Artifact Unit & Top-level manifest structure
    manifest = data.get("manifest")
    if manifest is None:
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#5.1",
                message="Missing required top-level 'manifest' object.",
                path="manifest",
            )
        )
    elif not isinstance(manifest, dict):
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#5.1",
                message="Top-level 'manifest' must be a JSON object.",
                path="manifest",
            )
        )
    else:
        # S04#6.1: Structural validity of manifest identity
        name = manifest.get("name")
        if name is None:
            is_structurally_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.1",
                    message="Missing required manifest field 'name'.",
                    path="manifest.name",
                )
            )
        elif not isinstance(name, str) or not name.strip():
            is_structurally_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.1",
                    message="Manifest 'name' must be a non-empty string.",
                    path="manifest.name",
                )
            )

        # S04#6.2: Validity closure of manifest version and kind
        version = manifest.get("version")
        if version is None:
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Missing required manifest field 'version'.",
                    path="manifest.version",
                )
            )
        elif not isinstance(version, str) or not version.strip():
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Manifest 'version' must be a non-empty string.",
                    path="manifest.version",
                )
            )

        kind = manifest.get("kind")
        if kind is None:
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Missing required manifest field 'kind'.",
                    path="manifest.kind",
                )
            )
        elif not isinstance(kind, str) or not kind.strip():
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Manifest 'kind' must be a non-empty string.",
                    path="manifest.kind",
                )
            )

        # S04#5.2: Stage 1 self-containment - validate dependencies list if provided
        dependencies = manifest.get("dependencies")
        if dependencies is not None:
            if not isinstance(dependencies, list):
                is_closure_valid = False
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#5.2",
                        message="Manifest 'dependencies' must be a JSON list.",
                        path="manifest.dependencies",
                    )
                )
            else:
                for idx, dep in enumerate(dependencies):
                    if not isinstance(dep, str) or not dep.strip():
                        is_closure_valid = False
                        diagnostics.append(
                            Diagnostic(
                                code=DiagnosticCode.VALIDATION_ERROR,
                                clause_id="S04#5.2",
                                message=f"Dependency at index {idx} must be a non-empty string identifier.",
                                path=f"manifest.dependencies[{idx}]",
                            )
                        )

    # -------------------------------------------------------------
    # Stage 2: S04#9.1–S04#9.4 Typed Data Model Core
    # -------------------------------------------------------------
    declared_types: dict[str, Any] = {}
    types_section = data.get("types")
    if types_section is not None:
        if not isinstance(types_section, dict):
            is_structurally_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.3",
                    message="Top-level 'types' must be a JSON object mapping type names to definitions.",
                    path="types",
                )
            )
        else:
            for type_name, type_def in types_section.items():
                t_path = f"types.{type_name}"
                type_diags = validate_type_annotation(type_def, t_path, declared_types)
                if type_diags:
                    is_structurally_valid = False
                    diagnostics.extend(type_diags)
                else:
                    declared_types[type_name] = type_def

    # Declarations / Fields Schema Validation (S04#9.3, S04#9.4)
    declarations = data.get("declarations") or data.get("fields")
    if declarations is not None:
        if not isinstance(declarations, dict):
            is_structurally_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.3",
                    message="Declarations section must be a JSON object.",
                    path="declarations",
                )
            )
        else:
            for decl_name, decl_spec in declarations.items():
                d_path = f"declarations.{decl_name}"
                if isinstance(decl_spec, str) or isinstance(decl_spec, dict):
                    decl_diags = validate_type_annotation(decl_spec, d_path, declared_types)
                    if decl_diags:
                        is_structurally_valid = False
                        diagnostics.extend(decl_diags)
                else:
                    is_structurally_valid = False
                    diagnostics.append(
                        Diagnostic(
                            code=DiagnosticCode.VALIDATION_ERROR,
                            clause_id="S04#9.3",
                            message=f"Declaration '{decl_name}' has invalid specification.",
                            path=d_path,
                        )
                    )

    # Properties / Values Conformance Validation (S04#9.4)
    properties = data.get("properties") or data.get("values")
    if properties is not None:
        if not isinstance(properties, dict):
            is_structurally_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.4",
                    message="Properties section must be a JSON object.",
                    path="properties",
                )
            )
        else:
            if isinstance(declarations, dict):
                for prop_name, prop_val in properties.items():
                    p_path = f"properties.{prop_name}"
                    if prop_name in declarations:
                        type_spec = declarations[prop_name]
                        val_diags = validate_value_conformance(prop_val, type_spec, p_path, declared_types)
                        if val_diags:
                            is_structurally_valid = False
                            diagnostics.extend(val_diags)

    # -------------------------------------------------------------
    # Stage 2: S04#10.1–S04#10.7 Pure Deterministic Expressions & Invariants
    # -------------------------------------------------------------
    # Build evaluation context from manifest, declarations, properties
    eval_context: dict[str, Any] = {}
    if isinstance(manifest, dict):
        for k, v in manifest.items():
            eval_context[k] = v
            eval_context[f"manifest.{k}"] = v
    if isinstance(properties, dict):
        for k, v in properties.items():
            eval_context[k] = v
            eval_context[f"properties.{k}"] = v

    # Evaluate Invariants (S04#10.5)
    invariants = data.get("invariants")
    if invariants is not None:
        if not isinstance(invariants, list):
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.5",
                    message="Top-level 'invariants' must be a JSON list.",
                    path="invariants",
                )
            )
        else:
            inv_diags = evaluate_declarative_invariants(invariants, eval_context, "invariants")
            if inv_diags:
                is_closure_valid = False
                diagnostics.extend(inv_diags)

    # Manifest-level invariants if specified
    if isinstance(manifest, dict) and "invariants" in manifest:
        man_invs = manifest["invariants"]
        if not isinstance(man_invs, list):
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.5",
                    message="Manifest 'invariants' must be a JSON list.",
                    path="manifest.invariants",
                )
            )
        else:
            inv_diags = evaluate_declarative_invariants(man_invs, eval_context, "manifest.invariants")
            if inv_diags:
                is_closure_valid = False
                diagnostics.extend(inv_diags)

    # Computed / Expressions section if specified (S04#10.1–S04#10.7)
    expressions = data.get("expressions")
    if expressions is not None:
        if not isinstance(expressions, dict):
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#10.7",
                    message="Top-level 'expressions' must be a JSON object mapping names to expression ASTs.",
                    path="expressions",
                )
            )
        else:
            for expr_name, expr_ast in expressions.items():
                e_path = f"expressions.{expr_name}"
                res_val, expr_diags = evaluate_static_expression(expr_ast, eval_context, e_path)
                if expr_diags:
                    is_closure_valid = False
                    diagnostics.extend(expr_diags)
                else:
                    eval_context[expr_name] = res_val

    sorted_diags = sort_diagnostics(diagnostics)
    # S04#7.2: Violated-clause identification (unique and ordered)
    violated_clauses: list[str] = sorted(list({d.clause_id for d in sorted_diags if d.clause_id}))

    status = (
        ValidationStatus.ACCEPTED
        if is_structurally_valid and is_closure_valid and not sorted_diags
        else ValidationStatus.REJECTED
    )

    return ValidationOutcome(
        status=status,
        is_structurally_valid=is_structurally_valid,
        is_closure_valid=is_closure_valid and is_structurally_valid,
        violated_clauses=violated_clauses,
        diagnostics=sorted_diags,
    )


def validate_artifact(data: dict[str, Any]) -> list[Diagnostic]:
    """Compatibility wrapper returning list of diagnostics."""
    return evaluate_artifact_validity(data).diagnostics
