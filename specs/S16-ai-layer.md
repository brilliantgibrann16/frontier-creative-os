# S16 — AI Layer Subsystem Specification

**Status:** In Review · **Subsystem:** S16 (Blueprint §2, "Active as contributor") · **Date:** 2026-08-02

## Scope

AI participation in FCOS engineering: the rules under which AI actors
contribute. S16 is unusual — it is *already operating* (this corpus is
AI-authored under these rules). Excludes: any AI-facing product features
(rejected — RFC-0013 planner P-A, RFC-0016 agent framework A-A;
TODO(blocked-by: acceptance ADRs) for the rejections’ recording).

## Responsibilities

- Contribute through the identical gates as human contributors: same
  branches, PRs, reviews (P-4; INV-19; Constitution Art. 2 first-class
  participants — first-class means same rules, not fewer).
- Never self-approve; never hold defining authority (INV-5: no
  AI-authored content becomes binding without the human decision path).
- Respect the write-path prohibition: no direct writes into S1
  (governance), S2 (architecture), or S4 (language definition) content
  outside the proposal path (Blueprint §3, L-5).
- Never fabricate: missing information is recorded as a blocked item
  referencing the blocking decision, never invented (the standing
  no-fabrication rule; CN-14 operationally).

## Interfaces

- **AI interface = absence of a special interface** (Blueprint §8, P-4):
  AI consumes the repository interface and, when it exists, the same SDK
  surface as humans (S8). No AI-privileged endpoint may ever exist.
- AI-artifact classes (memory, context, prompts beyond the ratified
  Engineering Prompt class): **BLOCKED** — missing: artifact-class
  definitions (U-13/D-14); blocked by: RFC-0014 (memory routing M-A/B/C
  undecided) and RFC-0015 (context engine blocked on L-12 definition);
  unblock: their acceptance ADRs.

## Data model

- **Engineering Prompt** (the one ratified AI artifact class, ADR-0003):
  versioned document in `docs/prompts/`, zero decision authority,
  RFC-preparation/operational character.
- Memory/context models: **BLOCKED** as above (RFC-0014/0015).

## API contracts

None — by design (P-4). Any future AI-relevant contract is an S8
contract available to all consumers.

## State machines

**AI contribution:** Drafted → Proposed (PR) → human-reviewed →
(Merged | Rejected). No transition bypasses human review; there is no
auto-merge state.

## Sequence flows

1. **Contribution cycle:** mission received → governed-corpus reading →
   branch → incremental commits → PR with caveats/flags → human decision.
   (This PR instantiates the flow.)
2. **Blocked-information flow:** missing requirement → exact-gap
   identification → blocking-decision citation → explicit marker →
   continue remaining work — never silent invention.
3. **Directive-conflict flow:** instruction conflicts with recorded
   rules → comply where the Maintainer has authority → flag the conflict
   for recording — never silently execute or silently refuse.

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Fabricated fact/behavior | review; source audit | revert; recorded as defect class of highest severity |
| Gate bypass by AI | audit | revert + recorded incident (INV-20 machinery) |
| AI-authored content treated as binding without ADR | citation audit | invalidate; route through decision path (INV-5) |
| Bulk destructive edit | review; history | prohibited by standing rule; restore from history |

## Security requirements

AI actors hold no credentials beyond ordinary-contributor scope; no
access to publishing/approval credentials; all AI actions attributable
in history (CN-23 bounds; INV-19).

## Performance budgets

Not applicable — no ratified document defines AI throughput requirements,
and contribution speed is explicitly subordinate to gate compliance
(Doctrine: correctness of process over velocity).

## Observability requirements

Every AI contribution identifiable and auditable from repository history
alone; session/ops records mirrored to S3 (Ops Log); flags and caveats
surfaced in PR bodies, not buried.

## Testing requirements

Audit-style: sample merged AI contributions for gate compliance and
citation integrity; verify zero self-approvals in review metadata;
verify no AI-privileged surfaces exist. Encoding: TODO(blocked-by:
acceptance ADR for RFC-0011).

## Acceptance criteria

- 100% of AI contributions in history traversed the full gate path (the
  ADR-0001 direct-to-main event stands as a recorded exception, not a
  precedent).
- Zero binding artifacts authored by AI without a recording ADR.
- Rejected capabilities (planner, agent framework) remain absent until
  the rejections are revisited via RFC.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| First-class, same rules | Constitution Art. 2; Baseline P-4 |
| No defining authority | INV-5; L-5 |
| Uniform interface | Blueprint §8 (AI interface); INV-19 |
| Prompt class | ADR-0003 |
| Rejections | RFC-0013, RFC-0016 (acceptance pending) |
| Artifact-class unknowns | RFC-0014, RFC-0015; Blueprint §14 (D-14/U-13) |
| Bounds | Doctrine CN-23 |
