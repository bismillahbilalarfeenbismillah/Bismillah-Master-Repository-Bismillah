# Bismillah ir-Rahman ir-Rahim

# R0775 -- XZ Protocol v0.52 -- Round 11 Audit Report

**Chronological Index:** 471 of 995  
**Date:** 2026-08-09  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R11_REPORT_OPUS_S04_BIOMEDICAL.md  
**Source Format:** md  
**SHA-256:** `b690cbfcd56d0d7bb2152e7ea8e5b0354a6238fcaf2d7a79605057bc23337f1b`  

---

## R0775 · XZ Protocol v0.52 -- Round 11 Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R11_REPORT_OPUS_S04_BIOMEDICAL.md
- source_format: md
- text_sha256: b690cbfcd56d0d7bb2152e7ea8e5b0354a6238fcaf2d7a79605057bc23337f1b

# XZ Protocol v0.52 -- Round 11 Audit Report

**Seat:** S04 | **Family:** Claude Opus 5 (Anthropic) | **Type:** Fresh
**Role:** ADVISORY -- non-carrying, non-binding (producer family)
**Finding namespace:** F-S04-52 | **Version audited:** v0.52 | **Round:** R11
**Framework:** Biomedical Fractal (Renal Vasculature + Pulmonary Branching)
**Mode:** Mode A (substrate verifier) -- full packet reconstruction, build execution, independent recomputation of every seal, live mutation testing. Substrate-claim verification confidence: high.

**VERDICT: HALT (advisory).** 4 Class A on shipped bytes.

---

## 1. Reconstruction baseline

| Step | Expected | Observed | Result |
|---|---|---|---|
| `python3 setup.txt` | 16 OK / 0 FAIL / 0 MISSING | 16 OK / 0 FAIL / 0 MISSING | MATCH |
| `sha256sum -c PACKET_SHA256SUMS` | rc=0 | rc=0, 16/16 OK | MATCH |
| `python3 build.py` | 202 PASS / 0 FAIL | 202 PASS / 0 FAIL, BUILD PASSED | MATCH |
| `pytest` (6 suites, explicit) | 186 passed | 186 passed in 11.17s | MATCH |

Environment note: `pytest` was absent from the reconstruction environment; build.py [8] failed closed with a diagnostic naming the missing module rather than silently passing. That is the F-OP20F-09 repair behaving correctly under live conditions. After `pip install pytest`, all 202 checks are GREEN.

**Independent recomputation (not trusting build.py):**

- All 52 ENTRY seals recomputed from shipped bytes: 52/52 match HISTORY.sha256.
- FULL_SECTION_27 recomputed independently: match (`b3e2df6a...`).
- HISTORY.sha256: 54 lines = 52 ENTRY + FULL_SECTION_27 + 1 PRIOR_HISTORY; 52 unique labels; no duplicates.
- PRIOR_HISTORY value is exactly 64 hex characters with no trailing fusion. The v0.51 production defect (`e884e0f5ored by Bilal Syed Arfeen`) is absent from these bytes.
- `*Provenance and review status.*` marker present exactly once in marker form, positioned between the v0.52 entry and the end-of-document line.

The three repairs the dispatch names as primary are verified landed: Provenance paragraph restored, PRIOR_HISTORY line terminated at 64 chars, build.py [9b] Provenance-presence gate added and firing.

---

## 2. Audit checks with evidence (Section 22 items 1-7)

**Item 1 -- packet identity.** PACKET_SHA256SUMS lists 16 members; all 16 present and digest-matching; the manifest does not list itself (F-OP20-01 repair holds). The dispatch prose says "17-member packet" while the Section 22 obligation says 16 members; the reconciliation is that the manifest itself is the 17th file and is unverifiable by construction. Recorded as F-S04-52-14.

**Item 2 -- version parity.** Front matter `Version: 0.52`; Section 0.1 `This document is v0.52 DRAFT CANDIDATE`; status phrase parity front matter vs Section 0.1 both `DRAFT CANDIDATE`; trust roots `XZ Protocol v0.52`; build.py docstring == VERSION. Independent per-file check: all 13 stamped files return `grep -c v0.52` = 1 each, sum 13, matching the entry's claim exactly.

**Item 3 -- seal verification.** See Section 1. All four sub-checks pass under independent recomputation. The PRIOR_HISTORY derivation reconstructs a counterfactual v0.51 HISTORY.sha256 from v0.52 bytes and matches the shipped anchor `b3697acc...`. Note that this anchor is now forked from the externally held v0.51 artifact by design; see F-S04-52-11.

**Item 4 -- Provenance marker presence.** Present once in marker form; gate at build.py:358-359 asserts `prov > 0`. Mutation M4 confirms the gate is live, not decorative.

