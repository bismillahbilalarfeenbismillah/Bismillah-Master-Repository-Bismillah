# Bismillah ir-Rahman ir-Rahim

# R0465 -- Synthesized Round-1 Model Council Audit — "Procurement Concentration and Recoverable Competitive Savings in New York City Contracting" (v0.3)

**Chronological Index:** 769 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-PC-R1_synthesis.md  
**Source Format:** md  
**SHA-256:** `ecc1ed448df7c3018b534cb785d19950726a86efec83aa19c9804409d692c243`  

---

## R0465 · Synthesized Round-1 Model Council Audit — "Procurement Concentration and Recoverable Competitive Savings in New York City Contracting" (v0.3)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-PC-R1_synthesis.md
- source_format: md
- text_sha256: ecc1ed448df7c3018b534cb785d19950726a86efec83aa19c9804409d692c243

# Synthesized Round-1 Model Council Audit — "Procurement Concentration and Recoverable Competitive Savings in New York City Contracting" (v0.3)

**Namespace:** F-PC-R1  |  **Round:** 1  |  **Framework:** Audit Framework v3.0, Standing Rule 7
**Synthesizer:** Perplexity Computer (orchestrator), operating over four independently dispatched, memoryless council members.
**Packet used:** the attached `NYC_Procurement_ReproPackage.zip`, the paper v0.3, and the Round-1 brief — only. No chat history, memory, or prior-round carryover was made available to members; each received one isolated extracted copy of the package in its own workspace.

---

## (a) Per-member identity, lineage, execution status, verdict, and attestation

| Member (friendly) | Lineage | Qualifying? | Execution (Steps 1–5) | No-history/no-memory attestation | Verdict | CRIT/HIGH |
|---|---|---|---|---|---|---|
| GPT 5.5 | OpenAI | **Yes** | Executed; real outputs pasted; exit 0 throughout | Attested verbatim | PASS | 0 / 0 |
| GPT 5.4 | OpenAI | **Yes** | Executed; real outputs pasted; exit 0 throughout | Attested verbatim | NON-PASS | 0 / **1** |
| Gemini 3.1 Pro | Google | **Yes** | Executed; real outputs pasted; exit 0 throughout | Attested verbatim | PASS | 0 / 0 |
| Claude Opus 4.8 | Anthropic (Claude) | **No — producer lineage, ADVISORY-ONLY** | Executed; real outputs pasted; exit 0 throughout; additionally retrieved Appendix 1 and reconciled it | Attested verbatim | PASS (advisory; not convergence-bearing) | 0 / 0 |

**No-history/no-memory attestation (council-wide):** Each member was convened as a brand-new, memoryless instance in a clean session with no stored memory, no personalization, no saved skills, no prior-conversation context, and no access to any other member's work until this synthesis. Each attested to this verbatim in its own report. Memory/history was not disabled at the interface level (no such toggle exists for subagent instances); instead, isolation was enforced structurally — each member received a private workspace with its own extracted copy of the package and an objective forbidding use of any outside context. If a strict "memory disabled at the platform layer" reading is required, that condition should be treated as INCOMPLETE; under the structural-isolation reading actually implemented, the attestations hold.

**Reproduction verification (synthesizer):** All four members pasted real, mutually-identical, unedited outputs for the three script invocations and the independent recompute/trap check. I independently re-ran all five protocol steps in my own environment before dispatch and again during synthesis; every Tier-1 figure reproduces byte-deterministically. No member scored PASS on the basis of comparing stated numbers — all four executed.

## (b) Qualifying members

Qualifying (non-Claude, non-producer lineage): **GPT 5.5, GPT 5.4, Gemini 3.1 Pro** (three members, two provider families — OpenAI and Google — satisfying the rotated-membership requirement). Claude Opus 4.8 is quarantined as producer lineage and is **advisory-only**; its findings and verdict are recorded for reference and do not count toward convergence.

---

## Tier-1 reproduction: unanimous and clean

Every byte-deterministic check reproduced exactly across all four members, offline and live:

