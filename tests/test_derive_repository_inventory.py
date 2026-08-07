"""Fixture tests for the repository inventory generator (P13 platform)."""

from pathlib import Path

from tools.docs.derive_repository_inventory import (
    OUTPUT_PATH,
    derive_repository_inventory,
    iter_repository_files,
    main,
)


def _write(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_inventory_groups_counts_and_sorting(tmp_path):
    _write(tmp_path, "README.md", "# R\n")
    _write(tmp_path, "docs/b.md", "# B\n")
    _write(tmp_path, "docs/a.md", "# A\n")
    _write(tmp_path, "tools/x.py", "x = 1\n")
    out = derive_repository_inventory(tmp_path)
    assert "## (repository root) (files: 1)" in out
    assert "## `docs/` (files: 2)" in out
    assert "## `tools/` (files: 1)" in out
    assert out.index("- `docs/a.md`") < out.index("- `docs/b.md`")
    assert "- Files listed: 4" in out
    assert "- Top-level groups: 3" in out


def test_inventory_excludes_caches_derived_output_and_git(tmp_path):
    _write(tmp_path, "docs/a.md", "# A\n")
    _write(tmp_path, "docs/derived/NAVIGATION.md", "# N\n")
    _write(tmp_path, "tools/__pycache__/x.pyc", "z")
    _write(tmp_path, "tools/y.pyc", "z")
    _write(tmp_path, ".git/config", "z")
    _write(tmp_path, ".pytest_cache/v/cache", "z")
    assert iter_repository_files(tmp_path) == ["docs/a.md"]
    out = derive_repository_inventory(tmp_path)
    assert "- `docs/derived/NAVIGATION.md`" not in out
    assert "- `tools/__pycache__/x.pyc`" not in out
    assert "- `tools/y.pyc`" not in out
    assert "- `.git/config`" not in out
    assert "- Files listed: 1" in out


def test_inventory_empty_tree(tmp_path):
    out = derive_repository_inventory(tmp_path)
    assert "- Files listed: 0" in out
    assert "- Top-level groups: 0" in out


def test_inventory_declares_derived_and_nonauthoritative(tmp_path):
    _write(tmp_path, "docs/a.md", "# A\n")
    out = derive_repository_inventory(tmp_path)
    assert out.startswith("# Repository Inventory (derived)")
    assert "DERIVED, NON-AUTHORITATIVE" in out


def test_inventory_deterministic(tmp_path):
    _write(tmp_path, "docs/a.md", "# A\n")
    assert derive_repository_inventory(tmp_path) == derive_repository_inventory(tmp_path)


def test_main_idempotent_across_runs(tmp_path):
    _write(tmp_path, "docs/a.md", "# A\n")
    assert main(["derive_repository_inventory.py", str(tmp_path)]) == 0
    first = (tmp_path / OUTPUT_PATH).read_text(encoding="utf-8")
    assert main(["derive_repository_inventory.py", str(tmp_path)]) == 0
    second = (tmp_path / OUTPUT_PATH).read_text(encoding="utf-8")
    assert first == second
    # The second run executes with docs/derived/ already on disk; the
    # inventory must not list its own output file (self-listing would
    # make regeneration non-idempotent).
    assert f"- `{OUTPUT_PATH}`" not in second