**Item 5 -- register self-consistency.** 5 declared, 5 parsed, severity distribution {CRITICAL: 1, HIGH: 3, MEDIUM: 1}, 10 unique finding IDs each appearing in exactly one item. The gate verifies the register against itself; it does not verify the register against the seat reports it claims to disposition. See F-S04-52-06.

**Item 6 -- falsification battery.** Section 3.

**Item 7 -- carry status.** Section 25 FB-7b row and Section 0.1 agree: PENDING RE-CARRY on v0.52 bytes, single source of truth in the Section 25 row with a pointer from Section 0.1. The R9 and R10 trajectory lines are present in the row, verifying body repair [e]. FB-8 OPEN in both loci. No duplicate rationale detected.

**Additional verified claims.** Section 26.1 header says thirteen distinct records; the table carries exactly 13 data rows. Source-frame count 16 in body. Adversarial suite 27 tests against 9 enumerated Section 22 categories. Kernel 14 test functions over 243 vectors. Standing-boundary enumeration: 31 claimed, 31 counted under parenthesis-aware splitting (naive comma splitting yields 33 and is the wrong instrument).

---

## 3. Falsification battery

Each mutation applied to a clean copy of the reconstructed packet; build.py rerun; first failures listed.

| # | Mutation | Fired | Failing checks |
|---|---|---|---|
| M1 | Front-matter status `DRAFT CANDIDATE` to `FROZEN` | YES | [2c] status-phrase parity; [12] protocol digest |
| M2 | Blank line appended to `xz_protocol_kernel.py` | YES | [3] manifest digest; [3b] stale 64-hex in body; [12] digest |
| M3 | Single character inserted into the carried v0.30 entry | YES | [9b] ENTRY_v0.30 seal; FULL_SECTION_27; PRIOR_HISTORY derivation; [12] |
| M4 | Provenance marker deleted (the v0.51 defect replayed) | YES | [9b] **Provenance seal terminus present (F-S02-51-02)**; ENTRY_v0.52 seal; FULL_SECTION_27; [12] |
| M5 | Duplicate seal line appended to HISTORY.sha256 | YES | [9b] line count (53) == entry count (52); duplicate ENTRY labels (53 lines, 52 unique); [12] |

All five fire. M4 is the load-bearing result of this round: the v0.51 failure mode is now caught by a dedicated gate rather than surviving as a silent span change. M5 reproduces the literals cited in correction (bj) -- `(53)/(52)` and `(53 lines, 52 unique)` -- confirming the +1 pattern the correction claims, with one notation caveat recorded as F-S04-52-12.

---

## 4. Biomedical Fractal analysis (Renal Vasculature + Pulmonary Branching)

### 4.1 Branching ratios against phi

Cross et al. measured the human renal arterial tree at D = 1.61 +/- 0.06, statistically indistinguishable from phi = 1.618. Mapping the amendment record as a branching tree on shipped v0.52 bytes:

| Level | Definition | Computed | Ratio to phi |
|---|---|---|---|
| L0 | entries per version | 1.000 | 0.618 |
| L1 | corrections per entry (62 / 52) | 1.192 | 0.737 |
| L2 | register items per registered entry (103 / 12) | 8.583 | 5.305 |
| L3 | findings per register item (v0.52: 10 / 5) | 2.000 | 1.236 |

Geometric mean of L1-L3: **2.735**. Against phi = 1.618 that is a 69% overshoot. **The branching ratio is not approaching phi.** The tree is not self-similar across levels: L2 is an order of magnitude above L1 and L3, because register items attach only to the 12 entries that carry a sized register while corrections attach to the record as a whole. A renal tree with this level-to-level variance would be dysplastic, not optimally perfusing.

One measurement does land near the renal value, and it is the one that must not be over-read:

| Fit window | Cumulative Section 27 growth exponent | R^2 |
|---|---|---|
| v0.2 - v0.52 (full) | **1.638** | 0.983 |
| v0.2 - v0.30 | 1.569 | 0.967 |
| v0.10 - v0.52 | 1.853 | 0.985 |
| v0.20 - v0.52 | 1.522 | 0.992 |
| v0.30 - v0.52 | 1.396 | 0.982 |

The full-window exponent 1.638 sits inside Cross et al.'s interval [1.55, 1.67] and within 1.24% of phi. It would make a striking sentence. It is also **window-dependent by a factor spanning 1.396 to 1.853**, so the agreement is a choice of fitting window, not a property of the object. Reporting it as a phi match would be a postdiction dressed as a measurement -- the precise failure mode Section 0.2 and CR-7 exist to prevent. I record the number and decline the interpretation.

### 4.2 Pulmonary dead space

