from pathlib import Path

from tools.compiler.fcos.parser import Parser


def test_parser_can_parse_single_document(tmp_path: Path) -> None:
    specification = tmp_path / "sample.md"

    specification.write_text(
        """---
id: TEST-001
version: 1.0.0
---

# Sample

Hello FCOS.
""",
        encoding="utf-8",
    )

    parser = Parser()

    ast = parser.parse(specification)

    assert ast.document_identifier == "sample"
    assert ast.root.metadata["id"] == "TEST-001"
    assert len(ast.root.children) == 1