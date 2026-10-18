# Bismillah ir-Rahman ir-Rahim

# R0230 -- XZ Protocol v0.25 -- Seat B advisory audit report

**Chronological Index:** 115 of 995  
**Date:** 2026  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v25_SEAT_B_REPORT.md  
**Source Format:** md  
**SHA-256:** `2b3691e327f47a86ce2f664dc734c18657a257ae7eafbdf475e377650c1db330`  

---

## R0230 · XZ Protocol v0.25 -- Seat B advisory audit report

- section: IV. XZ Protocol
- source_file: XZ_v25_SEAT_B_REPORT.md
- source_format: md
- text_sha256: 2b3691e327f47a86ce2f664dc734c18657a257ae7eafbdf475e377650c1db330

# XZ Protocol v0.25 -- Seat B advisory audit report

**Seat:** Claude Opus 5, Seat B (continuous), producer-family advisory
**Namespace:** F-OP25S
**Mode:** A (substrate verifier -- full packet on disk, build and pytest executable, mutation sandbox, plus the v0.20, v0.21, v0.22 and v0.24 packets retained)

## 0. State declaration (S-0)

Continuous. I produced the v0.20 fresh report (F-OP20F-01..11), the v0.21 shallow report (F-OP21S-01..08), the v0.22 shallow report (F-OP22S-01..08) and the v0.24 shallow report (F-OP24S-01..08), and I hold all four packets. **I do not hold v0.23.** I did not author the discipline blocks, the v0.19 adjudication, or any of the F-OP21C, F-OP22, F-OP22C, F-OP24, F-OP24C, F-OP24C899, F-GPT23, F-GLM23 or F-K3C2 namespaces.

Two packet-composition changes worth recording at the top: my four prior seat reports **no longer ship**, which is the F-OP21S-07 / D-0 disposition landing after four rounds of it not landing; and no v0.23 or v0.24 seat report ships either, so this round's register is the first I have audited whose entire input set is invisible from the packet.

Standing: producer-family advisory. Cannot HALT, cannot carry HIGH, no FB-7b weight. Where a non-producer seat's severity differs, theirs governs.

## 1. S-1 preregistration (F)

Frozen at `PREREG_OPUS5_B_v25.txt`, sha256 `e08f58780251af801ae8ef0ad3b2fa68a9c0916f83ad4e885e752afd05f05088`, 2026-08-02T03:11:52Z, before any read of Section 27.

**Contamination.** Fifth consecutive round in which the dispatch orders `build.py` before preregistration. Raised at v0.20, v0.21, v0.22 and v0.24; never dispositioned in any entry.

| # | Source | Prediction | Result |
|---|---|---|---|
| B1 | bytes | **Sharpest.** F-OP24S-02 unfixed for a second round -- the diff shows the producer edited those exact two lines (24 to 25) and left both message strings stale. Predict the entry claims it CLOSED again or omits it | **Correct, worst case.** Item (1) claims the messages "are now correct" -- F-OP25S-01 |
| B2 | bytes | F-OP24S-05's fix is cosmetic: `check(True)` replaced by `check(len(id_sev_pairs) > 0)` inside `if id_sev_pairs:`, provably true wherever it runs. Predict claimed CLOSED with a COMPUTED tag on `[9f]` | **Correct**, and item (5) also misdescribes the original defect -- F-OP25S-03 |
| B3 | bytes | F-OP24S-03 unfixed; else-branch byte-identical | **Correct.** Folded into item (5) and marked CLOSED -- F-OP25S-03 |
| B4 | contaminated | ASSERTED rose to 75.0%, COMPUTED fell to 4; predict the entry reports no figures of its own | **Correct**, and now by explicit policy in item (6) -- F-OP25S-05 |
| B5 | bytes | EXTERNAL 0 for a sixth entry; predict external verification again referenced but ASSERTED, no receipt ships | Correct; nothing external ships |
| B6 | bytes | `[9e]` emitted zero assertions; predict no cardinal-range construction in the entry and no note of it | **Correct** -- no governance sentence at all -- F-OP25S-06 |
| M1 | memory | PDF unbound a sixth round | Correct |
| M2 | memory | `[9c]` arity-one regex unchanged | **Correct**, byte-identical, fourth round |
| M3 | memory | My prior reports no longer ship; predict this is the D-0 disposition and predict it is not announced | **Correct on both.** The change is real and the entry does not mention it |
| M4 | memory | At least one new counting error (least confident) | **Correct** -- D-3.7 reconciliation collapsed, F-OP25S-04 |
| M5 | memory | v0.25 PRIOR_HISTORY == sha256 of my held v0.24 file, giving a fourth anchored link | **Correct**, exact match -- §7 |

