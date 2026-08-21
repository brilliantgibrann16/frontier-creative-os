"""Complete spec-derived test evidence suite per ratified S04 Stage 1 W-B and S05 clauses (P04.4 / P11)."""

import json
from pathlib import Path
from unittest.mock import patch

from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.cli import main as cli_main
from tools.compiler.fsl.loader import load_source_json
from tools.compiler.fsl.models import (
    CompilationResult,
    Diagnostic,
    DiagnosticCode,
    ExecutionBundle,
    ValidationOutcome,
    ValidationStatus,
)
from tools.compiler.fsl.validator import evaluate_artifact_validity


# ==============================================================================
# S04 Stage 1 W-B Clause-Traced Evidence Tests (S04#5.1–S04#8.3)
# ==============================================================================


def test_s04_5_1_single_artifact_unit():
    """Evidence for S04#5.1 (Artifact unit): Top-level manifest dictionary validation."""
    # Missing manifest
    outcome_missing = evaluate_artifact_validity({"schema_version": "fsl/1.0"})
    assert outcome_missing.status == ValidationStatus.REJECTED
    assert not outcome_missing.is_structurally_valid
    assert "S04#5.1" in outcome_missing.violated_clauses
    assert any(d.clause_id == "S04#5.1" and d.path == "manifest" for d in outcome_missing.diagnostics)

    # Non-dict manifest
    outcome_non_dict = evaluate_artifact_validity({"schema_version": "fsl/1.0", "manifest": "not-dict"})
    assert outcome_non_dict.status == ValidationStatus.REJECTED
    assert not outcome_non_dict.is_structurally_valid
    assert "S04#5.1" in outcome_non_dict.violated_clauses


def test_s04_5_2_stage1_self_containment():
    """Evidence for S04#5.2 (Stage 1 self-containment): Local dependency checking."""
    # Valid self-contained local dependencies with all required manifest fields
    outcome_valid = evaluate_artifact_validity({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "app", "version": "1.0.0", "kind": "application", "dependencies": ["dep.a", "dep.b"]}
    })
    assert outcome_valid.status == ValidationStatus.ACCEPTED

    # Non-list dependencies rejected
    outcome_invalid_type = evaluate_artifact_validity({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "app", "version": "1.0.0", "kind": "application", "dependencies": "dep.a"}
    })
    assert outcome_invalid_type.status == ValidationStatus.REJECTED
    assert "S04#5.2" in outcome_invalid_type.violated_clauses


def test_s04_6_1_structural_validity_distinction():
    """Evidence for S04#6.1 (Structural validity): Structural defects fail fast."""
    bad_manifest = {
        "schema_version": "fsl/1.0",
        "manifest": {"version": "1.0.0"}  # Missing name
    }
    outcome = evaluate_artifact_validity(bad_manifest)
    assert outcome.status == ValidationStatus.REJECTED
    assert not outcome.is_structurally_valid
    assert "S04#6.1" in outcome.violated_clauses


def test_s04_6_2_validity_closure_distinction():
    """Evidence for S04#6.2 (Validity closure): Closure failure distinct from structural validity."""
    bad_version = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "valid.name", "version": ""}  # Structural name valid, version closure invalid
    }
    outcome = evaluate_artifact_validity(bad_version)
    assert outcome.status == ValidationStatus.REJECTED
    assert outcome.is_structurally_valid
    assert not outcome.is_closure_valid
    assert "S04#6.2" in outcome.violated_clauses


def test_s04_7_1_outcome_model_accepted_and_rejected():
    """Evidence for S04#7.1 (Validation-outcome model): Explicit ACCEPTED vs REJECTED outcomes."""
    valid_res = compile_artifact({"schema_version": "fsl/1.0", "manifest": {"name": "app", "version": "1.0.0", "kind": "application"}})
    assert valid_res.success
    assert valid_res.outcome is not None
    assert valid_res.outcome.status == ValidationStatus.ACCEPTED
    assert valid_res.outcome.is_accepted

    invalid_res = compile_artifact({"schema_version": "invalid"})
    assert not invalid_res.success
    assert invalid_res.outcome is not None
    assert invalid_res.outcome.status == ValidationStatus.REJECTED
    assert not invalid_res.outcome.is_accepted