- **Hashes:** `sole_source_vendors_fy25.csv` = `990993de…f4306f5`; `negotiated_acquisition_vendors_fy25.csv` = `5d0d640d…bba2ce4`. Both OK on independent SHA-256.
- **Sole Source (clean rows):** 106 vendors, $1,597,506,644.98, top-1 82.5004%, top-5 90.5858%, top-10 94.0642%, top-20 97.2606%, Gini 0.95557; top vendor NYCEDC $1,317,949,728.
- **Negotiated (clean rows):** 462 vendors, $3,865,895,209.67, top-1 24.0334%, top-5 36.9178%, top-10 46.2163%, top-20 55.3833%, Gini 0.81855; top vendor HANYC $929,104,960.
- **Savings bases (official Table 7):** Core $5,658,002,459; Wide $6,984,040,398; NYCEDC-adjusted $4,340,052,731; all 10%/20% products correct.
- **Selftest:** 14 perturbations, 0 missed.
- **Live MTA FY2024:** 13,718 records / 2,656 vendors / $65,189,755,228.64 face / top-10 30.4151% / Gini 0.93117 — **no drift**; FY2024 (13,718) correctly used, not the 37,988 three-year snapshot.
- **Adversarial trap:** including the `TOTAL` + footnote rows doubles the totals and drives top-1 to exactly 50.0000% (the TOTAL row equals the vendor sum); the paper's clean-row basis correctly excludes them. Confirmed by all four members and by the synthesizer.

**Tier-1 verdict: zero discrepancies.** The empirical spine of the paper reproduces exactly.

---

## The decisive divergence: one verified savings-disclosure finding

The only point on which qualifying members disagree at the severity level is the paper's Section 5.0 basis-mixing note. The paper states:

> "The NYCEDC-adjusted row subtracts NYCEDC's $1,317,949,728 (a real, identically-valued contract in both bases) from the official Core, so it mixes the two bases by about $2M -- immaterial to the result but noted for completeness."

**Synthesizer-independent recompute (corroborates GPT 5.4):**

- Published NYCEDC-adjusted row = official Core ($5,658,002,459) − NYCEDC ($1,317,949,728) = **$4,340,052,731**.
- A fully positive-basis adjusted row = positive Core ($5,463,401,854.65) − NYCEDC = **$4,145,452,126.65**.
- **Actual basis discrepancy of the adjusted row = $194,600,604.35, not ~$2M.** The paper's "$2M" is the Sole Source gap alone ($1,644,123); it omits the $192,956,481 Negotiated gap the adjusted row still carries (because the adjusted row is built on the full official Core, which includes the entire official Negotiated total).
- Savings impact: the published 10%/20% floor ($434,005,273 / $868,010,546) sits **$19.46M / $38.92M above** a pure-positive-basis floor ($414,545,213 / $829,090,425).

**How each qualifying member handled this exact point:**

- **GPT 5.4** flagged it as **F-PC-R1-001, HIGH**, with the correct $194.6M recompute. Its arithmetic is verified-correct.
- **GPT 5.5** did not address the "$2M" claim at all; its MEDIUM concerns the general overreach of applying deltas to the full base, not this disclosure.
- **Gemini 3.1 Pro** examined the same row but wrote *"As noted by the paper, this is an immaterial ~$2M error"* — i.e., it accepted the paper's false figure at face value and did not independently recompute the $194.6M.

So the two qualifying PASS verdicts did not independently rebut the HIGH: one missed the point, the other adopted the paper's incorrect characterization. (Advisory Claude flagged the broader delta-on-full-base issue as LOW but did not adjudicate the "$2M" claim either.)

**Adjudication.** The paper makes a specific, false quantitative assurance ("about $2M — immaterial") about the basis exposure of the NYCEDC-adjusted row, which the conclusion emphasizes as "a plausible floor near $434 million." The immediately preceding sentence does disclose the combined-bases difference as "~$195M," which is why this is not CRITICAL and the underlying savings arithmetic is itself correct — but that adjacent disclosure does not neutralize the false sentence, because the very next sentence tells the reader the adjusted row's own basis exposure is only ~$2M. The two statements are internally conflicting, and the false one concerns the savings floor. Gemini's repetition of the paper's "~$2M" premise is not an independent rebuttal; it is evidence that the wording can mislead even an auditor. Under the brief's directive to be logical rather than deferential, a verified, unrebutted HIGH cannot be overridden by two PASS verdicts that did not examine the point.

---

## (c) Synthesized findings (F-PC-R1), over qualifying members (advisory origin noted)

