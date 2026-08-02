# WP23 — UI Architecture Prompt

Class: RFC-preparation (partial S9 overlap). Status: **BLOCKED for
product UI; narrowly executable for S9 Developer Tools.**

TODO(blocked-by: Maintainer scope ruling — developer tooling (S9) vs
product UI (new subsystem, Blueprint §13 path)).

## Mission

The ratified Blueprint contains no product/end-user UI subsystem. The
nearest ratified home is S9 Developer Tools: editing, navigation,
formatting, and diagnostics presentation via published contracts
(Baseline §4). This prompt covers the S9-scoped work that is legal now
and routes everything else to an introduction RFC.

## Objectives

1. Obtain the scope ruling (Baseline §8 routing): is the requested "UI"
   S9 tooling, or a new subsystem?
2. S9-scoped (executable after D-01 and tooling-contract specs exist):
   inventory which published contracts tools require (grammar, AST,
   diagnostics — never implementation internals, Baseline §4) and
   produce the tooling-contract requirements input to WP16.
3. New-subsystem-scoped: introduction RFC per the WP18 pattern.

## Constraints

- Tools must never accept or reject programs differently from the
  specification — dialect creation is a forbidden responsibility
  (Baseline §4, P-2).
- No visual design, frameworks, or interface layouts may be produced
  under this library; those are implementation-plan territory after
  ratified scope exists.
- Tooling consumes published contracts only; contracts are
  TODO(blocked-by: D-01, grammar/AST RFCs).

## Acceptance Criteria

- Scope ruling recorded before any further work.
- S9 requirements contain zero dependencies on implementation internals.

## Completion Checklist

- [ ] Scope ruling filed and answered
- [ ] S9 tooling-contract requirements delivered to WP16 (if S9 scope)
- [ ] Introduction RFC draft (if new-subsystem scope)
- [ ] Dialect-prevention constraint check passed
