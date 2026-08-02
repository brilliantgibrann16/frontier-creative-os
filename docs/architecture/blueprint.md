# Frontier Creative OS — Master System Blueprint

**Status:** Ratified — adoption recorded as ADR-0002 (2026-08-02)
**Artifact class:** Blueprint — descriptive reference; carries no normative
authority. Where this document and `baseline.md` diverge, the Baseline
wins.
**Standing unknown:** the language identity decision (D-01) is unresolved.
Every identity-dependent statement below is marked UNKNOWN rather than
assumed.

---

## 1. Overall System Purpose

Frontier Creative OS is an engineering ecosystem whose product is a
language — the Frontier Specification Language (scope and identity:
UNKNOWN, pending D-01) — together with everything required for that
language to be defined, implemented, verified, distributed, and governed
with full traceability over multi-decade horizons.

**Inside the system boundary:** all authoritative definitions; official
implementations (compiler(s), runtime(s), standard library); official
tooling (SDK, build system, package manager, developer tools); the
conformance and testing apparatus; documentation and knowledge systems; the
release function.

**Outside the boundary:** user programs; third-party implementation
internals (FCOS governs only their conformance status); host operating
systems and hardware; external infrastructure; the internal reasoning of AI
systems.

**External actors:** the Maintainer (Article 6); contributors, human and
AI; end developers; downstream integrators; third-party implementers;
future governance participants.

**FCOS intentionally does not own:** correctness of user programs; behavior
of non-conforming implementations; guarantees about environments not
addressed by ratified specifications; truthfulness of AI-generated content
prior to human ratification; any commercial or adoption function.

## 2. System Decomposition

| # | Subsystem | Responsibility | Status |
| --- | --- | --- | --- |
| S1 | Governance | Decision rules, roles, amendment processes | Realized (ratified) |
| S2 | Architecture | Structure, boundaries, dependency law | Proposed (this document set) |
| S3 | Knowledge System | Recording state, rationale, registers, history | Realized |
| S4 | Language Definition | Specifications defining validity and meaning | Empty by design (blocked by D-01) |
| S5 | Compiler | Translation, diagnostics, optimization | Not begun (prototype pipeline out of scope, L-7) |
| S6 | Runtime | Spec-declared execution services | Not begun; required scope UNKNOWN (D-01) |
| S7 | Standard Library | Ratified, specified shipped capabilities | Not begun; scope UNKNOWN (D-01) |
| S8 | SDK | Versioned public developer interfaces | Not begun |
| S9 | Developer Tools | Editing, navigation, diagnostics via published contracts | Not begun |
| S10 | Build System | Deterministic orchestration | Not begun |
| S11 | Package Manager | Naming, versioning, distribution, resolution | Not begun; necessity UNKNOWN (D-01) |
| S12 | Testing | Correctness evidence of implementations | Prototype tests exist (historical context only) |
| S13 | Verification & Conformance | Implementation-independent conformance judgment | Model defined (Baseline §10); suite not begun |
| S14 | Documentation System | Human-readable derivation from ratified content | Minimal |
| S15 | Release & Distribution | Gate-checked publication | Not begun (blocked by CI, Article 9) |
| S16 | AI Layer | Artifact production/consumption via public interfaces | Active as contributor; artifact classes UNKNOWN (D-14) |

## 3. Subsystem Relationship Graph

```
S1 Governance
 └─► S2 Architecture
      └─► S4 Language Definition
           ├─► S5 Compiler ──────────┐
           ├─► S6 Runtime ───────────┤
           ├─► S7 Standard Library ──┤   (all judged by S13)
           ├─► S13 Verification ◄────┘
           └─► published contracts ─► S9 Tools, S10 Build, S11 Pkg Mgr, S16 AI
S5,S6,S7 ─► S8 SDK ─► end developers
S5,S12 ─► S10 Build ─► S15 Release
S13,S12 ─► S15 Release
S4..S15 ─► S14 Documentation (derived)
all ─► S3 Knowledge (derived recording)
```

**Cycles: none at subsystem level.** Known design co-dependencies (type /
ownership / concurrency; grammar / metaprogramming) are decision cycles
inside S4, resolved by iterative co-design during the RFC process; they
never become structural cycles between subsystems.

