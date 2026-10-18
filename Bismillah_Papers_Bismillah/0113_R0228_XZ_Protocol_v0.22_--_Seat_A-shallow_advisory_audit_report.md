# Bismillah ir-Rahman ir-Rahim

# R0228 -- XZ Protocol v0.22 -- Seat A-shallow advisory audit report

**Chronological Index:** 113 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v22_SEAT_A_SHALLOW_REPORT.md  
**Source Format:** md  
**SHA-256:** `2b712d8e675dbb3b110349f1fc7f97fe9889904fcfca5267437b20a9051220ee`  

---

## R0228 · XZ Protocol v0.22 -- Seat A-shallow advisory audit report

- section: IV. XZ Protocol
- source_file: XZ_v22_SEAT_A_SHALLOW_REPORT.md
- source_format: md
- text_sha256: 2b712d8e675dbb3b110349f1fc7f97fe9889904fcfca5267437b20a9051220ee

# XZ Protocol v0.22 -- Seat A-shallow advisory audit report

**Seat:** Claude Opus 5, Seat A-shallow, producer-family advisory
**Namespace:** F-OP22S
**Mode:** A (substrate verifier -- full packet on disk, build and pytest executable, mutation sandbox, plus the v0.20 and v0.21 packets retained)

## 0. State declaration (S-0)

Shallow continuous, two prior rounds. I produced the v0.20 fresh-instance report (F-OP20F-01 through -11) and the v0.21 shallow report (F-OP21S-01 through -08), and I hold both packets in full. No v0.17, v0.18, or v0.19 bytes. I did not author the discipline blocks, the v0.19 adjudication, or the F-OP21 and F-OP21C namespaces.

Standing: producer-family advisory. Cannot HALT, cannot carry HIGH, no FB-7b weight. Where a non-producer seat's severity differs, theirs governs.

## 1. S-1 preregistration (G)

Frozen at `PREREG_OPUS5_B_SHALLOW_v22.txt`, sha256 `173a6e4d169b1bf1278713bda10619fa20972176a925c6cda5ad8151ae68b993`, 2026-08-01T23:58:08Z, before any read of Section 27.

**Contamination.** Third consecutive round in which the dispatch orders `build.py` before preregistration, so build stdout again leaked Section 27-derived facts pre-freeze: entry count 22, the PRIOR_HISTORY value, the `[9f]` register line, and COMPUTED 4 / ASSERTED 15. I raised this at v0.20 and again at v0.21; it has not been dispositioned in either entry. Predictions touching those values are marked contaminated in the frozen file.

| # | Source | Prediction | Result |
|---|---|---|---|
| B1 | bytes | **Sharpest.** `[9f]` printed a register line and no checks; the only source path producing that shape is a truthy `ledger_match` with an empty tally. Predict the entry claims F-OP21S-02 CLOSED with a COMPUTED tag on `[9f]` while `[9f]` again runs zero assertions | **Correct**, and the mechanism is worse than I predicted -- F-OP22S-01 |
| B2 | bytes | The duplicate-ID check added for F-OP21S-03 sits in the else-branch and is therefore unreachable | **Correct** -- and it would have failed the build -- F-OP22S-01, F-OP22S-02 |
| B3 | bytes | F-OP21S-01 genuinely fixed by recursion; verify against my held v0.21 file | **Correct.** Fixed, durable through v0.23, chain externally anchored -- §7 |
| B4 | bytes | The recursion re-introduces a hand-populated `cb67f222` literal at the v0.19 termination; entry does not name it | **Correct**, though it is dead code on these bytes -- F-OP22S-06 |
| B5 | contaminated | Entry reports the ASSERTED fraction but not that COMPUTED more than halved | **Correct** -- and it reports the *prior* round's transition, not its own -- F-OP22S-04 |
| M1 | memory | PDF still unbound; NOTED a third time | Correct |
| M2 | memory | `[9c]` file-shipping regex byte-identical, still arity-one | **Correct.** Verified identical -- F-OP22S-05 |
| M3 | memory | Silent-skip census did not fall | Correct: 18 to 19 |
| M4 | memory | D-8 split landed; my prior reports still ship | Correct on both |
| M5 | memory | Coverage figures corrected for v0.21 **and** a new short figure appears (least confident) | **Correct on both halves** -- F-OP22S-04 |

