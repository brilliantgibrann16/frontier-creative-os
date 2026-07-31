from pathlib import Path

from tools.compiler.fcos.compiler import Compiler


def test_compiler_pipeline(tmp_path: Path) -> None:
    specs = tmp_path / "specs"
    specs.mkdir()

    specification = specs / "example.md"

    specification.write_text(
        """---
id: SPEC-001
version: 1.0.0
classification: Specification
status: Stable
---

# Example

Compiler pipeline test.
""",
        encoding="utf-8",
    )

    compiler = Compiler()

    result = compiler.compile(tmp_path)

    assert result.compilation_status == "Success"

    assert result.metrics.files_parsed == 1
    assert result.metrics.documents_parsed == 1
    assert result.metrics.artifacts_generated == 1

    assert result.validation_report.release_status == "Passed"

    assert len(result.execution_bundle.artifacts) == 1