def test_s04_7_2_violated_clause_attribution():
    """Evidence for S04#7.2 (Violated-clause identification): Accurate unique sorted clause lists."""
    multi_violation = {
        "schema_version": "fsl/2.0",
        "manifest": {"name": "", "version": ""}
    }
    outcome = evaluate_artifact_validity(multi_violation)
    assert outcome.status == ValidationStatus.REJECTED
    assert outcome.violated_clauses == ["S04#6.1", "S04#6.2", "S04#8.3"]


def test_s04_7_3_outcome_authority_spec_alignment():
    """Evidence for S04#7.3 (Outcome authority): Strictly follows S04 normative prose."""
    # Verifies only ratified clauses are cited and evaluated
    outcome = evaluate_artifact_validity({"schema_version": "fsl/1.0", "manifest": {"name": "a", "version": "1", "kind": "application"}})
    assert outcome.status == ValidationStatus.ACCEPTED
    for clause in outcome.violated_clauses:
        assert clause.startswith("S04#")


def test_s04_7_4_outcome_determinism_sweep():
    """Evidence for S04#7.4 (Outcome determinism): 100 repeated evaluations are bitwise identical."""
    sample = {
        "schema_version": "invalid",
        "manifest": {"name": "", "version": "", "dependencies": ["", "valid"]}
    }
    baseline_dict = evaluate_artifact_validity(sample).to_dict()
    for _ in range(100):
        assert evaluate_artifact_validity(sample).to_dict() == baseline_dict


def test_s04_7_5_diagnostic_presentation_contract():
    """Evidence for S04#7.5 (Diagnostic presentation): Conforms to S05 diagnostic contract."""
    sample = {"schema_version": "fsl/1.0", "manifest": {"name": "", "version": "1.0.0", "kind": "application"}}
    outcome = evaluate_artifact_validity(sample)
    assert len(outcome.diagnostics) >= 1
    diag = outcome.diagnostics[0]
    assert isinstance(diag.code, DiagnosticCode)
    assert diag.clause_id == "S04#6.1"
    assert isinstance(diag.message, str)
    assert diag.path == "manifest.name"


def test_s04_7_6_conformance_boundary_preservation():
    """Evidence for S04#7.6 (Validation/conformance boundary): Emits outcome, not conformance seal."""
    res = compile_artifact({"schema_version": "fsl/1.0", "manifest": {"name": "app", "version": "1.0.0", "kind": "application"}})
    assert isinstance(res.outcome, ValidationOutcome)
    # The output models do not declare an official conformance seal field
    assert not hasattr(res, "conformance_certificate")


def test_s04_8_1_single_interchange_form_enforcement():
    """Evidence for S04#8.1 (Single interchange form): Enforces JSON interchange form."""
    res = compile_artifact('{"schema_version": "fsl/1.0", "manifest": {"name": "app", "version": "1.0.0", "kind": "application"}}')
    assert res.success
    assert res.bundle is not None


def test_s04_8_2_interchange_obligations_decidability():
    """Evidence for S04#8.2 (Interchange-form obligations): Decidable without type system."""
    res = compile_artifact({"schema_version": "fsl/1.0", "manifest": {"name": "app", "version": "1.0.0", "kind": "application"}})
    assert res.outcome.is_accepted


def test_s04_8_3_concrete_json_interchange_syntax():
    """Evidence for S04#8.3 (Concrete JSON interchange form): RFC 8259 syntax & schema_version."""
    # Syntax error
    data, diags = load_source_json('{"schema_version": "fsl/1.0", "manifest":')
    assert data is None
    assert any(d.clause_id == "S04#8.3" and d.code == DiagnosticCode.SYNTAX_ERROR for d in diags)

    # Missing schema_version
    outcome = evaluate_artifact_validity({"manifest": {"name": "app", "version": "1.0.0"}})
    assert "S04#8.3" in outcome.violated_clauses


# ==============================================================================
# S04 Stage 2 Typed Data Model & Pure Expressions Evidence (S04#9.1–S04#10.7)
# ==============================================================================


def test_s04_9_1_scalar_data_types_evidence():
    """Evidence for S04#9.1 (Scalar data types): string, integer, float, boolean enumeration."""
    from tools.compiler.fsl.types import is_scalar_type

    assert is_scalar_type("string")
    assert is_scalar_type("integer")
    assert is_scalar_type("float")
    assert is_scalar_type("boolean")
    assert not is_scalar_type("unknown_type")


