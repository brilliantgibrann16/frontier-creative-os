"""Fixture tests for the architecture outline generator (P13 platform)."""

from pathlib import Path

from tools.docs.derive_architecture_outline import (
    OUTPUT_PATH,
    derive_architecture_outline,
    main,
)


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_outline_levels_indentation_and_fence_exclusion(tmp_path):
    _write(
        tmp_path,
        "docs/architecture/baseline.md",
        "# Title X\n\n## Purpose\n\ntext\n\n### Sub\n\n```\n## Fenced heading\n```\n\n## Next\n",
    )
    out = derive_architecture_outline(tmp_path)
    assert "## `docs/architecture/baseline.md` -- Title X" in out
    assert "\n- Purpose\n" in out
    assert "\n  - Sub\n" in out
    assert "\n- Next\n" in out
    assert "Fenced heading" not in out


def test_outline_sorted_by_filename(tmp_path):
    _write(tmp_path, "docs/architecture/doctrine.md", "# D\n")
    _write(tmp_path, "docs/architecture/baseline.md", "# B\n")
    out = derive_architecture_outline(tmp_path)
    assert out.index("baseline.md") < out.index("doctrine.md")


def test_outline_missing_directory(tmp_path):
    out = derive_architecture_outline(tmp_path)
    assert "- (no files found)" in out


def test_outline_file_without_sections(tmp_path):
    _write(tmp_path, "docs/architecture/README.md", "# Only Title\n\nprose\n")
    out = derive_architecture_outline(tmp_path)
    assert "- (no section headings found)" in out


def test_outline_declares_derived_and_nonauthoritative(tmp_path):
    _write(tmp_path, "docs/architecture/baseline.md", "# B\n\n## S\n")
    out = derive_architecture_outline(tmp_path)
    assert out.startswith("# Architecture Outline (derived)")
    assert "DERIVED, NON-AUTHORITATIVE" in out


def test_outline_deterministic(tmp_path):
    _write(tmp_path, "docs/architecture/baseline.md", "# B\n\n## S\n")
    assert derive_architecture_outline(tmp_path) == derive_architecture_outline(tmp_path)


def test_main_writes_output(tmp_path):
    _write(tmp_path, "docs/architecture/baseline.md", "# B\n\n## S\n")
    assert main(["derive_architecture_outline.py", str(tmp_path)]) == 0
    written = tmp_path / OUTPUT_PATH
    assert written.is_file()
    assert written.read_text(encoding="utf-8") == derive_architecture_outline(tmp_path)
