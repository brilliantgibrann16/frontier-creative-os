# WP25 — Observability Prompt

Class: Derived-executable (cross-cutting practice, not a subsystem).
Governing anchors: Baseline §4 (Testing/CI responsibilities), §10
(evidence), Blueprint §9 (Testing ↔ Release trust boundary), U-12.

## Mission

Define what must be observable across FCOS engineering so that every gate
decision rests on mechanical evidence — without introducing a telemetry
subsystem, which does not exist in the ratified decomposition and would
require the Blueprint §13 path.

## Objectives

1. Evidence observability: CI results are the sole admissible evidence at
   the release boundary (Blueprint §9); define the evidence retention and
   audit-trail requirements. Platform encoding
   TODO(blocked-by: U-12).
2. Diagnostics observability: implementations report and never rule
   (Blueprint §6); define the requirement that diagnostics be contract-
   governed (input to WP16), content TODO(blocked-by: D-01).
3. Process observability: change rates per authority rank are an
   architectural alarm metric (DP-20, GL-10); define the measurement.
4. Traceability observability: orphan detection, trace closure, and
   ⊑-acyclicity checks as mechanically runnable audits (Doctrine §13).

## Outputs

- Observability requirements document (Implementation Plan class).
- Metric definitions: rank change rates, unknown count (DP-32), trace
  closure percentage.

## Constraints

- No monitoring stack, telemetry protocol, or dashboard tooling may be
  selected here — TODO(blocked-by: U-12 and ordinary engineering
  decisions at implementation time).
- Observation never becomes authority: metrics inform proposals; they
  decide nothing (AX-2, DP-26).
- No end-user or program-level telemetry is implied anywhere in the
  ratified corpus; proposing it would be a new-subsystem RFC.

## Failure Modes and Recovery

- Gate erosion via unrecorded overrides: named illegal flow; recovery is
  the recorded one-time exception mechanism (INV-20).
- Metric gaming replacing judgment: metrics are GL-class inputs, never
  gates by themselves (CN-11).

## Acceptance Criteria

- Every observability requirement names its consuming gate or audit.
- Zero tooling selections; zero new subsystems.

## Completion Checklist

- [ ] Evidence requirements defined for the release boundary
- [ ] Diagnostics contract requirements handed to WP16
- [ ] Rank change-rate metric defined
- [ ] Traceability audit checks specified for future CI (U-12 marker)
