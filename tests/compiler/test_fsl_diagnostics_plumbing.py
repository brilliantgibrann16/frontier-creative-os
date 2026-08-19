"""Comprehensive tests for P04.2 diagnostics plumbing, S04 Stage 1 clauses, and S05 boundary compliance."""

import json
from pathlib import Path
from unittest.mock import patch

from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.cli import main as cli_main
from tools.compiler.fsl.loader import load_source_json
from tools.compiler.fsl.models import DiagnosticCode


def test_s04_s05_malformed_json_syntax_error():
    """Verify S04#8.3 / S05#1.1 syntax error on malformed JSON."""
    raw_text = '{"schema_version": "fsl/1.0", "manifest": {'
    data, diags = load_source_json(raw_text)
    assert data is None
    assert len(diags) == 1
    assert diags[0].code == DiagnosticCode.SYNTAX_ERROR
    assert diags[0].clause_id == "S04#8.3"


def test_s04_s05_duplicate_key_rejection():
    """Verify S04#8.3 / S05#1.3 rejection of duplicate object keys."""
    raw_text = '{"schema_version": "fsl/1.0", "manifest": {}, "manifest": {}}'
    data, diags = load_source_json(raw_text)
    assert data is None
    assert len(diags) == 1
    assert diags[0].code == DiagnosticCode.SYNTAX_ERROR
    assert diags[0].clause_id == "S04#8.3"
    assert "Duplicate key" in diags[0].message


def test_s04_s05_top_level_type_error():
    """Verify S04#8.3 top-level must be JSON object."""
    raw_text = '["schema_version", "fsl/1.0"]'
    data, diags = load_source_json(raw_text)
    assert data is None
    assert len(diags) == 1
    assert diags[0].code == DiagnosticCode.SYNTAX_ERROR
    assert diags[0].clause_id == "S04#8.3"


def test_s04_missing_or_invalid_schema_version():
    """Verify S04#8.3 / S05#1.2 schema version validation."""
    # Missing
    res = compile_artifact({"manifest": {"name": "app", "version": "1.0.0"}})
    assert not res.success
    assert any(d.clause_id == "S04#8.3" and "Missing" in d.message for d in res.diagnostics)

    # Invalid version string
    res2 = compile_artifact({"schema_version": "2.0", "manifest": {"name": "app", "version": "1.0.0"}})
    assert not res2.success
    assert any(d.clause_id == "S04#8.3" and "Expected schema_version" in d.message for d in res2.diagnostics)


def test_s04_missing_or_invalid_manifest():
    """Verify S04#5.1 / S04#6.1 manifest object requirements."""
    # Missing manifest
    res = compile_artifact({"schema_version": "fsl/1.0"})
    assert not res.success
    assert any(d.clause_id == "S04#5.1" and "Missing" in d.message for d in res.diagnostics)

    # Non-object manifest
    res2 = compile_artifact({"schema_version": "fsl/1.0", "manifest": "not-an-object"})
    assert not res2.success
    assert any(d.clause_id == "S04#5.1" and "must be a JSON object" in d.message for d in res2.diagnostics)


def test_s04_manifest_identity_and_version_clauses():
    """Verify S04#6.1 and S04#6.2 clause citations."""
    # Missing name (S04#6.1)
    res1 = compile_artifact({"schema_version": "fsl/1.0", "manifest": {"version": "1.0.0"}})
    assert not res1.success
    assert any(d.clause_id == "S04#6.1" and d.path == "manifest.name" for d in res1.diagnostics)

    # Missing version (S04#6.2)
    res2 = compile_artifact({"schema_version": "fsl/1.0", "manifest": {"name": "app"}})
    assert not res2.success
    assert any(d.clause_id == "S04#6.2" and d.path == "manifest.version" for d in res2.diagnostics)


def test_s04_manifest_dependencies_self_containment():
    """Verify S04#5.2 self-containment dependency list checks."""
    # Non-list dependencies
    res1 = compile_artifact({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "app", "version": "1.0.0", "dependencies": "dep1"}
    })
    assert not res1.success
    assert any(d.clause_id == "S04#5.2" and d.path == "manifest.dependencies" for d in res1.diagnostics)

    # Invalid dependency entry in list
    res2 = compile_artifact({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "app", "version": "1.0.0", "dependencies": ["valid.dep", ""]}
    })
    assert not res2.success
    assert any(d.clause_id == "S04#5.2" and d.path == "manifest.dependencies[1]" for d in res2.diagnostics)


def test_s05_diagnostics_deterministic_ordering():
    """Verify S05#2.3 deterministic diagnostic ordering across multiple violations."""
    invalid_data = {
        "schema_version": "invalid",
        "manifest": {
            "name": "",
            "version": "",
            "dependencies": [""]
        }
    }
    res = compile_artifact(invalid_data)
    assert not res.success
    paths = [d.path for d in res.diagnostics]
    assert paths == sorted(paths)


def test_s05_cli_all_exit_codes(tmp_path: Path):
    """Verify S05#3.2 CLI exit codes 0, 1, 2, 3."""
    # Code 0: Success
    valid_file = tmp_path / "valid.json"
    valid_file.write_text(json.dumps({
        "schema_version": "fsl/1.0",
        "manifest": {"name": "app", "version": "1.0.0"}
    }), encoding="utf-8")
    assert cli_main([str(valid_file), "--format", "text"]) == 0

    # Code 1: Validation failure
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text('{"schema_version": "wrong"}', encoding="utf-8")
    assert cli_main([str(invalid_file), "--format", "text"]) == 1

    # Code 2: Usage / missing file
    assert cli_main(["missing_file_for_cli.json"]) == 2

    # Code 3: Internal fault
    with patch("tools.compiler.fsl.cli.compile_artifact", side_effect=RuntimeError("Simulated fault")):
        assert cli_main([str(valid_file)]) == 3


def test_s05_byte_for_byte_reproducibility():
    """Verify S05#4.3 byte-level reproducibility guarantee across repeated invocations."""
    source = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "reproducible.artifact",
            "version": "1.0.0",
            "dependencies": ["dep.b", "dep.a", "dep.c"]
        }
    }
    opts = {"compiler_version": "0.1.0", "timestamp_utc": "1970-01-01T00:00:00Z"}
    res1 = compile_artifact(source, opts)
    res2 = compile_artifact(source, opts)

    assert res1.success and res2.success
    json1 = json.dumps(res1.bundle.to_dict(), indent=2)
    json2 = json.dumps(res2.bundle.to_dict(), indent=2)
    assert json1 == json2