Six-element format: identifier | severity | locus | substance (surface vs substrate) | disposition | cross-reference.

| ID | Severity | Locus | Substance (surface vs substrate) | Disposition | Cross-ref |
|---|---|---|---|---|---|
| F-PC-R1-001 | **HIGH** | §5.0 basis note; Table 3 adjusted row | **Surface:** "the NYCEDC-adjusted row… mixes the two bases by about $2M — immaterial." **Substrate:** the adjusted row's actual cross-basis delta is $194,600,604.35 (official-adjusted $4,340,052,731 vs positive-adjusted $4,145,452,126.65); the published 10%/20% floor is $19.46M/$38.92M above a consistent-basis floor. The "$2M" is the Sole Source gap alone and omits the $192.96M Negotiated gap the row still carries. Verified by synthesizer recompute and GPT 5.4; not rebutted by the two PASS members. | Revise §5.0: delete the "~$2M — immaterial" sentence, or state the adjusted row is $194.6M above a fully positive-basis adjusted row, and/or add the positive-basis adjusted row ($4,145,452,126.65; 10%=$414,545,213; 20%=$829,090,425). | §5.0; Table 3; §9 |
| F-PC-R1-002 | MEDIUM | §4.4; §3.1; README "Known open item" | **Surface:** the $192.96M Negotiated gap's likely mechanism is "positive-value contracts unattributable to a distinct vendor name," and Appendix 1 is "access-gated (HTTP 403)." **Substrate:** three members (GPT 5.5, GPT 5.4, advisory Claude) retrieved Appendix 1 (HTTP 200) and reconciled it — 935 FY25 Negotiated rows, 100% positive, 100% vendor-named (0 blank/NULL), 0 null/zero/neg; nothing was dropped for missing names. The gap is 27 contracts absent from Appendix 1 entirely (Table 7 count 962 vs file 935) — a Table-7-vs-Appendix-1 coverage difference, not intra-file attribution loss. The 403 claim is not reproducible. Gemini could not fetch (server error) and accepted the paper's mechanism. The 95.25% coverage disclosure is adequate and stands. | Correct the stated mechanism to a coverage/scope difference; drop or qualify the 403 claim; perform and publish the line-item reconciliation (it is achievable). | §4.4; §3.1; §5.0 basis note; README |
| F-PC-R1-003 | MEDIUM | §5; Table 3; §4.5; §8 | **Surface:** a single-bid-elimination price delta (Czech ~10%, Slovak ~19pp) is applied to the entire official Core/Wide base. **Substrate:** that delta is estimated on single→multi-bidder transitions; the base is dominated by designated single-vehicle intermediaries (NYCEDC 82.5% of Sole Source, HANYC 24.0% of Negotiated) for which the delta is, by the paper's own §4.5, largely inapplicable. Disclosed and partly mitigated (NYCEDC-adjusted row, pilot gate, Limitations 5–6), but HANYC-type Negotiated spend is not haircut and the paper concedes the figure is "likely still an overestimate." | Bound the addressable share (apply an intermediary screen to Negotiated as done for Sole Source) before any headline; keep the pilot gate. | §5; Table 3; §4.5; §8 |
| F-PC-R1-004 | MEDIUM *(advisory origin)* | Abstract (line 14) vs §5.0 (line 146) and §9 (line 204) | **Surface:** abstract headline range "$434 million to $1.40 billion." **Substrate:** the body's own headline is "$500 million to $1.4 billion," with $434M explicitly labeled a sensitivity floor "not a revised headline." The abstract folds the sensitivity floor into the headline, contradicting the body's framing. (Flagged by advisory Claude only; not separately flagged by qualifying members.) | Reconcile to one headline range; present $434M uniformly as a sensitivity floor. | Abstract; §5; §9 |
| F-PC-R1-005 | LOW | Title (line 1); Table 3 title | **Surface:** "Recoverable Competitive Savings" / "Estimated Recoverable Savings" unqualified. **Substrate:** the body's binding rule is that no figure should be called recoverable before the pilot; the unqualified title label sits in tension with that discipline. Not an in-prose assertion of verified recovery. | Bound the label (e.g., "Conditional / Potentially Recoverable"). | Title; Table 3; §5.0 |
| F-PC-R1-006 | INFO | House style / internal consistency | All conformance checks pass: 0 em/en-dashes (ASCII `--` used); "BayyinahEnterprise" present and correct; MTA reproduction described as nine rounds; version uniformly v0.3; concentration and base figures consistent across abstract, Table 2, body, conclusion. | No action. | General |
| F-PC-R1-007 | INFO | Negotiated CSV `TOTAL` cell | Stored `TOTAL` reads `3865895209.68`; summed clean vendor rows = `3865895209.67` (1-cent rounding artifact in the stored total). Not carried into any reported figure; excluded by the clean-row filter. Corroborates the Appendix 1 microdata sum ($3,865,895,209.68 across 935 rows). | No action; noted for completeness. | Step 5 / Appendix 1 reconciliation |
| F-PC-R1-008 | INFO | Lines 8, 22 vs 132 | "at-Ta'līm" (macron) vs "at-Ta'lim" (plain) transliteration inconsistency. (Advisory origin.) | Normalize spelling. | — |

