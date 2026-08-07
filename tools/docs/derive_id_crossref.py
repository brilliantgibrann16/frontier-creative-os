"""Generate ``docs/derived/ID_CROSSREF.md``: identifier occurrence index.

For every recorded identifier family (see ``tools.docs.corpus.ID_FAMILIES``)
this maps each token to the ratified-corpus files that mention it, with
occurrence counts. An occurrence is a lexical token match, never a semantic
relationship. Governed by ``docs/program/DOC_DERIVATION_CONVENTIONS.md``.

Also reports ADR-/RFC-style tokens whose backing file does not exist -- a
mechanical existence check mirroring ``tools/checks/check_ids.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path

from tools.docs.corpus import (
    ID_FAMILIES,
    SOURCE_SETS,
    banner,
    extract_ids,
    iter_source_files,
    read_text,
    token_sort_key,
)

OUTPUT_PATH = "docs/derived/ID_CROSSREF.md"

# Families whose tokens are backed by files, checked for existence.
_FILE_BACKED_FAMILIES = (
    ("Decision records", "docs/decisions"),
    ("RFCs", "docs/rfc"),
)


def derive_id_crossref(root: Path) -> str:
    occurrences: dict[str, dict[str, dict[str, int]]] = {}
    for _title, _directory, files in iter_source_files(root):
        for path in files:
            rel = path.relative_to(root).as_posix()
            for label, counter in extract_ids(read_text(path)).items():
                for token, count in counter.items():
                    occurrences.setdefault(label, {}).setdefault(token, {})[rel] = count

    lines = [
        banner(
            title="Identifier Cross-Reference",
            tool="tools/docs/derive_id_crossref.py",
            output=OUTPUT_PATH,
            sources=[
                f"`{directory}/{pattern}`"
                for _title, directory, pattern in SOURCE_SETS
            ],
            limitations=[
                "An occurrence is a lexical token match, never a semantic"
                " relationship or a status statement.",
                "Document-local option/assumption labels (for example \"I-A\","
                " \"N-B\", \"A-1\") are not indexed.",
            ],
        )
    ]

    for label, source, _pattern in ID_FAMILIES:
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"Vocabulary recorded in: {source}.")
        lines.append("")
        tokens = occurrences.get(label, {})
        if not tokens:
            lines.append("- (no occurrences in the source corpus)")
            lines.append("")
            continue
        lines.append("| Identifier | Occurrences |")
        lines.append("| --- | --- |")
        for token in sorted(tokens, key=token_sort_key):
            cells = "; ".join(
                f"`{rel}` ({tokens[token][rel]})" for rel in sorted(tokens[token])
            )
            lines.append(f"| {token} | {cells} |")
        lines.append("")

    lines.append("## Unresolved governance references")
    lines.append("")
    lines.append("ADR-/RFC-style tokens found in the source corpus whose file does not")
    lines.append("exist (mechanical existence check, mirroring `tools/checks/check_ids.py`):")
    lines.append("")
    unresolved: list[str] = []
    for label, directory in _FILE_BACKED_FAMILIES:
        for token in sorted(occurrences.get(label, {}), key=token_sort_key):
            expected_rel = f"{directory}/{token}.md"
            if not (root / expected_rel).is_file():
                refs = "; ".join(
                    f"`{rel}`" for rel in sorted(occurrences[label][token])
                )
                unresolved.append(
                    f"- {token} (expected `{expected_rel}`) referenced in {refs}"
                )
    if unresolved:
        lines.extend(unresolved)
    else:
        lines.append("- (none)")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    output = root / OUTPUT_PATH
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(derive_id_crossref(root), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
