# Documentation platform (`tools/docs/`)

Mechanical derivation pipeline for `docs/derived/` (program lane P13,
Documentation System / S14). Governing conventions:
`docs/program/DOC_DERIVATION_CONVENTIONS.md`.

## What this is

- Generators that derive navigation, indexes, cross-references, document
  graphs, outlines, and inventories from the ratified source corpus.
- Everything is mechanical: verbatim headings, repository paths, lexical
  identifier tokens, and Markdown link targets. No summaries, no
  interpretation, no status synthesis, no behavior claims.
- Every output begins with a standard banner declaring it DERIVED and
  NON-AUTHORITATIVE and stating ownership, generation path, regeneration
  instructions, sources, and limitations.

## Components

| Tool | Output |
| --- | --- |
| `derive_corpus_index.py` | `docs/derived/CORPUS_INDEX.md` -- index of the ratified corpus |
| `derive_navigation.py` | `docs/derived/NAVIGATION.md` -- corpus navigation plus entry points (path links only) |
| `derive_id_crossref.py` | `docs/derived/ID_CROSSREF.md` -- identifier occurrence tables plus unresolved ADR/RFC reference report |
| `derive_document_graph.py` | `docs/derived/DOCUMENT_GRAPH.md` -- link/reference edges plus Mermaid ADR/RFC graph |
| `derive_architecture_outline.py` | `docs/derived/ARCHITECTURE_OUTLINE.md` -- verbatim heading outlines of `docs/architecture/` |
| `derive_repository_inventory.py` | `docs/derived/REPOSITORY_INVENTORY.md` -- paths-only file inventory |

Shared mechanical helpers live in `corpus.py` (source sets, banner,
heading/identifier/link extraction, natural token ordering). The
orchestrator is `build_docs.py`.

## Usage

From the repository root:

```
python tools/docs/build_docs.py            # regenerate all derived docs
python tools/docs/build_docs.py --check    # fail if committed output is stale
python tools/docs/derive_navigation.py     # regenerate one document
```

Every generator also accepts an explicit root argument, for example
`python tools/docs/build_docs.py /path/to/checkout`.

## Design rules

- Standard-library Python only (Python 3.11 in CI).
- Deterministic: byte-identical output for the same tree; stable sorted
  ordering; no timestamps.
- Idempotent: rebuilding over an existing `docs/derived/` produces the
  same bytes. The repository inventory excludes `docs/derived/` for
  exactly this reason.
- Content sources are only the ratified corpus sets declared in
  `corpus.py` (`docs/constitution/*.md`, `docs/architecture/*.md`,
  `docs/decisions/ADR-*.md`, `docs/rfc/RFC-*.md`). `specs/` and
  `docs/program/` are never content sources. Two path-only surfaces copy
  no document content: navigation entry-point links and the repository
  inventory.
- Writes go only to `docs/derived/`. Nothing here writes to
  `docs/constitution/`, `docs/architecture/`, `docs/decisions/`,
  `docs/rfc/`, or `specs/`.

## Tests

Fixture tests live in `tests/` (`test_docs_corpus.py`,
`test_derive_navigation.py`, `test_derive_id_crossref.py`,
`test_derive_document_graph.py`, `test_derive_architecture_outline.py`,
`test_derive_repository_inventory.py`, `test_build_docs.py`) and run in
the CI `tests` job. They cover determinism, sorting, empty and partial
corpora, missing directories, unresolved references, duplicate tokens,
failure paths, and byte-level idempotence. A freshness test asserts the
committed `docs/derived/` matches regeneration; it is skipped until the
first generation exists.

## First generation and staleness

`docs/derived/` does not exist until the first
`python tools/docs/build_docs.py` run is committed (a Maintainer tool
execution per the derivation conventions). Derived output is committed
through the normal PR path and carries no authority of its own
(Baseline L-2). Fix staleness by regenerating -- never by hand-editing.

## Extending the platform

- New identifier family: add one `(label, recorded-in, pattern)` tuple
  to `ID_FAMILIES` in `corpus.py`, plus tests.
- New generator: follow the existing module shape (`OUTPUT_PATH`
  constant, `derive_*(root) -> str`, `main(argv)`), reuse `banner(...)`,
  register the module in `build_docs.GENERATORS`, and add fixture tests.
