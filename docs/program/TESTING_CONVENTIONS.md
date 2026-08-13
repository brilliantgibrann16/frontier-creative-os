# Testing Conventions

- Status: Active (Wave 0, program P11)
- Artifact class: program documentation (non-normative; restates ratified sources and defines mechanical conventions only)
- Governing artifacts: Blueprint INV-4 (tests are evidence, not definition), Baseline L-5 / Blueprint INV-19 (identical gates for human and AI contributions), Baseline L-7 (prototype quarantine), RFC-0002 dispositions N-B/N-C per ADR-0004 (clause identifier scheme).

## 1. Toolchain

- Python **3.11** — the version the existing suite was authored against (verified from repository evidence).
- **pytest** — the sole third-party dependency; everything under test is standard-library only.
- Invocation from the repository root:

```
python -m pytest tests/ -v
```

## 2. Layout and naming

- All tests live flat in `tests/`, named `test_<unit>.py`; test functions are named `test_<behavior>`.
- Use pytest `tmp_path` fixtures for filesystem interaction. Tests must not write outside the fixture directory, must not require network access, and must not depend on execution order.
- Imports address production code by full path from the repository root, e.g. `from tools.compiler.fcos.parser import Parser` or `from tools.checks.check_links import collect_errors`.

## 3. Meaning of tests (INV-4)

Tests are **evidence, not definition**. A passing suite demonstrates that code behaves as its tests describe; it does not define FCOS behavior. The prototype under `tools/compiler/` is quarantined (L-7): its tests protect a tool, and nothing about the FCOS language, runtime, or model may be inferred from them.

## 4. Traceability convention (recorded now; consumable after ratification)

When specification-derived implementation begins, every test that exercises a normative requirement must name the governing clause identifier (scheme per RFC-0002 dispositions N-B/N-C) in its test name or docstring, so conformance evidence is mechanically traceable. Ratified clauses now exist: the S04 Stage 0 minimal contract clause set (S04#1.1–S04#4.2, ADR-0011). A test may name one of those clause identifiers as spec-derived evidence for the obligation it exercises. For every other specification (unratified; G-SPEC, blocker B-08), **no test may claim to verify a specification clause**, and conformance judgments remain prohibited regardless (section 5).

## 5. Prohibited test classes (current state)

- **Performance/benchmark tests** — prohibited while no ratified performance requirement exists (B-10). A benchmark without a governing requirement would resolve governance through code.
- **Conformance judgments** — see `docs/program/CONFORMANCE_FRAME.md`; blocked by G-SPEC(S13) / B-08.

## 6. Gates

The CI workflow (`.github/workflows/ci.yml`) runs the full test suite plus the mechanical documentation checks on every push to `main` and every pull request. Gates apply identically to human and AI contributions (L-5 / INV-19).
