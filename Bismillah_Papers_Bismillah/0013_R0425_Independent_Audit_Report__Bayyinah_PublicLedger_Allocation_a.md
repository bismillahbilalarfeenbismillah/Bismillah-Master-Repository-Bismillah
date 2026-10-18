# Bismillah ir-Rahman ir-Rahim

# R0425 -- Independent Audit Report: Bayyinah PublicLedger Allocation and Asymmetric-Measure Audits

**Chronological Index:** 13 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R2_gpt_report.pdf  
**Source Format:** pdf  
**SHA-256:** `0f81f9fa88417dad29820ce962c56aa77389a363bd7ce63b2dbc8f6b44d9d0a5`  

---

## R0425 · Independent Audit Report: Bayyinah PublicLedger Allocation and Asymmetric-Measure Audits

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R2_gpt_report.pdf
- source_format: pdf
- text_sha256: 0f81f9fa88417dad29820ce962c56aa77389a363bd7ce63b2dbc8f6b44d9d0a5

Independent Audit Report: Bayyinah PublicLedger Allocation and Asymmetric-Measure Audits
v0.2
Audit namespace: F-AA-R2
Artifact: Bayyinah_AllocationAsymmetry_v0.2.md and companion/reproduction package
Verdict: NON-PASS
Severity count: 0 CRITICAL, 2 HIGH, 3 MEDIUM, 1 LOW

1. Independence attestation
Lineage: I am an OpenAI GPT lineage and had no drafting role in the artifact. I am therefore outside the
Claude/Anthropic producing lineage.
Model-family independence: The companion identifies the first-round auditor as another OpenAI GPT
instance. This audit therefore does not provide the preferred different-model-family independence
requested in the brief.
Context independence: This was not a clean fresh-session audit in the strict sense required by the
dispatch. The current conversation contains Bayyinah continuity context, and the packet itself contains the
prior findings ledger. I independently recomputed the numerical results and did not treat the first-round
verdict as binding, but I cannot attest to full context independence.
Accordingly, even absent substantive HIGH findings, this execution should not be counted as the preferred
fully independent second-lineage audit round.

2. Executive determination
The frozen snapshot is internally reproducible. I independently confirmed:
• 37,988 records across FY2022–FY2024.
• FY2024 face-value sum: $65,189,755,228.64.
• FY2024 annual-expenditure sum: $8,170,228,558.54.
• MWBE prime-vendor shares for FY2024: 18.7345% by count, 3.9532% by face value, and 7.0612%
by annual expenditure.
• Face-value concentration: top five 22.1434%, top ten 30.4151%, top twenty 41.7769%, Gini
0.93117.
• Award years range from 1984 through 2025.
• 91.6876% of FY2024 face value is associated with contracts awarded before 2024.
• FY2024 has 1,348 missing and 48 explicit-zero contract_amount records.
• The manifest contains the actual union of 22 fields.
• The snapshot SHA-256 validates.

1


• The program aborts on a deliberately introduced field-inventory mismatch.
The reader note is substantially improved and generally uses the correct descriptive framing. It
nevertheless remains unsupported in material respects because:
1. The companion expressly reinstates the prohibited claim that the 3.95% face-value statistic is the
MWBE “operative substrate.”
2. The reproduction script falsely represents its live-comparison coverage. It compares only three
MWBE percentages, not “every emitted statistic, schema, and row/hash summary” as documented.
The note therefore still claims more than its data-validation implementation and companion framing
support.

