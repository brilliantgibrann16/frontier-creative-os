# RFC Index

RFCs propose and justify changes; they carry authority for rationale only
(Baseline §6, rank 4). An RFC resolves nothing by itself: resolution
occurs when the Maintainer accepts it and the acceptance is recorded as an
ADR (Article 7, L-8). Lifecycle: Draft → In Review → Accepted / Rejected /
Withdrawn → Implemented.

All RFCs below are **decision-framing**: they enumerate assumptions,
alternatives, trade-offs, and open questions without choosing. Where a
recommendation appears it is labeled and non-binding.

Numbering is provisional pending RFC-0002 (identifier scheme); renumbering
after D-03 resolution, if any, will preserve a mapping table here.

| RFC | Title | Resolves | Subsystem |
| --- | --- | --- | --- |
| 0001 | Language Identity and Design Philosophy | U-1 (D-01) | S4 |
| 0002 | Artifact Identifier and Namespace Scheme | U-2 (D-03) | cross-cutting |
| 0003 | Specification Corpus Location and Repository Taxonomy | U-3 (D-13), D-14 remainder | cross-cutting |
| 0004 | Conformance Levels and Third-Party Certification | U-5 (D-04), U-13 | S13 |
| 0005 | Compatibility and Stability Policy | U-6 | S4/S15 |
| 0006 | Reference Implementation Policy | U-7 | S5 |
| 0007 | Package Distribution Model | U-8 | S11 |
| 0008 | Machine-Readable Specification Format | U-9 | S4/S13 |
| 0009 | Language Versioning Scheme | U-10 | S4 |
| 0010 | Multi-Maintainer Governance Procedure | U-11 | S1 |
| 0011 | CI Platform and Gate Encoding | U-12 | S12/S15 |
| 0012 | Runtime Scope | U-14 | S6 |
| 0013 | Candidate Subsystem: Planner | — (introduction) | none (new) |
| 0014 | Candidate Subsystem: Memory | — (routing + introduction) | S4 or new |
| 0015 | Candidate Subsystem: Context Engine | — (introduction) | none (new) |
| 0016 | Candidate Subsystem: Agent Framework | — (introduction) | S16-adjacent |
| 0017 | Candidate Subsystem: Product UI | — (scope + introduction) | S9 or new |

Dependency order: RFC-0001 (D-01) is the controlling decision; RFC-0005,
0007, 0008, 0009, 0012 and parts of 0004 cannot be *decided* before it,
though they can be reviewed in parallel. RFC-0002, 0003, 0010, 0011 are
D-01-independent and decidable immediately.
