#!/usr/bin/env python3
"""Mechanical conformance claims registry verification check (S13#4.4, P12.4).

Verifies:
1. Public claims directory `docs/conformance/claims/` exists.
2. Every claim file has valid JSON and contains all required S13#4.2 fields.
3. Every claim has a corresponding .report.json evaluation report.
4. The SHA-256 digest of the report file matches `evidence_report_digest_sha256` in the claim.
5. Every claim in the registry has a binary verdict of CONFORMING with clause totality achieved.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

REQUIRED_CLAIM_FIELDS = {
    "claim_id",
    "candidate_name",
    "candidate_commit_sha",
    "candidate_release_version",
    "target_specification_version",
    "harness_hash_sha256",
    "verdict",
    "evidence_report_digest_sha256",
    "assertion_date_utc",
}


def check_conformance_registry(repo_root: Path | None = None) -> list[str]:
    """Audit the public conformance claims registry and return a list of error findings."""
    if repo_root is None:
        repo_root = Path(__file__).resolve().parents[2]

    claims_dir = repo_root / "docs" / "conformance" / "claims"
    if not claims_dir.is_dir():
        return [f"Conformance claims directory not found at '{claims_dir}'."]

    claim_files = sorted(
        [
            p
            for p in claims_dir.glob("*.json")
            if not p.name.endswith(".report.json") and not p.name.endswith(".manifest.json")
        ]
    )

    if not claim_files:
        return [f"No claim .json files found in '{claims_dir}'."]

    findings: list[str] = []

    for claim_path in claim_files:
        try:
            claim_text = claim_path.read_text(encoding="utf-8")
            claim_data = json.loads(claim_text)
        except Exception as e:
            findings.append(f"{claim_path.name}: Failed to read/parse JSON: {e}")
            continue

        # Check required fields
        missing_fields = REQUIRED_CLAIM_FIELDS - set(claim_data.keys())
        if missing_fields:
            findings.append(
                f"{claim_path.name}: Missing required S13#4.2 fields: {sorted(missing_fields)}"
            )

        claim_id = claim_data.get("claim_id")
        if not claim_id:
            findings.append(f"{claim_path.name}: Empty or missing 'claim_id'.")
            continue

        verdict = claim_data.get("verdict")
        if verdict != "CONFORMING":
            findings.append(
                f"{claim_path.name}: Claim verdict is '{verdict}', expected 'CONFORMING'."
            )

        # Verify corresponding report file
        report_path = claims_dir / f"{claim_id}.report.json"
        if not report_path.exists():
            # Also try matching file stem if claim_id differs
            alt_report = claims_dir / f"{claim_path.stem}.report.json"
            if alt_report.exists():
                report_path = alt_report
            else:
                findings.append(
                    f"{claim_path.name}: Missing evaluation report file at '{report_path.name}'."
                )
                continue

        try:
            report_text = report_path.read_text(encoding="utf-8")
            report_data = json.loads(report_text)
        except Exception as e:
            findings.append(f"{report_path.name}: Failed to read/parse JSON: {e}")
            continue

        # Verify SHA-256 digest
        computed_digest = hashlib.sha256(report_text.encode("utf-8")).hexdigest()
        declared_digest = claim_data.get("evidence_report_digest_sha256")
        if computed_digest != declared_digest:
            findings.append(
                f"{claim_path.name}: Evidence digest mismatch! Claim has '{declared_digest}', "
                f"actual report SHA-256 is '{computed_digest}'."
            )

        # Verify report status
        if not report_data.get("clause_totality_achieved"):
            findings.append(
                f"{report_path.name}: Report indicates clause totality was not achieved."
            )

        if report_data.get("verdict") != "CONFORMING":
            findings.append(
                f"{report_path.name}: Report verdict is '{report_data.get('verdict')}', expected 'CONFORMING'."
            )

    return findings


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for mechanical conformance claims registry check."""
    findings = check_conformance_registry()
    if findings:
        for finding in findings:
            print(f"ERROR check_conformance: {finding}", file=sys.stderr)
        return 1

    print("check_conformance: all registered conformance claims are valid and verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
