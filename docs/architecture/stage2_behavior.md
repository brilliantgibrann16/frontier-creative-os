# FSL Stage 2 Behavior & Architecture Guide

- **Status:** Ratified Reference (informative / non-normative)
- **Artifact Class:** Behavior & Architecture Documentation (P13.3, S14)
- **Authority Notice:** The specification (`specs/S04-language-definition.md`) is authoritative; this document is an explanatory, implementation-oriented behavioral guide (Baseline L-2, Blueprint §9, AX-1, DP-2).
- **Governing Decisions:** ADR-0016 (RFC-0023 Acceptance: D1 Stage 2 Entered, D2 Package S2-B, D3 Static Evaluation Only, D4 Additive `fsl/1.0`), ADR-0013, ADR-0014, ADR-0015.

---

## 1. Overview & Capability Model

Stage 2 of the Frontier Specification Language (FSL) extends the Stage 1 interchange kernel (`S04#5.1`–`S04#8.3`) by introducing a **Typed Data Model Core** and **Pure Deterministic Expressions** under ratified Scope Package **S2-B** (ADR-0016).

```
┌──────────────────────────────────────────────────────────────────┐
│                   Stage 2 Architectural Scope                    │
│                                                                  │
│  ┌───────────────────────────────┐ ┌──────────────────────────┐  │
│  │   Typed Data Model Core (§9)  │ │ Pure Expressions (§10)   │  │
│  │   • Scalar Types (S04#9.1)    │ │ • Evaluation Model (10.1)│  │
│  │   • Compound Types (S04#9.2)  │ │ • Operators (10.2, 10.3) │  │
│  │   • Annotations (S04#9.3)     │ │ • Conditionals (10.4)    │  │
│  │   • Schema Validation (S04#9.4│ │ • Invariants (10.5)      │  │
│  └───────────────────────────────┘ └──────────────────────────┘  │
│                                  │                               │
│                                  ▼                               │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │        Static-Only Compile & Validation Boundary (§10.6)   │  │
│  │        JSON AST Interchange Syntax under fsl/1.0 (§10.7)   │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

### 1.1 Non-Normative Boundary
This guide does not define or alter normative language behavior. Every behavior described herein is directly traceable to ratified clauses in `specs/S04-language-definition.md` or ratified compiler boundary contracts in `specs/S05-compiler.md`.

### 1.2 Explicit Non-Scope & Invariants
In accordance with ADR-0016:
- **No Dedicated Surface Syntax:** Package S2-C is not selected; FSL does not define a custom human grammar at Stage 2. All constructs are represented in JSON AST.
- **Static Evaluation Only:** Stage 2 evaluation occurs solely during compilation and artifact validation. There is **no runtime evaluator** and no execution semantics for S06.
- **Schema Compatibility:** Stage 2 is an additive extension within `schema_version: "fsl/1.0"`.

---

## 2. Typed Data Model Core (`S04#9.1`–`S04#9.4`)

The Stage 2 Typed Data Model provides unambiguous scalar and compound types for modeling software architectures and domain invariants.

### 2.1 Scalar Data Types (`S04#9.1`)
FSL defines four primitive scalar types:

| Scalar Type | Definition | JSON Representation |
| --- | --- | --- |
| `string` | UTF-8 encoded text sequence | JSON string |
| `integer` | Finite signed whole number | JSON number (integer value) |
| `float` | Finite IEEE 754 floating-point number | JSON number |
| `boolean` | Logical truth value (`true` or `false`) | JSON boolean |

*Implementation Reference:* `tools/compiler/fsl/types.py` (`SCALAR_TYPES`, `validate_type_annotation`).

### 2.2 Compound Data Structures (`S04#9.2`)
FSL defines three compound structures:

| Compound Type | Definition | Structure / Syntax |
| --- | --- | --- |
| `record` | Finite set of named, typed fields | `{"type": "record", "fields": {"<name>": "<type_spec>"}}` |
| `list` | Ordered sequence of elements | `{"type": "list", "element_type": "<type_spec>"}` |
| `map` | Key-value dictionary with string keys | `{"type": "map", "value_type": "<type_spec>"}` |

*Implementation Reference:* `tools/compiler/fsl/types.py` (`COMPOUND_TYPES`, `validate_compound_type_definition`).

### 2.3 Type Annotations & Declarations (`S04#9.3`)
Artifact declarations may declare explicit type annotations across components, interfaces, and schemas. Type annotations can be simple scalar names or structured type descriptors.

```json
{
  "name": "UserPayload",
  "type": "record",
  "fields": {
    "id": "integer",
    "username": "string",
    "active": "boolean",
    "tags": {
      "type": "list",
      "element_type": "string"
    }
  }
}
```

### 2.4 Schema Validation Rules (`S04#9.4`)
An artifact is valid under Stage 2 if and only if all declared fields and property values conform strictly to their declared types.
- Type mismatches yield validation rejection per `S04#7.1`.
- Diagnostics identify the exact violated clause `S04#9.4` and the field path per `S04#7.2`.

---

## 3. Pure Deterministic Expressions (`S04#10.1`–`S04#10.7`)

Stage 2 expressions provide side-effect-free functional computations used for constant evaluation, invariant assertions, and property constraints.

### 3.1 Pure Evaluation Model (`S04#10.1`)
- **Purity:** Side-effect-free; evaluation never mutates artifact state or performs external I/O.
- **Totality:** All valid expressions are terminating.
- **Determinism:** Given identical input operands, evaluation produces identical results across all conforming implementations (`S04#7.4`, GL-15).

