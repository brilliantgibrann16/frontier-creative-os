"""Spec-derived test evidence for S04 Stage 2 Pure Deterministic Expressions (S04#10.1–S04#10.7)."""

import pytest
from tools.compiler.fsl.api import compile_artifact
from tools.compiler.fsl.expressions import (
    evaluate_declarative_invariants,
    evaluate_static_expression,
)
from tools.compiler.fsl.models import DiagnosticCode, ValidationStatus


def test_s04_10_1_pure_expression_evaluation_model():
    """Verify S04#10.1 side-effect-free, deterministic expression evaluation."""
    ctx = {"base_port": 8000, "offset": 80}
    expr = {
        "kind": "binary_op",
        "op": "+",
        "left": {"kind": "ref", "name": "base_port"},
        "right": {"kind": "ref", "name": "offset"},
    }

    # Deterministic repetition
    val1, diags1 = evaluate_static_expression(expr, ctx)
    val2, diags2 = evaluate_static_expression(expr, ctx)

    assert not diags1
    assert val1 == 8080
    assert val1 == val2
    # Context remains unmutated
    assert ctx == {"base_port": 8000, "offset": 80}


def test_s04_10_2_arithmetic_operations():
    """Verify S04#10.2 arithmetic operators (+, -, *, /, %) and error handling."""
    # Addition
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "+", "left": 10, "right": 20})
    assert val == 30 and not diags

    # Subtraction
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "-", "left": 50, "right": 15})
    assert val == 35 and not diags

    # Multiplication
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "*", "left": 6, "right": 7})
    assert val == 42 and not diags

    # Division (exact integer vs float)
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "/", "left": 100, "right": 4})
    assert val == 25 and not diags

    # Modulo
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "%", "left": 23, "right": 5})
    assert val == 3 and not diags

    # Division by zero diagnostic attribution
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "/", "left": 10, "right": 0})
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#10.2"
    assert "Division by zero" in diags[0].message

    # Modulo by zero diagnostic attribution
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "%", "left": 10, "right": 0})
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#10.2"
    assert "Modulo by zero" in diags[0].message


def test_s04_10_2_boolean_and_relational_operations():
    """Verify S04#10.2 boolean logic (and, or, not) and comparisons (==, !=, <, <=, >, >=)."""
    # Logic
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "and", "left": True, "right": False})
    assert val is False and not diags

    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "or", "left": True, "right": False})
    assert val is True and not diags

    val, diags = evaluate_static_expression({"kind": "unary_op", "op": "not", "operand": False})
    assert val is True and not diags

    # Comparisons
    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "==", "left": "alpha", "right": "alpha"})
    assert val is True and not diags

    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "!=", "left": 10, "right": 20})
    assert val is True and not diags

    val, diags = evaluate_static_expression({"kind": "binary_op", "op": "<", "left": 5, "right": 10})
    assert val is True and not diags

    val, diags = evaluate_static_expression({"kind": "binary_op", "op": ">=", "left": 10, "right": 10})
    assert val is True and not diags


def test_s04_10_3_string_and_collection_operations():
    """Verify S04#10.3 string concat, length, list indexing, and map lookup."""
    # String concat
    val, diags = evaluate_static_expression({"kind": "concat", "left": "Frontier ", "right": "OS"})
    assert val == "Frontier OS" and not diags

    # String length
    val, diags = evaluate_static_expression({"kind": "length", "operand": "creative"})
    assert val == 8 and not diags

    # Collection length
    val, diags = evaluate_static_expression({"kind": "length", "operand": {"kind": "literal", "value": [1, 2, 3, 4]}})
    assert val == 4 and not diags

    # List indexing
    val, diags = evaluate_static_expression({
        "kind": "index",
        "target": {"kind": "literal", "value": ["a", "b", "c"]},
        "index": 1,
    })
    assert val == "b" and not diags

    # List indexing out of bounds
    val, diags = evaluate_static_expression({
        "kind": "index",
        "target": {"kind": "literal", "value": ["a", "b"]},
        "index": 5,
    })
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#10.3"
    assert "out of bounds" in diags[0].message

    # Map lookup
    val, diags = evaluate_static_expression({
        "kind": "lookup",
        "target": {"kind": "literal", "value": {"timeout_ms": 5000}},
        "key": "timeout_ms",
    })
    assert val == 5000 and not diags

    # Map lookup missing key
    val, diags = evaluate_static_expression({
        "kind": "lookup",
        "target": {"kind": "literal", "value": {"timeout_ms": 5000}},
        "key": "retry_count",
    })
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#10.3"
    assert "not found" in diags[0].message


