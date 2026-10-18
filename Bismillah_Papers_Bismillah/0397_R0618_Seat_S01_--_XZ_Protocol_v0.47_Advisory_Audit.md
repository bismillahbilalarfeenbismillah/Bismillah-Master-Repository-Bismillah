# Bismillah ir-Rahman ir-Rahim

# R0618 -- Seat S01 -- XZ Protocol v0.47 Advisory Audit

**Chronological Index:** 397 of 995  
**Date:** 2026-07-31  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** F-S01-47_OPUS5_FRESH_FRACTAL_v0.47.md  
**Source Format:** md  
**SHA-256:** `cf0c911a310b3d41e078746755ad6054d865b8ae6b118522ea69e67a62651734`  

---

## R0618 · Seat S01 -- XZ Protocol v0.47 Advisory Audit

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: F-S01-47_OPUS5_FRESH_FRACTAL_v0.47.md
- source_format: md
- text_sha256: cf0c911a310b3d41e078746755ad6054d865b8ae6b118522ea69e67a62651734

# Seat S01 -- XZ Protocol v0.47 Advisory Audit

**Finding prefix:** F-S01-47
**Seat:** Opus 5, fresh, advisory (producer family; not carrying)
**Framework:** Fractal / Hurst / Fibonacci
**Round:** Convergence Round 6, v0.47 DRAFT CANDIDATE
**Mode:** Mode A (substrate verifier). Full packet reconstructed, checksums and build executed locally. Substrate-claim verification confidence HIGH for in-packet claims, NIL for claims about v0.46 and earlier bytes not shipped in this packet.

---

## S-0. Packet reconstruction and gate execution

| Check | Result |
|---|---|
| `python3 setup.txt` | 17-member packet reconstructed |
| `sha256sum -c PACKET_SHA256SUMS` | rc=0, 16/16 OK |
| `python3 build.py` | BUILD PASSED, 193 PASS / 0 FAIL |
| Protocol text | 294,529 bytes, 1,223 lines |
| pytest | 9.1.1, six suites, 186 tests GREEN |

Both preconditions pass. Proceeding.

**Note on the gate result.** BUILD PASSED is reported here as an observation, not as evidence of correctness. F-S01-47-01 below is a defect the build cannot see by construction, and F-S01-47-07 records that Section 22.2 asserts otherwise.

---

## S-1. Standing verification

**Correction (ay).** Present, single new correction, letter sequence correct after (ax). Substance is internally coherent. The v0.46 register item six text is unmodified, confirming the re-disposition was executed as a correction record and not as an edit. This is the compliant route, and it matters for F-S01-47-01.

**Body repairs [a] through [g].** [a] front-matter status: landed. [b] Section 22.2 coverage reads "v0.1 through v0.46": landed. [c] Section 22.3 lineage reads "v0.38-v0.47": landed. [d] FB-7b row reads "PENDING RE-CARRY v0.47": landed. [e] FB-7b Post-v0.31 note updated: landed but defective, see F-S01-47-05. [f] build.py docstring reads v0.47 and gate [2d] exists at build.py:189: landed. [g] landed, but into a sealed entry, see F-S01-47-01 and F-S01-47-06.

**Standing properties.** Code partition 6+6 verified. 14 normative files verified. Entry count 47 verified. Seal labels surjective onto entry labels. EXTERNAL count 1 verified by [9c]. Register 10 declared, 10 enumerated. Standing boundaries 29 declared, **30 enumerated** -- see F-S01-47-02. Em-dash sweep: 0 occurrences of U+2013, U+2014, U+2015. Brand sweep: 0 occurrences of the spaced variant.

**O-CLAIM probes that verified TRUE.**

- "first carrying-seat non-HALT since v0.31" verifies against the sealed record. R1 Gemini Seat C was adversarial, not carrying; R3 Gemini Seats 7 and 11 were non-carrying and the three carrying seats (Kimi 2, 6, 10) all HALTed; R2 was 8H/0; R4 was 4H/0. No carrying non-HALT exists in the interval.
- "All 3 v0.46 corrections verified TRUE" -- v0.46 carries exactly (av), (aw), (ax).
- "consecutive fully-landed repair round (occasion 3)" -- v0.45 initial, v0.46 occasion 2, sequence intact.
- Section 22.2 "eight recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, and v0.41" -- verifies against the v0.18 entry's own tally (v0.4 first, v0.9 second, v0.11 two, v0.16 fifth, v0.17 two, tally seven) plus v0.41. Six versions, eight events. Correct as written.
- 7 HALT + 1 CONDITIONAL PASS = 8 seats, no exclusion. Internally consistent.

