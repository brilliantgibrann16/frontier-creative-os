from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .diagnostic import Diagnostic
from .execution_bundle import ExecutionBundle
from .validation import ValidationReport


@dataclass(slots=True)
class CompilationMetrics:
    files_parsed: int = 0
    documents_parsed: int = 0
    artifacts_generated: int = 0
    warnings: int = 0
    errors: int = 0
    fatal_errors: int = 0
    compilation_duration: float = 0.0
    memory_usage: int | None = None


@dataclass(slots=True)
class CompilationResult:
    compilation_identifier: str
    compiler_version: str
    repository_identifier: str
    compilation_status: str

    execution_bundle: ExecutionBundle
    validation_report: ValidationReport

    diagnostics: list[Diagnostic] = field(default_factory=list)

    metrics: CompilationMetrics = field(
        default_factory=CompilationMetrics
    )

    metadata: dict[str, Any] = field(default_factory=dict)

    start_timestamp: str = ""
    end_timestamp: str = ""
    duration: float = 0.0

    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        self.diagnostics.append(diagnostic)

    @property
    def succeeded(self) -> bool:
        return self.compilation_status in (
            "Success",
            "Success With Warnings",
        )