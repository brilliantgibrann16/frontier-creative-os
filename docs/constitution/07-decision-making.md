# Article 7 — Decision Making

## Decision lifecycle

1. **Proposal** — an RFC: Draft → In Review → Accepted / Rejected / Withdrawn → Implemented.
2. **Definition** — a Specification: Draft → In Review → Ratified → Deprecated.
3. **Record** — an Architecture Decision Record: Proposed → Accepted / Rejected → Superseded.
4. **Implementation** — GitHub issues and pull requests referencing the governing artifacts.

No architectural or governance decision is binding until recorded as an ADR. An architectural or governance decision that is not recorded is treated as not made. Routine engineering decisions do not require an ADR.

## Quality gates

| Transition | Gate |
| --- | --- |
| RFC → Accepted | Reviewed under the RFC process |
| Specification → Ratified | Source RFC is Accepted; validation rules are defined |
| ADR → Accepted | Context and consequences documented; implementation referenced |
| Release | Governed by the Release Policy (Article 9) |
