"""Unit tests for tools/checks/check_conformance.py (S13#4.4, P12.4)."""

import hashlib
import json
from pathlib import Path

from tools.checks.check_conformance import check_conformance_registry, main as check_conformance_main


def test_valid_conformance_registry_passes():
    """Verify check_conformance_registry passes cleanly on the repository's standing claims."""
    findings = check_conformance_registry()
    assert findings == [], f"Unexpected findings on clean repo: {findings}"


def test_missing_claims_dir_reported(tmp_path: Path):
    """Verify error finding when docs/conformance/claims directory does not exist."""
    findings = check_conformance_registry(tmp_path)
    assert len(findings) == 1
    assert "not found" in findings[0]


def test_empty_claims_dir_reported(tmp_path: Path):
    """Verify error finding when docs/conformance/claims contains no claim files."""
    claims_dir = tmp_path / "docs" / "conformance" / "claims"
    claims_dir.mkdir(parents=True)
    findings = check_conformance_registry(tmp_path)
    assert len(findings) == 1
    assert "No claim .json files found" in findings[0]


def test_missing_report_file_reported(tmp_path: Path):
    """Verify finding when claim exists without a corresponding .report.json file."""
    claims_dir = tmp_path / "docs" / "conformance" / "claims"
    claims_dir.mkdir(parents=True)

    claim_data = {
        "claim_id": "CLAIM-TEST-1.0",
        "candidate_name": "test",
        "candidate_commit_sha": "abc",
        "candidate_release_version": "1.0",
        "target_specification_version": "fsl/1.0",
        "harness_hash_sha256": "h" * 64,
        "verdict": "CONFORMING",
        "evidence_report_digest_sha256": "d" * 64,
        "assertion_date_utc": "2026-08-19T00:00:00Z",
    }
    (claims_dir / "CLAIM-TEST-1.0.json").write_text(json.dumps(claim_data), encoding="utf-8")

    findings = check_conformance_registry(tmp_path)
    assert any("Missing evaluation report file" in f for f in findings)


def test_tampered_report_digest_mismatch_reported(tmp_path: Path):
    """Verify finding when evaluation report content does not match declared SHA-256 digest."""
    claims_dir = tmp_path / "docs" / "conformance" / "claims"
    claims_dir.mkdir(parents=True)

    report_text = '{"verdict": "CONFORMING", "clause_totality_achieved": true}\n'
    wrong_digest = "0" * 64

    claim_data = {
        "claim_id": "CLAIM-TEST-1.0",
        "candidate_name": "test",
        "candidate_commit_sha": "abc",
        "candidate_release_version": "1.0",
        "target_specification_version": "fsl/1.0",
        "harness_hash_sha256": "h" * 64,
        "verdict": "CONFORMING",
        "evidence_report_digest_sha256": wrong_digest,
        "assertion_date_utc": "2026-08-19T00:00:00Z",
    }

    (claims_dir / "CLAIM-TEST-1.0.json").write_text(json.dumps(claim_data), encoding="utf-8")
    (claims_dir / "CLAIM-TEST-1.0.report.json").write_text(report_text, encoding="utf-8")

    findings = check_conformance_registry(tmp_path)
    assert any("Evidence digest mismatch" in f for f in findings)


def test_missing_required_fields_reported(tmp_path: Path):
    """Verify finding when claim is missing required S13#4.2 fields."""
    claims_dir = tmp_path / "docs" / "conformance" / "claims"
    claims_dir.mkdir(parents=True)

    claim_data = {
        "claim_id": "CLAIM-INCOMPLETE",
        "candidate_name": "test",
    }
    (claims_dir / "CLAIM-INCOMPLETE.json").write_text(json.dumps(claim_data), encoding="utf-8")

    findings = check_conformance_registry(tmp_path)
    assert any("Missing required S13#4.2 fields" in f for f in findings)


def test_cli_main_exit_codes():
    """Verify check_conformance main() CLI returns 0 on clean repository."""
    ret = check_conformance_main([])
    assert ret == 0
