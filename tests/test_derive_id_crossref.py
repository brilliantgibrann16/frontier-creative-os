"""Fixture tests for the identifier cross-reference generator (P13 platform)."""

from pathlib import Path

from tools.docs.derive_id_crossref import OUTPUT_PATH, derive_id_crossref, main


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _corpus(root: Path) -> None:
    _write(
        root,
        "docs/decisions/ADR-0001.md",
        "# ADR-0001 - First\n\nCites RFC-0001 and INV-9 and INV-9.\n",
    )
    _write(root, "docs/rfc/RFC-0001.md", "# RFC-0001 - First\n\nCites U-2 and U-14.\n")


def test_crossref_maps_tokens_to_files_with_counts(tmp_path):
    _corpus(tmp_path)
    out = derive_id_crossref(tmp_path)
    assert "| INV-9 | `docs/decisions/ADR-0001.md` (2) |" in out
    assert (
        "| RFC-0001 | `docs/decisions/ADR-0001.md` (1); `docs/rfc/RFC-0001.md` (1) |"
        in out
    )
    assert "| ADR-0001 | `docs/decisions/ADR-0001.md` (1) |" in out


def test_crossref_natural_token_sort(tmp_path):
    _write(tmp_path, "docs/rfc/RFC-0001.md", "# RFC-0001\n\nU-1 U-2 U-14\n")
    out = derive_id_crossref(tmp_path)
    assert out.index("| U-1 |") < out.index("| U-2 |") < out.index("| U-14 |")


def test_crossref_reports_unresolved_governance_references(tmp_path):
    _write(tmp_path, "docs/rfc/RFC-0001.md", "# RFC-0001\n\nMentions ADR-0099.\n")
    out = derive_id_crossref(tmp_path)
    assert (
        "- ADR-0099 (expected `docs/decisions/ADR-0099.md`) referenced in"
        " `docs/rfc/RFC-0001.md`" in out
    )


def test_crossref_unresolved_none_when_clean(tmp_path):
    _corpus(tmp_path)
    out = derive_id_crossref(tmp_path)
    assert "- (none)" in out
    assert "(expected" not in out


def test_crossref_empty_corpus(tmp_path):
    out = derive_id_crossref(tmp_path)
    assert "- (no occurrences in the source corpus)" in out
    assert "- (none)" in out


def test_crossref_declares_derived_and_nonauthoritative(tmp_path):
    _corpus(tmp_path)
    out = derive_id_crossref(tmp_path)
    assert out.startswith("# Identifier Cross-Reference (derived)")
    assert "DERIVED, NON-AUTHORITATIVE" in out


def test_crossref_deterministic(tmp_path):
    _corpus(tmp_path)
    assert derive_id_crossref(tmp_path) == derive_id_crossref(tmp_path)


def test_main_writes_output(tmp_path):
    _corpus(tmp_path)
    assert main(["derive_id_crossref.py", str(tmp_path)]) == 0
    written = tmp_path / OUTPUT_PATH
    assert written.is_file()
    assert written.read_text(encoding="utf-8") == derive_id_crossref(tmp_path)
