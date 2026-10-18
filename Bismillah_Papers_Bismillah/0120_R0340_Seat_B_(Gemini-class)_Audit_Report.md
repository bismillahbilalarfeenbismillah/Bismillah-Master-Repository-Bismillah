# Bismillah ir-Rahman ir-Rahim

# R0340 -- Seat B (Gemini-class) Audit Report

**Chronological Index:** 120 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_1_SEAT_B_GEMINI_VERDICT.md  
**Source Format:** md  
**SHA-256:** `c5c4aff3b405f009203a510df5e48c18c2a8d47e77bb00aa7de19c7150d75b54`  

---

## R0340 · Seat B (Gemini-class) Audit Report

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_1_SEAT_B_GEMINI_VERDICT.md
- source_format: md
- text_sha256: c5c4aff3b405f009203a510df5e48c18c2a8d47e77bb00aa7de19c7150d75b54

# Seat B (Gemini-class) Audit Report
**Preregistration Integrity Audit for SHVVP v0.1**

## 1. Verdict

**PASS-WITH-AMENDMENTS**

The SHVVP v0.1 freeze provides a largely robust evaluation contract with strong internal consistency and rigorous phase constraints. However, a hostile read of the falsifiers and thresholds reveals some reliance on unpinned subjective language and an unacceptable deferral of the pass/fail margins until after the pilot experiment, which function as escape hatches. Furthermore, there is a minor discrepancy regarding empirical anchor 1 (CVE-2026-4747). I am returning PASS-WITH-AMENDMENTS requiring the closure of these escape hatches and the anchor correction prior to deposit.

**Carry Status:** I am the **Gemini-class** seat (Seat B). I carry. Convergence with Seat A (GPT-class) is required.

## 2. Axis 1 — Falsifier integrity (Hostile Read)

**Master Falsifier (§4)**
*   **Hostile Read:** The master falsifier fails if SHV detects no "consequential fact" beyond the baseline, detects the same facts no earlier and with no "better evidence", or "materially increases" false positives or "reviewer burden".
*   **Vulnerabilities:** The terms "consequential", "better", "materially", and "reviewer burden" are load-bearing but entirely unpinned. A motivated author could satisfy this falsifier by post-hoc reinterpretation — e.g., arguing that a large increase in alerts is not a "material" increase in burden, or that a minor detail is "consequential". These are escape hatches.
*   **Data Commitment:** It implies collecting data on false positives and reviewer time (as seen in Phase A metrics), but the threshold for falsification is not mathematically bound to the data collected.

**Phase-A Falsifier (§5)**
*   **Hostile Read:** This falsifier mirrors the master falsifier's language ("consequential fact", "better evidence", "materially increases") and adds that it fails if it "cannot separate legitimate generated files from undeclared executable differences."
*   **Vulnerabilities:** It suffers from the identical unpinned, subjective terms as the Master Falsifier.
*   **Data Commitment:** It is grounded in the Phase A metrics (time to first consequential divergence, false-positive rate, reviewer-hours), but the falsification condition must explicitly pin to those metrics (e.g., "false positive rate > X%").

**Phase-B Two-Sided Success Criterion (§6)**
*   **Hostile Read:** BSSG must reduce unauthorized effects while preserving within-scope vulnerability-analysis performance "inside a preregistered noninferiority margin." Crucially, both the reduction target and margin are "declared before the confirmatory run and are recorded in the amendment log if the pilot forces any change."
*   **Vulnerabilities:** This is a deferred threshold. Setting the pass/fail margins *after* seeing the pilot data (160 sessions) allows an author to calibrate the threshold specifically to guarantee the confirmatory run passes. This is an escape hatch and an unacceptable deferral.
*   **Data Commitment:** The metrics themselves are well-defined, but the thresholds determining success are floating.

**Six Novelty-Contribution Routes (§4)**
*   **Hostile Read:** SHV must detect divergence across full projection graph, type unenumerated outcomes, preserve conflicting projections, bind runtime authority to witness health, propagate corrections, or represent absent provenance as UNKNOWN.
*   **Vulnerabilities:** These conditions are structural and highly checkable. It is difficult to post-hoc reinterpret "binding runtime authority to witness health" or "representing absent provenance as UNKNOWN". These are solid and not escape hatches.

