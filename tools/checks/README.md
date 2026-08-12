# Mechanical Documentation Checks

Status: Active (Wave 0, programs P01 and P13 frame)

Governing artifacts: RFC-0011 disposition E-A (gates encoded in CI, per ADR-0004), Architecture Baseline L-10 (mechanical checks never encode policy), Blueprint INV-19 and Baseline L-5 (identical gates for human and AI contributions).

## Purpose

Small, dependency-free scripts that verify **mechanical** properties of the repository's Markdown documentation. They express no policy and resolve no governance question (L-10). Any check whose outcome would require interpretation of document content does not belong here; it must route through the decision process first.

## Checks

| Script | What it verifies | What it does NOT do |
| --- | --- | --- |
| `check_links.py` | Every relative Markdown link in scanned docs points to an existing file or directory. | Does not validate external URLs, anchors within files, or content quality. |
| `check_ids.py` | Every `ADR-XXXX` / `RFC-XXXX` identifier mentioned in scanned docs has a corresponding file in `docs/decisions/` / `docs/rfc/`. | Does not check identifier status, disposition, or the correctness of the citation. |
| `check_clause_index.py` | Every clause-index sidecar (`specs/<spec>.index.yaml`, ADR-0010) is consistent with its specification prose: clause ↔ index correspondence, duplicate IDs, category/status vocabularies, identifier syntax, and source references (ADR-0010 decision 11; implementation authorized by ADR-0011). | Does not interpret clause content, does not judge categorization correctness, and never modifies or auto-fixes anything. |

## Scope

- Scanned roots: `README.md`, `docs/`, `specs/`.
- Excluded: `specs/fcos/` — a legacy prototype specification tree whose disposition is an open Maintainer decision (see the P00.1 blocker in `docs/program/WAVE_0_VERIFICATION.md`). The exclusion is neutrality-preserving: scanning it would presume it is governed documentation, deleting it would presume the opposite, and neither presumption is this tool's to make.

## Running

From the repository root:

```
python tools/checks/check_links.py
python tools/checks/check_ids.py
python tools/checks/check_clause_index.py
```

Each script prints one line per finding and exits non-zero when findings exist. An optional argument overrides the repository root (used by the tests):

```
python tools/checks/check_links.py /path/to/repo
```

## Tests

Fixture-based tests live in `tests/test_check_links.py`, `tests/test_check_ids.py`, and `tests/test_check_clause_index.py` (pytest, `tmp_path` fixtures, standard library only), following `docs/program/TESTING_CONVENTIONS.md`.

## CI integration

The link, ID, and clause-index checks run in `.github/workflows/ci.yml` on every push to `main` and every pull request, alongside the prototype test suite. They gate all contributions identically (INV-19 / L-5). `check_clause_index.py` joined the documentation-gates job by explicit Maintainer decision on 2026-08-13 (P03.5 — the exact decision surface ADR-0011, Decision 8, left open); the RFC-0011 E-A baseline gates (tests + link checks + ID checks) are unchanged, and any further gate-set expansion remains decision-level (PROGRAM.md P01). Its regression tests run inside the CI test job like every other test.

## Design constraints

- Standard library only; no third-party dependencies.
- Each script is standalone and runnable directly; the small amount of shared scanning logic is deliberately duplicated so each check stays independently auditable.
- New checks must be mechanical in the L-10 sense. Anything policy-adjacent requires a decision artifact before implementation.
