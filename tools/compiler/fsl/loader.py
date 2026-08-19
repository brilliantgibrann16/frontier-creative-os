"""Input loader adhering to S05#1.1–S05#1.3."""

import json
from typing import Any

from tools.compiler.fsl.models import Diagnostic, DiagnosticCode


class DuplicateKeyCheckingDecoder(json.JSONDecoder):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(object_pairs_hook=self._check_duplicate_keys, *args, **kwargs)

    @staticmethod
    def _check_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate key encountered in JSON object: '{key}'")
            result[key] = value
        return result


def load_source_json(raw_text: str) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    """Parse UTF-8 JSON text strictly adhering to RFC 8259 and reject duplicate keys (S05#1.1, S05#1.3)."""
    try:
        data = json.loads(raw_text, cls=DuplicateKeyCheckingDecoder)
        if not isinstance(data, dict):
            return None, [
                Diagnostic(
                    code=DiagnosticCode.SYNTAX_ERROR,
                    clause_id="S04#8.3",
                    message="Top-level FSL artifact must be a JSON object.",
                    path="",
                )
            ]
        return data, []
    except json.JSONDecodeError as exc:
        return None, [
            Diagnostic(
                code=DiagnosticCode.SYNTAX_ERROR,
                clause_id="S04#8.3",
                message=f"Invalid JSON syntax: {exc.msg} at line {exc.lineno} column {exc.colno}",
                path="",
            )
        ]
    except ValueError as exc:
        return None, [
            Diagnostic(
                code=DiagnosticCode.SYNTAX_ERROR,
                clause_id="S04#8.3",
                message=str(exc),
                path="",
            )
        ]
