"""Comprehensive test suite for P12.2 S13 Conformance Test Harness."""

import json
from pathlib import Path
import tempfile

import pytest

from tools.compiler.fsl.api import compile_artifact
from tools.conformance.cli import main as cli_main
from tools.conformance.models import (
    EvaluationVerdict,
    FixtureEvaluationResult,
    FixtureType,
    TestCaseFixture,
)
from tools.conformance.runner import ConformanceHarness


@pytest.fixture
def sample_positive_fixture() -> TestCaseFixture:
    """A valid Stage 1 W-B positive fixture for S04#5.1 and S05#1.1."""
    return TestCaseFixture(
        fixture_id="pos_s04_5_1_minimal_valid",
        target_clause_ids=["S04#5.1", "S05#1.1"],
        fixture_type=FixtureType.POSITIVE,
        input_payload={
            "schema_version": "fsl/1.0",
            "manifest": {
                "name": "valid-minimal-test",
                "version": "1.0.0",
                "kind": "application",
            },
        },
        expected_exit_code=0,
        expected_diagnostic_codes=[],
        description="Minimal valid artifact unit testing S04#5.1 acceptance.",
    )


@pytest.fixture
def sample_negative_fixture() -> TestCaseFixture:
    """An invalid Stage 1 W-B negative fixture for S04#8.3 schema version."""
    return TestCaseFixture(
        fixture_id="neg_s04_8_3_missing_schema_version",
        target_clause_ids=["S04#8.3", "S05#1.2"],
        fixture_type=FixtureType.NEGATIVE,
        input_payload={
            "manifest": {
                "name": "missing-version",
                "version": "1.0.0",
                "kind": "application",
            },
        },
        expected_exit_code=1,
        expected_diagnostic_codes=["S04#8.3"],
        description="Missing schema_version field testing S04#8.3 rejection.",
    )


def test_harness_evaluates_positive_fixture_successfully(sample_positive_fixture: TestCaseFixture) -> None:
    """Test harness correctly evaluates and approves a conforming positive fixture."""
    harness = ConformanceHarness()
    result = harness.evaluate_fixture(sample_positive_fixture)

    assert result.passed is True
    assert result.observed_exit_code == 0
    assert result.expected_exit_code == 0
    assert len(result.failure_reasons) == 0


def test_harness_evaluates_negative_fixture_and_verifies_diagnostics(
    sample_negative_fixture: TestCaseFixture,
) -> None:
    """Test harness correctly evaluates and approves a conforming negative fixture with clause attribution."""
    harness = ConformanceHarness()
    result = harness.evaluate_fixture(sample_negative_fixture)

    assert result.passed is True
    assert result.observed_exit_code == 1
    assert result.diagnostics_clause_match is True
    assert "S04#8.3" in result.observed_diagnostic_codes


def test_harness_detects_unexpected_acceptance_failure() -> None:
    """Test harness fails when an invalid artifact is unexpectedly accepted."""
    faulty_fixture = TestCaseFixture(
        fixture_id="neg_should_fail",
        target_clause_ids=["S04#8.3"],
        fixture_type=FixtureType.NEGATIVE,
        input_payload={
            "schema_version": "fsl/1.0",
            "manifest": {"name": "valid", "version": "1.0.0", "kind": "application"},
        },
        expected_exit_code=1,
        expected_diagnostic_codes=["S04#8.3"],
    )
    harness = ConformanceHarness()
    result = harness.evaluate_fixture(faulty_fixture)

    assert result.passed is False
    assert result.observed_exit_code == 0
    assert any("Exit code mismatch" in r for r in result.failure_reasons)


def test_harness_detects_missing_diagnostic_clause_id() -> None:
    """Test harness fails when expected diagnostic clause_id is not emitted."""
    faulty_fixture = TestCaseFixture(
        fixture_id="neg_wrong_clause",
        target_clause_ids=["S04#5.1"],
        fixture_type=FixtureType.NEGATIVE,
        input_payload={"manifest": {"name": "valid", "version": "1.0.0", "kind": "application"}},
        expected_exit_code=1,
        expected_diagnostic_codes=["S04#99.99"],  # non-existent clause
    )
    harness = ConformanceHarness()
    result = harness.evaluate_fixture(faulty_fixture)

    assert result.passed is False
    assert result.diagnostics_clause_match is False
    assert any("Expected diagnostic clause_id 'S04#99.99' was not emitted" in r for r in result.failure_reasons)


