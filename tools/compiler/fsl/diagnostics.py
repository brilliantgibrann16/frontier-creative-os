"""Diagnostic sorting and engine utilities adhering to S05#2.1–S05#2.4."""

from tools.compiler.fsl.models import Diagnostic


def sort_diagnostics(diagnostics: list[Diagnostic]) -> list[Diagnostic]:
    """Sort diagnostics deterministically by JSON path, then by clause ID (S05#2.3)."""
    return sorted(
        diagnostics,
        key=lambda d: (d.path, d.clause_id or "", d.code.value, d.message),
    )
