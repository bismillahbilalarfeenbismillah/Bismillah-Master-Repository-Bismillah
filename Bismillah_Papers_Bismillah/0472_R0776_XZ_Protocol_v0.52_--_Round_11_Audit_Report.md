# Bismillah ir-Rahman ir-Rahim

# R0776 -- XZ Protocol v0.52 -- Round 11 Audit Report

**Chronological Index:** 472 of 995  
**Date:** 2026-08-09  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R11_S02_OPUS5_FRACTAL_HURST_v0.52_AUDIT.md  
**Source Format:** md  
**SHA-256:** `329b5d4487dd6a1385adf56f434a1859d2076ff618c9cbb3c64d968635f3c28a`  

---

## R0776 · XZ Protocol v0.52 -- Round 11 Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R11_S02_OPUS5_FRACTAL_HURST_v0.52_AUDIT.md
- source_format: md
- text_sha256: 329b5d4487dd6a1385adf56f434a1859d2076ff618c9cbb3c64d968635f3c28a

# XZ Protocol v0.52 -- Round 11 Audit Report

**Seat:** S02
**Family:** Claude Opus 5 (Anthropic) -- producer family
**Type:** Fresh (no prior seat context loaded before execution)
**Role:** ADVISORY -- non-carrying, non-binding
**Finding namespace:** F-S02-52
**Version audited:** v0.52 DRAFT CANDIDATE
**Round:** R11 (Convergence Round 11)
**Analytical lens:** Recursive Fractal Cube + Hurst Exponent
**Dispatch:** `R11_DISPATCH_OPUS_S02_FRACTAL_HURST.zip` (9 files)
**Report date:** 2026-08-09

**VERDICT: HALT (advisory)** -- 3 Class A, 3 Class B, 3 Class D, 2 Class E.

---

## 1. Reconstruction baseline

| Step | Expected | Observed | Result |
|---|---|---|---|
| `python3 setup.txt` | 16 OK / 0 FAIL / 0 MISSING | 16 OK / 0 FAIL / 0 MISSING | PASS |
| `python3 build.py` | 202 PASS / 0 FAIL | 202 PASS / 0 FAIL, rc=0 | PASS |
| six-suite `pytest` | 186 passed | 186 passed in 8.58s | PASS |

All three declared expectations reproduce exactly on the dispatched bytes.

**Environment note.** `pytest` was absent from the execution container. The first `build.py` run failed on `[8]` with `No module named pytest` and `Test count parsed from pytest output`. After `pip install pytest` (9.1.1) the build returned rc=0 with 202 PASS. This is the disclosed standing boundary "execution environment unsealed" behaving as documented; it is not a finding against the artifact.

**Packet integrity as received.** All 16 members verified against `PACKET_SHA256SUMS`. `PACKET_SHA256SUMS` does not list itself (F-OP20-01 control holds).

**Dispatch-level discrepancy.** `prompt.txt` describes a "17-member packet" in the Packet paragraph and "packet identity (16 members)" in Core audit obligations. 16 is correct. Recorded as F-S02-52-11.

---

## 2. Audit checks with evidence (Section 22 items 1-7)

### 2.1 Packet identity (item 2)

16/16 members OK, 0 FAIL, 0 MISSING. Reconstruction from the 9 dispatch `.txt` files is deterministic and byte-exact.

### 2.2 Version parity (item 2)

| Surface | Expected | Observed |
|---|---|---|
| Front matter `**Version:**` | `0.52,` | `0.52,` |
| Section 0.1 `This document is v0.X` | v0.52 | v0.52 |
| 12 Python files, `v0.52` stamp | 12 | 12 (one occurrence each) |
| `xz_protocol_trust_roots_PUBLIC.json` | `XZ Protocol v0.52` | `XZ Protocol v0.52` |
| Total files carrying the stamp | 13 | 13 |

The entry claim `[COMPUTED: grep -c v0.52 across 13 files = 13]` reproduces exactly.

### 2.3 Seal verification (item 2) -- independently recomputed

Recomputation was performed outside `build.py`, from the protocol bytes and `HISTORY.sha256`, using an independent implementation of the documented canonicalization.

| Object | Result |
|---|---|
| ENTRY seals | 52 entries parsed, 52 seals present, **0 mismatches** |
| `ENTRY_v0.51` | `61fdc45fa4b787bf7c3096cc70a4facff11e99466563fbb846c2838e9fb59504` |
| `ENTRY_v0.52` | `4e6a4de44336bf4535697011e1323eefdfaa45dc9e0ae5dfb0d59f608a146512` |
| `FULL_SECTION_27` | `b3e2df6a1334a4bc8c18e96c61bd49ccae79b53b7299dec7aa2b6385a5ebfc72` -- MATCH |
| `PRIOR_HISTORY` shipped | `b3697acc8561a3b3ed8336a85300b4983429d0b29bec2414045628fd86c56b97` |
| `PRIOR_HISTORY` independently derived | `b3697acc8561a3b3ed8336a85300b4983429d0b29bec2414045628fd86c56b97` -- MATCH |
| Cardinality | 52 seal lines == 52 entries |
| Duplicate labels | none (52 lines, 52 unique) |
| Entry ordering | ascending, no duplicate versions |

