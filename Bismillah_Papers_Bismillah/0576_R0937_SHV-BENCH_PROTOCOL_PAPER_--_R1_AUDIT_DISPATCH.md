# Bismillah ir-Rahman ir-Rahim

# R0937 -- SHV-BENCH PROTOCOL PAPER -- R1 AUDIT DISPATCH

**Chronological Index:** 576 of 995  
**Date:** 2026-08-20  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S04_SB_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `3d086d0d4d5b7de22f6b434f74d56b2be5b49b89a61e0f713999e21f003377cb`  

---

## R0937 · SHV-BENCH PROTOCOL PAPER -- R1 AUDIT DISPATCH

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S04_SB_DISPATCH.txt
- source_format: txt
- text_sha256: 3d086d0d4d5b7de22f6b434f74d56b2be5b49b89a61e0f713999e21f003377cb

SHV-BENCH PROTOCOL PAPER -- R1 AUDIT DISPATCH
Seat S04 | Google Gemini 3.1 Pro | ADVISORY | Mode B | FRESH
Round R1 | 2026-08-20 | Dispatched by Bilal Syed Arfeen

================================================================
ROLE
================================================================

You are the ADVISORY seat. Your verdict is non-binding.
Your value is unique-finding surfacing and task corpus
verification. Also assess readability for a reviewer who has
not read the full Structural Honesty corpus.

================================================================
ARTIFACT
================================================================

SHV_BENCH_PROTOCOL.pdf (9 pages).
Companion: SHV_BENCH_TASK_CORPUS.csv (1,673 rows).

================================================================
ANALYTICAL LENS (your ml orientation)
================================================================

LENS: TASK CORPUS INTEGRITY + SHVVP CROSS-REFERENCE

Your primary job is to verify the task corpus and check whether
the protocol is consistent with the deposited SHVVP
preregistration.

TASK CORPUS VERIFICATION:

  (a) Open SHV_BENCH_TASK_CORPUS.csv. Count rows (excluding
      header). Does the count match Section 3.1's "1,673"?

  (b) Count unique values in the "vendor" column. Does it
      match Section 3.1's "278"?

  (c) For each of the 14 vulnerability classes in Section
      3.2's table, count the matching rows in the CSV's
      "vuln_class" column. Do the counts match the table?

  (d) Spot-check 5 CVE IDs from the CSV against the live
      CISA KEV catalog (https://www.cisa.gov/known-exploited-
      vulnerabilities-catalog). Do the entries exist? Do the
      vendor, product, and description match?

  (e) Check the "Unclassified" entries (493). Sample 10 and
      assess whether a reasonable keyword classification
      would have assigned them a class. Is 29.5% unclassified
      a quality concern?

  (f) Check the known_ransomware column. Does the count of
      "Known" entries match Section 3.1's "349 (20.9%)"?

  (g) Is the CSV safe? Does it contain any exploit code,
      weaponized payloads, or activation recipes? (It should
      contain only identifiers, vendor names, product names,
      vulnerability class labels, and dates.)

SHVVP CROSS-REFERENCE:

  (h) The SHVVP preregistration (DOI 10.5281/zenodo.21583202)
      defines Phase B. Does SHV-Bench's protocol match Phase
      B's design as described in the SHVVP? Specifically:
        - Pilot 160 / confirmatory 800 sessions?
        - 6 canaries?
        - Two-sided success criterion?
        - Mann-Whitney + BH-FDR + power >= 80%?

  (i) The rename from "CVE-Bench" to "SHV-Bench" -- does the
      paper change anything SUBSTANTIVE from the preregistered
      design, or is it a name-only change? If substantive
      changes exist, are they disclosed?

  (j) Does the paper correctly cite the SHVVP DOI?

DIFFICULTY TIERING ASSESSMENT:

  (k) Section 3.3 defines four tiers. Are the eligibility
      estimates (Tier 2: 400-600, Tier 3: 150-250, Tier 4:
      40-80) plausible given the KEV catalog's contents?

  (l) Are the time budgets (Tier 1: 15min, Tier 2: 30min,
      Tier 3: 60min) reasonable for the described tasks?

================================================================
READABILITY ASSESSMENT
================================================================

  (a) Can a reviewer unfamiliar with the Structural Honesty
      program understand the benchmark design?
  (b) Is the two-sided success criterion clear?
  (c) Is the statistical framework accessible to an ML
      researcher who is not a statistician?
  (d) Is the safety boundary (Section 7) clear about what
      will and will not be done?
  (e) Is the landscape positioning (Section 9) fair?

Rate each (a)-(e) as CLEAR, ADEQUATE, or UNCLEAR.

================================================================
AUDITOR STEPS (A-2, A-5, A-6, A-7 -- Mode B)
================================================================

A-2  CLAIM AUDIT
     Classify load-bearing sentences.

A-5  COVERAGE GAP ANALYSIS
     Report ASSERTED fraction.

A-6  CROSS-VERSION CONSISTENCY
     This IS your primary step -- the SHVVP cross-reference
     and task corpus verification above.

A-7  BLIND SPOT REPORT
     Name the single most likely error.

================================================================
PUBLICATION-POSTURE COMPLIANCE
================================================================

Same constraints as other seats. Each violation is a finding.

================================================================
FINDING FORMAT
================================================================

  ID:              F-S04-SB-NN
  SEVERITY:        CRITICAL | HIGH | MEDIUM | LOW
  LOCUS:           Section and paragraph, or CSV row/column
  SUBSTANCE:       What is wrong
  DISPOSITION:     OPEN
  CROSS-REFERENCE: Which source or verification item

================================================================
VERDICT FORMAT
================================================================

VERDICT: [PASS | CONDITIONAL PASS | HALT]
FINDING COUNT: [N]
TASK CORPUS: [per-item (a)-(g) VERIFIED / UNVERIFIED / FAILED]
SHVVP CROSS-REF: [per-item (h)-(j) CONSISTENT / INCONSISTENT]
TIERING: [per-item (k)-(l) PLAUSIBLE / IMPLAUSIBLE]
READABILITY: [per-item (a)-(e) CLEAR / ADEQUATE / UNCLEAR]
BLIND SPOT: [one sentence]

FINDINGS:
[all findings in six-element format]

SUMMARY: [one paragraph]

---

# Bismillah ir-Rahman ir-Rahim
