from __future__ import annotations

from dataclasses import dataclass, field

from .diagnostic import Diagnostic


@dataclass(slots=True)
class QualityGateResult:
    name: str
    passed: bool
    message: str = ""


@dataclass(slots=True)
class ValidationReport:
    report_identifier: str
    compiler_version: str
    validation_timestamp: str

    quality_gates: list[QualityGateResult] = field(default_factory=list)

    diagnostics: list[Diagnostic] = field(default_factory=list)

    release_status: str = "Passed"

    metadata: dict[str, str] = field(default_factory=dict)

    def add_quality_gate(self, gate: QualityGateResult) -> None:
        self.quality_gates.append(gate)

    def add_diagnostic(self, diagnostic: Diagnostic) -> None:
        self.diagnostics.append(diagnostic)

    @property
    def passed(self) -> bool:
        return self.release_status in (
            "Passed",
            "Passed With Warnings",
        )