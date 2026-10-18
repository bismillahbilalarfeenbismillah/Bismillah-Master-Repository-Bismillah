# Bismillah ir-Rahman ir-Rahim

# R0570 -- AX-SH 5 Model-Council Adjudication Record

**Chronological Index:** 66 of 995  
**Date:** 2024-08-13  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** ax-sh-5-model-council-adjudication.pplx (1).md  
**Source Format:** md  
**SHA-256:** `743aeb0ec6c6a5cf69e486521797e16561d5a36bbaff099945e3de1f6d3eafda`  

---

## R0570 · AX-SH 5 Model-Council Adjudication Record

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: ax-sh-5-model-council-adjudication.pplx (1).md
- source_format: md
- text_sha256: 743aeb0ec6c6a5cf69e486521797e16561d5a36bbaff099945e3de1f6d3eafda

# AX-SH 5 Model-Council Adjudication Record

**Subject:** *Is Evidence Independence an Axiom? Decomposing a Proposed Extension to AX-SH* (Bilal Syed Arfeen, July 23, 2026)

**Council seats:** Claude Opus 4.8 (Anthropic), GPT-5.4 (OpenAI), Gemini 3.1 Pro (Google).

**Independent stress test:** included separately (Section 6), **not** counted as a fourth council vote.

**Adjudication scope (fixed by the source document's own falsification conditions):** A5.1 as the surviving axiom, the independence witness (F-2), and the joint-satisfiability construction (F-7), together with the clause-by-clause status of A5.2-A5.5, the cryptographic boundary, publication defects, and sequencing.

This record is a **cross-model consistency check**, not human peer review. Model-council agreement is not presented as peer review anywhere in this record or the paper.

**Audit-trail packet (in-record pointers).** This adjudication, the three council reviews, the independent stress-test memo, the Claude Fable 5 HALT-AND-ESCALATE audit, and the remediation receipt are all included together in the release packet (`axsh5_release/`, manifested by `README.md` and `SHA256SUMS`). The "companion adjudication" pointer in the paper's author note therefore resolves in-record. The named canonical files this record attests are exactly the regenerated pair `is-evidence-independence-an-axiom-canonical.pplx.md` and `is-evidence-independence-an-axiom-canonical.pdf`, both generated from the single authoritative source `axsh5_content.py` and verified by the G9 concordance receipt (`concordance_receipt.txt`).

---

## 1. Where Models Agree

| Finding | Claude Opus 4.8 | GPT-5.4 | Gemini 3.1 Pro | Evidence |
| --- | --- | --- | --- | --- |
| A5.1 is **not derivable** from A1-A4 and is the sole axiom candidate | ✓ | ✓ | ✓ | A4 is conditional on projections existing; A2 permits an all-internal observer model [1] |
| A5.2 is non-derivable and belongs in a **control layer (SHIELD)**, not the axiom set | ✓ | ✓ | ✓ | A1-A4 are representational; A5.2 is causal; admitting it changes diagnostic→control character, against the flagship non-prevention disclaimer [1] |
| A5.5 is a **theorem from A2** (both halves) | ✓ | ✓ | ✓ | Completeness boundary is the observer model's coverage extent; uncovered-event guarantee is an A2 surface-substrate divergence [1] |
| A5.3 **splits**: no-default half is a theorem; record/escalate half is not cleanly derivable | ✓ | ✓ | ✓ | No-default derives from A4 (violation) and A2 (compliance); recording obligation needs an unproved A1 bridging lemma |
| A5.4 is **not structural** - a deployment condition restated as measured out-of-authority coverage | ✓ | ✓ | ✓ | No architecture verifies operator-external authority; markedness converts the existential to a reportable fraction |
| **Joint-satisfiability construction must be exhibited**, not described as a maturity level | ✓ | ✓ | ✓ | An unshown consistency witness risks vacuity; F-7 is disqualifying if unmet |
| **Cryptographic split is sound**: hash integrity more robust than signature attribution under quantum attack | ✓ | ✓ | ✓ | Grover quadratic vs. Shor break; FIPS 204/205 finalized Aug 13, 2024 [12][13] |
| Paper is **publishable only after major revision**; not deposit-ready as drafted | ✓ | ✓ | ✓ | Two open falsifiers (F-2, F-7) plus sketched proofs and publication defects |
| **Sequencing:** finalize AX-SH 5 first; defer corpus/monograph edits until after adjudication | ✓ | ✓ | ✓ | Canon revision restarts an audit clock on a deposited artifact |

---

## 2. Where Models Disagree

| Topic | Claude Opus 4.8 | GPT-5.4 | Gemini 3.1 Pro | Why They Differ |
| --- | --- | --- | --- | --- |
| Whether "SHIELD already contains the gate" can be asserted | No SHIELD text available - flag as a preserved UNKNOWN dependency; keep relocation | Publish A5.2 as a SHIELD control *principle*; state the control-layer derivation the relocation claims | Lead author must **confirm** the relocation and its program implications before deposit | Claude and the stress test emphasize the missing artifact; GPT emphasizes writing the derivation; Gemini frames it as a governance sign-off. Resolved by treating relocation as **proposed** (no artifact claim) - see Decision D3 |
| Positive vs. negative result terminology for F-1 | Reconcile explicitly: contribution = negative decomposition, surviving claim = one positive result; do not silently overwrite the note's "negative result" wording | (Did not foreground this) | (Did not foreground this) | Only the Anthropic seat surfaced the note/PDF terminology conflict; adopted verbatim as Decision D-defect-4 |
| Emphasis on non-apportionment derivation | Keep as explicit deployment rule; add F-condition | Add non-apportionment as transfer #4, prevents "satisfiable by procurement" | (Endorsed measurability generally) | Different depth of attention; converged on "explicit rule + test condition" (D6) |
| Framework-character characterization authority | A governance judgment reserved for the lead; do not ratify silently by council | Type-shift is a clean logical result; state it as such | Lead must confirm | Reconciled by framing it as an **explicit authorial architecture decision** in the paper (D2), contestable via F-3 |

---

## 3. Unique Discoveries

| Model | Unique Finding | Why It Matters |
| --- | --- | --- |
| Claude Opus 4.8 (Anthropic) | The **positive/negative-result terminology conflict** between the working note (line 216, "central negative result") and the PDF ("central positive result") for F-1 | A canonical paper cannot use both labels for one falsification condition; forced an explicit reconciliation in Section 1 of the paper |
| Claude Opus 4.8 (Anthropic) | Broken LaTeX superscript on the event-set symbol (an empty-superscript form) in the **boxed axiom statement** (Section 7 of the draft), where Section 4 correctly used the starred form \(E^{*}\) | A canonical axiom must not carry a typo in its own statement; fixed to \(E^{*}\) throughout |
| GPT-5.4 (OpenAI) | Explicit **two-projection countermodel** (\(W=\{w_1,w_2\}\), \(\pi_1(e)=\pi_2(e)\)) that removes any suggestion A4 was satisfied only vacuously | Strengthened the independence witness against a vacuity objection; adopted in Section 6.2 |
| GPT-5.4 (OpenAI) | Distinguishing **axiom-set satisfiability (A1-A4+A5.1)** from **proposal-bundle implementability (A5.1-A5.5)** as two different claims the draft blurred | Prevented an overclaim about "joint satisfiability of all five"; adopted in Section 7 |
| Gemini 3.1 Pro (Google) | The joint-satisfiability model must handle **asynchronous external-witness failure** without introducing unhandled A3 outcomes or A4 inconsistencies | Motivated `witness-unavailable` as a first-class \(R_{may}\) member and the loss/asynchrony → UNKNOWN rule in Section 7 |

---

## 4. Comprehensive Analysis

**High-confidence findings.** All three council seats converge, without material dissent, on the paper's central architecture: the proposed five-clause "Axiom 5" is not one axiom but four different kinds of thing, and only **A5.1 (acting-system-independent evidence generation)** survives as an axiom candidate. The convergence is strong because each seat reaches it by the same load-bearing textual move, independently verified against the deposited flagship source [1]: Axiom 4's own sentence - *absence of a projection at a point places that point outside the axiom's scope, not inside it as a violation* - makes A4 conditional on projections existing, while A5.1 is existential about existence, so A4 cannot entail it; and A2 permits a system to declare its own logs as its observer model, which is precisely the configuration A5.1 forbids. Where three models trained by different organizations reach an identical model-theoretic judgment from the same primary text, the reliability of that judgment is high. The seats likewise agree that A5.2 is causal where A1-A4 are representational (so it cannot be derived and would change the framework's diagnostic character), that A5.5 is a clean two-part theorem from A2, that A5.3 splits into a derivable no-default theorem and a non-derivable recording obligation, and that A5.4 is institutional rather than structural and should be restated as a measured out-of-authority coverage quantity. On the cryptographic boundary, all three (and the stress test) independently confirm the hash-integrity-versus-signature-attribution split and the August 13, 2024 finalization of FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) [12][13].

