# Bismillah ir-Rahman ir-Rahim

# R0273 -- BSSG: An Evidence-Independent Control Plane for Bounded Artificial Agency

**Chronological Index:** 351 of 995  
**Date:** 2026-07-25  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md.txt  
**Source Format:** txt  
**SHA-256:** `e4afaaad5ba19808e173159e3245fcd33d5e16871944a79cccc3f40a96905a9d`  

---

## R0273 · BSSG: An Evidence-Independent Control Plane for Bounded Artificial Agency

- section: V. BSSG & SHVVP Protocols
- source_file: BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md.txt
- source_format: txt
- merged_variants: 4 (BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md)
- text_sha256: e4afaaad5ba19808e173159e3245fcd33d5e16871944a79cccc3f40a96905a9d

# BSSG: An Evidence-Independent Control Plane for Bounded Artificial Agency

**Version:** v0.1 DRAFT
**Status:** DRAFT / NOT CARRIED / NOT PUBLICATION-READY
**Document class:** architecture and conformance specification
**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**AI producer disclosure:** this first draft was assembled by an AI producer agent (Claude, Anthropic) operating inside Perplexity Computer, from a source-grounded evidence report and four independent AI council seat reports (Claude Opus 5, GPT 5.6 Sol, Gemini 3.1 Pro, GLM 5.2). No council seat approved this text. Seat verdicts on the pre-draft material were: Claude Opus 5 HALT-WITH-FINDINGS, GPT 5.6 Sol HALT pending normative repair, Gemini 3.1 Pro CONDITIONAL APPROVAL, GLM 5.2 CONDITIONAL APPROVAL.
**License recommendation:** CC-BY-4.0 for this paper, Apache-2.0 for the accompanying code. No LICENSE file is shipped in this first-draft packet, therefore no grant of license is made by this document.
**Date of draft:** 2026-07-25

---

## Abstract

BSSG (Bounded Structural Safety Gate) is a control plane whose purpose is to make the set of consequential effects an artificial agent can actually cause a function of externally held evidence rather than a function of the agent's own account of itself. This document specifies the architecture: a frozen five-conjunct authorization kernel, an atomic commit protocol wrapped around that kernel, a three-valued decision semantics in which UNKNOWN is never satisfied, an authority lattice in which witness degradation narrows authority monotonically, six record schemas, a set of cross-record invariants, conformance profiles, and a runnable reference gate with an exhaustive kernel truth-state suite and an adversarial suite.

