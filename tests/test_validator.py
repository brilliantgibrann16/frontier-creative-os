from tools.compiler.fcos.models import ExecutionBundle
from tools.compiler.fcos.validator import Validator


def test_validator_accepts_valid_bundle() -> None:
    bundle = ExecutionBundle(
        bundle_identifier="bundle",
        bundle_version="1.0.0",
        compiler_version="1.0.0",
        specification_version="1.0.0",
    )

    bundle.manifest = {
        "repository": "repository",
    }

    bundle.artifacts.append(
        object()
    )

    validator = Validator()

    report = validator.validate(bundle)

    assert report.release_status == "Passed"

    assert len(report.diagnostics) == 0

    assert len(report.quality_gates) == 2