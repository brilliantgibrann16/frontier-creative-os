# S6 — Runtime Subsystem Specification

**Status:** In Review · **Subsystem:** S6 (Blueprint §2, scope UNKNOWN) · **Date:** 2026-08-02

## Scope

**Scope decided: S-B** — a validation-evaluation runtime (U-14
resolved inside the RFC-0001 acceptance ADR per RFC-0012’s routing:
ADR-0006, Decision 2; Baseline L-3 stands — zero defining authority).
Runtime content remains **BLOCKED** — missing: the S-B boundary drawn
as specification clauses ("the boundary between the
validation-evaluation runtime and S13 conformance tooling must be
drawn precisely in specification work" — ADR-0006, Decision 2);
blocked by: ratified S04 Stage 0 clauses (P03); unblock: that
specification work.

Everything specifiable independent of the remaining boundary work is
recorded below; every other section is blocked with the same citation.

## Responsibilities

Conditional obligations (bind if and only if a runtime exists):

- Provide only spec-declared execution services (Blueprint §2);
  observable behavior fully spec-defined (L-2).
- Hold zero defining authority (A4; INV-2).
- Interact with the compiler exclusively through spec-defined contracts
  (L-11, INV-11); no private semantic agreements.

## Interfaces

Runtime embedding boundary exists as an architectural placeholder
(Blueprint §8) “required only if D-01 yields an executed language.”
**BLOCKED** — missing: all interface content; blocked by: the S-B
boundary specification work above (S-B decided — ADR-0006, Decision 2).

## Data model

**BLOCKED** — same citation. (Any state model implies an execution model,
which implies the identity decision.)

## API contracts

**BLOCKED** — same citation.

## State machines

**BLOCKED** — same citation.

## Sequence flows

**BLOCKED** — same citation.

## Error model

Obligation frame only: if a runtime exists, error surfaces are
spec-classified (defined/implementation-defined/unspecified/undefined —
Baseline §10), and runtime failures are contained to one runtime
(Blueprint §11). Content: **BLOCKED** — same citation.

## Security requirements

Obligation frame only: a runtime executing untrusted programs is a trust
boundary and must be specified as one before implementation. Content:
**BLOCKED** — same citation.

## Performance budgets

**BLOCKED** — missing: any ratified requirement; blocked by:
RFC-0001/RFC-0012; unblock: post-identity specs.

## Observability requirements

**BLOCKED** — same citation.

## Testing requirements

Frame: same two-suite discipline as S5 (INV-4, INV-16, L-4). Content:
**BLOCKED** — same citation.

## Acceptance criteria

- No runtime work of any kind before RFC-0012’s resolution is recorded.
- If S-A (no runtime) is chosen: this spec is Deprecated with a successor
  pointer and S6 is retired via the Baseline §13 amendment path — an
  architecture change this spec cannot itself perform.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Scope unknown | Blueprint §2 (S6), §14 U-14 |
| Design space | RFC-0012 (acceptance pending) |
| Contract discipline | L-11; INV-11 |
| Containment | Blueprint §11 |
| No implicit resolution | Blueprint §14 closing rule; CN-14 |
