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


class Compiler:
    """
    FCOS Reference Compiler.
    """

    VERSION = "1.0.0"

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

        start = time.perf_counter()

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

        bundle = self.generator.generate(
            optimized_model,
        )

        validation = self.validator.validate(
            bundle,
        )

        duration = time.perf_counter() - start

        metrics = CompilationMetrics(
            files_parsed=len(specification_files),
            documents_parsed=len(optimized_model.documents),
            artifacts_generated=len(bundle.artifacts),
            warnings=sum(
                1
                for diagnostic in validation.diagnostics
                if diagnostic.severity.name == "WARNING"
            ),
            errors=sum(
                1
                for diagnostic in validation.diagnostics
                if diagnostic.severity.name == "ERROR"
            ),
            fatal_errors=sum(
                1
                for diagnostic in validation.diagnostics
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
            compiler_version=self.VERSION,
            repository_identifier=str(repository),
            compilation_status=status.value,
            execution_bundle=bundle,
            validation_report=validation,
            diagnostics=validation.diagnostics,
            metrics=metrics,
            duration=duration,
        )