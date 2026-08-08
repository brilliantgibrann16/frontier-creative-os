"""Regression tests for the documented docs-tool command-line form.

Each generated banner and ``docs/program/DOC_DERIVATION_CONVENTIONS.md``
document direct script execution from the repository root, for example
``python tools/docs/build_docs.py``. ``tools`` is a namespace package
(there is no ``tools/__init__.py``), so plain script execution must put
the repository root on ``sys.path`` itself; a failure there is invisible
to in-process imports and only surfaces in subprocess runs. These tests
execute the real scripts exactly as documented, against a throwaway root
so nothing outside the fixture directory is written.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

DERIVE_TOOLS = (
    ("tools/docs/derive_corpus_index.py", "CORPUS_INDEX.md"),
    ("tools/docs/derive_navigation.py", "NAVIGATION.md"),
    ("tools/docs/derive_id_crossref.py", "ID_CROSSREF.md"),
    ("tools/docs/derive_document_graph.py", "DOCUMENT_GRAPH.md"),
    ("tools/docs/derive_architecture_outline.py", "ARCHITECTURE_OUTLINE.md"),
    ("tools/docs/derive_repository_inventory.py", "REPOSITORY_INVENTORY.md"),
)


def run_tool(script: str, root: Path) -> subprocess.CompletedProcess[str]:
    """Run ``python <script> <root>`` from the repository root."""
    return subprocess.run(
        [sys.executable, script, str(root)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def test_build_docs_runs_as_documented_script(tmp_path: Path) -> None:
    result = run_tool("tools/docs/build_docs.py", tmp_path)
    assert result.returncode == 0, result.stderr
    assert result.stdout.count("wrote ") == len(DERIVE_TOOLS)
    written = sorted(p.name for p in (tmp_path / "docs" / "derived").glob("*.md"))
    assert written == sorted(output for _script, output in DERIVE_TOOLS)


@pytest.mark.parametrize(("script", "output"), DERIVE_TOOLS)
def test_derive_tool_runs_as_documented_script(
    tmp_path: Path, script: str, output: str
) -> None:
    result = run_tool(script, tmp_path)
    assert result.returncode == 0, result.stderr
    path = tmp_path / "docs" / "derived" / output
    assert path.is_file()
    first_line = path.read_text(encoding="utf-8").splitlines()[0]
    assert first_line.startswith("# ")
    assert first_line.endswith("(derived)")
