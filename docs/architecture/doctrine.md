# Frontier Creative OS — Universal Engineering Doctrine

**Status:** Ratified — adoption recorded as ADR-0002 (2026-08-02)
**Artifact class:** Doctrine — explanatory; defines WHY. Binds nothing by
itself; tagged CONSTRAINTS take effect only upon adoption recorded as an
ADR.
**Normative precedence:** Constitution > Architecture Baseline > Blueprint.
The Doctrine derives and explains; in any normative dispute it yields to
all three.
**Category discipline:** every statement is an AXIOM (AX-n), DERIVED
PRINCIPLE (DP-n), INVARIANT (INV-n, per Blueprint §12), CONSTRAINT (CN-n),
GUIDELINE (GL-n), OBSERVATION (OB-n), or UNKNOWN (U-n, per Blueprint §14).
Categories are never mixed within a statement.

---

## 1. Engineering Axioms

- **AX-1** Meaning must have exactly one authoritative source.
- **AX-2** Authority must be explicit, positional, and unidirectional.
- **AX-3** Every claim requires a judge distinct from the claimant.
- **AX-4** An artifact is trustworthy only to the degree it is traceable to
  a recorded decision.
- **AX-5** Systems outlive their authors; correctness must not depend on
  persons or memory.
- **AX-6** Change is continuous; evolution must use the same mechanism as
  operation.
- **AX-7** All contributors, human or artificial, are fallible; every
  contribution is untrusted until reviewed.
- **AX-8** Engineering capacity is finite; effort must be allocated in
  proportion to irreversibility.

The set is intended to be minimal and independent: removing any axiom
orphans at least one derived principle; no axiom is derivable from the
others. New axioms enter only by Doctrine amendment demonstrating that
existing axioms cannot derive the needed principle (**CN-32**).

## 2. Worldview

The ecosystem consists of artifacts carrying declared authority, claims
carrying none, and evidence linking them. The default posture toward any
unverified claim — in code, chat, documentation, or AI output — is
distrust. **DP-2** Trust attaches to artifacts, not authors. **CN-2** No
process may grant trust based on the identity or nature (human/AI) of the
author.

## 3. Systems and Architecture

A system is components, boundaries, and contracts, where all
inter-component effect passes through contracts. Boundaries exist to make
failure local and responsibility assignable. **DP-3** Every inter-subsystem
effect must traverse a published contract. **CN-3** No subsystem may be
added without declared boundaries, ownership, and forbidden
responsibilities.

Architecture is the set of decisions whose reversal cost is highest — the
structures that remain when all implementations are replaced. **DP-4**
Architecture documents contain only statements expected to survive
implementation turnover. **GL-1** When in doubt, place content in a
register, not the Baseline. **CN-4** A statement falsified by an
implementation change was misplaced and must be relocated, not defended.

## 4. Languages, Specifications, and Meaning

A language is a contract among all present and future producers and
consumers of programs, fixing which texts are valid and what they mean.
From AX-1: the language is its specification, never its implementation.
**DP-5** Multiple implementations are a health indicator because they force
the specification to carry the full contract. **CN-5** No language feature
may exist that is expressible only through one implementation's behavior.
**U-1** The identity of the Frontier Specification Language is UNKNOWN
(D-01); this doctrine asserts nothing that depends on the outcome.

Specification silence is a defect; labeled openness is a decision
(**DP-6**). **CN-6** No specification may be ratified with unlabeled
territory in scope. **GL-2** Prefer narrow scopes ratified completely over
broad scopes ratified partially.

Meaning is assigned, not discovered. Nothing in an implementation, test,
document, or AI output *is* meaning; at best each reflects it. **DP-7** Any
artifact asserting meaning without being a ratified specification is making
a claim, and claims are untrusted. **CN-7** No process may be created in
which meaning is inferred from implementation consensus. **OB-4** In the
current repository the meaning space is empty, not implicit in the
prototype.

## 5. Implementations and Conformance

An implementation is a claim of conformance: presumed defective until
proven, replaceable without loss of meaning, plural by expectation.
**DP-8** Implementation quality competes on everything the specification
does not fix, and nothing it does. **GL-3** Treat accidental observable
behaviors as compatibility hazards to minimize. **CN-8** No official
implementation may be designated "the reference" in a way that grants
defining authority (policy UNKNOWN, U-7).

Conformance is judged, never self-declared: the suite is a separate
artifact from any implementation's tests, derived clause-by-clause,
applicable to any implementation. **DP-9** A conformance finding is never
negotiable at the implementation level; the only appeals are "the test
mistraces the clause" (fix the test) or "the clause is wrong" (amend the
spec via the forward pass). **CN-9** Every normative clause carries at
least one traceable conformance test before its behavior may ship.

## 6. Verification, Validation, and Traceability

Verification checks an artifact against its governing artifact; it must be
mechanical wherever possible (**DP-10**, **GL-4**). **CN-10** No artifact
is exempted from verification by rank, urgency, or authorship.

