"""Fixture tests for the document graph generator (P13 platform)."""

from pathlib import Path

from tools.docs.derive_document_graph import OUTPUT_PATH, derive_document_graph, main


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _corpus(root: Path) -> None:
    _write(
        root,
        "docs/architecture/README.md",
        "# Arch\n\nSee [Baseline](./baseline.md) and [missing](./absent.md).\n",
    )
    _write(root, "docs/architecture/baseline.md", "# Baseline\n")
    _write(root, "docs/decisions/ADR-0001.md", "# ADR-0001 - First\n\nAccepts RFC-0001.\n")
    _write(root, "docs/rfc/RFC-0001.md", "# RFC-0001 - First\n")


def test_graph_link_edges_resolved_and_unresolved(tmp_path):
    _corpus(tmp_path)
    out = derive_document_graph(tmp_path)
    assert (
        "| `docs/architecture/README.md` | `docs/architecture/baseline.md`;"
        " `docs/architecture/absent.md` (unresolved) | (none) |" in out
    )


def test_graph_reference_edges_and_mermaid(tmp_path):
    _corpus(tmp_path)
    out = derive_document_graph(tmp_path)
    assert "| `docs/decisions/ADR-0001.md` | (none) | `docs/rfc/RFC-0001.md` |" in out
    assert '  ADR0001["ADR-0001"]' in out
    assert '  RFC0001["RFC-0001"]' in out
    assert "  ADR0001 --> RFC0001" in out
    assert "ADR0001 --> ADR0001" not in out


def test_graph_unresolved_governance_token_marked(tmp_path):
    _write(tmp_path, "docs/rfc/RFC-0001.md", "# RFC-0001\n\nMentions ADR-0099.\n")
    out = derive_document_graph(tmp_path)
    assert "ADR-0099 (unresolved)" in out
    assert "- (no reference edges found)" in out


def test_graph_empty_corpus(tmp_path):
    out = derive_document_graph(tmp_path)
    assert "- (no files found)" in out
    assert "- (no reference edges found)" in out


def test_graph_partial_corpus_without_governance_files(tmp_path):
    _write(tmp_path, "docs/constitution/01-mission.md", "# One\n")
    out = derive_document_graph(tmp_path)
    assert "| `docs/constitution/01-mission.md` | (none) | (none) |" in out
    assert "- (no reference edges found)" in out


def test_graph_declares_derived_and_nonauthoritative(tmp_path):
    _corpus(tmp_path)
    out = derive_document_graph(tmp_path)
    assert out.startswith("# Document Graph (derived)")
    assert "DERIVED, NON-AUTHORITATIVE" in out


def test_graph_deterministic(tmp_path):
    _corpus(tmp_path)
    assert derive_document_graph(tmp_path) == derive_document_graph(tmp_path)


def test_main_writes_output(tmp_path):
    _corpus(tmp_path)
    assert main(["derive_document_graph.py", str(tmp_path)]) == 0
    written = tmp_path / OUTPUT_PATH
    assert written.is_file()
    assert written.read_text(encoding="utf-8") == derive_document_graph(tmp_path)
