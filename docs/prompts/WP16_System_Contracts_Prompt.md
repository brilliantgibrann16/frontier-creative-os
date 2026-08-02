# WP16 — System Contracts Prompt

Class: Derived-executable. Governing anchors: Blueprint §8 (Interface
Universe), Baseline §4 (communication paths), §5 (L-11), §6.

## Mission

Produce contract definition documents for the architectural boundaries
enumerated in Blueprint §8, so that every inter-subsystem effect traverses
a published contract (DP-3, CN-3).

## Objectives

1. For each boundary in Blueprint §8, produce one contract document
   stating: parties, direction of authority, obligations of each side,
   what the contract deliberately does not cover.
2. Classify each contract as specifiable-now vs blocked, with the
   blocking decision named.
3. Propose the ratification route for each (RFC → Specification, per
   Baseline §8 category 3/4).

## Inputs

- Blueprint §8 boundary list; Baseline §4 layer contracts; Doctrine §3.
- Accepted ADRs.

## Outputs

- `docs/rfc/` drafts (one per specifiable contract) or a consolidated
  contracts RFC — Maintainer routing choice.
- A contract register table (boundary, status, blocking decision).

## Constraints

- No protocol, serialization format, wire format, or API shape may be
  invented (Blueprint §8: all forms UNKNOWN until specified).
- No lateral semantic contracts between implementations (L-11).
- The AI interface is the absence of a special interface (P-4, CN-23);
  no contract may create one.
- Contracts bind only after ratification (L-8).

## Boundary worklist (from Blueprint §8)

| Boundary | Status |
| --- | --- |
| Repository interface (branches, PRs, protected main) | Specifiable now (document current enforced rules) |
| Knowledge interface (repo → mirror, one-way) | Specifiable now (L-9) |
| Governance review surface | Specifiable now (Constitution-derived) |
| Conformance harness boundary | Specifiable after D-04/U-5 |
| Specification → machine contract | TODO(blocked-by: U-9) |
| Compiler boundary (invocation, diagnostics) | TODO(blocked-by: D-01) |
| Syntax-tree / tooling contract | TODO(blocked-by: D-01, grammar RFCs) |
| Compiler ↔ runtime boundary | TODO(blocked-by: D-01, U-14) |
| Runtime embedding boundary | TODO(blocked-by: D-01, U-14) |
| SDK surface | TODO(blocked-by: D-01) |
| Package registry boundary | TODO(blocked-by: D-01, U-8) |

## Failure Modes and Recovery

- Contract drift (implementation behavior treated as contract): illegal
  reverse flow (Baseline §7); recovery is revert-until-RFC.
- Shadow contracts in documentation: CN-16; recovery is deletion or
  ratification, never tolerance.

## Acceptance Criteria

- Every Blueprint §8 boundary appears exactly once: contract draft or
  TODO with blocking decision.
- Zero invented formats or protocols.
- Every draft names its governing specification-to-be and its judge.

## Completion Checklist

- [ ] Contract register complete against Blueprint §8
- [ ] Specifiable-now contracts drafted as RFC inputs
- [ ] All blocked contracts carry TODO(blocked-by: …)
- [ ] Consistency check against L-11, P-4, INV-19 passed
- [ ] Filed as Issue(s) and routed per Baseline §8
