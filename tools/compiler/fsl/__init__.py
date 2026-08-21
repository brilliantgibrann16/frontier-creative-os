"""FSL Compiler Package (Conforming to S04 Stage 1 & Stage 2 S2-B, and S05).

Quarantine Policy:
This package derives strictly from ratified specifications S04 and S05 (ADR-0013, ADR-0014, ADR-0016).
It is strictly isolated from the historical Phase 0 prototype in tools.compiler.fcos (L-7/INV-7).
"""

from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.expressions import (
    evaluate_declarative_invariants,
    evaluate_static_expression,
)
from tools.compiler.fsl.models import (
    CompilationResult,
    Diagnostic,
    DiagnosticCode,
    ExecutionBundle,
    ValidationOutcome,
    ValidationStatus,
)
from tools.compiler.fsl.types import (
    CompoundType,
    ScalarType,
    validate_type_annotation,
    validate_value_conformance,
)

__all__ = [
    "CompilationResult",
    "CompoundType",
    "Diagnostic",
    "DiagnosticCode",
    "ExecutionBundle",
    "ScalarType",
    "ValidationOutcome",
    "ValidationStatus",
    "compile_artifact",
    "evaluate_declarative_invariants",
    "evaluate_static_expression",
    "validate_type_annotation",
    "validate_value_conformance",
]

__version__ = "0.1.0"
