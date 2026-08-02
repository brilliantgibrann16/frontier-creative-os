# WP30 — Final System Audit Prompt

Class: Derived-executable. Governing anchors: Doctrine §13 (architectural
mathematics: checkable properties 1–5), §16 (consistency/completeness
audit form), Baseline §13 (amendment review), Blueprint §12 (INV-1–20),
§14 (U-1–14).

## Mission

Execute a full-system consistency, traceability, and health audit of the
FCOS ecosystem — the recurring closing gate for every major engineering
cycle.

## Objectives

1. **Structural checks** (mechanical, from Doctrine §13):
   - ⊑-acyclicity: the authority graph over all artifacts is a DAG
     (CN-27);
   - single-governor: every artifact except the Constitution has exactly
     one primary governor;
   - flow legality: every information channel is classified forward,
     feedback, or forbidden (CN-28), and no illegal reverse flow from
     Baseline §7 is instantiated;
   - trace closure: every shipped behavior reaches a ratified clause and
     a recorded decision (INV-17, AX-4).
2. **Invariant sweep**: check each of INV-1…INV-20 against the current
   repository and workspace state; record pass/fail with evidence.
3. **Unknown discipline check**: no unknown (U-1…U-14 plus any new)
   resolved implicitly by shipped behavior (CN-14/CN-30); unknown count
   reported as the health metric (DP-32).
4. **Vocabulary check**: no undefined or redefined terms against
   Baseline §12 (L-12); naming rule compliance ("compiler" vs
   "specification-document pipeline (prototype)").
5. **Record hygiene**: accepted ADRs unmodified (INV-18); supersession
   chains intact; every exception explicit, recorded, one-time (INV-20).
6. **Mirror fidelity**: workspace mirror consistent with repository;
   divergences resolved toward the repository (L-9).
7. **Findings register**: number findings (F-n continuation), each with
   violated law/invariant, severity by irreversibility (DP-21), and
   routed disposition per Baseline §8.

## Inputs

Entire repository at audit commit (recorded SHA); Accepted ADRs;
workspace registers; previous audit findings.

## Outputs

- Audit report: check matrix, findings register, unknown census,
  invariant sweep results, audit SHA.
- Issues filed for every finding requiring work.

## Constraints

- The audit observes and reports; it decides nothing (AX-3: the audit is
  a judge's input, the Maintainer is the judge).
- Audit tooling automation TODO(blocked-by: U-12); until then the audit
  is executed manually with the checklist below.

## Acceptance Criteria

- Every check has an explicit pass/fail with evidence reference.
- Zero unrouted findings.

## Completion Checklist

- [ ] Structural checks executed (DAG, governor, flows, trace closure)
- [ ] INV-1–20 sweep recorded
- [ ] Unknown census updated
- [ ] Vocabulary and record hygiene checked
- [ ] Mirror fidelity verified
- [ ] Findings register + Issues filed
- [ ] Report delivered with audit SHA