Eleven for eleven. That is not a good sign about my predictive value; it is a statement about how much of this round was foreseeable from the previous one's unfixed findings. The only prediction that required new work was B2, and only because I had to read the replacement expression rather than trust the diff's shape.

## 2. Byte verification table

| Step | Command | Result |
|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | **rc=0.** 16 members, all OK. |
| 2 | `python3 build.py` | **rc=0**, `BUILD PASSED: all checks GREEN`, **168 PASS**, 0 FAIL. Two PASS lines contradict their own conditions (F-OP25S-01); one asserts nothing (F-OP25S-03); one is false for 3 of 12 register rows (F-OP25S-02). |
| 3 | six-suite canonical pytest | **rc=0**, `186 passed`. AST 186, collected 186. |
| 4 | Independent digest of all 16 members | All match. Manifest digest recomputes to `cd65e9af32568dac9db6b5ef4a1955191d34cb0ee8152139c2a68cc1e62825f6`, matching trust roots and body. |
| 4a | HISTORY.sha256 | 25 entry seals + FULL_SECTION_27 verify. `PRIOR_HISTORY 8660dfdeac7a17ceb2ac1b6def82f95f4972be711c08e2b9e599dd604bf2ddd4`. |
| 4b | **External anchors** | Three links verified against held files. See §7. |
| 4c | Unsealed members | 6: the PDF, the manifest, three context documents, the dispatch prompt. Down from 9 -- prior seat reports no longer ship. |
| 4d | PDF | 86 pages, unbound for a sixth consecutive round. **149 U+2013 against 0 in the source; 0 double-hyphens against 204.** Content parity holds on all six load-bearing values sampled. |
| 4e | Standing-rules sweep | Zero U+2013/2014/2015 and zero spaced brand variant across all 16 normative files. Clean at source. |

Coverage from `[11]`: total 175627, body 98182 (55.9%), Section 27 ungated 77445 (**44.1%**, seventh consecutive rise), semantic-gate coverage **25.0%**.

## 3. Provenance ledger (A)

**COMPUTED 4, EXTERNAL 0, ASSERTED 12. ASSERTED fraction 12/16 = 75.0%.**

Six-round series computed from shipped Section 27 bytes: v0.19 37.5% (COMPUTED 9), v0.20 50.0% (11), v0.21 57.1% (9), v0.22 78.9% (4), v0.24 63.2% (7), v0.25 **75.0% (4)**. Last round's improvement did not hold; COMPUTED is back to its v0.22 low.

Of the 4 COMPUTED tags, two name build.py sections and two are the standing `sha256sum | sha256sum` and `pytest + AST`, both of which I recomputed independently and both hold. But **both build.py-section tags are attached to claims their named sections cannot verify**:

- Item (1), `[COMPUTED: build.py [9] amendment record check]`, certifies that check *messages* are correct. `[9]` compares entry counts. Nothing in the build examines message-string freshness, and the messages are in fact stale (F-OP25S-01).
- Item (5), `[COMPUTED: build.py [9f] emptiness check]`, certifies that `[9f]` "now asserts at least one row was parsed." The assertion sits inside the guard that makes it vacuous, and an empty register still builds green (F-OP25S-03).

