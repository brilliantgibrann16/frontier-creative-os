# S04 Language-Definition Charter — Preparation and the Q1/Q2 Decision Surface

- Status: Q1/Q2 resolved — the disposition at this recorded DP-15
  review point (ADR-0006, Decision 5) is recorded in ADR-0007
  (2026-08-11). Charter content is recorded in §6; the P03 execution
  state is recorded in §7 — its namespace decision surface is resolved
  (ADR-0008).
- Artifact class: program documentation (P03 first act — charter
  preparation and decision surface). It carries **no decision authority**
  (Blueprint §7), **contains no recommendation**, and compiles, without
  addition, what the repository already records. The decisions and their
  recording ADR are the Maintainer's alone (Article 6, Article 7, INV-8).
- Governing artifacts: ADR-0006 (Decisions 1–5; queued follow-up 5);
  RFC-0001 (Open Questions; Consequences; Recommendation); RFC-0002
  (N-B + N-C, per the ADR-0004 disposition); RFC-0008 (M-B, per the
  ADR-0004 disposition); RFC-0012 (S-B); Baseline 1.1.0 §13; PROGRAM.md
  (P03); WORK_BREAKDOWN_STRUCTURE.md (P03.1–P03.6); Doctrine DP-15; CN-14.

## 1. Recorded mandate

- ADR-0006, queued follow-up 5: "S04 charter work (P03) — where the
  Q1/Q2 re-deferrals come due."
- ADR-0006, Decision 5: Q1 and Q2 are "explicitly re-deferred"; the
  recorded review point is "the S04 language-definition charter, the
  first act of P03 (DP-15 review point recorded)."
- D01_DECISION_DOSSIER.md §16, steps 4–5: "P03 entry discharges. First
  use of the RFC-0002 clause-ID scheme (N-B + N-C) and the RFC-0008 M-B
  machine-readable clause index." then "Specification production flow
  begins … acceptance ADR → spec charter → Draft → In Review →
  ratification ADR → suite tracing → implementations authorized."
- specs/S04-language-definition.md, §Sequence flows, step 1 records the
  same production flow ("spec charter per component").

## 2. Binding inputs — already decided, not open in this charter

| Input | Recorded decision | Source |
| --- | --- | --- |
| Identity (U-1 / D-01) | **I-D** — "an interchange/definition core (I-A scope) with a staged evolution path toward executable semantics" | ADR-0006, Decision 1 |
| Staging discipline | Ratified up front: capability stages are explicit and ordered; Stage 0 is the definition/validation core scoped by ADR-0006 (the I-D core with the S-B runtime); execution-facing semantics beyond Stage 0 are deferred without being foreclosed; each stage transition is a future Maintainer decision travelling the RFC → ADR path, never entered implicitly (CN-14); **S04 must encode the stage model** | ADR-0006, Decision 3 |
| Runtime scope (U-14) | **S-B** — validation-evaluation runtime; Baseline L-3 stands (zero defining authority); "the boundary between the validation-evaluation runtime and S13 conformance tooling must be drawn precisely in specification work" | ADR-0006, Decision 2 |
| Packaging (U-8) | **N-no** — no package-distribution subsystem exists; S11 retired by supersession (Baseline 1.1.0, §13 Amendment record); Program P10 does not exist; no packaging content enters S04 | ADR-0006, Decision 4; Baseline §13 |
| Naming (Q4) | "the name Frontier Specification Language is retained" — per RFC-0001 A-3 the name is not evidence and constrains nothing | ADR-0006, Decision 5 |
| Clause identifiers | **N-B + N-C** composite (namespaced sequential document IDs + hierarchical dotted clause IDs; clauses may not renumber after ratification) | RFC-0002; ADR-0004 disposition; ADR-0008 (registry authority, grandfathering, token discipline); WBS P03.2 |
| Machine-readable index | **M-B** posture — prose authoritative + structured clause index; concrete schema deferred to first specification ratification | RFC-0008; ADR-0004 disposition; WBS P03.4 |
| Versioning / compatibility interim rules | P-D (pre-1.0 instability window) and V-D (no language version before 1.0) remain in force; the eventual versioning scheme must encode capability stages (U-10) | ADR-0004; ADR-0006, Decision 5 (Q3 row) |

## 3. Charter work plan — recorded WBS packages, no new scope

The plan is the recorded WBS P03 package list; nothing is added here:

1. **P03.1** Ratify the S04 container specification (G-SPEC(S04)).
2. **P03.2** Apply the RFC-0002 (N-B + N-C) identifier scheme to clause
   numbering; record the scheme's spec text.
3. **P03.3** Draft → review → ratify the clause set the D-01 decision
   defines — per the WBS, "scope comes from the acceptance ADR, not
   from this plan."
4. **P03.4** Build the machine-readable clause index (RFC-0008 M-B;
   prose stays authoritative).
5. **P03.5** Wire clause-index validation into P01 checks.
6. **P03.6** Update `specs/` TODO(blocked-by…) markers that the
   acceptance ADR discharges.

## 4. Decision surface — RFC-0001 Q1 and Q2 (RESOLVED — ADR-0007)

Exactly as recorded in RFC-0001, §Open Questions:

> 1. Who are the first-class consumers: humans authoring, tools
>    consuming, AI systems doing both symmetrically (INV-19)?
> 2. What is the success criterion at year 1, year 5, year 20?

Recorded status: both were explicitly re-deferred by ADR-0006
(Decision 5) to this charter, with the DP-15 review point recorded.
They came due here. Resolution: recorded in ADR-0007 (2026-08-11) —
admissible disposition 1 below was taken; both questions are decided;
neither is re-deferred.

