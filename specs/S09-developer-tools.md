# S9 — Developer Tools Subsystem Specification

**Status:** In Review · **Subsystem:** S9 (Blueprint §2, "Not begun") · **Date:** 2026-08-02

## Scope

Editing, navigation, and diagnostics tooling operating via published
contracts. Scope ruling per RFC-0017: S9 covers tooling serving
engineering work on FCOS artifacts; a distinct end-user product surface
is not part of S9 (RFC-0017 recommends ruling U-A;
TODO(blocked-by: acceptance ADR for RFC-0017)).

## Responsibilities

- Consume only published contracts — grammar, AST, diagnostics — never
  implementation internals (Blueprint §8 syntax-tree/tooling contract).
- Report, never rule: tool output carries zero authority (Blueprint §6).
- Degrade gracefully when contracts evolve (versioned consumption).

## Interfaces

The tooling contract itself: **BLOCKED** — missing: published
grammar/AST/diagnostics contract forms ("UNKNOWN" in Blueprint §8);
blocked by: RFC-0001 + S4/S5 interface specs; unblock: those
ratifications.

## Data model

**BLOCKED** — same citation. (Tool-side models mirror the published
contracts; none exist.)

## API contracts

Tools are consumers, not publishers, of FCOS contracts; any tool that
publishes its own programmatic surface follows S8 rules for it.
Consumed-contract content: **BLOCKED** — same citation.

## State machines

Not applicable at subsystem level — no ratified document defines tool
lifecycle states; per-tool lifecycles are implementation concerns below
the specification line.

## Sequence flows

Frame: tool reads published contract version → operates on artifacts →
emits informative output → never writes into governed artifacts outside
the ordinary PR path. Content: **BLOCKED** as above.

## Error model

Obligation: a tool encountering contract-invalid input reports it as
informative diagnosis; it never "corrects" governed artifacts silently.
Taxonomy: **BLOCKED** pending contracts.

## Security requirements

Tools hold no elevated repository rights: their write path is the same
gated PR path as any contributor (INV-6, INV-19 analogue for tooling).

## Performance budgets

**BLOCKED** — missing: any ratified requirement; blocked by: contract
specs; unblock: post-contract tooling specs if ever needed.

## Observability requirements

Obligation: tool output must be distinguishable from authoritative
diagnostics surfaces once those exist. Concrete requirements: **BLOCKED**
pending diagnostics contract.

## Testing requirements

Contract-conformance tests against published contract versions (evidence
class); golden-file tests are legitimate evidence but never definitions
(INV-4). Content: **BLOCKED** pending contracts.

## Acceptance criteria

- Zero tools consuming implementation internals at any audit.
- Every tool declares which published contract versions it consumes.
- U-A/U-B scope ruling recorded before any product-UI-shaped work.

## Traceability

| Requirement source | Anchor |
| --- | --- |
| Contract-only consumption | Blueprint §8 (tooling contract), §3 (S9 dependency) |
| Zero authority | Blueprint §6; INV-4 analogue |
| Scope ruling | RFC-0017 (acceptance pending) |
| Blockage | U-9-adjacent contract unknowns; RFC-0001 |
