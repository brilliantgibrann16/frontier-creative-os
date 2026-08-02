# S3 — Knowledge System Subsystem Specification

**Status:** In Review · **Subsystem:** S3 (Blueprint §2) · **Date:** 2026-08-02

## Scope

Recording of engineering state, rationale, and history: the workspace
mirror (Notion), the living registers (Decision Register, Risk Register,
Operations Log, Glossary), and dual-homed document mirrors. Excludes:
being a source of authority for anything (L-9, INV-9).

## Responsibilities

- Mirror repository-authoritative content one-way: repository → workspace.
- Maintain registers as indexed, append-oriented records so volume never
  bloats core documents (Blueprint §10).
- Record operations history (Ops Log) for every engineering cycle.
- Dual-home ADRs, RFCs, and specifications per the 2026-08-01 Maintainer
  decision (repository = permanent archive; workspace = working surface).
- Forbidden: any subsystem treating S3 content as authoritative (L-9);
  S3-originated edits flowing back into governed artifacts without the
  normal proposal path.

## Interfaces

- **Knowledge interface** (Blueprint §8): one-way authority, repository →
  mirror. Write access to the mirror is unrestricted for derived content;
  write access to the repository from S3 does not exist.
- Human consumption surface: workspace pages, databases, registers.

## Data model

- **ADR Log:** number (auto-increment), title, status select
  (Proposed/Accepted/Rejected/Superseded), GitHub link — mirrors
  `docs/decisions/`.
- **RFC Index / Specification Index:** mirror rows keyed by repo path,
  status, GitHub link.
- **Decision/Risk Registers:** ID, statement, status, owner, dates.
- **Operations Log:** timestamped cycle entries (append-only table).
- **Glossary:** term → ratified definition (vocabulary is binding,
  INV-12; the ratified copy lives in Baseline §9 — glossary is derived).

## API contracts

Not applicable — the mirror is operated through the workspace's own
tooling; no FCOS-published programmatic API exists or is required by any
ratified document.

## State machines

- **Mirror entry:** Absent → Synced → Stale (repo changed) → Synced.
  Stale is presumed in any conflict (Blueprint §9: mirror assumed stale).
- **Register row:** Open → Closed (or status-specific lifecycle, e.g.
  risk: Open → Mitigated → Closed); rows are never deleted, only closed.

## Sequence flows

1. **Sync:** repo merge event → mirror update (manual or tooled) → Ops
   Log entry. Known outstanding sync: ADR-0002/0003, RFC set,
   Governance/Architecture pages.
2. **Conflict resolution:** divergence detected → repository wins
   mechanically (L-9) → mirror corrected → divergence cause logged.
3. **Register update:** engineering event → register row appended/closed
   → no further propagation (registers are terminal records).

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Mirror divergence | periodic comparison; any consumer report | resolve toward repository (L-9); log cause |
| Register gap (unlogged cycle) | audit of PR history vs Ops Log | backfill entry, marked as backfilled |
| Mirror treated as authority | citation audit | correct the citing artifact; L-9 reminder in review |
| Workspace data loss | trash/recovery events | restore from workspace trash; repository unaffected by construction |

## Security requirements

Mirror carries no authority, so its compromise cannot alter meaning
(failure containment: "workspace only", Blueprint §11). Repository links
in mirror rows must point to the authoritative copy. No secrets in
registers or logs.

## Performance budgets

No ratified quantitative requirements exist. **BLOCKED** — missing:
ratified sync-latency requirement; blocked by: none pending; unblock:
future decision. Operationally, sync follows each merged governance PR
(sequence flow 1) without a mandated deadline.

## Observability requirements

The Ops Log is itself the observability surface for engineering
operations; sync staleness is reportable per entity (last-synced
reference vs repo head).

## Testing requirements

Mechanical: every `docs/decisions/*.md` has exactly one ADR Log row with
matching status; index rows resolve to existing repo paths; Ops Log
covers every merged governance PR. TODO(blocked-by: acceptance ADR for
RFC-0011) for CI encoding.

## Acceptance criteria

- Zero authoritative citations of mirror content anywhere in the corpus.
- ADR/RFC/spec mirrors complete and status-consistent with the repo.
- Every merged PR since project start has an Ops Log entry.
- All known divergences resolved toward the repository with logged cause.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| One-way authority | Baseline L-9; INV-9; Blueprint §8, §9 |
| Dual-homing | Maintainer decision 2026-08-01 (recorded in session log; ADR-0001 context) |
| Registers absorb volume | Blueprint §10 |
| Failure containment | Blueprint §11 (knowledge inconsistency row) |
| Vocabulary bindingness | INV-12; Baseline §9 |
