"""Immutable data models for the S05 Compiler Subsystem."""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class DiagnosticCode(str, Enum):
    SYNTAX_ERROR = "SYNTAX_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    DEPENDENCY_ERROR = "DEPENDENCY_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"


@dataclass(frozen=True)
class Diagnostic:
    """Represents a compiler diagnostic adhering to S05#2.2."""

    code: DiagnosticCode
    clause_id: str | None
    message: str
    path: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code.value,
            "clause_id": self.clause_id,
            "message": self.message,
            "path": self.path,
        }


@dataclass(frozen=True)
class ExecutionBundle:
    """Represents a Stage 1 execution bundle adhering to S05#4.2."""

    bundle_version: str
    compiler_version: str
    artifact: dict[str, Any]
    resolved_dependencies: list[str]
    compilation_timestamp_utc: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "bundle_version": self.bundle_version,
            "compiler_version": self.compiler_version,
            "artifact": self.artifact,
            "resolved_dependencies": self.resolved_dependencies,
            "compilation_timestamp_utc": self.compilation_timestamp_utc,
        }


@dataclass(frozen=True)
class CompilationResult:
    """Result of a compilation invocation adhering to S05#3.3."""

    success: bool
    diagnostics: list[Diagnostic]
    bundle: ExecutionBundle | None = None
