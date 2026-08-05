# Documentation Derivation Conventions

- Status: Active (Wave 0, program P13 — package P13.1)
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

- Tool: `tools/docs/derive_corpus_index.py` (standard library only).
- Output: `docs/derived/CORPUS_INDEX.md` — the derived index of the
  ratified corpus.
- Invocation, from the repository root:

```
python tools/docs/derive_corpus_index.py
```

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
documentation.