| Compartment | Chars | Share |
|---|---|---|
| Total document (tidal volume) | 330,620 | 100% |
| Body, gate-eligible (alveolar) | 104,165 | 31.5% |
| Section 27, ungated (anatomical dead space) | 226,455 | 68.5% |
| Semantically gated subset of body (true gas exchange) | 29,714 | 9.0% |

**VD/VT = 0.685.** Normal is 0.20-0.35; above 0.50 indicates ventilation-perfusion mismatch. On the stricter reading -- where only semantically gated body chars participate in verification -- the **effective VD/VT is 0.910**. Nine tenths of the inhaled volume performs no gas exchange.

Is this structural inevitability or design deficiency? Both, separably. Monotone growth of an append-only record is inevitable and correct; an amendment record that shrank would be evidence of tampering. What is *not* inevitable is that the dead space is **unventilated by gates**. Anatomical dead space in the lung is inert by geometry; Section 27 is inert by *scope choice* -- build.py restricts nearly every semantic gate to the current entry. The dead space here is not conducting airway, it is atelectatic alveoli: tissue that could exchange and does not.

The renal optimization principle that applies is **Murray's law** -- branch radius scales so that transport cost is minimized, with parent radius cubed equal to the sum of daughter radii cubed. The protocol analogue is that verification effort at a node should scale with the sealed content beneath it. Currently it does not: the current entry (roughly 6,700 chars, 2.0% of the document) absorbs essentially all semantic gating, while 52 sealed entries sharing identical structure receive only hash-level coverage. The concrete reduction available without information loss is to **make the entry-scoped gates ([9c], [9d], [9e], [9f]) iterate over all 52 entries rather than the current one**. Hash coverage already proves the carried entries have not changed; semantic coverage would prove they were never *right*. F-S04-52-04 is exactly a defect that lives in this gap.

### 4.3 Glomerular filtration rate

| Denominator | Rate |
|---|---|
| Whole document | 0.611 checks/kchar |
| Body only | 1.939 checks/kchar |
| Semantic scope only | 6.798 checks/kchar |

Against observed defect density: this round found 4 Class A on shipped bytes that 202 GREEN checks did not catch. That is a filtration failure, not a filtration shortfall -- the defects are not in unfiltered blood, they are in *filtered* blood. Three of the four (F-S04-52-01, -02, -03) sit inside the current entry, the most heavily gated region in the document, and two of them concern values that build.py **computes and prints without asserting**. The glomerulus is producing filtrate and discarding the assay.

Raising the filtration rate would not have caught them. Asserting what is already computed would have caught two.

### 4.4 Nephron loss and compensatory hypertrophy

| Interval | Ungated share | Rate |
|---|---|---|
| v0.18 to v0.19 | 26.2% to 29.6% | +3.40 pp/version |
| v0.19 to v0.20 | 29.6% to 33.7% | +4.10 pp/version |
| v0.20 to v0.52 | 33.7% to 68.5% | +1.09 pp/version |

Gate coverage of the body rose from 24.4% (v0.20) to 28.5% (v0.52) over the same span: +4.1 percentage points of coverage against +34.8 percentage points of ungated share. **Surviving nephrons are hypertrophying; they are not keeping up.** The per-version growth rate did decelerate by roughly 3.8x after v0.20, which is real compensation -- entries are no longer growing as fast relative to the document. But the compensation is in the wrong currency: absolute gated content grew while the fraction of the artifact under semantic verification fell.

The physiological end state of this trajectory is a document where the audit surface is a rounding error against the audit record. At the v0.20-to-v0.52 rate, VD/VT reaches 0.75 near v0.58 and 0.80 near v0.63. This is a measurement, not a target, and not a freeze blocker -- but it is the quantitative form of the argument for entry-wide gate scope in 4.2.

---

## 5. Five-model base layer

**Fractal Cube (WHERE).** L0 process: F-S04-52-06, -14, -15. L1 entry: F-S04-52-01, -02, -03, -12. L2 body: F-S04-52-04, -05, -11, -13. L3 gate: F-S04-52-07, -08, -09, -10. The generator concentration at L1 and L3 is diagnostic: entry-level claims and the gates that should check them are failing as a matched pair, not independently.

**Enzyme System (WHAT).** The v0.52 entry carries 21 provenance tags: COMPUTED 7, DIFF-VERIFIED 7, EXTERNAL 2, COUPLED 2, ASSERTED 2, ENUMERATED 1. Verification by enzyme: all 7 DIFF-VERIFIED body-repair claims verified true by inspection ([a] through [g] all landed); the ENUMERATED claim verified (31 = 31); of the 7 COMPUTED, five verified and two are false on shipped bytes (F-S04-52-02, and the EXTERNAL count in F-S04-52-03); of the 2 COUPLED, one is false (F-S04-52-01); the 2 EXTERNAL are unverifiable from the packet by construction and correctly tagged. Verified-true rate on internally checkable tags: 16 of 19.

