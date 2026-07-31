from __future__ import annotations

import time
from pathlib import Path

from .generator import ArtifactGenerator
from .io import discover_specifications
from .models import (
    CompilationMetrics,
    CompilationResult,
)
from .optimizer import Optimizer
from .parser import Parser
from .semantic import SemanticAnalyzer
from .types import CompilationStatus
from .validator import Validator
from .version import VERSION


class Compiler:
    """
    FCOS Reference Compiler.

    Coordinates the complete FCOS compilation pipeline.
    """

    def __init__(self) -> None:
        self.parser = Parser()
        self.semantic = SemanticAnalyzer()
        self.optimizer = Optimizer()
        self.generator = ArtifactGenerator()
        self.validator = Validator()

    def compile(
        self,
        repository: Path,
    ) -> CompilationResult:
        """
        Compile an FCOS repository.
        """

        start_time = time.perf_counter()

        specification_files = discover_specifications(
            repository,
        )

        asts = self.parser.parse_repository(
            specification_files,
        )

        semantic_model = self.semantic.analyze_repository(
            asts,
        )

        optimized_model = self.optimizer.optimize(
            semantic_model,
        )

        execution_bundle = self.generator.generate(
            optimized_model,
        )

        validation_report = self.validator.validate(
            execution_bundle,
        )

        duration = time.perf_counter() - start_time

        metrics = CompilationMetrics(
            files_parsed=len(specification_files),
            documents_parsed=len(
                optimized_model.documents,
            ),
            artifacts_generated=len(
                execution_bundle.artifacts,
            ),
            warnings=sum(
                1
                for diagnostic in validation_report.diagnostics
                if diagnostic.severity.name == "WARNING"
            ),
            errors=sum(
                1
                for diagnostic in validation_report.diagnostics
                if diagnostic.severity.name == "ERROR"
            ),
            fatal_errors=sum(
                1
                for diagnostic in validation_report.diagnostics
                if diagnostic.severity.name == "FATAL"
            ),
            compilation_duration=duration,
        )

        status = (
            CompilationStatus.SUCCESS
            if metrics.errors == 0
            else CompilationStatus.FAILED
        )

        return CompilationResult(
            compilation_identifier="compile",
            compiler_version=VERSION,
            repository_identifier=str(repository),
            compilation_status=status.value,
            execution_bundle=execution_bundle,
            validation_report=validation_report,
            diagnostics=validation_report.diagnostics,
            metrics=metrics,
            duration=duration,
        )