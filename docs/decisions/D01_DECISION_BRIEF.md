# D-01 Decision Brief — Language Identity and Design Philosophy

**Artifact class:** Decision-support brief — carries **no decision
authority** (Blueprint §7) and **contains no recommendation**. It compiles,
without addition, what the repository already records. The decision and its
recording ADR are the Maintainer's alone (Article 6, Article 7, INV-8).
This document is **not** an ADR; it is placed in `docs/decisions/` by
explicit Maintainer instruction (2026-08-05).
**Decision:** D-01 (Decision Register) = U-1 (Blueprint §14), the
controlling unknown. RFC-0001 is its decision frame.
**Sources (exhaustive):** RFC-0001; RFC-0005, RFC-0007, RFC-0009, RFC-0012
(the RFCs whose decisions are blocked by RFC-0001); specifications S04,
S05, S06, S07, S11 (blocked at content, scope, or existence level by
D-01); PROGRAM.md; DEPENDENCY_GRAPH.md; ADR-0004 (dispositions).

---

## 1. The exact decision question

As recorded in RFC-0001 (Summary):

> Decide what the Frontier Specification Language (FSL) *is*: its purpose,
> its intended consumers, its success criteria, and consequently which
> downstream subsystems (runtime, package manager, stdlib scope) exist at
> all.

The acceptance ADR that records the decision also, per the recorded gate
definition (PROGRAM.md G-D01; RFC-0012 as disposed by ADR-0004):

- resolves **U-14** (runtime existence/scope) in the same act, and
- opens the decision windows for **RFC-0005** (compatibility),
  **RFC-0007** (packaging), and **RFC-0009** (language versioning).

RFC-0001 additionally records four open questions the decision must
answer or explicitly re-defer:

1. Who are the first-class consumers: humans authoring, tools consuming,
   AI systems doing both symmetrically (INV-19)?
2. What is the success criterion at year 1, year 5, year 20?
3. Which of U-5/U-6/U-8/U-9/U-10/U-14 are decided within the acceptance
   ADR, and which are explicitly re-deferred?
4. Does the identity require renaming ("Specification" in FSL), or does
   the name constrain nothing (RFC-0001 A-3: the name is not evidence)?

## 2. Admissible options (only those already described in repository documents)

**Identity options** — RFC-0001 §Design Space, verbatim in substance:

| # | Identity |
| --- | --- |
| I-A | Specification/definition language: programs are structured definitions (specs, contracts, artifacts) consumed by tools |
| I-B | General-purpose programming language |
| I-C | Domain-specific language for creative-systems orchestration |
| I-D | Interchange/definition core (I-A) with staged evolution path toward executable semantics |
| DEFER | Recorded deferral with a review date — named admissible by RFC-0001 §Consequences ("Deferral: legitimate (DP-15) but must be recorded with a review date; all implementation remains blocked (CN-14)") |

No other identity option appears in any repository document; per the
mission and the no-invention rule, none is added here.

**Coupled sub-decision spaces** (already recorded; constrained by, not
identical to, the identity choice):

| Unknown | Space (source) | Recorded coherence with identity |
| --- | --- | --- |
| U-14 runtime scope | S-A no runtime / S-B validation-evaluation runtime / S-C full execution environment (RFC-0012) | S-A ↔ I-A; S-B ↔ I-A/I-D; S-C ↔ I-B/I-C (RFC-0012 table; descriptive, not binding) |
| U-8 packaging | N-yes / N-no / N-defer (RFC-0007); N-defer accepted interim per ADR-0004, mandatory review inside the RFC-0001 acceptance ADR | a definition-language identity "may need only document distribution" (RFC-0007) |
| U-6 compatibility | P-A strong backward compat / P-B editions / P-C semver-style / P-D interim instability window then one of the former (RFC-0005); P-D window already in force per ADR-0004 | "the identity fixes who the consumers are" (RFC-0005 §Consequences) |
| U-10 language versioning | V-A monotonic / V-B semver-like / V-C date editions / V-D no language version pre-1.0 (RFC-0009); V-D already in force per ADR-0004 | V-C "meaningless unless" RFC-0005 P-B adopted; declaration syntax is D-01-dependent (RFC-0009 Q1) |

## 3. Consequences of each option (as recorded)

| Option | Recorded consequences (RFC-0001 unless noted) |
| --- | --- |
| I-A | Runtime likely minimal or absent (U-14 small); packaging may reduce to document distribution (U-8 small); conformance = validation semantics. Smallest surface, fastest to specify; lowest expressive ambition; risk of under-serving future needs |
| I-B | Full runtime, stdlib, packaging, versioning all required; RFC volume ≈45–70 (Phase 2 estimate; RFC-0012 locates most of it in the S-C runtime). Maximal ambition and cost; decades-scale commitment; highest risk under a sole maintainer |
| I-C | Runtime scope moderate and domain-shaped; stdlib is domain library; conformance suites domain-specific. Requires defining the domain precisely first — a sub-decision as hard as D-01 itself |
| I-D | Defers execution decisions without foreclosing them; versioning scheme must encode capability stages (U-10 interaction). Two-phase identity risks permanent limbo; staging discipline must be ratified up front |
| DEFER | All implementation remains blocked (CN-14); review date mandatory (DP-15); risk R-1 (identity ambiguity, rated Critical) remains open — "without this decision, any implementation work resolves the unknown by accident" (RFC-0001 §Motivation) |

