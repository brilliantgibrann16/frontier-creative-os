# Architecture Documents

This directory holds the architectural reference documents of Frontier
Creative OS (FCOS). These documents sit directly beneath the Constitution
in the artifact hierarchy.

## Documents

| Document | Role | Authority |
| --- | --- | --- |
| [`baseline.md`](./baseline.md) | Architecture Baseline — structure, boundaries, and law (WHAT) | Normative (rank 2, beneath the Constitution) |
| [`blueprint.md`](./blueprint.md) | Master System Blueprint — whole-system description (WHAT IT IS) | Descriptive only |
| [`doctrine.md`](./doctrine.md) | Universal Engineering Doctrine — axioms and rationale (WHY) | Explanatory only |
| [`stage2_behavior.md`](./stage2_behavior.md) | FSL Stage 2 Behavior & Architecture Guide (P13.3) | Informative / Explanatory Reference |

## Precedence

In any normative conflict:

```
Constitution  >  Architecture Baseline  >  Blueprint  >  Doctrine
```

The Blueprint and Doctrine never override the Baseline. The Baseline never
overrides the Constitution.

## Status

All documents in this directory carry an explicit `Status` header.
Per Constitution Article 7, no document here is binding until its adoption
is recorded as an ADR. Documents with `Status: Proposed` are candidates
awaiting an adoption ADR.

## Amendment

Ratified architecture documents are amended only by the forward pass:
RFC → ADR → pull request approved by the Maintainer and merged into `main`.
Superseded rules are struck with a pointer to their replacement; history is
never rewritten.

## Scope guarantee

Nothing in this directory defines language syntax, keywords, grammar,
semantics, memory, concurrency, or execution behavior. Every decision that
would do so is recorded as UNKNOWN with an owning future decision
(see `blueprint.md`, section "Future Unknowns").