Counterfactual value produced inside the derivation recursion at level 51:
`FULL_SECTION_27(v0.51-terminal) = a3f07ac7fec28f3769c814abd51af7a99126bf0a2afbd80682312ff48386e9c6`.
This value is load-bearing for finding F-S02-52-02.

### 2.4 Provenance marker presence (item 2)

The asterisked literal `*Provenance and review status.*` occurs **exactly once**, at line 1255, at line start, positioned after the last amendment entry. The seal terminus is sound and the R10 Class A is genuinely closed on these bytes.

The unasterisked substring `Provenance and review status` occurs **three** times (lines 1246, 1252, 1255). See F-S02-52-03.

### 2.5 Register self-consistency (item 2)

```
[9f] Register parsed at least one item (5 found)        PASS
     Register parsed == declared (5 parsed, 5 declared) PASS
     Register: 5 items, {'CRITICAL': 1, 'HIGH': 3, 'MEDIUM': 1}
     No duplicate-severity finding IDs (10 unique)      PASS
[10b] All 10 finding IDs appear in exactly one item     PASS
```

5/5 internal consistency confirmed. The gate does not reconcile the register against the entry's own narrated seat tallies; see F-S02-52-05.

### 2.6 Section 0.1 count claims -- all verified against bytes

| Claim | Method | Observed |
|---|---|---|
| 186 test functions | AST across six suites | 14 + 29 + 29 + 18 + 27 + 69 = 186 |
| 186 collected | explicit six-suite pytest | 186 passed |
| 14 test functions exercising 243 vectors | AST on kernel suite | 14 |
| 16-source public-record manifest | `len(SOURCE_FRAME_MANIFEST)` | 16 |
| 27-test adversarial suite | AST | 27 |
| 6 modules + 6 suites, 12 distinct Python files | file inventory | 12 |
| 14 normative files | 12 + trust roots + protocol text | 14 |

### 2.7 Prohibited language (Section 0.3)

Swept every sentence containing `BSSG` for effectiveness verbs (`prevents`, `mitigates`, `reduces`, `ensures`, `guarantees`, `protects`, `stopped`, `would have stopped/caught`). Two hits, both inside the Section 0.3 prohibition register itself. The three trap phrases (`attack prevention`, `the kernel denies the attack`, `Structural Honesty has been validated`) appear only within their own negations. No `DENY_FALSE + DENY_UNKNOWN` aggregation. **CLEAN.**

### 2.8 Standing-boundary enumeration

The v0.52 entry claims `Disclosed standing boundaries -- 31 items: ... [ENUMERATED: 31 items]`. Naive comma-split yields 33 tokens; two tokens are parenthetical fragments of single items (`A-side seam (condition_a.py, SHIELD-scoped)` and `self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02)`). Corrected count = **31**. Claim VERIFIED.

---

## 3. Falsification battery

Executed against isolated copies of the reconstructed packet. `resync` = recompute `PACKET_SHA256SUMS`. `reseal` = full regeneration of `HISTORY.sha256` (all entry seals, `FULL_SECTION_27`, and the `PRIOR_HISTORY` recursion) using the documented canonicalization.

| # | Probe | Manipulation | Result |
|---|---|---|---|
| M1 | Status mutation | front matter only, `DRAFT CANDIDATE` to `FROZEN RELEASE`, resync | **CAUGHT** -- `[2c]` arity-two phrase mismatch |
| M1b | Status mutation, coordinated | front matter **and** Section 0.1, resync | **PASSED GREEN** |
| M2 | Code append | one comment line to `xz_protocol_kernel.py`, resync | **CAUGHT** -- manifest digest, trust roots, absence gate (6 FAIL) |
| M3 | Entry mutation | in-place edit of carried v0.30 entry, resync | **CAUGHT** -- entry seal, `FULL_SECTION_27`, `PRIOR_HISTORY` (6 FAIL) |
| M4 | Provenance deletion | remove marker literal, resync | **CAUGHT** -- `[9b]` fires, plus `FULL_SECTION_27` and `ENTRY_v0.52` |
| M5 | Duplicate seal line | duplicate `ENTRY_v0.50` line, resync | **CAUGHT** -- `[53]` vs `[52]`, `[53 lines, 52 unique]` |
| P6 | Provenance text substitution | marker kept, paragraph body rewritten, reseal | **PASSED GREEN** |
| P7 | Seal-span collapse (deliberate) | marker literal inserted after `## 27.` heading, reseal | **PASSED GREEN**, span = 37 of 226,502 chars |
| P7b | P7 + non-entry-text injection | fabricated carry note between entries, reseal | **PASSED GREEN** |
| P7c | Control: injection + reseal, no collapse | same injection, reseal only | **PASSED GREEN** |
| P8 | Seal-span collapse (accidental) | asterisked quotation inside the v0.52 entry, reseal | **PASSED GREEN**, 6,335 chars silently unsealed |