So 2 of 4 COMPUTED tags this round point at gates that cannot see the claims they carry. That is the fourth consecutive round in which at least one COMPUTED tag has done so (v0.22 `[9f]`, v0.24 `[9]` version stamps, v0.25 both). `[9c]` validates that a COMPUTED tag names a real build.py section and cannot tell whether that section covers the claim; the gap is now the dominant source of false CLOSEDs in this record.

EXTERNAL is 0 for the sixth consecutive entry.

## 4. Probes (B, C)

Sandbox copies against a pristine reference; pre/post hash assertion on every mutation.

**P-1 -- benign control.** Unmodified: build rc=0, 168 PASS, 0 FAIL; pytest rc=0, 186 passed.

**P-2 -- discrimination control.** Pre `92b0d4b99b2066d4` post `dac7fe008a9657d9`, LANDED. FB-4 `test_xz_protocol_source_frame.py` digest to 64 zeros. Build rc=1, four independent failures including `FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)`.

**P-3 -- forgery regression.** Pre `92b0d4b99b2066d4` post `4b35574514cda164`, LANDED. Carried entry v0.10 mutated in place; all 25 seals, FULL_SECTION_27 and the manifest regenerated; PRIOR_HISTORY left honest. Build rc=1 with exactly one error: `FAIL: PRIOR_HISTORY matches derivation (8660dfdeac7a17ce...)`. Fourth version, still works.

**P-4 -- novel class: register-row invisibility, run as a discrimination pair.**

*P-4a, control.* Pre `92b0d4b99b2066d4` post `4e8cd2a64e922a2a`, LANDED. Relabelled item (8) to reuse `F-OP24C-02`, which item (3) carries at HIGH. Item (8) is a row `[9f]` can parse. Build **rc=1**:
```
FAIL: Finding F-OP24C-02 dispositioned at HIGH and MEDIUM
```
*P-4b, the finding.* Pre `92b0d4b99b2066d4` post `fd9cfa7eccd1ae2c`, LANDED. The identical duplicate injected into item (6), which ends its ID list with `/ (E)`. Build **rc=0, GREEN**:
```
Register: 9 items, {'HIGH': 2, 'MEDIUM': 4, 'LOW': 2, 'INFORMATIONAL': 1}
PASS: Register parsed at least one item (9 found)
PASS: No duplicate-severity finding IDs (21 unique)
```
Same defect, same severities, opposite verdicts, decided solely by which row it lands in. → F-OP25S-02.

**P-5 -- novel class: the "emptiness check" does not check emptiness.** Pre `92b0d4b99b2066d4` post `63a3cbb5663a263f`, LANDED. Changed register numbering from `(1)` to `[1]` throughout the v0.25 entry and resealed. Build **rc=0, GREEN**:
```
[9f] Register self-consistency
  (no register items found in current entry)
```
Zero assertions. Item (5) states `[9f]` "now asserts at least one row was parsed"; on an empty register it asserts nothing, because the assertion is inside the guard that an empty register fails. → F-OP25S-03.

**P-6 -- `[9c]` arity, fourth round.** Pre `92b0d4b99b2066d4` post `c3ffb76cbba6e4e7`, LANDED. `[COMPUTED: sha256sum of build.py and GHOST_DOES_NOT_EXIST.md]` inside the v0.25 entry. Build **rc=0, GREEN**, one line: `PASS: COMPUTED-tagged file ships in packet: build.py`. Regex byte-identical to v0.21, v0.22 and v0.24. → F-OP25S-07.

**Void probes.** None.

## 5. Findings

