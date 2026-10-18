# Bismillah ir-Rahman ir-Rahim

# R0219 -- Seat S02-OPUS -- XZ Protocol v0.50 R9 Advisory Audit

**Chronological Index:** 470 of 995  
**Date:** 2026-08-09  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v0.50_R9_Seat_S02_OPUS_Audit.md  
**Source Format:** md  
**SHA-256:** `968941f81dfebb322ecf93fe82e8ae54470b1fafe061f986fa23e7a7c6bc792c`  

---

## R0219 · Seat S02-OPUS -- XZ Protocol v0.50 R9 Advisory Audit

- section: IV. XZ Protocol
- source_file: XZ_v0.50_R9_Seat_S02_OPUS_Audit.md
- source_format: md
- text_sha256: 968941f81dfebb322ecf93fe82e8ae54470b1fafe061f986fa23e7a7c6bc792c

# Seat S02-OPUS -- XZ Protocol v0.50 R9 Advisory Audit

**Seat ID:** S02
**Family:** Claude Opus 5 (Anthropic)
**Type:** Fresh
**Role:** ADVISORY -- producer family, non-carrying, non-binding
**Finding namespace:** F-S02-50
**Mode:** A (substrate verifier, full tool access)
**Substrate-claim verification confidence:** HIGH
**Date:** 2026-08-09
**Protocol version under audit:** v0.50
**Round:** R9

**PACKET_SHA256SUMS digest:** `7a6196fa256218a42c4d8c41c8f0a18cca90c24d2d4ea540608ca4ea914dab0a`

---

## 1. Reconstruction & Baseline

| Step | Command | Result |
|---|---|---|
| Packet reconstruction | `python3 setup.txt` | 16/16 OK, 0 FAIL, 0 MISSING |
| Build verification | `python3 build.py` | 199 checks, BUILD PASSED |
| Standard test suites | `python3 -m pytest -q` | 117 passed |
| Phase A tests | `python3 -m pytest xz_protocol_phase_a_tests.py -q` | 69 passed |
| **Total** | | **186/186 GREEN, 6 suites** |

All 50 HISTORY.sha256 seals verified against entry bytes. FULL_SECTION_27 seal verified. PRIOR_HISTORY derivation verified (`3d695f8c...`). All 16 PACKET_SHA256SUMS members byte-identical to shipped files.

---

## 2. Mutation Attack Register

Seven mutations executed, each with a benign control (restore clean bytes, confirm BUILD PASSED). The dispatch required at least 5 mutations with MUTATION-LANDED proof and benign control; 7 were executed.

### MUTATION 1: [10b] same-severity cross-item duplicate

- **Injected:** F-S01-49-04 (already in register item 1 at HIGH) duplicated into item 3 at HIGH.
- **Gate under test:** [10b] finding-ID cross-item uniqueness.
- **Result:** **CAUGHT.**

```
FAIL: Finding F-S01-49-04 appears in multiple register items: item 1 (HIGH), item 3 (HIGH)
BUILD FAILED: 4 error(s)
```

- **Benign control:** BUILD PASSED.
- **Assessment:** [10b] is effective for F-prefixed IDs regardless of severity match. No finding.

### MUTATION 2: HISTORY cardinality -- exact-duplicate seal line

- **Injected:** ENTRY_v0.50 seal line duplicated (identical bytes appended to HISTORY.sha256).
- **Gate under test:** [9b] HISTORY cardinality check (v0.50 addition).
- **Result:** Cardinality check **EVADED.**

```
PASS: HISTORY seal count (50) == entry count (50) (no duplicates)
```

Only PACKET_SHA256SUMS digest mismatch caught the mutation (external integrity, not semantic gate).

- **Root cause:** build.py line 356 -- `seal_labels` is a set comprehension (`{l.split()[1] for l in ...}`). A set automatically deduplicates identical entries. The "no duplicates" claim in the check message is false; the check tests cardinality of unique labels against entry count, not raw line count against unique label count.
- **Benign control:** BUILD PASSED.
- **Assessment:** GATE DEFECT. **Finding F-S02-50-01 issued.**

### MUTATION 3: [DIFF-VERIFIED] tag forgery

- **Injected:** False `[DIFF-VERIFIED: old text absent, new text present]` on a fabricated body repair [g] claiming a mutation count change that never occurred.
- **Gate under test:** [9c] provenance tag validation.
- **Result:** [9c] **EVADED** entirely.

```
[9c] Provenance tag validation
  PASS: Current-version entry v0.50 found in Section 27
  PASS: COMPUTED tag references existing build.py section [10b]
  COMPUTED: 5, EXTERNAL: 3, ASSERTED: 2
  ASSERTED fraction (tagged claims): 2/10 (20.0%)
```

