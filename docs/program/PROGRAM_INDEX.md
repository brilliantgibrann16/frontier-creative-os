# Program Index

**Artifact class:** Implementation Plan (index) — no decision authority
(Blueprint §7). See `PROGRAM.md` for full program definitions.

## Document map (`docs/program/`)

| File | Contents |
| --- | --- |
| `PROGRAM.md` | Master program: derivation sources, taxonomy, global gates, full 16-field definition of every program, blocker register |
| `PROGRAM_INDEX.md` | This index |
| `DEPENDENCY_GRAPH.md` | Complete dependency graph, critical path, topological build order, parallel work opportunities |
| `WORK_BREAKDOWN_STRUCTURE.md` | Work packages per program with blocked markers |
| `IMPLEMENTATION_STRATEGY.md` | Execution principles, wave model, blocker protocol, staffing model |
| `DELIVERY_STRATEGY.md` | Branch, merge, release, testing, and verification strategies |
| `MILESTONE_TEMPLATE.md` | Mandatory template for every program milestone |
| `RISK_REGISTER.md` | Program-execution risk register |
| `DOC_DERIVATION_CONVENTIONS.md` | Documentation derivation conventions: source corpus, mechanical rules, the `tools/docs/` pipeline and its `docs/derived/` outputs, staleness and freshness gates (P13.1) |
| `KNOWLEDGE_SYNC_RUNBOOK.md` | Repo→mirror sync runbook: ADR Log, RFC Index, Spec Index, Ops Log, registers; repo wins on conflict (P02.1) |
| `WAVE_0_VERIFICATION.md` | Wave 0 verification record: hygiene and gate evidence (P00/P01) |
| `AGENT_CONTRIBUTION_CONVENTIONS.md` | Agent contribution conventions: one path, review rules, disclosure duties, blocker protocol (P15.1) |
| `TESTING_CONVENTIONS.md` | Test harness conventions and the evidence taxonomy (P11.2/P11.3) |
| `CONFORMANCE_FRAME.md` | Conformance frame status: accepted RFC-0004 frame, blocking conditions (P12.1) |

## Program catalog

| ID | Program | Subsystem | Status | Entry gate | Controlling blocker |
| --- | --- | --- | --- | --- | --- |
| P00 | Repository Bootstrap | — (repo interface; INV-6) | **ACTIVE** | none | — |
| P01 | Core Infrastructure (CI & Gates) | gate encoding (RFC-0011 E-A) | **ACTIVE** | none | — |
| P02 | Knowledge System | S3 | **STANDING** | none | — |
| P03 | Language Definition | S4 | GATED | G-D01 | B-01 |
| P04 | Compiler | S5 | GATED | G-SPEC(S04/S05) | B-01, B-06, B-08 |
| P05 | Runtime | S6 | GATED (existence undecided) | G-D01 (U-14) | B-02 |
| P06 | Standard Library | S7 | GATED | G-D01 + P03 | B-01 |
| P07 | SDK | S8 | GATED | ratified interface specs | B-06, B-08 |
| P08 | Developer Tools | S9 | GATED (scope rule U-A) | tooling contract ratified | B-06 |
| P09 | Build System | S10 | GATED | compiler contract ratified | B-06 |
| P10 | Package Manager | S11 | **DEFERRED** | packaging decision at/after RFC-0001 acceptance | B-03 |
| P11 | Testing Infrastructure | S12 | **ACTIVE** | none | — |
| P12 | Verification & Conformance | S13 | PARTIALLY GATED | frame now; full scope needs P03 index | B-07, B-08 |
| P13 | Documentation System | S14 | **ACTIVE (frame)** | none; behavior docs need P03 | B-01 (behavior docs) |
| P14 | Release Infrastructure | S15 | GATED | G-CI (Article 9) | B-04, B-05 |
| P15 | AI Layer | S16 | **STANDING** | none | — |

## Non-programs (recorded, not planned)

| Candidate | Disposition | Source |
| --- | --- | --- |
| S1 Governance, S2 Architecture | Complete/Ratified — maintenance via RFC → ADR path only | ADR-0002, ADR-0004 |
| Planner | Rejected (P-A) — no program may be created without a new RFC | RFC-0013; ADR-0004 |
| Agent Framework | Rejected (A-A) | RFC-0016; ADR-0004 |
| Memory | Open — routing M-A/B/C unchosen; no program | RFC-0014; ADR-0004 |
| Context Engine | Open — blocked on definition (L-12); no program | RFC-0015; ADR-0004 |

## Global gates (state at plan issue, 2026-08-02)

| Gate | State |
| --- | --- |
| G0 governance closure | **MET** (PR #14 merged) |
| G-D01 identity decision + acceptance ADR | **OPEN — controlling** |
| G-CI mechanical gates live | OPEN (P01 exit) |
| G-SPEC(x) per-program spec ratification | OPEN for all |
| G-CONF conformance judgment available | OPEN |
