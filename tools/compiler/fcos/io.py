from __future__ import annotations

from pathlib import Path


SUPPORTED_SPEC_EXTENSIONS = {".md"}


def discover_specifications(repository: Path) -> list[Path]:
    """
    Discover all FCOS specification files inside a repository.
    """

    specifications: list[Path] = []

    specs_root = repository / "specs"

    if not specs_root.exists():
        return specifications

    for path in specs_root.rglob("*"):
        if path.is_file() and path.suffix in SUPPORTED_SPEC_EXTENSIONS:
            specifications.append(path)

    return sorted(specifications)


def read_text(path: Path) -> str:
    """
    Read a UTF-8 encoded text file.
    """

    return path.read_text(
        encoding="utf-8",
    )


def write_text(path: Path, content: str) -> None:
    """
    Write UTF-8 encoded text to a file.
    """

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        content,
        encoding="utf-8",
    )