"""FSL Stage 1 Compiler Package (Conforming to S04/S05).

Quarantine Policy:
This package derives strictly from ratified specifications S04 and S05 (ADR-0013, ADR-0014).
It is strictly isolated from the historical Phase 0 prototype in tools.compiler.fcos (L-7/INV-7).
"""

from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.models import (
    CompilationResult,
    Diagnostic,
    DiagnosticCode,
    ExecutionBundle,
    ValidationOutcome,
    ValidationStatus,
)

__all__ = [
    "CompilationResult",
    "Diagnostic",
    "DiagnosticCode",
    "ExecutionBundle",
    "ValidationOutcome",
    "ValidationStatus",
    "compile_artifact",
]

__version__ = "0.1.0"
