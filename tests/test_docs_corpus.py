"""Fixture tests for the shared corpus library of the P13 platform."""

from pathlib import Path

from tools.docs.corpus import (
    banner,
    extract_headings,
    extract_ids,
    extract_link_targets,
    iter_source_files,
    resolve_link,
    strip_code,
    token_sort_key,
)


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_extract_ids_counts_duplicates_per_family():
    ids = extract_ids("ADR-0001 then ADR-0001 again, RFC-0002, INV-9, not adr-0001")
    assert ids["Decision records"]["ADR-0001"] == 2
    assert ids["RFCs"]["RFC-0002"] == 1
    assert ids["Invariants (INV-)"]["INV-9"] == 1
    assert "Doctrine axioms (AX-)" not in ids


def test_extract_ids_requires_word_boundaries():
    ids = extract_ids("XADR-0001 ADR-00012 D-01 GD01")
    assert "Decision records" not in ids
    assert ids["Decision register entries (D-)"]["D-01"] == 1


def test_strip_code_removes_fenced_and_inline_spans():
    text = "keep `gone` keep\n```\nfenced gone\n```\nkeep"
    stripped = strip_code(text)
    assert "gone" not in stripped
    assert stripped.count("keep") == 3


def test_extract_link_targets_skips_code_and_external():
    text = (
        "See [a](./x.md) and [b](https://example.com) and `[c](./y.md)`\n"
        "```\n[d](./z.md)\n```\n[e](#frag) [f](mailto:x@y.z)"
    )
    assert extract_link_targets(text) == ["./x.md"]


def test_resolve_link_relative_root_and_missing(tmp_path):
    _write(tmp_path, "docs/a/source.md", "x")
    _write(tmp_path, "docs/b/target.md", "y")
    source = tmp_path / "docs/a/source.md"
    assert resolve_link(tmp_path, source, "../b/target.md") == ("docs/b/target.md", True)
    assert resolve_link(tmp_path, source, "/docs/b/target.md") == ("docs/b/target.md", True)
    assert resolve_link(tmp_path, source, "../b/absent.md#frag") == ("docs/b/absent.md", False)


def test_extract_headings_skips_fenced_code():
    text = "# T\n\n## Real\n\n```\n## Fenced\n```\n\n### Deep\n"
    assert extract_headings(text) == [(1, "T"), (2, "Real"), (3, "Deep")]


def test_iter_source_files_sorted_and_missing_dirs_empty(tmp_path):
    _write(tmp_path, "docs/constitution/02-b.md", "# B")
    _write(tmp_path, "docs/constitution/01-a.md", "# A")
    sets = {directory: files for _title, directory, files in iter_source_files(tmp_path)}
    assert [p.name for p in sets["docs/constitution"]] == ["01-a.md", "02-b.md"]
    assert sets["docs/rfc"] == []


def test_iter_source_files_filters_by_pattern(tmp_path):
    _write(tmp_path, "docs/decisions/ADR-0001.md", "# ADR-0001")
    _write(tmp_path, "docs/decisions/D01_DECISION_BRIEF.md", "# Brief")
    sets = {directory: files for _title, directory, files in iter_source_files(tmp_path)}
    assert [p.name for p in sets["docs/decisions"]] == ["ADR-0001.md"]


def test_token_sort_key_natural_order():
    assert sorted(["U-14", "U-2", "U-1"], key=token_sort_key) == ["U-1", "U-2", "U-14"]


def test_banner_declares_required_fields():
    text = banner(
        title="Sample",
        tool="tools/docs/derive_sample.py",
        output="docs/derived/SAMPLE.md",
        sources=["`docs/constitution/*.md`"],
        limitations=["Extra limitation."],
    )
    assert text.startswith("# Sample (derived)")
    assert "DERIVED, NON-AUTHORITATIVE" in text
    assert "Ownership: P13 documentation pipeline" in text
    assert "`tools/docs/derive_sample.py`" in text
    assert "Regenerate from the repository root" in text
    assert "`docs/constitution/*.md`" in text
    assert "Extra limitation." in text
