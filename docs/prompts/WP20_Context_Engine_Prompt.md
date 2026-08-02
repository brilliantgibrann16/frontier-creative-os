# WP20 — Context Engine Prompt

Class: RFC-preparation. Status: **BLOCKED — subsystem not in ratified
architecture.**

TODO(blocked-by: new-subsystem RFC → Baseline amendment → adoption ADR,
per Blueprint §13).

## Mission

A "Context Engine" does not exist in the ratified Blueprint (S1–S16), is
not implied by the Baseline, and no ratified artifact defines the term.
Per L-12 (vocabulary is binding) the first obligation is definitional:
an RFC introducing this subsystem must define "context" as a new term —
existing ratified vocabulary (Baseline §12) does not contain it.

## Objectives

1. Define the candidate term precisely enough to survive Baseline §12
   vocabulary review.
2. Establish necessity from filed needs (RFC necessity proof, Baseline
   §10). If the need is actually served by an existing subsystem (S3
   Knowledge, S14 Documentation, S16 AI Layer), record that finding and
   recommend rejection — subsystem duplication violates INV-14 (one
   purpose per artifact) at the subsystem level.
3. If necessity survives: produce the introduction RFC per the WP18
   pattern.

## Constraints

- No engine architecture, retrieval strategies, storage design, or
  interfaces before adoption (CN-14).
- Overlap analysis against S3/S14/S16 is mandatory before any proposal.

## Acceptance Criteria

- Term defined or proposal rejected for vagueness; no undefined
  vocabulary ships (CN-6 analogue for architecture documents).
- Overlap analysis complete against the ratified decomposition.

## Completion Checklist

- [ ] Vocabulary definition drafted
- [ ] Overlap analysis vs S3, S14, S16 recorded
- [ ] Necessity evidence or rejection recommendation
- [ ] Introduction RFC draft (only if necessity survives)