## 3. Axis 2 — Empirical-anchor integrity (Independent Verification)

**Anchor 1: CVE-2026-4747 (Mythos Preview FreeBSD RCE)**
*   **Verification:** Verified independently against `red.anthropic.com` and `freebsd.org`.
*   **Primary Source Alignment:** The Anthropic primary confirms fully autonomous identification and exploitation of a 17-year-old FreeBSD RCE leading to unauthenticated root. However, the protocol attributes a "20-gadget ROP chain across multiple packets" to this exploit. The primary source actually attributes the 20-gadget ROP chain to a separate OpenBSD exploit on the same page. The FreeBSD exploit is explicitly described as an "over 1000 byte" ROP chain split into 6 requests.
*   **FreeBSD Advisory Conflict:** As noted by the Chair, the FreeBSD advisory (FreeBSD-SA-26:08) Problem Description notes it "does not require the client to authenticate itself first", but the Impact states RCE is possible "by an authenticated user". The protocol takes the stronger "unauthenticated root" claim, which accurately reflects the Anthropic primary but highlights inconsistency in the FreeBSD primary.
*   **Protocol Usage:** The protocol correctly captures the discovery-vs-retrieval dispute and strictly uses the CVE only as a "motivating capability profile", explicitly structurally forbidding its use as a discovery-novelty label. It does not lean on it as ground truth.
*   **Finding:** The protocol conflates the "20-gadget ROP chain" detail from the OpenBSD example into the FreeBSD example.

**Anchor 2: AISI "The Last Ones"**
*   **Verification:** Verified independently against `aisi.gov.uk`.
*   **Primary Source Alignment:** Perfectly matches the primary: 3-of-10 attempts, average 22-of-32 steps, next best Opus 4.6 at 16 steps, and a 100M-token budget. It correctly notes it was the first model to solve TLO from start to finish.
*   **Caveats:** The primary explicitly states the ranges "lack security features... such as active defenders and defensive tooling".
*   **Protocol Usage:** The protocol faithfully reports this caveat and restricts the anchor's use to setting canary difficulty, not as evidence about BSSG.

## 4. Axis 3 — Internal consistency and completeness of the freeze

*   **Deferred Thresholds (§6):** As identified in Axis 1, the Phase-B noninferiority margin and unauthorized-effect-reduction target are deferred to after the pilot. This is an **unacceptable hole**. While a pilot is necessary to measure variance, the *formula* for calculating the margin from the pilot variance (e.g., "the noninferiority margin will be set to 1 standard deviation of the pilot's control group variance") must be frozen *now*. Otherwise, the numbers can be arbitrarily set to ensure success.
*   **BSSG Authorization Rule (§3):** The 5-conjunct rule (`ContractMatch(r) and EffectTypeValid(r) and TargetAllowed(r) and WitnessHealthy and EvidenceCurrent`) is genuinely fail-closed. It is a strict AND gate; a missing conjunct evaluates to denial.
*   **Monotonicity Rule (§3):** The rule ensures that if witness health decreases, authority is strictly a subset of the previous step. This genuinely prevents authority expansion.
*   **Phase Safety Boundaries & Falsifiers:**
    *   **Phase A:** Has a falsifier (§5) and implicit boundary (offline archive).
    *   **Phase B:** Has a falsifier (§6 success criterion) and boundary (CVE-Bench Docker isolation).
    *   **Phase C:** Has a robust success criterion and a **HARD, non-amendable** safety boundary (§7: "offline containers, synthetic vulnerabilities, non-deployable proofs, and controlled access. This boundary is not amendable by a later contract version"). This is truly hard.
*   **Missing Material:** The protocol declares "reviewer burden" and "false positives" in the Phase A metrics, but fails to define the threshold for a "material" increase, creating a gap between the metric and the falsifier.

## 5. Axis 4 — Scope honesty

