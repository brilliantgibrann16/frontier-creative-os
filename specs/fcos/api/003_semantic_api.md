---
id: FCOS-API-003
title: Semantic Analyzer Public API
version: 1.0.0
status: Stable

classification: API Contract

owner: Frontier Creative Operating System

---

# Semantic Analyzer Public API

## Purpose

The Semantic Analyzer transforms Abstract Syntax Trees (AST) into validated Semantic Models.

Unlike the Parser, the Semantic Analyzer understands the meaning and relationships contained within FCOS specifications.

---

# Responsibilities

The Semantic Analyzer SHALL:

- validate semantic correctness
- resolve document references
- resolve dependencies
- detect semantic conflicts
- construct a Semantic Model
- produce semantic diagnostics

The Semantic Analyzer SHALL NOT:

- modify source documents
- optimize execution
- generate artifacts
- validate generated bundles

---

# Inputs

The Semantic Analyzer accepts:

- Abstract Syntax Tree
- Collection of ASTs
- Repository Context

---

# Outputs

The Semantic Analyzer produces:

- Semantic Model
- Semantic Diagnostics
- Dependency Graph

---

# Public Interface

analyze()

Analyzes a single AST.

Input

Abstract Syntax Tree

Output

Semantic Model

---

analyze_repository()

Analyzes every AST in a repository.

Input

Collection of ASTs

Output

Repository Semantic Model

---

# Semantic Model

Every Semantic Model SHALL contain:

- document identifier
- resolved metadata
- dependency graph
- capability definitions
- artifact definitions
- compiler directives
- diagnostics

---

# Dependency Resolution

The Semantic Analyzer SHALL:

identify producers,

identify consumers,

detect missing references,

detect circular dependencies,

construct a complete dependency graph.

---

# Semantic Validation

Validate:

required metadata,

identifier uniqueness,

reference integrity,

dependency integrity,

capability compatibility,

artifact consistency.

---

# Diagnostics

Diagnostics SHALL be categorized as:

Information

Warning

Error

Fatal

Every diagnostic SHALL include:

severity,

message,

source location,

affected object,

recommended resolution.

---

# Semantic States

Idle

Resolving

Analyzing

Building Model

Validating

Completed

Failed

---

# Determinism

Identical AST inputs SHALL produce identical Semantic Models.

---

# Extension Points

Future implementations MAY support:

external semantic plugins,

custom capability registries,

domain-specific semantic analyzers.

---

# Guiding Statement

The Semantic Analyzer understands meaning.

It transforms syntax into knowledge.