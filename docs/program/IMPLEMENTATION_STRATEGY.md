# Implementation Strategy

**Artifact class:** Implementation Plan (strategy) — no decision authority.

## 1. Execution principles

1. **Spec-first, always.** No production code may realize behavior that is
   not traceable to a ratified specification clause (INV-17). Ratification
   of the governing spec sections is therefore the first work package of
   every implementation program (B-08).
2. **Event-gated, never date-based.** Programs open when gates pass
   (decisions recorded, specs ratified, CI green) — never on a calendar.
   This plan contains no dates by design.
3. **Decisions are not engineering.** The critical path starts at G-D01, a
   Maintainer decision. Engineering effort cannot substitute for it, and no
   program may presume its outcome (Blueprint §14 rule: no unknown is
   resolved implicitly by shipping behavior).
4. **Blocker protocol.** When required information is missing: do not
   invent; record `Blocked-by:` with the governing artifact (RFC, ADR,
   Blueprint section); continue with all unblocked work. Blockers are
   disposed only by ADRs (Article 7, INV-8) — never by this plan, a PR
   description, or a code comment.
5. **Authority flows downward only** (INV-13). Feedback from
   implementation, testing, or consumption enters as new Issues → RFCs at
   the top — never as in-place edits to ratified artifacts.
6. **Prototype quarantine.** The Phase 0 pipeline under
   `tools/compiler/fcos/` is historical context only; it is never a
   starting point, precedent, or design constraint (L-7, INV-7).
7. **Identical gates for humans and AI** (P-4, INV-19). One contribution
   path: feature branch → PR → review → mechanical gates → merge. AI never
   self-approves (L-5) and carries a per-PR self-review disclosure duty
   (ADR-0004).
8. **No bulk rewrites.** Changes are minimal and targeted; wholesale
   rewrites of existing artifacts are prohibited by standing rule.
9. **Immutability by supersession.** Ratified/accepted artifacts are never
   edited in place; corrections supersede (INV-18).
10. **Incremental delivery.** Small PRs, frequent commits, every commit
    leaves the repository consistent and CI-green.

## 2. Wave model

Execution proceeds in gate-separated waves (full graph in
`DEPENDENCY_GRAPH.md`):

- **Wave 0 — now:** everything D-01-independent: P00, P01, P02, P11,
  P12(frame), P13(frame), P15. Purpose: when G-D01 passes, nothing
  infrastructural delays Wave 1.
- **Gate G-D01:** the Maintainer decides RFC-0001; the acceptance ADR also
  resolves U-14 (RFC-0012) and opens the RFC-0005/0007/0009 decision
  windows.
- **Wave 1:** P03 — meaning production. Clause index (P03.4) is scheduled
  early because P12's full suite consumes it.
- **Wave 2:** P04 (+P05 if it exists, P06) against ratified clauses, with
  P12 judging.
- **Wave 3:** P07/P08/P09 against published contracts; P10 only if decided.
- **Wave 4:** P14 first gate-checked release (Article 9).
- **Standing lanes:** P00 hygiene, P02 sync, P13 docs, P15 AI conventions
  run continuously and never block a wave.

## 3. Staffing model (dozens of engineers and agents)

- **Roles, not headcount:** author (human or AI), independent reviewer,
  Maintainer (terminal decision authority, Article 6). Authority is
  positional, never personal (INV-15).
- **Current reality:** one Maintainer plus AI agents. The plan therefore
  keeps every wave executable by a small set of streams, and scales by
  adding parallel streams — not by changing the process (Blueprint §10:
  the contribution path is uniform for contributor #1 and #500).
- **Parallelism is contract-bounded.** Streams parallelize only across
  ratified contracts or independent files. Adding agents before contracts
  exist produces review-queue congestion, not progress.
- **Review capacity is the scaling bottleneck.** RFC-0010 (accepted, G-D +
  cooling rule) provides the governance procedure for growing beyond a
  single Maintainer when that bottleneck binds.
- **Work assignment unit:** the WBS package. One package → one branch → one
  PR, citing the package ID and, where applicable, clause IDs.

## 4. What this plan may never do

- Decide anything (no ADR authority).
- Modify governance, architecture, RFCs, or specifications.
- Start a blocked package by inventing the missing input.
- Create programs for rejected candidates (Planner, Agent Framework) or
  undecided candidates (Memory, Context Engine) — ADR-0004.
- Generate production code (planning artifact only).
