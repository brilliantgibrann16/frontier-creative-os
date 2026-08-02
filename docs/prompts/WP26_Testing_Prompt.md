# WP26 — Testing Prompt

Class: Derived-executable. Governing anchors: Blueprint S12/S13, Baseline
§10 (Conformance Model), §5 (L-4), §9 step 5, Doctrine §5 (DP-9, CN-9),
ADR-0001 context.

## Mission

Engineer the testing architecture of FCOS: the permanent separation
between implementation test suites (evidence for one implementation) and
the conformance suite (the implementation-independent judge), and the
path from ratified clauses to traceable tests.

## Objectives

1. Define the two-suite architecture and its ownership: unit/integration
   suites live with each implementation (S12); the conformance suite is a
   separate artifact derived clause-by-clause from ratified
   specifications (S13, Baseline §10).
2. Define clause traceability: every normative clause carries at least
   one traceable test ID before its behavior ships (CN-9); specify the
   ID scheme requirement — scheme itself TODO(blocked-by: D-03).
3. Define the disagreement protocol: when test and spec disagree, the
   test is wrong by definition (L-4); the discrepancy is filed as an
   Issue; the only appeals are mistraced clause (fix test) or wrong
   clause (amend spec via forward pass) (DP-9).
4. Define conformance levels/classes placeholder:
   TODO(blocked-by: D-04 / U-5).
5. Current-repo action: classify the existing prototype tests as
   evidence for the specification-document pipeline (prototype) only —
   historical context, zero semantic authority (L-7).
6. Recommend the binding of the tests-before-implementation ordering
   (Baseline §9 step 5 note): requires an ADR to bind; prepare that
   ADR's decision material.

## Outputs

- Testing architecture document (routes per Baseline §8; the two-suite
  separation is already Baseline law, so this is category-5 work).
- ADR decision material for the test-first ordering.
- Issue filings for any current-repo test hygiene findings.

## Constraints

- Tests never define semantics (INV-4); no test may ship behavior not
  traceable to a ratified clause (INV-17).
- The conformance suite must be runnable against any implementation — no
  implementation-specific hooks (INV-16).
- No test frameworks or harness designs selected before implementations
  exist — TODO(blocked-by: D-01 and implementation plans).

## Failure Modes and Recovery

- Evidence tampering (adjusting tests to pass): named illegal reverse
  flow; recovery is revert + Issue.
- Conformance suite fork per implementation: violates INV-16;
  structurally rejected.

## Acceptance Criteria

- Two-suite separation stated with owners and judges.
- Disagreement protocol complete and Issue-routed.
- All deferred choices carry blocking-decision markers.

## Completion Checklist

- [ ] Testing architecture document drafted
- [ ] Clause-to-test traceability requirement specified (D-03 marker)
- [ ] Disagreement protocol documented
- [ ] Prototype tests classified as historical evidence
- [ ] Test-first ADR decision material prepared
