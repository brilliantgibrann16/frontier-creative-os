"""Build orchestrator for the P13 documentation platform.

Builds every derived document under ``docs/derived/`` in one
deterministic pass, or verifies (``--check``) that the committed derived
output matches regeneration byte for byte.

Governed by ``docs/program/DOC_DERIVATION_CONVENTIONS.md``: derived
output is DERIVED / NON-AUTHORITATIVE, informative only (Baseline L-2),
and staleness is corrected by regeneration, never by hand-editing.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path

from tools.docs import (
    derive_architecture_outline,
    derive_corpus_index,
    derive_document_graph,
    derive_id_crossref,
    derive_navigation,
    derive_repository_inventory,
)

# Registry of (output path, derivation callable). Order is the build
# order; every generator is independent of the others' output (the
# repository inventory excludes docs/derived/), so order does not affect
# results -- it is fixed here for stable, readable logs.
GENERATORS: tuple[tuple[str, Callable[[Path], str]], ...] = (
    (derive_corpus_index.OUTPUT_PATH, derive_corpus_index.derive_index),
    (derive_navigation.OUTPUT_PATH, derive_navigation.derive_navigation),
    (derive_id_crossref.OUTPUT_PATH, derive_id_crossref.derive_id_crossref),
    (derive_document_graph.OUTPUT_PATH, derive_document_graph.derive_document_graph),
    (
        derive_architecture_outline.OUTPUT_PATH,
        derive_architecture_outline.derive_architecture_outline,
    ),
    (
        derive_repository_inventory.OUTPUT_PATH,
        derive_repository_inventory.derive_repository_inventory,
    ),
)


def build(root: Path) -> list[Path]:
    """Regenerate every derived document. Returns the written paths."""
    written: list[Path] = []
    for output_path, derive in GENERATORS:
        output = root / output_path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(derive(root), encoding="utf-8")
        written.append(output)
    return written


def check(root: Path) -> list[str]:
    """Compare committed derived output with regeneration.

    Returns problem strings (MISSING/STALE); an empty list means fresh.
    """
    problems: list[str] = []
    for output_path, derive in GENERATORS:
        output = root / output_path
        if not output.is_file():
            problems.append(f"MISSING: {output_path}")
            continue
        if output.read_text(encoding="utf-8") != derive(root):
            problems.append(
                f"STALE: {output_path}"
                " (regenerate: python tools/docs/build_docs.py)"
            )
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build or verify the derived documentation set."
    )
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify committed derived output matches regeneration",
    )
    args = parser.parse_args(argv)
    root = Path(args.root)
    if args.check:
        problems = check(root)
        for problem in problems:
            print(problem)
        if problems:
            return 1
        print("derived documentation is fresh")
        return 0
    for output in build(root):
        print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