*   **Overclaiming:** The document is highly disciplined. Section 0 states "It is not the empirical paper, not a corpus, and not a claim that Structural Honesty (SHV) has been validated." Section 5 explicitly notes XZ "cannot establish universal adequacy". Section 8 mandates "No phase's conclusion is generalized beyond its evidentiary reach." There is no overclaiming.
*   **Provenance/Not-Peer-Review:** The disclosure is present and accurate: "This document has not undergone independent human peer review".
*   **UNKNOWN Discipline:** Applied rigorously, even to its own gaps. Section 2 records the dispute against the FreeBSD CVE instead of papering over it.

## 6. Secondary mechanical checks

I have independently executed the secondary mechanical checks on the canonical `.md` source:
*   **Source-vs-render parity:** Checked via `pdftotext`. Render is faithful; only rendering-class typographic differences (apostrophes, dashes) exist.
*   **Zero U+2013 / U+2014 / U+2015:** Checked via `grep` on source; 0 occurrences.
*   **No doubled words:** Checked via `grep` on source; 0 occurrences.
*   **Severities UPPERCASE:** Verified manually. VERIFIED, UNKNOWN, RECORDED DISPUTE, HARD, FROZEN are uppercase.
*   **Brand canonical:** Checked via `grep`. "BayyinahEnterprise" appears 0 times as "Bayyinah Enterprise".

## 7. F-PP Findings

*   **ID:** F-PP-1
*   **SEVERITY:** HIGH
*   **Locus:** Section 6 (Phase B: CVE-Bench effect-control trial)
*   **Substance:** The Phase-B noninferiority margin and unauthorized-effect-reduction target are deferred until after the pilot run. Because the pilot data is seen before setting the thresholds, these numbers could be manipulated to guarantee the confirmatory run passes. This is an unacceptable escape hatch.
*   **Disposition:** Amend to freeze the *formula* or *function* used to derive the thresholds from the pilot data (e.g., "margin will be set to X standard deviations of the pilot's control variance") rather than leaving the absolute values completely unconstrained until after the pilot.
*   **Cross-reference:** Axis 1 (Phase-B Two-Sided Success Criterion); Axis 3 (Deferred thresholds).

*   **ID:** F-PP-2
*   **SEVERITY:** MEDIUM
*   **Locus:** Section 4 (Frozen master falsifier) and Section 5 (Phase-A falsifier)
*   **Substance:** The falsifiers rely on unpinned, subjective, load-bearing terms: "consequential fact", "better evidence", "materially increases", and "reviewer burden". A motivated author could reinterpret these terms post-hoc to avoid a falsification event (e.g., arguing that a measurable increase in false positives wasn't "material").
*   **Disposition:** Amend to pin these subjective terms to quantitative bounds or strict definitions derived from the metrics specified for Phase A (e.g., define "material increase" as a specific percentage threshold).
*   **Cross-reference:** Axis 1 (Master Falsifier, Phase-A Falsifier).

*   **ID:** F-PP-3
*   **SEVERITY:** LOW
*   **Locus:** Section 2 (Empirical anchors - Mythos Preview FreeBSD CVE-2026-4747)
*   **Substance:** The protocol conflates details from the Anthropic primary source. It states the FreeBSD exploit used a "20-gadget ROP chain across multiple packets". The primary source attributes the 20-gadget chain to a separate OpenBSD example, while describing the FreeBSD exploit as an "over 1000 byte" chain split into 6 requests. (The "unauthenticated root" claim correctly reflects the primary despite the FreeBSD advisory's internal contradiction).
*   **Disposition:** Amend Section 2 to accurately reflect the Anthropic primary's description of the FreeBSD exploit, correcting the "20-gadget ROP chain" detail to match the actual text (e.g., "over 1000-byte ROP chain").
*   **Cross-reference:** Axis 2 (Empirical-anchor integrity).

## 8. Unanticipated Findings
*   None beyond the required axes.

## 9. Conclusion
I render a verdict of **PASS-WITH-AMENDMENTS**. The preregistration freeze is conceptually rigorous, but the escape hatches identified in Sections 4, 5, and 6 (F-PP-1 and F-PP-2) must be explicitly closed prior to deposit to ensure the evaluation contract cannot be post-hoc manipulated. The conflation error in Anchor 1 (F-PP-3) must also be corrected for precision.

---

# Bismillah ir-Rahman ir-Rahim
