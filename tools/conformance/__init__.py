"""S13 Conformance Test Harness package.

Adheres strictly to ratified specification S13 (ADR-0015):
- S13#1.1: Sole judge authority
- S13#1.2: Binary conformance model
- S13#1.3: Clause totality
- S13#2.1: Black-box invocation boundary
- S13#2.2: Standard harness interface
- S13#2.3: Deterministic harness execution
- S13#2.4: Reproducible test reporting
- S13#3.1–S13#3.4: Clause-traced fixtures
- S13#4.1–S13#4.4: Self-certification claim regime
"""

from tools.conformance.models import (
    ClauseEvaluation,
    ConformanceClaim,
    ConformanceEvaluationReport,
    EvaluationVerdict,
    FixtureEvaluationResult,
    FixtureType,
    TestCaseFixture,
)
from tools.conformance.runner import ConformanceHarness

__all__ = [
    "ConformanceHarness",
    "TestCaseFixture",
    "FixtureType",
    "FixtureEvaluationResult",
    "ClauseEvaluation",
    "ConformanceEvaluationReport",
    "ConformanceClaim",
    "EvaluationVerdict",
]
