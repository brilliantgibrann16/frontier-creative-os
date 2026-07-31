from __future__ import annotations

from enum import Enum


class CompilationStatus(str, Enum):
    SUCCESS = "Success"
    SUCCESS_WITH_WARNINGS = "Success With Warnings"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    INTERNAL_ERROR = "Internal Error"


class ReleaseStatus(str, Enum):
    PASSED = "Passed"
    PASSED_WITH_WARNINGS = "Passed With Warnings"
    FAILED = "Failed"
    BLOCKED = "Blocked"


class ArtifactType(str, Enum):
    BOOTSTRAP = "Bootstrap"
    MASTER_PROMPT = "Master Prompt"
    REVIEW_PROMPT = "Review Prompt"
    REFACTOR_PROMPT = "Refactor Prompt"
    ITERATION_PROMPT = "Iteration Prompt"
    REPOSITORY_PLAYBOOK = "Repository Playbook"
    EXECUTION_MANIFEST = "Execution Manifest"