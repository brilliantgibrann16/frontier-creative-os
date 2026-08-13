# Work Breakdown Structure

**Artifact class:** Implementation Plan (WBS) — no decision authority.
Work packages are numbered `P<program>.<n>`. Blocked packages carry
`Blocked-by:` with the governing artifact and are **never** to be started by
inventing the missing information. Ordering inside a program is top-to-bottom
unless noted.

## P00 — Repository Bootstrap (ACTIVE)

- **P00.1** Remove obsolete `specs/fcos/` scaffold (authorized by ADR-0005).
- **P00.2** Remove tracked `__pycache__`; verify `.gitignore` covers it.
- **P00.3** Rename prototype `writter.py` → corrected name; fix imports;
  prototype tests must stay green.
- **P00.4** Delete merged remote branches (manual Maintainer action — no
  branch-deletion automation exists).
- **P00.5** Verify root README layout matches the tree after P00.1–P00.4.

## P01 — Core Infrastructure: CI & Gates (ACTIVE)

- **P01.1** CI workflow: run the prototype test suite on every PR and on
  `main` (RFC-0011 E-A).
- **P01.2** Link-integrity check over `docs/` and `specs/` (E-A).
- **P01.3** Identifier/cross-reference check (ADR/RFC/spec IDs resolve; E-A).
- **P01.4** Fixture tests for P01.2/P01.3 (known-bad inputs must fail).
- **P01.5** Enable required checks on `main` (Maintainer console action;
  record in Ops Log).
- **P01.6** Close the standing no-CI risk in the Risk Register(s).

## P02 — Knowledge System (STANDING)

- **P02.1** Write the repo→mirror sync runbook (ADR Log, RFC Index, Spec
  Index, Ops Log, registers; repo wins on conflict, L-9).
- **P02.2** Execute a full sync covering ADR-0002…0005, the RFC set
  dispositions, and the specs corpus (on Maintainer instruction).
- **P02.3** Staleness checklist executed after every governance/spec merge.

## P03 — Language Definition (EXECUTED at Stage 0 scope)

- **P03.0** Entry gate met — the RFC-0001 acceptance ADR is recorded
  (ADR-0006, 2026-08-10; G-D01 MET). No pre-gate packages existed by
  design (L-1).
- **P03.1** Ratify the S04 container specification (G-SPEC(S04)).
- **P03.2** Apply the RFC-0002 (N-B + N-C) identifier scheme to clause
  numbering; record the scheme's spec text.
- **P03.3** Draft → review → ratify the clause set the D-01 decision defines
  (scope comes from the acceptance ADR, not from this plan).
- **P03.4** Build the machine-readable clause index (RFC-0008 M-B; prose
  stays authoritative).
- **P03.5** Wire clause-index validation into P01 checks.
- **P03.6** Update `specs/` TODO(blocked-by…) markers that the acceptance
  ADR discharges (spec-editing work, done inside this program).

*Status (2026-08-13): P03.1–P03.6 are all executed — the per-package record
lives in `docs/program/S04_CHARTER.md` §7. The Stage 0 scope is a minimal
contract inventory (ADR-0011); language-content clauses enter S04 only
through the amendment path (RFC → recording ADR).*

## P04 — Compiler (GATED)

- **P04.0** ⛔ Entry — Blocked-by: ratified S04 clauses + ratified S05
  compiler-boundary contract (Blueprint §8; B-06, B-08).
- **P04.1** Record the implementation-plan note fixing source location and
  toolchain (no decision authority; just a recorded plan).
- **P04.2** Skeleton + diagnostics plumbing per the ratified diagnostics
  contract.
- **P04.3** Implement ratified clauses incrementally; every PR cites the
  clause IDs it realizes (INV-17 traceability).
- **P04.4** Spec-derived test evidence per clause (with P11).
- **P04.5** Conformance submission to P12; iterate to green.

## P05 — Runtime (GATED: existence undecided)

- **P05.0** ⛔ Entry — Blocked-by: U-14 resolution inside the RFC-0001
  acceptance ADR (RFC-0012 procedural; ADR-0004). If D-01 yields a
  non-executed language, close this program with a record. All further
  packages are defined post-gate.

## P06 — Standard Library (GATED)

- **P06.0** ⛔ Entry — Blocked-by: D-01 (scope UNKNOWN, Blueprint §2).
- **P06.1** Ratify library surface specs per module (post-gate).
- **P06.2** Implement per ratified surface; conformance per P12.

## P07 — SDK (GATED)

