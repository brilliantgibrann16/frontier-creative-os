"""
FCOS Compiler Domain Models.

This package contains the canonical domain models used
throughout the FCOS compiler implementation.
"""

from .artifact import Artifact
from .ast import ASTNode, AbstractSyntaxTree
from .compilation_result import CompilationMetrics, CompilationResult
from .diagnostic import (
    Diagnostic,
    DiagnosticSeverity,
    SourceLocation,
)
from .execution_bundle import ExecutionBundle
from .semantic import (
    Dependency,
    SemanticDocument,
    SemanticModel,
)
from .validation import (
    QualityGateResult,
    ValidationReport,
)

__all__ = [
    "Artifact",
    "ASTNode",
    "AbstractSyntaxTree",
    "CompilationMetrics",
    "CompilationResult",
    "Dependency",
    "Diagnostic",
    "DiagnosticSeverity",
    "ExecutionBundle",
    "QualityGateResult",
    "SemanticDocument",
    "SemanticModel",
    "SourceLocation",
    "ValidationReport",
]