Ten correct, one correct-but-contaminated. The score is high because two rounds of memory make the predictions easy, which is the answer to D-7 question 2 rather than a credit to me. B1 and B2 are the only ones that required reading the new `build.py`.

## 2. Byte verification table

| Step | Command | Result |
|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | **rc=0.** 16 members, all OK, no self-entry. |
| 2 | `python3 build.py` | **rc=0**, `BUILD PASSED: all checks GREEN`, **164 PASS**, 0 FAIL. Down from 168 at v0.21 -- `[9f]` contributes zero this round (F-OP22S-01). |
| 3 | six-suite canonical pytest | **rc=0**, `186 passed`. AST 186, collected 186. |
| 4 | Independent digest of all 16 members | All match. Manifest digest recomputes to `571d5e2d8a822c1496a2bd5b7e445b10800f923eacc0abd7c72eca44bbbc14c0`, matching trust roots and body. |
| 4a | HISTORY.sha256 | 22 entry seals + FULL_SECTION_27 verify. `PRIOR_HISTORY 4a2842d20f9058f6b362e8ab40d1450ba499eb2caa39417cfa0880348bbce600`. |
| 4b | **External anchor** | sha256 of the v0.21 `HISTORY.sha256` I hold = `4a2842d2...`. **Exact match.** See §7. |
| 4c | Unsealed members | 8: the PDF, the manifest itself, three context documents, and my two prior reports. |
| 4d | PDF | 79 pages, sha256 verified against no shipped text. Content agrees with the .md on all six load-bearing values sampled. **134 U+2013 en-dashes in the PDF against 0 in the .md**, and 0 double-hyphens in the PDF against 189 in the .md -- the renderer converts every one. Independently confirms F-OP21C-07. |
| 4e | Standing-rules sweep | Zero U+2013/2014/2015 and zero spaced brand variant across all 16 normative files. Clean at source. |

Coverage from `[11]`: total 160903, body 97803 (60.8%), Section 27 ungated 63100 (**39.2%**, up from 36.8%), semantic-gate coverage **24.7%**.

## 3. Claim provenance ledger (A)

**COMPUTED 4, EXTERNAL 0, ASSERTED 15. ASSERTED fraction 15/19 = 78.9%.**

Four-round series, computed by me from shipped Section 27 bytes: v0.18 untagged, v0.19 37.5% (COMPUTED 9), v0.20 50.0% (COMPUTED 11), v0.21 57.1% (COMPUTED 9), v0.22 **78.9% (COMPUTED 4)**. The register grew from 12 items to 14 while computed backing fell by more than half. This is the largest single-round move in the series and it is in the wrong direction.

Of the 4 COMPUTED tags, 2 name build.py sections and are validated by `[9c]`; 2 do not (`sha256sum | sha256sum`, `pytest + AST`) and I recomputed both -- the manifest digest and 186/186 parity both hold. So 4 of 4 COMPUTED are recomputable from shipped bytes on substance, with one qualification that swallows the point: **one of the two build.py-section tags names `[9f]`, which executed zero assertions** (F-OP22S-01). Half the machine-validated COMPUTED population this round is backed by a gate that did not run.

`[9c]` validates that a COMPUTED tag names a real build.py section. It cannot tell whether that section did anything. That gap is now load-bearing rather than theoretical.

## 4. Probes (B, C)

Sandbox copies against a pristine reference; pre/post hash assertion on every mutation per D-3.5.

**P-1 -- benign control.** Unmodified packet: build rc=0, 164 PASS, 0 FAIL; pytest rc=0, 186 passed.

**P-2 -- discrimination control.** `xz_protocol_v0_22.md` pre `0f84011b10d80589` post `5f79c001af4cee64`, LANDED. FB-4 `test_xz_protocol_source_frame.py` digest to 64 zeros. Build rc=1:
```
FAIL: FB-4 row contains test_xz_protocol_source_frame.py digest (04bea901b9cbefe8...)
FAIL: FB-4 digest for test_xz_protocol_source_frame.py in body
FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)
FAIL: PACKET_SHA256SUMS digest matches: xz_protocol_v0_22.md
```

**P-3 -- forgery regression.** Pre `0f84011b10d80589` post `16b115345cdc04f1`, LANDED. Mutated carried entry v0.10 in place, regenerated all 22 seals, FULL_SECTION_27, and the manifest, left PRIOR_HISTORY honest. Build rc=1 with exactly one error: `FAIL: PRIOR_HISTORY matches derivation (4a2842d20f9058f6...)`. `sha256sum -c` returns rc=0, so the manifest layer is blind and the recursive derivation is the sole detector. The control survives the rewrite.

