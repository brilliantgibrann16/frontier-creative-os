# FCOS Implementation Program

**Status:** Active (program plan)
**Artifact class:** Implementation Plan (program level) — carries **no decision
authority** (Blueprint §7). Binding decisions exist only as ADRs (Article 7,
INV-8, L-8). If this document conflicts with any ratified artifact, the
ratified artifact wins.
**Owner:** Maintainer (Article 6)

---

## 1. Purpose

This is the master engineering execution roadmap for Frontier Creative OS. It
defines the order in which every subsystem is built, the gates each program
must pass, and the blockers that prevent work from starting. It is an
execution plan, not a feature roadmap: ordering is **event-gated** (decisions,
ratifications, passing gates), never date-based.

## 2. Derivation sources (exhaustive)

| Source | Status | Authority |
| --- | --- | --- |
| Constitution v1 (`docs/constitution/`) | Ratified 1.0.0 | Rank 1 |
| Architecture Baseline (`docs/architecture/baseline.md`) | Ratified 1.0.0 (ADR-0002) | Rank 2 |
| Master System Blueprint (`docs/architecture/blueprint.md`) | Ratified — descriptive (ADR-0002) | None (descriptive) |
| Universal Engineering Doctrine (`docs/architecture/doctrine.md`) | Ratified — explanatory (ADR-0002) | None (explanatory) |
| ADR-0001 … ADR-0006 (`docs/decisions/`) | Accepted | Rank 3 |
| RFC-0001 … RFC-0017 (`docs/rfc/`) | Disposed per ADR-0004; RFC-0001 accepted (I-D), RFC-0007 decided (N-no), RFC-0012 discharged per ADR-0006 | Rationale only |
| Specifications S01–S16 (`specs/`) | **In Review — not ratified** | None until ratified |

Because no specification is ratified yet, **no program may cite `specs/` as
binding**. Ratification of the governing spec sections is the first work
package of every implementation program (see B-08).

## 3. Program taxonomy — subsystem coverage

Programs derive one-to-one from Blueprint §2 subsystems. Nothing is added.

| Program | Name | Blueprint subsystem | Status |
| --- | --- | --- | --- |
| P00 | Repository Bootstrap | — (repository interface, Blueprint §8; INV-6) | ACTIVE |
| P01 | Core Infrastructure (CI & Mechanical Gates) | gate encoding for S12/S15/S1 enforcement (U-12 → RFC-0011 E-A) | ACTIVE |
| P02 | Knowledge System | S3 | STANDING |
| P03 | Language Definition | S4 | ACTIVE (G-D01 met — ADR-0006) |
| P04 | Compiler | S5 | GATED |
| P05 | Runtime | S6 | GATED (exists — minimal scope S-B, ADR-0006) |
| P06 | Standard Library | S7 | GATED |
| P07 | SDK | S8 | GATED |
| P08 | Developer Tools | S9 | GATED (scope rule U-A) |
| P09 | Build System | S10 | GATED |
| P10 | Package Manager | S11 | CLOSED (RFC-0007 N-no, ADR-0006 — program does not exist) |
| P11 | Testing Infrastructure | S12 | ACTIVE |
| P12 | Verification & Conformance | S13 | PARTIALLY GATED |
| P13 | Documentation System | S14 | ACTIVE (frame) |
| P14 | Release Infrastructure | S15 | GATED (Article 9) |
| P15 | AI Layer | S16 | STANDING |

**Coverage notes (no invention):**

- **S1 Governance, S2 Architecture** are Complete/Ratified. They receive no
  implementation program; changes travel the RFC → ADR path only. Program
  documents may never modify them.
- **Planner and Agent Framework** subsystems were **rejected** (RFC-0013 P-A,
  RFC-0016 A-A per ADR-0004): no programs exist and none may be created
  without a new RFC.
- **Memory (RFC-0014)** and **Context Engine (RFC-0015)** remain **open**: no
  programs exist. If the Maintainer later decides them, this program plan is
  re-issued (see §6 change process).
