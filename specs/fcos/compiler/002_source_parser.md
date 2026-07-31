---
id: FCOS-COMP-002
title: Source Parser
version: 0.1.0
status: Stable
classification: Compiler

owner: Frontier Creative Operating System

depends_on:
  - FCOS-COMP-001

produces:
  - Parsed Document Model
  - Metadata Registry
  - Parse Report
---

# Source Parser

## Purpose

The Source Parser transforms raw FCOS specification documents into structured compiler objects.

The parser SHALL preserve semantic meaning while extracting metadata required for dependency analysis, artifact generation, and validation.

The parser SHALL NOT modify specification content.

---

# Objectives

The Source Parser SHALL:

- discover specification documents
- classify document types
- extract metadata
- validate document structure
- normalize parsed objects
- produce deterministic parse results

---

# Supported Sources

The parser SHALL support:

- Markdown (.md)

Future versions MAY support:

- JSON
- YAML
- TOML

---

# Document Structure

Each specification SHALL contain:

Front Matter

↓

Metadata

↓

Body

↓

Sections

↓

Guiding Statement

Missing required sections SHALL produce validation errors.

---

# Metadata Extraction

The parser SHALL extract:

- id
- title
- version
- status
- classification
- owner
- depends_on
- implements
- produces

Unknown metadata SHALL be preserved for downstream consumers.

---

# Section Model

Every document SHALL be represented as:

Document

↓

Sections

↓

Blocks

↓

Paragraphs

The parser SHALL preserve ordering.

---

# Parsing Pipeline

Repository Discovery

↓

Document Loading

↓

Front Matter Parsing

↓

Metadata Validation

↓

Body Parsing

↓

Section Mapping

↓

Document Model Generation

↓

Parse Report

---

# Parsed Document Model

Each parsed document SHALL contain:

Identifier

Version

Classification

Dependencies

Capabilities

Outputs

Section Index

Content Hash

Source Location

Validation Status

---

# Validation Rules

The parser SHALL verify:

required metadata,

unique identifiers,

valid versions,

well-formed front matter,

duplicate identifiers,

document integrity.

---

# Error Classification

Parser errors SHALL be categorized as:

Information

Warning

Error

Blocking

Blocking errors SHALL terminate parsing for the affected document.

---

# Parse Report

The parser SHALL produce:

- processed documents
- failed documents
- warnings
- blocking errors
- duplicate identifiers
- metadata summary

---

# Determinism

Given identical repository contents, the parser MUST produce identical parsed models.

Ordering SHALL be deterministic.

Hash generation SHALL be deterministic.

---

# Failure Conditions

Parsing SHALL fail when:

required metadata is missing,

document syntax is invalid,

duplicate identifiers exist,

mandatory fields cannot be interpreted.

---

# Future Extensions

The parser MAY support:

- incremental parsing
- cached parsing
- semantic indexing
- cross-document references
- plugin parsers

---

# Guiding Statement

A compiler cannot reason about documents until every document has been transformed into a structured, deterministic representation.