# Conformance Frame

- Status: Frame only (Wave 0, program P12) — no conformance judgment is possible yet
- Artifact class: program documentation (non-normative; restates accepted dispositions only)
- Governing artifacts: RFC-0004 (frame accepted per ADR-0004: options L-A + C-A), Blueprint INV-16 (single conformance judge).

## 1. What is accepted today

- The RFC-0004 conformance **frame** — the labeling model L-A and checking approach C-A — as recorded in ADR-0004. This document does not expand or reinterpret those options; RFC-0004 and ADR-0004 remain the authoritative statements.
- INV-16: there is exactly one conformance judge. No parallel or competing source of conformance judgments may be created.

## 2. What explicitly does not exist yet

- No conformance harness, no fixture corpus, no official judgments (packages P12.2 and beyond): **blocked by G-SPEC(S13) and B-08** — the specifications, including S13, are In Review and unratified, so there are no ratified clauses to judge against.
- No conformance levels or versioning beyond what ADR-0004 records.

## 3. Blocking conditions

| Item | Blocked by |
| --- | --- |
| Conformance harness implementation | G-SPEC(S13), B-08 |
| Fixture corpora | Harness + ratified clauses |
| Official judgments | All of the above + INV-16 judge designation |

## 4. Non-duplication rule

This note deliberately does not restate S13 (In Review). When S13 is ratified, S13 governs conformance content; this document then records program-level status only.
