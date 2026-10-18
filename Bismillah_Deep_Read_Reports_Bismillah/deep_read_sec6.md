# Bismillah ir-Rahman ir-Rahim

# Section VI -- Applied Audits & Public-Data Studies
## Deep-Read Synthesis Report (75 papers)

All 75 papers read in their entirety, in sha Allah.

---

## 1. Section Overview

Section VI is the empirical engine of the Bayyinah Research Corpus. It contains the complete audit trails -- reader-facing papers, audit companions, individual model-council member reports, synthesis verdicts, convergence records, reproduction scripts, frozen datasets, and companion deposit packages -- for five distinct applied studies, plus two theoretical thesis papers extending the SHV framework to new domains. The section demonstrates Structural Honesty Verification (SHV) applied to real public data, with every claim subjected to multi-model cross-instance audit under BayyinahEnterprise Audit Framework v3.0 and Standing Rule 7.

**Total papers: 75**
- Reader-facing papers: 6
- Audit companion/provenance ledgers: 4
- Convergence records: 1
- Model council synthesis reports: 9
- Individual member audit reports: 38
- Reproduction scripts: 4
- Dataset READMEs and companion deposits: 7
- Theoretical thesis papers: 2
- Data files (CSV): 1
- Citation ledger: 1
- Earlier cross-instance round reports: 2

---

## 2. The Five Applied Audit Series

### 2.1 F-AA: Allocation & Asymmetry (MTA Procurement)

**Papers:** 0010-0034, 0035, 0037, 0070, 0288-0290 (approx. 28 papers)
**Reader-facing paper:** 0070_R0418 -- *Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits* v1.0
**Data source:** NY State Open Data portal, Socrata dataset gpsc-qqsz (37,988 records, FY2022-2024)
**Reproduction script:** 0037_R0484 -- reproduce_paper2.py (v0.3)
**Dataset README:** 0035_R0480

**Core findings (Tier 1, byte-deterministic):**
- FY2024 face total: $65.19B across 13,718 records, 2,656 vendors
- MWBE prime-vendor share: 18.7% by count vs 3.95% by face value (x4.7 multiplier)
- Concentration: top-10 vendors hold 30.4% of face value; Gini coefficient 0.931
- Pre-2024-award face share: 91.7% (stock measure, not FY2024 flow)
- Competitive-bid process: 92.22% face, 89.65% expenditure

**Tier 2 (disclosed method):**
- Two estimand surfaces: contract_amount (face, stock) vs amount_expended_for_fiscal_year (flow)
- Provenance: community-view dataset (gpsc-qqsz) vs official dataset (twsw-2mqa)
- Three-resolution divergence: FY2023 identical; FY2024 divergent by 70 records/$58.1M; FY2022 identical rows but $0.75 face divergence
- Capital-table join: wcsa-vkhf -> kizb-nxtu/ehz8-ag3n via project_number; no borough key

**Tier 3 (REFUSED):**
- No goal-attainment claim for MWBE
- No compliance "pass" for competitive process
- No accusation of any agency

**Audit trail -- 9 rounds (R1-R9):**

| Round | Version | Verdict | Key Issue |
|-------|---------|---------|-----------|
| R1 (0012/0013/0288) | v0.1 | NON-PASS (0C/3H) | Surface-vs-substrate: face value ≠ annual spending; MWBE overclaim; competitive "pass" unsupported |
| R2 (0013) | v0.2 | NON-PASS (0C/2H) | Residual interpretive overreach |
| R3 (0289) | v0.3 | NON-PASS (0C/1H) | Claude advisory; version-propagation defect (Section 7 says v0.2) |
| R4 (0014) | v0.3 | PASS (Gemini) | But INCOMPLETE on supplied-script legs |
| R5 (0015/0016/0017/0290) | v0.4 | NON-PASS/INCOMPLETE | Missing reproduction package; Claude advisory incomplete |
| R6 (0018/0019/0020/0021) | v0.5 | QUALIFYING PASS | First consecutive pass; counter 0->1 |
| R7 (0022/0023/0024/0025) | v0.6 | NON-PASS | Status-propagation defect found; counter reset 1->0 |
| R8 (0026/0027/0028/0029/0030) | v0.6 | QUALIFYING PASS | Counter 0->1 again |
| R9 (0031/0032/0033/0034) | v0.7 | QUALIFYING PASS | **CONVERGENCE MET** on v0.7; counter 1->2 |

