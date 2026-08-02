# S11 — Package Manager Subsystem Specification

**Status:** In Review · **Subsystem:** S11 (Blueprint §2, "necessity UNKNOWN") · **Date:** 2026-08-02

## Scope

**BLOCKED at the existence level** — missing: whether FCOS needs a
package manager at all; blocked by: RFC-0007 (U-8), which recommends
recording N-defer inside RFC-0001's acceptance ADR; unblock: that ADR.

S11 is the only subsystem whose existence is conditional (Blueprint §2).
This specification therefore fixes only the bounds that would bind any
future package manager, so that no interim work forecloses the decision.

## Responsibilities

Conditional obligations (bind if and only if S11 is adopted):

- Naming, versioning, distribution, resolution of packages — and nothing
  semantic: the package manager never changes what resolved code means
  (Baseline §4 forbidden responsibility).
- Package identity respects the ratified identifier scheme (RFC-0002)
  and versioning scheme (RFC-0009) — both TODO(blocked-by: acceptance
  ADRs).

## Interfaces

Package registry boundary: "conditional on D-01. UNKNOWN" (Blueprint
§8). **BLOCKED** — same citation as Scope.

## Data model

Frame from the artifact universe (Blueprint §7): package lifecycle
Published → yanked/superseded; published packages presumed immutable
with yank-as-status (RFC-0007 open question 1). All schemas: **BLOCKED**.

## API contracts

**BLOCKED** — same citation.

## State machines

Specifiable frame: Package: Published → (Superseded | Yanked); no
deletion state exists — yanking is a status, not removal. Further
content: **BLOCKED**.

## Sequence flows

**BLOCKED** — same citation.

## Error model

**BLOCKED** — same citation.

## Security requirements

Bound (binds any future S11): supply-chain trust — signing, provenance,
namespace publishing rights — must be specified before the first package
is published, per RFC-0007's open questions. Content: **BLOCKED**.

## Performance budgets

**BLOCKED** — same citation.

## Observability requirements

**BLOCKED** — same citation.

## Testing requirements

**BLOCKED** — same citation.

## Acceptance criteria

- Zero package infrastructure exists before U-8 is recorded as decided.
- If N-no is recorded: this spec is Deprecated and S11 retired via the
  Baseline §13 path.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Conditional existence | Blueprint §2 (S11), §14 U-8 |
| Necessity framing | RFC-0007 (acceptance pending) |
| No semantic authority | Baseline §4 |
| Lifecycle bound | Blueprint §7 (package row) |