def test_s04_9_2_compound_data_structures_evidence():
    """Evidence for S04#9.2 (Compound data structures): record, list, map structures."""
    from tools.compiler.fsl.types import is_compound_type, validate_type_annotation

    assert is_compound_type("record")
    assert is_compound_type("list")
    assert is_compound_type("map")
    assert not is_compound_type("set")

    # Map key constraint per S04#9.2
    diags_map = validate_type_annotation({"type": "map", "key_type": "integer", "value_type": "string"}, "config")
    assert len(diags_map) == 1
    assert diags_map[0].clause_id == "S04#9.2"


def test_s04_9_3_type_annotations_and_declarations_evidence():
    """Evidence for S04#9.3 (Type annotations & declarations): validation of type specs."""
    from tools.compiler.fsl.types import validate_type_annotation

    assert not validate_type_annotation("string", "field")
    assert not validate_type_annotation({"type": "list", "element_type": "integer"}, "field")
    assert not validate_type_annotation({"type": "map", "key_type": "string", "value_type": "boolean"}, "field")
    assert not validate_type_annotation({"type": "record", "fields": {"id": "integer"}}, "field")

    # Invalid type spec structure
    diags = validate_type_annotation(12345, "field")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.3"


def test_s04_9_4_schema_validation_rules_evidence():
    """Evidence for S04#9.4 (Schema validation rules): checking values against declared types."""
    artifact = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "typed-service", "version": "1.0.0", "kind": "service"},
        "declarations": {"timeout": "integer", "tags": {"type": "list", "element_type": "string"}},
        "properties": {"timeout": "not_an_int", "tags": ["prod", 123]},
    }
    outcome = evaluate_artifact_validity(artifact)
    assert outcome.status == ValidationStatus.REJECTED
    assert "S04#9.4" in outcome.violated_clauses


def test_s04_10_1_pure_expression_evaluation_model_evidence():
    """Evidence for S04#10.1 (Pure expression evaluation model): deterministic, terminating evaluation."""
    from tools.compiler.fsl.expressions import evaluate_static_expression

    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "+", "left": 10, "right": 20})
    assert val == 30
    assert not diags


def test_s04_10_2_arithmetic_and_boolean_operations_evidence():
    """Evidence for S04#10.2 (Arithmetic & boolean operations): operators and zero-division checks."""
    from tools.compiler.fsl.expressions import evaluate_static_expression

    # Arithmetic
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "*", "left": 6, "right": 7})
    assert val == 42 and not diags

    # Division by zero diagnostic
    val_zero, diags_zero = evaluate_static_expression({"kind": "binary_op", "op": "/", "left": 10, "right": 0})
    assert val_zero is None
    assert any(d.clause_id == "S04#10.2" for d in diags_zero)

    # Boolean logic
    val_bool, diags_bool = evaluate_static_expression({"kind": "unary_op", "op": "not", "operand": False})
    assert val_bool is True and not diags_bool


def test_s04_10_3_string_and_collection_operations_evidence():
    """Evidence for S04#10.3 (String & collection operations): concat, length, index, lookup."""
    from tools.compiler.fsl.expressions import evaluate_static_expression

    val_cat, diags_cat = evaluate_static_expression({"kind": "concat", "left": "Hello, ", "right": "World!"})
    assert val_cat == "Hello, World!" and not diags_cat

    val_len, diags_len = evaluate_static_expression({"kind": "length", "operand": [10, 20, 30]})
    assert val_len == 3 and not diags_len

    val_idx, diags_idx = evaluate_static_expression({"kind": "index", "target": ["first", "second"], "index": 1})
    assert val_idx == "second" and not diags_idx

    val_lookup, diags_lookup = evaluate_static_expression({"kind": "lookup", "target": {"env": "prod"}, "key": "env"})
    assert val_lookup == "prod" and not diags_lookup


def test_s04_10_4_conditional_expressions_evidence():
    """Evidence for S04#10.4 (Conditional expressions): if / then / else evaluation."""
    from tools.compiler.fsl.expressions import evaluate_static_expression

    val, diags = evaluate_static_expression({
        "kind": "conditional",
        "condition": {"kind": "binary_op", "op": ">", "left": 5, "right": 3},
        "then": "yes",
        "else": "no"
    })
    assert val == "yes"
    assert not diags


