# S2 — Architecture Subsystem Specification

**Status:** In Review · **Subsystem:** S2 (Blueprint §2) · **Date:** 2026-08-02

## Scope

Maintenance and evolution of the architecture document set (Baseline,
Blueprint, Doctrine), the dependency law, and the subsystem decomposition.
Excludes: making decisions (S1 records them; this subsystem hosts their
structural content) and any language meaning (S4).

## Responsibilities

- Keep `docs/architecture/` internally consistent and consistent with all
  Accepted ADRs.
- Execute the amendment path (Baseline §13): RFC → Baseline amendment →
  recording ADR — in that order, before dependent implementation.
- Run consistency audits (Doctrine §13): ⊑-DAG acyclicity (CN-27), orphan
  detection, trace closure, vocabulary bindingness (INV-12).
- Maintain the unknowns registry (Blueprint §14) — no unknown resolved
  implicitly by shipped behavior.
- Forbidden: depending on any implementation (INV-1, L-1); silent
  contradiction of an RFC by architecture edit (RFCs may extend/refine,
  never silently contradict — Baseline preamble).

## Interfaces

Repository interface only (PRs into `docs/architecture/`); consumers read
via the repository and the S3 mirror. No programmatic surface.

## Data model

- **Baseline:** normative rank 2; MAJOR.MINOR version; status header.
- **Blueprint:** descriptive; revised with MAJOR Baseline changes.
- **Doctrine:** explanatory; amended by supersession.
- **Registries:** subsystem table (S1–S16), invariants (INV-1..20),
  unknowns (U-1..14) with resolving-decision pointers.

## API contracts

Not applicable — document contracts only (status headers, version fields,
registry table schemas above).

## State machines

- **Baseline version:** vM.N → vM.(N+1) (compatible clarification) or
  v(M+1).0 (structural change) — each via RFC + ADR.
- **Document status:** Proposed → Ratified → (portions) Superseded.
  Note: the three architecture documents still carry `Status: Proposed`
  headers; ADR-0002 records ratification and mandates the header flip —
  an outstanding mechanical TODO, not a status ambiguity.
- **Subsystem lifecycle:** Proposed → Adopted (RFC + amendment + ADR) →
  Deprecated (status, never deletion) with successor pointer.

## Sequence flows

1. **Amendment:** Issue → RFC → Maintainer acceptance → Baseline text
   change + version bump → recording ADR → Blueprint revision if MAJOR.
2. **Subsystem addition** (Blueprint §13): necessity RFC → layer-model
   placement + forbidden-responsibilities definition → adoption ADR →
   only then any implementation.
3. **Audit cycle:** run Doctrine §13 checks → file findings as Issues →
   fixes via normal PR path.

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Architecture/ADR contradiction | audit diff | architecture text corrected toward ADR, or superseding ADR |
| Dependency-law violation in a change | review + audit | reject PR; violation never merges |
| Unknown resolved implicitly | audit: behavior presumes an answer | revert; route through the resolving decision (Blueprint §14 rule) |
| Version header drift | mechanical check | hygiene commit (e.g. the ADR-0002 header TODO) |

## Security requirements

Same repository protections as S1; additionally, no write path into
`docs/architecture/` outside PR review — architecture is a rank-2
surface and inherits the strictest review posture below the Constitution.

## Performance budgets

No ratified quantitative requirements exist. **BLOCKED** — missing: any
ratified audit-frequency or latency requirement; blocked by: none
pending; unblock: future decision if needed. Audit *coverage* (which
checks run) is specified under Testing; only timing is unspecified.

## Observability requirements

Rank-change rate is the doctrine-designated health metric (DP-20/GL-10):
frequency of changes to rank-1/2 artifacts should trend toward zero;
reported per audit cycle in the Operations Log.

## Testing requirements

Mechanical (per RFC-0011, RFC-0008 posture; TODO(blocked-by: acceptance
ADRs)): ⊑-DAG acyclicity (CN-27); every INV/U/L/P ID unique and
referenced consistently; unknowns registry entries each name a resolving
decision; Blueprint subsystem table matches spec corpus index.

## Acceptance criteria

- Zero contradictions between architecture documents and Accepted ADRs.
- Every structural change in history followed the §13 path.
- Audit findings all tracked as Issues (none silently fixed).
- Status headers match ADR-recorded reality (post header-flip TODO).

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Document set + precedence | ADR-0002 |
| Amendment path | Baseline §13; Blueprint §13 |
| Audits | Doctrine §13 (CN-27, trace closure) |
| Unknowns discipline | Blueprint §14 closing rule; CN-14 |
| Health metric | Doctrine DP-20, GL-10 |