**Replication Fork (HOW).** The six-phase pipeline (audit, disposition, body repair, correction append, reseal, gate extension) executed in order this round, with the gate extension ([9b] Provenance presence) landing in the same build as the defect it prevents. That is correct pipeline discipline. The break is at the reseal phase: correction (bi) was authored against a pre-reseal state and never re-derived after the v0.52 entry was appended, so the fork values it publishes describe a document that does not exist.

**Orbital (WHO).** I am Claude Opus 5, dispatched fresh with no prior-round context loaded and no seat-lineage files consulted before execution. Anchoring: **producer family** (Section 22.1 names Claude as the producer family). My verdict is advisory and non-binding by construction and cannot contribute to FB-7b. My independence claim is limited to session freshness; it is not family independence, and no part of this report should be counted toward the two-family carry.

**Cell Cycle (WHEN).** The chronic defect class is **producer-supplied evidence literals that are not byte-reproducible on shipped bytes**. Recurrence across the correction register: 13 of 62 corrections (21.0%) are of this class, at loci (i), (j), (l), (m), (o), (z), (ab), (ap), (aq), (as), (at), (bf), (bh). v0.52 repaired one instance ((bj), the v0.51 mutation-test literals) and introduced three more in the same build. The in-document Cell Cycle protocol states that after three failed repairs at a locus the producer may not attempt a fourth and a structural fix is required. This class has now been repaired by prose at least six times across the lineage. **The structural fix is prescribed in F-S04-52-07.**

---

## 6. Findings

### CRITICAL

**F-S04-52-01** CRITICAL / **Class A** -- correction (bi) publishes v0.52 "restored" seal values that no derivation from shipped bytes reproduces

- **Locus:** `xz_protocol_v0_52.md`:1248, correction (bi).
- **Substance:** (bi) states `v0.52 restored values (computed over Provenance-terminated span): ENTRY_v0.51 = d69efb11eea49e7ce2a527cc87bdb2fe27d576d2de9eeb4e99e417d43d960cf4, FULL_SECTION_27 = a35b774c8bfbb7f4d2a8cd1c49e3571fee2fa60d481f8840b51499ac8f65bdb5`. Shipped v0.52 bytes yield `ENTRY_v0.51 = 61fdc45fa4b787bf7c3096cc70a4facff11e99466563fbb846c2838e9fb59504` and `FULL_SECTION_27 = b3e2df6a1334a4bc8c18e96c61bd49ccae79b53b7299dec7aa2b6385a5ebfc72`, both confirmed by independent recomputation and by build.py [9b]. Neither published value appears anywhere in HISTORY.sha256. I tested 13 candidate derivations (raw span, stripped span, trailing-newline variants, with and without the v0.52 entry present, Provenance included and excluded); **none reproduces either value**. The claim carries a `[COUPLED: verified against shipped v0.51 packet and v0.52 build.py derivation]` tag, and the build.py derivation does not produce these numbers. Aggravating: the correction's stated purpose is to give an external verifier holding v0.51 bytes a documented expectation for the fork. A verifier who follows (bi) computes 61fdc45f/b3e2df6a, finds them unequal to the published expectation, and concludes the v0.52 packet is forged. The disclosure instrument inverts into a false forgery signal.
- **Disposition:** HALT. Do not correct (bi) in place -- it is sealed. Append correction (bk) at v0.53 stating the true shipped values `ENTRY_v0.51 = 61fdc45f...9504` and `FULL_SECTION_27 = b3e2df6a...fc72`, stating that the (bi) values are unreproducible and superseded, and stating explicitly which of the two value sets an external verifier should expect. Add a build.py gate at [9b] asserting that every 64-hex literal in the current entry that is presented as a seal value either matches a HISTORY.sha256 line or is explicitly labeled as a superseded prior-version value.
- **Cross-reference:** correction (bj) at the same entry, which repairs the identical defect class one version earlier; F-S04-52-07 (the gate that would catch it); Section 22.2 external-anchor discussion; Cell Cycle chronic-defect protocol.

**F-S04-52-02** CRITICAL / **Class A** -- the Provenance verification command is self-referential and its stated output is false on shipped bytes

