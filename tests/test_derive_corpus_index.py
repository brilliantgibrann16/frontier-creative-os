"""Fixture tests for tools/docs/derive_corpus_index.py (P13.1 derivation pipeline)."""

from pathlib import Path

from tools.docs.derive_corpus_index import derive_index, first_heading, main


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _corpus(tmp_path: Path) -> Path:
    _write(tmp_path / "docs" / "constitution" / "01-mission.md", "# Mission\n\nBody.\n")
    _write(tmp_path / "docs" / "architecture" / "baseline.md", "# Sample Baseline\n")
    _write(
        tmp_path / "docs" / "decisions" / "ADR-0001.md",
        "# ADR-0001 \u2014 Sample record\n\n**Status:** Accepted\n",
    )
    _write(
        tmp_path / "docs" / "rfc" / "RFC-0001.md",
        "# RFC-0001 \u2014 Sample proposal\n\n**Status:** In Review\n",
    )
    return tmp_path


def test_titles_are_extracted_verbatim(tmp_path: Path) -> None:
    text = derive_index(_corpus(tmp_path))
    assert "- `docs/constitution/01-mission.md` -- Mission" in text
    assert "- `docs/architecture/baseline.md` -- Sample Baseline" in text
    assert "- `docs/decisions/ADR-0001.md` -- ADR-0001 \u2014 Sample record" in text
    assert "- `docs/rfc/RFC-0001.md` -- RFC-0001 \u2014 Sample proposal" in text


def test_per_file_status_lines_are_not_copied(tmp_path: Path) -> None:
    text = derive_index(_corpus(tmp_path))
    assert "Accepted" not in text
    assert "In Review" not in text


def test_output_is_deterministic_and_sorted(tmp_path: Path) -> None:
    root = _corpus(tmp_path)
    _write(root / "docs" / "decisions" / "ADR-0002.md", "# ADR-0002 \u2014 Later record\n")
    first = derive_index(root)
    second = derive_index(root)
    assert first == second
    assert first.index("ADR-0001.md") < first.index("ADR-0002.md")


def test_unratified_sources_are_excluded(tmp_path: Path) -> None:
    root = _corpus(tmp_path)
    _write(root / "specs" / "S01-governance.md", "# Sample spec\n")
    _write(root / "docs" / "program" / "PROGRAM.md", "# Sample program plan\n")
    text = derive_index(root)
    assert "S01-governance.md" not in text
    assert "PROGRAM.md" not in text


def test_non_matching_decision_documents_are_ignored(tmp_path: Path) -> None:
    root = _corpus(tmp_path)
    _write(root / "docs" / "decisions" / "D01_DECISION_BRIEF.md", "# Sample brief\n")
    text = derive_index(root)
    assert "D01_DECISION_BRIEF.md" not in text


def test_missing_heading_falls_back_to_filename(tmp_path: Path) -> None:
    root = _corpus(tmp_path)
    _write(root / "docs" / "rfc" / "RFC-0002.md", "no heading here\n")
    text = derive_index(root)
    assert "- `docs/rfc/RFC-0002.md` -- RFC-0002.md" in text
    assert first_heading(root / "docs" / "rfc" / "RFC-0002.md") == "RFC-0002.md"


def test_derived_marker_is_present(tmp_path: Path) -> None:
    text = derive_index(_corpus(tmp_path))
    assert text.startswith("# Ratified Corpus Index (derived)")
    assert "informative only" in text


def test_main_writes_output_file(tmp_path: Path) -> None:
    root = _corpus(tmp_path)
    assert main(["derive_corpus_index.py", str(root)]) == 0
    out = root / "docs" / "derived" / "CORPUS_INDEX.md"
    assert out.is_file()
    assert out.read_text(encoding="utf-8") == derive_index(root)


def test_empty_source_directory_is_reported_not_invented(tmp_path: Path) -> None:
    root = tmp_path
    _write(root / "docs" / "constitution" / "01-mission.md", "# Mission\n")
    text = derive_index(root)
    assert "- (no files found)" in text