- **P07.0** ⛔ Entry — Blocked-by: ratified interface specifications
  (Blueprint §8 marks all interface forms UNKNOWN).
- **P07.1** Ratify the first public surface spec (G-SPEC(S08)).
- **P07.2** Implement + contract-test the surface; version it.

## P08 — Developer Tools (GATED; scope rule U-A)

- **P08.0** ⛔ Entry (language tooling) — Blocked-by: published
  syntax-tree/tooling contract (UNKNOWN until S4/S05 ratify).
- **P08.1** Engineering checks already in scope are delivered under P01
  (RFC-0017 U-A confines S9 to engineering tooling).
- **P08.2** Post-contract: language-aware tools consuming only ratified
  contracts; no-internals review gate.

## P09 — Build System (GATED)

- **P09.0** ⛔ Entry — Blocked-by: ratified compiler invocation/artifact
  contract (Blueprint §8).
- **P09.1** Deterministic orchestration per contract; reproducibility tests.

## P10 — Package Manager (DEFERRED)

- **P10.0** ⛔ Entry — Blocked-by: packaging decision at/after RFC-0001
  acceptance (RFC-0007 N-defer; ADR-0004). No packages defined; if decided
  “not needed”, close with a record.

## P11 — Testing Infrastructure (ACTIVE)

- **P11.1** Keep the prototype suite green; wire into P01.1.
- **P11.2** Document harness conventions and the evidence taxonomy
  (unit / spec-derived / conformance-facing; INV-4: evidence, never
  definition).
- **P11.3** Traceability convention: every future spec-derived test names
  its clause ID (consumes RFC-0002 scheme post-P03).
- **P11.4** ⛔ Performance testing — Blocked-by: no ratified quantitative
  requirement exists (PR #13 census; B-10).

## P12 — Verification & Conformance (PARTIALLY GATED)

- **P12.1** Harness architecture per the accepted RFC-0004 frame (L-A +
  C-A); implementation-independent by construction (INV-16).
- **P12.2** ⛔ Fixture validation (harness judges known-conforming and
  known-violating fixtures correctly) — Blocked-by: G-SPEC(S13) + B-08
  (`CONFORMANCE_FRAME.md` §2 records packages P12.2 and beyond as
  blocked; no ratified clauses exist to judge against).
- **P12.3** ⛔ Clause-indexed suite — the P03.4 clause-index prerequisite is
  met (`specs/S04-language-definition.index.yaml`, ADR-0011); still
  Blocked-by: the P12.2 harness (G-SPEC(S13) + B-08) and the absence of
  ratified language-behavior clauses to judge.
- **P12.4** ⛔ Official judgments — Blocked-by: S13 ratification
  (G-SPEC(S13)).
- **P12.5** ⛔ Conformance levels — Blocked-by: future work per ADR-0004
  (RFC-0004 frame only).

## P13 — Documentation System (ACTIVE frame)

- **P13.1** Derivation pipeline conventions over the ratified corpus
  (constitution, architecture, ADRs, dispositions).
- **P13.2** Traceability lint: behavior claims must carry clause refs
  (with P01).
- **P13.3** ⛔ Behavior documentation — Blocked-by: existence of ratified
  language-behavior clauses (the Stage 0 contract inventory ratified by
  ADR-0011 records governance obligations, not language behavior; behavior
  clauses enter S04 only through the amendment path).

## P14 — Release Infrastructure (GATED: Article 9)

- **P14.0** ⛔ Entry — Blocked-by: G-CI (P01.5 complete and stable).
- **P14.1** Encode release gates on top of CI; gate-bypass detection.
- **P14.2** Release-notes process (immutable after publication).
- **P14.3** ⛔ Versioned language releases — Blocked-by: RFC-0009 V-D
  interim rule (no language version pre-1.0) and the post-G-D01 full
  scheme.
- **P14.4** ⛔ Compatibility guarantees — Blocked-by: RFC-0005 full policy
  (interim instability window only).
- **P14.5** First gate-checked release (needs P03/P04/P12 outputs).

## P15 — AI Layer (STANDING)

- **P15.1** Agent contribution conventions: identical gates, attribution,
  no self-approval (L-5, INV-19), per-PR self-review disclosure duty
  (ADR-0004 J.4 note).
- **P15.2** Maintain `docs/prompts/` (class ratified by ADR-0003); prompts
  updated only via PR.
- **P15.3** ⛔ Memory / Context Engine work — Blocked-by: RFC-0014 routing
  and RFC-0015 definition (both open per ADR-0004). Excluded from this
  program.
