"""Fixture tests for the documentation build orchestrator (P13 platform)."""

from pathlib import Path

import pytest

from tools.docs.build_docs import GENERATORS, build, check, main


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _corpus(root: Path) -> None:
    _write(root, "docs/constitution/README.md", "# The Constitution\n")
    _write(root, "docs/architecture/baseline.md", "# Baseline\n\n## Purpose\n")
    _write(root, "docs/decisions/ADR-0001.md", "# ADR-0001 - First\n")
    _write(root, "docs/rfc/RFC-0001.md", "# RFC-0001 - First\n\nSee ADR-0001.\n")


def test_build_writes_every_registered_output(tmp_path):
    _corpus(tmp_path)
    written = build(tmp_path)
    assert len(written) == len(GENERATORS)
    for output_path, _derive in GENERATORS:
        assert (tmp_path / output_path).is_file()


def test_build_is_idempotent_byte_for_byte(tmp_path):
    _corpus(tmp_path)
    build(tmp_path)
    first = {
        output_path: (tmp_path / output_path).read_text(encoding="utf-8")
        for output_path, _derive in GENERATORS
    }
    build(tmp_path)
    second = {
        output_path: (tmp_path / output_path).read_text(encoding="utf-8")
        for output_path, _derive in GENERATORS
    }
    assert first == second


def test_check_passes_after_build(tmp_path):
    _corpus(tmp_path)
    build(tmp_path)
    assert check(tmp_path) == []


def test_check_reports_stale_output(tmp_path):
    _corpus(tmp_path)
    build(tmp_path)
    target = tmp_path / GENERATORS[0][0]
    target.write_text(
        target.read_text(encoding="utf-8") + "tampered\n", encoding="utf-8"
    )
    problems = check(tmp_path)
    assert any(problem.startswith("STALE: ") for problem in problems)


def test_check_reports_missing_output(tmp_path):
    _corpus(tmp_path)
    build(tmp_path)
    (tmp_path / GENERATORS[1][0]).unlink()
    problems = check(tmp_path)
    assert any(problem.startswith("MISSING: ") for problem in problems)


def test_check_empty_corpus_still_deterministic(tmp_path):
    build(tmp_path)
    assert check(tmp_path) == []


def test_main_build_and_check_exit_codes(tmp_path):
    _corpus(tmp_path)
    assert main([str(tmp_path)]) == 0
    assert main([str(tmp_path), "--check"]) == 0
    (tmp_path / GENERATORS[0][0]).unlink()
    assert main([str(tmp_path), "--check"]) == 1


def test_committed_derived_output_is_fresh_when_present():
    repo_root = Path(__file__).resolve().parents[1]
    if not (repo_root / "docs" / "derived").is_dir():
        pytest.skip(
            "docs/derived/ does not exist yet; first generation is a "
            "Maintainer-run `python tools/docs/build_docs.py` "
            "(DOC_DERIVATION_CONVENTIONS.md section 4)"
        )
    assert check(repo_root) == []