**Areas of divergence.** The genuine disagreements are narrow and concern presentation and governance rather than logic. First, the seats differ on how to handle SHIELD: the Anthropic seat and the stress test stress that **no citable SHIELD artifact is available**, so the paper cannot assert SHIELD "already contains" the gate; the OpenAI seat emphasizes writing the control-layer derivation the relocation would rely on; the Google seat frames the whole relocation as requiring **lead-author confirmation** before deposit. These are not contradictory - they are three angles on the same gap - and the adjudication resolves them by stating the relocation as a **proposed** control principle with the derivation given as a shape, and by framing the diagnostic-versus-control characterization as an **explicit authorial architecture decision** (contestable via F-3) rather than a silently ratified fact. Second, only the Anthropic seat surfaced the **positive/negative-result terminology conflict** for F-1; because a canonical paper cannot label one falsification condition both ways, the adjudication adopts the reconciliation that the paper's *contribution* is the negative decomposition while its one *positive result* is the surviving axiom. Third, the seats weight the non-apportionment clause differently; they converge on stating it as an explicit deployment rule with its own test condition (F-9) rather than as a derived theorem.

**Unique insights worth noting.** The most consequential unique contributions were structural, not evaluative. GPT-5.4's insistence on a **two-projection countermodel** and on separating axiom-set satisfiability from proposal-bundle implementability directly shaped Sections 6.2 and 7 of the canonical paper, discharging F-2 and F-7 by exhibited paper models without overclaiming (they remain live against defects or stronger semantics). Gemini 3.1 Pro's attention to **asynchronous external-witness failure** forced the joint-satisfiability witness to treat witness unavailability as a handled A3 incompleteness indicator that would violate A5 in a different run - rather than relaxing the predeclared boundary - the single most important robustness fix in the consistency construction. Final QA further tightened this so that the boundary B is fixed ex ante and an in-B occurrence with missing timely evidence carries two distinct statuses (axiom-level UNSATISFIED (nonconforming); event-level UNKNOWN under Proposition 1), never moved outside B post hoc. Claude Opus 4.8's catch of the **broken \(E^{*}\) superscript in the boxed axiom** and the **note/PDF terminology conflict** are exactly the class of canonical-deposit defect that a logic-only review would miss.