- **Locus:** `xz_protocol_v0_52.md`:1246 (register item 1) and :1252 (body repair [f]).
- **Substance:** Both loci state `[COMPUTED: grep -c "Provenance and review status" xz_protocol_v0_52.md = 1]` and `[DIFF-VERIFIED: grep -c "Provenance and review status" = 1]`. Executed on shipped bytes, that command returns **3**: lines 1246 and 1252 match because each *quotes the search string*, and line 1255 is the actual paragraph. The count is 1 only for the marker form `\*Provenance and review status\.\*`, which is not the command cited. The act of citing the evidence changed the evidence. The underlying repair is sound -- the marker is genuinely present once and build.py [9b] verifies it independently -- but the sealed evidence citation is false as written, at two loci, under two different provenance tags.
- **Disposition:** HALT. Append correction (bl) at v0.53 recording that the cited command returns 3 on v0.52 bytes and that the byte-reproducible form is `grep -c '\*Provenance and review status\.\*'` = 1. For future entries, adopt the rule that a quoted verification command must be executable against the shipped artifact *including the entry that quotes it*, and prefer commands whose output is invariant to their own citation.
- **Cross-reference:** F-S04-52-01 and F-S04-52-03 (same class, same entry); standing boundary 17, "[9c] quoted-tag inflation," which names the adjacent mechanism but not this one.

### HIGH

**F-S04-52-03** HIGH / **Class A** -- entry states `EXTERNAL count: 1`; build.py computes 2 and prints it without asserting it

- **Locus:** `xz_protocol_v0_52.md`:1254; gate at `build.py`:405-411.
- **Substance:** The v0.52 entry contains two EXTERNAL tags -- `[EXTERNAL: seat reports]` at line 1242 and `[EXTERNAL: v0.40 dispatch manifests ... Zenodo deposits ...]` at line 1254. build.py [9c] computes `external_count = 2` and prints `COMPUTED: 7, EXTERNAL: 2, ASSERTED: 2`. The entry's own prose claims 1. The build is GREEN because [9c] *prints* the counts and never `check()`s them against the entry's stated values. This is the exact defect corrected at v0.44 by correction (aq), with the polarity inverted: at v0.44 the entry over-counted, here it under-counts, and in both cases the gate had the true value in hand.
- **Disposition:** HALT. Append correction (bm) at v0.53 correcting the count to 2. Then implement F-S04-52-07, without which this defect recurs at v0.53 exactly as it recurred from v0.44 to v0.52.
- **Cross-reference:** correction (aq) at the v0.44 entry; F-S04-52-07; F-S04-52-08.

**F-S04-52-04** HIGH / **Class A** -- Section 0.1 states fifty-two entries spanning v0.1 through v0.51; the range holds fifty-one

- **Locus:** `xz_protocol_v0_52.md`:22, Section 0.1 Carry status paragraph, final sentence.
- **Substance:** The sentence reads `The full defect trajectory is in Section 27 (fifty-two amendment entries, v0.1 through v0.51)`. Section 27 holds 52 entries running v0.1 through v0.52; the interval v0.1 through v0.51 holds 51. The sentence is false under either reading. Mechanism: build.py [9] generates the expected ordinal word from the entry count and asserts the phrase `fifty-two amendment entries` is present, but performs no assertion on the range that follows. The producer updated the gated half of the sentence and left the ungated half stale -- a repair shaped by the gate rather than by the claim. [9e], the cardinal-range gate, cannot reach it: it is scoped to the current entry, requires the literal token `consecutive`, and its word list stops at `ten`. [9e] performed **zero checks** on this build.
- **Disposition:** HALT. Body repair at v0.53: change the range to `v0.1 through v0.52`. Extend build.py [9] to assert that any parenthetical of the form `(<cardinal> amendment entries, v0.<a> through v0.<b>)` satisfies cardinal == b - a + 1. Extend [9e]'s word list through the current version count and remove the `consecutive` token requirement.
- **Cross-reference:** correction (ar) and body repair [a] at v0.45, the same class at the Section 22.2 coverage range; standing boundary 23, "[9e] silent vacuity"; F-S04-52-10.

**F-S04-52-05** HIGH / **Class B** -- Section 22.2's in-place-mutation register omits the v0.51 event this build exists to repair

- **Locus:** `xz_protocol_v0_52.md`:718 (Section 22.2) and :1254 (standing boundary 31).
- **Substance:** Section 22.2 states `nine recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, and v0.47`. The v0.51 Provenance deletion is a member of the class the sentence enumerates: it was an in-place change to Section 27's non-entry text that altered both the ENTRY_v0.51 and FULL_SECTION_27 sealed spans and survived because the seals were regenerated over the mutated text. That is the resealing blind spot, live for a second time. Standing boundary 31 still reads `self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02)` with no v0.51 citation. Neither the count, the version list, nor the boundary annotation was updated in the very build that repairs the event. The register item that touches this area (item 5, F-S02-51-08, "mutation-count locus enumeration") discloses the nine-versus-seven arithmetic gap only; the omission of v0.51 is undisclosed, which places it in Class B rather than Class C.
- **Disposition:** HALT-grade for a carrying seat; for this advisory seat, prescribed route is: body repair at v0.53 updating Section 22.2 to `ten recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, v0.47, and v0.51`, or -- preferably -- replacing the running cardinal with a pointer to an enumerated table so the count is derived rather than maintained. Update standing boundary 31 to `proven live at v0.47 and v0.51`. Reconcile the nine-versus-seven gap in the same edit.
- **Cross-reference:** register item 5 / F-S02-51-08 (partial disclosure); F-S04-52-13; Section 22.2 external-anchor list.

