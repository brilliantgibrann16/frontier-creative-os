from tools.compiler.fcos.models import (
    Dependency,
    SemanticDocument,
    SemanticModel,
)
from tools.compiler.fcos.optimizer import Optimizer


def test_optimizer_deduplicates_dependencies() -> None:
    model = SemanticModel(
        repository_identifier="repo",
    )

    document = SemanticDocument(
        identifier="DOC-001",
        version="1.0.0",
        classification="Specification",
        status="Stable",
    )

    dependency = Dependency(
        source="DOC-001",
        target="DOC-002",
        relationship="reference",
    )

    document.dependencies.extend(
        [
            dependency,
            dependency,
        ]
    )

    model.documents.append(document)

    optimizer = Optimizer()

    optimized = optimizer.optimize(model)

    assert len(
        optimized.documents[0].dependencies
    ) == 1