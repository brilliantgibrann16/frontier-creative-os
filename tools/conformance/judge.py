"""Official S13 Conformance Judge and Claim Publisher.

Adheres strictly to ratified specification S13 (ADR-0015):
- S13#1.1: Sole judge authority
- S13#1.2: Binary conformance model (CONFORMING vs NON_CONFORMING)
- S13#1.3: Clause totality (100% of testable clauses satisfied)
- S13#2.1–S13#2.4: Standard black-box harness evaluation
- S13#4.1–S13#4.4: Self-certification protocol, claim structure, and registry publication
"""

import argparse
import datetime
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Callable

from tools.conformance.models import (
    ConformanceClaim,
    ConformanceEvaluationReport,
    EvaluationVerdict,
    TestCaseFixture,
)
from tools.conformance.runner import ConformanceHarness


def compute_harness_hash() -> str:
    """Compute SHA-256 digest of the S13 Conformance Judge and Harness code files."""
    hasher = hashlib.sha256()
    conformance_dir = Path(__file__).resolve().parent

    # Hash core harness and judge source files in deterministic alphabetical order
    source_files = sorted(
        [
            conformance_dir / "__init__.py",
            conformance_dir / "models.py",
            conformance_dir / "runner.py",
            conformance_dir / "judge.py",
        ]
    )

    for sf in source_files:
        if sf.exists():
            hasher.update(sf.read_bytes())

    return hasher.hexdigest()


