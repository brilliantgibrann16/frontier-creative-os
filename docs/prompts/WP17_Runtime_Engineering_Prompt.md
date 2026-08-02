# WP17 — Runtime Engineering Prompt

Class: RFC-first. Governing anchors: Blueprint S6 (Runtime — status "not
begun; required scope UNKNOWN"), U-14, Baseline §4 (Runtime layer), L-2,
L-11.

## Mission

Prepare the decision material that makes runtime engineering possible.
S6 exists in the ratified decomposition, but its necessity and scope are
UNKNOWN (U-14) because they follow from the language identity decision
D-01. No runtime may be designed or implemented before that resolution
(CN-14: no unknown may be resolved by shipping behavior that presumes an
answer).

## Objectives

1. Produce the runtime section of the D-01 decision material: for each
   candidate language identity in the D-01 design space, state what
   execution services would be required, without choosing.
2. Draft the S6 scope RFC skeleton: questions the RFC must answer
   (execution model ownership, spec-declared services, embedding
   requirements), each mapped to its deciding artifact.
3. Define the conformance obligations any future runtime inherits from
   Baseline §10 (implementation row) regardless of D-01 outcome.

## Inputs

- Blueprint S6, U-1, U-14; Baseline §4 (Runtime responsibilities and
  forbidden responsibilities), §10, §12 (Runtime, Execution, Behavior).
- Decision Register entry D-01.

## Outputs

- Runtime scope analysis attached to the D-01 decision material.
- S6 scope RFC skeleton (questions only, no answers).
- Runtime conformance obligations note (derivable now).

## Constraints

- Never invent execution models, memory models, scheduling, or runtime
  APIs — all TODO(blocked-by: D-01, then spec RFCs).
- A runtime realizes spec-declared services and never extends semantics
  (Baseline §4); no feature unavailable to other conforming runtimes.
- Compiler↔runtime interaction only via spec-defined contracts (L-11).

## Dependencies

D-01 (blocking) → U-14 resolution → execution-model RFCs → runtime
specifications → implementation plan → code.

## Failure Modes and Recovery

- Premature runtime prototyping becoming precedent: forbidden by L-7;
  recovery is reclassification as historical context.
- Runtime-defined semantics: illegal reverse flow (bug canonization);
  recovery is fix-toward-spec, always (L-2).

## Acceptance Criteria

- Zero design choices made; every open point carries its blocking
  decision.
- Conformance obligations stated in D-01-independent form.

## Completion Checklist

- [ ] D-01 runtime analysis delivered (design space, no choices)
- [ ] S6 scope RFC skeleton filed as Issue
- [ ] Conformance obligations note reviewed against Baseline §10
- [ ] TODO(blocked-by: D-01) markers on all deferred content
