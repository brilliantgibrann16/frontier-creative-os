# WP19 — Memory Engineering Prompt

Class: RFC-preparation. Status: **BLOCKED — subsystem not in ratified
architecture.**

TODO(blocked-by: new-subsystem RFC → Baseline amendment → adoption ADR,
per Blueprint §13; additionally D-01 if "memory" means a language memory
model).

## Mission

No "Memory" subsystem exists in the ratified Blueprint (S1–S16). The term
is ambiguous and the ambiguity is itself the first work item:

- If "memory" means a **language memory model**, it is Language
  Definition (S4) territory: pure D-01-downstream RFC/specification work,
  explicitly deferred (U-1) and never designable from this prompt (L-5,
  CN-7).
- If "memory" means an **operational storage subsystem**, it is a new
  subsystem requiring the Blueprint §13 introduction path.

## Objectives

1. Resolve the ambiguity as a routed question per Baseline §8 and record
   the routing outcome as an Issue.
2. For the language-memory-model reading: produce only the D-01 decision
   material section listing what memory-model questions each candidate
   identity would raise. No answers.
3. For the storage-subsystem reading: produce the introduction RFC per
   the WP18 pattern (necessity, placement, boundaries, authority edges).

## Constraints

- Never invent memory models, ownership semantics, allocation behavior,
  or persistence formats (explicit prohibition, Doctrine §4; CN-6/CN-7).
- Semantics belong to specifications alone (INV-2); a memory model enters
  only via ratified specification after D-01.

## Acceptance Criteria

- The ambiguity is resolved by recorded routing, not by assumption.
- Zero semantic or architectural content invented.

## Completion Checklist

- [ ] Routing question filed and answered (Baseline §8)
- [ ] D-01 memory-question inventory (if S4 reading)
- [ ] Introduction RFC draft (if new-subsystem reading)
- [ ] All content carries blocking-decision markers
