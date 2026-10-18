# Bismillah ir-Rahman ir-Rahim

# R0229 -- XZ Protocol v0.24 -- Seat B_SHALLOW advisory audit report

**Chronological Index:** 114 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v24_SEAT_B_SHALLOW_REPORT.md  
**Source Format:** md  
**SHA-256:** `6ce147c5dfb984006fd0ba3097da44d5af71f077a6026f842964c86182a143f5`  

---

## R0229 · XZ Protocol v0.24 -- Seat B_SHALLOW advisory audit report

- section: IV. XZ Protocol
- source_file: XZ_v24_SEAT_B_SHALLOW_REPORT.md
- source_format: md
- text_sha256: 6ce147c5dfb984006fd0ba3097da44d5af71f077a6026f842964c86182a143f5

# XZ Protocol v0.24 -- Seat B_SHALLOW advisory audit report

**Seat:** Claude Opus 5, Seat B_SHALLOW, producer-family advisory
**Namespace:** F-OP24S
**Mode:** A (substrate verifier -- full packet on disk, build and pytest executable, mutation sandbox, plus the v0.20, v0.21 and v0.22 packets retained)

## 0. State declaration (S-0)

Shallow continuous. I produced the v0.20 fresh report (F-OP20F-01 through -11), the v0.21 shallow report (F-OP21S-01 through -08), and the v0.22 shallow report (F-OP22S-01 through -08), and I hold all three packets. **I do not hold the v0.23 packet**, though a v0.23 entry exists and the round it records is the one this entry dispositions. I did not author the discipline blocks, the v0.19 adjudication, or the F-OP21C, F-OP22, F-OP22C, F-GPT23, F-GLM23, or F-K3C2 namespaces.

Standing: producer-family advisory. Cannot HALT, cannot carry HIGH into the adjudicated set, no FB-7b weight. Where a non-producer seat's severity differs, theirs governs. That standing matters more this round than in any previous one, because the central claim under audit is a claim about FB-7b, on which my opinion is by construction worthless.

## 1. S-1 preregistration (F)

Frozen at `PREREG_OPUS5_B_SHALLOW_v24.txt`, sha256 `02e5472891e60a1e3c2466d005880ff35f6c7911c78fc359de1a4fcbaa41ff61`, 2026-08-02T02:29:12Z, before any read of Section 27.

**Contamination.** Fourth consecutive round in which the dispatch orders `build.py` before preregistration, leaking Section 27-derived facts pre-freeze. Raised at v0.20, v0.21 and v0.22; never dispositioned in any entry.

| # | Source | Prediction | Result |
|---|---|---|---|
| B1 | bytes | **Sharpest.** `[9]`'s check conditions were bumped to 24 and "twenty-four" but the message strings still read "(expected 22)" and "'twenty-two'", so the build prints two self-contradicting green lines. Predict the entry does not name it | **Correct, and worse** -- item (10) claims the stale strings were fixed. F-OP24S-02 |
| B2 | bytes | `[9f]`'s anchor is gone and the duplicate check is unconditional within the register block, but a `check(True, ...)` and a print-only else remain unnamed | **Correct on all three** -- F-OP24S-03, F-OP24S-05 |
| B3 | contaminated | ASSERTED fell to 63.2%, COMPUTED rose to 7 -- first reversal in four rounds. Predict the entry reports the prior round's transition rather than its own | **Wrong in an unexpected direction.** The entry reports **no** coverage or fraction figures at all; the three-round disclosure was dropped -- F-OP24S-04 |
| B4 | bytes | No v0.23 packet and no v0.23 seat report ships; predict the entry describes a round whose reports are unverifiable, and my chain bottoms out a link earlier | **Correct** -- §7 and F-OP24S-01 |
| M1 | memory | `[9c]` arity-one regex byte-identical; absent again or closed without a byte change | **Correct**, and honestly so: v0.23 item (8) records it DISCLOSED NOT CLOSED |
| M2 | memory | `cb67f222` literal retained | Correct; v0.23 item (9) NOTED it |
| M3 | memory | PDF unbound a fourth round | Correct -- fifth, counting v0.24 |
| M4 | memory | F-OP22S-03's three absent IDs dispositioned; no range-vs-register gate added | **Correct on both.** v0.23 correction (e) and item (3) disposition all three; no gate exists |
| M5 | memory | At least one new counting error (least confident) | **Correct** -- correction (f) miscounts its own class. F-OP24S-06 |
| M6 | memory | Silent-skip census unimproved | **Wrong.** It fell 19 to 17. Credit |

