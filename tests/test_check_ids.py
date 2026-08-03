"""Fixture tests for tools/checks/check_ids.py (mechanical ID reference checker)."""

from pathlib import Path

from tools.checks.check_ids import collect_errors


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_known_identifiers_resolve(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "decisions" / "ADR-0001.md", "# ADR-0001")
    _write(tmp_path / "docs" / "rfc" / "RFC-0001.md", "# RFC-0001")
    _write(
        tmp_path / "docs" / "note.md",
        "Derived from ADR-0001 and RFC-0001.",
    )
    assert collect_errors(tmp_path) == []


def test_unknown_adr_is_reported(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "note.md", "Cites ADR-0099.")
    errors = collect_errors(tmp_path)
    assert len(errors) == 1
    assert "ADR-0099" in errors[0]
    assert "docs/decisions/ADR-0099.md" in errors[0]


def test_unknown_rfc_is_reported(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "note.md", "Cites RFC-0042.")
    errors = collect_errors(tmp_path)
    assert len(errors) == 1
    assert "RFC-0042" in errors[0]


def test_duplicate_mentions_are_reported_once(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs" / "note.md",
        "ADR-0099 is cited twice: ADR-0099.",
    )
    assert len(collect_errors(tmp_path)) == 1


def test_partial_tokens_do_not_match(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs" / "note.md",
        "Tokens like ADR-1, RFC-12345x, and XADR-0001 are not identifiers.",
    )
    assert collect_errors(tmp_path) == []


def test_excluded_tree_is_skipped(tmp_path: Path) -> None:
    _write(tmp_path / "specs" / "fcos" / "old.md", "Cites ADR-0099 and RFC-0042.")
    assert collect_errors(tmp_path) == []
