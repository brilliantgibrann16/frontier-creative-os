"""Stage 1 Execution Bundle emitter adhering to S05#4.1–S05#4.3."""

from typing import Any

from tools.compiler.fsl.models import ExecutionBundle


def emit_execution_bundle(
    artifact: dict[str, Any],
    compiler_version: str = "0.1.0",
    compilation_timestamp_utc: str = "1970-01-01T00:00:00Z",
) -> ExecutionBundle:
    """Emit a deterministic ExecutionBundle conforming to S05#4.1–S05#4.3."""
    # Extract dependencies deterministically
    dependencies = []
    manifest = artifact.get("manifest", {})
    if isinstance(manifest, dict):
        deps = manifest.get("dependencies", [])
        if isinstance(deps, list):
            dependencies = sorted([str(d) for d in deps if isinstance(d, str)])

    return ExecutionBundle(
        bundle_version="1.0.0",
        compiler_version=compiler_version,
        artifact=artifact,
        resolved_dependencies=dependencies,
        compilation_timestamp_utc=compilation_timestamp_utc,
    )
