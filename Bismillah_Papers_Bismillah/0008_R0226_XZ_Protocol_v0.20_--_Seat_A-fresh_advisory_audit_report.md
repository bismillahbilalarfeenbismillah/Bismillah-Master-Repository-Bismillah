# Bismillah ir-Rahman ir-Rahim

# R0226 -- XZ Protocol v0.20 -- Seat A-fresh advisory audit report

**Chronological Index:** 8 of 995  
**Date:** 2024  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v20_SEAT_A_FRESH_REPORT.md  
**Source Format:** md  
**SHA-256:** `b57419adec757176aefa351f6b513ad57d31b998d4f10931a30947e505e5cae2`  

---

## R0226 · XZ Protocol v0.20 -- Seat A-fresh advisory audit report

- section: IV. XZ Protocol
- source_file: XZ_v20_SEAT_A_FRESH_REPORT.md
- source_format: md
- text_sha256: b57419adec757176aefa351f6b513ad57d31b998d4f10931a30947e505e5cae2

# XZ Protocol v0.20 -- Seat A-fresh advisory audit report

**Seat:** Claude Opus 5 (Anthropic), Seat A-fresh, producer-family advisory
**Namespace:** F-OP20F
**Mode:** A (substrate verifier -- full packet on disk, build and pytest executable, mutation sandbox)

## 0. State declaration (S-0)

I am a fresh Claude Opus 5 instance. I hold no v0.17, v0.18, or v0.19 packet bytes; I did not author the v0.19 adjudication, the discipline blocks, or the producer brief, and I have no self-model of prior rounds to trust or mistrust.

One disclosure the dispatch could not anticipate: this surface carries a persistent memory store containing a file on the XZ Protocol. I did not open it. Its one-line index description reached me unavoidably ("construct-validation preregistration instrument, retrospective replay of the XZ Utils / CVE-2024-3094 incident"); nothing further did. Every cross-version statement below is derived from bytes in this packet, and I mark each one's origin.

Standing: advisory. My findings cannot HALT, cannot carry CRITICAL or HIGH into the adjudicated set, and do not count toward FB-7b. Where a non-producer seat's severity differs from mine, theirs governs.

## 1. S-1 preregistration

Frozen to disk before any read of Section 27, at `PREREG_OPUS5_FRESH.txt`, sha256 `d3677a4e0bd9d03987b6e66d7d0a1262652b0d498d968b6060211e0faa2c196b`, 2026-08-01T22:03:27Z.

**Contamination, declared at freeze time.** The dispatch orders `build.py` at step 2 and preregistration at deliverable G. build.py's stdout prints Section 27-derived facts: entry count 20, the string "twenty", all 20 seal labels, the FULL_SECTION_27 PASS, PRIOR_HISTORY `41428758...`, and the tally COMPUTED 11 / EXTERNAL 0 / ASSERTED 11 = 50.0%. A preregistration written after that step cannot be blind to those values. I marked each prediction `[BLIND]` or `[CONTAMINATED]` at freeze rather than after scoring. Only the blind ones carry weight. **This is a defect in the dispatch's ordering, not the producer's:** G is unexecutable as specified. Moving preregistration ahead of step 2, or having build.py suppress Section 27-derived output under a flag, would fix it.

| # | Prediction (abbreviated) | Result |
|---|---|---|
| P1 | Entry claims PRIOR_HISTORY closure without disclosing the hardcoded comparand | **Claim correct, framing refuted** -- see F-OP20F-05 |
| P2 | [3c] prose-citation guard silently skips non-shipped files, undisclosed | Correct, and stronger than predicted |
| P3 | PDF unsealed; entry does not name it | Correct |
| P4 | EXTERNAL=0 while the entry narrates other seats' findings | Correct |
| P5 | `sha256sum -c` fails by construction; entry marks the finding CLOSED | Correct |
| P6 | [9d] ordinal gate is one-directional and unstated | Correct (no live hit on these bytes) |
| P7 | build [8] cannot distinguish absent pytest from failing tests | Correct -- confirmed on my own first run |
| P8 | Semantic coverage well under 50%, framed as disclosed | Correct (24.4%) |
| P9 | ASSERTED fraction is 50.0% | Correct -- **contaminated, no weight** |
| P10 | At least one CLOSED cites a report that ships nowhere | Correct |
| P11 | The 20 entries are internally coherent (flagged as my weakest) | **Refuted** -- two contradictions, F-OP20F-02 and -03 |
| P12 | The v0.20 seal gives zero tamper-evidence for carried entries | **Refuted, in the artifact's favour** -- F-OP20F-05 |

