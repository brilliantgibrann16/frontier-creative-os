# WP29 — Optimization Prompt

Class: Derived-executable (methodology only). Governing anchors: Baseline
§4 (Compiler: optimization within spec-observable equivalence), L-3,
Blueprint §11 (compiler bug containment), Doctrine GL-3, DP-19.

## Mission

Define the rules under which any future FCOS implementation may optimize:
the permanent envelope that keeps optimization subordinate to specified
meaning — before any optimizer exists and without designing one.

## Objectives

1. State the optimization envelope from ratified text: an implementation
   may transform anything so long as observable behavior remains within
   spec-defined territory (conformance as set containment, Doctrine
   §13); optimization never defines or extends behavior (L-3).
2. Define the labeled-territory rule: optimizations may exploit
   implementation-defined / unspecified / undefined labels only as the
   ratified specification assigns them; label application to any language
   area is TODO(blocked-by: D-01 and future spec RFCs).
3. Define the evidence obligation: every optimization claim is backed by
   conformance-suite green plus benchmark methodology (WP27); a
   speedup that changes observable behavior is a defect, not a win.
4. Define the accidental-guarantee hazard: optimized behavior that users
   can observe will be depended upon (DP-19, GL-3); treat optimization
   stability as a compatibility concern under the future U-6 policy.

## Outputs

- Optimization policy document (Implementation Plan class).
- Requirements input to WP26 (conformance evidence) and WP27
  (measurement).

## Constraints

- No optimization algorithms, passes, IR designs, or heuristics may be
  designed now — TODO(blocked-by: D-01, semantics RFCs, compiler
  implementation plans).
- The prototype pipeline's optimizer is historical context only (L-7)
  and constrains nothing.

## Failure Modes and Recovery

- Optimizer-canonized behavior (users depending on transformed
  semantics): bug canonization flow; recovery is fix-toward-spec (L-2).
- Benchmark-driven meaning drift: see WP27 failure modes.

## Acceptance Criteria

- Envelope statement fully cited to ratified clauses.
- Zero designed optimization content.

## Completion Checklist

- [ ] Optimization envelope documented
- [ ] Labeled-territory rule stated with blocking markers
- [ ] Evidence obligations linked to WP26/WP27
- [ ] Compatibility hazard noted under U-6
