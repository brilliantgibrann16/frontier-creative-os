---
id: FCOS-API-006
title: Validator Public API
version: 1.0.0
status: Stable

classification: API Contract

owner: Frontier Creative Operating System

---

# Validator Public API

## Purpose

The Validator verifies that generated artifacts satisfy all required quality gates before release.

Validation SHALL detect inconsistencies, missing artifacts, structural violations, and specification errors.

The Validator SHALL NOT modify artifacts.

---

# Responsibilities

The Validator SHALL:

- validate execution bundles
- validate generated artifacts
- verify directory structure
- verify manifest integrity
- verify artifact completeness
- produce validation reports
- generate diagnostics

The Validator SHALL NOT:

- regenerate artifacts
- modify generated outputs
- perform semantic analysis
- optimize execution bundles

---

# Inputs

The Validator accepts:

- Execution Bundle
- Generated Artifacts
- Validation Configuration

---

# Outputs

The Validator produces:

- Validation Report
- Diagnostics
- Quality Gate Results

---

# Public Interface

validate()

Validates a complete Execution Bundle.

Input

Execution Bundle

Output

Validation Report

---

validate_artifact()

Validates a single generated artifact.

Input

Artifact

Output

Artifact Validation Result

---

validate_repository()

Validates every generated artifact within a repository.

Input

Repository Path

Output

Repository Validation Report

---

# Validation Rules

The Validator SHALL verify:

- required artifacts exist
- manifests are valid
- directory structure is correct
- metadata integrity
- artifact consistency
- naming conventions
- quality gate compliance

---

# Quality Gates

Every validation SHALL evaluate:

Architecture

Consistency

Documentation

Maintainability

Accessibility

Performance Metadata

Artifact Integrity

Manifest Integrity

---

# Diagnostics

Diagnostics SHALL include:

Information

Warning

Error

Fatal

Fatal diagnostics SHALL prevent release.

---

# Validator States

Idle

Loading

Inspecting

Validating

Reporting

Completed

Failed

---

# Determinism

Identical Execution Bundles SHALL produce identical Validation Reports.

---

# Extension Points

Future implementations MAY support:

custom validation rules,

plugin validators,

CI integration,

policy-based validation.

---

# Guiding Statement

The Validator verifies correctness.

It never changes generated artifacts.