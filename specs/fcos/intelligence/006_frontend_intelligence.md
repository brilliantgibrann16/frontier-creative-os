---
id: FCOS-INT-006
title: Frontend Intelligence
version: 0.1.0
status: Stable
classification: Intelligence

owner: Frontier Creative Operating System

depends_on:
  - FCOS-INT-001
  - FCOS-INT-003
  - FCOS-INT-004
  - FCOS-INT-005

implements:
  - CAP-008

produces:
  - Frontend Architecture
  - Component Strategy
  - Rendering Strategy
  - State Management Strategy
  - Frontend Evaluation Report
---

# Frontend Intelligence

## Purpose

Frontend Intelligence transforms design intent into maintainable frontend architecture.

Its objective is to preserve visual quality while maximizing maintainability, scalability, accessibility, and runtime performance.

---

# Cognitive Objective

Before generating implementation, the AI SHALL answer:

- Which rendering strategy is appropriate?
- Which components should be reusable?
- Which state belongs locally?
- Which state belongs globally?
- Which interactions require client execution?
- Which logic should remain on the server?
- Which abstractions improve maintainability?

---

# Inputs

Frontend Intelligence consumes:

- Repository Intelligence Report
- Design Strategy
- UX Strategy
- Motion Strategy
- Technical Constraints

---

# Architecture Pipeline

## Stage 1 — Rendering Analysis

Determine:

- Server Rendering
- Client Rendering
- Static Generation
- Hybrid Rendering
- Streaming
- Partial Hydration

Selection SHALL be justified.

---

## Stage 2 — Component Modeling

Identify:

- layout components
- reusable components
- feature components
- shared primitives
- composition opportunities

Output:

Component Architecture

---

## Stage 3 — State Analysis

Classify state into:

- local
- shared
- server
- cache
- derived
- transient

Global state SHALL be minimized.

---

## Stage 4 — Data Flow

Evaluate:

- API boundaries
- asynchronous operations
- loading states
- optimistic updates
- error handling

Output:

Data Flow Specification

---

## Stage 5 — Performance Review

Evaluate:

- bundle size
- lazy loading
- code splitting
- image optimization
- font loading
- rendering cost

Output:

Performance Strategy

---

# Component Principles

Components SHOULD be:

- cohesive
- reusable
- composable
- predictable
- testable

Components MUST avoid hidden side effects.

---

# Decision Criteria

Every architectural decision SHOULD optimize:

- maintainability
- readability
- scalability
- performance
- accessibility
- developer experience

---

# Anti-Patterns

The AI MUST avoid:

God Components

Deep prop drilling

Duplicate logic

Monolithic layouts

Unnecessary client rendering

Excessive global state

Premature abstraction

Inconsistent component APIs

---

# Outputs

Frontend Intelligence produces:

- Frontend Architecture
- Component Tree
- Rendering Strategy
- State Strategy
- Data Flow Diagram
- Performance Recommendations

---

# Failure Conditions

Frontend Intelligence SHALL fail when:

component boundaries are unclear,

rendering strategy is inconsistent,

performance costs are unjustified,

state ownership is ambiguous,

architecture cannot scale.

---

# Quality Criteria

Frontend Intelligence is complete when:

component hierarchy is coherent,

rendering decisions are justified,

performance strategy is documented,

state ownership is explicit,

architecture supports future growth.

---

# Consumers

Outputs are consumed by:

- Engineering Intelligence
- Quality Engine
- Compiler

---

# Guiding Statement

Frontend architecture is the discipline of preserving design intent while minimizing long-term implementation complexity.