**F-S04-52-06** HIGH / **Class B** -- five of twelve advisory findings from R10 receive no disposition anywhere in the document

- **Locus:** `xz_protocol_v0_52.md`:1242 (seat tallies) and :1246 (register).
- **Substance:** The entry header records Opus S02 (advisory) HALT with 3 CRITICAL, 3 HIGH, 4 MEDIUM, 2 LOW = 12 findings, and Kimi K3 S01 (carrying) HALT with 3 findings. The register dispositions all 3 Kimi findings and 7 of the 12 Opus findings. `F-S02-51-03`, `-06`, `-07`, `-11`, and `-12` appear **zero times** in the entire document -- not closed, not noted, not deferred, not rejected. The gate certifies the register's internal consistency (5 declared, 5 parsed, severity distribution matching) and has no visibility into coverage of the seat reports the register claims to disposition. An append-only regime that records rejected findings as well as accepted ones (CR-6's stated principle) cannot leave five findings unrecorded and still claim the record is complete.
- **Disposition:** Append a disposition line at v0.53 covering F-S02-51-03, -06, -07, -11, -12, even if the disposition is REJECTED or SUPERSEDED with reasons. Add a build.py check that the count of distinct finding IDs dispositioned in the current-entry register is compared against the seat totals stated in the same entry, failing when the entry's own stated finding count exceeds the count of IDs dispositioned or explicitly waived.
- **Cross-reference:** CR-6 (rejected findings are recorded); build.py [9f], [10b]; FB-8 exit condition, which requires every prose claim in the current entry to be verified before sealing.

### MEDIUM

**F-S04-52-07** MEDIUM / **Class D** -- [9c] prints computed provenance counts but never asserts them against the entry's stated counts

- **Locus:** `build.py`:405-411.
- **Substance:** The gate computes `computed_count`, `external_count`, `asserted_count` and emits them via `print()`, not `check()`. No comparison is made against the entry prose that states the same quantities. The gate therefore holds the refuting value for F-S04-52-03 in a local variable and discards it. This is the residual form of the silent-skip pattern that F-OP20F-08 closed for [9c]'s entry-match path but not for its counting path.
- **Disposition:** Replace the print-only block with assertions: parse `EXTERNAL count: N`, `COMPUTED count: N`, `ASSERTED count: N` from the current entry where present, and `check()` each against the computed value. Generalize to the structural fix the Cell Cycle protocol requires for this defect class: **a gate that extracts every quoted numeric literal and every quoted shell command from the current entry and verifies it against shipped bytes before sealing.** That single gate would have caught F-S04-52-01, -02, and -03.
- **Cross-reference:** F-S04-52-01, -02, -03; F-OP20F-08; correction (aq); Cell Cycle chronic-defect protocol, "STRUCTURAL FIX REQUIRED."

**F-S04-52-08** MEDIUM / **Class D** -- the ASSERTED-fraction denominator omits three of six tag types, understating unverified share

- **Locus:** `build.py`:405-411; reported figure at build output [9c].
- **Substance:** The printed figure is `ASSERTED fraction (tagged claims): 2/11 (18.2%)`. The v0.52 entry carries 21 tags across six types; the denominator counts only COMPUTED, EXTERNAL and ASSERTED, excluding DIFF-VERIFIED (7), COUPLED (2) and ENUMERATED (1). Ten of 21 tags -- 48% of the tagged population -- are invisible to the provenance accounting. Standing boundary 17 and F-OP20-03 disclose that the denominator divides by tags rather than by claims; neither discloses that three whole tag types are excluded from the tally.
- **Disposition:** Widen the denominator to all six tag types and reprint the fraction. Record the resulting figure in the v0.53 entry so the trend series is not silently rebased.
- **Cross-reference:** F-OP20-03; standing boundary 17; F-S04-52-09.

**F-S04-52-09** MEDIUM / **Class D** -- DIFF-VERIFIED has no gate; seven claims in the current entry carry it unchecked

