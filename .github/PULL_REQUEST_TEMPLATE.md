## Summary

<!-- What does this PR deliver? One work package per PR. -->

- **WBS package ID(s):** <!-- from docs/program/WORK_BREAKDOWN_STRUCTURE.md; disclose any bundling deviation for Maintainer judgment -->
- **Governing artifacts cited:** <!-- the ratified/accepted sources this work derives from -->
- **Blockers touched:** <!-- Blocked-by IDs, or "none" — no blocker may be silently disposed; blockers are disposed only by ADRs -->
- **Cross-PR ordering dependencies:** <!-- e.g. "merge after #NN", or "none" -->

## Merge preconditions (docs/program/DELIVERY_STRATEGY.md, Merge strategy)

- [ ] Feature branch named per `docs/program/DELIVERY_STRATEGY.md`; no direct commits to `main`
- [ ] Mechanical gates green: `python -m pytest tests/ -v`, `python tools/checks/check_links.py`, `python tools/checks/check_ids.py`
- [ ] No DRAFT documents committed; work enters review as In Review
- [ ] Minimal targeted diff; no bulk rewrites; unrelated content byte-identical
- [ ] No in-place edits to ratified or accepted artifacts (corrections travel by supersession)

## Disclosures (required for agent-authored PRs — docs/program/AGENT_CONTRIBUTION_CONVENTIONS.md)

- **AI involvement:** <!-- disclose authorship/involvement -->
- **Self-review disclosure:** <!-- known limitations, verifications not executed, deviations from plan or convention -->
- **Zero-invention statement:** <!-- required when the PR touches planning, governance-adjacent, or specification-adjacent artifacts -->
