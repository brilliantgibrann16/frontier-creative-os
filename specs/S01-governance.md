# S1 — Governance Subsystem Specification

**Status:** In Review · **Subsystem:** S1 (Blueprint §2) · **Date:** 2026-08-02

## Scope

The operational decision-making machinery: how proposals become binding
decisions, how decisions are recorded, amended, and superseded, and the
gates every change traverses. Excludes: the content of any decision
(owned by the deciding artifact) and workspace mirroring (S3).

## Responsibilities

- Maintain the decision path: Issue → RFC → review → ADR → (specification
  work where applicable).
- Record every binding decision as an ADR (INV-8); no decision binds
  otherwise (L-8).
- Operate the amendment processes of rank-1/rank-2 artifacts by their own
  rules (Constitution amendment; Baseline §13).
- Administer recorded one-time exceptions (INV-20).
- Forbidden (Blueprint §3/§4): deciding language meaning (A3 belongs to
  S4); delegating policy to CI (L-10, INV-10).

## Interfaces

- **Repository interface** (sole write path): feature branches, PRs into
  protected `main`, review approval. Direct-to-main only by explicit
  recorded Maintainer exception (trust boundary, Blueprint §9).
- **Decision surfaces:** `docs/decisions/` (ADRs), `docs/rfc/` (RFCs),
  GitHub Issues (work/intent), PR review threads (review record).

## Data model

- **ADR document:** number (immutable, unique), title, status
  (Proposed | Accepted | Rejected | Superseded), date, context, decision,
  consequences, supersession pointer (optional).
- **RFC document:** number, title, status (Draft | In Review | Accepted |
  Rejected | Withdrawn | Implemented), resolves-reference (unknown or
  decision ID), body per RFC index conventions.
- **Exception record:** an ADR or ADR-referenced entry naming the
  violated rule, the scope, and the one-time nature (INV-20).

## API contracts

Not applicable — S1 exposes document and review contracts, not
programmatic APIs. The document contracts above are the binding surface.

## State machines

- **RFC:** Draft → In Review → (Accepted | Rejected | Withdrawn);
  Accepted → Implemented. No other transitions. Accepted/Rejected are
  terminal except Implemented.
- **ADR:** Proposed → (Accepted | Rejected); Accepted → Superseded (by a
  new ADR only — never edited, INV-18).
- **Exception:** Requested → Recorded → Closed (single use; reuse is a
  new exception).

## Sequence flows

1. **Decision flow:** Issue filed → RFC drafted on branch → PR opened →
   review (cooling rule per RFC-0010, TODO(blocked-by: acceptance ADR for
   RFC-0010)) → Maintainer decision → ADR recorded → downstream artifact
   work authorized.
2. **Supersession flow:** new ADR cites superseded ADR → old ADR status
   updated to Superseded with pointer → history preserved.

## Error model

| Failure | Detection | Resolution |
| --- | --- | --- |
| Unrecorded decision acted upon | audit: artifact cites no ADR | halt work; record ADR or revert |
| ADR edited after acceptance | history diff | revert; supersede instead (INV-18) |
| Gate bypass | protected-branch audit | recorded one-time exception or revert (INV-20) |
| Self-approval by author | review metadata | re-review; cooling rule (RFC-0010) |

## Security requirements

Branch protection on `main`; attributable commits; AI contributions
traverse identical gates with no self-approval (L-5, INV-19); no
unrecorded overrides (Blueprint §9 Testing↔Release boundary applies to
all gates).

## Performance budgets

No ratified quantitative requirements exist for decision latency.
**BLOCKED** — missing: any ratified latency/throughput requirement;
blocked by: Maintainer decision (none pending); unblock: future
governance RFC if ever needed. (Inventing a budget here would fabricate
policy.)

## Observability requirements

Every decision discoverable from `docs/decisions/` alone; Operations Log
(S3) mirrors governance events; PR history is the review audit trail.
Mechanical audit: every Accepted RFC has exactly one recording ADR.

## Testing requirements

Mechanical checks (CI, per RFC-0011 E-A once accepted): ADR/RFC ID
uniqueness; status-value validity; supersession pointers resolve;
Accepted-RFC→ADR closure. TODO(blocked-by: acceptance ADR for RFC-0011).

## Acceptance criteria

- Every binding decision in the repository traces to an Accepted ADR.
- No ADR has ever been edited post-acceptance (history check).
- All state-machine transitions observed in history are legal ones.
- Exception records exist for every recorded gate deviation.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Decision path, Maintainer authority | Constitution Art. 6, 7 |
| ADR-only bindingness | Baseline L-8; INV-8 |
| Immutability/supersession | INV-18; Blueprint §7 |
| Review procedure, cooling rule | RFC-0010 (acceptance pending) |
| Gate mechanics | RFC-0011; Constitution Art. 9 |
| Recorded exceptions | INV-20; ADR-0001 precedent |