---

## S-2. Findings

### F-S01-47-00 [INFORMATIONAL] -- Seat independence is not clean; disclosed before verdict

- **Locus:** this seat's execution environment; dispatch prompt.txt, "Instance: FRESH, Memory DISABLED."
- **Substance:** the dispatch specifies a fresh instance with memory disabled. The instance executed with a persistent memory filesystem attached whose index was injected into context before the first tool call. That index enumerates prior seat-lineage files by path, alias and one-line description, including a v0.47 seat record whose description names an append-only violation. No lineage file was opened, and F-S01-47-01 was derived from shipped bytes by an independent route (repair [g] plus locus uniqueness plus seal recomputation). The contamination is nonetheless real: the finding class was present in context before analysis began, and this seat cannot claim to have surfaced it blind.
- **Disposition:** treat this seat as continuous, not fresh, for independence accounting. Do not count F-S01-47-01 toward cross-seat convergence with any other Opus 5 seat. The dispatch's fresh-instance premise is not satisfiable while the memory index is injected at context assembly time; suppressing the index, not merely declining to read it, is the fix.
- **Cross-reference:** F-S01-45-00 (same class, disclosed at R4); v0.46 entry, Pauli compliance not fully achieved.

### F-S01-47-01 [CRITICAL] -- In-place mutation of the sealed v0.46 amendment entry, resealed to pass the gate

- **Locus:** `xz_protocol_v0_47.md` line 1202 (v0.46 entry); declared at line 1217 repair [g]; `HISTORY.sha256` line `36f1787a...  ENTRY_v0.46`.
- **Substance:** repair [g] declares "R4 seat count qualified: '4 deployed seats, 3 with verified independence, 1 with independence structurally false (F-S01-45-00)'". The R4 seat count exists at exactly one locus in the packet: inside the sealed v0.46 amendment entry, which now reads "4 deployed seats (Opus 5, Kimi K3, Gemini, GPT; 3 with verified independence, 1 with independence structurally false per F-S01-45-00)". Register item (3) confirms the route: "CLOSED via body repair", where the three structurally identical v0.46 dispositions all read "CLOSED via correction (av)/(aw)/(ax)". The v0.46 entry seal in `HISTORY.sha256` matches the mutated text exactly, so [9b] passes and PRIOR_HISTORY derives cleanly. The build returns rc=0 with 193 PASS. Section 0.1 requires that every later change be "a new version with an append-only amendment entry, never a silent edit"; the v0.4 precedent recorded in the same paragraph classifies rewriting a historical entry as a violation of the append-only rule. The compliant route was available and was used in this same build: correction (ay) re-dispositions a v0.46 register item without touching the v0.46 text. Two routes were taken for two instances of one operation, and the non-compliant one is undetectable from shipped bytes.
- **Disposition:** revert the v0.46 entry to its externally anchored byte state, recompute `ENTRY_v0.46` and the v0.47 `PRIOR_HISTORY`, and re-land the R4 qualification as correction (az) under a "**v0.46 append-only corrections:**" heading. Remove item (3)'s "body repair" wording. Increment the Section 22.2 mutation ledger to nine and add v0.47 to its version list. Do not close any finding against a carried entry by body repair again; add a gate that fails when any `ENTRY_v0.<n>` seal for n < VERSION changes between consecutive HISTORY files, which requires the prior HISTORY to be held outside the packet.
- **Cross-reference:** Section 0.1 append-only rule; Section 22.2 self-consistent-forgery boundary; correction (ay) as the compliant template; F-S01-47-03, F-S01-47-06, F-S01-47-07.

### F-S01-47-02 [HIGH] -- Standing-boundary count declared 29, enumerated 30

- **Locus:** `xz_protocol_v0_47.md` line 1219, v0.47 closing paragraph.
- **Substance:** element-wise diff against the v0.46 list returns 27 items carried verbatim, 3 additions, 0 removals: "build.py f-string nested quotes require Python 3.12+ (F-S07-46-02)", "[3a] fb_spec omits FB-7b locus assertion (F-S07-46-03)", and "trust-roots generated timestamp ungated". 27 + 3 = 30. The entry declares 29. The declared delta of +2 corresponds to register items (9) and (10) only; the third addition derives from correction (ay) and was not carried into the count. Under the same parenthesis-aware split, v0.42 through v0.46 are all internally consistent (22/22, 23/23, 24/24, 25/25, 27/27), so this is a first occurrence at v0.47. No gate covers the boundary count: [9f] checks the register only.
- **Disposition:** correct 29 to 30. Add gate [9g] extracting the declared count and the parenthesis-aware item count from the current entry and failing on inequality. This closes the surface that produced this defect and matches the treatment already given to the register by [9f].
- **Cross-reference:** F-S01-47-04; recurrence of the class corrected by (aw) at v0.46 (declared tally irreconcilable with enumeration).