3. Findings
F-AA-R2-01
Severity: HIGH
Locus: Bayyinah_AllocationAsymmetry_AuditCompanion.md , Section A, “Framing-claim
corroboration,” paragraph beginning “EV corroborated two interpretive claims.”
Substance — surface versus substrate divergence:
The v0.2 reader note states that the 3.95% face-value share is only a descriptive prime-vendor statistic and
expressly says it must not be treated as the MWBE-goal “operative substrate.” The companion nevertheless
states that dollar-denominated MWBE goals support “Section 4.2’s reading that the 3.95 percent dollar
share is the operative substrate.”
That is not Section 4.2’s current reading. It is the exact interpretive claim that F-AA-R1-02 required v0.2 to
remove. The cited legal concept—goals expressed as a percentage of qualifying dollar value—does not
establish that total prime-contract face value is the applicable denominator. Eligible expenditures,
subcontracting opportunities, participation tiers, exclusions, and waivers remain absent.
Disposition: REQUIRED CORRECTION. Remove the “operative substrate” sentence and replace it with
language consistent with the reader note: dollar denomination alone does not establish that either supplied
ledger amount is the legally operative MWBE-goal denominator.
Cross-reference: F-AA-R1-02; reader Sections 4.2 and 6; audit-checklist item 2.

F-AA-R2-02
Severity: HIGH

2


Locus: reproduce_paper2.py , docstring and live_compare() ; companion Appendix, disposition of
F-AA-R1-09.
Substance — surface versus substrate divergence:
The script claims that --live compares:
“every emitted statistic, schema, and row/hash summary”
The companion similarly says the revised script “compares every emitted statistic.”
The implementation does not do this. After calculating stats() , live_compare() compares only:
• mwbe_count
• mwbe_face
• mwbe_ae
It does not compare:
• Face-value totals.
• Annual-expenditure totals.
• Missing counts.
• Explicit-zero counts.
• Process-composition shares.
• Top-5, top-10, or top-20 concentration.
• Vendor count.
• Gini.
• Pre-2024 award share.
• Award-year range.
• Live field inventory or schema.
• Row-level identity, canonical hash, or any live hash summary.
• Cross-vintage overlap statistics.
Even the printed frozen-versus-live row count is not used to trigger drift or a nonzero exit.
This means F-AA-R1-09 was documented as absorbed more broadly than it was actually implemented.
Material live drift in several headline figures could occur while the program prints “no material drift” and
exits successfully.
Disposition: REQUIRED CORRECTION. Refactor the calculations into a single complete structured-statistics
object used by both offline reporting and live comparison. Compare every public numerical claim and every
declared integrity dimension, with explicit tolerances and nonzero exit on any mismatch. Add tests that
deliberately alter each statistic to confirm detection.
Cross-reference: F-AA-R1-09; audit-checklist items 1–7; script documentation.

3


F-AA-R2-03
Severity: MEDIUM
Locus: Reader Section 4.0, sentence stating that “an exact full-field fingerprint finds several thousand
records shared across the three report years.”
Substance — surface versus substrate divergence:
An exact canonical fingerprint of every field in each frozen row produces zero cross-vintage matches. This is
expected because fiscal_year_end_date changes between vintages, and expenditure/balance fields
often change as well.
The following results were obtained:
• Exact all-field overlap, FY2022/FY2023: 0
• Exact all-field overlap, FY2022/FY2024: 0
• Exact all-field overlap, FY2023/FY2024: 0
After excluding only fiscal_year_end_date , the pairwise overlaps are 193, 85, and 135—not “several
thousand.”
Several-thousand-level overlap appears only after also excluding annual expenditure, expenditure-to-date,
and balance fields:
• FY2022/FY2023: 2,115
• FY2022/FY2024: 604
• FY2023/FY2024: 1,002
Thus the underlying proposition—that many contracts recur—is plausible and supported by a normalized
contract-identity fingerprint, but the stated “exact full-field fingerprint” method is false.
Disposition: REQUIRED CORRECTION. Define the identity fields used to identify recurring contracts and
call the comparison a normalized or stable-field fingerprint. Report the actual pairwise counts and explain
why annual-state fields are excluded.
Cross-reference: F-AA-R1-01; reader Sections 4.0 and 6; audit-checklist item 1.

F-AA-R2-04
Severity: MEDIUM
Locus: Companion Section C, fourth falsifiability criterion.
Substance — surface versus substrate divergence:
The companion says:

4