**Forbidden dependencies:** S4 → any implementation (L-1, L-7); S13 →
implementations as authority source (L-4); S5 ⟷ S6 private semantic
contracts (L-11); S16 → S1/S2/S4 by direct write (L-5); S14 → anything as a
definition source (L-2); any subsystem → S3 as authority (L-9).

## 4. Authority Graph

```
Constitution (S1)
  ▼
Architecture Baseline (S2)          ── A1: governance vs structure
  ▼
ADRs / accepted RFCs                ── A2: law vs decision record
  ▼
Specifications (S4)                 ── A3: decision vs definition ("the meaning line")
  ▼
Compiler · Runtime · Stdlib (S5–S7) ── A4: definition vs realization
  ▼
SDK · Tools · Build · Packages      ── A5: realization vs delivery
  ▼
Releases (S15)                      ── A6: delivery vs publication
  ▼
Applications / end users            ── A7: FCOS edge (authority ends here)
```

Authority crosses each boundary downward only. A3 is the most consequential
boundary: everything above it decides what is true; everything below is
judged against that truth. S13 sits beside A4 with delegated judging
authority derived from S4. S3 and S14 sit outside the authority chain
entirely.

## 5. Data Flow

```
Design intent (Issues, Decision Register)
  ▼
RFC (rationale) ─► ADR (binding record)
  ▼
Specification (normative content)
  ▼
Implementation Plan → Source Code (S5–S11)
  ▼
Testing evidence (S12) + Conformance judgment (S13)
  ▼
CI gate results
  ▼
Release (S15) → Release Notes
  ▼
Consumption → Documentation (S14), Knowledge mirror (S3)

Feedback (legal): consumption/testing/implementation ──(new Issue → new RFC)──► top
```

Illegal reverse flows: see Baseline §7 (named violations).

## 6. Control Flow

Authority (the right to decide) is strictly separated from execution (the
act of performing).

- **Maintainer** — terminal decision authority; positional, not personal.
- **Reviewers** — delegated, revocable gate authority; gate but do not own.
- **CI** — enforces mechanically; never decides; a CI change is never a
  policy change (L-10).
- **Compiler / Runtime / Build / Tools** — execute under total
  specification authority; diagnostics report, they do not rule.
- **Human developers and AI** — author proposals and code; control nothing
  until review passes; AI additionally never self-approves (L-5).
- **End users** — control only their own programs; influence FCOS solely
  via Issues.

## 7. Artifact Universe

| Artifact | Purpose | Authority | Lifecycle |
| --- | --- | --- | --- |
| Constitution | Governance rules | Rank 1 | Amended by its own process |
| Architecture Baseline | Structure and law | Rank 2 | MAJOR.MINOR, amended via RFC + ADR |
| Master System Blueprint | Whole-system description | Descriptive only | Revised with MAJOR Baseline changes |
| Universal Engineering Doctrine | Axioms and rationale | Explanatory only | Amended by supersession |
| ADR | Binding record of one decision | Rank 3 | Immutable after acceptance; superseded, never edited |
| RFC | Proposal and rationale | Rationale only | Draft → In Review → Accepted/Rejected/Withdrawn → Implemented |
| Specification | Sole definition of meaning in scope | Rank 5 (normative) | Draft → In Review → Ratified → Deprecated |
| Conformance Suite | Implementation-independent judge | Delegated judging | Versioned with spec clauses |
| Test Suite | Evidence for one implementation | None (evidence) | Continuous with code |
| Implementation Plan | How ratified content is built | None | Per work item |
| Source Code | Realization | None | Continuous, PR-gated |
| Binary / build artifact | Executable output | None | Generated, reproducible, disposable |
| Package | Distributable unit (format UNKNOWN) | None | Published → yanked/superseded |
| Release | Gate-checked published version | None | Assembled → published → superseded |
| Release Notes | Change enumeration | None | Immutable after publication |
| Documentation | Human explanation | None (informative) | Regenerated; corrected freely |
| Issue | One unit of work or defect | None | Open → Closed |
| Decision Register / Risk Register / Operations Log / Glossary | Living records | None (derived) | Continuous |
| CI Configuration | Mechanical gate encoding | None (enforcement) | Follows gate decisions |

