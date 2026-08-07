# Contributing to Frontier Creative OS

This guide is a convenience entry point for contributors. It carries **no
decision authority**: it restates ratified project law for day-to-day use
and creates no policy. If anything here conflicts with the
[Constitution](./docs/constitution/), a recorded decision in
[`docs/decisions/`](./docs/decisions/), or the ratified
[architecture set](./docs/architecture/), the ratified artifact wins.

## Before you start

- **The language is not designed yet.** Its identity and scope are an open
  decision (D-01, RFC-0001); all identity-dependent work is blocked until
  that decision is recorded as an ADR. Do not propose syntax, grammar, or
  semantics in issues or pull requests.
- The work plan lives in [`docs/program/`](./docs/program/). The unit of
  assignment is the work package defined in
  [`WORK_BREAKDOWN_STRUCTURE.md`](./docs/program/WORK_BREAKDOWN_STRUCTURE.md);
  gated packages must not be started.
- AI agents are first-class contributors and use exactly the same path as
  humans — no special interface exists. See
  [`AGENT_CONTRIBUTION_CONVENTIONS.md`](./docs/program/AGENT_CONTRIBUTION_CONVENTIONS.md).

## The one contribution path

feature branch → pull request → independent review → mechanical gates
(CI) → Maintainer merge.

1. **Branch** from `main`. Direct commits to `main` are prohibited.
   Branch names follow
   [`DELIVERY_STRATEGY.md`](./docs/program/DELIVERY_STRATEGY.md):
   `docs/*`, `specs/*`, `ci/*`, `impl/<subsystem>/*`, and `governance/*`
   (reserved for Maintainer-directed governance work only). One work
   package → one branch → one PR; disclose any bundling deviation in the
   PR body.
2. **Commit** incrementally. Conventional Commits are used throughout.
3. **Open a pull request** into `main`. Squash-merge is the established
   convention. The required PR body contents are encoded in the pull
   request template.
4. **Review.** No self-approval and no self-merge. Merge authority rests
   with the Maintainer (Constitution, Article 6).

## Mechanical gates

Every PR runs the CI defined in `.github/workflows/ci.yml`; there is no
merge on red. The same gates run locally:

- Prototype and tooling tests: `python -m pytest tests/ -v`
- Documentation gates: `python tools/checks/check_links.py` and
  `python tools/checks/check_ids.py`

Test conventions (Python 3.11, pytest as the sole dependency, flat
`tests/` layout, `tmp_path` fixtures) are defined in
[`TESTING_CONVENTIONS.md`](./docs/program/TESTING_CONVENTIONS.md).
Tests are evidence, never definition: a test contradicting a ratified
specification is the defect.

## Hard rules

- Never commit DRAFT documents; work enters review as In Review.
- Never merge without a pull request.
- Never fabricate content. Missing information is recorded as a blocker
  (`Blocked-by:` plus the governing artifact) — blockers are disposed
  only by ADRs (Constitution, Article 7), never by PR descriptions or
  code comments. Continue with unblocked work in the meantime.
- Ratified and accepted artifacts are never edited in place; corrections
  travel by supersession.
- No bulk rewrites: changes are minimal and targeted, and unrelated
  content is left byte-identical.
- Prototype quarantine: `tools/compiler/fcos/` is historical context
  only — never a starting point, precedent, or semantic authority.
- Governance is never resolved through code or documentation; decisions
  travel the RFC → ADR path.

## Releases and versioning

There is deliberately **no release, changelog, or semantic-versioning
workflow** in this repository yet. No language versions exist pre-1.0
(RFC-0009 as disposed by ADR-0004), and Article 9 forbids any release
before CI gates are live and green. Do not add release automation; the
underlying policies must first be decided after D-01 and recorded as
ADRs (see `docs/program/DELIVERY_STRATEGY.md`, Release strategy).

## Where things live

| What | Where |
| --- | --- |
| Governance — how the project is run | [`docs/constitution/`](./docs/constitution/) |
| Binding decisions (ADRs) | [`docs/decisions/`](./docs/decisions/) |
| Ratified architecture | [`docs/architecture/`](./docs/architecture/) |
| Proposals and their dispositions | [`docs/rfc/`](./docs/rfc/) (dispositions recorded in ADR-0004) |
| Specification corpus (binds only when ratified) | [`specs/`](./specs/) |
| Program, plans, and conventions | [`docs/program/`](./docs/program/) |
| Mechanical checks | [`tools/checks/`](./tools/checks/) |
| Documentation derivation platform (regenerates `docs/derived/`) | [`tools/docs/`](./tools/docs/) |
| Engineering prompt library | [`docs/prompts/`](./docs/prompts/) |
