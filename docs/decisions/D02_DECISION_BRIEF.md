# D-02 Decision Brief — S04 Stage 2 Capability Transition & Scope Framing

**Artifact class:** Decision-support brief — carries **no decision authority** (Blueprint §7) and **contains no recommendation or invented option**. It compiles, without addition, what the repository already records. The decisions and their recording ADR are the Maintainer's alone (Constitution Article 6, Article 7, INV-8).
**Decision:** D-02 Decision Surface (RFC-0023 D1–D4) — controlling the Stage 1 → Stage 2 capability transition, language content boundary, S06 runtime relationship, and versioning strategy.
**Governing Ratifications:** S04 Stage 0 (ADR-0011), S04 Stage 1 W-B (ADR-0013), S05 Compiler Boundary (ADR-0014), S13 Verification & Conformance (ADR-0015).
**Sources (exhaustive):** RFC-0023; RFC-0001 (D-01); RFC-0012 (U-14); RFC-0019; RFC-0020; RFC-0021; RFC-0022; ADR-0006; ADR-0012; ADR-0013; ADR-0014; ADR-0015; specs S04, S05, S13; PROGRAM.md; DEPENDENCY_GRAPH.md.

---

## 1. The Exact Decision Questions

As framed in RFC-0023 §4.B, the Maintainer faces four coupled decision questions to authorize Stage 2 progression:

1. **D1 — Stage Transition Timing:** Does FCOS enter Stage 2 now based on the conforming Stage 1 W-B foundation (`G-CONF` MET), or defer entry with a recorded review point?
2. **D2 — Stage 2 Content-Scope Package:** Which discrete capability package defines the Stage 2 language boundary:
   - **Package S2-A:** Typed Data Model Core (scalar and compound data structures, field constraints, schema validation rules);
   - **Package S2-B:** Data Model + Pure Deterministic Expressions (Package S2-A plus side-effect-free pure deterministic expressions: arithmetic, boolean logic, string operations, collection indexing, conditionals `if/then/else`, and declarative invariant assertions);
   - **Package S2-C:** Data Model + Expressions + Human Surface Syntax (Package S2-B plus a dedicated human-authorable surface grammar compiling to JSON AST).
3. **D3 — Runtime Relationship (S06 S-B Integration):** Is Stage 2 expression evaluation confined strictly to static compilation/validation time (**Option D3-A**), or does it define the formal evaluation contract for the S06 S-B validation-evaluation runtime (**Option D3-B**)?
4. **D4 — Compatibility & Versioning Strategy:** Are Stage 2 constructs added as backward-compatible extensions within `schema_version: "fsl/1.0"` (**Option D4-A**), or do they establish a new schema version `fsl/2.0` (**Option D4-B**)?

---

## 2. Admissible Options (Recorded in RFC-0023)

| Decision | Option / Package | Summary Definition |
|---|---|---|
| **D1: Timing** | **Option D1-A** | Enter Stage 2 now. Unlocks Wave 3 S04 amendment drafting and S05/S13 extensions. |
| | **Option D1-B** | Defer Stage 2 entry with a recorded DP-15 review date. |
| **D2: Scope** | **Package S2-A** | *Typed Data Model Core:* Scalar types (`string`, `integer`, `float`, `boolean`), compound types (`record`, `list`, `map`), type declarations, and schema validation rules. |
| | **Package S2-B** | *Data Model + Pure Expressions:* Package S2-A + side-effect-free pure deterministic expressions, conditional logic, and invariant assertions. |
| | **Package S2-C** | *Data Model + Expressions + Surface Syntax:* Package S2-B + dedicated human surface syntax and grammar compiler. |
| **D3: Runtime** | **Option D3-A** | *Static Evaluation Only:* Expressions evaluated purely at compile/validation time (constant folding, static assertions). |
| | **Option D3-B** | *Runtime Evaluation Contract:* Establishes formal evaluation semantics for the S06 S-B validation-evaluation runtime. |
| **D4: Versioning** | **Option D4-A** | *Additive Extension to `fsl/1.0`:* All Stage 1 artifacts remain valid Stage 2 artifacts without schema increment. |
| | **Option D4-B** | *New Major Version `fsl/2.0`:* Bumps schema version with explicit migration mapping. |

---

## 3. Consequences of Each Option

### D1: Timing Consequences
- **Option D1-A (Enter Now):** Leverages the 100% verified Stage 1 compiler and S13 conformance judge to expand FSL expressivity cleanly.
- **Option D1-B (Defer):** Preserves Stage 1 W-B as the stable terminal state for the current cycle; delays richer domain modeling.

### D2: Scope Consequences
- **Package S2-A (Data Model Core):** Smallest delta (~10–12 clauses). Highly predictable, zero expression complexity, but lacks computed constraints.
- **Package S2-B (Data Model + Pure Expressions):** Balanced expressivity (~20–25 clauses). Enables rich declarative invariant checking and parameterization without parser/grammar bloat. JSON AST remains the single interchange format.
- **Package S2-C (Full Surface Syntax):** Highest expressivity (~35–40 clauses), but introduces lexer/parser grammar ambiguity risks, AST translation layers, and higher maintenance overhead.

### D3: Runtime Consequences
- **Option D3-A (Static Only):** Simplifies runtime requirements; delays S06 runtime engine specification.
- **Option D3-B (Runtime Contract):** Unlocks S06 S-B specification drafting with a well-defined pure evaluation boundary, aligning compiler outputs with runtime evaluation.

### D4: Versioning Consequences
- **Option D4-A (Additive `fsl/1.0`):** Maximizes backward compatibility; existing Stage 1 test fixtures and documents remain 100% conforming.
- **Option D4-B (New `fsl/2.0`):** Enforces strict stage boundaries in schema version metadata; requires version negotiation in tooling.

---

## 4. Downstream Execution Order Following Decision

```
[Maintainer ADR Ratifying D1–D4]
              │
              ▼
[S04 Stage 2 Amendment Proposal RFC]
              │
              ▼
[Ratification of S04 Stage 2 Clauses]
              │
              ▼
[Compiler P04 Stage 2 Realization & Conformance Expansion]
              │
              ▼
[S06 Runtime Specification (if Option D3-B)]
```

---

## 5. Stop Boundary

This brief provides decision support only. It selects no option and authorizes no implementation work until the Maintainer records a binding decision via an ADR (Article 6, Article 7, INV-8).
