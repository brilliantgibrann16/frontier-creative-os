---
id: FCOS-API-002
title: Parser Public API
version: 1.0.0
status: Stable

classification: API Contract

owner: Frontier Creative Operating System

---

# Parser Public API

## Purpose

The Parser transforms FCOS source specifications into a structured Abstract Syntax Tree (AST).

The Parser SHALL validate syntax only.

It SHALL NOT perform semantic validation.

---

# Responsibilities

The Parser SHALL:

- discover supported specification files
- tokenize document structure
- parse metadata
- parse document sections
- construct an Abstract Syntax Tree
- report syntax diagnostics

The Parser SHALL NOT:

- resolve dependencies
- validate semantics
- optimize specifications
- generate artifacts

---

# Inputs

The Parser accepts:

- Repository Path
- Specification File
- Document Stream

Supported formats:

- Markdown (.md)

Future versions MAY support:

- YAML
- JSON
- FSL

---

# Outputs

The Parser produces:

- Abstract Syntax Tree (AST)
- Parse Diagnostics
- Source Mapping

---

# Public Interface

parse()

Parses a single specification document.

Input

Specification File

Output

Abstract Syntax Tree

---

parse_repository()

Parses every supported specification within a repository.

Input

Repository Path

Output

Collection of Abstract Syntax Trees

---

# AST Requirements

Every AST SHALL contain:

- document identifier
- metadata
- section hierarchy
- source locations
- syntax diagnostics

---

# Error Model

The Parser SHALL report:

Syntax Error

Unexpected Structure

Missing Metadata

Duplicate Metadata

Unsupported Format

Unknown Section

Errors SHALL include source location whenever possible.

---

# Parser States

Idle

Loading

Tokenizing

Parsing

Building AST

Completed

Failed

---

# Determinism

Identical source files SHALL always produce identical AST structures.

---

# Extension Points

Future parser extensions MAY support:

- plugin parsers
- custom section handlers
- alternative specification languages

---

# Guiding Statement

The Parser understands structure.

It does not understand meaning.