Score: 9 blind correct, 2 blind refuted, 1 blind partially refuted, 1 contaminated. Both refutations landed on predictions I had flagged as uncertain, and both were settled by probe rather than by argument. P12 is the one I most want the continuous instance to check against its own report.

## 2. Byte verification table

| Step | Command | Result |
|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | **rc=1.** 16 OK, 1 FAILED (`PACKET_SHA256SUMS` itself). Failure is structural, not content -- see F-OP20F-01. I did not stop; the 16 content seals all verify and the failing line is a manifest self-reference artifact. Stopping would make the dispatch's own step 1 unexecutable on a clean packet. |
| 2 | `python3 build.py` (first run) | **rc=1.** Sole error: `FAIL: All tests GREEN (rc=1)`, with `pytest: ` empty. Cause was environmental -- pytest absent from the container, not a test failure. See F-OP20F-09. |
| 2' | `python3 build.py` (pytest 9.1.1 installed) | **rc=0**, `BUILD PASSED: all checks GREEN`, 164 PASS lines, 0 FAIL. |
| 3 | six-suite canonical pytest invocation | **rc=0**, `186 passed in 12.75s`. AST total 186; collected 186; parity holds. |
| 4 | Independent digest of all 16 manifest members | All 16 match `PACKET_SHA256SUMS`. Normative manifest digest over the 12 code files recomputes to `96178ceb33e6b070a5c4193c72febdd05b3eafe50abdcfa941376c5e372f6799`, matching trust roots and body. |
| 4a | HISTORY.sha256 | 20 entry seals + FULL_SECTION_27 all recompute correctly under build.py's canonicalization. FULL_SECTION_27 independently recomputed to `210e10782d1e66c9b1ccc4e8e5d8c4b17308f125528abe6a188df346c95a6f17`. |
| 4b | PDF | `xz_protocol_v0_20.pdf`, 74 pages, sha256 `61fa7657e8ffc006611a984c038ff49b459f47c578a80c937c54694d00027684`. Not in the manifest, not in `NORMATIVE_FILES`. See F-OP20F-07. |
| 4c | Standing-rules sweep | Zero U+2013/2014/2015 across all 16 normative files and all four context documents. Zero occurrences of the spaced brand variant. Clean. |

Packet arithmetic: manifest covers 17 members (16 content + itself); build.py counts 14 normative files; the zip ships 22. The dispatch's "18 files, PACKET_SHA256SUMS verified" matches none of these directly and is false on both conjuncts as written.

## 3. Claim provenance ledger

22 tags in the v0.20 entry: **COMPUTED 11, EXTERNAL 0, ASSERTED 11. ASSERTED fraction 11/22 = 50.0%.** This reproduces build.py [9c].

The tally is not the interesting number. Two corrections to how it should be read:

**Only 7 of 11 COMPUTED tags are validated by any gate.** build.py [9c] matches `[COMPUTED: build.py [NN]]` only. The remaining four -- `sha256sum | sha256sum`, `pytest + AST`, `grep of Section 22 body`, and `sha256sum of XZ_v17_SEAT_A_REPORT.md and XZ_v17_SEAT_B_REPORT.md` -- are counted and never checked. I recomputed the first three independently from shipped bytes and all three hold. The fourth cannot be recomputed by anyone: neither file ships and neither digest matches any shipped file. See F-OP20F-04.

**The ASSERTED bucket overstates the unanchored region.** At least four ASSERTED claims are checkable from bytes in this dispatch: the adjudicated ledger, the seat verdicts, and the packet composition are all sourced from `XZ_v19_ADJUDICATION.md`, which ships; "the second producer handoff in the program's record" is derivable by counting handoffs in Section 27. Under-tagging is the safe direction and I raise no finding on it, but it means the printed fraction and the quantity D-7 question 3 asks about are different quantities.

Net grading on substance rather than label: 10 of 11 COMPUTED verified by me from shipped bytes; 1 unverifiable by anyone; of the 11 ASSERTED, roughly 4 are verifiable-but-undertagged and 7 genuinely rest on documents outside the packet.

## 4. Probes

All mutations run in sandbox copies against a pristine reference. Every probe carries a pre/post hash assertion per D-3.5.

**P-1 -- benign control.** Unmodified packet. `build.py` rc=0, `BUILD PASSED: all checks GREEN`. Pytest rc=0, 186 passed. The build discriminates.

