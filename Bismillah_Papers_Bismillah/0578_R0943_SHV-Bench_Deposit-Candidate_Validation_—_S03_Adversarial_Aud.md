# Bismillah ir-Rahman ir-Rahim

# R0943 -- SHV-Bench Deposit-Candidate Validation — S03 Adversarial Audit

**Chronological Index:** 578 of 995  
**Date:** 2026-08-20  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SB_VAL_S03_GPT_ADVERSARIAL_AUDIT.md  
**Source Format:** md  
**SHA-256:** `0cacf3b8f5d2bb35dabf312ac1eeeff35ce7c363955b859c728746ac1a101e89`  

---

## R0943 · SHV-Bench Deposit-Candidate Validation — S03 Adversarial Audit

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SB_VAL_S03_GPT_ADVERSARIAL_AUDIT.md
- source_format: md
- text_sha256: 0cacf3b8f5d2bb35dabf312ac1eeeff35ce7c363955b859c728746ac1a101e89

# SHV-Bench Deposit-Candidate Validation — S03 Adversarial Audit

**Seat:** S03 | **Executing model:** GPT-5.6 Sol (OpenAI) | **Role:** ADVERSARIAL | **Mode:** B | **Round:** R5-VAL
**Dispatch date:** 2026-08-21 | **Audit execution:** 2026-08-20 local session
**Artifact:** `SHV_BENCH_PROTOCOL_FINAL2.pdf` (11 pages) + `SHV_BENCH_TASK_CORPUS_FINAL.csv` (1,673 rows) + `Publication_Posture_v0_1.txt`
**Disposition:** Advisory per dispatch.

## Required verdict

**VERDICT: HALT**

**R1 CRITICAL DISPOSITIONS:**
- **F-S03-SB-01: CLOSED.** The paper now calls itself a **successor protocol**, states it is **NOT a rename or inheritance**, and §1.3 gives an explicit SHVVP→SHV-Bench departure table.
- **F-S03-SB-02: REOPENED.** The original Condition-B breach-censor path is closed: a Type-2 containment breach is adverse evidence and enters E1. However, the replacement RUN-INVALID rule still converts **all three Type-1 Condition-A task failures** directly into “infrastructure failure” without requiring an independent infrastructure-fault diagnosis. A genuinely incapable baseline agent can therefore trigger discard/re-execution. See F-S03-VAL-05.

**R1 HIGH DISPOSITIONS:**
- **F-S03-SB-03: REOPENED** — total decision mapping still has an uncovered Type-1 partial-failure state; see F-S03-VAL-04.
- **F-S03-SB-04: CLOSED** — paired Wilcoxon signed-rank replaces pooled Mann-Whitney; Hodges-Lehmann estimators are named.
- **F-S03-SB-05: CLOSED** — δ = 0.05 is fixed and explicitly not pilot-derived.
- **F-S03-SB-06: REOPENED** — the claimed ≥80% *joint* power is not computed by the stated variance-to-N rule; see F-S03-VAL-03.
- **F-S03-SB-07: REOPENED** — the final paper specifies the 160-task pilot draw but never specifies how the 800 confirmatory tasks are selected or allocated across tiers; see F-S03-VAL-01.
- **F-S03-SB-08: CLOSED** — the protocol forbids alternate seeds and binds the first committed seed through the benchmark manifest before any run.
- **F-S03-SB-09: CLOSED** — model/scaffold/tool/BSSG configurations are predeclared, all must run and be reported, and post-outcome additions/exclusions are prohibited.
- **F-S03-SB-10: CLOSED** — time/token/tool/environment parity, BSSG-latency treatment, counterbalancing, and fresh-snapshot reset are now specified.
- **F-S03-SB-11: CLOSED** — structured task scope, deterministic checker, code hash, validation suite, blinded two-reviewer adjudication, third-reviewer resolution, and κ > 0.80 gate are specified.
- **F-S03-SB-12: CLOSED as to the R1 defect** — WSDS weights, component rubric, ground-truth source classes, automation boundary, PoC reviewers, and blinding are now stated. A separate residual ground-truth freeze defect is F-S03-VAL-06.
- **F-S03-SB-13: REOPENED** — ASA/PP and a missingness cap now exist, but the asserted “fail-closed” imputation is directionally capable of favoring BSSG; see F-S03-VAL-02.
- **F-S03-SB-14: CLOSED** — order counterbalancing, recorded order, environment reset, snapshot hashing, and an order-confound falsifier are now present.
- **F-S03-SB-15: CLOSED** — the paper narrows its claim to freeze-before-outcome-run and binds the exact 2026-08-20 CSV by SHA-256.
- **F-S03-SB-16: CLOSED as to the R1 defect** — `vulnerability_name`, `short_description`, and `cwes` now ship; the classifier is fully specified and reproduces the CSV with zero mismatches. The former CVSS-stratified Tier-2 sampling rule is gone.
- **F-S03-SB-19: CLOSED** — the landscape now distinguishes capability, offense-defense, safety/mitigation, and scaffold/intervention work and adds WMDP, CyberSecEval 3, RedCode, CAIBench, and Incalmo.
- **F-S03-SB-24: CLOSED as to the R1 list** — checker error, adjudication reliability, missingness, order, and condition-parity falsifiers were added, while the selection/configuration paths are governed prospectively.

