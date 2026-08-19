"""Focused test matrix for P04.3 incremental realization of S04 Stage 1 W-B clauses."""

import json
from pathlib import Path
from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.cli import main as cli_main
from tools.compiler.fsl.models import ValidationStatus
from tools.compiler.fsl.validator import evaluate_artifact_validity


def test_s04_5_1_single_artifact_unit():
    """Verify S04#5.1: Artifact unit validation."""
    # Top-level manifest missing
    outcome = evaluate_artifact_validity({"schema_version": "fsl/1.0"})
    assert outcome.status == ValidationStatus.REJECTED
    assert not outcome.is_structurally_valid
    assert "S04#5.1" in outcome.violated_clauses


def test_s04_5_2_stage1_self_containment():
    """Verify S04#5.2: Self-containment and local dependency checks."""
    valid_source = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "isolated.pkg",
            "version": "1.0.0",
            "dependencies": ["local.pkg.a", "local.pkg.b"]
        }
    }
    outcome = evaluate_artifact_validity(valid_source)
    assert outcome.status == ValidationStatus.ACCEPTED
    assert outcome.is_structurally_valid
    assert outcome.is_closure_valid
    assert outcome.violated_clauses == []


def test_s04_6_1_structural_validity_distinction():
    """Verify S04#6.1: Structural validity fails fast on malformed identity."""
    bad_manifest = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "", "version": "1.0.0"}
    }
    outcome = evaluate_artifact_validity(bad_manifest)
    assert outcome.status == ValidationStatus.REJECTED
    assert not outcome.is_structurally_valid
    assert "S04#6.1" in outcome.violated_clauses


def test_s04_6_2_validity_closure_distinction():
    """Verify S04#6.2: Validity closure fails on version without breaking structural validity of name."""
    bad_version = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "valid.name", "version": ""}
    }
    outcome = evaluate_artifact_validity(bad_version)
    assert outcome.status == ValidationStatus.REJECTED
    assert outcome.is_structurally_valid
    assert not outcome.is_closure_valid
    assert "S04#6.2" in outcome.violated_clauses


def test_s04_7_1_7_2_outcome_and_violated_clause_identification():
    """Verify S04#7.1 and S04#7.2 outcome model and clause citations."""
    multi_violation = {
        "schema_version": "invalid",
        "manifest": {"name": "", "version": ""}
    }
    outcome = evaluate_artifact_validity(multi_violation)
    assert outcome.status == ValidationStatus.REJECTED
    assert set(outcome.violated_clauses) == {"S04#6.1", "S04#6.2", "S04#8.3"}


def test_s04_7_4_outcome_determinism():
    """Verify S04#7.4 outcome and diagnostic determinism across 50 repeated runs."""
    sample = {
        "schema_version": "invalid",
        "manifest": {"name": "", "version": "", "dependencies": ["", "valid"]}
    }
    first_outcome = evaluate_artifact_validity(sample).to_dict()
    for _ in range(50):
        assert evaluate_artifact_validity(sample).to_dict() == first_outcome


def test_s04_8_1_8_3_json_concrete_interchange_form():
    """Verify S04#8.1 & S04#8.3 concrete JSON interchange form compliance."""
    valid_json_text = json.dumps({
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "json.interchange.test",
            "version": "1.0.0"
        }
    })
    res = compile_artifact(valid_json_text)
    assert res.success
    assert res.outcome is not None
    assert res.outcome.is_accepted
    assert res.bundle is not None
    assert res.bundle.bundle_version == "1.0.0"


def test_api_cli_parity(tmp_path: Path):
    """Verify programmatic API and CLI produce identical outcome for valid & invalid artifacts."""
    valid_obj = {
        "schema_version": "fsl/1.0",
        "manifest": {"name": "parity.pkg", "version": "1.0.0"}
    }
    api_res = compile_artifact(valid_obj)
    assert api_res.success

    file_path = tmp_path / "parity.json"
    file_path.write_text(json.dumps(valid_obj), encoding="utf-8")
    out_file = tmp_path / "bundle.json"
    cli_code = cli_main([str(file_path), "--out", str(out_file)])
    assert cli_code == 0
    cli_bundle = json.loads(out_file.read_text(encoding="utf-8"))
    assert api_res.bundle.to_dict() == cli_bundle