**P-2 -- discrimination control, body digest corruption.** `xz_protocol_v0_20.md` pre `3c11c51e4bc5fcdd` post `7154092b3fed92db`, MUTATION_LANDED=True. Replaced the FB-4 `xz_protocol_source_frame.py` digest with 64 zeros, one occurrence. Build rc=1 with five independent failures:
```
FAIL: FB-4 row contains xz_protocol_source_frame.py digest (14af97bc2fd052fd...)
FAIL: FB-4 digest for xz_protocol_source_frame.py in body
FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)
FAIL: Prose citation: xz_protocol_source_frame.py digest matches (0000000000000000...)
FAIL: PACKET_SHA256SUMS digest matches: xz_protocol_v0_20.md
```
Gates [3a], [3b], [3c] and [12] are live and mutually redundant on this surface. Not decorative.

**P-3 -- mutation-landed, manifest self-entry.** `PACKET_SHA256SUMS` pre `e4373e4bd2a8c9dc` post `5359974cee3233e1`, MUTATION_LANDED=True. Self-entry digest replaced with 64 zeros. **Build rc=0, zero FAIL lines, `BUILD PASSED: all checks GREEN`.** `sha256sum -c` on the same file: `PACKET_SHA256SUMS: FAILED`. The control the v0.20 entry cites to close F-ADJ19-11 does not cover the line that the canonical verify command reports on. → F-OP20F-01.

**P-4 -- mutation-landed, AST/collection parity.** `test_xz_protocol_kernel.py` pre `2ed9b4c6fc4e5e42` post `2dce37a656efdc1f`, MUTATION_LANDED=True. Appended a `test_`-prefixed function nested inside a helper: `ast.walk` counts it, pytest does not collect it. Build rc=1, `FAIL: Collected (186) == AST (187)`. The parity check lands. The 186 figure is not inflatable by nested definitions without detection.

**P-5 -- novel class: retroactive forgery of a carried historical entry.** `xz_protocol_v0_20.md` pre `3c11c51e4bc5fcdd` post `2a182c04ba4e4f44`; `HISTORY.sha256` pre `e181d6427153ab23` post `2f180cbf47eec355`. Mutated the v0.10 entry title in place, then regenerated all 20 seals, FULL_SECTION_27, and PACKET_SHA256SUMS, leaving `PRIOR_HISTORY` pinned at `41428758...`. **Build rc=0, 164 PASS, zero FAIL** -- including `PASS: FULL_SECTION_27 seal matches` and `PASS: PRIOR_HISTORY digest matches expected`. The build is blind to it, as F-ADJ19-06 discloses. But the independent derivation of the prior HISTORY file over the same forged bytes returns `b25d664fd5e9719905df6b1ec058c959cb2b4ea7e552189c684b67a9ee949b5a` against the pinned `41428758...` -- **forgery detected.** → F-OP20F-05, F-OP20F-06.

**P-6 -- novel class: derivation of the PRIOR_HISTORY chain from v0.20 bytes alone.** No mutation; a pure derivation, so no landing assertion applies. Reconstructed the v0.19 `HISTORY.sha256` as the 19 carried entry seals, plus FULL_SECTION_27 recomputed over Section 27 with the v0.20 entry excised, plus `PRIOR_HISTORY cb67f222...` read from the v0.19 entry text; canonical two-space separator, trailing newline. sha256 = `41428758dc8d25eb310581a0583cfa4c32cd08ba0da08bfb6ec22237d421adc5`. **Exact match to the shipped PRIOR_HISTORY and to build.py's hardcoded literal, first attempt, no tuning.** Extending one link: the v0.18 file predates the PRIOR_HISTORY line, so it is 18 seals plus its own FULL_SECTION_27; sha256 = `cb67f222dd889a520a6fe6230f532d5e8d802c3c7b452feace574ee4a2ea3860`, **exact match** to the value the v0.19 entry records. Two independent SHA-256 matches. → F-OP20F-05.

**Void probes, reported as void per D-3.5.** My first attempt at P-2 and P-3 used a write-then-read lambda that truncated each target before reading it. Post-hashes were `e3b0c44298fc1c14` (sha256 of empty) and `01ba4719c80b6fe9` (sha256 of "0"). The mutations did not land as specified; both runs are VOID and contributed nothing to the findings above. Re-run correctly with the results shown.

## 5. Findings

