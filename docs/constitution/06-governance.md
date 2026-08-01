# Article 6 — Governance

## Roles

| Role | Responsibilities |
| --- | --- |
| Maintainer | Final approval of RFCs, specifications, ADRs, and releases; repository administration |
| Reviewer | Reviews RFCs, specifications, and pull requests before acceptance |
| Contributor | Proposes changes through issues, RFCs, and pull requests |

The Maintainer role is held by the repository owner.

## Single-maintainer provision

While the project has a single engineer, the Maintainer may self-approve changes. Every non-trivial decision must nonetheless be recorded as an ADR so that rationale survives the growth of the organization.

## Repository governance

1. Direct commits to `main` are prohibited; all changes merge through reviewed pull requests.
2. Every pull request references the issue or artifact that motivates it.
3. Work is tracked in GitHub Issues; implementation history lives in pull requests.
