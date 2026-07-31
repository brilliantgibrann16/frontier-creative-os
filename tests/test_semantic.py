from pathlib import Path

from tools.compiler.fcos.parser import Parser
from tools.compiler.fcos.semantic import SemanticAnalyzer


def test_semantic_analysis_creates_document(tmp_path: Path) -> None:
    specification = tmp_path / "semantic.md"

    specification.write_text(
        """---
id: DOC-001
version: 1.0.0
classification: Specification
status: Stable
---

# Semantic
""",
        encoding="utf-8",
    )

    parser = Parser()
    analyzer = SemanticAnalyzer()

    ast = parser.parse(specification)

    model = analyzer.analyze(ast)

    assert len(model.documents) == 1

    document = model.documents[0]

    assert document.identifier == "DOC-001"
    assert document.version == "1.0.0"
    assert document.classification == "Specification"
    assert document.status == "Stable"