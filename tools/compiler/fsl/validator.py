"""S04 Stage 1 W-B schema and semantic boundary validator."""

import re
from typing import Any

from tools.compiler.fsl.models import Diagnostic, DiagnosticCode

_IDENTIFIER_PATTERN = re.compile(r"^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*$")


def validate_artifact(data: dict[str, Any]) -> list[Diagnostic]:
    """Validate FSL artifact against ratified S04 Stage 1 W-B clauses."""
    diagnostics: list[Diagnostic] = []

    # S05#1.2 / S04#8.3: Schema version validation
    schema_version = data.get("schema_version")
    if schema_version != "fsl/1.0":
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message=f"Expected schema_version 'fsl/1.0', got '{schema_version}'.",
                path="schema_version",
            )
        )

    # S04#5.1: Top-level artifact model keys
    manifest = data.get("manifest")
    if manifest is None:
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#5.1",
                message="Missing required top-level 'manifest' object.",
                path="manifest",
            )
        )
    elif not isinstance(manifest, dict):
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#5.1",
                message="Top-level 'manifest' must be an object.",
                path="manifest",
            )
        )
    else:
        # S04#6.1: Manifest identity
        name = manifest.get("name")
        if not name or not isinstance(name, str) or not _IDENTIFIER_PATTERN.match(name):
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.1",
                    message="Manifest 'name' must be a non-empty alphanumeric/dot-separated identifier string.",
                    path="manifest.name",
                )
            )

        # S04#6.2: Manifest version
        version = manifest.get("version")
        if not version or not isinstance(version, str):
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Manifest 'version' must be a valid non-empty string.",
                    path="manifest.version",
                )
            )

    return diagnostics
