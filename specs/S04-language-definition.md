# S4 — Language Definition Subsystem Specification

**Status:** Ratified (container: ADR-0009; Stage 0 contract clause set: ADR-0011; Stage 1 W-B clause set: ADR-0013; Stage 2 clause set: ADR-0016) · **Subsystem:** S4 (Blueprint §2, "Empty by design") · **Date:** 2026-08-02

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
ratified per-clause (ADR-0011; §Stage 0 clause set below), the
Stage 1 **W-B interchange kernel** is ratified per-clause (ADR-0012,
D1/D2; ADR-0013; §Stage 1 clause set below), and the Stage 2 **typed data model
and pure deterministic expressions** are ratified per-clause (ADR-0016;
§Stage 2 clause set below). Language content beyond the ratified Stage 0,
Stage 1, and Stage 2 inventories — execution-facing runtime semantics and
dedicated human surface syntax (rejected/deferred under S2-B) — remains
**BLOCKED** and enters only through the amendment path (RFC → ADR).

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
- Language content model: **BLOCKED** beyond the ratified inventories —
  the ratified Stage 0 clause set (ADR-0011) is the minimal contract
  inventory and the ratified Stage 1 clause set (ADR-0013) is the W-B
  interchange kernel (artifact model, validity, validation outcomes,
  and the JSON interchange form); no syntax, grammar, or type/data
  model is defined by them (ADR-0012, D3); further language content
  enters only through the amendment path (RFC → ADR).

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
clause-ID and index checks are active for the ratified Stage 0 and
Stage 1 clause sets (`tools/checks/check_clause_index.py`; ADR-0011;
ADR-0013). CN-9 closure is
a recorded exception (ADR-0011, Decision 7): no conformance suite
exists yet (G-CONF open); the exception discharges when P12 produces
clause-traced tests.

## Acceptance criteria

- Container criteria (checkable now): this structure ratified; ID scheme
  adopted; lifecycle enforced on first Draft.
- Content criteria: the Stage 0 minimal contract inventory is
  ratified per-clause (ADR-0011; §Stage 0 clause set), and the Stage 1
  W-B interchange kernel is ratified per-clause (ADR-0013; §Stage 1
  clause set). Remaining language-content criteria stay **BLOCKED** —
  future content outside the ratified inventories; amendment path only.

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

## Stage 1 clause set (W-B interchange kernel)

Ratified per-clause by ADR-0013 (2026-08-19) through the amendment
path (proposal RFC-0020, revised 2026-08-19 with the Maintainer's F1
decision → recording ADR — §Sequence flows, step 2; INV-18). Scope per
ADR-0012, D2: the W-B interchange kernel — artifact model, Stage 1
validity conditions, validation-outcome contract, and one concrete
serialized interchange form, decided F1-A: **JSON** (Maintainer
decision, 2026-08-19; ADR-0013, Decision 1). The type/data model is
explicitly deferred (ADR-0012, D3) and enters, if ever, through its
own amendment cycle; syntax and grammar remain future content outside
this inventory. Clause declarations follow the ratified convention
(ADR-0011, Decision 5); clauses are listed in clause-ID order; every
clause below has status **ratified** and is indexed in
`specs/S04-language-definition.index.yaml` (ADR-0010).