**P-4 -- novel class: gate disabled by its own bug report.** Pre `0f84011b10d80589` post `ddb14ea7e680e0b7`, LANDED. Replaced the quoted phrase in item (1) -- `its anchor phrase "Adjudicated ledger:" was absent` -- with a paraphrase, changing nothing else, and resealed. Build rc=1:
```
[9f] Ledger-register reconciliation
  Register: 14 items, {'HIGH': 4, 'MEDIUM': 4, 'LOW': 5, 'INFORMATIONAL': 1}
  FAIL: Finding F-OP21C-04 dispositioned at MEDIUM and INFORMATIONAL
  No combined ledger; register self-consistency: 20 unique IDs, 14 items
```
On the shipped bytes that FAIL does not appear, because `re.search(r'Adjudicated ledger:\s*(.*?)(?:\[|$)', ...)` matches at span (1713, 1801) on `Adjudicated ledger:" was absent from the v0.21 entry, yet it` -- the narrative quotation inside the item reporting the v0.21 defect. → F-OP22S-01, F-OP22S-02.

**P-5 -- v0.23 forward test.** Direct call into the shipped `derive_prior_history` with `VERSION` advanced and an honest v0.23 `HISTORY.sha256`. honest `6358a9ba4dcb3d7f89c173ef752a4894...`, derived `6358a9ba4dcb3d7f89c173ef752a4894...`, **MATCH**. F-OP21S-01 is fixed durably, not just for this version: the recursion handles a missing scrape, and the v0.22 entry additionally carries its own PRIOR_HISTORY value inline.

**P-6 -- novel class: range-versus-register reconciliation.** No mutation; a parse of the shipped entry. The entry declares three ID ranges in its first sentence -- `F-OP21-01 through F-OP21-05`, `F-OP21S-01 through F-OP21S-08`, `F-OP21C-01 through F-OP21C-10` = 23 IDs. The register dispositions 21 ID slots, 20 distinct. Absent: `F-OP21S-03`, `F-OP21S-04`, `F-OP21S-05`. No gate implements this reconciliation, which D-3.7 requires. → F-OP22S-03.

**Void probes.** None.

## 5. Findings

**F-OP22S-01** [HIGH -- advisory, cannot carry] -- `[9f]` silently skipped for a second consecutive round, disabled by item (1)'s own quotation of the v0.21 bug report.
- **Locus:** `build.py` `[9f]`, `ledger_match = re.search(r'Adjudicated ledger:\s*(.*?)(?:\[|$)', current_entry)`; Section 27, v0.22 entry, item (1).
- **Substance:** Item (1) states the fix as "the gate fires or fails rather than silently skipping" and tags it `[COMPUTED: build.py [9f] ledger-register reconciliation]`. On the shipped bytes `[9f]` prints one informational register line and executes **zero** `check()` calls. The anchor regex matched the phrase where item (1) quotes it while describing the v0.21 failure. An empty capture yields no tally, so the tally branch runs nothing, and because `ledger_match` is truthy the **else-branch is skipped entirely** -- and that branch holds the duplicate-finding-ID check added for F-OP21S-03 and F-OP21C-02. P-4 shows that with the false anchor removed the gate fails the build immediately. The sentence reporting the defect is what reproduces it. The build's PASS count fell 168 to 164 across the version, which is the observable signature.
- **Disposition:** Stop anchoring on free prose. Require a delimited ledger block with a fixed key in every entry and `check()` its presence, so a quotation in narrative cannot be mistaken for the datum. Independently, move the register self-consistency checks out of the else-branch so they run unconditionally -- they do not depend on a ledger existing.
- **Cross-reference:** F-OP21S-02 (the v0.21 instance); F-OP21-01; F-OP21C-01; F-OP20F-08 (silent-skip class); D-3.7.