**F-OP20F-01** [HIGH -- advisory, cannot carry] -- `sha256sum -c PACKET_SHA256SUMS` cannot pass on a clean packet, and build.py [12] does not check the line that makes it fail.
- **Locus:** `PACKET_SHA256SUMS` line 17; `build.py` [12], the `if mem == "PACKET_SHA256SUMS"` branch.
- **Substance:** The self-entry holds `41efce72...`, which is sha256 of the manifest's first 16 lines. The file's own sha256 is `e4373e4b...` and appears nowhere. So the dispatch's execution step 1 -- "stop if it fails" -- returns rc=1 on every clean packet, making the gate unsatisfiable as written. build.py [12] checks digest equality for all 16 members and, for itself, only membership: `check(mem in packet_dict, "PACKET_SHA256SUMS lists itself")`. P-3 confirms a garbage self-digest passes the build green. The v0.20 entry marks F-ADJ19-11 MEDIUM CLOSED on `[COMPUTED: build.py [12] PACKET_SHA256SUMS verification]`.
- **Disposition:** Either remove the self-line and publish the body digest separately, so `sha256sum -c` returns 0; or keep it, relabel it as a body seal in comment form, and have [12] recompute sha256 over lines 1..N-1 and check it. Retag F-ADJ19-11 CLOSED IN PART until step 1 returns 0.
- **Cross-reference:** F-ADJ19-11; D-3.6; dispatch execution step 1.

**F-OP20F-02** [HIGH -- advisory, cannot carry] -- the v0.20 governance count is false, contradicts its own parenthetical, and overwrites a correct carried value.
- **Locus:** Section 27, v0.20 entry, closing sentence of paragraph 1.
- **Substance:** "five consecutive producer-family advisory cycles (v0.16 through v0.19) preceded this round." The range names four versions. The v0.19 entry states "four consecutive producer-family advisory cycles (v0.16 through v0.19)"; `XZ_v19_ADJUDICATION.md` line 515 states "four consecutive producer-family advisory cycles preceded this round." A correct value, twice recorded, was changed to an incorrect one during production of v0.20. It is now sealed into the append-only record. This is the Axiom-3 class -- a count carried from narrative rather than derived -- recurring in the same paragraph that introduces the register.
- **Disposition:** Append-only correction in the v0.21 entry restoring "four". Add a gate asserting that any `<cardinal> consecutive ... (v0.X through v0.Y)` construction in the current entry satisfies cardinal == Y - X + 1.
- **Cross-reference:** v0.19 entry governance sentence; `XZ_v19_ADJUDICATION.md` §515; F-ADJ19-03 (the ordinal gate at [9d] is scoped to "recurrence" and misses this).

**F-OP20F-03** [HIGH -- advisory, cannot carry] -- the adjudicated ledger tallies 11 findings; the register it introduces dispositions 12.
- **Locus:** Section 27, v0.20 entry, sentence 3, and the twelve-item defect register in the same entry.
- **Substance:** Ledger reads 0 CRITICAL / 4 HIGH consensus / 1 HIGH-tentative / 2 MEDIUM / 3 LOW / 1 INFORMATIONAL = 11. The register dispositions F-ADJ19-01 through -12 at 5 HIGH, 2 MEDIUM, 4 LOW, 1 INFORMATIONAL = 12. The LOW bucket is short by one; the register's LOWs are 07, 09, 10, and 12. The defect is inherited verbatim from `XZ_v19_ADJUDICATION.md` lines 394-396, which likewise enumerates twelve and tallies eleven. The tag `[ASSERTED: severity counts from adjudication; no gate covers cross-document severity tallies]` is accurate as to provenance; the value is wrong, and it was checkable against a document shipping in this same packet and against the entry's own next paragraph.
- **Disposition:** Correct to 4 LOW in the v0.21 append-only entry, and correct the source in any re-issue of the adjudication. Add a gate that parses `F-<ns>-NN <SEVERITY>` from the current entry's register and asserts the ledger sentence's per-severity counts equal it. Reproduced by `xz_v20_fresh_seat_probes.py` section [D].
- **Cross-reference:** `XZ_v19_ADJUDICATION.md` §394-396; F-ADJ19-02; D-3.7 ("the count raised must equal the count dispositioned").

