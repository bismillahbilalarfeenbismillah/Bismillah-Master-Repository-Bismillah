# Bismillah ir-Rahman ir-Rahim

# R0461 -- Model Council Audit Report — Claude Opus 4.8 (ADVISORY-ONLY)

**Chronological Index:** 768 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-PC-R1_claude_advisory.md  
**Source Format:** md  
**SHA-256:** `67dee38f9a289b156ce7683d1ec7788a4b0cb68393e334e4e43f16118f17f2a1`  

---

## R0461 · Model Council Audit Report — Claude Opus 4.8 (ADVISORY-ONLY)

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-PC-R1_claude_advisory.md
- source_format: md
- text_sha256: 67dee38f9a289b156ce7683d1ec7788a4b0cb68393e334e4e43f16118f17f2a1

# Model Council Audit Report — Claude Opus 4.8 (ADVISORY-ONLY)

## Cross-Instance Audit of "Procurement Concentration and Recoverable Competitive Savings in New York City Contracting" (v0.3)
### Namespace: F-PC-R1 | Round 1

---

## 1. Identity and Lineage

- **Member identity:** Claude Opus 4.8 (Anthropic).
- **Lineage:** Anthropic / Claude.
- **Producer-lineage status:** Claude is the PRODUCER LINEAGE for this paper's program (BayyinahEnterprise / Bayyinah Civic Integrity Program). Under the audit brief's Operating Condition 5 (producer-lineage quarantine) and Standing Rule 7 of Audit Framework v3.0, any Claude-family member is **ADVISORY-ONLY** and **EXCLUDED from the convergence-bearing verdict**. This instance is therefore **NON-QUALIFYING (advisory)**. My verdict is recorded for reference only and does **not** count toward the two-consecutive-qualifying-PASS convergence requirement.

## 2. No-History / No-Memory Attestation (verbatim)

I am an INDEPENDENT, FRESH, MEMORYLESS audit instance on a Model Council. I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, NO carryover from any earlier Bayyinah round, and NO access to any other council member's work. I worked only from the materials in my workspace (`/home/user/workspace/council/claude/`).

## 3. Execution Status

**EXECUTED — in full.** All five mandatory steps were run in the workspace with real, unedited outputs pasted below. I additionally obtained the Comptroller Appendix 1 microdata (which the paper says returns HTTP 403) and performed the exact line-item reconciliation the paper deferred. This is a genuine reproduction, not a comparison of stated numbers.

Environment note: `python3` standard library; `openpyxl` installed only for reading the Appendix 1 `.xlsx` during independent reconciliation (Step 4 core recompute used the standard library only and did **not** import any function from `reproduce_procurement.py`).

---

## 4. Pasted Real Outputs (Steps 1–5)

### Step 1 — `python3 reproduce_procurement.py`

```
[integrity] sole_source  OK
[integrity] negotiated   OK

Concentration (Table 2), clean vendor rows:
  sole_source  vendors=106 total=$1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% gini=0.95557  [OK]
  negotiated   vendors=462 total=$3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% gini=0.81855  [OK]

Addressable base and savings (Table 3), official Table 7 basis:
  savings base Core             $5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492  [OK]
  savings base Wide             $6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080  [OK]
  savings base NYCEDC-adjusted  $4,340,052,731  @10%=$434,005,273  @20%=$868,010,546  [OK]

MTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):
  FY2024: 13718 records, 2656 vendors, $65189755228.64 face, top10 30.4151%, Gini 0.93117

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official (open reconciliation item). This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
EXIT_CODE=0
```
**Result:** Both hashes OK; both subgroups reproduce exactly; all three savings bases OK; exit 0; every line OK.

### Step 2 — `python3 reproduce_procurement.py --selftest`

```
[integrity] sole_source  OK
[integrity] negotiated   OK
[selftest] perturbing each checked value...
[selftest] perturbed 14 values; missed 0
EXIT_CODE=0
```
**Result:** Comparator detected all 14 perturbations, missed 0. Exit 0.