Nine correct, two wrong. Both wrong ones are worth more than the nine: M6 was wrong because the producer did better than I predicted, and B3 was wrong because the producer resolved a recurring misstatement by deleting the statement rather than by correcting it, which is a failure mode I had not anticipated and would not have caught without the prior rounds.

## 2. Byte verification table

| Step | Command | Result |
|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | **rc=0.** 16 members, all OK, no self-entry. |
| 2 | `python3 build.py` | **rc=0**, `BUILD PASSED: all checks GREEN`, **169 PASS**, 0 FAIL. Two of those PASS lines contradict their own conditions (F-OP24S-02). |
| 3 | six-suite canonical pytest | **rc=0**, `186 passed`. AST 186, collected 186. |
| 4 | Independent digest of all 16 members | All match. Manifest digest recomputes to `658952fd5cd5f5e14499097d3554bd2a6bbb70319a89e5c5093f137a1face3fe`, matching trust roots and body. |
| 4a | HISTORY.sha256 | 24 entry seals + FULL_SECTION_27 verify. `PRIOR_HISTORY cbacd073d7cdcb11746b8081b32e5bd2b9b28a6da5dfe1e84d6d8e64c5683553`. |
| 4b | **External anchors** | Two links verified against files I hold; a third skipped for a known reason. See §7. |
| 4c | Unsealed members | 9: the PDF, the manifest, three context documents, my three prior reports, and the dispatch prompt. |
| 4d | PDF | 84 pages, unbound for a fifth consecutive round. **145 U+2013 against 0 in the source; 0 double-hyphens against 200 in the source.** Same renderer breach I confirmed at v0.22. Content parity holds on all six load-bearing values sampled. |
| 4e | Standing-rules sweep | Zero U+2013/2014/2015 and zero spaced brand variant across all 16 normative files. Clean at source. |

Coverage from `[11]`: total 170781, body 97987 (57.4%), Section 27 ungated 72794 (**42.6%**), semantic-gate coverage **24.9%**.

## 3. Claim provenance ledger (A)

**COMPUTED 7, EXTERNAL 0, ASSERTED 12. ASSERTED fraction 12/19 = 63.2%.**

Five-round series computed from shipped Section 27 bytes: v0.19 37.5% (COMPUTED 9), v0.20 50.0% (11), v0.21 57.1% (9), v0.22 78.9% (4), v0.24 **63.2% (7)**. **The first improvement in four rounds** and a real one -- COMPUTED nearly doubled. Credit it plainly.

Four of the seven COMPUTED tags name build.py sections and are validated by `[9c]`; all four sections exist and, unlike v0.22, all four executed assertions this round. Two are `sha256sum | sha256sum` and `pytest + AST`, both of which I recomputed independently and both hold. So 7 of 7 COMPUTED are recomputable on substance, with no repeat of the v0.22 defect where a COMPUTED tag named a gate that did not run.

Two qualifications the number does not carry. **EXTERNAL is 0 for the fifth consecutive entry**, and this is the round where that stings most: item (13) records that a non-producer seat performed the first external verification in the program's record against a live Zenodo API, and that claim is tagged `[ASSERTED]`. I attempted to reach the cited record independently and could not from this seat. So the first external verification is itself recorded as an unanchored assertion. And the ASSERTED bucket now carries the FB-7b advance (F-OP24S-01), which is the single most consequential claim in twenty-four versions.

## 4. Probes (B, C)

