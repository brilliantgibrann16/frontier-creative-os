from __future__ import annotations

from .models import (
    Diagnostic,
    DiagnosticSeverity,
    ExecutionBundle,
    QualityGateResult,
    ValidationReport,
)


class Validator:
    """
    FCOS Execution Bundle Validator.
    """

    VERSION = "1.0.0"

    def validate(
        self,
        bundle: ExecutionBundle,
    ) -> ValidationReport:

        report = ValidationReport(
            report_identifier=bundle.bundle_identifier,
            compiler_version=bundle.compiler_version,
            validation_timestamp=bundle.creation_timestamp,
        )

        self._validate_artifacts(
            bundle,
            report,
        )

        self._validate_manifest(
            bundle,
            report,
        )

        if report.diagnostics:
            report.release_status = "Failed"

        return report

    def _validate_artifacts(
        self,
        bundle: ExecutionBundle,
        report: ValidationReport,
    ) -> None:

        passed = True

        if not bundle.artifacts:
            passed = False

            report.add_diagnostic(
                Diagnostic(
                    identifier="VAL001",
                    severity=DiagnosticSeverity.ERROR,
                    message="Execution bundle contains no artifacts.",
                )
            )

        report.add_quality_gate(
            QualityGateResult(
                name="Artifacts",
                passed=passed,
            )
        )

    def _validate_manifest(
        self,
        bundle: ExecutionBundle,
        report: ValidationReport,
    ) -> None:

        passed = True

        if not bundle.manifest:
            passed = False

            report.add_diagnostic(
                Diagnostic(
                    identifier="VAL002",
                    severity=DiagnosticSeverity.ERROR,
                    message="Manifest is missing.",
                )
            )

        report.add_quality_gate(
            QualityGateResult(
                name="Manifest",
                passed=passed,
            )
        )