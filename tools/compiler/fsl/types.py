"""S04 Stage 2 Typed Data Model implementation adhering to S04#9.1–S04#9.4."""

from dataclasses import dataclass
from enum import Enum
import math
from typing import Any

from tools.compiler.fsl.models import Diagnostic, DiagnosticCode


class ScalarType(str, Enum):
    """S04#9.1 — Stage 2 scalar data types."""

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"


class CompoundType(str, Enum):
    """S04#9.2 — Stage 2 compound data structures."""

    RECORD = "record"
    LIST = "list"
    MAP = "map"


VALID_TYPE_NAMES = {
    ScalarType.STRING.value,
    ScalarType.INTEGER.value,
    ScalarType.FLOAT.value,
    ScalarType.BOOLEAN.value,
    CompoundType.RECORD.value,
    CompoundType.LIST.value,
    CompoundType.MAP.value,
}


def is_scalar_type(type_name: str) -> bool:
    """Check if type name is an authorized scalar type (S04#9.1)."""
    return type_name in {t.value for t in ScalarType}


def is_compound_type(type_name: str) -> bool:
    """Check if type name is an authorized compound type (S04#9.2)."""
    return type_name in {t.value for t in CompoundType}


def validate_type_annotation(
    type_spec: Any,
    path: str,
    declared_custom_types: dict[str, Any] | None = None,
) -> list[Diagnostic]:
    """Validate a type annotation against S04#9.1–S04#9.3."""
    diagnostics: list[Diagnostic] = []
    custom_types = declared_custom_types or {}

    if isinstance(type_spec, str):
        if type_spec not in VALID_TYPE_NAMES and type_spec not in custom_types:
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.3",
                    message=f"Unrecognized type annotation '{type_spec}'. Expected one of {sorted(VALID_TYPE_NAMES | set(custom_types.keys()))}.",
                    path=path,
                )
            )
    elif isinstance(type_spec, dict):
        type_name = type_spec.get("type")
        if not type_name or not isinstance(type_name, str):
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.3",
                    message="Type specification object must declare a string 'type' field.",
                    path=f"{path}.type" if path else "type",
                )
            )
            return diagnostics

        if type_name not in VALID_TYPE_NAMES and type_name not in custom_types:
            diagnostics.append(
                Diagnostic(
                    code=DiagnosticCode.VALIDATION_ERROR,
                    clause_id="S04#9.3",
                    message=f"Unrecognized compound type '{type_name}'.",
                    path=f"{path}.type" if path else "type",
                )
            )
            return diagnostics

        if type_name == CompoundType.RECORD.value:
            fields = type_spec.get("fields")
            if fields is not None:
                if not isinstance(fields, dict):
                    diagnostics.append(
                        Diagnostic(
                            code=DiagnosticCode.VALIDATION_ERROR,
                            clause_id="S04#9.2",
                            message="Record 'fields' specification must be an object.",
                            path=f"{path}.fields" if path else "fields",
                        )
                    )
                else:
                    for field_name, field_spec in fields.items():
                        sub_path = f"{path}.fields.{field_name}" if path else f"fields.{field_name}"
                        diagnostics.extend(validate_type_annotation(field_spec, sub_path, custom_types))

        elif type_name == CompoundType.LIST.value:
            elem_spec = type_spec.get("element_type") or type_spec.get("items")
            if elem_spec is not None:
                sub_path = f"{path}.element_type" if path else "element_type"
                diagnostics.extend(validate_type_annotation(elem_spec, sub_path, custom_types))

        elif type_name == CompoundType.MAP.value:
            key_spec = type_spec.get("key_type")
            if key_spec is not None:
                if key_spec != ScalarType.STRING.value:
                    diagnostics.append(
                        Diagnostic(
                            code=DiagnosticCode.VALIDATION_ERROR,
                            clause_id="S04#9.2",
                            message="Map keys must be of type 'string'.",
                            path=f"{path}.key_type" if path else "key_type",
                        )
                    )
            val_spec = type_spec.get("value_type") or type_spec.get("values")
            if val_spec is not None:
                sub_path = f"{path}.value_type" if path else "value_type"
                diagnostics.extend(validate_type_annotation(val_spec, sub_path, custom_types))
    else:
        diagnostics.append(
            Diagnostic(
                code=DiagnosticCode.VALIDATION_ERROR,
                clause_id="S04#9.3",
                message=f"Invalid type annotation structure of type {type(type_spec).__name__}.",
                path=path,
            )
        )

    return diagnostics