### Step 3 — `python3 reproduce_procurement.py --live`

```
[integrity] sole_source  OK
[integrity] negotiated   OK

Concentration (Table 2), clean vendor rows:
  sole_source  vendors=106 total=$1597506644.98 top1=82.5004% top5=90.5858% top10=94.0642% gini=0.95557  [OK]
  negotiated   vendors=462 total=$3865895209.67 top1=24.0334% top5=36.9178% top10=46.2163% gini=0.81855  [OK]

Addressable base and savings (Table 3), official Table 7 basis:
  savings base Core             $5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492  [OK]
  savings base Wide             $6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080  [OK]
  savings base NYCEDC-adjusted  $4,340,052,731  @10%=$434,005,273  @20%=$868,010,546  [OK]

MTA FY2024 cross-check (live re-pull from data.ny.gov):
  MTA FY2024 live: records=13718 vendors=2656 face=$65189755228.64 top10=30.4151% gini=0.93117  [OK]

MTA constants carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552):
  FY2024: 13718 records, 2656 vendors, $65189755228.64 face, top10 30.4151%, Gini 0.93117

[note] Concentration is measured on the positive-amount vendor basis; the savings model uses the official Table 7 base. The Negotiated positive basis is about 4.75% ($192.96M) below official (open reconciliation item). This tool measures; it does not judge whether any award should have been competed (refused).

All checks reproduced exactly. Exit 0.
EXIT_CODE=0
```
**Result:** Live re-pull from data.ny.gov confirms **13,718 records / 2,656 vendors / $65,189,755,228.64 face / top-10 30.4151% / Gini 0.93117** with **no drift** from the carried constants. Exit 0.

### Step 4 — Independent recompute (my own code; no import of script functions)

