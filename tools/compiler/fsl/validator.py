"""S04 Stage 1 W-B schema and semantic boundary validator adhering to S04#5.1–S04#8.3 and S05#2.1–S05#2.4."""

from typing import Any

from tools.compiler.fsl.diagnostics import sort_diagnostics
from tools.compiler.fsl.models import (
    Diagnostic,
    DiagnosticCode,
    ValidationOutcome,
    ValidationStatus,
)


def evaluate_artifact_validity(data: dict[str, Any]) -> ValidationOutcome:
    """Evaluate structural validity (S04#6.1), validity closure (S04#6.2), and outcome (S04#7.1)."""
    diagnostics: list[Diagnostic] = []
    is_structurally_valid = True
    is_closure_valid = True

    # S04#8.1, S04#8.2, S04#8.3, S05#1.2: Schema version validation (Interchange Form)
    schema_version = data.get("schema_version")
    if schema_version is None:
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message="Missing required top-level 'schema_version' field.",
                path="schema_version",
            )
        )
    elif schema_version != "fsl/1.0":
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#8.3",
                message=f"Expected schema_version 'fsl/1.0', got '{schema_version}'.",
                path="schema_version",
            )
        )

    # S04#5.1 & S04#6.1: Single Artifact Unit & Top-level manifest structure
    manifest = data.get("manifest")
    if manifest is None:
        is_structurally_valid = False
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#5.1",
                message="Missing required top-level 'manifest' object.",
                path="manifest",
            )
        )
    elif not isinstance(manifest, dict):
        is_structurally_valid = False
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
            is_structurally_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.1",
                    message="Missing required manifest field 'name'.",
                    path="manifest.name",
                )
            )
        elif not isinstance(name, str) or not name.strip():
            is_structurally_valid = False
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
            is_closure_valid = False
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#6.2",
                    message="Missing required manifest field 'version'.",
                    path="manifest.version",
                )
            )
        elif not isinstance(version, str) or not version.strip():
            is_closure_valid = False
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
                is_closure_valid = False
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
                        is_closure_valid = False
                        diagnostics.append(
                            Diagnostic(
                                code=DiagnosticCode.VALIDATION_ERROR,
                                clause_id="S04#5.2",
                                message=f"Dependency at index {idx} must be a non-empty string identifier.",
                                path=f"manifest.dependencies[{idx}]",
                            )
                        )

    sorted_diags = sort_diagnostics(diagnostics)
    # S04#7.2: Violated-clause identification (unique and ordered)
    violated_clauses: list[str] = sorted(list({d.clause_id for d in sorted_diags if d.clause_id}))

    status = (
        ValidationStatus.ACCEPTED
        if is_structurally_valid and is_closure_valid and not sorted_diags
        else ValidationStatus.REJECTED
    )

    return ValidationOutcome(
        status=status,
        is_structurally_valid=is_structurally_valid,
        is_closure_valid=is_closure_valid and is_structurally_valid,
        violated_clauses=violated_clauses,
        diagnostics=sorted_diags,
    )


def validate_artifact(data: dict[str, Any]) -> list[Diagnostic]:
    """Compatibility wrapper returning list of diagnostics."""
    return evaluate_artifact_validity(data).diagnostics
