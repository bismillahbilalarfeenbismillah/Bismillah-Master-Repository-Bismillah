# Bismillah ir-Rahman ir-Rahim

# Deep Read Report -- Section VI-B: Applied Audits (Batch 2)
## Papers Read: 25

## Total Size: 510,270 characters across 7,991 lines

---

## Per-Paper Summaries

### R0480 -- Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits -- Reproduction and Audit Dataset (v1.0)
- **Date:** 2024
- **Source:** README.md
- **Size:** 69 lines, 4,773 chars
- **SHA-256:** `2bb1d161a3f4ba05...`

**Structure:**
  - Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits -- Reproduction and Audit Dataset (v1.0)
  -   Related deposits
  -   Contents
  -   How to reproduce
  -   Expected top-line values (FY2024, community view gpsc-qqsz)
  -   Audit trail summary

**Key Concepts:** DOI, MANIFEST, SHA, MWBE, NON, PASS, GPT

**Content Summary:**
- source_format: md - text_sha256: 2bb1d161a3f4ba05bd3758efa535ae631a95736bfa94796c416de4611ce00dd3
# Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits -- Reproduction and Audit Dataset (v1.0)
This dataset accompanies the canonical v1.0 release and lets any party reproduce every figure in the paper and inspect the full nine-round cross-instance audit trail.

---

### R0483 -- reproduce_mizan.py — reproduce_mizan.py -- Bayyinah al-Mizan reproduction package (v0.1)
- **Date:** 2024
- **Source:** reproduce_mizan.py
- **Size:** 242 lines, 12,245 chars
- **SHA-256:** `a43b3cbe6fc5c7cb...`

**Structure:**
  - !/usr/bin/env python3
  - ---- EXPECTED values (verified against the frozen snapshot); a mismatch is a finding ----
  - GAO government-wide rollup (reconciliation target, cited, not computed here):
  - Coverage per CRFB analysis of GAO FY2025 (reconciliation target for --live vs USAspending):
  - FY2025 agency rollup reconciliation (the coverage + reconciliation-gap finding):
  - ---------- parsers ----------
  - embedded chart series (dollar amounts, in the order the site emits them)
  - ---------- concentration ----------
  - ---------- modes ----------
  - hashes
  - government-wide improper rate
  - HHS integrity facts
  - FY2025 rollup reconciliation (recomputed from the frozen page, not read from JSON)
  - PIIA non-compliance exposure (agency-years found non-compliant)
  - numeric fields: perturb by a detectable delta

**Key Concepts:** MEASUREMENT, NOT, PIIA, HHS, SHA, CODE, YEAR, USA, REFUSED, BASE

**Content Summary:**
- source_format: py - text_sha256: a43b3cbe6fc5c7cb7c4375b95bb720385df5dbeaa34bbd293b4bcdfb1841ad23
#!/usr/bin/env python3 """ reproduce_mizan.py -- Bayyinah al-Mizan reproduction package (v0.1)
Structural Honesty Verification of the U.S. federal improper-payment MEASUREMENT. This tool does NOT re-detect improper payments (that requires protected claims data). It verifies the coverage, reconciliation, and completeness integrity of the government's own published estimate on PaymentAccuracy.gov, against the substrate of federal spending and the government's own risk / PIIA-compliance determinations.

---

### R0484 -- reproduce_paper2.py — Reproduce every figure in Bayyinah Allocation & Asymmetric-Measure Audits (Paper 2, v0.3).
- **Date:** 2024
- **Source:** reproduce_paper2.py
- **Size:** 180 lines, 8,957 chars
- **SHA-256:** `74fa6ef7b9dd32e5...`

**Structure:**
  - !/usr/bin/env python3
  - FY2024 detail
  - navigate to the leaf and bump it by 10x tolerance
  - schema perturbation

**Key Concepts:** EVERY, HERE, SNAP, MAN, MANIFEST, FYS, PCT, TOL, REL, ABORT

**Content Summary:**
- source_format: py - text_sha256: 74fa6ef7b9dd32e57fe0707e44b5c4487e4a19a41873e583f55e02e8ddef9f84
#!/usr/bin/env python3 """ Reproduce every figure in Bayyinah Allocation & Asymmetric-Measure Audits (Paper 2, v0.3).
A single stats() object holds EVERY published statistic. It drives three modes: python3 reproduce_paper2.py           # offline report from the frozen snapshot (hash + field-inventory validated) python3 reproduce_paper2.py --live    # re-pull all 3 years live; compare EVERY statistic + schema + row count python3 reproduce_paper2.py --selftest# perturb each statistic and confirm the comparator detects it Exit status is nonzero on any integrity failure, any live drift beyond tolerance, or any missed perturbation. Source: NY State Open Data, community view gpsc-qqsz (first-party...

---

### R0485 -- reproduce_paper3.py — reproduce_paper3.py -- Provenance Integrity for Public Open Data (Bayyinah Paper 3).
- **Date:** 2024
- **Source:** reproduce_paper3.py
- **Size:** 229 lines, 9,624 chars
- **SHA-256:** `188e21a072c1ccb9...`

**Structure:**
  - !/usr/bin/env python3
  - 1. Provenance classification and community-vs-official divergence.
  - 2. Snapshot integrity (SHA-256 of the frozen capture vs MANIFEST).
  - 3. Declared-vs-actual freshness (row-level :created_at postdating the reporting period).
  - 4. Schema divergence (served field inventory per dataset).
  - ---------- io ----------
  - ---------- live pull (mirrors how the capture was built) ----------
  - ---------- flatten for comparison / perturbation ----------
  - ---------- the four checks (offline, from the frozen capture) ----------
  - ---------- selftest ----------

**Key Concepts:** SHA, MANIFEST, NOT, HERE, SNAP, PORTAL, FYS, CHECKED, WINDOW, KEYS

