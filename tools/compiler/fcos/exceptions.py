from __future__ import annotations


class FCOSCompilerError(Exception):
    """Base exception for all FCOS compiler errors."""


class ParserError(FCOSCompilerError):
    """Raised when parsing fails."""


class SemanticError(FCOSCompilerError):
    """Raised when semantic analysis fails."""


class OptimizationError(FCOSCompilerError):
    """Raised when optimization fails."""


class GenerationError(FCOSCompilerError):
    """Raised when artifact generation fails."""


class ValidationError(FCOSCompilerError):
    """Raised when validation fails."""