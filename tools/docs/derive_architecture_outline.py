"""Generate ``docs/derived/ARCHITECTURE_OUTLINE.md``: architecture browser.

For each file under ``docs/architecture/``, emits the verbatim first
heading and an indented outline of its section headings (levels 2 and
deeper; fenced code excluded). Headings are copied verbatim -- no
summaries, no interpretation. Governed by
``docs/program/DOC_DERIVATION_CONVENTIONS.md``.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Support the documented direct-execution form from the repository root,
#     python tools/docs/derive_architecture_outline.py
# ``tools`` is a namespace package, so the repository root must be on
# ``sys.path`` before the ``tools.docs`` imports resolve; plain script
# execution puts only this file's directory there.
_REPO_ROOT = str(Path(__file__).resolve().parents[2])
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tools.docs.corpus import banner, extract_headings, first_heading, read_text

OUTPUT_PATH = "docs/derived/ARCHITECTURE_OUTLINE.md"

SOURCE_DIRECTORY = "docs/architecture"


def derive_architecture_outline(root: Path) -> str:
    base = root / SOURCE_DIRECTORY
    files = sorted(base.glob("*.md")) if base.is_dir() else []
    lines = [
        banner(
            title="Architecture Outline",
            tool="tools/docs/derive_architecture_outline.py",
            output=OUTPUT_PATH,
            sources=[f"`{SOURCE_DIRECTORY}/*.md`"],
            limitations=[
                "Headings are copied verbatim; outline depth mirrors the"
                " source heading levels.",
            ],
        )
    ]
    if not files:
        lines.append("- (no files found)")
        lines.append("")
        return "\n".join(lines)
    for path in files:
        rel = path.relative_to(root).as_posix()
        lines.append(f"## `{rel}` -- {first_heading(path)}")
        lines.append("")
        headings = [
            (level, text)
            for level, text in extract_headings(read_text(path))
            if level >= 2
        ]
        if not headings:
            lines.append("- (no section headings found)")
        else:
            for level, text in headings:
                indent = "  " * (level - 2)
                lines.append(f"{indent}- {text}")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    output = root / OUTPUT_PATH
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(derive_architecture_outline(root), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
