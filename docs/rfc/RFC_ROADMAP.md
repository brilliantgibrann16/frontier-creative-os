# RFC Architectural Review and Acceptance Roadmap

**Class:** Derived review artifact — informative, zero authority.
**Date:** 2026-08-02 · **Scope:** RFC-0001…RFC-0017 (`docs/rfc/`, branch `docs/rfc-decision-set`)

> **Self-review disclosure.** The author of the reviewed RFCs and the
> author of this review are the same actor — a live instance of blocker
> J.4 (sole-maintainer review). Mitigation: mechanical rubric, explicit
> traceability checks, and every verdict expressed as a non-binding
> recommendation to the Maintainer. RFC-0010's interim cooling-period
> rule, once adopted, governs exactly this situation.

## Review rubric

Completeness (/10): structure (2), traceability to ratified corpus (2),
alternatives with trade-offs (2), open-question coverage (2),
decidability clarity — what acceptance means and what blocks it (2).

Classification: **READY** = Maintainer can decide now with information
in hand · **NEEDS REVISION** = defect in the RFC itself · **BLOCKED** =
decision requires an unresolved upstream decision or missing input ·
**REJECT** = reviewer recommends closing with a rejection outcome.

## Classification summary

| RFC | Title (short) | Score | Class | Blocked by |
| --- | --- | --- | --- | --- |
| 0001 | Language identity | 9 | READY | — (requires Maintainer deliberation) |
| 0002 | Identifier scheme | 9 | READY | — |
| 0003 | Spec taxonomy | 9 | READY | — |
| 0004 | Conformance frame | 8 | READY (frame only) | levels: 0001 + first spec |
| 0005 | Compatibility policy | 8 | BLOCKED | 0001 (interim rule severable now) |
| 0006 | Reference impl policy | 9 | READY (posture) | — |
| 0007 | Package distribution | 7 | BLOCKED | 0001 (necessity), 0002, 0009 |
| 0008 | Machine-readable specs | 8 | READY (posture only) | schema: 0001 + first spec |
| 0009 | Language versioning | 8 | BLOCKED | 0001; joint with 0005 |
| 0010 | Governance procedure | 9 | READY | — |
| 0011 | CI gate encoding | 8 | READY | — (audit depth: 0008) |
| 0012 | Runtime scope | 8 | BLOCKED | 0001 (resolve in same ADR) |
| 0013 | Candidate: Planner | 7 | REJECT | reopen path: necessity evidence |
| 0014 | Candidate: Memory | 8 | READY (routing only) | design: 0001 or evidence |
| 0015 | Candidate: Context Engine | 6 | BLOCKED | Maintainer definition (L-12) |
| 0016 | Candidate: Agent Framework | 8 | REJECT | reopen path: evidence + bounds analysis |
| 0017 | Candidate: Product UI | 8 | READY (scope ruling) | U-B path: 0001 + evidence |

**NEEDS REVISION: none assigned.** The set was authored this session
against the ratified corpus, so structural defects are unlikely to be
found by the same author — see the self-review disclosure. Independent
defect discovery is exactly what Maintainer review of PR #12 is for.

## Dependency graph

```
Merge order:  PR #11 ==> PR #12  (RFCs cite ADR-0002/0003 + prompt files)

RFC-0010 --> (review legitimacy for every acceptance below)
RFC-0002 --> RFC-0008 (clause-ID compatibility, co-design)
RFC-0002 --> RFC-0007 (package namespaces)
RFC-0008 --> RFC-0011 (mechanical audit depth)
RFC-0010 --> RFC-0004 (certification option C-C only)

RFC-0001 ==> RFC-0005 (policy family)     ==> joint with RFC-0009
RFC-0001 ==> RFC-0007 (necessity)
RFC-0001 ==> RFC-0008 (schema, not posture)
RFC-0001 ==> RFC-0009 (stable scheme)
RFC-0001 ==> RFC-0012 (runtime scope; same ADR recommended)
RFC-0001 ==> RFC-0004 (level enumeration, with first spec)
RFC-0001 ==> RFC-0014 route M-A / RFC-0017 path U-B

No cycles. Single dominating node: RFC-0001 (D-01).
```

