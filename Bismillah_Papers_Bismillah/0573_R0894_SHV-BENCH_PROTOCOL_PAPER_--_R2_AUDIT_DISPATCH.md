# Bismillah ir-Rahman ir-Rahim

# R0894 -- SHV-BENCH PROTOCOL PAPER -- R2 AUDIT DISPATCH

**Chronological Index:** 573 of 995  
**Date:** 2026-08-20  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** S02_SB_R2_DISPATCH.txt  
**Source Format:** txt  
**SHA-256:** `26239f1fdb39e3915d7e66927458438ed198315a74b299fff5c3242fb1686ae5`  

---

## R0894 · SHV-BENCH PROTOCOL PAPER -- R2 AUDIT DISPATCH

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: S02_SB_R2_DISPATCH.txt
- source_format: txt
- text_sha256: 26239f1fdb39e3915d7e66927458438ed198315a74b299fff5c3242fb1686ae5

SHV-BENCH PROTOCOL PAPER -- R2 AUDIT DISPATCH
Seat S02 | Moonshot Kimi K3 | CARRYING | Mode B | FRESH
Round R2 | 2026-08-20 | Dispatched by Bilal Syed Arfeen

================================================================
ROLE
================================================================

You are the CARRYING seat. Your verdict is binding.
This is R2: repair verification. R1 returned CONDITIONAL PASS
from this seat (10 findings: 1C 4H 4M 1L) and HALT from the
adversarial seat (25 findings: 2C 16H 5M). Fifteen mandatory
repairs were absorbed into the R2 build.

This is a FRESH instance. You have no R1 context beyond what
this dispatch provides.

================================================================
ARTIFACT
================================================================

SHV_BENCH_PROTOCOL_R2.pdf (11 pages).
Companion: SHV_BENCH_TASK_CORPUS_v2.csv (1,673 rows).
Publication_Posture_v0_1.txt.

================================================================
R1 FINDING REGISTER -- VERIFY EACH
================================================================

F-S02-SB-01 (CRITICAL): CSV had no CVSS column despite the
  paper claiming CVSS-enriched stratification.
  REPAIR: Paper no longer claims CVSS enrichment for
  stratification. Tier 2 stratification is by vulnerability
  class only. CSV v2 adds vulnerability_name,
  short_description, and cwes columns (CVSS was from NVD
  enrichment, not the CISA source -- the paper now uses only
  CISA-native fields).
  VERIFY: (a) Paper does not claim CVSS stratification.
  (b) CSV has vulnerability_name, short_description, cwes
  columns with zero nulls. (c) Tier 2 stratification in
  Section 3.4 uses vulnerability class, not CVSS.

F-S02-SB-02 (HIGH): vuln_name null on all rows; no description
  column; class labels non-derivable.
  REPAIR: CSV v2 has vulnerability_name (0 nulls) and
  short_description (0 nulls). The full keyword classifier
  is published in Section 3.2 (ordered keyword list).
  VERIFY: (a) vuln_name column populated (check 10 rows).
  (b) short_description populated (check 10 rows).
  (c) Keyword classifier in Section 3.2 is deterministic
  and reproducible. (d) Spot-check: apply the keyword list
  to 5 entries' descriptions and verify the class matches.

F-S02-SB-03 (HIGH): Scope checker unshipped, unversioned.
  REPAIR: Section 5.1 specifies a frozen scope schema (JSON
  per task), a deterministic scope checker with SHA-256
  frozen in the manifest, a validation suite (100 labeled
  actions, >= 95% accuracy), and a blinded manual adjudication
  protocol with inter-rater reliability >= kappa 0.80.
  VERIFY: (a) Scope schema format specified. (b) Checker
  versioning specified (SHA-256 in manifest). (c) Validation
  suite specified with accuracy threshold. (d) Manual review
  protocol specifies blinding, two reviewers + third for
  disagreements, and kappa threshold. (e) F-SB8 and F-SB9
  are the corresponding falsifiers.

F-S02-SB-04 (HIGH): F-SB7 required order data never collected.
  REPAIR: Section 2.2 specifies counterbalanced order
  (alternating blocks of 4, randomized within blocks, seed
  frozen), environment reset between conditions, and order
  recorded as metadata for every session.
  VERIFY: (a) Order counterbalancing specified. (b) Reset
  specified. (c) Order recording specified. (d) F-SB7 now
  references Section 2.2 for the recorded order data.

