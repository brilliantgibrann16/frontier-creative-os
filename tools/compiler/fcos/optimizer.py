from __future__ import annotations

from .models import SemanticModel


class Optimizer:
    """
    FCOS Semantic Model Optimizer.
    """

    VERSION = "1.0.0"

    def optimize(
        self,
        model: SemanticModel,
    ) -> SemanticModel:
        """
        Optimize a semantic model.
        """

        self._sort_documents(model)

        self._deduplicate_dependencies(model)

        return model

    def _sort_documents(
        self,
        model: SemanticModel,
    ) -> None:
        model.documents.sort(
            key=lambda document: document.identifier,
        )

    def _deduplicate_dependencies(
        self,
        model: SemanticModel,
    ) -> None:

        for document in model.documents:

            seen: set[tuple[str, str, str]] = set()

            unique = []

            for dependency in document.dependencies:

                key = (
                    dependency.source,
                    dependency.target,
                    dependency.relationship,
                )

                if key in seen:
                    continue

                seen.add(key)

                unique.append(dependency)

            document.dependencies = unique