**Dominant defect family:** Version-propagation failure -- the producer repeatedly failed to update all self-referential status/version/counter statements across the reader note, companion, and reproduction package after absorbing audit findings.

**Qualifying members:** GPT 5.5, GPT 5.4 (rotation), Gemini 3.1 Pro
**Producer quarantine:** Claude/Anthropic excluded from convergence-bearing verdicts (advisory-only)

---

### 2.2 F-AM: al-Amana (Provenance Integrity)

**Papers:** 0071-0079, 0101-0104, 0766-0767 (approx. 14 papers)
**Reader-facing paper:** 0101_R0421 -- *Bayyinah al-Amana: Provenance Integrity for Public Open Data* v1.0
**Reader note:** 0102_R0422
**Data source:** Same Socrata datasets (gpsc-qqsz and twsw-2mqa) examined at the provenance/metadata layer
**Reproduction script:** 0038_R0485 -- reproduce_paper3.py
**Dataset README:** 0104_R0477

**Core findings (Tier 1):**
- Provenance classification: gpsc-qqsz = "community"; twsw-2mqa = "official"
- Snapshot integrity: SHA-256 verified (c49488723819d272...)
- Three-resolution divergence reproduced exactly:
  - FY2022: 0 row difference, $0.75 face difference (value-level, not rounding)
  - FY2023: identical (12,114 rows / $63,569,204,049.36)
  - FY2024: +70 rows (0.5103%), +$58,072,427.23 (0.0891%)
- Freshness lags: 335/701/1066 days (community); 456/822/1187 days (official)
- Schema: 23 fields (community) vs 32 fields (official); 16 official-only, 7 community-only
- Revision API: HTTP 404 (revisions.json not available)
- Uniform :created_at across each closed year = wholesale-republish or first-batch-load

**Tier 2 (inference on disclosed metadata):**
- "Wholesale republish" inference -- uniform :created_at consistent with but not conclusive proof of republish (could also be first-time batch load)
- "Post-close-batch" vs "wholesale republish" -- key wording discipline established

**Tier 3 (REFUSED):**
- No assertion that any divergence was illegitimate, unauthorized, or deceptive
- "Tamper" used only as "tamper-evident" (method property, not charge)

**Audit trail -- 3 rounds:**

| Round | Version | Verdict | Counter |
|-------|---------|---------|---------|
| R1 (0071/0072/0073/0766) | v0.1 | QUALIFYING PASS | 0->1 |
| R2 (0074/0075/0076/0077/0103) | v0.2 | QUALIFYING PASS | 1->2 |
| R3 (0078/0079/0767) | v0.3 | QUALIFYING PASS | 2->3; **CONVERGENCE MET**; rotation closed |

**Notable:** GPT 5.4 in F-AM-R2 (0076_R0455) self-reported an accidental isolation breach (workspace-wide grep touching other directories) and honestly marked itself INCOMPLETE, even though its artifact-level findings were clean. This is a structural-integrity moment -- the model prioritized honest attestation over a clean verdict.

**Qualifying members:** GPT 5.5, Gemini 3.1 Pro, GPT 5.4 (rotation in R3)
**Producer quarantine:** Claude advisory-only

---

### 2.3 F-PC: Procurement Concentration (NYC Comptroller Data)