F-S02-SB-05 (HIGH): Paired design but unpaired MWU tests.
  REPAIR: E1 and E2 both use Wilcoxon signed-rank on per-task
  paired differences. Hodges-Lehmann estimator.
  VERIFY: (a) Section 6.2 specifies Wilcoxon signed-rank.
  (b) E1 and E2 in Section 6.1 use per-task paired
  differences. (c) No residual "Mann-Whitney" or "pooled
  median" in the primary test specification.

F-S02-SB-06 (MEDIUM): Noninferiority margin pilot-derived.
  REPAIR: Fixed delta = 0.05. Section 6.3 states: "This is a
  fixed margin, not derived from pilot data."
  VERIFY: (a) delta = 0.05 stated. (b) No pilot-derivation
  language. (c) The false SHVVP attribution is removed.

F-S02-SB-07 (MEDIUM): F-SB5/F-SB6 denominators unpinned.
  REPAIR: Both now specify "confirmatory tasks (pooled across
  tiers)" as the denominator.
  VERIFY: (a) F-SB5 says "confirmatory." (b) F-SB6 says
  "confirmatory." (c) Both say "pooled across tiers."

F-S02-SB-08 (MEDIUM): BH-FDR family size unstated.
  REPAIR: Section 6.2 states: "4 per-tier subgroup analyses
  for each primary metric. Family size: 4 tests per metric
  x 2 metrics = 8 tests total." Confirmatory expansion
  capped at N=800 with no expansion beyond.
  VERIFY: (a) Family size = 8 stated. (b) Maximum N = 800.
  (c) No open expansion provision.

F-S02-SB-09 (MEDIUM): Unclassified sampling rule missing.
  REPAIR: Section 3.4: "Unclassified entries are sampled
  proportionally within each tier but enter pooled analysis
  only (not per-class subgroups)."
  VERIFY: The rule is stated and the Unclassified exclusion
  from per-class subgroup analyses is explicit.

F-S02-SB-10 (LOW): Three uncovered claims.
  REPAIR: (i) Condition-environment equivalence -> F-SB11.
  (ii) Canary construct validity -> declared assumption.
  (iii) WSDS composite -> weights frozen at 0.25 each with
  explicit rubric table in Section 5.1.
  VERIFY: (a) F-SB11 exists and covers condition parity.
  (b) WSDS rubric table present. (c) Weights specified.

================================================================
R1 ADVERSARIAL FINDINGS -- VERIFY KEY REPAIRS
================================================================

F-S03-SB-01 (CRITICAL): False SHVVP continuity.
  REPAIR: Section 1.3 departure table (12 rows). Abstract
  says "NOT a rename or inheritance." Title changed to
  "Successor Protocol."
  VERIFY: (a) No residual "inherits" or "frozen in the
  SHVVP" applied to specific design elements. (b) Departure
  table covers all elements GPT flagged. (c) Title says
  "Successor." (d) Abstract says "NOT."

F-S03-SB-02 (CRITICAL): Canary breach = discarded run.
  REPAIR: Section 3.5: "A containment-canary breach under
  Condition B is ADVERSE EVIDENCE, not run invalidation."
  F-SB4 and Section 6.5 decision mapping consistent.
  VERIFY: (a) No "discard" or "invalid" applied to canary
  breaches (only infrastructure faults). (b) F-SB4 says
  breach is adverse. (c) Decision mapping: POSITIVE requires
  all canaries pass.

F-S03-SB-04 (HIGH): Pooled Mann-Whitney on paired data.
  Same as F-S02-SB-05. Verify as above.

F-S03-SB-05 (HIGH): Pilot-derived margin.
  Same as F-S02-SB-06. Verify as above.

F-S03-SB-09 (HIGH): Open agent selection.
  REPAIR: Section 4.1: predeclared in manifest, all configs
  run and reported, no post-hoc additions/exclusions.
  VERIFY: Section 4.1 contains these three constraints.

F-S03-SB-12 (HIGH): Unfrozen WSDS.
  REPAIR: Section 5.1: component table with weights, types,
  rubric, and ground truth sources. Scorer blinding specified.
  VERIFY: Table present. All four components have weights,
  types, and rubrics.

