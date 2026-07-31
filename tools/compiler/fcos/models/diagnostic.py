from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class DiagnosticSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal"


@dataclass(slots=True)
class SourceLocation:
    file: str
    line: int
    column: int


@dataclass(slots=True)
class Diagnostic:
    identifier: str
    severity: DiagnosticSeverity
    message: str
    location: Optional[SourceLocation] = None
    recommendation: Optional[str] = None