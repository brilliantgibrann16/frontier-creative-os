# Agent Contribution Conventions

**Artifact class:** Implementation Plan (conventions) — carries **no decision
authority** (Blueprint §7). This document restates ratified law for
day-to-day use and creates no policy, gate, or mechanical check. If it
conflicts with any ratified artifact, the ratified artifact wins.
**Program:** P15 — AI Layer (S16) · Work package P15.1
**Owner:** Maintainer (Article 6)

---

## 1. Principle: no special interface

The AI layer is architecturally defined as the **absence** of a special
interface (Baseline P-4; INV-19). Agents produce and consume project
artifacts through exactly the channels humans use — branches, pull
requests, reviews, issues, and recorded decisions. No AI-only channel,
contract, or shortcut may exist (Blueprint trust boundaries).

## 2. One contribution path

feature branch → pull request → independent review → mechanical gates
(CI) → Maintainer merge.

- Branch names follow `DELIVERY_STRATEGY.md`: `docs/*`, `specs/*`,
  `ci/*`, `impl/<subsystem>/*`, `governance/*`.
- The unit of assignment is the work package: one package → one branch
  → one PR, citing the WBS package ID (`IMPLEMENTATION_STRATEGY.md`).
  Any bundling deviation is disclosed in the PR body for Maintainer
  judgment.
- Never commit directly to `main`. Exceptions are Maintainer-recorded
  one-time events (INV-20; ADR-0001 precedent).
- Never commit DRAFT documents. Never merge without a PR.

## 3. Review and approval

- No self-approval and no self-merge (L-5). Merge authority rests with
  the Maintainer (Article 6).
- Identical gates: an AI-authored PR passes exactly the checks a
  human-authored PR passes (INV-19). Gates are mechanical and never
  decide policy (L-10, INV-10).

## 4. Per-PR disclosure duties

Every agent-authored PR body must:

1. Disclose AI authorship/involvement (ADR-0004, J.4 note).
2. Include a self-review disclosure: known limitations, verifications
   not executed, and any deviation from plan or convention.
3. Carry a zero-invention statement when the PR touches planning,
   governance-adjacent, or specification-adjacent artifacts.

## 5. Blocker protocol

Missing information is never invented. When required information does
not exist in a ratified or accepted artifact, the agent records
`Blocked-by:` with the governing artifact and continues with unblocked
work (`IMPLEMENTATION_STRATEGY.md`). Blockers are disposed only by ADRs
(Article 7, INV-8) — never by PR descriptions, code comments, or this
document.

## 6. Content boundaries

- Ratified and accepted artifacts are never edited in place;
  corrections travel by supersession (INV-18).
- Governance is never resolved through code or documentation (INV-8,
  L-8; Blueprint §14: no unknown is resolved implicitly).
- Prototype quarantine: `tools/compiler/fcos/` is historical context
  only — never a starting point, precedent, or semantic authority
  (L-7, INV-7).
- The Engineering Prompt library `docs/prompts/` (artifact class
  ratified by ADR-0003) changes only via PR.
- No bulk rewrites: changes are minimal and targeted; unrelated content
  is left byte-identical.

## 7. Attribution

Every agent contribution is attributable: the PR is the attribution
surface and names the agent involvement (J.4); commit history remains
the implementation record of truth. The repository is authoritative;
the knowledge mirror is one-way derived (L-9, INV-9).

## Traceability

| Convention | Governing source |
| --- | --- |
| No special AI interface | Baseline P-4; INV-19 |
| One path; PR-only; no direct `main` commits | Constitution workflow rules; INV-20 |
| No self-approval / self-merge | L-5; Article 6 |
| Mechanical gates, never policy | L-10; INV-10; RFC-0011 E-A (ADR-0004) |
| Per-PR disclosure duties | ADR-0004 (J.4 note) |
| Blocker protocol | Article 7; INV-8 |
| Supersession, no in-place edits | INV-18 |
| Prototype quarantine | L-7; INV-7 |
| Prompt library maintenance | ADR-0003 |
| Repository authoritative, mirror derived | L-9; INV-9 |
