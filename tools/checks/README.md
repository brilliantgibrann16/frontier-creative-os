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

## Scope

- Scanned roots: `README.md`, `docs/`, `specs/`.
- Excluded: `specs/fcos/` — a legacy prototype specification tree whose disposition is an open Maintainer decision (see the P00.1 blocker in `docs/program/WAVE_0_VERIFICATION.md`). The exclusion is neutrality-preserving: scanning it would presume it is governed documentation, deleting it would presume the opposite, and neither presumption is this tool's to make.

## Running

From the repository root:

```
python tools/checks/check_links.py
python tools/checks/check_ids.py
```

Each script prints one line per finding and exits non-zero when findings exist. An optional argument overrides the repository root (used by the tests):

```
python tools/checks/check_links.py /path/to/repo
```

## Tests

Fixture-based tests live in `tests/test_check_links.py` and `tests/test_check_ids.py` (pytest, `tmp_path` fixtures, standard library only), following `docs/program/TESTING_CONVENTIONS.md`.

## CI integration

Both checks run in `.github/workflows/ci.yml` on every push to `main` and every pull request, alongside the prototype test suite. They gate all contributions identically (INV-19 / L-5).

## Design constraints

- Standard library only; no third-party dependencies.
- Each script is standalone and runnable directly; the small amount of shared scanning logic is deliberately duplicated so each check stays independently auditable.
- New checks must be mechanical in the L-10 sense. Anything policy-adjacent requires a decision artifact before implementation.
