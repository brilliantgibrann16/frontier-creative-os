# Conformance Frame

- Status: Frame only (Wave 0, program P12) — no conformance judgment is possible yet
- Artifact class: program documentation (non-normative; restates accepted dispositions only)
- Governing artifacts: RFC-0004 (frame accepted per ADR-0004: options L-A + C-A), Blueprint INV-16 (single conformance judge).

## 1. What is accepted today

- The RFC-0004 conformance **frame** — the labeling model L-A and checking approach C-A — as recorded in ADR-0004. This document does not expand or reinterpret those options; RFC-0004 and ADR-0004 remain the authoritative statements.
- INV-16: there is exactly one conformance judge. No parallel or competing source of conformance judgments may be created.

## 2. What explicitly does not exist yet
 
- Conformance harness implementation, fixture corpus, and official judgments (packages P12.2–P12.4): unblocked by S13 ratification (ADR-0015) and scheduled for execution under P12.
- No conformance levels or versioning beyond what ADR-0004 records.

## 3. Blocking conditions

| Item | Blocked by | Status |
| --- | --- | --- |
| S13 Specification Ratification | G-SPEC(S13), B-08 | ✅ MET (ADR-0015) |
| Conformance harness implementation (P12.2) | S13 ratification | Unblocked (Ready for execution) |
| Fixture corpora (P12.3) | Harness + ratified clauses | Unblocked |
| Official judgments & claims (P12.4) | Harness + Fixtures + S13 Judge | Unblocked |

## 4. Non-duplication rule

This note deliberately does not restate S13 (In Review). When S13 is ratified, S13 governs conformance content; this document then records program-level status only.