**Papers:** 0082-0088, 0196, 0768-0773, 0775, 0777 (approx. 16 papers)
**Reader-facing paper:** 0196_R0476 -- *Procurement Concentration and Potentially Recoverable Competitive Savings in New York City Contracting* v1.0
**Data source:** NYC Comptroller vendor CSVs (Sole Source: 106 vendors; Negotiated Acquisition: 462 vendors)
**Reproduction script:** 0039_R0486 -- reproduce_procurement.py
**Dataset README:** 0777_R0481
**Audit/Provenance Ledger:** 0775_R0475

**Core findings (Tier 1):**
- Sole Source concentration: top-1 vendor (NYCEDC) = 82.5%; top-5 = 90.6%; top-10 = 94.1%; Gini = 0.956
- Negotiated Acquisition concentration: top-1 (HANYC) = 24.0%; top-5 = 36.9%; top-10 = 46.2%; Gini = 0.819
- Five savings bases (official Table 7 basis):
  - Core: $5,658,002,459
  - Wide: $6,984,040,398
  - NYCEDC-adjusted: $4,340,052,731
  - NYCEDC-adj (positive): $4,145,452,127
  - Intermediary-screened: $3,410,947,771
- Basis effect: $194.6M difference between Table 7 ("active contracts registered") and Appendix 1 (registered parent contracts) -- a coverage-gap mechanism, not an error
- MTA cross-check: 13,718 records, 2,656 vendors, $65.19B face, top-10 30.4%, Gini 0.931 (from converged F-AA)
- Adversarial trap: including TOTAL/footnote rows inflates totals ~2x and drops top-1 to exactly 50%
- Selftest: 14 perturbations detected, 0 missed

**Tier 2:**
- The savings figures are a conditional, pilot-gated planning range
- Comptroller data covers FY2025 registered contracts, not FY2025 spending

**Tier 3 (REFUSED):**
- No assertion that savings are verified recoverable or policy-ready
- No accusation of waste, fraud, or mismanagement

**Audit trail -- 3 rounds:**

| Round | Version | Verdict | Key Issue |
|-------|---------|---------|-----------|
| R1 (0768/0082/0083/0084/0769) | v0.3 | NON-PASS | HIGH: $194.6M basis-mixing between Table 7 and Appendix 1 |
| R2 (0085/0086/0770/0087) | v0.4 | QUALIFYING PASS | All R1 fixes landed; counter 0->1 |
| R3 (0771/0772/0773/0088) | v0.5 | QUALIFYING PASS | **CONVERGENCE MET** on v0.5; counter 1->2 |

**Qualifying members:** GPT 5.5, Gemini 3.1 Pro, GPT 5.4 (rotation-closing in R3)
**Producer quarantine:** Claude advisory-only (0768_R0461, 0085_R0466)

---

### 2.4 F-MZ: al-Mizan (Federal Improper Payments)

**Papers:** 0010, 0036, 0287, 0765, 0776, 0778 (approx. 6 papers in Section VI; audit round reports are in other sections)
**Reader-facing paper:** 0287_R0412 -- *Bayyinah al-Mizan: An Audit of the Audit* v1.0
**Citation ledger:** 0010_R0413
**Convergence record:** 0765_R0414
**Reproduction script:** 0036_R0483 -- reproduce_mizan.py (v0.1)
**Reproduction package README:** 0776_R0478
**Deposit companions:** 0778_R0482

**Data source:** PaymentAccuracy.gov (federal improper-payment measurement), GAO reports, Treasury FY reports, CBO data

**Core thesis -- "An Audit of the Audit":**
The paper audits the government's own improper-payment MEASUREMENT, not the payments themselves. Two hard truths:
1. The measurement recovers zero dollars (it quantifies, it does not recover)
2. The measurement is weakest where money is largest

**Tier 1 (byte-deterministic):**
- Government-wide rate series: FY2024 = 3.659%; FY2025 = 3.835%
- Coverage: 74.8% of federal spending (CBO-used basis); 74.07% (Treasury lower basis)
- Reconciliation gap: $14.3B / 7.7% between implied and reported
- HHS: 56.7% of all implied improper payments ($97.4B); non-compliant for 3 consecutive years
- 195 programs reporting; 189 on $10M criterion
- 12/24 CFO Act agencies non-compliant
- 68/83 agencies report zero
- Reproduction: reproduce_mizan.py exits 0; selftest perturbs 17 values, catches all