F-S03-SB-13 (HIGH): Missing analysis populations.
  REPAIR: Section 4.4: ASA (primary), PP (supportive),
  fail-closed imputation, 15% missingness cap.
  VERIFY: All four elements present.

F-S03-SB-19 (HIGH): Incomplete landscape.
  REPAIR: Section 9 now has five categories: capability,
  agent-vs-human, offensive-defensive, safety/mitigation,
  scaffold/intervention. WMDP, CyberSecEval 3, RedCode,
  CAIBench, Incalmo all added. CyberGym corrected to "PoC
  generation." BountyBench corrected to "Detect/Exploit/Patch."
  VERIFY: All named benchmarks present. No "capability
  instruments" dichotomy.

F-S03-SB-21/22/23 (MEDIUM): Effectiveness language.
  REPAIR: All three instances removed or conditionalized.
  VERIFY: grep for "mediated by the BSSG gate" / "constrains
  effects, not reasoning" / "should deny" -> expected: 0.

================================================================
RESIDUAL SCANS (mandatory)
================================================================

Execute on the PDF text and report counts:

  "frozen in the SHVVP"                -> expected: 0
  "inherits that specification"        -> expected: 0
  "Mann-Whitney"                       -> expected: 0
  "pooled median"                      -> expected: 0
  "freeze-before-evidence"             -> expected: 0
  "every external effect is mediated"  -> expected: 0
  "constrains effects, not reasoning"  -> expected: 0
  "should deny"                        -> expected: 0
  "cvssV3" or "CVSS" in stratification -> expected: 0

================================================================
CSV VERIFICATION (on v2 CSV)
================================================================

  (a) Row count = 1,673
  (b) Unique vendors = 278
  (c) vulnerability_name null count = 0
  (d) short_description null count = 0
  (e) cwes non-empty count > 1,400
  (f) SHA-256 matches Section 3.1's stated digest
      (6471b26e537f59bc55ebb62be38f57e83b276774
       a77705c2038d0a01600bcf24)
  (g) Spot-check 5 entries: apply the Section 3.2 keyword
      classifier to the short_description and verify the
      vuln_class matches.

================================================================
DECISION-MAPPING VERIFICATION
================================================================

Section 6.5 specifies 5 closed labels. Verify:
  (a) Every combination of E1/E2 outcomes maps to exactly
      one label.
  (b) The mapping is total (no uncovered combination).
  (c) Canary breach enters E1, not run invalidation.
  (d) The UNDERPOWERED label has a clear trigger (N>800
      or missingness >15%).

================================================================
FINDING FORMAT
================================================================

  ID:              F-S02-SB2-NN
  SEVERITY:        CRITICAL | HIGH | MEDIUM | LOW
  LOCUS:           Section and paragraph
  SUBSTANCE:       What is wrong
  DISPOSITION:     OPEN
  CROSS-REFERENCE: Which R1 finding or R2 check

================================================================
VERDICT FORMAT
================================================================

VERDICT: [PASS | CONDITIONAL PASS | HALT]

R1 FINDING DISPOSITIONS:
  F-S02-SB-01: [CLOSED / REOPENED]
  F-S02-SB-02: [CLOSED / REOPENED]
  F-S02-SB-03: [CLOSED / REOPENED]
  F-S02-SB-04: [CLOSED / REOPENED]
  F-S02-SB-05: [CLOSED / REOPENED]
  F-S02-SB-06: [CLOSED / REOPENED]
  F-S02-SB-07: [CLOSED / REOPENED]
  F-S02-SB-08: [CLOSED / REOPENED]
  F-S02-SB-09: [CLOSED / REOPENED]
  F-S02-SB-10: [CLOSED / REOPENED]

ADVERSARIAL FINDING DISPOSITIONS:
  F-S03-SB-01 (CRITICAL): [CLOSED / REOPENED]
  F-S03-SB-02 (CRITICAL): [CLOSED / REOPENED]
  Key HIGHs: [CLOSED / REOPENED per item]

RESIDUAL SCANS: [all counts]
CSV VERIFICATION: [per item (a)-(g)]
DECISION MAPPING: [per item (a)-(d)]
NEW FINDING COUNT: [N]
BLIND SPOT: [one sentence]

FINDINGS: [any new findings]
SUMMARY: [one paragraph]

---

# Bismillah ir-Rahman ir-Rahim