**F-OP20F-04** [HIGH -- advisory, cannot carry] -- a COMPUTED tag certifies digests of two files that ship nowhere, and no gate can reach it.
- **Locus:** Section 27, v0.20 entry, item (8), F-ADJ19-08.
- **Substance:** `[COMPUTED: sha256sum of XZ_v17_SEAT_A_REPORT.md and XZ_v17_SEAT_B_REPORT.md]` attaches to `eab568a7...` and `f7841692...`. Neither file is in the packet; neither digest matches any shipped file. Three gates might have caught it and none does: [9c] validates only COMPUTED tags naming a `build.py [NN]` section; [3c] is scoped to `body`, so Section 27 is out of range; and [3c] is additionally guarded by `if os.path.exists(cited_file)`, which is false. COMPUTED is the ledger's strongest grade and it is assignable to a claim no party can recompute. This is the same substance F-ADJ19-02 was raised to fix, surviving at a locus the fix does not cover.
- **Disposition:** Retag EXTERNAL if the two reports are deposited with retrievable digests, ASSERTED otherwise. Extend [9c] to require that every COMPUTED tag not naming a build.py section names a file present in the packet, and fail otherwise.
- **Cross-reference:** F-ADJ19-02 (CLOSED IN PART); F-OP18-11; D-3.2.

**F-OP20F-05** [MEDIUM -- advisory, cannot carry] -- F-ADJ19-01 is implemented as a hand-populated literal, which D-8 forbids, when the derivable form is available in these bytes and is materially stronger.
- **Locus:** `build.py` [9b], `EXPECTED_PRIOR_HISTORY`; Section 27, v0.20 entry, item (1).
- **Substance:** build.py compares the shipped `PRIOR_HISTORY` value against a 64-hex literal embedded in build.py. Both operands ship and both are producer-authored; the comparison is between two constants in the same packet. `AUDIT_DISPATCH_DISCIPLINE_v2.md` D-8 requires "Any value set the build compares against is derived from the file list by tool. No hand-populated set, no fill-in placeholder." The entry describes the check as comparing "against the sha256 of the v0.19 HISTORY.sha256 file" and does not disclose that the file does not ship or that the comparand is a literal; build.py's own comment does disclose it. **The value is not unanchored.** Probe P-6 reconstructs the v0.19 HISTORY file from v0.20 bytes alone and reproduces `41428758...` exactly, and reconstructs the v0.18 file and reproduces `cb67f222...` exactly. Probe P-5 shows the derivation detects a retroactive mutation of a carried entry that the build passes green. The severity here is MEDIUM rather than HIGH precisely because the artifact is stronger than its own documentation: the control exists, it is simply not wired up and not described accurately.
- **Disposition:** In [9b], replace the literal with the derivation -- excise the current-version entry from Section 27, recompute FULL_SECTION_27 over the remainder, assemble carried seals + FULL_SECTION_27 line + the prior entry's recorded PRIOR value, sha256, and check equality against the shipped `PRIOR_HISTORY`. `xz_v20_fresh_seat_probes.py` section [C] is a working reference implementation. Separately, publish the PRIOR_HISTORY value in an external record so it becomes EXTERNAL rather than ASSERTED; without that, a forger who also edits build.py defeats the check. Correct the entry's description of what [9b] compares.
- **Cross-reference:** F-ADJ19-01; D-3.4 ("If the prior file does not ship, that absence is itself the finding"); D-8; F-OP20F-06.

**F-OP20F-06** [MEDIUM -- advisory, cannot carry] -- F-ADJ19-06's boundary statement is overbroad and discourages a defense the packet already supports.
- **Locus:** Section 27, v0.20 entry, item (6); Section 22.2.
- **Substance:** The disclosure states the gate suite is blind to self-consistent forgery -- "a party controlling all normative files can mutate any artifact, recompute every internal surface, and produce a packet passing all build checks." True of the build as shipped; P-5 confirms it. Not true of the packet's information content: `PRIOR_HISTORY` pins entries v0.1 through v0.19 to a value fixed at v0.19, and the F-OP20F-05 derivation detects retroactive mutation of any of them. Stated at full generality the boundary invites the conclusion that no internal control can help, when the historically dominant failure mode in this record -- in-place mutation of a historical entry, seven recorded instances at v0.4, v0.9, v0.11 twice, v0.16, and v0.17 twice -- is exactly the one the packet can detect. Every one of those seven was a side effect, not an attack, and all seven are inside the derivation's reach.
- **Disposition:** Narrow the Section 22.2 statement to blindness against a forger who also controls `build.py`, and record the carried-entry derivation as an implemented control once F-OP20F-05 lands.
- **Cross-reference:** F-ADJ19-06; F-OP20F-05; v0.18 entry item (a).

