"""CLI entry point for the S13 Conformance Test Harness adhering to S13#2.1–S13#2.4."""

import argparse
import json
from pathlib import Path
import sys

from tools.conformance.models import EvaluationVerdict
from tools.conformance.runner import ConformanceHarness


def main(argv: list[str] | None = None) -> int:
    """Run the fcos-conformance CLI."""
    parser = argparse.ArgumentParser(
        prog="fcos-conformance",
        description="FSL S13 Conformance Test Harness (P12.2).",
    )
    parser.add_argument(
        "--fixtures-dir",
        "-f",
        required=True,
        help="Directory containing JSON conformance fixture files.",
    )
    parser.add_argument(
        "--out",
        "-o",
        help="Optional output path for the machine-readable evaluation report JSON.",
    )
    parser.add_argument(
        "--cli-cmd",
        nargs="+",
        help="Optional CLI command list to invoke candidate compiler as subprocess.",
    )
    parser.add_argument(
        "--spec-version",
        default="fsl/1.0",
        help="Target specification version (default: 'fsl/1.0').",
    )

    args = parser.parse_args(argv)

    fixtures_path = Path(args.fixtures_dir)
    if not fixtures_path.exists() or not fixtures_path.is_dir():
        print(f"Error: fixtures directory '{fixtures_path}' not found.", file=sys.stderr)
        return 2

    fixture_files = sorted([f for f in fixtures_path.glob("*.json") if f.name != "manifest.json"])
    if not fixture_files:
        print(f"Error: no test fixture .json files found in '{fixtures_path}'.", file=sys.stderr)
        return 2

    harness = ConformanceHarness(
        candidate_cli_cmd=args.cli_cmd,
        target_spec_version=args.spec_version,
    )

    fixtures = [harness.load_fixture_from_file(ff) for ff in fixture_files]
    use_cli = bool(args.cli_cmd)
    report = harness.evaluate_suite(fixtures, use_cli=use_cli)

    report_json = harness.generate_report_json(report)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report_json + "\n")

    print(f"S13 Conformance Evaluation: {report.verdict.value}")
    print(f"Clauses Tested: {report.total_clauses_tested} | Passed: {report.clauses_passed}")
    print(f"Fixtures Evaluated: {len(report.fixture_results)}")

    return 0 if report.verdict == EvaluationVerdict.CONFORMING else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
