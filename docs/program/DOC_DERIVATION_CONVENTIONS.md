# Documentation Derivation Conventions

- Status: Active (Wave 0, program P13 — derivation pipeline; initial
  package P13.1)
- Artifact class: program documentation (non-normative; defines mechanical
  conventions only)
- Governing artifacts: Baseline L-2 (documentation is informative, never
  definitional), Blueprint §9 (behavior claims are valid only if traceable
  to a ratified clause), PROGRAM.md P13, WORK_BREAKDOWN_STRUCTURE.md P13.1.

## 1. Source corpus (what may be derived from)

Derived documentation is generated only from the ratified corpus:

| Source | Path | Notes |
| --- | --- | --- |
| Constitution v1 | `docs/constitution/` | Ratified 1.0.0 |
| Architecture documents | `docs/architecture/` | Ratified per ADR-0002 (baseline binding; blueprint descriptive; doctrine explanatory) |
| Decision records | `docs/decisions/` (`ADR-*.md`) | Accepted ADRs |
| RFCs | `docs/rfc/` (`RFC-*.md`) | Rationale only; dispositions recorded in ADR-0004 |

`specs/` is excluded until specifications ratify (blocker B-08). Program
documents (`docs/program/`) are plans, not ratified content, and are
excluded.

## 2. Derivation rules

1. **Mechanical extraction only.** Derived documents copy verbatim
   headings, paths, and structure from source files. Derivation never
   summarizes into new claims, never interprets, and never invents.
2. **No behavior documentation.** Behavior claims require ratified
   clauses; none exist (package P13.3 is blocked by P03). Derived
   documents therefore contain no statements about FCOS behavior.
3. **Informative only (L-2).** Every derived document begins with a
   marker declaring it derived, informative, and non-authoritative. On
   any conflict the repository sources win; the fix is regeneration.
4. **Statuses are not copied.** Per-file RFC status lines are historical;
   dispositions live in ADR-0004 and `docs/rfc/README.md`. Copying
   per-file status lines into derived output would create a second,
   potentially conflicting statement.
5. **Determinism.** Given the same tree, the pipeline produces
   byte-identical output (sorted traversal, fixed template).

## 3. Pipeline

The derivation platform lives under `tools/docs/` (standard library
only) and writes to `docs/derived/`. `tools/docs/README.md` documents
the platform; `tools/docs/corpus.py` holds the shared mechanical
helpers.

| Tool | Output |
| --- | --- |
| `tools/docs/derive_corpus_index.py` | `docs/derived/CORPUS_INDEX.md` |
| `tools/docs/derive_navigation.py` | `docs/derived/NAVIGATION.md` |
| `tools/docs/derive_id_crossref.py` | `docs/derived/ID_CROSSREF.md` |
| `tools/docs/derive_document_graph.py` | `docs/derived/DOCUMENT_GRAPH.md` |
| `tools/docs/derive_architecture_outline.py` | `docs/derived/ARCHITECTURE_OUTLINE.md` |
| `tools/docs/derive_repository_inventory.py` | `docs/derived/REPOSITORY_INVENTORY.md` |

- Build everything, from the repository root:

```
python tools/docs/build_docs.py
```

- Verify committed derived output matches regeneration:

```
python tools/docs/build_docs.py --check
```

- Content extraction stays within the §1 source corpus. Two path-only
  surfaces copy no document content: the repository inventory records
  file paths across the tracked tree, and the navigation document links
  to human-maintained entry-point indexes by path only.
- Location note: the documentation area is `docs/derived/` and the
  derivation tooling lives under `tools/docs/`. This is an
  implementation-plan note (PROGRAM.md P13, repository areas), not a
  governance change.

## 4. Staleness

Regenerate after every merge that touches the source corpus. A stale
derived document is corrected by regeneration, never by hand-editing
(P13 rollback strategy). Generated output is committed through the
normal PR path and carries no authority of its own.

## 5. Gates

Fixture tests for the pipeline live in `tests/` and run in the CI test
job (see `docs/program/TESTING_CONVENTIONS.md`). Derived output under
`docs/` is scanned by the link and identifier checks like any other
documentation. A freshness test compares committed derived output with
regeneration (`python tools/docs/build_docs.py --check`); it activates
once `docs/derived/` exists (first generation) and is skipped before
that.