Common to accepting **any** of I-A/I-B/I-C/I-D (RFC-0001 §Consequences):
unblocks RFC-0005, RFC-0007, RFC-0009, RFC-0012 for decision (RFC-0002
and RFC-0008 are already accepted per ADR-0004 and await first use); S4
specification work; the RFC-count roadmap.

## 4. Engineering impact

| Option | Impact |
| --- | --- |
| I-A | Smallest engineering surface: S04 content + validation-semantics conformance; S05 compiler bounded by validation identity; P05 small or void; distribution possibly repository/release artifacts only |
| I-B | Largest: full S06 (S-C), full S07, likely S11 machinery; the ≈45–70 RFC roadmap dominates engineering for the foreseeable horizon |
| I-C | Moderate, domain-shaped S06/S07; a precise domain definition precedes any clause work (prior sub-decision) |
| I-D | I-A-scale engineering now plus staging machinery: the versioning scheme must encode capability stages before execution semantics arrive |
| DEFER | Zero new engineering: Wave 0 standing lanes (P00 hygiene, P02 sync, P13 frame, P15 conventions) remain the only executable work (DEPENDENCY_GRAPH §2: "No engineering acceleration shortens it while G-D01 is open") |

Under every option the critical path is unchanged in shape
(DEPENDENCY_GRAPH §2): decision → P03 ratified clauses + clause index →
P04 conforming compiler → P11/P12 evidence + judgment → P14 first
gate-checked release. The options change the *volume* traversing that
path, not its order.

## 5. Governance impact

| Option | Impact |
| --- | --- |
| Any of I-A…I-D | One Maintainer-authored acceptance ADR records: the identity; the U-14 resolution (same act, per G-D01/RFC-0012 disposition); the mandatory RFC-0007 packaging review; answers or explicit re-deferrals for RFC-0001 Q1–Q4 (including naming). It then opens the RFC-0005/RFC-0009 full-policy decisions |
| I-A with S-A | S6 retirement is an architecture change via the Baseline §13 amendment path — beyond the S06 spec itself (S06 §Acceptance criteria) |
| I-B | Largest standing governance volume: the ≈45–70 RFC roadmap all travels RFC → ADR |
| I-C | Requires a prior recorded domain-definition decision "as hard as D-01 itself" (RFC-0001) |
| I-D | The staging discipline must be **ratified up front** (RFC-0001); each stage transition is a future decision event |
| U-8 = N-no (any identity) | S11 retirement via the Baseline §13 path (S11 §Acceptance criteria) |
| DEFER | A recorded deferral with review date (DP-15); G-D01 stays open; no other governance change is admissible |

## 6. Repository impact

| Option | Impact |
| --- | --- |
| Any of I-A…I-D | S04 blocked content sections unblock; spec production flow starts (S04 §Sequence flows: acceptance ADR → spec charter → Draft → In Review → ratification ADR → suite tracing → implementations authorized); clause IDs assigned per RFC-0002, index per RFC-0008 M-B; `TODO(blocked-by:` markers discharged progressively across the corpus; PROGRAM.md is revised by PR because a gate changes state (PROGRAM.md §7) |
| I-A with S-A | S06 → Deprecated with successor pointer; S6 retired via Baseline §13 |
| I-B / I-C | S06 populated per decided scope; S07 populated; S05 compiler-boundary contract specified toward ratification |
| I-D | S04 must additionally encode the stage model; execution-facing specs stay blocked per stage |
| U-8 = N-no | S11 → Deprecated (S11 §Acceptance criteria); if N-yes, S11 schemas unblock |
| DEFER | No repository change beyond the deferral record; every BLOCKED marker stands |

Implementation-area locations are fixed by recorded implementation-plan
notes before the first code PR (PROGRAM.md P04) — not by this decision.

## 7. Migration impact

- **No code migration exists under any option.** The Phase 0 prototype is
  historical context only and constrains nothing (RFC-0001 A-2; L-7,
  INV-7). No option inherits it.
- **No consumer migration exists today.** No language version exists
  pre-1.0 (RFC-0009 V-D, in force per ADR-0004) and the interim
  instability window (RFC-0005 P-D declaration, in force per ADR-0004)
  means no compatibility promise has been issued that any option would
  break.
- **I-D specific:** future migration between capability stages is a
  designed-in obligation — the versioning scheme must encode stages
  (RFC-0001; RFC-0009 U-10 interaction).
