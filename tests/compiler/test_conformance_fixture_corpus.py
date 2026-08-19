"""Comprehensive tests for P12.3 Conformance Fixture Corpus."""

import json
from pathlib import Path

import pytest

from tools.conformance.models import EvaluationVerdict
from tools.conformance.runner import ConformanceHarness

CORPUS_DIR = Path("tests/fixtures/conformance")


def test_conformance_fixture_corpus_manifest_validity() -> None:
    """Verify the conformance fixture corpus manifest schema and file references."""
    manifest_path = CORPUS_DIR / "manifest.json"
    assert manifest_path.exists(), "manifest.json must exist in conformance fixtures directory"

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    assert manifest["corpus_version"] == "1.0.0"
    assert manifest["target_specification_version"] == "fsl/1.0"
    assert len(manifest["fixtures"]) >= 8

    for entry in manifest["fixtures"]:
        fixture_file = CORPUS_DIR / entry["file"]
        assert fixture_file.exists(), f"Fixture file '{entry['file']}' referenced in manifest does not exist"
        with open(fixture_file, "r", encoding="utf-8") as ff:
            fdata = json.load(ff)
        assert fdata["fixture_id"] == entry["id"]
        assert fdata["fixture_type"] == entry["type"]


def test_conformance_harness_evaluates_p12_3_canonical_corpus_to_conforming() -> None:
    """Execute P12.2 Conformance Harness against full P12.3 Canonical Fixture Corpus."""
    manifest_path = CORPUS_DIR / "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    harness = ConformanceHarness(target_spec_version="fsl/1.0")
    fixtures = [harness.load_fixture_from_file(CORPUS_DIR / entry["file"]) for entry in manifest["fixtures"]]

    report = harness.evaluate_suite(fixtures)

    assert report.verdict == EvaluationVerdict.CONFORMING
    assert report.clause_totality_achieved is True
    assert report.total_clauses_tested >= 8
    assert report.clauses_passed == report.total_clauses_tested
    assert all(r.passed for r in report.fixture_results)
    assert len(report.fixture_results) == len(manifest["fixtures"])


def test_conformance_harness_cli_evaluates_p12_3_corpus_via_subprocess() -> None:
    """Execute CLI subprocess invocation against P12.3 Canonical Fixture Corpus."""
    harness = ConformanceHarness(
        candidate_cli_cmd=["python3", "-m", "tools.compiler.fsl.cli"],
        target_spec_version="fsl/1.0",
    )
    fixture_files = sorted([f for f in CORPUS_DIR.glob("*.json") if f.name != "manifest.json"])
    fixtures = [harness.load_fixture_from_file(ff) for ff in fixture_files]

    report = harness.evaluate_suite(fixtures, use_cli=True)

    assert report.verdict == EvaluationVerdict.CONFORMING
    assert report.clause_totality_achieved is True
    assert all(r.passed for r in report.fixture_results)
