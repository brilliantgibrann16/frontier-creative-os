# Public Conformance Claims Registry

**Specification:** S13 Verification & Conformance Subsystem (`S13#4.4`)  
**Governing ADR:** ADR-0015  
**Dispositions:** RFC-0004 (L-A + C-A), ADR-0004  

This directory serves as the immutable public registry of all official Conformance Claims asserted for Frontier Creative OS candidate implementations.

## Conformance Claim Architecture (S13#4.1–S13#4.4)

1. **Self-Certification Protocol (`S13#4.1`):** Conformance claims are issued via self-certification backed by published, reproducible evaluation reports.
2. **Claim Structure (`S13#4.2`):** Every claim record documents candidate name, commit SHA, release version, target specification version, harness hash digest, binary verdict (`CONFORMING` vs `NON_CONFORMING`), and evidence report digest.
3. **Immutability & Traceability (`S13#4.3`, `S13#4.4`):** Claims and accompanying evaluation reports are permanently archived; modifications or re-certifications require creating new claim records.

## Standing Claims Index

| Claim ID | Candidate | Release Version | Spec Version | Verdict | Commit SHA | Assertion Date |
|---|---|---|---|---|---|---|
| `CLAIM-FSL-1.0-TOOLS.COMPILER.FSL-0.1.0-STAGE1.WB` | `tools.compiler.fsl` | `0.1.0-stage1.wb` | `fsl/1.0` | `CONFORMING` | `688552a` | `2026-08-19T00:00:00Z` |
