"""Generate ``docs/derived/DOCUMENT_GRAPH.md``: corpus link/reference graph.

Two mechanical edge kinds over the ratified source corpus:

- Markdown link edges: relative link targets, resolved from the containing
  file (unresolved targets are marked, not dropped).
- Governance reference edges: lexical ADR-/RFC-token occurrences that map
  to an existing file under ``docs/decisions/`` / ``docs/rfc/``.

An edge is never a semantic, status, or authority relationship. Governed
by ``docs/program/DOC_DERIVATION_CONVENTIONS.md``.
"""

from __future__ import annotations

import sys
from pathlib import Path

from tools.docs.corpus import (
    SOURCE_SETS,
    banner,
    extract_ids,
    extract_link_targets,
    iter_source_files,
    read_text,
    resolve_link,
    token_sort_key,
)

OUTPUT_PATH = "docs/derived/DOCUMENT_GRAPH.md"

_GOVERNANCE_LABELS = ("Decision records", "RFCs")


def _node(token: str) -> str:
    """Mermaid-safe node id for a governance token."""
    return token.replace("-", "")


def derive_document_graph(root: Path) -> str:
    all_files = [
        path for _title, _directory, files in iter_source_files(root) for path in files
    ]
    rel_of = {path: path.relative_to(root).as_posix() for path in all_files}
    governance_files = {
        path.stem: rel_of[path]
        for path in all_files
        if path.stem.startswith(("ADR-", "RFC-"))
    }

    rows: list[tuple[str, list[str], list[str]]] = []
    ref_edges: set[tuple[str, str]] = set()
    for path in sorted(all_files, key=lambda item: rel_of[item]):
        rel = rel_of[path]
        text = read_text(path)
        links: list[str] = []
        for target in dict.fromkeys(extract_link_targets(text)):
            resolved, exists = resolve_link(root, path, target)
            links.append(f"`{resolved}`" if exists else f"`{resolved}` (unresolved)")
        ids = extract_ids(text)
        tokens: set[str] = set()
        for label in _GOVERNANCE_LABELS:
            tokens.update(ids.get(label, {}))
        refs: list[str] = []
        for token in sorted(tokens, key=token_sort_key):
            target_rel = governance_files.get(token)
            if target_rel == rel:
                continue
            if target_rel:
                refs.append(f"`{target_rel}`")
                if path.stem in governance_files:
                    ref_edges.add((path.stem, token))
            else:
                refs.append(f"{token} (unresolved)")
        rows.append((rel, links, refs))

    lines = [
        banner(
            title="Document Graph",
            tool="tools/docs/derive_document_graph.py",
            output=OUTPUT_PATH,
            sources=[
                f"`{directory}/{pattern}`"
                for _title, directory, pattern in SOURCE_SETS
            ],
            limitations=[
                "An edge is a Markdown link or a lexical token occurrence,"
                " never a semantic, status, or authority relationship.",
                "External, fragment-only, and placeholder link targets are"
                " not graphed.",
            ],
        )
    ]
    lines.append("## Edges by document")
    lines.append("")
    if not rows:
        lines.append("- (no files found)")
        lines.append("")
    else:
        lines.append("| Document | Relative links to | Governance records referenced |")
        lines.append("| --- | --- | --- |")
        for rel, links, refs in rows:
            link_cell = "; ".join(links) if links else "(none)"
            ref_cell = "; ".join(refs) if refs else "(none)"
            lines.append(f"| `{rel}` | {link_cell} | {ref_cell} |")
        lines.append("")
    lines.append("## Governance reference graph (ADR / RFC files)")
    lines.append("")
    lines.append('Edges read "source mentions target" -- lexical token occurrence only.')
    lines.append("")
    if not ref_edges:
        lines.append("- (no reference edges found)")
        lines.append("")
    else:
        nodes = sorted({token for edge in ref_edges for token in edge}, key=token_sort_key)
        lines.append("```mermaid")
        lines.append("flowchart LR")
        for node in nodes:
            lines.append(f'  {_node(node)}["{node}"]')
        for source, target in sorted(ref_edges):
            lines.append(f"  {_node(source)} --> {_node(target)}")
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    output = root / OUTPUT_PATH
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(derive_document_graph(root), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