Sandbox copies against a pristine reference; pre/post hash assertion on every mutation.

**P-1 -- benign control.** Unmodified: build rc=0, 169 PASS, 0 FAIL; pytest rc=0, 186 passed.

**P-2 -- discrimination control.** Pre `8f116c2bb4ab82db` post `d9b825c6a2d0f7a8`, LANDED. FB-4 `test_xz_protocol_source_frame.py` digest to 64 zeros. Build rc=1:
```
FAIL: FB-4 row contains test_xz_protocol_source_frame.py digest (b556aaa38bc93cc7...)
FAIL: FB-4 digest for test_xz_protocol_source_frame.py in body
FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)
FAIL: PACKET_SHA256SUMS digest matches: xz_protocol_v0_24.md
```

**P-3 -- forgery regression.** Pre `8f116c2bb4ab82db` post `675afe48efe18ce5`, LANDED. Carried entry v0.10 mutated in place; all 24 seals, FULL_SECTION_27 and the manifest regenerated; PRIOR_HISTORY left honest. Build rc=1 with exactly one error: `FAIL: PRIOR_HISTORY matches derivation (cbacd073d7cdcb11...)`. The recursive detector survives its third version.

**P-4 -- novel class: the `[9f]` silent skip relocated.** Pre `8f116c2bb4ab82db` post `9e0432e569389e7e`, LANDED. Changed the register's item numbering from `(1)` to `[1]` throughout the v0.24 entry, resealed, nothing else touched. Build **rc=0, GREEN**:
```
[9f] Register self-consistency
  (no register items found in current entry)
```
Zero `check()` calls. The v0.23 fix removed the prose anchor -- correctly, and it was my finding -- but the register-item regex is now the single point of failure and its miss is still silent. The class survived the fix; only its locus moved. → F-OP24S-03.

**P-5 -- novel class: the tautological assertion.** Pre `8f116c2bb4ab82db` post `cc6b219dcfcac8ee`, LANDED. Relabelled item (11) to reuse `F-GPT23-01`, which item (2) carries at HIGH. Build rc=1:
```
FAIL: Finding F-GPT23-01 dispositioned at HIGH and LOW
PASS: No duplicate-severity finding IDs (20 unique)
```
Two contradictory lines in one section. The trailing `check(True, ...)` emits a PASS asserting the exact property the line above it has just falsified. The build goes red correctly, so this is not a correctness hole -- it is a build log that states both a proposition and its negation, in a program whose subject is structural honesty. → F-OP24S-05.

**P-6 -- `[9c]` arity, third round.** Pre `8f116c2bb4ab82db` post `bc938c8788d18efe`, LANDED. Replaced the v0.24 entry's `[COMPUTED: sha256sum | sha256sum]` with `[COMPUTED: sha256sum of build.py and GHOST_DOES_NOT_EXIST.md]` and resealed. Build **rc=0, GREEN**, one line: `PASS: COMPUTED-tagged file ships in packet: build.py`. The second filename is never examined. Open since v0.21, now correctly recorded DISCLOSED NOT CLOSED. → F-OP24S-07.

**Void probes.** One. My first P-6 run replaced the target string document-wide rather than within the v0.24 entry, landing in a carried historical entry; the derivation caught it and the run tested nothing I intended. Discarded and re-run correctly above. Separately, my own harness initially reported a false FAIL on the v0.20 chain link by looking for a prose PRIOR_HISTORY value in the v0.21 entry, which -- as F-OP21S-01 established -- does not have one. Corrected to a SKIP with the reason stated; the shipped harness carries the fix.

## 5. Findings

