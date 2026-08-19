# S5 — Compiler Subsystem Specification

**Status:** Ratified · **Subsystem:** S5 (Blueprint §2) · **Date:** 2026-08-19 · **Governing ADR:** ADR-0014

## Scope

Translation of source artifacts into build artifacts, diagnostics, and
optimization — under total specification authority (A4). The Phase 0
prototype pipeline is historical context only and is outside this spec
(L-7). Implementation work is governed by ratified S04 and S05 clauses.

## Responsibilities

- Realize ratified specifications exactly; divergence is a compiler
  defect by definition (L-2, INV-3).
- Emit diagnostics that report and never rule (Blueprint §6).
- Optimize only within spec-observable equivalence (L-3).
- Forbidden: defining behavior; private semantic contracts with the
  runtime (L-11, INV-11).

## Interfaces

Compiler boundary per Blueprint §8: invocation, input acceptance,
artifact emission, diagnostics contract.

## Data model & Artifacts

Execution bundle format and validation data models for Stage 1.

## API contracts

Standard CLI and Python programmatic interfaces.

## State machines

Per-invocation lifecycle: Accepted-input → Diagnosed (≥0 diagnostics) → (Artifacts-emitted | Failed).

## Sequence flows

1. Invocation via CLI or programmatic API.
2. Input validation against ratified S04 schema.
3. Diagnostic emission citing violated ratified clause IDs.
4. Deterministic Execution Bundle emission.
5. Exit status return.

## Error & Diagnostic Model

Traceable machine-readable diagnostics citing violated S04 clause IDs.

## Security requirements

Compiler processes untrusted input (user source): it must not execute
source content during translation unless a ratified spec defines such a
phase; resource exhaustion on malicious input is a defect class.

## Performance budgets

Deterministic reproducibility required (DP-28).

## Observability requirements

Diagnostics are the primary surface; a conforming compiler’s observable
behavior must be fully explainable by ratified clauses (no oracle behavior).

## Testing requirements

Implementation test suite (evidence, zero authority, INV-4) + conformance
suite judgment (INV-16).

## Acceptance criteria

100% of shipped behavior traceable to ratified clauses (INV-17); conformance
suite passes.

## Stage 1 Compiler Boundary Clause Set

Ratified per-clause by ADR-0014 (2026-08-19) through the amendment path
(proposal RFC-0021 → recording ADR).

Clause declaration convention (mechanical — ADR-0010 / ADR-0011):
each clause is declared by exactly one list line beginning
`- **<clause ID> — <title>.**`. Clauses are listed in clause-ID order.
Every clause below has status **ratified** and is indexed in
`specs/S05-compiler.index.yaml`.

- **S05#1.1 — Input format.** Category: defined. The compiler shall accept as primary source input a UTF-8 encoded file containing a single JSON object conforming strictly to the ratified S04 Stage 1 W-B interchange specification (`S04#5.1`–`S04#8.3`). (RFC-0021 §3.1.)
- **S05#1.2 — Schema version validation.** Category: defined. The compiler shall immediately validate that the input object contains `schema_version` matching `"fsl/1.0"` (`S04#8.3`). Any mismatched or missing schema version shall cause immediate rejection citing `S04#8.3`. (RFC-0021 §3.1.)
- **S05#1.3 — Deterministic JSON parse.** Category: defined. Parsing of JSON input must follow strict RFC 8259 syntax without extensions. Duplicate keys within any JSON object shall be rejected as invalid input citing `S04#8.3`. (RFC-0021 §3.1.)
- **S05#2.1 — Clause-traceable diagnostics.** Category: defined. When the compiler rejects an input artifact, it must emit machine-readable diagnostics. Every diagnostic representing a specification violation must cite the exact ratified clause identifier (`S04#6.1`–`S04#7.6`, `S04#8.3`) governing the failure (INV-17). (RFC-0021 §3.2.)
- **S05#2.2 — Diagnostic structure.** Category: defined. Each diagnostic entry shall contain string `code` (`"SYNTAX_ERROR"`, `"VALIDATION_ERROR"`, `"DEPENDENCY_ERROR"`, or `"INTERNAL_ERROR"`), string `clause_id` (citing the governing ratified clause ID, or null for internal errors), human-readable string `message`, and string `path` pointing to the offending field. (RFC-0021 §3.2.)
- **S05#2.3 — Deterministic diagnostic ordering.** Category: defined. Diagnostic lists must be sorted deterministically by JSON path, then by clause ID, ensuring identical diagnostics output across environments for identical invalid inputs. (RFC-0021 §3.2.)
- **S05#2.4 — No semantic inventions.** Category: defined. The compiler shall not emit diagnostics asserting behavioral or semantic constraints not ratified in S04 (INV-3, Baseline §6). (RFC-0021 §3.2.)
- **S05#3.1 — CLI entry point.** Category: defined. The compiler CLI shall be invokable via `fcos-compile <input-artifact.json> [--out <output-path>] [--format json|text]`. (RFC-0021 §3.3.)
- **S05#3.2 — Exit codes.** Category: defined. The compiler process shall return deterministic status codes: 0 for success, 1 for validation/specification failure, 2 for CLI usage/invocation error, and 3 for internal unhandled compiler fault. (RFC-0021 §3.3.)
- **S05#3.3 — Programmatic API.** Category: defined. The compiler must provide a standard Python API `def compile_artifact(source_data: dict | str, options: dict | None = None) -> CompilationResult:` returning boolean success, diagnostic list, and optional execution bundle. (RFC-0021 §3.3.)
- **S05#4.1 — Stage 1 output target.** Category: defined. In Stage 1, compilation consists of full structural validation and dependency resolution. The output emitted is a deterministic Execution Bundle JSON document (`.fcos-bundle.json`). (RFC-0021 §3.4.)
- **S05#4.2 — Execution bundle structure.** Category: defined. The bundle must contain `bundle_version` (`"1.0.0"`), string `compiler_version`, validated `artifact` payload, `resolved_dependencies` list, and deterministic `compilation_timestamp_utc`. (RFC-0021 §3.4.)
- **S05#4.3 — Determinism guarantee.** Category: defined. Given identical input bytes and identical compiler version, the output bundle bytes must be byte-for-byte identical (reproducibility rule, DP-28). (RFC-0021 §3.4.)

## Deferred Functionality (Stage ≥ 2)

The following areas are explicitly outside the Stage 1 S05 specification and deferred to subsequent specification cycles:
1. Executable bytecode emission and intermediate representation (IR) generation.
2. Runtime ABI definition and execution semantics (S06 Runtime).
3. Type-system typechecking rules (deferred under ADR-0012 D3).
4. Package distribution and remote registry resolution (S11 Deprecated; S04#3.1 local scope).

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Spec supremacy | Baseline P-1, L-2, L-3; INV-2, INV-3 |
| No lateral contracts | L-11; INV-11 |
| Prototype exclusion | L-7; INV-7 |
| Traceable diagnostics | INV-17; RFC-0021; ADR-0014 |
| Boundary contract | RFC-0021; ADR-0014 |
