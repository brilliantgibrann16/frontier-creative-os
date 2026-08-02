# Frontier Creative OS

Frontier Creative OS (FCOS) is a long-term engineering project building the
Frontier Specification Language and its surrounding ecosystem: governance,
architecture, specifications, implementations, tooling, and conformance.

The language itself is not yet designed. Its identity and scope are an open
decision (D-01); no syntax, grammar, or semantics exist yet, by design.

## Project status

| Phase | State |
| --- | --- |
| Phase 0 — Foundation | Complete |
| Phase 1 — Governance | Complete — Constitution v1 ratified (1.0.0) |
| Phase 2 — Architecture | In progress |

## Authority chain

In any normative conflict, higher documents win:

1. [`docs/constitution/`](./docs/constitution/) — Constitution v1
   (Status: Ratified, Version 1.0.0). How the project is governed.
2. [`docs/architecture/`](./docs/architecture/) — Architecture Baseline,
   Master System Blueprint, and Universal Engineering Doctrine
   (Status: Proposed pending adoption ADR). How the system is structured
   and why.
3. [`docs/decisions/`](./docs/decisions/) — Architecture Decision Records.
   Per Article 7, no architectural or governance decision is binding until
   recorded as an ADR.

## Repository layout

- `docs/` — authoritative documents (constitution, decisions, architecture)
- `specs/` — specification scaffold (taxonomy unratified; carries no
  decision authority)
- `tools/compiler/fcos/` — the Phase 0 specification-document pipeline
  (prototype). Historical context only; it is not the language compiler and
  never constrains language design.
- `tests/` — tests for the prototype pipeline
- `schemas/`, `examples/`, `build/`, `assets/` — scaffolding (empty)

## Contributing

All changes go through feature branches and pull requests into a protected
`main`; direct commits to `main` are not permitted. Conventional Commits
are used throughout. Work is tracked in GitHub Issues and mirrored in the
engineering knowledge base.