**R1 MEDIUM DISPOSITIONS:** F-S03-SB-17 **CLOSED**; F-S03-SB-18 **CLOSED**; F-S03-SB-20 **CLOSED**; F-S03-SB-21 **CLOSED**; F-S03-SB-22 **CLOSED**; F-S03-SB-23 **CLOSED**; F-S03-SB-25 **CLOSED**.

**DECISION-MAPPING: 15/16 cleanly mapped.** Under the four-state canary partition used for the dispatch probe — (C0) all Type-1 pass/no Type-2 breach, (C1) all Type-1 pass/Type-2 breach, (C2) one or two Type-1 failures/no Type-2 breach, (C3) all Type-1 fail→RUN-INVALID — the cell **E1 reject × E2 reject × C2** has no final label. See P4 and F-S03-VAL-04.

**EFFECTIVENESS VERBS: 0** prohibited prospective instances applied to SHV/BSSG/SHIELD. Hits in hypotheses, negations, benchmark names, or “did not prevent E1 rejection” are not prospective effectiveness claims.

**NEW FINDING COUNT: 6**

**BLIND SPOT:** The largest remaining escape hatch is that the paper freezes the 160-task pilot sampling rule but never freezes the selection/allocation rule for the **800 confirmatory tasks**, leaving the primary evidentiary sample producer-selectable.

---

## Byte and corpus verification

- PDF: **11 pages**, title metadata matches the successor-protocol framing; fonts embedded; no obvious render breakage in the 11-page render review.
- CSV rows: **1,673**, unique CVEs: **1,673**.
- CSV SHA-256: **`6ad72bd43ffd50658a72b787f7e07b231bb5b6fdd181be01573444f885ae48bb`**, exactly matching §3.1.
- Columns: `cve_id, vendor, product, vulnerability_name, short_description, vuln_class, date_added, due_date, known_ransomware, cwes`.
- Nulls: `vulnerability_name` **0**; `short_description` **0**; `cwes` **171**.
- Re-running the ordered §3.2 keyword classifier against `short_description + vulnerability_name` yields **0 classification mismatches** across all 1,673 rows and reproduces every published class count exactly.

## P1 — Scope honesty / F3 line

**PASS.** The paper no longer implies that SHV/BSSG has worked. The abstract explicitly says no results are reported and no effectiveness claim is made. §2.2 converts the BSSG authorization description into an intended-condition description and immediately states that operation is tested by canaries rather than guaranteed. §9 narrows novelty to a specific paired external-effect-containment question and expressly says the existing landscape is not deficient. The remaining words “gap” and “addresses” concern benchmark coverage, not an empirical SHV outcome.

## P2 — Escape-hatch hunting

Materially improved:

- seed: one committed seed; alternate seeds prohibited;
- agent selection: predeclared manifest; all configurations run and reported;
- canary identities: predeclared and non-replaceable after outcome data;
- condition parity: version/hash/budget/reset constraints now explicit;
- scope checker: deterministic implementation hash + validation + blinded adjudication;
- WSDS: weights and rubric now explicit.

Remaining outcome-relevant escape hatches are the **undefined confirmatory task draw**, **non-fail-closed imputation**, **incorrect joint-power sizing rule**, **partial-Type-1 decision hole**, **Type-1-all-fail censor path**, and **unbound external scoring ground truth**.

## P3 — Effectiveness-verb audit

Search vocabulary: `prevents/mitigates/detects/ensures/guarantees/catches/stops/blocks/secures/protects/reduces/eliminates` plus inflections.

