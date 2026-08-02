# S10 — Build System Subsystem Specification

**Status:** In Review · **Subsystem:** S10 (Blueprint §2, "Not begun") · **Date:** 2026-08-02

## Scope

Deterministic orchestration: turning ratified inputs (source, ratified
configs) into reproducible build artifacts, feeding S15 release. This
spec fixes the determinism and authority frame; concrete build content is
blocked.

## Responsibilities

- **Determinism:** identical inputs → identical artifacts (Blueprint §2;
  artifact table: "generated, reproducible, disposable").
- Orchestrate, never decide: build configuration carries no decision
  authority (INV-6 analogue; a build flag never changes what code means —
  Baseline §4 forbidden responsibility shared with S11).
- Provide CI its execution substrate without becoming policy (L-10,
  INV-10).

## Interfaces

Build invocation and artifact-manifest surfaces: **BLOCKED** — missing:
what is built (identity-dependent) and artifact formats; blocked by:
RFC-0001 + S5 specs; unblock: those ratifications.

## Data model

Frame: build = (input closure, environment declaration, output manifest).
All three concrete schemas: **BLOCKED** — same citation. Rule specifiable
now: the input closure must be fully declared — undeclared inputs are a
determinism defect.

## API contracts

**BLOCKED** — same citation.

## State machines

Per-build lifecycle: Declared → Executing → (Succeeded + manifest |
Failed + diagnosis). Retries create new builds; builds are never mutated.

## Sequence flows

Frame: input closure resolved → environment pinned → execution → manifest
emitted → artifacts handed to S12 (testing) and S15 (release). Content:
**BLOCKED** as above.

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Non-determinism (same inputs, different artifacts) | manifest comparison | defect; root input undeclared or environment unpinned |
| Undeclared input | closure audit | build rejected as non-conforming |
| Build-config semantic drift | review | rejected — configs never change meaning |

## Security requirements

Build executes only declared inputs; artifact provenance recorded in the
manifest (supply-chain frame; concrete signing requirements deferred to
RFC-0007's trust questions — TODO(blocked-by: acceptance ADR for
RFC-0007) if packages exist).

## Performance budgets

**BLOCKED** — missing: any ratified requirement; blocked by: RFC-0001;
unblock: post-identity engineering decisions.

## Observability requirements

Every build fully reconstructable from its manifest; manifests retained
for every released artifact (INV-17 support: shipped behavior → clause
traceability requires knowing exactly what shipped).

## Testing requirements

Determinism verification (rebuild-and-compare) as a mechanical check;
manifest completeness audit. Encoding: TODO(blocked-by: acceptance ADR
for RFC-0011).

## Acceptance criteria

- Rebuild of any released artifact from its manifest is bit-identical or
  the deviation is a recorded defect.
- Zero undeclared inputs across all builds at audit.
- No build configuration change has ever altered program meaning.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Determinism | Blueprint §2 (S10), §7 (binary artifact row) |
| No authority | INV-6; L-10; Baseline §4 |
| Release feed | Blueprint §3 (S5,S12 → S10 → S15) |
| Provenance | RFC-0007 trust frame (acceptance pending) |
