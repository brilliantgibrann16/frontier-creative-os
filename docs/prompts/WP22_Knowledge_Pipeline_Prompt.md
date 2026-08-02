# WP22 — Knowledge Pipeline Prompt

Class: Derived-executable. Governing anchors: Blueprint S3 (Knowledge
System), S14 (Documentation System), Baseline L-9, Doctrine §8 (CN-15,
CN-16, GL-7, GL-8, DP-16, DP-17).

## Mission

Engineer the pipeline that keeps derived knowledge — the workspace mirror,
registers, and documentation — faithful to the authoritative repository,
mechanically and in one direction only.

## Objectives

1. Define the mirror synchronization procedure: repository → workspace,
   one-way (L-9); conflicts always resolve toward the repository.
2. Define register maintenance: Decision Register, Risk Register,
   Operations Log, unknowns registry (Blueprint §14) — update triggers,
   owners, and staleness detection.
3. Define documentation derivation: which documents are regenerated from
   ratified sources (GL-8) vs hand-maintained, and the fidelity check
   (every behavior claim traceable to a ratified clause, CN-16).
4. Specify traceability tooling requirements: machine-checkable chains
   (DP-12) — requirements only; tool selection is
   TODO(blocked-by: U-12 / engineering decision).

## Inputs

- Blueprint §7 artifact universe (lifecycle column); Baseline §6–§7.
- Current workspace structure (Engineering Operations page, registers).

## Outputs

- Knowledge pipeline procedure document (Implementation Plan class,
  Baseline §8 category 5 — no RFC required).
- Staleness/consistency checklist for the maintenance cadence.

## Constraints

- The knowledge system records decisions and never constitutes them
  (Baseline §4, L-8).
- No knowledge tool may become a hard dependency of correctness; the
  repository must always suffice for reconstruction (CN-15).
- Documentation is never citable as authority (CN-16).

## Data Flow

Repository (authoritative) → sync → workspace mirror → human consumption.
Feedback: workspace observations → filed Issues → forward pass. No other
reverse edge exists; "mirror authority" is a named illegal flow
(Baseline §7).

## Failure Modes and Recovery

- Mirror divergence: assumed stale; mechanical re-sync from repository.
- Register rot: staleness detection at maintenance cadence; owner
  TODO(blocked-by: maintenance cadence decision, Pending).
- Shadow specification via documentation: deletion or ratification.

## Acceptance Criteria

- Every sync path is one-way with the repository as source.
- Every register has an update trigger and a staleness check.
- Zero authority claims in any derived artifact.

## Completion Checklist

- [ ] Sync procedure documented and exercised once
- [ ] Register maintenance table complete
- [ ] Derivation vs hand-maintenance classification done
- [ ] Traceability tooling requirements filed (tool choice deferred)
