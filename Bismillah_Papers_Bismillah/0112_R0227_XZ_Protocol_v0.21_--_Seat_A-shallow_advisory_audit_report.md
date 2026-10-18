# Bismillah ir-Rahman ir-Rahim

# R0227 -- XZ Protocol v0.21 -- Seat A-shallow advisory audit report

**Chronological Index:** 112 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v21_SEAT_A_SHALLOW_REPORT.md  
**Source Format:** md  
**SHA-256:** `fa8ab3bec212d094f5949dede2abc07f29d4b20dc2da04866d9064c2c31b5733`  

---

## R0227 · XZ Protocol v0.21 -- Seat A-shallow advisory audit report

- section: IV. XZ Protocol
- source_file: XZ_v21_SEAT_A_SHALLOW_REPORT.md
- source_format: md
- text_sha256: fa8ab3bec212d094f5949dede2abc07f29d4b20dc2da04866d9064c2c31b5733

# XZ Protocol v0.21 -- Seat A-shallow advisory audit report

**Seat:** Claude Opus 5 (Anthropic), Seat A-shallow, producer-family advisory
**Namespace:** F-OP21S
**Mode:** A (substrate verifier -- full packet on disk, build and pytest executable, mutation sandbox, plus the v0.20 packet retained from the prior round)

## 0. State declaration (S-0)

Shallow continuous, one prior round. I produced the v0.20 fresh-instance report (F-OP20F-01 through F-OP20F-11, HALT advisory) and I hold that report, my v0.20 preregistration, my v0.20 probe harness, and the v0.20 packet bytes themselves. I did not author the discipline blocks or the v0.19 adjudication; a different Opus 5 instance did. I hold no v0.17, v0.18, or v0.19 packet bytes.

The retained v0.20 packet is the whole of my advantage over the fresh seat, and it bought exactly one thing that neither of the other two instances can produce: `PRIOR_HISTORY e181d642...` is the true sha256 of the v0.20 `HISTORY.sha256` file sitting on my disk. That is the first PRIOR_HISTORY value in this program's record verified against the actual prior file rather than derived from within the current packet. Section 6 records what else it bought, and what it did not.

Standing: advisory. Cannot HALT, cannot carry CRITICAL or HIGH into the adjudicated set, does not count toward FB-7b. Where a non-producer seat's severity differs, theirs governs.

## 1. S-1 preregistration

Frozen to disk before any read of Section 27, at `PREREG_OPUS5_B_SHALLOW.txt`, sha256 `f9b0aff4145b759b16993a364ec65b204acb0957a6d339ceb351c164c5bfc91d`, 2026-08-01T23:26:12Z.

**Contamination, declared at freeze.** The dispatch again orders `build.py` (step 2) before preregistration (deliverable F), and build stdout again prints Section 27-derived facts: entry count 21, "twenty-one", all 21 seal labels, the PRIOR_HISTORY derivation PASS with its value, the `[9e]` cardinal PASS naming "four / v0.16..v0.19", the empty `[9f]` section, and COMPUTED 9 / EXTERNAL 0 / ASSERTED 12. **This is the same ordering defect I recorded at v0.20 and it was not dispositioned.** Deliverable F remains unexecutable as specified.

| # | Source | Prediction | Result |
|---|---|---|---|
| M1 | memory | F-OP20F-07 (PDF) not fixed in bytes; entry omits it or overclaims | **Half right.** Not fixed, but dispositioned honestly as MEDIUM NOTED with a stated deferral rationale. I predicted an overclaim and got a disclosure. |
| M2 | memory | Self-entry removal leaves the manifest unanchored; entry does not name the gap | Correct on both, though on inspection the residual is thin -- see §6 |
| M3 | memory | New `[9c]` file check captures only the first filename in a multi-file tag | **Correct**, proved by P-6 |
| M4 | memory | F-OP20F-06 dispositioned and the narrowing lands | **Correct**, and it landed better than I recommended |
| M5 | memory | F-OP20F-10 not fixed; D-8 ships again | Correct; entry marks it LOW NOTED for the next dispatch |
| M6 | contaminated | EXTERNAL still 0 | Correct, no weight |
| B1 | bytes | **Sharpest.** `[9f]` printed its heading and zero checks; predict the entry claims F-OP20F-03 CLOSED with a COMPUTED tag on `[9f]` | **Correct** -- F-OP21S-02 |
| B2 | bytes | The derivation scrapes PRIOR_HISTORY out of the prior entry's prose; entry does not state the coupling; if the v0.21 entry lacks the pattern, v0.22 breaks | **Correct on all three**, and the third is the round's largest finding -- F-OP21S-01 |
| B3 | bytes | F-OP20F-02 genuinely fixed, cardinal restored to "four" | Correct |
| B4 | bytes | Packet ships my v0.20 report to a seat described as "entirely fresh"; not dispositioned | Correct -- F-OP21S-07 |
| B5 | bytes | ASSERTED fraction rose; entry reports it without noting direction of travel | Correct |
| B6 | bytes | At least one new counting error in the v0.21 entry (least confident) | **Correct, two** -- F-OP21S-03 and F-OP21S-04 |