- “Core Infrastructure” (P01) is not a new subsystem: it is the mechanical
  encoding of already-declared gates (INV-10, L-10, Article 9) per the
  accepted RFC-0011 recommendation E-A.

## 4. Global gates

| Gate | Definition | State |
| --- | --- | --- |
| **G0** | Governance closure: ADR-0004/0005 merged, indexes consistent (PR #14) | **MET** (2026-08-02) |
| **G-D01** | RFC-0001 decided by Maintainer and recorded as an acceptance ADR. Per RFC-0012 (procedural, ADR-0004) that ADR also resolves U-14; it unlocks full decisions on RFC-0005, RFC-0007, RFC-0009 | **MET** (2026-08-10, ADR-0006 — U-14 resolved S-B and RFC-0007 decided N-no in the same act; RFC-0005/RFC-0009 decision windows open) |
| **G-CI** | CI gates live per RFC-0011 E-A and enforced as required checks on `main` | OPEN (P01 exit) |
| **G-SPEC(x)** | The governing specification sections for program x are ratified (PR + recorded ratification per Article 7) | OPEN for all programs |
| **G-CONF** | Conformance judgment available from P12 for the ratified clause set | OPEN |

## 5. Program catalog

Each program carries the sixteen mandated planning fields. “Blocked-by”
entries record missing information with its governing artifact; they are
never to be filled by invention.

---

### P00 — Repository Bootstrap (ACTIVE)

- **Purpose:** a mechanically clean, navigable repository ready for
  many-agent contribution. Repository structure carries no decision
  authority (INV-6).
- **Scope:** hygiene only — remove the obsolete `specs/fcos/` scaffold
  (authorized by ADR-0005); remove tracked `__pycache__`; correct the
  prototype filename `writter.py`; delete merged branches; keep root and
  directory indexes current.
- **Deliverables:** clean tree matching the root README layout; hygiene PRs.
- **Dependencies:** none.
- **Required RFCs:** none. **Required ADRs:** none new (ADR-0005 suffices).
- **Required Specifications:** none.
- **Required Tests:** prototype test suite remains green after every
  move/rename.
- **Acceptance Gates:** PR review; CI green once P01 lands.
- **Exit Criteria:** no obsolete paths; tree matches documented layout.
- **Engineering Risks:** deleting a referenced path; breaking prototype
  imports on rename.
- **Rollback Strategy:** `git revert` of hygiene commits (pure-move changes
  revert cleanly).
- **Estimated Parallelism:** 1 stream.
- **Required Teams:** 1 engineer or AI agent + Maintainer review.
- **Repository Areas:** `specs/fcos/`, `tools/compiler/fcos/`, `tests/`.
- **Future Expansion:** recurring hygiene cadence attached to every wave.

---

### P01 — Core Infrastructure: CI & Mechanical Gates (ACTIVE)

- **Purpose:** encode the already-declared gates mechanically. CI enforces
  and never decides (INV-10, L-10); Article 9 makes CI a release
  precondition.
- **Scope:** exactly the accepted RFC-0011 E-A gate set: run the test suite;
  link-integrity checks; identifier/cross-reference checks. Gate-set
  expansion is decision-level and out of scope.
- **Deliverables:** `.github/workflows/` pipelines; check tooling under
  `tools/` (engineering tooling, within the RFC-0017 U-A scope rule);
  required-checks branch protection (Maintainer console action, recorded in
  the Ops Log).
- **Dependencies:** none hard; P00 helpful.
- **Required RFCs:** RFC-0011 (accepted, ADR-0004).
- **Required ADRs:** none new.
- **Required Specifications:** S12/S15 obligations inform design but E-A
  minimum does not require spec ratification.
- **Required Tests:** CI reproduces local test results deterministically;
  checks are themselves tested against known-bad fixtures.
- **Acceptance Gates:** CI green on `main`; required checks enabled.
- **Exit Criteria:** every PR mechanically gated; the standing no-CI risk
  closable in the Risk Register.
- **Engineering Risks:** CI drift into policy (L-10 violation); flaky checks
  eroding gate credibility.
- **Rollback Strategy:** revert workflow files; the declared gates are
  unaffected (they live above CI).
- **Estimated Parallelism:** 2 streams (test job; link/ID job).
- **Required Teams:** 1–2 engineers/agents + Maintainer review.
- **Repository Areas:** `.github/workflows/`, `tools/`.
- **Future Expansion:** release-gate encoding (P14), conformance jobs (P12),
  traceability checking over the RFC-0008 M-B clause index (post-P03).

---

### P02 — Knowledge System, S3 (STANDING)

- **Purpose:** derived recording of project state. The repository is
  authoritative; the mirror is one-way derived (L-9, INV-9).
- **Scope:** documented repo→mirror sync procedure for the ADR Log, RFC
  Index, Spec Index, Ops Log, and registers; staleness detection checklist.
- **Deliverables:** sync runbook; synchronized mirror after every governance
  or spec merge.
- **Dependencies:** none.
- **Required RFCs / ADRs:** none. **Required Specifications:** S03
  obligations (In Review) inform the runbook; ratification not required for
  manual procedure.
- **Required Tests:** per-sync consistency checklist (every ADR, RFC
  disposition, and spec status matches the repository).
- **Acceptance Gates:** zero repo/mirror conflicts (repo wins on conflict).
- **Exit Criteria:** standing program — steady state is “every merged change
  mirrored within one sync cycle”; no terminal exit.
- **Engineering Risks:** mirror treated as authority (INV-9 violation);
  silent drift.
- **Rollback Strategy:** resynchronize from the repository.
- **Estimated Parallelism:** 1.
- **Required Teams:** 1 agent per sync cycle.
- **Repository Areas:** read-only; writes land in the knowledge workspace.
- **Future Expansion:** sync automation — an engineering decision once
  tooling exists; never a source of authority.

---

### P03 — Language Definition, S4 (ACTIVE — G-D01 met, ADR-0006)

- **Purpose:** the sole home of meaning (INV-2); everything below the A3
  meaning line is judged against it.
- **Scope:** **pre-gate: none.** No syntax, grammar, or semantics may be
  drafted — RFC-0001 records no recommendation and inventing identity would
  violate L-1 and the no-invention rule. Post-gate: ratify the S04 container
  spec; produce the specification corpus that the D-01 decision defines;
  assign clause identifiers per RFC-0002 (N-B + N-C); build the
  machine-readable clause index per RFC-0008 (M-B — prose stays
  authoritative).
- **Deliverables:** ratified language-definition clauses; clause index;
  ratification records.
- **Dependencies:** G-D01.
- **Required RFCs:** RFC-0001 (accepted — identity I-D, ADR-0006); RFC-0002,
  RFC-0008 (accepted).
- **Required ADRs:** ADR-0006 (the RFC-0001 acceptance ADR — recorded); a
  recorded ratification per spec version (Article 7).
- **Required Specifications:** S04 (In Review; container only today).
- **Required Tests:** spec lint via P01 (ID validity, cross-references);
  alignment review against the P12 conformance suite.
- **Acceptance Gates:** per-clause ratification via PR + recorded decision.
- **Exit Criteria:** first ratified language-definition version. Versioning
  follows the interim rule V-D — no language version pre-1.0 (RFC-0009,
  ADR-0004).
- **Engineering Risks:** prototype contamination (L-7, INV-7); scope creep
  beyond the D-01 decision; clause-index tooling drifting into authority
  (M-B guard: prose wins).
- **Rollback Strategy:** ratified clauses are corrected by supersession,
  never edited in place (INV-18 analogue at spec rank).
- **Estimated Parallelism:** 1 stream until the clause index exists; N
  parallel clause streams after.
- **Required Teams:** spec editors + independent reviewers + Maintainer
  ratification.
- **Repository Areas:** `specs/` (home per ADR-0005), `docs/decisions/`.
- **Future Expansion:** conformance-level content (RFC-0004 frame); full
  versioning scheme post-1.0 (RFC-0009).

---

### P04 — Compiler, S5 (GATED: ratified S04 clauses)

- **Purpose:** first conforming translation implementation. The compiler
  never defines language behavior (INV-3); no implementation holds defining
  authority (RFC-0006 R-A).
- **Scope:** implementation plan → compiler realizing ratified clauses;
  diagnostics per the ratified diagnostics contract.
- **Deliverables:** conforming compiler; diagnostics; S12 test evidence;
  S13 conformance judgment.
- **Dependencies:** P03 (ratified clauses); P11 (harness); P12 (judge);
  G-CI.
- **Required RFCs:** RFC-0006 (accepted).
- **Required ADRs:** none decision-level foreseen; a recorded
  implementation-plan note fixes the source location before the first code
  PR — **Blocked-by: that recorded choice (Blueprint §8 leaves the
  compiler boundary UNKNOWN until specified)**.
- **Required Specifications:** S04 clauses + S05 compiler-boundary contract,
  ratified — **Blocked-by: G-SPEC(S05)**.
- **Required Tests:** unit + spec-derived tests (evidence only, INV-4).
- **Acceptance Gates:** CI; conformance judgment from P12 for the ratified
  clause set.
- **Exit Criteria:** compiler passes the conformance suite for all ratified
  clauses in scope.
- **Engineering Risks:** implementation semantics becoming de facto
  definition; private compiler↔runtime contracts (L-11 violation).
- **Rollback Strategy:** code revert; meaning is unaffected by construction
  (Blueprint §11 failure containment).
- **Estimated Parallelism:** 2–4 streams (front-end, diagnostics, back-end)
  once contracts are ratified.
- **Required Teams:** 2–4 engineers/agents + independent reviewers.
- **Repository Areas:** new implementation area (location per the recorded
  plan). The prototype `tools/compiler/fcos/` is **not** the starting point
  (L-7, INV-7).
- **Future Expansion:** optimization; additional targets — each via the
  normal decision path if consumer-observable.

---

### P05 — Runtime, S6 (GATED — exists, minimal scope S-B per ADR-0006)

- **Purpose:** spec-declared execution services — a validation-evaluation
  runtime (S-B, ADR-0006).
- **Scope:** **Resolved (ADR-0006): U-14 = S-B.** The program exists with
  minimal scope bounded by the validation-evaluation runtime; the runtime's
  observable behavior is spec-defined and it holds zero defining authority
  (L-3). S06 is scoped minimal now and grows only by recorded stage
  transitions; the boundary between the S-B runtime and S13 conformance
  tooling must be drawn precisely in specification work (RFC-0012 S-B row).
- **Deliverables / Required Tests / Acceptance Gates / Exit Criteria:**
  definable only as ratified S06 specification content lands (B-08);
  recorded here as pending, not invented.
- **Dependencies:** G-D01; P03; P12.
- **Required RFCs:** RFC-0001 + RFC-0012 (procedural).
- **Required ADRs:** ADR-0006 (recorded — disposes this program's existence
  as S-B).
- **Required Specifications:** S06 (In Review; bounds only).
- **Engineering Risks:** scope creep beyond the S-B validation-evaluation
  boundary; entering a later capability stage without its recorded RFC →
  ADR transition (CN-14).
- **Rollback Strategy:** no artifacts exist yet; code reverts once
  implementation begins.
- **Estimated Parallelism / Required Teams:** determined post-gate.
- **Repository Areas:** none pre-gate.
- **Future Expansion:** embedding boundary work (Blueprint §8) if the
  program exists.

---

### P06 — Standard Library, S7 (GATED: G-D01)

- **Purpose:** ratified, specified shipped capabilities.
- **Scope:** **Blocked-by: D-01 (scope UNKNOWN, Blueprint §2).** No library
  surface may be sketched pre-gate.
- **Dependencies:** G-D01; P03; P04 (a conforming implementation to run
  against); P12.
- **Required RFCs:** RFC-0001. **Required ADRs:** ratification records per
  library spec. **Required Specifications:** S07 (In Review; frame).
- **Required Tests:** spec-derived; conformance judged by P12 (INV-16).
- **Acceptance Gates:** clause ratification + conformance.
- **Exit Criteria:** first ratified library surface shipping with a
  conforming implementation.
- **Engineering Risks:** library surface defined by implementation
  convenience rather than ratified spec (INV-2).
- **Rollback Strategy:** supersession for specs; revert for code.
- **Estimated Parallelism:** high post-gate (per-module streams).
- **Required Teams:** determined post-gate.
- **Repository Areas:** `specs/` + implementation area per recorded plan.
- **Future Expansion:** growth is decision-gated per surface.

---

### P07 — SDK, S8 (GATED)

- **Purpose:** the only supported programmatic entry for developers and AI
  alike (Blueprint §8).
- **Scope:** versioned public developer interfaces over S5–S7.
  **Blocked-by: ratified interface specifications — all interface forms are
  UNKNOWN until specified (Blueprint §8).**
- **Dependencies:** P04 (and P05/P06 to the extent they exist); G-SPEC(S08).
- **Required RFCs:** none additional recorded. **Required ADRs:**
  ratification records for each published surface.
- **Required Specifications:** S08 (In Review; frame).
- **Required Tests:** contract tests against published surfaces.
- **Acceptance Gates:** CI + published-contract review (consumer-observable
  changes are decision-level events, Blueprint §13).
- **Exit Criteria:** first versioned SDK surface published.
- **Engineering Risks:** accidental de facto interfaces bypassing the SDK.
- **Rollback Strategy:** version supersession; published surfaces are never
  silently changed.
- **Estimated Parallelism:** per-surface streams.
- **Required Teams:** 1–2 per surface + reviewers.
- **Repository Areas:** implementation area per recorded plan.
- **Future Expansion:** additional language bindings — decision-gated.

---

### P08 — Developer Tools, S9 (GATED; scope rule U-A)

- **Purpose:** editing, navigation, diagnostics via published contracts
  only — never via implementation internals (Blueprint §3).
- **Scope:** the accepted RFC-0017 U-A scope rule confines S9 to
  **engineering tooling**. D-01-independent engineering checks are delivered
  under P01. Language-aware tooling is **Blocked-by: the published
  syntax-tree/tooling contract (UNKNOWN until S4/S05 specs ratify —
  Blueprint §8).**
- **Dependencies:** P01 (now); P03/P04 contracts (later).
- **Required RFCs:** RFC-0017 (accepted scope rule).
- **Required ADRs:** none new pre-gate.
- **Required Specifications:** S09 (In Review); the tooling contract spec.
- **Required Tests:** tool behavior tests against published contracts only.
- **Acceptance Gates:** CI; no-internals review check.
- **Exit Criteria:** language tooling consuming only ratified contracts.
- **Engineering Risks:** scope creep into product UI (rejected direction,
  RFC-0017/ADR-0004); internals coupling.
- **Rollback Strategy:** revert; contracts unaffected.
- **Estimated Parallelism:** per-tool streams.
- **Required Teams:** 1–2 per tool.
- **Repository Areas:** `tools/`.
- **Future Expansion:** editor integrations once contracts stabilize.

---

### P09 — Build System, S10 (GATED)

- **Purpose:** deterministic orchestration (Blueprint §2).
- **Scope:** **Blocked-by: the compiler invocation/artifact contract
  (UNKNOWN until S05 ratifies — Blueprint §8).** The prototype pipeline is
  historical context only (L-7).
- **Dependencies:** P04 contract; P11.
- **Required RFCs:** none additional recorded. **Required ADRs:**
  ratification record for the build contract.
- **Required Specifications:** S10 (In Review; frame).
- **Required Tests:** reproducibility tests (identical inputs → identical
  artifacts).
- **Acceptance Gates:** CI + reproducibility evidence.
- **Exit Criteria:** deterministic builds of every official artifact.
- **Engineering Risks:** hidden nondeterminism; build system accreting
  policy.
- **Rollback Strategy:** revert; build artifacts are disposable by class
  (Blueprint §7).
- **Estimated Parallelism:** 1–2 streams.
- **Required Teams:** 1–2.
- **Repository Areas:** implementation area per recorded plan; `build/`
  scaffold.
- **Future Expansion:** caching/distribution — engineering decisions within
  the ratified contract.

---

### P10 — Package Manager, S11 (CLOSED: RFC-0007 N-no, ADR-0006)

- **Purpose:** naming, versioning, distribution, resolution — **decided not
  needed** (RFC-0007 N-no, ADR-0006).
- **Scope:** **Decided (ADR-0006): N-no.** The mandatory RFC-0007 review was
  conducted inside the D-01 acceptance act: no package-distribution
  subsystem exists and this program does not exist. The interim N-defer
  disposition (ADR-0004) is superseded. S11 retires via the Baseline §13
  amendment path — supersession with a successor pointer, never deletion —
  as a queued follow-up. No work items exist.
- **Dependencies:** none — the packaging decision is taken (N-no); the
  program is closed.
- **Required RFCs:** RFC-0007 (reviewed — N-no). **Required ADRs:** ADR-0006
  (recorded). **Required Specifications:** S11 — retires via the Baseline
  §13 amendment (queued).
- **Required Tests / Acceptance Gates / Exit Criteria / Parallelism /
  Teams:** none — the program is closed (N-no).
- **Engineering Risks:** anticipatory registry work presuming an outcome.
- **Rollback Strategy:** n/a — closed with no artifacts.
- **Repository Areas:** none.
- **Future Expansion:** none — reopening requires a new RFC → ADR decision
  (CN-14).

---

### P11 — Testing Infrastructure, S12 (ACTIVE)

- **Purpose:** correctness evidence for implementations. Tests never define
  semantics (INV-4, L-4).
- **Scope now:** keep prototype tests green; harness conventions; evidence
  taxonomy (unit / spec-derived / conformance-facing); CI integration with
  P01. **Post-G-D01:** spec-derived test authoring conventions keyed to
  clause identifiers (RFC-0002).
- **Deliverables:** test harness conventions document; passing suites wired
  into CI.
- **Dependencies:** P01 (CI).
- **Required RFCs:** none additional. **Required ADRs:** none new.
- **Required Specifications:** S12 (In Review) obligations inform design.
- **Required Tests:** the harness is exercised by the existing prototype
  suite (6 tests) until real subjects exist.
- **Acceptance Gates:** CI green; evidence traceable to its subject.
- **Exit Criteria:** standing harness consumed by P04+ programs.
- **Engineering Risks:** tests drifting into semantics definition; evidence
  without traceability.
- **Rollback Strategy:** revert harness changes; evidence is regenerable.
- **Estimated Parallelism:** 1–2 streams.
- **Required Teams:** 1–2.
- **Repository Areas:** `tests/`, `.github/workflows/`.
- **Future Expansion:** performance evidence — **Blocked-by: no ratified
  quantitative requirement exists anywhere in the corpus (PR #13 census);
  budgets arrive only via ratified specs.**

---

### P12 — Verification & Conformance, S13 (PARTIALLY GATED)

- **Purpose:** the single implementation-independent judge (INV-16); judging
  authority delegated from ratified specs (L-4, Blueprint §4).
- **Scope now:** harness architecture consistent with the accepted RFC-0004
  frame (L-A + C-A). **Post-P03:** clause-indexed conformance suite
  (consuming the RFC-0008 M-B index); conformance levels remain **future
  work** per ADR-0004 — not to be invented here.
- **Deliverables:** conformance harness; per-clause suite; judgment reports.
- **Dependencies:** P03 (clauses + index); P11; G-CI.
- **Required RFCs:** RFC-0004 (accepted frame), RFC-0008 (accepted).
- **Required ADRs:** future level definitions via the normal path.
- **Required Specifications:** S13 (In Review); ratification required before
  judgments are official — **Blocked-by: G-SPEC(S13)**.
- **Required Tests:** the suite is itself validated against known-conforming
  and known-violating fixtures.
- **Acceptance Gates:** suite versioned with spec clauses (Blueprint §7).
- **Exit Criteria:** every ratified clause judgeable by the suite.
- **Engineering Risks:** suite divergence from prose (M-B guard: prose
  authoritative); implementation-specific leakage into the judge.
- **Rollback Strategy:** suite versions superseded, never silently edited.
- **Estimated Parallelism:** per-clause-family streams post-index.
- **Required Teams:** 1–2 pre-gate; scales with clause count.
- **Repository Areas:** conformance area per recorded plan; `specs/`.
- **Future Expansion:** third-party certification (U-13) — future RFC per
  RFC-0004 disposition.

---

### P13 — Documentation System, S14 (ACTIVE frame)

- **Purpose:** human-readable derivation from ratified content; informative
  only (L-2); behavior claims valid only if traceable to a ratified clause
  (Blueprint §9).
- **Scope now:** documentation generation over the ratified corpus
  (constitution, architecture, ADRs, RFC dispositions). **Behavior
  documentation is Blocked-by: existence of ratified clauses (P03).**
- **Deliverables:** derivation pipeline conventions; generated doc set.
- **Dependencies:** P01 (link checks); P03 for behavior docs.
- **Required RFCs / ADRs:** none new. **Required Specifications:** S14 (In
  Review) obligations inform design.
- **Required Tests:** every behavior claim carries a clause reference (lint
  via P01).
- **Acceptance Gates:** traceability lint green.
- **Exit Criteria:** standing pipeline regenerating docs from ratified
  sources.
- **Engineering Risks:** docs mistaken for definition (L-2); stale
  derivations.
- **Rollback Strategy:** regenerate; docs are freely correctable by class.
- **Estimated Parallelism:** 1–2 streams.
- **Required Teams:** 1–2.
- **Repository Areas:** documentation area per recorded plan (location is an
  implementation-plan note, not a governance change).
- **Future Expansion:** published documentation channels alongside P14.

---

### P14 — Release Infrastructure, S15 (GATED: Article 9)

- **Purpose:** gate-checked publication; CI results are the sole admissible
  evidence (Blueprint §9).
- **Scope:** release gate encoding on top of P01; release-notes process
  (immutable after publication). **Blocked-by (guarantees):** full
  compatibility policy — RFC-0005 accepted as interim instability window
  only; **Blocked-by (versioning):** RFC-0009 V-D interim rule — no language
  version pre-1.0; the full scheme awaits G-D01.
- **Deliverables:** encoded release gates; release runbook; first release
  only when gates + ratified content exist.
- **Dependencies:** G-CI (hard, Article 9); P03/P04/P12 for anything worth
  releasing.
- **Required RFCs:** RFC-0005, RFC-0009 (interim rules; full policies
  post-G-D01).
- **Required ADRs:** recording ADRs for the full compat + versioning
  policies when decided.
- **Required Specifications:** S15 (In Review).
- **Required Tests:** release dry-runs; gate-bypass detection.
- **Acceptance Gates:** all declared gates green; no unrecorded overrides.
- **Exit Criteria:** first gate-checked release of ratified content.
- **Engineering Risks:** gate bypass (requires recorded one-time exception,
  INV-20); releasing unratified content (INV-17).
- **Rollback Strategy:** releases superseded, never unpublished silently;
  notes immutable.
- **Estimated Parallelism:** 1 stream.
- **Required Teams:** 1 + Maintainer.
- **Repository Areas:** `.github/workflows/`, release area per recorded
  plan.
- **Future Expansion:** distribution channels — decision-gated (interacts
  with the deferred RFC-0007).

---

### P15 — AI Layer, S16 (STANDING)

- **Purpose:** artifact production/consumption via public interfaces only.
  Architecturally defined as the **absence** of a special interface (P-4,
  INV-19).
- **Scope:** agent contribution workflow conventions (identical PR/review
  gates; no self-approval, L-5); maintenance of the ratified Engineering
  Prompt library (`docs/prompts/`, class ratified by ADR-0003); attribution
  and the per-PR self-review disclosure duty (ADR-0004, J.4 note).
- **Deliverables:** agent workflow conventions document; maintained prompt
  library; attribution records.
- **Dependencies:** P01 (gates make the identical-path guarantee
  mechanical).
- **Required RFCs:** none new — Memory (RFC-0014) and Context Engine
  (RFC-0015) remain **open** and are explicitly excluded; Planner/Agent
  Framework are rejected (ADR-0004).
- **Required ADRs:** ADR-0003 (in force).
- **Required Specifications:** S16 (In Review) obligations inform
  conventions.
- **Required Tests:** convention compliance is review-checked; nothing
  semantic to test.
- **Acceptance Gates:** every AI PR passes the same gates as human PRs.
- **Exit Criteria:** standing program; steady state is fully attributable,
  gate-clean AI contribution at scale.
- **Engineering Risks:** AI-only channels forming (trust boundary table);
  hallucinated content reaching rank 1–5 artifacts (guarded by review
  path).
- **Rollback Strategy:** revert offending PRs; supersede tainted records.
- **Estimated Parallelism:** scales with agent count by design (Blueprint
  §10).
- **Required Teams:** all contributing agents + reviewing humans.
- **Repository Areas:** `docs/prompts/`; conventions doc under
  `docs/program/`.
- **Future Expansion:** only via new RFCs (e.g. if RFC-0014/0015 are ever
  decided).

---

## 6. Blocker register (program-level)

| ID | Blocker | Blocks | Governing artifact |
| --- | --- | --- | --- |
| B-01 | **Closed (ADR-0006, 2026-08-10):** D-01 decided — identity I-D (definition core with staged evolution) | P03–P10 entry — released | RFC-0001; ADR-0004; ADR-0006 |
| B-02 | **Resolved (ADR-0006):** U-14 = S-B — P05 exists with minimal validation-evaluation scope | P05 existence — resolved | RFC-0012 (procedural); ADR-0004; ADR-0006 |
| B-03 | **Closed (ADR-0006):** packaging decided N-no — P10 does not exist; S11 retirement via Baseline §13 amendment queued | P10 entirely — program closed | RFC-0007 (N-no); ADR-0004; ADR-0006 |
| B-04 | Compatibility policy: interim instability window only | P14 guarantees | RFC-0005; ADR-0004 |
| B-05 | No language versioning scheme pre-1.0 (V-D) | P14 versioned releases | RFC-0009; ADR-0004 |
| B-06 | All interface forms UNKNOWN until specified (compiler boundary, tooling contract, SDK surfaces, embedding, registry) | P04, P07, P08, P09 contracts | Blueprint §8 |
| B-07 | Conformance levels are future work; only the L-A + C-A frame is accepted | P12 full scope | RFC-0004; ADR-0004 |
| B-08 | Specifications S01–S16 are In Review, not ratified; nothing may build against them as binding | first WP of every implementation program | Blueprint §7 lifecycle; PR #13 |
| B-09 | Memory routing (M-A/B/C) and Context Engine definition (L-12) undecided | no programs exist for these candidates | RFC-0014, RFC-0015; ADR-0004 |
| B-10 | No ratified quantitative performance requirement exists anywhere | all performance budgets and performance testing | PR #13 blocked-section census |
| B-11 | `specs/fcos/` is not an empty scaffold — it holds ~40 substantive legacy specification documents; their disposal (delete / archive / adopt) is an undecided Maintainer question. Discovered during Wave 0 (PR #16); detailed in WAVE_0_VERIFICATION.md | P00.1 | ADR-0005 (governs the specification home, not legacy-content disposal); PR #16 verification record |

## 7. Change process

This program plan is revised by PR whenever (a) a gate changes state, (b) an
ADR lands that disposes a blocker, or (c) the Maintainer redirects
priorities. The plan itself never disposes a blocker: only ADRs do
(Article 7, INV-8). Superseded plan versions remain in history.