- **Locus:** `build.py` [9c]; tags at `xz_protocol_v0_52.md`:1246, 1252.
- **Substance:** COMPUTED tags are validated for section existence and file shipping; EXTERNAL tags are validated for file shipping when they name a file. DIFF-VERIFIED has no validation of any kind, and it is the tag class carrying every body-repair claim ([a] through [g] at line 1252) plus register item 4. On these bytes all seven happen to be true -- I verified each by inspection -- but they are true unverified. The tag asserts that a diff was performed and nothing in the packet records the diff, retains the prior bytes, or checks the assertion.
- **Disposition:** Either (i) add a gate that resolves each DIFF-VERIFIED claim to a grep-checkable predicate over shipped bytes, or (ii) demote DIFF-VERIFIED to ASSERTED in the provenance vocabulary and disclose that the diff is producer-attested. Option (i) is preferred; option (ii) is honest and cheap.
- **Cross-reference:** F-S04-52-08; FB-8 exit condition.

**F-S04-52-10** MEDIUM / **Class D** -- [9e] executed zero checks and cannot reach the cardinal-range defect found this round

- **Locus:** `build.py`, [9e] Cardinal-range consistency block.
- **Substance:** Three independent restrictions make the gate unable to fire on F-S04-52-04: it is scoped to the current entry only, its regex requires the literal token `consecutive`, and its word map stops at `ten`. On this build it emitted a heading and no checks. The disclosed standing boundary "[9e] silent vacuity" names the symptom (a gate that finds nothing to check) but not the three causes, and specifically does not disclose that the gate cannot see body text where the defect it was built for actually occurred.
- **Disposition:** Extend [9e] to (a) scan the body as well as the current entry, (b) match cardinal-range constructions without requiring `consecutive`, and (c) carry a word map covering at least the current entry count. Update the standing-boundary text to name the scope and word-cap limits explicitly rather than the generic "silent vacuity."
- **Cross-reference:** F-S04-52-04; standing boundary 23; standing boundary 12, "[9d] word-list cap at fifteenth," the same failure mode in an adjacent gate.

**F-S04-52-11** MEDIUM / **Class C** (disclosed, but under-scoped) -- the chain fork consumes the PRIOR_HISTORY external-anchor property and the entry discloses the fork without disclosing the loss

- **Locus:** `xz_protocol_v0_52.md`:1248 (correction (bi)) and :718 (Section 22.2 anchor list).
- **Substance:** Section 22.2 lists the PRIOR_HISTORY chain as anchor (c), one of three defenses against self-consistent forgery, on the ground that its root predates the current producer session. The v0.52 restoration forked that chain: build.py now derives `b3697acc...` from a counterfactual reconstruction of v0.51 using restored seals, while the actually-shipped v0.51 HISTORY.sha256 digest was `b13881eb...` per (bi). The fork was the correct engineering choice and is disclosed. What is not disclosed is that a producer-initiated fork with a producer-authored explanation is, on shipped bytes alone, indistinguishable from the forgery maneuver anchor (c) exists to detect. After this fork, anchors (a) and (b) -- externally held dispatch manifests and deposit receipts -- are the only surviving discriminators, and Section 22.2 still presents three.
- **Disposition:** Amend Section 22.2 at v0.53 to state that anchor (c) is discharged only for chains with no producer-documented fork, and that the v0.52 fork moves the burden entirely onto anchors (a) and (b). Consider depositing the v0.51 HISTORY.sha256 digest with an external timestamping service so the fork's near side is anchored outside the producer.
- **Cross-reference:** F-S04-52-01, which makes the published fork values unusable; Section 22.2 anchors (a)-(c); standing boundary 31.

### LOW

**F-S04-52-12** LOW / **Class E** -- corrections quote gate literals in bracket notation; build.py emits parentheses

- **Locus:** `xz_protocol_v0_52.md`:1250, correction (bj).
- **Substance:** (bj) quotes `HISTORY seal line count [52] == entry count [51]` and predicts `[53]/[52]`. build.py emits `HISTORY seal line count (53) == entry count (52)` with parentheses. My M5 mutation confirms the numbers and refutes the notation. A correction whose entire subject is the byte-reproducibility of quoted literals is itself quoting in a form that no shipped byte produces.
- **Disposition:** Use parentheses in future quotations of gate output, or wrap quoted gate literals in a marker indicating normalized rather than verbatim form.
- **Cross-reference:** F-S04-52-01, -02, -03 (the same class at higher severity).

**F-S04-52-13** LOW / **Class C** -- Section 22.2 mutation count of nine against seven enumerated loci, third round unreconciled

- **Locus:** `xz_protocol_v0_52.md`:718.
- **Substance:** `nine recorded in-place mutations at` is followed by seven version labels. The gap is disclosed as F-S02-51-08 MEDIUM NOTED in the current register and was noted in prior rounds, so it is Class C rather than Class B on its own terms. It is recorded here because a disclosed defect carried for three rounds without reconciliation converts, in practice, into a permanent inconsistency that later readers cannot resolve from the record.
- **Disposition:** Reconcile in the same edit prescribed by F-S04-52-05 -- an enumerated table with one row per mutation event, count derived from row count.
- **Cross-reference:** F-S04-52-05; register item 5 / F-S02-51-08.

