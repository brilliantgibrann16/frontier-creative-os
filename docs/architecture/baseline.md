# Frontier Creative OS — Architecture Baseline

**Status:** Ratified — adoption recorded as ADR-0002 (2026-08-02); amended per
ADR-0006 (2026-08-10, MINOR — see §13 Amendment record)
**Version:** 1.1.0 (MINOR amendment per ADR-0006 — S11 retirement recorded in
§13; 1.0.0 = Architecture Baseline v1, per the adoption terms of ADR-0002)
**Subordinate to:** Constitution v1 (1.0.0)
**Companions:** `blueprint.md` (descriptive), `doctrine.md` (explanatory) — both subordinate to this document

---

## §1 Purpose and Authority

The Architecture Baseline records the structures, boundaries, and laws of
the FCOS ecosystem. It is the permanent architectural reference for every
RFC that follows.

- The Baseline ranks directly beneath the Constitution and above all RFCs,
  specifications, and implementations.
- RFCs may extend or refine the Baseline. RFCs may never silently
  contradict it.
- The Baseline states structure and law only. It defines no language
  content: no syntax, keywords, grammar, types, semantics, memory,
  concurrency, or execution behavior.
- Where the Baseline and the Constitution diverge, the Constitution wins.

## §2 Architectural Principles

- **P-1 — Specification supremacy.** The ratified specification is the sole
  source of meaning within its scope.
- **P-2 — No dialects.** There is exactly one definition of the language,
  and one implementation-independent conformance judge for all
  implementations.
- **P-3 — One-way authority.** Authority flows from specification to
  implementation, never in reverse.
- **P-4 — AI symmetry.** Human and AI contributions traverse identical
  gates. No privileged AI channel exists into authoritative artifacts.
- **P-5 — Standard library honesty.** The standard library exposes only
  behavior defined by ratified specifications; nothing ships as ambient or
  undocumented capability.

## §3 System Context

FCOS comprises: all authoritative definitions (Constitution, this Baseline,
ADRs, RFCs, specifications); official implementations (compiler(s),
runtime(s), standard library); official tooling (SDK, build system, package
manager, developer tools); the conformance and testing apparatus; the
documentation and knowledge systems; and the release function. Outside the
boundary: user programs, third-party implementation internals, host
platforms, and the internal reasoning of AI systems. The full decomposition
is descriptive material and lives in `blueprint.md`.

## §4 Layer Model

Twelve layers in six strata. Authority crosses stratum boundaries downward
only; feedback travels only as governed proposals (Issues, RFCs).

Strata: 0 Governance · 1 Definition · 2 Realization · 3 Delivery ·
4 Assurance · 5 Consumption.

| Layer (stratum) | Responsibilities | Forbidden responsibilities |
| --- | --- | --- |
| Engineering Knowledge (0) | Recording state, rationale, risk, traceability | Making decisions; knowledge records decisions, never constitutes them |
| Architecture (0) | System boundaries, layer contracts, dependency law, artifact authority | Language content of any kind |
| Language Specification (1) | Sole definition of validity and meaning; explicit labeling of implementation-defined / unspecified / undefined territory | Implementation strategy; performance; tool behavior |
| Compiler (2) | Translation, diagnostics, optimization within spec-observable equivalence | Defining or extending language behavior |
| Runtime (2) | Execution services realizing spec-declared models | Semantic extensions; features unavailable to other conforming runtimes |
| SDK (3) | Coherent, versioned packaging of public interfaces | Exposing compiler/runtime internals as de facto API |
| Developer Tools (3) | Editing, navigation, formatting, diagnostics presentation via published contracts | Dialect creation; accepting/rejecting programs differently from the spec |
| Build System (3) | Deterministic orchestration of compilation, testing, packaging | Altering program meaning; configuration-dependent semantics |
| Package Manager (3) | Naming, versioning, distribution, dependency resolution | Changing what resolved code means |
| Testing (4) | Evidence of conformance and correctness, derived from specifications | Defining semantics; a test disagreeing with the spec is a defective test |
| CI/CD (4) | Mechanical enforcement of declared gates | Policy-making; a skipped gate is a violation, not a waiver |
| AI Layer (5) | Producing and consuming artifacts through the same public interfaces available to humans | Privileged semantic access; entering Stratum 0–1 artifacts outside the human decision process |

