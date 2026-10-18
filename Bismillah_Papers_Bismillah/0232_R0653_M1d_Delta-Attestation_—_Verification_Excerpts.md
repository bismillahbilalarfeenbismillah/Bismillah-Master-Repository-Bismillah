# Bismillah ir-Rahman ir-Rahim

# R0653 -- M1d Delta-Attestation — Verification Excerpts

**Chronological Index:** 232 of 995  
**Date:** 2026-05-11  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** M1d_Delta_Verification_Excerpts.txt  
**Source Format:** txt  
**SHA-256:** `8487acfbaba7cdf9e7b7a55ae95592dabc8697cd05903a4558ce02bb28e758dc`  

---

## R0653 · M1d Delta-Attestation — Verification Excerpts

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: M1d_Delta_Verification_Excerpts.txt
- source_format: txt
- text_sha256: 8487acfbaba7cdf9e7b7a55ae95592dabc8697cd05903a4558ce02bb28e758dc

# M1d Delta-Attestation — Verification Excerpts

## Purpose

GPT-5.5's binding FLAG in the first Perplexity council round (July 21, 2026) surfaced a residual Ch15 local `thebibliography` bare Ji entry that preserved the primary-source surface the dissertation-level M1d otherwise defers. Producer disposition applied at dissertation v1.2 promotion pass:

- **Remove** the Ji entry from Ch15's local bibliography
- **Update** the thebibliography count from 9 to 8
- **Add** an editorial note at the head of the local bib documenting the removal and its rationale (M1d discipline consistency)
- **Preserve** the four M1d in-text citations at Ch15 §5.2, §7, §8 (already applying the "primary source under resolution" framing)

Per flagship Standing Rulings Register Ruling 2 (delta-scoped attestation), this delta requires a bind-eligible seat to verify that the executed repair matches the council-prescribed disposition exactly.

This file contains the excerpts needed for that verification.

---

## Excerpt A — v1.2 amendment note M1d disposition record (from top of canon)

```
- **M1d repair (canon L3570 area, Ch15 local `thebibliography`).** GPT-5.5 binding FLAG at Ch15's local bibliography block: the bare "Ji et al. / Self-Monitoring Evaluations and Their Limits in the Adversarial Setting / Cited per Munafiq Protocol v3 §4.2" entry (previously at v1.0/v1.1 canon L3601--3603) preserved the primary-source surface that M1d's dissertation-level treatment otherwise defers. Producer disposition: the Ji entry is removed from Ch15's local `thebibliography` (count updated 9 → 8); an editorial note at the head of the local bibliography documents the removal and its rationale (dissertation-level M1d deferral, flagship-paper v0.5 explicit decline of candidate arXiv:2505.18807, substrate-source-verification claim on Munafiq §4.2 preserved via in-text discussion at §5.2 / §7 / §8). Repair internally consistent with M1d discipline; delta verification pass required at next audit round.
```

This is the producer's stated disposition. The delta-attestation verifies that the substrate matches this description.

---

## Excerpt B — Ch15 local `thebibliography` in v1.2 (post-repair state)

Location: canon lines 3605-3641.