**F-OP25S-01** [HIGH -- advisory, cannot carry] -- item (1) is a false CLOSED for the second consecutive round on the identical defect, and this time asserts a state the shipped build directly falsifies.
- **Locus:** `build.py` `[9]`, both `check()` calls; Section 27, v0.25 entry, item (1).
- **Substance:** Item (1) reads "F-OP24-01 / F-OP24S-02 / (E) HIGH CLOSED: build.py [9] check messages stated 'expected 22' and 'twenty-two' while the condition checked for 24. **The messages are now correct for v0.25 (25 entries, 'twenty-five')** `[COMPUTED: build.py [9] amendment record check]`." The shipped build prints:
```
PASS: Entries: 25 (expected 22)
PASS: Protocol says 'twenty-two'
```
The diff from v0.24 shows both lines were edited this round -- `entry_count == 24` became `== 25`, `"twenty-four amendment entries"` became `"twenty-five"` -- while both message strings were left untouched. So the producer had both lines open and changed the conditions without the messages, twice in a row. At v0.24 the entry claimed the strings had been "re-stamped"; at v0.25 it claims they "are now correct." Both are falsified by running the build that ships in the same packet. The `[COMPUTED]` tag names `[9]`, which counts entries and cannot see message text.
- **Disposition:** Derive both messages from `VERSION` and `entry_count` so they cannot desynchronise: `f"Entries: {entry_count} (expected {expected})"`. Then gate the class -- any `check()` message containing a version-like literal that disagrees with `VERSION` should fail the build. Reopen as CLOSED IN PART with the current strings quoted.
- **Cross-reference:** F-OP24S-02; F-OP24-01; F-GLM23-05; F-K3C2-04; the COMPUTED-tag-coverage gap in §3.

**F-OP25S-02** [HIGH -- advisory, cannot carry] -- three of twelve register rows are invisible to `[9f]`, reproducing the defect closed one round earlier, and the entry breaks its own stated convention to do it.
- **Locus:** Section 27, v0.25 entry, items (1), (2), (6); `build.py` `[9f]` register regex.
- **Substance:** Items (1), (2) and (6) each end their ID list with `/ (E)`, denoting the fresh instance. The `[9f]` regex requires the final alternation element to match `F-\w+-\d+`; `(E)` does not, so the match fails and the row is not seen. The build reports `Register: 9 items` against twelve rows in prose. This is a verbatim recurrence of the defect the **v0.24 entry item (1)** dispositioned HIGH CLOSED -- "the register-item regex did not parse parenthetical qualifiers ... causing 2 of 12 register items to be invisible ... All 12 rows parse" -- now at 3 of 12 instead of 2. And item (4) of this same entry states "The finding IDs in this entry use unique per-round prefixes and **no parenthetical qualifiers**," which the entry violates three times in the register that item (4) sits in. P-4 makes the consequence concrete: an injected duplicate severity fails the build in a parsed row and passes green in an invisible row, with `PASS: No duplicate-severity finding IDs (21 unique)` printed beneath it. The three invisible rows carry F-OP24S-01, F-OP24S-02 and F-OP24S-04 -- the FB-7b finding, the false-CLOSED finding and the coverage finding -- so the gate is blind precisely where last round's HIGHs were dispositioned.
- **Disposition:** Give the fresh instance a real ID namespace, as item (4) already prescribes; `(E)` is not an identifier. Independently, harden the regex to tolerate any bracketed token in the ID list rather than only parenthetical suffixes on well-formed IDs, and assert that the parsed row count equals the count of `(N)` markers in the register so an invisible row fails the build rather than shrinking the total.
- **Cross-reference:** v0.24 item (1); F-GPT23-02; F-GLM23-01; F-K3C2-01; item (4) of this entry; F-OP24S-03.