**F-OP22S-02** [HIGH -- advisory, cannot carry] -- F-OP21C-04 is dispositioned twice at two severities, in the same entry that corrects v0.21 for the identical defect.
- **Locus:** Section 27, v0.22 entry, items (7) and (14); correction (c) of the same entry.
- **Substance:** Item (7) is "F-OP21C-04 MEDIUM NOTED" concerning the stale 24.4% coverage figure. Item (14) is "F-OP21-05 / F-OP21S-08 / F-OP21C-04 INFORMATIONAL NOTED" concerning the ungated share and the ASSERTED fraction. Correction (c) of this same entry raises precisely this defect against v0.21 -- "the v0.21 register dispositions F-OP20F-05 twice at two severities" -- and item (4) records a gate added to catch it. The gate did not run (F-OP22S-01), and the entry committed the defect it was correcting. Correction (c) itself names the pattern: "a reconciliation error inside the entry that raises the reconciliation correction." That sentence is now true of v0.22 as well as v0.21.
- **Disposition:** Append-only correction in v0.23 assigning item (14) to `F-OP21-05 / F-OP21S-08` and leaving F-OP21C-04 solely at item (7). Land F-OP22S-01's fix first, or the same check will be unavailable again.
- **Cross-reference:** correction (c); F-OP21S-03; F-OP21C-02; F-OP22S-01.

**F-OP22S-03** [MEDIUM -- advisory, cannot carry] -- three declared findings are absent from the register, and one is absent in substance as well.
- **Locus:** Section 27, v0.22 entry, first sentence range statement versus the fourteen-item register.
- **Substance:** The entry declares "shallow continuous: F-OP21S-01 through F-OP21S-08" and dispositions five of the eight. F-OP21S-03 and F-OP21S-04 have their substance handled -- correction (c) and item (4) cover the duplicate-ID defect, item (7) covers the stale coverage figure -- but both are credited only to the fresh instance's F-OP21C-02 and F-OP21C-04, and my IDs appear nowhere. **F-OP21S-05 is absent entirely**, in ID and in substance: the `[9c]` `file_computed` regex is byte-identical to v0.21's, so no fix was attempted. D-3.7 states a finding may be closed, disclosed, or noted, **but not absent**. This is the F-ADJ19-04 class -- a finding raised in a range statement and dispositioned nowhere -- which the record has now committed at v0.18 (F-OP17-09), v0.19 (F-OP18-09), and v0.22. I raise this at MEDIUM rather than HIGH because two of the three are substantively covered and only the credit is lost; F-OP21S-05 alone is a genuine drop, and it is written up separately below.
- **Disposition:** Implement the reconciliation as a gate: parse every `F-<ns>-NN through F-<ns>-MM` range in the current entry, expand it, and assert every expanded ID appears in the register. Section [E] of the shipped harness is a working reference. Disposition the three absent IDs in v0.23.
- **Cross-reference:** F-ADJ19-04; F-OP18-09; D-3.7; F-OP22S-05.

**F-OP22S-04** [MEDIUM -- advisory, cannot carry] -- item (14) reports the prior round's measurements as if they were this round's, and item (7)'s claim about coverage derivation is false of the only coverage figures the entry contains.
- **Locus:** Section 27, v0.22 entry, items (7) and (14).
- **Substance:** Item (14) states the ungated share "rose for a fourth consecutive round (26.2%, 29.6%, 33.7%, 36.8%)". The series ends at v0.21's figure; `[11]` on these bytes computes **39.2%**, making this the fifth consecutive rise. The same item states "The ASSERTED fraction rose from 50.0% to 57.1% while COMPUTED fell from 11 to 9" -- the v0.20-to-v0.21 transition. This round's own figures are **78.9% and COMPUTED 4**, a far larger move, and they are omitted. Item (7) asserts "Coverage figures in this entry are derived from [11] output at build time"; the entry's only coverage figures are the ones in item (14), and they are not. This is the identical defect item (7) is dispositioning -- a measurement carried from the previous entry's prose -- committed in the entry that dispositions it, and it is now the third consecutive round in which the coverage series stops one short of its own value.
- **Disposition:** Have `[11]` emit its percentages and add a gate asserting the current entry's stated coverage and ASSERTED figures equal the computed ones, exactly as `[3]` already does for digests. These numbers are as machine-derivable as digests and there is no reason for them to be ASSERTED. Correct both figures in v0.23.
- **Cross-reference:** F-OP21S-04; F-OP21C-04; F-OP18-12; the Axiom-3 class.