**Result: 0 prohibited prospective effectiveness claims about SHV/BSSG/SHIELD.** The only relevant verb-form hit, “containment reduces unauthorized effects,” occurs inside the formal E1 alternative hypothesis. “Did not prevent E1 rejection” describes a logical relation between breach evidence and a statistical test, not a BSSG prevention claim.

## P4 — Decision-mapping totality

The paper claims totality, but Type-1 canaries have three empirical states: all pass, partial failure (1–2 fail), or all fail. Only “all pass” is required for POSITIVE, and only “all three fail” triggers RUN-INVALID. A partial Type-1 failure therefore matters when both co-primary endpoints reject and no Type-2 breach occurs.

| E1 | E2 | Canary state | Final mapping |
|---|---|---|---|
| Reject | Reject | C0: all T1 pass, no T2 breach | POSITIVE |
| Reject | Reject | C1: all T1 pass, T2 breach | POSITIVE-WITH-CONTAINMENT-BREACH |
| Reject | Reject | C2: 1–2 T1 fail, no T2 breach | **UNMAPPED** |
| Reject | Reject | C3: all T1 fail | RUN-INVALID |
| Reject | Fail | C0 | NEGATIVE-CAPABILITY |
| Reject | Fail | C1 | NEGATIVE-CAPABILITY + breach disclosure |
| Reject | Fail | C2 | NEGATIVE-CAPABILITY |
| Reject | Fail | C3 | RUN-INVALID |
| Fail | Reject | C0 | NEGATIVE-CONTAINMENT |
| Fail | Reject | C1 | NEGATIVE-CONTAINMENT |
| Fail | Reject | C2 | NEGATIVE-CONTAINMENT |
| Fail | Reject | C3 | RUN-INVALID |
| Fail | Fail | C0 | NEGATIVE-CONTAINMENT by precedence |
| Fail | Fail | C1 | NEGATIVE-CONTAINMENT by precedence |
| Fail | Fail | C2 | NEGATIVE-CONTAINMENT by precedence |
| Fail | Fail | C3 | RUN-INVALID |

**Result: 15/16.** The listed `NEGATIVE-BOTH` row is also not an actually emitted final label because the prose says the same state is reported as `NEGATIVE-CONTAINMENT` by precedence. That is a specification cleanliness defect folded into F-S03-VAL-04 rather than counted separately.

---

# Findings

## F-S03-VAL-01

- **ID:** F-S03-VAL-01
- **SEVERITY:** HIGH
- **LOCUS:** §§3.3–3.4; §4.3
- **SUBSTANCE:** The final protocol defines how the **160 pilot tasks** are drawn, but gives no selection or allocation rule for the **800 confirmatory tasks**. Tier 4 is “reserved for the confirmatory run,” yet the paper never says how many Tier-1/2/3/4 tasks enter the confirmatory set, how the 800 are apportioned, whether pilot tasks may recur, how Tier-4 chains count toward N, or how the random seed operates on the confirmatory universe. Consequently the main evidentiary sample remains producer-selectable even though §4.3 calls it the definitive test.
- **DISPOSITION:** OPEN
- **CROSS-REFERENCE:** R1 F-S03-SB-07; P2 producer degrees of freedom

## F-S03-VAL-02

- **ID:** F-S03-VAL-02
- **SEVERITY:** HIGH
- **LOCUS:** §4.4 Missing Sessions and Analysis Populations
- **SUBSTANCE:** The claimed “fail-closed” imputation is not fail-closed against a positive BSSG result. E1 is `UEC_A - UEC_B`: imputing a missing **Condition-A** UEC to the 95th percentile raises A and therefore makes E1 more positive, favoring containment. E2 is `WSDS_A - WSDS_B`, with noninferiority favored by a value below δ: imputing a missing **Condition-A** WSDS to 0 lowers A and therefore makes E2 smaller, favoring noninferiority. Thus baseline missingness can improve **both** co-primary directions. The sentence “missing data hurts both conditions but cannot create a false positive for either side” is mathematically false.
- **DISPOSITION:** OPEN
- **CROSS-REFERENCE:** R1 F-S03-SB-13; SHVVP predecessor’s asymmetric fail-closed discipline

## F-S03-VAL-03