**(bj) mutation-test claim verified.** The entry states `[COMPUTED: mutation test on v0.52 bytes yields [53]/[52] and [53 lines, 52 unique], confirming the +1 pattern]`. Probe M5 produced exactly:

```
FAIL: HISTORY seal line count (53) == entry count (52)
FAIL: No duplicate ENTRY labels in HISTORY (53 lines, 52 unique)
```

**Honest scoping of P7.** P7c establishes that a plain full reseal, with no span collapse, already defeats non-entry-text injection. The collapse vector therefore adds nothing to the *forgery* threat model beyond the already-disclosed self-consistent-resealing blind spot (standing boundary #32, proven live at v0.47). Its force is entirely in the **accidental** register, which is where this program's defects actually originate -- see P8 and F-S02-52-04.

---

## 4. Framework-specific analysis: Recursive Fractal Cube + Hurst

### 4.1 The 27-cell decomposition

Axes: **Z** = layer (Claims / Gates / Evidence), **X** = surface (Identity-parity / Integrity-seals / Narrative-register), **Y** = locus (front matter + Section 0.1 / body Sections 1-26 / Section 27 + HISTORY).

| Layer | Locus | Identity-parity | Integrity-seals | Narrative-register |
|---|---|---|---|---|
| **Claims** | FM + 0.1 | GATED `[2][2b][2c][5][6]` | UNGATED | **UNGATED** (A) |
| **Claims** | body 1-26 | GATED `[3][3a][3b]` | PARTIAL `[10]` one literal | PARTIAL `[3a]` digests only |
| **Claims** | Section 27 | PARTIAL `[9]` count word only | **UNGATED** (A) | PARTIAL `[9f][10b]` |
| **Gates** | FM + 0.1 | GATED (self-tested `[2d]`) | PARTIAL `[9b]` presence only | UNGATED |
| **Gates** | body 1-26 | GATED | **UNGATED** (no meta-gate) | UNGATED |
| **Gates** | Section 27 | GATED `[9][9a]` | GATED `[9b]` seals | GATED `[9f][10b]` |
| **Evidence** | FM + 0.1 | UNGATED (no tags) | UNGATED | UNGATED |
| **Evidence** | body 1-26 | UNGATED | **UNGATED** COUPLED (A) | PARTIAL `[9c]` counts only |
| **Evidence** | Section 27 | PARTIAL `[9c]` (A) | UNGATED ENUMERATED | UNGATED seat reports |

**Tally:** 7 GATED, 7 PARTIALLY GATED, 13 UNGATED.

### 4.2 Dead-space ratio and effective dimension

```
strictly ungated share            = 13/27   = 48.1%
ungated share, partials at 1/2    = 16.5/27 = 61.1%

D_strict  = log(7)    / log(3) = 1.7712
D_partial = log(10.5) / log(3) = 2.1408
D_Menger  = log(20)   / log(3) = 2.7268
```

The protocol removes substantially more analytical volume than a Menger sponge: it retains 7 of 27 cells where the sponge retains 20.

**Corroborating byte measurement from `build.py [11]`:**

```
Total document                     330,620 chars
Body (in gate scope)               104,165 chars (31.5%)
Section 27 (out of body scope)     226,455 chars (68.5%)
Semantic-gate coverage of body      29,714 / 104,165 (28.5%)
=> whole-document semantic coverage  ~9.0%
```

### 4.3 The 7 removed cells: sponge geometry versus protocol geometry

Menger removal set for a 3x3x3 indexed `(Z,X,Y)` is the center `(2,2,2)` plus six face centers.

| Sponge cell | Protocol cell | Protocol state | Agreement |
|---|---|---|---|
| (2,2,2) center | Gates / Integrity / body -- meta-gate | UNGATED | agrees |
| (1,2,2) | Claims / Integrity / body | PARTIAL | partial |
| (3,2,2) | Evidence / Integrity / body -- COUPLED tags | UNGATED | agrees |
| (2,1,2) | Gates / Identity / body | **GATED** | diverges |
| (2,3,2) | Gates / Narrative / body | UNGATED | agrees |
| (2,2,1) | Gates / Integrity / FM+0.1 -- `[9b]` | PARTIAL | partial |
| (2,2,3) | Gates / Integrity / Section 27 | **GATED** | diverges |

**The protocol's removal pattern is not self-similar to the sponge.** Two sponge-removed cells are the protocol's strongest gates, while the ungated mass clusters in the entire **Evidence layer** and the **narrative column** -- semantic surfaces, not geometric face centers. The one exact agreement is the center: no gate verifies gate efficacy.

### 4.4 Required check: no Class A in a GATED cell

| Finding | Cell | State |
|---|---|---|
| F-S02-52-01 | Claims / Narrative / FM+0.1 | UNGATED |
| F-S02-52-02 | Claims / Integrity / Section 27 **and** Evidence / Integrity / body | UNGATED |
| F-S02-52-03 | Evidence / Identity / Section 27 | PARTIAL (`[9c]` present but vacuous on values) |

**No Class A finding lives in a fully GATED cell.** The gate suite is not failing. It is absent where the failures are.

### 4.5 Hurst exponent of the seal chain

52 `ENTRY` digests, hex converted to integer mod 2^16, ordered v0.1 through v0.52. Mean 32,600.8, population sd 18,826.5. Classical rescaled-range over windows {4, 8, 13, 16, 26, 52}:

| window n | windows | mean R/S |
|---|---|---|
| 4 | 13 | 1.6247 |
| 8 | 6 | 2.4383 |
| 13 | 4 | 3.8978 |
| 16 | 3 | 3.7968 |
| 26 | 2 | 5.6446 |
| 52 | 1 | 7.1808 |

```
H (OLS slope, log-log)                       = 0.5986
Anis-Lloyd E[H] for i.i.d. noise at n = 52   = 0.6128
H - 0.5                                      = +0.0986
H - E[H]                                     = -0.0142
```

Measured against the naive 0.5 the chain looks mildly persistent; measured against the **correct finite-sample null** it is indistinguishable from random. That is the expected SHA-256 result: no structural bias in the input text is detectable through the digest.

**Methodological caveat, recorded as a standing observation.** This probe has zero diagnostic power on this artifact. SHA-256 destroys input structure by construction, so `H` approximately equal to `E[H]` is guaranteed whether the underlying text is honest or wholly forged. A clean Hurst result must not be counted as evidence of integrity in any future round.

### 4.6 Fibonacci structure of entry lengths

52 amendment entries, word counts: min 75, max 1303, median 610.5, total 30,218.

```
mean |nearest_Fib(len) - len| / len   = 0.118
   (uniform-random expectation in this range ~0.10 to 0.12)
successive-length ratio: median        = 0.941
successive-length ratio: mean          = 1.212
ratios within 5% of phi (1.618)        = 1 of 51
```

**No Fibonacci-adjacent clustering and no golden-ratio self-similarity.** Entry lengths are editorially determined by how much repair each round required; they carry no generative structure. The median of 610.5 sitting beside Fib(15) = 610 is coincidence, not signal. Like the Hurst probe, this test cannot discriminate an honest artifact from a forged one and should be retired from future dispatches.

### 4.7 Enzyme classification (WHAT) -- v0.52 entry claim inventory

Entry size: 938 words, 7,370 chars.

| Tag class | Count | Gate coverage | Verification outcome |
|---|---|---|---|
| COMPUTED | 7 | `[9c]` matched **0 of 7** | 4 verified true, 1 **FALSE** (F-S02-52-03), 2 unverifiable |
| DIFF-VERIFIED | 7 | none | 6 verified true, 1 **FALSE by omission** (F-S02-52-06) |
| COUPLED | 2 | none | 1 **FALSE** (F-S02-52-02), 1 unverifiable |
| EXTERNAL | 2 | file-existence only | unverifiable -- referenced artifacts do not ship |
| ENUMERATED | 1 | none | verified true (31 items) |
| ASSERTED | 2 | counted only | n/a by construction |
| PROVENANCE | 0 | -- | -- |
| **Total** | **21** | | |

`build.py [9c]` computes `total_tags = COMPUTED + EXTERNAL + ASSERTED = 11` and reports `ASSERTED fraction 2/11 (18.2%)`, excluding DIFF-VERIFIED, COUPLED, and ENUMERATED from the denominator. See F-S02-52-09.

The `[9c]` COMPUTED validator matches only `[COMPUTED: build.py [id] ...]` and `[COMPUTED: sha256sum <file>]`. None of the seven COMPUTED tags in this entry uses either form, so none was validated. See F-S02-52-07.

### 4.8 Replication Fork (HOW) -- six-phase pipeline compliance

| Phase | Compliance |
|---|---|
| Specify | COMPLIANT -- repairs enumerated as `[a]` through `[g]` before execution |
| Execute | COMPLIANT -- repairs landed; Provenance restoration and `[9b]` gate both verified in bytes |
| Verify | **NON-COMPLIANT** -- three claims shipped that a single command each falsifies |
| Seal | COMPLIANT -- 52/52 seals, `FULL_SECTION_27`, `PRIOR_HISTORY` all verify |
| Narrate | **NON-COMPLIANT** -- narration precedes recomputation at three loci |
| Dispatch | COMPLIANT -- packet reconstructs byte-exact |

The break is at Verify-then-Narrate, the same joint as at v0.51.

### 4.9 Orbital (WHO) -- seat independence

**Family:** Anthropic (Claude Opus 5). Under Section 22.1 this is the **producer family** -- the same family that authored the kernel module, Condition A evaluator, source-frame manifest, control-graph standard, Phase A scoring module, adversarial suite, and trust roots. This seat is advisory and carries no weight toward FB-7b in either direction.

**Prior-context discipline.** No prior seat-lineage record was opened before execution. Every finding derives from the dispatched packet and independent recomputation.

**Anchoring status: PARTIAL.** `prompt.txt` narrates the v0.51 defect and both R10 verdicts. This seat is therefore not context-free: I could not have independently discovered that the Provenance deletion was the R10 dominant defect, and F-S02-52-02 and -03 were reached by auditing a repair the dispatch told me to expect. Findings independent of that priming: **F-S02-52-01, -04, -05, -06, -07, -08, -09**.

### 4.10 Cell Cycle (WHEN) -- chronic defect registry

Entries explicitly naming the Axiom-3 / narration-from-memory / not-byte-reproducible pattern:

```
v0.6, v0.7, v0.8, v0.9, v0.15, v0.16, v0.17, v0.18, v0.19,
v0.20, v0.21, v0.36, v0.44, v0.45, v0.46, v0.52
```

**Recurrence fraction = 16/52 = 0.308.**

Section 22.2 records nine in-place mutations at v0.4, v0.9, v0.11 (two), v0.16, v0.17 (two), v0.41, v0.47. No new in-place mutation of a carried entry was found at v0.52; all 52 seals verify.

The chronic class that did recur is narration-from-memory. v0.52 corrects v0.51's non-byte-reproducible literals in correction (bj) and commits the same class in the two adjacent paragraphs.

### 4.11 Level-0 generator analysis

The dispatch asks whether fresh-instance production eliminated the tidal-locking class that produced the Section 0.1 chronic defect.

**It did not.** Three of the four Class A/B findings are pure narration-from-memory:

- a `grep` output stated as `1` when the shipped bytes return `3`
- two seal values presented as computed that no construction over shipped bytes reproduces
- a body-repair enumeration that omits the edit the producer actually made

Additionally, the surviving Section 0.1 defect (F-S02-52-01) is *itself* a Section 0.1 defect, in the same sentence family the dispatch names as the chronic locus, introduced at v0.52 by a gate-shaped repair.

**Conclusion:** fresh context removes *stale* memory; it does not change the *narrate-then-ship* order of operations. The generator level has not shifted. It has been re-instantiated. The durable fix is not a fresher instance but a Verify-before-Narrate gate that executes quoted commands and compares their output.

---

## 5. Findings (six-element format)

### F-S02-52-01 -- CRITICAL / Class A

- **Locus:** Section 0.1, line 22 of `xz_protocol_v0_52.md`.
- **Substance:** The sentence reads `The full defect trajectory is in Section 27 (fifty-two amendment entries, v0.1 through v0.51)`. Section 27 contains 52 entries spanning v0.1 through **v0.52**. The count word is true; the range terminus is false on shipped bytes. Gate `[9]` generates the count word from the parsed entry count and asserts the phrase `fifty-two amendment entries` is present -- it PASSES -- but checks nothing about the adjoining range. At v0.51 the sentence read correctly (fifty-one entries, v0.1 through v0.51). The v0.52 producer updated exactly the token the gate reads and left the token the gate does not read. Gate `[9e]` cannot catch this: its cardinal-range regex requires the literal `consecutive` and a word from `two..ten`.
- **Disposition:** OPEN. Correct the range to `v0.1 through v0.52`. Extend `[9]` to parse `v0.(\d+) through v0.(\d+)` adjacent to the count phrase and assert the terminus equals `VERSION`.
- **Cross-reference:** Cell Claims / Narrative / Section 0.1 (UNGATED). Same class as F-FABLE5-06 (v0.17 stale Section 0.1 version prose). The gate that closed F-FABLE5-06 sweeps `DRAFT CANDIDATE` and `This document is` prose only.

### F-S02-52-02 -- CRITICAL / Class A

- **Locus:** Section 27, v0.52 entry, append-only correction (bi).
- **Substance:** The correction states `v0.52 restored values (computed over Provenance-terminated span): ENTRY_v0.51 = d69efb11eea49e7ce2a527cc87bdb2fe27d576d2de9eeb4e99e417d43d960cf4, FULL_SECTION_27 = a35b774c8bfbb7f4d2a8cd1c49e3571fee2fa60d481f8840b51499ac8f65bdb5`, tagged `[COUPLED: verified against shipped v0.51 packet and v0.52 build.py derivation]`. Both values are false against the shipped packet:
  - Shipped `HISTORY.sha256` carries `ENTRY_v0.51 = 61fdc45fa4b787bf7c3096cc70a4facff11e99466563fbb846c2838e9fb59504`, which I recomputed independently from bytes and which `build.py [9b]` verifies. `d69efb11` is not that value.
  - The v0.52 `derive_prior_history` recursion computes the counterfactual v0.51 `FULL_SECTION_27` as `a3f07ac7fec28f3769c814abd51af7a99126bf0a2afbd80682312ff48386e9c6`. I reproduced this independently; it is the value that makes the shipped `PRIOR_HISTORY = b3697acc...` verify. `a35b774c` is not that value.
  - Neither claimed digest appears anywhere in the packet except in this one sentence. An exhaustive sweep -- every contiguous line range over lines 1200-1257 and every Section 27 prefix, under raw / `.strip()` / trailing-newline canonicalization, with and without the v0.52 entry stripped -- produced **no construction over shipped bytes yielding either digest**.

  Because entry text is preserved verbatim under append-only, `ENTRY_v0.51` is invariant across the documents it appears in. The claim therefore admits no benign reading: either the stated values are simply wrong, or the v0.51 entry text was altered at v0.52, which would be a tenth in-place mutation. The related figure `ENTRY_v0.51 included 813 bytes of Provenance text` also fails to reproduce; the closest reconstruction from shipped bytes gives 812 (767-char fused remainder + 2 newlines + 43-char end marker).
- **Disposition:** OPEN. Blocking for a carrying seat. Either recompute both values by tool and restate them, or restate them as UNVERIFIABLE-FROM-SHIPPED-BYTES and downgrade the evidence tag from COUPLED to ASSERTED. The chain fork itself is correctly reasoned and correctly disclosed; only the numbers are wrong.
- **Cross-reference:** Cells Claims / Integrity / Section 27 and Evidence / Integrity / body (both UNGATED). Exact recurrence of the class corrected by (bj) in the same entry, and of F-XZ07-OP-01 (v0.8 digest narrated from memory).

### F-S02-52-03 -- HIGH / Class A

- **Locus:** Section 27, v0.52 entry, register item (1) and body repair `[f]`.
- **Substance:** Both cite `grep -c "Provenance and review status" xz_protocol_v0_52.md = 1`. Running that exact command on shipped bytes returns **3** -- lines 1246, 1252, and 1255 -- because the entry's own two citations match their own search string. The evidence is self-inflating: the act of citing the check changes the check's result. The literal that actually establishes the terminus, `*Provenance and review status.*` with asterisks, does occur exactly once, so the underlying repair is sound; but the stated command and stated output are not the ones that establish it.
- **Disposition:** OPEN. Restate as `grep -cF '*Provenance and review status.*' xz_protocol_v0_52.md = 1`, and note that this correction must be applied together with the fix for F-S02-52-04 or it will silently collapse the seal span.
- **Cross-reference:** Cell Evidence / Identity / Section 27 (PARTIAL). Same class as (bj), one paragraph away. Standing boundary #17, `[9c]` quoted-tag inflation, names this surface but no gate acts on it.

### F-S02-52-04 -- HIGH / Class B

- **Locus:** Section 27, v0.52 entry, second paragraph; `build.py` `[9b]`, line 358-359.
- **Substance:** The entry claims `build.py now gates Provenance marker presence at [9b]: absence is a build failure, not a silent span change`. The implementation is `prov = s27_text.find("*Provenance and review status.*")` followed by `check(prov > 0, ...)` -- first occurrence, position never tested. A silent span change therefore still passes. Demonstrated without adversarial intent: applying the correction that F-S02-52-03 requires (citing the marker with its asterisks) drops `FULL_SECTION_27` coverage from 226,458 to 220,123 Section 27 characters -- **6,335 characters silently unsealed** -- while the build prints `PASS: Provenance seal terminus present (F-S02-51-02)` and returns rc=0. Deliberate insertion of the literal immediately after the `## 27.` heading collapses the sealed span to **37 of 226,502 characters (0.016%)**, still GREEN. The same `find` call governs `_full_seal`, so the derivation recursion collapses with it. The gate closes deletion and leaves relocation open; the entry claims it closes both.
- **Disposition:** OPEN. Assert that the marker occurs after the last amendment entry and that `len(s27[:prov].strip()) > 0.99 * len(s27)`; fail the build on any earlier occurrence.
- **Cross-reference:** Cell Gates / Integrity / Section 0.1 (PARTIAL) -- sponge face-center (2,2,1). Standing boundary #6 discloses the terminus literal but not this behaviour. Related to standing boundary #17.

### F-S02-52-05 -- HIGH / Class B

- **Locus:** Section 27, v0.52 entry, opening narrative versus defect register.
- **Substance:** The entry narrates `Opus S02 (advisory) HALT -- 3 CRITICAL, 3 HIGH, 4 MEDIUM, 2 LOW`, that is 12 findings. The register disposes 7 S02 identifiers: `-01`, `-02`, `-04`, `-05`, `-08`, `-09`, `-10`. Parsed severities are 1 CRITICAL, 3 HIGH (one of which is Kimi's F-S01-51-02), and 4 MEDIUM. **Undispositioned: 2 CRITICAL, 1 HIGH, 2 LOW.** Identifiers `-03`, `-06`, `-07`, `-11`, `-12` appear nowhere in the packet. The omission is not disclosed anywhere in the entry. What makes this Class B rather than Class E is the asymmetry: the entry has a below-threshold disclosure mechanism -- register item (5) explains that four MEDIUM items are `noted as standing observations ... below the convergence-repair threshold (1-seat each)` -- and applies it to the four MEDIUMs while silently dropping two CRITICALs.
- **Disposition:** OPEN. Either disposition the five, or record them explicitly as out of scope with a stated basis, or correct the narrated tally.
- **Cross-reference:** Cell Claims / Narrative / Section 27 (PARTIAL). `[9f]` verifies declared-equals-parsed *within* the register only; no gate reconciles the register against the entry's own narrated seat tallies.

### F-S02-52-06 -- MEDIUM / Class B

- **Locus:** Section 27, v0.52 entry, `Body repairs landed at v0.52: [a] ... [g]`.
- **Substance:** The enumeration omits the Section 0.1 edit from `fifty-one` to `fifty-two`. That edit did land in the normative body, and gate `[9]` forced it -- the build fails without it. An enumerated repair list that omits a landed edit is false by omission, and the omitted edit is precisely the one carrying F-S02-52-01. The `[DIFF-VERIFIED]` tag on the enumeration is therefore unearned.
- **Disposition:** OPEN. Add item `[h]` recording the Section 0.1 count-word update and the accompanying range correction.
- **Cross-reference:** Cell Claims / Narrative / Section 27. Same class as F-GLM52-08 (v0.15, fix claims not substantiated in bytes).

### F-S02-52-07 -- MEDIUM / Class D

- **Locus:** `build.py` `[9c]`, lines 395-404.
- **Substance:** The COMPUTED-tag validator matches only two shapes: `[COMPUTED: build.py [id] ...]` and `[COMPUTED: sha256sum <file>]`. The v0.52 entry carries 7 COMPUTED tags; **none matches either shape**, so `[9c]` validated zero of them. The gate verifies that a referenced build section exists and that a cited file ships. It never verifies that a stated value is true. It would not have caught F-S02-52-03 in any formulation.
- **Disposition:** OPEN. Extend `[9c]` to recognise quoted shell forms (`grep -c "..." <file> = N`) and execute them, comparing actual output to the stated value; fail on mismatch. This single gate would have caught F-S02-52-03 and, generalised to digest citations, F-S02-52-02.
- **Cross-reference:** Cell Evidence / Identity / Section 27 (PARTIAL). This is the vacuity that keeps the Class A findings out of GATED cells.

### F-S02-52-08 -- MEDIUM / Class D

- **Locus:** Section 27 seal architecture; `build.py` `_full_seal`.
- **Substance:** Restoring the marker as seal terminus places the 804-character Provenance paragraph and the end-of-document marker **outside every HISTORY seal**. `FULL_SECTION_27` truncates at `prov`; no ENTRY seal reaches past the last entry; the `[3b]` absence gate covers body only. The sole control is the marker's presence. Probe P6 replaced the paragraph wholesale -- inverting `This document has NOT undergone independent human peer review` to `This document HAS undergone independent human peer review and is endorsed by the reviewers` -- resealed, and the build returned GREEN across all 202 checks. The AI-assistance disclosure, the no-peer-review disclosure, and the no-effectiveness-claim disclosure are the document's highest-stakes prose and its least-sealed bytes.
- **Disposition:** OPEN. Seal the Provenance paragraph under a distinct `PROVENANCE_BLOCK` label in `HISTORY.sha256` so that its content, not only its marker, is covered.
- **Cross-reference:** Cell Gates / Integrity / body (UNGATED) -- the sponge center (2,2,2), the one cell where protocol geometry and sponge geometry agree exactly. Standing boundary #6 covers the terminus literal, not the content.

### F-S02-52-09 -- LOW / Class E

- **Locus:** `build.py` `[9c]`, lines 405-411.
- **Substance:** `total_tags = COMPUTED + EXTERNAL + ASSERTED = 11`, producing the reported `ASSERTED fraction (tagged claims): 2/11 (18.2%)`. The entry carries 21 tags; DIFF-VERIFIED (7), COUPLED (2), and ENUMERATED (1) are excluded from the denominator. Since 0 of the 7 COMPUTED tags are gate-validated, and 2 of the 4 verifiable non-COMPUTED tags proved false on these bytes, the published fraction understates the genuinely unverified share by roughly half.
- **Disposition:** NOTED. Compute the denominator over all evidence-tag classes, and report a separate gate-validated fraction.
- **Cross-reference:** Cell Evidence / Narrative / body (PARTIAL). Metric-integrity observation, not a byte-level error.

### F-S02-52-10 -- LOW / Class D

- **Locus:** `build.py` `[2b]`, `[2c]`.
- **Substance:** A coordinated two-locus edit changing both the front-matter status line and the Section 0.1 status sentence to `v0.52 FROZEN RELEASE`, followed by manifest resync, returns BUILD PASSED with 202 PASS / 0 FAIL. Section 27 is untouched, so every seal still verifies. A document that has not achieved non-HALT in ten consecutive convergence rounds can assert FROZEN with a fully green build.
- **Disposition:** DISCLOSED-CONFIRMED. Standing boundaries #16 (no gate checks FROZEN status token) and #24 (`[2c]` arity-two) remain live at v0.52. A status-token allow-list is a one-line gate that has now survived sixteen rounds.
- **Cross-reference:** Cell Gates / Identity / Section 0.1. Confirms rather than extends the disclosure.

### F-S02-52-11 -- LOW / Class E

- **Locus:** `prompt.txt`, Packet paragraph versus Core audit obligations paragraph.
- **Substance:** The dispatch describes a `17-member packet` in one paragraph and `packet identity (16 members)` in the next. 16 is correct: `PACKET_SHA256SUMS` lists 16 members and does not list itself.
- **Disposition:** NOTED. Dispatch-level only; no protocol impact.
- **Cross-reference:** Process observation. Recorded because dispatch arithmetic is itself part of the audit surface.

### Verified clean

Recorded so that the next round can distinguish untested surfaces from tested ones: all 52 entry seals against bytes; `FULL_SECTION_27`; the `PRIOR_HISTORY` recursive derivation, independently reimplemented; cardinality and duplicate-label gates (R9 repair efficacious under mutation); the `[9b]` presence gate against deletion (R10 repair efficacious under mutation); the `[ENUMERATED: 31 items]` boundary count; `grep -c v0.52 = 13`; six suites at 186 GREEN; every Section 0.1 count claim; the (bj) `[53]/[52]` mutation arithmetic; Section 22.2 coverage to v0.51; Section 22.3 carry lineage to v0.38-v0.52; Section 25 FB-7b row carrying R9 and R10 trajectory; Section 0.3 prohibited-language compliance.

---

## 6. VERDICT

**HALT (advisory).**

Three Class A findings on shipped bytes, each reachable by a single command.

**F-S02-52-02 is the load-bearing one.** Correction (bi) is the entry's own account of the chain fork -- the mechanism by which this version explains why an external verifier holding v0.51 bytes will see a seal mismatch. It is tagged as verified against the v0.52 `build.py` derivation, and the v0.52 `build.py` derivation demonstrably does not produce either of its two values. An exhaustive sweep over shipped bytes produces neither. The one paragraph whose entire function is to give an external verifier a documented expectation gives that verifier two digests it cannot reproduce.

**F-S02-52-01** places a false entry range in Section 0.1, introduced at v0.52 by a repair shaped exactly to the token gate `[9]` reads. **F-S02-52-03** states a `grep` output of 1 where the shipped bytes return 3, in evidence that inflates itself by being written.

The R9 and R10 structural repairs both landed and both hold under mutation. That is real progress and I want it recorded as such: the cardinality gate catches duplicate seal lines, the Provenance presence gate catches deletion, all 52 seals verify, the derivation reproduces independently, and no new in-place mutation of a carried entry occurred. The append-only chain is in better condition at v0.52 than at any point since v0.46.

But v0.52 corrects v0.51's non-byte-reproducible literals in one paragraph and commits the same class in the two adjacent ones. The recurrence fraction is 0.308 and this entry is its newest member. The fresh-instance handoff addressed staleness; it did not address the order of operations. Narration still precedes recomputation.

**On the target condition.** The dispatch states that non-HALT with zero Class A from carrying seats satisfies FB-7b, and instructs that the verdict not be softened to achieve it. It is not met on these bytes. This seat is advisory and producer-family under Section 22.1, so this verdict cannot satisfy or block FB-7b in either direction; it is submitted as an adversarial record only.

**Single highest-value change for v0.53.** Not another repair round. Extend `[9c]` to execute the shell commands and digest citations that COMPUTED and COUPLED tags quote, and compare their real output to the stated value. That one gate closes F-S02-52-02, -03, and -07, and it converts the chronic narration-from-memory class from a thing auditors find into a thing the build refuses to ship.

**On the analytical lens.** The 27-cell decomposition did real work: it predicted, before inspection, that failures would cluster in the Evidence layer and the narrative column, and all Class A and Class B findings landed there. The Hurst and Fibonacci probes returned clean nulls and would have returned clean nulls over a wholly forged packet. I recommend retaining the cube and retiring Hurst and Fibonacci from future dispatches rather than continuing to report reassuring numbers that cannot discriminate.

---

*Seat S02, Round 11, XZ Protocol v0.52. Advisory, non-binding, producer family. Findings derived from the dispatched packet and independent recomputation; no prior seat-lineage record was consulted before execution.*

---

# Bismillah ir-Rahman ir-Rahim