Artifact classes not listed (e.g. "playbooks", "prompts") have no standing
until ratified or retired (D-14 — UNKNOWN).

## 8. Interface Universe

Architectural boundaries only; all forms are UNKNOWN until specified.

- **Human:** governance review surface (PRs, RFC review); knowledge
  workspace (mirror); published documentation; release channels.
- **Specification → machine:** machine-readable expression of ratified
  contracts; existence is an architectural requirement for scalable
  conformance; form UNKNOWN (U-9).
- **Compiler boundary:** invocation, input acceptance, artifact emission,
  diagnostics contract. UNKNOWN.
- **Syntax-tree / tooling contract:** the published structure tools may
  consume; tools need only grammar, AST, diagnostics — never internals.
  UNKNOWN.
- **Compiler ↔ runtime boundary:** exclusively spec-defined contracts
  (L-11); intermediate artifact publication UNKNOWN.
- **Runtime embedding boundary:** required only if D-01 yields an executed
  language. UNKNOWN.
- **SDK surface:** the only supported programmatic entry for developers and
  AI alike.
- **Conformance harness boundary:** how any implementation is submitted for
  judgment; implementation-independent by construction.
- **Package registry boundary:** conditional on D-01. UNKNOWN.
- **Repository interface:** branches, PRs, protected `main`; the sole write
  path into authoritative artifacts.
- **Knowledge interface:** one-way authority, repository → mirror.
- **AI interface:** architecturally defined as the absence of a special
  interface (Baseline P-4).

## 9. Trust Boundaries

| Boundary | Assumption | Isolation requirement |
| --- | --- | --- |
| Human ↔ AI | AI output untrusted until human review | No self-approval; identical PR/review gates; no AI-only channels into rank 1–5 artifacts |
| AI ↔ Repository | Write access mediated, logged, attributable | Branch protection; attribution; direct-to-main only by explicit recorded Maintainer exception |
| Specification ↔ Implementation | Implementations defective until proven | Conformance suite is the judge; spec never editable from the implementation side without RFC |
| Compiler ↔ Runtime | Neither trusts unspecified behavior | Spec-defined contracts only (L-11) |
| Testing ↔ Release | Releases trust only mechanical gate results | CI results are the sole admissible evidence; no unrecorded overrides |
| Knowledge ↔ Source of truth | Mirror assumed stale when in conflict | One-way authority (L-9) |
| Documentation ↔ Meaning | Docs assumed potentially wrong | Behavior claims valid only if traceable to a ratified clause |
| Prototype ↔ Design | Historically informative, never normative | L-7 |
| FCOS ↔ External world | Outside guarantee scope | Assertions limited to ratified specs and published conformance statuses |

## 10. Scalability Model

The architecture is population- and volume-independent because: authority
is positional, not personal; meaning has one home judged by one
implementation-independent suite; volume is absorbed by indexed registers,
not core documents; traceability is machine-checkable; the contribution
path is uniform for contributor #1 and contributor #500, human or AI;
subsystem boundaries follow authority lines, so ownership shards cleanly.

Scale-critical prerequisites (recorded requirements, designs UNKNOWN):
namespace-capable identifiers (D-03) and machine-checkable traceability.

## 11. Failure Containment

Failures propagate only along authority edges, and authority edges point
one way. A defect below the meaning line (A3) can never rewrite anything
above it.

| Failure | Containment | Blast radius |
| --- | --- | --- |
| Compiler bug | Spec defines correctness; conformance suite detects; fixed toward spec (L-2) | One implementation |
| Runtime bug | Same asymmetry; no lateral contracts (L-11) | One runtime |
| AI hallucination | Untrusted-until-reviewed boundary; cannot reach rank 1–5 without ratification | Derived artifacts at worst |
| Documentation error | Informative only; claims trace to clauses or are invalid | Reader confusion; zero meaning drift |
| Repository corruption | Content-addressed, distributed history; mirror as secondary evidence | Recoverable |
| Knowledge inconsistency | Resolves toward repository mechanically (L-9) | Workspace only |
| Test defect | Cannot redefine behavior (L-4) | Assurance layer only |
| Gate bypass | Violation requiring recorded one-time exception | Single recorded event |
| Bad architectural decision | Superseded, never edited; history preserved | Bounded and reversible |