**Content Summary:**
- source_format: py - text_sha256: 188e21a072c1ccb9663a6375c1e4d03f07ab327e6d08d45fe7f2cb0a6e3b6689
#!/usr/bin/env python3 """ reproduce_paper3.py -- Provenance Integrity for Public Open Data (Bayyinah Paper 3).
Reproduces four provenance-integrity checks against the frozen capture: 1. Provenance classification and community-vs-official divergence. 2. Snapshot integrity (SHA-256 of the frozen capture vs MANIFEST). 3. Declared-vs-actual freshness (row-level :created_at postdating the reporting period). 4. Schema divergence (served field inventory per dataset).

---

### R0486 -- reproduce_procurement.py — reproduce_procurement.py -- NYC Procurement Concentration and Recoverable Savings (Bayyinah).
- **Date:** 2024
- **Source:** reproduce_procurement.py
- **Size:** 235 lines, 11,705 chars
- **SHA-256:** `c6b57211210a6ab1...`

**Structure:**
  - !/usr/bin/env python3
  - ---- expected values (independently reproduced; a mismatch is a finding) ----
  - Note: Negotiated total below is the sum of per-vendor values pre-rounded to 2 decimals
  - ($3,865,895,209.67); the raw Appendix 1 / CSV TOTAL sum is $3,865,895,209.68 (1-cent
  - rounding artifact, within the $1 tolerance; every headline figure rounds identically).
  - official FY25 Table 7 subgroup totals (Comptroller Annual Summary Contracts Report)
  - MTA FY2024 cross-check constants, carried from converged AllocationAsymmetry (DOI 10.5281/zenodo.21445552)
  - perturb each expected value; confirm the checker would flag it
  - savings perturbation

**Key Concepts:** NYC, CSV, MTA, MTA FY, TOTAL, HERE, MANIFEST, CSV TOTAL, EXPECT, NEW YORK CITY ECONOMIC DEVELOPMENT CORPORATION

**Content Summary:**
- source_format: py - text_sha256: c6b57211210a6ab164ac3c2f4479045ed83fd4c5cdfba4ad00fa686ab53e21fd
#!/usr/bin/env python3 """ reproduce_procurement.py -- NYC Procurement Concentration and Recoverable Savings (Bayyinah).
Reproduces, from the two frozen vendor CSVs, the paper's concentration figures (Table 2), the addressable-base and savings arithmetic (Table 3), and -- with --live -- re-pulls the MTA cross-check constants from data.ny.gov.

---

### R0418 -- Bayyinah: Public-Ledger Allocation and Asymmetric-Measure
- **Date:** 2024-12-31
- **Source:** Bayyinah_AllocationAsymmetry_Paper_v1.0.pdf
- **Size:** 375 lines, 24,799 chars
- **SHA-256:** `683db9bfce9eac26...`

**Structure:**
  - 1. Purpose and Scope
  - 2. The Method: Descriptive Count-versus-Dollar Asymmetry
  - 3. The Data-Interface Contract and the New York Adapter
  - 4. Worked Example: MTA FY2024 Procurement Report
  - 4.0 Naming the estimand, and a stock-versus-flow disclosure
  - 4.1 Process composition (descriptive; no compliance claim)
  - 4.2 MWBE prime-vendor count-versus-dollar asymmetry (descriptive)
  - 4.3 Vendor concentration (face-value stock)
  - 4.4 What the method emits, and what it refuses
  - 5. Portability
  - 6. Limitations
  - 7. Provenance and Verification
  - 8. Data Availability and Reproduction

**Key Concepts:** MTA, DOI, MWBE

**Content Summary:**
- source_format: pdf - text_sha256: 683db9bfce9eac26c474b3d307e82501a04cb8dceca61485a0968ce998d43e43
Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits A Descriptive Count-versus-Dollar Asymmetry in Public-Authority Procurement, with a Reproducible Worked Example on New York MTA Data Bilal Syed Arfeen (BayyinahEnterprise), with collaborative analytical assistance from Claude (Anthropic). DOI:
10.5281/zenodo.21445556. Version 1.0, the canonical converged release: the two-consecutivequalifying-pass convergence gate under Audit Framework v3.0 Standing Rule 7 was met on the identical v0.7 substance (F-AA-R8 and F-AA-R9, three qualifying non-producer members, executed reproduction, zero critical and zero high in both rounds). The full round history and the honestly-recorded conver...

---

### R0449 -- F-AM-R1 Audit Report — Bayyinah al-Amāna: Provenance Integrity for Public Open Data (v0.1)
- **Date:** 2024-12-31
- **Source:** F-AM-R1_claude_advisory.md
- **Size:** 274 lines, 19,703 chars
- **SHA-256:** `a8407db44bea85e6...`

**Structure:**
  - F-AM-R1 Audit Report — Bayyinah al-Amāna: Provenance Integrity for Public Open Data (v0.1)
  -   1. Identity, lineage, qualifying status, and no-prior-state attestation
  -   2. Execution status per step (real, unedited outputs)
  -     Step 1 — `python3 reproduce_paper3.py` (offline) — **PASS**, exit 0
  -     Step 2 — `python3 reproduce_paper3.py --selftest` — **PASS**, exit 0
  -     Step 3 — `python3 reproduce_paper3.py --live` — **PASS**, exit 0
  -     Step 4 — Independent recompute with my own code — **PASS**
  - !/usr/bin/env python3
  - (gather + a/b/c/d sections — full file in repro/independent_recompute_opus.py)
  -     Step 5 — Data-interface contract — **PASS**
  -     Step 6 — Adversarial mutation test — **PASS** (comparator-nonzero on mutated-but-rehashed capture)
  -   3. Findings (six-element F-AM-R1 format)
  -     F-AM-R1-001 · INFO · Reader note §5.2 (and Abstract, Tier-2 definition §3), term "wholesale republish"
  -     F-AM-R1-002 · INFO · Reader note §5.1 / §5.4, cross-dataset `sum(contract_amount)` comparability
  -     F-AM-R1-003 · INFO · Refusal boundary — held (affirmative finding)

