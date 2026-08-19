"""Stage 1 Execution Bundle emitter adhering to S05#4.1–S05#4.3 and S04 Stage 1 W-B."""

import json
from typing import Any

from tools.compiler.fsl.models import ExecutionBundle


def emit_execution_bundle(
    artifact: dict[str, Any],
    compiler_version: str = "0.1.0",
    compilation_timestamp_utc: str = "1970-01-01T00:00:00Z",
) -> ExecutionBundle:
    """Emit a deterministic ExecutionBundle conforming to S05#4.1–S05#4.3."""
    dependencies = []
    manifest = artifact.get("manifest", {})
    if isinstance(manifest, dict):
        deps = manifest.get("dependencies", [])
        if isinstance(deps, list):
            dependencies = sorted([str(d) for d in deps if isinstance(d, str)])

    # Canonicalize artifact dictionary structure for deterministic serialization
    canonical_artifact = json.loads(json.dumps(artifact, sort_keys=True))

    return ExecutionBundle(
        bundle_version="1.0.0",
        compiler_version=compiler_version,
        artifact=canonical_artifact,
        resolved_dependencies=dependencies,
        compilation_timestamp_utc=compilation_timestamp_utc,
    )
