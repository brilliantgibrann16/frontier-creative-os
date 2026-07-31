from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .diagnostic import Diagnostic


@dataclass(slots=True)
class Artifact:
    identifier: str
    name: str
    artifact_type: str
    version: str
    output_path: str
    target_platform: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    diagnostics: list[Diagnostic] = field(default_factory=list)
    generation_timestamp: str = ""

    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        self.diagnostics.append(diagnostic)