“if the competitive-bid dollar share were not dominant, the Section 4.1 ‘pass’ would be
wrong.”
The current Section 4.1 contains no pass. It expressly withdraws the former compliance pass and states that
process composition is descriptive only.
Moreover, dominance of competitive-bid dollars would not make a compliance pass correct; nondominance
would merely contradict the descriptive composition result. Compliance requires operative rules and
exception documentation, independently of whether the aggregate share is high or low.
This stale criterion both misdescribes v0.2 and preserves the invalid inference rejected in F-AA-R1-03.
Disposition: REQUIRED CORRECTION. Replace the criterion with: if recomputation does not reproduce the
reported process-composition percentages, the descriptive Section 4.1 figures are falsified. State separately
that no composition result, dominant or otherwise, establishes compliance.
Cross-reference: F-AA-R1-03; reader Sections 4.1 and 4.4; audit-checklist item 3.

F-AA-R2-05
Severity: MEDIUM
Locus: Companion Sections B and D, particularly “One substantive finding to date,” “v0.1 (corrected) [this
state],” and the statement that the note carries zero open findings above INFO.
Substance — surface versus substrate divergence:
The companion combines an append-only historical ledger with present-tense status labels that still
designate the pre-v0.2 state as “this state.” It also says there was “one substantive finding to date” and that
the artifact carries zero open findings above INFO, although the appended ledger records nine additional
findings, including three HIGH findings, and describes v0.2 as a resubmission following a NON-PASS.
Historical text may properly be preserved, but it must be clearly scoped as superseded. Here, the reader
cannot reliably distinguish current status from retained historical status.
Disposition: REQUIRED CORRECTION. Preserve the historical bytes under an explicitly marked supersededstate block, and add an authoritative current-state ledger summary at the beginning of the companion.
Remove or qualify “this state,” “one substantive finding,” and “zero open findings” wherever they are no
longer current.
Cross-reference: Companion Appendix; F-AA-R1 ledger; audit-checklist item 8.

5


F-AA-R2-06
Severity: LOW
Locus: Reader Section 4.3 and reproduction coverage.
Substance — surface versus substrate divergence:
Section 4.3 says the reported concentration “supplies a structural explanation for the count-versus-dollar
asymmetry on both measures,” although the section and script report concentration only for face value and
acknowledge that annual-expenditure concentration differs.
Independent calculation shows that annual expenditure is also highly concentrated—top five 16.87%, top
ten 26.24%, top twenty 37.57%, Gini 0.904—so the general proposition is empirically plausible. But those
figures are neither disclosed nor included in the reproduction output, leaving the “both measures”
explanation incompletely demonstrated in the package.
Disposition: RECOMMENDED CORRECTION. Either add annual-expenditure concentration figures and
reproduce them, or limit the explanatory sentence to the face-value asymmetry and describe the annualexpenditure mechanism as a separate result requiring its own calculation.
Cross-reference: Reader Section 4.3; audit-checklist item 4; F-AA-R2-02.

4. Checklist determination
4.1 Estimand integrity
Mostly satisfied, with one method-description defect.
The reader correctly distinguishes face value from annual expenditure, gives the correct totals, discloses the
91.7% pre-2024 share, and says the vintages must not be summed. No surviving reader-note passage
presents $65.19 billion as FY2024 annual spending.
The claimed “exact full-field fingerprint,” however, is not reproducible as described. See F-AA-R2-03.

4.2 MWBE framing
Not satisfied across the complete artifact.
The reader note is appropriately descriptive and states the prime-only, indirect-participation, eligible-spend,
contract-goal, and waiver limitations.
The companion reinstates “operative substrate” language. See F-AA-R2-01.

6


The frozen numerical results reproduce exactly:
Vintage

Count share

Face-value share

Ratio

Annual-expenditure share

Ratio

FY2022

16.4199%

3.2733%

5.02×

4.2468%

3.87×

FY2023

18.5818%

3.5148%

5.29×

6.2714%

2.96×

FY2024

18.7345%

3.9532%

4.74×

7.0612%

2.65×

The annual-expenditure asymmetry narrows across the three reported vintages.