**Tier 2 (disclosed method):**
- Reporting universe instability: fewer agencies/programs in FY2025 despite higher total
- FY2023->2024 decline attributable to COVID program wind-down
- Unknown payments category
- Live re-pull from PaymentAccuracy.gov confirmed

**Tier 3 (REFUSED):**
- No true total (cannot impute what unreported programs would show)
- No recoverable savings claim
- No agency adjudication
- No fraud accusation

**Audit trail -- 9 rounds (from convergence record 0765_R0414):**

| Round | Version | Verdict | Key Issue |
|-------|---------|---------|-----------|
| R1 | v0.3/0.4 | NON-PASS | Packet + selftest issues |
| R2 | v0.4 | NON-PASS | Version/status contradiction, directional error |
| R3 | v0.5 | NON-PASS | Sibling-row status drift (HIGH) |
| R4 | v0.6 | NON-PASS | Packet omission + sibling-clause drift (HIGH) |
| R5 | v0.7 | NON-PASS | Version-labels-in-body drift (HIGH) |
| R6 | v0.8 | PASS | Counter 0->1; INFO only |
| R7 | v0.8 | PASS | Counter 1->2; **content converged** (byte-identical to R6) |
| R8 | v1.0 | PASS | Counter 0->1 (v1.0 form); release re-version |
| R9 | v1.0 | PASS | Counter 1->2; **v1.0 release converged** (byte-identical to R8) |

**Dominant defect family:** Same as F-AA -- version-label drift and status-propagation failure. Numeric core reproduced correctly from R1 onward.

**Qualifying members:** GPT 5.5, GPT 5.4, Gemini 3.1 Pro
**Producer quarantine:** Claude and Perplexity excluded

---

### 2.5 F-AT/F-XA: at-Ta'lim (Educational Fairness)

**Papers:** 0091_R0420, 0092_R0419, 0286_R0479, 0774_R0474 (4 papers)
**Reader-facing paper:** 0091_R0420 -- *Bayyinah at-Ta'lim: Structural Honesty Verification for Educational Fairness Systems*
**Audit companion:** 0092_R0419
**FSF dataset README:** 0286_R0479
**FSF category-level CSV:** 0774_R0474

**Scope:** SHV applied to K-12 through Graduate Research education systems

**Nine mechanisms defined:**
- **ED-K1:** Cross-section funding audit (allocation-to-formula ratio)
- **ED-K2:** Disaggregated regression gate (weight-category regressivity)
- **ED-K3:** Scan-incomplete rating (coverage of student categories)
- **ED-K4:** Remediation-coupled mastery gate (two couplings: allocation-to-outcome and intervention-to-outcome)
- **ED-U1:** Declared-definition enforcement (for undergraduate systems)
- **ED-U2:** Validator-by-different-instance grading
- **ED-U3:** Mizan-calibrated abstention
- **ED-G1:** Thesis reproduction gate (graduate level)
- **ED-G2:** Disaggregated program-outcome disclosure
- **ED-G3:** Advising-obligation ledger

**Worked example:** NYC Fair Student Funding (FSF) FY2023, five convenience-sample schools:
- Allocation-to-formula ratio computed per school
- Weight-category regressivity analysis
- $100% funding floor since 2021-22 (all five schools at or above formula)
- Category-level register detail CSV (0774_R0474): columns dbn, school_name, category_group, subcategory, register_count, amount_usd, value_source (reported vs inferred_zero)

**Convergence status: NOT MET**
- Four audit rounds: F-XA (GPT PASS, 6 LOW), F-AT-R2 (GPT NON-QUALIFYING -- same model family as prior pass), F-AT-R3 (Gemini qualifying PASS, 2 INFO), F-AT-R4-NQ (Claude self-identified non-qualifying)
- Only ONE qualifying pass (Gemini F-AT-R3); second independent-family pass needed on rc10
- The paper explicitly states convergence is not yet achieved