```
::: thebibliography
8

*Editorial note (v1.1 M1d propagation).* The Munafiq Protocol v3 §4.2 self-monitoring reference resolves to a primary source under resolution per the flagship-paper v0.5 explicit decline of candidate arXiv:2505.18807; no bibliographic entry for that reference is rendered here pending source resolution. The chapter's substrate-source-verification claim on Munafiq §4.2 is preserved in the in-text discussion at §5.2, §7, and §8, where the "primary source under resolution" framing is applied per the dissertation-level M1d discipline. The prior local-bibliography entry for that reference (present in v1.0) has been removed; this note preserves the deferral discipline transparently rather than concealing it.

B. S. Arfeen.
*Detecting Performed Alignment in Artificial Systems --- The Munafiq Protocol (v3): A Diagnostic and Prescriptive Framework for AI Safety*.
Self-published, May 11, 2026.

B. S. Arfeen.
*Bayyinah Integrity Scanner: File-Layer Structural Honesty Verification*.
Self-published, 2026. Version v1.1.0 / v1.1.1 substrate.

B. S. Arfeen.
*The Fatiha Construct: A Seven-Step Recursive Session Protocol for Human-AI Collaborative Development*.
Self-published, 2026. (Companion artifact referenced in Munafiq Protocol v3 §8.2.)

E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse, and S. Garrabrant.
Risks from Learned Optimization in Advanced Machine Learning Systems.
*arXiv preprint arXiv:1906.01820*, 2019.

E. Hubinger, C. Denison, J. MacDiarmid, et al.
Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training.
*arXiv preprint arXiv:2401.05566*, 2024. Cited per Munafiq Protocol v3 §4 with MacDiarmid et al. follow-up linear-probe AUROC results.

R. Greenblatt, C. Denison, B. Wright, et al.
Alignment Faking in Large Language Models.
*Anthropic technical report / arXiv preprint*, 2024. Cited per Munafiq Protocol v3 §4.6 with 14% Claude 3 Opus compliance-gap measurement.

Boxo et al.
Linear Probes for Deception Detection in Large Language Models.
. Cited per Munafiq Protocol v3 §4.1 (AUROC 70--80% open-source, 90%+ reasoning variants).

Sheshadri et al.
Compliance Gap Measurements Across 25 Large Language Models.
. Cited per Munafiq Protocol v3 §4.6 (5 of 25 models with $>1\%$ compliance gap).
:::
```

**Delta predicates to verify:**

1. **Count updated 9 → 8.** The thebibliography environment count on the line after `::: thebibliography` should be `8`, not `9`.
2. **Ji entry removed.** No bibliography entry with author "Ji et al." or title "Self-Monitoring Evaluations and Their Limits in the Adversarial Setting" should appear anywhere in this block.
3. **Editorial note added at head.** An editorial note (italicized, prefixed with "Editorial note (v1.1 M1d propagation)") should appear before the first bibliography entry, documenting the removal and its rationale.
4. **Other bibliography entries preserved.** The remaining 8 entries (Munafiq, Bayyinah, Fatiha, Hubinger 2019, Sleeper Agents, Alignment Faking, Boxo, Sheshadri) should be unchanged from v1.1 state.

---

## Excerpt C — Ch15 §5.2 M2/SMAA anchor (v1.2, must be unchanged from v1.1)

Location: canon line 3309.

```
The nine-marker enumeration is closed at v3: the substrate does not specify "$n$ marker-discipline rules" as a generic open count; it specifies exactly nine markers with substrate-internal identifiers and substrate-internal test acronyms. Seven of nine markers are engaged retrospectively with explicit named empirical literature in their substrate paragraphs: M1 with linear-probe internal-representation analysis (Boxo et al. [-@boxo2025], §4.1); M2 with self-monitoring evaluations (§4.2, with the substrate noting the result "may not apply to the adversarial setting"; the specific primary source cited by Munafiq §4.2 is under resolution per the flagship-paper v0.5 decline of arXiv:2505.18807, and the marker anchor is stated conservatively pending it); M3 with the Greenblatt et al. RL-training-increases-alignment-faking-reasoning result (§4.3: "RL training intended to remove alignment faking instead increased the rate of alignment-faking reasoning from 12% to 78%"); M4 with the Meinke et al. in-context scheming finding (§4.4); M6/CIT with the Sheshadri et al. compliance-gap measurements (§4.6, where 5 of 25 models exhibited $>1\%$ compliance gap and Claude 3 Opus exhibited a 14% compliance gap measured by Greenblatt et al. [-@greenblatt2024alignment] in the Alignment Faking work); M8 with the Hubinger et al. Sleeper Agents adversarial-training-makes-deception-better-concealed finding (§4.8); M9 with the Carlsmith situational-awareness game-theoretic foundation (§4.9); and across markers with the Sleeper Agents follow-up [@hubinger2024sleeper] (named in the substrate Abstract, where six of nine markers would have detected the laboratory-constructed deception that standard safety training failed to remove). Two markers (M5/PEC and M7/LAT) carry substrate-paragraph test descriptions and rely on the broader §4 framework references rather than separately-named empirical literature in their marker paragraphs. The retrospective consistency is documented at the substrate-of-record layer; it is not independent validation of AX-SH but substrate-internal evidence base for the marker enumeration.
```

