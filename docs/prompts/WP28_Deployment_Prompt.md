# WP28 — Deployment Prompt

Class: Derived-executable. Governing anchors: Blueprint S15 (Release &
Distribution), §9 (Testing ↔ Release trust boundary), Constitution
Article 9, Baseline §9 step 10, §10 (release row); U-8, U-12.

## Mission

Engineer the release and distribution function of FCOS: how gate-checked
versions are assembled, published, and superseded — within the ratified
constraint that no production release may occur before continuous
integration exists for the test suite (Article 9).

## Objectives

1. Define the release gate sequence from ratified sources: Article 9
   gates; conformance suite green (Baseline §10); traceability audit
   (every shipped behavior → ratified clause, INV-17; every significant
   decision → ADR); release notes enumerating changes (immutable after
   publication, Blueprint §7).
2. Define release classes from ratified text: dev/alpha/nightly/internal
   builds are permitted pre-CI; production releases are not (Article 9
   as amended in PR #9 review).
3. Define supersession mechanics: releases are superseded, never mutated;
   yanked packages follow the package lifecycle (Blueprint §7) — details
   TODO(blocked-by: U-8).
4. Specify the CI prerequisite work item: CI platform and gate encoding
   TODO(blocked-by: U-12); CI enforces declared gates and never makes
   policy (L-10, INV-10).
5. Distribution channels: TODO(blocked-by: U-8, D-01).

## Outputs

- Release process document (Implementation Plan class; binding elements
  already live in Constitution/Baseline — this document only assembles
  them operationally).
- CI prerequisite Issue with gate inventory attached.

## Constraints

- No deployment infrastructure, packaging formats, or channel tooling
  may be selected now (U-8, U-12).
- Gate bypasses are recorded one-time exceptions, never process (INV-20,
  DP-13).
- Only CI results are admissible evidence at the release boundary
  (Blueprint §9).

## Failure Modes and Recovery

- Gate erosion under release pressure: named illegal reverse flow;
  recovery is halt + recorded exception or gate satisfaction.
- Shipped-but-untraceable behavior: release blocker per INV-17; recovery
  is revert or retroactive forward pass ordered by the Maintainer.

## Acceptance Criteria

- Every gate in the sequence cites its ratified source.
- Pre-CI release classes match Article 9's ratified wording exactly.

## Completion Checklist

- [ ] Gate sequence assembled with citations
- [ ] Release class table drafted
- [ ] Supersession/yank mechanics outlined with U-8 markers
- [ ] CI prerequisite Issue filed (U-12)
