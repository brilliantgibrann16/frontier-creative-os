"""Mechanical internal-link checker for repository Markdown documentation.

Scope (L-10): this check is mechanical only. It verifies that relative
Markdown links point at files or directories that exist in the repository.
It expresses no policy and makes no judgment about document content.

Scanned roots: README.md, docs/, specs/.
Excluded: specs/fcos/ (legacy prototype specification tree; its disposition
is an open Maintainer decision recorded in docs/program/WAVE_0_VERIFICATION.md).

Exit status: 0 when all internal links resolve, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterator, List

SCAN_ROOTS = ("README.md", "docs", "specs")
EXCLUDED_TREES = ("specs/fcos",)
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "{{")

FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")


def _is_excluded(relative_path: str) -> bool:
    return any(
        relative_path == tree or relative_path.startswith(tree + "/")
        for tree in EXCLUDED_TREES
    )


def iter_markdown_files(repo_root: Path) -> Iterator[Path]:
    """Yield every Markdown file under the scanned roots, minus exclusions."""
    for entry in SCAN_ROOTS:
        target = repo_root / entry
        if target.is_file():
            yield target
        elif target.is_dir():
            for path in sorted(target.rglob("*.md")):
                if _is_excluded(path.relative_to(repo_root).as_posix()):
                    continue
                yield path


def collect_errors(repo_root: Path) -> List[str]:
    """Return one error string per broken relative link found."""
    errors: List[str] = []
    for path in iter_markdown_files(repo_root):
        text = path.read_text(encoding="utf-8")
        text = FENCED_CODE.sub("", text)
        text = INLINE_CODE.sub("", text)
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1)
            if raw_target.startswith(SKIP_PREFIXES):
                continue
            target = raw_target.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                resolved = repo_root / target.lstrip("/")
            else:
                resolved = path.parent / target
            if not resolved.exists():
                relative = path.relative_to(repo_root).as_posix()
                errors.append(f"{relative}: broken link -> {raw_target}")
    return errors


def main(argv: List[str]) -> int:
    repo_root = (
        Path(argv[1]).resolve()
        if len(argv) > 1
        else Path(__file__).resolve().parents[2]
    )
    errors = collect_errors(repo_root)
    for error in errors:
        print(error)
    if errors:
        print(f"check_links: {len(errors)} broken internal link(s) found.")
        return 1
    print("check_links: all internal Markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
