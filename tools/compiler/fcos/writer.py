from __future__ import annotations

import json
from pathlib import Path

from .models import ExecutionBundle


class BundleWriter:
    """
    Serialize compiler output.
    """

    def write(
        self,
        bundle: ExecutionBundle,
        output_directory: Path,
    ) -> None:

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        manifest = output_directory / "manifest.json"

        manifest.write_text(
            json.dumps(
                bundle.manifest,
                indent=2,
            ),
            encoding="utf-8",
        )