**F-OP20F-07** [MEDIUM -- advisory, cannot carry] -- the PDF ships in the dispatch, is bound by nothing, and D-8 requires that it be bound.
- **Locus:** `PACKET_SHA256SUMS` (absent); `build.py` `NORMATIVE_FILES` (absent); dispatch prompt, "18 files, PACKET_SHA256SUMS verified".
- **Substance:** `xz_protocol_v0_20.pdf`, 74 pages, sha256 `61fa7657...`, is the human-readable rendering and carries no digest in any shipped text. D-8 requires "The build hashes every packet member, not only the normative files." It does not. On these bytes I sampled six load-bearing values across the two renderings -- version prose, 186, "14 normative files", the manifest digest, "twenty amendment entries", and the PRIOR_HISTORY prefix -- and all six agree, and the PDF carries 20 entries. No divergence exists today; the finding is the absent control. F-FABLE5-03 scoped reference PDFs out of the brand sweep only, and nothing scopes them out of digest, count, or version parity.
- **Disposition:** Add the PDF to `PACKET_SHA256SUMS` and to [12]'s required-member list. Reconcile the dispatch's "18 files" against the manifest's 17 members.
- **Cross-reference:** F-FABLE5-03; D-3.6; D-8.

**F-OP20F-08** [LOW -- advisory, cannot carry] -- F-ADJ19-05's defect class closed at one locus while four structurally identical sites remain.
- **Locus:** `build.py` [3c] `if os.path.exists(cited_file)`; [8] `if m:` around the collection-parity check; [9c] and [9d] `if current_entry_match:`; [9b] and [12] `if len(parts) >= 2` line parsers.
- **Substance:** F-ADJ19-05 HIGH CLOSED describes this class exactly -- "the bare `if os.path.exists(...)` skipped the entire seal block and the build returned green with zero fail-checks" -- and the fix wrapped one site in `check()`. Four identical patterns remain in the same file. [9c] is the load-bearing one: if the entry heading stops matching the regex, the entire provenance-ledger validation prints "(no v0.20 entry found; skipping tag validation)" and appends no error. Severity is LOW, not MEDIUM, because the [9b] seals bind the entry bytes, so no path reaches [9c]'s skip without also regenerating `HISTORY.sha256`, which is F-OP20F-05 territory rather than an independent route.
- **Disposition:** Convert each to `check()` so absence is a failure. For [8], assert separately that the parity regex matched.
- **Cross-reference:** F-ADJ19-05; F-OP18-10.

**F-OP20F-09** [LOW -- advisory, cannot carry] -- build.py [8] cannot distinguish a failing suite from an absent pytest.
- **Locus:** `build.py` [8].
- **Substance:** On my first execution, with pytest not installed, [8] emitted verbatim `FAIL: All tests GREEN (rc=1)` followed by `  pytest: ` with an empty value. The subprocess captured a ModuleNotFoundError on stderr and discarded it. The build record cannot distinguish an environment gap from a genuine red suite. The gate fails safe -- it never reports GREEN when tests did not run -- so this is a diagnostic defect, not a correctness one, and it cost me one round trip rather than a wrong conclusion.
- **Disposition:** Print the tail of `r.stderr` on non-zero rc, and check separately that a test count parsed out of stdout.
- **Cross-reference:** F-OP20F-08.

**F-OP20F-10** [LOW -- advisory, cannot carry] -- D-8, whose heading says it does not ship to auditors, shipped to this auditor.
- **Locus:** `AUDIT_DISPATCH_DISCIPLINE_v2.md` lines 198-223.
- **Substance:** The heading reads "PRODUCER-SIDE COORDINATION (not shipped to auditors)" and the body states the producer does not receive the withheld sections, i.e. the two documents are meant to be disjoint. I received both. The block enumerates the producer's build obligations, which is a direct statement of expected values -- the D-0 leakage class. The v0.20 entry marks F-ADJ19-12 LOW NOTED and claims v0.20 withholds expected values from carrying-seat bundles; I am advisory, not carrying, so that claim is not falsified. **Effect on this report, disclosed:** F-OP20F-05 and F-OP20F-07 both cite D-8 as corroboration. Neither originated there -- F-OP20F-05 came from build.py's `EXPECTED_PRIOR_HISTORY` comment and F-OP20F-07 from `grep pdf PACKET_SHA256SUMS` -- but D-8 sharpened both dispositions, and that is leakage regardless of origin.
- **Disposition:** Split D-8 into a separate file excluded from all seat bundles.
- **Cross-reference:** F-ADJ19-12; D-0.

