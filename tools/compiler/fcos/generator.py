from __future__ import annotations

from datetime import UTC, datetime

from .models import (
    Artifact,
    ExecutionBundle,
    SemanticModel,
)


class ArtifactGenerator:
    """
    FCOS Artifact Generator.

    Generates execution artifacts from semantic models.
    """

    VERSION = "1.0.0"

    def generate(
        self,
        model: SemanticModel,
    ) -> ExecutionBundle:

        bundle = ExecutionBundle(
            bundle_identifier=model.repository_identifier,
            bundle_version="1.0.0",
            compiler_version=self.VERSION,
            specification_version=model.semantic_version,
            creation_timestamp=datetime.now(
                UTC,
            ).isoformat(),
        )

        for document in model.documents:

            artifact = Artifact(
                identifier=document.identifier,
                name=document.identifier,
                artifact_type=document.classification
                or "Specification",
                version=document.version,
                output_path=f"build/{document.identifier}.json",
                target_platform="FCOS",
                content=self._serialize_document(
                    document,
                ),
            )

            bundle.add_artifact(
                artifact,
            )

        bundle.manifest = self._build_manifest(
            model,
        )

        bundle.build_metadata = {
            "documents": len(model.documents),
            "artifacts": len(bundle.artifacts),
            "generator_version": self.VERSION,
        }

        return bundle

    def _serialize_document(
        self,
        document,
    ) -> str:

        return (
            f"Identifier: {document.identifier}\n"
            f"Version: {document.version}\n"
            f"Status: {document.status}\n"
            f"Classification: {document.classification}\n"
        )

    def _build_manifest(
        self,
        model: SemanticModel,
    ) -> dict:

        return {
            "repository": model.repository_identifier,
            "semantic_version": model.semantic_version,
            "documents": [
                document.identifier
                for document in model.documents
            ],
        }