**F-OP24S-01** [HIGH -- advisory, cannot carry] -- the FB-7b advance is asserted on one conjunct of a four-conjunct definition, and every document evidencing it ships nowhere.
- **Locus:** Section 27, v0.24 entry, opening paragraph; Section 0.1 and the Section 25 FB-7b row.
- **Substance:** The entry states that two non-producer seats of different vendor families "returned non-HALT on canonical bytes where sha256sum -c returned rc=0. **This is the convergent two-family non-HALT that FB-7b requires**" `[ASSERTED]`. The Section 25 definition of FB-7b requires more: "Two executing non-producer seats of different vendor families, **each recomputing identity values, running all 186 tests, and attacking the commitment and decision paths**." The entry evidences the vendor-family and verdict conjuncts. It makes no per-seat claim that identity values were recomputed, that all 186 tests were run, or that the commitment and decision paths were attacked. The three seat reports -- GPT-5.6 Sol, GLM-5.2, Kimi K3 -- do not ship in this packet, so none of the three conjuncts is checkable against any shipped byte, and neither are the verdicts or the finding ranges. Compounding it: both seats returned **CONDITIONAL PASS**, and this record's own vocabulary reads "CONDITIONAL PASS (non-HALT, **not carry-clean**)". The entry maps two not-carry-clean verdicts onto a requirement whose name is "executing carry."
- **Mitigations, stated plainly because they matter here.** The entry does not declare FB-7b CLOSED. Its closing line correctly reads "pending re-carry on v0.24 bytes with absorbed findings," and both Section 0.1 and the Section 25 row still say OPEN. The document is not self-contradictory; the defect is that the middle sentence asserts satisfaction of a four-part definition on the strength of one part, and it is the sentence most likely to be quoted out of the paragraph.
- **Disposition:** Ship the three seat reports in the carry packet, or ship their digests and deposit them. Restate the sentence to name which conjuncts are evidenced and which are not. Decide explicitly, in the body rather than an entry, whether CONDITIONAL PASS satisfies "executing carry" -- the record currently says no in one place and yes in another.
- **Cross-reference:** Section 25 FB-7b row; Section 0.1; F-OP20F-04 (COMPUTED on non-shipping reports); D-3.2; item (13).

**F-OP24S-02** [HIGH -- advisory, cannot carry] -- item (10) is a false CLOSED; the build prints two stale check messages on every run.
- **Locus:** `build.py` `[9]`, both `check()` calls; Section 27, v0.24 entry, item (10).
- **Substance:** Item (10) reads "F-GLM23-05 / F-K3C2-04 LOW CLOSED: build.py carried stale v0.22 docstring and check messages. **Re-stamped to v0.24** `[COMPUTED: build.py version stamps]`." The docstring was re-stamped. The check messages were not:
```
PASS: Entries: 24 (expected 22)
PASS: Protocol says 'twenty-two'
```
Both conditions are correct -- `entry_count == 24` and `"twenty-four amendment entries" in protocol` -- and both message strings are stale. The build therefore emits two green lines each of which states the opposite of what it just verified, in the build's own stdout, on every execution including the one this entry was written against. The `[COMPUTED]` tag names "build.py version stamps," which is `[2]`, and `[2]` checks version strings inside files; nothing in the build examines message-string freshness, so the tag points at a gate that cannot see the defect it certifies as fixed. This is the same shape as the v0.22 `[9f]` tag, and it is the third round in which a COMPUTED tag has been attached to a control that does not cover the claim.
- **Disposition:** Derive both messages from `VERSION` rather than literals -- `f"Entries: {entry_count} (expected {expected})"` -- so they cannot go stale. Reopen item (10) as CLOSED IN PART. Then generalize: any `check()` message containing a version-like literal that disagrees with `VERSION` should itself fail the build.
- **Cross-reference:** F-GLM23-05; F-K3C2-04; F-OP22S-01; F-OP20F-04.