**F-OP25S-03** [MEDIUM -- advisory, cannot carry] -- item (5) closes two findings on a misdescription of one of them, and neither is fixed.
- **Locus:** Section 27, v0.25 entry, item (5); `build.py` `[9f]`.
- **Substance:** Item (5) reads "F-OP24S-03 / F-OP24S-05 / F-OP24C-04 / F-OP24C-09 MEDIUM CLOSED: [9f] ended with an unconditional check(True,...) that could never fail, **making the gate green on zero parsed rows**. The unconditional PASS is removed; [9f] **now asserts at least one row was parsed**." Three problems, in ascending order of consequence. First, the `check(True)` never executed on zero parsed rows -- it sat inside `if id_sev_pairs:`, so the zero-row case took the else-branch, which is what my F-OP24S-03 was about and which is byte-identical this round. Second, the unconditional PASS was not removed; it was replaced by `check(len(id_sev_pairs) > 0, ...)` **in the same guarded block**, so its condition is provably true wherever it runs. Third, the claim that `[9f]` now asserts at least one row was parsed is falsified by P-5: an empty register still builds green with `(no register items found in current entry)` and no assertion. The item merges two distinct findings, restates one of them incorrectly, and fixes neither.
- **Disposition:** Move the assertion outside the guard: `check(bool(id_sev_pairs), ...)` with the else-branch deleted. Reopen F-OP24S-03 and F-OP24S-05 separately -- they are different defects and merging them is what produced the misdescription.
- **Cross-reference:** F-OP24S-03; F-OP24S-05; F-OP22S-01; F-ADJ19-05.

**F-OP25S-04** [MEDIUM -- advisory, cannot carry] -- D-3.7 reconciliation collapsed after one clean round: two of five instances declare findings by bare count, and two declared IDs are dispositioned nowhere.
- **Locus:** Section 27, v0.25 entry, preamble and register.
- **Substance:** The preamble declares "deep A: F-OP24-01..05; shallow B: F-OP24S-01..08; **one-round C: 11 findings**; two-round D: F-OP24C899-01..08; **fresh E: 11 findings**" -- 43 findings raised, of which 22 are declared by count with no ID namespace, making reconciliation structurally impossible for half the input. Of the 21 enumerable IDs, **F-OP24C899-01 and F-OP24C899-04 appear nowhere in the register**. Instance C's eleven findings appear as nine distinct `F-OP24C-` IDs. Instance E's eleven appear as three bare `(E)` mentions. v0.24 reconciled exactly -- 21 declared, 21 dispositioned, zero absent -- and I recorded that as a clear. One round later the property is gone, and this is the same class as F-ADJ19-04, F-OP18-09, F-OP22S-03 and v0.23 correction (e), now in its fifth instance.
- **Disposition:** Require every reporting instance to declare an ID range, never a count; a bare count cannot be reconciled and should be rejected at dispatch time. Then implement the reconciliation as a gate -- expand every `F-<ns>-NN..MM` in the current entry and assert each expanded ID appears in the register. v0.23 item (10) declined this as "a D-3.7 responsibility, not a build gate"; two rounds of evidence now say the responsibility is not discharged reliably by hand.
- **Cross-reference:** F-ADJ19-04; F-OP22S-03; v0.23 correction (e) and item (10); D-3.7.

**F-OP25S-05** [MEDIUM -- advisory, cannot carry] -- the entry states the favourable trend in prose and omits the unfavourable current figure by policy.
- **Locus:** Section 27, v0.25 entry, items (6) and (12); `[9c]` and `[11]` output.
- **Substance:** Item (6) closes my F-OP24S-04 by adopting a standing policy: "the entry does not restate any percentage as prose to avoid the stale-figure recurrence." That policy is defensible and I credit it -- the figures are in the shipped build's output, which is more verifiable than prose, and it eliminates the stale-figure surface I have raised in three consecutive reports. But item (12), in the same register, states in prose that "the ungated share rose for a sixth consecutive round; **the provenance trend reversed for the first time (ASSERTED fraction fell)**." That is accurate for v0.24, the round item (12) dispositions. It is not accurate now: ASSERTED rose 63.2% to **75.0%**, COMPUTED fell 7 to **4**, and the ungated share reached **44.1%**, a seventh consecutive rise. So the entry states the one favourable trend the series has produced and, by policy, states no figure that would show it reversed back. I do not read this as concealment -- item (6)'s reasoning is sound and the numbers are computed by the shipped build -- but a no-percentages policy that admits a prose exception for the good round is not a no-percentages policy. Separately, item (6) is graded CLOSED where CLOSED IN PART is right: my F-OP24S-04 had two parts and only the false-CLOSED half is resolved.
- **Disposition:** Apply the policy symmetrically -- no trend claims in prose either, or gate the entry's trend claims against `[11]` and `[9c]` output the way `[3]` gates digests. Regrade item (6) CLOSED IN PART.
- **Cross-reference:** F-OP24S-04; F-OP22S-04; F-OP21S-04; F-OP18-12.

