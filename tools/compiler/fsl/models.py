"""Immutable data models for the S05 Compiler Subsystem and S04 Stage 1 W-B."""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class DiagnosticCode(str, Enum):
    SYNTAX_ERROR = "SYNTAX_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    DEPENDENCY_ERROR = "DEPENDENCY_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class ValidationStatus(str, Enum):
    """Validation outcome status per S04#7.1."""

    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


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
class ValidationOutcome:
    """Explicit validation outcome model adhering to S04#7.1, S04#7.2, S04#7.4."""

    status: ValidationStatus
    is_structurally_valid: bool  # S04#6.1
    is_closure_valid: bool       # S04#6.2
    violated_clauses: list[str]  # S04#7.2
    diagnostics: list[Diagnostic]

    @property
    def is_accepted(self) -> bool:
        return self.status == ValidationStatus.ACCEPTED

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.value,
            "is_structurally_valid": self.is_structurally_valid,
            "is_closure_valid": self.is_closure_valid,
            "violated_clauses": self.violated_clauses,
            "diagnostics": [d.to_dict() for d in self.diagnostics],
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
    """Result of a compilation invocation adhering to S05#3.3 & S04#7.1."""

    success: bool
    diagnostics: list[Diagnostic]
    outcome: ValidationOutcome | None = None
    bundle: ExecutionBundle | None = None