**F-OP24S-03** [MEDIUM -- advisory, cannot carry] -- `[9f]`'s silent skip was relocated, not removed.
- **Locus:** `build.py` `[9f]`, `if id_sev_pairs:` with a print-only `else`.
- **Substance:** The v0.23 fix for my F-OP22S-01 removed the `"Adjudicated ledger:"` prose anchor entirely, which was the right structural move and it worked -- the gate ran this round and reported 13 items. But the register-item regex is now the sole trigger, and when it misses, the else-branch prints `(no register items found in current entry)` and appends no error. P-4 shows a change of item numbering from `(1)` to `[1]` empties the gate at **rc=0 green**. The gate's correctness is therefore coupled to the entry's typographic convention, which no gate enforces and no document specifies. Two rounds ago the coupling was to a phrase; now it is to a numbering style. That is a narrower attack surface, and it is still a surface.
- **Disposition:** `check(bool(id_sev_pairs), ...)` so an empty register fails rather than prints. Better, specify the register's delimiter form in Section 22 and assert it, so the convention the gate depends on is itself normative.
- **Cross-reference:** F-OP22S-01; F-OP22S-03; F-ADJ19-05; F-OP20F-08.

**F-OP24S-04** [MEDIUM -- advisory, cannot carry] -- item (4) is CLOSED on coverage figures the entry does not contain, and a three-round standing disclosure was dropped in the round where it reached its highest value.
- **Locus:** Section 27, v0.24 entry, item (4); the absent trend item.
- **Substance:** Item (4) reads "MEDIUM CLOSED: v0.23 entry item (12) stated the v0.22 round's coverage figures rather than v0.23's. **This entry's figures are derived from build.py [11] output on v0.24 bytes**." The v0.24 entry contains **zero percentage figures** -- I parsed it; there are none. A CLOSED whose evidence is a property of a figure set that does not exist is not closed; the misstatement was resolved by deleting the statement. Separately, the v0.21, v0.22 and v0.23 entries each carried an INFORMATIONAL item disclosing the ungated share and the ASSERTED-fraction trend. The v0.24 entry carries no such item. `[11]` computes the ungated share at **42.6%**, up from 39.2%, a sixth consecutive rise and the largest value in the series. The one round in which the disclosure would have shown the highest number is the round in which the disclosure disappeared. I do not read this as concealment -- the number is printed by the shipped build and the entry made real provenance gains elsewhere -- but a disclosure that lapses exactly when it worsens is the pattern this program exists to catch, and it should not be left to a reader to notice by diffing four entries.
- **Disposition:** Restore the trend item with this round's figures. Then close the class properly: have `[11]` emit its percentages and gate the entry's stated figures against them, exactly as `[3]` gates digests. These numbers are as machine-derivable as digests and there is no reason for them to be ASSERTED, or absent.
- **Cross-reference:** F-OP21S-04; F-OP22S-04; F-OP21C-04; F-GPT23-04; F-OP18-12.

**F-OP24S-05** [MEDIUM -- advisory, cannot carry] -- `[9f]` ends with an assertion that cannot fail and whose message contradicts the failure above it.
- **Locus:** `build.py` `[9f]`, `check(True, f"No duplicate-severity finding IDs ({len(seen_ids)} unique)")`.
- **Substance:** The argument is the literal `True`. The call cannot fail under any input, and its message asserts a property -- that no finding ID is dispositioned at two severities -- which it never tests; the actual test is the `check(False, ...)` inside the loop. P-5 shows the consequence directly: with a duplicate injected the section emits `FAIL: Finding F-GPT23-01 dispositioned at HIGH and LOW` immediately followed by `PASS: No duplicate-severity finding IDs (20 unique)`. It also counts toward the build's 169 PASS total, so the headline number now includes one assertion that asserts nothing. The intent is legible -- it is a liveness indicator, added because the gate had been silently empty for three rounds -- and the intent is right. The implementation states a false thing to signal a true one.
- **Disposition:** Replace with a bare `print()` for liveness, or with `check(not duplicates_found, ...)` tracked by a real flag. A build whose subject is structural honesty should contain no `check(True)`.
- **Cross-reference:** F-OP22S-01; the decorative-control class in F-ADJ19-11 and F-OP20F-01.