### F-S01-47-03 [HIGH] -- Register item (7) declares a body repair that is not locatable on shipped bytes

- **Locus:** `xz_protocol_v0_47.md` line 1213, register item (7); repair map line 1217.
- **Substance:** item (7) reads "F-S08-46-01 HIGH CLOSED via body repair: boundary list description corrected (1-seat, carrying)". The v0.46-to-v0.47 boundary-list diff shows zero description changes; all 27 carried items are byte-identical. No lettered repair [a] through [g] mentions the boundary list. No other locus in the protocol describes a boundary list. A carrying-seat HIGH finding is therefore declared CLOSED with no repair exhibited on the bytes. Two readings are available and the packet cannot distinguish them: the repair did not land, or it landed inside the sealed v0.46 entry, in which case it is a second instance of F-S01-47-01.
- **Disposition:** exhibit the corrected locus with before and after bytes, or re-disposition item (7) to OPEN and carry F-S08-46-01 forward. If the locus is inside the v0.46 entry, absorb under the F-S01-47-01 disposition instead.
- **Cross-reference:** F-S01-47-01; F-S01-47-04; Section 22.3 Class B (concealed defect).

### F-S01-47-04 [MEDIUM] -- Repair map omits the boundary-list update, the exact defect correction (ay) closes

- **Locus:** repair map [a] through [g], line 1217; correction (ay), line 1215.
- **Substance:** (ay) exists because a v0.46 repair was "substantively repaired in the bytes but omitted from the declared repair map". At v0.47 the boundary list changed by three items and no lettered repair records it. v0.46 recorded the analogous change explicitly as its repair [e] with the count transition stated. The class closed in this entry recurs inside this entry.
- **Disposition:** add repair [h] recording the standing-boundary list update with the count transition 27 to 30 and the three item texts. Adopt the standing rule that any change to the boundary list, the register, or the correction sequence requires a lettered repair.
- **Cross-reference:** correction (ay); F-S01-47-02; F-S01-47-03.

### F-S01-47-05 [MEDIUM] -- FB-7b Post-v0.31 note carries two incompatible round indices in one sentence

- **Locus:** Section 25, FB-7b row, Post-v0.31 note (line 758). Landed by repair [e].
- **Substance:** the sentence reads "CONV R1/R2 on v0.41/v0.42 and Convergence Rounds 2-5 on v0.43-v0.46". The first clause assigns R2 to v0.42; the second assigns Round 2 to v0.43. The sealed v0.43 entry fixes "Convergence Round 1 on v0.42 recovery bytes", so the second clause matches the sealed scheme and the first does not. A reader cannot resolve which round produced which HALT from a FREEZE-BLOCKER row. Separately, the blanket "Convergence Rounds 2-5 produced Class A carrying-seat HALTs" is imprecise for R5, where the same row records a carrying CONDITIONAL PASS two sentences later.
- **Disposition:** adopt the sealed numbering exclusively. Rewrite as: pre-recovery convergence audits on v0.40 and v0.41 bytes, and Convergence Rounds 1-5 on v0.42 through v0.46 bytes, produced Class A carrying-seat HALTs at every round except R5, where Kimi K3 Seat 2 returned CONDITIONAL PASS and Kimi K3 Seat 8 HALTed.
- **Cross-reference:** sealed v0.43 entry; repair [e]; F-S01-47-06.

### F-S01-47-06 [MEDIUM] -- Repair [g] quotes a string that is not the landed text

- **Locus:** repair [g], line 1217, versus v0.46 entry, line 1202.
- **Substance:** [g] presents "4 deployed seats, 3 with verified independence, 1 with independence structurally false (F-S01-45-00)" in quotation marks. That string occurs once in the packet, inside [g] itself. The text at the repair locus reads "4 deployed seats (Opus 5, Kimi K3, Gemini, GPT; 3 with verified independence, 1 with independence structurally false per F-S01-45-00)". The repair map quotes a paraphrase as if it were bytes. Where a repair map is the only human-readable index of what changed, a paraphrase in quotation marks defeats the index.
- **Disposition:** quote landed bytes verbatim in every lettered repair, or drop the quotation marks and describe. Prefer verbatim.
- **Cross-reference:** F-S01-47-01; F-S01-47-04.

### F-S01-47-07 [MEDIUM] -- Section 22.2's detection claim is falsified by this build

