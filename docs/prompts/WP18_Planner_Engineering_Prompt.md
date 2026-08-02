# WP18 — Planner Engineering Prompt

Class: RFC-preparation. Status: **BLOCKED — subsystem not in ratified
architecture.**

TODO(blocked-by: new-subsystem RFC → Baseline amendment → adoption ADR,
per Blueprint §13 and Baseline §13).

## Mission

A "Planner" subsystem does not exist in the ratified Blueprint
decomposition (S1–S16) and is not implied by the Architecture Baseline.
This prompt therefore directs exactly one thing: production of the RFC
that would introduce it — or a recorded decision not to.

## Objectives

1. State the engineering need a Planner would serve, traced to filed
   Issues or the Decision Register — not asserted (Baseline §10,
   RFC necessity proof).
2. Position the candidate subsystem: proposed stratum, owner,
   responsibilities, forbidden responsibilities, boundaries (CN-3).
3. Enumerate authority implications: which boundary of Blueprint §4 it
   sits under; confirm no upward authority edge is created (INV-13,
   CN-27 acyclicity).
4. Enumerate the unknowns it depends on (at minimum D-01: whether the
   language identity implies any execution-planning function at all).

## Outputs

- RFC draft `docs/rfc/` proposing the subsystem, or a recorded
  recommendation to reject, with rationale either way.
- Baseline amendment sketch (layer placement) attached to the RFC.

## Constraints

- No planner architecture, algorithms, data structures, or interfaces may
  be designed before adoption (CN-14; L-6: presence of this file grants
  no standing).
- The RFC must pass the Baseline §8 routing questions and Doctrine §16
  consistency checks.

## Acceptance Criteria

- The necessity case cites real, filed needs; zero invented requirements.
- All authority/dependency edges shown acyclic against Blueprint §3–§4.

## Completion Checklist

- [ ] Necessity evidence gathered from Issues/Decision Register
- [ ] RFC draft or rejection recommendation written
- [ ] Baseline amendment sketch attached
- [ ] Blocking decisions listed (D-01 at minimum)
- [ ] Routed to Maintainer decision (Article 6/7)