**What Q1/Q2 block (recorded):**

- The S04 blocked-content items "purpose, consumers, success criteria"
  (specs/S04-language-definition.md, §Scope) — identity itself is now
  decided (I-D), so these are the remaining content blockers at charter
  level.
- Completion of this charter: its consumers and success-criteria
  sections cannot be written until Q1/Q2 are recorded.
- The clause scope of P03.3, whose scope "comes from the acceptance
  ADR, not from this plan" (WBS).

**Recorded constraints on any answer (compiled without addition):**

- INV-19 symmetry is named inside Q1's own text.
- The identity decision (I-D) and the ratified staging discipline bound
  the scope any answer may assume; execution-facing semantics beyond
  Stage 0 remain blocked per stage (ADR-0006, Decision 3).
- Any success criterion that touches versioning interacts with the
  recorded rule that the eventual scheme must encode capability stages
  (U-10; ADR-0006, Decision 5, Q3 row).
- RFC-0001 records **no option set** for Q1/Q2 and no recommendation:
  "None. Per the Maintainer's standing ruling, the language is designed
  collaboratively; this RFC supplies the decision frame only." This
  charter therefore presents no candidate answers.

**Admissible dispositions (per recorded rules; the choice is the
Maintainer's alone):**

1. Decide Q1 and/or Q2 now, recorded through the decision path as an
   ADR (Article 6, Article 7).
2. Re-defer with a new recorded review date (DP-15). This document is
   the recorded review point; any further deferral requires its own
   recorded date.

## 5. Stop boundary

- No syntax, grammar, or semantics is drafted under this preparation
  (PROGRAM.md P03: content scope comes from recorded decisions —
  ADR-0006 and ADR-0007; clause drafting additionally awaits the
  identifier decision surface recorded in §7).
- No Wave-1 implementation begins (CN-14; the G-SPEC gates stand).
- This document selects no answer to Q1 or Q2.

## 6. Consumers and success criteria (recorded — ADR-0007)

Charter content, compiled from the recording ADR without addition.

**Consumers (Q1).** The first-class consumers of the Frontier
Specification Language are exactly the three classes named in RFC-0001
Q1, affirmed jointly and symmetrically: humans authoring (RFC-0001
§Recommendation collaborative ruling; Article 6), tools consuming
(identity I-D: structured definitions "consumed by tools" — ADR-0006,
Decision 1), and AI systems doing both (Article 2; INV-19; Baseline
P-4; CN-23 bounds per the RFC-0016 rejection, ADR-0004). Bounds: no
consumer class acquires defining authority (A-1, P-1, L-2; Baseline
L-3; R-A), and the classes are stage-invariant under the ratified
staging discipline (ADR-0006, Decision 3; CN-14). Source: ADR-0007,
Decision Q1.

**Success criteria (Q2).** At every horizon the criterion is the
Article 1 metric — "The project measures success by the quality and
traceability of its engineering, not by speed of delivery" —
instantiated by the Article 10 goals and indexed to phases and
capability stages, never calendar deadlines: year 1 = traceability of
every significant decision plus Stage 0 discipline (goal 2; CN-14;
ADR-0006, Decision 3); year 5 = roadmap advancement through recorded
decisions plus a contributor community under the constitution (goals 1
and 3); year 20 = ten-year comprehensibility preserved (goal 4;
Article 1 decade-scale maintainability). No calendar commitment and no
new metric exist. Source: ADR-0007, Decision Q2.

## 7. P03 execution state and the next decision surface (2026-08-11)

Recorded classification of the WBS packages after ADR-0007:

| Package | State | Governing reason |
| --- | --- | --- |
| P03.1 | Blocked (one decision out) | Needs the P03.2 scheme text recorded in S04, then its own recorded ratification per Article 7 (G-SPEC(S04)) — a Maintainer decision |
| P03.2 | **Unblocked (ADR-0008)** | Registry authority, grandfathering, and token discipline are recorded; the grandfathered document ID `S04` carries the N-C clause-ID layering, so the scheme's spec text proceeds with no namespace token — specification work via its own P03 PR |
| P03.3 | Blocked | Needs the merged P03.2 scheme text and a drafted Stage 0 clause inventory travelling Draft → In Review → per-clause ratification (PROGRAM.md P03, acceptance gates); no recorded decision enumerates the clause inventory, so no clause ID is derivable today |
| P03.4 | Blocked | M-B schema is "deferred to first specification ratification" (RFC-0008, §Recommendation and §Consequences; ADR-0004) |
| P03.5 | Blocked | Depends on the P03.4 index existing (WBS) |
| P03.6 | Executed (reopens per decision) | ADR-0006/0007-discharged markers updated in PR #35; the ADR-0008-discharged markers (S04 §Data model assignment TODO) update in the P03.2 specification PR |

**Decision surface resolved (2026-08-11 — ADR-0008):** the Maintainer
decided explicitly: every new namespace requires its own RFC → ADR
path (no delegated register); every existing identifier is
grandfathered — authoritative, never renumbered, never migrated, no
mapping table; and no concrete namespace token is ratified — each
future token enters through its own RFC → ADR decision. RFC-0002 Open
Questions 2 (mirror ID display) and 3 (exact clause-freeze point)
remain open; the freeze point becomes binding at the S04 container
ratification. Remaining Maintainer decisions ahead of P03: the S04
container ratification ADR (P03.1, after the P03.2 scheme text
merges) and, when first needed, the first concrete namespace token.