def test_harness_suite_totality_and_binary_verdict(
    sample_positive_fixture: TestCaseFixture,
    sample_negative_fixture: TestCaseFixture,
) -> None:
    """Test full suite evaluation yields binary CONFORMING verdict upon totality."""
    harness = ConformanceHarness()
    report = harness.evaluate_suite([sample_positive_fixture, sample_negative_fixture])

    assert report.verdict == EvaluationVerdict.CONFORMING
    assert report.clause_totality_achieved is True
    assert report.total_clauses_tested == 4  # S04#5.1, S05#1.1, S04#8.3, S05#1.2
    assert report.clauses_passed == 4
    assert len(report.fixture_results) == 2


def test_harness_suite_yields_non_conforming_verdict_on_failure(
    sample_positive_fixture: TestCaseFixture,
) -> None:
    """Test suite evaluation returns NON_CONFORMING when any fixture fails."""
    failing_fixture = TestCaseFixture(
        fixture_id="failing_fixture",
        target_clause_ids=["S04#5.1"],
        fixture_type=FixtureType.POSITIVE,
        input_payload={"invalid": "payload"},  # will fail validation
        expected_exit_code=0,
    )
    harness = ConformanceHarness()
    report = harness.evaluate_suite([sample_positive_fixture, failing_fixture])

    assert report.verdict == EvaluationVerdict.NON_CONFORMING
    assert report.clause_totality_achieved is False


def test_harness_cli_subprocess_invocation(
    sample_positive_fixture: TestCaseFixture,
    sample_negative_fixture: TestCaseFixture,
) -> None:
    """Test harness black-box subprocess CLI invocation of candidate compiler (S13#2.1)."""
    harness = ConformanceHarness(
        candidate_cli_cmd=["python3", "-m", "tools.compiler.fsl.cli"],
    )
    report = harness.evaluate_suite([sample_positive_fixture, sample_negative_fixture], use_cli=True)

    assert report.verdict == EvaluationVerdict.CONFORMING
    assert report.clause_totality_achieved is True
    assert all(r.passed for r in report.fixture_results)


def test_harness_report_serialization_is_byte_for_byte_deterministic(
    sample_positive_fixture: TestCaseFixture,
    sample_negative_fixture: TestCaseFixture,
) -> None:
    """Test report JSON serialization is completely deterministic and reproducible (DP-28)."""
    harness = ConformanceHarness()
    report1 = harness.evaluate_suite([sample_positive_fixture, sample_negative_fixture])
    json1 = harness.generate_report_json(report1)

    report2 = harness.evaluate_suite([sample_negative_fixture, sample_positive_fixture])  # reversed input order
    json2 = harness.generate_report_json(report2)

    assert json1 == json2


def test_harness_cli_entry_point_execution(
    sample_positive_fixture: TestCaseFixture,
    sample_negative_fixture: TestCaseFixture,
) -> None:
    """Test fcos-conformance CLI entry point execution over fixture directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        f1_path = dir_path / "fixture_pos.json"
        f2_path = dir_path / "fixture_neg.json"
        out_report = dir_path / "report.json"

        with open(f1_path, "w", encoding="utf-8") as f:
            json.dump(sample_positive_fixture.to_dict(), f)
        with open(f2_path, "w", encoding="utf-8") as f:
            json.dump(sample_negative_fixture.to_dict(), f)

        exit_code = cli_main(["--fixtures-dir", str(dir_path), "--out", str(out_report)])

        assert exit_code == 0
        assert out_report.exists()
        with open(out_report, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data["verdict"] == "CONFORMING"
        assert data["total_clauses_tested"] == 4