- **S04#5.1 — Artifact unit.** Category: defined. A Stage 1 FSL
  artifact is a finite serialized unit of FSL definition content
  expressed in the ratified Stage 1 interchange form (S04#8.1). The
  artifact is the unit of validation: every Stage 1 validity condition
  and every validation outcome applies to exactly one artifact.
  Source: ADR-0006, Decision 1; ADR-0012, D2.

- **S04#5.2 — Stage 1 self-containment.** Category: defined. Whether a
  Stage 1 artifact is valid is decidable from the artifact's serialized
  content and the ratified S04 clauses alone. Artifacts do not
  reference other artifacts at Stage 1; composition and inter-artifact
  reference are explicitly labeled deferred territory, entering, if
  ever, through their own amendment cycle. Source: Baseline §10
  labeling obligation; GL-2 narrow-complete guidance; ADR-0012, item 5
  (nothing else is decided).

- **S04#6.1 — Structural validity.** Category: defined. An artifact is
  structurally valid if and only if it conforms to the ratified
  interchange-form clauses (S04#8.1–S04#8.3). Structural validity is
  mechanically decidable from the artifact alone; an artifact that is
  not structurally valid is invalid without further evaluation.
  Source: ADR-0012, D2; Doctrine CN-6.

- **S04#6.2 — Validity closure.** Category: defined. An artifact is
  valid if and only if it violates no ratified Stage 1 validity clause.
  Every Stage 1 validity condition is a ratified S04 clause; no other
  source may add, remove, or weaken a validity condition (S04#2.1).
  Territory not covered by a ratified clause is never implicitly
  defined: per S04#3.3, every behavior specified at Stage 1 carries
  exactly one of the four ratified categories, and deferred territory
  is labeled, never silent. Source: Baseline §10; CN-6; S04#2.1;
  S04#3.3.

- **S04#7.1 — Validation-outcome model.** Category: defined. Validating
  an artifact yields exactly one outcome: accepted or rejected. An
  artifact is accepted if and only if it is valid per S04#6.2;
  otherwise it is rejected. Source: ADR-0012, D2.

- **S04#7.2 — Violated-clause identification.** Category: defined.
  Every rejection identifies the violated ratified clause or clauses by
  clause identifier. The set of violated clause identifiers reported
  for an artifact is a function of the artifact and the ratified clause
  set. A rejection that cites no violated clause is itself defective.
  Source: INV-17 corollary; the RFC-0019 DR-4 row.

- **S04#7.3 — Outcome authority.** Category: defined. Validation
  outcomes report; they never rule. The ratified prose is
  authoritative: an outcome that contradicts the ratified clauses is
  defective, whichever tool produced it, and no validator — including
  the S-B validation-evaluation runtime — acquires defining authority
  through its outcomes. Source: Baseline L-2, L-3; AX-1; S04#1.3;
  S04#2.1.

- **S04#7.4 — Outcome determinism.** Category: defined. For identical
  artifact content validated against the same ratified S04 clause set,
  the validation outcome and the set of violated clause identifiers are
  identical across runs, implementations, and consumer classes.
  Source: ADR-0012, D4; Blueprint §13, property 4.

- **S04#7.5 — Diagnostic presentation.** Category: unspecified. The
  wording, ordering, rendering, and formatting of diagnostic messages
  beyond the S04#7.2 violated-clause-identifier set are unspecified at
  Stage 1. A binding diagnostics contract is S05 territory and enters,
  if ever, through S05's own ratification path — never through this
  clause. Source: Baseline §10 labeling obligation; B-06.

- **S04#7.6 — Validation/conformance boundary.** Category: defined. A
  Stage 1 validation outcome is evidence about one artifact; it is
  never a conformance judgment about an implementation. Conformance
  judgment belongs exclusively to the S13 conformance suite as the
  single implementation-independent judge; the S-B runtime evaluates
  artifacts and holds no judging authority. Source: ADR-0006,
  Decision 2 boundary obligation; INV-16; S04#1.3.

- **S04#8.1 — Single interchange form.** Category: defined. At Stage 1
  exactly one concrete serialized interchange form is ratified for FSL
  artifacts, and a Stage 1 artifact exists only in that form.
  Additional or alternative forms enter, if ever, through their own
  amendment cycle. Source: ADR-0012, D2.

- **S04#8.2 — Interchange-form obligations.** Category: defined. The
  ratified interchange form must satisfy all of the following, each
  compiled from a recorded decision: (a) it carries the S04#5.1
  artifact model; (b) well-formedness against the form is mechanically
  decidable, so that S04#6.1 structural validity and S04#7.4
  determinism are testable; (c) it is authorable and consumable by all
  three first-class consumer classes symmetrically (S04#2.2); (d) it
  embeds no type/data-model semantics — the deferral recorded by
  ADR-0012, D3 cannot be re-entered through the format. Source:
  ADR-0007, Decision Q1; ADR-0012, D2–D4.

- **S04#8.3 — Concrete interchange form.** Category: defined. The
  single interchange form required by S04#8.1 is JSON: a Stage 1 FSL
  artifact is exactly one JSON text as defined by RFC 8259 / ECMA-404,
  encoded per RFC 8259's interchange encoding rule (UTF-8).
  Well-formedness against the JSON grammar is mechanically decidable,
  satisfying S04#8.2 item b. JSON serves as serialization only: its
  value notation carries no FSL type/data model, and none enters
  through it — the ADR-0012 D3 deferral stands (S04#8.2 item d). Any
  concrete artifact schema over this form beyond the ratified Stage 1
  clauses is deferred, labeled territory entering, if ever, through
  its own amendment cycle. Source: Maintainer F1 decision, 2026-08-19
  (F1-A per GL-15/DP-28); ADR-0012, D2/D3; recording ADR-0013.

## Stage 2 clause set (Typed Data Model & Pure Expressions)

Ratified per-clause by ADR-0016 (2026-08-21) through the amendment
path (proposal RFC-0023 → recording ADR — §Sequence flows, step 2;
INV-18). Scope per ADR-0016, Decision 2 (Package S2-B): typed data
model core and pure deterministic expressions. Evaluation is static-only
(ADR-0016, Decision 3); interchange remains concrete JSON within
`schema_version: "fsl/1.0"` (ADR-0016, Decision 4); dedicated surface
syntax (S2-C) is deferred. Clause declarations follow the ratified
convention (ADR-0011, Decision 5); clauses are listed in clause-ID
order; every clause below has status **ratified** and is indexed in
`specs/S04-language-definition.index.yaml` (ADR-0010).

- **S04#9.1 — Stage 2 scalar data types.** Category: defined. Stage 2
  FSL defines four primitive scalar data types: `string` (UTF-8 text
  sequences), `integer` (finite signed whole numbers), `float` (finite
  IEEE 754 floating-point numbers), and `boolean` (`true` or `false`).
  Scalar values map directly to JSON primitive values in the concrete
  interchange syntax. Source: ADR-0016, Decision 2.

- **S04#9.2 — Stage 2 compound data structures.** Category: defined.
  Stage 2 FSL defines three structured compound types: `record` (a
  finite set of named, typed fields), `list` (an ordered homogeneous or
  heterogeneous sequence of elements), and `map` (a key-value
  dictionary with string keys). Compound values map directly to JSON
  objects and arrays in the concrete interchange syntax. Source:
  ADR-0016, Decision 2.

- **S04#9.3 — Stage 2 type annotations & declarations.** Category:
  defined. FSL artifact declarations may specify explicit type
  annotations for fields, parameters, and properties using declared
  scalar and compound type identifiers. Source: ADR-0016, Decision 2.

- **S04#9.4 — Stage 2 schema validation rules.** Category: defined. An
  artifact is structurally valid under Stage 2 if all field and
  property values conform strictly to their declared scalar or compound
  types. A type constraint violation constitutes a validation failure
  and yields a rejected validation outcome per S04#7.1. Source:
  ADR-0016, Decision 2.

- **S04#10.1 — Pure expression evaluation model.** Category: defined.
  Stage 2 expressions are side-effect-free, deterministic, and total
  (terminating) functional computations over literal values and artifact
  properties. Expression evaluation never mutates artifact state or
  performs external I/O. Source: ADR-0016, Decision 2; Doctrine GL-15.

- **S04#10.2 — Arithmetic & boolean operations.** Category: defined.
  Stage 2 supports standard pure arithmetic operators (`+`, `-`, `*`,
  `/`, `%` with division-by-zero yielding validation failure), boolean
  logic operators (`and`, `or`, `not`), and relational comparison
  operators (`==`, `!=`, `<`, `<=`, `>`, `>=`). Source: ADR-0016,
  Decision 2.

- **S04#10.3 — String & collection operations.** Category: defined.
  Stage 2 supports pure string concatenation and length operations,
  list element indexing and sequence length queries, and map key-value
  lookups. Out-of-bounds indexing or missing required keys yield
  validation failure. Source: ADR-0016, Decision 2.

- **S04#10.4 — Conditional expressions.** Category: defined. Stage 2
  supports conditional branching expressions of the form
  `if <condition> then <consequent> else <alternate>`, where the
  condition evaluates to boolean, and exactly one branch is evaluated
  deterministically. Source: ADR-0016, Decision 2.

- **S04#10.5 — Declarative invariant assertions.** Category: defined.
  FSL declarations may attach declarative invariant assertions
  expressed as boolean expressions. An invariant evaluating to `false`
  yields a rejected validation outcome per S04#7.1 citing S04#10.5.
  Source: ADR-0016, Decision 2.

- **S04#10.6 — Static evaluation boundary.** Category: defined.
  Stage 2 expression evaluation is performed strictly at compile and
  validation time (static constraint checking, constant folding, and
  declarative invariant validation). Runtime evaluation semantics remain
  deferred and S06 runtime behavior is not defined by this clause.
  Source: ADR-0016, Decision 3.

- **S04#10.7 — Stage 2 JSON AST expression representation.** Category:
  defined. Stage 2 expressions are represented as structured JSON AST
  nodes within the concrete interchange syntax under
  `schema_version: "fsl/1.0"`. Dedicated surface syntax is deferred per
  Package S2-B. Source: ADR-0016, Decisions 2, 4.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Sole ownership of meaning | INV-2..5; Baseline P-1, L-1, L-2 |
| Four-category conformance model | Baseline §10 |
| Lifecycle | Blueprint §7 |
| Identity decision | RFC-0001; ADR-0006; ADR-0007; CN-14 |
| Clause IDs / index | RFC-0002 N-B + N-C; ADR-0004; ADR-0008; namespace registry via recording ADRs; S04 freeze point at container ratification |
| Stage 0 contract inventory | RFC-0018; ADR-0011 (Maintainer directive, 2026-08-12) |
| Stage 1 W-B interchange kernel | RFC-0019; ADR-0012 (D1–D4); RFC-0020 (revised); ADR-0013 (Maintainer F1/F2 decisions, 2026-08-19) |
| Stage 2 Typed Data Model & Pure Expressions | RFC-0023; ADR-0016 (Maintainer D1–D4 decisions, 2026-08-21) |
