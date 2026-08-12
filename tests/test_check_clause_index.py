"""Fixture tests for tools/checks/check_clause_index.py (clause-index drift checker)."""

import subprocess
import sys
from pathlib import Path

from tools.checks.check_clause_index import collect_errors

SPEC_REL = "specs/S04-language-definition.md"
INDEX_REL = "specs/S04-language-definition.index.yaml"

SPEC_TWO_CLAUSES = (
    "# S4 \u2014 Spec\n\n## Stage 0 clause set\n\n"
    "- **S04#1.1 \u2014 Alpha.** Category: defined. Restates a decision.\n"
    "- **S04#1.2 \u2014 Beta.** Category: defined. Restates a decision.\n"
)
SPEC_ONE_CLAUSE = (
    "# S4 \u2014 Spec\n\n## Stage 0 clause set\n\n"
    "- **S04#1.1 \u2014 Alpha.** Category: defined. Restates a decision.\n"
)
SPEC_NO_CLAUSES = "# S4 \u2014 Spec\n\nContainer only; no clauses declared.\n"


def _entry(
    clause_id: str = "S04#1.1",
    category: str = "defined",
    title: str = "Alpha",
    status: str = "ratified",
    source: str = SPEC_REL,
) -> str:
    return (
        f'  - id: "{clause_id}"\n'
        f"    category: {category}\n"
        f"    title: {title}\n"
        f"    status: {status}\n"
        f"    source: {source}\n"
    )


def _index(*entries: str) -> str:
    header = "spec:\n  id: S04\n  version: 1.0.0\n"
    if entries:
        return header + "clauses:\n" + "".join(entries)
    return header + "clauses: []\n"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _repo(tmp_path: Path, spec_text: str, index_text: str) -> Path:
    _write(tmp_path / SPEC_REL, spec_text)
    _write(tmp_path / INDEX_REL, index_text)
    return tmp_path


def test_no_sidecars_is_clean(tmp_path: Path) -> None:
    _write(tmp_path / SPEC_REL, SPEC_TWO_CLAUSES)
    assert collect_errors(tmp_path) == []


def test_valid_populated_index_passes(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_TWO_CLAUSES,
        _index(_entry(), _entry("S04#1.2", title="Beta")),
    )
    assert collect_errors(repo) == []


def test_valid_empty_index_passes(tmp_path: Path) -> None:
    repo = _repo(tmp_path, SPEC_NO_CLAUSES, _index())
    assert collect_errors(repo) == []


def test_missing_index_entry_is_reported(tmp_path: Path) -> None:
    repo = _repo(tmp_path, SPEC_TWO_CLAUSES, _index(_entry()))
    errors = collect_errors(repo)
    assert any(
        "missing index entry" in error and "S04#1.2" in error
        for error in errors
    )


def test_orphan_index_entry_is_reported(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_ONE_CLAUSE,
        _index(_entry(), _entry("S04#1.3", title="Ghost")),
    )
    errors = collect_errors(repo)
    assert any(
        "no corresponding clause declaration" in error and "S04#1.3" in error
        for error in errors
    )


def test_duplicate_index_ids_are_reported(tmp_path: Path) -> None:
    repo = _repo(tmp_path, SPEC_ONE_CLAUSE, _index(_entry(), _entry()))
    errors = collect_errors(repo)
    assert any(
        "duplicate clause ID S04#1.1 in index" in error for error in errors
    )


def test_duplicate_prose_declarations_are_reported(tmp_path: Path) -> None:
    spec = SPEC_ONE_CLAUSE + "- **S04#1.1 \u2014 Alpha again.** Duplicate.\n"
    repo = _repo(tmp_path, spec, _index(_entry()))
    errors = collect_errors(repo)
    assert any(
        "duplicate clause declaration S04#1.1" in error for error in errors
    )


def test_invalid_category_is_reported(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path, SPEC_ONE_CLAUSE, _index(_entry(category="normative"))
    )
    errors = collect_errors(repo)
    assert any("invalid category 'normative'" in error for error in errors)


def test_invalid_status_is_reported(tmp_path: Path) -> None:
    repo = _repo(tmp_path, SPEC_ONE_CLAUSE, _index(_entry(status="accepted")))
    errors = collect_errors(repo)
    assert any("invalid status 'accepted'" in error for error in errors)


def test_malformed_identifier_syntax_is_reported(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_ONE_CLAUSE,
        _index(_entry(), _entry("S04#1..2", title="Bad")),
    )
    errors = collect_errors(repo)
    assert any("invalid identifier syntax 'S04#1..2'" in error for error in errors)


def test_identifier_prefix_must_match_spec_id(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_ONE_CLAUSE,
        _index(_entry(), _entry("S99#1.1", title="Foreign")),
    )
    errors = collect_errors(repo)
    assert any("invalid identifier syntax 'S99#1.1'" in error for error in errors)


def test_broken_source_missing_file_is_reported(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path, SPEC_ONE_CLAUSE, _index(_entry(source="specs/missing.md"))
    )
    errors = collect_errors(repo)
    assert any("no such file" in error for error in errors)