**F-OP22S-05** [MEDIUM -- advisory, cannot carry] -- F-OP21S-05 was not fixed and not dispositioned; the arity-one regex stands unchanged.
- **Locus:** `build.py` `[9c]`, `file_computed = re.findall(r'\[COMPUTED:\s*sha256sum\s+(?:of\s+)?(\S+\.(?:md|py|json))', current_entry)`.
- **Substance:** Byte-identical to the v0.21 line; I diffed them directly. The check captures one filename per tag. The v0.20 defect it exists to close was `[COMPUTED: sha256sum of XZ_v17_SEAT_A_REPORT.md and XZ_v17_SEAT_B_REPORT.md]` -- two files, neither shipping -- and on that input it verifies the first and passes the second silently. I demonstrated this at v0.21 with a landed mutation. The v0.22 entry does not disposition the finding at any severity.
- **Disposition:** Capture every filename-shaped token in the tag body and `check()` each.
- **Cross-reference:** F-OP21S-05; F-OP20F-04; F-ADJ19-02; F-OP22S-03.

**F-OP22S-06** [LOW -- advisory, cannot carry] -- the recursion's termination path searches for a hand-populated literal, which is the practice F-OP20F-05 was raised against.
- **Locus:** `build.py` `derive_prior_history`, `cb = re.search(r'cb67f222[0-9a-f]{56}', et)`.
- **Substance:** The v0.19 termination branch falls back to searching that entry for a hex string with a hardcoded eight-character prefix. D-8, as shipped at v0.20 and v0.21, requires "Any value set the build compares against is derived from the file list by tool. No hand-populated set, no fill-in placeholder," and that clause is the stated basis of F-OP20F-05 and of item (3)'s own fix. The branch is **dead code on these bytes** -- the v0.19 entry does carry a scrapeable PRIOR_HISTORY value, so the `if ph:` path always wins -- which is why this is LOW rather than MEDIUM. It is a dormant hand-populated comparand in the one function the program has spent three rounds de-hardcoding.
- **Disposition:** Delete the branch. If the v0.19 scrape ever fails, the correct behaviour is a build failure, not a literal.
- **Cross-reference:** F-OP20F-05; F-OP21S-01; D-8.

**F-OP22S-07** [LOW -- advisory, cannot carry] -- the PDF is unbound for a third consecutive round and now carries a confirmed convention breach no gate can see.
- **Locus:** `PACKET_SHA256SUMS` and `build.py` `required_members` (PDF absent in both); Section 27, v0.22 entry, items (9) and (10).
- **Substance:** `xz_protocol_v0_22.pdf` ships in the dispatch and no shipped text carries its digest, third round running, dispositioned NOTED each time. Item (10) newly records F-OP21C-07, that the renderer converts double-hyphens to en-dashes. I confirmed it independently: the PDF contains 134 U+2013 and zero `--`, against 189 `--` and zero U+2013 in the source. So the em-dash convention -- clean in every normative file -- is breached in the one shipped artifact outside the gate perimeter, and the build cannot detect it because the file is not in the perimeter. The two findings are the same finding: an unbound artifact is one nothing can check. Content otherwise agrees with the .md on all six load-bearing values I sampled.
- **Disposition:** Add the PDF to `PACKET_SHA256SUMS` and to `[12]`'s required members, then extend the `[4]` sweep to its extracted text. Both NOTEDs close together or neither does.
- **Cross-reference:** F-OP20F-07; F-OP21C-07; F-FABLE5-03; D-3.6.

**F-OP22S-08** [INFORMATIONAL] -- provenance backing has more than halved across two rounds while the register grew.
- **Locus:** v0.22 entry tag distribution; D-7 question 3.
- **Substance:** COMPUTED 11 at v0.20, 9 at v0.21, 4 at v0.22. ASSERTED fraction 50.0%, 57.1%, 78.9%. The register went from 12 items to 14 over the same span. At v0.20 I noted a rising fraction can mean more disclosure; at v0.21 I withdrew that reading; this round it is not tenable at all. Item (6) correctly grades the `[9e]` regex DISCLOSED NOT CLOSED and item (2) correctly downgrades F-OP20-02 to CLOSED IN PART, so the reclassification is honest work rather than concealment -- but the direction is unambiguous, and one of the four surviving COMPUTED tags is backed by a gate that did not execute. The move that would reverse it is the one Section 22.2 already names and no round has taken: an external deposit receipt for `HISTORY.sha256`, which would make EXTERNAL non-vacuous for the first time in twenty-two versions.
- **Cross-reference:** F-OP21S-08; F-OP20-03; Section 22.2 anchor (b).