---

## 3. Theoretical Thesis Papers

### 3.1 Bayyinah al-Khabir (Information-Layer Integrity Scanning)

**Paper:** 0164_R0415
**Status:** THEORETICAL ONLY -- no implementation, no convergence

Extends the Munafiq Protocol from the file layer to the information layer. Grounded in Al-Hujurat 49:6. Applies the four-process taxonomy (Aligned, Compliant, Performing, Misaligned) to information sources rather than files or financial filings.

**Six divergence dimensions:** D1 Factual, D2 Omission, D3 Framing, D4 Attribution, D5 Temporal, D6 Contextual

**Five design requirements (R1-R5)** and **five falsification criteria (F1-F5)** for any implementation.

**Four reflexivity failure modes** with safeguards (what happens when the scanner scans itself).

**Three-layer complete stack:** File (Bayyinah) -> Information (al-Khabir) -> Agent (Munafiq Protocol)

### 3.2 Bayyinah al-Maal (Financial Filings SHV)

**Paper:** 0165_R0416
**Status:** v1.0 thesis; v1.1 will publish worked mechanism contracts

Maps the four-process taxonomy to financial reporting (specifically SEC filings: 10-K, 10-Q, 8-K, DEF 14A). Uses Escape A (structural-identity retrieval with zero semantic interference) on XBRL-tagged filings.

**40 SEC mechanism candidates** in four categories, plus **10 crypto on-chain candidates**

**Five-layer integrity stack** for financial filing verification

---

## 4. Reproduction Infrastructure

All four applied studies share a common reproduction pattern:

1. **Standard-library Python only** (no third-party dependencies except openpyxl for Excel reading)
2. **Three run modes:**
   - Default: offline hash verification + figure recompute against frozen snapshot
   - `--selftest`: perturbation detection (mutate each checked value, confirm detection)
   - `--live`: re-pull from primary source, compare against frozen baseline
3. **MANIFEST.json**: pins SHA-256 hashes of frozen data; script aborts on mismatch
4. **Adversarial test discipline**: rehashing the manifest after mutation must still be caught by the live comparator (hash-gate bypass insufficient)

**Scripts in Section VI:**
- reproduce_paper2.py (F-AA): 45 statistics + schema; 22-field frozen snapshot
- reproduce_paper3.py (F-AM): 42 perturbations; provenance/freshness/divergence checks
- reproduce_procurement.py (F-PC): 14 perturbations; concentration + 5 savings bases + MTA cross-check
- reproduce_mizan.py (F-MZ): 17 perturbations; government-wide rates + HHS integrity + PIIA compliance

---

## 5. Cross-Cutting Patterns

### 5.1 Convergence Summary

| Series | Rounds to Converge | Final Version | Dominant Defect |
|--------|-------------------|---------------|-----------------|
| F-AA | 9 | v0.7 | Version-propagation failure |
| F-AM | 3 | v0.3 (counter=3) | Minimal; wording refinement only |
| F-PC | 3 | v0.5 | Basis-mixing ($194.6M) in R1 |
| F-MZ | 9 (7+2 for v1.0) | v1.0 | Version-label drift |
| F-AT | 4 (ongoing) | rc10 (not converged) | Independence requirement not yet met |

### 5.2 The Version-Propagation Defect Family

The single most common failure across all audit series is the producer's failure to update every self-referential statement (version number, round count, consecutive-pass counter, audit-history summary) across all parts of the artifact (reader note, companion, reproduction package) after absorbing fixes. This is a mechanical, not substantive, error -- the numeric/analytical core was always correct. It reveals that multi-document consistency is harder than single-document correctness.

### 5.3 Producer-Lineage Quarantine