**Recommendation.** The council's collective verdict is **publish after major revision, then deposit as a decomposition paper that ratifies one axiom, relocates one requirement to a proposed control principle, demotes two clauses to theorems (one with a preserved open half), and reclassifies one as a measured deployment condition** - not as "Axiom 5: Observer Independence and Evidence Completeness." The canonical revision in `is-evidence-independence-an-axiom-canonical.pplx.md` implements every gating item below.

---

## 5. Decision Register

| # | Decision | Basis | Status |
| --- | --- | --- | --- |
| D1 | Only **A5.1 survives** as Axiom 5 (Evidence independence), with covered event occurrences and explicit declared boundary \(B\) | All seats + stress test | Implemented (§6.1) |
| D2 | Define independence by a **control predicate** WithinAuth(x,S) - S can cause, modify, suppress, reconfigure, or credential the act without an independently detectable violation - requiring ¬WithinAuth(gen(r),S); **not** by label mismatch auth(gen(r))≠auth(S), which is too weak under overlapping/nested domains. Keep operator authority separate (operator may control both S and witness: satisfies A5, violates A5.4). Labels retained only as illustrative assignments. | Final QA correction; all seats; stress test §4 | Implemented (§6.1, §11) |
| D3 | A5.2 relocation stated as a **proposed SHIELD control principle**; do **not** claim SHIELD already contains it (no citable artifact); confirm the diagnostic→control change as an **explicit authorial architecture decision** | Stress test gap #2; Anthropic UNKNOWN; Google lead-confirmation | Implemented (§8) |
| D4 | Replace categorical "self-attestation is not evidence" with **"self-attestation may be evidence but cannot independently discharge an evidence-independence requirement"** (ISO recognizes first-party evidence) | ISO conformity attestation [11] | Implemented (§11.1, abstract framing) |
| D5 | Exhibit a **finite countermodel** (A1-A4 hold, A5 fails) with **two coherent projections**, verified clause-by-clause | GPT two-projection; F-2 | Implemented (§6.2) |
| D6 | Exhibit a **separate finite joint-satisfiability model** for A1-A4+A5, verified clause-by-clause (using WithinAuth); distinguish axiom-set consistency from proposal-bundle implementability. Boundary **B fixed ex ante** by event class, time interval, and observer commitment; an in-B occurrence lacking timely external evidence carries two distinct statuses (**axiom-level UNSATISFIED (nonconforming); event-level UNKNOWN under Proposition 1**), and is **never moved outside B post hoc**; only ab-initio-excluded events are uncovered. M+'s actual event is a **successful external-witness occurrence**; witness-unavailable is a handled A3 outcome that would violate A5 in a different run, not satisfy it. | Final QA correction; GPT satisfiability split; Gemini async | Implemented (§7) |
| D7 | A5.3a proved as a **proposition** (no-default); A5.3b kept as an **open operational requirement** (unproved A1 bridging lemma) | All seats; stress test §3 | Implemented (§9) |
| D8 | A5.4 as a **deployment condition** measured via \(\mathrm{Ev}(O,e,A)\), reporting out/same/unknown-authority coverage; non-apportionment as an **explicit deployment rule + test (F-9)**; no claim architecture guarantees operator independence | All seats; stress test §4 gap #5 | Implemented (§11) |
| D9 | A5.5 proved as a **proposition** from A2, with temporal-boundary handling | All seats; stress test §3 | Implemented (§10) |
| D10 | Name the **markedness discipline** explicitly as internal methodological consistency, not external proof of generality | Anthropic §9; stress test gap #7 | Implemented (§12) |
| D11 | **Narrow cryptographic claims**: ML-DSA primary, SLH-DSA hash-based alternative (not categorically preferable); size/throughput tradeoff explicit; conditional (not unconditional) retroactive-forgery risk; no "survives quantum" categorical | All seats; stress test §7 | Implemented (§13) |
| D12 | Add **external methodological grounding**: NIST SP 800-53, ISO/IEC 17029, ISO conformity attestation | Stress test; task | Implemented (§8, §11) |
| D13 | Add **disclosure**: self-published on Zenodo, AI-assisted, cross-model reviewed, not human peer review; council agreement is not peer review | Stress test gap #9 | Implemented (§15) |
| D14 | Add falsifiers **F-8** (crypto), **F-9** (non-apportionment), **F-10** (positive inconsistency); F-2/F-7 **discharged by exhibited paper models, remaining live against defects or stronger semantics** | Anthropic F-8; stress test F-8/F-10; final QA | Implemented (§16) |
| D15 | **State but do not execute** monograph consequences; sequence corpus ontology after publication | All seats; screenshot option 3 | Implemented (§14) |
| D16 | Label all proofs **finite model-theoretic paper proofs**; proof-assistant formalization is future work; no machine-checked claim | Stress test §1; task | Implemented (§5, §15, §17) |
| D-defect-1 | Fix **future date** → July 23, 2026 | All seats; screenshot option 1 | Implemented (front matter) |
| D-defect-2 | Fix **broken \(E^{*}\)** superscript in boxed axiom | Anthropic §10.2 | Implemented (§6.1) |
| D-defect-3 | Fix **stale section references** (draft §4.3/§4.5 → clause proofs); use numbered references | Anthropic; OpenAI; Google | Implemented (renumbered §9-§10) |
| D-defect-4 | Reconcile **positive/negative-result** terminology for F-1 without silently overwriting the note | Anthropic §10.4 | Implemented (§1, §16 F-1) |
| D-defect-5 | Fix **capitalization** (sentence-initial lowercase after bolded lead-ins) and **abstract overstatement** ("two clauses are theorems ... proved as such") | Anthropic §10.5; OpenAI defects 2-3 | Implemented (abstract, §9) |

