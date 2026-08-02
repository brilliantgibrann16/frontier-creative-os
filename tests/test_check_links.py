"""Fixture tests for tools/checks/check_links.py (mechanical link checker)."""

from pathlib import Path

from tools.checks.check_links import collect_errors


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_resolving_links_pass(tmp_path: Path) -> None:
    _write(tmp_path / "README.md", "Root readme.")
    _write(
        tmp_path / "docs" / "a.md",
        "See [b](b.md) and [root](../README.md) and [dir](sub).",
    )
    _write(tmp_path / "docs" / "b.md", "Back to [a](a.md).")
    _write(tmp_path / "docs" / "sub" / "c.md", "Leaf.")
    assert collect_errors(tmp_path) == []


def test_external_anchor_and_placeholder_links_are_skipped(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs" / "a.md",
        "[x](https://example.com) [y](http://example.com) "
        "[m](mailto:a@b.c) [anchor](#section) [tpl]({{placeholder}})",
    )
    assert collect_errors(tmp_path) == []


def test_broken_link_is_reported(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "a.md", "See [missing](missing.md).")
    errors = collect_errors(tmp_path)
    assert len(errors) == 1
    assert "docs/a.md" in errors[0]
    assert "missing.md" in errors[0]


def test_anchor_suffix_is_stripped_before_resolution(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "a.md", "See [b](b.md#section).")
    _write(tmp_path / "docs" / "b.md", "Target.")
    assert collect_errors(tmp_path) == []


def test_fenced_and_inline_code_are_ignored(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs" / "a.md",
        "```\n[not a link](nowhere.md)\n```\n\nAnd `[also not](gone.md)` inline.\n",
    )
    assert collect_errors(tmp_path) == []


def test_excluded_tree_is_skipped(tmp_path: Path) -> None:
    _write(tmp_path / "specs" / "fcos" / "old.md", "[gone](gone.md)")
    _write(tmp_path / "specs" / "S01.md", "No links here.")
    assert collect_errors(tmp_path) == []


def test_root_relative_links_resolve_from_repo_root(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "deep" / "a.md", "See [readme](/README.md).")
    _write(tmp_path / "README.md", "Root readme.")
    assert collect_errors(tmp_path) == []
