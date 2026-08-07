"""Shared mechanical-extraction library for the P13 documentation platform.

Governing conventions: ``docs/program/DOC_DERIVATION_CONVENTIONS.md``
(program P13, Documentation System, S14).

Everything in this module is mechanical: verbatim first headings, heading
outlines, identifier-token occurrences, and Markdown link targets. Nothing
here summarizes, interprets, or invents content, and nothing here reads or
synthesizes document status or disposition.

Scope rules (from the conventions):

- Content extraction is limited to the ratified source corpus declared in
  ``SOURCE_SETS``. ``specs/`` (In Review, blocker B-08) and
  ``docs/program/`` (plans) are never content sources.
- Derived output is informative only (Baseline L-2), never authoritative.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Sequence
from pathlib import Path

from tools.docs.derive_corpus_index import first_heading

__all__ = [
    "DERIVED_DIR",
    "ID_FAMILIES",
    "SOURCE_SETS",
    "banner",
    "extract_headings",
    "extract_ids",
    "extract_link_targets",
    "first_heading",
    "iter_source_files",
    "read_text",
    "resolve_link",
    "strip_code",
    "token_sort_key",
]

# The ratified source corpus. Kept aligned with
# tools/docs/derive_corpus_index.py (P13.1), which remains unmodified.
SOURCE_SETS: tuple[tuple[str, str, str], ...] = (
    ("Constitution", "docs/constitution", "*.md"),
    ("Architecture", "docs/architecture", "*.md"),
    ("Decision records (ADRs)", "docs/decisions", "ADR-*.md"),
    ("RFCs (dispositions recorded in ADR-0004)", "docs/rfc", "RFC-*.md"),
)

DERIVED_DIR = "docs/derived"

# Cross-document identifier families: (family label, where the vocabulary
# is recorded, token pattern). Purely lexical -- an occurrence is a token
# match, never a semantic relationship. Document-local labels (for example
# RFC option/assumption IDs such as "I-A", "N-B", "A-1") are deliberately
# not families: they are meaningful only inside one document.
ID_FAMILIES: tuple[tuple[str, str, re.Pattern[str]], ...] = (
    ("Decision records", "`docs/decisions/`", re.compile(r"\bADR-\d{4}\b")),
    ("RFCs", "`docs/rfc/`", re.compile(r"\bRFC-\d{4}\b")),
    ("Architectural principles (P-)", "Baseline \u00a72", re.compile(r"\bP-\d+\b")),
    ("Dependency laws (L-)", "Baseline \u00a75", re.compile(r"\bL-\d+\b")),
    ("Invariants (INV-)", "Blueprint \u00a712", re.compile(r"\bINV-\d+\b")),
    ("Unknowns (U-)", "Blueprint \u00a714", re.compile(r"\bU-\d+\b")),
    ("Subsystems (S)", "Blueprint \u00a72", re.compile(r"\bS\d{1,2}\b")),
    ("Decision register entries (D-)", "Baseline \u00a712; Blueprint \u00a714", re.compile(r"\bD-\d{2}\b")),
    ("Doctrine axioms (AX-)", "Doctrine \u00a71", re.compile(r"\bAX-\d+\b")),
    ("Doctrine derived principles (DP-)", "Doctrine", re.compile(r"\bDP-\d+\b")),
    ("Doctrine constraints (CN-)", "Doctrine", re.compile(r"\bCN-\d+\b")),
    ("Doctrine guidelines (GL-)", "Doctrine", re.compile(r"\bGL-\d+\b")),
    ("Doctrine observations (OB-)", "Doctrine", re.compile(r"\bOB-\d+\b")),
    ("Program blockers (B-)", "`docs/program/PROGRAM.md` \u00a76", re.compile(r"\bB-\d{2}\b")),
    ("Work prompts (WP)", "`docs/prompts/`", re.compile(r"\bWP\d{2}\b")),
)

FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "{{")

_NUM = re.compile(r"(\d+)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_code(text: str) -> str:
    """Remove fenced and inline code spans (mirrors tools/checks/check_links.py)."""
    return INLINE_CODE.sub("", FENCED_CODE.sub("", text))


def iter_source_files(root: Path) -> list[tuple[str, str, list[Path]]]:
    """Return (set title, directory, sorted files) per source set.

    Missing directories yield an empty file list; nothing is invented.
    """
    sets: list[tuple[str, str, list[Path]]] = []
    for title, directory, pattern in SOURCE_SETS:
        base = root / directory
        files = sorted(base.glob(pattern)) if base.is_dir() else []
        sets.append((title, directory, files))
    return sets


def extract_headings(text: str) -> list[tuple[int, str]]:
    """Return (level, verbatim heading text) pairs outside fenced code."""
    headings: list[tuple[int, str]] = []
    for line in FENCED_CODE.sub("", text).splitlines():
        match = HEADING.match(line)
        if match:
            headings.append((len(match.group(1)), match.group(2)))
    return headings


def extract_ids(text: str) -> dict[str, Counter]:
    """Count identifier-token occurrences per family. Lexical only."""
    found: dict[str, Counter] = {}
    for label, _source, pattern in ID_FAMILIES:
        tokens = pattern.findall(text)
        if tokens:
            found[label] = Counter(tokens)
    return found


def extract_link_targets(text: str) -> list[str]:
    """Return internal Markdown link targets in document order.

    Code spans are removed first and external/fragment/placeholder targets
    are skipped, mirroring tools/checks/check_links.py.
    """
    targets: list[str] = []
    for target in MARKDOWN_LINK.findall(strip_code(text)):
        if not target.startswith(LINK_SKIP_PREFIXES):
            targets.append(target)
    return targets


def resolve_link(root: Path, source_file: Path, target: str) -> tuple[str, bool]:
    """Resolve a link target to (repository-relative path, exists).

    Targets with a leading "/" resolve from the repository root; all other
    targets resolve from the containing file's directory. Fragments are
    dropped. Targets escaping the repository root resolve to the raw
    target with exists=False.
    """
    fragmentless = target.split("#", 1)[0]
    if not fragmentless:
        return target, False
    if fragmentless.startswith("/"):
        resolved = (root / fragmentless.lstrip("/")).resolve()
    else:
        resolved = (source_file.parent / fragmentless).resolve()
    try:
        rel = resolved.relative_to(root.resolve())
    except ValueError:
        return fragmentless, False
    return rel.as_posix(), resolved.exists()


def token_sort_key(token: str) -> tuple:
    """Natural sort: numeric segments compare as integers (U-2 before U-14)."""
    return tuple(int(part) if part.isdigit() else part for part in _NUM.split(token))


def banner(
    title: str,
    tool: str,
    output: str,
    sources: Sequence[str],
    limitations: Sequence[str] = (),
) -> str:
    """Standard header for every derived document.

    Declares the DERIVED / NON-AUTHORITATIVE class, ownership, generation
    path, regeneration instructions, source list, and limitations
    (DOC_DERIVATION_CONVENTIONS.md rule 3).
    """
    lines = [
        f"# {title} (derived)",
        "",
        "- Class: DERIVED, NON-AUTHORITATIVE -- informative documentation only",
        "  (Baseline L-2). It defines nothing; on any conflict the repository",
        "  source documents win and this file is regenerated.",
        "- Ownership: P13 documentation pipeline",
        "  (`docs/program/DOC_DERIVATION_CONVENTIONS.md`); never hand-edited.",
        f"- Generated by: `{tool}`.",
        f"- Regenerate from the repository root: `python {tool}`",
        "  (or `python tools/docs/build_docs.py` to rebuild all derived docs).",
        f"- Output: `{output}`.",
        "- Sources:",
    ]
    for source in sources:
        lines.append(f"  - {source}")
    lines.append("- Limitations: mechanical extraction only -- no summaries, no")
    lines.append("  interpretation, no status or disposition synthesis, no behavior")
    lines.append("  claims.")
    for item in limitations:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)