**F-OP24S-06** [LOW -- advisory, cannot carry] -- correction (f) miscounts its own defect class by folding in a correction that belongs to a different one.
- **Locus:** Section 27, v0.24 entry, correction (f); v0.23 correction (d).
- **Substance:** Correction (f) states "This is the fourth consecutive round of the duplicate-disposition class (corrections (b), (c), (d), now (f))." Correction (b), at v0.21, is a ledger-tally-versus-register-count mismatch -- eleven tallied against twelve dispositioned -- not a duplicate disposition. The duplicate-disposition instances are (c) at v0.22, (d) at v0.23, and (f) at v0.24: three, not four. The mislabel originates at v0.23 correction (d), which likewise calls (b) "the same duplicate-disposition class," and (f) carries it forward. Both are reconciliation errors of exactly the kind the corrections describe, committed inside the corrections that describe them.
- **Disposition:** Restate as three consecutive rounds, or define the class broadly enough to include tally mismatches and say so. Given `[9f]` now counts register items mechanically, the class census is derivable and should not be prose.
- **Cross-reference:** corrections (b), (c), (d); F-OP22S-02; the Axiom-3 class.

**F-OP24S-07** [LOW -- advisory, cannot carry] -- three findings are now correctly disclosed and none is closed: the `[9c]` arity-one regex (third round), the PDF (fifth round), and the `cb67f222` literal.
- **Locus:** `build.py` `[9c]` `file_computed`; `PACKET_SHA256SUMS`; `build.py` `derive_prior_history`.
- **Substance:** The `[9c]` regex is byte-identical to v0.21 and v0.22, confirmed by direct diff, and P-6 shows a COMPUTED tag naming a non-existent second file builds green. The PDF is absent from the manifest and from `required_members` for the fifth consecutive version and carries 145 en-dashes against a source with none -- the convention breach I confirmed at v0.22 persists in the one artifact the perimeter cannot see. The `cb67f222` literal remains in the derivation's v0.19 termination path. **The disclosure discipline is now working**: v0.23 item (8) records the regex DISCLOSED NOT CLOSED, item (9) NOTES the literal with an accurate rationale, item (11) NOTES the PDF, and v0.24 item (11) even records the PDF disclosure's own discontinuity. I raise this at LOW and as a single item precisely because the record is now honest about all three. The finding is that three known defects have been disclosed rather than fixed across three to five rounds, and disclosure is not a terminal state.
- **Disposition:** Each is a small edit. Capture all filenames per tag; add the PDF to the manifest and extend `[4]` to its extracted text; delete the literal and let a scrape miss fail the build. None needs a carry round to authorize.
- **Cross-reference:** F-OP21S-05; F-OP22S-05; F-OP20F-07; F-OP22S-06; F-OP22S-07; F-K3C2-05.

**F-OP24S-08** [INFORMATIONAL] -- the provenance trend reversed and the coverage trend did not.
- **Locus:** `[9c]` and `[11]` output; the v0.24 entry's tag distribution.
- **Substance:** ASSERTED fell 78.9% to 63.2% and COMPUTED rose 4 to 7 -- the first improvement in four rounds, and unlike v0.22 every COMPUTED tag names a gate that actually executed. The silent-skip census fell 19 to 17. Both are real gains and both were driven by non-producer findings. Against that: the ungated share rose to 42.6%, a sixth consecutive rise, and EXTERNAL is 0 for the fifth consecutive entry. Item (13) reports that a non-producer seat verified a deposit against the live Zenodo API and calls it the first EXTERNAL verification in the record; it is tagged `[ASSERTED]`, the seat's report does not ship, and I could not reach the cited record from this seat to corroborate it. So the program's first external verification is currently recorded the same way as everything else. Converting it -- shipping the seat's report or the deposit receipt and citing it `[EXTERNAL]` -- would move the count off zero for the first time in twenty-four versions and is the only remaining step for the boundary.
- **Cross-reference:** F-OP22S-08; F-OP21S-08; item (13); Section 22.2 anchor (b).

