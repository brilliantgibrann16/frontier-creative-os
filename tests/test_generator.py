from tools.compiler.fcos.generator import ArtifactGenerator
from tools.compiler.fcos.models import (
    SemanticDocument,
    SemanticModel,
)


def test_generator_creates_execution_bundle() -> None:
    model = SemanticModel(
        repository_identifier="repository",
        semantic_version="1.0.0",
    )

    document = SemanticDocument(
        identifier="DOC-001",
        version="1.0.0",
        classification="Specification",
        status="Stable",
    )

    model.documents.append(document)

    generator = ArtifactGenerator()

    bundle = generator.generate(model)

    assert bundle.bundle_identifier == "repository"

    assert len(bundle.artifacts) == 1

    artifact = bundle.artifacts[0]

    assert artifact.identifier == "DOC-001"
    assert artifact.version == "1.0.0"

    assert bundle.manifest["repository"] == "repository"