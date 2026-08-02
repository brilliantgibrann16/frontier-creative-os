# Implementation Readiness Report

**Class:** Derived review artifact — informative, zero authority.
**Date:** 2026-08-02 · **Question:** may FCOS begin implementation?

## Verdict

**NOT READY. 0 of 8 readiness gates are met.**

"Implementation" here means production code embodying language or
subsystem semantics — the thing CN-14 guards: code written before
decisions ratify resolves unknowns by accident, and under R-4 the first
implementation silently becomes the specification. It does *not* mean
repository hygiene, CI workflow files, documentation tooling, or
maintenance of the Phase 0 prototype (historical status, L-7).

## Readiness gates

| # | Gate | Source | Status |
| --- | --- | --- | --- |
| G-1 | Review legitimacy: governance procedure ratified (RFC-0010), J.4 neutralized | Article 6, OB-4 | ✗ NOT MET |
| G-2 | Identifier scheme frozen (RFC-0002) so specs/tests/clauses are traceable from birth | CN-9, DP-12 | ✗ NOT MET |
| G-3 | Single unambiguous specification home (RFC-0003) | AX-1, F-3 | ✗ NOT MET |
| G-4 | Article 9 gate mechanically enforced: CI exists (RFC-0011) | Article 9, Risk Register | ✗ NOT MET (`.github/workflows/` empty) |
| G-5 | **Language identity decided (RFC-0001 / D-01)** — the controlling gate | U-1, R-1 | ✗ NOT MET |
| G-6 | Compatibility posture declared (interim rule from RFC-0005/0009) so no accidental promises form | OB-6, CN-18 | ✗ NOT MET |
| G-7 | At least one ratified specification exists for the component being implemented | P-1, L-2, CN-14 | ✗ NOT MET (no spec corpus) |
| G-8 | Conformance judge frame exists (RFC-0004 frame + suite skeleton) before code claims correctness | INV-16 | ✗ NOT MET |

Gate logic: G-7 and G-8 are per-component and permanent (every future
component re-passes them); G-1…G-6 are one-time project gates.

## Critical path to readiness

1. **Merge PR #11, then PR #12** (artifacts currently exist only on
   branches; nothing is decidable from `main` as it stands).
2. **One governance sitting:** roadmap Steps 1–9 → closes G-1, G-2,
   G-3, G-4 (posture; workflows follow as hygiene PRs), G-6, and the
   RFC-0004 frame half of G-8.
3. **The identity summit:** RFC-0001 acceptance ADR (with RFC-0012 and
   the RFC-0007 review inside it) → closes G-5. This is the only gate
   that cannot be scheduled — it takes the deliberation it takes.
4. **Specification authoring** (S4 work; authoring, not implementation)
   under RFC-0005/0009 decisions → first ratified spec closes G-7.
5. **Conformance suite skeleton** traced to that spec's clauses →
   closes G-8. Implementation of that component may then begin, subject
   to the RFC-0006 posture (no implementation acquires authority).

## What is permitted today (while NOT READY)

- Prototype maintenance and its tests (historical, L-7; constrains nothing).
- Repository hygiene: merged-branch deletion, tracked `__pycache__`
  removal, `writter.py` rename, issue templates.
- CI workflow files per RFC-0011 E-A once accepted (tests + link/ID
  checks) — tooling for gates, not semantics.
- Documentation work: WP16 contracts inventory, WP22 traceability
  register work, Notion mirror synchronization (L-9).
- All governance work in the roadmap.

## Risk summary

- **Highest risk:** beginning implementation before G-5 (identity by
  accident, R-1 Critical) or before G-7/G-8 (compiler-is-the-spec, R-4
  Critical). Both are irreversible in practice once external consumers
  observe behavior (OB-6).
- **Lowest-cost wins available now:** Steps 1–9 are one sitting and
  close five gates.
- **Schedule honesty:** no date is offered for G-5; per the Maintainer's
  standing ruling the identity is designed collaboratively, and this
  report treats deliberation time as a feature, not a delay.

## Standing review

This report is point-in-time. Re-issue after each roadmap step, or at
minimum after Step 9 and after Step 10, so the verdict tracks the gate
table rather than memory.
