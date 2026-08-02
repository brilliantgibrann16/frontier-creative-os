# S12 — Testing Subsystem Specification

**Status:** In Review · **Subsystem:** S12 (Blueprint §2) · **Date:** 2026-08-02

## Scope

Correctness evidence for implementations: per-implementation test suites
and the testing discipline they follow. Excludes: conformance judgment
(S13 — the judge is a different subsystem by construction) and defining
any behavior (INV-4).

The existing prototype tests (6/6 passing) are historical context only
(L-7) and carry no obligations into this spec.

## Responsibilities

- Produce evidence, never authority: a test contradicting a ratified
  spec is itself the defect (L-4, INV-4).
- Maintain the two-suite architecture: implementation test suites (S12,
  evidence) strictly separate from the conformance suite (S13, judge).
- Trace tests to ratified clauses where they assert specified behavior
  (CN-9); unclause-traced tests are permitted only as internal evidence
  and make no behavior claims.

## Interfaces

- **CI execution surface:** suites run under CI per RFC-0011 E-A
  (TODO(blocked-by: acceptance ADR for RFC-0011)); results are the sole
  admissible release evidence (Blueprint §9).
- Harness form: **BLOCKED** — missing: implementation languages/build
  shapes (identity-dependent); blocked by: RFC-0001; unblock: S5–S7 work.

## Data model

- **Test case:** ID, target implementation, clause references (≥0),
  expected result derivation (from clause, never from implementation
  observation — the anti-"lock in current behavior" rule).
- **Test run:** suite version, implementation version, environment,
  results — retained as evidence.

## API contracts

Not applicable — S12 publishes no programmatic surface; its contract is
the evidence format above, concretized when harnesses exist (**BLOCKED**
as in Interfaces).

## State machines

**Test case:** Proposed → Active → (Retired | Quarantined). Quarantine
is for spec-disagreement investigation: a failing test either reveals an
implementation defect (stays Active, bug filed) or contradicts the spec
(test is the defect, L-4 — Retired with cause recorded).

## Sequence flows

1. **Disagreement protocol (L-4/DP-9):** test fails → compare against
   ratified clause → implementation defect (fix code) XOR test defect
   (fix test) XOR clause ambiguity (file spec Issue → RFC path; neither
   code nor test "wins" in the meantime — quarantine).
2. **Coverage flow:** new ratified clause → conformance test in S13 +
   implementation tests here as needed → CN-9 closure check.

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Test asserts unspecified behavior | clause-trace audit | retire or re-scope test |
| Flaky test | run-history variance | quarantine; flakiness is evidence pollution |
| Suite green on defective implementation | conformance suite disagreement | S13 judgment prevails; S12 gap filed |

## Security requirements

Test code runs in CI with no access to publishing credentials or
governed-artifact write paths; evidence is append-only.

## Performance budgets

No ratified requirements exist. **BLOCKED** — missing: any ratified
suite-runtime requirement; blocked by: none pending; unblock: engineering
decision when suites exist.

## Observability requirements

Every release-gating run reproducible from recorded suite/implementation/
environment versions; pass-rate and quarantine-count reported per cycle.

## Testing requirements

(Meta-tests.) Mechanical: clause references resolve; no Active test
references a Deprecated clause without a filed migration Issue;
quarantine list has an owner Issue per entry. Encoding:
TODO(blocked-by: acceptance ADR for RFC-0011).

## Acceptance criteria

- Two-suite separation observable in repository layout and CI config.
- 100% of behavior-asserting Active tests are clause-traced (CN-9).
- Disagreement protocol followed in every recorded spec-vs-test conflict.
- Prototype tests remain clearly segregated as historical (L-7).

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Evidence, not authority | INV-4; L-4; Doctrine DP-9 |
| Two-suite architecture | Baseline §10; INV-16; WP26 prompt |
| Clause traceability | CN-9 |
| CI evidence rule | Blueprint §9 (Testing ↔ Release) |
| Prototype exclusion | L-7; INV-7 |
