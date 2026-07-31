from __future__ import annotations

from .models import (
    ASTNode,
    AbstractSyntaxTree,
    Dependency,
    SemanticDocument,
    SemanticModel,
)


class SemanticAnalyzer:
    """
    FCOS Semantic Analyzer.

    Converts Abstract Syntax Trees into Semantic Models.
    """

    VERSION = "1.0.0"

    def analyze(
        self,
        ast: AbstractSyntaxTree,
    ) -> SemanticModel:

        root = ast.root

        document = SemanticDocument(
            identifier=root.metadata.get(
                "id",
                ast.document_identifier,
            ),
            version=root.metadata.get(
                "version",
                "1.0.0",
            ),
            classification=root.metadata.get(
                "classification",
                "",
            ),
            status=root.metadata.get(
                "status",
                "",
            ),
            metadata=root.metadata,
        )

        model = SemanticModel(
            repository_identifier=ast.document_identifier,
            semantic_version=self.VERSION,
        )

        self._collect_dependencies(
            root,
            document,
        )

        model.add_document(document)

        return model

    def analyze_repository(
        self,
        trees: list[AbstractSyntaxTree],
    ) -> SemanticModel:

        model = SemanticModel(
            repository_identifier="repository",
            semantic_version=self.VERSION,
        )

        for tree in trees:

            partial = self.analyze(tree)

            model.documents.extend(
                partial.documents,
            )

            model.diagnostics.extend(
                partial.diagnostics,
            )

        return model

    def _collect_dependencies(
        self,
        node: ASTNode,
        document: SemanticDocument,
    ) -> None:

        dependencies = node.metadata.get(
            "dependencies",
        )

        if isinstance(
            dependencies,
            str,
        ):

            for value in dependencies.split(","):

                value = value.strip()

                if not value:
                    continue

                document.dependencies.append(
                    Dependency(
                        source=document.identifier,
                        target=value,
                        relationship="reference",
                    )
                )

        for child in node.children:

            self._collect_dependencies(
                child,
                document,
            )