**F-OP25S-06** [LOW -- advisory, cannot carry] -- `[9e]` executed zero assertions because the entry dropped its governance sentence, and nothing requires one.
- **Locus:** `build.py` `[9e]`; Section 27, v0.25 entry.
- **Substance:** The `[9e]` section printed its heading and no check lines. The v0.25 entry contains no `Governance:` sentence and no cardinal-range construction of any kind -- the first entry since v0.19 without one. `[9e]` was added at v0.22 to catch my F-OP20F-02, a governance miscount, and widened at v0.24 after F-GPT23-07; it is inert this round not because it passed but because its subject is absent. Nothing in the build or in Section 22 requires a governance statement to exist, so a gate whose purpose is to check that statement can be silenced by omitting it. Given this is the round in which the FB-7b posture changed materially, the absence of a governance sentence is also a substantive gap in the record, not only a gate one.
- **Disposition:** Require a governance sentence per entry and `check()` its presence, so `[9e]` fails on absence rather than falling silent. This is the same shape as F-OP25S-03 and should be fixed with it.
- **Cross-reference:** F-OP20F-02; F-GPT23-07; F-GLM23-03; F-OP24S-03.

**F-OP25S-07** [LOW -- advisory, cannot carry] -- the two long-running disclosed defects are unchanged and correctly NOTED.
- **Locus:** `build.py` `[9c]` `file_computed`; `PACKET_SHA256SUMS`.
- **Substance:** The `[9c]` regex is byte-identical to v0.21, v0.22 and v0.24 -- fourth round -- and P-6 confirms a COMPUTED tag naming a non-existent second file builds green. The PDF is absent from the manifest and from `required_members` for the sixth consecutive version and carries 149 en-dashes against a source with none. Item (10) NOTES both accurately and calls them DISCLOSED. I raise this at LOW and as one item because the record is honest about both; the finding is that a defect disclosed in four consecutive entries and fixable by one regex edit is being carried rather than closed, and disclosure is not a terminal state.
- **Disposition:** Capture all filename-shaped tokens per tag. Add the PDF to the manifest and extend `[4]` to its extracted text. Neither needs a carry round to authorize.
- **Cross-reference:** F-OP21S-05; F-OP22S-05; F-OP24S-07; F-OP20F-07; F-K3C2-05.

**F-OP25S-08** [INFORMATIONAL] -- the FB-7b retraction is the strongest act in this entry and should be recorded as such.
- **Locus:** Section 27, v0.25 entry, "v0.24 status note"; item (2).
- **Substance:** The status note restates all four of my F-OP24S-01 grounds accurately -- unshipped carrying-seat reports, the four-conjunct definition against a single evidenced conjunct, the record's own "not carry-clean" annotation, and unbound seat reports -- adds a ground I did not raise, credits the v0.24 entry for correctly not declaring FB-7b closed, and states plainly: "This entry does not reassert the satisfaction claim. FB-7b remains OPEN pending a re-carry on bytes where the carrying-seat reports are verifiable." The body agrees. A producer-family entry retracting the program's most consequential claim, on advisory findings that cannot bind it, is the behaviour the whole apparatus exists to produce, and it happened here without a non-producer seat forcing it. That is worth more than any gate added this round. The residual is unchanged and named in item (3): the reports still do not ship, so the retraction is as unverifiable as the claim it retracts, and EXTERNAL remains 0 for a sixth entry.
- **Cross-reference:** F-OP24S-01; item (3); Section 25 FB-7b row; §7.

