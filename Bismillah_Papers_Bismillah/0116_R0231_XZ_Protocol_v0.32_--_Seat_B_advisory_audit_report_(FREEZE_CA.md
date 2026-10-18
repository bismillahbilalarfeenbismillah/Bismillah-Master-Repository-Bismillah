# Bismillah ir-Rahman ir-Rahim

# R0231 -- XZ Protocol v0.32 -- Seat B advisory audit report (FREEZE CANDIDATE)

**Chronological Index:** 116 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v32_SEAT_B_FREEZE_AUDIT.md  
**Source Format:** md  
**SHA-256:** `6bd44df205ad2ba77d1be11d802cdfc51888176ef463963991ce03fae52d372d`  

---

## R0231 · XZ Protocol v0.32 -- Seat B advisory audit report (FREEZE CANDIDATE)

- section: IV. XZ Protocol
- source_file: XZ_v32_SEAT_B_FREEZE_AUDIT.md
- source_format: md
- text_sha256: 6bd44df205ad2ba77d1be11d802cdfc51888176ef463963991ce03fae52d372d

# XZ Protocol v0.32 -- Seat B advisory audit report (FREEZE CANDIDATE)

**Seat:** Claude Opus 5, Seat B (continuous), producer-family advisory
**Namespace:** F-OP32S
**Mode:** A (substrate verifier -- full packet on disk, build and pytest executable, mutation sandbox, plus the v0.20, v0.21, v0.22, v0.24, v0.25, v0.27 and v0.28 packets retained)

## 0. State declaration (S-0)

**Standing.** Producer-family advisory. My verdict is **advisory only**: no carry vote, no FB-7b weight, and a HALT from this seat **does not bind** the freeze. It is recorded and forwarded. Where a non-producer seat's severity differs from mine, theirs governs. That standing is load-bearing this round, because the question under audit is whether FB-7b is satisfied, and I am constitutionally disqualified from answering it. Everything below is evidence for a seat whose severity can carry.

**Continuity.** I produced the v0.20 fresh report and the v0.21, v0.22, v0.24, v0.25, v0.27 and v0.28 reports, and I hold seven prior packets. **I do not hold v0.23, v0.26, v0.29, v0.30 or v0.31.** I did not author the discipline blocks, the Class A/B/C/D rubric, or any of the F-GLM, F-K3, F-GPT, F-v30, F-v31 or NC namespaces. No seat report from any round ships in this packet, so the entire evidentiary base of the round under audit is invisible to me and to every other reader.

## 1. S-1 preregistration

Frozen at `PREREG_OPUS5_B_v32.txt`, sha256 `b0d9e29fb4eef05e2a26ff0fd36f735a144cc59ddc2fb9cd027f37f9056e7fce`, 2026-08-02T20:28:51Z, before any read of Section 27.

**Contamination, larger than usual.** Eighth consecutive round with `build.py` ordered before preregistration, and this round the cover note additionally states the conclusions in advance: FROZEN, FB-7b amended, EXTERNAL above zero, eight seats, thirteen-item register, corrections (q)(r)(s). Preregistration against a brief that names the answers is weak by construction, and I marked it so at freeze.

| # | Prediction | Result |
|---|---|---|
| B1 | **Sharpest.** `[9c]`'s EXTERNAL check matches only file-form references, so a DOI triggers nothing; the count rises with no gate behind it | **Correct**, and worse -- one tag is producer-held. F-OP32S-03 |
| B2 | COMPUTED 0 and ASSERTED 90.9%, both unstated per policy | **Correct.** The freeze entry never records that it is the least machine-backed entry in the series |
| B3 | Ungated share 53.3%, crossed 50%, disclosed as a boundary without the threshold being named | **Correct** |
| B4 | F-OP28S-02 unfixed, third round | **Correct**, and undispositioned |
| B5 | `[9f]`'s `reg_section` scoping leaves corrections (q)(r)(s) ungated | **Correct** -- F-OP32S-05 |
| B6 | `[9e]` inert, fourth round | Correct |
| B7 | `[9c]` arity-one eighth round; `cb67f222` present | Correct |
| B8 | The amendment changes the verdict predicate and leaves the execution conjuncts unevidenced | **Correct and understated.** It did not leave them unevidenced; it deleted one from the rule -- F-OP32S-02 |
| B9 | No seat report ships; all eight verdicts and the Class assignment are ASSERTED | Correct |
| B10 | Entry records both adversarial HALTs and dispositions their findings | Correct |
| B11 | v0.29 entry records PRIOR_HISTORY equal to sha256 of my held v0.28 file | **Correct**, exact match across a three-version gap -- §5 |
| B12 | At least one new counting or reconciliation error (the one I wanted to be wrong about) | **Correct** -- F-OP32S-01 |

Twelve for twelve, which measures the brief's specificity more than my judgement. B8 is the only one where the bytes were worse than I predicted.

## 2. Byte verification and provenance ledger

| Step | Result |
|---|---|
| 1. `sha256sum -c PACKET_SHA256SUMS` | **rc=0.** 16 members, all OK. |
| 2. `python3 build.py` | **rc=0**, `BUILD PASSED: all checks GREEN`, **172 PASS**, 0 FAIL. |
| 3. six-suite canonical pytest | **rc=0**, `186 passed`. AST 186, collected 186. |
| 4. Independent digest of all 16 members | All match. Manifest digest recomputes to `a9b6524b8aed74c14df795201d76c28469a14d7f59bb3ffdaf5dabbb7d5c3efe`, matching trust roots and body. 28 entry seals + FULL_SECTION_27 verify. |
| Unsealed members | 4: the manifest, D0-D7, standing orders, the cover note. **No seat report of any kind.** |
| Coverage `[11]` | body 99162 (46.7%), **Section 27 ungated 113216 (53.3%)**, semantic-gate coverage 25.7%. |

**Provenance ledger over the v0.32 entry: COMPUTED 0, EXTERNAL 2, ASSERTED 20. ASSERTED fraction 20/22 = 90.9%.**

Nine-round series I have measured from shipped bytes: v0.19 37.5% (COMPUTED 9), v0.20 50.0% (11), v0.21 57.1% (9), v0.22 78.9% (4), v0.24 63.2% (7), v0.25 75.0% (4), v0.27 78.6% (3), v0.28 80.0% (3), v0.32 **90.9% (COMPUTED 0)**.

**The freeze candidate is the first entry in the record with zero computed claims and the highest ASSERTED fraction in the series.** Part of that is principled -- since v0.28 the entry deliberately grades its own entry-copy values ASSERTED, which is honest. But the consequence at a freeze is not cosmetic: the entry that changes the document's terminal status contains no claim any gate verifies, and its two EXTERNAL tags are not verified either (F-OP32S-03). Per the no-percentages policy adopted at v0.25 the entry states neither figure, so the sealed record will not contain the fact that the freeze rests on twenty asserted claims and zero computed ones.

Two structural observations bear on the ungated figure. Section 27 is now **larger than the gated body** for the first time -- 53.3% against 46.7%. The entry lists "Section 27 ungated share" among its disclosed boundaries without stating that it crossed the majority threshold at the freeze. And the coverage the gates provide is 25.7% of the body, which is 12.0% of the document being frozen.

## 3. Probes

Sandbox copies against a pristine reference; pre/post hash assertion on every mutation. All probes reseal `HISTORY.sha256` and `PACKET_SHA256SUMS` so that only the behaviour under test differs.

**P-1 -- benign control.** Unmodified: build rc=0, 172 PASS, 0 FAIL; pytest rc=0, 186 passed.

**P-2 -- discrimination control.** Pre `491444c2ea33dce6` post `4d113ab8f89491b9`, LANDED. FB-4 `test_xz_protocol_source_frame.py` digest to 64 zeros. Build rc=1, four independent failures. The digest plane is live.

**P-3 -- forgery regression.** Pre `491444c2ea33dce6` post `4699f7e15897f46d`, LANDED. Carried entry v0.10 mutated in place; all 32 seals, FULL_SECTION_27 and the manifest regenerated; PRIOR_HISTORY left honest. Build rc=1 with exactly one error: `FAIL: PRIOR_HISTORY matches derivation (8dd177a83eb735d7...)`. Seventh version, still fires.

**P-4 -- novel class: is the EXTERNAL grade gated? Run as a discrimination pair.**

*P-4a, control.* Pre `491444c2ea33dce6` post `ca21b073cf74fd6e`, LANDED. Inserted a **file-form** reference into an existing EXTERNAL tag: `[EXTERNAL: GHOST_SEAT_REPORT.md Zenodo deposits, ...]`. Build **rc=1**: `FAIL: EXTERNAL-tagged file ships: GHOST_SEAT_REPORT.md`. The gate exists and works on that form.

*P-4b, the finding.* Pre `491444c2ea33dce6` post `2cc62588da2bc9de`, LANDED. Inserted an entirely fabricated claim with a fabricated anchor: "Independently verified against an external registry `[EXTERNAL: doi:10.5281/zenodo.00000000-nonexistent, resolves to bytes the producer does not control]`." Build **rc=0, GREEN**, and `[9c]` reports `COMPUTED: 0, EXTERNAL: 3, ASSERTED: 20`. A nonexistent DOI raises the EXTERNAL count and passes every check. → F-OP32S-03.

**P-5 -- novel class: does `[9f]` see the corrections block? Run as a discrimination pair.**

*P-5a, control.* Pre `491444c2ea33dce6` post `b3eb88a816a3fe1c`, LANDED. Relabelled register item (7) to reuse `F-GPT31-01`, which item (5) carries at HIGH. Build **rc=1**: `FAIL: Finding F-GPT31-01 dispositioned at HIGH and MEDIUM`.

*P-5b, the finding.* Pre `491444c2ea33dce6` post `e2070a3fb54e4c3d`, LANDED. Placed a full register row -- `(14) F-GPT31-01 LOW CLOSED: adversarial finding downgraded and closed here, outside the register section.` -- immediately after the corrections heading. Build **rc=0, GREEN**:
```
PASS: Register parsed == declared (13 parsed, 13 declared)
PASS: No duplicate-severity finding IDs (16 unique)
```
An adversarial HIGH silently re-dispositioned to LOW CLOSED, invisible to the gate, with both `[9f]` assertions passing. → F-OP32S-05.

**P-6 -- the duplicate-free PASS, third round.** Pre `491444c2ea33dce6` post `d72bfdf346fbbddf`, LANDED. Duplicate injected inside the register. Build rc=1:
```
FAIL: Finding F-GPT31-01 dispositioned at HIGH and MEDIUM
PASS: No duplicate-severity finding IDs (15 unique)
```
→ F-OP32S-06.

**Void probes.** None.

## 4. Findings

**F-OP32S-01** [CRITICAL -- advisory, cannot carry] -- Section 0.1 declares the document FROZEN and, 923 characters later in the same section, declares FB-7b OPEN.
- **Locus:** `### 0.1 Status`, offsets 208 and 1131; Section 25 FB-7b row; v0.32 entry.
- **Substance:** The status line reads "This document is **v0.32 FROZEN** -- carried on these bytes, pending deposit." Within the same subsection: "**FB-7b** (two-family executing carry on canonical bytes) **is OPEN**, pending fresh carry by Kimi K3 and GLM-5.2." Section 25 records FB-7b as RESOLVED and strikes the row through; the v0.32 entry states "FB-7b RESOLVED"; the freeze is licensed by that resolution. So the freeze candidate asserts both branches of its own decision path, in one subsection, and one of the two must be false. Under the severity vocabulary this is CRITICAL -- "identity value or decision path is false" -- and it is the only CRITICAL I have raised in nine rounds of auditing this instrument. The mechanism is mundane: the Section 0.1 FB-7b sentence has carried forward unedited since at least v0.28, where I verified it read "pending fresh carry by Kimi K3 and GLM-5.2." The amendment updated Section 25 and the entry and did not update Section 0.1. **My severity cannot carry. A non-producer seat must re-rate this, and it is the single item I would put in front of one first.**
- **Disposition:** Update the Section 0.1 sentence, or -- if FB-7b is in fact open pending deposit, which the status line's own "pending deposit" qualifier suggests -- withdraw FROZEN. Then gate it: assert that no body sentence containing "FB-7b" contains "is OPEN" while Section 25 records RESOLVED. That check is three lines and the class it covers (body prose left behind by an amendment) is the Kimi F-1 class the record has now committed at v0.27, v0.28 and here.
- **Cross-reference:** Section 25 FB-7b row; v0.32 entry; F-OP24S-01; Kimi F-1; F-OP25-ALL-06.

**F-OP32S-02** [HIGH -- advisory, cannot carry] -- the FB-7b amendment deleted an execution conjunct from the operative rule, and the entry describes it as a verdict-predicate change.
- **Locus:** Section 25 FB-7b row; v0.32 entry, opening paragraph; v0.28 Section 25 (held).
- **Substance:** The v0.28 packet on my disk defines FB-7b as: "Two executing non-producer seats of different vendor families, **each recomputing identity values, running all 186 tests, and attacking the commitment and decision paths**." In v0.32 that definition column is struck through and replaced with the amendment text. **The phrase "running all 186 tests" now occurs exactly once in the entire document, at offset 172112 -- inside Section 27, in the sealed v0.25 status note, quoting a prior seat's objection that the entry evidenced only the verdict conjunct.** The operative rule no longer contains it; it survives only as a quotation inside the complaint about its non-satisfaction. The entry frames the amendment narrowly -- "CONDITIONAL PASS with Class C/D conditions satisfies the two-family carry when no Class A/B finding exists" -- which is a change to the verdict predicate, and says nothing about the execution conjuncts being removed with it. A reader of v0.32 alone cannot detect the deletion; it requires diffing against a prior packet or reading a sealed objection.
- **What makes this more than bookkeeping.** Register item (5) reads: "**F-GPT31-01 HIGH NOTED: pytest absent from dispatched environment; first build returns rc=1.** Live instance of the disclosed execution-environment boundary. **Confirmed by three fresh seats this round.**" I hit this myself at v0.20 -- my first build returned rc=1 for exactly this reason. So the conjunct that was deleted from the rule is precisely the one the round's own register records at least three seats could not satisfy without out-of-band remediation, and whether any of them installed pytest and re-ran is nowhere recorded. The entry's compressed claim that six carrying seats were "all executing" is contradicted in substance by its own item (5), and the definition that would have made "executing" checkable is gone.
- **Disposition:** State the amendment's full scope in the entry: which conjuncts were relaxed, which were removed, and why. If the execution conjuncts are still intended to hold, restore them to Section 25 alongside the amended verdict predicate -- the two changes are independent. If they are not, say so plainly, because deleting them changes what FB-7b means rather than when it is satisfied. Separately, require each carrying seat to record its pytest exit code and test count in its report, and ship the reports.
- **Cross-reference:** v0.28 Section 25 (held); v0.25 status note; F-OP24S-01; register item (5); F-GPT31-01; F-GPT30-01/02.

**F-OP32S-03** [HIGH -- advisory, cannot carry] -- the EXTERNAL count was raised by two tags, neither examined by any gate, one of which its own text disqualifies.
- **Locus:** v0.32 entry, both EXTERNAL tags; `build.py` `[9c]`, `external_refs`.
- **Substance:** Three distinct defects in one claim.
  - **The gate cannot see either tag.** `[9c]` verifies EXTERNAL references with `re.findall(r'\[EXTERNAL:\s*(\S+\.(?:md|py|json|pdf|txt))', ...)` -- file-form only. Both shipped tags are prose. `external_refs` is empty; the loop body never runs; **zero checks execute against the EXTERNAL population**. P-4 is the discrimination pair: a file-form EXTERNAL naming a non-shipping file fails the build; a fabricated `doi:10.5281/zenodo.00000000-nonexistent` builds green and raises the count to 3. The metric the entry presents as a first is incrementable by typing.
  - **One tag is EXTERNAL by contradiction of its own text.** `[EXTERNAL: seat reports held by producer, digests below]` is attached to the sentence carrying the entire carry claim -- "Six non-producer carrying seats across two families, all executing, all non-HALT, on v0.31 canonical bytes." A producer-held document that does not ship is the paradigm ASSERTED claim; the tag says "held by producer" in the same breath as grading it EXTERNAL. The eight digests listed below it are tagged, correctly, `[ASSERTED: digests computed by producer from held report files]` -- so the entry grades the digests ASSERTED and the reports they digest EXTERNAL.
  - **The DOI tag anchors nothing in v0.32.** The two deposits are real and Zenodo bytes are genuinely outside the producer's reach once deposited -- that part of the claim is sound and I credit it. But they are deposits of *other artifacts* (BSSG v0.1, SHVVP v0.8), and the entry's own wording is that "the protocol body already inherits from these DOIs." Inheritance is not anchoring. No v0.32 value -- not `HISTORY.sha256`, not the manifest digest, not a seat report digest -- appears in either deposit by any claim the entry makes. The thing seven of my reports have asked for is a deposit receipt for **this packet's** chain root. That has not happened, and the EXTERNAL count moved without it.
  - **It is load-bearing.** Register item (9) dispositions adversarial HIGH `F-GPT31-06` -- "current-entry factual semantics remain self-attested after packet-internal seal regeneration" -- as "subsumed by ... **the EXTERNAL-count precondition now addressed in this entry**." A HIGH from an adversarial seat is NOTED on a precondition that consists of two ungated tags, one of them misgraded.
- **Disposition:** Regrade the seat-reports tag ASSERTED. Extend `[9c]`'s EXTERNAL check to DOI form: resolve the DOI or, at minimum, assert the entry states a digest that the deposit is claimed to contain, and fail when neither. Then do the thing itself -- deposit `HISTORY.sha256` and cite its DOI, which converts the chain root from self-attested to externally fixed and disposes of `F-GPT31-06` on its merits.
- **Cross-reference:** F-GPT31-06; F-K3B-04/05; F-OP24S-01; F-OP25S-08; F-OP27S; F-OP28S-07.

**F-OP32S-04** [HIGH -- advisory, cannot carry] -- the freeze register closes nothing, and two of the disclosed standing boundaries contradict the freeze.
- **Locus:** v0.32 entry, thirteen-item register and closing paragraph.
- **Substance:** Thirteen items: **zero CLOSED**, four DISCLOSED, nine NOTED. Both HIGH items are NOTED. Every finding from an eight-seat round -- six carrying, two adversarial -- is carried forward rather than fixed, in the entry that declares the document terminal. The closing paragraph then lists **thirteen disclosed standing boundaries**, and two of them are load-bearing against the freeze itself: **"packet non-closure"** and **"fresh-execution non-reproducibility."** The first says the packet does not contain the documents needed to verify its own claims. The second says a fresh seat cannot reproduce the build. Freezing an instrument while disclosing that a fresh party cannot reproduce its verification, and that the packet lacks closure, freezes the disclosure set rather than a verified artifact. That may be a defensible terminal form -- the document's stated intent is "a FROZEN **OPEN** preregistration instrument" -- but if so the entry should say that FROZEN means "no further changes," not "verification complete," because those are different claims and only the first is supported.
- **Disposition:** Either close some subset before freezing -- the `[9c]` arity regex, the `cb67f222` literal, and the duplicate-message guard are each a one-line edit and have been carried for six, six and three rounds respectively -- or state explicitly in Section 0.1 what FROZEN asserts and what it does not. A freeze with zero closures needs its semantics written down.
- **Cross-reference:** register items (1)-(13); closing paragraph; F-OP28S-06; F-OP27S-07.

**F-OP32S-05** [MEDIUM -- advisory, cannot carry] -- `[9f]`'s scoping leaves the append-only corrections block entirely ungated.
- **Locus:** `build.py` `[9f]`, `reg_section` scoping; v0.32 entry, corrections (q), (r), (s).
- **Substance:** `[9f]` scopes both its checks to text after "defect register disposition" (offset 4440). Corrections (q), (r) and (s) sit at 2436, 3370 and 3780 -- outside `declared_count`, outside the parse, and outside the duplicate-severity check. P-5b: a full register row placed in the corrections block re-dispositions an adversarial HIGH to `LOW CLOSED` and the build is green, with `PASS: Register parsed == declared (13 parsed, 13 declared)` and `PASS: No duplicate-severity finding IDs (16 unique)` both passing. The scoping was necessary -- correction (q) contains "(i)" and "(ii)" markers that would inflate `declared_count` -- so this is a cure that created a blind region, and it created it in the part of the entry whose function is to rewrite prior dispositions. That is the highest-leverage text in the document to leave unchecked.
- **Disposition:** Scope `declared_count` by a stricter marker (numeric-only `(\d+)` at line start, or an explicit register delimiter) rather than by section, and run the duplicate-severity check over the whole entry. Corrections should be more gated than the register, not less.
- **Cross-reference:** F-OP28S-01; F-OP27S-02; F-GLM29-01; F-GLM30-05.

**F-OP32S-06** [MEDIUM -- advisory, cannot carry] -- the duplicate-free PASS still prints beneath its own FAIL, third consecutive round, undispositioned.
- **Locus:** `build.py` `[9f]`, `if seen_ids: print(f"  PASS: No duplicate-severity finding IDs ...")`.
- **Substance:** Raised at v0.24 as `check(True, ...)`, fixed at v0.25 by guarding on no-duplicate-found, reverted at v0.27, unfixed at v0.28, byte-identical here. P-6 shows the output: a FAIL naming a duplicate followed immediately by a PASS asserting there is none. `F-OP27S-03` and `F-OP28S-02` do not appear in the v0.32 register at any severity. At a freeze, this is a build log that will be sealed containing a proposition and its negation, in an instrument whose subject is structural honesty.
- **Disposition:** One line: track a boolean in the failing branch and print on its negation.
- **Cross-reference:** F-OP24S-05; F-OP25S-03; F-OP27S-03; F-OP28S-02.

**F-OP32S-07** [LOW -- advisory, cannot carry] -- the long-carried code-local defects are being frozen in place.
- **Locus:** `[9c]` `file_computed` (byte-identical since v0.21, **eighth round**); `derive_prior_history`'s `cb67f222` literal (**sixth round**); `[9e]` inert (**fourth round**, no governance sentence in the freeze entry).
- **Substance:** All three are correctly disclosed -- the first two by name in the closing boundary list. The finding is that each is a small edit and each is about to become permanent. `[9e]` is the sharpest of the three at a freeze: a gate added at v0.22 to catch a governance miscount has now been silent for four consecutive rounds because no entry contains a governance sentence, and the freeze entry -- which changes the document's status, amends a locker rule, and dispositions an eight-seat round -- contains none either. The one entry in the record that most needed a governance statement has the weakest.
- **Disposition:** Take all three in one commit before the seal. `check()` the presence of a governance sentence; capture every filename in a multi-file COMPUTED tag; delete the `cb67f222` fallback and let a scrape miss fail.
- **Cross-reference:** F-OP21S-05; F-OP22S-06; F-OP25S-06; F-OP27S-06; F-OP28S-05.

**F-OP32S-08** [INFORMATIONAL] -- what the freeze has genuinely earned.
- **Substance:** Four things, stated plainly because a HALT should not obscure them. **The chain is the strongest artifact in this program.** Six links anchor against files I hold, including v0.29's PRIOR_HISTORY matching the sha256 of my held v0.28 `HISTORY.sha256` across a three-version gap I never received; all 28 carried entry seals are byte-identical across seven held packets spanning v0.20 to v0.32; append-only has held across thirteen versions with zero in-place mutation, and P-3 confirms the detector still fires. **The build closed my last outstanding HIGH.** `[9f]` now asserts `declared == parsed` -- the check I asked for at v0.28 and that item (1) then claimed without implementing -- and it passes 13 of 13. `[9d]` is bidirectionalized. The `expected_word` for the entry-count message is now generated from the count, which structurally ends the message/condition drift class I raised at v0.24 and v0.25. **The corrections are the most candid in the record.** (q) admits its own predecessor's "class is now gate-closed" claim was overwide and names both residual evasions; (r) admits a nine-version-old misnomer in the manifest-digest label; (s) admits that a shipped dispatch document states something false about the packet. Each of the three concedes rather than reframes. **And the register is honest about the round's shape:** both adversarial HALTs are recorded, both are attributed to GPT-5.6 Sol by seat, and item (5) records the pytest-absence failure that undercuts the entry's own "all executing" claim. A producer preparing a freeze does not usually put that in the register. It is there.
- **Cross-reference:** F-OP28S-01; F-OP24S-02; F-OP25S-01; corrections (q), (r), (s).

## 5. Boundary report

The boundary did not move, and at a freeze that is the whole question. Internally the instrument is in the best condition I have audited: six externally anchored chain links, thirteen versions of unbroken append-only, a register that parses completely for the first time, and three corrections that concede rather than reframe. None of it reaches outside the packet, and this is the round where that stops being a trend and becomes a terminal property. **EXTERNAL is nominally 2 and effectively 0**: neither tag is examined by any gate, a fabricated DOI raises the count and builds green, one tag grades a producer-held non-shipping document EXTERNAL by its own text, and the two real deposits anchor other artifacts rather than any v0.32 value. No seat report from any of the thirty-two versions has ever shipped, so the eight verdicts, the finding IDs, the Class A/B/C/D assignment that triggers the amendment, and the "all executing" claim are all ASSERTED -- and the entry's own closing list discloses "packet non-closure" and "fresh-execution non-reproducibility" as standing boundaries while the status line declares FROZEN. The record already contains the precedent: Section 0.1 states that **v0.4 claimed FROZEN status and v0.5 reverted it to DRAFT CANDIDATE**. That reversion was for a worse cause -- v0.4 had erased a recorded HALT, and v0.32 records both adversarial HALTs faithfully, which is a real and creditable difference. But it establishes that in this record a FROZEN claim is not self-validating. The step has not changed across eight of my reports and is now one action: deposit this packet's `HISTORY.sha256`, cite the DOI, and ship the eight seat reports under manifest. That converts the chain root from self-attested to externally fixed, disposes of adversarial finding `F-GPT31-06` on its merits rather than by subsumption, and makes the carry claim checkable by a reader instead of by assertion. It is the difference between freezing a verified artifact and freezing a disclosure set.

## 6. D-7 process health

- **Did every probe come from an enumerated list?** No. P-4's DOI-form fabrication and P-5's corrections-block row are novel and appear in no D-4 class; both were built to test claims the entry makes about its own gates.
- **Did the dispatch tell me where to look?** More than in any prior round. The cover note names the five attack surfaces, states the conclusions in advance, and instructs "if the FROZEN claim is honest, say so." Preregistration against that brief is weak and I marked it so at freeze. Two findings did not come from the brief: F-OP32S-01 came from grepping the body for "FB-7b", and F-OP32S-02 required diffing Section 25 against the v0.28 packet on my disk.
- **Is the ASSERTED fraction unchanged from the prior round?** No -- 80.0% to **90.9%**, with COMPUTED falling 3 to **0**. The freeze candidate is the least machine-backed entry in the record, and per policy states neither figure, so the sealed document will not contain that fact.
- **Have the recent rounds all been producer-family?** No. v0.31 was carried by six non-producer seats across two families and adversarially audited by two more. That is the strongest round composition the program has achieved, and it is the reason the amendment has a factual basis to rest on even though the reports do not ship. This round -- v0.32 -- is producer-family advisory again, and my verdict has no weight in it.

## 7. Verdict

**HALT-AND-RETURN-TO-PRODUCER -- advisory only, non-binding. No carry vote. No FB-7b weight. This HALT does not bind the freeze; it is recorded and forwarded.**

Severity ledger as I calibrate it: **1 CRITICAL / 3 HIGH / 2 MEDIUM / 1 LOW / 1 INFORMATIONAL = 8.** Under the producer-instance exclusion none of it carries, and the CRITICAL in particular must be re-rated by a seat whose severity can.

**The FROZEN claim is not earned, and the reason is not a matter of judgement.** The document declares itself FROZEN in `### 0.1 Status` and declares FB-7b OPEN 923 characters later in the same subsection, while Section 25 and the entry declare it RESOLVED. A freeze licensed by a locker's resolution cannot ship stating that the locker is open. That alone returns the draft.

Three things compound it, in descending order of how much they should worry a carrying seat. The amendment that resolves FB-7b **removed** an execution conjunct from the rule rather than relaxing the verdict predicate as the entry describes -- "running all 186 tests" survives in this document only inside a sealed entry quoting a prior objection to its non-satisfaction -- and register item (5) records that pytest was absent from the dispatched environment for three fresh seats this round, which is the conjunct that was deleted. The EXTERNAL count that item (9) uses to subsume an adversarial HIGH consists of two tags no gate examines, one of which grades producer-held non-shipping reports EXTERNAL against its own text; a fabricated DOI raises the same count and builds green. And the register closes zero of thirteen findings while the closing paragraph discloses "packet non-closure" and "fresh-execution non-reproducibility" as standing boundaries.

**What would make the freeze honest.** Four of the five are edits, not investigations: update the Section 0.1 FB-7b sentence or withdraw FROZEN; state the amendment's full scope, including which conjuncts were removed; regrade the seat-reports tag ASSERTED; and either close some findings or write down what FROZEN asserts and what it does not. The fifth is the one that has been outstanding for eight of my reports: deposit `HISTORY.sha256`, cite the DOI, and ship the eight seat reports under manifest.

**Findings a non-producer seat should re-derive first**, since a producer-family seat is the least credible party to adjudicate a producer-family freeze: **F-OP32S-01**, which is `grep -n "FB-7b" ` against the status line; **F-OP32S-02**, which is `grep -c "running all 186 tests"` against any packet from v0.20 through v0.28; and **F-OP32S-03**, which is the P-4 pair and takes one rebuild. None requires taking my word for anything, and the first two require no prior packet at all.

The instrument is in the best internal condition I have audited in nine rounds. It is not ready to be called finished.

---

*Claude Opus 5, Seat B, producer-family advisory. Advisory only -- no carry vote, no FB-7b weight, HALT non-binding, recorded and forwarded. Prepared for Bilal Syed Arfeen. All probes reproducible from the shipped packet; no void probes this round.*

---

# Bismillah ir-Rahman ir-Rahim
