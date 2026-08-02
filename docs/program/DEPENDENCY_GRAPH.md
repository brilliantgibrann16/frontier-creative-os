# Program Dependency Graph

**Artifact class:** Implementation Plan (analysis) — no decision authority.
Derived from Blueprint §3–§5 (subsystem, authority, and data-flow graphs)
and the ADR-0004 dispositions. Ordering is event-gated; no dates.

## 1. Complete dependency graph

Edges read “depends on”. Decision gates are diamonds.

```
                     ┌──────────────────────────────┐
                     │ WAVE 0 (executable today)      │
                     │  P00 Bootstrap                 │
                     │  P01 CI & Gates ◄── P00 (soft) │
                     │  P02 Knowledge (standing)      │
                     │  P11 Testing ◄───── P01        │
                     │  P13 Docs frame ◄─── P01 (lint)│
                     │  P15 AI Layer ◄───── P01 (gates)│
                     │  P12 frame ◄──────── P11       │
                     └───────────┬─────────────────┘
                                 │
                          ◇ G-D01 — RFC-0001 acceptance ADR
                          │   (also resolves U-14; unlocks
                          │    RFC-0005/0007/0009 decisions)
                                 │
                     ┌───────────▼─────────────────┐
                     │ WAVE 1                          │
                     │  P03 Language Definition (S4)   │
                     │   ├─ clauses (RFC-0002 IDs)     │
                     │   └─ clause index (RFC-0008 M-B)│
                     └──┬───────┬────────┬─────────┘
                        │       │        │
            ┌─────────▼─┐  ┌──▼────┐  ┌▼───────────┐
            │ WAVE 2     │  │ P05?  │  │ P12 full    │
            │  P04       │  │ (U-14)│  │ (suite over │
            │  Compiler  │  │ P06   │  │ clause idx) │
            └──┬───┬────┘  └───┬───┘  └─────┬──────┘
               │   │            │              │
     ┌────────▼┐ ┌▼──────────▼┐            │
     │ WAVE 3   │ │ P07 SDK     │            │
     │  P09     │ │ P08 Tools   │            │
     │  Build   │ │ (contracts) │            │
     └────┬────┘ └─────┬──────┘            │
          │             │                    │
          │   ◇ packaging decision           │
          │   (RFC-0007, at/after G-D01)     │
          │        └─► P10 Package Manager?  │
          │             │                    │
     ┌────▼────────────▼────────────────▼┐
     │ WAVE 4: P14 Release Infrastructure  │
     │ (Article 9: requires G-CI;          │
     │  releases require ratified content, │
     │  test evidence, conformance judgment)│
     └───────────────────────────────────┘

Standing lanes (run continuously, all waves):
  P02 Knowledge sync │ P13 Documentation │ P15 AI Layer │ P00 hygiene
```

**Edge list (hard dependencies only):**

| Program | Depends on | Nature |
| --- | --- | --- |
| P01 | — | none |
| P03 | G-D01 | decision gate |
| P04 | P03 (ratified clauses), P11, P12, G-CI | spec + evidence + judge |
| P05 | G-D01 (U-14), P03 | existence decided by gate |
| P06 | G-D01, P03, P04 | needs conforming implementation |
| P07 | P04 (+P05/P06 as they exist), G-SPEC(S08) | published surfaces |
| P08 | P01 (now); ratified tooling contract (later) | contract |
| P09 | P04 contract, P11 | reproducibility evidence |
| P10 | packaging decision (RFC-0007, post-G-D01) | deferred decision |
| P11 | P01 | CI wiring |
| P12 | P11 (now); P03 clause index (full) | judge inputs |
| P13 | P01 (lint); P03 (behavior docs) | traceability |
| P14 | G-CI (hard, Article 9); P03/P04/P12 for content | gates + content |
| P15 | P01 | mechanical gate parity |

## 2. Critical path

```
G-D01 (Maintainer decision + acceptance ADR)
  → P03: first ratified clause set + clause index (RFC-0002, RFC-0008)
  → P04: conforming compiler for that clause set
  → P11/P12: test evidence + conformance judgment (INV-16)
  → P14: first gate-checked release (Article 9)
```

**The critical path begins with a decision, not with engineering.** No
engineering acceleration shortens it while G-D01 is open. The only
critical-path work executable today is reducing downstream latency: P01
(gates), P11 (harness), P12 (frame) — all Wave 0.

Secondary critical dependency: P12's full suite consumes the P03 clause
index, so index production should be scheduled early inside P03.

## 3. Topological build order

1. **Wave 0 (now):** P00, P01 → P11 → P12(frame); P02, P13(frame), P15 in
   parallel.
2. **Gate:** G-D01.
3. **Wave 1:** P03 (clauses + index). P05 existence decided here (U-14);
   packaging decision window opens (RFC-0007).
4. **Wave 2:** P04; P05 (if it exists) and P06 as clauses ratify; P12 full
   suite in lockstep with the clause index.
5. **Wave 3:** P09 (after compiler contract); P07, P08 (after published
   contracts); P10 (only if decided).
6. **Wave 4:** P14 first release once every declared gate is green.

## 4. Parallel work opportunities

| Window | Parallel streams |
| --- | --- |
| Today (pre-G-D01) | P00 hygiene ∥ P01 test job ∥ P01 link/ID job ∥ P11 harness ∥ P12 frame ∥ P13 pipeline ∥ P02 sync ∥ P15 conventions — up to 8 independent streams |
| Wave 1 | pre-index: single P03 stream; post-index: N clause streams ∥ P12 suite streams |
| Wave 2 | P04 front-end ∥ diagnostics ∥ back-end; P06 per-module streams; P05 per its decided scope |
| Wave 3 | P07 per-surface ∥ P08 per-tool ∥ P09 |
| Always | standing lanes P02, P13, P15, P00 never block and are never blocked |

**Scale note (Blueprint §10):** parallelism is bounded by ratified-contract
availability, not headcount. Adding agents before contracts ratify only
lengthens review queues — see IMPLEMENTATION_STRATEGY.md.