```
=== Independent SHA-256 (my own hashing) ===
  sole_source_vendors_fy25.csv: MATCH  990993de3c435972dc68720eb2244b1a3cb7ab62d24f769193d40a227f4306f5
  negotiated_acquisition_vendors_fy25.csv: MATCH  5d0d640daba04ec7f16b37d74cd9565441fab2e5a69c702ebe18bd7d6bba2ce4

=== SOLE SOURCE (independent) ===
  vendors        = 106
  total          = $1,597,506,644.98
  top-1 share    = 82.5004%
  top-5 share    = 90.5858%
  top-10 share   = 94.0642%
  top-20 share   = 97.2606%
  Gini           = 0.95557
  top vendor     = NEW YORK CITY ECONOMIC DEVELOPMENT CORPORATION @ $1,317,949,728.00

=== NEGOTIATED (independent) ===
  vendors        = 462
  total          = $3,865,895,209.67
  top-1 share    = 24.0334%
  top-5 share    = 36.9178%
  top-10 share   = 46.2163%
  top-20 share   = 55.3833%
  Gini           = 0.81855
  top vendor     = HANYC FOUNDATION INC @ $929,104,960.00

=== Independent savings bases from OFFICIAL Table 7 figures ===
  Core             base=$5,658,002,459  @10%=$565,800,246  @20%=$1,131,600,492
  Wide             base=$6,984,040,398  @10%=$698,404,040  @20%=$1,396,808,080
  NYCEDC-adjusted  base=$4,340,052,731  @10%=$434,005,273  @20%=$868,010,546

=== Negotiated official-base coverage check ===
  official negotiated = $4,058,851,691
  positive-basis      = $3,865,895,209.67
  gap                 = $192,956,481.33  (4.75% of official)
  coverage            = 95.25% of official base
  sole source gap     = $1,644,123.02 (0.1028% of official)
```
**Result:** My independent implementation (own SHA-256, own CSV parse with an independent positive-integer-Rank filter, own mean-absolute-difference Gini formulation distinct from the script's sort-index formula) reproduces **every** figure exactly: both vendor counts, all top-1/5/10/20 shares, both Ginis, both top vendors and amounts, and all three savings bases computed from the official Table 7 figures ($1,599,150,768 + $4,058,851,691 = $5,658,002,459; + $1,326,037,939 = $6,984,040,398; − $1,317,949,728 = $4,340,052,731). Negotiated coverage is **95.25%** of the official base; Sole Source gap is only 0.1028%.

### Step 5 — Adversarial trap check (deliberately include TOTAL + footnote rows)

```
=== SOLE SOURCE WITH TOTAL ROW INCLUDED (trap) ===
  row count (incl TOTAL) = 107
  inflated total         = $3,195,013,289.96
  top-1 share            = 50.0000%  <-- TOTAL row equals sum of vendors -> ~50%
  largest entry          = $1,597,506,644.98

=== NEGOTIATED WITH TOTAL ROW INCLUDED (trap) ===
  row count (incl TOTAL) = 463
  inflated total         = $7,731,790,419.35
  top-1 share            = 50.0000%  <-- TOTAL row equals sum of vendors -> ~50%
  largest entry          = $3,865,895,209.68
```
**Result:** Trap confirmed. Including the `TOTAL` row roughly doubles each total ($1.598B → $3.195B; $3.866B → $7.732B) and drives top-1 to **exactly 50.0000%** (the TOTAL row equals the sum of the vendor rows). The three footnote rows (`Source`, `Official report total`, `URL`) have non-numeric value fields and self-exclude. Both the supplied script's `Rank.isdigit()` filter and my independent positive-integer-Rank filter correctly exclude all four rows. The paper's stated basis (clean vendor rows only) is therefore the non-inflated one. **The paper does not fall into the trap.**

Minor observation: the Negotiated CSV's stored `TOTAL` cell reads `3865895209.68`, one cent above the summed vendor total `3865895209.67` — a rounding artifact in the stored total, immaterial and not carried into any reported figure.

---

## 5. Two Points Pressed Hardest

### 5.1 The $192.96M Negotiated reconciliation — I OBTAINED THE MICRODATA AND RECONCILED IT

**Access:** The paper (Section 4.4), README, and brief all state the Comptroller Appendix 1 microdata is "access-gated to automated retrieval (HTTP 403 with a bot-detection page)." **This is not reproducible from my environment.** I retrieved the file cleanly:
- `curl` default UA → **HTTP 200** (12,070,166 bytes, valid `Microsoft Excel 2007+`)
- `curl` browser UA → HTTP 200
- `python urllib` with `User-Agent: bayyinah-proc` → HTTP 200
- `python urllib` with **no** UA → HTTP 200

The stated 403 blocker does not hold; the reconciliation the paper deferred as an "open audit item" **is achievable**, and I performed it.

**Line-item reconciliation (FY2025 rows in `Appendix-1-Parent-Contracts.xlsx`, sheet `FY25_ASCR`):**

| Subgroup (FY2025) | Microdata rows | All positive? | Blank/NULL vendor names | Null/zero/neg amounts | Distinct vendors | Microdata sum | Official Table 7 | Contract-count gap | Dollar gap |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| Negotiated Acquisition | 935 | yes (935/935) | **0** | 0 | 462 | $3,865,895,209.68 | 962 / $4,058,851,691 | **27** | **$192,956,481.32** |
| Sole Source | 115 | yes (115/115) | **0** | 0 | 106 | $1,597,506,644.98 | 126 / $1,599,150,768 | 11 | $1,644,123.02 |

**Logic tests (confirmed):**
- **Zero/blank records ruled out:** correct — a zero-amount record does not move a sum, and there are in fact **zero** null/zero-amount rows in the FY25 microdata. Magnitude ($193M) cannot come from zeros.
- **Dropped negatives ruled out:** correct — removing negatives from a positive-only total would *raise* it, not lower it; and there are **zero** negative rows. Magnitude cannot come from negatives.
- **Paper's stated likely mechanism — "positive-value contracts that could not be attributed to a distinct vendor name and were therefore dropped by the vendor-level aggregation" — is CONTRADICTED by the microdata.** All 935 FY25 Negotiated microdata rows carry a non-blank vendor name (0 blank/NULL); none were dropped during vendor aggregation for lack of a name. The gap is not attribution-loss inside the file. **The 27 missing contracts (and $192.96M) are simply absent from the published Appendix 1 file** — Table 7's aggregate count (962) exceeds the count of parent-contract rows in Appendix 1 (935). The correct mechanism is a **coverage/scope difference between Table 7's aggregate and the Appendix 1 parent-contracts extract**, not intra-file name-attribution loss. The paper reached a plausible-sounding but demonstrably wrong micro-mechanism because it did not open the file it claimed was blocked.
- **Disclosure of 95.25% basis:** the paper **does** disclose this adequately and repeatedly — Section 4.4 ("computed on about 95.25% of the official subgroup dollar base"), Section 5.0's basis note, the script's runtime `[note]`, and the README. That disclosure is a strength. The defect is the *stated cause*, not the disclosure of the magnitude.

### 5.2 The savings estimate's conditional framing

Adversarial reading of the abstract, Section 5.0, the conclusion, and all four recommendations plus the pilot:
- **In-prose framing holds.** Every prose statement of the number is conditionalized: "conditional planning range," "not a verified recoverable amount," "gated on a pilot," "not a measurement of money the City is losing or a promise of money it will save," "No figure here should be cited as recoverable until the pilot in Section 7 tests the alternative-vendor assumption," "should not be cited as recoverable before it does." The leak-trigger phrases on line 134 appear inside an explicit **negation** ("*not* a measurement of money the City is losing *or* a promise of money it will save"), which is compliant, not a leak.
- **Titles are the one soft spot.** The **document title** ("Recoverable Competitive Savings") and **Table 3 title** ("Estimated Recoverable Savings") use "Recoverable" unqualified. Under strict adversarial reading this is in tension with the body's rule that no figure should be *called* recoverable pre-pilot. It does not rise to an in-prose assertion that the money *is* recoverable (Table 3 is softened by "Estimated"), so I score it LOW, but it should be bounded further (e.g., "Potentially Recoverable" / "Conditional Competitive Savings").
- **Logic of applying a single-bid-elimination delta to the whole addressable base:** this is an **overreach the paper should further bound**, and the paper partially concedes it. The Czech ~10% and Slovak ~19pp deltas are estimated on contracts that transition *from single-bidder to multi-bidder*. Applying that delta to the *entire* Sole Source + Negotiated base assumes the whole base both (a) has viable alternative vendors and (b) would realize the same delta — but the paper's own Section 4.5 shows the base is dominated by designated single-vehicle intermediaries (NYCEDC 82.5% of Sole Source; HANYC 24.0% of Negotiated) for which the delta is, by the paper's own argument, largely inapplicable. The paper mitigates this with the NYCEDC-adjusted row, the pilot gate, and Limitation bullets 5–6, but it does **not** apply the same haircut to HANYC-type Negotiated intermediaries and concedes the adjusted-core figure "is therefore likely still an overestimate." The estimate is directionally bounded but the multiplier-times-full-base construction remains an acknowledged overestimate; this is a MEDIUM methodological caution, disclosed but not fully bounded.

### 5.3 Tier-3 refusal boundary

No Tier-3 violation. Every accusation-adjacent term is used in an **exculpatory/negating** construction: "Group 2 is not inherently improper" (line 20); "a non-culpable structural explanation rather than evidence of misconduct" (line 122); "non-culpable structural pattern, not recoverable waste" (line 132). The paper consistently measures and refuses to accuse any award or vendor of impropriety or to assert recoverability as fact. Compliant.

### 5.4 House-style and internal consistency

- **Em/en-dashes:** 0 en-dashes (U+2013), 0 em-dashes (U+2014). Uses ASCII `--`. PASS.
- **Brand "BayyinahEnterprise":** present and correct. PASS.
- **MTA reproduction described as nine rounds:** consistent ("nine audit rounds," "nine rounds," "nine independent"). PASS.
- **Version uniformly v0.3:** only "Draft v0.3" appears; no stray versions. PASS.
- **Concentration figures consistent** across abstract, Table 2, and body (Gini 0.956 / 0.931 / 0.819; top-1 82.5% / 24.03%). PASS.
- **Savings/base figures consistent** ($5.66–$6.98B base; Table 3 products verified). PASS on arithmetic.
- **Inconsistency found (see F-PC-R1-002):** the **abstract states the headline range as "$434 million to $1.40 billion,"** but **Section 5.0 and the Conclusion state the headline as "$500 million to $1.4 billion" and expressly treat $434M as a sensitivity *floor*, "not a revised headline."** The abstract folds the sensitivity floor into the headline range, contradicting the body's own framing.
- **Trivial spelling inconsistency:** "at-Ta'līm" (macron, lines 8, 22) vs "at-Ta'lim" (plain, line 132). INFO.

---

## 6. Findings Table (F-PC-R1)

Six-element format: (identifier | severity | locus | substance = surface-vs-substrate divergence | disposition | cross-reference).

| ID | Severity | Locus | Substance (surface vs substrate) | Disposition | Cross-ref |
|---|---|---|---|---|---|
| **F-PC-R1-001** | **MEDIUM** | §4.4; README "Known open item"; brief §"two points" | **Surface:** paper asserts the $192.96M Negotiated gap's likely mechanism is "positive-value contracts unattributable to a distinct vendor name, dropped by vendor aggregation," and that Appendix 1 is unreachable (HTTP 403). **Substrate:** I retrieved Appendix 1 (HTTP 200, four methods) and reconciled it — the 935 FY25 Negotiated microdata rows are 100% positive, 100% named (0 blank/NULL), 0 null/zero/neg; nothing was dropped for missing names. The gap is 27 contracts absent from Appendix 1 entirely (962 Table 7 vs 935 file rows), i.e., a Table-7-vs-Appendix-1 coverage difference, not intra-file attribution loss. | Correct the stated mechanism; drop or qualify the 403 claim; the reconciliation is achievable and should be performed. Magnitude/95.25% disclosure is adequate and may stand. | §4.4; §5.0 basis note; §5.2 above |
| **F-PC-R1-002** | **MEDIUM** | Abstract (line 14) vs §5 (line 146) and §9 (line 204) | **Surface:** abstract presents the headline savings range as "$434 million to $1.40 billion." **Substrate:** the body's own stated headline is "$500 million to $1.4 billion," with $434M explicitly labeled a sensitivity floor "not a revised headline." The abstract contradicts the body's framing of its own primary number. | Reconcile: state one headline range consistently; present $434M uniformly as a sensitivity floor if that is the intent. | §5, ¶line146; §9 |
| **F-PC-R1-003** | **LOW** | Title (line 1); Table 3 title (line 138) | **Surface:** titles say "Recoverable Competitive Savings" / "Estimated Recoverable Savings" unqualified. **Substrate:** the body's binding rule is that no figure should be *called* recoverable before the pilot; the unqualified title label sits in tension with that discipline. Not an in-prose assertion of verified recovery. | Bound the label (e.g., "Conditional/Potentially Recoverable") to match the body's conditional frame. | §5.0; §5.2 above |
| **F-PC-R1-004** | **LOW** | §5 (Table 3 construction); §3.1 literature | **Surface:** a single-bid-elimination price delta (Czech ~10%, Slovak ~19pp) is applied to the entire addressable base. **Substrate:** the delta is estimated on single→multi-bidder transitions; the base is dominated by designated single-vehicle intermediaries (NYCEDC 82.5% SS, HANYC 24.0% Neg) for which the delta is, per the paper's own §4.5, largely inapplicable. Disclosed and partly mitigated (NYCEDC-adjusted row, pilot gate, Limitations 5–6), but HANYC-type Negotiated spend is not haircut and the figure is conceded to be "likely still an overestimate." | Further bound: apply an intermediary screen to Negotiated as done for Sole Source before any headline number; keep the pilot gate. | §5; §4.5; §8 |
| **F-PC-R1-005** | **INFO** | Lines 8, 22 vs 132 | **Surface:** program name rendered "at-Ta'līm" (macron) in most places, "at-Ta'lim" (plain) once. **Substrate:** trivial transliteration inconsistency; no substantive effect. | Normalize spelling. | — |
| **F-PC-R1-006** | **INFO** | Negotiated CSV `TOTAL` cell | **Surface:** stored TOTAL reads `3865895209.68`. **Substrate:** summed vendor rows = `3865895209.67` (1-cent rounding artifact in the stored total). Not carried into any reported figure; excluded by the clean-row filter. | No action; noted for completeness. | Step 5 |

**Tier-1 (byte-deterministic) verification:** hashes, both subgroups' concentration (counts, top-N, Gini, top vendor/amount), all three savings bases, and all MTA FY2024 constants (offline and live) **all reproduce exactly**. Zero Tier-1 discrepancies.

**Severity tally:** CRITICAL 0 | HIGH 0 | MEDIUM 2 | LOW 2 | INFO 2.

---

## 7. Advisory Verdict

**VERDICT: PASS (ADVISORY-ONLY — DOES NOT COUNT TOWARD CONVERGENCE).**

- **Zero CRITICAL and zero HIGH findings**, with fully documented executed reproduction (Steps 1–5 pasted above) plus an independent line-item reconciliation of the one open item. On the qualifying criteria (zero CRITICAL/zero HIGH + executed reproduction), this package would meet a PASS bar.
- **However, this verdict is ADVISORY-ONLY because Claude (Anthropic) is the producer lineage for this program.** Per the brief's Operating Condition 5 and Standing Rule 7, I am quarantined and **excluded from the convergence-bearing verdict**. My PASS is recorded for reference only and **does not move the consecutive-qualifying-PASS count** (which remains driven solely by non-Claude qualifying members).
- **Convergence-count impact from this instance: NONE (0 → 0).** Convergence still requires two consecutive qualifying (non-Claude, non-producer) members who both execute the reproduction and return zero CRITICAL/zero HIGH. This instance cannot contribute to that count.

**Reasoning basis:** every conclusion above is drawn from executed code and retrieved primary data, not from the brief's assertions or the paper's confidence. The two MEDIUM findings are disclosure/consistency defects (a wrong micro-mechanism for a correctly-magnituded and adequately-disclosed gap; an abstract-vs-body headline-range mismatch) — material enough to fix in a v0.4 but not integrity-breaking, and specifically **not** Tier-1 arithmetic errors. Notably, my Appendix 1 reconciliation strengthens rather than undermines the paper's core numbers: the microdata independently confirms the 935-row / $3,865,895,209.68 / 462-vendor Negotiated basis and the 115-row / $1,597,506,644.98 / 106-vendor Sole Source basis to the cent.

---

## 8. Artifacts written to workspace

- `/home/user/workspace/council/claude/independent_recompute.py` — my independent recompute (Step 4).
- `/home/user/workspace/council/claude/trap_check.py` — adversarial trap check (Step 5).
- `/home/user/workspace/council/claude/reconcile2.py`, `reconcile3.py` — Appendix 1 line-item reconciliation.
- `/home/user/workspace/council/claude/appendix1.xlsx` — retrieved Comptroller Appendix 1 microdata (12.07 MB, HTTP 200).
- `/home/user/workspace/model-council-claude.md` — this report.

---

# Bismillah ir-Rahman ir-Rahim