**F-OP20F-11** [INFORMATIONAL] -- the EXTERNAL grade is unexercised, so build.py's EXTERNAL verification path never runs.
- **Locus:** v0.20 entry tag distribution; `build.py` [9c] `external_refs` loop.
- **Substance:** EXTERNAL count is 0, so the EXTERNAL-file-shipping check executes zero times. A control present in source and never exercised is not evidence about the artifact. Meanwhile `XZ_v19_ADJUDICATION.md` ships in this dispatch and is the source for the ledger, the seat verdicts, and the packet-composition claims, all of which carry ASSERTED. Under-tagging is the safe direction and I raise no finding on the choice itself; the observation is that the ASSERTED fraction is not a measure of the unanchored region, and D-7 question 3 is asking about a quantity the build does not print.
- **Cross-reference:** F-ADJ19-02; D-3.2; D-7.

**Clears.** Gates [3a], [3b], [3c] and [12] are live and mutually redundant on body digests (P-2). The AST/collection parity check lands (P-4). All 20 entry seals and FULL_SECTION_27 recompute correctly under the documented canonicalization. The normative manifest digest, the 186 test count, the 14-file count, the 16-source count, and the Section 22 "when shipped" repair all verify independently. Em-dash and brand sweeps are clean across all 16 normative files and all four context documents. The code plane is byte-clean.

## 6. Internal consistency check

**Does every CLOSED claim in the v0.20 entry have byte evidence in this package?** Nine of twelve register items do, and I verified each: (1) has a live check but a misdescribed comparand (F-OP20F-05); (2), (3), (5), (7), (9), (11) verify at their named build.py sections; (12) is NOTED, not CLOSED. Three do not. Item (4) is DISCLOSED and self-describes as ungated. Item (8)'s CLOSED rests on two digests of files that ship nowhere (F-OP20F-04). Item (10)'s five F-DB19 dispositions rest on `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md`, which does not ship in this packet -- so F-DB19-04 and F-DB19-05, both marked CLOSED, have no byte evidence here. The entry's own tag concedes this ("dispositions from discipline-block text, not gated"), so I record it as a boundary rather than a false CLOSED.

**Do the HISTORY.sha256 seals verify against the Section 27 text?** Yes -- all 20 entry seals, plus FULL_SECTION_27, recomputed independently of build.py. Surjectivity holds: seal labels equal entry labels exactly.

**Is the PRIOR_HISTORY chain value plausible?** Stronger than plausible: exactly reproducible. Both links -- `41428758...` for v0.19 and `cb67f222...` for v0.18 -- derive from v0.20 bytes alone, first attempt. This is the single most consequential result in this report and it runs in the artifact's favour. It also proves something no one has claimed: **the append-only discipline over entries v0.1 through v0.19 is verifiable from this packet.** Two independent SHA-256 matches would both break under any in-place mutation of any carried entry or of Section 27's non-entry text. The record's oldest and most persistent defect -- seven historical in-place mutations across v0.4 through v0.17 -- has a detector sitting unused in the bytes.

**Claims about prior reports unverifiable from any shipped file.** Six: the two v0.17 report digests (item 8); the three seat verdicts and the packet-composition figures of 33/28/15 members, which trace to `XZ_v19_ADJUDICATION.md` -- that document does ship, so these are verifiable against it, though it is itself outside `PACKET_SHA256SUMS`; the F-DB19 dispositions; and `XZ_v20_BUILD_SPECIFICATION.md` and `HANDOFF_ADDENDUM_v20.md`, both named in paragraph 2 and neither shipped.

**Does the record read coherently end to end?** Largely yes, and the append-only corrections at v0.5, v0.17, and v0.18 are unusually candid -- v0.18 item (a) correcting v0.17's own "Section 27 untouched" claim against itself is the strongest single act of self-correction in the twenty entries. Two contradictions emerge that a continuous instance is well placed to miss, because both require reading two entries side by side rather than recalling one:

1. The governance cardinal changed from "four" at v0.19 to "five" at v0.20 over the identical parenthetical range, in the direction of overstatement, overwriting a value the shipped adjudication also records as four (F-OP20F-02).
2. The adjudicated ledger sums to 11 while the register it introduces dispositions 12, an error inherited verbatim from the adjudication and never checked against the paragraph immediately below it (F-OP20F-03).

Both are Axiom-3 instances at v0.20. Both are in ungated prose. Neither is the kind of thing memory of prior rounds would surface -- memory would supply the remembered figure and move on, which is exactly the mechanism by which the correct "four" became "five."

One further scoping note. F-ADJ19-03's gate at [9d] checks only the current-version entry. The v0.16 entry asserts the Axiom-3 pattern "recurred for the ninth time", v0.17 "the tenth time", v0.18 "an eleventh time", v0.19 "the twelfth" -- all sealed, all unauditable, and all outside the gate's reach by construction, since amending them would violate append-only. F-OPUS5-17-06 already records the ordinals as underivable. The correct reading is that F-ADJ19-03 is closed prospectively only; the record retains four ordinal assertions no party can check.