**Communication paths.** Definition publishes contracts downward
(specification → compiler/runtime; grammar/AST/diagnostics contracts →
tools, build, AI). Realization and below publish only evidence and
proposals upward. There is no lateral semantic channel: same-stratum
components interoperate only through contracts published at the Definition
stratum.

## §5 Dependency Law

- **L-1** Architecture must not depend on implementation.
- **L-2** Specifications define; implementations realize. An implementation
  may not redefine, extend, or narrow specified behavior. Divergence is a
  defect in the implementation, always.
- **L-3** The compiler must not define language behavior. Observable
  behavior absent from the specification is a conformance violation, not a
  feature.
- **L-4** Tests must not define semantics. When test and spec disagree, the
  test is wrong by definition; the discrepancy is filed as an Issue.
- **L-5** The AI layer must not define meaning. AI-produced content enters
  authoritative artifacts only through the same RFC/ADR/review path as
  human-produced content.
- **L-6** Repository structure is not architecture. Directories, scaffolds,
  and layouts carry zero decision authority.
- **L-7** Prototypes are not precedent. Prototype behavior may be cited
  only as historical context and may never constrain design.
  (Maintainer ruling of 2026-08-01, elevated to law.)
- **L-8** Decisions bind only as ADRs (Constitution Article 7). Chat,
  workspace edits, commit messages, and code comments never constitute
  decisions.
- **L-9** Mirrors are derived. For dual-homed artifacts, the repository
  copy is authoritative; conflicts resolve toward the repository.
- **L-10** Gates are declared above, enforced below. Quality gates are
  defined in the Constitution, this Baseline, and ADRs; CI encodes them.
  Editing CI is never a way to change a gate.
- **L-11** No lateral semantic contracts. Same-stratum components
  interoperate only via contracts published at the Definition stratum.
- **L-12** Vocabulary is binding. Terms defined in §12 mean exactly that in
  every FCOS artifact; a document needing a different meaning must define a
  new term.

## §6 Artifact Hierarchy

| Rank | Artifact | Purpose (single) | Class |
| --- | --- | --- | --- |
| 1 | Constitution | How the project is governed | Authoritative |
| 2 | Architecture Baseline | How the system is structured | Authoritative |
| 3 | ADR | Binding record of one decision | Authoritative (record) |
| 4 | RFC | Proposal and rationale for one change | Authoritative for rationale only |
| 5 | Specification | Normative definition of one area | Authoritative (content) |
| 6 | Implementation Plan | How ratified content will be built | Derived |
| 7 | Conformance Tests / Source Code | Evidence / realization | Derived |
| 8 | Issue / Documentation / Release Notes | Tracking / explanation | Operational / derived |
| 9 | CI Configuration | Mechanical gate encoding | Derived |

**Reference rules.** Any artifact may cite artifacts of equal or higher
rank. Higher-rank artifacts may reference lower ranks only as informative
context, never as a dependency. Accepted ADRs are immutable; correction
happens by supersession. Every artifact type has exactly one purpose; an
artifact serving two purposes is split.

## §7 Information Flow Model

```
Constitution → Architecture Baseline → RFC → ADR → Specification
  → Implementation Plan → Source Code → Tests → CI → Release → Documentation
```

Every artifact's correctness is judged against the artifact above it. The
only legal feedback is a new proposal entering at the top (Issue → RFC),
which is a new forward pass, not reverse flow.

**Named illegal reverse flows:** bug canonization (implementation → spec);
evidence tampering (implementation → tests); parser-convenience grammar
drift (implementation → contracts without RFC); shadow specification
(documentation → meaning); gate erosion (release pressure → CI);
ungoverned AI insertion (AI → authoritative artifacts); scaffold authority
(repository layout → architecture); mirror authority (workspace →
repository); prototype precedent (historical code → design).