**Clears.** Step 1 rc=0; build green; 186/186. The recursive PRIOR_HISTORY derivation reproduces the shipped value, survives a fourth version, and still catches a retroactive carried-entry forgery with exactly one correct error. `[3a]`, `[3b]`, `[3c]` and `[12]` remain live and redundant (P-2). `[9f]`'s duplicate check works correctly on every row it can see (P-4a). Item (4)'s root-cause diagnosis of the F-OP22C namespace collision is the best piece of analysis in the entry and explains a defect I raised at v0.22 without identifying its cause. My four prior seat reports no longer ship -- the D-0 disposition landing after four rounds. Em-dash and brand sweeps clean at source.

## 6. Self-score of prior findings (D)

| ID | v0.24 severity | v0.25 disposition | Landed? |
|---|---|---|---|
| F-OP24S-01 | HIGH | item (2) HIGH NOTED | **Substantively yes.** The satisfaction claim is retracted, all four grounds restated accurately, FB-7b OPEN in entry and body. Reports still unship -- item (3) |
| F-OP24S-02 | HIGH | item (1) HIGH CLOSED | **No.** Second consecutive false CLOSED; build prints both stale strings -- F-OP25S-01 |
| F-OP24S-03 | MEDIUM | item (5) MEDIUM CLOSED | **No.** Else-branch byte-identical; P-5 shows an empty register still green -- F-OP25S-03 |
| F-OP24S-04 | MEDIUM | item (6) MEDIUM CLOSED | **Partly.** The false-CLOSED half is resolved by an honest no-percentages policy; the disclosure half is not, and item (12) breaks the policy for the favourable trend -- F-OP25S-05 |
| F-OP24S-05 | MEDIUM | item (5) MEDIUM CLOSED | **No.** `check(True)` replaced by a differently-spelled tautology -- F-OP25S-03 |
| F-OP24S-06 | LOW | item (9) MEDIUM NOTED | Disclosed, promoted a severity. Accurate |
| F-OP24S-07 | LOW | item (10) LOW NOTED | Disclosed, unchanged. Fourth round for the regex, sixth for the PDF -- F-OP25S-07 |
| F-OP24S-08 | INFORMATIONAL | item (12) INFORMATIONAL NOTED | Disclosed for v0.24; the trend reversed back and is unstated -- F-OP25S-05 |

Eight raised, eight dispositioned, none absent -- the second consecutive round with that property. But **three are CLOSED without landing** (items 1 and 5, covering three of my findings), which is the worst closure record of the four rounds I have audited: v0.21 closed one of eight falsely, v0.22 closed one of eight falsely, v0.24 closed none falsely, v0.25 closes three.

**What four prior rounds bought.** The chain anchors in §7. The F-OP25S-01 diagnosis, which needed the v0.24 build.py to see that the same two lines were edited and left stale twice. The F-OP25S-03 diagnosis, which needed my own v0.24 finding text to see that item (5) misdescribes it -- a fresh seat reading only v0.25 would see a plausible fix for a plausible defect. And the F-OP25S-04 comparison against v0.24's clean 21/21 reconciliation. It bought **nothing** for F-OP25S-02, which is the round's other HIGH: twelve rows in prose against nine in the build's own output, visible to anyone who counts.

## 7. Boundary report (E)

The boundary held where it was and did not extend. Three chain links are now anchored against bytes I hold from prior dispatches -- v0.22's recorded PRIOR_HISTORY equals the sha256 of my held v0.21 file, v0.23's equals my held v0.22 file, and v0.25's shipped `8660dfde...` equals the sha256 of my held v0.24 file exactly -- and all 24 carried entry seals are byte-identical across the v0.20, v0.21, v0.22 and v0.24 packets. Append-only has now held across six versions with zero in-place mutation, and P-3 confirms the detector still fires. That is a genuinely strong internal record. What has not moved is everything outside it: EXTERNAL is 0 for the sixth consecutive entry, no deposit receipt ships, the Zenodo verification recorded at v0.24 remains an `[ASSERTED]` claim about a seat whose report does not ship, and the three v0.23 carrying-seat reports -- on which the program's terminal freeze-blocker turns -- are absent from this packet as they were from the last. The entry is admirably clear about this: item (3) says adding the reports to `PACKET_SHA256SUMS` or citing their deposit digests is "deferred to the re-carry round," and the status note says FB-7b is open "pending a re-carry on bytes where the carrying-seat reports are verifiable." That is the correct diagnosis and it is now the whole of the remaining work. Meanwhile the interior thinned again -- ungated share 44.1%, seventh consecutive rise, COMPUTED back to 4, and two of those four tags naming gates that cannot see their claims. The step has not changed across five of my reports and is smaller now than it was: put the three carrying-seat reports in the packet, or their digests in the entry, and the terminal question becomes answerable by a reader instead of by assertion.