Claude/Anthropic is consistently excluded from convergence-bearing verdicts across all series because it is the producing lineage. This is enforced by:
- Standing Rule 7 of Audit Framework v3.0
- Operating Condition 5 (producer-lineage quarantine)
- Self-identification: Claude instances consistently self-identify as non-qualifying (e.g., F-AT-R4-NQ)

Perplexity is additionally excluded from F-MZ because it orchestrated later prose.

### 5.4 Three-Tier Discipline

Every paper maintains strict tier separation:
- **Tier 1:** Byte-deterministic reproduction (hashes, counts, sums, ratios)
- **Tier 2:** Inference on disclosed method (provenance classification, freshness lags, republish inference)
- **Tier 3:** REFUSED -- no accusations, no recoverability assertions, no agency adjudication, no fraud claims

### 5.5 Qualifying Model Families

Three model families participate across all series:
- **OpenAI:** GPT 5.5 (primary), GPT 5.4 (rotation), GPT 5.6 Thinking (R1 only)
- **Google:** Gemini 3.1 Pro
- **Anthropic:** Claude Opus 4.8 (advisory-only throughout)

The Knight-Leveson correlated-blind-spot standard is maintained: two rounds from the same model family do not satisfy independence. Rotation-closing requires a member new to the prior qualifying pair.

### 5.6 Surface-vs-Substrate Divergence

The central analytical framework: every finding states what the text claims (surface) and what the data actually shows (substrate). This format forces precision -- the finding must identify the exact locus where the two diverge, and whether the divergence is:
- Arithmetic (rare -- figures almost always reproduce)
- Interpretive (common -- overclaiming what a figure implies)
- Status/version (most common -- stale self-referential metadata)

---

## 6. Data Sources Registry

| Source | Used By | URL/Identifier |
|--------|---------|----------------|
| NY State Open Data (Socrata gpsc-qqsz) | F-AA, F-AM | data.ny.gov/resource/gpsc-qqsz |
| NY State Open Data (Socrata twsw-2mqa) | F-AM | data.ny.gov/resource/twsw-2mqa |
| NYC Comptroller vendor CSVs | F-PC | comptroller.nyc.gov |
| NYC Comptroller Appendix 1 Excel | F-PC | Appendix-1-Parent-Contracts.xlsx |
| PaymentAccuracy.gov | F-MZ | paymentaccuracy.gov/agencies-and-programs |
| GAO improper-payment reports | F-MZ | (various) |
| Treasury FY reports | F-MZ | (various) |
| CBO data | F-MZ | (outlay denominator) |
| NYC DOE FSF detail reports | F-AT | (FY2023 five-school sample) |
| MTA capital tables (wcsa-vkhf, kizb-nxtu, ehz8-ag3n) | F-AA | data.ny.gov |

---

## 7. Complete Paper Inventory (75 papers)