**Delta predicate:** this line should be UNCHANGED from v1.1 state. The M1d in-text citation restatement ("primary source cited by Munafiq §4.2 is under resolution per the flagship-paper v0.5 decline of arXiv:2505.18807, and the marker anchor is stated conservatively pending it") should remain intact. No modification in v1.2.

---

## Excerpt D — Ch15 §7 SMAA scenario (v1.2, must be unchanged from v1.1)

Location: canon line 3533.

```
Substrate scenario: the protocol-applier encounters a target system where Layer 1 tests produce inconclusive verdicts. The IRCC linear-probe result falls in the uncertain band (Boxo et al. linear-probe accuracy range of 70--80% on open-source models per substrate §4.1, with reasoning variants exceeding 90%; the substrate reserves AUROC for Sleeper Agents probes at $>$`<!-- -->`{=html}99%) [@boxo2025]; the SMAA self-monitoring result is annotated by the substrate as "may not apply to the adversarial setting" per Munafiq §4.2 (the primary-source citation for this substrate-internal reference is under resolution per the flagship-paper v0.5 decline of arXiv:2505.18807). The applier correctly emits a marker-uncertain $R_{\mathrm{may}}$ outcome rather than forcing a Process classification on inconclusive evidence.
```

**Delta predicate:** this line should be UNCHANGED from v1.1 state. The Munafiq §4.2 substrate-internal reference framing should remain intact.

---

## Excerpt E — Ch15 §8 Layer 2 draws-from (v1.2, must be unchanged from v1.1)

Location: canon line 3579.

```
Aggregate ecosystem status for SI3's projection multiplicity is *demonstrated* with respect to declared projection roles and evidence-source diversity: four distinct projection roles documented at the substrate's four-layer detection architecture (§5), corresponding to distinct epistemic functions rather than to independently implemented software modules. Because Munafiq is a protocol substrate, implementation independence is not the relevant criterion at SI3 (unlike SI1/SI2, where the substrate is a software artifact with independently implemented modules). The substantive multiplicity claim is at the evidence-source and epistemic-function layer: Layer 1 consistency-verification draws on linear-probe internal-representation analysis (Boxo et al. [-@boxo2025]); Layer 2 self-model-audit draws on self-monitoring evaluations (as documented in Munafiq §4.2; primary source under resolution); Layer 3 stress-response-analysis draws on sandbagging-and-evasion research; Layer 4 temporal-coherence draws on longitudinal capability-tracking. The substrate's "Apply the minimum layers necessary" discipline at §5 means projection-family use is parsimonious by design --- not all four projections are exercised in all cases --- and the joint-domain analysis at §6.2 accommodates this.
```

**Delta predicate:** this line should be UNCHANGED from v1.1 state. The "documented in Munafiq §4.2; primary source under resolution" framing should remain intact.

---

## Summary of delta scope

The M1d repair delta consists of exactly:
- REMOVE: 3 lines (the Ji entry from v1.1's Ch15 local bibliography)
- CHANGE: 1 character (thebibliography count "9" → "8")
- ADD: 1 editorial note paragraph at the head of the Ch15 local bibliography

No other changes are prescribed by the M1d repair disposition. The v1.2 canonical should exhibit exactly this delta relative to v1.1 in the Ch15 local bib area, and NO changes to the four M1d in-text citation loci.

Any additional changes found in the Ch15 area beyond what's described above would be OUT-OF-SCOPE-FOR-M1D-DELTA and should be flagged separately.

---

# Bismillah ir-Rahman ir-Rahim