## 12. Architectural Invariants

1. **INV-1** Architecture never depends on implementation.
2. **INV-2** Specifications always own meaning; implementations realize and never redefine it.
3. **INV-3** The compiler never defines language behavior.
4. **INV-4** Tests never define semantics; a test contradicting the spec is the defect.
5. **INV-5** AI never defines meaning; AI content enters authoritative artifacts only through the human decision path.
6. **INV-6** Repository structure carries no decision authority.
7. **INV-7** Prototypes are never precedent.
8. **INV-8** Decisions bind only as ADRs.
9. **INV-9** Mirrors are derived; the repository copy is authoritative.
10. **INV-10** Gates are declared above CI and enforced by it; CI never makes policy.
11. **INV-11** No lateral semantic contracts between implementations.
12. **INV-12** Ratified vocabulary is binding across all artifacts.
13. **INV-13** Authority flows downward only; feedback enters as new proposals at the top.
14. **INV-14** Every artifact type has exactly one purpose.
15. **INV-15** Authority is positional, never personal.
16. **INV-16** One implementation-independent conformance judge exists for all implementations.
17. **INV-17** Every shipped behavior is traceable to a ratified specification clause.
18. **INV-18** Accepted decision records are immutable; correction happens by supersession.
19. **INV-19** The AI layer holds no privileged interface; human and AI contributions traverse identical gates.
20. **INV-20** Exceptions to any invariant are explicit, recorded, one-time, and never precedent.

## 13. Evolution Model

- **Adding a subsystem:** RFC demonstrating necessity → Baseline amendment
  placing it in the layer model with ownership and forbidden
  responsibilities → ADR recording adoption — before any implementation
  exists.
- **Retiring a subsystem:** deprecation is a status, not a deletion; an ADR
  records retirement; artifacts move to Deprecated with successor pointers;
  history remains.
- **Interface evolution:** published contracts are versioned; any
  consumer-observable contract change is a decision-level event (RFC path).
  Transition policy: UNKNOWN (future governance RFC).
- **Compatibility evolution:** the compatibility/stability policy is
  UNKNOWN (U-6); the architecture fixes only where it lives — ratified
  specifications and release governance, never implementation accidents.
- **Architecture change:** by Baseline §13; the Blueprint is revised
  whenever a MAJOR Baseline change lands.

## 14. Future Unknowns

| # | Unknown | Why it exists | Resolving decision | Owning artifact |
| --- | --- | --- | --- | --- |
| U-1 | Language identity and scope | Deliberately deferred; controls nearly every downstream decision | D-01 | ADR + RFC-0001 |
| U-2 | Identifier and namespace scheme | Must be namespace-capable for scale | D-03 | ADR |
| U-3 | `specs/fcos/` vs `docs/specifications/` disposition | Two candidate homes; scaffold has no authority | D-13 | ADR |
| U-4 | Status of "playbooks"/"prompts" AI artifact classes | Present in tree without ratification | D-14 | ADR |
| U-5 | Conformance levels/classes | Baseline gives the model, not the levels | D-04 | RFC + Specification |
| U-6 | Compatibility and stability policy | Guarantee-defining; premature before U-1 | Future RFC | RFC + ADR + release governance |
| U-7 | Reference-implementation policy | Determines how implementations are staffed and judged | Future RFC | RFC + ADR |
| U-8 | Package distribution model | Conditional on U-1 | Future RFC | RFC + Specification |
| U-9 | Machine-readable specification format | Required for scalable conformance | Future RFC | RFC + Specification |
| U-10 | Language versioning scheme | Distinct from artifact versioning | Future RFC | RFC + ADR |
| U-11 | Multi-maintainer governance procedure | Single-maintainer processes will not scale | Future governance RFC | RFC + Constitution amendment |
| U-12 | CI platform and gate encoding | Gates declared but not yet enforced (Article 9 dependency) | Engineering decision + ADR if architectural | Implementation Plan / ADR |
| U-13 | Third-party conformance certification | Relevant when external implementations exist | Future RFC | RFC + governance artifacts |
| U-14 | Runtime necessity and scope | Follows from D-01 | D-01 consequence | ADR + Specifications |

Rule: no unknown may be resolved implicitly by shipping behavior that
presumes an answer.