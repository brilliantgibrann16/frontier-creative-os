# S4 — Language Definition Subsystem Specification

**Status:** Ratified (container-only, ADR-0009) · **Subsystem:** S4 (Blueprint §2, "Empty by design") · **Date:** 2026-08-02

## Scope

The specification documents that alone define validity and meaning of the
Frontier Specification Language (A3, "the meaning line"). This document
specifies the *container*: structure, lifecycle, and obligations of
language specifications. The *content* is entirely blocked.

**Content inputs decided.** Identity and purpose: I-D — an
interchange/definition core (I-A scope) with a staged evolution path
toward executable semantics (ADR-0006, Decision 1). Consumers: humans
authoring, tools consuming, AI systems doing both symmetrically
(ADR-0007, Q1). Success criteria: the Article 1 metric instantiated by
the Article 10 goals, indexed to phases and capability stages
(ADR-0007, Q2). Clause content remains **BLOCKED** — missing: ratified
Stage 0 clause set; blocked by: P03.3 per-clause ratification (Article
7); unblock: the P03.3 package.

## Responsibilities

- Own all definitions of program validity and meaning (INV-2); nothing
  else may define either (INV-3, INV-4, INV-5).
- Classify every specified behavior as exactly one of: defined,
  implementation-defined, unspecified, or undefined (Baseline conformance
  model, §10).
- Never depend on any implementation (L-1) or prototype (L-7, INV-7).

## Interfaces

- **Specification → machine:** machine-readable expression required for
  scalable conformance; posture M-B per RFC-0008 (prose authoritative +
  clause index; posture ratified by ADR-0004). Schema: **BLOCKED** —
  missing: index schema; blocked by: first specification ratification
  (RFC-0008, §Consequences: the schema is decided there); unblock:
  P03.4 at that ratification.
- **Human authoring/review:** repository interface (PR path) only.

## Data model

- **Specification document:** ID per the adopted **N-B + N-C** scheme
  (ADR-0004; ADR-0008). This S04 document uses the grandfathered
  document identifier `S04`. N-B supplies the namespace-capable document
  identifier layer; N-C supplies hierarchical dotted clause identifiers
  layered on the document identifier. Existing identifiers are
  grandfathered exactly as assigned: they are never renumbered or
  migrated, and no mapping table is created. No concrete namespace token
  is ratified by this specification; each future namespace token requires
  its own RFC → ADR path, and the recording ADRs constitute the namespace
  registry. Clause-numbering freeze is binding as of the S04 container
  ratification (ADR-0008, RFC-0002 OQ3; ratified container-only by
  ADR-0009).
- **Clause:** stable ID (never renumbered after ratification), category
  (one of the four above), text, traceability links (tests, RFCs, ADRs).
- Language content model: **BLOCKED** — missing: ratified Stage 0
  clause set (identity, consumers, and success criteria are decided —
  ADR-0006, ADR-0007); blocked by: P03.3; unblock: per-clause
  ratification.

## API contracts

Not applicable — S4 is a document subsystem. Its binding "API" is the
clause contract above plus the machine-readable index (blocked).

## State machines

**Specification lifecycle** (Blueprint §7): Draft → In Review → Ratified
→ Deprecated (with successor pointer). Clause IDs freeze at ratification;
post-ratification change is amendment via RFC + ADR, never silent edit.

## Sequence flows

1. **Spec production:** RFC-0001 acceptance ADR → spec charter per
   component → Draft → In Review (PR) → ratification ADR → conformance
   suite clauses traced (CN-9) → implementations authorized.
2. **Amendment:** proposal RFC → amended clauses (new IDs for new
   content) → recording ADR → suite update in same decision cycle.

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Spec/spec contradiction | consistency audit | amendment; the later-ratified clause is presumed defective until decided |
| Spec/implementation divergence | conformance suite | implementation is defective by definition (L-2) |
| Clause renumbering | mechanical ID audit | revert; renumbering after ratification is prohibited |
| Shadow specification (meaning asserted outside S4) | citation audit | invalidate; route content through S4 |

## Security requirements

Strictest review surface below Constitution/Baseline: ratification
requires explicit ADR; no AI-authored content enters Ratified status
without the human decision path (INV-5).

## Performance budgets

Not applicable to a document subsystem; no ratified requirements exist.
(Authoring throughput is not a specifiable behavior.)

## Observability requirements

Clause count, category distribution, and amendment rate reported per
audit cycle; every ratified clause discoverable by ID.

## Testing requirements

Mechanical: clause-ID uniqueness and stability; four-category totality
(every normative sentence categorized); CN-9 closure (every clause → ≥1
conformance test, marker D-03-style exceptions recorded). All
**BLOCKED** in practice — missing: any ratified spec to check; blocked
by: P03.1/P03.3 ratification (RFC-0001 is decided — ADR-0006,
ADR-0007); unblock: first ratified specification.

## Acceptance criteria

- Container criteria (checkable now): this structure ratified; ID scheme
  adopted; lifecycle enforced on first Draft.
- Content criteria: **BLOCKED** by per-clause ratification (P03.3);
  the governing decisions are recorded (ADR-0006, ADR-0007).

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Sole ownership of meaning | INV-2..5; Baseline P-1, L-1, L-2 |
| Four-category conformance model | Baseline §10 |
| Lifecycle | Blueprint §7 |
| Identity decision | RFC-0001; ADR-0006; ADR-0007; CN-14 |
| Clause IDs / index | RFC-0002 N-B + N-C; ADR-0004; ADR-0008; namespace registry via recording ADRs; S04 freeze point at container ratification |
