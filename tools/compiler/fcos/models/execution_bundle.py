from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .artifact import Artifact
from .diagnostic import Diagnostic


@dataclass(slots=True)
class ExecutionBundle:
    bundle_identifier: str
    bundle_version: str
    compiler_version: str
    specification_version: str

    artifacts: list[Artifact] = field(default_factory=list)

    manifest: dict[str, Any] = field(default_factory=dict)

    build_metadata: dict[str, Any] = field(default_factory=dict)

    diagnostics: list[Diagnostic] = field(default_factory=list)

    creation_timestamp: str = ""

    def add_artifact(self, artifact: Artifact) -> None:
        self.artifacts.append(artifact)

    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        self.diagnostics.append(diagnostic)