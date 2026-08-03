# Delivery Strategy

**Artifact class:** Implementation Plan (delivery) — no decision authority.
All rules below restate or operationalize already-ratified law; nothing here
creates policy.

## 1. Branch strategy

- `main` is protected and authoritative. Direct commits to `main` are
  prohibited; the one historical exception (ADR-0001) was explicitly
  recorded and is not precedent (INV-20).
- All work happens on feature branches, one WBS package per branch, named
  by area:
  - `docs/*` — documentation and planning artifacts
  - `specs/*` — specification work (P03, P06…)
  - `ci/*` — P01/P14 gate encoding
  - `impl/<subsystem>/*` — implementation programs (P04+), opened only
    after the program's entry gate passes
  - `governance/*` — reserved for Maintainer-directed governance work only
- Branches are short-lived: branch → PR → merge → delete (deletion is a
  manual Maintainer action; tracked as P00 hygiene).
- Never commit DRAFT documents; work enters review as In Review.

## 2. Merge strategy

- Every change merges via pull request into `main`; squash-merge is the
  established convention (single reviewable unit per package; clean
  history).
- Merge preconditions, in order: (1) mechanical gates green (P01, once
  live — required checks per RFC-0011 E-A); (2) independent review — AI
  authors never self-approve (L-5, INV-19); (3) Maintainer decision where
  the change is decision-adjacent (Article 6/7).
- Every PR body must state: WBS package ID(s), governing artifacts cited,
  blockers touched (none may be silently disposed), and the per-PR
  self-review disclosure where author and reviewer roles overlap
  (ADR-0004, J.4 note).
- Cross-PR ordering dependencies are declared in the PR body (precedent:
  PR #12's merge-order dependency on PR #11).
- No bulk-rewrite PRs; minimal targeted diffs only.

## 3. Release strategy

- **Article 9 is absolute:** no release before CI gates are live and green
  (G-CI). CI results are the sole admissible release evidence; overrides
  require a recorded one-time exception (INV-20).
- **Interim state (now):** no language versions exist pre-1.0 (RFC-0009
  V-D, ADR-0004); compatibility guarantees are limited to the interim
  instability window (RFC-0005, ADR-0004). Therefore: **no public releases
  are planned in Waves 0–3.** Document versioning (Baseline MAJOR.MINOR)
  continues independently.
- **First release (Wave 4):** gate-checked publication of ratified content
  with test evidence (P11) and conformance judgment (P12); immutable
  release notes. The full versioning and compatibility policies must be
  decided post-G-D01 and recorded as ADRs before any versioned language
  release.
- Releases are superseded, never silently unpublished.

## 4. Testing strategy

- Tests are **evidence, never definition** (INV-4, L-4): a test
  contradicting a ratified spec is the defect.
- Layers: (1) unit tests — implementation-internal; (2) spec-derived tests
  — keyed to clause IDs (RFC-0002 scheme, post-P03); (3) conformance-facing
  fixtures feeding P12.
- Every PR runs the full mechanical gate set; no merge on red.
- Test traceability: spec-derived tests name their clause IDs so coverage
  is machine-checkable against the clause index (RFC-0008 M-B).
- Performance testing is **blocked** — no ratified quantitative requirement
  exists anywhere (B-10); budgets arrive only via ratified specs, never
  via invented numbers.

## 5. Verification strategy

- One implementation-independent conformance judge for all implementations
  (INV-16), operating the accepted RFC-0004 frame (L-A + C-A); levels are
  future work per ADR-0004 and will not be improvised.
- The judge's authority is delegated from ratified specifications (L-4);
  prose remains authoritative over the clause index and any generated
  artifacts (RFC-0008 M-B guard).
- The suite is versioned with the spec clauses it judges (Blueprint §7);
  suite corrections supersede, never silently edit.
- Official conformance judgments require S13 ratification (G-SPEC(S13));
  until then P12 outputs are engineering signals only.
- Implementations never gain conformance status by negotiation with the
  judge — spec changes travel the RFC → ADR path (INV-2).

## 6. Escalation

Any conflict between this strategy and a ratified artifact resolves in the
ratified artifact's favor, and the discrepancy is fixed here by PR. Any
needed rule that does not exist yet is a blocker routed to the RFC → ADR
path — never improvised in delivery.
