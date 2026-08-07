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
| Phase 2 — Architecture | Complete — architecture document set ratified (ADR-0002); RFC set disposed (ADR-0004) |

The controlling open decision is the language identity (D-01, RFC-0001);
all identity-dependent work is blocked until it is decided and recorded.

## Authority chain

In any normative conflict, higher documents win:

1. [`docs/constitution/`](./docs/constitution/) — Constitution v1
   (Status: Ratified, Version 1.0.0). How the project is governed.
2. [`docs/architecture/`](./docs/architecture/) — Architecture Baseline,
   Master System Blueprint, and Universal Engineering Doctrine
   (Status: Ratified — adopted by ADR-0002). How the system is structured
   and why.
3. [`docs/decisions/`](./docs/decisions/) — Architecture Decision Records
   (ADR-0001…ADR-0005). Per Article 7, no architectural or governance
   decision is binding until recorded as an ADR.

## Repository layout

- `docs/` — authoritative documents (constitution, decisions, architecture,
  RFCs, engineering prompts) plus the implementation program plans and
  conventions (`docs/program/`) and the draft engineering specification
  standard (`docs/engineering/`)
- `specs/` — implementation specification corpus (home recorded by
  ADR-0005; individual specifications bind only when ratified)
- `tools/checks/` — mechanical documentation checks (internal links,
  governance identifiers); they run as CI gates on every pull request and
  every push to `main`
- `tools/compiler/fcos/` — the Phase 0 specification-document pipeline
  (prototype). Historical context only; it is not the language compiler and
  never constrains language design.
- `tools/docs/` — documentation derivation platform for the derived
  documentation set (`docs/derived/`, which appears with its first
  committed generation; see `docs/program/DOC_DERIVATION_CONVENTIONS.md`)
- `tests/` — tests for the prototype pipeline, the mechanical checks, and
  the documentation platform
- `schemas/`, `examples/`, `assets/` — scaffolding (empty)
- `build/` — retained Phase 0 build-process artifacts (bootstrap prompt,
  execution manifest, playbook, prompt templates). Historical context
  only, zero authority; disposition is a pending Maintainer hygiene
  decision.

## Contributing

All changes go through feature branches and pull requests into a protected
`main`; direct commits to `main` are not permitted. Conventional Commits
are used throughout. Work is tracked in GitHub Issues and mirrored in the
engineering knowledge base.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the full contributor guide;
the required PR contents are encoded in the pull request template.
