"""CLI entry point adhering to S05#3.1–S05#3.2."""

import argparse
import json
import sys
from pathlib import Path

from tools.compiler.fsl.api import compile_artifact


def main(argv: list[str] | None = None) -> int:
    """Run the fcos-compile CLI interface adhering to S05#3.1–S05#3.2."""
    parser = argparse.ArgumentParser(
        prog="fcos-compile",
        description="FSL Stage 1 Boundary Compiler (S05 conforming).",
    )
    parser.add_argument("input", help="Path to input FSL JSON artifact.")
    parser.add_argument("--out", "-o", help="Optional path to output execution bundle JSON.")
    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="Diagnostic output format (default: json).",
    )

    args = parser.parse_args(argv)

    input_path = Path(args.input)
    if not input_path.exists() or not input_path.is_file():
        if args.format == "json":
            print(
                json.dumps(
                    [
                        {
                            "code": "INTERNAL_ERROR",
                            "clause_id": None,
                            "message": f"Input file not found or inaccessible: {args.input}",
                            "path": "",
                        }
                    ],
                    indent=2,
                ),
                file=sys.stderr,
            )
        else:
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        return 2  # S05#3.2 Invocation / CLI usage error

    try:
        raw_text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        if args.format == "json":
            print(
                json.dumps(
                    [
                        {
                            "code": "SYNTAX_ERROR",
                            "clause_id": "S05#1.1",
                            "message": f"Input file is not valid UTF-8: {exc}",
                            "path": "",
                        }
                    ],
                    indent=2,
                ),
                file=sys.stderr,
            )
        else:
            print(f"Error: Input file is not valid UTF-8: {exc}", file=sys.stderr)
        return 1  # S05#3.2 Input validation failure

    try:
        result = compile_artifact(raw_text)
    except Exception as exc:
        if args.format == "json":
            print(
                json.dumps(
                    [
                        {
                            "code": "INTERNAL_ERROR",
                            "clause_id": None,
                            "message": f"Internal compiler fault: {exc}",
                            "path": "",
                        }
                    ],
                    indent=2,
                ),
                file=sys.stderr,
            )
        else:
            print(f"Internal compiler fault: {exc}", file=sys.stderr)
        return 3  # S05#3.2 Internal unhandled fault

    if not result.success:
        if args.format == "json":
            print(
                json.dumps([d.to_dict() for d in result.diagnostics], indent=2),
                file=sys.stderr,
            )
        else:
            for diag in result.diagnostics:
                clause_str = f" [{diag.clause_id}]" if diag.clause_id else ""
                print(
                    f"{diag.code.value}{clause_str}: {diag.message} at '{diag.path}'",
                    file=sys.stderr,
                )
        return 1  # S05#3.2 Specification / validation failure

    assert result.bundle is not None
    bundle_json = json.dumps(result.bundle.to_dict(), indent=2)

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(bundle_json + "\n", encoding="utf-8")
    else:
        print(bundle_json)

    return 0  # S05#3.2 Success


if __name__ == "__main__":
    sys.exit(main())