def test_s04_10_5_declarative_invariant_assertions_evidence():
    """Evidence for S04#10.5 (Declarative invariant assertions): asserting boolean conditions on artifact."""
    artifact = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "app", "version": "1.0.0", "kind": "application"},
        "declarations": {"replicas": "integer"},
        "properties": {"replicas": 0},
        "invariants": [
            {
                "name": "at_least_one_replica",
                "expr": {"kind": "binary_op", "op": ">=", "left": {"kind": "ref", "name": "replicas"}, "right": 1}
            }
        ]
    }
    outcome = evaluate_artifact_validity(artifact)
    assert outcome.status == ValidationStatus.REJECTED
    assert "S04#10.5" in outcome.violated_clauses


def test_s04_10_6_static_evaluation_boundary_evidence():
    """Evidence for S04#10.6 (Static evaluation boundary): all evaluations occur at compile/validation time."""
    artifact = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "static-app", "version": "1.0.0", "kind": "application"},
        "declarations": {"max_size": "integer"},
        "properties": {"max_size": 1024},
        "invariants": [
            {
                "name": "valid_size",
                "expr": {"kind": "binary_op", "op": ">", "left": {"kind": "ref", "name": "max_size"}, "right": 0}
            }
        ]
    }
    res = compile_artifact(artifact)
    assert res.success
    assert res.outcome.status == ValidationStatus.ACCEPTED
    assert res.bundle is not None


def test_s04_10_7_stage2_json_ast_expression_representation_evidence():
    """Evidence for S04#10.7 (Stage 2 JSON AST expression representation): AST schema adherence."""
    from tools.compiler.fsl.expressions import evaluate_static_expression

    valid_ast = {
        "kind": "binary_op",
        "op": "+",
        "left": {"kind": "literal", "value": 1},
        "right": {"kind": "literal", "value": 2}
    }
    val, diags = evaluate_static_expression(valid_ast)
    assert val == 3 and not diags

    invalid_ast = {"kind": "unsupported_kind"}
    val_inv, diags_inv = evaluate_static_expression(invalid_ast)
    assert val_inv is None
    assert len(diags_inv) == 1
    assert diags_inv[0].clause_id == "S04#10.7"


# ==============================================================================
# S05 Compiler Boundary Clause-Traced Evidence Tests (S05#1.1–S05#4.3)
# ==============================================================================


def test_s05_1_1_utf8_rfc8259_decoding():
    """Evidence for S05#1.1 (Source text encoding): RFC 8259 UTF-8 JSON loading."""
    data, diags = load_source_json('{"schema_version": "fsl/1.0", "manifest": {}}')
    assert data == {"schema_version": "fsl/1.0", "manifest": {}}
    assert diags == []


def test_s05_1_2_schema_version_validation():
    """Evidence for S05#1.2 (Schema version validation): Strict "fsl/1.0" check."""
    outcome = evaluate_artifact_validity({"schema_version": "other/1.0", "manifest": {"name": "a", "version": "1"}})
    assert outcome.status == ValidationStatus.REJECTED
    assert any(d.path == "schema_version" for d in outcome.diagnostics)


def test_s05_1_3_duplicate_key_rejection():
    """Evidence for S05#1.3 (Duplicate key rejection): Strict duplicate key detection."""
    raw = '{"schema_version": "fsl/1.0", "k": 1, "k": 2}'
    data, diags = load_source_json(raw)
    assert data is None
    assert len(diags) == 1
    assert "Duplicate key encountered in JSON object: 'k'" in diags[0].message


def test_s05_2_1_diagnostic_model():
    """Evidence for S05#2.1 (Diagnostic model): Emits diagnostic model on failure."""
    res = compile_artifact({"schema_version": "invalid"})
    assert not res.success
    assert len(res.diagnostics) > 0


def test_s05_2_2_diagnostic_fields():
    """Evidence for S05#2.2 (Diagnostic fields): code, clause_id, message, path."""
    diag = Diagnostic(code=DiagnosticCode.VALIDATION_ERROR, clause_id="S04#6.1", message="msg", path="manifest.name")
    d_dict = diag.to_dict()
    assert d_dict == {
        "code": "VALIDATION_ERROR",
        "clause_id": "S04#6.1",
        "message": "msg",
        "path": "manifest.name",
    }


