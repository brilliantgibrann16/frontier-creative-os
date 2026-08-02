# Program Risk Register

**Artifact class:** Implementation Plan (register) — no decision authority.
Scope: risks to **program execution**. Architectural failure containment is
already designed in Blueprint §11 and is not restated here. The knowledge
workspace mirrors this register (repo copy authoritative, L-9/INV-9).

| ID | Risk | Programs | Likelihood | Impact | Mitigation | Governing artifact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PR-01 | G-D01 stays open indefinitely; the entire critical path is stalled and Wave 0 completes with nothing to feed | P03–P10, P14 | Medium | Critical | Wave 0 exhausts all D-01-independent work; RFC-0001 decision materials are complete and awaiting the Maintainer; nothing else can shorten this | RFC-0001; ADR-0004 | Open |
| PR-02 | Single-Maintainer review/decision bottleneck as agent count grows | all | High | High | One-package-one-PR keeps units small; RFC-0010 (accepted G-D + cooling rule) provides the growth procedure when the bottleneck binds | RFC-0010; ADR-0004; Article 6 | Open |
| PR-03 | CI absent while development proceeds; unmerged gates erode Article 9 discipline | P01, P14 | High until P01 exits | High | P01 is first in Wave 0; required checks enabled at P01.5; standing no-CI risk closed only then | Article 9; RFC-0011 | Open |
| PR-04 | CI drift into policy (checks quietly becoming rules) | P01, P14 | Medium | Medium | L-10: a CI change is never a policy change; gate-set expansion routed to the decision path; fixture tests pin check behavior | L-10; INV-10 | Open |
| PR-05 | Prototype contamination: Phase 0 pipeline shapes language/compiler design | P03, P04, P09 | Medium | High | L-7/INV-7 quarantine; P04.1 records a fresh implementation plan; reviews reject prototype-derived design rationale | L-7; INV-7 | Open |
| PR-06 | Implementation semantics become de facto definition (spec–implementation divergence) | P04–P07 | Medium | Critical | INV-2/INV-3; every code PR cites clause IDs (INV-17); P12 judges independently (INV-16) | INV-2/3/16/17 | Open |
| PR-07 | Clause index or generated artifacts treated as authority over prose | P03, P12, P13 | Low | High | RFC-0008 M-B guard: prose authoritative; index validation is mechanical only | RFC-0008; ADR-0004 | Open |
| PR-08 | AI-generated content reaches rank 1–5 artifacts without human ratification | all, esp. P03 | Medium | Critical | Trust boundary: untrusted-until-reviewed; no self-approval (L-5); identical gates (INV-19); disclosure duty (ADR-0004) | Blueprint §9; L-5; INV-19 | Open |
| PR-09 | Anticipatory work presumes open decisions (runtime, packaging, memory, context engine) | P05, P10, P15 | Medium | High | Entry gates hard-block WBS P05.0/P10.0/P15.3; Blueprint §14 rule: no unknown resolved implicitly | RFC-0007/0012/0014/0015; ADR-0004 | Open |
| PR-10 | Tool scope creep beyond the U-A engineering-tooling rule (product UI by accretion) | P08 | Low | Medium | RFC-0017 scope rule cited in P08 reviews; rejected directions (Planner, Agent Framework) have no programs | RFC-0017; ADR-0004 | Open |
| PR-11 | Mirror drift or mirror treated as authority | P02 | Medium | Low | L-9 one-way authority; per-sync consistency checklist; repo wins on conflict | L-9; INV-9 | Open |
| PR-12 | Traceability debt: code/tests/docs lose clause linkage as volume grows | P04+, P11, P13 | Medium | High | Machine-checkable traceability via P01 ID checks + clause index; traceability is a merge gate, not a cleanup task | INV-17; RFC-0002/0008 | Open |
| PR-13 | Parallel-agent merge congestion and conflicting edits to shared files | all waves | Medium | Medium | One WBS package per branch; contract-bounded parallelism; standing lanes isolated from wave lanes | Blueprint §10 | Open |
| PR-14 | Flaky or slow gates erode trust and invite bypasses | P01, P14 | Medium | High | Fixture-tested checks (P01.4); gate bypass requires a recorded one-time exception (INV-20); bypass detection in P14.1 | INV-20; Article 9 | Open |
| PR-15 | Invented performance budgets enter specs or tests under delivery pressure | P11, P12, specs | Low | High | B-10 standing block: no quantitative requirement exists until ratified; reviews reject numeric budgets without a ratified source | PR #13 census; INV-17 | Open |
| PR-16 | Release pressure before versioning/compat policies exist post-G-D01 | P14 | Medium | High | P14.3/P14.4 hard blocks; interim rules V-D + instability window are the only guarantees until superseding ADRs land | RFC-0005/0009; ADR-0004 | Open |

## Review cadence

This register is reviewed and updated by PR at every gate transition
(G-D01, G-CI, each G-SPEC) and whenever a milestone surfaces a new
execution risk. Risks close only with the evidence that closes them
(e.g. PR-03 closes at P01.5), never by assertion.