def validate_value_conformance(
    value: Any,
    type_spec: Any,
    path: str,
    declared_custom_types: dict[str, Any] | None = None,
) -> list[Diagnostic]:
    """Validate that a concrete value conforms strictly to its declared type (S04#9.4)."""
    diagnostics: list[Diagnostic] = []
    custom_types = declared_custom_types or {}

    # Resolve custom alias if applicable
    if isinstance(type_spec, str) and type_spec in custom_types:
        type_spec = custom_types[type_spec]

    if isinstance(type_spec, str):
        if type_spec == ScalarType.STRING.value:
            if not isinstance(value, str):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected type 'string', got {type(value).__name__}.",
                        path=path,
                    )
                )
        elif type_spec == ScalarType.BOOLEAN.value:
            if not isinstance(value, bool):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected type 'boolean', got {type(value).__name__}.",
                        path=path,
                    )
                )
        elif type_spec == ScalarType.INTEGER.value:
            if isinstance(value, bool) or not isinstance(value, int):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected type 'integer', got {type(value).__name__}.",
                        path=path,
                    )
                )
        elif type_spec == ScalarType.FLOAT.value:
            if isinstance(value, bool) or not isinstance(value, (int, float)) or (isinstance(value, float) and (math.isnan(value) or math.isinf(value))):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected finite type 'float', got {type(value).__name__}.",
                        path=path,
                    )
                )
        elif type_spec == CompoundType.RECORD.value:
            if not isinstance(value, dict):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected type 'record' (JSON object), got {type(value).__name__}.",
                        path=path,
                    )
                )
        elif type_spec == CompoundType.LIST.value:
            if not isinstance(value, list):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected type 'list' (JSON array), got {type(value).__name__}.",
                        path=path,
                    )
                )
        elif type_spec == CompoundType.MAP.value:
            if not isinstance(value, dict):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected type 'map' (JSON object), got {type(value).__name__}.",
                        path=path,
                    )
                )

    elif isinstance(type_spec, dict):
        type_name = type_spec.get("type")
        if type_name == CompoundType.RECORD.value:
            if not isinstance(value, dict):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected 'record', got {type(value).__name__}.",
                        path=path,
                    )
                )
            else:
                fields = type_spec.get("fields", {})
                for f_name, f_spec in fields.items():
                    sub_path = f"{path}.{f_name}" if path else f_name
                    if f_name not in value:
                        # Required field check
                        required = True
                        if isinstance(f_spec, dict) and f_spec.get("optional", False):
                            required = False
                        if required:
                            diagnostics.append(
                                Diagnostic(
                                    code=DiagnosticCode.VALIDATION_ERROR,
                                    clause_id="S04#9.4",
                                    message=f"Missing required record field '{f_name}'.",
                                    path=sub_path,
                                )
                            )
                    else:
                        diagnostics.extend(
                            validate_value_conformance(value[f_name], f_spec, sub_path, custom_types)
                        )

        elif type_name == CompoundType.LIST.value:
            if not isinstance(value, list):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected 'list', got {type(value).__name__}.",
                        path=path,
                    )
                )
            else:
                elem_spec = type_spec.get("element_type") or type_spec.get("items")
                if elem_spec is not None:
                    for idx, elem in enumerate(value):
                        sub_path = f"{path}[{idx}]"
                        diagnostics.extend(
                            validate_value_conformance(elem, elem_spec, sub_path, custom_types)
                        )

        elif type_name == CompoundType.MAP.value:
            if not isinstance(value, dict):
                diagnostics.append(
                    Diagnostic(
                        code=DiagnosticCode.VALIDATION_ERROR,
                        clause_id="S04#9.4",
                        message=f"Value at '{path}' expected 'map', got {type(value).__name__}.",
                        path=path,
                    )
                )
            else:
                val_spec = type_spec.get("value_type") or type_spec.get("values")
                for k, v in value.items():
                    sub_path = f"{path}.{k}" if path else str(k)
                    if not isinstance(k, str):
                        diagnostics.append(
                            Diagnostic(
                                code=DiagnosticCode.VALIDATION_ERROR,
                                clause_id="S04#9.4",
                                message=f"Map key at '{path}' must be a string, got {type(k).__name__}.",
                                path=sub_path,
                            )
                        )
                    if val_spec is not None:
                        diagnostics.extend(
                            validate_value_conformance(v, val_spec, sub_path, custom_types)
                        )
        elif type_name and is_scalar_type(type_name):
            diagnostics.extend(validate_value_conformance(value, type_name, path, custom_types))

    return diagnostics