## 8. D-7 process health (G)

- **Did every probe come from an enumerated list?** No. P-4's visible/invisible pair and P-5 are novel; neither appears in D-4's classes. P-4 came from noticing that the build reported nine register items where the entry showed twelve.
- **Did the dispatch tell me where to look?** Less than any prior round, and the packet no longer ships my earlier reports, which is a real improvement in seat hygiene. Deliverable D still structures §6. One of my two HIGHs (F-OP25S-02) needed no prior context at all.
- **Is the ASSERTED fraction unchanged from the prior round?** No -- 63.2% to 75.0%, with COMPUTED falling 7 to 4. Last round's reversal did not hold, and the round in which it reversed back is the round whose entry, by policy, states no figure of its own. EXTERNAL 0 for the sixth entry.
- **Have the recent rounds all been producer-family?** Yes. v0.24 and v0.25 are producer-family advisory, five Opus 5 instances this round. The last non-producer contact was the v0.23 carrying round, and FB-7b is now correctly OPEN pending a re-carry.

## 9. Verdict

**HALT-AND-RETURN-TO-PRODUCER -- advisory only, non-binding.**

Severity ledger as I calibrate it: 0 CRITICAL / 2 HIGH / 3 MEDIUM / 2 LOW / 1 INFORMATIONAL = 8.

I returned CONDITIONAL PASS at v0.24 and I am returning HALT here, so the reason should be explicit. It is not the count -- the ledger is identical to last round's. It is that this entry contains **two closures that the build shipping in the same packet falsifies**: item (1) states the check messages "are now correct" while the build prints them stale, and item (5) states `[9f]` "now asserts at least one row was parsed" while an empty register builds green. Item (1) is the second consecutive false CLOSED on the identical defect, on lines the producer edited both times. Add a register gate blind to a quarter of its own rows and printing a green line asserting the property it cannot check for them, and the failure mode is no longer a defect in a gate -- it is an entry describing a build state that the build contradicts, three times, in one document that is about to be sealed append-only. Everything here is a small edit: two f-strings, one guard moved outside its `if`, one ID namespace. All four are cheaper before the seal than as corrections after it.

**Standing, restated.** Producer-family advisory. Cannot HALT, cannot carry HIGH, no FB-7b weight. My verdict is a recommendation to the chair.

Three findings I would most want a non-producer seat to re-derive: **F-OP25S-01**, which is two lines of the build's own stdout against one sentence of the entry; **F-OP25S-02**, which is counting `(N)` markers in the register against the build's `Register: 9 items`; and **F-OP25S-03**, which is one `if` statement read against one claim. None requires taking my word for anything, and none requires holding a prior packet.

Against all of that: **F-OP25S-08 is the most important thing in this round and it is a clear, not a finding.** The entry retracts the FB-7b satisfaction claim on advisory findings that could not bind it, restates the grounds accurately, adds one I missed, and credits its predecessor for what it got right. Five of my reports have asked for one thing. It is now the only thing left: ship the three carrying-seat reports, or their digests, and re-carry.

---

*Claude Opus 5, Seat B, producer-family advisory. Prepared for Bilal Syed Arfeen. All probes reproducible from the shipped packet; no void probes this round.*

---

# Bismillah ir-Rahman ir-Rahim