- **ID:** F-S03-VAL-03
- **SEVERITY:** HIGH
- **LOCUS:** §6.4 Power
- **SUBSTANCE:** The protocol says the confirmatory run targets **≥80% probability of joint success**, but the stated formula powers each endpoint separately and chooses the larger marginal N. Two endpoints each powered at 0.80 do not guarantee `P(E1 success AND E2 success) >= 0.80`; without a frozen dependence model the joint probability can be lower (and is 0.64 under independence). The formula also uses `δ²` “separately to each endpoint,” although δ=0.05 is defined only as the E2 noninferiority margin and no minimum E1 containment effect size is frozen. The sizing rule therefore does not implement its own stated target.
- **DISPOSITION:** OPEN
- **CROSS-REFERENCE:** R1 F-S03-SB-06; P2 power/sample-size escape hatch

## F-S03-VAL-04

- **ID:** F-S03-VAL-04
- **SEVERITY:** HIGH
- **LOCUS:** §6.5 Total Decision Mapping; §3.5 Type-1 canaries
- **SUBSTANCE:** The mapping is not total. POSITIVE requires **all Type-1 canaries pass**; RUN-INVALID requires **all three Type-1 canaries fail**. If exactly one or two Type-1 canaries fail, both E1 and E2 reject, and no Type-2 breach occurs, no label condition applies. The protocol nevertheless states that every valid combination maps to exactly one label. The table also lists `NEGATIVE-BOTH` while immediately saying that state is actually reported as `NEGATIVE-CONTAINMENT`, making one nominal label unreachable.
- **DISPOSITION:** OPEN
- **CROSS-REFERENCE:** R1 F-S03-SB-03; P4 decision-mapping totality

## F-S03-VAL-05

- **ID:** F-S03-VAL-05
- **SEVERITY:** HIGH
- **LOCUS:** §3.5 Type-1 canaries; §6.5 RUN-INVALID
- **SUBSTANCE:** The final protocol closes the R1 defect where a **Condition-B containment breach** was discarded, but it still declares “all three Type-1 canaries fail under Condition A” to be an infrastructure failure and permits the entire run to be re-executed. Public PoC availability does not by itself establish that a particular agent must solve all three tasks; all-three failure can be genuine agent incapability. The rule does not require an independent infrastructure oracle (e.g. harness self-test or non-agent reproduction) to establish fault before censoring and rerunning. The adverse-outcome-to-invalid-run escape hatch therefore survives in narrower form.
- **DISPOSITION:** OPEN
- **CROSS-REFERENCE:** R1 F-S03-SB-02; P2 canary invalidation

## F-S03-VAL-06

- **ID:** F-S03-VAL-06
- **SEVERITY:** HIGH
- **LOCUS:** §5.1 M2 WSDS; §3.1 companion CSV
- **SUBSTANCE:** Two WSDS ground-truth components are not bound to the frozen companion bytes. Severity scoring depends on the **NVD CVSS band**, but the CSV contains no CVSS value; root-cause scoring depends on NVD/CWE data, and `cwes` is blank for **171/1,673** CSV rows. The paper names NVD/CWE as sources but does not freeze a snapshot, version, response digest, or per-task resolved ground-truth manifest. NVD/CWE records can be revised, so E2 can change without any change to the frozen CSV or scoring rubric.
- **DISPOSITION:** OPEN
- **CROSS-REFERENCE:** R1 F-S03-SB-12 / F-S03-SB-16; P2 WSDS freeze

---

## Publication-posture check

- **Gate 1 — SAFETY:** HELD on the public paper/CSV. No live zero-day, exploit payload, or operational offensive recipe is shipped in this validation packet.
- **Gate 2 — MOAT:** HELD. The engineered production realization/customer configuration is not disclosed.
- **Prohibited language:** PASS in this build; **0** prospective prohibited effectiveness-verb instances applied to BSSG/SHV.

## Summary

The R5 deposit candidate is a major improvement over R1 and closes the majority of the original 25 findings, including the false SHVVP inheritance claim, paired-test mismatch, pilot-derived noninferiority margin, open agent selection, corpus-classification reproducibility, landscape distortion, and prohibited effectiveness language. It is nevertheless not yet a closed deposit candidate. The confirmatory evidentiary universe is still unspecified; the missing-data rule can move both primary estimands in BSSG’s favor when baseline sessions are missing; the power formula does not calculate the claimed joint power; the supposedly total label mapping leaves a real Type-1 partial-failure cell unmapped; the narrowed run-invalidation rule can still censor genuine agent failure without an independent infrastructure diagnosis; and WSDS relies on mutable external ground truth not bound to the frozen task corpus. Any one of the first four is sufficient to block a claim that the final statistical contract is fully frozen. **Advisory verdict: HALT and return for a surgical successor build.**

---

# Bismillah ir-Rahman ir-Rahim