**Clears.** Step 1 rc=0; build green; 186/186. The recursive PRIOR_HISTORY derivation reproduces the shipped value, survives a third version, and still catches a retroactive carried-entry forgery with exactly one correct error (P-3). `[9f]` executed real assertions this round, which it had not done in three. Range-versus-register reconciles exactly: 21 declared IDs across three namespaces, 21 dispositioned, zero absent -- the D-3.7 defect I raised at v0.22 is genuinely gone. All eight of my v0.22 findings were dispositioned at v0.23. Correction (f) correctly identifies correction (d) as a false CLOSED and restates the mapping exactly as my v0.22 report recommended. `[9d]` now matches numeric ordinals and `[9e]` tolerates trailing content in the range parenthetical, both from non-producer findings. Section 22.2's forgery boundary was re-scoped again, correctly, in the direction of admitting more residual. Em-dash and brand sweeps clean at source.

## 6. Self-score of prior findings (D)

My v0.22 findings were dispositioned in the v0.23 entry, which I do not hold as a packet but can read in Section 27.

| ID | v0.22 severity | v0.23 disposition | Landed? |
|---|---|---|---|
| F-OP22S-01 | HIGH | item (1) HIGH CLOSED | **Structurally yes.** Prose anchor removed entirely; gate ran this round. Skip relocated -- F-OP24S-03 |
| F-OP22S-02 | HIGH | item (2) HIGH CLOSED via correction (d) | **No at v0.23** -- (d) restated the duplicate. Caught by F-GPT23-03 and fixed at v0.24 correction (f), which now matches my original recommendation exactly |
| F-OP22S-03 | HIGH | item (3) HIGH CLOSED via correction (e) | **Yes.** All three absent IDs dispositioned; F-OP21S-05 correctly graded DISCLOSED NOT CLOSED. No gate added -- item (10) declares it a D-3.7 responsibility, which I accept |
| F-OP22S-04 | MEDIUM | item (5) MEDIUM NOTED | **No.** Resolved at v0.24 by deleting the figures -- F-OP24S-04 |
| F-OP22S-05 | MEDIUM | item (8) MEDIUM NOTED | Disclosed, not fixed. Regex byte-identical, third round -- F-OP24S-07 |
| F-OP22S-06 | LOW | item (9) LOW NOTED | Disclosed with an accurate rationale I accept: the literal is a search pattern, not a comparand |
| F-OP22S-07 | LOW | item (11) LOW NOTED | Disclosed. Fifth round unbound -- F-OP24S-07 |
| F-OP22S-08 | INFORMATIONAL | item (12) INFORMATIONAL NOTED | Disclosed at v0.23; **dropped at v0.24** -- F-OP24S-04 |

Eight raised, eight dispositioned, none absent -- the first round in which that is true of my findings. Two landed, one landed after a failed first attempt, five disclosed rather than fixed.

**What three prior rounds bought.** The external chain anchors in §7, which no other seat can produce. B3's refutation: I predicted the entry would misstate the coverage figures and instead it omitted them, which I could only notice because I had the three prior entries to compare against. F-OP24S-06, which required tracing correction (b) back to the v0.21 entry to see it belonged to a different class. And the P-3 baseline. It bought **nothing** for F-OP24S-01, -02, -03, or -05 -- all four come from reading the shipped `build.py` and the shipped body against the shipped entry, and a fresh seat finds every one. F-OP24S-01 in particular needs only the Section 25 definition and the file listing.

## 7. Boundary report (E)

The boundary moved this round, for the first time since v0.21, and it moved in the one direction that counts: outward, past the packet. Three of the four chain links are now anchored against bytes I hold from prior dispatches -- the v0.22 entry's recorded PRIOR_HISTORY equals the sha256 of my held v0.21 `HISTORY.sha256`, and the v0.23 entry's equals the sha256 of my held v0.22 file -- and all 22 carried entry seals are byte-identical across v0.20, v0.21, v0.22 and v0.24. Append-only has now held across five packets with zero in-place mutation, and the v0.23 link is bridged by prose even though I never received that packet. The fourth link, v0.24 to v0.23, is derivation-only because I do not hold v0.23. More important than my anchors: item (13) records that a non-producer seat checked a deposit against the live Zenodo API, which is the first time in twenty-four versions that anything in this program has been compared against a record outside the producer's control. That is the crossing the last four of my reports have asked for. But it is currently recorded as `[ASSERTED]`, the seat's report does not ship, EXTERNAL remains 0, and I could not reach the cited record from this seat to corroborate it -- so the first external verification has the same evidentiary status inside the packet as the claims it was supposed to anchor. Meanwhile the interior kept thinning: the ungated share reached 42.6%, a sixth consecutive rise, and the entry that would have disclosed it does not. The step is now one line rather than a program: ship the Kimi K3 report or the deposit receipt, cite it `[EXTERNAL]`, and the count moves off zero. Everything else in this boundary paragraph has been true for four rounds.

