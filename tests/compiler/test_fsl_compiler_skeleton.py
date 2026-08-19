"""Tests for P04.1 compiler skeleton and S05 boundary compliance."""

import json
from pathlib import Path
from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.cli import main as cli_main
from tools.compiler.fsl.loader import load_source_json
from tools.compiler.fsl.models import DiagnosticCode


def test_s05_input_loader_rejects_duplicate_keys():
    """Verify S05#1.3 duplicate key rejection."""
    raw_json = '{"schema_version": "fsl/1.0", "a": 1, "a": 2}'
    data, diags = load_source_json(raw_json)
    assert data is None
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#8.3"
    assert diags[0].code == DiagnosticCode.SYNTAX_ERROR
    assert "Duplicate key" in diags[0].message


def test_s05_schema_version_validation():
    """Verify S05#1.2 schema version validation."""
    raw_json = json.dumps({
        "schema_version": "fsl/0.9",
        "manifest": {"name": "test.pkg", "version": "1.0.0"}
    })
    result = compile_artifact(raw_json)
    assert not result.success
    assert any(d.clause_id == "S04#8.3" and "fsl/1.0" in d.message for d in result.diagnostics)


def test_s05_successful_compilation_and_bundle_emission():
    """Verify S05#3.3, S05#4.1–S05#4.3 valid compilation and execution bundle."""
    valid_source = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "core.component",
            "version": "1.0.0",
            "dependencies": ["lib.b", "lib.a"]
        }
    }
    res1 = compile_artifact(valid_source, {"timestamp_utc": "2026-08-19T00:00:00Z"})
    res2 = compile_artifact(valid_source, {"timestamp_utc": "2026-08-19T00:00:00Z"})

    assert res1.success
    assert res1.bundle is not None
    assert res1.bundle.bundle_version == "1.0.0"
    assert res1.bundle.resolved_dependencies == ["lib.a", "lib.b"]  # sorted deterministically
    assert res1.bundle.to_dict() == res2.bundle.to_dict()  # S05#4.3 Determinism


def test_s05_cli_exit_codes(tmp_path: Path):
    """Verify S05#3.1–S05#3.2 CLI exit codes."""
    # Exit code 2: Missing file
    assert cli_main(["non_existent_file.json"]) == 2

    # Exit code 1: Invalid artifact
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text('{"schema_version": "invalid"}', encoding="utf-8")
    assert cli_main([str(invalid_file)]) == 1

    # Exit code 0: Valid artifact
    valid_file = tmp_path / "valid.json"
    valid_file.write_text(json.dumps({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "sample.app", "version": "1.0.0"}
    }), encoding="utf-8")
    out_bundle = tmp_path / "out.bundle.json"
    assert cli_main([str(valid_file), "--out", str(out_bundle)]) == 0
    assert out_bundle.exists()
    data = json.loads(out_bundle.read_text(encoding="utf-8"))
    assert data["bundle_version"] == "1.0.0"