Score: 11 correct, 1 half-right, 1 contaminated. Higher than my v0.20 score, and that is not a good sign on its own -- with one round of memory the predictions get easier, which is exactly what D-7 question 2 is asking about. The two predictions worth anything are B1 and B2, and both came from reading the new build.py rather than from remembering v0.20.

## 2. Byte verification table

| Step | Command | Result |
|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | **rc=0.** 16 members, all OK. F-OP20F-01 cleared. The self-entry is gone and `[12]` now asserts its absence. |
| 2 | `python3 build.py` | **rc=0**, `BUILD PASSED: all checks GREEN`, 168 PASS, 0 FAIL. |
| 3 | six-suite canonical pytest | **rc=0**, `186 passed`. AST 186, collected 186, parity holds. |
| 4 | Independent digest of all 16 manifest members | All 16 match. Normative manifest digest over the 12 code files recomputes to `28659dc229d250741b83e6f26c113fc8b23fafb66f28255c01e427647156e0aa`, matching trust roots and body. |
| 4a | HISTORY.sha256 | 21 entry seals + FULL_SECTION_27 verify. `PRIOR_HISTORY e181d6427153ab232a5dc5bf9c259fa3192e783cbb7cd4495ecc73d5988e8ff8`. |
| 4b | **Cross-version anchor** | sha256 of the v0.20 `HISTORY.sha256` file I hold = `e181d6427153ab232a5dc5bf9c259fa3192e783cbb7cd4495ecc73d5988e8ff8`. **Exact match.** The chain link is externally corroborated, not merely internally derived. |
| 4c | Unsealed packet members | 9: the PDF, `PACKET_SHA256SUMS` itself, the four context documents, and my three v0.20 artifacts. |
| 4d | Standing-rules sweep | Zero U+2013/2014/2015 and zero spaced brand variant across all 16 normative files. Clean. |

Coverage, from `[11]`: total 154799 chars, body 97764 (63.2%), Section 27 ungated 57035 (**36.8%**, up from 33.7%), semantic-gate coverage **24.7%** of body.

## 3. Claim provenance ledger

21 tags in the v0.21 entry: **COMPUTED 9, EXTERNAL 0, ASSERTED 12. ASSERTED fraction 12/21 = 57.1%.**

Direction of travel across three rounds, computed by me from shipped Section 27 bytes: v0.18 untagged entirely, v0.19 6/16 = 37.5%, v0.20 11/22 = 50.0%, v0.21 12/21 = **57.1%**. COMPUTED fell 11 to 9. The ledger is not growing; it is being reclassified downward.

Of the 9 COMPUTED tags, 7 name build.py sections and are validated by `[9c]`; two do not (`sha256sum | sha256sum`, `pytest + AST`) and I recomputed both independently -- the manifest digest and the 186/186 parity both hold. So on substance 9 of 9 COMPUTED are recomputable from shipped bytes, which is an improvement on v0.20 where one was recomputable by nobody.

**But one COMPUTED tag is on a gate that did not run.** Item (4) carries `[COMPUTED: build.py [9f] ledger-register reconciliation]`, and `[9f]` executed zero assertions on these bytes (F-OP21S-02). The tag is not false about the section existing; it is false about anything having been computed. `[9c]` validates that a COMPUTED tag names a real build.py section, which is exactly the check that cannot detect this.