build.py contains **zero** references to `DIFF-VERIFIED` (confirmed: `grep -c 'DIFF.VERIFIED' build.py` returns 0). The protocol uses DIFF-VERIFIED 5 times in the v0.49/v0.50 entries.

- **Benign control:** BUILD PASSED.
- **Assessment:** UNGATED TAG CLASS. **Finding F-S02-50-03 issued.**

### MUTATION 4: [10b] NC-prefix evasion

- **Injected:** NC-FORGE-01 placed in both register items (1) and (3) at HIGH.
- **Gate under test:** [10b] finding-ID cross-item uniqueness.
- **Result:** [10b] **EVADED.**

```
[10b] Finding-ID cross-item uniqueness
  PASS: All 11 finding IDs appear in exactly one register item
```

The gate extracts only `F-[\w-]+` IDs (line 489). NC-prefixed IDs, which the [9f] regex (line 453, `(?:F|NC)-` alternation) accepts as valid register entries, are completely invisible to the cross-item uniqueness check.

- **Benign control:** BUILD PASSED.
- **Assessment:** REGEX SCOPE GAP. **Finding F-S02-50-02 issued.**

### MUTATION 5: Phantom 5th register item

- **Injected:** `(5) F-PHANTOM-01 LOW NOTED` appended after item (4). Prose header still says "4 items".
- **Gate under test:** [9f] register self-consistency (declared-vs-parsed count).
- **Result:** [9f] **EVADED.**

```
[9f] Register self-consistency
  PASS: Register parsed at least one item (5 found)
  PASS: Register parsed == declared (5 parsed, 5 declared)
  Register: 5 items, {'HIGH': 3, 'MEDIUM': 1, 'LOW': 1}
```

The "declared count" is derived from `re.findall(r'\(\d+\)', reg_section)` -- the same `(\d+)` markers that the parser uses to find items. The comparison `reg_total == declared_count` is tautological.

- **Benign control:** BUILD PASSED.
- **Assessment:** TAUTOLOGICAL CHECK. **Finding F-S02-50-04 issued.**

### MUTATION 6: SEALED-ANNOTATION tag forgery

- **Injected:** False `[SEALED-ANNOTATION: v0.48 entry preserved verbatim -- FORGED CLAIM, entry was actually modified]` on register item (3).
- **Gate under test:** [9c] provenance tag validation.
- **Result:** [9c] **EVADED** entirely. build.py contains zero references to SEALED-ANNOTATION, COUPLED, ENUMERATED, or PROVENANCE.

```
[9c] Provenance tag validation
  PASS
```

- **Benign control:** BUILD PASSED.
- **Assessment:** Subsumed by F-S02-50-03 (ungated tag class). Full ungated inventory: DIFF-VERIFIED, SEALED-ANNOTATION, COUPLED, ENUMERATED, PROVENANCE.

### MUTATION 7: Section 0.1 structural fix verification (non-adversarial)

- **Verified:** Section 0.1 line 18 contains the pointer to Section 25 ("single source of truth; no duplicate rationale maintained here"). No standalone FB-7b rationale present.
- **Verified:** Section 25 FB-7b row (line 758) contains R6 (`v0.47`), R7 (`v0.48`), and R8 text.
- **Assessment:** The chronic-defect structural fix is **CONFIRMED PRESENT**. No finding.

---

## 3. Substrate Verification (non-mutation)

### Section 0.1 pointer (structural fix, chronic-defect class)

- Line 18: `FB-7b status, rationale, and the full carrying-seat trajectory are recorded in the Section 25 FB-7b row (single source of truth; no duplicate rationale maintained here).`
- **Status:** VERIFIED. Old standalone rationale absent. Pointer present.

### Section 25 FB-7b row trajectory

- Line 758 contains: `R6 (v0.47): all 3 carrying seats (Kimi K3) HALTed binding (append-only violation). R7 (v0.48): all 3 carrying seats HALTed binding (phantom repair). R8 (v0.49): Kimi K3 S01 carrying seat HALTed binding (register-ID collision, duplicate HISTORY seal).`
- **Status:** VERIFIED. R6/R7/R8 trajectory complete.

### Front-matter version parity

- Line 4: `**Version:** 0.50, draft candidate, 2026-08-09`
- Line 5: `**Status:** v0.50 DRAFT CANDIDATE`
- **Status:** VERIFIED via build.py [2]/[2b]/[2c] (all PASS).

### HISTORY.sha256 seal chain

- 50 ENTRY seals verified against entry bytes (build.py [9b], all PASS).
- FULL_SECTION_27 seal verified.
- PRIOR_HISTORY derivation verified: `3d695f8c068d945c5076fa52a2061c15dae621f716a1197c26481c831c06dd66`.
- **Status:** VERIFIED.

### Body repair [b] locus trace (incomplete)

