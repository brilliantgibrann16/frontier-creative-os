# Wave 0 Verification Artifact

- Date: 2026-08-02
- Branch: `ci/wave-0` from `main` @ `4e65829a`
- Program source: `docs/program/PROGRAM.md`, `docs/program/WORK_BREAKDOWN_STRUCTURE.md` (PR #15 branch; treated as the wave plan under review)
- Mission constraints honored: no architecture redesign, no governance artifacts, no RFCs, no ADR modifications, no blocked package implemented, no governance resolved through code.

## 1. Verification method

Before implementing each work package, three checks were performed against repository state at `4e65829a`:

1. **Dependency chain** — all upstream packages/gates satisfied.
2. **Blockers** — no open blocker (B-01…B-10) or gate (G-D01, G-CI, G-SPEC(x), G-CONF) applies.
3. **Governance neutrality** — the change resolves or narrows no undecided question.

Facts were verified by direct inspection of the repository tree and file contents, not from memory or search indexes.

## 2. Package dispositions

### P00 — Repository hygiene

| Package | Disposition | Verification summary | Evidence |
| --- | --- | --- | --- |
| P00.1 remove `specs/fcos/` | **BLOCKED — new blocker B-11** | Premise check failed: `specs/fcos/` is not an empty scaffold. It holds ~40 substantive specification documents across `api/`, `compiler/`, `core/`, `intelligence/`, `model/`, `runtime/` (only `playbooks/` and `prompts/` are `.gitkeep`-only). ADR-0005 decided the specification home; it did not decide the disposal of this content. Deleting would destroy potentially referenced material; adopting would promote unratified documents. Either action resolves an undecided question, so neither was taken. | Tree listing @ `4e65829a` |
| P00.2 purge tracked bytecode | EXECUTED | Deps: none. Blockers: none. Neutrality: mechanical hygiene; `.gitignore` already excludes `__pycache__/` and `*.py[cod]`. 25 tracked `.pyc` files enumerated (7 in `tests/__pycache__/`, 10 in `tools/compiler/fcos/__pycache__/`, 8 in `tools/compiler/fcos/models/__pycache__/`) and removed, one commit per file. | commits `f33e14ea`…`6ae0086a` (25) |
| P00.3 rename `writter.py` → `writer.py` | EXECUTED | Deps: none. Blockers: none. Neutrality: content byte-identical. Importer check: the import lists of `compiler.py`, `generator.py`, `parser.py` were read directly — none import `writter`; the tracked `__pycache__` (a complete record of the last test run) contains no `writter` bytecode, so no module imported it at runtime either; code search returned zero references but flagged an incomplete index, so manual inspection was treated as primary evidence. | commits `1a69f555`, `3de1d1f4` |
| P00.4 delete merged branches | NOT EXECUTABLE BY AGENT | Available tooling has no branch-deletion capability. Maintainer console action. | — |
| P00.5 README layout | VERIFIED — NO CHANGE | Corrected in PR #14; re-verified at `4e65829a`. | — |

### P01 — CI and mechanical checks

| Package | Disposition | Verification summary | Evidence |
| --- | --- | --- | --- |
| P01.1 CI workflow | EXECUTED | Deps: none (`.github/workflows/` was empty). Blockers: none. Neutrality: encodes only already-accepted artifacts — RFC-0011 disposition E-A (per ADR-0004) and Constitution Article 9; gates apply identically to all contributors (L-5 / INV-19). Python 3.11 + pytest chosen from repository evidence (existing bytecode metadata: CPython 3.11, pytest 9.1.1), not preference. | commit `d860edf5` |
| P01.2 internal link check | EXECUTED | Standard-library, mechanical-only (L-10). Scans `README.md`, `docs/`, `specs/`; excludes `specs/fcos/` (neutrality under B-11). | commit `704fc756` |
| P01.3 governance ID check | EXECUTED | Same frame. Verifies `ADR-XXXX`/`RFC-XXXX` mentions map to files in `docs/decisions/` / `docs/rfc/`; checks existence only — never status, disposition, or content. | commit `704fc756` |
| P01.4 check tests + docs | EXECUTED | Fixture tests (`tests/test_check_links.py`, `tests/test_check_ids.py`) and `tools/checks/README.md` documenting L-10 scope. | commit `704fc756` |
| P01.5 enforce required status checks | NOT EXECUTABLE BY AGENT | Repository settings (Maintainer console). Suggested required checks: “Prototype and tooling tests”, “Documentation gates (links, IDs)”. | — |
| P01.6 close no-CI risk | PENDING P01.5 | Risk PR-03 stays open until required checks are enforced on `main`. | — |

### P02 — Knowledge sync

| Package | Disposition | Verification summary | Evidence |
| --- | --- | --- | --- |
| P02.1 sync runbook | EXECUTED | One-way repository→mirror procedure per L-9 / INV-9. No sync was executed from branch state. | this commit |
| P02.2 full mirror sync | DEFERRED | Executes only after this PR merges: the mirror reflects `main` only. | — |

### P11 — Testing

| Package | Disposition | Verification summary | Evidence |
| --- | --- | --- | --- |
| P11.1 wire tests into CI | EXECUTED | See P01.1. | commit `d860edf5` |
| P11.2 testing conventions | EXECUTED | Restates INV-4 and the prototype quarantine (L-7); defines mechanical conventions only. | this commit |
| P11.3 traceability convention | EXECUTED (recorded, not yet consumable) | Clause-identifier naming per RFC-0002 dispositions N-B/N-C; usable only after specifications ratify. No test may claim to verify a specification clause today. | this commit |
| P11.4 performance testing | BLOCKED (B-10) | No ratified performance requirement exists; adding a benchmark would resolve governance through code. | — |

### P12 — Conformance

| Package | Disposition | Verification summary | Evidence |
| --- | --- | --- | --- |
| P12.1 conformance frame note | EXECUTED (minimal) | Restates only the RFC-0004 frame accepted in ADR-0004 (L-A + C-A) and INV-16; deliberately does not duplicate S13, which is In Review. | this commit |
| P12.2+ harness / fixtures / judgments | BLOCKED | G-SPEC(S13), B-08 — there are no ratified clauses to judge against. | — |

### P13 / P15

| Package | Disposition | Verification summary | Evidence |
| --- | --- | --- | --- |
| P13 documentation gates frame | SATISFIED VIA P01 | Mechanical link/ID gates now run in CI. Behavior-level documentation checks remain gated with their subsystems. | commits `704fc756`, `d860edf5` |
| P15 standing obligations | STANDING — NO NEW ARTIFACT | No ratified source defines an additional pre-D-01 mechanical check (for example, an AI-disclosure linter is not ratified anywhere); implementing one would invent policy. Gate equality (INV-19 / L-5) is already encoded in the CI workflow. | — |

## 3. New blocker record — B-11

**B-11 — `specs/fcos/` content disposition.** `specs/fcos/` contains ~40 legacy specification documents; the P00.1 premise (“empty scaffold”) is false. Whether this content is deleted, archived, or adopted is a Maintainer decision. Until decided: P00.1 must not execute, and the mechanical documentation checks exclude `specs/fcos/` from scanning (scanning would presume the tree is governed documentation; deleting would presume the opposite). This blocker is registered here rather than by editing the PROGRAM.md blocker register (B-01…B-10), so that the plan amendment itself receives Maintainer review together with this PR; on acceptance the register should be amended to include B-11.

## 4. Governance-neutrality statement

No ADR, RFC, constitution, architecture, or specification file was created or modified in this wave. No undecided question — D-01 identity, RFC-0014, RFC-0015, S13 ratification, performance requirements, `specs/fcos/` disposition — is resolved or implicitly narrowed by any change here. All behavior encoded in CI derives from already-ratified or already-accepted artifacts (RFC-0011 E-A per ADR-0004; Constitution Article 9; L-5, L-10, INV-19).

## 5. Known verification gap (disclosed)

The check scripts and their tests were authored without local execution; the first CI run on this pull request is their verification run. If the link/ID checks report findings on pre-existing documentation, those are true findings to be triaged — not check defects — and the checks must not be weakened in response within this PR.
