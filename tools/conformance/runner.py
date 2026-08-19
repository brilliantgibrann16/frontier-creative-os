"""Conformance Test Harness execution engine adhering to S13#2.1–S13#2.4 and S13#3.1–S13#3.4."""

from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Callable

from tools.compiler.fsl.api import compile_artifact
from tools.conformance.models import (
    ClauseEvaluation,
    ConformanceEvaluationReport,
    EvaluationVerdict,
    FixtureEvaluationResult,
    FixtureType,
    TestCaseFixture,
)

HARNESS_VERSION = "1.0.0"


class ConformanceHarness:
    """S13 Conformance Test Harness implementation (P12.2).

    Drives candidate tools black-box via ratified CLI (fcos-compile) or programmatic API (compile_artifact).
    """

    def __init__(
        self,
        candidate_cli_cmd: list[str] | None = None,
        candidate_api_fn: Callable[[dict[str, Any]], Any] | None = None,
        target_spec_version: str = "fsl/1.0",
        candidate_identifier: str = "tools.compiler.fsl (built-in)",
    ) -> None:
        self.candidate_cli_cmd = candidate_cli_cmd
        self.candidate_api_fn = candidate_api_fn or compile_artifact
        self.target_spec_version = target_spec_version
        self.candidate_identifier = candidate_identifier

    def load_fixture_from_dict(self, data: dict[str, Any]) -> TestCaseFixture:
        """Load a TestCaseFixture from dictionary."""
        return TestCaseFixture(
            fixture_id=str(data["fixture_id"]),
            target_clause_ids=[str(cid) for cid in data.get("target_clause_ids", [])],
            fixture_type=FixtureType(data.get("fixture_type", "positive")),
            input_payload=data.get("input_payload", {}),
            expected_exit_code=int(data.get("expected_exit_code", 0)),
            expected_diagnostic_codes=[str(c) for c in data.get("expected_diagnostic_codes", [])],
            description=str(data.get("description", "")),
        )

    def load_fixture_from_file(self, fixture_path: Path | str) -> TestCaseFixture:
        """Load a TestCaseFixture from JSON file adhering to S13#3.1."""
        path = Path(fixture_path)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return self.load_fixture_from_dict(data)

    def evaluate_fixture(self, fixture: TestCaseFixture, use_cli: bool = False) -> FixtureEvaluationResult:
        """Evaluate a single test fixture against candidate implementation in a black-box manner (S13#2.1)."""
        failure_reasons: list[str] = []
        observed_exit_code: int = -1
        observed_diagnostic_codes: list[str] = []

        if use_cli and self.candidate_cli_cmd:
            import tempfile

            with tempfile.NamedTemporaryFile(suffix=".json", mode="w", encoding="utf-8", delete=False) as tf:
                json.dump(fixture.input_payload, tf)
                temp_path = tf.name

            try:
                cmd = self.candidate_cli_cmd + [temp_path, "--format", "json"]
                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                )
                observed_exit_code = proc.returncode
                raw_output = proc.stderr.strip() if proc.returncode != 0 else proc.stdout.strip()
                if raw_output:
                    try:
                        out_json = json.loads(raw_output)
                        if isinstance(out_json, list):
                            observed_diagnostic_codes = [
                                str(d.get("clause_id"))
                                for d in out_json
                                if isinstance(d, dict) and d.get("clause_id")
                            ]
                        elif isinstance(out_json, dict) and "diagnostics" in out_json:
                            observed_diagnostic_codes = [
                                str(d.get("clause_id"))
                                for d in out_json["diagnostics"]
                                if isinstance(d, dict) and d.get("clause_id")
                            ]
                    except json.JSONDecodeError:
                        pass
            except Exception as e:
                observed_exit_code = 3
                failure_reasons.append(f"Subprocess invocation error: {e}")
            finally:
                import os

                if os.path.exists(temp_path):
                    os.remove(temp_path)
        else:
            # Black-box programmatic API invocation
            try:
                result = self.candidate_api_fn(fixture.input_payload)
                if hasattr(result, "success"):
                    observed_exit_code = 0 if result.success else 1
                    if hasattr(result, "diagnostics") and isinstance(result.diagnostics, list):
                        observed_diagnostic_codes = [
                            d.clause_id for d in result.diagnostics if hasattr(d, "clause_id") and d.clause_id
                        ]
                else:
                    observed_exit_code = 3
                    failure_reasons.append("API did not return valid CompilationResult object")
            except Exception as e:
                observed_exit_code = 3
                failure_reasons.append(f"API unhandled exception: {e}")

        # Evaluate exit code match
        if observed_exit_code != fixture.expected_exit_code:
            failure_reasons.append(
                f"Exit code mismatch: expected {fixture.expected_exit_code}, got {observed_exit_code}"
            )

        # Evaluate diagnostic clause code match for negative fixtures
        diagnostics_clause_match = True
        if fixture.fixture_type == FixtureType.NEGATIVE and fixture.expected_diagnostic_codes:
            for expected_cid in fixture.expected_diagnostic_codes:
                if expected_cid not in observed_diagnostic_codes:
                    diagnostics_clause_match = False
                    failure_reasons.append(
                        f"Expected diagnostic clause_id '{expected_cid}' was not emitted (observed: {observed_diagnostic_codes})"
                    )

        passed = len(failure_reasons) == 0

        return FixtureEvaluationResult(
            fixture_id=fixture.fixture_id,
            target_clause_ids=sorted(fixture.target_clause_ids),
            passed=passed,
            observed_exit_code=observed_exit_code,
            expected_exit_code=fixture.expected_exit_code,
            observed_diagnostic_codes=sorted(observed_diagnostic_codes),
            expected_diagnostic_codes=sorted(fixture.expected_diagnostic_codes),
            diagnostics_clause_match=diagnostics_clause_match,
            failure_reasons=failure_reasons,
        )

    def evaluate_suite(
        self,
        fixtures: list[TestCaseFixture],
        use_cli: bool = False,
    ) -> ConformanceEvaluationReport:
        """Evaluate a full fixture suite and construct a deterministic ConformanceEvaluationReport (S13#2.4)."""
        fixture_results: list[FixtureEvaluationResult] = []
        clause_fixtures: dict[str, list[TestCaseFixture]] = defaultdict(list)
        clause_results: dict[str, list[FixtureEvaluationResult]] = defaultdict(list)

        for fixture in sorted(fixtures, key=lambda f: f.fixture_id):
            result = self.evaluate_fixture(fixture, use_cli=use_cli)
            fixture_results.append(result)
            for cid in fixture.target_clause_ids:
                clause_fixtures[cid].append(fixture)
                clause_results[cid].append(result)

        clause_evaluations: list[ClauseEvaluation] = []
        for cid in sorted(clause_fixtures.keys()):
            c_fixtures = clause_fixtures[cid]
            c_results = clause_results[cid]
            total_f = len(c_fixtures)
            passed_f = sum(1 for r in c_results if r.passed)
            pos_f = sum(1 for f in c_fixtures if f.fixture_type == FixtureType.POSITIVE)
            neg_f = sum(1 for f in c_fixtures if f.fixture_type == FixtureType.NEGATIVE)
            clause_passed = total_f > 0 and passed_f == total_f

            clause_evaluations.append(
                ClauseEvaluation(
                    clause_id=cid,
                    total_fixtures=total_f,
                    passed_fixtures=passed_f,
                    positive_fixtures_count=pos_f,
                    negative_fixtures_count=neg_f,
                    passed=clause_passed,
                )
            )

        total_clauses = len(clause_evaluations)
        clauses_passed = sum(1 for ce in clause_evaluations if ce.passed)
        totality_achieved = total_clauses > 0 and clauses_passed == total_clauses
        all_fixtures_passed = len(fixture_results) > 0 and all(fr.passed for fr in fixture_results)

        verdict = (
            EvaluationVerdict.CONFORMING
            if (totality_achieved and all_fixtures_passed)
            else EvaluationVerdict.NON_CONFORMING
        )

        return ConformanceEvaluationReport(
            harness_version=HARNESS_VERSION,
            target_spec_version=self.target_spec_version,
            candidate_identifier=self.candidate_identifier,
            verdict=verdict,
            total_clauses_tested=total_clauses,
            clauses_passed=clauses_passed,
            clause_totality_achieved=totality_achieved,
            clause_evaluations=clause_evaluations,
            fixture_results=fixture_results,
        )

    def generate_report_json(self, report: ConformanceEvaluationReport) -> str:
        """Serialize report to deterministic JSON (DP-28)."""
        return json.dumps(report.to_dict(), indent=2, sort_keys=True)
