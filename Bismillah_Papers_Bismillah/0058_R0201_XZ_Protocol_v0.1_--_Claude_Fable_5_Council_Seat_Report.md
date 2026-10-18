# Bismillah ir-Rahman ir-Rahim

# R0201 -- XZ Protocol v0.1 -- Claude Fable 5 Council Seat Report

**Chronological Index:** 58 of 995  
**Date:** 2024-03-29  
**Section:** IV. XZ Protocol  
**Source File:** xz_protocol_council_claude_fable_5.md  
**Source Format:** md  
**SHA-256:** `d25c83add449eb6b39a6b3448615f50072e3330a3f1507e30b99e2fa684da7e1`  

---

## R0201 · XZ Protocol v0.1 -- Claude Fable 5 Council Seat Report

- section: IV. XZ Protocol
- source_file: xz_protocol_council_claude_fable_5.md
- source_format: md
- text_sha256: d25c83add449eb6b39a6b3448615f50072e3330a3f1507e30b99e2fa684da7e1

# XZ Protocol v0.1 -- Claude Fable 5 Council Seat Report

**Seat:** Claude Fable 5 (Anthropic-family), model-council advisory seat.
**Program:** Structural Honesty, author of record Bilal Syed Arfeen.
**Task:** Independent draft and adversarial review of an initial XZ Protocol v0.1 FROZEN preregistration candidate.
**Date of seat report:** 2026-07-30.

**Seat status disclosure (binding on this report).** This is one advisory seat in a three-model council. This report is NOT peer review, NOT an independent human audit, and NOT a carry. Under the program's own council discipline, producer-lineage review is ADVISORY and NON-CARRYING by construction (SHVVP v0.8, Section 10 and Status), and the Anthropic family is the producer lineage of both the SHVVP v0.8 artifact and the BSSG reference artifact. This seat therefore carries a structural conflict that no wording can remove: it is reviewing an instrument chain its own model family helped produce. That conflict is disclosed here, is repeated in the adjudicator-dependence finding (F-7), and caps the evidential weight of every judgment in this report at "advisory consistency check."

**Sources read for this seat (local corpus):** DOI_INDEX.md; SHVVP_v0_8_flagship.txt Sections 0, 0.1-0.3, 1, 2, 4, 5, 5.1-5.4, 8 (headers and claim rules), 9-14, amendment record and provenance note; BSSG_PAPER.txt (abstract, Sections 1-3, disclosures, DOIs); BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md Sections 1-8, 11, 19, 22-context; ATTACK_AND_FALSIFIER_REGISTER.md in full; REQUIREMENTS_TRACEABILITY.md in full; SHUDP_v0_5_flagship.txt Axiom 5 canonical form and adjudication discipline; SHUDP_v0_4.txt (spot); SHV_Method_v1_1.txt (spot); PMD_v1_8.txt (spot); BAF_v3_0.txt (spot).

