# Engineering Prompt Library

**Artifact class:** Engineering Prompt (ratified by ADR-0003; derived,
informative, zero authority).

Every prompt in this directory is derived from the ratified corpus:
Constitution v1, Architecture Baseline v1, Master System Blueprint,
Universal Engineering Doctrine, and Accepted ADRs. Prompts direct work;
they never define architecture, meaning, or decisions. Outputs produced by
executing a prompt acquire authority only through the forward pass
(Issue → RFC → ADR → Specification → implementation → review).

## Conventions

- Gaps are marked `TODO(blocked-by: <decision>)` and are never filled by
  invention (CN-14, CN-30).
- A prompt that contradicts a ratified document is defective and is
  revised toward the ratified document (ADR-0003 conflict rule).
- Prompts come in two classes:
  - **Derived-executable** — the target subsystem exists in Blueprint
    §2 (S1–S16); the prompt directs engineering work now.
  - **RFC-preparation** — the target subsystem is *not* in the ratified
    Blueprint; per Blueprint §13 a subsystem enters only via RFC →
    Baseline amendment → ADR. The prompt directs production of that RFC
    and forbids implementation until adoption.

## Index

| # | Prompt | Class | Governing anchor | Blocking decisions |
| --- | --- | --- | --- | --- |
| WP15 | Architecture Completion | ⚠ see note | Baseline §1–§13 | — |
| WP16 | System Contracts | Derived-executable | Blueprint §8 | U-9, D-01 (partial) |
| WP17 | Runtime Engineering | RFC-first (S6 exists; scope UNKNOWN) | Blueprint S6, U-14 | D-01 |
| WP18 | Planner Engineering | RFC-preparation | Blueprint §13 | New-subsystem RFC + Baseline amendment |
| WP19 | Memory Engineering | RFC-preparation | Blueprint §13 | New-subsystem RFC + Baseline amendment |
| WP20 | Context Engine | RFC-preparation | Blueprint §13 | New-subsystem RFC + Baseline amendment |
| WP21 | Agent Framework | RFC-preparation | Blueprint S16, §13 | New-subsystem RFC; INV-19/CN-23 bounds |
| WP22 | Knowledge Pipeline | Derived-executable | Blueprint S3/S14 | — |
| WP23 | UI Architecture | RFC-preparation (S9 partial) | Blueprint S9, §13 | Scope ruling: developer tools vs product UI |
| WP24 | API Engineering | Derived-executable | Blueprint S8 | D-01 (surface content) |
| WP25 | Observability | Derived-executable (cross-cutting) | Baseline §4, U-12 | U-12 |
| WP26 | Testing | Derived-executable | Blueprint S12/S13, Baseline §10 | D-04/U-5 (levels) |
| WP27 | Benchmark | Derived-executable (methodology only) | Doctrine DP-8 | D-01 (workloads) |
| WP28 | Deployment | Derived-executable | Blueprint S15, Article 9 | U-8, U-12 |
| WP29 | Optimization | Derived-executable (methodology only) | Baseline L-3 | D-01, ratified specs |
| WP30 | Final System Audit | Derived-executable | Doctrine §13 | — |

## ⚠ WP15 conflict note (flagged for Maintainer)

`WP15_Architecture_Completion_Prompt.md` (Maintainer-authored) enumerates
subsystems — Planner, Agents, UI, Storage, Authentication, Plugin System,
Search, Execution Engine, Telemetry — that do not appear in the ratified
Blueprint decomposition (S1–S16). Per the adopted precedence order
(ADR-0002), the Baseline and Blueprint prevail. Executing WP15 therefore
means: inventory the ratified S1–S16, and treat every non-Blueprint
subsystem as an RFC candidate under Blueprint §13 (see WP18–WP21, WP23).
WP15 itself is not modified here; its revision is a Maintainer edit.
