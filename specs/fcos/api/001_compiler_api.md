---
id: FCOS-API-001
title: Compiler Public API
version: 1.0.0
status: Stable

classification: API Contract

owner: Frontier Creative Operating System

---

# Compiler Public API

## Purpose

Defines the public interface exposed by the FCOS compiler.

The Compiler is the primary orchestration component responsible for coordinating all compilation stages.

Consumers SHALL interact with the compiler only through this public API.

---

# Responsibilities

The Compiler SHALL:

- discover specifications
- invoke the parser
- invoke semantic analysis
- invoke optimization
- invoke artifact generation
- invoke validation
- produce execution bundles

The Compiler SHALL NOT perform parser logic directly.

---

# Public Interface

compile()

Compiles an FCOS repository.

Input

Repository Path

Output

Execution Bundle

---

validate()

Validates an already generated Execution Bundle.

Input

Execution Bundle

Output

Validation Report

---

generate()

Generates artifacts from an optimized semantic model.

Input

Semantic Model

Output

Generated Artifacts

---

analyze()

Performs repository analysis without generation.

Input

Repository Path

Output

Semantic Model

---

# Compiler Lifecycle

Compiler

↓

Parser

↓

Semantic Analyzer

↓

Optimizer

↓

Artifact Generator

↓

Validator

↓

Execution Bundle

---

# Compiler States

Idle

Initializing

Parsing

Analyzing

Optimizing

Generating

Validating

Completed

Failed

---

# Error Model

Every public API SHALL return:

Success

↓

Diagnostics

↓

Warnings

↓

Errors

↓

Artifacts

The Compiler SHALL never terminate silently.

---

# Thread Safety

Compiler instances SHALL be isolated.

Compilation state SHALL NOT leak between executions.

---

# Determinism

Identical inputs SHALL produce identical outputs.

---

# Guiding Statement

The Compiler coordinates the compilation process.

It does not perform every compilation stage itself.