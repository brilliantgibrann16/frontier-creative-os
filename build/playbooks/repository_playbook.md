# FCOS Repository Playbook v1.0

> Frontier Creative Operating System
>
> Repository Operational Guide

---

# Purpose

This playbook defines the standard operating procedure for using the Frontier Creative Operating System (FCOS).

Every repository SHALL follow this workflow unless an explicit project-specific exception exists.

---

# Operating Principles

FCOS is a reasoning system before it is a prompting system.

Never begin implementation before understanding the project.

Never optimize for speed at the expense of quality.

Every significant decision SHALL be documented and justified.

---

# Standard Workflow

The recommended workflow is:

Repository Analysis

↓

Bootstrap

↓

Master Prompt

↓

Implementation

↓

Review

↓

Refactor

↓

Iteration

↓

Release Validation

---

# Stage 1 — Repository Analysis

Objectives:

- understand project structure
- identify technologies
- identify stakeholders
- identify constraints
- identify architecture
- identify design language
- identify existing quality

Deliverables:

- Repository Summary
- Architecture Overview
- Initial Risk Assessment

---

# Stage 2 — Bootstrap

Execute:

build/bootstrap/claude_bootstrap.md

Purpose:

Initialize the operational environment.

Output:

Operational reasoning context.

---

# Stage 3 — Master Prompt

Execute:

build/prompts/master_prompt.md

Purpose:

Generate the implementation strategy.

Output:

Implementation roadmap.

---

# Stage 4 — Implementation

Implement only after:

- repository understanding
- planning
- assumptions documented
- quality risks identified

Implementation SHALL follow the generated roadmap.

---

# Stage 5 — Review

Execute:

build/prompts/review_prompt.md

Purpose:

Evaluate implementation quality.

Output:

Review Report

Quality Findings

Risk Assessment

---

# Stage 6 — Refactor

Execute:

build/prompts/refactor_prompt.md

Purpose:

Improve maintainability while preserving behavior.

Output:

Refactoring Plan

Refactoring Changes

Validation Results

---

# Stage 7 — Iteration

Execute:

build/prompts/iteration_prompt.md

Purpose:

Determine the highest-value next milestone.

Output:

Iteration Plan

Project Health Report

Priority Roadmap

---

# Stage 8 — Release Validation

Verify:

Architecture

Accessibility

Performance

Maintainability

Consistency

Documentation

Testing

Quality Gates

Only after all required checks pass may the project be considered production ready.

---

# Continuous Improvement

Repeat:

Review

↓

Refactor

↓

Iteration

until project objectives are satisfied.

---

# Repository Health Indicators

Monitor:

Architecture Quality

Technical Debt

UX Quality

Accessibility

Performance

Documentation

Testing

Developer Experience

Scalability

Track trends over time rather than isolated measurements.

---

# Failure Handling

If a stage fails:

document the failure,

identify root cause,

define corrective action,

repeat only the affected stages whenever possible.

Avoid restarting the entire workflow unnecessarily.

---

# Recommended Cadence

Major Feature

↓

Review

↓

Refactor

↓

Iteration

↓

Validation

↓

Release

---

# Guiding Statement

The objective of FCOS is not simply to complete work.

The objective is to continuously improve the quality of the repository through disciplined engineering, structured reasoning, and repeatable operational workflows.

End of Repository Playbook.