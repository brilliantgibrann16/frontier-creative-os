"""Programmatic API interface adhering to S05#3.3."""

from typing import Any

from tools.compiler.fsl.diagnostics import sort_diagnostics
from tools.compiler.fsl.emitter import emit_execution_bundle
from tools.compiler.fsl.loader import load_source_json
from tools.compiler.fsl.models import CompilationResult
from tools.compiler.fsl.validator import validate_artifact


def compile_artifact(
    source_data: dict[str, Any] | str,
    options: dict[str, Any] | None = None,
) -> CompilationResult:
    """Compile and validate an FSL source artifact under the S05 boundary contract (S05#3.3)."""
    options = options or {}
    compiler_version = options.get("compiler_version", "0.1.0")
    timestamp = options.get("timestamp_utc", "1970-01-01T00:00:00Z")

    if isinstance(source_data, str):
        artifact, load_diags = load_source_json(source_data)
        if load_diags:
            return CompilationResult(
                success=False,
                diagnostics=sort_diagnostics(load_diags),
                bundle=None,
            )
    elif isinstance(source_data, dict):
        artifact = source_data
    else:
        from tools.compiler.fsl.models import Diagnostic, DiagnosticCode

        return CompilationResult(
            success=False,
            diagnostics=[
                Diagnostic(
                    code=DiagnosticCode.SYNTAX_ERROR,
                    clause_id="S04#8.3",
                    message="Source data must be a JSON string or dict object.",
                    path="",
                )
            ],
            bundle=None,
        )

    assert artifact is not None
    validation_diags = validate_artifact(artifact)
    if validation_diags:
        return CompilationResult(
            success=False,
            diagnostics=sort_diagnostics(validation_diags),
            bundle=None,
        )

    bundle = emit_execution_bundle(
        artifact=artifact,
        compiler_version=compiler_version,
        compilation_timestamp_utc=timestamp,
    )
    return CompilationResult(success=True, diagnostics=[], bundle=bundle)