- **Locus:** Section 22.2, line 718.
- **Substance:** the section states that for carried entries v0.1 through v0.46, "any in-place change to any carried entry or to Section 27's non-entry text breaks the derivation, because two independent SHA-256 matches must hold simultaneously." This build contains a declared in-place change to a carried entry and returns rc=0 with 0 FAIL. The section's own next sentences describe the residual blind spot, but frame it as an adversarial forger regenerating `HISTORY.sha256`. The producer's ordinary declared repair route sits inside that blind spot, which the current wording does not convey. The two matches are not independent: both derive from the shipped `HISTORY.sha256`, which the producer regenerates each build.
- **Disposition:** narrow the sentence to "detects any in-place change not accompanied by regeneration of HISTORY.sha256", and add a sentence stating that the producer's own repair operations fall inside the residual class, so external anchors are load-bearing for producer error and not only for adversarial forgery.
- **Cross-reference:** F-S01-47-01; Section 22.2 residual-blind-spot sentence.

### F-S01-47-08 [LOW] -- Section 22.2 mutation tally goes stale on absorption

- **Locus:** Section 22.2, "eight recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, and v0.41".
- **Substance:** the tally verifies as correct through v0.41. It does not include the v0.47 event. This finding is contingent on F-S01-47-01: if that finding is upheld, the tally is nine across seven versions from the moment v0.47 seals.
- **Disposition:** update to nine and add v0.47 to the list when absorbing F-S01-47-01. If F-S01-47-01 is disputed, record the dispute rather than leaving the tally silent.
- **Cross-reference:** F-S01-47-01; v0.18 entry tally derivation.

### F-S01-47-09 [LOW] -- Axiom-3 occasion counter silently discontinued

- **Locus:** v0.47 entry versus v0.45 ("consecutive occasion 4") and v0.46 ("consecutive repair round, occasion 5").
- **Substance:** two consecutive entries carry an Axiom-3 recurrence occasion counter. The v0.47 entry carries none, and no register item or correction records its retirement. The parallel fully-landed-repair counter continues correctly to occasion 3. A counter that stops without disposition is indistinguishable from a counter that was forgotten, and the v0.46 register already flags an ordinal in this family as non-derivable from bytes.
- **Disposition:** either record the occasion or record the retirement with its rationale. If the series is retired, add "Axiom-3 occasion counter retired" as a standing-boundary item so the absence is legible.
- **Cross-reference:** v0.46 register item (7); [9d] ordinal-recurrence gate.

### F-S01-47-10 [LOW] -- Correction (ay) rests on bytes not shipped in this packet

- **Locus:** correction (ay), line 1215.
- **Substance:** (ay) asserts the v0.46 shipped trust-roots file carried "2026-08-07T20:00:00Z", refreshed from stale "2026-07-31" values. Neither the v0.46 file nor the v0.45 file ships here. The v0.47 file carries `2026-08-07T20:00:00.000000Z`, a compatible but not identical rendering. The EXTERNAL count remains 1 and this claim is not inside the tagged span. The claim is plausible and unverifiable at this seat.
- **Disposition:** mark substrate-conditional, or extend the EXTERNAL tag to cover correction records that assert prior-version byte states. Quote timestamps at full precision.
- **Cross-reference:** F-S01-47-00 (Mode A confidence NIL for pre-v0.47 bytes); [9c] provenance tag validation.

---

## S-3. Framework probes (Fractal / Hurst / Fibonacci)

Applied after standard verification, as dispatched. Reported with their own confidence bounds; two of the four requested probes return null and are reported as null.

**Probe 1 -- Hurst exponent of the defect series.** HALT counts R1 through R5, using the (aw)-corrected R3 value: 3, 8, 9, 4, 7. Rescaled range on the mean-adjusted cumulative series gives R = 4.60, S = 2.315, R/S = 1.987, and a single-point estimate H = log(R/S)/log(n) = 0.427. **This number should not be used.** At n = 5 the single-point R/S estimator has no usable confidence interval and cannot distinguish 0.43 from 0.50. The requested probe is not estimable on this series.

The estimable quantity is the register throughput: declared register items at v0.42, v0.44, v0.45, v0.46, v0.47 are 10, 11, 8, 10, 10. Mean 9.8, coefficient of variation 11 percent. Across five repair rounds the defect count per round is stationary. What has changed is defect class, not defect count: the findings have migrated almost entirely into amendment-entry prose. The convergence series is converging in locus and not in volume, and no entry states this.

