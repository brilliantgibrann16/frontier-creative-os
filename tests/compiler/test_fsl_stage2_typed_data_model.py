"""Spec-derived test evidence for S04 Stage 2 Typed Data Model Core (S04#9.1–S04#9.4)."""

import pytest
from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.models import DiagnosticCode, ValidationStatus
from tools.compiler.fsl.types import (
    CompoundType,
    ScalarType,
    is_compound_type,
    is_scalar_type,
    validate_type_annotation,
    validate_value_conformance,
)


def test_s04_9_1_scalar_types_enumeration():
    """Verify S04#9.1 four primitive scalar types."""
    assert is_scalar_type("string")
    assert is_scalar_type("integer")
    assert is_scalar_type("float")
    assert is_scalar_type("boolean")
    assert not is_scalar_type("double")
    assert not is_scalar_type("char")
    assert not is_scalar_type("null")


def test_s04_9_2_compound_types_enumeration():
    """Verify S04#9.2 three structured compound types."""
    assert is_compound_type("record")
    assert is_compound_type("list")
    assert is_compound_type("map")
    assert not is_compound_type("tuple")
    assert not is_compound_type("set")
    assert not is_compound_type("union")


def test_s04_9_3_type_annotations_and_declarations_validation():
    """Verify S04#9.3 valid and invalid type declarations."""
    # Valid scalar annotations
    assert not validate_type_annotation("string", "path")
    assert not validate_type_annotation("integer", "path")
    assert not validate_type_annotation("float", "path")
    assert not validate_type_annotation("boolean", "path")

    # Valid compound descriptors
    valid_record = {
        "type": "record",
        "fields": {
            "title": "string",
            "count": "integer",
            "score": "float",
            "active": "boolean",
        },
    }
    assert not validate_type_annotation(valid_record, "fields")

    valid_list = {"type": "list", "element_type": "string"}
    assert not validate_type_annotation(valid_list, "tags")

    valid_map = {"type": "map", "key_type": "string", "value_type": "integer"}
    assert not validate_type_annotation(valid_map, "scores")

    # Invalid type annotations
    diags = validate_type_annotation("unknown_type", "field")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.3"
    assert diags[0].code == DiagnosticCode.VALIDATION_ERROR

    invalid_compound = {"type": "invalid_compound"}
    diags2 = validate_type_annotation(invalid_compound, "field")
    assert len(diags2) == 1
    assert diags2[0].clause_id == "S04#9.3"


def test_s04_9_4_scalar_values_conformance():
    """Verify S04#9.4 scalar value conformance and type violation attribution."""
    # String
    assert not validate_value_conformance("hello world", "string", "prop")
    diags = validate_value_conformance(123, "string", "prop")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.4"

    # Integer
    assert not validate_value_conformance(42, "integer", "prop")
    # Boolean is not integer in FSL
    diags = validate_value_conformance(True, "integer", "prop")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.4"

    # Float
    assert not validate_value_conformance(3.14159, "float", "prop")
    assert not validate_value_conformance(10, "float", "prop")
    diags = validate_value_conformance(float("nan"), "float", "prop")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.4"

    # Boolean
    assert not validate_value_conformance(True, "boolean", "prop")
    assert not validate_value_conformance(False, "boolean", "prop")
    diags = validate_value_conformance(1, "boolean", "prop")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.4"


def test_s04_9_4_compound_values_conformance():
    """Verify S04#9.4 compound value schema validation."""
    record_spec = {
        "type": "record",
        "fields": {
            "name": "string",
            "age": "integer",
        },
    }
    # Valid record
    assert not validate_value_conformance({"name": "Alice", "age": 30}, record_spec, "user")

    # Missing field
    diags = validate_value_conformance({"name": "Bob"}, record_spec, "user")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.4"
    assert "Missing required record field 'age'" in diags[0].message

    # Field type mismatch
    diags = validate_value_conformance({"name": "Charlie", "age": "thirty"}, record_spec, "user")
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#9.4"
    assert diags[0].path == "user.age"


def test_s04_9_compiler_integration():
    """Verify end-to-end artifact compilation with typed data model."""
    valid_artifact = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "typed-service",
            "version": "1.0.0",
            "kind": "service",
        },
        "types": {
            "Coordinates": {
                "type": "record",
                "fields": {
                    "lat": "float",
                    "lng": "float",
                },
            }
        },
        "declarations": {
            "origin": "Coordinates",
            "retries": "integer",
            "label": "string",
        },
        "properties": {
            "origin": {"lat": 37.7749, "lng": -122.4194},
            "retries": 3,
            "label": "primary-node",
        },
    }

    result = compile_artifact(valid_artifact)
    assert result.success
    assert result.outcome.status == ValidationStatus.ACCEPTED
    assert result.bundle is not None

    # Invalid artifact with type error
    invalid_artifact = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "invalid-typed-service",
            "version": "1.0.0",
            "kind": "service",
        },
        "declarations": {
            "retries": "integer",
        },
        "properties": {
            "retries": "not-an-integer",
        },
    }

    res_invalid = compile_artifact(invalid_artifact)
    assert not res_invalid.success
    assert res_invalid.outcome.status == ValidationStatus.REJECTED
    assert "S04#9.4" in res_invalid.outcome.violated_clauses