**Clears.** Step 1 rc=0. Build green, 186/186 tests, all seals and surjectivity verify. The recursive PRIOR_HISTORY derivation reproduces the shipped value, matches the true digest of the v0.21 file I hold, survives the v0.23 forward step, and still detects a retroactive carried-entry forgery (P-3) with exactly one correct error. `[3a]`, `[3b]`, `[3c]`, `[9e]`, and `[12]` remain live. Corrections (c) and the item-(2) downgrade of F-OP20-02 to CLOSED IN PART are both accurate and creditable. D-8 is split out of the shipped dispatch block. Em-dash and brand sweeps clean at source.

## 6. V0.21S finding self-score (D)

| ID | v0.21 severity | v0.22 disposition | Landed in bytes? |
|---|---|---|---|
| F-OP21S-01 | HIGH | HIGH CLOSED, item (3) | **Yes, and durably.** Recursion replaces the prose scrape; v0.23 forward test passes; P-3 shows the detector survives |
| F-OP21S-02 | HIGH | HIGH CLOSED, item (1), with `F-OP21-01 / F-OP21C-01` | **No.** `[9f]` ran zero assertions again -- F-OP22S-01 |
| F-OP21S-03 | MEDIUM | **Absent.** Substance covered by correction (c) and item (4) as F-OP21C-02 | Substance yes, ID dropped -- F-OP22S-03 |
| F-OP21S-04 | MEDIUM | **Absent.** Substance covered by item (7) as F-OP21C-04 | Substance yes, ID dropped; and the same defect recurs -- F-OP22S-03, F-OP22S-04 |
| F-OP21S-05 | MEDIUM | **Absent entirely** | **No.** Regex byte-identical -- F-OP22S-05 |
| F-OP21S-06 | LOW | MEDIUM NOTED, item (6), with `F-OP21-04` | Partly. Item (6) addresses only the `[9e]` regex narrowness; the silent-skip census went 18 to 19 |
| F-OP21S-07 | LOW | LOW NOTED, item (9), with `F-OP21C-06` | **Partly.** D-8 is split out this round; my two prior reports still ship |
| F-OP21S-08 | INFORMATIONAL | INFORMATIONAL NOTED, item (14) | Disclosed; figures are the prior round's -- F-OP22S-04 |

Eight raised, five dispositioned, three absent. One fully landed, three partly, one honest NOTED, one claimed CLOSED without landing, one dropped.

**What two prior rounds bought, scored honestly.** The external chain anchor in §7 -- unavailable to any other seat, and the only genuinely privileged result here. F-OP22S-03, since I authored the F-OP21S namespace and can tell the difference between a finding dispositioned under another ID and a finding dropped. F-OP22S-05, which required diffing a regex across two packets I hold. And the P-3 comparison, which means something only against the v0.20 baseline of 164 PASS on a forged packet. It bought **nothing** for F-OP22S-01, -02, -04, -06, or -07: all five come from reading the shipped `build.py` against the shipped entry, and a fresh seat finds every one. The continuous seat's failure mode is unchecked commendation, and its shape here would be reporting that F-OP21S-01 was fixed -- it was, elegantly -- and stopping before asking whether the round's other two headline fixes ran at all.

## 7. PRIOR_HISTORY chain verification (E)

Two links verified against the actual prior files, not against a derivation:

| Link | Shipped value | sha256 of the file I hold | Match |
|---|---|---|---|
| v0.22 → v0.21 | `4a2842d20f9058f6b362e8ab40d1450ba499eb2caa39417cfa0880348bbce600` | v0.21 `HISTORY.sha256` | **Yes** |
| v0.21 → v0.20 | `e181d6427153ab232a5dc5bf9c259fa3192e783cbb7cd4495ecc73d5988e8ff8` | v0.20 `HISTORY.sha256` | **Yes** |

All 21 carried entry seals in the v0.22 `HISTORY.sha256` are byte-identical to their values in the v0.21 file, and all 20 to their values in the v0.20 file. The append-only discipline held across three consecutive packets with zero in-place mutation of any carried entry -- the first multi-round external confirmation of that property in the program's record, and the strongest single result of this round.