**Primary XZ sources permitted for citation:** the Andres Freund disclosure on [oss-security](https://www.openwall.com/lists/oss-security/2024/03/29/4); the [NVD record for CVE-2024-3094](https://nvd.nist.gov/vuln/detail/cve-2024-3094); the [official xz repository response](https://github.com/tukaani-project/xz/issues/103); and the [GitHub advisory GHSA-rxwq-x6h5-x525](https://github.com/advisories/GHSA-rxwq-x6h5-x525).

**Binding program chain:** AX-SH5 -> SHUDP -> SHVVP -> BSSG -> XZ Protocol -> XZ Corpus -> XZ Empirical. The XZ Protocol inherits upward and may not weaken anything frozen upstream. Where this draft and the deposited SHVVP v0.8 ([doi:10.5281/zenodo.21583202](https://doi.org/10.5281/zenodo.21583202)) could be read as differing, SHVVP governs unless a formal amendment is proposed and recorded; two such potential conflicts are resolved explicitly in Part III.

---

# PART I -- CANDIDATE PROTOCOL TEXT AND OUTLINE

The following is this seat's complete candidate draft for XZ Protocol v0.1. It is written as preregistration text so the council can redline clauses directly. Clauses are numbered XP-n. Text in [SEAT NOTE] brackets is council commentary and would not ship in the frozen instrument.

---

## XZ Protocol v0.1 (candidate) -- A Frozen Preregistration for the Retrospective XZ Structural-Decision Replay

**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise).
**Status (at freeze):** CANDIDATE DRAFT -- NOT FROZEN, NOT CARRIED, NOT DEPOSITED. A v0.1 FROZEN status attaches only after (a) council convergence, (b) resolution of the blocking findings in Part II of the producing seat reports, and (c) the carry rule of Clause XP-21.
**Access at deposit:** OPEN.
**Position in chain:** downstream of BSSG v0.1 (paper record supplied as [doi:10.5281/zenodo.21713180](https://doi.org/10.5281/zenodo.21713180); see Clause XP-24 for the dual-DOI record) and of SHVVP v0.8 ([doi:10.5281/zenodo.21583202](https://doi.org/10.5281/zenodo.21583202)); upstream of the XZ Corpus and XZ Empirical instruments, neither of which exists at this freeze.

### XP-0. What this document is and is not

This document is an evaluation contract for a single retrospective case study: a structural-decision replay of the XZ Utils supply-chain compromise, CVE-2024-3094, disclosed by Andres Freund on 2024-03-29 ([oss-security disclosure](https://www.openwall.com/lists/oss-security/2024/03/29/4); [NVD CVE-2024-3094](https://nvd.nist.gov/vuln/detail/cve-2024-3094); [tukaani-project/xz issue 103](https://github.com/tukaani-project/xz/issues/103); [GHSA-rxwq-x6h5-x525](https://github.com/advisories/GHSA-rxwq-x6h5-x525)).

It is not the corpus, not the empirical paper, and not a claim that BSSG or SHV has been validated. As of this freeze no XZ corpus exists under this protocol, no annotation exists, no conjunct has been scored, and no result of any kind exists. Every number in this document is a commitment made before data. This mirrors, and is bound by, the SHVVP v0.8 freeze discipline: "protocol first, corpus second, paper third."

**Prohibited-language inheritance (frozen).** The prohibited-sentence register of BSSG v0.1 Section 1.3 is inherited in full and extended by Clause XP-19. No effectiveness verb -- prevents, mitigates, reduces, ensures, guarantees, protects, or a paraphrase -- may be applied to BSSG anywhere in this protocol, in the later corpus, in deposit metadata, or in any output of the replay. BSSG v0.1 is an architecture-and-conformance artifact that makes no effectiveness claim; this protocol does not create one retroactively.

### XP-1. Scope and claim boundary (frozen)

1. **In scope.** A retrospective replay in which (a) a sealed universe of historical effect-boundary instances from the XZ case is enumerated under a frozen procedure; (b) for each instance, a Condition A record and a Condition B record are produced under staged blinding; and (c) the frozen BSSG kernel decision function is evaluated on Condition B evidence packets, with a frozen fair mapping producing comparable Condition A decisions.
2. **Out of scope.** Attack prevention, harm outcomes, attacker behavior under adaptation, deployment feasibility, performance, cost, generalization beyond the XZ case, and every downstream instrument. No conclusion of this replay generalizes beyond the single historical case examined, and the scope limit MUST appear in the same sentence as any claim it limits (drafting rule inherited from BSSG v0.1 Section 1.2).
3. **Kernel under replay (restated informatively; the BSSG spec governs).** Allow(r) iff ContractMatch AND EffectTypeValid AND TargetAllowed AND WitnessHealthy AND EvidenceCurrent. Conjuncts are three-valued (TRUE, FALSE, UNKNOWN); UNKNOWN never satisfies; FALSE dominates order-independently; DENY_FALSE and DENY_UNKNOWN are distinct outcomes and are never aggregated in any reported figure. BSSG makes no effectiveness claim, and neither does this protocol.

### XP-2. The counterfactual estimand, stated honestly (frozen)

1. **Estimand E-XZ.** For each sealed effect-boundary instance i and condition c in {A, B}, the structural decision D(i, c) that the frozen decision function for condition c yields when applied to the sealed, time-sliced evidence packet for i under the declared assumption set of Clause XP-8. D(i, B) takes values in {ALLOW, DENY_FALSE, DENY_UNKNOWN, NOT-EVALUABLE}. D(i, A) takes values in the frozen Condition A decision vocabulary of Clause XP-6. The primary quantity is the divergence set Delta = {i : D(i, B) differs from D(i, A) under the frozen comparability map}, reported per stratum with full composition.
2. **What E-XZ is.** A statement about structural decision divergence: whether a declared decision architecture, evaluated on declared evidence under declared assumptions, classifies a historical boundary crossing differently from a declared baseline. It is a property of the frozen rules and the sealed packets.
3. **What E-XZ is not.** It is not attack prevention, not harm avoidance, not a claim about what any actor, distribution, or system would have done in 2024, and not a claim about outcomes in any deployment. The modal phrase "would have" applied to any historical outcome is PROHIBITED in all reporting. The admissible verb form is "the kernel evaluates instance i to DENY_UNKNOWN under assumption set DA," and its analogues.
4. **DENY_UNKNOWN honesty rule (frozen).** A DENY_UNKNOWN under Condition B frequently reflects nothing more than the absence, in the modeled deployment, of evidence that no one generated in 2024. It is therefore never reported as detection, never aggregated with DENY_FALSE, and never presented as a favorable result without the same-sentence qualifier that it is assumption-driven. The split of Delta into FALSE-driven and UNKNOWN-driven divergence is a primary reporting obligation (metric XS-2).

### XP-3. Research questions (frozen)

- **RQ1 (enumerability).** Does the frozen enumeration procedure of Clause XP-4, executed independently twice, produce the same effect-boundary universe (set equality on instance identifiers) over the declared artifact graph?
- **RQ2 (decidability of the replay).** For every sealed instance, do the frozen decision functions terminate in exactly one label of their closed vocabularies, with every UNKNOWN carrying a typed reason code?
- **RQ3 (divergence structure).** What is Delta, per boundary stratum, and what is its composition across {ALLOW vs DENY_FALSE vs DENY_UNKNOWN vs NOT-EVALUABLE} and across the five conjuncts?
- **RQ4 (assumption sensitivity).** Which members of Delta survive every admissible alternative in the frozen sensitivity grid (actor-role mapping alternatives, WithinAuth interpretation alternatives, UNKNOWN tipping)? Only these members may be described as mapping-robust.
- **RQ5 (reliability).** Do two blinded adjudicators reproduce conjunct scoring and fact adjudication at Krippendorff alpha at least 0.80 (SHVVP M12 gate, inherited)?
- **RQ6 (incremental forensic value, inherited).** The SHVVP v0.8 Phase A questions over M1-M12 and T1-T8 are inherited by reference and are not restated as new commitments (Clause XP-11).

No RQ asserts, and no answer to any RQ can establish, an effectiveness claim about BSSG.

### XP-4. Retrospective effect-boundary universe and enumeration procedure (frozen)

1. **A priori boundary classes (frozen strata).** The protocol freezes six boundary classes before any corpus work. These are classes of decision points at which, in the historical record, an artifact or authority crossed from one custody or execution domain into another:
   - **S1 COMMIT** -- acceptance of a change into the upstream source repository under a maintainer identity.
   - **S2 RELEASE** -- creation and signing of a distributed release artifact (including generated tarballs that differ by declared design from the tagged source).
   - **S3 BUILD** -- execution of a build recipe transforming released source into a binary in a downstream build environment, including conditional activation logic sensitive to architecture, compiler, linker, or packaging context.
   - **S4 DISTRIBUTION** -- publication of a built package into a distribution channel consumed by downstream systems.
   - **S5 INSTALLATION** -- installation or upgrade of the package onto an end system.
   - **S6 RUNTIME-AUTHENTICATION** -- runtime linkage or invocation of the artifact within an authentication-relevant process boundary.
   These six strata are a priori: they are derivable from the public shape of the incident as disclosed ([oss-security](https://www.openwall.com/lists/oss-security/2024/03/29/4); [NVD](https://nvd.nist.gov/vuln/detail/cve-2024-3094)) without reference to any ledger fact, mechanism detail, or corpus label. Nothing in this clause encodes which instances in any stratum were divergent; that is corpus content and appears nowhere in this protocol (Clause XP-18).
2. **Enumeration procedure (frozen).** The non-blinded custodian enumerates instances by applying the following rule to the declared artifact graph: an instance exists for every (stratum, artifact, custody transition) triple recorded in the public forensic record within the frozen observation window, for BOTH the affected release lineage AND at least one clean prior lineage and one clean successor lineage. Enumeration is structural: it is driven by the artifact graph's edges, not by knowledge of where divergence occurred. The observation window, repository set, distribution set, and lineage list are fixed in the custodian's pre-seal manifest.
3. **Coverage floor (frozen).** The universe MUST contain instances from all six strata and MUST contain clean-lineage instances in every stratum in which affected-lineage instances appear. An enumeration that covers only the compromised path is INVALID and cannot be sealed. This is the structural anti-hindsight control: the universe cannot be built around the known-bad chain.
4. **Seal.** The custodian hash-commits the instance list, the per-instance evidence-packet manifests, and the enumeration inputs, and records the commit in the run log before any executor, annotator, or adjudicator receives any material. The cardinality of the universe and its per-stratum counts are UNKNOWN in this document by design and become fixed by the seal, exactly as SHVVP v0.8 Section 5.1 fixes the Divergence Ledger cardinality. Post-seal universe changes are substantive amendments and void confirmatory status for the affected analyses (Clause XP-22).
5. **Dual enumeration (frozen).** A second enumerator, independent of the custodian and without ledger access, executes the same frozen rule. RQ1 is answered by set comparison. Non-equality above a frozen tolerance of zero instances (set equality required) yields ENUMERATION-DISCORDANT, and the universe may not be sealed until the discordance is resolved and logged.

### XP-5. Condition A -- fair conventional baseline (frozen; labels bound to SHVVP)

1. **Label binding (frozen, conflict-resolved).** Condition A IS the conventional baseline and Condition B IS the SHV/BSSG-enhanced condition. This binding is fixed by deposited SHVVP v0.8 Section 5 ("Condition A (conventional baseline, independent team)"; "Condition B (SHV-enhanced)") and is inherited unchanged. Any draft, table, script, or figure that reverses these labels is defective and MUST be corrected with a logged correction record, never silently (see Part III, Resolution R-1).
2. **Condition A stack.** A competent SLSA-style provenance, in-toto step attestation, signature verification, source-to-artifact diff, reproducible-build check, and standard static and malware scanning stack, implemented and configured by a team independent of the SHV implementers, per SHVVP v0.8 Sections 4 and 5.1. Competence means documented defaults of each tool at its published recommended settings, attested in a configuration manifest signed by the baseline team before unsealing.
3. **Condition A decision vocabulary (new in this protocol, frozen).** Because the baseline stack is a verification stack rather than an authorization kernel, a frozen comparability map assigns each instance a Condition A decision in {PASS, FAIL, NO-VERDICT}: FAIL if any baseline verifier configured per its documented defaults rejects the instance's artifacts; PASS if all applicable verifiers accept; NO-VERDICT if no baseline verifier is applicable to that boundary instance or required inputs do not exist in the packet. The comparability map for divergence is: D(i, A) = PASS corresponds to ALLOW; FAIL corresponds to DENY_FALSE; NO-VERDICT corresponds to a typed Condition A analogue of UNKNOWN and is never scored as PASS.
4. **Fairness rules (frozen).**
   - (a) Every ambiguity in mapping a baseline tool's behavior to {PASS, FAIL, NO-VERDICT} is resolved in the direction most favorable to Condition A, and the resolution is logged per instance.
   - (b) Condition A is never required to produce evidence types its tools do not emit; absence of a BSSG-specific record type is NO-VERDICT for A, not FAIL.
   - (c) The baseline team receives the identical evidence packets, time-sliced identically, at the same time as the Condition B team.
   - (d) Where the baseline's own documentation mandates fail-closed behavior on a missing attestation, that documented behavior is used; it is not weakened to make Condition B look better, and not strengthened beyond documentation to make Condition A look better.
5. **Fairness attestation.** The baseline team signs an attestation that the configuration meets published recommended settings and that no fairness rule was violated. A breached attestation triggers falsifier XZ-F6.

### XP-6. Condition B -- BSSG/SHV-enhanced mapping (frozen)

1. Condition B is Condition A plus the SHV/BSSG layer, per SHVVP v0.8 Section 5: the declared transformation contract, caller-conditioned outcome enumeration, recursive Bayyinah verification, independent projection reconciliation, UNKNOWN typing, and the descendant correction ledger, with the BSSG v0.1 kernel of Clause XP-1.3 as the decision function.
2. **Modeled-deployment declaration (frozen).** Because no BSSG deployment existed in 2024, Condition B evaluates the kernel over a declared modeled deployment: a frozen document specifying, per stratum, the hypothetical contract registry, effect-type registry, target scopes, witness set W, evidence ledger L, freshness authority, and the WithinAuth interpretation (Clause XP-9). Every element of the modeled deployment is a declared assumption, enumerated and tagged in the assumption register (Clause XP-8). The kernel is evaluated on the sealed packet AS IF the modeled deployment's records were being requested; any record the historical evidence cannot supply is UNKNOWN, never synthesized as TRUE.
3. **Contamination barrier.** Condition B materials (contracts, modeled-deployment document, kernel tooling) are never disclosed to the Condition A team; Condition A configuration is disclosed to Condition B only as the inherited SHVVP baseline definition. Personnel and model instances do not overlap across conditions. Breach is logged and triggers falsifier XZ-F7.

### XP-7. Staged blinding and information barriers (frozen)

1. **Impossible-blinding honesty clause (frozen).** The XZ compromise is one of the most publicly documented supply-chain incidents on record. No human or model participant can be presumed ignorant of its existence, of its general mechanism, or of its published chronology. This protocol therefore does NOT claim participant ignorance of the incident, and any such claim in any output is PROHIBITED. Blinding in this protocol means exactly and only:
   - (a) **Ledger blinding.** No executor, annotator, or adjudicator has access to the sealed Divergence Ledger or to the sealed universe's affected/clean lineage tags.
   - (b) **Mechanism-citation discipline.** A finding, annotation, or conjunct score whose recorded justification cites mechanism knowledge not derivable from the instance's sealed, time-sliced evidence packet is a label-dependence event, counted under inherited metric M10, with zero tolerance under inherited threshold T6.
   - (c) **Condition and identity concealment at adjudication.** Adjudicators receive annotation records stripped of condition labels, team identity, and annotator identity, in randomized order.
   - (d) **Custodian isolation.** The non-blinded custodian performs no annotation, no adjudication, and no analysis.
2. **Stages.** Stage 0: custodian seals ledger, universe, and packets. Stage 1: dual enumeration check (RQ1). Stage 2: condition execution (A team, B team, barrier per XP-6.3). Stage 3: conjunct annotation on Condition B records and decision mapping on Condition A records. Stage 4: blinded dual adjudication. Stage 5: analysis on hash-verified frozen tables only. Each stage's outputs are hash-committed before the next stage begins; the run log records every hash with a timestamp.
3. **Time-sliced evidence packets (frozen; the load-bearing anti-hindsight control).** Each instance's packet contains only artifacts, records, and metadata whose historical timestamps precede or equal that instance's historical decision time. In particular, packets for pre-disclosure instances contain no advisory, no disclosure email, and no post-2024-03-29 forensic material. The packet manifest is sealed per XP-4.4. Post-disclosure knowledge can then enter scoring only through a participant's memory, which is exactly what the M10 citation discipline detects and counts.

### XP-8. Sealed ground truth, evidence-packet commitments, and the assumption register (frozen)

1. **Ground truth.** The sealed Divergence Ledger of SHVVP v0.8 Section 5.1 is inherited unchanged: classes K1 (undeclared executable divergence), K2 (conditional-build activation condition), K3 (downstream propagation), K4 (maintainer/release-authority fact), K5 (correction/reversion lineage), with "consequential fact" meaning an adjudicated member of K1-K3 and nothing else. The ledger is sealed and hash-committed by the custodian before any executor session; cardinality is fixed by the seal.
2. **Auxiliary corpora.** The SHVVP-frozen auxiliary corpora are inherited by reference: the 200-item legitimate-difference corpus (40 hard), the 240-item discrimination set, and the sealed descendant universe as the denominator for correction reach.
3. **Assumption register (new in this protocol, frozen).** Every declared assumption of the modeled deployment (XP-6.2) and of the WithinAuth interpretation (XP-9) receives an identifier DA-n, a statement, a tag in {LOAD-BEARING, CONTEXTUAL}, and a list of the conjuncts whose evaluation depends on it. An assumption is LOAD-BEARING if flipping it can change any D(i, B). The register is sealed with the universe. Any conjunct score that rests on an unregistered assumption is INVALID and is rescored.

### XP-9. Evidence-independence and WithinAuth treatment (frozen)

1. **Canonical form inherited.** Axiom 5 is carried as stated in SHUDP v0.5: for every covered event within the declared boundary there exist a witness w in W and a record r in L such that r evidences the event, generation of r is attributable to w, and not WithinAuth(gen(r), S), where WithinAuth(x, S) holds exactly when S can cause, modify, suppress, reconfigure, or credential x without an independently detectable violation. A5 is quantified over the acting substrate S, not the operator institution.
2. **Fixed interpretation before data.** The WithinAuth interpretation for each stratum's modeled deployment -- which historical actors and systems constitute S, and which record-generation acts lie inside S's authority -- is fixed and sealed in the assumption register before any annotation. In the XZ case S at strata S1-S2 includes the release-engineering authority as historically held; consequently, any modeled witness whose records that authority could cause, modify, suppress, reconfigure, or credential without independently detectable violation FAILS WithinAuth and discharges nothing. Caller-supplied evidence is WithinAuth of the supplier and discharges nothing under evidence independence (BSSG paper, Section on evidence independence).
3. **NOT-EVALUABLE discipline (inherited from SHUDP v0.5 adjudication practice).** Where the declared A5 objects (E*, B, W, L, fixed WithinAuth interpretation) cannot be given a historically grounded modeled value for an instance, the WitnessHealthy conjunct for that instance is NOT-EVALUABLE, not UNKNOWN and not FALSE. No failure is inferred from absence of a declaration that no one made in 2024; equally, no satisfaction is inferred. Axiom-level status and instance-level decision are kept distinct and are both reported.

### XP-10. Annotation schema (frozen)

Each annotation record contains, in a closed schema with additionalProperties false:
- instance identifier, stratum, packet manifest hash;
- condition (A or B) -- stripped before adjudication;
- for Condition B: five conjunct values in {TRUE, FALSE, UNKNOWN, NOT-EVALUABLE}, each with (i) a typed reason code from a closed list, (ii) the packet items relied on, by hash, and (iii) the DA-n assumptions relied on, by identifier;
- for Condition A: verdict in {PASS, FAIL, NO-VERDICT} with tool, version, configuration reference, and packet items relied on;
- free-text justification, which is the object of the M10 mechanism-citation check;
- annotator session identifier and timestamp.
A record with an out-of-schema field, an unlisted reason code, an unregistered assumption citation, or a missing packet-hash citation is structurally rejected before adjudication, in the same spirit as the BSSG gate's structural rejection of caller-supplied derived facts.

### XP-11. Conjunct scoring rules (frozen)

1. Each conjunct is scored solely from the sealed packet plus the sealed modeled-deployment document. Scoring is fail-closed: absence, unverifiability, scope mismatch, or evaluator error yields UNKNOWN with a typed reason code, never TRUE.
2. Kernel composition is computed by frozen executable code shipped with the protocol, never by hand: ALLOW iff all five TRUE; DENY_FALSE if any FALSE; DENY_UNKNOWN if no FALSE and at least one UNKNOWN; NOT-EVALUABLE if any conjunct is NOT-EVALUABLE under XP-9.3 and no conjunct is FALSE. [SEAT NOTE: FALSE dominates NOT-EVALUABLE by the same order-independent dominance the BSSG kernel gives FALSE over UNKNOWN; council should confirm.]
3. The text and the shipped code are the same rule written twice; a divergence between them is a defect raised as a finding, never resolved by an analyst at analysis time (rule inherited from SHVVP v0.8 Section 0).
4. No caller-supplied derived fact is admissible: an annotation asserting a conjunct value without packet-hash citations is rejected structurally (XP-10).

### XP-12. Inherited metrics M1-M12 and BSSG-specific seam metrics (frozen; conflict-resolved)

1. **Inheritance (frozen).** SHVVP v0.8 Section 5.2 freezes metrics M1 through M12 -- twelve metrics, not nine -- together with thresholds T1 through T8 and the Phase A decision table A1-A6. This protocol inherits all of them BY REFERENCE, unchanged, for the forensic-comparison layer of the replay. Any statement anywhere in this program that SHVVP froze nine metrics is defective and is corrected non-silently (Part III, Resolution R-2). This protocol renumbers nothing, prunes nothing, and adds nothing to the M-series; altering the M-series would require a formal SHVVP amendment, and none is proposed here.
2. **Seam metrics (new, additive, descriptive only).** The following XS-series metrics are specific to the kernel-replay seam that SHVVP Phase A does not itself instrument. Each is descriptive; none carries an inferential test; each names its denominator:
   - **XS-1 Decision distribution.** Count of ALLOW / DENY_FALSE / DENY_UNKNOWN / NOT-EVALUABLE per condition per stratum. Denominator: sealed instance count of that stratum.
   - **XS-2 Divergence composition.** |Delta| per stratum, split by driving value (FALSE-driven vs UNKNOWN-driven vs NOT-EVALUABLE-driven) and by conjunct. Denominator: sealed instance count of that stratum. The FALSE/UNKNOWN split is a primary reporting obligation (XP-2.4).
   - **XS-3 Assumption load.** Mean and maximum count of LOAD-BEARING DA-n citations per conjunct evaluation, per stratum. Denominator: conjunct evaluations in the stratum.
   - **XS-4 Mapping-sensitive share.** Fraction of Delta members whose membership changes under any admissible alternative in the sensitivity grid (XP-16). Denominator: |Delta|.
   - **XS-5 WithinAuth evaluability.** Fraction of witness-role mappings for which WithinAuth is evaluable from the sealed record. Denominator: witness-role mappings in the modeled deployment.
   - **XS-6 UNKNOWN typing completeness.** Fraction of UNKNOWN conjunct values carrying a typed reason code from the closed list. Denominator: UNKNOWN conjunct values. Frozen requirement: 1.00; anything less is a protocol-execution defect.

### XP-13. Thresholds and four-way decision labels (frozen)

1. **Inherited thresholds.** T1-T8 govern the inherited M-series exactly as frozen in SHVVP v0.8 Section 5.3, including the M12 Krippendorff-alpha gate at 0.80 with the 0.67-0.79 TENTATIVE band and the below-0.67 INDETERMINATE-ADJUDICATION rule.
2. **Replay-layer thresholds (new, frozen).**
   - **XT-1 UNKNOWN-domination cap.** If, within a stratum, more than 50 percent of Condition B conjunct evaluations are UNKNOWN, that stratum's divergence characterization is NOT-EVALUABLE: divergence driven predominantly by modeled-evidence absence is an artifact of the assumption set, not a finding about structure.
   - **XT-2 NOT-EVALUABLE cap.** If more than 25 percent of a stratum's instances are NOT-EVALUABLE under XP-9.3, that stratum is NOT-EVALUABLE for headline reporting and is reported in full in the appendix ledger.
   - **XT-3 Mapping-robustness bar.** Only Delta members with XS-4 sensitivity zero across the entire frozen grid may be called mapping-robust; all others carry the MAPPING-SENSITIVE tag in every mention.
3. **Four-way protocol outcome labels (closed list, frozen).** Every registered claim of Clause XP-14 resolves to exactly one of: **FALSIFIED**, **NOT-FALSIFIED**, **INDETERMINATE-ADJUDICATION**, **NOT-EVALUABLE**. NOT-FALSIFIED additionally requires the M12 gate passed and every denominator complete or UNKNOWN-scored, exactly parallel to the SHVVP Phase A rule. Negative results are preserved and reported in the audit ledger; a FALSIFIED label is a publishable primary outcome of this program, not a suppressible one.

### XP-14. Falsifier register (frozen)

Each falsifier is a finite observation. One occurrence flips the named claim. Falsifiers are never averaged into a pass rate (discipline inherited from the BSSG Attack and Falsifier Register).

| ID | Registered claim | Falsifying observation | Resulting label logic |
|---|---|---|---|
| XZ-F1 | The enumeration procedure is complete over the declared graph | A post-seal discovery of a (stratum, artifact, custody transition) triple satisfying the frozen rule but absent from the sealed universe | Claim FALSIFIED; affected analyses NOT-EVALUABLE; universe reseal requires amendment |
| XZ-F2 | The replay respects mechanism-citation blinding | Inherited M10 at least 1 (any load-bearing post-hoc mechanism citation) | Blinding claim FALSIFIED (T6 zero tolerance); affected instances excluded and listed |
| XZ-F3 | The BSSG mapping yields structural decision divergence on the XZ chain | Delta empty in every stratum after adjudication with M12 at least 0.80 | Divergence claim FALSIFIED; the negative result is deposited and reported as a primary outcome |
| XZ-F4 | Divergence characterization is evidence-driven, not assumption-driven | XT-1 breached in a stratum | Stratum NOT-EVALUABLE; no divergence language for that stratum |
| XZ-F5 | Adjudication is reliable | M12 below 0.67 on either fact adjudication or conjunct scoring | INDETERMINATE-ADJUDICATION; rubric retrained, third blinded adjudicator added, both scores reported |
| XZ-F6 | Condition A is a fair competent baseline | Baseline attestation breached, a below-default configuration found, or any A-mapping ambiguity resolved against Condition A | Fairness claim FALSIFIED; all comparative results NOT-EVALUABLE |
| XZ-F7 | Information barriers held | Any logged cross-condition disclosure of Condition B materials, or personnel/model-instance overlap | Barrier claim FALSIFIED; affected instances excluded; if exclusions exceed 10 percent of the universe, the run is NOT-EVALUABLE |
| XZ-F8 | UNKNOWN discipline held in execution | Inherited M11 at least 1 (any absent projection, record, or attestation scored clean/compliant/safe), or any UNKNOWN resolved to TRUE by default, retry, cache, or override (AF-7 analogue) | Discipline claim FALSIFIED (T8 zero tolerance) |
| XZ-F9 | Evidence-independence treatment is sound | Any WitnessHealthy TRUE whose witness record generation is WithinAuth of the modeled subject (AF-6 analogue) | Treatment claim FALSIFIED; conjunct rescored |
| XZ-F10 | Reporting discipline held | Any published figure aggregating DENY_FALSE with DENY_UNKNOWN, omitting a required MAPPING-SENSITIVE tag, or using a prohibited effectiveness verb or "would have" outcome modal | Reporting claim FALSIFIED; correction record required, append-only |
| XZ-F11 | Denominators are sealed | Any metric computed against a denominator differing from the sealed manifest | Claim FALSIFIED; the computation is void |
| XZ-F12 | The protocol itself is internally consistent | Shipped decision code and protocol text yield different labels on any input | Consistency claim FALSIFIED; finding raised; frozen version required to repair |

Every registered claim resolves through this table to one of the four labels of XP-13.3. INDETERMINATE-ADJUDICATION and NOT-EVALUABLE are reported with the same prominence as FALSIFIED and NOT-FALSIFIED; none is a failure to publish.

### XP-15. Missing data and UNKNOWN handling (frozen)

1. Missing, absent, unverifiable, or out-of-scope evidence is UNKNOWN with a typed reason code; it is never imputed favorably, never defaulted, and never dropped silently (inheritance of the SHVVP UNKNOWN discipline and BSSG R-S2 fail-closed requirements).
2. A missing or corrupt packet item renders dependent conjuncts UNKNOWN and is logged as a packet defect; if packet defects affect more than 10 percent of a stratum's instances, the stratum is NOT-EVALUABLE.
3. Lost or crashed annotation sessions are recorded as INDETERMINATE session outcomes and reannotated by a different annotator; the original record is preserved append-only.
4. The protocol applies the UNKNOWN discipline to itself: every value not fixed here is listed in the residual-UNKNOWN register at freeze (custodian identity and seal hashes; universe cardinality and per-stratum counts; modeled-deployment parameter values; annotator and adjudicator identities; analysis software versions) and no favorable default may be assumed for any of them.

### XP-16. Analysis plan and sensitivity analyses (frozen)

1. **Descriptive posture.** The replay is a single-case construct validation. There is no hypothesis test across conditions, no p-value, no population claim, and no inferential novelty claim; this inherits both the SHVVP Phase A inferential-honesty clause and the SHVVP v0.8 withdrawal of route-level inference. Where intervals are reported for inherited M-series quantities, they are item-level bootstrap intervals computed exactly as SHVVP freezes them, and nothing else.
2. **Dependence among instances.** Boundary instances within a lineage are causally dependent: one upstream state propagates downstream. Instances are therefore grouped into lineage clusters at seal; any resampling resamples whole clusters, never instances; per-stratum tables are reported without cross-stratum pooling; and no statement treats instance counts as independent observations.
3. **Primary outputs.** The sealed-universe description; XS-1 through XS-6 per stratum; the inherited M-series results per the SHVVP contract; the falsifier ledger with one four-way label per registered claim; the full assumption register with per-assumption citation counts.
4. **Sensitivity grid (frozen before data).**
   - (a) Actor-role mapping alternatives: the sealed mapping table (XP-17) lists, per role assignment, every admissible alternative; the kernel is re-evaluated under each; XS-4 reports the result.
   - (b) WithinAuth alternatives: at least two frozen interpretations per stratum where the register records interpretive ambiguity, spanning the narrowest and broadest defensible readings.
   - (c) UNKNOWN tipping: each UNKNOWN conjunct value is flipped to TRUE and to FALSE in turn (tipping-point style); Delta membership changes are reported per instance.
   - (d) Time-slice tolerance: packet cutoffs shifted by the frozen timestamp-uncertainty window for instances whose historical timestamps carry recorded uncertainty.
5. No sensitivity analysis may promote a result; sensitivity can only demote a Delta member from mapping-robust to MAPPING-SENSITIVE or demote a stratum to NOT-EVALUABLE.

### XP-17. Actor-to-role mapping discipline (frozen)

1. A sealed mapping table assigns each historical actor and system (upstream maintainers, release-engineering authority, distribution build infrastructure, package archives, installing systems, runtime hosts) to BSSG roles (subject, witness, decision point, enforcement point, freshness authority, adjudicator domains) per stratum, with a stated basis in the public record for each assignment.
2. Every assignment carries a confidence tag in {SETTLED, CONTESTABLE}; every CONTESTABLE assignment lists its admissible alternatives, which populate the sensitivity grid.
3. No mapping may place the same historical authority as both subject and witness for the same instance unless the purpose is to demonstrate a WithinAuth failure; such demonstrations are labeled as such.
4. The historical maintainer-identity question (which natural person or persons controlled which identity) is explicitly OUT OF SCOPE: roles bind to authority positions evidenced in the public record ([xz issue 103](https://github.com/tukaani-project/xz/issues/103)), never to identity attributions, and the protocol makes no claim about any natural person.

### XP-18. Separation of a priori content from corpus content (frozen)

This protocol contains, and may contain: boundary classes (XP-4.1), the enumeration rule, condition definitions, blinding stages, schemas, scoring rules, metrics, thresholds, falsifiers, the assumption-register format, and the mapping discipline.
This protocol does not contain, and MUST NOT contain: XZ corpus labels; per-instance conjunct outcomes; ledger contents or cardinalities; hazardous payload details; compromised binaries or their identifying hashes beyond citation of the public advisories; activation conditions or recipes; or any information enabling reconstruction of the malicious functionality. Verification hook: a pre-deposit scan confirms the protocol text cites only the four permitted public XZ sources and the program's own DOIs, and contains no artifact hashes other than its own manifest hashes.

### XP-19. Safety and publication posture (frozen)

1. **This protocol: OPEN.** Deposited open-access, hazard-free by construction of XP-18.
2. **Later corpus: SPLIT.** The XZ Corpus deposit is split: open metadata, schemas, clean-lineage materials, annotation tables, and results; hazardous artifacts (compromised release archives, extracted payload objects, activation materials) restricted under a separate DOI whose public record carries only a manifest of content hashes and access conditions. Access requires a logged, justified request under the custodian's access policy.
3. **Metadata hygiene (frozen).** Hazardous artifact names, payload details, and activation conditions never appear in any deposit title, abstract, keyword list, description, or in this protocol text. Compromised binaries are never executed on a reachable host; no public service is exposed (inherited from SHVVP v0.8 Section 5 and the Phase C hard safety boundary posture).
4. **Prohibited-sentence extension (frozen).** In addition to the BSSG v0.1 register, the following are prohibited in all outputs of this protocol and its downstream instruments: "BSSG would have stopped the xz backdoor"; "BSSG would have caught Jia Tan"; any sentence applying prevents, mitigates, reduces, ensures, guarantees, or protects to BSSG; any sentence reporting DENY_UNKNOWN as detection; any unqualified "the kernel denies the attack." The admissible summary form is: "Under assumption set DA and the sealed packet, the kernel evaluates instance i to <label>."

### XP-20. Adjudication and reliability (frozen)

Two blinded adjudicators score fact adjudication and conjunct annotations independently; M12 (Krippendorff alpha) gates every scored conclusion at 0.80, with the TENTATIVE band and INDETERMINATE-ADJUDICATION rule inherited verbatim from SHVVP v0.8 Section 5.3, and kappa additionally reported against the Landis-Koch bands. Adjudicators are non-producer with respect to the Condition B execution; neither adjudicator's control domain is the custodian's. Disagreements are recorded, never forced to consensus; the resolution path (rubric retraining, third adjudicator, dual reporting) is frozen.

### XP-21. Audit and carry plan (frozen)

1. Council review: producer-lineage seats are ADVISORY; carrying review requires executing non-producer seats of different vendor families, each of which must run the shipped decision code against the shipped vectors, recompute the manifest hash, and return a verdict. A HALT from either carrying seat blocks the freeze outright (rule inherited from the SHVVP carrying discipline that HALTED v0.1 through v0.7).
2. The Anthropic family (producer lineage of the SHVVP and BSSG reference artifacts, and of this candidate draft) is EXCLUDED from the carrying pool for this protocol.
3. Every seat report ships unmodified with the deposit; rejected findings are recorded in the amendment record alongside accepted ones (append-only regime records rejected findings, not only accepted ones -- SHVVP A-2.7 precedent).

### XP-22. Deviations and amendment rule (frozen)

1. **Substantive vs editorial.** The SHVVP v0.8 Section 12 rule is inherited verbatim: a change to any estimand attribute, threshold, decision rule or its Boolean structure, analysis population or missing-data rule, universe or ledger content, scope statement, safety boundary, or anchor fact is SUBSTANTIVE and requires a new frozen version, an amendment-record entry, re-hashing, and a re-run carrying audit. Editorial changes (formatting, typography, cross-references incapable of changing any decision) may ship as dated errata.
2. **Deviations in execution.** Any deviation from a frozen procedure during the replay is logged at occurrence with its scope of effect; deviations are reported in full in the results deposit; an unlogged deviation discovered later voids the affected analyses (NOT-EVALUABLE) and is itself a finding.
3. **Non-amendable floor.** The safety posture of XP-19 and the hard safety boundary inherited from SHVVP Section 7.6 are non-amendable by any later version of this protocol.

### XP-23. Zenodo deposit composition (frozen)

The v0.1 FROZEN deposit consists of: (1) this protocol PDF; (2) the machine-readable decision rules and kernel-composition code with tests; (3) the annotation and packet-manifest schemas (closed, additionalProperties false); (4) the falsifier register as a machine-readable table; (5) the assumption-register template and mapping-table template (empty of corpus content); (6) the residual-UNKNOWN register; (7) the amendment record; (8) all council seat reports, unmodified; (9) a SHA-256 manifest over all files; (10) deposit metadata naming the author of record, the OPEN license, and the program-chain DOIs. The deposit contains no corpus content of any kind.

### XP-24. Citation record and the dual-DOI clarification (frozen)

1. Upstream instruments: SHVVP v0.8, [doi:10.5281/zenodo.21583202](https://doi.org/10.5281/zenodo.21583202); SHUDP v0.5, [doi:10.5281/zenodo.21539816](https://doi.org/10.5281/zenodo.21539816); SHUDP v0.4, [doi:10.5281/zenodo.21522932](https://doi.org/10.5281/zenodo.21522932); flagship axioms, [doi:10.5281/zenodo.21500700](https://doi.org/10.5281/zenodo.21500700); consolidated canon v1.4, [doi:10.5281/zenodo.21501912](https://doi.org/10.5281/zenodo.21501912); verification method v1.1, [doi:10.5281/zenodo.21450932](https://doi.org/10.5281/zenodo.21450932); AX-SH 5 companion, doi:10.5281/zenodo.21539074 as cited within SHVVP v0.8 Section 14.
2. **BSSG dual-DOI record (frozen, roles preserved).** The BSSG paper is cited in two distinct roles that MUST NOT be collapsed:
   - **Supplied record role:** the Zenodo record from which this program's working corpus was retrieved is [doi:10.5281/zenodo.21713180](https://doi.org/10.5281/zenodo.21713180) (per the corpus DOI index). This is the version-of-record actually read by this council.
   - **Embedded self-citation role:** the paper PDF itself embeds "Paper DOI: 10.5281/zenodo.21712482" and "BSSG Concept DOI: 10.5281/zenodo.21611192" on its front matter.
   Both identifiers are preserved with their roles stated. The discrepancy between the supplied record identifier and the embedded paper identifier is RECORDED, not silently resolved; the plausible reading is that 21712482 is an earlier version DOI under concept 21611192 and 21713180 is a later version record, but that reading is UNVERIFIED at this freeze and is listed in the residual-UNKNOWN register. Pre-deposit obligation: resolve the version relationship against the live Zenodo records and record the resolution in the amendment record. Citing either DOI as if it were the other, or dropping one, is a citation-integrity defect (falsifier XZ-F10 territory).
3. XZ primary sources: exactly the four permitted URLs of the header, cited as fetched public records; no other XZ source is load-bearing in this protocol.

### XP-25. Residual-UNKNOWN register at freeze (frozen format; values UNKNOWN by design)

1. Custodian identity and seal hashes. 2. Universe cardinality and per-stratum counts. 3. Divergence Ledger cardinality and class counts (fixed by the SHVVP custodian seal). 4. Modeled-deployment parameter values per stratum. 5. Annotator, adjudicator, enumerator, and team identities, and the model families or humans occupying them. 6. The Zenodo version relationship of XP-24.2. 7. Analysis software versions. No favorable default may be assumed for any item.

--- END OF CANDIDATE PROTOCOL TEXT ---

---

# PART II -- ADVERSARIAL STRESS TEST: BLOCKING AND NON-BLOCKING FINDINGS

This seat's analytical angle: methodological integrity of a retrospective single-case replay, with special attention to where the design could quietly manufacture a favorable result. Each finding states the threat, its severity for a v0.1 FROZEN status, and the resolution adopted in the candidate text (or left open for council).

**F-1. Counterfactual validity (BLOCKING if unresolved; resolved in XP-2).**
The deepest threat is estimand conflation: a replay that computes kernel decisions on reconstructed packets and then narrates them as what would have happened in 2024. The counterfactual has at least three missing supports: no BSSG deployment existed; the modeled contracts, witnesses, and freshness authorities are authored in 2026 with full knowledge of the incident; and an adaptive adversary facing a gated boundary is not the historical adversary. Resolution: XP-2 fixes the estimand as structural decision divergence under a sealed assumption register, bans outcome modals ("would have"), and makes the DENY_UNKNOWN/DENY_FALSE split a primary reporting obligation. Residual risk accepted and disclosed: even the disciplined estimand can be socially misread as a prevention claim; XP-19.4's prohibited-sentence extension is the only available control, and it controls the program's language, not its readers.

**F-2. Hindsight leakage (BLOCKING if unresolved; resolved in XP-4, XP-7.3).**
Three channels: (a) universe construction around the known-bad chain; (b) modeled-deployment parameters tuned so the known divergence trips a conjunct; (c) annotator memory of the published mechanism. Resolutions: (a) structural enumeration rule plus the clean-lineage coverage floor plus dual enumeration; (b) the assumption register with LOAD-BEARING tagging plus the sensitivity grid, which exposes parameter choices that carry the result; (c) time-sliced packets plus the inherited M10/T6 zero-tolerance citation discipline. Channel (b) is the least controllable: a 2026 author cannot un-know the incident when writing the modeled contracts. The honest posture, adopted in XP-2.3 and XP-16.5, is that the replay characterizes a declared architecture, it does not discover one; sensitivity can only demote results.

**F-3. Impossible blinding (BLOCKING if the protocol overclaims; resolved in XP-7.1).**
Any claim that participants are blind to the XZ incident would be false on its face and would poison the instrument's credibility. Resolution: the impossible-blinding honesty clause restricts blinding claims to ledger blinding, mechanism-citation discipline, and adjudication concealment, and prohibits stronger claims. This is the same move SHVVP makes by policing mechanism-label dependence (M10) rather than pretending ignorance.

**F-4. Treatment contamination (HIGH; resolved in XP-6.3, XZ-F7).**
Condition B contains Condition A by construction (B = A + SHV), so contamination risk is asymmetric: the danger is Condition A executors absorbing SHV framing (deflating A), or shared personnel/model lineage homogenizing behavior. Resolution: hard barrier, no personnel or model-instance overlap, logged-breach falsifier with a 10 percent exclusion cap. Open for council: whether model instances of the same vendor family on both teams constitutes overlap; this seat recommends YES (family-level separation), consistent with the program's carrying rule that same-vendor seats count once.

**F-5. Dependence among boundary instances (HIGH; resolved in XP-16.2).**
The six strata are a causal chain: one K1 divergence at S2 propagates to S3-S6. Counting each downstream instance as a separate divergence event would multiply one structural fact into many. Resolution: lineage clustering at seal, cluster-level resampling only, per-stratum reporting without pooling, and an explicit ban on treating instance counts as independent observations. This is also why the replay is descriptive: there is no unit of randomization, exactly as SHVVP's Phase A inferential-honesty clause states.

**F-6. Baseline fairness (BLOCKING if unresolved; resolved in XP-5).**
A strawman Condition A is the single most likely way this program could manufacture apparent SHV value. Threat vectors: under-configured baseline tools; resolving tool-output ambiguity against A; demanding record types A's tools do not emit and scoring their absence as A failures. Resolution: independent-team requirement (inherited), documented-defaults competence standard, signed fairness attestation, favorable-to-A ambiguity rule, NO-VERDICT (not FAIL) for inapplicable verifiers, and falsifier XZ-F6 voiding all comparative results on breach. Note the deliberate asymmetry: fairness ambiguities break toward A, sensitivity analyses break against B. Both asymmetries protect the same thing -- a surviving positive result that cannot be attributed to design tilt.

**F-7. Adjudicator dependence (HIGH; partially resolvable only).**
Every adjudicator, human or model, is recruited, instructed, and paid (or prompted) within a single-author program, and the BSSG paper itself discloses that methodology interpretation and amendments are single-author acts with no external governance body. Model adjudicators of every family have trained on public XZ forensics, so cross-family agreement is not evidence of independent judgment about this case. Resolution adopted: non-producer adjudicators, alpha gate, dual reporting, and disclosure. Residual risk accepted and disclosed: M12 measures agreement, not independence; two adjudicators sharing a common bias will agree. This cannot be engineered away inside the program; it can only be disclosed, and XP-21.3's ship-all-seat-reports rule is the transparency backstop. This is a permanent ceiling on the evidential weight of the replay and should be stated in the eventual paper's limitations.

**F-8. Denominator gaming (BLOCKING if unresolved; resolved in XP-4.4, XZ-F11).**
The program's own audit history is the best argument here: SHVVP v0.5 through v0.7 were HALTED precisely for caller-selectable evidence universes and post-result universe assembly (F-P5-1, F-P6-1, F-P7-2). The XZ Protocol must not reintroduce that defect at the corpus layer. Resolution: pre-annotation hash-committed universe and packet manifests, sealed denominators named per metric, post-seal changes as confirmatory-status-voiding amendments, and falsifier XZ-F11. Recommendation to council: adopt the SHVVP v0.8 three-trust-root commitment pattern (commitment authority, independent anchor, run logger) for the custodian's seal rather than a bare hash in a log, since a bare hash held by a single party reproduces the v0.7 defect one level up.

**F-9. Multiplicity (MEDIUM; resolved in XP-16.1).**
With six strata, five conjuncts, twelve inherited metrics, six seam metrics, and a sensitivity grid, there are hundreds of reportable cells; cherry-picking is trivial if inference is permitted. Resolution: no inference anywhere in the replay layer (inheriting the spirit of SHVVP v0.8's withdrawal of route-level inference); closed label lists; complete-table reporting obligations (all strata, all cells, appendix ledger for NOT-EVALUABLE strata); intervals only where SHVVP already froze them. Multiplicity is controlled by refusing the game, not by adjusting for it.

**F-10. Actor-to-BSSG-role mapping ambiguity (BLOCKING if unresolved; resolved in XP-17).**
Who is the subject at the RELEASE boundary -- the maintainer identity, the release process, the hosting platform? Is a distribution's build system a caller, a subject, or a witness? Different defensible mappings yield different kernel outcomes. An unfrozen mapping is a free parameter tunable to any desired result. Resolution: sealed mapping table with SETTLED/CONTESTABLE tags, admissible-alternative enumeration feeding the sensitivity grid, the MAPPING-SENSITIVE reporting tag with the XT-3 robustness bar, and the natural-person exclusion (roles bind to authority positions, not identity attributions -- also the correct ethical posture given that the historical maintainer-identity question is unresolved in the public record).

**F-11. Overclaim risk (BLOCKING if unresolved; resolved in XP-2.4, XP-19.4, XZ-F10).**
The specific overclaim this case invites: "the kernel denies the compromised release, therefore the architecture works." Under the assumption register, most denials at pre-disclosure timestamps will foreseeably be DENY_UNKNOWN -- reflecting that the 2024 ecosystem generated none of the records the modeled deployment requires -- and a naive reading converts modeled-evidence absence into apparent efficacy. Resolution: the DENY_UNKNOWN honesty rule (never detection, never aggregated with DENY_FALSE, assumption-driven qualifier in the same sentence), the XT-1 UNKNOWN-domination cap that withdraws divergence language entirely from assumption-dominated strata, and the prohibited-sentence extension. This seat regards XT-1 as the single most important novel clause in the candidate text.

**F-12. Dual-DOI citation integrity (MEDIUM; resolved in XP-24.2).**
The supplied record is 10.5281/zenodo.21713180; the paper PDF embeds Paper DOI 10.5281/zenodo.21712482 and Concept DOI 10.5281/zenodo.21611192. Silently choosing one would either miscite the artifact actually read or erase the paper's self-identification. Resolution: both roles preserved and stated; version relationship flagged UNVERIFIED with a pre-deposit resolution obligation. Non-blocking for the draft; blocking for deposit metadata if unresolved.

**F-13. Kernel-composition edge case (MEDIUM; OPEN for council).**
The candidate text (XP-11.2) had to invent a composition rule for NOT-EVALUABLE, which is a protocol-layer value, not a BSSG kernel value; the BSSG kernel is strictly three-valued. The draft rules that FALSE dominates NOT-EVALUABLE, and NOT-EVALUABLE otherwise dominates UNKNOWN. Council must either ratify this or map NOT-EVALUABLE conjuncts to UNKNOWN at the kernel and reserve NOT-EVALUABLE for the instance level. This seat weakly prefers the drafted rule because collapsing NOT-EVALUABLE into UNKNOWN would launder "the axiom's objects do not exist historically" into "evidence was absent," which SHUDP v0.5's adjudication discipline keeps distinct for good reason. Either choice must be frozen before any annotation exists.

**F-14. Enumeration rule circularity (MEDIUM; OPEN for council).**
XP-4.2 enumerates instances from "the public forensic record," but most of that record post-dates disclosure and was written because of the compromise; the artifact graph itself is thus partially hindsight-shaped (for example, clean lineages are documented far more thinly than the affected one). Partial mitigation is the coverage floor and dual enumeration; full mitigation is impossible for a retrospective case. Recommendation: add to the limitations section of the eventual paper, and require the enumeration-input manifest to record, per input document, whether it pre- or post-dates 2024-03-29, so that graph asymmetry is measurable rather than invisible.

---

# PART III -- EXPLICIT CONFLICT RESOLUTIONS (SHVVP GOVERNS)

**R-1. Condition labels.** Deposited SHVVP v0.8 Section 5 fixes Condition A = conventional baseline (independent team; SLSA-style provenance, in-toto attestations, signature verification, source-to-artifact diff, reproducible-build checks, scanning) and Condition B = SHV-enhanced (A plus the declared transformation contract, caller-conditioned outcome enumeration, recursive Bayyinah verification, independent projection reconciliation, UNKNOWN typing, descendant correction ledger). Any drafting input to this council that reverses these labels is REJECTED in favor of the deposited SHVVP. No formal amendment is required because no reason to reverse exists; the candidate text binds the labels in XP-5.1 and requires any discovered reversal to be corrected with a logged correction record, never silently.

**R-2. Metric count.** Deposited SHVVP v0.8 Section 5.2 freezes twelve metrics, M1 through M12, with thresholds T1 through T8. Any statement that the frozen set is nine metrics is REJECTED in favor of the deposited SHVVP. The XZ Protocol inherits M1-M12 by reference, unchanged and unrenumbered (XP-12.1); its XS-series seam metrics are additive and descriptive and do not touch the M-series. Altering, pruning, or renumbering the M-series would require a formal SHVVP amendment under SHVVP Section 12; none is proposed, and this council has no authority to make one.

**R-3 (supplementary, from the task's citation-correction instruction).** BSSG paper DOI roles preserved per XP-24.2: supplied record 10.5281/zenodo.21713180 (version actually retrieved and read); embedded Paper DOI 10.5281/zenodo.21712482 and Concept DOI 10.5281/zenodo.21611192 (the paper's self-identification). Neither is silently substituted for the other; the version relationship is a pre-deposit verification obligation.

---

# PART IV -- FALSIFIER SUMMARY

The full register is XP-14 (XZ-F1 through XZ-F12), each yielding exactly one of FALSIFIED, NOT-FALSIFIED, INDETERMINATE-ADJUDICATION, or NOT-EVALUABLE for its registered claim, with negative results preserved as primary publishable outcomes. The three falsifiers this seat considers decisive for program honesty:
- **XZ-F3** makes the null result binding: an empty divergence set after reliable adjudication FALSIFIES the divergence claim and must be deposited as such.
- **XZ-F4 / XT-1** makes assumption-driven divergence non-reportable as a finding: UNKNOWN-dominated strata are NOT-EVALUABLE, closing the largest overclaim channel.
- **XZ-F6** makes baseline unfairness fatal to every comparative result, not merely a caveat.

---

# PART V -- PUBLICATION-READINESS VERDICT

**Verdict for an initial v0.1 draft: CONDITIONALLY READY FOR COUNCIL SYNTHESIS -- NOT READY FOR FREEZE, NOT READY FOR DEPOSIT.**

Basis:
1. The candidate text in Part I resolves, in draft form, all findings this seat rates BLOCKING (F-1, F-2, F-3, F-6, F-8, F-10, F-11), but two frozen-before-data decisions remain genuinely open (F-13 kernel composition of NOT-EVALUABLE; F-14 enumeration-input asymmetry recording) and one is a pre-deposit obligation (F-12 DOI version relationship). A preregistration with open normative decisions cannot be FROZEN.
2. The freeze must be followed by the program's own carry rule: two executing non-producer families of different vendors, with a HALT from either blocking deposit. No carry exists; this seat is producer-lineage and advisory and its approval would count for nothing under the program's own discipline -- correctly so.
3. Custodian designation, the seal architecture (this seat recommends the SHVVP v0.8 three-trust-root pattern per F-8), and the modeled-deployment document must exist before the universe can be sealed; none exists.
4. Nothing in this report claims peer review, independence beyond a model-council advisory seat, or any effectiveness property of BSSG. The candidate protocol makes no effectiveness claim, uses no prohibited verb applied to BSSG, contains no corpus labels, no conjunct outcomes, no payload details, and no activation information, and confines XZ citation to the four permitted public sources ([oss-security](https://www.openwall.com/lists/oss-security/2024/03/29/4), [NVD](https://nvd.nist.gov/vuln/detail/cve-2024-3094), [xz issue 103](https://github.com/tukaani-project/xz/issues/103), [GHSA advisory](https://github.com/advisories/GHSA-rxwq-x6h5-x525)).

**Recommended next actions for the council:** (1) merge seat drafts clause-by-clause with the other two seats; (2) vote F-13 and F-14; (3) verify the Zenodo DOI version relationship; (4) designate custodian and seal architecture; (5) dispatch the merged v0.1 candidate to two executing non-producer families for carry.

-- End of Claude Fable 5 seat report --

---

# Bismillah ir-Rahman ir-Rahim