Validation checks purpose and completeness; it cannot be mechanized because
purpose is decided, not computed. It lives at the human decision gates.
**DP-11** Validation authority follows decision authority. **GL-5** Every
validation gate publishes its checklist. **CN-11** No mechanical system,
including CI and AI, may be the final validator of purpose.

Traceability is the organization's memory, externalized: an unbroken chain
from shipped behavior to ratified clause to recorded decision. **DP-12**
Traceability that depends on human memory is absent at scale; it must be
structural and machine-checkable. **CN-12** Reference chains are part of
the artifact, not droppable metadata.

## 7. Governance and Decisions

Governance converts disagreement and uncertainty into recorded, binding,
supersedable decisions. Without it, decisions are made anyway — implicitly,
by whoever commits first. **DP-13** Every governance exception must cost
more in process than compliance would have, or exceptions become the
process. **CN-13** No decision path may bypass recording.

Decision effort is proportional to irreversibility (routing per Baseline
§8). Deferral is itself a decision and must be recorded as an UNKNOWN with
rationale, design space, and owning future artifact. **DP-14** A decision
made without the information it depends on is a deferred defect. **DP-15**
Recorded deferral preserves option value; premature choice destroys it.
**GL-6** Separate separable decisions. **CN-14** No unknown may be resolved
implicitly by shipping behavior that presumes an answer.

## 8. Knowledge and Documentation

Knowledge must be recorded to survive turnover (AX-5) but must never become
authority (AX-1, AX-2). **DP-16** Volatile content belongs in registers;
permanent content in ratified documents; misplacement in either direction
is a defect. **GL-7** Optimize knowledge for findability by strangers.
**CN-15** No knowledge tool may become a hard dependency of correctness;
the repository must always suffice for reconstruction.

Documentation must never be a second source of meaning; the shadow
specification is dangerous precisely because documentation is more readable
than specification and wins mindshare when they diverge. **DP-17**
Documentation quality is fidelity first, clarity second; a clear falsehood
is worse than an awkward truth. **GL-8** Regenerate rather than
hand-maintain wherever derivable. **CN-16** Documentation may never be
cited as authority in any conformance or review dispute.

## 9. Evolution, Compatibility, and Stability

A system with two change mechanisms routes all controversial change through
the fast path, and the formal mechanism becomes fiction. Evolution
therefore uses the identical forward pass as operation; correction is
supersession, never mutation. **DP-18** The absence of a second change
mechanism is a feature to be defended. **GL-9** Make the single mechanism
fast enough that no one needs a bypass; process latency is a security
property. **CN-17** No "experimental" or "temporary" channel may ship
observable behavior outside the forward pass.

Compatibility is a promise artifact living in ratified specifications and
release governance — never in implementation accidents. **OB-6** Absent
explicit promises, consumers depend on every observable behavior an
implementation exhibits. **DP-19** Anything shipped and observable will be
depended upon; ship deliberately or label deliberately. **CN-18** No
compatibility promise may be created, extended, or revoked by
implementation behavior. **U-6** The compatibility/stability policy is
UNKNOWN.

Stability is the guaranteed inverse relation between authority rank and
rate of change. **DP-20** Rank up implies churn down; violation of this
relation is an architectural alarm. **GL-10** Measure change rates per
rank. **CN-19** No process change may raise a higher rank's change rate
above a lower rank's.

## 10. Risk and Failure

Risk is dominated by irreversibility × ambiguity: the risks that matter
foreclose future correction — meaning drift, dialect divergence, authority
erosion, unrecorded decisions. **DP-21** Rank risks by irreversibility
first, probability second. **GL-11** Every critical risk names its
structural mitigation. **CN-20** No critical-class risk may be accepted
silently.

Failure is certain; the design variable is blast radius. Because authority
edges point one way, a failure below the meaning line can never rewrite
anything above it. Failure information re-enters as new forward passes.
**DP-22** Design so the direction of failure propagation is knowable in
advance; unknowable propagation is architectural debt. **GL-12** Incident
records state which boundary held and which was crossed. **CN-21** No
recovery procedure may repair a failure by crossing a boundary the failure
itself could not cross.

## 11. Humans, AI, and Authority

Humans are capable, fallible, and temporary: authority binds to roles,
correctness binds to artifacts and judges, and every process must be
operable by a competent stranger reading the record. **DP-23** Any process
only its author can operate is undone work. **GL-13** Onboarding cost is an
architecture metric. **CN-22** No individual may accumulate authority not
expressible as a named, transferable role.

AI participation is symmetric by design: fallibility is the ground truth
for humans and AI alike, so the gates are identical. Capability is never
authority — an AI that is right does not thereby decide. The design is
capability-independent: it requires no revision if AI systems become far
stronger, because it was never premised on their weakness. **DP-24** The
absence of a privileged AI interface is simultaneously a security property
and a fairness property. **CN-23** No future optimization may introduce an
AI-only channel into rank 1–5 artifacts, regardless of demonstrated
reliability. **OB-8** FCOS is itself evidence of the model: substantially
AI-produced, entirely human-ratified.

