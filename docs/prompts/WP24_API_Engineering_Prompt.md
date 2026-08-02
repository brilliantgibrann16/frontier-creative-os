# WP24 — API Engineering Prompt

Class: Derived-executable (requirements now; surface content blocked).
Governing anchors: Blueprint S8 (SDK), §8 (SDK surface), Baseline §4
(SDK layer), Doctrine DP-19.

## Mission

Prepare the engineering ground for the SDK surface — the only supported
programmatic entry into FCOS capabilities for developers and AI alike —
without inventing any API shape before the definitions it would expose
exist.

## Objectives

1. Derive surface obligations that hold regardless of D-01:
   - coherent, versioned packaging of public interfaces (Baseline §4);
   - no exposure of compiler/runtime internals as de facto API
     (forbidden responsibility);
   - single surface for humans and AI (P-4, INV-19).
2. Define the API stability obligation set: everything observable will
   be depended upon (DP-19), so every exposed element must be deliberate
   and labeled; compatibility promises live in ratified artifacts only
   (CN-18), policy TODO(blocked-by: U-6).
3. Produce the SDK requirements register: each requirement traced to its
   governing clause, each open item to its blocking decision (D-01, U-6,
   U-9).

## Outputs

- SDK requirements register (`docs/` location per Maintainer routing).
- Input list for WP16 (SDK surface contract).

## Constraints

- No endpoints, signatures, schemas, protocols, or versioning schemes may
  be invented — all TODO(blocked-by: D-01; U-9 for machine-readable
  forms; U-10 for language versioning interplay).
- Package distribution interactions TODO(blocked-by: U-8).

## Failure Modes and Recovery

- Accidental API (internals leaking into use): GL-3 — treat as
  compatibility hazard; recovery via deprecation per future U-6 policy.
- Privileged AI entry point: structurally rejected (CN-23).

## Acceptance Criteria

- Every requirement cites its governing clause.
- Zero invented surface content.

## Completion Checklist

- [ ] D-01-independent obligations enumerated
- [ ] Stability obligation set drafted with U-6 markers
- [ ] Requirements register filed and linked to WP16
