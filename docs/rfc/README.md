# RFC Index

RFCs propose and justify changes; they carry authority for rationale only
(Baseline §6, rank 4). An RFC resolves nothing by itself: resolution
occurs when the Maintainer accepts it and the acceptance is recorded as an
ADR (Article 7, L-8). Lifecycle: Draft → In Review → Accepted / Rejected /
Withdrawn → Implemented.

All RFCs below are **decision-framing**: they enumerate assumptions,
alternatives, trade-offs, and open questions without choosing. Where a
recommendation appears it is labeled and non-binding.

**Disposition (2026-08-02):** the set was disposed by **ADR-0004** (with
ADR-0005 amending the specification-home element of RFC-0003). The table
below is the authoritative disposition record together with ADR-0004
and ADR-0006;
individual RFC files retain their submission-time `Status: In Review`
headers by design — per the standing no-bulk-rewrite rule, they are not
rewritten wholesale.

Numbering is settled (ADR-0008): every existing identifier is
grandfathered — never renumbered, never migrated; no mapping table
exists because no migration is performed. New namespaces enter only
through their own RFC → ADR decision.

| RFC | Title | Resolves | Subsystem | Disposition (ADR-0004; ADR-0006 where cited) |
| --- | --- | --- | --- | --- |
| 0001 | Language Identity and Design Philosophy | U-1 (D-01) | S4 | **Accepted (I-D — ADR-0006)**; Q1/Q2 resolved at the charter review point (ADR-0007); Q4: name FSL retained |
| 0002 | Artifact Identifier and Namespace Scheme | U-2 (D-03) | cross-cutting | Accepted (N-B + N-C); registry authority, grandfathering, and token discipline recorded in **ADR-0008** |
| 0003 | Specification Corpus Location and Repository Taxonomy | U-3 (D-13), D-14 remainder | cross-cutting | Accepted (T-A), home amended by ADR-0005 to `/specs` |
| 0004 | Conformance Levels and Third-Party Certification | U-5 (D-04), U-13 | S13 | Accepted — frame (L-A + C-A); levels remain future work |
| 0005 | Compatibility and Stability Policy | U-6 | S4/S15 | Accepted — interim rule only (pre-1.0 instability window); full policy blocked by RFC-0001 |
| 0006 | Reference Implementation Policy | U-7 | S5 | Accepted (R-A — no defining-authority reference implementation) |
| 0007 | Package Distribution Model | U-8 | S11 | Accepted — deferral (N-defer) discharged: decided **N-no** (ADR-0006); S11 retires via Baseline §13 supersession |
| 0008 | Machine-Readable Specification Format | U-9 | S4/S13 | Accepted (M-B — prose-authoritative + clause index); concrete schema recorded in **ADR-0010** — per-spec YAML sidecar, derived hygiene, OQ1–OQ3 discharged |
| 0009 | Language Versioning Scheme | U-10 | S4 | Accepted — interim rule only (V-D, no language version pre-1.0) |
| 0010 | Multi-Maintainer Governance Procedure | U-11 | S1 | Accepted (G-D + cooling rule); blocker J.4 removed |
| 0011 | CI Platform and Gate Encoding | U-12 | S12/S15 | Accepted (E-A — tests + link/ID checks) |
| 0012 | Runtime Scope | U-14 | S6 | Accepted — procedural routing discharged: U-14 resolved **S-B** in ADR-0006 |
| 0013 | Candidate Subsystem: Planner | — (introduction) | none (new) | **Rejected** (P-A) |
| 0014 | Candidate Subsystem: Memory | — (routing + introduction) | S4 or new | **Open** — routing (M-A/M-B/M-C) unchosen |
| 0015 | Candidate Subsystem: Context Engine | — (introduction) | none (new) | **Open** — blocked on definition (L-12) |
| 0016 | Candidate Subsystem: Agent Framework | — (introduction) | S16-adjacent | **Rejected** (A-A) |
| 0017 | Candidate Subsystem: Product UI | — (scope + introduction) | S9 or new | Accepted — scope rule (U-A: S9 engineering tooling only) |
| 0018 | S04 Stage 0 Minimal Contract Clause Set (amendment proposal) | P03.3 content gate | S4 | **Accepted (ADR-0011)** — the twelve-clause Stage 0 minimal contract inventory is ratified into S04 through the amendment path |
| 0019 | S04 Stage 1 Language-Content Scope (Minimum P04 Unlock) | frames the Stage 0 → Stage 1 transition (S04#1.2) and the P04 language-content prerequisite | S4 | **Accepted (ADR-0012)** — D1: Stage 1 entered; D2: scope **W-B** (interchange kernel); D3: type/data model explicitly labeled deferred; D4: deterministic validation outcomes required; clause content travels subsequent S04 amendment cycles |
| 0020 | S04 Stage 1 W-B Interchange-Kernel Clause Set (amendment proposal) | ADR-0012 follow-up 1 — the Wave 2 W-B clause-drafting cycle | S4 | **Accepted (ADR-0013)** — F1 decided 2026-08-19: **JSON** (F1-A per GL-15/DP-28); F2 decided path 1 (revise-then-ratify); the revised thirteen-clause W-B kernel (S04#5.1–S04#8.3) is ratified into S04 through the amendment path |

Dependency order: RFC-0001 (D-01) is the controlling decision; RFC-0005,
0007, 0008, 0009, 0012 and parts of 0004 cannot be *decided* before it,
though they can be reviewed in parallel. RFC-0002, 0003, 0010, 0011 are
D-01-independent and decidable immediately.

*Post-disposition note (2026-08-06):* the dependency-order paragraph
above is the submission-time analysis, retained for the record; it is
superseded by the disposition column. ADR-0004 disposed RFC-0007
(deferral with trigger), RFC-0008 (M-B) and RFC-0012 (procedural
routing) ahead of RFC-0001, and gave RFC-0005 and RFC-0009 interim
rules; the full compatibility policy (RFC-0005) and the U-14
resolution (RFC-0012) still land at or after RFC-0001 acceptance,
exactly as the table records.

*Post-disposition note (2026-08-12):* **RFC-0018** is the first
post-set RFC: an amendment proposal under the ratified S04 sequence
flow (proposal RFC → amended clauses → recording ADR, same decision
cycle), accepted and recorded by **ADR-0011** per the Maintainer's
explicit written directive of 2026-08-12. Unlike the decision-framing
0001–0017 set described above, it proposes a concrete clause set (its
recommendation is labeled and non-binding per convention).

*Post-disposition note (2026-08-14):* **RFC-0019** is the second
post-set RFC: a decision-framing proposal covering the Stage 0 →
Stage 1 capability-stage transition (S04#1.2) and the Stage 1
language-content scope that P04 requires. Like the 0001–0017 set it
selects nothing: the transition, the scope package, and the
type-model and determinism dispositions are Maintainer decisions,
binding only when recorded as an ADR (L-8/INV-8). It proposes no
clause text; if accepted, clause content travels subsequent S04
amendment cycles (proposal RFC → recording ADR).

*Post-disposition note (2026-08-10):* **ADR-0006** (the D-01 acceptance)
disposed the three rows above that ADR-0004 had left open or routed
forward: RFC-0001 is accepted with identity **I-D** (Q1/Q2 explicitly
re-deferred to the S04 language-definition charter; Q4 — the name
Frontier Specification Language is retained); RFC-0007's deferral
trigger fired and the decision is **N-no** (the interim N-defer
disposition is superseded; S11 retires via the Baseline §13 amendment
path — supersession with a successor pointer, never deletion — queued as
its own follow-up); RFC-0012's procedural routing is discharged, with
U-14 resolved **S-B** inside ADR-0006. The interim rules of RFC-0005
(P-D) and RFC-0009 (V-D) remain in force; their decision windows are
open per ADR-0006. Individual RFC files keep their submission-time
`Status: In Review` headers per the ADR-0004 convention: this index plus
the disposing ADRs are the authoritative disposition record.

*Post-disposition note (2026-08-18):* **ADR-0012** records the
Maintainer's acceptance of RFC-0019: Stage 1 is entered (D1), the
Stage 1 scope is the **W-B interchange kernel** (D2), the type/data
model is explicitly labeled deferred (D3), and deterministic
validation outcomes are required at Stage 1 (D4). Acceptance ratifies
no clause text: the Stage 1 clauses travel subsequent S04 amendment
cycles (proposal RFC → recording ADR), and the interchange form's
format sub-decision (existing boring format per GL-15/DP-28 versus a
bespoke form) is recorded for that cycle. The RFC file keeps its
submission-time `Status: In Review` header per the ADR-0004
convention.

*Post-disposition note (2026-08-18, later):* **RFC-0020** is the third
post-set RFC: an amendment proposal under the ratified S04 sequence
flow (proposal RFC → recording ADR; INV-18), begun under the
Maintainer's explicit written directive of 2026-08-18, which supplies
the authorization that ADR-0012 follow-up 1 requires. It drafts the
twelve-clause Stage 1 W-B kernel with proposal-time identifiers
(allocated only at ratification, per the RFC-0018 precedent), reserves
S04#8.3 for the recorded interchange-format sub-decision (F1), and
presents that decision surface without choosing. Its recommendation is
labeled and non-binding per convention; nothing in it is ratified by
its existence (L-8/INV-8).

*Post-disposition note (2026-08-19):* **ADR-0013** records the
Maintainer's explicit written decisions of 2026-08-19 on the RFC-0020
decision surface — F1 = F1-A with **JSON** as the concrete interchange
form; F2 = sequencing path 1 (revise-then-ratify) — and the acceptance
of the revised RFC-0020. Per path 1 the RFC was revised in the same
decision cycle to draft S04#8.3 from the recorded decision; the
thirteen Stage 1 W-B clauses (S04#5.1–S04#8.3) are ratified into
`specs/S04-language-definition.md` through the amendment path
(S04 §Sequence flows, step 2; INV-18), identifiers allocated exactly
as proposed and frozen (ADR-0009), the sidecar extended (ADR-0010
schema), and `spec.version` recorded unchanged at 1.0.0 (no versioning
policy — ADR-0011, Decision 2). The RFC file keeps its submission-time
`Status: In Review` header per the ADR-0004 convention; its 2026-08-19
revision is part of the proposal record.
