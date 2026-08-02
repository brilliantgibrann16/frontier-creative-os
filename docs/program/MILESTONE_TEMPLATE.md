# Milestone Template

**Artifact class:** Implementation Plan (template) — no decision authority.
Every program milestone MUST use this template in full. Empty fields are
invalid; a field whose information does not exist yet must contain a
`Blocked-by:` entry naming the governing artifact.

---

```markdown
# Milestone <Program>-M<n>: <name>

**Program:** P<nn> — <program name> (subsystem S<n>)
**Status:** Planned | In Progress | Blocked | Done | Voided
**Owner:** <role — authority is positional, INV-15>

## Objective
One sentence. What is true when this milestone is done that is not true now.

## Entry criteria
- Gates that must already be passed (e.g. G-D01, G-CI, G-SPEC(Sxx)),
  each with its current state.
- Upstream milestones/WBS packages that must be Done.

## Work packages
- WBS IDs in scope (P<nn>.<k> …), one branch + PR per package.

## Required decisions
- ADRs this milestone depends on (existing: cite; missing: Blocked-by).
- Decisions this milestone must NOT presume (list explicitly if adjacent
  to an open unknown — Blueprint §14).

## Specification dependencies
- Ratified clauses/sections built against, by ID. In-Review specs may be
  cited as obligations only, never as binding (B-08).

## Test evidence
- Suites/fixtures that prove the milestone; clause IDs covered
  (spec-derived tests); evidence is never definition (INV-4).

## Acceptance gate
- The mechanical + review gates that must be green to declare Done
  (CI checks, conformance judgment, Maintainer sign-off where
  decision-adjacent).

## Exit criteria
- Observable, binary statements. No “mostly”.

## Traceability
- Constitution/Baseline/ADR/RFC/spec citations for every normative claim
  this milestone relies on.

## Rollback
- Exact revert/supersession path if the milestone must be undone
  (ratified artifacts supersede, never edit — INV-18).

## Disclosure
- Author/reviewer roles; AI attribution; per-PR self-review disclosure
  where roles overlap (ADR-0004, J.4 note).

## Blockers touched
- Blocker register IDs (B-xx) this milestone consumes, waits on, or
  surfaces. Milestones never dispose blockers — only ADRs do (INV-8).
```

---

## Usage rules

1. Milestones are proposed by PR adding a file under the owning program's
   planning area; they carry no authority until their acceptance gate is
   defined and reviewable.
2. A milestone that would require inventing missing information is invalid
   by construction — split it: unblocked part proceeds, blocked part waits
   on its governing artifact.
3. Voided milestones (e.g. P05 if U-14 resolves to “no runtime”) are closed
   with a record, never deleted.
