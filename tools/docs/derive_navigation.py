"""Generate ``docs/derived/NAVIGATION.md``: navigation over the ratified corpus.

Mechanical only: verbatim first headings and repository paths, plus a fixed
list of human-maintained entry points linked by path (no content is read
from them). Governed by ``docs/program/DOC_DERIVATION_CONVENTIONS.md``.
"""

from __future__ import annotations

import sys
from pathlib import Path

from tools.docs.corpus import SOURCE_SETS, banner, first_heading, iter_source_files

OUTPUT_PATH = "docs/derived/NAVIGATION.md"

# Human-maintained entry points, linked by path only (their content is not
# a derivation source). Fixed list; an entry is emitted only when the file
# exists in the tree being scanned, so generated links always resolve.
ENTRY_POINTS = (
    "README.md",
    "CONTRIBUTING.md",
    "docs/rfc/README.md",
    "docs/prompts/README.md",
    "docs/program/PROGRAM_INDEX.md",
    "specs/README.md",
)


def _rel_from_output(rel_path: str) -> str:
    """Relative path from ``docs/derived/`` to a repository-relative path."""
    if rel_path.startswith("docs/"):
        return "../" + rel_path[len("docs/"):]
    return "../../" + rel_path


def derive_navigation(root: Path) -> str:
    lines = [
        banner(
            title="Corpus Navigation",
            tool="tools/docs/derive_navigation.py",
            output=OUTPUT_PATH,
            sources=[
                f"`{directory}/{pattern}`"
                for _title, directory, pattern in SOURCE_SETS
            ],
            limitations=[
                "Titles are verbatim first headings; files without a heading"
                " fall back to the filename.",
                "Entry points are linked by path only; their content is not"
                " derived from.",
            ],
        )
    ]
    for title, directory, files in iter_source_files(root):
        lines.append(f"## {title} (`{directory}/`)")
        lines.append("")
        if not files:
            lines.append("- (no files found)")
        else:
            for path in files:
                rel = path.relative_to(root).as_posix()
                lines.append(
                    f"- [{first_heading(path)}]({_rel_from_output(rel)}) -- `{rel}`"
                )
        lines.append("")
    lines.append("## Repository entry points (path links only)")
    lines.append("")
    entries = [entry for entry in ENTRY_POINTS if (root / entry).is_file()]
    if not entries:
        lines.append("- (no files found)")
    else:
        for entry in entries:
            lines.append(f"- [`{entry}`]({_rel_from_output(entry)})")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    output = root / OUTPUT_PATH
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(derive_navigation(root), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
