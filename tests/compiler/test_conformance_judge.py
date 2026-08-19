"""Unit and integration tests for S13 Official Conformance Judge adhering to S13#1.1–S13#4.4 (P12.4)."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
from unittest.mock import MagicMock

from tools.compiler.fsl.api import compile_artifact
from tools.conformance.judge import ConformanceJudge, compute_harness_hash, main as judge_cli_main
from tools.conformance.models import EvaluationVerdict


def test_compute_harness_hash_is_deterministic():
    """Verify compute_harness_hash produces a valid, reproducible 64-char hex SHA-256 digest."""
    h1 = compute_harness_hash()
    h2 = compute_harness_hash()
    assert isinstance(h1, str)
    assert len(h1) == 64
    assert h1 == h2


def test_judge_executes_valid_judgment_and_returns_conforming_claim():
    """Verify ConformanceJudge produces valid ConformanceClaim under S13#4.2."""
    judge = ConformanceJudge(
        target_spec_version="fsl/1.0",
        fixtures_dir=Path("tests/fixtures/conformance"),
    )

    claim, report = judge.execute_judgment(
        candidate_name="tools.compiler.fsl",
        candidate_commit_sha="abcdef1234567890abcdef1234567890abcdef12",
        candidate_release_version="0.1.0",
        assertion_date_utc="2026-08-19T00:00:00Z",
    )

    assert claim.verdict == EvaluationVerdict.CONFORMING
    assert claim.target_specification_version == "fsl/1.0"
    assert claim.candidate_name == "tools.compiler.fsl"
    assert claim.candidate_release_version == "0.1.0"
    assert claim.candidate_commit_sha == "abcdef1234567890abcdef1234567890abcdef12"
    assert claim.assertion_date_utc == "2026-08-19T00:00:00Z"
    assert len(claim.harness_hash_sha256) == 64
    assert len(claim.evidence_report_digest_sha256) == 64

    # Verify evidence report digest matches actual report JSON hash
    report_json = judge.harness.generate_report_json(report) + "\n"
    expected_digest = hashlib.sha256(report_json.encode("utf-8")).hexdigest()
    assert claim.evidence_report_digest_sha256 == expected_digest


def test_judge_claim_publication_and_immutability_enforcement(tmp_path: Path):
    """Verify publishing claim to registry directory and enforcing immutability (S13#4.3, S13#4.4)."""
    judge = ConformanceJudge(
        target_spec_version="fsl/1.0",
        fixtures_dir=Path("tests/fixtures/conformance"),
    )

    claim, report = judge.execute_judgment(
        candidate_name="test.candidate",
        candidate_commit_sha="1111222233334444555566667777888899990000",
        candidate_release_version="1.0.0",
        assertion_date_utc="2026-08-19T12:00:00Z",
    )

    reg_dir = tmp_path / "claims"
    claim_path, report_path = judge.publish_claim(claim, report, registry_dir=reg_dir)

    assert claim_path.exists()
    assert report_path.exists()

    # Re-publishing identical claim succeeds
    judge.publish_claim(claim, report, registry_dir=reg_dir)

    # Re-publishing with modified claim content raises ValueError (immutability violation)
    claim_file = reg_dir / f"{claim.claim_id}.json"
    claim_file.write_text('{"tampered": true}\n', encoding="utf-8")

    try:
        judge.publish_claim(claim, report, registry_dir=reg_dir)
        assert False, "Should raise ValueError on tampered claim file"
    except ValueError as e:
        assert "Immutability violation" in str(e)


def test_judge_detects_non_conforming_verdict_when_candidate_fails():
    """Verify judge produces NON_CONFORMING verdict when candidate fails fixtures."""
    failing_api = MagicMock(return_value=MagicMock(success=False, diagnostics=[]))

    judge = ConformanceJudge(
        target_spec_version="fsl/1.0",
        fixtures_dir=Path("tests/fixtures/conformance"),
        candidate_api_fn=failing_api,
    )

    claim, report = judge.execute_judgment(
        candidate_name="failing.candidate",
        candidate_commit_sha="0000000000000000000000000000000000000000",
        candidate_release_version="0.0.1",
    )

    assert claim.verdict == EvaluationVerdict.NON_CONFORMING
    assert report.verdict == EvaluationVerdict.NON_CONFORMING
    assert report.clause_totality_achieved is False


def test_judge_cli_entry_point_execution(tmp_path: Path):
    """Verify fcos-judge CLI main function execution with --publish flag."""
    reg_dir = tmp_path / "cli_claims"
    argv = [
        "--candidate-name", "tools.compiler.fsl",
        "--candidate-sha", "688552a926177b9bbfa7a49646b0f3408093d5b0",
        "--candidate-version", "0.1.0-stage1.wb",
        "--spec-version", "fsl/1.0",
        "--fixtures-dir", "tests/fixtures/conformance",
        "--registry-dir", str(reg_dir),
        "--assertion-date", "2026-08-19T00:00:00Z",
        "--publish",
    ]

    ret = judge_cli_main(argv)
    assert ret == 0

    claim_files = list(reg_dir.glob("*.json"))
    assert len(claim_files) == 2  # .json and .report.json


def test_standing_claim_integrity_and_digest_verification():
    """Verify repository standing claim in docs/conformance/claims/ has valid digests."""
    claims_dir = Path("docs/conformance/claims")
    claim_file = claims_dir / "CLAIM-FSL-1.0-TOOLS.COMPILER.FSL-0.1.0-STAGE1.WB.json"
    report_file = claims_dir / "CLAIM-FSL-1.0-TOOLS.COMPILER.FSL-0.1.0-STAGE1.WB.report.json"

    assert claim_file.exists(), "Standing claim file must exist in repository registry"
    assert report_file.exists(), "Standing report file must exist in repository registry"

    claim_data = json.loads(claim_file.read_text(encoding="utf-8"))
    report_text = report_file.read_text(encoding="utf-8")

    # Verify report JSON matches the SHA-256 digest in the claim
    expected_digest = hashlib.sha256(report_text.encode("utf-8")).hexdigest()
    assert claim_data["evidence_report_digest_sha256"] == expected_digest
    assert claim_data["verdict"] == "CONFORMING"
    assert claim_data["target_specification_version"] == "fsl/1.0"
