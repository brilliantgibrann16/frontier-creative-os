from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .diagnostic import Diagnostic


@dataclass(slots=True)
class ASTNode:
    identifier: str
    node_type: str
    value: Any | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    children: list["ASTNode"] = field(default_factory=list)
    start_line: int = 0
    end_line: int = 0
    start_column: int = 0
    end_column: int = 0

    def add_child(self, node: "ASTNode") -> None:
        self.children.append(node)


@dataclass(slots=True)
class AbstractSyntaxTree:
    document_identifier: str
    document_path: str
    parser_version: str
    root: ASTNode
    diagnostics: list[Diagnostic] = field(default_factory=list)

    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        self.diagnostics.append(diagnostic)