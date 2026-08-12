# S4 — Language Definition Subsystem Specification

**Status:** Ratified (container: ADR-0009; Stage 0 contract clause set: ADR-0011) · **Subsystem:** S4 (Blueprint §2, "Empty by design") · **Date:** 2026-08-02

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
(ADR-0007, Q2). Clause content: the Stage 0 **minimal contract inventory** is
ratified per-clause (ADR-0011; §Stage 0 clause set below). Language
content — syntax, grammar, and semantics — remains **BLOCKED**: it is
future content outside the Stage 0 contract inventory (ADR-0011,
Decision 1) and enters only through the amendment path (RFC → ADR).

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
  clause index; posture ratified by ADR-0004). Schema: recorded by
  ADR-0010 (per-spec YAML sidecar, five required clause fields); the
  S04 sidecar `specs/S04-language-definition.index.yaml` is
  instantiated per ADR-0011 with `spec.version` 1.0.0.
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
- Language content model: **BLOCKED** — the ratified Stage 0 clause
  set (ADR-0011) is the minimal contract inventory only; no syntax,
  grammar, or semantics is defined by it; language content enters only
  through the amendment path (RFC → ADR).

## API contracts

Not applicable — S4 is a document subsystem. Its binding "API" is the
clause contract above plus the machine-readable index
(`specs/S04-language-definition.index.yaml`, instantiated per
ADR-0010 / ADR-0011).

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
conformance test, marker D-03-style exceptions recorded). Mechanical
clause-ID and index checks are active for the ratified Stage 0 clause
set (`tools/checks/check_clause_index.py`; ADR-0011). CN-9 closure is
a recorded exception (ADR-0011, Decision 7): no conformance suite
exists yet (G-CONF open); the exception discharges when P12 produces
clause-traced tests.

## Acceptance criteria

- Container criteria (checkable now): this structure ratified; ID scheme
  adopted; lifecycle enforced on first Draft.
- Content criteria: the Stage 0 minimal contract inventory is
  ratified per-clause (ADR-0011; §Stage 0 clause set). Language-content
  criteria remain **BLOCKED** — future content outside Stage 0's
  contract inventory; amendment path only.

## Stage 0 clause set (minimal contract inventory)

Ratified per-clause by ADR-0011 (2026-08-12) through the amendment
path (proposal RFC-0018 → recording ADR — §Sequence flows, step 2;
INV-18). Scope per ADR-0011, Decision 1: only obligations already
authoritative on `main`; no new syntax, grammar, semantics, namespace
token, or implementation requirement. Language content is future
content outside this inventory and enters only through the amendment
path.

Clause declaration convention (mechanical — ADR-0011, Decision 5):
each clause is declared by exactly one list line beginning
`- **<clause ID> — <title>.**`; clause IDs use the grandfathered
document identifier `S04` with hierarchical dotted N-C fragments
(RFC-0002; ADR-0008). Clauses are listed in clause-ID order. Every
clause below has status **ratified** and is indexed in
`specs/S04-language-definition.index.yaml` (ADR-0010).

- **S04#1.1 — Language identity.** Category: defined. The Frontier
  Specification Language is an interchange/definition core (I-A scope)
  with a staged evolution path toward executable semantics. (ADR-0006,
  Decision 1.)
- **S04#1.2 — Staging discipline.** Category: defined. Capability
  stages are explicit and ordered; Stage 0 is the definition/validation
  core scoped by ADR-0006; execution-facing semantics beyond Stage 0
  are deferred without being foreclosed; each stage transition is a
  Maintainer decision travelling the RFC → ADR path, never entered
  implicitly. (ADR-0006, Decision 3; CN-14.)
- **S04#1.3 — Runtime scope.** Category: defined. The only runtime in
  scope is the S-B validation-evaluation runtime, and it holds zero
  defining authority over language meaning. (ADR-0006, Decision 2;
  Baseline L-3.)
- **S04#2.1 — Sole ownership of meaning.** Category: defined. All
  definitions of program validity and meaning are owned by this
  specification; nothing else may define either. (INV-2, INV-3, INV-4,
  INV-5; Baseline P-1, L-1, L-2.)
- **S04#2.2 — First-class consumers.** Category: defined. The
  first-class consumers are exactly three classes, affirmed jointly
  and symmetrically: humans authoring, tools consuming, and AI systems
  doing both; no consumer class acquires defining authority; the
  classes are stage-invariant. (ADR-0007, Decision Q1.)
- **S04#2.3 — Success criteria.** Category: defined. At every horizon
  the success criterion is the Article 1 metric instantiated by the
  Article 10 goals, indexed to phases and capability stages, never
  calendar deadlines. (ADR-0007, Decision Q2.)
- **S04#3.1 — Identifier scheme.** Category: defined. Artifact and
  clause identifiers follow the ratified N-B + N-C composite scheme;
  this document uses the grandfathered identifier `S04`; every
  existing identifier is grandfathered — never renumbered, never
  migrated; each new namespace token requires its own RFC → ADR
  decision, and the recording ADRs constitute the namespace registry.
  (ADR-0004; ADR-0008, Decisions 1–4.)
- **S04#3.2 — Clause-identifier stability.** Category: defined. Clause
  identifiers are assigned exactly once and never renumbered after
  ratification; the identifier/clause-numbering freeze is binding as
  of the S04 container ratification. (RFC-0002 A-1; ADR-0008,
  Decision 5; ADR-0009, Decision 3.)
- **S04#3.3 — Behavior categorization.** Category: defined. Every
  specified behavior is classified as exactly one of: defined,
  implementation-defined, unspecified, or undefined. (Baseline §10;
  §Responsibilities above.)
- **S04#3.4 — Lifecycle and amendment.** Category: defined. The
  specification lifecycle is Draft → In Review → Ratified → Deprecated
  (with successor pointer); post-ratification change is amendment via
  RFC + ADR, never silent edit. (Blueprint §7; INV-18; §State machines
  above.)
- **S04#4.1 — Index posture.** Category: defined. The specification
  prose is authoritative; the machine-readable clause index is derived
  hygiene and consistency infrastructure — never independently
  normative, never overriding prose. (RFC-0008 M-B; ADR-0004;
  ADR-0010, Decision 1.)
- **S04#4.2 — Index schema and audits.** Category: defined. The clause
  index is a per-spec YAML sidecar with required entry fields id,
  category, title, status, and source; entries are ordered by ratified
  clause ID; the index is mechanically checked by the ADR-0010 drift
  checks plus the repository link/ID gates. (ADR-0010,
  Decisions 3–12.)

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Sole ownership of meaning | INV-2..5; Baseline P-1, L-1, L-2 |
| Four-category conformance model | Baseline §10 |
| Lifecycle | Blueprint §7 |
| Identity decision | RFC-0001; ADR-0006; ADR-0007; CN-14 |
| Clause IDs / index | RFC-0002 N-B + N-C; ADR-0004; ADR-0008; namespace registry via recording ADRs; S04 freeze point at container ratification |
| Stage 0 contract inventory | RFC-0018; ADR-0011 (Maintainer directive, 2026-08-12) |