**Tier-3 (refusal) boundary:** no violation. Every accusation-adjacent term appears in an exculpatory/negating construction ("Group 2 is not inherently improper"; "non-culpable structural explanation rather than evidence of misconduct"; "not recoverable waste"). No sentence accuses any award or vendor of impropriety or asserts recoverability as fact. The savings number stays inside its conditional, pilot-gated frame in all prose; the only framing leakage is the unqualified "Recoverable" in the title/Table-3 label (F-PC-R1-005, LOW) and the abstract headline-range inconsistency (F-PC-R1-004).

---

## Synthesized verdict over qualifying members

**NON-PASS.**

- Tier-1 reproduction is **unanimously clean** across all four members — a genuine strength of the package.
- However, Round 1 does **not** produce a qualifying PASS. One qualifying member (GPT 5.4) identified a **verified HIGH** savings-basis disclosure error (F-PC-R1-001): the paper's claim that the NYCEDC-adjusted row "mixes the two bases by about $2M — immaterial" is false — the actual basis discrepancy is $194.6M, shifting the savings floor by $19.46M–$38.92M. The synthesizer's independent recompute confirms GPT 5.4's arithmetic.
- The other two qualifying PASS verdicts did not independently rebut this error: GPT 5.5 did not adjudicate the "$2M" claim; Gemini examined the row but accepted the paper's false "~$2M" characterization at face value. A PASS built on a miss and a face-value acceptance is not sound where a verified defect exists, and the brief directs logical adjudication over deference to a majority.
- Per the pass criterion, any CRITICAL or HIGH from the qualifying-member synthesis leaves the count at ZERO. The count cannot advance on a synthesis carrying an unrebutted HIGH.

**Consecutive qualifying-PASS count outcome: remains ZERO (0 → 0).**

This round can at most have moved the count from ZERO to ONE; it does not. Convergence still requires two consecutive qualifying passes (zero CRITICAL / zero HIGH) by independent, non-producer-lineage members who execute the reproduction. Round 2 should be re-dispatched after the producer revises v0.3 → v0.4 to resolve F-PC-R1-001 (and ideally F-PC-R1-002/003/004), at which point a fresh, memoryless council can attempt the first qualifying pass.

---

## Recommended v0.4 fix targets (for the producer)

1. **F-PC-R1-001 (blocking):** In §5.0, delete or correct the "about $2M — immaterial" sentence. Either state plainly that the published NYCEDC-adjusted official-basis row is $194.6M above a fully positive-basis adjusted row, or add the positive-basis adjusted row: $4,145,452,126.65 (10% = $414,545,213; 20% = $829,090,425). A single-basis pass for all of Table 3 remains the cleanest fix.
2. **F-PC-R1-002:** Correct the Negotiated-gap mechanism to a Table-7-vs-Appendix-1 coverage difference (not intra-file name-attribution loss); drop/qualify the HTTP-403 claim (the file is reachable); publish the line-item reconciliation.
3. **F-PC-R1-003:** Apply an intermediary screen to Negotiated (HANYC-type) spend as was done for Sole Source/NYCEDC, or move full-base arithmetic to a secondary sensitivity.
4. **F-PC-R1-004/005:** Reconcile the abstract headline range with the body's "$500M–$1.4B" framing; bound the "Recoverable" label in the title and Table 3.

---

# Bismillah ir-Rahman ir-Rahim