- **Retirements (S-A, N-no) migrate by supersession**, never deletion:
  Deprecated status with successor pointer (S06/S11 acceptance criteria;
  Blueprint §7 lifecycle).
- **Naming:** whether the identity requires renaming is RFC-0001 Q4; the
  acceptance ADR answers it either way (A-3: the current name is not
  evidence and creates no migration debt by itself).

## 8. Long-term maintenance impact

| Option | Impact (as recorded) |
| --- | --- |
| I-A | Smallest maintained surface; recorded risk: under-serving future needs (RFC-0001) |
| I-B | "Decades-scale commitment; highest risk under a sole maintainer" (RFC-0001); the single-maintainer reality (OB-4) is echoed in RFC-0012 Q3 |
| I-C | Domain-specific conformance suites to maintain; the domain definition itself becomes a maintained artifact whose drift is identity-scale |
| I-D | Standing staging-discipline duty; recorded risk of permanent limbo (RFC-0001) |
| DEFER | The blocked state itself is maintained: review dates, Wave-0-only activity, and Critical risk R-1 remain open indefinitely |

Cross-cutting: the 1.0 compatibility policy family eventually chosen
under RFC-0005 (P-A heavy cost on early mistakes / P-B machinery /
P-C ecosystem fragmentation) sets the dominant long-run cost profile for
whichever identity is selected — that choice is explicitly downstream of
D-01 and is not made here.

## 9. Programs that become executable after each option

Per DEPENDENCY_GRAPH (edge list and topological order), closing G-D01 by
accepting **any** identity makes exactly one program newly executable:
**P03 Language Definition (Wave 1)** — plus resolution of P05's
existence in the same act (U-14). Everything else becomes *reachable*
but stays gated on ratified specs and contracts:

| Option | Newly executable at once | Becomes reachable (still gated by G-SPEC/B-06/B-08) | Existence outcomes decided in the same ADR |
| --- | --- | --- | --- |
| I-A | P03 | P04, P12 full suite, P13 behavior docs as clauses ratify; P07/P08/P09 per later contracts | P05: void (S-A) or minimal (S-B) per the recorded coherence; P10: small/likely unneeded (U-8 small) — decided at the RFC-0007 review |
| I-B | P03 | P04, P05, P06, P07, P08, P09, P12 full, P13 behavior docs — in wave order | P05 exists (S-C); P10 decided at the RFC-0007 review |
| I-C | P03 (after the prior domain-definition sub-decision) | as I-B, domain-shaped | P05 exists (S-C); P10 decided at the RFC-0007 review |
| I-D | P03 | as I-A now; execution-facing programs per ratified stages | P05: S-B per the recorded coherence; stage transitions decided later |
| DEFER | none | none | none — all existence questions stay open |

Under every option the standing lanes P00/P02/P13/P15 continue, and P01
remains complete except the Maintainer console action (required checks).
The coherence mappings above are RFC-0012's descriptive table, not
automatic outcomes: the acceptance ADR records the actual U-14 and U-8
resolutions.

## 10. Blockers remaining after each option

Register per PROGRAM.md §6 (B-01…B-11):

| Blocker | I-A | I-B | I-C | I-D | DEFER |
| --- | --- | --- | --- | --- | --- |
| B-01 D-01 undecided | closed | closed | closed | closed | **remains** |
| B-02 U-14 runtime | resolved in the ADR (void or scoped) | resolved (S-C) | resolved (S-C) | resolved (S-B) | **remains** |
| B-03 packaging deferral | review opens; remains until RFC-0007 decided (re-deferral admissible) | same | same | same | **remains** |
| B-04 compatibility policy | decidable; **remains** until the 1.0 family is decided (interim window stays in force) | same | same | same | **remains** |
| B-05 versioning scheme | decidable; **remains** until decided with RFC-0005 (V-D stays in force) | same | same | same | **remains** |
| B-06 interface forms UNKNOWN | **remains** until each interface spec ratifies (Blueprint §8) | **remains** | **remains** | **remains** | **remains** |
| B-07 conformance levels | **remains** (future work per RFC-0004 disposition) | **remains** | **remains** | **remains** | **remains** |
| B-08 specs not ratified | **remains**; P03 begins discharging it clause by clause | same | same | same | **remains** in full |
| B-09 memory/context undecided | **remains** (RFC-0014, RFC-0015 are independent of D-01) | **remains** | **remains** | **remains** | **remains** |
| B-10 no ratified performance requirement | **remains** until a ratified spec supplies one | **remains** | **remains** | **remains** | **remains** |
| B-11 `specs/fcos/` disposal | **remains** (orthogonal Maintainer decision) | **remains** | **remains** | **remains** | **remains** |

---

*This brief records no preference. Option ordering reproduces RFC-0001's
own table order. Every statement above cites its repository source;
nothing here disposes any blocker or unknown (Article 7, INV-8).*
