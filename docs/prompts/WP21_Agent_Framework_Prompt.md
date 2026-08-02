# WP21 — Agent Framework Prompt

Class: RFC-preparation. Status: **BLOCKED — subsystem not in ratified
architecture; hard doctrine bounds apply.**

TODO(blocked-by: new-subsystem RFC → Baseline amendment → adoption ADR,
per Blueprint §13; scope interaction with S16 must be resolved first).

## Mission

The ratified architecture contains an AI Layer (S16) whose defining
property is the **absence of a special interface**: AI participates
through exactly the same public interfaces and gates as humans
(Baseline P-4, INV-19, Blueprint §8). An "Agent Framework" — dedicated
infrastructure for AI actors — is not in the decomposition and sits close
to the most protected constraints in the corpus. This prompt directs
preparation of the introducing RFC under those bounds.

## Objectives

1. Scope analysis: determine whether the proposed capability is (a) S16
   consumption tooling using existing public interfaces — which needs no
   new subsystem — or (b) genuinely new infrastructure — which needs the
   Blueprint §13 path.
2. Constraint compliance analysis, mandatory sections:
   - CN-23: no AI-only channel into rank 1–5 artifacts, regardless of
     demonstrated reliability. The RFC must prove the framework creates
     none.
   - INV-19: identical gates for human and AI contributions.
   - L-5 / INV-5: nothing in the framework may let AI output reach
     authoritative artifacts outside the human decision path.
   - Blueprint §9 trust boundary: AI output untrusted until human review;
     no self-approval.
3. Necessity, placement, and authority-edge analysis per the WP18
   pattern.

## Constraints

- No agent architectures, orchestration designs, prompt formats, or
  tool protocols before adoption (CN-14).
- Any design granting AI privileged access is structurally rejected
  before its merits are argued (CN-27 analogue: constraint check precedes
  design review).

## Acceptance Criteria

- The (a)/(b) scope question is answered with evidence.
- Every CN-23/INV-19/L-5 obligation has an explicit compliance argument.

## Completion Checklist

- [ ] Scope analysis (S16 tooling vs new subsystem) recorded
- [ ] Constraint compliance section complete
- [ ] Necessity evidence gathered
- [ ] Introduction RFC draft or rejection recommendation
- [ ] Routed to Maintainer decision
