# Bismillah ir-Rahman ir-Rahim

# R0435 -- Model Council Synthesis: Bayyinah Allocation and Asymmetric-Measure Audits v0.5, Round 6

**Chronological Index:** 21 of 995  
**Date:** 2024  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** F-AA-R6_synthesis.md  
**Source Format:** md  
**SHA-256:** `2516b65972a42a3cbde494e8d69a58aab9cf2e6d7c980a61f4f15723abb565c3`  

---

## R0435 · Model Council Synthesis: Bayyinah Allocation and Asymmetric-Measure Audits v0.5, Round 6

- section: VI. Applied Audits & Public-Data Studies
- source_file: F-AA-R6_synthesis.md
- source_format: md
- text_sha256: 2516b65972a42a3cbde494e8d69a58aab9cf2e6d7c980a61f4f15723abb565c3

# Model Council Synthesis: Bayyinah Allocation and Asymmetric-Measure Audits v0.5, Round 6

Council members: GPT 5.5 (OpenAI, qualifying), Gemini 3.1 Pro (Google, qualifying), and Claude Opus 4.8 (Anthropic/Claude producing lineage, quarantined advisory-only).

## Where Models Agree

| Finding | GPT 5.5 | Gemini 3.1 Pro | Claude Opus 4.8 | Evidence |
|---|---:|---:|---:|---|
| The supplied package was present and passed snapshot hash, 22-field inventory, and 37,988-row integrity checks. | ✓ | ✓ | ✓ | Each member independently unpacked the submitted ZIP and ran the offline reproducer. |
| All headline statistics reproduce: FY2024 face value $65.19B, annual expenditure $8.17B, MWBE shares 18.73% / 3.95% / 7.06%, top-10 face concentration 30.42%, and vendor Ginis 0.931 / 0.904. | ✓ | ✓ | ✓ | Independent implementations reproduced the frozen figures and the specified vendor-level positive-total Gini method. |
| The correct vintage fingerprint is the three pairwise 18-field overlaps 2,115 / 604 / 1,002, with zero pairwise all-field overlap. | ✓ | ✓ | ✓ | All members independently implemented the specified field exclusions and pairwise comparisons. |
| The supplied self-test detects all 45 deliberate perturbations, the live comparator reports no drift with exit 0, and a one-cell non-MWBE mutation produces a nonzero comparator result. | ✓ | ✓ | ✓ | Each report includes executed outputs for all three tests against the [New York State community contract view](https://data.ny.gov/resource/gpsc-qqsz.json). |
| Provenance is correctly separated: the exact FY2024 query returns 13,718 / $65.19B for `gpsc-qqsz` and 13,648 / $65.13B for `twsw-2mqa`, corresponding to about 0.51% count divergence and 0.089% face divergence. | ✓ | ✓ | ✓ | The results were independently queried from [gpsc-qqsz](https://data.ny.gov/resource/gpsc-qqsz.json) and [twsw-2mqa](https://data.ny.gov/resource/twsw-2mqa.json). |
| The companion header contains a stale v0.4 reference even though the reader, adjacent companion text, and Current State block identify v0.5. | ✓ | ✓ | ✓ | All three members independently located the same cross-artifact version-propagation defect and rated it MEDIUM. |

## Where Models Disagree

| Topic | GPT 5.5 | Gemini 3.1 Pro | Claude Opus 4.8 | Why They Differ |
|---|---|---|---|---|
| Capital-key coverage | An all-project check found 2,608 of 2,609 matches in both target datasets; `L50502SX` was absent from both. | Found 2,608 matches in `kizb-nxtu` and 2,288 in `ehz8-ag3n`. | A defined 120-project batch matched 120/120 in both targets. | GPT used batched key queries over the full source set, Gemini downloaded capped result sets, and Claude tested a bounded batch. All still established join feasibility and confirmed that `wcsa-vkhf` has no borough key. |
| Packet brief wording | Added a LOW observation that the ZIP itself contains three artifacts rather than a separate brief file. | No separate finding. | Treated the user’s audit request as the brief and found the package gate satisfied. | GPT interpreted “packet” as the ZIP inventory, while the other members treated the request text plus attachment as the packet. This does not affect execution or verdict. |
| Additional capital caveat | Added an INFO finding that the historical 120/120 result should not imply universal live-table coverage. | Reported match counts without a separate caveat finding. | Considered the requested batch test sufficient. | GPT broadened the requested batch test into a full-key coverage audit. |

## Unique Discoveries

| Model | Unique Finding | Why It Matters |
|---|---|---|
| GPT 5.5 | Identified `L50502SX` as the single `wcsa-vkhf` project number absent from both allocation views in its full-key query. | It refines the capital-join claim from universal coverage to near-complete live coverage without undermining feasibility. |
| Claude Opus 4.8 | Cross-checked the Gini with two independent formulas and computed the 18-field three-way intersection as 265 solely as a guard against substituting it for the required pairwise metric. | It directly addresses the method-confusion failure mode from the prior round, though Claude remains advisory-only. |

## Comprehensive Analysis

The council satisfies the no-prior-state requirement. GPT 5.5, Gemini 3.1 Pro, and Claude Opus 4.8 each attested that they ran as fresh instances without memory, personalization, saved state, prior reports, or access to another member’s work. They used separate working directories and independently unpacked the attached reproduction package. Claude Opus 4.8 is explicitly quarantined because Anthropic/Claude is the producing lineage; its work is advisory and is not included in the convergence-bearing vote.

The two qualifying members are GPT 5.5 and Gemini 3.1 Pro. Both executed the offline reproducer, self-test, live comparator, independent recomputation, provenance reconciliation, capital join, and adversarial mutation. Their separate verdicts are both PASS, each with zero CRITICAL and zero HIGH findings. The qualifying synthesis is therefore PASS. Claude Opus 4.8 independently reached an advisory PASS with zero CRITICAL and zero HIGH, but that vote has no effect on the synthesized qualifying verdict.

The strongest convergence is quantitative. Independent code reproduced 37,988 rows; FY2024 face value of $65,189,755,228.64; annual expenditure of $8,170,228,558.54; MWBE count, face, and expenditure shares of 18.7345%, 3.9532%, and 7.0612%; top-10 face concentration of 30.4151%; and face and expenditure Ginis of 0.93117 and 0.90435. The members also reproduced the specified pairwise 18-field overlaps of 2,115, 604, and 1,002, while every pairwise all-field overlap was zero. This rules out the prior method substitutions involving a three-way intersection or reduced identity subset.

The operational controls also worked. The frozen snapshot passed hash and field-inventory validation; the self-test detected all 45 perturbations; the live pull of all three years reported no drift and exited 0; and each adversarial alteration of one non-MWBE contract amount triggered a nonzero result. Exact-date provenance queries against [gpsc-qqsz](https://data.ny.gov/resource/gpsc-qqsz.json) and [twsw-2mqa](https://data.ny.gov/resource/twsw-2mqa.json) confirmed that the artifact correctly separates the approximately 0.089% face-value divergence from the approximately 0.51% record-count divergence. Capital joins through [wcsa-vkhf](https://data.ny.gov/resource/wcsa-vkhf.json), [kizb-nxtu](https://data.ny.gov/resource/kizb-nxtu.json), and [ehz8-ag3n](https://data.ny.gov/resource/ehz8-ag3n.json) were demonstrated, and all members confirmed that the location table has no borough key.

The artifact’s substantive framing also holds. Face value is treated as a stock, annual expenditure as a flow, approximately 91.7% of FY2024 face value predates 2024, and vintages are not summed. MWBE results remain descriptive prime-vendor statistics with limitations, not goal-attainment, operative-substrate, short-measure, or pass claims. Concentration is used only as a non-culpable structural explanation. The fingerprint prose matches the implemented 18-field method, Section 8 correctly directs auditors to the attached package rather than related DOIs, and the live convergence language uses one counter.

One new defect converged across every member: `Bayyinah_AllocationAsymmetry_AuditCompanion.md` line 3 still calls the reader-facing note v0.4, while the actual reader, companion line 5, and Current State block say v0.5. The council rates this F-AA-R6-01 MEDIUM. It is a real recurrence of the version-propagation family but does not reach the stated blocking threshold.

**Synthesized qualifying verdict: PASS.** This Round 6 result is the first of the two consecutive qualifying passes required for convergence. The consecutive qualifying-PASS count moves from ZERO to ONE for v0.5, and one further qualifying passing round on the then-current corrected artifact remains necessary.

---

# Bismillah ir-Rahman ir-Rahim
