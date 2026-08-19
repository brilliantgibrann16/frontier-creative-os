# P04.1 — Compiler Implementation Plan & Architecture Boundary Note

**Status:** Active · **Subsystem:** S5 · **Program Package:** P04.1 · **Date:** 2026-08-19  
**Governing Ratifications:** S04 Stage 1 W-B (ADR-0013), S05 Compiler Subsystem Boundary Contract (ADR-0014)

---

## 1. Objective & Scope

This note fulfills WBS package **`P04.1`**, establishing the formal implementation plan, source organization, toolchain environment, and boundary skeleton for the Frontier Specification Language (FSL) compiler under total specification authority (A4, L-2, INV-3).

### Strict Boundary Non-Scope
In accordance with ADR-0012, ADR-0013, and ADR-0014:
- **No Bytecode Emission:** Executable bytecode codegen is deferred to Stage ≥ 2 (S06 Runtime).
- **No Runtime ABI:** Execution semantics are owned by S06.
- **No Type System Typechecking:** Type/data models are deferred (ADR-0012 D3).
- **No Remote Package Resolution:** S11 is Deprecated/Superceded; module resolution is local-only (`S04#3.1`).
- **No Prototype Contamination:** The Phase 0 prototype pipeline (`tools/compiler/fcos/`) is strictly quarantined under `L-7` / `INV-7`.

---

## 2. Source Code & Layout Architecture

The conforming compiler package resides under `tools/compiler/fsl/`:

```
tools/compiler/
├── fsl/                      # Conforming FSL Stage 1 Compiler Package
│   ├── __init__.py           # Package root, exports compile_artifact and models
│   ├── api.py                # S05#3.3 Programmatic API implementation
│   ├── cli.py                # S05#3.1 CLI entry point (fcos-compile)
│   ├── diagnostics.py        # S05#2.1–S05#2.4 Clause-traceable diagnostics engine
│   ├── emitter.py            # S05#4.1–S05#4.3 Deterministic Execution Bundle emitter
│   ├── loader.py             # S05#1.1–S05#1.3 Input loader & duplicate key rejector
│   ├── models.py             # Core immutable data structures (Diagnostic, CompilationResult, Bundle)
│   └── validator.py          # S04 Stage 1 W-B schema & semantic boundary validator
└── fcos/                     # QUARANTINED Phase 0 prototype (Historical reference only; L-7)
```

---

## 3. Toolchain & Runtime Environment

- **Language & Runtime:** Python 3.11+ (standard library only; zero external production dependencies per GL-15 / DP-28).
- **Encoding & Parsing:** Standard library `json` with custom `JSONDecoder` object pair hooks for strict duplicate-key detection (`S05#1.3`).
- **CLI Framework:** Python standard library `argparse` with deterministic status codes (`S05#3.2`).
- **Testing:** `pytest` test runner under CI isolation with pure assert-based verification (`P11`).

---

## 4. Subsystem Interfaces & Traceability Map

| Interface Requirement | S05 Clause | Implementation Module | Mechanical Verification |
|---|---|---|---|
| **Input Format (UTF-8 JSON)** | `S05#1.1` | `loader.py` | `tests/compiler/test_loader.py` |
| **Schema Version Validation** | `S05#1.2` | `validator.py` | `tests/compiler/test_validator_boundary.py` |
| **Duplicate Key Rejection** | `S05#1.3` | `loader.py` | `tests/compiler/test_loader.py` |
| **Clause-Traceable Diagnostics** | `S05#2.1` | `diagnostics.py` | `tests/compiler/test_diagnostics.py` |
| **Diagnostic Structure & Path** | `S05#2.2` | `models.py` | `tests/compiler/test_diagnostics.py` |
| **Deterministic Sorting** | `S05#2.3` | `diagnostics.py` | `tests/compiler/test_diagnostics.py` |
| **No Semantic Inventions** | `S05#2.4` | `validator.py` | `tests/compiler/test_validator_boundary.py` |
| **CLI Entry Point (`fcos-compile`)** | `S05#3.1` | `cli.py` | `tests/compiler/test_cli.py` |
| **Exit Code Protocol** | `S05#3.2` | `cli.py` | `tests/compiler/test_cli.py` |
| **Programmatic API** | `S05#3.3` | `api.py` | `tests/compiler/test_api.py` |
| **Stage 1 Execution Bundle** | `S05#4.1` | `emitter.py` | `tests/compiler/test_emitter.py` |
| **Bundle Structure & Metadata** | `S05#4.2` | `emitter.py` | `tests/compiler/test_emitter.py` |
| **Byte-Level Determinism** | `S05#4.3` | `emitter.py` | `tests/compiler/test_emitter.py` |

---

## 5. Prototype Quarantine Policy (`L-7` / `INV-7`)

1. All new compiler development is restricted strictly to `tools/compiler/fsl/`.
2. No symbols, helpers, or data models from `tools/compiler/fcos/` shall be imported into `tools/compiler/fsl/`.
3. CI and testing environments test `tools/compiler/fsl/` independently against ratified specification fixtures.