**Key Concepts:** ADVISORY, ONLY, MEMBER, INSTRUCTIONS, DOI, PASS, MTA, DIVERGENT, SHA, WHOLESALE

**Content Summary:**
- source_format: md - text_sha256: a8407db44bea85e69d214614483d6ff61c32fc80a6a05b04dca750abe8e58771
# F-AM-R1 Audit Report — Bayyinah al-Amāna: Provenance Integrity for Public Open Data (v0.1)
## 1. Identity, lineage, qualifying status, and no-prior-state attestation

---

### R0450 -- Audit Report: F-AM-R1
- **Date:** 2024-12-31
- **Source:** F-AM-R1_gemini31.md
- **Size:** 409 lines, 15,522 chars
- **SHA-256:** `93fa53ddbd061641...`

**Structure:**
  - Audit Report: F-AM-R1
  -   1. Member Identity, Lineage, and Qualifying Status
  -   2. Execution Status
  - Step 1: Reproduce package offline
  - Step 2: Selftest
  - Step 3: Live Re-pull
  - Step 4: Independent Recompute
  - 1. Provenance and schema
  - 2. Year queries
  - Step 5: Data-Interface Contract
  - Step 6: Adversarial Mutation Test
  -   3. Findings
  -   4. Verdict
  - PASS
  -   Addendum — verbatim outputs

**Key Concepts:** QUALIFYING, SUCCESS, MTA, DIVERGENT, SHA, WHOLESALE, REPUBLISH, HTTP, DRIFT, MANIFEST