def test_source_without_clause_id_is_reported(tmp_path: Path) -> None:
    _write(tmp_path / "specs" / "other.md", "No clause IDs here.\n")
    repo = _repo(
        tmp_path, SPEC_ONE_CLAUSE, _index(_entry(source="specs/other.md"))
    )
    errors = collect_errors(repo)
    assert any("does not contain clause ID S04#1.1" in error for error in errors)


def test_escaping_source_path_is_rejected(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path, SPEC_ONE_CLAUSE, _index(_entry(source="../outside.md"))
    )
    errors = collect_errors(repo)
    assert any("unsafe path" in error for error in errors)


def test_missing_specification_file_is_reported(tmp_path: Path) -> None:
    _write(tmp_path / INDEX_REL, _index())
    errors = collect_errors(tmp_path)
    assert any("no specification file" in error for error in errors)


def test_malformed_yaml_is_reported_without_crashing(tmp_path: Path) -> None:
    _write(tmp_path / SPEC_REL, SPEC_ONE_CLAUSE)
    _write(
        tmp_path / INDEX_REL,
        'spec: {id: S04, version: 1.0.0}\nclauses: [oops\n  garbage\n',
    )
    errors = collect_errors(tmp_path)
    assert errors, "malformed sidecar must produce findings"
    assert any("unexpected top-level entry" in error for error in errors)


def test_unexpected_clause_field_is_reported(tmp_path: Path) -> None:
    index_text = _index(_entry()) + "    owner: nobody\n"
    repo = _repo(tmp_path, SPEC_ONE_CLAUSE, index_text)
    errors = collect_errors(repo)
    assert any("unexpected clause field 'owner'" in error for error in errors)


def test_missing_required_field_is_reported(tmp_path: Path) -> None:
    entry = '  - id: "S04#1.1"\n    category: defined\n    title: Alpha\n'
    repo = _repo(
        tmp_path,
        SPEC_ONE_CLAUSE,
        "spec:\n  id: S04\n  version: 1.0.0\nclauses:\n" + entry,
    )
    errors = collect_errors(repo)
    assert any("missing required field 'status'" in error for error in errors)
    assert any("missing required field 'source'" in error for error in errors)


def test_missing_spec_header_fields_are_reported(tmp_path: Path) -> None:
    repo = _repo(tmp_path, SPEC_NO_CLAUSES, "clauses: []\n")
    errors = collect_errors(repo)
    assert any("missing required `spec.id`" in error for error in errors)
    assert any("missing required `spec.version`" in error for error in errors)


def test_findings_are_deterministically_ordered(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_TWO_CLAUSES,
        _index(_entry(category="bogus"), _entry("S04#9.9", title="Ghost")),
    )
    first = collect_errors(repo)
    second = collect_errors(repo)
    assert first == second
    assert first, "fixture must produce findings"


def test_excluded_fcos_tree_is_skipped(tmp_path: Path) -> None:
    _write(
        tmp_path / "specs" / "fcos" / "legacy.index.yaml",
        "totally: not\nvalid: schema\n",
    )
    assert collect_errors(tmp_path) == []


# ---------------------------------------------------------------------------
# CLI behavior: the exact invocation the CI documentation-gates job runs
# (P03.5 gate integration; failure must propagate as a non-zero exit).
# ---------------------------------------------------------------------------

_CHECKER = (
    Path(__file__).resolve().parents[1] / "tools" / "checks" / "check_clause_index.py"
)


def _run_cli(root: Path) -> "subprocess.CompletedProcess[str]":
    return subprocess.run(
        [sys.executable, str(_CHECKER), str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_exits_zero_on_consistent_repo(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_TWO_CLAUSES,
        _index(_entry(), _entry("S04#1.2", title="Beta")),
    )
    result = _run_cli(repo)
    assert result.returncode == 0
    assert "all clause indexes are consistent" in result.stdout


def test_cli_exits_nonzero_on_drifted_index(tmp_path: Path) -> None:
    repo = _repo(
        tmp_path,
        SPEC_ONE_CLAUSE,
        _index(_entry(), _entry("S04#9.9", title="Ghost")),
    )
    result = _run_cli(repo)
    assert result.returncode == 1
    assert "S04#9.9" in result.stdout
    assert "drift finding" in result.stdout


def test_cli_failure_stops_a_fail_fast_gate_sequence(tmp_path: Path) -> None:
    """A drifted index must abort a fail-fast step sequence (CI job semantics)."""
    repo = _repo(
        tmp_path,
        SPEC_ONE_CLAUSE,
        _index(_entry(), _entry("S04#9.9", title="Ghost")),
    )
    marker = tmp_path / "next-step-ran"
    script = (
        "set -e\n"
        f'"{sys.executable}" "{_CHECKER}" "{repo}"\n'
        f'touch "{marker}"\n'
    )
    result = subprocess.run(
        ["bash", "-c", script], capture_output=True, text=True, check=False
    )
    assert result.returncode != 0
    assert not marker.exists()
