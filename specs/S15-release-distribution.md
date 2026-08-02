# S15 — Release & Distribution Subsystem Specification

**Status:** In Review · **Subsystem:** S15 (Blueprint §2, "Not begun; blocked by CI") · **Date:** 2026-08-02

## Scope

Producing and distributing releases of FCOS deliverables. Constitutionally
gated: no production release without CI (Constitution Art. 9), and no CI
exists yet (`.github/workflows` empty; RFC-0011 unaccepted). This spec
fixes the gate structure; channels and packaging are blocked.

## Responsibilities

- Enforce the release gate chain (below); CI results are the sole
  admissible evidence at the Testing ↔ Release trust boundary
  (Blueprint §9) — no unrecorded human override.
- Version releases per the ratified versioning policy (RFC-0009 interim
  V-D: no language version pre-1.0; TODO(blocked-by: acceptance ADR for
  RFC-0009)).
- Distribute only built-and-manifested artifacts (S10) — never ad-hoc
  binaries.

## Interfaces

Distribution channels: **BLOCKED** — missing: what is released
(identity-dependent) and whether packages exist (U-8/RFC-0007); blocked
by: RFC-0001, RFC-0007; unblock: those ADRs.

## Data model

- **Release record:** version, artifact manifests (S10), CI evidence
  reference, conformance claim reference (S13), gate checklist, recorded
  approver.
- Channel/package schemas: **BLOCKED** as above.

## API contracts

**BLOCKED** — same citation as Interfaces.

## State machines

**Release:** Proposed → Gates-passing → Published → (Superseded |
Withdrawn-by-status). Published releases are immutable; a bad release is
superseded or status-marked, never deleted.

## Sequence flows

**Gate chain (specifiable now):** ratified specs exist for shipped
behavior (INV-17) → S10 deterministic build + manifest → S12 suites
green in CI → S13 conformance claim (once suite exists; gate G-8) →
version assigned per policy → release record committed → publication.
Any gate failure halts the chain; overrides require a recorded exception
(INV-20).

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Release without CI evidence | release-record audit | constitutional violation (Art. 9); withdraw by status; recorded incident |
| Artifact without manifest | record audit | rebuild through S10; never patch in place |
| Version policy violation | mechanical check | supersede with corrected version |

## Security requirements

Publishing credentials separated from CI test execution (S12 security
rule); artifact provenance chain (S10 manifest → release record)
verifiable end-to-end; signing requirements **BLOCKED** pending
RFC-0007's trust decisions.

## Performance budgets

No ratified requirements exist. **BLOCKED** — missing: any ratified
release-cadence/latency requirement; blocked by: none pending; unblock:
future decision if needed.

## Observability requirements

Every release fully reconstructable from its release record; public
release index; gate-failure log retained.

## Testing requirements

Mechanical: release records complete (all fields); every published
artifact’s manifest resolves; no Published release lacks CI evidence.
Encoding: TODO(blocked-by: acceptance ADR for RFC-0011).

## Acceptance criteria

- Zero production releases before CI exists (Art. 9 — currently
  trivially satisfied: none have occurred).
- First release, whenever it comes, passes the full gate chain with a
  complete release record.
- All eight readiness gates (IMPLEMENTATION_READINESS_REPORT) closed
  before any implementation release.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| CI-before-release | Constitution Art. 9; Blueprint §2 (S15 blocked-by) |
| Trust boundary | Blueprint §9 (Testing ↔ Release) |
| Versioning | RFC-0009 (acceptance pending) |
| CI shape | RFC-0011 E-A (acceptance pending) |
| Shipped-behavior traceability | INV-17 |
| Exceptions | INV-20 |
