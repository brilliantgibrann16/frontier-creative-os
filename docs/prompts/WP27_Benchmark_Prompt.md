# WP27 — Benchmark Prompt

Class: Derived-executable (methodology only). Governing anchors: Doctrine
DP-8 (implementation quality competes on what the specification does not
fix), Baseline §4 (Language Specification forbidden responsibilities
include performance), L-3, L-4.

## Mission

Define the benchmarking methodology for FCOS implementations — the rules
under which performance is measured, compared, and reported — without
inventing workloads for a language that does not yet exist.

## Objectives

1. Position benchmarking architecturally: performance is implementation-
   quality territory (DP-8); specifications do not define it and
   benchmarks never acquire gate authority over meaning.
2. Define methodology requirements that are D-01-independent:
   - reproducibility: environment, inputs, and harness versioned and
     re-runnable (deterministic orchestration, Baseline §4 Build System);
   - comparability: identical workloads and conformance status for any
     cross-implementation comparison (only conforming implementations
     are comparable — a fast non-conforming implementation is a defect,
     L-2);
   - honesty: results reported with configuration and variance; no
     marketing-form claims (Constitution style rules).
3. Define the benchmark/conformance separation: benchmark suites are
   evidence of quality, never of correctness; they may not substitute
   for the conformance suite (INV-16) or define behavior (L-4).
4. Workload definitions: TODO(blocked-by: D-01, ratified specifications,
   and existing implementations).

## Outputs

- Benchmark methodology document (Implementation Plan class).
- Requirements input to WP25 (metric definitions) and WP28 (release
  reporting).

## Constraints

- No performance targets, workloads, or harness tooling may be invented
  now.
- Benchmark results never gate ratification of any specification; they
  may inform implementation plans only.

## Failure Modes and Recovery

- Benchmark-driven semantics (optimizing meaning into the spec):
  illegal reverse flow; recovery is revert-until-RFC.
- Unreproducible claims: results without versioned harness are invalid
  and withdrawn.

## Acceptance Criteria

- Methodology complete, D-01-independent, with all workload content
  marked TODO.
- Separation from conformance stated and consistent with INV-16.

## Completion Checklist

- [ ] Methodology document drafted
- [ ] Reproducibility requirements defined
- [ ] Conformance/benchmark separation documented
- [ ] Workload TODOs carry blocking decisions