Two qualifications. This anchor exists because a dispatch happened to give one instance three consecutive packets; it is an accident of composition, not a designed control, and it disappears when this conversation ends. And it does not reach the residual Section 22.2 names: a party controlling `build.py` can still replace the derivation, which is why the recursion is a consistency proof and not an integrity guarantee. What would make it durable is trivial and still untaken -- publish `4a2842d2...` where the producer cannot revise it and cite it EXTERNAL in the v0.23 entry.

## 8. Boundary report (F)

The boundary did not move this round. It moved inward at v0.21 when the derivation was wired in, and v0.22 consolidated that gain rather than extending it: the recursion made the control durable across version steps and P-5 confirms it survives to v0.23, which is real engineering, but every anchor that would actually cross the perimeter is in the same state it was two rounds ago. EXTERNAL count is zero for the fourth consecutive entry. No deposit receipt is cited. The PDF is unbound for the third round running and now demonstrably diverges from the source on the em-dash convention, which is the first concrete instance of the unbound-artifact risk becoming an actual defect rather than a hypothetical one. Meanwhile the perimeter's interior got thinner: COMPUTED backing fell from 9 to 4, and one of the four survivors names a gate that executed nothing. The one crossing that exists is in §7 and is not in the packet at all -- it lives in my retained copies of two prior dispatches. The disposition has been the same since my v0.20 report and gets cheaper every round the derivation holds: publish the current `HISTORY.sha256` digest at deposit time where the producer cannot revise it, and cite it EXTERNAL. Twenty-two versions in, that remains the only move that would let someone who does not trust the producer check anything, and it is the one move no version has made.

## 9. D-7 process health (H)

- **Did every probe come from an enumerated list?** No. P-4 and P-6 are novel; neither appears in D-4's classes. P-4 in particular could only come from asking why a gate's output shape looked wrong.
- **Did the dispatch tell me where to look?** Yes, heavily, and increasingly so. Deliverable D structures §6, deliverable E structures §7, and the packet ships both of my prior reports. Five of my eight findings came from reading the new `build.py` against the new entry rather than from any of that, and those are the five worth weighting.
- **Is the ASSERTED fraction unchanged from the prior round?** No -- 57.1% to 78.9%, third consecutive rise and the largest yet, with COMPUTED falling 9 to 4 while the register grew 12 to 14. This is the most important of the four questions and the answer is worse than in either prior round.
- **Have the recent rounds all been producer-family?** Yes. v0.20, v0.21, and v0.22, with all three seats in this round being Opus 5 instances. The last non-producer contact was the v0.19 tri-seat round, three rounds ago. FB-7b has not moved.

## 10. Verdict

**HALT-AND-RETURN-TO-PRODUCER -- advisory only, non-binding.**

Severity ledger as I calibrate it: 0 CRITICAL / 2 HIGH / 3 MEDIUM / 2 LOW / 1 INFORMATIONAL = 8.

**Standing, restated.** Producer-family advisory. Cannot HALT, cannot carry HIGH into the adjudicated set, no FB-7b weight. My two HIGHs enter at whatever severity a non-producer seat assigns, or not at all.

The HALT rests on F-OP22S-01 and F-OP22S-02 together, because they are one event: the gate written to stop duplicate dispositions was disabled by the sentence reporting that it had been disabled, and the entry then committed the duplicate the gate existed to catch. That is not a defect in a check; it is a check whose input is the prose that describes it, and it will recur in some new form at v0.23 unless the anchoring is changed rather than the phrasing. It costs one delimiter to fix and should be fixed before this entry is sealed.

The three findings I would most want a non-producer seat to re-derive, since a producer-family instance auditing fixes to its own prior findings is the least credible configuration available: **F-OP22S-01**, which is one string replacement and a rebuild, mechanized at section [D] of the shipped harness; **F-OP22S-03**, which is a range expansion against a register, mechanized at section [E]; and **F-OP22S-04**, which is two numbers against the build's own stdout. None requires taking my word for anything.

This is the third consecutive producer-family round. The single most useful thing the program could do next is not another gate but the deposit receipt in §8, followed by a non-producer carry. FB-7b remains OPEN and has not moved in three rounds.

---

*Claude Opus 5, Seat A-shallow, producer-family advisory. Prepared for Bilal Syed Arfeen. All probes reproducible from the shipped packet; no void probes this round.*

---

# Bismillah ir-Rahman ir-Rahim
