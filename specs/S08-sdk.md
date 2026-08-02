# S8 — SDK Subsystem Specification

**Status:** In Review · **Subsystem:** S8 (Blueprint §2, "Not begun") · **Date:** 2026-08-02

## Scope

The versioned public developer interfaces: the only supported
programmatic entry into FCOS capabilities for end developers and AI alike
(Blueprint §8). This spec fixes obligations and lifecycle; the concrete
surface is blocked.

## Responsibilities

- Publish versioned, documented interfaces; consumers depend on nothing
  else (delivery boundary A5).
- Uniform surface for human and AI consumers (P-4, INV-19): no AI-only
  entry points.
- Never expose implementation internals (S5–S7) directly; the SDK is a
  contract layer, not a tunnel.

## Interfaces

Concrete surface: **BLOCKED** — missing: which capabilities exist to
expose (identity-dependent) and the tooling contracts they ride on;
blocked by: RFC-0001 (D-01) and S4/S5 interface specs; unblock: those
ratifications.

## Data model

- **Interface version:** every public surface carries a version;
  consumer-observable change is a decision-level event (Blueprint §13
  interface evolution).
- Payload/entity models: **BLOCKED** — same citation as Interfaces.

## API contracts

Contract *rules* (binding now): stability per the compatibility policy
(RFC-0005; interim rule: pre-1.0, no stability guarantees —
TODO(blocked-by: acceptance ADR for RFC-0005)); deprecation is a status
with successor pointer, never silent removal. Contract *content*:
**BLOCKED** — same citation as Interfaces.

## State machines

**Interface lifecycle:** Proposed → Published(vN) → Deprecated(vN, with
successor) → Removed only per ratified deprecation policy (policy content
TODO(blocked-by: acceptance ADR for RFC-0005)).

## Sequence flows

Frame: capability ratified (S4–S7) → SDK surface proposed (RFC path if
consumer-observable) → published with version → consumed → evolved by
decision-level events only. Content: **BLOCKED** as above.

## Error model

Obligation: every SDK error is part of the published contract —
undocumented error behavior is a defect (OB-6: consumers depend on every
observable behavior). Taxonomy: **BLOCKED** pending surface definition.

## Security requirements

Uniform authentication/authorization posture for human and AI consumers
(INV-19); no capability reachable via SDK that bypasses gates governing
the same action elsewhere. Concrete mechanisms: **BLOCKED** pending
surface definition.

## Performance budgets

**BLOCKED** — missing: any ratified requirement; blocked by: RFC-0001;
unblock: post-identity specs. If budgets are ever published they become
promised surface (RFC-0005 interaction) — a decision, not a default.

## Observability requirements

Obligation: versioned surfaces must make consumer-visible deprecation
status discoverable. Metrics: **BLOCKED** pending surface definition.

## Testing requirements

Contract tests per published interface version (evidence class, INV-4);
compatibility tests across supported versions once RFC-0005's policy is
recorded. Content: **BLOCKED** pending first published surface.

## Acceptance criteria

- No SDK surface published before the capability it exposes is ratified.
- Every published surface versioned, documented, and covered by contract
  tests at publication.
- Zero AI-only or human-only entry points at any audit.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Sole programmatic entry | Blueprint §8 (SDK surface) |
| Uniformity | Baseline P-4; INV-19 |
| Interface evolution | Blueprint §13 |
| Stability | RFC-0005 (acceptance pending); DP-19; CN-18; OB-6 |
| Delivery boundary | Blueprint §4 (A5) |