def test_s04_10_4_conditional_expressions():
    """Verify S04#10.4 deterministic conditional branching (if/then/else)."""
    expr_true = {
        "kind": "conditional",
        "condition": {"kind": "binary_op", "op": ">", "left": 10, "right": 5},
        "then": "high_throughput",
        "else": "low_throughput",
    }
    val, diags = evaluate_static_expression(expr_true)
    assert val == "high_throughput" and not diags

    expr_false = {
        "kind": "conditional",
        "condition": {"kind": "binary_op", "op": "<", "left": 10, "right": 5},
        "then": "high_throughput",
        "else": "low_throughput",
    }
    val, diags = evaluate_static_expression(expr_false)
    assert val == "low_throughput" and not diags

    # Non-boolean condition error
    expr_invalid_cond = {
        "kind": "conditional",
        "condition": 42,
        "then": "a",
        "else": "b",
    }
    val, diags = evaluate_static_expression(expr_invalid_cond)
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#10.4"
    assert "must evaluate to boolean" in diags[0].message


def test_s04_10_5_declarative_invariants_validation():
    """Verify S04#10.5 declarative invariant assertions and failure attribution."""
    ctx = {"max_connections": 100, "min_connections": 10}

    # Passing invariants
    valid_invs = [
        {
            "name": "valid_limits",
            "expr": {
                "kind": "binary_op",
                "op": ">",
                "left": {"kind": "ref", "name": "max_connections"},
                "right": {"kind": "ref", "name": "min_connections"},
            },
        }
    ]
    diags = evaluate_declarative_invariants(valid_invs, ctx)
    assert not diags

    # Failing invariant
    failing_invs = [
        {
            "name": "impossible_limit",
            "expr": {
                "kind": "binary_op",
                "op": "<",
                "left": {"kind": "ref", "name": "max_connections"},
                "right": {"kind": "ref", "name": "min_connections"},
            },
        }
    ]
    diags = evaluate_declarative_invariants(failing_invs, ctx)
    assert len(diags) == 1
    assert diags[0].clause_id == "S04#10.5"
    assert "evaluated to false" in diags[0].message


def test_s04_10_6_and_10_7_artifact_compilation_with_invariants():
    """Verify S04#10.6 static evaluation boundary & S04#10.7 JSON AST representation."""
    artifact = {
        "schema_version": "fsl/1.0",
        "manifest": {
            "name": "invariant-verified-service",
            "version": "1.0.0",
            "kind": "service",
        },
        "declarations": {
            "port": "integer",
            "tls_enabled": "boolean",
        },
        "properties": {
            "port": 8443,
            "tls_enabled": True,
        },
        "invariants": [
            {
                "name": "port_in_secure_range",
                "expr": {
                    "kind": "binary_op",
                    "op": ">",
                    "left": {"kind": "ref", "name": "port"},
                    "right": 1024,
                },
            },
            {
                "name": "tls_must_be_active",
                "expr": {"kind": "ref", "name": "tls_enabled"},
            },
        ],
    }

    result = compile_artifact(artifact)
    assert result.success
    assert result.outcome.status == ValidationStatus.ACCEPTED
    assert result.bundle is not None

    # Invariant failure rejection
    failing_artifact = dict(artifact)
    failing_artifact["properties"] = {"port": 80, "tls_enabled": True}  # port < 1024 violates invariant
    res_failing = compile_artifact(failing_artifact)
    assert not res_failing.success
    assert res_failing.outcome.status == ValidationStatus.REJECTED
    assert "S04#10.5" in res_failing.outcome.violated_clauses