- v0.50 entry claims: `[b] Section 22.2 coverage to v0.49 [DIFF-VERIFIED]`.
- Grep for `v0.1 through v0.49` in the body (outside Section 27) returns empty.
- Section 0.1 line 22 says `v0.1 through v0.50` (current version).
- **Status:** The body text is correct (it says v0.50). The DIFF-VERIFIED claim may be imprecise -- the coverage string appears to have been updated directly to v0.50 rather than landing as v0.49 first. **Finding F-S02-50-05 issued** (tentative, MEDIUM).

---

## 4. Findings

### F-S02-50-01 [HIGH] -- HISTORY cardinality check is a set-based no-op for exact-duplicate seal lines

- **Locus:** build.py lines 356--361
- **Substance:** The cardinality check claims "no duplicates" but `seal_labels` is a set comprehension (`{l.split()[1] for l in ...}`), which silently deduplicates identical lines. An exact-duplicate seal line -- the R8 defect class this gate was built to prevent -- passes the check. The mutation is caught only by the external PACKET_SHA256SUMS digest (file bytes changed), not by the cardinality gate itself. The gate's claim ("no duplicates") is stronger than its mechanism (unique-label cardinality == entry count).
- **Disposition:** Change `seal_labels` from a set to a list for the raw count, then assert `len(raw_seal_lines) == len(set(raw_seal_lines))` to detect exact-duplicate lines. Alternatively, count raw ENTRY_ lines (list) against unique ENTRY_ labels (set) and fail when they differ.
- **Cross-reference:** v0.50 register item (1), F-S01-49-04 / F-S02-49-03 / F-S03-49-01 / F-S04-49-01 / F-S04-49-02. The gate added to prevent recurrence does not actually prevent exact-duplicate recurrence.

### F-S02-50-02 [HIGH] -- [10b] finding-ID uniqueness gate blind to NC-prefixed IDs

- **Locus:** build.py line 489 (`re.findall(r"F-[\w-]+", ids_str)`)
- **Substance:** [10b] extracts only `F-[\w-]+` IDs. The [9f] parser (line 453) accepts `NC-` prefixed IDs as valid register entries via the `(?:F|NC)-` alternation. An NC-prefixed ID can appear in multiple register items with conflicting dispositions and [10b] will not detect it. The two gates disagree on the finding-ID namespace they cover.
- **Disposition:** Widen the [10b] extraction regex to `(?:F|NC)-[\w-]+`, matching the [9f] parser's acceptance set. Alternatively, refactor both [9f] and [10b] to share a single `FINDING_ID_PATTERN` constant.
- **Cross-reference:** v0.50 register item (3), F-S01-49-02 / F-S01-49-03. The gate prevents F- collisions but not NC- collisions.

### F-S02-50-03 [HIGH] -- Five enzyme-type provenance tags are completely ungated

- **Locus:** build.py [9c] (lines 390--409); protocol Section 27 v0.49/v0.50 entries
- **Substance:** The [9c] provenance tag validator counts COMPUTED, EXTERNAL, and ASSERTED tags but does not count, validate, or acknowledge DIFF-VERIFIED, SEALED-ANNOTATION, COUPLED, ENUMERATED, or PROVENANCE tags. These five tag types are used 15+ times across v0.49/v0.50 entries as substantive provenance claims (e.g., `[DIFF-VERIFIED: old text absent, new text present]`; `[SEALED-ANNOTATION: entry preserved verbatim]`). A forged tag of any of these types passes the build with zero detection. The [9c] tag census reports 10 total tags for the v0.50 entry; the actual count including ungated types is higher, and the ASSERTED fraction is understated.
- **Disposition:** Either (a) extend [9c] to count all five tag types in the census and validate DIFF-VERIFIED claims against the shipped body (confirm old text absent and new text present at the cited locus), or (b) explicitly disclose the ungated tag classes as a standing boundary in the v0.50 entry with the semantic caveat that these tags are auditor-directed markers rather than machine-verified claims. Option (b) is the lighter path; option (a) is the structurally honest one.
- **Cross-reference:** v0.50 body repairs [a]--[e] (all carry [DIFF-VERIFIED]); register item (4) (carries [DIFF-VERIFIED] and [ASSERTED]). The standing-boundary list (31 items) does not include this gap.

### F-S02-50-04 [MEDIUM] -- [9f] declared-vs-parsed register count is tautological

- **Locus:** build.py lines 447--462
- **Substance:** The "declared count" is derived from `re.findall(r'\(\d+\)', reg_section)` -- the same `(\d+)` markers that the parser uses to locate items. The check `reg_total == declared_count` therefore compares the parser's output count against its own input count. A phantom register item bearing a valid `(N)` marker passes both sides of the comparison simultaneously. The prose claim "N items" in the register header is never cross-referenced.
- **Disposition:** Extract the declared count from the prose string (parse "4 items" or equivalent from the register header sentence) and compare against the parsed marker count. Alternatively, disclose as a standing boundary.
- **Cross-reference:** Standing boundary list, [9c] arity-one regex. Same class of gate-vs-prose divergence.