## §8 Decision Framework

Ask in order; the first "yes" fixes the home:

1. Changes how decisions are made or who decides? → Constitution amendment.
2. Changes system structure, boundaries, artifact authority, or law?
   → Baseline amendment (§13).
3. Changes what programs are valid or what they mean? → RFC →
   Specification, with ADR recording acceptance.
4. One-time architectural or governance choice fixing no program meaning?
   → ADR directly.
5. Changes how ratified content is built, with no observable behavioral
   difference? → Implementation Plan + PR review; no RFC.
6. About whether the build is correct? → Testing, reviewed in the PR.
7. About whether to ship? → Release process (Article 9 gates).

**Disambiguation.** If a question fits two homes, the higher-ranked home
wins. If an "implementation detail" turns out to be observable to a
conforming program, it is retroactively a category-3 question and the
change reverts until an RFC exists. Routine engineering decisions
(categories 5–7) never require ADRs.

## §9 Engineering Lifecycle

How an idea becomes shipped behavior, integrated with Constitution v1:

1. **Issue** — the need is recorded and tracked.
2. **RFC** — proposal drafted; Draft → In Review → Accepted/Rejected
   (Maintainer decision, Article 6/7).
3. **ADR** — acceptance and its consequences recorded (Article 7).
4. **Specification** — normative content drafted and ratified against the
   completeness obligations of §10.
5. **Conformance tests** — derived from ratified clauses.
   *Recommended before implementation begins; adopting this ordering as
   binding requires an ADR, as it exceeds the Constitution's letter.*
6. **Implementation Plan** — scope, approach, and Definition of Done.
7. **Implementation** — on a feature branch; Conventional Commits; never
   direct to `main`.
8. **Pull Request** — review against spec, plan, and gates; linked to its
   Issue.
9. **Merge** — by Maintainer decision; gates green.
10. **Release** — Article 9 gates plus §10 release obligations; release
    notes enumerate changes.

## §10 Conformance Model

Proof obligations only; no semantics are defined here.

| Subject | Proves | By |
| --- | --- | --- |
| Implementation | Conformance | Conformance suite derived clause-by-clause from ratified specs, maintained separately from unit tests; every normative clause carries at least one traceable test ID; suite green in CI; deviations enumerated as spec-labeled implementation-defined items |
| Specification | Completeness | Ratification checklist: every construct in scope has validity conditions and defined meaning, or is explicitly labeled implementation-defined / unspecified / undefined; validation rules defined (Article 7 gate); no undefined vocabulary; all cross-references resolve |
| RFC | Necessity | Problem statement traced to the Decision Register or a filed Issue; no existing ratified artifact answers it; alternatives with rejection rationale; evaluation against ratified design criteria (pending D-02) |
| ADR | A real decision | Context, decision, consequences, implementation reference (Article 7 gate); supersession chain intact |
| Release | Readiness | Article 9 gates; conformance suite green; traceability audit (every shipped behavior traces to a ratified clause; every significant decision has an ADR); release notes complete |

## §11 Risk Model

Permanent-damage risk classes (instances live in the Risk Register, never
here):

- **Meaning drift** — meaning acquiring a second source (violates P-1).
  Structural containment: L-2, L-3, L-4, L-5.
- **Dialect divergence** — implementations becoming de facto definitions.
  Containment: P-2, single conformance judge.
- **Authority erosion** — gate bypasses, mirror authority, exception creep.
  Containment: L-8, L-9, L-10; exceptions are explicit, recorded, one-time.
- **Unrecorded decisions** — resolution of open questions by accident or by
  shipping. Containment: L-8; unknowns registry; traceability audit.
- **Identity ambiguity** — proceeding as if the language identity decision
  (D-01) were made. Containment: UNKNOWN discipline; §12 naming rule.
