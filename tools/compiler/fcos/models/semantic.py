from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .diagnostic import Diagnostic


@dataclass(slots=True)
class Dependency:
    source: str
    target: str
    relationship: str


@dataclass(slots=True)
class SemanticDocument:
    identifier: str
    version: str
    classification: str
    status: str
    metadata: dict[str, Any] = field(default_factory=dict)
    dependencies: list[Dependency] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)
    diagnostics: list[Diagnostic] = field(default_factory=list)


@dataclass(slots=True)
class SemanticModel:
    repository_identifier: str
    repository_metadata: dict[str, Any] = field(default_factory=dict)
    documents: list[SemanticDocument] = field(default_factory=list)
    compiler_directives: dict[str, Any] = field(default_factory=dict)
    diagnostics: list[Diagnostic] = field(default_factory=list)
    semantic_version: str = "1.0.0"

    def add_document(self, document: SemanticDocument) -> None:
        self.documents.append(document)

    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        self.diagnostics.append(diagnostic)