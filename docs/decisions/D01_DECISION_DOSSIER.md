# D-01 Decision Dossier — Language Identity and Design Philosophy

**Artifact class:** Decision-support dossier — carries **no decision
authority** (Blueprint §7) and contains **no recommendation, no ranking,
and no invented option** (Maintainer mission, 2026-08-06). It compiles,
quotes, and traces what the repository already records. The decision and
its recording ADR are the Maintainer's alone (Constitution Article 6,
Article 7, INV-8).
**Relationship to `D01_DECISION_BRIEF.md`:** this dossier extends the
merged brief (PR #18, 2026-08-05) into the complete eighteen-section
record ordered by the Maintainer. Both documents restate the same merged
sources; neither carries authority; the brief is not superseded.
**Notation:** the future RFC-0001 acceptance ADR does not yet exist. It
is written throughout as `ADR-0006` (code-formatted) because the merged
ID gate (`tools/checks/check_ids.py`, RFC-0011 E-A) requires plain ADR
identifiers in scanned documents to resolve to existing files.
**Repository state at compilation:** `main` = `e300f506`
(2026-08-05, merge of PR #21). PRs #10–#21 merged and authoritative; no
open pull requests; `docs/decisions/` contains ADR-0001..ADR-0005 and
`D01_DECISION_BRIEF.md`.

---

## 1. Decision statement

As recorded in RFC-0001 (Summary), verbatim:

> Decide what the Frontier Specification Language (FSL) *is*: its purpose,
> its intended consumers, its success criteria, and consequently which
> downstream subsystems (runtime, package manager, stdlib scope) exist at
> all. This is the controlling unknown of the project; nearly every other
> registered unknown is downstream of it.

Identity of the decision across registers (RFC-0001 header):
**Resolves: U-1 (D-01)** — D-01 in the Decision Register = U-1 in
Blueprint §14. **Controls: U-5, U-6, U-8, U-9, U-10, U-14.**
Risk framing (RFC-0001 §Motivation, verbatim):

> Risk R-1 (identity ambiguity) is rated Critical: without this decision,
> any implementation work resolves the unknown by accident (CN-14).

The recording act is a single Maintainer-authored acceptance ADR
(`ADR-0006`). Per ADR-0004 (RFC-0012 row, verbatim): *"Procedural
ruling: runtime scope (U-14) is resolved inside the future RFC-0001
acceptance ADR, not separately."* Per PROGRAM.md §4, G-D01 (the identity
decision plus its acceptance ADR) is the **OPEN — controlling** gate of
the entire program.

## 2. Exact governing artifacts

| Artifact | Governing role for D-01 |
| --- | --- |
| `docs/constitution/` Article 6 | Sole decision authority: the Maintainer |
| `docs/constitution/` Article 7 · Baseline L-8 · INV-8 | ADR-binding: "no RFC resolves anything until its acceptance is recorded as an ADR" (ADR-0004 §Context) |
| `docs/architecture/` Blueprint §14 (U-1), §2 (S4, S6), §7 (artifact classes/lifecycle), §8 (interface forms UNKNOWN) | Registers the unknown; fixes artifact authority and lifecycle |
| `docs/architecture/` Baseline §8 (category routing), §13 (amendment path) | Routes identity-class decisions; sole path for subsystem retirement |
| `docs/architecture/` Doctrine §4, §14 — CN-14, DP-15 | No implicit resolution; deferral requires a recorded review date |
| `docs/rfc/RFC-0001.md` | The decision frame: design space, assumptions A-1..A-3, open questions Q1–Q4, consequences. Carries **no recommendation** by design |
| `docs/rfc/RFC-0012.md` | U-14 scope space (S-A/S-B/S-C) and its coherence table; routed into `ADR-0006` by ADR-0004 |
| `docs/rfc/RFC-0005.md` · `docs/rfc/RFC-0007.md` · `docs/rfc/RFC-0009.md` | The blocked decision windows D-01 opens (U-6, U-8, U-10) |
| `docs/decisions/ADR-0004.md` | Dispositions: interim rules P-D (U-6) and V-D (U-10) in force; N-defer (U-8) accepted with decision "at or after RFC-0001 acceptance"; U-14 routing; RFC-0001 recorded as **remaining open** |
| `docs/decisions/ADR-0005.md` | Spec corpus home `/specs` (with ADR-0003 amendment of taxonomy) |
| `docs/program/PROGRAM.md` §4 (gates: G0, G-D01, G-CI, G-SPEC(x), G-CONF), §6 (blockers B-01..B-11), §7 (change process) | Gate and blocker registers; gate-state changes are recorded by PR |
| `docs/program/DEPENDENCY_GRAPH.md` | Edge list, critical path, standing lanes |
| `docs/program/WORK_BREAKDOWN_STRUCTURE.md` | Package rows with Blocked-by markers (P00–P15) |
| `docs/program/CONFORMANCE_FRAME.md` §2 | P12.2+ blocked by G-SPEC(S13) and B-08 |
| `specs/README.md` + S04, S05, S06, S07, S11, S12, S13 | Specifiability index and blocked-section convention |
| `docs/decisions/D01_DECISION_BRIEF.md` | The merged compact decision brief this dossier extends |

## 3. Complete dependency graph

Upstream of the decision, everything required is already merged: the
frame (RFC-0001), the routed sub-decision space (RFC-0012), the
dispositions (ADR-0004), and the decision brief. **No engineering input
remains outstanding; the sole missing input is the Maintainer act.**

```text
RFC-0001 (frame; no recommendation)      RFC-0012 (U-14 space; routed by ADR-0004)
            \                                /
             ▼   Maintainer decision (Article 6)   ▼
        `ADR-0006` — records: identity (U-1/D-01) · U-14 resolution or explicit
        re-deferral · answers/re-deferrals for RFC-0001 Q1–Q4 · the mandatory
        RFC-0007 packaging review outcome or its scheduling
            │
            ├─ closes gate G-D01 (PROGRAM.md §4: "OPEN — controlling")
            ├─ closes blockers B-01, B-02 (PROGRAM.md §6; see §8 below)
            ├─ opens decision windows: RFC-0005 (U-6 full policy),
            │  RFC-0007 (U-8 review), RFC-0009 (U-10 scheme)
            ▼
        P03 Language Definition (Wave 1) — the only program made newly
        executable at once (DEPENDENCY_GRAPH topological order)
            ├─ first use of RFC-0002 clause-ID scheme (N-B + N-C)
            ├─ RFC-0008 M-B machine-readable clause index
            ├─ S04 blocked sections unblock; TODO(blocked-by:) markers
            │  discharge progressively across the corpus
            ▼
        G-SPEC(x) per ratified spec → P04 compiler → P11/P12 evidence and
        judgment → P14 first gate-checked release (G-CI also required)
```

Critical path (DEPENDENCY_GRAPH §2, as quoted in the brief): decision →
P03 ratified clauses + clause index → P04 conforming compiler → P11/P12
evidence + judgment → P14 first gate-checked release; and *"No
engineering acceleration shortens it while G-D01 is open."* The options
change the **volume** traversing that path, not its order (brief §4).

**Independent of D-01** (edges that do not pass through G-D01): standing
lanes P00/P02/P13.1/P15.1–.2; P01.5/P01.6 (Maintainer console, G-CI);
B-09 (RFC-0014/RFC-0015, both "remaining open" per ADR-0004 for reasons
unrelated to identity); B-10 (no ratified performance requirement); B-11
(`specs/fcos/` disposal); P12.2/P12.4 (G-SPEC(S13) + B-08 per
CONFORMANCE_FRAME §2, discharged only as Wave 1 ratifies specs).

## 4. Every downstream package affected

Per WORK_BREAKDOWN_STRUCTURE.md (post-PR #21 state) and
DEPENDENCY_GRAPH.md:

| Package | Effect of `ADR-0006` | Source |
| --- | --- | --- |
| P03 Language Definition | Entry gate G-D01 discharged — newly executable at once | WBS P03.0; DEPENDENCY_GRAPH topological order |
| P04 Compiler | Reachable; still gated on ratified clauses (G-SPEC) | WBS; DEPENDENCY_GRAPH critical path |
| P05 Runtime | **Existence decided** in the same act (U-14: void, minimal, or full) | RFC-0012; ADR-0004 routing |
| P06 Standard Library | Reachable per identity scope; gated on ratified specs | WBS; RFC-0001 design-space consequences |
| P07/P08/P09 (SDK, tools, build) | Reachable per later ratified contracts (B-06 survives) | WBS; Blueprint §8 |
| P10 Package Manager | Existence decided at the mandatory RFC-0007 review | ADR-0004 (N-defer); RFC-0007 |
| P11.4 Performance evidence | Unaffected — blocked by B-10 regardless | WBS P11.4 |
| P12.2/P12.4 Conformance suite | Unaffected directly — blocked by G-SPEC(S13) + B-08; discharged as Wave 1 ratifies | CONFORMANCE_FRAME §2; WBS (reconciled by PR #21) |
| P12.3 | Blocked by P03.4 — becomes reachable via P03 | WBS P12.3 |
| P13.2/P13.3 Derived docs | P13.2 partially unblocks once the P03.2 clause-ID scheme is in first use (its gate-set expansion remains a separate RFC-0011 E-A decision); P13.3 follows P03 | WBS; PR #19 record |
| P14 Release | Reachable via RFC-0009 (P14.3) and RFC-0005 (P14.4) windows; P14.0 still requires G-CI | WBS P14 rows |
| P15.3 | Unaffected — blocked by RFC-0014/RFC-0015 | WBS P15.3 |
| P00/P01/P02/P13.1/P15.1–.2 | Continue as standing/maintainer lanes under every option | DEPENDENCY_GRAPH standing lanes |

## 5. Every RFC dependent on D-01

| RFC | Dependency (recorded) | Present disposition (ADR-0004) |
| --- | --- | --- |
| RFC-0001 | The frame itself; "deliberately records no recommendation; resolution requires a dedicated Maintainer decision and its own ADR (roadmap Step 10)" | **Remaining open** |
| RFC-0005 | Full compatibility policy blocked: "the identity fixes who the consumers are" (RFC-0005 §Consequences) | Interim P-D instability window **in force** |
| RFC-0007 | "Whether package distribution exists is decided at or after RFC-0001 acceptance" | N-defer **accepted**; review mandatory |
| RFC-0009 | Versioning scheme blocked; declaration syntax is D-01-dependent (RFC-0009 Q1) | Interim V-D (no language version pre-1.0) **in force** |
| RFC-0012 | "Not decidable before RFC-0001; this RFC pre-commits the decision space so that RFC-0001's acceptance ADR can resolve U-14 in the same act or explicitly re-defer it with a review point" | Procedural routing **accepted** |

Not dependent on D-01: RFC-0002 and RFC-0008 (accepted; awaiting first
use in P03); RFC-0014 and RFC-0015 (open — options unchosen / blocked on
an L-12 definition, both independent of identity); all other RFCs
disposed by ADR-0004.

## 6. Every Specification dependent on D-01

Corpus-level assumption 2 (`specs/README.md`, verbatim):

> **D-01 remains unrecorded.** RFC-0001 deliberately carries no
> recommendation. Every identity-dependent statement in this corpus is
> BLOCKED, never assumed (CN-14).

Index rows (verbatim "Specifiability today" values):

| Spec | Specifiability today | D-01 dependency |
| --- | --- | --- |
| S04-language-definition.md | Frame only (D-01) | Direct — content sections blocked |
| S05-compiler.md | Obligations only (D-01, G-7) | Direct — compiler boundary follows identity |
| S06-runtime.md | Obligations only (U-14) | Direct via U-14 (resolved inside `ADR-0006`) |
| S07-standard-library.md | Obligations only (D-01) | Direct — stdlib scope follows identity |
| S11-package-manager.md | Existence undecided (U-8) | Via the mandatory RFC-0007 review opened by `ADR-0006` |
| S12-testing.md | Architecture full; content blocked | Indirect — test content needs ratified clauses (P03) |
| S13-verification-conformance.md | Model full; suite blocked | Indirect — suite needs clause IDs (B-08 discharge via P03) |

Unblocked-by-other-events only: S15 (gate frame, CI pending — G-CI, not
D-01). Already Full: S01, S02, S03, S14, S16. Retirement outcomes: if
S-A, S06 is retired via the Baseline §13 amendment path; if N-no, S11
likewise (S06/S11 acceptance criteria; brief §5–§6).

## 7. Every Program package gated by D-01

Directly gated (Blocked-by names G-D01 or a same-act unknown):
**P03.0-entry** (G-D01); **P05** existence (U-14); **P10** existence
(U-8). Transitively gated (blocker discharges only through P03/Wave 1 or
a window `ADR-0006` opens): **P04**, **P06**, **P07**, **P08**, **P09**
(entry gates + B-06 contracts); **P12.3** (P03.4); **P13.2** (P03.2
first-use precondition), **P13.3** (P03); **P14.3** (RFC-0009), **P14.4**
(RFC-0005). Gated by other authorities and **not** by D-01: P00.1
(B-11), P00.4/P00.5 and P01.5/P01.6 (Maintainer console), P11.4 (B-10),
P12.2/P12.4 (G-SPEC(S13)+B-08), P14.0 (G-CI), P15.3 (RFC-0014/0015).
Source: WORK_BREAKDOWN_STRUCTURE.md rows at `e300f506`;
DEPENDENCY_GRAPH.md edge list.

## 8. Every blocker that disappears after D-01

Per PROGRAM.md §6 and the brief §10 (which this table restates):

| Blocker | Closure condition | Note |
| --- | --- | --- |
| B-01 — D-01 undecided | Closes on acceptance of **any** identity (I-A/I-B/I-C/I-D) | Survives only under DEFER |
| B-02 — U-14 runtime unknown | Resolved **in the same act** (void or scoped per the recorded space) | Unless `ADR-0006` explicitly re-defers it with a review point (RFC-0012 §Consequences) — then it survives with a recorded date |

No other blocker in the register closes on D-01 alone.

## 9. Every blocker that survives D-01

| Blocker | Survival (recorded) |
| --- | --- |
| B-03 packaging deferral | Review opens; remains until RFC-0007 is decided (re-deferral admissible) |
| B-04 compatibility policy | Decidable; remains until the 1.0 family is decided (interim P-D window stays in force) |
| B-05 versioning scheme | Decidable; remains until decided with RFC-0005 (V-D stays in force) |
| B-06 interface forms UNKNOWN | Remains until each interface spec ratifies (Blueprint §8) |
| B-07 conformance levels | Remains — future work post-RFC-0001 (ADR-0004, RFC-0004 row) |
| B-08 specs not ratified | Remains; P03 begins discharging it clause by clause |
| B-09 memory/context undecided | Remains — RFC-0014/RFC-0015 are independent of D-01 |
| B-10 no ratified performance requirement | Remains until a ratified spec supplies one |
| B-11 `specs/fcos/` disposal | Remains — orthogonal Maintainer decision |

Under DEFER, **all eleven** blockers remain, including B-01 and B-02
(brief §10, final column).

## 10. Every architectural invariant that constrains D-01

| Constraint | Recorded statement | Source |
| --- | --- | --- |
| Article 6 | The Maintainer is the sole decider | Constitution; ADR-0004 header ("Decider: Maintainer (Constitution Article 6)") |
| Article 7 · L-8 · INV-8 | "no RFC resolves anything until its acceptance is recorded as an ADR" | ADR-0004 §Context |
| P-1 · L-2 (A-1) | "The language specification is authoritative; implementations conform to it … This holds under every alternative." | RFC-0001 §Assumptions |
| L-3 | "If a runtime exists, its observable behavior is spec-defined and it holds zero defining authority" | RFC-0012 A-1 |
| L-7 · INV-7 (A-2) | "The Phase 0 prototype … is historical context only and constrains nothing (L-7; Maintainer ruling 2026-08-01)" | RFC-0001 §Assumptions |
| A-3 | The name FSL "does not by itself decide identity; treating the name as evidence would be inference from a label, not a decision" | RFC-0001 §Assumptions |
| CN-14 | No implicit resolution: "without this decision, any implementation work resolves the unknown by accident" | RFC-0001 §Motivation; Doctrine |
| DP-15 | "Deferral: legitimate (DP-15) but must be recorded with a review date; all implementation remains blocked (CN-14)" | RFC-0001 §Consequences |
| INV-19 · CN-23 | AI systems as symmetric first-class consumers is Q1 of the decision; bounds reaffirmed by the RFC-0016 rejection (A-A) | RFC-0001 Q1; ADR-0004 §Rejected |
| R-A (RFC-0006) | "No implementation is designated a reference implementation with defining authority" — constrains every identity's implementation path | ADR-0004 disposition table |
| Baseline §13 | Subsystem retirement (S6 under S-A; S11 under N-no) is an architecture change via the amendment path — beyond the spec itself | RFC-0012 S-A row; brief §5 |
| Blueprint §7 · INV-18 | Retirement migrates by supersession, never deletion: Deprecated status with successor pointer | brief §7 |
| L-A + C-A · INV-16 | Binary conformance judgment + self-certification frame is already ratified; conformance *levels* remain future work post-RFC-0001 | ADR-0004 (RFC-0004 row); CONFORMANCE_FRAME |
| L-12 | Vocabulary discipline blocks RFC-0015 independently of D-01 | ADR-0004 §Remaining open |

## 11. Every admissible option already recorded in repository history

**Identity options** — RFC-0001 §Design Space, order preserved, identity
column verbatim:

| # | Identity (verbatim) |
| --- | --- |
| I-A | Specification/definition language: programs are structured definitions (specs, contracts, artifacts) consumed by tools |
| I-B | General-purpose programming language |
| I-C | Domain-specific language for creative-systems orchestration |
| I-D | Interchange/definition core (I-A) with staged evolution path toward executable semantics |
| DEFER | Recorded deferral with a review date — named admissible by RFC-0001 §Consequences: "Deferral: legitimate (DP-15) but must be recorded with a review date; all implementation remains blocked (CN-14)" |

No other identity option appears in any repository document; per the
mission's no-invention rule, none is added here.

**Coupled sub-decision spaces** (recorded; constrained by, not identical
to, the identity choice):

| Unknown | Recorded space | Source | In force today |
| --- | --- | --- | --- |
| U-14 runtime scope | S-A no runtime (S6 retired by Baseline amendment) · S-B validation/evaluation runtime · S-C full execution environment (scheduling, I/O, resource model) | RFC-0012 §Design Space | — (routed into `ADR-0006`) |
| U-8 packaging | N-yes · N-no · N-defer | RFC-0007 | N-defer accepted; review mandatory (ADR-0004) |
| U-6 compatibility | P-A strong backward compatibility · P-B editions · P-C semver-style · P-D interim instability window then one of the former | RFC-0005 | P-D window in force (ADR-0004) |
| U-10 language versioning | V-A monotonic · V-B semver-like · V-C date editions · V-D no language version pre-1.0 | RFC-0009 | V-D in force (ADR-0004) |

## 12. Every recorded consequence for every option

Common to accepting **any** of I-A/I-B/I-C/I-D (RFC-0001 §Consequences,
verbatim): *"Accepting any alternative unblocks: RFC-0005, 0007, 0008,
0009, 0012 for decision; S4 specification work; the RFC-count roadmap."*
(RFC-0002 and RFC-0008 have since been accepted by ADR-0004 and await
first use; the remaining windows are RFC-0005/0007/0009, with RFC-0012
routed into the same act.) Common migration facts: no code migration
exists under any option (RFC-0001 A-2; L-7) and no consumer migration
exists today (V-D and the P-D window in force; brief §7).

**I-A — definition language**
- Consequences (RFC-0001, verbatim): "Runtime likely minimal or absent (U-14 small); packaging may reduce to document distribution (U-8 small); conformance = validation semantics"
- Trade-offs (verbatim): "Smallest surface, fastest to specify; lowest expressive ambition; risk of under-serving future needs"
- Engineering (brief §4): smallest surface — S04 content + validation-semantics conformance; S05 bounded by validation identity; P05 small or void; distribution possibly repository/release artifacts only
- Governance (brief §5): with S-A, S6 retirement travels the Baseline §13 amendment path
- Repository (brief §6): with S-A, S06 → Deprecated with successor pointer
- Maintenance (brief §8): smallest maintained surface; recorded risk of under-serving future needs

**I-B — general-purpose language**
- Consequences (verbatim): "Full runtime, stdlib, packaging, versioning all required; RFC volume ≈45–70 (Phase 2 estimate)" — RFC-0012 S-C row: "the Phase 2 45–70 RFC estimate mostly lives here"
- Trade-offs (verbatim): "Maximal ambition and cost; decades-scale commitment; highest risk under a sole maintainer"
- Engineering (brief §4): largest — full S06 (S-C), full S07, likely S11 machinery; the RFC roadmap dominates engineering
- Governance (brief §5): largest standing volume — the roadmap all travels RFC → ADR
- Maintenance (brief §8): single-maintainer reality (OB-4) echoed in RFC-0012 Q3

**I-C — domain-specific language**
- Consequences (verbatim): "Runtime scope moderate and domain-shaped; stdlib is domain library; conformance suites domain-specific"
- Trade-offs (verbatim): "Requires defining the domain precisely first — a sub-decision as hard as D-01 itself"
- Engineering (brief §4): moderate, domain-shaped S06/S07; a precise domain definition precedes any clause work
- Governance (brief §5): requires a prior recorded domain-definition decision
- Maintenance (brief §8): the domain definition becomes a maintained artifact whose drift is identity-scale

**I-D — staged core**
- Consequences (verbatim): "Defers execution decisions without foreclosing them; versioning scheme must encode capability stages (U-10 interaction)"
- Trade-offs (verbatim): "Two-phase identity risks permanent limbo; staging discipline must be ratified up front"
- Engineering (brief §4): I-A-scale engineering now plus staging machinery
- Governance (brief §5): each stage transition is a future decision event
- Migration (brief §7): future migration between capability stages is a designed-in obligation

**DEFER**
- Consequences (RFC-0001 §Consequences): review date mandatory (DP-15); all implementation remains blocked (CN-14)
- Engineering (brief §4): zero new engineering — Wave 0 standing lanes remain the only executable work
- Governance (brief §5): a recorded deferral with review date; G-D01 stays open; no other governance change is admissible
- Maintenance (brief §8): "The blocked state itself is maintained: review dates, Wave-0-only activity, and Critical risk R-1 remain open indefinitely"

## 13. Cross-impact matrix

The U-14 column reproduces RFC-0012's coherence table, which is
**descriptive, not binding** — `ADR-0006` records the actual resolutions
(RFC-0012 §Design Space; brief §2).

| Option | U-14 coherence | U-8 signal | S04 | S05 | S06 | S07 | S11 | P05 | P10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I-A | S-A or S-B | "may need only document distribution" (RFC-0007) | Content unblocks | Bounded by validation identity | Retired (S-A, via Baseline §13) or minimal (S-B) | Scoped small | Decided at RFC-0007 review | Void or minimal | Small/likely unneeded — decided at review |
| I-B | S-C | Full packaging space opens | Content unblocks | Full compiler contract | Full (S-C) | Full stdlib | Decided at RFC-0007 review | Exists (S-C) | Decided at review |
| I-C | S-C (domain-shaped) | Domain-shaped | Content unblocks after prior domain definition | Domain-shaped | Moderate, domain-shaped | Domain library | Decided at RFC-0007 review | Exists (S-C) | Decided at review |
| I-D | S-B | Staged | Content unblocks + must encode the stage model | Bounded per stage | Minimal now (S-B) | Per stage | Decided at RFC-0007 review | S-B per coherence | Decided at review |
| DEFER | — open | — deferred | Blocked | Blocked | Blocked | Blocked | Blocked | — | — |

Recorded cross-couplings between the opened windows:
- RFC-0009 V-C is "meaningless unless" RFC-0005 P-B is adopted (brief §2, from RFC-0009)
- The version-declaration syntax is itself D-01-dependent (RFC-0009 Q1)
- Whether a runtime's diagnostic surface joins the compatibility promise is RFC-0012 Q2 → RFC-0005 Q1
- I-D forces the U-10 scheme to encode capability stages (RFC-0001 I-D row)
- "The identity fixes who the consumers are" (RFC-0005 §Consequences) — the compatibility family choice is downstream of every identity branch

## 14. Risk matrix

Only risks already recorded in merged artifacts; ratings appear only
where the repository records one. Program-level register:
`docs/program/RISK_REGISTER.md`.

| Scope | Recorded risk | Recorded rating | Source |
| --- | --- | --- | --- |
| The undecided state | R-1 identity ambiguity — "any implementation work resolves the unknown by accident" | **Critical** | RFC-0001 §Motivation |
| I-A | "risk of under-serving future needs" | — | RFC-0001 trade-offs |
| I-B | "decades-scale commitment; highest risk under a sole maintainer" (OB-4; RFC-0012 Q3) | — | RFC-0001 trade-offs |
| I-C | Domain definition is "a sub-decision as hard as D-01 itself"; its drift is identity-scale | — | RFC-0001 trade-offs; brief §8 |
| I-D | "Two-phase identity risks permanent limbo"; standing staging-discipline duty | — | RFC-0001 trade-offs; brief §8 |
| DEFER | R-1 remains open indefinitely; blocked state itself must be maintained | Critical (R-1 persists) | RFC-0001; brief §8 |
| Cross-cutting | The RFC-0005 1.0 family eventually chosen (P-A heavy cost on early mistakes / P-B machinery / P-C ecosystem fragmentation) sets the dominant long-run cost profile for whichever identity is selected | — | brief §8 |

## 15. Decision tree

Branch order reproduces RFC-0001's own table order, then DEFER as
RFC-0001 §Consequences lists it. The tree ranks nothing.

```text
D-01 (U-1) — Maintainer act (Article 6), recorded as `ADR-0006` (Article 7)
│
├─ Accept I-A — definition language
│    U-14 coherence: S-A or S-B (RFC-0012, descriptive)
│    ├─ S-A → S6 retirement via Baseline §13 amendment path (RFC-0012 S-A row)
│    └─ S-B → boundary with S13 conformance tooling "must be drawn precisely" (RFC-0012 S-B row)
├─ Accept I-B — general-purpose language
│    U-14 coherence: S-C; ≈45–70 RFC roadmap mostly in S-C (RFC-0012 S-C row)
├─ Accept I-C — domain-specific language
│    prior recorded sub-decision: precise domain definition (RFC-0001 I-C row)
│    U-14 coherence: S-C, domain-shaped
├─ Accept I-D — staged core
│    staging discipline ratified up front (RFC-0001 I-D row)
│    U-14 coherence: S-B; U-10 scheme must encode stages
│
│  on every Accept branch, inside the same act:
│  • resolve U-14 or explicitly re-defer with a review point (RFC-0012 §Consequences)
│  • answer or explicitly re-defer Q1–Q4 (RFC-0001 §Open Questions)
│  • conduct or schedule the mandatory RFC-0007 packaging review
│    (ADR-0004: "at or after RFC-0001 acceptance")
│  • decision windows open: RFC-0005 full policy, RFC-0009 scheme
│    (interim P-D and V-D remain in force until superseded)
│
└─ DEFER (DP-15)
     record a review date; all implementation remains blocked (CN-14);
     R-1 stays open; G-D01 stays open; the tree re-enters at the review date
```

## 16. Wave 1 activation sequence

1. `ADR-0006` merges into `docs/decisions/` — Maintainer-authored, via
   feature branch and PR (the single recorded path, CONTRIBUTING.md;
   Article 7).
2. PROGRAM.md revision PR: §4 gate table (G-D01) and §6 blocker register
   (B-01, B-02) updated — "PROGRAM.md is revised by PR because a gate
   changes state" (PROGRAM.md §7, as quoted in the brief §6).
3. Knowledge-mirror sync runs (P02.3) — trigger: governance merge
   (KNOWLEDGE_SYNC_RUNBOOK).
4. P03 entry discharges. First use of the RFC-0002 clause-ID scheme
   (N-B + N-C) and the RFC-0008 M-B machine-readable clause index.
5. Specification production flow begins (S04 §Sequence flows, as quoted
   in the brief §6): acceptance ADR → spec charter → Draft → In Review →
   ratification ADR → suite tracing → implementations authorized.
6. `TODO(blocked-by:)` markers referencing the identity decision
   discharge progressively as specification work proceeds
   (`specs/README.md` conventions; ADR-0004 §Consequences).
7. Per ratified spec: G-SPEC(x) met → P04 begins; P12.2/P12.4 discharge
   as S13 ratifies and clause IDs exist (B-08); P12.3 follows P03.4
   (CONFORMANCE_FRAME §2; WBS).
8. On their own tracks: the mandatory RFC-0007 review decides P10
   existence; RFC-0005 and RFC-0009 full decisions precede P14.4 and
   P14.3 respectively.
9. Throughout: P14.0 additionally requires G-CI — required status checks
   enabled by Maintainer console action (P01.5) — independent of D-01.

Under DEFER the sequence does not start; the only artifact is the
deferral record with its review date (DP-15).

## 17. Exact repository state immediately after `ADR-0006` would exist

Relative to `main` = `e300f506`, the merge of the acceptance ADR changes
**exactly one thing**:

- `docs/decisions/` gains one file (`docs/decisions/ADR-0006.md`),
  making its contents: ADR-0001..ADR-0005, `ADR-0006`,
  `D01_DECISION_BRIEF.md`, `D01_DECISION_DOSSIER.md`.
- In substance (facts recorded inside the ADR): G-D01 is met; B-01
  closed; B-02 resolved or explicitly re-deferred; the RFC-0005/0007/0009
  windows are open; P05 and (at the review) P10 existence are determined.

**Everything else is unchanged until its own follow-up PR — nothing
updates automatically:**

- PROGRAM.md §4 still prints G-D01 as OPEN and §6 still lists B-01/B-02
  until the §7 revision PR (step 2 above).
- WORK_BREAKDOWN_STRUCTURE.md ⛔ entry-gate markers stand until revised
  by PR.
- Every specification keeps `Status: In Review` and its
  `TODO(blocked-by:)` markers until specification work discharges them.
- Individual RFC files keep their submission-time `Status: In Review`
  headers (ADR-0004 §Consequences: the index plus the ADR are the
  authoritative disposition record; no bulk rewrite).
- `docs/rfc/README.md`'s disposition column lacks the new row until
  updated by PR.
- The Notion knowledge mirror is stale until the P02.3 sync runs
  (KNOWLEDGE_SYNC_RUNBOOK trigger: governance merge).
- CI configuration is unchanged. The derived corpus index
  (`docs/derived/CORPUS_INDEX.md`) does not yet exist; its first
  generation is a Maintainer execution act, and because the source corpus
  includes `docs/decisions/ADR-*.md`, the new ADR enters it on the next
  regeneration (DOC_DERIVATION_CONVENTIONS: regenerate, never hand-edit).

## 18. Checklist the Maintainer must complete before writing `ADR-0006`

- [ ] Select the identity from the recorded space (I-A / I-B / I-C /
      I-D) — or record DEFER with an explicit review date (RFC-0001
      §Design Space; DP-15).
- [ ] Resolve U-14 within the same act (S-A / S-B / S-C) or explicitly
      re-defer it with a review point (RFC-0012 §Consequences; ADR-0004
      routing).
- [ ] Answer or explicitly re-defer Q1: first-class consumers — humans,
      tools, AI symmetrically (RFC-0001 Q1; INV-19).
- [ ] Answer or explicitly re-defer Q2: success criteria at year 1,
      year 5, year 20 (RFC-0001 Q2).
- [ ] Record which of U-5/U-6/U-8/U-9/U-10/U-14 are decided inside the
      ADR and which are explicitly re-deferred (RFC-0001 Q3).
- [ ] Answer Q4: whether the identity requires renaming — noting A-3:
      the current name is not evidence (RFC-0001 Q4, A-3).
- [ ] Conduct the mandatory RFC-0007 packaging review (N-yes / N-no /
      re-deferral) or schedule it: the disposition permits "at or after
      RFC-0001 acceptance" (ADR-0004).
- [ ] If I-C: record the prior domain-definition sub-decision (RFC-0001
      I-C row).
- [ ] If I-D: ratify the staging discipline up front (RFC-0001 I-D row).
- [ ] If S-A (or later N-no): plan the Baseline §13 amendment for S6 (or
      S11) retirement — supersession with successor pointer, never
      deletion (RFC-0012; S06/S11 acceptance criteria; Blueprint §7).
- [ ] Confirm the choice stays within the recorded option space — any
      new option would resolve the unknown outside the frame (CN-14).
- [ ] Record that interim rules P-D and V-D remain in force until their
      full decisions supersede them (ADR-0004).
- [ ] Author the ADR per Article 7 (decision, context, consequences
      recorded; ADR-binding) and merge it via the single recorded path
      (CONTRIBUTING.md).
- [ ] Queue the follow-ups: PROGRAM.md §4/§6 revision PR (§7 change
      process); knowledge-mirror sync (P02.3); RFC index disposition row.

---

*This dossier records no preference. Option ordering reproduces
RFC-0001's own table order. Every statement above cites its repository
source; nothing here decides, ranks, or disposes any option, blocker, or
unknown (Article 6, Article 7, INV-8).*