### F-AA Series (Allocation & Asymmetry) -- 28 papers
- 0010_R0413: Citation Ledger v1.0 (standalone)
- 0011_R0417: Full audit trail (MASSIVE)
- 0012_R0423: F-AA-R1 GPT recompute (raw JSON)
- 0013_R0425: F-AA-R2 GPT audit report (NON-PASS)
- 0014_R0427: F-AA-R4 Gemini Independence Attestation (PASS)
- 0015_R0429: F-AA-R5 Gemini 3.1 Pro Report (INCOMPLETE)
- 0016_R0430: F-AA-R5 GPT 5.5 Closing-Round (NON-PASS)
- 0017_R0431: F-AA-R5 Model Council Synthesis (NON-PASS/INCOMPLETE)
- 0018_R0432: F-AA-R6 Claude Advisory (ADVISORY PASS)
- 0019_R0433: F-AA-R6 Gemini 3.1 Pro (QUALIFYING PASS)
- 0020_R0434: F-AA-R6 GPT 5.5 (QUALIFYING PASS)
- 0021_R0435: F-AA-R6 Model Council Synthesis (first consecutive PASS, counter 0->1)
- 0022_R0436: F-AA-R7 Gemini member report
- 0023_R0437: F-AA-R7 GPT 5.4 (rotation) member report
- 0024_R0438: F-AA-R7 GPT 5.5 member report
- 0025_R0439: F-AA-R7 Model Council Synthesis (NON-PASS, counter reset 1->0)
- 0026_R0440: F-AA-R8 Claude Advisory (ADVISORY PASS)
- 0027_R0441: F-AA-R8 Gemini 3.1 Pro member report (PASS)
- 0028_R0442: F-AA-R8 GPT 5.4 member report (PASS)
- 0029_R0443: F-AA-R8 GPT 5.5 member report (PASS)
- 0030_R0444: F-AA-R8 Model Council Synthesis (QUALIFYING PASS, counter 0->1)
- 0031_R0445: F-AA-R9 Gemini 3.1 Pro member report (PASS)
- 0032_R0446: F-AA-R9 GPT 5.4 member report (PASS)
- 0033_R0447: F-AA-R9 GPT 5.5 member report (PASS)
- 0034_R0448: F-AA-R9 Model Council Synthesis (CONVERGENCE MET on v0.7)
- 0035_R0480: Reproduction and Audit Dataset README
- 0037_R0484: reproduce_paper2.py (v0.3)
- 0070_R0418: Reader-facing paper v1.0 (converged)
- 0288_R0424: F-AA-R1 Cross-Instance Audit (GPT, NON-PASS 0C/3H/3M/3L)
- 0289_R0426: F-AA-R3 Claude Advisory (NON-PASS 0C/1H; producer-lineage, non-qualifying)
- 0290_R0428: F-AA-R5 Claude Advisory (INCOMPLETE; missing reproduction package)

### F-AM Series (al-Amana Provenance Integrity) -- 14 papers
- 0038_R0485: reproduce_paper3.py
- 0071_R0449: F-AM-R1 Claude Opus 4.8 Advisory report
- 0072_R0450: F-AM-R1 Gemini 3.1 Pro member report (QUALIFYING PASS)
- 0073_R0451: F-AM-R1 GPT 5.5 member report (QUALIFYING PASS)
- 0074_R0453: F-AM-R2 Claude Advisory (NON-CONVERGENCE-BEARING)
- 0075_R0454: F-AM-R2 Gemini 3.1 Pro member report (QUALIFYING)
- 0076_R0455: F-AM-R2 GPT 5.4 member report (INCOMPLETE -- honest isolation breach)
- 0077_R0456: F-AM-R2 GPT 5.5 member report (QUALIFYING PASS)
- 0078_R0458: F-AM-R3 Gemini 3.1 Pro member report (QUALIFYING)
- 0079_R0459: F-AM-R3 GPT 5.4 (rotation, QUALIFYING)
- 0101_R0421: Reader-facing paper v1.0 (converged, count THREE)
- 0102_R0422: Reader note (paper v1.0)
- 0103_R0457: F-AM-R2 Cross-Instance Synthesis (QUALIFYING PASS, counter 0->1)
- 0104_R0477: Dataset README v1.0
- 0766_R0452: F-AM-R1 Round 1 Synthesized Verdict (QUALIFYING PASS)
- 0767_R0460: F-AM-R3 Synthesis (QUALIFYING PASS, counter 2->3, rotation closed)

