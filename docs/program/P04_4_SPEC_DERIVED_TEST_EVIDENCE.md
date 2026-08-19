# P04.4 — Spec-Derived Test Evidence per Ratified S04/S05 Clause

**Status:** Active · **Subsystem:** S5 / S4 · **Program Package:** P04.4 · **Date:** 2026-08-19  
**Governing Ratifications:** S04 Stage 0 (ADR-0011), S04 Stage 1 W-B (ADR-0013), S05 Compiler Subsystem Boundary (ADR-0014)  
**Program Dependencies:** P04.3 (Complete via PR #53), P11 Testing Infrastructure (Active), P12 Conformance Frame (Partially Gated)

---

## 1. Executive Summary & Purpose

This document records the systematic, spec-derived engineering test evidence across the 13 ratified S04 Stage 1 W-B clauses (`S04#5.1`–`S04#8.3`) and 13 ratified S05 compiler subsystem boundary clauses (`S05#1.1`–`S05#4.3`).

Per **Blueprint INV-4** and **TESTING_CONVENTIONS §3**, tests are **evidence, not definition**. Furthermore, per **S04#7.6** and **CONFORMANCE_FRAME.md**, implementation test evidence does not constitute an official conformance certification, which remains strictly governed under the unratified S13 specification.

---

## 2. S04 Stage 1 W-B Clause Evidence Matrix

| Clause ID | Category & Title | Traceable Test Function | Verification Scope & Observed Behavior | Status |
|---|---|---|---|---|
| `S04#5.1` | Defined · Artifact unit | `test_s04_5_1_single_artifact_unit` | Verifies top-level unit structure requiring manifest dictionary. Rejects non-object and missing manifest with `S04#5.1`. | **Verified** |
| `S04#5.2` | Defined · Stage 1 self-containment | `test_s04_5_2_stage1_self_containment` | Verifies local dependency declaration list validation without attempting cross-artifact network resolution. | **Verified** |
| `S04#6.1` | Defined · Structural validity | `test_s04_6_1_structural_validity_distinction` | Verifies structural validation failure on missing/empty manifest name; marks `is_structurally_valid = False`. | **Verified** |
| `S04#6.2` | Defined · Validity closure | `test_s04_6_2_validity_closure_distinction` | Verifies validity closure failure on invalid version string while preserving `is_structurally_valid = True`. | **Verified** |
| `S04#7.1` | Defined · Validation-outcome model | `test_s04_7_1_outcome_model_accepted_and_rejected` | Verifies explicit `ValidationOutcome` structure (`ACCEPTED` vs `REJECTED`) and state fields. | **Verified** |
| `S04#7.2` | Defined · Violated-clause identification | `test_s04_7_2_violated_clause_attribution` | Verifies sorted, unique attribution of all violated clause IDs in `outcome.violated_clauses`. | **Verified** |
| `S04#7.3` | Defined · Outcome authority | `test_s04_7_3_outcome_authority_spec_alignment` | Verifies validator adheres strictly to S04 normative prose without invented extra-spec rules. | **Verified** |
| `S04#7.4` | Defined · Outcome determinism | `test_s04_7_4_outcome_determinism_sweep` | Verifies 100 repeated compilations yield bitwise identical `ValidationOutcome` and diagnostic lists. | **Verified** |
| `S04#7.5` | Unspecified · Diagnostic presentation | `test_s04_7_5_diagnostic_presentation_contract` | Verifies diagnostics conform to S05 contract (`code`, `clause_id`, `message`, `path`). | **Verified** |
| `S04#7.6` | Defined · Validation/conformance boundary | `test_s04_7_6_conformance_boundary_preservation` | Verifies compiler produces validation outcome without issuing conformance certificates. | **Verified** |
| `S04#8.1` | Defined · Single interchange form | `test_s04_8_1_single_interchange_form_enforcement` | Verifies JSON as the sole accepted interchange format for Stage 1. | **Verified** |
| `S04#8.2` | Defined · Interchange-form obligations | `test_s04_8_2_interchange_obligations_decidability` | Verifies mechanical decidability without requiring type system inference. | **Verified** |
| `S04#8.3` | Defined · Concrete interchange form | `test_s04_8_3_concrete_json_interchange_syntax` | Verifies UTF-8 RFC 8259, duplicate key rejection, and `schema_version: "fsl/1.0"`. | **Verified** |

---

## 3. S05 Compiler Subsystem Boundary Clause Evidence Matrix

| Clause ID | Category & Title | Traceable Test Function | Verification Scope & Observed Behavior | Status |
|---|---|---|---|---|
| `S05#1.1` | Defined · Source text encoding | `test_s05_1_1_utf8_rfc8259_decoding` | Verifies rejection of malformed JSON strings with `SYNTAX_ERROR` citing `S04#8.3`. | **Verified** |
| `S05#1.2` | Defined · Schema version validation | `test_s05_1_2_schema_version_validation` | Verifies exact matching of `schema_version == "fsl/1.0"`; rejects missing or non-matching versions. | **Verified** |
| `S05#1.3` | Defined · Duplicate key rejection | `test_s05_1_3_duplicate_key_rejection` | Verifies strict RFC 8259 duplicate key rejection via `DuplicateKeyCheckingDecoder`. | **Verified** |
| `S05#2.1` | Defined · Diagnostic model | `test_s05_2_1_diagnostic_model` | Verifies diagnostics are emitted on any syntax or validation violation. | **Verified** |
| `S05#2.2` | Defined · Diagnostic fields | `test_s05_2_2_diagnostic_fields` | Verifies every diagnostic contains exact fields `code`, `clause_id`, `message`, `path`. | **Verified** |
| `S05#2.3` | Defined · Deterministic diagnostic order | `test_s05_2_3_deterministic_diagnostic_sorting` | Verifies diagnostics sort deterministically by JSON path followed by clause ID. | **Verified** |
| `S05#2.4` | Defined · Clause-traceable diagnostics | `test_s05_2_4_clause_traceable_diagnostics` | Verifies all specification violation diagnostics cite their governing clause ID. | **Verified** |
| `S05#3.1` | Defined · Command-line interface | `test_s05_3_1_cli_interface` | Verifies `fcos-compile` CLI invocation, arguments, and format options. | **Verified** |
| `S05#3.2` | Defined · Exit code protocol | `test_s05_3_2_cli_exit_code_protocol` | Verifies exact exit codes `0` (success), `1` (validation failure), `2` (usage/IO), `3` (internal fault). | **Verified** |
| `S05#3.3` | Defined · Programmatic API | `test_s05_3_3_programmatic_api_parity` | Verifies `compile_artifact()` returns `CompilationResult` with full parity to CLI. | **Verified** |
| `S05#4.1` | Defined · Execution bundle output | `test_s05_4_1_execution_bundle_emission` | Verifies emission of `.fcos-bundle.json` upon successful compilation. | **Verified** |
| `S05#4.2` | Defined · Bundle structure | `test_s05_4_2_bundle_structure_contract` | Verifies bundle contains `bundle_version`, `compiler_version`, `artifact`, `resolved_dependencies`, and `compilation_timestamp_utc`. | **Verified** |
| `S05#4.3` | Defined · Reproducibility guarantee | `test_s05_4_3_byte_for_byte_reproducibility` | Verifies identical inputs produce bitwise identical `.fcos-bundle.json` byte streams. | **Verified** |

---

## 4. P12 Boundary Statement

In accordance with **`docs/program/CONFORMANCE_FRAME.md` §1–§2** and **ADR-0004 (INV-16)**:
- The tests documented herein provide mechanical verification of compiler implementation behavior under **P11 (Testing Infrastructure)**.
- Official conformance certification remains blocked by **G-SPEC(S13)** and **B-08** pending the ratification of specification S13.
- No test assertion in this suite purports to issue an official conformance seal.