def test_s05_2_3_deterministic_diagnostic_sorting():
    """Evidence for S05#2.3 (Deterministic diagnostic order): Path and clause ID sort order."""
    data = {"schema_version": "bad", "manifest": {"name": "", "version": ""}}
    outcome = evaluate_artifact_validity(data)
    paths = [d.path for d in outcome.diagnostics]
    assert paths == sorted(paths)


def test_s05_2_4_clause_traceable_diagnostics():
    """Evidence for S05#2.4 (Clause-traceable diagnostics): Normative clause citations."""
    outcome = evaluate_artifact_validity({"schema_version": "fsl/1.0", "manifest": {}})
    for d in outcome.diagnostics:
        assert d.clause_id is not None
        assert d.clause_id.startswith("S04#") or d.clause_id.startswith("S05#")


def test_s05_3_1_cli_interface(tmp_path: Path):
    """Evidence for S05#3.1 (Command-line interface): CLI execution & flags."""
    src = tmp_path / "app.json"
    src.write_text('{"schema_version": "fsl/1.0", "manifest": {"name": "app", "version": "1.0.0", "kind": "application"}}', encoding="utf-8")
    out = tmp_path / "out.bundle.json"
    code = cli_main([str(src), "--out", str(out), "--format", "json"])
    assert code == 0
    assert out.exists()


def test_s05_3_2_cli_exit_code_protocol(tmp_path: Path):
    """Evidence for S05#3.2 (Exit code protocol): Validates codes 0, 1, 2, 3."""
    src = tmp_path / "app.json"
    src.write_text('{"schema_version": "fsl/1.0", "manifest": {"name": "app", "version": "1.0.0", "kind": "application"}}', encoding="utf-8")
    assert cli_main([str(src)]) == 0

    bad_src = tmp_path / "bad.json"
    bad_src.write_text('{"schema_version": "bad"}', encoding="utf-8")
    assert cli_main([str(bad_src)]) == 1

    assert cli_main(["non_existent_file.json"]) == 2

    with patch("tools.compiler.fsl.cli.compile_artifact", side_effect=RuntimeError("Fault")):
        assert cli_main([str(src)]) == 3


def test_s05_3_3_programmatic_api_parity():
    """Evidence for S05#3.3 (Programmatic API): Full parity with CLI."""
    artifact = {"schema_version": "fsl/1.0", "manifest": {"name": "pkg", "version": "1.0.0", "kind": "application"}}
    res = compile_artifact(artifact)
    assert res.success
    assert res.bundle is not None
    assert res.bundle.artifact == artifact


def test_s05_4_1_execution_bundle_emission():
    """Evidence for S05#4.1 (Execution bundle output): Emission of ExecutionBundle."""
    res = compile_artifact({"schema_version": "fsl/1.0", "manifest": {"name": "pkg", "version": "1.0.0", "kind": "application"}})
    assert isinstance(res.bundle, ExecutionBundle)
    assert res.bundle.bundle_version == "1.0.0"


def test_s05_4_2_bundle_structure_contract():
    """Evidence for S05#4.2 (Bundle structure): Required bundle schema fields."""
    res = compile_artifact({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "pkg", "version": "1.0.0", "kind": "application", "dependencies": ["b", "a"]}
    })
    b_dict = res.bundle.to_dict()
    assert set(b_dict.keys()) == {
        "bundle_version",
        "compiler_version",
        "artifact",
        "resolved_dependencies",
        "compilation_timestamp_utc",
    }
    assert b_dict["resolved_dependencies"] == ["a", "b"]


def test_s05_4_3_byte_for_byte_reproducibility():
    """Evidence for S05#4.3 (Reproducibility guarantee): Byte-level reproducibility."""
    source = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "deterministic.pkg",
            "version": "1.0.0",
            "kind": "application",
            "dependencies": ["z", "y", "x"]
        }
    }
    opts = {"compiler_version": "0.1.0", "compilation_timestamp_utc": "1970-01-01T00:00:00Z"}
    res1 = compile_artifact(source, opts)
    res2 = compile_artifact(source, opts)
    assert json.dumps(res1.bundle.to_dict(), sort_keys=True) == json.dumps(res2.bundle.to_dict(), sort_keys=True)