### F-S02-50-05 [MEDIUM] -- Body repair [b] DIFF-VERIFIED claim cites v0.49 but body reads v0.50

- **Locus:** Section 27 v0.50 entry, body repairs line: `[b] Section 22.2 coverage to v0.49 [DIFF-VERIFIED]`
- **Substance:** The v0.50 entry claims body repair [b] updated Section 22.2 coverage "to v0.49". A grep for `v0.1 through v0.49` in the body (outside Section 27) returns empty. Section 0.1 line 22 says `v0.1 through v0.50`. If the coverage string was updated directly to v0.50 (the current version) rather than first landing as v0.49, the [DIFF-VERIFIED] target is misstated. The body text is correct; the provenance tag in the amendment entry is imprecise.
- **Disposition:** Correct the body-repair claim to `[b] Section 22.2 coverage to v0.50 [DIFF-VERIFIED]`, or verify that "coverage to v0.49" means the diff was against v0.48's coverage string (which would have said v0.48), in which case the phrasing should be clarified.
- **Cross-reference:** F-S02-50-03 (ungated DIFF-VERIFIED tags; this finding demonstrates the practical consequence).

---

## 5. Standing-Rules Compliance Sweep

| Rule | Result |
|---|---|
| Em-dash policy (U+2013, U+2014, U+2015, `---`) | CLEAN on protocol body; build.py uses `--` double-hyphen only |
| Brand canonical ("BayyinahEnterprise" without space) | CLEAN (build.py [4] confirms zero occurrences in 14 normative files + body) |
| Severity uppercase (CRITICAL, HIGH, MEDIUM, LOW) | CLEAN in v0.50 register |
| Six-element findings format | N/A (this audit produces findings, not the protocol) |
| Substrate-of-record uniqueness | Section 0.1 FB-7b pointer confirmed (no duplicate rationale) |
| Audit-chain immutability | 50 seals verified; no in-place mutation detected on shipped bytes |

---

## 6. Verdict

**Verdict:** HALT-AND-RETURN-TO-PRODUCER.

**Severity ledger:** 0 CRITICAL / 3 HIGH / 2 MEDIUM / 0 LOW.

The three HIGH findings are all gate-evasion defects in build.py -- the very gates that v0.50 introduced to close R8 findings:

1. **F-S02-50-01:** The HISTORY cardinality check uses a set where it needs a list, making it blind to the exact defect class it was built to catch.
2. **F-S02-50-02:** The [10b] uniqueness gate has a narrower regex than the [9f] parser it guards, creating a namespace blind spot.
3. **F-S02-50-03:** Five of the protocol's provenance tag types can be forged without any gate detecting the forgery.

All three are single-line or few-line fixes in build.py. No structural redesign required. The body text, sealed entries, and Section 0.1 structural fix are intact. The protocol's analytical substance is not affected; the defects are in the verification machinery only.

**Recommendation:** Absorb F-S02-50-01 through F-S02-50-04 (four code fixes in build.py), disposition F-S02-50-05 after substrate trace, and re-dispatch to a non-producer family for R10 carrying audit on v0.51 bytes.

---

## 7. Cross-Vendor Recommendation

This seat is producer-family (Claude Opus 5, Anthropic). The next carrying audit should be dispatched to Kimi K3 (the current carrying family) on v0.51 bytes. If an adversarial seat is desired for the next round, GPT-class or Gemini-class is recommended to maintain cross-vendor rotation.

---

## 8. Appendix: Gate Coverage Summary

| Gate | What it checks | What it misses (from this audit) |
|---|---|---|
| [9b] HISTORY cardinality | unique label count == entry count | exact-duplicate lines (set dedup, F-S02-50-01) |
| [9c] Provenance tags | COMPUTED, EXTERNAL, ASSERTED counts | DIFF-VERIFIED, SEALED-ANNOTATION, COUPLED, ENUMERATED, PROVENANCE (F-S02-50-03) |
| [9f] Register self-consistency | parsed item count == `(\d+)` marker count | prose "N items" claim (F-S02-50-04) |
| [10b] Finding-ID uniqueness | F-prefixed IDs across register items | NC-prefixed IDs (F-S02-50-02) |
| [3b] Absence gate | unresolvable 64-hex in body | (no finding this round) |
| [2]/[2b]/[2c] Version parity | version strings across all files | (no finding this round) |

**Semantic-gate coverage (build.py [11]):** 29,798 / 104,249 body chars (28.6%). Section 27 ungated share: 214,327 / 318,576 total chars (67.3%).

---

# Bismillah ir-Rahman ir-Rahim
