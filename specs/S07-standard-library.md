# S7 — Standard Library Subsystem Specification

**Status:** In Review · **Subsystem:** S7 (Blueprint §2, scope UNKNOWN) · **Date:** 2026-08-02

## Scope

Ratified, specified shipped capabilities of the language. Scope content:
**BLOCKED** — missing: what capabilities a stdlib provides (wholly
identity-dependent); blocked by: RFC-0001 (D-01); unblock: acceptance ADR
+ S4 specs.

## Responsibilities

Binding obligations independent of identity:

- **Stdlib honesty (Baseline P-5):** every shipped capability is
  specified; nothing ships as “library magic” exempt from the conformance
  model. A stdlib capability without a ratified clause is a violation,
  not a feature.
- Stdlib behavior is judged by the same conformance suite as everything
  else (INV-16); stdlib code holds zero defining authority.

## Interfaces

**BLOCKED** — missing: all surface content; blocked by: RFC-0001.

## Data model

**BLOCKED** — same citation.

## API contracts

**BLOCKED** — same citation. (The stdlib’s API *is* language surface;
specifying any of it now would define language content outside S4.)

## State machines

**BLOCKED** — same citation.

## Sequence flows

**BLOCKED** — same citation.

## Error model

Obligation frame: stdlib error surfaces are spec-classified like all
language behavior (Baseline §10). Content: **BLOCKED** — same citation.

## Security requirements

Obligation frame: capabilities with security character (if any) require
explicit ratified clauses before shipping; P-5 forbids undocumented
privileged behavior. Content: **BLOCKED** — same citation.

## Performance budgets

**BLOCKED** — missing: any ratified requirement; blocked by: RFC-0001.
Note: if performance characteristics are ever promised, they become
spec-observable surface under the compatibility policy (RFC-0005) — a
decision, not a default.

## Observability requirements

**BLOCKED** — same citation.

## Testing requirements

Frame: clause-traced conformance tests per capability (CN-9); two-suite
discipline (INV-4, INV-16). Content: **BLOCKED** — same citation.

## Acceptance criteria

- Zero stdlib work before ratified S4 clauses exist for the capability.
- At any release: 100% of shipped stdlib capabilities have ratified
  clauses (P-5 audit); no capability exists only in code.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Stdlib honesty | Baseline P-5 |
| Scope unknown | Blueprint §2 (S7); U-1/D-01 |
| Conformance parity | INV-16; Baseline §10 |
| Compatibility interaction | RFC-0005 (acceptance pending) |
