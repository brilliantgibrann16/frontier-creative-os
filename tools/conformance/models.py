"""Data models for S13 Conformance Test Harness adhering to S13#1.2, S13#2.4, S13#3.1–S13#3.4, S13#4.2."""

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class FixtureType(str, Enum):
    """Fixture classification adhering to S13#3.2."""

    POSITIVE = "positive"
    NEGATIVE = "negative"


class EvaluationVerdict(str, Enum):
    """Binary evaluation verdict adhering to S13#1.2."""

    CONFORMING = "CONFORMING"
    NON_CONFORMING = "NON_CONFORMING"


@dataclass(frozen=True)
class TestCaseFixture:
    """Normative test case fixture specification adhering to S13#3.1–S13#3.4."""

    __test__ = False  # Prevent pytest from collecting this data class as a test suite

    fixture_id: str
    target_clause_ids: list[str]
    fixture_type: FixtureType
    input_payload: dict[str, Any]
    expected_exit_code: int
    expected_diagnostic_codes: list[str] = field(default_factory=list)
    description: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Return deterministic dictionary representation."""
        return {
            "fixture_id": self.fixture_id,
            "target_clause_ids": sorted(self.target_clause_ids),
            "fixture_type": self.fixture_type.value,
            "input_payload": self.input_payload,
            "expected_exit_code": self.expected_exit_code,
            "expected_diagnostic_codes": sorted(self.expected_diagnostic_codes),
            "description": self.description,
        }


@dataclass(frozen=True)
class FixtureEvaluationResult:
    """Individual fixture execution result record."""

    fixture_id: str
    target_clause_ids: list[str]
    passed: bool
    observed_exit_code: int
    expected_exit_code: int
    observed_diagnostic_codes: list[str]
    expected_diagnostic_codes: list[str]
    diagnostics_clause_match: bool
    failure_reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Return deterministic dictionary representation."""
        return {
            "fixture_id": self.fixture_id,
            "target_clause_ids": sorted(self.target_clause_ids),
            "passed": self.passed,
            "observed_exit_code": self.observed_exit_code,
            "expected_exit_code": self.expected_exit_code,
            "observed_diagnostic_codes": sorted(self.observed_diagnostic_codes),
            "expected_diagnostic_codes": sorted(self.expected_diagnostic_codes),
            "diagnostics_clause_match": self.diagnostics_clause_match,
            "failure_reasons": self.failure_reasons,
        }


@dataclass(frozen=True)
class ClauseEvaluation:
    """Per-clause evaluation summary adhering to S13#1.3."""

    clause_id: str
    total_fixtures: int
    passed_fixtures: int
    positive_fixtures_count: int
    negative_fixtures_count: int
    passed: bool

    def to_dict(self) -> dict[str, Any]:
        """Return deterministic dictionary representation."""
        return {
            "clause_id": self.clause_id,
            "total_fixtures": self.total_fixtures,
            "passed_fixtures": self.passed_fixtures,
            "positive_fixtures_count": self.positive_fixtures_count,
            "negative_fixtures_count": self.negative_fixtures_count,
            "passed": self.passed,
        }


@dataclass(frozen=True)
class ConformanceEvaluationReport:
    """Machine-readable conformance evaluation report adhering to S13#2.4."""

    harness_version: str
    target_spec_version: str
    candidate_identifier: str
    verdict: EvaluationVerdict
    total_clauses_tested: int
    clauses_passed: int
    clause_totality_achieved: bool
    clause_evaluations: list[ClauseEvaluation]
    fixture_results: list[FixtureEvaluationResult]

    def to_dict(self) -> dict[str, Any]:
        """Return deterministic dictionary representation."""
        return {
            "harness_version": self.harness_version,
            "target_spec_version": self.target_spec_version,
            "candidate_identifier": self.candidate_identifier,
            "verdict": self.verdict.value,
            "total_clauses_tested": self.total_clauses_tested,
            "clauses_passed": self.clauses_passed,
            "clause_totality_achieved": self.clause_totality_achieved,
            "clause_evaluations": [c.to_dict() for c in sorted(self.clause_evaluations, key=lambda x: x.clause_id)],
            "fixture_results": [f.to_dict() for f in sorted(self.fixture_results, key=lambda x: x.fixture_id)],
        }


@dataclass(frozen=True)
class ConformanceClaim:
    """Official Conformance Claim document adhering to S13#4.2."""

    claim_id: str
    candidate_name: str
    candidate_commit_sha: str
    candidate_release_version: str
    target_specification_version: str
    harness_hash_sha256: str
    verdict: EvaluationVerdict
    evidence_report_digest_sha256: str
    assertion_date_utc: str

    def to_dict(self) -> dict[str, Any]:
        """Return deterministic dictionary representation."""
        return {
            "claim_id": self.claim_id,
            "candidate_name": self.candidate_name,
            "candidate_commit_sha": self.candidate_commit_sha,
            "candidate_release_version": self.candidate_release_version,
            "target_specification_version": self.target_specification_version,
            "harness_hash_sha256": self.harness_hash_sha256,
            "verdict": self.verdict.value,
            "evidence_report_digest_sha256": self.evidence_report_digest_sha256,
            "assertion_date_utc": self.assertion_date_utc,
        }