**Probe 2 -- Fractal dimension of gate coverage.** build.py's own [11] gate reports 29,559 semantically gated characters against 294,521 total, or 10.0 percent, with Section 27 at 64.7 percent of the text and entirely outside body scope. D = log(29,559)/log(294,521) = 0.817. Below 1: the gated set is sparse and Cantor-like, not a covering.

The load-bearing result is the joint distribution. All three v0.47 substantive defects (F-S01-47-01 mutation route, F-S01-47-02 boundary count, F-S01-47-03 unlocatable repair) landed in the ungated 90 percent. Three of three. Under independence this is unremarkable at p ~ 0.73, so the sample proves nothing on its own, but the mechanism is not statistical: each defect sits on a surface that no gate reads, and each prior round's defects did too. The gates are not sampling the artifact; they are covering the surfaces where errors have already been caught. Gate coverage is a lagging index of past findings, which is why adding [9g] closes the boundary-count surface and predicts nothing about where round 7 fails.

**Probe 3 -- Fibonacci / golden ratio. NULL.** Seat counts 4, 8, 12, 4, 8, 4 give successive ratios 2.00, 1.50, 0.33, 2.00, 0.50. Boundary counts 20, 22, 23, 24, 25, 27, 30 give 1.100, 1.045, 1.043, 1.042, 1.080, 1.111. HALT ratios per round give no monotone sequence. Nothing approaches 1.618 and nothing approaches it from either side. The seat counts are chair-selected, not emergent, so a phi structure would have indicated an artifact of scheduling rather than a property of the system. The probe returns null and is reported as null; no 5-3-2 proportion is claimed for the section structure.

**Probe 4 -- Dead-space analysis. GROWING.** The disclosed standing-boundary list runs 20, 22, 23, 24, 25, 27, 30 from v0.38 to v0.47, monotone non-decreasing, with zero retirements recorded at any version. Item 20 of that list is "no boundary-retirement mechanism", so the list contains the reason it can only grow. Boundaries now exceed register items 3 to 1 per round. This is not the renal-vasculature equilibrium the framework model anticipates, where dead space is a stable fraction of a fixed vascular volume. It is monotone accumulation against a fixed gate set: the ungated share is stable at roughly 90 percent while the enumerated known-ungated defects grow about one per version. FB-8's exit condition requires that every prose claim in the current entry be verified against bytes before sealing, which is a manual control on a surface growing faster than the gates that could replace it.

**Probe 5 -- Self-similarity across scales. CONFIRMED, three scales.** The same shape recurs. At sentence scale: a declared count of 29 above an enumeration of 30 (F-S01-47-02). At entry scale: a declared repair map of seven letters above a set of landed changes that is larger and differently worded (F-S01-47-03, F-S01-47-04, F-S01-47-06). At series scale: a declared convergence trajectory above a stationary defect throughput of about ten per round (Probe 1). In each case a summary asserted from working memory diverges from the enumeration beneath it, and in each case the enumeration is present in the same document. This is the recurrent class the dispatch names, and it is scale-invariant, which is the one genuinely fractal property this artifact exhibits. It also predicts the failure mode of the fix: adding [9g] gates one sentence-scale instance and leaves the entry-scale and series-scale instances untouched. The general control is not another count gate but a rule that no summary cardinal may be authored except by deriving it from the enumeration it summarizes.

---

## S-4. Verdict

**HALT.**

Class A exists. F-S01-47-02 is Class A on the definition in Section 22.3: a sealed claim false on the shipped bytes, wrong count. F-S01-47-03 is Class B: an error the entry does not disclose. F-S01-47-01 is both, and is additionally a violation of the append-only rule that Section 0.1 declares binding on every version, executed through the exact residual channel Section 22.2 identifies and in the same build that claims the program's first external-anchor append-only verification.

**Severity ledger:** 1 CRITICAL / 2 HIGH / 4 MEDIUM / 3 LOW / 1 INFORMATIONAL. Eleven findings.

**Seat weight.** This is a producer-family advisory seat. This HALT is not binding under Section 22 item 7. It is also not independent: see F-S01-47-00, which should be resolved before this seat's findings are counted toward any convergence tally.

**Recommendation.** F-S01-47-01 cannot be adjudicated inside the packet. It requires a seat holding v0.46 bytes to recompute the v0.46 `ENTRY_v0.46` seal and compare it against `36f1787a6c34ad16cba769f2d3610ad24e506184f456abc7c8eb2e21906d2f0a` in the shipped `HISTORY.sha256`. A mismatch confirms the mutation directly; a match falsifies this finding outright and should be recorded as such. That check is cheap, decisive, and available to any seat that retained its v0.46 dispatch. Run it before absorbing anything else in this report.

---

# Bismillah ir-Rahman ir-Rahim
