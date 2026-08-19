# S13 — Verification & Conformance Subsystem Specification

**Status:** Ratified · **Subsystem:** S13 (Blueprint §2) · **Date:** 2026-08-19 · **Governing ADR:** ADR-0015
**Frame Dispositions:** RFC-0004 (L-A + C-A, accepted per ADR-0004), RFC-0008 (M-B, accepted per ADR-0004 / ADR-0010)

---

## Scope

The judgment machinery: the conformance test harness, fixture corpora, conformance claims, and the rules by which an implementation is declared conforming.

## Responsibilities

- Serve as the sole judge of conformance (INV-16); no implementation, test suite, or maintainer opinion substitutes.
- Derive every suite test and fixture directly from ratified specification clauses (L-4, CN-9; forbidden dependency Blueprint §3).
- Administer the binary conformance-claim regime and self-certification protocol (RFC-0004 L-A + C-A; ADR-0004, ADR-0015).

## Interfaces

- **Conformance Harness Boundary (`S13#2.1`–`S13#2.4`):** Black-box invocation driving candidate implementations exclusively via ratified public boundaries (S05 CLI `fcos-compile` / API `compile_artifact`).
- **Claim Surface (`S13#4.1`–`S13#4.4`):** Published machine-readable statements recording implementation version, specification version, harness hash, and evidence report digest.

## Data Model & Artifacts

- **Fixture Document:** Test ID, target clause IDs, input artifact payload, expected exit code, expected diagnostic codes, and expected output bundle structure.
- **Evaluation Report:** Structured machine-readable record (`conformance-report.json`) detailing per-clause evaluation traces and verdict.
- **Conformance Claim:** Official statement (`docs/conformance/claims/*.json`) certifying binary conformance status.

## State Machines

- **Suite Version:** Monotonically tracks specification revisions. New or amended clauses require a matching harness/fixture update.
- **Claim State:** `Asserted` → (`Standing` | `Invalidated` via supersession or discovered divergence). Claims are immutable; re-certification generates a new record.

## Error & Divergence Model

| Failure / Condition | Detection | Resolution |
|---|---|---|
| Fixture not clause-traced | Mechanical audit | Rejected; untraced fixture is invalid (`CN-9`). |
| Fixture encodes implementation behavior | Review vs specification prose | Specification defect (`L-4`); rewrite strictly from clause text. |
| Implementation passes suite but diverges from clause | Divergence discovery | Suite gap (`L-2`); implementation remains defective until suite gap closes. |
| Specification version mismatch | Automated harness check | Immediate rejection; candidate must declare exact target spec version. |

## Security & Integrity Requirements

- Harness execution must run in isolated, sandboxed environments.
- Self-certification (`C-A`) requires retained, published, reproducible evidence evaluation reports. Trust resides in verifiable evidence, not claimant assertion.

## Performance & Determinism Budgets

- Conformance judging and evaluation reports must be 100% deterministic and byte-reproducible across identical runs (`DP-28`, `S13#2.3`).

## Observability Requirements

- Public repository registry of all asserted conformance claims (`docs/conformance/claims/`).
- 100% clause traceability published in every evaluation report.

## Verification & Conformance Clause Set

Ratified per-clause by ADR-0015 (2026-08-19) through the amendment path (proposal RFC-0022 → recording ADR).

Clause declaration convention (mechanical — ADR-0010 / ADR-0011):
each clause is declared by exactly one list line beginning
`- **<clause ID> — <title>.**`. Clauses are listed in clause-ID order.
Every clause below has status **ratified** and is indexed in
`specs/S13-verification-conformance.index.yaml`.

- **S13#1.1 — Sole judge authority.** Category: defined. Conformance to FSL specifications is judged exclusively by the S13 Conformance Test Harness executing against ratified specification clauses (INV-16). (RFC-0022 §3.1.)
- **S13#1.2 — Binary conformance model.** Category: defined. Conformance is binary (`CONFORMING` vs `NON_CONFORMING`) for a given specification version. No partial conformance levels, tiers, or profiles exist in Stage 1 (RFC-0004 L-A, ADR-0004). (RFC-0022 §3.1.)
- **S13#1.3 — Clause totality.** Category: defined. To achieve `CONFORMING` status for a specification version, a candidate implementation must satisfy 100% of the active, testable ratified clauses for that version without exception. (RFC-0022 §3.1.)
- **S13#2.1 — Black-box invocation.** Category: defined. The conformance harness shall drive candidate implementations exclusively through their ratified public invocation boundaries without inspecting or depending on implementation internals (L-4, Blueprint §3). (RFC-0022 §3.2.)
- **S13#2.2 — Standard harness interface.** Category: defined. Candidate tools must accept standard input interchange files (`.fsl.json`) and emit standard exit codes and execution bundles (`.fcos-bundle.json`) or structured diagnostics. (RFC-0022 §3.2.)
- **S13#2.3 — Deterministic harness execution.** Category: defined. The harness must execute fixture suites in a deterministic, isolated environment, ensuring identical verdict outcomes across platforms (DP-28). (RFC-0022 §3.2.)
- **S13#2.4 — Reproducible test reporting.** Category: defined. Harness output shall consist of a structured, machine-readable Conformance Evaluation Report (`conformance-report.json`) detailing per-clause evaluations, fixture inputs, observed exit codes, and diagnostic match verifications. (RFC-0022 §3.2.)
- **S13#3.1 — Clause-traced fixtures.** Category: defined. Every fixture in the normative corpus (`tests/fixtures/conformance/`) must carry metadata explicitly tracing it to one or more ratified clause IDs (CN-9 discipline). (RFC-0022 §3.3.)
- **S13#3.2 — Dual-corpus requirement.** Category: defined. Every testable clause must be covered by at least one positive fixture and at least one negative fixture. (RFC-0022 §3.3.)
- **S13#3.3 — Fixture immutability.** Category: defined. Conformance fixtures are version-pinned to specification revisions; modifying fixture expectations requires an explicit specification amendment cycle. (RFC-0022 §3.3.)
- **S13#3.4 — Synthetic independence.** Category: defined. Fixtures must be authored directly from specification prose and sidecars, completely independent of implementation code. (RFC-0022 §3.3.)
- **S13#4.1 — Self-certification protocol.** Category: defined. Conformance claims are issued via self-certification backed by published, reproducible evidence dossiers (RFC-0004 C-A, ADR-0004). (RFC-0022 §3.4.)
- **S13#4.2 — Conformance claim structure.** Category: defined. A formal Conformance Claim document must record candidate name, commit SHA, release version, target specification version, harness hash, binary verdict, and evidence report digest. (RFC-0022 §3.4.)
- **S13#4.3 — Claim invalidation.** Category: defined. A standing claim is invalidated upon superseding specification ratification or upon verified specification divergence discovery. (RFC-0022 §3.4.)
- **S13#4.4 — Public claim registry.** Category: defined. All asserted claims are recorded immutably in the repository conformance registry (`docs/conformance/claims/`). (RFC-0022 §3.4.)

## Deferred Functionality

1. **Graded Conformance Levels (Core vs Full):** Deferred per RFC-0004 / ADR-0004. Binary model is enforced for Stage 1.
2. **Third-Party Certification Authorities:** Deferred per RFC-0004 C-A.
3. **Runtime & Dynamic Execution Conformance:** Deferred to Stage ≥ 2 (dependent on S06 Runtime specification).
4. **Performance Budgets & Benchmarking:** Deferred per WBS P11.4 / B-10 (no quantitative performance requirements ratified).