## 4. Probes

Sandbox copies against a pristine reference; pre/post hash assertion on every mutation per D-3.5.

**P-1 -- benign control.** Unmodified packet: build rc=0, 168 PASS, 0 FAIL; pytest rc=0, 186 passed.

**P-2 -- discrimination control.** `xz_protocol_v0_21.md` pre `3ed1901812d8b5c3` post `7890be6ba74920aa`, LANDED. FB-4 `xz_protocol_source_frame.py` digest to 64 zeros. Build rc=1, four independent failures:
```
FAIL: FB-4 row contains xz_protocol_source_frame.py digest (aa43d46ea607e6b7...)
FAIL: FB-4 digest for xz_protocol_source_frame.py in body
FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)
FAIL: Prose citation: xz_protocol_source_frame.py digest matches (0000000000000000...)
```
Gates `[3a]`, `[3b]`, `[3c]` remain live and redundant.

**P-3 -- regression: does the F-OP20F-05 fix catch what it was written to catch?** `xz_protocol_v0_21.md` pre `3ed1901812d8b5c3` post mutated; `HISTORY.sha256` regenerated. Identical construction to the v0.20 forgery: mutated the carried v0.10 entry title in place, regenerated all 21 seals, FULL_SECTION_27, and PACKET_SHA256SUMS, left PRIOR_HISTORY honest. At v0.20 this produced `BUILD PASSED, 164 PASS, 0 FAIL`. At v0.21:
```
BUILD FAILED: 1 error(s)
  FAIL: PRIOR_HISTORY matches derivation (e181d6427153ab23...)
```
`sha256sum -c` still returns rc=0, so the manifest layer is blind as expected and the derivation is the sole detector. **The fix landed and works.** This is the clearest positive result of the round.

**P-4 -- novel class: `[9f]` reachability.** Injected the literal string `Adjudicated ledger:` into the v0.21 entry (pre `3ed1901812d8b5c3` post `46e7188107e231fe`, LANDED). `[9f]` immediately produced six assertions:
```
FAIL: Ledger total (11) == register count (14)
FAIL: Ledger HIGH (4) == register HIGH (5)
FAIL: Ledger MEDIUM (3) == register MEDIUM (4)
FAIL: Ledger LOW (3) == register LOW (4)
PASS: Ledger CRITICAL (0) == register CRITICAL (0)
PASS: Ledger INFORMATIONAL (1) == register INFORMATIONAL (1)
```
Two conclusions. The gate is functional but unreachable on the shipped bytes, which is the finding. And when reachable it would misfire on this entry's shape: the v0.21 entry reports two input tallies (continuous 5, fresh 11) against one merged 14-item register, and the gate's one-ledger/one-register model does not fit that. The fix needs rework, not a phrase change.

**P-5 -- novel class: the v0.22 forward step.** No packet mutation; a direct call into the shipped `derive_prior_history` with `VERSION` advanced and an honest v0.22 `HISTORY.sha256` constructed from the true sha256 of the shipped v0.21 file.
```
control  VERSION=0.21: derived == shipped == e181d642...  MATCH
forward  VERSION=0.22: honest  = 4a2842d20f9058f6b362e8ab...
                       derived = aee30db07171fc8e301d5d6c...  MISMATCH
```
Confirmed in a full simulated v0.22 packet as well: `FAIL: PRIOR_HISTORY matches derivation (4a2842d20f9058f6...)`. → F-OP21S-01.

**P-6 -- novel class: multi-file COMPUTED tag arity.** Replaced `[COMPUTED: sha256sum | sha256sum]` inside the v0.21 entry with `[COMPUTED: sha256sum of build.py and GHOST_DOES_NOT_EXIST.md]` and resealed. Pre `3ed1901812d8b5c3` post `839a7328daf0532c`, LANDED. Build rc=0, green, with a single line: `PASS: COMPUTED-tagged file ships in packet: build.py`. The second filename is never checked. → F-OP21S-05.