Authority must be explicit (findable in artifacts), positional (attached to
roles and ranks), and unidirectional (downward only); implicit, personal,
or bidirectional authority cannot be audited, transferred, or bounded.
Delegation is legitimate exactly because it is bounded and revocable.
**DP-25** Any authority not traceable to a ratified artifact does not
exist. **DP-26** Explanation is never permission: doctrine, docs, and
knowledge grant no rights. **CN-24** Every new authority enters only by
ratified artifact naming its bounds and revocation path.

## 12. Scale, Sustainability, and Economics

Every load-bearing element must be population-independent; what may scale
with population is throughput machinery, which is process, not
architecture. **DP-27** If a rule mentions a person, a count, or a tool, it
is process; if it mentions artifacts and relations, it may be architecture.
**GL-14** Grow throughput machinery reactively; grow structure only by
amendment. **CN-25** No scaling measure may introduce a second contribution
path.

Over decades, every person leaves, every tool is replaced. What survives is
plain, versioned, self-describing text under distributed version control.
**DP-28** Durability correlates with plainness. **GL-15** Prefer boring,
widely-implemented formats for authoritative artifacts. **CN-26** No
authoritative artifact may require proprietary or single-vendor tooling to
read.

Reversal cost dominates at the top of the hierarchy — which is why FCOS
built governance and architecture before code. Gates, records, and
traceability are capital expenditures: they cost now and pay every year the
system exists. **DP-31** Process weight must track reversal cost in both
directions — heavy where irreversible, light where cheap. **GL-17** When
effort competes, fund the artifact whose absence is irreversible first.
**CN-29** No efficiency measure may remove a record or gate whose value is
realized only in failure or turnover scenarios.

## 13. Architectural Mathematics and Information Flow

Let A be the set of artifacts and ⊑ ("is governed by") a relation on A. The
architecture asserts, as checkable properties: (1) ⊑ is a strict partial
order — the authority graph is a DAG; (2) every artifact except the
Constitution has exactly one primary governor; (3) legal information-flow
edges are consistent with ⊑; (4) conformance is set containment of
observable behavior within spec-defined territory; (5) traceability is
reachability from every shipped behavior to a decision. Each property
corresponds to a mechanical check (cycle detection, orphan detection, trace
closure) that CI can eventually enforce. **DP-29** Every architectural
claim should be expressible as a property of a finite graph. **CN-27**
Acyclicity of ⊑ is non-negotiable; any edge creating a cycle is rejected
structurally, before its merits are argued.

Information flows one direction because every artifact's correctness is
judged against the artifact above it; bidirectional authority would leave
no fixed judge and make conformance circular. **DP-30** Any channel moving
information upward while skipping the proposal gate is an authority leak,
whatever it is called. **GL-16** Review checklists name the reverse flows
explicitly. **CN-28** New channels (tooling, automation, AI pipelines) must
be classified as forward, feedback, or forbidden before activation.

## 14. Future Unknowns

An unrecorded unknown gets resolved by accident — by whoever ships first —
which is an unrecorded decision, the worst object in the system. Recording
unknowns converts them from hazards into scheduled work. The discipline:
never guess; record why the unknown matters; enumerate the design space
without choosing; name the future artifact that owns the answer. **DP-32**
The number of recorded unknowns is a health metric; the number of
unrecorded ones is the risk. **CN-30** No unknown may be resolved by
shipped behavior. The current registry is Blueprint §14 (U-1…U-14).

## 15. Invariants and Derivation Map

The twenty invariants INV-1…INV-20 (Blueprint §12) are adopted by reference,
unrestated, to avoid divergence between copies. Derivational closure:
INV-1…4 from AX-1/AX-3; INV-5, INV-19 from AX-7 with AX-2; INV-6, INV-7
from AX-4; INV-8, INV-18, INV-20 from AX-4/AX-6; INV-9 from AX-1/AX-5;
INV-10, INV-13 from AX-2; INV-11 from AX-1; INV-12 from AX-1; INV-14 from
AX-3; INV-15 from AX-5; INV-16, INV-17 from AX-3/AX-4. **CN-31** Amending
any invariant is a MAJOR architectural event requiring the full forward
pass.

Axiom → theory map: AX-1 → §4, §8; AX-2 → §7, §11, §13; AX-3 → §5, §6,
§13; AX-4 → §6, §7, §14; AX-5 → §11, §12; AX-6 → §9, §10; AX-7 → §2, §10,
§11; AX-8 → §3, §7, §9, §10, §12.

## 16. Consistency and Completeness

- No contradictions with Constitution v1, ADR-0001, the Baseline, or the
  Blueprint were found during doctrine construction.
- Article 2's "intelligent systems … as first-class participants" is
  interpreted as first-class *participation*, never first-class
  *authority* — consistent with L-5 and INV-19. This is an interpretation,
  not a quotation, and is flagged for Maintainer confirmation at adoption.
- Statement census: 8 axioms (closed set), 32 derived principles, 20
  invariants (by reference), 32 constraints, 17 guidelines, 8 observations,
  14 standing unknowns (by reference).
- Deliberately open: everything downstream of D-01; quantitative methods;
  multi-maintainer procedure (U-11); the formal semantics of the language
  (future specification territory, permanently outside doctrine scope).