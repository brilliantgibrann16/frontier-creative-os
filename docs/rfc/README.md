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
below is the authoritative disposition record together with ADR-0004;
individual RFC files retain their submission-time `Status: In Review`
headers by design — per the standing no-bulk-rewrite rule, they are not
rewritten wholesale.

Numbering is provisional pending RFC-0002 (identifier scheme); renumbering
after D-03 resolution, if any, will preserve a mapping table here.

| RFC | Title | Resolves | Subsystem | Disposition (ADR-0004) |
| --- | --- | --- | --- | --- |
| 0001 | Language Identity and Design Philosophy | U-1 (D-01) | S4 | **Open** — no recommendation recorded; requires dedicated decision + ADR |
| 0002 | Artifact Identifier and Namespace Scheme | U-2 (D-03) | cross-cutting | Accepted (N-B + N-C) |
| 0003 | Specification Corpus Location and Repository Taxonomy | U-3 (D-13), D-14 remainder | cross-cutting | Accepted (T-A), home amended by ADR-0005 to `/specs` |
| 0004 | Conformance Levels and Third-Party Certification | U-5 (D-04), U-13 | S13 | Accepted — frame (L-A + C-A); levels remain future work |
| 0005 | Compatibility and Stability Policy | U-6 | S4/S15 | Accepted — interim rule only (pre-1.0 instability window); full policy blocked by RFC-0001 |
| 0006 | Reference Implementation Policy | U-7 | S5 | Accepted (R-A — no defining-authority reference implementation) |
| 0007 | Package Distribution Model | U-8 | S11 | Accepted — deferral (N-defer, decided at/after RFC-0001 acceptance) |
| 0008 | Machine-Readable Specification Format | U-9 | S4/S13 | Accepted (M-B — prose-authoritative + clause index) |
| 0009 | Language Versioning Scheme | U-10 | S4 | Accepted — interim rule only (V-D, no language version pre-1.0) |
| 0010 | Multi-Maintainer Governance Procedure | U-11 | S1 | Accepted (G-D + cooling rule); blocker J.4 removed |
| 0011 | CI Platform and Gate Encoding | U-12 | S12/S15 | Accepted (E-A — tests + link/ID checks) |
| 0012 | Runtime Scope | U-14 | S6 | Accepted — procedural (U-14 resolved inside the future RFC-0001 acceptance ADR) |
| 0013 | Candidate Subsystem: Planner | — (introduction) | none (new) | **Rejected** (P-A) |
| 0014 | Candidate Subsystem: Memory | — (routing + introduction) | S4 or new | **Open** — routing (M-A/M-B/M-C) unchosen |
| 0015 | Candidate Subsystem: Context Engine | — (introduction) | none (new) | **Open** — blocked on definition (L-12) |
| 0016 | Candidate Subsystem: Agent Framework | — (introduction) | S16-adjacent | **Rejected** (A-A) |
| 0017 | Candidate Subsystem: Product UI | — (scope + introduction) | S9 or new | Accepted — scope rule (U-A: S9 engineering tooling only) |

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