This document makes no effectiveness claim of any kind. It does not assert that a BSSG deployment achieves safety, security, harm-reduction, or superiority over any alternative. Every property in Section 22 is stated at one of four claim levels: enforced by the reference gate, detectable with evidence, assumed, or out of model. Empirical questions belong to the Structural Honesty Validation Protocol (SHVVP) v0.8 ([Zenodo record 21583202](https://zenodo.org/records/21583202)) and to the downstream XZ Protocol, XZ Empirical, and CVE-Bench work, none of which has produced results that this document may cite.

The specification's defensible content is therefore narrow and, we argue, exactly as narrow as it should be: a decidable admission function, a commit protocol that closes the interval between decision and effect, a record format that makes each of those decisions offline-checkable, and an explicit register of the things the architecture cannot do.

---

## 1. Status, claim boundary, and prohibited language

### 1.1 Status

This is a FIRST DRAFT. It is **DRAFT / NOT CARRIED / NOT PUBLICATION-READY**. It has not been carried by an independent non-producer implementation, has not been deposited, and has not been approved by any council seat. Two of the four council seats returned HALT-class verdicts on the pre-draft material and their blocking findings are reproduced, dispositioned, and in some cases still open in `BSSG_v0_1_DECISION_REGISTER.md`.

### 1.2 Claim boundary

BSSG v0.1 is an architecture-and-conformance document. Conformance to this specification is a statement about a named deployment's implementation of a mediation semantics inside a declared boundary, at a named profile, against a named adversary class. It is never a statement about outcomes.

The specification therefore makes no claim that a conformant deployment reduces, prevents, mitigates, or bounds any real-world harm; no claim about attacker success rates; no claim of superiority over any baseline; and no claim that the architecture generalizes beyond its declared boundary. Whether BSSG changes anything measurable is an empirical question, reserved to SHVVP and its successors, and no data exists at the time of this draft.

Following the drafting convention inherited from SHVVP, a scope limit MUST appear in the same sentence as the claim it limits. "BSSG-conformant" as an unqualified phrase is PROHIBITED; a conformance statement MUST name the profile, the deployment, the declared mediation boundary, and the adversary class.

### 1.3 Prohibited sentences

<!-- PROHIBITED-PHRASE-REGISTRY: the phrases below are listed as forbidden. Scanners MUST skip lines carrying this marker. -->

The following sentences and their paraphrases MUST NOT appear in any BSSG document, marketing text, README, commit message, or deposit abstract: <!-- PROHIBITED-PHRASE-REGISTRY -->

1. "BSSG prevents harm." <!-- PROHIBITED-PHRASE-REGISTRY -->
2. "BSSG makes agents safe." <!-- PROHIBITED-PHRASE-REGISTRY -->
3. "BSSG reduces unauthorized effects." <!-- PROHIBITED-PHRASE-REGISTRY -->
4. "BSSG outperforms" any named or unnamed alternative. <!-- PROHIBITED-PHRASE-REGISTRY -->
5. "BSSG is validated", "BSSG is proven secure", "BSSG guarantees safety". <!-- PROHIBITED-PHRASE-REGISTRY -->
6. "BSSG prevents equivocation" absent a named trusted primitive that does so. <!-- PROHIBITED-PHRASE-REGISTRY -->
7. "BSSG tolerates witness failure." Witness failure is converted into denial, which is a cost, not a tolerance. <!-- PROHIBITED-PHRASE-REGISTRY -->
8. "BSSG preserves capability" without the conditional "under evidence-plane health". <!-- PROHIBITED-PHRASE-REGISTRY -->

The accompanying verifier `verify_bssg_v0_1.py` scans the package for these phrases and FAILS the package if any appears outside this registry.

### 1.4 Claim levels

Every property, obligation, and mechanism in this document carries exactly one of four claim levels:

| Level | Meaning |
|---|---|
| **ENFORCED** | Enforced by the reference gate `bssg_gate.py` on the records it processes, given its inputs. Enforcement is relative to the code, not to a deployment. |
| **DETECTABLE** | Not prevented. A violation leaves evidence that a specified checker can find, given that the evidence is actually collected and examined. |
| **ASSUMED** | An assumption about the deployment or the environment. It can be reviewed and it can be refuted; it cannot be established by this architecture. |
| **OUT OF MODEL** | Outside the architecture entirely. BSSG says nothing about it and any claim made about it from BSSG is invalid. |

Auditing is a precondition of every DETECTABLE claim. As Crosby and Wallach state, "Tamper-evidence requires auditing. If the log is never examined, then tampering cannot be detected." ([Crosby and Wallach, USENIX Security 2009](https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf)).

---

## 2. Lineage

BSSG occupies a specific position in a declared program chain:

```
AX-SH 5  ->  SHUDP  ->  SHVVP  ->  BSSG Canonical Spec  ->  XZ Protocol + Corpus  ->  XZ Empirical  ->  CVE-Bench  ->  Mythos-Class
```

- **AX-SH 5**, "Is Evidence Independence an Axiom? Decomposing a Proposed Extension to AX-SH" ([DOI 10.5281/zenodo.21539074](https://doi.org/10.5281/zenodo.21539074)), states that acting-system-independent evidence generation (A5.1) "is not derivable and is stated as Axiom 5 (Evidence independence) over a control predicate (WithinAuth), with a finite countermodel establishing independence from A1-A4". The same record states that "Causal gating (A5.2) is relocated as a proposed control principle for a control layer rather than the axiom set" and that "the recording/escalation half of A5.3 is preserved as an open operational requirement" ([AX-SH 5](https://doi.org/10.5281/zenodo.21539074)). BSSG is the control layer that inherits those relocated obligations. AX-SH 5 also declares that "All proofs are finite model-theoretic paper proofs verified by clause-by-clause enumeration; no machine-checked verification is claimed" ([AX-SH 5](https://doi.org/10.5281/zenodo.21539074)); BSSG inherits that honesty requirement about its own proof status.
- **SHUDP** ([Zenodo record 21522932](https://zenodo.org/records/21522932)) supplies the upstream disclosure and documentation protocol under which this program operates.
- **SHVVP v0.8** ([Zenodo record 21583202](https://zenodo.org/records/21583202)) is the frozen preregistration instrument. Its record states a "three-trust-root universe-commitment design (commitment authority, independent pre-commitment anchor, run logger; no runtime key override; signed and resolved commitment identifiers)", "an adversarial regression suite (35 checks), and a producer self-check verifier (10 gates)", a manifest digest of `f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c`, and that it was "Independently carried by two executing non-producer model families of different vendors (Kimi / Moonshot AI and Qwen / Alibaba)" ([SHVVP v0.8](https://zenodo.org/records/21583202)).
- **BSSG** (this document) is the architecture-and-conformance layer.
- **XZ Protocol and Corpus, XZ Empirical, CVE-Bench, Mythos-Class** are downstream and are future work. No result from any of them may be cited by this document, and none is cited.

**A structural warning inherited from the Claude Opus 5 seat, absorbed here as normative.** SHVVP's executable maturity is in the evidence-scoring plane, not the enforcement plane. The five kernel conjunct names appear in SHVVP prose but SHVVP ships no runtime authorization monitor. BSSG therefore begins with an implementation deficit, not an implementation surplus. This document MUST NOT cite SHVVP's "35 checks" or its three trust roots as evidence that a BSSG gate is engineered. To reduce a terminology collision, this document says **kernel**, **decision point**, or **broker**, and reserves "gate" for the reference implementation file name.

---

## 3. Terminology and normative language

### 3.1 RFC 2119 / RFC 8174 usage

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, and OPTIONAL in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals. Lowercase uses of these words carry their ordinary English meaning and impose no requirement.

### 3.2 Defined terms

- **Subject.** The acting system (an artificial agent or a process acting for one). The subject is untrusted for every derived fact.
- **Consequential effect.** An operation in a contract's closed effect registry whose completion can mutate, disclose, transmit, deploy, authorize, spend, publish, or irreversibly release a protected resource.
- **Mediation boundary.** The enumerated subjects, effect types, adapters, resources, transports, and channels over which a conformance claim is made. A claim outside the boundary is invalid.
- **Decision point.** The component that recomputes the five conjuncts and issues or refuses an authorization receipt.
- **Enforcement point.** The component that redeems a commit token and performs the effect through a registered adapter.
- **Witness.** A component that emits signed receipts about its own observed state and its coverage of a subject. A witness is not an oracle of truth.
- **Established.** Validated from admissible raw evidence under the frozen trust and freshness policy. Absence, invalidity, unverifiability, scope mismatch, or evaluator error is NOT establishment.
- **UNKNOWN.** A required fact that is neither established TRUE nor established FALSE. UNKNOWN is not "probably false", not "not observed", and not "clean". RFC 6960 supplies the three-valued precedent: "the 'revoked' status indicates that a certificate with the requested serial number should be rejected, while the 'unknown' status indicates that the status could not be determined by this responder" ([RFC 6960](https://www.rfc-editor.org/rfc/rfc6960.html)). Note that RFC 6960 assigns the disposition of `unknown` to the client; BSSG's rule that UNKNOWN is never satisfied is therefore a policy overlay consistent with, but not mandated by, RFC 6960.
- **Authority.** The set of capabilities currently redeemable by a subject, including constraints on effect type, target, parameters, and validity window. Following Miller, authority rather than permission is the quantity to bound: "Permission is relative to a frame of reference. Authority is invariant." ([Miller, Robust Composition](http://www.erights.org/talks/thesis/markm-thesis.pdf)).
- **Authority epoch.** A monotone non-decreasing counter incremented on every change to the authority ceiling. Authorizations bind an epoch; a commit under a different epoch MUST fail.
- **Commit token.** A one-time, non-transferable redemption token bound to a specific authorization receipt.
- **WithinAuth.** The control predicate of AX-SH 5 over whether a record's generation lies inside or outside the acting system's authority ([AX-SH 5](https://doi.org/10.5281/zenodo.21539074)). In BSSG it is carried as a declared assessment on a witness receipt, never derived from a signature.

---

## 4. Problem

An autonomous or semi-autonomous software agent, whose internal reasoning is not reliably legible and whose stated intentions are not a reliable predictor of its actions, is granted the ability to cause consequential effects outside itself. BSSG addresses one question:

> By what architecture can the set of effects an agent can actually cause be made a decidable function of externally held evidence, rather than a function of the agent's own account of itself?

Three words are load bearing. **Decidable** commits BSSG to a monitor that terminates with a verdict on every request, which in turn constrains which properties BSSG may claim; Schneider requires that "any execution rejected by an enforcement mechanism must be rejected after a finite period" ([Schneider, Enforceable Security Policies](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)). **Externally held** is the architectural bet, and is exactly AX-SH 5's Axiom 5 over `WithinAuth`. **Effects** rather than intentions or beliefs fixes the object of control.

BSSG is not an alignment mechanism, a deception detector, an intent classifier, or a limiter on reasoning. Attestation and provenance systems describe and support appraisal of states and events; they do not by themselves mediate effects. RFC 9334 separates Attester, Verifier, and Relying Party and treats appraisal as input to a relying-party decision, not as execution control ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)). SLSA describes how an artifact was produced ([SLSA v1.0 levels](https://slsa.dev/spec/v1.0/levels)); in-toto supplies signed supply-chain metadata and layout verification ([in-toto, USENIX Security 2019](https://www.usenix.org/system/files/sec19-torres-arias.pdf)). None of these is a universal policy enforcement point for agent effects. BSSG's contribution, if any, is the enforcement placement and the record discipline, not the cryptographic primitives, which are all borrowed.

---

## 5. Design goals and non-goals

### 5.1 Goals

G1. Every consequential effect inside a declared mediation boundary SHALL be reachable only through a decision point that recomputes all five kernel conjuncts from raw evidence.
G2. The decision function SHALL be total, three-valued, and deny-by-default. Saltzer and Schroeder: "Base access decisions on permission rather than exclusion... the default situation is lack of access" ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)).
G3. Authorization SHALL bind to canonical request bytes and to the exact evidence snapshot, and SHALL be redeemable at most once.
G4. Degradation of witness state SHALL narrow authority and SHALL NOT widen it.
G5. Every decision, commit, and correction SHALL be offline-checkable from the emitted records alone.
G6. The specification SHALL be public and SHALL NOT depend on the ignorance of an attacker: "The design should not be secret" ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)).
G7. The kernel SHALL be small enough to be subject to analysis and tests, per the reference-validation-mechanism requirements "always invoked (i.e., complete mediation), tamperproof, and small enough to be subject to analysis and tests" ([NIST CSRC glossary](https://csrc.nist.gov/glossary/term/reference_monitor)).

### 5.2 Non-goals

N1. BSSG does not evaluate the semantic content of a permitted effect. A permitted effect type to a permitted target with an adversarial payload is allowed. BSSG mediates authority, not meaning.
N2. BSSG does not model the subject's internal states.
N3. BSSG does not provide availability. Fail-closed converts evidence-plane failure into denial.
N4. BSSG does not define new cryptographic primitives, a new transparency log format, or a new provenance format. It SHOULD adopt existing ones.
N5. BSSG does not measure anything. Measurement is SHVVP's estimand.

---

## 6. Threat model and adversary lattice

### 6.1 Assets

Effect authority; credentials; target resources; contract and policy state; witness keys and witness state; evidence; authorization receipts and commit tokens; execution journals; lineage graphs; correction state; and recovery authority.

### 6.2 Adversary lattice

Profiles and property claims are indexed by adversary class. A class subsumes all lower classes.

| Class | Capability | Notes |
|---|---|---|
| **A1** | Full control of the subject: prompts, memory, tool arguments, all untrusted request fields, and unlimited request volume | The baseline adversary |
| **A2** | A1 plus network position: reorder, delay, drop, and replay messages; degrade or silence the witness; manipulate name resolution | Denial of service is always available to this class ([TUF spec](https://theupdateframework.github.io/specification/latest/)) |
| **A3** | A2 plus compromise of one witness or one evidence producer | Single-witness collusion is invisible to the kernel (Section 22.5, Section 27) |
| **A4** | A3 plus compromise of the executor host, local clock, or storage, including restore-from-backup | Rollback and freeze attacks live here ([TUF spec](https://theupdateframework.github.io/specification/latest/)) |
| **A5** | A4 plus collusion at or above the trust-root threshold, or compromise of the decision point itself | Total collapse. No graceful degradation exists |

Byzantine bounds apply to any quorum construction BSSG uses: "no solution with fewer than 3m + 1 generals can cope with m traitors" for oral messages, while "THEOREM 2. For any m, Algorithm SM(m) solves the Byzantine Generals Problem if there are at most m traitors" for signed messages ([Lamport, Shostak and Pease](https://lamport.azurewebsites.net/pubs/byz.pdf)); and "The resiliency of our algorithm is optimal: 3f+1 is the minimum number of replicas that allow an asynchronous system to provide the safety and liveness properties when up to f replicas are faulty" ([Castro and Liskov, PBFT](http://pmg.csail.mit.edu/papers/osdi99.pdf)). Both results assume independent failures: "We assume independent node failures." ([Castro and Liskov](http://pmg.csail.mit.edu/papers/osdi99.pdf)). Correlated or colluding components violate that assumption directly, and BSSG MUST state its quorum threshold together with its independence assumption rather than as a bare number.

### 6.3 Out of the threat model

Covert and side channels; the semantic correctness of adapters; malicious targets; physical channels; human operators acting within their authority; and cryptographic breaks. Miller's exclusion is inherited verbatim in kind: "Since this dissertation examines only models, not implementations, we ignore covert and side channels." ([Miller](http://www.erights.org/talks/thesis/markm-thesis.pdf)).

**Same-process object access (decision-point compromise).** The reference gate's immutability properties are scoped to the **API surface** (this is a structural property of the reference implementation under the stated threat model, not an assurance of any outcome): an actor that calls `authorize`, `commit`, or `submit_amendment` and holds only their return values cannot substitute a bound effect, replay a consumed token, or rewrite an audit record, because inputs are snapshotted into fresh built-in objects at the boundary and every returned/stored record is a deep copy. This is distinct from an actor that holds a direct in-process reference to the gate's private state (`gate.state.tokens`, `gate.state.records`) and mutates those objects' attributes. No in-process reference monitor can defend its own heap from code sharing its address space; such an actor is **already at or above adversary tier A5 (compromise of the decision point itself)** and is out of the threat model by construction. A deployment obligation (BSSG-H) is that the decision point runs in an isolation domain the mediated agent cannot address directly. The repaired property is therefore "API-surface immutability," not "same-process object immutability," and is stated as such rather than overclaimed.

**Trusted injected dependencies.** The clock, signature verifier, and token factory are part of the decision point's trusted computing base, injected at construction. A dependency that returns malformed or adversarial output (a non-monotonic clock, a verifier that mis-signs, a factory that emits a malformed token, or one that re-enters the gate) is a decision-point compromise, not a mediated-agent capability. The gate applies cheap defensive checks where practical (a re-entrant call is refused; a non-Boolean verifier result is treated as not-valid; a non-string token id aborts), but the general case is A5 and out of model.

**Indeterminate outcomes and terminality (`DENY_UNKNOWN`).** `DENY_UNKNOWN` is the indeterminate outcome: the decision point could not establish that all five conjuncts hold, because a trusted evaluator was unavailable or the supplied evidence was malformed. Every deny -- `DENY_FALSE` and `DENY_UNKNOWN` alike -- is **terminal for its `(request, nonce)` snapshot**: the snapshot is recorded and the nonce is consumed, so the identical submission cannot be re-evaluated (a repeat is `E-REQUEST-DENIED-TERMINAL` or `E-NONCE-REPLAY`). This upholds no-allow-after-deny uniformly and matches the state machine's terminal `DENY`. A transient fault does not permanently foreclose the caller's *intent*: because the nonce is part of the snapshot, a retry submitted as a fresh request (fresh nonce) is a distinct snapshot that re-evaluates cleanly and may `ALLOW` once the fault clears. There are two abort shapes. (1) A **post-admission abort** -- a trusted evaluator or the token factory raised AFTER structural admission and nonce consumption -- records a terminal `DENY_UNKNOWN` for its own snapshot and consumes its nonce, and it **does not roll back any authenticated, security-monotonic authority/epoch state** it had already established: an authenticated monotonic advance or narrowing is a security fact that MUST survive a later token-mint failure so it continues to invalidate older, wider grants (rolling it back could revive a superseded grant). Only issuance is incomplete, and it committed nothing; the abort record preserves the evaluated conjuncts and the surviving authority epoch and ceiling. The nonce is deliberately **not** rolled back: doing so could erase a nonce consumed by an earlier completed authorization and let the identical request replay for a second token. (2) A **pre-admission reentrant refusal** -- a nested `authorize`/`commit`/`submit_amendment` entered while another transaction is in flight -- is refused (`E-REENTRANT-CALL`) before it admits any request: it consumes **no** nonce, records a `DENY_UNKNOWN` that terminalizes **no** snapshot, and never mutates the outer invocation's state. The caller retries either abort as a fresh request. `FALSE` domination holds regardless of evaluation order: a determinate `FALSE` conjunct knowable without evidence yields `DENY_FALSE` even when the evidence bundle is malformed.

---

## 7. Assumptions and trust boundaries

### 7.1 Assumptions

Each assumption is labelled ASSUMED. Each can be refuted by a finite observation, listed in Section 28.

- **AX-CM (complete mediation).** Every consequential effect inside the declared boundary transits the decision point and the enforcement point. This is an assumption about system construction, not a theorem. It can be refuted by exhibiting one unmediated channel and can never be confirmed. Saltzer and Schroeder require that complete mediation "forces a system-wide view of access control, which in addition to normal operation includes initialization, recovery, shutdown, and maintenance" ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)), which binds the recovery path of Section 21 into the same obligation.
- **AX-ID (unforgeable request origin).** "It implies that a foolproof method of identifying the source of every request must be devised." ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)).
- **AX-EI (evidence independence).** For each covered event, at least one admissible witness record is generated in a control domain not transitively writable, truncatable, forkable, signable, reconfigurable, or rollback-able by the subject. This is AX-SH 5's Axiom 5. It is ASSUMED plus DETECTABLE via a declared `WithinAuth` assessment and a reviewed control graph. It is NOT derivable from a valid signature and MUST NOT be inferred from one.
- **AX-TIME (declared time or freshness authority).** A named freshness mechanism exists and is declared. RFC 9334 enumerates the three approaches, explicit timekeeping with synchronized clocks, implicit timekeeping using nonces, and implicit timekeeping using epoch identifiers, and states that "Provisioning of freshness has an impact on the number of needed round trips in a protocol; therefore, it must be made very early in the design" ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)). Where the mechanism is absent or ambiguous, `EvidenceCurrent` MUST evaluate UNKNOWN. A trustworthy clock may simply not exist: "a trustworthy clock might not be available in some use cases" ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)).
- **AX-TCB (decision point integrity).** The decision point is not compromised. Under A5 this fails and nothing in this document applies.
- **AX-CANON (canonicalization correctness).** The canonicalization implementation is correct. A canonicalization bug is a silent total failure with no defence in depth, and it SHOULD be the first target of any formal-methods obligation.

### 7.2 Trust boundaries

| ID | Boundary | Trusted for | Not trusted for |
|---|---|---|---|
| TB-1 | Subject | Nothing | Everything derived |
| TB-2 | Decision point | Recomputation of conjuncts, issuance of receipts | Observing unmediated channels |
| TB-3 | Enforcement point and adapter | Redemption, binding fidelity | Semantic correctness of the effect |
| TB-4 | Time or freshness authority | Freshness anchoring | Being unavailable without consequence |
| TB-5 | Witness | Emitting signed receipts about its own state | Honesty, correctness, non-collusion |
| TB-6 | Adjudication authority | Widening authority and lifting terminal states | Being right |
| TB-7 | Log and lineage store | Recording | Preventing equivocation absent a trusted primitive |

The control plane is itself a single point of failure. NIST notes that "An operational error could prevent an entire enterprise from functioning if the policy engine or policy administrator component becomes inaccessible from the network" and that "If an attacker disrupts or denies access to the PEP(s) or PE/PA (i.e., DoS attack or route hijack), it can adversely impact enterprise operations" ([NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)). BSSG accepts this cost explicitly rather than designing around it.

---

## 8. Formal model

### 8.1 Truth domain

Let the truth domain be `T = {TRUE, FALSE, UNKNOWN}`. Every predicate is total into `T`. Evaluator exceptions, absent attributes, unrecognized versions, unverifiable signatures, stale status, and scope ambiguity MUST return UNKNOWN and MUST NOT return TRUE.

### 8.2 The frozen kernel

```
Allow(r) <=> ContractMatch(r) AND EffectTypeValid(r) AND TargetAllowed(r)
             AND WitnessHealthy AND EvidenceCurrent
```

with the frozen side conditions that witness degradation MUST monotonically narrow authority and that UNKNOWN is never treated as satisfied.

**The equation is frozen.** This document does not add a sixth conjunct and MUST NOT be read as adding one. Commit-time revalidation, introduced in Section 15, is a protocol obligation that surrounds the kernel; it is recorded in the execution receipt's `revalidation` object, not in the `conjuncts` object, and any implementation that writes a sixth key into `conjuncts` is nonconformant.

### 8.3 Decision rule

`Allow(r)` is TRUE if and only if all five conjuncts are TRUE. Otherwise the external decision is DENY, refined into two reason classes:

- `DENY_FALSE` if at least one conjunct is FALSE;
- `DENY_UNKNOWN` if no conjunct is FALSE and at least one is UNKNOWN.

The refinement MUST be preserved in the record. Collapsing it destroys the distinction between an attack signal and an outage signal and destroys the UNKNOWN-domination statistic that any later empirical work would need.

### 8.4 Enforceability class

BSSG's enforced predicates MUST be safety properties. Schneider: "If the set of executions for a security policy ... is not a safety property, then an enforcement mechanism from EM does not exist" ([Schneider](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)); and the monitor "must prohibit" a prefix even where a later continuation would have been compliant ([Schneider](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)). One consequence is load bearing and uncomfortable: "Mechanisms that use more information than would be available only from observing the steps of a target's execution are, by definition, excluded from EM." ([Schneider](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)). BSSG resolves this explicitly: **independent evidence enters the kernel as an observable input event, namely a witness receipt delivered to the decision point, and never as an out-of-band oracle consulted outside the execution stream.** A deployment that consults an oracle outside the observed input stream leaves the EM class and MUST NOT claim the enforceability argument of this section.

### 8.5 Snapshot and linearization

All five conjuncts MUST be evaluated against a single immutable decision snapshot

```
S_d = (contract_digest, policy_digest, witness_epoch, evidence_epoch, authority_epoch, resolver_revision)
```

(`resolver_revision` is a **reserved** descriptor component in v0.1: it is fixed to a constant and is not yet an input to any gate transition. It is named here so the snapshot descriptor is forward-stable; a future revision that makes resolver identity load-bearing will populate it. Kimi-P15-06.)

and the authorization receipt MUST bind `S_d`. Immediately before the external commit point the enforcement point performs a conditional redemption against the current epochs. If any epoch changed, it consumes or voids the grant and returns a non-ALLOW terminal result. It MUST NOT refresh one predicate in isolation.

This is the minimum repair for time-of-check to time-of-use. It does not abolish the final race with an external system; it moves the linearization point to the closest controlled boundary and requires the residual ambiguity to be recorded rather than resolved by guessing.

---

## 9. Authority lattice

Model a capability as a tuple `(effect, target_scope, parameter_region, count, not_before, not_after)`. An authority `A` is a set of capabilities ordered by semantic inclusion: `A1 <= A2` if and only if every effect permitted by `A1` is permitted by `A2`. Independent restrictions combine by meet (intersection), never by union. An UNKNOWN authority input maps to the least authority compatible with the profile, which for consequential effects is the empty set.

Let witness health be `h`, ordered `FAILED = UNKNOWN < DEGRADED < HEALTHY`. The required safety property is antitonicity:

```
h' <= h   =>   Ceiling(h') <= Ceiling(h)
```

**Strictness.** A ceiling function that is identical at HEALTHY and DEGRADED satisfies antitonicity vacuously. This specification therefore additionally REQUIRES that, whenever health strictly decreases and the current ceiling is non-empty, the new ceiling be a proper subset of the previous ceiling. The reference gate enforces this and treats a violation as terminal (`E-NONSTRICT-NARROWING`).

**A preserved disagreement.** The GPT 5.6 Sol seat rejects universal strict narrowing, on the ground that authority may already be empty or the degraded witness may be irrelevant to the currently held capability, and proposes instead "global non-increase plus strict removal of every currently present capability whose assurance dependency failed". This draft adopts strictness conditioned on a non-empty prior ceiling, which covers the empty case but not the irrelevant-witness case. The residue is recorded as **OD-6** in `OPEN_DECISIONS.md` and is unresolved.

**Recovery is not the inverse transition.** A transition from DEGRADED or FAILED back to HEALTHY MUST NOT revive old grants. It MAY restore authority only through a new witness epoch, fresh evidence, and a new authorization decision, and, where the profile requires it, an independently adjudicated amendment. The nearest standards analogues for monotone state are the tlog witness rule that a witness "MUST check that the old size matches the size of the latest checkpoint it cosigned" and must respond 409 on mismatch ([C2SP tlog-witness](https://c2sp.org/tlog-witness)), and TUF's version monotonicity, where a new timestamp version that is not strictly greater means "discard the new timestamp metadata and abort the update cycle" ([TUF spec](https://theupdateframework.github.io/specification/latest/)). No fetched standard defines "monotonically narrowing authority" as a term of art, and this document does not claim standardization for it.

---

## 10. Architecture

### 10.1 Components

1. **Subject** (untrusted). Emits effect requests.
2. **Decision point** (PDP). Recomputes the five conjuncts from raw evidence. Emits a decision record and, on ALLOW, an authorization receipt carrying a one-time commit token.
3. **Enforcement point** (PEP) and **registered adapters**. Redeems the token under compare-and-swap, revalidates bindings and epochs, and performs the effect. Emits an execution receipt.
4. **Witness set**. Emits witness receipts carrying health, epoch, sequence, checkpoint state, an independence declaration, and a `WithinAuth` assessment.
5. **Freshness authority**. Supplies the declared time or epoch anchor.
6. **Record store and lineage service**. Append-only where the profile requires it; emits lineage records.
7. **Adjudication authority**. The only path that widens authority or lifts a terminal state.

NIST SP 800-207 supplies the role separation: the policy engine is "responsible for the ultimate decision to grant access", the policy administrator for "establishing and/or shutting down the communication path between a subject and a resource", the PEP for "enabling, monitoring, and eventually terminating connections", and "The PA communicates with the PEP when creating the communication path. This communication is done via the control plane." ([NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)). Whether BSSG co-locates PE and PA is an open decision (OD-7); RFC 9334 warns that co-located roles must be re-analyzed rather than assumed safe ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)).

### 10.2 Required flow

```
subject --(effect-request + raw evidence)--> decision point
decision point --(recompute 5 conjuncts)--> decision record
   DENY  -> terminal for this request identifier and this snapshot
   ALLOW -> authorization-receipt { bindings, authority snapshot, commit token }
subject/executor --(commit token + execution binding)--> enforcement point
enforcement point --(CAS redeem + epoch and binding revalidation)--> execution-receipt
                --(record)--> lineage-record ; on error -> correction-event
```

Decisions MUST be logged at the point of decision: "The policy engine makes and logs the decision (as approved, or denied), and the policy administrator executes the decision." ([NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)).

### 10.3 Caching

Cached ALLOW decisions are PROHIBITED. Only evidence MAY be cached, with an effect-type specific freshness window, and the full five-conjunct rule MUST be re-evaluated against current epochs. This follows the classical requirement that "proposals to gain performance by remembering the result of an authority check be examined skeptically. If a change in authority occurs, such remembered results must be systematically updated." ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)).

---

## 11. The kernel

### 11.1 Predicate obligations

**ContractMatch(r).** TRUE only if the request binds the exact active contract digest, the digest recomputes over canonical bytes of the contract body, the contract binds the same policy digest the request carries, the contract's subject matches the request's subject, the contract is neither revoked nor expired at the decision instant, and no unknown field changes semantics. An unknown contract or an unknown policy is UNKNOWN, not FALSE: the decision point cannot distinguish "no such contract" from "registry unreachable". A digest mismatch is FALSE.

**EffectTypeValid(r).** TRUE only if the effect type is a member of a closed, versioned effect registry carried in the contract; the registry entry names an adapter digest; and the request's adapter digest equals it. An absent registry is UNKNOWN; an unregistered effect is FALSE. Structural schema validity alone is insufficient: JSON Schema's default posture is permissive, since "Unknown keywords SHOULD be treated as annotations" and "An instance can only fail an assertion that is present in the schema" ([JSON Schema 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core.html)). Closure MUST be chosen explicitly by the profile.

**TargetAllowed(r).** TRUE only if the declared target canonicalizes, the subject's declared canonical form equals the recomputed canonical form, the target class is permitted, the canonical target lies within the contract's target scopes, and both the effect and the target lie within the current authority ceiling. An uncanonicalizable target (wildcards, traversal, percent-encoded separators, embedded credentials) is UNKNOWN. A canonical mismatch is FALSE. This implements "only connectivity begets connectivity, all access must derive from previous access" ([Miller](http://www.erights.org/talks/thesis/markm-thesis.pdf)) and NIST's rule that "authentication and authorization to one resource will not automatically grant access to a different resource" ([NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)). Wildcard ambiguity is a known exploit surface: "the attacker can leverage the ambiguity of the wildcard patterns to register an artifact that was meant to be deleted" ([in-toto, USENIX Security 2019](https://www.usenix.org/system/files/sec19-torres-arias.pdf)).

**WitnessHealthy.** A fitness predicate over the witness set required for the coverage class of this request at this epoch: verified signature, monotone epoch and sequence, unexpired health lease, a declared control domain distinct from the subject's, an explicit declaration that the subject cannot administer the witness, and a `WithinAuth` assessment of `outside_subject_authority`. It is NOT a process-wide Boolean and it is NOT a statement of witness honesty. Ambiguity in any of these is UNKNOWN. Health `FAILED` is FALSE; health `UNKNOWN` is UNKNOWN; health `DEGRADED` may still be TRUE for the narrowed ceiling, because degradation is expressed through the authority ceiling rather than by overloading this conjunct. Cosignature semantics MUST be reported honestly: a cosignature "assures clients that S has been seen, and not immediately found erroneous, by those W observers" ([CoSi, Syta et al.](https://arxiv.org/abs/1503.08768)).

**EvidenceCurrent.** TRUE only when a declared freshness authority exists and is signed, the anchor and the evaluation clock agree within the declared skew, the evidence epoch is not lower than the highest epoch seen, the request's own time fields parse strictly and are inside their window, the evidence age is inside the type-specific limit, and the nonce has not been seen. Absence or ambiguity of the freshness authority is UNKNOWN, never TRUE. RFC 9334 fixes the semantics: freshness "compares the estimated epoch against an 'expiry' threshold defined locally to that policy" ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)), and a residual race is unavoidable: "There is, however, always a race condition possible in that the state of the Attester and the appraisal policies might change immediately after the Evidence or Attestation Result was generated." ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)). Age alone is insufficient: revocation must be checked at decision time, since path validation requires that "At the current time, the certificate is not revoked" ([RFC 5280](https://www.rfc-editor.org/rfc/rfc5280.html)), and precomputed responses admit replay "in which an old (good) response is replayed prior to its expiration date but after the certificate has been revoked" ([RFC 6960](https://www.rfc-editor.org/rfc/rfc6960.html)).

### 11.2 Raw evidence discipline

The decision point MUST recompute every conjunct from raw evidence. It MUST NOT accept any caller-supplied derived fact. A record carrying a field named (case-insensitively) `allow`, `decision`, `authorized`, `contract_match`, `effect_type_valid`, `target_allowed`, `witness_healthy`, `evidence_current`, `within_auth`, `verified`, `signature_valid`, `conjuncts`, or `override` MUST be rejected structurally, before evaluation. This rule exists because the historically observed failure mode in this program's lineage is a test fixture or an interface that lets the caller supply the property under test.

---

## 12. Decision semantics

1. Structural admission. Field-set exactness, digest and nonce lexical form, strict RFC 3339 UTC timestamps, no extra fields, no missing fields, no derived fields. Failure is terminal for these bytes and yields `REJECTED_SCHEMA`.
2. Terminal-state check. If the session is terminal, DENY with the recorded terminal reason. No evaluation occurs.
3. Snapshot capture.
4. Conjunct recomputation, in the order ContractMatch, EffectTypeValid, WitnessHealthy, ceiling recomputation and narrowing check, TargetAllowed, EvidenceCurrent. The order is an implementation convenience and MUST NOT change the result; the ceiling must be recomputed before TargetAllowed because TargetAllowed is evaluated against the ceiling.
5. Kernel evaluation and classification into ALLOW, `DENY_FALSE`, or `DENY_UNKNOWN`.
6. The nonce is consumed for every well-formed, non-terminal submission (not only ALLOW), so a request denied on an early evidence path still burns its nonce. On ALLOW additionally: advance the highest-seen epochs, mint exactly one commit token, and emit an authorization receipt.
7. Record emission in all cases, including the per-conjunct truth values and reason codes. Verification output richer than a Boolean is the correct posture: "APIs exposing verification logic for Transparent Statements may provide more details than a single boolean result." ([SCITT architecture draft 13](https://www.ietf.org/archive/id/draft-ietf-scitt-architecture-13.html)).

DENY is terminal for the request identifier and snapshot. A subject that wishes to retry MUST issue a new, linked request with a fresh nonce. Silent re-evaluation of the same request identifier after evidence changes creates replay and audit ambiguity.

---

## 13. Atomic commit protocol

The commit protocol is the specification's principal addition to the frozen kernel, and it is a protocol obligation rather than a predicate.

**Obligation CP-1.** An authorization receipt MUST bind, at minimum: request digest, request identifier, subject, session, contract digest, policy digest, witness receipt digest, evidence epoch, witness epoch, authority epoch, authority snapshot, effect type, canonical target, parameters digest, adapter digest, nonce, issue time, and expiry.

**Obligation CP-2.** The commit token MUST be one-time and MUST be redeemed by an atomic compare-and-swap from `UNUSED` to `CONSUMED` in storage controlled by the enforcement point. A repeated redemption MUST be denied even where the signature and expiry remain valid. Nonces bind request to response precisely to prevent replay: "The nonce cryptographically binds a request and a response to prevent replay attacks." ([RFC 6960](https://www.rfc-editor.org/rfc/rfc6960.html)).

**Obligation CP-3.** At redemption the enforcement point MUST revalidate: token status and expiry, session non-terminality, authority epoch equality, evidence epoch equality, witness epoch equality where a fresh witness assertion is supplied, and exact equality of every bound execution field. Any mismatch voids the token. The token is not re-issued; a new decision is REQUIRED.

**Obligation CP-4.** Revalidation results MUST be recorded in the execution receipt's `revalidation` object and MUST NOT be recorded as a kernel conjunct.

**Obligation CP-5.** An unknown remote outcome MUST be recorded as `INDETERMINATE` and MUST NOT be retried blindly. At-most-once redemption plus target-specific idempotency is the claim; exactly-once for arbitrary external effects is not claimable.

**Obligation CP-6.** State update and record emission MUST be atomic and durable in the same sense the witness specification requires: "The witness MUST persist the new checkpoint before responding. Note that checking the old size against the latest checkpoint and persisting the new checkpoint must be performed atomically" ([C2SP tlog-witness](https://c2sp.org/tlog-witness)). The reference gate appends its decision record before minting a token; an implementation that mints first has a window in which an effect can be authorized without a durable record.

---

## 14. State machine

### 14.1 States

`RECEIVED`, `REJECTED_SCHEMA`, `EVALUATING`, `DENIED_FALSE`, `DENIED_UNKNOWN`, `AUTHORIZED_UNUSED`, `COMMITTING`, `COMMITTED_PENDING_OUTCOME`, `SUCCEEDED`, `FAILED_NO_EFFECT`, `INDETERMINATE`, `QUARANTINED`, `VOID`, `SESSION_TERMINAL`.

### 14.2 Permitted transitions

```
RECEIVED -> REJECTED_SCHEMA | EVALUATING
EVALUATING -> DENIED_FALSE | DENIED_UNKNOWN | AUTHORIZED_UNUSED | SESSION_TERMINAL
AUTHORIZED_UNUSED -> COMMITTING | VOID (epoch change, revocation, expiry)
COMMITTING -> COMMITTED_PENDING_OUTCOME | VOID
COMMITTED_PENDING_OUTCOME -> SUCCEEDED | FAILED_NO_EFFECT | INDETERMINATE | QUARANTINED
SESSION_TERMINAL -> EVALUATING   (only via an accepted independent amendment)
```

### 14.3 Forbidden transitions

`DENIED_*` to `AUTHORIZED_UNUSED` for the same request identifier and snapshot; `AUTHORIZED_UNUSED` to `COMMITTING` twice; `INDETERMINATE` to any automatic retry; `SESSION_TERMINAL` to any state except via amendment; any transition that increases the authority ceiling without an amendment.

### 14.4 Terminal failures

Terminal failures are closed and exhaustive at this version. Each halts the session until an independent amendment is accepted.

| Code | Condition |
|---|---|
| `E-AUTHORITY-WIDENING` | A recomputed ceiling is not a subset of the prior ceiling |
| `E-NONSTRICT-NARROWING` | Health strictly decreased, the prior ceiling was non-empty, and the new ceiling is not a proper subset |
| `E-SESSION-TERMINAL` | Any request or commit in a session already terminal |
| `E-KERNEL-INVARIANT` | An ALLOW was computed with a non-TRUE conjunct (an implementation defect, and a falsifier of the kernel). **Never emitted by a correct gate** -- it is a falsifier reserved for conformance harnesses; its absence in `state.records` is the intended behavior. (Kimi-P15-08) |
| `E-CALLER-SUPPLIED-DERIVED-FIELD` | A caller supplied a derived authorization fact (per-request REJECTED_SCHEMA / snapshot-terminal; not a session-terminal failure) |
| `E-EQUIVOCATION-DETECTED` | Two accepted witness receipts covering overlapping sequence ranges are mutually inconsistent. **Not emitted in v0.1**: cross-receipt equivocation detection is declared out of model (A-tier assumption), and the code is reserved for a future evidence-correlation revision. (Kimi-P15-08) |

---

## 15. Cryptographic binding, freshness, replay, and rollback

### 15.1 Canonicalization and binding

All digests are computed over `BSSG-CANON-1`: sorted object keys, no insignificant whitespace, UTF-8, no floating point, integers restricted to the I-JSON safe range. This is a canonicalization strategy of the kind RFC 8785 describes, where "The output from JCS is a 'hashable' representation of JSON data that can be used by cryptographic methods" ([RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html)); it is not an RFC 8785 implementation and MUST NOT be described as one. RFC 8785 is itself informational: "This document is not an Internet Standards Track specification; it is published for informational purposes." ([RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html)).

There is a genuine architectural fork here. COSE avoids canonicalization by wrapping protected headers in a byte string, which "avoids the problem of all parties needing to be able to do a common canonical encoding of the map for input to cryptographic operations" ([RFC 9052](https://www.rfc-editor.org/rfc/rfc9052.html)). Both cannot be the normative binding method. The choice is recorded as **OD-1** and is UNRESOLVED in v0.1.

Subjects are bound by digest: "Each element MUST have `digest` set. Subjects are assumed to be immutable" ([in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md)). The same source warns that digest matching disregards content type: "Subject artifacts are matched purely by digest, regardless of content type." ([in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md)).

### 15.2 Signature envelopes

Receipts SHOULD be carried in COSE_Sign1 or COSE_Sign envelopes. The two are not interchangeable: "The structures cannot be converted between each other; as the signature computation includes a parameter identifying which structure is being used, the converted structure will fail signature validation." ([RFC 9052](https://www.rfc-editor.org/rfc/rfc9052.html)). Anything not intended to be integrity protected MUST be in the unprotected bucket, and "This bucket MUST be empty if it is not going to be included in a cryptographic computation." ([RFC 9052](https://www.rfc-editor.org/rfc/rfc9052.html)). Validity-window and anti-replay claims SHOULD follow CWT: `iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `cti`, where "The 'jti' claim is used to prevent the JWT from being replayed." ([RFC 8392](https://www.rfc-editor.org/rfc/rfc8392.html)).

**Honesty constraint on the reference implementation.** The shipped gate models signature verification through an injected verifier that returns TRUE, FALSE, or None (UNKNOWN). It performs no cryptography, establishes no key custody, and its receipts carry `verification_status: not_performed_by_reference_gate`. The schemas therefore MUST NOT be read as asserting that any signature was verified.

### 15.3 Freshness

Every object used to establish freshness MUST carry the applicable subset of observed time, issue time, not-before, expiry, maximum age, nonce or epoch identifier, issuer key epoch, and revocation epoch. The verifier MUST declare which clock it trusts, the maximum skew, and its behaviour on backward jumps. Where the declaration is absent or two sources disagree beyond the declared skew, `EvidenceCurrent` MUST be UNKNOWN. Claim generation and claim signing are distinct events and both MUST be governed: "It is important to note that the actual values in Claims might have been generated long before the Claims are signed." ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)). No numeric freshness bound is fixed by this version; RFC 9162 "deliberately does not specify any limits on the value to allow for experimentation" ([RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html)) and RFC 9334 leaves the threshold local to policy ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)). This is **OD-3**.

### 15.4 Replay and rollback

Anti-replay uses a nonce consumed on every well-formed non-terminal submission (an early denial still burns it) plus a one-time commit token. Rollback resistance requires monotone state external to any component that can be restored: a highest-seen epoch, an append sequence, an external checkpoint, or a hardware monotonic counter. A valid old signature is not current. On restore, any policy, contract, witness, evidence, ledger, or revocation epoch lower than the highest externally committed value MUST be rejected as rollback. TUF's version rules are the model: a new version that is not strictly greater means "discard the new timestamp metadata and abort the update cycle", and expiry checked against a fixed update start time defends against freeze ([TUF spec](https://theupdateframework.github.io/specification/latest/)).

**Scope limit stated in the same sentence as the claim.** Rollback resistance in the reference gate holds only during the lifetime of one non-rolled-back gate instance and only while process memory is intact, because the gate's highest-seen epochs live in process memory -- a process restart inside the same logical session erases that state -- and cross-session and cross-restore rollback resistance requires a named external monotonicity root, which this version does not fix (**OD-2**).

---

## 16. Witness model

A witness receipt carries: witness identifier, covered subject and its control domain, an independence declaration, a `WithinAuth` assessment, an epoch, a sequence, checkpoint state, a health value, an observation time, a lease expiry, and a signature.

**W-1.** A witness MUST hold per-log state and MUST refuse to cosign anything inconsistent with it ([C2SP tlog-witness](https://c2sp.org/tlog-witness)).
**W-2.** Non-monotone transitions MUST be rejected with a distinct error rather than silently ([C2SP tlog-witness](https://c2sp.org/tlog-witness)).
**W-3.** Signatures from unknown keys MUST be ignored rather than treated as degraded-but-present witnesses ([C2SP tlog-witness](https://c2sp.org/tlog-witness)).
**W-4.** Threshold counting MUST be by unique key identity: "each SIGNATURE which is counted towards the THRESHOLD MUST have a unique KEYID" ([TUF spec](https://theupdateframework.github.io/specification/latest/)).
**W-5.** A witness receipt attests observation and self-consistency. It MUST NOT be read as attesting the correctness of the subject's behaviour, the honesty of the witness, or the independence of the evidence.
**W-6.** Witness diversity is the design goal, not an achieved property, and a deployment MUST declare its witness count, its threshold, and the administrative domains involved.

**The honest-quorum limit.** A witness that is alive, responsive, protocol-conformant, and wrong satisfies `WitnessHealthy`. The kernel cannot distinguish healthy-and-correct from healthy-and-corrupted. This is not an implementation gap; it is a boundary of the architecture and it is listed as OUT OF MODEL in Section 31, with a passing test in `test_bssg_gate.py` that asserts the gate ALLOWS in exactly this case so that any future claim of detection requires visibly rewriting that test.

---

## 17. Provenance and correction lineage

Corrections are new entities, never edits. PROV-DM supplies the vocabulary: "A revision is a derivation for which the resulting entity is a revised version of some original", "Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity", and "A bundle is a named set of provenance descriptions, and is itself an entity, so allowing provenance of provenance to be expressed." ([W3C PROV-DM](https://www.w3.org/TR/prov-dm/)). The transparency-compatible primitive is supersede-by-reissue: "A registered Statement may be superseded by a subsequently submitted Signed Statement from the same Issuer, with the same subject" ([SCITT draft 13](https://www.ietf.org/archive/id/draft-ietf-scitt-architecture-13.html)).

**P-1.** A correction MUST NOT destroy the evidence that justified the original decision.
**P-2.** A correction MUST declare its descendant closure as `COMPLETE`, `PARTIAL`, or `UNKNOWN`, and MUST NOT declare `COMPLETE` while listing unreachable descendants. UNKNOWN is a first-class value here as everywhere.
**P-3.** A lineage record MUST declare its mediation boundary reference, and MUST NOT declare `COMPLETE` completeness while declaring gaps. Completeness means only that every mediated transformation inside the declared boundary has a recorded node. It never means that all causation has been reconstructed.
**P-4.** Reconciling an append-only log with an authoritative current-corrected-value view is unsolved in the fetched literature (**OD-5**); no fetched source reconciles them.

---

## 18. Recovery

**R-1.** Terminal states are exited only by an accepted correction event of class `LIFT_TERMINAL_STATE` (in v0.1; `AMEND_AUTHORITY` is a RESERVED class, admitted by the schema but NOT implemented by the v0.1 reference gate, which refuses it with `E-AMENDMENT-CLASS-UNIMPLEMENTED`), carrying at least two adjudicators in control domains distinct from each other and from the subject's domain, each with a signature the deployment's verifier accepts. Two-key gating is the classical precedent: "a protection mechanism that requires two keys to unlock it is more robust and flexible than one that allows access to the presenter of only a single key" ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)).
**R-2.** Recovery MUST NOT revive old grants, old epochs, or old ceilings. The ceiling is recomputed from the next observed health.
**R-3.** The recovery path is inside the mediation obligation, since complete mediation "includes initialization, recovery, shutdown, and maintenance" ([Saltzer and Schroeder](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)).
**R-4.** Structural independence of adjudicator domains is checked; actual independence is ASSUMED. The reference gate compares declared strings and nothing more.
**R-5.** Recovery from compromise of the root authority is not claimed. TUF states the analogous case plainly: "safely recovering from it is nearly impossible." ([TUF spec](https://theupdateframework.github.io/specification/latest/)).

**A ratchet warning.** Because only adjudication widens authority, every transient degradation permanently narrows a long session until a human intervenes. Over a long session, authority tends to the empty set. This is authority-reducing and operationally expensive; no safety outcome is claimed, and the expense is the thing that will be worked around in practice. The architectural answer preferred here is short sessions with fresh contracts, making re-arming a contract issuance event rather than a recovery event. No maximum session duration is fixed in v0.1 (**OD-8**).

---

## 19. Conformance profiles

Profiles are cumulative. A deployment MUST NOT claim a higher profile by declaring a lower-profile test out of scope. The mediation boundary MAY be narrow but MUST be explicit.

### 19.1 BSSG-M (Minimal). Defends A1. Concedes A2 and above.

REQUIRED: all six schemas with closed field sets; three-valued kernel with the exact ALLOW rule; distinct `DENY_FALSE` and `DENY_UNKNOWN`; canonical request digest binding; one-time commit tokens with compare-and-swap redemption and commit-time revalidation; nonce and epoch anti-replay; strict timestamp parsing; a closed terminal-failure taxonomy; an offline-checkable decision record.
NOT REQUIRED: multiple witnesses; transparency log inclusion; hardware roots.
MANDATORY DISCLOSURE: a BSSG-M deployment MUST state, in these words, that evidence independence at this profile rests on a declaration it cannot verify, and MUST NOT claim non-equivocation beyond detection at the single-observer level.

**A preserved disagreement.** The GPT 5.6 Sol seat holds that evidence independence and non-bypassability cannot be optional even at Minimal, "otherwise the profile conforms to a logger, not a safety gate". The Gemini 3.1 Pro seat holds the opposite tension, that minimal deployability cannot cryptographically establish witness fitness to a stateless decision point without out-of-band state syncing, so a strict kernel will frequently halt minimal deployments. Both positions are recorded; neither is resolved in v0.1 (**OD-9**).

### 19.2 BSSG-S (Standard). Defends A2, detects A3, concedes A4 and above.

Adds: at least one witness under distinct administrative control with a reviewed control graph; an external signed freshness anchor; frozen trust roots with no runtime key parameter anywhere in the interface; a frozen, strictly decreasing ceiling function per health level; checkpoint comparison giving equivocation detection; content-addressed quarantine for artifacts; correction events with at least two non-producer-lineage adjudicators carrying reproduction digests; and the ability to check an entire decision log offline against the cross-record invariants of Section 20.4.

### 19.3 BSSG-H (High assurance). Defends A3, detects A4, concedes A5.

Adds: at least three witnesses under distinct administrative control with threshold agreement on health, counted by unique key identity ([TUF spec](https://theupdateframework.github.io/specification/latest/)); a trusted monotonic or append-only primitive, or a public transparency-log inclusion proof, which is the only condition under which non-equivocation may be described as prevented rather than detected; a cross-session monotonicity root; a formal transition-system model with model-checked invariants; an independent implementation of the kernel by a non-producer lineage, with both implementations required to agree on the full adversarial corpus; and a published coverage declaration listing every known unmediated channel, which is the only honest way to expose AX-CM to review.

---

## 20. Schemas

### 20.1 The six schemas

Exactly six JSON Schema 2020-12 documents are normative at v0.1:

| File | Purpose |
|---|---|
| `schemas/effect-request.schema.json` | Subject request. Raw declarations only |
| `schemas/authorization-receipt.schema.json` | ALLOW receipt with bindings, authority snapshot, and one-time commit token |
| `schemas/witness-receipt.schema.json` | Witness state, independence declaration, `WithinAuth` assessment |
| `schemas/execution-receipt.schema.json` | Commit attempt, revalidation result, outcome including `INDETERMINATE` |
| `schemas/correction-event.schema.json` | Supersession, invalidation, authority amendment, terminal-state lift |
| `schemas/lineage-record.schema.json` | Hash-linked view with declared gaps and completeness |

The six-schema set is fixed by the specification's charter and overrides the alternate schema decompositions proposed by individual council seats (Claude Opus 5 proposed contract, request, attestation, decision, capability, amendment; GLM 5.2 proposed admission request, contract, witness health, evidence package, decision record, terminal failure report). Those alternates are recorded in the decision register; the contract and policy documents are represented here as digests bound by the request rather than as separate normative schemas, which is a real loss of expressiveness and is recorded as **OD-10**.

### 20.2 Closure

All six use `additionalProperties: false` at every object level where the field set is intended to be closed. This is a deliberate profile choice, not an inherited default, because "A JSON Schema MAY contain properties which are not schema keywords. Unknown keywords SHOULD be treated as annotations" ([JSON Schema 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core.html)). The 2020-12 dialect is pinned by normalized URI in every file, as REQUIRED: "The value of this keyword MUST be a URI (containing a scheme) and this URI MUST be normalized." ([JSON Schema 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core.html)). Schema identifiers use the `urn:bssg:schema:0.1:*` form because no BSSG namespace has been published and inventing a resolvable URL would be a fabrication.

Structural validation is necessary and insufficient. `format` keywords are annotations by default in 2020-12, so BSSG timestamps are constrained by explicit `pattern` rather than by `format: date-time`, and the reference gate parses them with a strict parser rather than relying on schema validation at all.

### 20.3 What the schemas do not assert

No schema asserts that a signature was verified, that a key is legitimate, that a declared control domain is genuinely independent, or that a declared `WithinAuth` value is true. Each such field is a declaration whose verification status is carried explicitly and whose default in the reference implementation is `not_performed_by_reference_gate`.

### 20.4 Cross-schema invariants

These are normative and are checked in `bssg_gate.check_cross_record_invariants` (X1-X4 token-id equality), `check_correction_closure` (X5), `check_lineage_completeness` (X6), `check_authority_history` (X7), `check_allow_receipt` (X8), and `check_single_redemption` (X4 redeemed-at-most-once). Each checker is exercised with positive and negative vectors by the test suite and re-exercised by verifier gate G11.

| ID | Invariant |
|---|---|
| X1 | `authorization.request_digest` equals the digest over the canonical bytes of the effect request |
| X2 | `authorization.witness_receipt_digest` equals the digest of the witness receipt used, and that receipt's `covered_subject` equals the request's `subject_id` |
| X3 | `execution.authorization_receipt_digest` equals the digest of the authorization receipt, and the executed request digest, canonical target, and parameters digest equal the authorized ones |
| X4 | `execution.commit_token_id` equals `authorization.commit_token.token_id`, and that token was redeemed at most once |
| X5 | A correction event MUST NOT declare `COMPLETE` descendant closure while listing unreachable descendants, and its closure status MUST be one of the three permitted values |
| X6 | A lineage record MUST NOT declare `COMPLETE` completeness while declaring gaps, and MUST NOT reference a parent node absent from the record while claiming completeness |
| X7 | `authority_epoch` is monotone non-decreasing across records, and a ceiling recorded after a health decrease is a subset, proper where the prior ceiling was non-empty. Three-valued: a grant-independently provable divergence (epoch regression, constant-epoch ceiling change, unlicensed widening with no marker, forged/unbound/unarmed marker, type-tamper, beyond-ceiling seed target-widening) is **X7** (VIOLATION); an armed forward re-widen whose legitimacy cannot be witnessed offline (the runtime grant is caller-supplied -- WithinAuth of its supplier -- and discharges nothing under evidence-independence) is **X7U** (UNCERTIFIABLE-offline); a stream with no re-widen is **clean**. Re-widen legitimacy is established only at runtime, proven over bounded schedules (BOUNDED-AUTH-INTRO) |
| X8 | Every ALLOW receipt carries exactly the five conjunct keys, each valued TRUE, and an empty reason-code list |

---

## 21. Reference implementation

`bssg_gate.py` is a Python 3 module, standard library only, with optional `jsonschema` used by the test suite. It implements canonicalization, the strict timestamp parser, the three-valued kernel, the authority lattice, target canonicalization, the five conjunct evaluators, the authorization path, the atomic commit protocol, terminal states, the amendment path, and the cross-record invariant checkers.

What it enforces is listed in its module docstring and in Section 22 at claim level ENFORCED. What it explicitly does not do:

- it performs no cryptography and models signature verification through an injected verifier, so a `TRUE` verification result is a statement about a callable and not about a key;
- it establishes no key custody, key distribution, or trust-root provenance;
- it cannot establish complete mediation, since it observes only what is handed to it;
- it keeps monotonicity state in process memory, so its rollback resistance does not survive a restart;
- it does not implement RFC 8785 and does not claim interoperability with it;
- token redemption is concurrency-safe: the `UNUSED` -> `CONSUMED` transition is an atomic compare-and-swap under a process-local lock, so a double-spend is refused even under concurrent redemption -- but this holds only within one process, and durable, cross-process single-use redemption requires a transactional store (a BSSG-H obligation);
- it is not otherwise hardened and is not intended for production deployment.

`test_bssg_gate.py` contains the exhaustive 3^5 = 243 kernel truth states plus adversarial and protocol tests. The suite is deterministic: injected clock, injected token factory, injected verifier, no randomness, no network. Exact counts and results are recorded in `README.md`.

---

## 22. Security properties, claim levels, and counterexamples

### 22.1 Non-bypassability

**Bounded claim.** Every declared consequential effect initiated by a covered subject inside the declared mediation boundary is preceded by an ALLOW decision and by the single redemption of a commit token bound to that decision.
**Claim level.** ENFORCED for records the gate processes; ASSUMED at the deployment level, conditional on AX-CM and on the declared effect-path inventory.
**Why conditional.** The classical requirement is that the reference validation mechanism be "always invoked" ([NIST CSRC glossary](https://csrc.nist.gov/glossary/term/reference_monitor)), which is a statement about system construction. The condition MUST appear in the same sentence as the claim in every document that makes it.
**Counterexample.** The subject retains a raw socket, an inherited file descriptor, or an emergency path. Every BSSG record is perfect and the effect happens anyway.
**Falsifier.** One observed covered effect with no matching grant and redemption chain.

### 22.2 Bounded authority

**Bounded claim.** No effect is authorized outside the intersection of the contract, the policy, the adapter registration, and the current authority ceiling; and witness degradation never enlarges that ceiling.
**Claim level.** ENFORCED (widening and non-strict narrowing are terminal in the reference gate). Grant-independent divergences (epoch regression, constant-epoch ceiling change, unlicensed widening, type-tamper) are DETECTABLE offline from the decision log (X7). An armed forward re-widen licensed by an accepted amendment is UNCERTIFIABLE offline (X7U) -- the runtime grant is caller-supplied (WithinAuth of its supplier) and cannot discharge the license under evidence-independence (SHV Axiom 5); its legitimacy is established only at runtime, proven over bounded schedules. A stream with no re-widen is clean.
**Counterexample.** A contract whose ceiling function is written so that the DEGRADED ceiling equals the HEALTHY ceiling satisfies antitonicity vacuously. This specification forbids it (Section 9) and the gate treats it as terminal, but the defence lives in the contract, so a deployment with a badly written contract retains a vacuous ceiling at every level below the profile check.
**Falsifier.** A decision log in which a later ceiling is not a subset of an earlier one with no interleaved amendment.

### 22.3 Non-equivocation

**Bounded claim.** Conflicting signed histories are DETECTABLE by comparison of checkpoints across observers within a declared checkpoint and gossip model. Below BSSG-H, BSSG does NOT prevent equivocation.
**Claim level.** DETECTABLE at BSSG-S; potentially prevented at BSSG-H only where a trusted monotonic or append-only primitive, or a quorum assumption, is present and named.
**Why.** Preventing a Byzantine participant from telling different stories to different parties requires a trusted component. The transparency-log route takes detection instead, and its own specification says so: "The logs do not themselves prevent misissuance, but they ensure that interested parties ... can detect such misissuance" ([RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html)). Worse, the detection mechanism itself can be defeated: "The log auditing mechanisms described in this document can be circumvented by a misbehaving log that shows different, inconsistent views of itself to different clients. Therefore, it is necessary to treat each log as a trusted third party." ([RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html)), and the mitigation, gossip, is "an active area of research and not defined here" ([RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html)). Cosigning is explicitly detection forcing rather than preventive ([CoSi](https://arxiv.org/abs/1503.08768)).
**Counterexample.** A compromised witness signs two receipts at the same sequence with the same predecessor for two different relying parties. Every signature verifies. Only cross-observer comparison finds it, and only if someone compares.
**Falsifier.** Two accepted inconsistent receipts for the same sequence and epoch with no protocol-detectable conflict.

### 22.4 Provenance continuity

**Bounded claim.** Every effect and artifact produced through a covered adapter has a hash-linked path to its request, authorization, execution, witness receipts, and corrections.
**Claim level.** ENFORCED for records produced by the gate; DETECTABLE for gaps; OUT OF MODEL for artifacts that never entered the boundary.
**Counterexample.** An artifact created outside the boundary and later referenced by digest inside it has a lineage node and no lineage.
**Falsifier.** A released covered object lacking a mandatory edge, or two objects sharing an identifier with different digests.

### 22.5 Evidence independence

**Bounded claim.** For each covered event, at least one admissible witness record is generated in a control domain not transitively controllable by the subject.
**Claim level.** ASSUMED, with a DETECTABLE proxy: the presence of a `WithinAuth` assessment of `outside_subject_authority` and an explicit declaration that the subject cannot administer the witness. It is NOT derivable from a signature and the gate does not derive it.
**Why.** AX-SH 5 states that acting-system-independent evidence generation "is not derivable and is stated as Axiom 5 (Evidence independence) over a control predicate (WithinAuth)" ([AX-SH 5](https://doi.org/10.5281/zenodo.21539074)). Independence of failures is likewise an assumption in the Byzantine literature ([Castro and Liskov](http://pmg.csail.mit.edu/papers/osdi99.pdf)), and remote attestation makes the isolation assumption explicit: "It is assumed that an Attesting Environment is sufficiently isolated from the Target Environment it collects Claims about" ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html)).
**Counterexample (independent key, common administrator).** The witness has a distinct key, host, and vendor, and one operator can reconfigure its collector, delete its storage, and restore a snapshot. Cryptographic separation exists; evidence independence does not. The gate ALLOWS.
**Counterexample (colluding but apparently healthy witness).** A subject-controlled witness emits a structurally perfect HEALTHY receipt declaring `subject_can_administer: false`. The gate ALLOWS and cannot do otherwise. This case is encoded as a passing test whose assertion is the limitation.
**Falsifier.** The subject or its transitive administrators can alter all admissible records for a covered event.

### 22.6 Non-advantage of concealment

Stated in its architectural form in Section 23. Claim level: ENFORCED for the decision-monotonicity half; ENFORCED for the response-CONTENT half of the no-regime-signal clause (the reference gate's `subject_facing()` projection collapses every denial to a constant response, closing the distinct-error-code channel); ASSUMED and a declared deployment obligation for the residual side channels (latency, capability lifetime, log-flush timing, response size); OUT OF MODEL for anything about the subject's behaviour.

---

## 23. Non-advantage of concealment, architectural formulation

Read as a behavioural property ("an agent that believes it is unobserved obtains no more unauthorized effect"), non-advantage of concealment is a hyperproperty over pairs of runs differing in an induced belief, it is not enforceable by any monitor, and it is an effectiveness claim, which this document is forbidden to make. Read naively as an architectural property ("the subject's belief is not an input to the decision function"), it is nearly vacuous, because no belief state appears anywhere in the kernel.

This specification therefore adopts a two-clause formulation, of which only the second clause has teeth:

> **PR-6 (non-advantage of concealment, architectural form).**
> **(a) Decision monotonicity under information loss.** Replacing any predicate input or supporting fact with UNKNOWN or FALSE, all else equal, MUST NOT change DENY to ALLOW, MUST NOT revive a grant, MUST NOT suppress a revocation, and MUST NOT widen authority. This is mechanically testable over the finite truth table and is ENFORCED by the reference gate: the exhaustive 243-state suite establishes that exactly one assignment allows, and every degradation of an input toward UNKNOWN or FALSE moves the decision away from ALLOW.
> **(b) No subject-visible regime signal.** No BSSG-mediated channel SHALL expose to the subject a signal that distinguishes observed from unobserved operation. Differential latency between DENY classes, differing error codes, capability lifetime variation, and log-flush timing are all channels through which a subject could infer its observation regime, and a conformant deployment MUST enumerate and address them.

Clause (b)'s response-content projection is PROVIDED by the reference gate but its use is a DEPLOYMENT OBLIGATION (the reference gate does not enforce which plane a deployment returns), and it remains a declared deployment obligation for the residual timing and size channels. The reference gate splits the planes: the rich decision record -- the `DENY_FALSE`/`DENY_UNKNOWN` refinement, the per-conjunct values, and the specific reason codes -- is written only to the AUDIT PLANE (the decision-record store), while `BSSGGate.subject_facing()` projects every denial to a single constant `DENIED`/`E-DENIED` and is the response a subject SHOULD receive. The distinct-error-code channel this clause originally flagged is closed ONLY WHEN a deployment routes `subject_facing()` to the subject; the reference gate PROVIDES this projection but does not enforce that a deployment uses it. This is a DEPLOYMENT OBLIGATION, not an enforced gate property. The residual channels it enumerates -- differential latency between DENY classes, capability-lifetime variation, log-flush and transport-close timing, and response size -- are NOT closed by the reference gate and MUST be enumerated and normalized by a conformant deployment (the covert-channel inventory); they are declared, not enforced. This is **OD-11**, now scoped to those residual side channels, with falsifier AF-9.

Neither clause claims anything about how a subject behaves. Behavioural invariance under concealment is SHVVP Phase C's estimand and is OUT OF MODEL here.

---

## 24. Attack analysis

| # | Attack | Class | Architectural response | Claim level |
|---|---|---|---|---|
| AT-1 | Forged effect request fields | A1 | Closed field sets, digest recomputation, canonical binding | ENFORCED |
| AT-2 | Caller supplies a derived authorization fact | A1 | Structural rejection before evaluation | ENFORCED |
| AT-3 | Nonce replay | A1, A2 | Nonce consumed on every well-formed non-terminal submission; reuse is DENY_FALSE | ENFORCED (in-process) |
| AT-4 | Double-spend of an authorization | A1, A2 | One-time token, compare-and-swap redemption | ENFORCED |
| AT-5 | TOCTOU between decision and effect | A2 | Epoch binding plus commit-time revalidation | ENFORCED for epochs the gate observes |
| AT-6 | Target aliasing, traversal, percent-encoding, wildcards | A1 | Canonicalization refusal mapped to UNKNOWN | ENFORCED |
| AT-7 | Confused deputy across contracts or subjects | A1 | Subject-contract binding, witness subject match | ENFORCED |
| AT-8 | Witness silencing or degradation | A2 | Ceiling narrowing to empty; UNKNOWN never satisfied | ENFORCED, cost is availability |
| AT-9 | Forged witness receipt | A2 | Injected verifier returns FALSE; DENY_FALSE | ENFORCED given a real verifier |
| AT-10 | Colluding but apparently healthy witness | A3 | None. Indistinguishable at the kernel | OUT OF MODEL |
| AT-11 | Witness equivocation | A3 | Checkpoint comparison across observers | DETECTABLE only |
| AT-12 | Evidence or witness epoch rollback | A4 | Highest-seen epoch rejection | ENFORCED in-process; cross-restart is OD-2 |
| AT-13 | Clock rewind or skew manipulation | A4 | Declared freshness authority, skew bound, UNKNOWN on ambiguity | ENFORCED given a declared authority |
| AT-14 | Stale but unexpired evidence | A2 | Age limit plus epoch binding; revocation epoch REQUIRED at BSSG-S | Partially ENFORCED |
| AT-15 | Lost response and blind retry | A2 | INDETERMINATE terminal outcome, no automatic retry | ENFORCED |
| AT-16 | Authority widening through a degraded path | A2 | Terminal `E-AUTHORITY-WIDENING` | ENFORCED |
| AT-17 | Recovery abuse (self-amendment) | A3 | Two adjudicators in distinct declared domains | ENFORCED structurally, ASSUMED semantically |
| AT-18 | Correction that hides its own gaps | A1 | Closure status invariant X5 | ENFORCED |
| AT-19 | Bypass through an unmediated channel | A1 | None | ASSUMED away by AX-CM; falsifier AF-2 |
| AT-20 | Adversarial payload inside a permitted effect | A1 | None. BSSG mediates authority, not meaning | OUT OF MODEL |
| AT-21 | Composition of individually authorized effects | A1 | None. No composition analysis exists in the kernel | OUT OF MODEL |
| AT-22 | Denial of service against the control plane | A2 | None. Converted into denial | ACCEPTED COST |
| AT-23 | Compromise of the decision point | A5 | None | OUT OF MODEL |

---

## 25. Architectural falsifiers

Each is a finite observation that refutes a specific claim. A failed falsifier makes the affected profile and boundary NONCONFORMANT and is not averaged away by a pass rate.

| ID | Falsifier | Refutes |
|---|---|---|
| AF-1 | A covered effect occurs with no preceding ALLOW and redemption | Non-bypassability |
| AF-2 | One unmediated channel capable of a consequential effect is exhibited | AX-CM, and with it the scope of every other property |
| AF-3 | A decision record shows ALLOW with any conjunct not TRUE | The kernel itself |
| AF-4 | A later ceiling is not a subset of an earlier one with no interleaved amendment | Bounded authority |
| AF-5 | Two accepted inconsistent receipts for the same sequence with no detected conflict | Non-equivocation as detection |
| AF-6 | An ALLOW exists whose witness receipt is signed by a key the subject can produce | Evidence independence |
| AF-7 | An UNKNOWN conjunct is resolved to TRUE by a default, retry, cache, or override | UNKNOWN discipline |
| AF-8 | A lineage record claims COMPLETE while a mediated transformation is unrecorded | Provenance continuity |
| AF-9 | A subject-visible signal distinguishes observed from unobserved operation | PR-6 clause (b) |
| AF-10 | Authority widens by any path other than an accepted independent amendment | Recovery discipline |
| AF-11 | A non-conformant architecture passes the conformance suite | The suite's own adequacy |
| AF-12 | Two independent implementations disagree on a frozen test vector | Conformance determinacy |
| AF-13 | A commit token is redeemed more than once | The commit protocol |
| AF-14 | An epoch lower than the highest committed value is accepted | Rollback resistance |
| AF-15 | An unknown remote outcome is reported as proved failure or retried automatically | Ambiguity discipline |

AF-11 is the meta-falsifier and SHOULD be listed first in any published summary. A conformance suite that a cheating implementation can pass is worse than no suite, because it launders nonconformance. The specific failure to guard against is a test fixture that assumes the property under test.

---

## 26. Verification strategy

1. **Structural.** All six schemas validate against the 2020-12 meta-schema; all example records validate; negative vectors fail for the intended reason.
2. **Kernel exhaustiveness.** All 3^5 = 243 truth states enumerated, with exactly one allowing state.
3. **Adversarial corpus.** The attack table of Section 24 mapped one-to-one onto tests, including the limitation tests that assert what the gate cannot do.
4. **Cross-record invariants.** X1 through X8 checked mechanically.
5. **Package verification.** `verify_bssg_v0_1.py` runs schema validation, the test suite, citation URL extraction sanity, a prohibited-effectiveness-language scan, a normative-term scan, file parity and version checks, and a SHA-256 manifest check.
6. **Partially done in v0.1; REQUIRED in full before any freeze.** The reference gate ships a bounded executable model check (`bssg_model_check.py`) that exhaustively verifies: the kernel truth table over all 243 states (3 to the 5), degradation antitonicity over 729 contract pairs, bounded authority-introduction over all schedules of length at most 4 from a 10-operation alphabet (11110 schedules, PASS), and operational refinement against the executable transition system. This is bounded real-gate checking, not a transition-system proof. A full TLA+ or equivalent model with model-checked invariants for type correctness, terminal closure, no-ALLOW-with-non-TRUE-conjunct, at-most-one redemption, no-execution-before-redemption, authority antitonicity, and no-stale-epoch-commit remains REQUIRED before freeze; bounded counterexample search over the lineage and control graphs; a second independent implementation agreeing on every frozen vector; and a release manifest binding every normative file, schema, test, dependency lock, and runtime version. Liveness MUST be stated only under explicit fairness assumptions, since a partitioned or malicious target invalidates unconditional liveness.

No unbounded transition-system proof or formal verification is claimed for anything in v0.1. The shipped model check is a bounded exhaustive enumeration over the reference gate's executable, not a formal proof. This matches the honesty standard AX-SH 5 sets for itself ([AX-SH 5](https://doi.org/10.5281/zenodo.21539074)).

---

## 27. Privacy and availability tradeoffs

**Availability.** Fail-closed under an asynchronous network converts denial of service into authority reduction. This is a priced choice, not a free property. NIST states the cost directly: "Incomplete knowledge will most often lead to a business process failure where the PE denies requests due to insufficient information." ([NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)). TUF states that the adversary always retains the option: "Fundamentally, an attacker positioned to intercept and modify a client's communication can always perform a denial of service." ([TUF spec](https://theupdateframework.github.io/specification/latest/)). BSSG chooses safety over liveness in the sense the Byzantine literature makes precise, where safety does not require synchrony but liveness does ([Castro and Liskov](http://pmg.csail.mit.edu/papers/osdi99.pdf)). The correct sentence is therefore: BSSG preserves capability under evidence-plane health and preserves its denial discipline under evidence-plane failure, and the adversary chooses which regime applies.

**Privacy.** Witnessing, receipts, and lineage records are, by construction, a record of what an agent tried to do and to whom. A deployment MUST declare what is recorded, who can read it, and for how long. Digest-only binding of parameters is the mechanism this specification uses to keep payloads out of receipts, at the cost that a receipt cannot be audited for content without out-of-band access to the parameters. Transparency is not a substitute for correctness: "A transparent system is not necessarily an accurate, privacy-enhanced, secure, or fair system." ([NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)).

**Diagnostics versus concealment signalling.** Rich reason codes serve auditors and also serve a probing subject. The tension is unresolved (OD-11).

---

## 28. Limitations and out-of-model residue

Stated plainly rather than softened.

1. Semantic content of permitted effects. A permitted effect type to a permitted target with an adversarial payload is allowed.
2. Compromise of the decision point (A5). Total collapse; no graceful degradation exists.
3. Collusion at or above the trust-root threshold. Undetectable by construction.
4. A legitimate adjudicator who is simply wrong. Irreducible; a governance problem in an architecture costume.
5. Covert and side channels, physical channels, and human operators inside their authority.
6. The subject's internal states, beliefs, and intentions.
7. Effectiveness of any kind. Whether BSSG changes any outcome is not an architectural question and is not answered here.
8. Composition of individually authorized effects. The kernel evaluates one request at a time and has no composition analysis.
9. The honest-quorum problem: a live, responsive, protocol-conformant, wrong witness satisfies `WitnessHealthy`.
10. A consistent liar. An agent that produces internally consistent false evidence is invisible to contradiction-based detection.
11. Cross-session and cross-restore rollback (OD-2), pending a named external monotonicity root.
12. Correctness of the canonicalization implementation. A bug here is a silent total failure with no defence in depth.
13. Long-run operational viability under the authority ratchet of Section 18. Whether operators will run a system that ratchets toward zero authority is a socio-technical question this architecture cannot settle.
14. Auditing as a precondition. Every DETECTABLE claim is void where nobody audits ([Crosby and Wallach](https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf)).

Documenting unmeasured properties is itself a governance obligation: "The risks or trustworthiness characteristics that will not or cannot be measured are properly documented", and "The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk." ([NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)).

---

## 29. Relation to SHVVP empirical phases

SHVVP v0.8 is a frozen preregistration instrument ([SHVVP v0.8](https://zenodo.org/records/21583202)). Its relationship to this document is strictly one-directional: SHVVP constrains what BSSG may claim, and BSSG supplies an architecture that SHVVP's phases could, in principle, later evaluate.

- **Phase A and Phase B** concern screening and confirmation of empirical questions that this document must not anticipate. No Phase B result exists to cite and none is cited.
- **Phase C** concerns concealment conditions. The behavioural reading of non-advantage of concealment is exactly Phase C's estimand and is deliberately excluded from Section 23.
- **Carriage discipline.** SHVVP's rule that an instrument is carried only by non-producer lineages applies to BSSG by inheritance: this draft was produced by an AI producer with council input from four model families, and none of those seats may be counted as a carry. A BSSG carry requires an independent implementation of the kernel by a non-producer lineage that reproduces every frozen vector.
- **Prohibited inheritance.** BSSG MUST NOT cite SHVVP's suite counts, trust roots, or independent carriage as evidence that a BSSG enforcement kernel is engineered or effective. Those artifacts belong to the evidence-scoring plane.

XZ Protocol and Corpus, XZ Empirical, CVE-Bench, and Mythos-Class are all future work under this program chain. Any statement about BSSG's effect on any benchmark is unavailable at v0.1 and will remain unavailable until those instruments produce results under their own preregistrations.

---

## 30. Open design decisions

Summarized here; enumerated with options and consequences in `OPEN_DECISIONS.md`.

| ID | Decision | Status |
|---|---|---|
| OD-1 | Canonicalization versus wrapped-byte signing as the normative binding method | UNRESOLVED |
| OD-2 | External monotonicity root for cross-session rollback | UNRESOLVED |
| OD-3 | Numeric freshness bounds per evidence type | UNRESOLVED |
| OD-4 | Hash and signature agility, including any post-quantum boundary | UNRESOLVED |
| OD-5 | Reconciling append-only logs with a current-corrected-value view | UNRESOLVED |
| OD-6 | Strict narrowing versus non-increase plus dependent-capability removal | UNRESOLVED, seats disagree |
| OD-7 | Split or co-located decision and administration roles | UNRESOLVED |
| OD-8 | Maximum session duration and re-arming semantics | UNRESOLVED |
| OD-9 | Whether evidence independence and non-bypassability are optional at Minimal | UNRESOLVED, seats disagree |
| OD-10 | Contract and policy as digests only, versus as normative schemas | UNRESOLVED, forced by the six-schema constraint |
| OD-11 | Diagnostic richness versus regime-signal suppression | UNRESOLVED, blocking-adjacent |
| OD-12 | Witness quorum size and diversity rule | UNRESOLVED, no fetched source specifies one |

---

## 31. Conclusion

BSSG v0.1 specifies a small, decidable admission function, an atomic commit protocol that closes the interval between decision and effect, an authority lattice that narrows under degradation, six closed record schemas, eight cross-record invariants, and a reference implementation with an exhaustive kernel suite and an adversarial corpus that includes tests whose assertions are the architecture's own limitations.

What this draft does not have is equally important. It has no empirical support and claims none. It has no carry. Two council seats returned HALT-class verdicts on the pre-draft material and several of their findings remain open, in particular the unresolved tension between diagnostic reason codes and concealment signalling, the absence of a named cross-session monotonicity root, and the unresolved canonicalization fork. Non-equivocation is detection only below high assurance. Evidence independence is an assumption carried by a declaration the architecture cannot check. A colluding witness that looks healthy defeats the kernel silently, and the test suite says so in the form of a passing test.

The honest summary is that BSSG v0.1 is a specification of where the decisions must be made and what must be recorded, not a claim that making them there helps. Whether it helps is an empirical question that belongs to SHVVP and to instruments downstream of it, and it has not been asked yet.

---

## 32. References

All URLs below were fetched during the evidence-gathering phase and are reproduced from the source-grounded evidence report. No URL in this document was invented.

- SHVVP v0.8, Zenodo record: https://zenodo.org/records/21583202
- AX-SH 5, "Is Evidence Independence an Axiom?": https://doi.org/10.5281/zenodo.21539074
- SHUDP, Zenodo record: https://zenodo.org/records/21522932
- Saltzer and Schroeder, The Protection of Information in Computer Systems: https://web.mit.edu/Saltzer/www/publications/protection/Basic.html
- NIST CSRC glossary, reference monitor: https://csrc.nist.gov/glossary/term/reference_monitor
- NIST SP 800-207, Zero Trust Architecture: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
- Schneider, Enforceable Security Policies: https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf
- Miller, Robust Composition: http://www.erights.org/talks/thesis/markm-thesis.pdf
- JSON Schema 2020-12 Core: https://json-schema.org/draft/2020-12/json-schema-core.html
- RFC 8785, JSON Canonicalization Scheme: https://www.rfc-editor.org/rfc/rfc8785.html
- RFC 9052, COSE: https://www.rfc-editor.org/rfc/rfc9052.html
- RFC 8392, CBOR Web Token: https://www.rfc-editor.org/rfc/rfc8392.html
- RFC 9162, Certificate Transparency v2.0: https://www.rfc-editor.org/rfc/rfc9162.html
- RFC 9334, RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html
- RFC 6960, OCSP: https://www.rfc-editor.org/rfc/rfc6960.html
- RFC 5280, X.509 PKI Certificate and CRL Profile: https://www.rfc-editor.org/rfc/rfc5280.html
- SCITT Architecture, draft-ietf-scitt-architecture-13: https://www.ietf.org/archive/id/draft-ietf-scitt-architecture-13.html
- C2SP tlog-witness: https://c2sp.org/tlog-witness
- C2SP tlog-checkpoint: https://c2sp.org/tlog-checkpoint
- Syta et al., CoSi: https://arxiv.org/abs/1503.08768
- Crosby and Wallach, Efficient Data Structures for Tamper-Evident Logging: https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf
- Sigstore Rekor overview: https://docs.sigstore.dev/logging/overview/
- SLSA v1.0 security levels: https://slsa.dev/spec/v1.0/levels
- SLSA v1.0 threats and mitigations: https://slsa.dev/spec/v1.0/threats
- in-toto Attestation Statement v1: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md
- Torres-Arias et al., in-toto, USENIX Security 2019: https://www.usenix.org/system/files/sec19-torres-arias.pdf
- The Update Framework specification: https://theupdateframework.github.io/specification/latest/
- NIST SP 800-218, SSDF v1.1: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf
- NIST AI 100-1, AI RMF 1.0: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- NIST AI 600-1, Generative AI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Lamport, Shostak and Pease, The Byzantine Generals Problem: https://lamport.azurewebsites.net/pubs/byz.pdf
- Castro and Liskov, Practical Byzantine Fault Tolerance: http://pmg.csail.mit.edu/papers/osdi99.pdf
- W3C PROV-DM: https://www.w3.org/TR/prov-dm/

---

*End of BSSG v0.1 DRAFT. This document is DRAFT / NOT CARRIED / NOT PUBLICATION-READY. No statement in it asserts or implies that BSSG is effective, secure, correct, or sufficient.*

---

# Bismillah ir-Rahman ir-Rahim