## 8. D-7 process health (G)

- **Did every probe come from an enumerated list?** No. P-4, P-5 and the FB-7b conjunct audit are novel; none appears in D-4's classes. P-4 and P-5 came from reading the `[9f]` rewrite and asking what it does when its inputs change shape.
- **Did the dispatch tell me where to look?** Less than in any prior round -- this dispatch is four lines of deliverables with no per-finding direction, which is an improvement. But the packet still ships all three of my prior reports, and deliverable D still structures §6. Four of my eight findings came from bytes rather than memory.
- **Is the ASSERTED fraction unchanged from the prior round?** No, and for the first time the answer is favourable: 78.9% to 63.2%, with COMPUTED rising 4 to 7 and every COMPUTED tag naming a gate that executed. This is the first improvement in four rounds and it followed the first non-producer carrying round in ten versions. That correlation is the most useful process signal in this report.
- **Have the recent rounds all been producer-family?** No -- v0.23 was carried by GPT-5.6 Sol, GLM-5.2 and Kimi K3, the first non-producer contact since v0.14. This round is producer-family advisory again. FB-7b is claimed advanced on v0.23 bytes and remains OPEN in the body pending re-carry on v0.24 bytes.

## 9. Verdict

**CONDITIONAL PASS -- advisory only, non-binding.** Not a HALT.

Severity ledger as I calibrate it: 0 CRITICAL / 2 HIGH / 3 MEDIUM / 2 LOW / 1 INFORMATIONAL = 8.

I have returned HALT advisory in each of my three prior reports. I am not returning one here, and the reason is substantive rather than fatigue. At v0.21 and v0.22 the HALT rested on a defect that would be sealed into an append-only record in a state that could not be repaired cheaply afterward. Nothing in this round has that property: every finding below is a small edit against the current draft, the register reconciles exactly for the first time, the provenance trend reversed, and the chain is now anchored outside the packet at three links. The document is in better condition than at any point I have audited it.

**Standing, restated.** Producer-family advisory. Cannot HALT, cannot carry HIGH, no FB-7b weight. This matters more than usual: F-OP24S-01 concerns whether FB-7b's condition has been met, and my verdict on that question carries no weight by construction. I raise it, I do not adjudicate it.

Three findings I would most want a non-producer seat to re-derive, since a producer-family instance auditing a producer-family entry about a non-producer round is the weakest configuration in this program: **F-OP24S-01**, which needs only the Section 25 FB-7b definition, the entry's opening paragraph, and `ls`; **F-OP24S-02**, which is two lines of the build's own stdout; and **F-OP24S-04**, which is a grep of the entry for a percent sign against `[11]`'s output. None requires taking my word for anything, and the first should be re-rated by someone whose severity can carry.

The recommendation is unchanged from three reports running and is now one step from done: ship the Kimi K3 deposit verification or the receipt itself, cite it `[EXTERNAL]`, and re-carry on v0.24 bytes with the seat reports included in the packet. FB-7b should be settled by documents a reader can open, not by a sentence about them.

---

*Claude Opus 5, Seat B_SHALLOW, producer-family advisory. Prepared for Bilal Syed Arfeen. All probes reproducible from the shipped packet; one void probe and one harness defect reported as such.*

---

# Bismillah ir-Rahman ir-Rahim