class ConformanceJudge:
    """Official S13 Conformance Judge (P12.4).

    Executes conformance test suite against candidate implementations and
    issues official, reproducible Conformance Claims under S13#4.1–S13#4.4.
    """

    def __init__(
        self,
        target_spec_version: str = "fsl/1.0",
        fixtures_dir: Path | str = Path("tests/fixtures/conformance"),
        candidate_cli_cmd: list[str] | None = None,
        candidate_api_fn: Callable[[dict[str, Any]], Any] | None = None,
    ) -> None:
        self.target_spec_version = target_spec_version
        self.fixtures_dir = Path(fixtures_dir)
        self.harness = ConformanceHarness(
            candidate_cli_cmd=candidate_cli_cmd,
            candidate_api_fn=candidate_api_fn,
            target_spec_version=target_spec_version,
            candidate_identifier="tools.compiler.fsl (built-in)",
        )

    def load_canonical_fixtures(self) -> list[TestCaseFixture]:
        """Load all canonical test fixtures from the fixtures directory, excluding manifest.json."""
        if not self.fixtures_dir.exists() or not self.fixtures_dir.is_dir():
            raise FileNotFoundError(f"Fixtures directory '{self.fixtures_dir}' not found.")

        fixture_files = sorted(
            [f for f in self.fixtures_dir.glob("*.json") if f.name != "manifest.json"]
        )
        if not fixture_files:
            raise ValueError(f"No .json fixture files found in '{self.fixtures_dir}'.")

        return [self.harness.load_fixture_from_file(f) for f in fixture_files]

    def execute_judgment(
        self,
        candidate_name: str,
        candidate_commit_sha: str,
        candidate_release_version: str,
        assertion_date_utc: str | None = None,
        claim_id: str | None = None,
        use_cli: bool = False,
    ) -> tuple[ConformanceClaim, ConformanceEvaluationReport]:
        """Execute judgment over canonical fixtures and produce a ConformanceClaim (S13#4.2)."""
        fixtures = self.load_canonical_fixtures()
        report = self.harness.evaluate_suite(fixtures, use_cli=use_cli)

        report_json = self.harness.generate_report_json(report) + "\n"
        evidence_digest = hashlib.sha256(report_json.encode("utf-8")).hexdigest()
        harness_hash = compute_harness_hash()

        date_str = (
            assertion_date_utc
            if assertion_date_utc
            else datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        )

        sanitized_spec = self.target_spec_version.replace("/", "-").upper()
        sanitized_candidate = candidate_name.replace(" ", "-").replace("/", "-").lower()
        generated_claim_id = (
            claim_id
            if claim_id
            else f"CLAIM-{sanitized_spec}-{sanitized_candidate}-{candidate_release_version}"
        )

        claim = ConformanceClaim(
            claim_id=generated_claim_id,
            candidate_name=candidate_name,
            candidate_commit_sha=candidate_commit_sha,
            candidate_release_version=candidate_release_version,
            target_specification_version=self.target_spec_version,
            harness_hash_sha256=harness_hash,
            verdict=report.verdict,
            evidence_report_digest_sha256=evidence_digest,
            assertion_date_utc=date_str,
        )

        return claim, report

    def publish_claim(
        self,
        claim: ConformanceClaim,
        report: ConformanceEvaluationReport,
        registry_dir: Path | str = Path("docs/conformance/claims"),
    ) -> tuple[Path, Path]:
        """Publish ConformanceClaim and evidence report to repository claim registry (S13#4.4)."""
        reg_path = Path(registry_dir)
        reg_path.mkdir(parents=True, exist_ok=True)

        claim_file = reg_path / f"{claim.claim_id}.json"
        report_file = reg_path / f"{claim.claim_id}.report.json"

        claim_json = json.dumps(claim.to_dict(), indent=2, sort_keys=True) + "\n"
        report_json = self.harness.generate_report_json(report) + "\n"

        # Check immutability (S13 state machine: claims are immutable)
        if claim_file.exists():
            existing_claim = claim_file.read_text(encoding="utf-8")
            if existing_claim != claim_json:
                raise ValueError(
                    f"Immutability violation: Claim '{claim.claim_id}' already exists with differing content."
                )

        claim_file.write_text(claim_json, encoding="utf-8")
        report_file.write_text(report_json, encoding="utf-8")

        return claim_file, report_file


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for official judging (fcos-judge)."""
    parser = argparse.ArgumentParser(
        prog="fcos-judge",
        description="FSL S13 Official Conformance Judge & Claim Publisher (P12.4).",
    )
    parser.add_argument(
        "--candidate-name",
        "-n",
        required=True,
        help="Name of candidate implementation under judgment.",
    )
    parser.add_argument(
        "--candidate-sha",
        "-s",
        required=True,
        help="Git commit SHA of candidate implementation.",
    )
    parser.add_argument(
        "--candidate-version",
        "-v",
        required=True,
        help="Release version string of candidate implementation.",
    )
    parser.add_argument(
        "--spec-version",
        default="fsl/1.0",
        help="Target specification version (default: 'fsl/1.0').",
    )
    parser.add_argument(
        "--fixtures-dir",
        "-f",
        default="tests/fixtures/conformance",
        help="Directory containing canonical JSON test fixtures (default: 'tests/fixtures/conformance').",
    )
    parser.add_argument(
        "--registry-dir",
        "-r",
        default="docs/conformance/claims",
        help="Registry directory for saving published claims (default: 'docs/conformance/claims').",
    )
    parser.add_argument(
        "--cli-cmd",
        nargs="+",
        help="Optional CLI command list to invoke candidate compiler as subprocess.",
    )
    parser.add_argument(
        "--claim-id",
        help="Optional explicit claim ID override.",
    )
    parser.add_argument(
        "--assertion-date",
        help="Optional explicit assertion date in ISO UTC format (e.g. '2026-08-19T00:00:00Z').",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Publish the resulting claim and report to the registry directory.",
    )

    args = parser.parse_args(argv)

    try:
        judge = ConformanceJudge(
            target_spec_version=args.spec_version,
            fixtures_dir=args.fixtures_dir,
            candidate_cli_cmd=args.cli_cmd,
        )
        claim, report = judge.execute_judgment(
            candidate_name=args.candidate_name,
            candidate_commit_sha=args.candidate_sha,
            candidate_release_version=args.candidate_version,
            assertion_date_utc=args.assertion_date,
            claim_id=args.claim_id,
            use_cli=bool(args.cli_cmd),
        )

        print(f"S13 Official Conformance Judgment: {claim.verdict.value}")
        print(f"Claim ID: {claim.claim_id}")
        print(f"Target Specification: {claim.target_specification_version}")
        print(f"Candidate: {claim.candidate_name} (version {claim.candidate_release_version}, commit {claim.candidate_commit_sha[:8]})")
        print(f"Clauses Tested: {report.total_clauses_tested} | Passed: {report.clauses_passed} | Totality: {report.clause_totality_achieved}")
        print(f"Harness Hash: {claim.harness_hash_sha256[:16]}... | Evidence Digest: {claim.evidence_report_digest_sha256[:16]}...")

        if args.publish:
            claim_path, report_path = judge.publish_claim(
                claim=claim,
                report=report,
                registry_dir=args.registry_dir,
            )
            print(f"Published Claim: {claim_path}")
            print(f"Published Report: {report_path}")

        return 0 if claim.verdict == EvaluationVerdict.CONFORMING else 1

    except Exception as e:
        print(f"Error during conformance judgment: {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
