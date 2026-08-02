# S13 — Verification & Conformance Subsystem Specification

**Status:** In Review · **Subsystem:** S13 (Blueprint §2, model defined; suite not begun) · **Date:** 2026-08-02

## Scope

The judgment machinery: the conformance suite, conformance claims, and
the rules by which an implementation is declared conforming. The model
is ratified (Baseline §10); the suite content is blocked.

## Responsibilities

- Serve as the sole judge of conformance (INV-16); no implementation,
  test suite, or maintainer opinion substitutes.
- Derive every suite test from a ratified clause — the suite tracks the
  spec, never any implementation (L-4; forbidden dependency Blueprint §3:
  S13 must not depend on implementations).
- Administer the conformance-claim regime: binary conformance,
  self-certification (RFC-0004 recommendations L-A + C-A;
  TODO(blocked-by: acceptance ADR for RFC-0004)).

## Interfaces

- **Conformance harness boundary** (Blueprint §8): how the suite drives a
  candidate implementation. Form: **BLOCKED** — missing: harness contract
  ("UNKNOWN"); blocked by: RFC-0001 + S4/S5 interface specs; unblock:
  those ratifications.
- **Claim surface:** published statement per implementation: suite
  version + result. Format concretized with RFC-0004's acceptance.

## Data model

- **Suite test:** ID, ratified clause reference (mandatory, exactly the
  CN-9 discipline), category of the clause tested, expected result
  derived from clause text.
- **Conformance claim:** implementation + version, suite version, verdict
  (binary: conforming / not conforming — no partial levels pre-decision,
  RFC-0004 L-A), certification mode (self, C-A).

## API contracts

Not applicable beyond the harness boundary (**BLOCKED** above); the claim
format is a document contract, fixed at RFC-0004 acceptance.

## State machines

- **Suite version:** tracks spec ratifications — new/amended clauses →
  new suite version in the same decision cycle (S4 spec sequence flow 2).
- **Claim:** Asserted → (Standing | Invalidated by suite-version
  supersession or discovered divergence). Claims are never edited;
  re-certification issues a new claim.

## Sequence flows

1. **Judgment:** candidate + suite version → full run → binary verdict →
   claim published with evidence retained.
2. **Divergence discovery:** implementation passes suite but diverges
   from a clause → suite gap (file suite defect; implementation still
   defective by L-2 — suite passage is necessary, not sufficient, until
   the gap closes).

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Suite test not clause-traced | mechanical audit | remove or trace; untraced judgment is invalid |
| Suite encodes implementation behavior | review vs clause text | suite defect (L-4); rewrite from clause |
| Conflicting claims | claim registry audit | later suite version prevails; older claim marked superseded |

## Security requirements

Suite integrity: suite content changes traverse the full PR path;
self-certification (C-A) requires retained, reproducible evidence so
claims are auditable — trust is in the evidence, not the claimant.

## Performance budgets

No ratified requirements exist. **BLOCKED** — missing: any ratified
suite-runtime bound; blocked by: none pending; unblock: engineering
decision when the suite exists.

## Observability requirements

Public registry of claims (suite version × implementation); per-clause
coverage figure published with each suite version; CN-9 exceptions
explicitly listed.

## Testing requirements

(Meta.) Mechanical: 100% of suite tests carry resolving clause
references; suite version monotonically tracks spec ratifications; no
suite test references implementation internals. Encoding:
TODO(blocked-by: acceptance ADR for RFC-0011). Suite content itself:
**BLOCKED** — missing: ratified clauses; blocked by: RFC-0001; unblock:
first S4 ratification.

## Acceptance criteria

- Suite exists before any implementation release claim (readiness gate
  G-8 closure path).
- Every claim in the registry is binary, versioned, evidence-backed.
- Zero suite tests derived from implementation observation at audit.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Sole judge | INV-16; Baseline §10 |
| No implementation dependency | Blueprint §3 (S13 forbidden deps); L-4 |
| Binary + self-cert | RFC-0004 (acceptance pending) |
| Clause traceability | CN-9 |
| Harness unknown | Blueprint §8 |
