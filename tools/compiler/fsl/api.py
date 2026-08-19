"""Programmatic API interface adhering to S05#3.3 & S04#7.1–S04#7.6."""

from typing import Any

from tools.compiler.fsl.diagnostics import sort_diagnostics
from tools.compiler.fsl.emitter import emit_execution_bundle
from tools.compiler.fsl.loader import load_source_json
from tools.compiler.fsl.models import (
    CompilationResult,
    Diagnostic,
    DiagnosticCode,
    ValidationOutcome,
    ValidationStatus,
)
from tools.compiler.fsl.validator import evaluate_artifact_validity


def compile_artifact(
    source_data: dict[str, Any] | str,
    options: dict[str, Any] | None = None,
) -> CompilationResult:
    """Compile and validate an FSL source artifact under S04 Stage 1 W-B and S05 boundary contracts."""
    options = options or {}
    compiler_version = options.get("compiler_version", "0.1.0")
    timestamp = options.get("timestamp_utc", "1970-01-01T00:00:00Z")

    if isinstance(source_data, str):
        artifact, load_diags = load_source_json(source_data)
        if load_diags:
            sorted_diags = sort_diagnostics(load_diags)
            violated = sorted(list({d.clause_id for d in sorted_diags if d.clause_id}))
            outcome = ValidationOutcome(
                status=ValidationStatus.REJECTED,
                is_structurally_valid=False,
                is_closure_valid=False,
                violated_clauses=violated,
                diagnostics=sorted_diags,
            )
            return CompilationResult(
                success=False,
                diagnostics=sorted_diags,
                outcome=outcome,
                bundle=None,
            )
    elif isinstance(source_data, dict):
        artifact = source_data
    else:
        diag = Diagnostic(
            code=DiagnosticCode.SYNTAX_ERROR,
            clause_id="S04#8.3",
            message="Source data must be a JSON string or dict object.",
            path="",
        )
        outcome = ValidationOutcome(
            status=ValidationStatus.REJECTED,
            is_structurally_valid=False,
            is_closure_valid=False,
            violated_clauses=["S04#8.3"],
            diagnostics=[diag],
        )
        return CompilationResult(
            success=False,
            diagnostics=[diag],
            outcome=outcome,
            bundle=None,
        )

    assert artifact is not None
    outcome = evaluate_artifact_validity(artifact)
    if not outcome.is_accepted:
        return CompilationResult(
            success=False,
            diagnostics=outcome.diagnostics,
            outcome=outcome,
            bundle=None,
        )

    bundle = emit_execution_bundle(
        artifact=artifact,
        compiler_version=compiler_version,
        compilation_timestamp_utc=timestamp,
    )
    return CompilationResult(
        success=True,
        diagnostics=[],
        outcome=outcome,
        bundle=bundle,
    )
