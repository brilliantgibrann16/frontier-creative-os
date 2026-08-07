"""Generate ``docs/derived/REPOSITORY_INVENTORY.md``: paths-only inventory.

Walks the repository tree and lists file paths grouped by top-level
directory, with counts. No file content is read and no meaning is
attached to any path. Governed by
``docs/program/DOC_DERIVATION_CONVENTIONS.md``.

Exclusions: ``.git/``, ``__pycache__/``, ``.pytest_cache/``, ``*.pyc``,
and the derived output directory ``docs/derived/`` itself. Excluding the
output area is what keeps generation idempotent: if the inventory listed
its own output, the first build and every rebuild would disagree.
"""

from __future__ import annotations

import sys
from pathlib import Path

from tools.docs.corpus import DERIVED_DIR, banner

OUTPUT_PATH = "docs/derived/REPOSITORY_INVENTORY.md"

EXCLUDED_DIR_NAMES = (".git", "__pycache__", ".pytest_cache")
EXCLUDED_TREES = (DERIVED_DIR,)
EXCLUDED_SUFFIXES = (".pyc",)

_ROOT_GROUP = "(repository root)"


def iter_repository_files(root: Path) -> list[str]:
    """Sorted repository-relative file paths, after exclusions."""
    results: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        parts = rel.split("/")
        if any(part in EXCLUDED_DIR_NAMES for part in parts):
            continue
        if any(rel == tree or rel.startswith(tree + "/") for tree in EXCLUDED_TREES):
            continue
        if rel.endswith(EXCLUDED_SUFFIXES):
            continue
        results.append(rel)
    return sorted(results)


def derive_repository_inventory(root: Path) -> str:
    files = iter_repository_files(root)
    groups: dict[str, list[str]] = {}
    for rel in files:
        top = rel.split("/", 1)[0] if "/" in rel else _ROOT_GROUP
        groups.setdefault(top, []).append(rel)

    lines = [
        banner(
            title="Repository Inventory",
            tool="tools/docs/derive_repository_inventory.py",
            output=OUTPUT_PATH,
            sources=[
                "Repository file tree (paths only; no file content is read).",
            ],
            limitations=[
                "Paths carry no meaning here: a listing is not a status,"
                " an endorsement, or an authority statement.",
                "Excluded from the walk: `.git/`, `__pycache__/`,"
                " `.pytest_cache/`, `*.pyc`, and the output area"
                " `docs/derived/` (self-listing would break idempotent"
                " regeneration).",
            ],
        )
    ]
    ordered = ([_ROOT_GROUP] if _ROOT_GROUP in groups else []) + sorted(
        key for key in groups if key != _ROOT_GROUP
    )
    for key in ordered:
        entries = groups[key]
        title = key if key == _ROOT_GROUP else f"`{key}/`"
        lines.append(f"## {title} (files: {len(entries)})")
        lines.append("")
        for rel in entries:
            lines.append(f"- `{rel}`")
        lines.append("")
    lines.append("## Totals")
    lines.append("")
    lines.append(f"- Files listed: {len(files)}")
    lines.append(f"- Top-level groups: {len(groups)}")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    output = root / OUTPUT_PATH
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(derive_repository_inventory(root), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
