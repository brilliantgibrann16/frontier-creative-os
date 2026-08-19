"""S04 Stage 1 W-B schema and semantic boundary validator adhering to S04#5.1–S04#8.3 and S05#2.1–S05#2.4."""

from typing import Any

from tools.compiler.fsl.models import Diagnostic, DiagnosticCode


def validate_artifact(data: dict[str, Any]) -> list[Diagnostic]:
    """Validate FSL artifact against ratified S04 Stage 1 W-B clauses and S05 boundary requirements."""
    diagnostics: list[Diagnostic] = []

    # S05#1.2 & S04#8.3: Schema version validation
    schema_version = data.get("schema_version")
    if schema_version is None:
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message="Missing required top-level 'schema_version' field.",
                path="schema_version",
            )
        )
    elif schema_version != "fsl/1.0":
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message=f"Expected schema_version 'fsl/1.0', got '{schema_version}'.",
                path="schema_version",
            )
        )

    # S04#5.1 & S04#6.1: Top-level artifact model keys (single artifact unit)
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
                message="Top-level 'manifest' must be a JSON object.",
                path="manifest",
            )
        )
    else:
        # S04#6.1: Structural validity of manifest identity
        name = manifest.get("name")
        if name is None:
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.1",
                    message="Missing required manifest field 'name'.",
                    path="manifest.name",
                )
            )
        elif not isinstance(name, str) or not name.strip():
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.1",
                    message="Manifest 'name' must be a non-empty string.",
                    path="manifest.name",
                )
            )

        # S04#6.2: Validity closure of manifest version
        version = manifest.get("version")
        if version is None:
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Missing required manifest field 'version'.",
                    path="manifest.version",
                )
            )
        elif not isinstance(version, str) or not version.strip():
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Manifest 'version' must be a non-empty string.",
                    path="manifest.version",
                )
            )

        # S04#5.2: Stage 1 self-containment - validate dependencies list if provided
        dependencies = manifest.get("dependencies")
        if dependencies is not None:
            if not isinstance(dependencies, list):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#5.2",
                        message="Manifest 'dependencies' must be a JSON list.",
                        path="manifest.dependencies",
                    )
                )
            else:
                for idx, dep in enumerate(dependencies):
                    if not isinstance(dep, str) or not dep.strip():
                        diagnostics.append(
                            Diagnostic(
                                code=DiagnosticCode.VALIDATION_ERROR,
                                clause_id="S04#5.2",
                                message=f"Dependency at index {idx} must be a non-empty string identifier.",
                                path=f"manifest.dependencies[{idx}]",
                            )
                        )

    return diagnostics
