# FCOS Specification Corpus

**Class:** Subsystem implementation specifications — normative for their
subsystem upon ratification. **Status of all documents: In Review**
(submitted via PR; nothing here is binding until ratified).

One specification per Blueprint subsystem (S1–S16). Each derives
exclusively from: Constitution · Architecture Baseline · System Blueprint ·
Engineering Doctrine · ADR-0001..0003 · the RFC set (RFC-0001..0017).

## Corpus-level assumptions (recorded, not silent)

1. **Acceptance ADRs do not yet exist.** `docs/decisions/` contains
   ADR-0001..0003 only. The Maintainer's 2026-08-02 directive declares the
   governance phase complete and the RFC set authoritative; where a
   specification relies on an RFC's labeled recommendation it cites that
   RFC explicitly, and `TODO(blocked-by: acceptance ADR for RFC-XXXX)`
   marks the dependency. A consolidated acceptance ADR is a required
   governance follow-up outside this cycle (governance modification was
   excluded from this mission).
2. **D-01 remains unrecorded.** RFC-0001 deliberately carries no
   recommendation. Every identity-dependent statement in this corpus is
   BLOCKED, never assumed (CN-14).
3. **⚠ Spec home.** This corpus lives at `/specs` by explicit Maintainer
   instruction (2026-08-02). That operationally resolves U-3/D-13 toward
   the `specs/` home and supersedes both the recorded 2026-08-01
   `docs/specifications/` path and RFC-0003's T-A recommendation. A
   recording ADR is required; flagged in the PR. The empty `specs/fcos/`
   scaffold is left untouched pending that ADR.

## Conventions

- **Blocked sections:**
  `**BLOCKED** — missing: <exact requirement>; blocked by: <RFC/ADR/decision>; unblock: <event>`
  Blocked sections are complete sections: they state precisely what cannot
  be specified and why. No section is silently omitted.
- **No invented numbers.** Where no ratified document supplies a
  quantitative requirement, the Performance budgets section says so and is
  blocked rather than populated with plausible values.
- **IDs.** Files are `S<nn>-<name>.md`; clause-level IDs follow RFC-0002's
  recommended scheme (N-B+N-C) once its acceptance ADR exists;
  `TODO(blocked-by: acceptance ADR for RFC-0002)` until then.
- **Section order** is fixed corpus-wide: Scope · Responsibilities ·
  Interfaces · Data model · API contracts · State machines · Sequence
  flows · Error model · Security requirements · Performance budgets ·
  Observability requirements · Testing requirements · Acceptance criteria ·
  Traceability.

## Index

| File | Subsystem | Specifiability today |
| --- | --- | --- |
| S01-governance.md | S1 Governance | Full |
| S02-architecture.md | S2 Architecture | Full |
| S03-knowledge-system.md | S3 Knowledge System | Full |
| S04-language-definition.md | S4 Language Definition | Frame only (D-01) |
| S05-compiler.md | S5 Compiler | Obligations only (D-01, G-7) |
| S06-runtime.md | S6 Runtime | Obligations only (U-14) |
| S07-standard-library.md | S7 Standard Library | Obligations only (D-01) |
| S08-sdk.md | S8 SDK | Obligations frame |
| S09-developer-tools.md | S9 Developer Tools | Boundary only (contracts UNKNOWN) |
| S10-build-system.md | S10 Build System | Determinism frame |
| S11-package-manager.md | S11 Package Manager | Existence undecided (U-8) |
| S12-testing.md | S12 Testing | Architecture full; content blocked |
| S13-verification-conformance.md | S13 Verification & Conformance | Model full; suite blocked |
| S14-documentation-system.md | S14 Documentation System | Full |
| S15-release-distribution.md | S15 Release & Distribution | Gate frame (CI pending) |
| S16-ai-layer.md | S16 AI Layer | Full |
