# S14 — Documentation System Subsystem Specification

**Status:** In Review · **Subsystem:** S14 (Blueprint §2, "Minimal") · **Date:** 2026-08-02

## Scope

Explanatory and instructional documentation for consumers of FCOS:
guides, references, examples. Excludes: defining anything — S14 is
forbidden from being a definition source (Blueprint §3: S14 must not
depend on, or serve as, definition-source authority; L-2 family) and
from being an authority mirror (→S3 rule, L-9).

## Responsibilities

- Explain ratified behavior accurately; documentation *describes*, the
  specification *defines*.
- Track ratified sources: every normative statement in docs cites the
  governing clause/document; divergence is a documentation defect.
- Maintain reader-facing structure (per-audience organization) without
  duplicating governed content (the no-duplication rule from the
  Engineering OS decisions: link, don't copy).

## Interfaces

Repository interface for authorship; published documentation surface for
readers. No programmatic surface. Rendering/hosting choices are
implementation details below this spec.

## Data model

- **Doc page:** audience, subject, cited sources (≥1 for any normative
  claim), freshness reference (which spec/ADR versions it describes).
- **Example:** runnable status flag — examples asserting behavior are
  evidence-class artifacts and must trace to clauses once clauses exist
  (**BLOCKED** for language examples — missing: any ratified language
  behavior; blocked by: RFC-0001; unblock: first S4 ratification).

## API contracts

Not applicable.

## State machines

**Doc page:** Current → Stale (cited source superseded/amended) →
Current (revised) or Archived. Staleness is mechanical: cited-version vs
ratified-version comparison.

## Sequence flows

1. **Publication:** governed change merges → affected pages identified
   via citations → revised via PR → published.
2. **Defect flow:** doc/spec divergence reported → doc corrected (the
   spec is never corrected to match docs — direction is one-way).

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Doc contradicts ratified source | citation audit / reader report | doc corrected; never vice versa |
| Uncited normative claim | mechanical audit | cite or demote to non-normative phrasing |
| Duplication of governed text | review | replace with link |

## Security requirements

Same PR-gated write path as all governed surfaces; no doc-publishing
pipeline may write into `docs/constitution/`, `docs/architecture/`,
`docs/decisions/`, `docs/rfc/`, or `specs/`.

## Performance budgets

Not applicable to a document subsystem; no ratified requirements exist.

## Observability requirements

Staleness dashboard: count of pages citing superseded versions, reported
per audit cycle; zero-normative-uncited-claims as a tracked metric.

## Testing requirements

Mechanical: citation links resolve; cited versions exist; link/ID checks
per RFC-0011 E-A (TODO(blocked-by: acceptance ADR for RFC-0011));
runnable examples execute against a conforming implementation once one
exists (**BLOCKED** as in Data model).

## Acceptance criteria

- Every normative statement cited; zero standing doc/spec contradictions
  at audit.
- No governed text duplicated into documentation.
- Staleness resolved or flagged within the audit cycle that detects it.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Describes, never defines | Blueprint §3 (S14 forbidden dep); INV-2 family |
| One-way authority | L-9 analogue for docs; Blueprint §8 |
| No duplication | Engineering OS decision (M4 era, ADR-0001 context) |
| Mechanical checks | RFC-0011 (acceptance pending) |