---

## 6. Independent Stress Test (recorded separately, not a council vote)

The independent stress-test adjudication memo is treated as a **separate check**, not a fourth council seat. Its distinctive contributions, all incorporated:

- **SHIELD artifact absence is publication-blocking** (gap #2): the claim "SHIELD already contains the gate" is UNKNOWN and unverifiable from the materials; the paper must say it is *proposing* relocation. → D3.
- **Narrower joint-satisfiability burden** (§5): because only A5.1 is the axiom, the actual burden is A1-A4+A5.1, not the five-clause conjunction - "very plausibly satisfiable" is not "shown consistent." → D6, and the axiom-set/proposal-bundle distinction in §7.
- **Non-apportionment has zero derivation and zero test** (gap #5): must be flagged as an explicit undefended normative commitment with its own F-condition. → D8, F-9.
- **Positive-inconsistency gap** (gap #6): the falsification set omitted the case where A5.1 is *inconsistent* with A1-A4 under an exotic model, not merely underived. → F-10.
- **"Three independent arrivals" overstates independence** (gap #7): all three arise from one author's program - internal consistency, not external discovery. → D10.
- **SLH-DSA size/throughput cost undisclosed** (gap #8): the conservative-choice recommendation must not read as costless. → D11.
- **Provenance/peer-review status undisclosed in the paper itself** (gap #9). → D13.
- **Verified verbatim against the deposited canon** rather than the draft's paraphrase, and confirmed FIPS 204/205 dating against NIST primary sources.

The stress test's one point of greater severity than the draft's self-assessment - treating joint satisfiability as unsettled - is resolved by the exhibited construction in §7, which the stress test itself anticipated as "very plausibly satisfiable."

---

## 7. Residual UNKNOWNs (preserved, not resolved by fiat)

1. **SHIELD instantiation.** Whether a citable SHIELD artifact contains an equivalent pre-action gate is UNKNOWN; relocation is stated as proposed. (Reopen when SHIELD is deposited.)
2. **A5.3b bridging lemma.** Whether the evidence ledger is an A1-eligible surface is unproved; A5.3b remains an open operational requirement. (F-4 tests it.)
3. **Non-apportionment derivation.** Whether non-apportionment derives from A2 (operator's account as an A2-owed surface) is UNKNOWN; retained as an explicit deployment rule. (F-9 tests it.)
4. **Operator-external-by-construction witness.** Whether a witness can be verifiably outside operator authority by construction rather than declaration is UNKNOWN and welcomed. (F-6.)
5. **Practical determinacy of coverage.** Whether \(\mathrm{Cov}_{\text{out}}\) is more determinate than the existential in practice is UNKNOWN. (F-5.)
6. **Deployed achievability.** Whether evidence independence is achievable in any deployed system is UNKNOWN; the assurance ladder's top rung has no public instantiation.
7. **Diagnostic-vs-control governance.** The characterization is stated as an authorial architecture decision; a program lead may still elect a different posture. (F-3 contests it.)

---

## 8. Publication Gate Checklist

| Gate item | Required by | Status |
| --- | --- | --- |
| A5.1 stated alone as Axiom 5, with WithinAuth control predicate and declared boundary | D1, D2 | ✅ Pass (§6.1) |
| Independence defined by control predicate WithinAuth (not label mismatch); operator authority kept separate | D2 | ✅ Pass (§6.1, §11) |
| Finite countermodel, ≥2 coherent projections, verified clause-by-clause with WithinAuth (discharges F-2) | D5 | ✅ Pass (§6.2) |
| Finite joint-satisfiability model A1-A4+A5, verified clause-by-clause (discharges F-7); axiom-set vs bundle distinguished; B fixed ex ante; in-B missing-evidence carries axiom-level UNSATISFIED (nonconforming) and event-level UNKNOWN under Proposition 1, never post-hoc-excluded; M+ actual event is a successful external-witness occurrence | D6 | ✅ Pass (§7) |
| A5.2 as proposed SHIELD control principle; no "already contains" claim; explicit architecture decision | D3 | ✅ Pass (§8) |
| A5.3a proposition + proof; A5.3b preserved as open requirement | D7 | ✅ Pass (§9) |
| A5.4 measured deployment condition; \(\mathrm{Ev}(O,e,A)\); coverage fractions; non-apportionment rule + F-9; no architecture-guarantee claim | D8 | ✅ Pass (§11) |
| A5.5 proposition + proof + temporal boundary | D9 | ✅ Pass (§10) |
| Markedness discipline named as internal consistency | D10 | ✅ Pass (§12) |
| Self-attestation reframed (may be evidence, cannot discharge) | D4 | ✅ Pass (§11.1) |
| Cryptography narrowed; ML-DSA primary / SLH-DSA alternative; size/throughput; conditional forgery; authoritative citations | D11, D12 | ✅ Pass (§13) |
| External grounding: SP 800-53, ISO/IEC 17029, ISO conformity attestation | D12 | ✅ Pass (§8, §11) |
| Disclosure: Zenodo self-publication, AI-assisted, cross-model (not peer review) | D13 | ✅ Pass (§15) |
| Falsifiers F-1...F-10; F-2/F-7 discharged by exhibited paper models, live against defects or stronger semantics | D14 | ✅ Pass (§16) |
| Monograph consequences stated, not executed; ontology sequenced after | D15 | ✅ Pass (§14) |
| Proofs labeled finite paper proofs; no machine-checked claim | D16 | ✅ Pass (§5, §15, §17) |
| Date July 23, 2026; \(E^{*}\) fixed; sections renumbered; abstract not overstated; terminology reconciled; capitalization | D-defect-1...5 | ✅ Pass |
| Author preserved: Bilal Syed Arfeen | Task | ✅ Pass |

**Council verdict (pre-remediation):** the canonical artifact **passes the substantive publication gate** for deposit as a decomposition paper. F-2 and F-7 are **discharged by the exhibited paper models** of Sections 6.2 and 7 and **remain live against defects or stronger semantics** - any reader who finds a defect, or who adopts a stronger model-theoretic semantics under which the constructions fail, reopens them. This adjudication is a cross-model consistency record and is not a substitute for independent human peer review.

**Revised publication verdict (post-Fable-audit):** the substantive verdict stands, but deposit is gated on the edition-integrity remediation below. **The paper passes the publication gate only after the G9 concordance receipt succeeds** on the regenerated Markdown/PDF pair. That receipt now reports **BIDIRECTIONAL PARITY: PASS** (116/116 content blocks present in both members, token similarity 1.0000, 16/16 load-bearing riders present in both, 3/3 forbidden strings absent in both). With the receipt passing and F-EI-1 through F-EI-9 dispositioned below, the pair is cleared for deposit.

---

## 9. Remediation decision register (F-EI-1 through F-EI-9)

Triggered by the Claude Fable 5 HALT-AND-ESCALATE audit (`claude-fable-5-audit-2026-07-23.md`; 1 CRITICAL / 5 MEDIUM / 3 LOW). Each finding is mapped to its disposition and status. The single authoritative source is `axsh5_content.py`; both the `.pplx.md` and the `.pdf` are mechanically generated from it, so edition divergence cannot recur by construction.

| Finding | Severity | Disposition | Status |
| --- | --- | --- | --- |
| **F-EI-1** Edition divergence; adjudication attested wrong edition | CRITICAL | Built one authoritative source (`axsh5_content.py`); regenerated both members from it; added a G9-class bidirectional, wrap-immune, quote/dash-normalized, sentence/block-level concordance receipt. All load-bearing riders verified in both members. | **CLOSED - receipt PASS** |
| **F-EI-2** ETSI EN 319 102-1 misused for preservation | MEDIUM | Replaced with ETSI TS 119 511 V1.2.1 (2025-10) in text and sources (now source [14]); EN 319 102-1 removed (not used for AdES creation/validation). TS 119 512 not needed and not cited. Citations renumbered. | **CLOSED** |
| **F-EI-3** Proposal uncited; dangling companion pointer | MEDIUM | Proposal cited as source [16] "unpublished working proposal, July 2026, on file with the author." A faithful source artifact is included in the audit-trail packet, and the adjudication, council reviews, stress test, Fable audit, and remediation receipt are shipped in the same packet so the companion pointer resolves in-record. | **CLOSED** |
| **F-EI-4** PDF metadata attributed authorship to the tool | MEDIUM | Byline Bilal Syed Arfeen preserved visibly. Title, Subject, Creator, Keywords, CreationDate, ModDate populated. Per PDF-skill rule, `/Author` is retained as "Perplexity Computer"; `/Subject` and `/Creator` explicitly state "Authored by Bilal Syed Arfeen; prepared with Perplexity Computer as an analytical and drafting instrument." The `/Author`-field limitation is recorded transparently in the remediation receipt rather than claimed as full closure. | **CLOSED with recorded metadata-layer limitation** |
| **F-EI-5** WithinAuth "independently detectable" regress | MEDIUM | Added the required sentence in Section 6.1: WithinAuth is a primitive relation of the declared formal structure; operationalizing "independently detectable" in deployment inherits the authority regress acknowledged in the conclusion and is bounded in M+ only by the declared-external-authority device, not eliminated. | **CLOSED** |
| **F-EI-6** Ambiguous compound-label shorthand vs Proposition 1 | MEDIUM | Abstract and Section 7 now state two distinct levels explicitly: axiom-level A5 status is UNSATISFIED (nonconforming) for an in-B occurrence lacking timely independent evidence; the event-level adjudicative verdict remains UNKNOWN under Proposition 1. The ambiguous compound label is removed everywhere in the canonical pair and in this adjudication. | **CLOSED** |
| **F-EI-7** Source-layer dash violations (U+2014/U+2013) | LOW | Authoritative source authored dash-free; both generated members verified at zero U+2014 and zero U+2013; companion packet copies normalized. | **CLOSED - zero-count verified** |
| **F-EI-8** Duplicate SP 800-57; over-reliance on Wikipedia | LOW | Duplicate SP 800-57 entry removed (single entry, source [8]). Wikipedia LSP entry removed because Liskov-Wing 1994 is present (now source [4], with DOI). Wikipedia axiom-independence retained (no primary replacement available among verified sources; no URL invented). | **CLOSED** |
| **F-EI-9** Quantum "collision-level" imprecision | LOW | Section 13 now distinguishes preimage/second-preimage under Grover (about 2^128 for a 256-bit hash) from generic collision query complexity (about 2^85 under the Brassard-Hoyer-Tapp bound where it applies), explicitly declines to call 128-bit a single "collision-level" figure, and names the notion wherever a number is used. Narrowly sourced to NIST. | **CLOSED** |

### Fable seat status

Under the program's **same-vendor-counts-once** rule, the Claude Fable 5 audit is **advisory and non-carrying** for this artifact: a prior Claude instance is in the decomposition's lineage, Claude Opus 4.8 held a council seat, and Claude is named as the corpus drafting instrument. It is nonetheless preserved as an **independent adversarial audit record** in the packet, and its CRITICAL finding drove this remediation pass. The **carrying** re-attestation seats for the receipt-level delta are GPT-5.4 and Gemini 3.1 Pro.

---

## 10. Final delta re-attestation (carrying seats)

After the remediation pass, two cross-vendor seats independently re-attested the remediated release packet at the receipt level. Both reached PASS and both carry. Their reports are included in the packet as `council-review-openai-gpt-5.4-delta-reattestation.pplx.md` and `council-review-google-gemini-3.1-pro-delta-reattestation.pplx.md`.

| Seat | Vendor | Verdict | Carry status |
| --- | --- | --- | --- |
| GPT-5.4 delta re-attestation | OpenAI | **PASS** | **Carries** |
| Gemini 3.1 Pro delta re-attestation | Google | **PASS** | **Carries** |
| Claude Fable 5 audit | Anthropic | HALT-AND-ESCALATE (driver of remediation) | Advisory, non-carrying (same-vendor-counts-once) |

**GPT-5.4 (OpenAI), PASS, carries.** Independently re-ran integrity and PDF checks, extracted PDF text and metadata, enumerated PDF hyperlink annotations, compared against `SHA256SUMS`, and ran an independent block/token comparison against the authoritative block list. Found no remaining blocking defect; assessed F-EI-1 through F-EI-9 closed for deposit with the single disclosed metadata caveat on `/Author`. Verified the load-bearing riders (F-2/F-7 discharged-but-live, the no-reconstruction-from-subject-emitted-logs rule, the WithinAuth-primitive sentence, the axiom-level-UNSATISFIED versus event-level-UNKNOWN split, the proposal-on-file citation, and the narrowed post-quantum wording) present in both canonical members, and confirmed no mathematical-meaning regression. GPT-5.4 also noted, as a non-blocking packet observation, that this adjudication still carried the ambiguous compound-label shorthand in explanatory prose even though the canonical pair did not; **that observation is now resolved in this revision** (the shorthand is replaced by the explicit two-level distinction throughout this record).

**Gemini 3.1 Pro (Google), PASS, carries.** Executed `concordance_check.py` locally, confirming bidirectional block-level parity (116/116) and global token similarity 1.0000 with all 16 riders present in both editions. Confirmed the ETSI TS 119 511 swap (text and source 14), the proposal citation (source 16) with companion documents resolvable in-record, the WithinAuth primitive-relation clarification, the two-level distinction between axiom-level UNSATISFIED (nonconforming) and event-level UNKNOWN, the SP 800-57 dedup and Wikipedia-LSP removal, and the corrected preimage/collision quantum language. Found no residual mathematical regression; the single remaining UNKNOWN (deployed achievability at the top assurance rung) is documented in Section 17 of the paper.

**Revised final verdict: DEPOSIT-CLEARED.** With two carrying cross-vendor seats at PASS (GPT-5.4 and Gemini 3.1 Pro), the Fable audit's CRITICAL and all MEDIUM/LOW findings closed, the G9 concordance receipt at BIDIRECTIONAL PARITY: PASS, and the compound-label shorthand now removed from this adjudication as well as the canonical pair, the remediated release packet is **cleared for deposit**. This adjudication remains a cross-model consistency record and is not a substitute for independent human peer review.

---

## Sources

1. Bilal Syed Arfeen, *Structural Honesty: Axioms for Detecting Surface-Substrate Divergence in AI Systems* (flagship), Zenodo, 2026. https://doi.org/10.5281/zenodo.21500700
2. Bilal Syed Arfeen, *Consolidated Reference Canon* v1.4, Zenodo, 2026. https://doi.org/10.5281/zenodo.21501912
11. ISO/CASCO, Attestations of conformity. https://casco.iso.org/attestations-of-conformity.html
12. NIST FIPS 204 (ML-DSA), final, Aug 13, 2024. https://csrc.nist.gov/pubs/fips/204/final
13. NIST FIPS 205 (SLH-DSA), final, Aug 13, 2024. https://csrc.nist.gov/pubs/fips/205/final

---

# Bismillah ir-Rahman ir-Rahim