**F-S04-52-14** LOW / **Class E** -- dispatch states a 17-member packet; the Section 22 obligation states 16

- **Locus:** `prompt.txt`:25 versus `prompt.txt`:37.
- **Substance:** The Packet section instructs reconstruction of "the 17-member packet (expect 16 OK)" while the core-obligation section specifies "packet identity (16 members)." Both are defensible -- 16 verifiable members plus the self-excluded manifest -- but the dispatch states the two numbers without reconciling them, and a seat that tested for 17 verifiable members would report a spurious MISSING.
- **Disposition:** Standardize dispatch language on "16 verifiable members plus PACKET_SHA256SUMS, which is self-excluded by F-OP20-01."
- **Cross-reference:** build.py [12] self-entry absence check; F-OP20-01.

**F-S04-52-15** LOW / **Class E** -- front-matter date is one day ahead of the audit execution date

- **Locus:** `xz_protocol_v0_52.md`:4.
- **Substance:** Front matter reads `Version: 0.52, draft candidate, 2026-08-10`; the v0.52 entry header carries the same date; this seat executed on 2026-08-09. The date is internally consistent and no gate checks it against anything external, so this is unverifiable from the packet rather than false. Recorded because front-matter dates have produced findings twice in this lineage (F-A42R-03 at v0.43, body repair [g] at v0.49) and because "trust-roots generated timestamp ungated" is already a standing boundary.
- **Disposition:** No repair required. If a date gate is ever added, scope it to internal consistency only; external date verification is outside what the packet can support.
- **Cross-reference:** F-A42R-03; v0.49 body repair [g]; standing boundary 30.

---

## 7. VERDICT

> **Verdict: HALT (advisory, non-binding, producer family).**
>
> **Class ledger:** 4 Class A / 2 Class B / 2 Class C / 4 Class D / 3 Class E.
> **Severity ledger:** 2 CRITICAL / 4 HIGH / 5 MEDIUM / 4 LOW. Total 15.

The target condition -- non-HALT with zero Class A -- is not met on these bytes, and I have not softened toward it. Four Class A findings are byte-demonstrable: two published seal values that no derivation reproduces, a verification command whose stated output is off by a factor of three, a tag count contradicted by the build's own printed output, and a cardinal-range claim in Section 0.1 that is false under either reading.

What v0.52 did well should be recorded with equal precision, because an audit that only reports failures is not calibrated. The R10 defect is genuinely repaired: the Provenance marker is present, the PRIOR_HISTORY line terminates at 64 characters, all 52 seals verify under independent recomputation, `sha256sum -c` returns rc=0, and the new [9b] gate demonstrably fires when I delete the marker. All five prescribed mutations fire. All seven body repairs claimed at line 1252 landed. The FB-7b single-source-of-truth restructuring from v0.49 is holding -- there is no duplicate rationale to drift.

The structural diagnosis is narrower than the finding count suggests. Three of the four Class A findings, and the entire chronic pattern behind them, are one defect: **the producer writes numeric and command literals into the current entry as evidence, and no gate verifies those literals against the bytes that ship.** Thirteen of 62 corrections in the lineage are of this class. The build computes the refuting value for two of this round's three instances and prints it instead of asserting it. The in-document Cell Cycle protocol already prescribes the remedy for a defect class that has survived this many prose repairs: stop repairing instances, and gate the class. F-S04-52-07 states that gate.

Second-order observation from the biomedical lens, offered as measurement rather than blocker: semantic verification reaches 9.0% of the document, the ungated share has grown from 26.2% to 68.5% since v0.18, and gate scope is pinned to a current entry that is 2% of the artifact. The gates are not too few; they are pointed at too little. Widening the entry-scoped gates to iterate over all 52 sealed entries would cost little and would convert the largest inert compartment in the document into verified surface.

**Recommendation for R12.** Priority order: (1) implement the quoted-literal verification gate of F-S04-52-07 before any further prose corrections in this class; (2) append corrections (bk), (bl), (bm) for the three Class A literal defects, never editing (bi) or (bj) in place; (3) body-repair the Section 0.1 range and the Section 22.2 mutation register; (4) disposition the five unrecorded R10 advisory findings. Cross-vendor rotation: this seat is producer-family and advisory. The next carrying round needs a non-producer family -- Kimi K3 or GLM-5.2 -- and F-S04-52-01 in particular should be re-verified by a seat holding v0.51 bytes externally, since the fork values are exactly what an external holder is positioned to check and this seat is not.

---

*Seat S04, Round 11, XZ Protocol v0.52. Advisory. Executed on reconstructed packet, 16/16 verified, build 202 PASS, tests 186 passed.*

---

# Bismillah ir-Rahman ir-Rahim