## 7. Boundary report

The outermost layer the build does not compute is the binding between any value in this packet and any record outside it. Every gate is an internal-consistency check: it verifies that the protocol text, the code, the trust roots, the seal file, and the manifest agree with one another, which is exactly the property a single party regenerating all of them preserves by construction. What would bring that layer inside is not a further gate but an external anchor -- a value fixed by a party who cannot revise it, published before the next version exists. The packet is closer to this than it knows. `PRIOR_HISTORY` is already a genuine anchor for anyone who held the v0.19 package, and I have shown both of its links are derivable rather than asserted, which converts the amendment record from self-attested to self-verifying for its historical portion. The step that closes the remaining gap is small: publish the current `HISTORY.sha256` digest at deposit time in a location the producer cannot retroactively edit -- the Zenodo record, or a seat report whose digest is itself recorded elsewhere -- and cite it as EXTERNAL in the next entry. That single act does more for the verification model than any additional gate, because it is the only move that makes a claim in this packet falsifiable by someone who does not trust the producer. Until then, the honest statement of the boundary is that the build proves the packet is self-consistent, proves the carried amendment entries have not been mutated since v0.18, and proves nothing at all about whether either claim corresponds to anything outside the packet.

## 8. D-7 process health

- **Did every probe come from an enumerated list?** No. P-5 and P-6 are not in D-4's classes or anywhere in the discipline blocks; both arose from reading build.py's `EXPECTED_PRIOR_HISTORY` comment and asking whether the value was derivable rather than merely comparable.
- **Did the dispatch tell me where to look, such that my findings were predetermined?** Partly, yes, and this is a finding. Deliverable F's five sub-questions map closely onto sections 3, 5, and 6 of this report, and D-8 -- which the discipline block says does not ship to auditors -- shipped and named two of my dispositions in advance (F-OP20F-10). The findings that did not come from the dispatch are F-OP20F-02, -03, -05, and -06.
- **Is the ASSERTED fraction unchanged from the prior round?** No: 37.5% at v0.19 (6/16, or 43.75% once the invalid EXTERNAL is retagged) to 50.0% at v0.20, computed by me from shipped Section 27 bytes rather than taken from any report. It moved outward. The fair reading is that the v0.20 entry tags 22 claims where v0.19 tagged 16 and v0.18 tagged none, so part of the rise is newly disclosed rather than newly unanchored. The unfair-to-ignore reading is that the boundary is not moving inward, and F-OP20F-05 identifies a specific, cheap move that would reclassify the single most load-bearing ASSERTED value in the packet.
- **Have the recent rounds all been producer-family?** Not this one -- v0.20 adjudicates a genuine tri-seat non-producer round, the first since v0.14. But the count of preceding producer-family cycles is misstated in the entry (F-OP20F-02), and I am producer-family, so this report does not change the answer for v0.20 itself.

## 9. Verdict

**HALT-AND-RETURN-TO-PRODUCER -- advisory only, non-binding.**

Severity ledger as I calibrate it: 0 CRITICAL / 4 HIGH / 3 MEDIUM / 3 LOW / 1 INFORMATIONAL.

**Standing, restated.** I am a producer-family instance. Under the producer-instance exclusion my findings enter as advisory only: they cannot HALT, cannot carry CRITICAL or HIGH into the adjudicated set, and do not count toward FB-7b. My four HIGHs enter the adjudicated set at whatever severity a non-producer seat assigns them, or not at all. Where my severity differs from a non-producer seat's, theirs governs. This verdict is a recommendation to the chair, not a gate.

FB-7b remains OPEN and this report does not advance it. The three findings I would most want a non-producer seat to re-derive independently, because they are the ones a producer-family instance is least entitled to be believed on, are F-OP20F-02 and F-OP20F-03 -- both plain arithmetic against shipped bytes, both cheap to check -- and F-OP20F-05, which is the one finding here that argues the artifact is stronger than its own record claims, and therefore the one where my family affiliation should count most against me.

Recommend the next cycle be carried by Kimi K3 and GLM-5.2 on canonical bytes, with `xz_v20_fresh_seat_probes.py` shipped as a re-runnable check rather than as a claim to be trusted.

---

*Claude Opus 5, Seat A-fresh, producer-family advisory. Prepared for Bilal Syed Arfeen. All probes reproducible from the shipped packet; void probes reported as void.*

---

# Bismillah ir-Rahman ir-Rahim