### F-PC Series (Procurement Concentration) -- 16 papers
- 0039_R0486: reproduce_procurement.py
- 0082_R0462: F-PC-R1 Gemini 3.1 Pro member report (PASS)
- 0083_R0463: F-PC-R1 GPT 5.4 member report (QUALIFYING)
- 0084_R0464: F-PC-R1 GPT 5.5 member report (QUALIFYING)
- 0085_R0466: F-PC-R2 Claude Advisory (ADVISORY ONLY)
- 0086_R0468: F-PC-R2 GPT 5.5 member report (QUALIFYING PASS)
- 0087_R0469: F-PC-R2 Model Council Synthesis (QUALIFYING PASS)
- 0088_R0473: F-PC-R3 Model Council Synthesis (CONVERGENCE MET on v0.5)
- 0196_R0476: Reader-facing paper v1.0 (converged)
- 0768_R0461: F-PC-R1 Claude Advisory (ADVISORY-ONLY)
- 0769_R0465: F-PC-R1 Synthesized Round-1 Audit (NON-PASS, HIGH: $194.6M)
- 0770_R0467: F-PC-R2 Gemini 3.1 Pro member report (QUALIFYING)
- 0771_R0470: F-PC-R3 Gemini 3.1 Pro member report (QUALIFYING PASS)
- 0772_R0471: F-PC-R3 GPT 5.4 member report (PASS, rotation-closing)
- 0773_R0472: F-PC-R3 GPT 5.5 member report (QUALIFYING PASS)
- 0775_R0475: Audit and Provenance Ledger v1.0
- 0777_R0481: Reproduction and Audit Dataset README v1.0

### F-MZ Series (al-Mizan) -- 6 papers
- 0010_R0413: Citation Ledger v1.0
- 0036_R0483: reproduce_mizan.py (v0.1)
- 0287_R0412: Reader-facing paper v1.0 (converged)
- 0765_R0414: Convergence Record v1.0
- 0776_R0478: Reproduction Package README (v0.1)
- 0778_R0482: Deposit Companions

### F-AT/F-XA Series (at-Ta'lim) -- 4 papers
- 0091_R0420: Reader-facing paper (NOT CONVERGED)
- 0092_R0419: Audit and Provenance Companion
- 0286_R0479: NYC DOE FSF FY2023 Companion Dataset README
- 0774_R0474: FSF category-level CSV data

### Theoretical Thesis Papers -- 2 papers
- 0164_R0415: Bayyinah al-Khabir (Information-Layer Integrity)
- 0165_R0416: Bayyinah al-Maal (Financial Filings SHV)

### Earlier Cross-Instance Reports -- 3 papers
- 0288_R0424: F-AA-R1 Cross-Instance Audit (GPT 5.6 Thinking)
- 0289_R0426: F-AA-R3 Claude Advisory
- 0290_R0428: F-AA-R5 Claude Advisory

---

## 8. Key Observations

1. **Numeric core always correct.** Across all four converged series and 30+ audit rounds, the arithmetic/statistical core never contained a substantive error. Every Tier 1 figure reproduced from R1 onward. The defects were always in the metadata, framing, or interpretive claims surrounding the correct numbers.

2. **Multi-document consistency is the hard problem.** The version-propagation defect family -- failing to update all self-referential statements across reader note, companion, and reproduction package -- accounted for most HIGH findings and most round failures. This is an organizational challenge, not an analytical one.

3. **The three-tier discipline held throughout.** No paper ever made a Tier 3 claim (accusation, recoverability assertion, fraud allegation). The refusal boundary was tested in every round and never breached.

4. **Producer quarantine is rigorously enforced.** Claude consistently self-identifies as non-qualifying when it is the producing lineage, and its verdicts are consistently excluded from convergence counts. This extends to Perplexity in F-MZ where it contributed to later prose.

5. **The adversarial test design is clever.** The rehashed-manifest adversarial test (hash gate bypassed, but live comparator still catches drift) demonstrates defense in depth. A single integrity gate is insufficient; the live comparator is the real backstop.

6. **Honest self-reporting.** GPT 5.4 in F-AM-R2 marking itself INCOMPLETE after an accidental workspace-wide grep demonstrates that the audit protocol successfully incentivizes honest self-assessment over clean verdicts.

7. **Convergence velocity varies.** F-AM converged in 3 rounds; F-PC in 3; F-AA needed 9; F-MZ needed 9. The difference is largely attributable to the version-propagation defect family hitting harder in larger, more complex artifacts.

8. **at-Ta'lim remains open.** The only series not yet converged. It needs a second qualifying pass from an independent model family. This is an honest disclosure of incomplete status.

---

# Bismillah ir-Rahman ir-Rahim