**Content Summary:**
- source_format: md - text_sha256: 93fa53ddbd061641730f0f25fad245589b55a1633d6b8b81171fe7feb471606f
## 1. Member Identity, Lineage, and Qualifying Status - **Identity**: Gemini 3.1 Pro - **Lineage**: Google - **Qualifying Status**: QUALIFYING (non-producer). My verdict counts toward convergence. - **Attestation**: I attest that I am a fresh, memoryless instance. I have not read, listed, or opened any sibling directory under `/home/user/workspace/audit/` (including `gpt_5_5`, `claude_opus_4_8`, or `inspect/`).
**Step 1: Reproduce package offline** Status: SUCCESS ``` [integrity] capture retrieved_utc: 2026-07-19T22:07:28Z

---

### R0451 -- F-AM-R1 Audit Council Report — GPT 5.5 (Qualifying)
- **Date:** 2024-12-31
- **Source:** F-AM-R1_gpt55.md
- **Size:** 352 lines, 22,530 chars
- **SHA-256:** `1f90f52cb13ebcbb...`

**Structure:**
  - F-AM-R1 Audit Council Report — GPT 5.5 (Qualifying)
  -   1. Identity, lineage, qualifying status, and no-prior-state attestation
  -   2. Execution status per mandatory step, with pasted real outputs
  -     Step 1 — Offline reproduction: `python3 reproduce_paper3.py`
  -     Step 2 — Self-test: `python3 reproduce_paper3.py --selftest`
  -     Step 3 — Live reproduction: `python3 reproduce_paper3.py --live`
  -     Step 4 — Independent recompute with my own code and live queries
  - !/usr/bin/env python3
  - Pull metadata and per-window aggregates independently.
  -     Step 5 — Data-interface contract
  -     Step 6 — Adversarial mutation test
  -   3. Audit findings — F-AM-R1 namespace
  -     F-AM-R1-001
  -     F-AM-R1-002
  -     F-AM-R1-003

**Key Concepts:** GPT, QUALIFYING, EXECUTED, MTA, DIVERGENT, SHA, WHOLESALE, REPUBLISH, EXIT, CODE

**Content Summary:**
- source_format: md - text_sha256: 1f90f52cb13ebcbbe47e7dcec42bf76fe9f6d61b9f3aee172c52c1fb9992f2e6
# F-AM-R1 Audit Council Report — GPT 5.5 (Qualifying)
## 1. Identity, lineage, qualifying status, and no-prior-state attestation

---

### R0453 -- F-AM-R2 Audit Report — Claude Opus 4.8 (ADVISORY / NON-CONVERGENCE-BEARING)
- **Date:** 2024-12-31
- **Source:** F-AM-R2_claude_advisory.md
- **Size:** 286 lines, 21,698 chars
- **SHA-256:** `2278d01ab8745f3f...`

**Structure:**
  - F-AM-R2 Audit Report — Claude Opus 4.8 (ADVISORY / NON-CONVERGENCE-BEARING)
  -   Attestation
  -   Executed reproduction — six steps (real, unedited outputs)
  -     Step 1 — `python3 reproduce_paper3.py` (offline), exit code 0
  -     Step 2 — `python3 reproduce_paper3.py --selftest` (42 perturbations), exit code 0
  -     Step 3 — `python3 reproduce_paper3.py --live` (re-pull data.ny.gov), exit code 0
  -     Step 4 — Independent recompute with my OWN code (did NOT import `reproduce_paper3.py`), exit code 0
  -     Step 5 — Data-interface facts (real output)
  -     Step 6 — Adversarial: mutate one captured value, re-hash MANIFEST so hash passes, confirm DRIFT (real output)
  -   Regression checks on absorbed R1 findings (loci cited)
  -   Status-propagation check (version / counter / round count)
  -   Findings (six-element format; namespace F-AM-R2)
  - F-AM-R2-S-001 — LOW
  - F-AM-R2-S-002 — INFO
  - F-AM-R2-S-003 — INFO (affirmative)

**Key Concepts:** ADVISORY, NON, CONVERGENCE, BEARING, PRODUCING, EXCLUDED, API, MANIFEST, DOI, MTA

**Content Summary:**
- source_format: md - text_sha256: 2278d01ab8745f3fcf5e03c97e2f589ba9d0c2e165eedb4078e041b1b0b35240
# F-AM-R2 Audit Report — Claude Opus 4.8 (ADVISORY / NON-CONVERGENCE-BEARING)
**Namespace:** F-AM-R2 **Member identity:** Claude Opus 4.8 (Anthropic) **Lineage:** Anthropic — the **PRODUCING** lineage. Per Operating Condition 5 (producer-lineage quarantine), this member is **advisory-only and EXCLUDED from the convergence-bearing synthesized verdict.** **Execution environment:** Perplexity Computer (code-execution + network to public `data.ny.gov` Socrata API). **Package used:** the extracted copy in my own working directory `/home/user/workspace/audit_r2/claude_opus_4_8/` (`reproduce_paper3.py`, `snapshot/provenance_capture.json`, `snapshot/MANIFEST.json`). Not recovered from any DOI or ext...

---

### R0454 -- Bayyinah al-Amāna Provenance-Integrity Audit (Round 2)
- **Date:** 2024-12-31
- **Source:** F-AM-R2_gemini31.md
- **Size:** 216 lines, 10,961 chars
- **SHA-256:** `01d8a5769f5fbee2...`

**Structure:**
  - Bayyinah al-Amāna Provenance-Integrity Audit (Round 2)
  -   Attestation
  -   Executed Steps
  -     Step 1: Baseline Offline Reproduction
  - Output:
  -     Step 2: Comparator Selftest
  - Output:
  -     Step 3: Live Verification
  - Output:
  -     Step 4: Independent Recompute
  - Code Executed:
  - Output:
  -     Step 5: Data-Interface Facts
  -     Step 6: Adversarial Testing
  - Methodology:

**Key Concepts:** QUALIFYING, MTA, DIVERGENT, SHA, POST, CLOSE, BATCH, Step 1, Step 2, Step 3

**Content Summary:**
- source_format: md - text_sha256: 01d8a5769f5fbee29f00df8a47d614949b4869247ea6cabc769ca53b0b2c2dad
# Bayyinah al-Amāna Provenance-Integrity Audit (Round 2) **Auditor**: Gemini 3.1 Pro (Google) - QUALIFYING **Namespace**: F-AM-R2
## Attestation "Fresh, memoryless instance; did not access any other member's work; worked only from my own directory copy."

---

### R0455 -- F-AM-R2 audit report (GPT 5.4)
- **Date:** 2024-12-31
- **Source:** F-AM-R2_gpt54.md
- **Size:** 470 lines, 24,632 chars
- **SHA-256:** `ba0f239be1b53a4a...`

**Structure:**
  - F-AM-R2 audit report (GPT 5.4)
  -   Scope and execution-status note
  -   Step 1
  -   Step 2
  -   Step 3
  -   Step 4 -- independent recompute with separate code
  - !/usr/bin/env python3
  -   Step 5 -- data-interface facts
  -   Step 6 -- adversarial mutate-and-rehash test
  -   Regression checks
  -     F-AM-R1-S-001 (republish over-claim)
  -     F-AM-R1-S-002 (provenance wording)
  -     F-AM-R1-S-003 (row-timestamp signal scope)
  -   Status-propagation check
  -   Findings (artifact-level)

**Key Concepts:** GPT, INCOMPLETE, HIGH, EXIT, CODE, MTA, DIVERGENT, SHA, POST, CLOSE

**Content Summary:**
- source_format: md - text_sha256: ba0f239be1b53a4abd48add115c2ac90c85ce1c820b5fb74ce3c128b99a8434e
Model: GPT 5.4 (OpenAI), qualifying non-producer auditor.
Working directory used for the audit: `/home/user/workspace/audit_r2/gpt_5_4/`.

---

### R0456 -- F-AM-R2 Audit Report — GPT 5.5 qualifying auditor
- **Date:** 2024-12-31
- **Source:** F-AM-R2_gpt55.md
- **Size:** 380 lines, 23,624 chars
- **SHA-256:** `3d719d3fcad4f139...`

**Structure:**
  - F-AM-R2 Audit Report — GPT 5.5 qualifying auditor
  -   Scope and attestation
  -   Verdict
  -   Step 1 — Offline reproduction
  -   Step 2 — Self-test
  -   Step 3 — Live reproduction
  -   Step 4 — Independent recompute, with my own code
  - !/usr/bin/env python3
  -   Step 5 — Data-interface facts
  -   Step 6 — Adversarial mutate-and-rehash
  -   Regression checks
  -     F-AM-R1-S-001
  -     F-AM-R1-S-002
  -     F-AM-R1-S-003
  -   Status-propagation check

**Key Concepts:** GPT, PASS, CRITICAL, HIGH, MEDIUM, LOW, MTA, DIVERGENT, SHA, POST

**Content Summary:**
- source_format: md - text_sha256: 3d719d3fcad4f139d0c9a4090f55155b1098828ea173f8791307eeb2a04327f8
# F-AM-R2 Audit Report — GPT 5.5 qualifying auditor
Fresh, memoryless instance; did not access any other member's work; worked only from my own directory copy: `/home/user/workspace/audit_r2/gpt_5_5/`.

---

### R0458 -- Audit Report: F-AM-R3-gemini31pro
- **Date:** 2024-12-31
- **Source:** F-AM-R3_gemini31.md
- **Size:** 287 lines, 15,945 chars
- **SHA-256:** `ebae8308c78714ed...`

**Structure:**
  - Audit Report: F-AM-R3-gemini31pro
  -   1. Member Identity
  -   2. Attestations and Command Log
  - Command Log Summary:
  -   3. Execution Status
  -     Step 1: `python3 repro/reproduce_paper3.py`
  -     Step 2: `python3 repro/reproduce_paper3.py --selftest`
  -     Step 3: `python3 repro/reproduce_paper3.py --live`
  -     Step 4: Independent Recompute
  -     Step 5: DATA-INTERFACE Facts
  -     Step 6: ADVERSARIAL Mutate and Rehash
  -   4. Audit-Scope Confirmations
  -   5. Regression Confirmations (F-AM-R2-001/002/003)
  -   6. Status-Propagation Check Result
  -   7. Findings

**Key Concepts:** QUALIFYING, GPT, SODA, MTA, DIVERGENT, SHA, POST, CLOSE, BATCH, Step 1

**Content Summary:**
- source_format: md - text_sha256: ebae8308c78714ed02a41235401d0e006373d329bc9f28e9e53e8f276897c131
## 1. Member Identity - Member: Gemini 3.1 Pro (model lineage: Google) - Role: QUALIFYING (non-producer lineage) - New relative to R1/R2 clean pair (GPT 5.5, Gemini 3.1 Pro)? NO — Gemini 3.1 Pro was in the R1/R2 clean qualifying pair
> I attest that I operated only within /home/user/workspace/R3-gemini31pro, did not list, read, search, or traverse any sibling, orchestrator, or workspace-root directory, and did not access another member's work.

---

### R0459 -- F-AM-R3 Audit Report — GPT 5.4 (OpenAI)
- **Date:** 2024-12-31
- **Source:** F-AM-R3_gpt54.md
- **Size:** 423 lines, 24,679 chars
- **SHA-256:** `1ee7c06652f4599e...`

**Structure:**
  - F-AM-R3 Audit Report — GPT 5.4 (OpenAI)
  -   1. Member identity, lineage, new-relative-to-R1/R2 flag, role
  -   2. Isolation attestation + no-prior-state attestation + command log summary
  -   3. Execution status for each of the six steps
  -     Step 1 — `python3 repro/reproduce_paper3.py`
  -     Step 2 — `python3 repro/reproduce_paper3.py --selftest`
  -     Step 3 — `python3 repro/reproduce_paper3.py --live`
  -     Step 4 — Independent recompute with fresh urllib code
  - !/usr/bin/env python3
  - Independent recompute using fresh urllib code
  - Cross-dataset divergence summary
  -     Step 5 — Independent data-interface confirmation (`revisions.json` HTTP codes; system columns queryable)
  - Revisions endpoint checks
  - System column query checks
  -     Step 6 — Adversarial mutate, re-hash, and comparator DRIFT check

**Key Concepts:** GPT, YES, QUALIFYING, HTTPS, SODA, COMPLETED, MTA, DIVERGENT, SHA, POST

**Content Summary:**
- source_format: md - text_sha256: 1ee7c06652f4599e51a39ca2e9a151b225d90ce11a28a0c169eca3777fb0942c
## 1. Member identity, lineage, new-relative-to-R1/R2 flag, role
- Member: GPT 5.4 - Model lineage: OpenAI - New relative to the R1/R2 clean qualifying pair (GPT 5.5, Gemini 3.1 Pro): YES - Role: QUALIFYING (non-producer lineage; rotated-in member for this confirming round)

---

### R0462 -- Audit Report: Procurement Concentration and Recoverable Competitive Savings in New York City Contracting (v0.3)
- **Date:** 2025
- **Source:** F-PC-R1_gemini31.md
- **Size:** 168 lines, 9,978 chars
- **SHA-256:** `427d0bd3a815c760...`

**Structure:**
  - Audit Report: Procurement Concentration and Recoverable Competitive Savings in New York City Contracting (v0.3)
  -   1. Reproduction Outputs
  -     Step 1: Baseline Reproduction Script
  -     Step 2: Selftest Mode
  -     Step 3: Live MTA Data Reproduction
  -     Step 4: Independent Clean Recompute
  -     Step 5: Adversarial Trap Recompute
  -   2. Findings Table
  -   3. Assessment of "Two Points to Press Hardest"
  - 1. Negotiated Acquisition Reconciliation ($192.96M Gap)
  - 2. Conditional Framing of Savings Estimate
  -   4. Tier 3 Boundaries

**Key Concepts:** INDEPENDENT, FRESH, MEMORYLESS, PASS, ONE, NYCEDC, MTA, DOI, MTA FY, CLEAN INDEPENDENT RECOMPUTE

**Content Summary:**
- source_format: md - text_sha256: 427d0bd3a815c760ecc281057b8bf5696790b3022313739fe90ec6dfa5fdc853
# Audit Report: Procurement Concentration and Recoverable Competitive Savings in New York City Contracting (v0.3)
**Identity & Lineage:** Gemini 3.1 Pro (Google). Lineage: Google. **Attestation:** I am an INDEPENDENT, FRESH, MEMORYLESS audit instance on a Model Council. I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, NO carryover from any earlier Bayyinah round, and NO access to any other council member's work. **Execution Status:** Executed (All 5 mandatory steps completed successfully). **Verdict:** PASS (Qualifying member) **Consecutive Qualifying-PASS Count Outcome:** ONE (First step toward convergence).

---

### R0463 -- Model Council Audit Report: GPT 5.4
- **Date:** 2025
- **Source:** F-PC-R1_gpt54.md
- **Size:** 148 lines, 12,971 chars
- **SHA-256:** `13f06e9ebc774af8...`

**Structure:**
  - Model Council Audit Report: GPT 5.4
  -   Identity and attestation
  -   Execution status
  -   Mandatory execution outputs
  -     Step 1: `python3 reproduce_procurement.py`
  -     Step 2: `python3 reproduce_procurement.py --selftest`
  -     Step 3: `python3 reproduce_procurement.py --live`
  -     Step 4: independent recompute with separate code
  -     Step 5: adversarial trap check including the trailing rows
  -   Assessment
  -   Findings table
  -   Verdict

**Key Concepts:** GPT, INDEPENDENT, FRESH, MEMORYLESS, NYCEDC, MTA, DOI, MTA FY, TOTAL, URL

**Content Summary:**
- source_format: md - text_sha256: 13f06e9ebc774af86b8fc9b82d54b7317c7ad9fd3a0cd5cc6e94526aa90a50d9
- **Model:** GPT 5.4 - **Lineage:** OpenAI - **Qualifying status:** Qualifying member for Round 1 (non-Claude, non-producer lineage). - **No-history/no-memory attestation:** "I am an INDEPENDENT, FRESH, MEMORYLESS audit instance on a Model Council. I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, NO carryover from any earlier Bayyinah round, and NO access to any other council member's work."
**Executed.** I read the attached brief and paper in the workspace and executed all five mandatory steps against the attached package ([audit brief](file:///home/user/workspace/council/gpt54/brief.md)), ([paper v0.3](file:///home/user/workspace/council/gpt54/paper_v0.3.m...

---

### R0464 -- Model Council Round-1 Audit Report - GPT 5.5
- **Date:** 2025
- **Source:** F-PC-R1_gpt55.md
- **Size:** 244 lines, 15,839 chars
- **SHA-256:** `91f6dd2e20d71536...`

**Structure:**
  - Model Council Round-1 Audit Report - GPT 5.5
  -   Identity and attestation
  -   Mandatory execution outputs
  -     Step 1 - `cd /home/user/workspace/council/gpt55 && python3 reproduce_procurement.py`
  -     Step 2 - `python3 reproduce_procurement.py --selftest`
  -     Step 3 - `python3 reproduce_procurement.py --live`
  -     Step 4 - independent recompute with my own code
  -     Step 5 - adversarial trap check
  -   Appendix 1 access and reconciliation attempt
  -   Savings framing, Tier 3 boundary, house style, and consistency assessment
  -   Findings table
  -   Verdict

**Key Concepts:** GPT, QUALIFYING, INDEPENDENT, FRESH, MEMORYLESS, README, MANIFEST, NYCEDC, MTA, DOI

**Content Summary:**
- source_format: md - text_sha256: 91f6dd2e20d71536307a625a61736250f8c76796cb72be51f05c5b11cf3cf4eb
Identity: GPT 5.5 (OpenAI). Lineage: OpenAI. Qualifying status: QUALIFYING member, non-Claude and non-producer lineage.
No-history/no-memory attestation: I am an INDEPENDENT, FRESH, MEMORYLESS audit instance on a Model Council. I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, NO carryover from any earlier Bayyinah round, and NO access to any other council member's work.

---

### R0466 -- (a) Identity, lineage, and attestation
- **Date:** 2025
- **Source:** F-PC-R2_claude_advisory.md
- **Size:** 283 lines, 19,685 chars
- **SHA-256:** `78a36ce00e370c8d...`

**Structure:**
  - Model Council Report — Round 2 Cross-Instance Audit of "Procurement Concentration and Potentially Recoverable Competitive Savings in New York City Contracting" (v0.4)
  -   (a) Identity, lineage, and attestation
  -   (b) Execution status — real, unedited outputs
  -     Step 1 — `python3 reproduce_procurement.py` (exit 0, every line OK)
  -     Step 2 — `python3 reproduce_procurement.py --selftest` (14 detected, 0 missed)
  -     Step 3 — `python3 reproduce_procurement.py --live` (live MTA re-pull, no drift)
  -     Step 4 — Independent recompute (my own code, no imports from the supplied script)
  -     Step 5 — Adversarial trap (include TOTAL + footnote rows)
  -     Step 6 — Appendix 1 reconciliation (independent)
  -     Section 5.0 basis-effect arithmetic (the Round-1 HIGH locus) — recomputed independently
  -     Consolidated Tier-1 cross-check (my values vs brief)
  -   (c) Findings (six-element format; namespace F-PC-R2)
  -     Round-1 fix verifications
  - F-PC-R2-001 — Section 5.0 basis note (was F-PC-R1-001, HIGH)
  - 1. Identifier: F-PC-R2-001

**Key Concepts:** PRODUCER, ADVISORY ONLY, ADVISORY, PASS, NYC, MTA, NYCEDC, DOI, EXIT CODE, SHA

**Content Summary:**
- source_format: md - text_sha256: 78a36ce00e370c8d5a63a87ccbf4862795775acc16dc3c5ecc2afeabf411c2d3
# Model Council Report — Round 2 Cross-Instance Audit of "Procurement Concentration and Potentially Recoverable Competitive Savings in New York City Contracting" (v0.4)
- **Member:** Claude Opus 4.8 - **Lineage:** Anthropic (Claude family) — this is the **PRODUCER lineage** of the paper under audit. - **Role / verdict weight:** **ADVISORY ONLY.** Under the brief's producer-lineage quarantine (Operating Condition 5) and Audit Framework v3.0 Standing Rule 7, a Claude-family member is excluded from the convergence-bearing verdict. My verdict below is explicitly marked ADVISORY and **does not bear on the consecutive qualifying-PASS count.**

---

### R0468 -- Round-2 Audit Council Report -- GPT 5.5 (Qualifying)
- **Date:** 2025
- **Source:** F-PC-R2_gpt55.md
- **Size:** 235 lines, 17,338 chars
- **SHA-256:** `64f60d8ff2bacd8a...`

**Structure:**
  - Round-2 Audit Council Report -- GPT 5.5 (Qualifying)
  -   Identity, lineage, isolation attestation
  -   Executive conclusion
  -   Mandatory execution status and pasted outputs
  -     1. Supplied reproduction: `python3 reproduce_procurement.py`
  -     2. Supplied selftest: `python3 reproduce_procurement.py --selftest`
  -     3. Supplied live MTA pull: `python3 reproduce_procurement.py --live`
  -     4-6. Independent recompute, adversarial trap, and Appendix 1 reconciliation
  -   Round-1 fix verification
  -     F-PC-R1-001 -- Section 5.0 basis note
  -     F-PC-R1-002 -- reconciliation/accessibility
  -     F-PC-R1-003 -- savings breadth and screened framing
  -     F-PC-R1-004 -- abstract/body headline
  -     F-PC-R1-005 -- title and Table 3 label
  -   Tier-1 deterministic checks

**Key Concepts:** GPT, MTA, PASS, MEDIUM, CRITICAL, HIGH, ZERO, ONE, NYCEDC, DOI

**Content Summary:**
- source_format: md - text_sha256: 64f60d8ff2bacd8a3cac712d86667c00ebe334811cf589244707cdaf3538052d
# Round-2 Audit Council Report -- GPT 5.5 (Qualifying)
- Member identity: GPT 5.5. - Lineage: OpenAI GPT family. - Qualifying status: qualifying non-producer-lineage member. The producer lineage identified in the brief is Claude/Anthropic; this member is not Claude-family. - Verbatim no-history/no-memory attestation: I have NO chat history, NO memory, NO saved skills, NO prior-conversation context, and NO access to any other member's work. - Scope discipline: I judged only the Round 2 brief, the v0.4 proposal, the supplied reproduction package, executed code, the public Appendix 1 Excel at https://comptroller.nyc.gov/wp-content/uploads/2025/10/Appendix-1-Parent-Contracts.xlsx, and the live d...

---

### R0469 -- Model Council Synthesis — Round 2 (F-PC-R2)
- **Date:** 2025
- **Source:** F-PC-R2_synthesis.md
- **Size:** 136 lines, 13,341 chars
- **SHA-256:** `1a534c088eea4f32...`

**Structure:**
  - Model Council Synthesis — Round 2 (F-PC-R2)
  -   Cross-Instance Audit of "Procurement Concentration and Potentially Recoverable Competitive Savings in New York City Contracting" (v0.4)
  -   (a) Per-member report
  -     What each member executed (real outputs, independently confirmed by synthesizer)
  -   (b) Qualifying-members determination
  -   (c) Synthesized verdict over qualifying members only
  - SYNTHESIZED VERDICT: PASS.
  -   Council agreement and disagreement
  -     Where the qualifying members agree
  -     Where the qualifying members diverge
  -     Synthesizer-unique finding (not raised by any member)
  -     Advisory member's notable extra finding
  -   Tier summary
  -   House style and internal consistency
  -   Final outcome

**Key Concepts:** GPT, CRIT, HIGH, MED, LOW, INFO, PASS, ADVISORY, MTA, SHA

**Content Summary:**
- source_format: md - text_sha256: 1a534c088eea4f3293f06c56e81d5a013e43922626d1821dde86a3af488517b7
# Model Council Synthesis — Round 2 (F-PC-R2) ## Cross-Instance Audit of "Procurement Concentration and Potentially Recoverable Competitive Savings in New York City Contracting" (v0.4)
**Council convened:** GPT 5.5 (OpenAI), Gemini 3.1 Pro (Google), Claude Opus 4.8 (Anthropic, advisory). **Synthesizer (this document's author):** the orchestrating Computer instance, which also executed the full reproduction independently before dispatch and re-verified every member's pasted output against its own code. The synthesizer is producer-lineage (Claude) and therefore does not itself count toward convergence; the verdict below is synthesized **over qualifying members only**.

---

### R0473 -- F-PC-R3 Model Council Audit -- Synthesized Verdict
- **Date:** 2025
- **Source:** F-PC-R3_synthesis.md
- **Size:** 160 lines, 14,734 chars
- **SHA-256:** `6a634046ab9f76ef...`

**Structure:**
  - F-PC-R3 Model Council Audit -- Synthesized Verdict
  -   1. Council membership and qualifying status
  -     Both passes on record (independence of the two consecutive passes)
  -   2. Synthesized verdict (qualifying members only)
  - PASS.
  -     Where members agree (Tier-1, byte-deterministic)
  -     Round-2 fix regression check (all three members, independently confirmed landed)
  -     Where members disagree (severity/emphasis only -- not on the verdict)
  -     Unique discoveries
  -   3. Findings (F-PC-R3 namespace, six-element format)
  -     F-PC-R3-001
  -     F-PC-R3-002
  -   4. Tier assessment (synthesized)
  -   5. Convergence determination and count outcome
  -   6. Per-member execution summary

**Key Concepts:** GPT, PASS, CRITICAL, HIGH, AND, CSV SHA, NYCEDC, MTA FY, TOTAL, ASCR

**Content Summary:**
- source_format: md - text_sha256: 6a634046ab9f76efa1a3383c8ec73b0f496afbe1da4c1ec1f8d523cd1424be01
# F-PC-R3 Model Council Audit -- Synthesized Verdict
**Paper audited:** "Procurement Concentration and Potentially Recoverable Competitive Savings in New York City Contracting" (v0.5) **Round:** F-PC-R3 (second consecutive-pass attempt), Audit Framework v3.0 **Producing lineage:** Claude / Anthropic (quarantined -- advisory only, excluded from the verdict) **Synthesizer:** Bayyinah Enterprise orchestrator (Computer environment, code-execution + web)

---

### R0420 -- Bayyinah at-Taʿlīm
- **Date:** 2025-05
- **Source:** Bayyinah_at-Taleem_Paper_rc10_DOIcorrected.pdf
- **Size:** 555 lines, 32,234 chars
- **SHA-256:** `f7811ccdb31f598e...`

**Structure:**
  - 1. Purpose and Scope
  - 2. The Governing Divergence: Declared Fairness versus Operative Fairness
  - 3. Tier Discipline: What Can and Cannot Be Verified
  - 4. Mechanisms
  - 4.1 Primary and Secondary (K-12)
  - 0.14 SD, a 3.5-fold gap).
  - 4.2 Undergraduate
  - 4.3 Graduate and Masters
  - 4.4 Worked Example: NYC Fair Student Funding
  - 5. Limitations
  - 6. Provenance and Verification
  - 7. AI Contribution Statement
  - 8. Data Availability

**Key Concepts:** DOI, SHV, DOE

**Content Summary:**
- source_format: pdf - text_sha256: f7811ccdb31f598e51480b6778b267830d0a576de95f8f50a254743a6e0c2814
Bayyinah at-Taʿlīm Structural Honesty Verification for Educational Fairness Systems, from Primary Schooling to Graduate Research Bilal Syed Arfeen (BayyinahEnterprise), with collaborative analytical assistance from Claude (Anthropic). DOI:
10.5281/zenodo.21436486 . Companion to: Bayyinah at-Tartīb (Arfeen 2026, DOI 10.5281/zenodo.20070782); AlMutaffifīn (Arfeen 2026, DOI 10.5281/zenodo.19894724); Structural Honesty Verification: A New Frontier (Arfeen and Ashraf 2026, DOI 10.5281/zenodo.20131072). Audit trail, full version history, finding-by-finding provenance, and cross-vendor verification discipline for this paper are published separately in the Audit and Provenance Companion (see Proven...

---

### R0419 -- Bayyinah at-Taʿlīm -- Audit and Provenance Companion
- **Date:** 2025-05-29
- **Source:** Bayyinah_at-Taleem_AuditCompanion_rc10.pdf
- **Size:** 1314 lines, 100,440 chars
- **SHA-256:** `f4e1d1307df7afb4...`

**Structure:**
  - 0.288 SD for Nickow, Oreopoulos & Quan (2024) with an explicit note distinguishing it from the
  - 14.5. The README also carries an explicit note that the dataset's public-archive DOI is

**Key Concepts:** DOI, PMD, RESOLVED, PARTIALLY, ABSORBED, OPEN, AND, RETAINED, CRITICAL, HIGH

**Content Summary:**
- source_format: pdf - text_sha256: f4e1d1307df7afb4e9f41d69867ad0387b89b481d7fb524c819c42af2a7d4148
Bayyinah at-Taʿlīm -- Audit and Provenance Companion Companion to: Bayyinah at-Taʿlīm: Structural Honesty Verification for Educational Fairness Systems, from Primary Schooling to Graduate Research (the reader-facing paper). DOI: 10.5281/zenodo.21436486 . Reader-facing paper: DOI 10.5281/zenodo.21436484 . Prepared under BayyinahEnterprise audit methodology (PMD v1.2, Audit Framework v3.0). Mirrors paper state v1.0-rc10 (four rounds recorded; convergence-counting decision pending owner). Human authorship and copyright to be assigned by project lead (Bilal Syed Arfeen); Claude (Anthropic) credited as collaborative research tool.
About this companion This document is the append-only audit trail...

---

### R0421 -- Bayyinah al-Amāna: Provenance Integrity for Public Open Data -Audit and Provenance Companion
- **Date:** 2025-12-01
- **Source:** Bayyinah_ProvenanceIntegrity_Ledger_v1.0.pdf
- **Size:** 321 lines, 22,313 chars
- **SHA-256:** `23fe612352963b40...`

**Key Concepts:** DOI, PMD, PASS, THREE, UPPERCASE, CRITICAL, HIGH, MEDIUM, LOW, INFO

**Content Summary:**
- source_format: pdf - text_sha256: 23fe612352963b4046316055f43373f83dfdd6dcbaf158e346081fa84ae19f56
Bayyinah al-Amāna: Provenance Integrity for Public Open Data -Audit and Provenance Companion Companion to: Bayyinah al-Amāna: Provenance Integrity for Public Open Data (the readerfacing note, v1.0; DOI 10.5281/zenodo.21446613). This ledger: DOI 10.5281/zenodo.21446618. Governed by: Bayyinah, Portable Structural Honesty Verification for Public-Service Institutions (the framework paper). Prepared under BayyinahEnterprise audit methodology (PMD v1.2, Audit Framework v3.0). Mirrors note state v1.0, the canonical converged release (three consecutive qualifying passes, F-AM-R1/R2/R3; the consecutive qualifying-PASS count is THREE, the gate met and confirmed clean at F-AM-R3 with the rotation gap ...

---

## Cross-Paper Themes

**Recurring Concepts (appearing in multiple papers):**
  - mta: 18 papers
  - sha: 16 papers
  - doi: 14 papers
  - step 1: 14 papers
  - step 2: 14 papers
  - step 3: 14 papers
  - gpt: 13 papers
  - pass: 10 papers
  - divergent: 9 papers
  - manifest: 7 papers
  - code: 7 papers
  - mta fy: 7 papers
  - exit: 7 papers
  - qualifying: 7 papers
  - high: 7 papers
  - post: 6 papers
  - close: 6 papers
  - batch: 6 papers
  - critical: 6 papers
  - nycedc: 6 papers

**Date Range:** 2024 to 2025-12-01

**Source Formats:** md(17), pdf(4), py(4)

## Key Findings

(See per-paper summaries above for detailed findings per paper.)

## Connections to Other Sections

**Cross-references found:** bayyinah, furqan, shv

# Bismillah ir-Rahman ir-Rahim
