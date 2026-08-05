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

*(Sections 11–18 follow.)*
