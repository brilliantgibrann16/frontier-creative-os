from __future__ import annotations

from pathlib import Path

from .io import read_text
from .models import (
    ASTNode,
    AbstractSyntaxTree,
)


class Parser:
    """
    FCOS specification parser.

    Responsibilities:
    - Read specification files
    - Parse YAML-like front matter
    - Build heading hierarchy
    - Attach section content
    """

    VERSION = "1.0.0"

    def parse(self, path: Path) -> AbstractSyntaxTree:
        content = read_text(path)
        lines = content.splitlines()

        metadata, body = self._extract_front_matter(lines)

        root = ASTNode(
            identifier=path.stem,
            node_type="document",
            value=None,
            metadata=metadata,
            start_line=1,
            end_line=len(lines),
        )

        self._build_heading_tree(root, body)

        return AbstractSyntaxTree(
            document_identifier=path.stem,
            document_path=str(path),
            parser_version=self.VERSION,
            root=root,
        )

    def parse_repository(
        self,
        specification_paths: list[Path],
    ) -> list[AbstractSyntaxTree]:
        return [self.parse(path) for path in specification_paths]

    def _extract_front_matter(
        self,
        lines: list[str],
    ) -> tuple[dict[str, str], list[str]]:
        """
        Extract simple YAML front matter.
        """

        if not lines:
            return {}, []

        if lines[0].strip() != "---":
            return {}, lines

        metadata: dict[str, str] = {}

        end = None

        for index in range(1, len(lines)):
            line = lines[index]

            if line.strip() == "---":
                end = index
                break

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            metadata[key.strip()] = value.strip()

        if end is None:
            return {}, lines

        return metadata, lines[end + 1 :]

    def _build_heading_tree(
        self,
        root: ASTNode,
        lines: list[str],
    ) -> None:
        """
        Build heading hierarchy and attach section content.
        """

        stack: list[tuple[int, ASTNode]] = [(0, root)]

        current_heading: ASTNode | None = None

        content_buffer: list[str] = []

        def flush() -> None:
            nonlocal content_buffer

            if current_heading is None:
                content_buffer = []
                return

            text = "\n".join(content_buffer).strip()

            if text:
                current_heading.add_child(
                    ASTNode(
                        identifier=f"{current_heading.identifier}-content",
                        node_type="content",
                        value=text,
                    )
                )

            content_buffer = []

        for line_number, line in enumerate(lines, start=1):

            stripped = line.strip()

            if stripped.startswith("#"):

                flush()

                level = len(stripped) - len(stripped.lstrip("#"))

                title = stripped[level:].strip()

                node = ASTNode(
                    identifier=f"heading-{line_number}",
                    node_type=f"h{level}",
                    value=title,
                    start_line=line_number,
                    end_line=line_number,
                )

                while stack and stack[-1][0] >= level:
                    stack.pop()

                parent = stack[-1][1]

                parent.add_child(node)

                stack.append((level, node))

                current_heading = node

            else:

                content_buffer.append(line)

        flush()