---
id: FCOS-003
title: Glossary
version: 0.1.0
status: Stable
classification: Core Specification
owner: Frontier Creative Operating System
depends_on:
  - FCOS-000 Project Manifest
  - FCOS-001 Document Conventions
  - FCOS-002 Project Architecture
next:
  - FCOS-004 Operating Principles
---

# Glossary

## Purpose

This glossary defines canonical terminology used throughout the Frontier Creative Operating System (FCOS).

Every defined term has exactly one meaning within the specification.

Consistency of terminology is mandatory.

---

# AI System

A frontier language model operating under the FCOS specification.

The AI System executes workflows, performs reasoning, and produces implementation artifacts.

---

# Artifact

Any output produced during execution.

Examples include:

- implementation plans
- design systems
- prompts
- reports
- source code
- documentation

---

# Capability

A well-defined competency provided by a module.

Examples include repository analysis, UX reasoning, performance evaluation, or planning.

Capabilities describe *what* the system can do rather than *how* it is implemented.

---

# Compilation

The process of transforming multiple FCOS source documents into consolidated operational artifacts.

Compilation never changes the meaning of source specifications.

---

# Compiled Artifact

A generated document produced by combining one or more source specifications.

Compiled artifacts are derived outputs and must not replace source documents.

---

# Constraint

A mandatory limitation that influences decision making.

Constraints may originate from project requirements, technical boundaries, user objectives, or FCOS rules.

---

# Context

The complete set of information available to the AI System before making a decision.

Context may include repository structure, documentation, requirements, design references, and implementation history.

---

# Decision

A justified conclusion reached by the AI System.

Every significant decision should be explainable and traceable.

---

# Dependency

A required relationship between documents, modules, or execution stages.

Dependencies determine execution order and information flow.

---

# Execution

The coordinated process of transforming objectives into validated implementation.

Execution consumes planning outputs and produces working artifacts.

---

# Execution Graph

A structured representation of ordered implementation tasks and their dependencies.

Execution graphs reduce ambiguity during complex projects.

---

# FCOS

The Frontier Creative Operating System.

A model-agnostic operating specification for creative software engineering.

---

# Human Operator

The individual responsible for defining objectives, approving decisions, and retaining final authority over project outcomes.

---

# Intelligence Module

A subsystem responsible for analytical reasoning.

Intelligence modules generate understanding but do not directly implement software.

---

# Layer

A logical architectural boundary within FCOS.

Each layer owns a distinct responsibility and communicates through structured outputs.

---

# Operational Prompt

A prompt generated from FCOS specifications to configure AI behavior during execution.

Operational prompts are artifacts, not authoritative specifications.

---

# Quality Gate

A validation checkpoint that determines whether implementation may proceed.

Quality gates may evaluate design, engineering, accessibility, performance, or consistency.

---

# Repository Mapping

The structured process of identifying the architecture, dependencies, technologies, and organization of an existing repository.

---

# Runtime

The execution environment defined by FCOS.

Runtime governs workflow progression rather than implementation decisions.

---

# Source Specification

A human-authored FCOS document representing the authoritative definition of system behavior.

All compiled artifacts originate from source specifications.

---

# State

A measurable condition of execution at a particular point within the workflow.

State transitions are managed by the Runtime layer.

---

# Validation

The process of determining whether outputs satisfy defined objectives, constraints, and quality gates.

---

# Workflow

A structured sequence of activities performed to achieve a defined objective.

FCOS workflows are deterministic, traceable, and repeatable.

---

# Guiding Principle

When introducing new terminology, authors should extend this glossary before using the term elsewhere in the specification.

The glossary serves as the single authoritative vocabulary for the entire FCOS ecosystem.