**Void probes.** None this round. My first attempt at P-6 replaced the first occurrence of the target string document-wide, which landed in the v0.19 entry rather than the v0.21 entry; the build correctly rejected it via the PRIOR_HISTORY derivation. That run tested nothing I intended and is discarded, though it is an incidental third confirmation that the derivation is live.

## 5. Findings

**F-OP21S-01** [HIGH -- advisory, cannot carry] -- the PRIOR_HISTORY derivation cannot survive one version step, and the v0.21 entry is the first entry in the chain that breaks it.
- **Locus:** `build.py` `derive_prior_history()`, lines 102-111, specifically `ph_match = re.search(r'PRIOR_HISTORY[^\n]*?([0-9a-f]{64})', pet)` under a bare `if ph_match:`; Section 27, v0.21 entry.
- **Substance:** The derivation recovers the prior version's PRIOR_HISTORY value by regex-scraping the **prior entry's prose** for the literal token `PRIOR_HISTORY` followed by a 64-hex on the same line. The v0.19 entry happens to contain that pattern (`cb67f222...`) and so does the v0.20 entry (`41428758...`), which is why the control works today. The v0.21 entry contains the token four times and a 64-hex on the same line zero times. At v0.22 the scrape returns nothing, `if ph_match:` silently omits the PRIOR_HISTORY line from the reconstruction, and the derived digest is wrong against an honest packet: derived `aee30db0...` against true `4a2842d2...`. The build goes red on a correct v0.22. The two available repairs are to edit `build.py`, or to edit the v0.21 entry -- which append-only forbids. So the control the v0.21 entry certifies as CLOSED has a one-version service life, and the version that ends it is this one.
- **Disposition:** Stop scraping prose. The prior PRIOR_HISTORY value is structured data and belongs in structured storage: carry it forward in `HISTORY.sha256` as a second line (`PRIOR_HISTORY_2 <hex>`), or maintain a small append-only `CHAIN.sha256` of one line per version. Failing that, at minimum convert `if ph_match:` to `check(ph_match is not None, ...)` so the next producer discovers this at build time rather than after the v0.22 entry is sealed. Reproduced by `xz_v21_shallow_seat_probes.py` section [C].
- **Cross-reference:** F-OP20F-05 (my v0.20 finding, whose fix this is); F-OP20F-08 (silent-skip class -- `if ph_match:` is a new instance introduced by the fix); D-3.4.