- **Taxonomy lock-in** — unratified scaffolds hardening into structure.
  Containment: L-6.

Rules: every critical-class risk names its structural mitigation (the law
or invariant that contains it); acceptance of a critical risk is a recorded
decision, never silent.

## §12 Architectural Vocabulary (normative)

- **Architecture** — the structures, boundaries, and laws governing the
  system, independent of any implementation.
- **Specification** — a normative document that alone defines validity and
  meaning within its scope.
- **Semantics** — the meaning a specification assigns; a property of
  specifications, never of implementations.
- **Implementation** — any artifact realizing a specification.
- **Compiler** — an implementation translating conforming input into
  artifacts, preserving specified meaning. *Naming rule:* unqualified
  "compiler" means the language compiler; the Phase 0 artifact is the
  **specification-document pipeline (prototype)** and is never called "the
  compiler."
- **Runtime** — an implementation providing spec-declared execution
  services.
- **Behavior** — externally observable effects of execution, as defined by
  specifications.
- **Execution** — the act of producing behavior; carries no defining
  authority.
- **Conformance** — the demonstrated property that an implementation's
  observable behavior matches its governing specifications.
- **Artifact** — any versioned engineering work product with exactly one
  purpose.
- **Authoritative / Derived** — an artifact that defines vs. one judged
  against a definition.
- **Normative / Informative** — text that binds vs. text that explains.
- **Validation** — checking an artifact against its purpose and
  completeness obligations.
- **Verification** — checking an artifact against its governing artifact.
- **Implementation-defined / Unspecified / Undefined** — the three labels a
  specification may attach to territory it deliberately does not fix. The
  labels are engineering categories; their application to any language area
  is future RFC work.
- **Decision Register** — the living index of identified-but-unmade
  decisions; contains no authority.
- **Prototype** — an exploratory implementation with zero defining
  authority (L-7).

## §13 Versioning and Amendment

- **Versioning:** `MAJOR.MINOR`. MAJOR: any change to the Layer Model, the
  Dependency Law, artifact authority ranking, or information flow
  direction. MINOR: clarifications, vocabulary additions, new sections that
  constrain nothing existing.
- **Amendment:** RFC proposing the change → ADR recording the outcome → PR
  approved by the Maintainer and merged into `main`. Ratified sections are
  amended, never silently edited; superseded rules are struck with a
  pointer.
- **Review:** every amendment passes a consistency check against the
  Constitution and all Accepted ADRs. MAJOR changes additionally require an
  impact statement listing every artifact citing the affected rule.
- **Extension:** new content enters as new numbered sections or new laws
  (L-13, …), never by reinterpreting existing text. Volatile content goes
  to registers, never into this document.

### Amendment record

- **1.1.0 (2026-08-10) — S11 retired by supersession (ADR-0006).** At
  D-01 acceptance the RFC-0007 deferral trigger fired and packaging was
  decided **N-no** (U-8): FCOS does not adopt a package manager.
  Subsystem S11 (Package Manager) is retired by supersession — struck
  with a pointer, never deleted. The superseding record is ADR-0006;
  there is no successor subsystem (the packaging responsibility lapses
  rather than transferring — no replacement is invented). Per the S11
  acceptance criteria, `specs/S11-package-manager.md` is **Deprecated**
  by this amendment; the specification file and all historical S11
  references remain in place as submission-time text, per the corpus
  convention that indexes plus the disposing ADR are the authoritative
  record. The corresponding program (P10) does not exist. Re-opening
  packaging requires a new RFC → ADR (CN-14). MINOR change: no Layer
  Model, Dependency Law, authority-ranking, or information-flow rule is
  affected.

---

**Open decisions this Baseline deliberately does not preempt:** ~~D-01
(language identity)~~ *(decided — ADR-0006, identity I-D; see §13
Amendment record)*, D-03 (identifier/namespace scheme; must be
namespace-capable), D-13 (`specs/fcos/` disposition), D-14 (AI artifact
classes). See `blueprint.md`, "Future Unknowns".