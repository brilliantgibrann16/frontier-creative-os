"""Mechanical clause-index drift checker (RFC-0008 M-B; ADR-0010; ADR-0011).

Scope (L-10): mechanical only. For every per-spec clause-index sidecar
(`specs/<spec>.index.yaml`, ADR-0010 decision 3) this check verifies
the ADR-0010 decision 11 drift conditions against the authoritative
specification prose:

- missing index entries for clauses declared in the specification;
- index entries with no corresponding declared clause;
- duplicate clause identifiers (in the index or in the prose);
- invalid category values;
- invalid status values;
- invalid identifier syntax;
- broken source references.

The prose is authoritative; the index is derived hygiene (ADR-0010
decision 1). This check never modifies any file, never creates clauses
or identifiers, and never auto-fixes drift. It fails deterministically,
one diagnostic line per finding.

Clause declaration convention (ADR-0011 decision 5): a clause is
declared by a Markdown list line beginning
`- **<clause ID> — <title>.**`, where the clause ID is the document
identifier plus a hierarchical dotted N-C fragment, e.g. `S04#1.1`.

Sidecar format: the restricted YAML subset fixed by ADR-0010 decision 5
(`spec:` mapping with `id` and `version`; `clauses:` list whose entries
carry exactly id, category, title, status, source). Anything outside
that subset is reported as malformed, never silently accepted.

Scanned root: specs/. Excluded: specs/fcos/ (legacy prototype tree;
same neutrality rule as the other checks).

Exit status: 0 when all indexes are consistent, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

SIDECAR_SUFFIX = ".index.yaml"
EXCLUDED_TREES = ("specs/fcos",)

VALID_CATEGORIES = (
    "defined",
    "implementation-defined",
    "unspecified",
    "undefined",
)
VALID_STATUSES = ("ratified", "in-review", "deprecated")
CLAUSE_FIELDS = ("id", "category", "title", "status", "source")
SPEC_FIELDS = ("id", "version")

# A clause declaration line in specification prose (ADR-0011 decision 5).
CLAUSE_DECLARATION = re.compile(r"^- \*\*([^\s*]+#[0-9][0-9.]*) \u2014")


def _is_excluded(relative_path: str) -> bool:
    return any(
        relative_path == tree or relative_path.startswith(tree + "/")
        for tree in EXCLUDED_TREES
    )


def iter_sidecars(repo_root: Path) -> Iterator[Path]:
    """Yield every clause-index sidecar under specs/, minus exclusions."""
    specs_root = repo_root / "specs"
    if not specs_root.is_dir():
        return
    for path in sorted(specs_root.rglob("*" + SIDECAR_SUFFIX)):
        if _is_excluded(path.relative_to(repo_root).as_posix()):
            continue
        yield path


def _parse_scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        value = value[1:-1]
    return value


def _split_key_value(
    stripped: str, line_number: int
) -> Tuple[Optional[str], str, Optional[str]]:
    if ":" not in stripped:
        return None, "", f"line {line_number}: {stripped!r} is not a `key: value` pair"
    key, _, raw_value = stripped.partition(":")
    key = key.strip()
    if not key:
        return None, "", f"line {line_number}: empty key"
    return key, _parse_scalar(raw_value), None


def parse_sidecar(
    text: str,
) -> Tuple[Dict[str, str], List[Dict[str, str]], List[str]]:
    """Parse the ADR-0010 restricted YAML subset.

    Returns (spec mapping, clause entries, format errors). Never raises
    on malformed input: every deviation from the fixed schema becomes an
    error string, so drift is reported instead of silently accepted.
    """
    spec: Dict[str, str] = {}
    clauses: List[Dict[str, str]] = []
    errors: List[str] = []
    section: Optional[str] = None
    current: Optional[Dict[str, str]] = None

    for line_number, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if not raw.startswith((" ", "\t")):
            stripped = raw.strip()
            current = None
            if stripped == "spec:":
                section = "spec"
            elif stripped == "clauses:":
                section = "clauses"
            elif stripped == "clauses: []":
                section = "clauses-empty"
            else:
                section = None
                errors.append(
                    f"line {line_number}: unexpected top-level entry "
                    f"{stripped!r} (schema allows only `spec:` and `clauses:` "
                    f"\u2014 ADR-0010 decision 5)"
                )
            continue

        stripped = raw.strip()
        if section == "spec":
            key, value, error = _split_key_value(stripped, line_number)
            if error:
                errors.append(error)
                continue
            if key not in SPEC_FIELDS:
                errors.append(
                    f"line {line_number}: unexpected spec field {key!r} "
                    f"(schema fields: {', '.join(SPEC_FIELDS)})"
                )
            elif key in spec:
                errors.append(f"line {line_number}: duplicate spec field {key!r}")
            else:
                spec[key] = value
        elif section == "clauses":
            if stripped.startswith("- "):
                current = {}
                clauses.append(current)
                stripped = stripped[2:].strip()
                if not stripped:
                    continue
            if current is None:
                errors.append(
                    f"line {line_number}: clause field outside a `- ` entry"
                )
                continue
            key, value, error = _split_key_value(stripped, line_number)
            if error:
                errors.append(error)
                continue
            if key not in CLAUSE_FIELDS:
                errors.append(
                    f"line {line_number}: unexpected clause field {key!r} "
                    f"(schema fields: {', '.join(CLAUSE_FIELDS)})"
                )
            elif key in current:
                errors.append(
                    f"line {line_number}: duplicate clause field {key!r}"
                )
            else:
                current[key] = value
        elif section == "clauses-empty":
            errors.append(f"line {line_number}: content after `clauses: []`")
        else:
            errors.append(
                f"line {line_number}: content outside a recognized section"
            )

    return spec, clauses, errors


def declared_clause_ids(spec_text: str) -> List[str]:
    """Return clause IDs declared in specification prose, in file order."""
    ids: List[str] = []
    for line in spec_text.splitlines():
        match = CLAUSE_DECLARATION.match(line)
        if match:
            ids.append(match.group(1))
    return ids


def _identifier_error(clause_id: str, document_id: Optional[str]) -> Optional[str]:
    if document_id:
        pattern = re.compile(re.escape(document_id) + r"#[0-9]+(\.[0-9]+)*")
        expected = f"{document_id}#<n>[.<n>...]"
    else:
        pattern = re.compile(r"[A-Za-z0-9-]+#[0-9]+(\.[0-9]+)*")
        expected = "<document ID>#<n>[.<n>...]"
    if not pattern.fullmatch(clause_id):
        return (
            f"invalid identifier syntax {clause_id!r} "
            f"(expected {expected} \u2014 RFC-0002 N-C; ADR-0008)"
        )
    return None


def _source_error(
    repo_root: Path, clause_id: str, source: str
) -> Optional[str]:
    path = Path(source)
    if path.is_absolute() or ".." in path.parts:
        return f"broken source reference {source!r}: unsafe path"
    target = repo_root / path
    if not target.is_file():
        return f"broken source reference {source!r}: no such file"
    try:
        text = target.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return (
            f"broken source reference {source!r}: unreadable "
            f"({exc.__class__.__name__})"
        )
    if clause_id not in text:
        return (
            f"broken source reference {source!r}: file does not contain "
            f"clause ID {clause_id}"
        )
    return None


def collect_errors(repo_root: Path) -> List[str]:
    """Return one error string per drift finding, in deterministic order."""
    errors: List[str] = []
    for sidecar in iter_sidecars(repo_root):
        rel = sidecar.relative_to(repo_root).as_posix()
        try:
            text = sidecar.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{rel}: unreadable sidecar ({exc.__class__.__name__})")
            continue
        spec, clauses, format_errors = parse_sidecar(text)
        errors.extend(f"{rel}: {error}" for error in format_errors)

        document_id = spec.get("id") or None
        if not spec.get("id"):
            errors.append(
                f"{rel}: missing required `spec.id` (ADR-0010 decision 5)"
            )
        if not spec.get("version"):
            errors.append(
                f"{rel}: missing required `spec.version` (ADR-0010 decision 5)"
            )

        spec_rel = rel[: -len(SIDECAR_SUFFIX)] + ".md"
        spec_path = repo_root / spec_rel
        declared: List[str] = []
        if spec_path.is_file():
            declared = declared_clause_ids(
                spec_path.read_text(encoding="utf-8")
            )
        else:
            errors.append(
                f"{rel}: no specification file at {spec_rel} "
                f"(prose is authoritative \u2014 ADR-0010 decision 1)"
            )

        seen_declared: set = set()
        for clause_id in declared:
            if clause_id in seen_declared:
                errors.append(
                    f"{spec_rel}: duplicate clause declaration {clause_id}"
                )
            seen_declared.add(clause_id)
        for clause_id in dict.fromkeys(declared):
            identifier_error = _identifier_error(clause_id, document_id)
            if identifier_error:
                errors.append(f"{spec_rel}: {identifier_error}")

        index_ids: List[str] = []
        for position, entry in enumerate(clauses, start=1):
            label = entry.get("id") or f"entry {position}"
            for field in CLAUSE_FIELDS:
                if not entry.get(field):
                    errors.append(
                        f"{rel}: clause {label}: missing required field "
                        f"{field!r}"
                    )
            clause_id = entry.get("id")
            if clause_id:
                index_ids.append(clause_id)
                identifier_error = _identifier_error(clause_id, document_id)
                if identifier_error:
                    errors.append(f"{rel}: {identifier_error}")
            category = entry.get("category")
            if category and category not in VALID_CATEGORIES:
                errors.append(
                    f"{rel}: clause {label}: invalid category {category!r} "
                    f"(valid: {', '.join(VALID_CATEGORIES)})"
                )
            status = entry.get("status")
            if status and status not in VALID_STATUSES:
                errors.append(
                    f"{rel}: clause {label}: invalid status {status!r} "
                    f"(valid: {', '.join(VALID_STATUSES)})"
                )
            source = entry.get("source")
            if clause_id and source:
                source_error = _source_error(repo_root, clause_id, source)
                if source_error:
                    errors.append(f"{rel}: clause {clause_id}: {source_error}")

        seen_index: set = set()
        for clause_id in index_ids:
            if clause_id in seen_index:
                errors.append(f"{rel}: duplicate clause ID {clause_id} in index")
            seen_index.add(clause_id)

        indexed = set(index_ids)
        declared_unique = set(declared)
        for clause_id in dict.fromkeys(declared):
            if clause_id not in indexed:
                errors.append(
                    f"{rel}: missing index entry for clause {clause_id} "
                    f"declared in {spec_rel}"
                )
        if spec_path.is_file():
            for clause_id in dict.fromkeys(index_ids):
                if clause_id not in declared_unique:
                    errors.append(
                        f"{rel}: index entry {clause_id} has no corresponding "
                        f"clause declaration in {spec_rel}"
                    )
    return errors


def main(argv: List[str]) -> int:
    repo_root = (
        Path(argv[1]).resolve()
        if len(argv) > 1
        else Path(__file__).resolve().parents[2]
    )
    if not any(iter_sidecars(repo_root)):
        print("check_clause_index: no clause-index sidecars found.")
        return 0
    errors = collect_errors(repo_root)
    for error in errors:
        print(error)
    if errors:
        print(
            f"check_clause_index: {len(errors)} clause-index drift "
            f"finding(s) found."
        )
        return 1
    print(
        "check_clause_index: all clause indexes are consistent with "
        "specification prose."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
