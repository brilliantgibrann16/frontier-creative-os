# S5 — Compiler Subsystem Specification

**Status:** In Review · **Subsystem:** S5 (Blueprint §2, "Not begun") · **Date:** 2026-08-02

## Scope

Translation of source artifacts into build artifacts, diagnostics, and
optimization — under total specification authority (A4). The Phase 0
prototype pipeline is historical context only and is outside this spec
(L-7). Implementation work is gated: G-5, G-7, G-8 of the readiness
report are unmet.

## Responsibilities

- Realize ratified specifications exactly; divergence is a compiler
  defect by definition (L-2, INV-3).
- Emit diagnostics that report and never rule (Blueprint §6).
- Optimize only within spec-observable equivalence (L-3; optimization
  envelope per the WP29 prompt).
- Forbidden: defining behavior; private semantic contracts with the
  runtime (L-11, INV-11).

## Interfaces

Compiler boundary per Blueprint §8: invocation, input acceptance,
artifact emission, diagnostics contract. All four: **BLOCKED** — missing:
ratified interface specifications; blocked by: RFC-0001 (D-01) and first
S4 specs; unblock: post-identity interface RFCs/specs.

## Data model

**BLOCKED** — missing: source model, artifact formats, symbol/IR models;
blocked by: RFC-0001; unblock: ratified S4 specs. (Recording any format
now would let the compiler define the language, INV-3.)

## API contracts

**BLOCKED** — missing: programmatic surface (if any; may be S8-mediated);
blocked by: RFC-0001 + S8 SDK spec; unblock: those decisions.

## State machines

Specifiable frame: per-invocation lifecycle Accepted-input → Diagnosed
(≥0 diagnostics) → (Artifacts-emitted | Failed). Semantic states:
**BLOCKED** by missing pipeline spec (which phases exist is
identity-dependent).

## Sequence flows

Frame only: invocation → input validation against ratified grammar →
diagnosis → artifact emission → exit status. Every step’s content:
**BLOCKED** by RFC-0001.

## Error model

Specifiable obligations: every rejection cites the violated ratified
clause (traceable diagnostics, INV-17 corollary); internal errors are
distinguishable from program errors; no diagnostic asserts behavior the
spec does not define. Diagnostic taxonomy: **BLOCKED** — missing: ratified
diagnostics contract; blocked by: RFC-0001 + tooling-contract spec (U-9
adjacent); unblock: those specs.

## Security requirements

Compiler processes untrusted input (user source): it must not execute
source content during translation unless a ratified spec defines such a
phase; resource exhaustion on malicious input is a defect class.
Concrete hardening requirements: **BLOCKED** pending interface specs.

## Performance budgets

**BLOCKED** — missing: any ratified performance requirement; blocked by:
RFC-0001 (identity determines workload shape; benchmark methodology per
WP27 is methodology-only by DP-8); unblock: post-identity benchmark spec.

## Observability requirements

Obligation frame: diagnostics are the primary surface; a conforming
compiler’s observable behavior must be fully explainable by ratified
clauses (no oracle behavior). Metrics/tracing requirements: **BLOCKED**
pending interface specs.

## Testing requirements

Two-suite discipline (S12/S13): implementation test suite (evidence,
zero authority, INV-4) + conformance suite judgment (INV-16). A test
contradicting the spec is the defect (L-4). Concrete tests: **BLOCKED**
— missing: ratified clauses; unblock: first S4 spec + suite skeleton.

## Acceptance criteria

- No compiler work begins before G-5/G-7/G-8 close (readiness report).
- At first release: 100% of shipped behavior traceable to ratified
  clauses (INV-17); conformance suite passes; R-4 posture (RFC-0006 R-A
  recommendation — no reference-implementation authority) upheld.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Spec supremacy | Baseline P-1, L-2, L-3; INV-2, INV-3 |
| No lateral contracts | L-11; INV-11 |
| Prototype exclusion | L-7; INV-7 |
| Gating | IMPLEMENTATION_READINESS_REPORT (G-5, G-7, G-8); CN-14 |
| Implementation policy | RFC-0006 (acceptance pending) |
