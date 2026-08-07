"""Fixture tests for the corpus navigation generator (P13 platform)."""

from pathlib import Path

from tools.docs.derive_navigation import OUTPUT_PATH, derive_navigation, main


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _corpus(root: Path) -> None:
    _write(root, "docs/constitution/01-mission.md", "# Article 1 - Mission\n\nBody.\n")
    _write(root, "docs/constitution/README.md", "# The Constitution\n")
    _write(root, "docs/architecture/baseline.md", "# The Baseline\n")
    _write(root, "docs/decisions/ADR-0001.md", "# ADR-0001 - First\n")
    _write(root, "docs/rfc/RFC-0001.md", "# RFC-0001 - First\n")


def test_navigation_links_and_verbatim_titles(tmp_path):
    _corpus(tmp_path)
    out = derive_navigation(tmp_path)
    assert (
        "- [Article 1 - Mission](../constitution/01-mission.md)"
        " -- `docs/constitution/01-mission.md`" in out
    )
    assert "- [The Baseline](../architecture/baseline.md) -- `docs/architecture/baseline.md`" in out
    assert "- [ADR-0001 - First](../decisions/ADR-0001.md) -- `docs/decisions/ADR-0001.md`" in out


def test_navigation_declares_derived_and_nonauthoritative(tmp_path):
    _corpus(tmp_path)
    out = derive_navigation(tmp_path)
    assert out.startswith("# Corpus Navigation (derived)")
    assert "DERIVED, NON-AUTHORITATIVE" in out


def test_navigation_empty_corpus_reports_no_files(tmp_path):
    out = derive_navigation(tmp_path)
    assert "## Constitution (`docs/constitution/`)" in out
    assert out.count("- (no files found)") >= 4


def test_navigation_partial_corpus_reports_missing_sets(tmp_path):
    _write(tmp_path, "docs/constitution/README.md", "# C\n")
    out = derive_navigation(tmp_path)
    assert "- [C](../constitution/README.md) -- `docs/constitution/README.md`" in out
    assert "- (no files found)" in out


def test_navigation_entry_points_only_when_present(tmp_path):
    _corpus(tmp_path)
    _write(tmp_path, "README.md", "# Root\n")
    out = derive_navigation(tmp_path)
    assert "- [`README.md`](../../README.md)" in out
    assert "CONTRIBUTING.md" not in out


def test_navigation_deterministic(tmp_path):
    _corpus(tmp_path)
    assert derive_navigation(tmp_path) == derive_navigation(tmp_path)


def test_main_writes_output(tmp_path):
    _corpus(tmp_path)
    assert main(["derive_navigation.py", str(tmp_path)]) == 0
    written = tmp_path / OUTPUT_PATH
    assert written.is_file()
    assert written.read_text(encoding="utf-8") == derive_navigation(tmp_path)
