"""Mechanical governance-identifier reference checker.

Scope (L-10): this check is mechanical only. It verifies that every
ADR-XXXX and RFC-XXXX identifier mentioned in the scanned Markdown
documentation corresponds to an existing file (docs/decisions/ADR-XXXX.md,
docs/rfc/RFC-XXXX.md). It does not interpret, rank, or enforce the content,
status, or disposition of any referenced document.

Scanned roots: README.md, docs/, specs/.
Excluded: specs/fcos/ (legacy prototype specification tree; its disposition
is an open Maintainer decision recorded in docs/program/WAVE_0_VERIFICATION.md).

Exit status: 0 when all identifiers resolve, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterator, List

SCAN_ROOTS = ("README.md", "docs", "specs")
EXCLUDED_TREES = ("specs/fcos",)

ID_RULES = (
    (re.compile(r"\bADR-(\d{4})\b"), "docs/decisions/ADR-{number}.md"),
    (re.compile(r"\bRFC-(\d{4})\b"), "docs/rfc/RFC-{number}.md"),
)


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
    """Return one error string per unresolved governance identifier."""
    errors: List[str] = []
    for path in iter_markdown_files(repo_root):
        text = path.read_text(encoding="utf-8")
        for pattern, template in ID_RULES:
            for match in pattern.finditer(text):
                expected = template.format(number=match.group(1))
                if not (repo_root / expected).exists():
                    relative = path.relative_to(repo_root).as_posix()
                    entry = (
                        f"{relative}: reference {match.group(0)} "
                        f"has no file at {expected}"
                    )
                    if entry not in errors:
                        errors.append(entry)
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
        print(f"check_ids: {len(errors)} unresolved governance identifier(s) found.")
        return 1
    print("check_ids: all ADR/RFC identifiers resolve to files.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