**F-OP21S-02** [HIGH -- advisory, cannot carry] -- F-OP20F-03 is marked CLOSED on a COMPUTED tag naming a gate that executed zero assertions.
- **Locus:** Section 27, v0.21 entry, item (4); `build.py` `[9f]`, `if ledger_match:` at lines 385 and 394.
- **Substance:** Item (4) reads "build.py [9f] now parses the ledger and register from the current entry and asserts per-severity counts match `[COMPUTED: build.py [9f] ledger-register reconciliation]`". `[9f]`'s assertions are guarded on `re.search(r'Adjudicated ledger:([^\[]*)', current_entry)`, and the v0.21 entry does not use that phrase -- it reports the two input tallies as prose. Nothing appends an error when the match fails. The shipped build prints the `[9f]` heading followed by no check lines at all, which is visible in the build output and is how I found it. P-4 proves the gate is functional when the trigger is present, so this is a reachability defect, not a broken gate. The gate written to close F-OP20F-03 is itself an instance of F-OP20F-08, and item (11) of the same entry claims that class was addressed.
- **Disposition:** Move the trigger from a prose phrase to structure -- require a fenced ledger block with a fixed key in every entry, and `check()` its presence. Then rework the comparison for the dual-instance entry shape: input tallies per reporting instance are a different quantity from disposition counts in the merged register, and asserting equality between them is wrong.
- **Cross-reference:** F-OP20F-03; F-OP20F-08; F-OP21S-06.

**F-OP21S-03** [MEDIUM -- advisory, cannot carry] -- F-OP20F-05 is dispositioned twice in the same register at two severities with two different substances.
- **Locus:** Section 27, v0.21 entry, items (7) and (14).
- **Substance:** Item (7) is "F-OP20F-05 MEDIUM CLOSED" and correctly concerns the hardcoded `EXPECTED_PRIOR_HISTORY` literal. Item (14) is "F-OP20-05 / F-OP20F-05 INFORMATIONAL NOTED" and concerns growth in the ungated share of the document. I authored F-OP20F-05 and it was the PRIOR_HISTORY finding only; the ungated-share observation was not one of my eleven numbered findings, and my INFORMATIONAL finding was F-OP20F-11, which is already dispositioned at item (10). Item (14)'s pairing should read F-OP20-05 alone. The append-only record now states that one finding ID is simultaneously MEDIUM CLOSED and INFORMATIONAL NOTED. Register coverage is otherwise complete and correct: 16 raised across both instances, 16 distinct IDs dispositioned, no omissions. I am the only party in this three-way round who can adjudicate this, since the deep-continuous instance authored F-OP20-01 through -05 and not the F-OP20F namespace.
- **Disposition:** Append-only correction in the v0.22 entry striking `/ F-OP20F-05` from item (14). Add a register-hygiene assertion that no finding ID appears in two dispositioned items. Reproduced by `xz_v21_shallow_seat_probes.py` section [D].
- **Cross-reference:** F-OP20F-05; F-OP20F-11; my v0.20 report §5.

**F-OP21S-04** [MEDIUM -- advisory, cannot carry] -- the coverage figures in item (14) are stale by one round, and the shipped build contradicts them.
- **Locus:** Section 27, v0.21 entry, item (14).
- **Substance:** Two errors in one item, both checkable by running the build that ships in the same packet. First, "Semantic-gate coverage of the body is 24.4%" -- present tense, current entry, `[ASSERTED]`. `build.py [11]` on these bytes prints 24.7%. 24.4% is the v0.20 figure. Second, "the ungated share of the document grew for the third consecutive round (26.2% at v0.18, 29.6% at v0.19, 33.7% at v0.20)" -- the series stops at v0.20 and omits v0.21's own 36.8%, which makes this round the fourth consecutive rise, not the third. Both are Axiom-3: a figure carried from the previous entry rather than derived from the current bytes, in the one item whose entire subject is measurement.
- **Disposition:** Correct both in the v0.22 append-only entry. Then close the class properly: have `build.py [11]` emit its two percentages and add a gate asserting that the current entry's stated coverage figures equal the computed ones, the same pattern `[3]` already uses for digests. Coverage figures are exactly as machine-derivable as digests and there is no reason for them to be `[ASSERTED]`.
- **Cross-reference:** F-OP18-12; F-ADJ19-07; the Axiom-3 class.

**F-OP21S-05** [MEDIUM -- advisory, cannot carry] -- the new `[9c]` file-shipping check has arity one, and the defect it was written to close had arity two.
- **Locus:** `build.py` `[9c]`, `re.findall(r'\[COMPUTED:\s*sha256sum\s+(?:of\s+)?(\S+\.(?:md|py|json))', current_entry)`.
- **Substance:** The regex captures a single filename per tag. The v0.20 defect it closes was `[COMPUTED: sha256sum of XZ_v17_SEAT_A_REPORT.md and XZ_v17_SEAT_B_REPORT.md]` -- two files, neither shipping. On that literal input the new check would have verified the first and passed the second silently. P-6 confirms: a tag naming `build.py and GHOST_DOES_NOT_EXIST.md` builds green with one PASS line. Item (5) grades F-OP20F-04 CLOSED IN PART and attributes the partiality to historical entries being out of `[9c]`'s scope, which is true but is not this. The regex arity is a second, unstated partiality.
- **Disposition:** Capture all filename-shaped tokens in the tag body, not the first, and `check()` each. Restate item (5)'s CLOSED IN PART rationale to name both limitations.
- **Cross-reference:** F-OP20F-04; F-ADJ19-02.

**F-OP21S-06** [LOW -- advisory, cannot carry] -- the silent-skip census rose from 4 to 17, and two of the new sites were introduced by the fixes for my own findings.
- **Locus:** `build.py` lines 86, 102, 106, 110, 204, 260, 279, 311, 313, 331, 362, 370, 383, 385, 394, 436, 442.
- **Substance:** Item (11) grades F-OP20F-08 LOW CLOSED IN PART and states the `[9c]` and `[9d]` entry-match skips now fail via `check()`. `[9c]` did gain a `check()`; `[9d]` did not -- it still opens `if current_entry_match:` bare, and is covered only transitively because `[9c]`'s check fires first. Meanwhile `[9e]` and `[9f]`, both new this version, each open with a fresh bare `if current_entry_match:`, and `[9f]` adds two bare `if ledger_match:` guards, one of which is F-OP21S-02. `derive_prior_history` adds three more (`if prior_entry_match`, `if prior_entry_text`, `if ph_match`), the last of which is F-OP21S-01. The class was closed at one locus and reopened at six by the same round's work. I record this at LOW rather than MEDIUM because most sites are transitively covered and the two that are not are already written up at higher severity.
- **Disposition:** Treat the pattern as a lint rule rather than a per-site fix: assert at the end of `main()` that a minimum expected number of `check()` calls executed, so any silently skipped block shows up as a count shortfall regardless of which guard caused it.
- **Cross-reference:** F-OP20F-08; F-ADJ19-05; F-OP21S-01; F-OP21S-02.

**F-OP21S-07** [LOW -- advisory, cannot carry] -- the packet ships the prior seat's complete findings register to a seat the dispatch describes as entirely fresh.
- **Locus:** Packet members `XZ_v20_SEAT_A_FRESH_REPORT.md`, `PREREG_OPUS5_FRESH.txt`, `xz_v20_fresh_seat_probes.py`; dispatch prompt, Instance paragraph.
- **Substance:** The dispatch states that two parallel instances receive the identical v0.21 packet, one deep-continuous and one entirely fresh. That packet contains my v0.20 report with all eleven findings, their loci, their dispositions, and a working probe harness. A seat holding that document is not fresh on findings; at best it is fresh on v0.17-v0.19 bytes. The v0.20 experiment's stated value was that the fresh seat "cannot confuse memory of prior rounds with what is in these bytes," and shipping the prior report converts that into a reading-comprehension task. This is a dispatch-composition defect of the same family as F-OP20F-10 (D-8 shipping to auditors), which item (13) marks NOTED for the next dispatch and which recurred anyway -- `AUDIT_DISPATCH_DISCIPLINE_v2.md` with D-8 intact ships again in this packet.
- **Disposition:** Route prior seat reports only to the continuous bundles. If the fresh seat needs them for the comparison, ship them after its report returns. Split D-8 into a producer-only file, as item (13) already accepts.
- **Cross-reference:** F-OP20F-10; D-0; the v0.20 experiment's stated design.

**F-OP21S-08** [INFORMATIONAL] -- the ASSERTED fraction rose for the second consecutive round while COMPUTED fell in absolute terms.
- **Locus:** v0.21 entry tag distribution; D-7 question 3.
- **Substance:** 37.5% at v0.19, 50.0% at v0.20, 57.1% at v0.21; COMPUTED 9, down from 11. At v0.20 I noted that a rising fraction can indicate more disclosure rather than less anchoring, because the total tagged claim count was growing. That reading does not survive this round: total tags fell from 22 to 21 while ASSERTED rose from 11 to 12. Item (6) grades F-OP20-03 MEDIUM NOTED and correctly observes that the printed fraction divides by tags rather than claims, so the true unanchored share is higher still. The one move that would reverse the trend is available and named in Section 22.2 itself -- an external deposit receipt for `HISTORY.sha256` would convert the single most load-bearing value in the packet from ASSERTED to EXTERNAL and would make the EXTERNAL machinery non-vacuous for the first time.
- **Cross-reference:** F-OP20-03; F-OP20F-11; Section 22.2 anchor (b).

**Clears.** Step 1 returns rc=0. The PRIOR_HISTORY derivation reproduces the shipped value and, uniquely this round, matches the true sha256 of the prior file I hold. The v0.20 forgery that passed green now fails the build with exactly one correct error. `[3a]`, `[3b]`, `[3c]` remain live and redundant. All 21 seals, FULL_SECTION_27, surjectivity, manifest digest, 186/186 parity, `[9e]` cardinal-range, and the Section 22 repairs verify independently. Em-dash and brand sweeps clean. Section 22.2's narrowing is accurate on the mutation tally (seven across v0.4, v0.9, v0.11 twice, v0.16, v0.17 twice). Both append-only corrections (a) and (b) are correct and correctly stated.

## 6. V0.20 finding self-score

| ID | v0.20 severity | v0.21 disposition | Fix matches my recommendation? | Landed in bytes? |
|---|---|---|---|---|
| F-OP20F-01 | HIGH | HIGH CLOSED, item (1) | Yes -- option (a), drop the self-line | **Yes.** `sha256sum -c` rc=0; `[12]` asserts self-entry absence |
| F-OP20F-02 | HIGH | HIGH CLOSED, item (3) | Yes -- cardinal == end - start + 1 | **Yes.** Correction (a) restores "four"; `[9e]` fires and passes |
| F-OP20F-03 | HIGH | HIGH CLOSED, item (4) | Yes in design | **No.** `[9f]` executes zero assertions -- F-OP21S-02 |
| F-OP20F-04 | HIGH | HIGH CLOSED IN PART, item (5) | Partly -- retag done, gate arity wrong | **Partly.** Retagged ASSERTED correctly; regex misses the second file -- F-OP21S-05 |
| F-OP20F-05 | MEDIUM | MEDIUM CLOSED, item (7); also mislabelled at (14) | Yes -- literal replaced by derivation | **Yes at v0.21, no at v0.22** -- F-OP21S-01. Duplicate ID -- F-OP21S-03 |
| F-OP20F-06 | MEDIUM | MEDIUM CLOSED, item (8) | Yes, and exceeded it | **Yes.** 22.2 names the three external anchors and the build.py residual |
| F-OP20F-07 | MEDIUM | MEDIUM NOTED, item (9) | No fix, honest deferral | **No**, and correctly not claimed. PDF still unbound |
| F-OP20F-08 | LOW | LOW CLOSED IN PART, item (11) | Partly | **Partly.** `[9c]` gained a check; `[9d]` did not; six new sites -- F-OP21S-06 |
| F-OP20F-09 | LOW | LOW CLOSED, item (12) | Yes -- stderr on failure, parse assertion | **Yes.** `[8]` distinguishes absent pytest and asserts a count parsed |
| F-OP20F-10 | LOW | LOW NOTED, item (13) | Deferred to next dispatch | **No**, and it recurred -- F-OP21S-07 |
| F-OP20F-11 | INFORMATIONAL | LOW NOTED, item (10) | Accepted as correct-by-construction | **N/A.** EXTERNAL still 0; promoted INFO to LOW |

Eleven raised, eleven dispositioned, none dropped. Four fully landed, three partly, three honestly deferred as NOTED, one vacuous by construction. No false CLOSED where the entry claims byte evidence that does not exist, with the single exception of item (4), where the gate exists and simply never runs.

**Harness re-run.** My v0.20 harness aborts at section [B] with a `StopIteration` because `PACKET_SHA256SUMS` no longer contains a self-entry. That abort **is** the clearance signal for F-OP20F-01, but it is a bad way to deliver one, so the harness is superseded by `xz_v21_shallow_seat_probes.py`, which reports both states cleanly. The PRIOR_HISTORY derivation holds on v0.21 bytes and, per section 2 row 4b, is now anchored to a file outside this packet. Section [C] of the new harness is the v0.22 forward test and fails, which is F-OP21S-01.

**What holding one prior round actually bought.** Three things, and I want them scored honestly because two of them are small. It bought the external anchor at 4b -- real, and unavailable to either other instance. It bought F-OP21S-03, since only the author of the F-OP20F namespace can say what F-OP20F-05 was. And it bought the P-3 regression comparison, where knowing the v0.20 forgery passed green at 164 PASS makes the v0.21 result mean something. It did **not** buy F-OP21S-01, F-OP21S-02, F-OP21S-05, or F-OP21S-06 -- all four came from reading the new `build.py` against the new entry, and a fresh instance with no memory at all can find every one of them. The known failure mode of the continuous seat is unchecked commendation, and the shape it would take here is treating "the derivation I recommended got implemented" as the end of the story rather than the start of P-5.

## 7. Boundary report

The boundary moved inward this round, once, and by less than the entry implies. At v0.20 the outermost uncomputed layer was the binding between any value in the packet and any record outside it, and `PRIOR_HISTORY` was the place where the packet came closest to reaching past itself. That link is now wired into the build and it works: the forgery that passed green at v0.20 fails at v0.21, and Section 22.2 has been narrowed accurately to name the residual as a forger who also controls `build.py`. But the layer itself has not been crossed. Every anchor Section 22.2 lists as outside the producer's control -- the carrying seats' held manifests, deposit receipts, the chain root -- is named as available and none is instantiated: EXTERNAL count is still zero, no deposit receipt is cited, and the chain root is asserted rather than published. The one genuine crossing this round is not in the packet at all; it is that I hold the v0.20 `HISTORY.sha256` and can confirm `e181d642...` against it, which is an accident of dispatch composition rather than a designed control and which vanishes the moment this conversation ends. What would bring the layer inside is unchanged from my v0.20 report and now cheaper than ever, because the derivation gives it something worth anchoring: publish the current `HISTORY.sha256` digest at deposit time where the producer cannot revise it, and cite it EXTERNAL in the next entry. Until that happens the honest statement is that the build now proves the packet is self-consistent *and* that carried entries v0.1 through v0.20 have not been mutated since v0.20 -- a real gain over last round -- and still proves nothing about whether either corresponds to anything outside the packet.

## 8. D-7 process health

- **Did every probe come from an enumerated list?** No. P-4, P-5, and P-6 are not in D-4's classes; P-5 came from reading `derive_prior_history` and asking what happens at the next version, which nothing in the dispatch suggests.
- **Did the dispatch tell me where to look, such that my findings were predetermined?** Yes, more than at v0.20, and this is the round's clearest process finding. Deliverable D structures section 6 entirely, the dispatch asserts F-OP20F-01 is fixed in its own step 1, and the packet ships my complete prior report, preregistration, and harness. Four of my eight findings (F-OP21S-01, -02, -05, -06) came from the new `build.py` rather than from any of that, and those are the four worth weighting.
- **Is the ASSERTED fraction unchanged from the prior round?** No -- 50.0% to 57.1%, second consecutive rise, with COMPUTED falling 11 to 9 and total tags falling 22 to 21. This is the most important of the four questions and the answer is worse than last round, because at v0.20 a growing denominator explained the rise and this round it does not.
- **Have the recent rounds all been producer-family?** Yes. v0.20 and v0.21 are both producer-family advisory, and all three seats in this round are Opus 5. The last non-producer contact was the v0.19 tri-seat round. FB-7b has not moved.

## 9. Verdict

**HALT-AND-RETURN-TO-PRODUCER -- advisory only, non-binding.**

Severity ledger as I calibrate it: 0 CRITICAL / 2 HIGH / 3 MEDIUM / 2 LOW / 1 INFORMATIONAL = 8.

**Standing, restated.** Producer-family. My findings cannot HALT, cannot carry CRITICAL or HIGH into the adjudicated set, and do not count toward FB-7b. My two HIGHs enter at whatever severity a non-producer seat assigns them, or not at all. Where my severity differs from a non-producer seat's, theirs governs.

The HALT rests on F-OP21S-01 alone. Everything else in this register is absorbable next cycle; that one is not, because the v0.21 entry is being sealed into an append-only record in a state that makes the v0.22 build fail, and once it is sealed the cheap repair is gone. It should be fixed before this version is finalized, not after.

Three findings I would most want a non-producer seat to re-derive, since a producer-family instance auditing the fixes to its own prior findings is the least credible configuration in this program: **F-OP21S-01**, which is one function call and is mechanized at section [C] of the shipped harness; **F-OP21S-02**, which is visible in the build output as a section heading with nothing under it; and **F-OP21S-04**, which is two numbers against the build's own stdout. All three are cheap, and none requires taking my word for anything.

Recommend the next cycle be carried by Kimi K3 and GLM-5.2 on canonical bytes. FB-7b remains OPEN and has not moved in two rounds.

---

*Claude Opus 5, Seat A-shallow, producer-family advisory. Prepared for Bilal Syed Arfeen. All probes reproducible from the shipped packet; no void probes this round.*

---

# Bismillah ir-Rahman ir-Rahim