4.3 Process composition
Reader satisfied; companion not fully satisfied.
The reader explicitly refuses a compliance conclusion. The companion’s falsifiability section still refers to a
Section 4.1 “pass.” See F-AA-R2-04.

4.4 Concentration
Face-value arithmetic satisfied.
The top-share and Gini results reproduce. The reader refuses intent and steering conclusions.
The claim that this reported concentration explains both dollar measures should either be supported with
annual-expenditure concentration or narrowed. See F-AA-R2-06.

4.5 Provenance and counts
Frozen package satisfied; live divergence not independently completed.
The reader identifies gpsc-qqsz as a community-created view, identifies twsw-2mqa as first-party, and
reports 37,988—not 111,879—for the three-vintage extract.
The public gpsc-qqsz endpoint itself was reachable through the browser interface and returned current
FY2024 records.
However, this execution environment’s Python DNS resolver failed during the required complete live pull. I
therefore do not certify the exact current live-versus-frozen divergence values or a complete first-party
rebase from this run.

4.6 Legal phrasing, missing/zero split, manifest, and refusals
Substantially satisfied.

7


The reader distinguishes statutory reporting from PARIS/schema/publication implementation. It separates
1,348 missing values from 48 explicit zeroes. The manifest accurately lists 22 fields, and the script aborts on
a field mismatch. The reader explicitly refuses intent, discrimination, goal attainment, and rule-compliance
determinations.
The companion contains stale legal/framing language addressed in F-AA-R2-01 and F-AA-R2-04.

4.7 Mandatory live and capital-join legs
Not completed in this execution.
python3 reproduce_paper2.py --live failed at DNS resolution before downloading live rows. This
environmental failure is distinct from F-AA-R2-02: even in a network-capable environment, the current
implementation does not perform the full comparison it claims.
I was also unable to execute a complete current row-level join against all three live capital datasets from the
Python environment. The join therefore remains uncertified by this auditor. The packet’s informal EV-2
assertion cannot substitute for the mandatory independent execution required by the brief.

4.8 Regression check
Failed.
• F-AA-R1-01: substantially absorbed, but the exact-fingerprint support statement is defective.
• F-AA-R1-02: regressed in the companion through “operative substrate” language.
• F-AA-R1-03: reader correction absorbed; stale “pass” survives in companion.
• F-AA-R1-04: reader correction appears absorbed.
• F-AA-R1-05: absorbed.
• F-AA-R1-06: reader correction appears absorbed, but companion retains older overbroad
corroboration language.
• F-AA-R1-07: absorbed.
• F-AA-R1-08: absorbed and functionally tested.
• F-AA-R1-09: not fully absorbed in code, despite the ledger claiming complete absorption.

5. Pass criterion and convergence status
Because this audit returns two HIGH findings, v0.2 does not pass the stated criterion of zero CRITICAL and
zero HIGH.
It therefore cannot count as the first of the two consecutive passing rounds required by Audit Framework
v3.0, Standing Rule 7. The consecutive-pass count remains at zero.

8


After correction, the then-current artifact requires a new independent audit round. A preferably non-OpenAI
auditor working in a fresh context should:
1. Re-execute the complete live comparison.
2. Reproduce against twsw-2mqa or the ABO statewide dataset.
3. Execute the row-level capital-table join.
4. Verify that all companion text, not merely the reader note, has removed the rejected interpretive
claims.
5. Confirm that the revised live checker detects drift in every published statistic.

6. Required explicit judgment
Does the note still claim anything its data or cited legal structure does not support?
Yes.
The reader note itself is mostly disciplined, but the complete v0.2 artifact still:
• Calls the 3.95% face-value statistic the MWBE-goal “operative substrate” in the companion.
• Refers to a withdrawn Section 4.1 compliance “pass.”
• Claims an “exact full-field fingerprint” result that the supplied rows do not produce.
• Claims a complete live comparison that the supplied implementation does not perform.
Final verdict: NON-PASS — 0 CRITICAL, 2 HIGH, 3 MEDIUM, 1 LOW.

9

---

# Bismillah ir-Rahman ir-Rahim
