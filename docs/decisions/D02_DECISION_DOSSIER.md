# D-02 Decision Dossier — S04 Stage 2 Capability-Stage Transition & Scope Framing

**Artifact class:** Decision-support dossier — carries **no decision authority** (Blueprint §7) and contains **no recommendation, no ranking, and no invented option**. It compiles, quotes, and traces what the repository already records. The decisions and their recording ADR are the Maintainer's alone (Constitution Article 6, Article 7, INV-8).
**Relationship to `D02_DECISION_BRIEF.md`:** This dossier extends `D02_DECISION_BRIEF.md` into the full multi-section analytical reference. Both documents compile merged sources without addition; neither carries decision authority.
**Decision:** D-02 Decision Surface (RFC-0023 D1–D4) — controlling Stage 2 capability transition, language content boundary, S06 runtime evaluation relationship, and versioning strategy.
**Governing Ratifications:** S04 Stage 0 (ADR-0011), S04 Stage 1 W-B (ADR-0013), S05 Compiler Boundary (ADR-0014), S13 Verification & Conformance (ADR-0015).
**Repository state at compilation:** `main` = `f50ea2e` (2026-08-19, merge of PR #61 / RFC-0023). 186/186 tests passing, `G-CONF` satisfied for Stage 1 W-B.

---

## 1. Decision Statement

Per ratified clause **`S04#1.2`**:
> *"The language capability stages are Stage 0 (minimal contract), Stage 1 (interchange kernel), Stage 2 (data model & expressions), Stage 3 (full language). Progression across stages requires explicit Maintainer authorization via the RFC → ADR decision path."*

Following the complete execution of the Stage 1 W-B implementation program (**P04.0–P04.5**, PR #51–PR #55) and its S13 verification/conformance certification (**P12.1–P12.4**, PR #57–PR #60, claim `CLAIM-FSL-1.0-TOOLS.COMPILER.FSL-0.1.0-STAGE1.WB`), the repository is in an unblocked state to consider progression to **Stage 2**.

RFC-0023 was merged in PR #61 to formalize the decision surface. This dossier compiles the full technical context, trade-offs, and downstream impacts across four discrete decision questions (**D1–D4**) for the Maintainer's determination.

---

## 2. Exact Governing Artifacts

| Artifact | Level / Rank | Governing Mandate |
|---|---|---|
| **Constitution v1** | Rank 1 | Article 6 (Maintainer sole decision authority), Article 7 (ADR binding mechanism), Article 9 (Release integrity). |
| **Architecture Baseline 1.1.0** | Rank 2 | §10 Language Identity, §13 Amendments, L-3 (Zero runtime defining authority), L-8 (Decision records). |
| **ADR-0006** | Rank 3 | Decision 1 (Identity I-D), Decision 2 (Runtime S-B), Decision 3 (Staging discipline), Decision 4 (Packaging N-no). |
| **ADR-0011** | Rank 3 | Ratification of S04 Stage 0 minimal contract clauses (`S04#1.1`–`S04#4.3`). |
| **ADR-0012 / ADR-0013** | Rank 3 | Ratification of S04 Stage 1 W-B interchange kernel clauses (`S04#5.1`–`S04#8.3`). |
| **ADR-0014** | Rank 3 | Ratification of S05 Compiler Boundary specification (`S05#1.1`–`S05#4.3`). |
| **ADR-0015** | Rank 3 | Ratification of S13 Verification & Conformance subsystem (`S13#1.1`–`S13#4.4`). |
| **RFC-0023** | Proposal Frame | Defines decision questions D1–D4, candidate scope packages S2-A/S2-B/S2-C, and downstream constraints. |

---

## 3. Stage 1 Baseline & Conformance Status

The Stage 1 W-B foundation is fully operational and locked:

1. **S04 Normative Clauses:** Thirteen clauses ratified across §5 Single-Artifact Unit Model, §6 Structural Validity & Validity Closure, §7 Validation Outcome Model, and §8 Concrete Interchange Syntax.
2. **S05 Compiler Implementation:** `tools.compiler.fsl` implements the Stage 1 kernel with full diagnostics sorting, clause-traceable errors, duplicate-key rejection, and CLI exit code parity.
3. **S13 Conformance Certification:** `tools.conformance.runner` evaluates the 10-fixture canonical corpus (`tests/fixtures/conformance/`), and `tools.conformance.judge` publishes verified claim `CLAIM-FSL-1.0-TOOLS.COMPILER.FSL-0.1.0-STAGE1.WB` in `docs/conformance/claims/`.
4. **Gate `G-CONF`:** Officially **MET** for Stage 1 W-B.

---

## 4. Detailed Decision Classes (D1–D4)

### D1 — Stage Transition Timing
- **Option D1-A (Enter Stage 2 Now):** Formally opens Stage 2 specification, design, and implementation tracks. Unlocks drafting of S04 Stage 2 amendment clauses.
- **Option D1-B (Defer Stage 2 Entry):** Records a formal deferral with a future DP-15 review milestone. The repository remains focused on Stage 1 tooling hardening.

### D2 — Stage 2 Content-Scope Package
- **Package S2-A (Typed Data Model Core):**
  - Defines scalar types (`string`, `integer`, `float`, `boolean`) and compound types (`record`, `list`, `map`).
  - Adds field type annotations and schema validation rules to FSL declarations.
  - Adds no expression syntax; constraints are purely static structural assertions.
- **Package S2-B (Data Model + Pure Deterministic Expressions):**
  - Incorporates all of Package S2-A.
  - Adds pure deterministic expressions: arithmetic (`+`, `-`, `*`, `/`, `%`), boolean logic (`and`, `or`, `not`), comparison (`==`, `!=`, `<`, `<=`, `>`, `>=`), string manipulation, list/map indexing, and conditional expressions (`if/then/else`).
  - Adds declarative invariant assertions over artifact properties.
  - Retains concrete JSON AST as the primary interchange syntax.
- **Package S2-C (Data Model + Expressions + Human Surface Syntax):**
  - Incorporates all of Package S2-B.
  - Adds a dedicated human-authorable surface syntax and formal grammar with compiler parsing to JSON AST.

### D3 — Runtime Relationship (S06 S-B Integration)
- **Option D3-A (Static Evaluation Only):** Stage 2 expressions are evaluated strictly at compile/validation time (e.g., constant folding, static invariant checking).
- **Option D3-B (Runtime Evaluation Contract):** Stage 2 defines both static constraints and the formal evaluation semantics for the S06 S-B validation-evaluation runtime, enabling runtime artifact parameter evaluation.

### D4 — Compatibility & Versioning Strategy
- **Option D4-A (Additive Extension to `fsl/1.0`):** Stage 2 language constructs are additive under `schema_version: "fsl/1.0"`. All Stage 1 documents remain strictly conforming.
- **Option D4-B (New Schema Version `fsl/2.0`):** Stage 2 introduces `schema_version: "fsl/2.0"`, establishing an explicit version boundary.

---

## 5. Subsystem Impact & Dependency Matrix

| Subsystem | Impact of Package S2-A | Impact of Package S2-B | Impact of Package S2-C |
|---|---|---|---|
| **S04 (Language Definition)** | ~10–12 new clauses defining type schemas | ~20–25 new clauses defining types, AST nodes, and pure evaluation semantics | ~35–40 new clauses defining types, AST, grammar, and surface syntax |
| **S05 (Compiler)** | Add type checker & schema validator | Add AST expression evaluator & invariant validator | Add lexer, parser, grammar validator, and AST generator |
| **S06 (Runtime)** | Minimal impact (structural checks only) | Formalizes S-B evaluation contract | Formalizes S-B evaluation contract |
| **S13 (Verification & Conformance)** | Add typed schema fixtures to corpus | Add expression evaluation & invariant fixtures | Add surface syntax parsing & compilation fixtures |
| **P04 (Compiler Program)** | Extends P04.3 to type verification | Extends P04.3 to expression evaluation | Requires new frontend compiler pipeline |
| **P12 (Conformance Program)** | Expands canonical fixture corpus | Expands fixture corpus with evaluator cases | Expands fixture corpus with parser cases |

---

## 6. Risk Analysis & Architectural Safeguards

1. **Risk of Accidental Language Creep (CN-14):**
   - *Mitigation:* Capability stages are strictly bounded. State machines, I/O, concurrency, and dynamic execution remain explicitly deferred to Stage 3+.
2. **Risk of Expression Non-Determinism (GL-15):**
   - *Mitigation:* If Package S2-B or S2-C is selected, expression evaluation must be strictly pure, side-effect-free, and total (terminating).
3. **Grammar Ambiguity Risk (DP-28):**
   - *Mitigation:* Under Package S2-B, concrete JSON AST remains the single interchange form, avoiding grammar ambiguity until surface syntax is formally needed.

---

## 7. Stop Boundary & Next Action

This dossier provides exhaustive decision support for the Maintainer. It selects no option and modifies no specification. The next governing action is the authoring and recording of the future Stage 2 capability transition ADR by the Maintainer to resolve questions D1–D4.