*Implementation Reference:* `tools/compiler/fsl/expressions.py` (`evaluate_expression`).

### 3.2 Operator Catalog (`S04#10.2`, `S04#10.3`)

| Operator Group | Operators / Forms | Semantics & Error Conditions |
| --- | --- | --- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `%` | Standard numeric operations. Division or modulo by zero yields rejection (`S04#10.2`). |
| **Boolean Logic** | `and`, `or`, `not` | Short-circuiting pure boolean operations over boolean operands. |
| **Relational** | `==`, `!=`, `<`, `<=`, `>`, `>=` | Strict equality and ordered comparisons across matching scalar types. |
| **String Ops** | `concat`, `len` | Concatenation of string sequences and length computation (`S04#10.3`). |
| **Collection Ops**| `index`, `len`, `get` | List indexing (0-based) and map lookup. Out-of-bounds or missing keys yield rejection (`S04#10.3`). |

### 3.3 Conditional Branching (`S04#10.4`)
Conditional expressions take the ternary branching form:

```json
{
  "op": "if",
  "condition": {"op": ">", "left": {"var": "count"}, "right": 0},
  "consequent": {"var": "count"},
  "alternate": 0
}
```
- Condition must evaluate to a boolean scalar.
- Only the selected branch is evaluated deterministically.

### 3.4 Declarative Invariants (`S04#10.5`)
Declarations may attach declarative invariants (`invariants: [...]`) containing boolean expressions.
- During compilation and validation, every invariant expression is evaluated.
- If any invariant evaluates to `false`, validation fails with outcome `rejected` (`S04#7.1`), citing `S04#10.5` (`S04#7.2`).

```json
{
  "schema_version": "fsl/1.0",
  "manifest": {
    "name": "bounded-service",
    "version": "1.0.0"
  },
  "declarations": [
    {
      "name": "pool_config",
      "type": "record",
      "fields": {
        "min_size": "integer",
        "max_size": "integer"
      },
      "values": {
        "min_size": 2,
        "max_size": 10
      },
      "invariants": [
        {
          "op": "<=",
          "left": {"var": "min_size"},
          "right": {"var": "max_size"}
        }
      ]
    }
  ]
}
```

---

## 4. Static-Only Evaluation Boundary (`S04#10.6`)

Per ADR-0016 Decision 3 (D3-A):
1. **Compilation-Time Evaluation:** All expression evaluation and invariant verification happen statically during artifact validation and bundle generation (`tools/compiler/fsl/validator.py`, `tools/compiler/fsl/expressions.py`).
2. **No S06 Runtime Behavior:** Stage 2 introduces zero runtime evaluation semantics. S06 runtime behavior remains gated under `G-SPEC(S06)` and is not unblocked.
3. **Determinism Guarantee:** Validation outcomes and execution bundle outputs are 100% byte-for-byte reproducible across independent toolchains (`S05#4.3`).

---

## 5. Concrete Interchange Syntax (`S04#10.7`)

Per ADR-0016 Decision 4 (D4-A):
- **Schema Version:** `schema_version: "fsl/1.0"`.
- **Serialization:** Strict RFC 8259 UTF-8 JSON.
- **Backward Compatibility:** All valid Stage 1 W-B artifacts remain valid Stage 2 artifacts without modification.
- **AST Node Structure:** Expressions are encoded as structured JSON AST dictionaries with explicit `op`, `literal`, or `var` discriminators.

---

## 6. Conformance & Verification Boundary

- **Informative Status:** This document is explanatory architecture guidance under Program P13 (S14). It does **not** create or certify conformance claims.
- **Standing Conformance Frame:** Official conformance judgment is governed exclusively by `specs/S13-verification-conformance.md` and executed via `tools/conformance/judge.py`.
- **Standing Claim:** Official standing claim `CLAIM-FSL-1.0-TOOLS.COMPILER.FSL-0.1.0-STAGE1.WB` remains scoped to the Stage 1 W-B clause set (`S04#5.1`–`S04#8.3`). Stage 2 conformance claims remain gated on future authorized P12 work packages.

---

## 7. Traceability Index

| Spec Clause | Title / Requirement | Implementation Source | Test Evidence |
| --- | --- | --- | --- |
| `S04#9.1` | Scalar data types | `tools/compiler/fsl/types.py` | `tests/compiler/test_fsl_stage2_typed_data_model.py` |
| `S04#9.2` | Compound data structures | `tools/compiler/fsl/types.py` | `tests/compiler/test_fsl_stage2_typed_data_model.py` |
| `S04#9.3` | Type annotations & declarations | `tools/compiler/fsl/types.py` | `tests/compiler/test_fsl_stage2_typed_data_model.py` |
| `S04#9.4` | Schema validation rules | `tools/compiler/fsl/validator.py` | `tests/compiler/test_fsl_stage2_typed_data_model.py` |
| `S04#10.1` | Pure expression evaluation model | `tools/compiler/fsl/expressions.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
| `S04#10.2` | Arithmetic & boolean operations | `tools/compiler/fsl/expressions.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
| `S04#10.3` | String & collection operations | `tools/compiler/fsl/expressions.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
| `S04#10.4` | Conditional expressions | `tools/compiler/fsl/expressions.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
| `S04#10.5` | Declarative invariant assertions | `tools/compiler/fsl/expressions.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
| `S04#10.6` | Static evaluation boundary | `tools/compiler/fsl/validator.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
| `S04#10.7` | Stage 2 JSON AST representation | `tools/compiler/fsl/loader.py` | `tests/compiler/test_fsl_stage2_pure_expressions.py` |