**Conflicts:** no RFC–RFC conflicts found. Two document-level conflicts
exist: (1) RFC-0013–0017 outcomes vs the WP15 prompt file's subsystem
list (already flagged in PR #11) — resolved automatically by the
candidate-disposition ADR in Step 8 below; (2) RFC-0003 option T-B would
contradict the recorded 2026-08-01 dual-homing decision — internal to
that RFC and requires explicit supersession if chosen.

## Per-RFC review

### RFC-0001 — Language Identity (9/10, READY)
- **Blocking / blocked-by:** blocks 7 RFCs (see graph); blocked by nothing.
- **Conflicts:** none.
- **Missing information:** the Maintainer's vision and decision criteria
  (year-1/5/20 success answers) — asked as open questions, unanswerable
  by anyone else; not a defect.
- **Implementation risk:** none from acceptance; extreme from *non*-decision
  (R-1 Critical: any implementation decides identity by accident, CN-14).
- **Governance impact:** highest — the acceptance ADR is the most
  consequential decision since the Constitution; should resolve or
  explicitly re-defer U-14 (RFC-0012) and review U-8 (RFC-0007).
- **Recommendation:** decide last in Wave 0 order but as soon as
  deliberation allows; do not let any Wave-2 pressure force it.

### RFC-0002 — Identifier Scheme (9/10, READY)
- **Blocks:** 0008 (co-design), 0007. **Blocked by:** —. **Conflicts:** none.
- **Missing:** namespace registry ownership answer (open question for ADR).
- **Implementation risk:** low; late decision forces renumbering churn
  that grows with every artifact created.
- **Governance impact:** medium — freezes IDs project-wide (A-1 no-reuse).
- **Recommendation:** accept early (Step 2); N-B+N-C is coherent and
  migration cost is near zero today.

### RFC-0003 — Spec Taxonomy (9/10, READY)
- **Blocks:** location of all ratified output. **Blocked by:** —.
- **Conflicts:** option T-B vs recorded 2026-08-01 decision (internal).
- **Missing:** U-9 tooling preference (interacts with T-C only).
- **Implementation risk:** low; ambiguity cost compounds at first spec.
- **Governance impact:** low-medium; T-A closes audit finding F-3.
- **Recommendation:** accept T-A (Step 4); retire empty playbook scaffold.

### RFC-0004 — Conformance Frame (8/10, READY — frame only)
- **Blocks:** certification claims. **Blocked by (levels):** 0001 + first
  spec; (option C-C): 0010. **Conflicts:** none.
- **Missing:** clause-category exclusion rules — deferred by design.
- **Implementation risk:** medium if undecided when a second
  implementation appears (ad-hoc precedent).
- **Governance impact:** medium; binds all future implementations.
- **Recommendation:** accept frame L-A + C-A (Step 6); revisit levels at
  first spec ratification.

### RFC-0005 — Compatibility Policy (8/10, BLOCKED by 0001)
- **Coupled:** joint decision with 0009. **Conflicts:** none.
- **Missing:** observable-surface definition (feeds from WP16 work).
- **Implementation risk:** high if unaddressed — accidental guarantees
  form the day anything is published (OB-6).
- **Governance impact:** high; promises bind for decades.
- **Recommendation:** sever the interim instability-window rule into a
  lightweight ADR now (Step 9); decide policy family after 0001 (Step 11).

### RFC-0006 — Reference Implementation Policy (9/10, READY — posture)
- **Blocks:** S5 posture. **Blocked by:** — (concrete plan: 0001).
- **Conflicts:** none. **Missing:** none for the posture decision.
- **Implementation risk:** decision *prevents* the project's
  highest-rated implementation risk (R-4 compiler-is-the-spec).
- **Governance impact:** medium; structural rejection of R-C is already
  implied by ratified P-1/L-3 — acceptance makes it explicit.
- **Recommendation:** accept R-A default posture (Step 7).

### RFC-0007 — Package Distribution (7/10, BLOCKED by 0001)
- **Blocked by:** 0001 (necessity), 0002 (namespaces), 0009 (versions).
- **Conflicts:** none. **Missing:** necessity itself — by design (S11 is
  the only conditionally-existing subsystem).
- **Implementation risk:** low now; high if infrastructure is built
  before necessity is decided.
- **Governance impact:** medium (trust/supply-chain frame later).
- **Recommendation:** record N-defer inside 0001's acceptance ADR (Step 12).

### RFC-0008 — Machine-Readable Specs (8/10, READY — posture only)
- **Blocks:** 0011 audit depth; co-designed with 0002. **Blocked by
  (schema):** 0001 + first spec. **Conflicts:** none.
- **Missing:** audit-priority list from Doctrine §13 (open question).
- **Implementation risk:** medium — without a posture, tooling improvises
  formats (shadow-spec hazard, Baseline §7).
- **Governance impact:** medium; fixes which representation is
  authoritative (AX-1 application).
- **Recommendation:** accept M-B posture (Step 3, adjacent to 0002).

### RFC-0009 — Language Versioning (8/10, BLOCKED by 0001)
- **Coupled:** joint with 0005. **Conflicts:** none.
- **Missing:** in-language vs manifest declaration (D-01-dependent).
- **Implementation risk:** medium; conflation of the three version
  spaces is how accidental promises form.
- **Governance impact:** medium-high (parameterizes certification).
- **Recommendation:** sever interim V-D rule now (Step 9); decide with
  0005 after 0001 (Step 11).

### RFC-0010 — Governance Procedure (9/10, READY)
- **Blocks:** legitimacy of every subsequent acceptance; 0004 option C-C.
  **Blocked by:** —. **Conflicts:** none.
- **Missing:** successor identity (only the Maintainer can supply).
- **Implementation risk:** none direct; governance debt compounds (OB-4).
- **Governance impact:** highest of the D-01-independent set — frames a
  constitutional amendment (Article 6) and neutralizes J.4 via the
  interim cooling rule.
- **Recommendation:** accept **first** (Step 1); every later acceptance
  then happens under a ratified review procedure.

### RFC-0011 — CI Gate Encoding (8/10, READY)
- **Blocks:** Article 9 enforceability. **Blocked by (depth):** 0008.
  **Conflicts:** none.
- **Missing:** gate-vs-signal answer for doc audits during design phase.
- **Implementation risk:** low; posture E-A is reversible and additive.
- **Governance impact:** medium — makes Article 9 mechanical; closes the
  Risk Register's oldest open item.
- **Recommendation:** accept E-A (Step 5); workflow files land as
  ordinary reviewed PRs afterward (hygiene, not "implementation").

### RFC-0012 — Runtime Scope (8/10, BLOCKED by 0001)
- **Conflicts:** none. **Missing:** nothing beyond D-01 itself.
- **Implementation risk:** high if runtime is defined implicitly by
  first implementation (R-4 analogue).
- **Governance impact:** S-A outcome would require a Baseline amendment
  (subsystem retirement) — flagged so the §13 path is followed.
- **Recommendation:** resolve inside 0001's acceptance ADR (Step 10) —
  one identity choice viewed twice.

### RFC-0013 — Candidate: Planner (7/10, REJECT)
- **Blocked-by (reopen):** Maintainer necessity evidence. **Conflicts:**
  WP15 file (document-level).
- **Missing:** the necessity case — deliberately not invented.
- **Implementation risk:** none from rejection; rejection is reversible
  by new RFC with evidence.
- **Governance impact:** low; disposes of one WP15 conflict item.
- **Recommendation:** close with P-A in the candidate-disposition ADR
  (Step 8) unless evidence is supplied during review.

### RFC-0014 — Candidate: Memory (8/10, READY — routing only)
- **Blocked by (design):** 0001 under route M-A; evidence under M-B.
- **Conflicts:** WP15 file (document-level).
- **Missing:** the Maintainer's intended reading (M-A/M-B/M-C).
- **Implementation risk:** low; routing answer is costless.
- **Governance impact:** low.
- **Recommendation:** answer routing in the Step-8 ADR; M-A folds into
  S4 work, M-B joins 0013's evidentiary bar.

### RFC-0015 — Candidate: Context Engine (6/10, BLOCKED)
- **Blocked by:** Maintainer definition of the term (L-12 precondition).
- **Conflicts:** WP15 file (document-level).
- **Missing:** the definition itself; overlap analysis vs S3/S14/S16
  cannot run without it. Lowest score in the set for exactly this reason.
- **Implementation risk:** none while blocked.
- **Governance impact:** low; interacts with the open Article-2
  interpretation flag.
- **Recommendation:** in the Step-8 ADR, either define-and-route or
  close as C-A (undefined terms cannot enter the subsystem graph).

### RFC-0016 — Candidate: Agent Framework (8/10, REJECT)
- **Blocked-by (reopen):** necessity evidence + explicit INV-19/CN-23
  bound-compliance analysis; Article-2 interpretation flag must be
  resolved before any acceptance.
- **Conflicts:** WP15 file (document-level).
- **Missing:** what a framework adds beyond what INV-19 already permits
  (AI participation demonstrably works today through ordinary interfaces).
- **Implementation risk:** the A-C path carries the set's highest
  structural risk (privileged-channel creep against CN-23).
- **Governance impact:** medium — touches the constitutional Article 2 zone.
- **Recommendation:** close with A-A in the Step-8 ADR; document A-B
  conventions later if AI-contributor friction is actually observed.

### RFC-0017 — Candidate: Product UI (8/10, READY — scope ruling)
- **Blocked by (U-B path):** 0001 + necessity evidence. **Conflicts:**
  WP15 file (document-level).
- **Missing:** the U-A/U-B scope ruling — only the Maintainer can give it.
- **Implementation risk:** low under U-A; U-B before 0001 would be
  identity-by-accident (CN-14).
- **Governance impact:** low-medium; U-B would also signal identity
  I-B/I-C, so the two decisions belong together.
- **Recommendation:** rule U-A in the Step-8 ADR (reversible); revisit
  U-B inside or after 0001.

## Acceptance roadmap (exact order)

**Step 0 — prerequisites (not RFC acceptances):** merge PR #11, then
PR #12; perform the ADR-0002 status-header hygiene commit.

| Step | Action | Resolves | Why this position |
| --- | --- | --- | --- |
| 1 | Accept RFC-0010 (G-D + interim cooling rule) | U-11, J.4 | Everything after happens under a ratified review procedure |
| 2 | Accept RFC-0002 (N-B+N-C) | U-2/D-03 | IDs freeze before more artifacts accumulate |
| 3 | Accept RFC-0008 posture (M-B) | U-9 (posture) | Co-designed with Step 2 clause-ID rules |
| 4 | Accept RFC-0003 (T-A) | U-3/D-13, F-3 | Spec home fixed before any spec exists |
| 5 | Accept RFC-0011 (E-A) | U-12, no-CI risk | Article 9 becomes mechanical |
| 6 | Accept RFC-0004 frame (L-A + C-A) | U-5/D-04 frame | Prevents ad-hoc conformance precedent |
| 7 | Accept RFC-0006 posture (R-A) | U-7 | Structurally forecloses R-4 before any impl work |
| 8 | Candidate-disposition ADR: reject 0013 (P-A), reject 0016 (A-A), route 0014, rule 0017 (U-A), define-or-close 0015 | WP15 conflict | One ADR disposes of all five candidates and the PR #11 flag |
| 9 | Lightweight interim-rules ADR severed from 0005+0009 (instability window; no language version pre-1.0) | accidental-promise hazard | Decidable now without accepting either RFC |
| 10 | **Accept RFC-0001** (identity summit), resolving RFC-0012 (U-14) and reviewing RFC-0007 (U-8 N-defer) in the same ADR | U-1/D-01, U-14 | The controlling decision, taken with maximal recorded context |
| 11 | Accept RFC-0005 + RFC-0009 jointly | U-6, U-10 | Meaningful only post-identity; mutually coupled |
| 12 | Decide RFC-0007 necessity | U-8 | Post-identity, post-0002/0009 |
| 13 | Revisit RFC-0004 level enumeration | U-5 residue | At first specification ratification |

Steps 1–9 are executable in a single governance sitting; none depend on
D-01. Step 10 is the summit and should take as long as it needs.

## Dependency-gap check (per mission rule)

No dependency gap requiring a new RFC was discovered. Every blocking
edge lands on an existing RFC, a Maintainer input, or the merge-order
prerequisite. U-4's playbook remainder is covered inside RFC-0003.
