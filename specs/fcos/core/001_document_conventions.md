---
id: FCOS-001
title: Document Conventions
version: 0.1.0
status: Stable
classification: Core Specification
owner: Frontier Creative Operating System
depends_on:
  - FCOS-000 Project Manifest
next:
  - FCOS-002 Project Architecture
---

# Document Conventions

## Purpose

This document defines the conventions that every FCOS specification must follow.

The objective is consistency.

Every document must be readable by both humans and AI systems while remaining maintainable as the specification grows.

These conventions are mandatory unless explicitly overridden by a future core specification.

---

# Document Metadata

Every specification document must begin with a YAML metadata block.

The metadata block enables:

- dependency tracking
- version control
- compilation
- document discovery
- automated tooling

Required fields:

- id
- title
- version
- status
- classification
- owner
- depends_on

Optional fields:

- next
- replaces
- notes

---

# Document Identifier

Every specification receives a unique identifier.

Format:

FCOS-XXX

Examples:

FCOS-000

FCOS-001

FCOS-014

FCOS-102

Identifiers are immutable.

Numbers are never reused.

---

# Versioning

Versioning follows Semantic Versioning.

Format:

MAJOR.MINOR.PATCH

Examples:

0.1.0

0.5.3

1.0.0

Rules:

Major

Breaking architectural changes.

Minor

New functionality.

Patch

Clarifications, corrections, wording improvements.

---

# Status Values

Allowed status values:

Draft

Review

Stable

Locked

Deprecated

Archived

Definitions:

Draft

Content is incomplete.

Review

Content is awaiting validation.

Stable

Approved for implementation.

Locked

No modifications without architectural review.

Deprecated

Replaced by another specification.

Archived

Retained only for historical purposes.

---

# Classification

Each document belongs to exactly one classification.

Allowed values:

Core

Runtime

Research

Creative

Engineering

Execution

Quality

Prompt

Appendix

Compiled

---

# Heading Rules

Documents must use a hierarchical structure.

Allowed heading order:

# Title

## Major Section

### Subsection

#### Detail

Heading levels must never be skipped.

Incorrect:

#

###

Correct:

#

##

###

---

# Lists

Bulleted lists describe unordered concepts.

Numbered lists describe sequences.

Checklist syntax is reserved for execution documents only.

---

# Terminology

Terms with specific meanings must remain consistent across all specifications.

If a new technical term is introduced:

- define it once
- add it to the glossary
- reuse the same wording everywhere

Avoid synonyms for defined concepts.

Consistency is preferred over literary variation.

---

# References

Documents reference each other using FCOS identifiers.

Example:

Depends on:

FCOS-001

References:

FCOS-014

Never reference filenames alone.

Identifiers remain stable even if filenames change.

---

# Dependencies

Dependencies describe required reading order.

A document may depend on multiple specifications.

Circular dependencies are prohibited.

Example:

FCOS-008 depends on:

FCOS-002

FCOS-005

FCOS-006

---

# Design Principles

Specifications must prioritize:

clarity

precision

consistency

traceability

maintainability

Every rule should be understandable without requiring hidden assumptions.

---

# Language

Specifications are written in English.

Engineering terminology should remain technically accurate.

Marketing language is prohibited.

Inspirational writing is discouraged unless explicitly part of the specification.

---

# Future Compatibility

Documents should avoid references to:

specific AI models

specific frameworks

temporary trends

vendor-specific implementations

Instead, describe capabilities.

The implementation layer may evolve independently from the specification.

---

# Modification Policy

Stable documents may receive:

clarifications

typo fixes

examples

Locked documents require architectural justification before modification.

Breaking changes must increment the major version.

---

# Review Criteria

A document may be promoted to Stable only if:

its terminology is consistent

its dependencies are valid

its identifiers are unique

its structure follows FCOS conventions

its rules do not conflict with existing specifications

---

# Guiding Principle

The purpose of these conventions is not bureaucratic consistency.

The purpose is to create a specification that can evolve for years without losing coherence, readability, or machine interpretability.