# Bismillah ir-Rahman ir-Rahim

# R0842 -- R29 Seat Reports (v0.72 audit)

**Chronological Index:** 560 of 995  
**Date:** 2026-08-17  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R29_REPORTS.txt  
**Source Format:** txt  
**SHA-256:** `3a7be3dd58052c9bc0bae07529d82045b34b25f53ab33ac1a0983825cf8877a6`  

---

## R0842 · R29 Seat Reports (v0.72 audit)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R29_REPORTS.txt
- source_format: txt
- text_sha256: 3a7be3dd58052c9bc0bae07529d82045b34b25f53ab33ac1a0983825cf8877a6

# R29 Seat Reports (v0.72 audit)

######_REPORT_SPLIT_######
# Source: SHIPPED_R29_S01_REPORT.md
# XZ_v072_R29_S01_REPORT -- XZ Protocol v0.72, Round 29, Seat S01 (FRESH, CARRYING, binding)

**VERDICT: HALT (binding).** Five Class A (HIGH) findings at Strings 3 and 5 -- outside the String-6 self-referential surface. Bearer 4 (Goedel confinement) = FALSE. R28 repair Groups 1-4 verified landed on the current bytes; Group 5 is NOT discharged (three live instances); the v0.71-entry/PRIOR_HISTORY surface carries two new Class A defects that only held v0.71 bytes can fully adjudicate.

- Seat: S01 | Role: CARRYING (binding) | Mode: FRESH (no prior context, no held bytes)
- Executor: Kimi K3, Moonshot AI -- not a default/blend/router. The platform exposes no checkpoint IDs or weight revisions to this seat; none are fabricated. The dispatch names this seat Kimi K3 and the seat executed is Kimi K3; no seat-label drift this round.
- Dispatch: R29 DISPATCH -- Seat S01 (FRESH), Round 29, v0.72, 2026-08-17; producer Claude Opus 4.6 (BARRED)
- Execution surface: Linux sandbox, Python 3.12, pytest 9.1.1 (installed this session; see D-5 note), packet dir `/mnt/agents/output/XZ_v072_R29/packet`
- Date of execution: 2026-08-17 (UTC)

Bismillah.

---

## S-0 STATE DECLARATION (frozen before the v0.72 entry was opened)

Frozen verbatim in `S0_S1_PREREGISTRATION_FROZEN.md` (sha256 c3f47188a2a5247e6af2fc19352726c29470992582cd7c92f0a76111a9d6b27c, frozen 2026-08-17 15:38 UTC, before any read of `xz_protocol_v0_72.md`, `build.py`, code modules, HISTORY content, or report bodies). Summary:

- Held packages: NONE. Fresh seat. PRIOR_HISTORY cannot be anchored to a held v0.71 HISTORY file; internal-derivation checks only, limitation stated.
- EXECUTING seat; family Moonshot (non-producer); carry is binding.
- Read before freezing: the nine non-protocol dispatch files, the extraction listing, and `sha256sum -c` output only.
- Metadata visibility: no checkpoint/weight identifiers are exposed to this seat; identity stated as dispatch-named, nothing further fabricated.

## S-1 PREREGISTERED PREDICTIONS -- SCORED

| # | Prediction (frozen) | Score | Evidence |
|---|---|---|---|
| P1 | At least one of the seven repairs byte-false/incomplete/mis-described | HELD | Group 5 repair not discharged (F-S01-72-01/02/03); Group 3 residual label defect (F-S01-72-06) |
| P2 | More narrated-not-derived counts beyond the 33/33 claim | HELD | F-S01-72-01 ("seventy-two ... v0.1 through v0.71"), F-S01-72-10 (33/33 vs 32/32) |
| P3 | Repair surface carries new Class A/B defect | HELD | F-S01-72-06 (gate [13] PASS label on failure path), F-S01-72-07 (gate [10h] substring satisfier) |
| P4 | Tagging defect at String 6 in the v0.72 entry | HELD (weak form) | F-S01-72-08 (COMPUTED-tag format escapes [9c]), F-S01-72-09 (untagged residuals); no substantively false COMPUTED tag found -- all nine mutation-verified |
| P5 | boundaries.json version 0.72 TRUE | HELD | `"version": "0.72"` on shipped bytes |
| P6 | pytest 186 passed; build BUILD PASSED 0 FAIL | HELD | 186 passed in 12.21s; build rc=0 |
| P7 | Gate [13] 39/39/0/0/0 independently reproduces | HELD | independent recount: 39 reports-side, 39 index-side, 0/0/0 |

No prediction was REFUTED; none NOT REACHED. (A seat that never records a REFUTED prediction is pattern-matching; this round the artifact confirmed all seven. Noted as a calibration warning for this seat's own priors.)

---

## 1. PACKET INTEGRITY AND STAGING

Extraction per AUDIT_CONTEXT script (split marker `######_XZPACKET_FILE_SPLIT_######\n`): 32 members extracted. The three top-level uploads (PROTOCOL.txt, FINDINGS_INDEX.txt, BOUNDARIES.txt) are byte-identical (`cmp`) to the in-packet members `xz_protocol_v0_72.md`, `r27_findings_index.json`, `xz_protocol_boundaries.json`.

`sha256sum -c PACKET_SHA256SUMS`: **32 members, 32 OK, 0 FAILED** (verbatim log: `logs/01_sha256sum.log`). The manifest has 32 lines; the AUDIT_CONTEXT "Build status (tool-derived)" section claims "33/33 OK" -- see F-S01-72-10.

Post-probing re-check (after all sabotage work, which ran only on copies under `probes/`): **32/32 OK, 0 FAIL**; no `__pycache__` or stray files in the packet dir (one auditor-side `__pycache__` created by an import probe was removed and the sums re-verified; canonical bytes never edited).

## 2. REQUIRED BASELINE EXECUTION

| Command | Log | Result | rc |
|---|---|---|---|
| `sha256sum -c PACKET_SHA256SUMS` | logs/01 | 32/32 OK | 0 |
| `python3 build.py` | logs/02 | 286 PASS lines, 0 FAIL, `BUILD PASSED: all checks GREEN` | 0 |
| `pytest` (explicit six-file list) | logs/03 | **186 passed** in 12.21s | 0 |
| gate [13] line (from build log) | logs/02 | `PASS: CI-8 cardinality: 39 in reports, 39 in index, 0 missing, 0 phantom, 0 severity mismatches` | -- |

D-5 environmental note: pytest was not pre-installed in this fresh sandbox; `pip install pytest` (9.1.1) preceded the first pytest run. No rc=1 was ever counted against the packet for environmental reasons; the first build.py run (after install) returned rc=0.

## 3. INDEPENDENT RECOMPUTATION (auditor-side code; build.py never imported/exec'd for derived values)

| Surface | Value | Result |
|---|---|---|
| PACKET_SHA256SUMS | 32 OK / 0 FAILED | OK |
| ENTRY seals in HISTORY.sha256 | 72/72 recomputed match (ENTRY_v0.1 .. ENTRY_v0.72) | OK |
| ENTRY_v0.72 seal | `f94ba27fbe229271b976deea872467504e8c5a02cf60c6beea700a3abf2f6bda` | matches HISTORY line |
| FULL_SECTION_27 | `15f64e55b5bc8c6f4f2ec2bd2089b02d38852095f96f7211a1abf2d9d758e4cf` | matches HISTORY line |
| Unsealed tail after `*Provenance and review status.*` | 819 chars | reported, unsealed by construction |
| Manifest (12 ALL_CODE_FILES parsed from build.py source) | `a48c291218672b1108082043dc8794616d002db4adad19f6f608564498c23c3d` | == trust_roots `manifest_digest` |
| PRIOR_HISTORY (HISTORY line) | `f88dd44ecb1646341c3718bd65ff842d2f44bac28d40f3a10cc21fb786c1aa33` | == recursive reconstruction over current bytes (reconstruct(71)) |
| PRIOR_HISTORY anchor to held v0.71 HISTORY | NOT POSSIBLE (fresh seat, nothing held) | limitation stated; see F-S01-72-04 |

Independent PRIOR_HISTORY chain reconstruction (auditor re-implementation of the [9b] recipe, `logs/06_prior_history.log`):

- reconstruct(70) = `2e41e74578df7bd66f4d9de3307bc0f5423fd3e6390c90bf9a042a9893d354d6` == v0.71 entry's embedded PRIOR_HISTORY. Convention holds at v0.71.
- reconstruct(71) = `f88dd44e...` == HISTORY.sha256 PRIOR line. Gate-consistent.
- v0.72 entry's embedded PRIOR_HISTORY = `01e0f76325cbabc43958d97f1a4ce013e755ed3edc00a28b89cf8435f4ca633c` == **neither** of the above. See F-S01-72-04.

## 4. R28 CLEARANCE VERIFICATION (discharge on CURRENT v0.72 bytes)

| R28 group | Required repair | Discharge evidence (this round, canonical bytes) | Status |
|---|---|---|---|
| G1 C-suffix in DECLARATION_PATTERNS | add C? to all five operative patterns; delete or wire in FINDING_ID_RE | All five patterns carry `C?` (source); falsifier probe: `F-S01C-70-99` heading extracts non-empty; all five declaration formats accept C-suffix; X-suffix control correctly rejected; mutation (C? stripped in a copy) makes the falsifier fail (logs 07, 15) | DISCHARGED; residual: extract_findings.py FINDING_ID_RE still dead code (folded into F-S01-72-08, LOW) |
| G2 gate [13] fail-open | else branch -> check(False, ...) | Source: `check(False, "CI-8 gate: no report files present (fail-closed, F-PR71-05)")`; sabotage probe with all R27 reports removed: `FAIL: CI-8 gate: no report files present`, BUILD FAILED rc=1 (log 08) | DISCHARGED |
| G3 summary hardcoded zeros | derive from computed variables | Source: f-string over `len(report_fids)`, `len(index_fids)`, `len(missing_from_index)`, `len(phantom_in_index)`, `len(sev_mismatches)`; values verified computed on failure-path probe (log 09) | VALUES DISCHARGED; the `PASS:` label is still hardcoded and prints on the failure path -- new finding F-S01-72-06 (MEDIUM) |
| G4 register reproduction crash | fix register_gen on r27 index; match entry text or update entry | `xz_protocol_register_gen.py r27_findings_index.json` rc=0, no warnings, 7 groups + 21 NOTED items; r25 index rc=0 (logs 05, 10). Entry register NOT byte-reproducible: entry lists groups in group_id order with compressed text and no NOTED section; generator sorts by severity and emits full text. The v0.72 entry itself scopes this: "Closes F-S01-70-01, F-S04-70-04 partially (register still not wired into build.py)" | PARTIAL (honestly scoped by the entry; carried, not re-findinged) |
| G5 version-token staleness (Section 0.1 / 22.2 / Status) | update all stale version tokens | Section 0.1 headline updated, but: (a) "seventy-two amendment entries, v0.1 through v0.71" -- internally impossible (72 entries; range spans 71; actual range v0.1-v0.72); (b) Section 22.2 carried-entry bound still reads "v0.1 through v0.68" -- four versions stale; (c) FB-7b trajectory row terminates at R27, R28 absent | NOT DISCHARGED -- F-S01-72-01, F-S01-72-02, F-S01-72-03 (all HIGH) |
| G6 gates [2f]/[10i] enforce false claims (VERSION-1 convention) | design decision required (NOTED at R28) | [10i] passes at v0.72 on the Section-0.1 occurrence of "v0.1 through v0.71" while the semantic 22.2 locus remains v0.68 -- the gate binds token presence anywhere in body, not the locus it names | STILL OPEN; mechanism confirmed live (F-S01-72-02 evidence) |

v0.72-entry claims about the R28 triage verified against the shipped R28 reports (packet-closed evidence): the transposition claim is TRUE (SHIPPED_R28_S02 lines 206/280: the C-suffix landed-assertion failure is F-S02-70-02; line 246/328: F-S02-70-06 is the summary-line finding; the triage cited 06 where 02 belongs and 07 where 06 belongs); the vanished-findings claim is TRUE (`F-S02-70-02` and `F-S04-70-05` occur nowhere in R28_TRIAGE.txt; both exist as HIGH findings in the shipped seat reports); "five of six R28 convergence groups marked CLOSED" is TRUE (groups 1-5 CLOSED, group 6 NOTED).

---

## 5. PROBE BATTERY (all probes on byte copies under `probes/`; canonical packet untouched, re-verified after)

Modelled adversaries: careless producer (stale tokens), stale-context producer (narrated counts), self-consistent forger (reseal after mutation), patient contributor (format-drift tag evasion).

| # | Probe | Type | Result | Log |
|---|---|---|---|---|
| P-01 | C-suffix falsifier from the v0.72 entry (`F-S01C-70-99` heading through all five declaration patterns) | landed-assertion | non-empty dict on all five patterns; X-suffix discrimination control empty | 07 |
| P-02 | C-suffix mutation: strip `C?` from DECLARATION_PATTERNS in a copy, re-run falsifier | mutation control | falsifier returns `{}` -- the entry's falsifier discriminates | 15 |
| P-03 | Gate [13] fail-closed: remove all four R27 reports from a copy | sabotage | `FAIL: CI-8 gate: no report files present (fail-closed, F-PR71-05)`; BUILD FAILED rc=1 | 08 |
| P-04 | Gate [13] failure-path output: delete one findings[] record from a copy of the index, reseal sums | sabotage+reseal | `FAIL: CI-8 missing from index: 1 (F-S01-68-01)` then `PASS: CI-8 cardinality: 39 in reports, 38 in index, 1 missing, 0 phantom, 0 severity mismatches`; BUILD FAILED rc=1 | 09 |
| P-05 | Register generator on shipped r27 index | reproduction | rc=0, zero warnings, 7 groups + 21 NOTED items | 05 |
| P-06 | Register generator on shipped r25 index (entry claim: "succeeds on r27 and r25") | landed-assertion | rc=0 | 10 |
| P-07 | Boundary list byte-comparison: `generate_boundary_list` vs entry text | exact-equality | byte-exact in both v0.71 and v0.72 entries | 11 |
| P-08 | Terminal-line census: `generate_terminal_line("0.72")` vs all 10 terminal lines in Section 27 | exact-equality | entries v0.63-v0.70 and v0.72 carry their own version's line; the v0.71 entry carries the v0.72 line; no v0.71-token line exists anywhere | 11 |
| P-09 | Terminal gate [10h]: delete the document-final terminal line from a copy (embedded v0.71-entry copy remains) | sabotage | gate [10h] prints `PASS: Terminal line matches v0.72 (draft candidate or FROZEN)`; build fails only on seal gates (stale HISTORY) | 12 |
| P-10 | P-09 + self-consistent HISTORY reseal (disclosed boundary-32 class) | sabotage+reseal | **BUILD PASSED rc=0 with NO document-final terminal line**; [10h] satisfied entirely by the entry-embedded duplicate | 13 |
| P-11 | Independent CI-8 recount (extractor over four R27 reports, filter 68, vs index) | reproduction | 39 / 39 / 0 missing / 0 phantom / 0 severity mismatches | 14 |
| P-12 | PRIOR_HISTORY chain reconstruction (auditor recipe, two levels) | recomputation | see Section 3; v0.72 embedded value matches nothing derivable | 06 |

No void probes. Controls fired where required (P-01 X-suffix, P-02 mutation).

## 6. FINDINGS

Namespace F-S01-72-NN (seat S01, version 72, serial). Class-to-severity per the v0.56 mapping (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL). String/position per the R28 six-string triage frame crossed with the shipped methodology's 24-position grid.

### F-S01-72-01 HIGH (Class A) -- Section 0.1 cardinal-range sentence internally impossible
- String 3 (cross-layer consistency), Position 9 (Section 0.1)
- Claim (protocol line 22): "The full defect trajectory is in Section 27 (seventy-two amendment entries, v0.1 through v0.71)."
- Evidence: HISTORY.sha256 carries exactly 72 ENTRY seals (v0.1 through v0.72 inclusive); the range "v0.1 through v0.71" spans 71 entries; 72 != 71. Gate [9e] cardinal-range check scopes to the current entry and to a "N consecutive ... (v0.X through v0.Y)" pattern; this sentence is in the body and outside the pattern, so it escapes.
- Falsifier: none available to the artifact -- the count and the range are both byte-derivable and mutually contradictory. Repair: "seventy-two amendment entries, v0.1 through v0.72" (and extend [9e]-class gating to the Section 0.1 range sentence).
- Recurrence: R13/R15/R17/R18 version-token class; R28 Group 5 required repair not discharged at this locus.

### F-S01-72-02 HIGH (Class A) -- Section 22.2 carried-entry bound still v0.68; gate [10i] satisfied by a different section's token
- String 3, Position 8 (status/consistency)
- Claim (protocol line 718, Section 22.2): "For carried entries (v0.1 through v0.68), the PRIOR_HISTORY derivation in build.py [9b] detects retroactive mutation ..."
- Evidence: at v0.72 the carried entries are v0.1 through v0.71. The bound is stale by four versions (v0.69, v0.70, v0.71, v0.72). R28 Group 5 (S02 F-S02-70-03, S04 F-S04-70-08) found this exact locus stale at v0.68 when it should have been v0.69; the disposition required "update all stale version tokens in the protocol body." Gate [10i] checks `expected_22_2 = f"v0.1 through {prior_ver}"` ("v0.1 through v0.71") with `in body` -- and passes on the Section 0.1 occurrence (line 22), not on the 22.2 locus it names. The gate manufactures green while its semantic target is red: the R28 Group 6 mechanism, live.
- Falsifier: quote the 22.2 sentence with bound v0.71+ on future bytes. Repair: update the 22.2 bound; scope [10i] to the 22.2 section text, not the whole body.

### F-S01-72-03 HIGH (Class A) -- FB-7b trajectory row terminates at R27; R28 absent
- String 3, Position 10 (FB-7b trajectory)
- Claim (Section 25 FB-7b row, protocol line 771): status "RESOLVED v0.31; PENDING RE-CARRY v0.72" with a per-round trajectory ending "... R27 (v0.68): 4 seats, all HALTed (gate 13 vacuous, Section 0.1 stale, FB-7b gap)."
- Evidence: the position-10 criterion is "row current through prior round"; the prior round is R28 (4/4 HALT on v0.70). No R28 entry exists in the trajectory. The row was last extended at the v0.69/v0.70 repair and not extended for R28, while the same row's status token was updated to v0.72 -- half-current.
- Falsifier: a row containing an R28 entry on future bytes. Repair: extend the trajectory through R28 (and make the row's last-round token gate-checkable).

### F-S01-72-04 HIGH (Class A) -- v0.72 entry's embedded PRIOR_HISTORY matches no derivable surface
- String 5 (temporal integrity), Position 16 (PRIOR_HISTORY)
- Claim (v0.72 entry, sealed): "PRIOR_HISTORY 01e0f76325cbabc43958d97f1a4ce013e755ed3edc00a28b89cf8435f4ca633c."
- Evidence (logs/06): the standing convention -- verified intact at the v0.71 entry, whose embedded value `2e41e745...` equals reconstruct(70) -- requires the v0.72 entry's embedded value to equal reconstruct(71) = `f88dd44e...` = the HISTORY.sha256 PRIOR line. It does not. `01e0f763...` equals nothing derivable from the shipped bytes. No shipped gate compares the entry-embedded PRIOR_HISTORY against the HISTORY line (the [9b] derivation consumes embedded values; it never checks the current entry's).
- Two readings, both defective: (a) the embedded value is simply wrong/narrated -- a byte-false provenance token in a sealed entry; (b) it is the sha256 of the genuine v0.71-build HISTORY -- which proves the v0.71 entry bytes shipped at v0.72 differ from the bytes the v0.71 build sealed (regeneration; see F-S01-72-05), an append-only breach at the v0.71 locus.
- Falsifier: produce held v0.71 bytes whose HISTORY hashes to `01e0f763...` AND whose v0.71 entry is byte-identical to the one sealed here. If the first conjunct holds and the second fails, reading (b) is confirmed and Bearer 1 falls at the v0.71 locus. Fresh seat holds nothing; this is the round's sharpest open enumeration.

### F-S01-72-05 HIGH (Class A) -- the sealed v0.71 entry terminates with a v0.72 line; "v0.71 entry is not edited" contradicted on the bytes
- String 5/String 3, Position 17/8
- Claims (v0.72 entry): "The withdrawal is recorded per the append-only rule; v0.71 entry is not edited."
- Evidence (log 11): every entry v0.63 through v0.72 terminates with its own version's generate_terminal_line output ("*End of XZ Protocol v0.NN draft candidate.*"). The v0.71 entry uniquely terminates with "*End of XZ Protocol v0.72 draft candidate.*" -- a token that cannot have been produced by a v0.71 build of generate_terminal_line, and whose "draft candidate" status contradicts the entry's own "FROZEN" headline. No "v0.71" terminal line exists anywhere in the document. Byte evidence: the v0.71 entry text as shipped was (re)generated during the v0.72 build.
- Falsifier: held v0.71 bytes containing this exact terminal line (which would relocate the defect to the v0.71 build itself rather than discharge it). The v0.71 seal verifies against the shipped bytes (seal integrity is not the finding; content provenance is).
- Note: this embedded duplicate is also the latent satisfier behind F-S01-72-07.

### F-S01-72-06 MEDIUM (Class B) -- gate [13] summary keeps a hardcoded "PASS:" label on the failure path
- String 1 (code), Position 3 (build gates)
- Evidence (log 09, sabotage copy: one findings[] record removed, sums resealed): the gate prints `FAIL: CI-8 missing from index: 1 (F-S01-68-01)` and then `PASS: CI-8 cardinality: 39 in reports, 38 in index, 1 missing, 0 phantom, 0 severity mismatches`. The v0.72 repair (3) made the values computed but left the summary line's PASS label unconditional -- a line labeled PASS describing a failing state. The overall build still fails (fail-closed intact); this is a false label in gate output, the R28 Group 3 narrated-label class at reduced blast radius.
- Falsifier: on the same sabotage, the summary line labeled from the conjunction of the three checks (or omitted on failure). Repair: emit the summary through check()-driven labeling.

### F-S01-72-07 MEDIUM (Class B) -- gate [10h] is substring-anywhere; the entry-embedded duplicate terminal line satisfies it with the true terminal line deleted
- String 4 (adversarial), Position 14 (format probe: strict match, not prefix/substring)
- Evidence (logs 12, 13): with the document-final terminal line deleted from a copy, [10h] prints PASS (satisfied by the v0.72-token copy embedded in the v0.71 entry); with HISTORY then resealed self-consistently (the disclosed boundary-32 adversary), BUILD PASSED rc=0 on a document with no terminal line at its end. Repair (6) landed (dual-token acceptance verified in source) but the gate binds neither position nor uniqueness of the terminal line.
- Falsifier: P-10's sabotage fails a future build. Repair: match the terminal line anchored at document end (post-Section-27 tail), and assert exactly one current-version terminal line in the document.
- Disclosure linkage: boundary 16 ("no gate checks FROZEN status token") and boundary 32 (self-consistent reseal) cover the general classes; the concrete satisfier-duplicate instance is new.

### F-S01-72-08 LOW (Class C) -- the v0.72 entry's build.py COMPUTED tags use a prose format that escapes gate [9c]; FINDING_ID_RE still dead code
- String 6 (methodology), Position 19 (tag accuracy/verifiability)
- Evidence (log 14): the entry carries 9 COMPUTED tags; zero match [9c]'s validation regex `\[COMPUTED:\s*build\.py\s*\[...\]`; the three build.py-referencing tags are written "[COMPUTED: build.py gate 13]" (x2) and "[COMPUTED: build.py gate 10h]" -- so no per-section validation fired (the build log shows no "COMPUTED tag references existing build.py section" lines this round). The tags are substantively accurate -- all nine were mutation- or execution-verified by this seat -- but the gate built to validate them is blind to the format used. Additionally, extract_findings.py line 26 retains FINDING_ID_RE defined-but-unused; the R28 Group 1 disposition's second half ("delete or wire in FINDING_ID_RE") was not executed.
- Falsifier: a future entry whose every build.py COMPUTED tag produces a [9c] per-section PASS line. Repair: normalize the tag format or widen [9c] to the prose form; delete or wire FINDING_ID_RE.

### F-S01-72-09 LOW (Class C) -- untagged-sentence residuals in the v0.72 entry
- String 6, Position 18 (tagging completeness)
- Evidence: the register header "R27 defect register disposition (from R27 4-seat round, all 7 convergence groups CLOSED): carried from v0.70. [ASSERTED]" is tagged, but the seven carried register items carry no per-item tags (the generator emits per-item [COMPUTED: generate_register]; the carried text drops them); the "v0.72 repairs (...)" header line is untagged; the opening paragraph runs multiple claim-sentences under one [ASSERTED]. Position-18's strict criterion ("zero untagged sentences") is not met. This is the disclosed F-OP20-03 class (gates do not detect untagged claims; divides-by-tags-not-claims).
- Falsifier: a future entry with per-sentence or per-item tags throughout. Severity LOW: the untagged spans sit under paragraph-level tags and no false claim was found inside them.

### F-S01-72-10 LOW (Class C) -- AUDIT_CONTEXT "33/33 OK" is false of the shipped manifest
- String 6, Position 20 (dispatch fidelity)
- Evidence: AUDIT_CONTEXT "Build status (tool-derived)" claims `sha256sum -c PACKET_SHA256SUMS: 33/33 OK`; the shipped PACKET_SHA256SUMS has 32 members and returns 32/32 OK (log 01). A narrated count in a section labeled tool-derived. Locus is the dispatch file, not the sealed protocol; classified LOW and String 6 accordingly.
- Falsifier: a manifest line-count matching the claimed figure. Repair: derive the count with `wc -l` at context-authoring time.

### F-S01-72-11 INFORMATIONAL (Class E) -- R28 report shipment: five files, one byte-identical duplicate; no R28 index; gate [13] never reads an R28 report
- Evidence: the packet ships SHIPPED_R28_S01..S04_REPORT.md (4 files, per repair claim (5) -- TRUE as claimed) plus XZ_v070_R28_S01_REPORT.md; `cmp` shows SHIPPED_R28_S01_REPORT.md and XZ_v070_R28_S01_REPORT.md are byte-identical duplicates under two names. Gate [13] globs `f.startswith("R") and f.endswith("_REPORT.md")` -- only R27_* match; the R28 reports participate in no cardinality check, and no r28_findings_index.json ships, so the R28 findings the v0.72 repairs close are unindexed and ungated.
- Note: the duplicate is harmless to the sums (all five manifested) but is manifest-hygiene noise; the unindexed R28 round means the next version's register has no R28 machine-readable source in this packet.

### F-S01-72-12 INFORMATIONAL (Class E) -- methodology identity: v7 invoked, v6 shipped
- Evidence: the Status line and the v0.72 entry invoke "Methodology: v7 canonical (six strings)"; AUDIT_CONTEXT names "Six Strings, Twenty-One Positions (v7)"; the shipped METHODOLOGY.txt self-describes as the successor of v5 ("v6 retains the insight ..."), seven layers, twenty-four positions, and contains no "string" vocabulary. The operative v7 framework (under which R28/R29 findings are string-classified) is not in the packet. Boundary 10 (packet non-closure) is the disclosed general class; the concrete version mismatch is recorded for the dispatch author.
- Consequence for this report: string labels follow the R28 triage frame; position labels follow the shipped 24-position grid. Both are cited so the triage can re-map.

## 7. PROVENANCE LEDGER (v0.72 entry)

| Tag | Count | Verification |
|---|---|---|
| COMPUTED | 9 | all nine executed or mutation-verified by this seat: extract_findings.py (P-01/P-02), build.py gate 13 x2 (P-03/P-04), xz_protocol_register_gen.py (P-05/P-06), sha256sum (log 01), build.py gate 10h (source + P-09/P-10), xz_protocol_boundaries.json (`"version": "0.72"` on bytes), generate_boundary_list (byte-exact, P-07), generate_terminal_line (P-08) |
| ASSERTED | 2 | header paragraph; carried-register header -- the carried register was verified field-by-field against the shipped index (7 groups, IDs, severities, surfaces all match; ordering differs from generator output, honestly scoped as "carried"/ASSERTED) |
| DISCLOSED | 2 | the Goedel sentence (x2) |
| EXTERNAL | 0 | -- |
| ENUMERATED | 1 | boundary list, 35 items -- recomputed from boundaries.json (count 35, `"count": 35` field consistent) |
| Gate-reported ASSERTED fraction | 2/11 = 18.2% of tagged claims | reproduction of gate arithmetic; F-OP20-03 disclosure applies (denominator is tags, not claims; DISCLOSED excluded) |

Zero substantively false COMPUTED tags found -- the first round this seat is aware of where every COMPUTED tag survived mutation verification. The tagging-layer defects that remain are format/coverage defects (F-S01-72-08, F-S01-72-09), not truth-value defects.

## 8. COVERAGE, HEDGES, BOUNDARY REPORT (D-3.3 / D-3.6 / D-3.8)

- Gate-reported coverage (log 02): body in-scope 108005 chars (22.7%); Section 27 ungated 367413 chars (77.3%); semantic-gate coverage 29.9% of body. The ungated share is the larger one and grew with the second R28-era entry; stated as measurement, not defect (v0.20 NOTED class).
- Hedge/deferral audit: the v0.72 entry defers exactly two items honestly -- register wiring ("partially ... register still not wired into build.py") and the item-7/furqan governance call. No hedge found masquerading as closure; the reverse defect was found (closure language -- "v0.71 entry is not edited" -- over regenerated bytes, F-S01-72-05).
- Outermost uncomputed layer (D-3.8): the v0.71-byte provenance question (F-S01-72-04/05). Everything internal to the v0.72 packet recomputes clean; the divergence is only adjudicable against HELD v0.71 bytes, which a fresh seat does not have. What would bring it inside: shipping the v0.71 packet (or its HISTORY.sha256 plus the v0.71 entry bytes) in the R30 dispatch, or a carrying seat that holds v0.71 bytes anchoring PRIOR_HISTORY externally. Until then the v0.71 locus sits at Layer 5, outside internal computation.
- PRIOR_HISTORY anchor: not possible (fresh seat); stated, not skipped.

## 9. D-7 (four one-line answers)

1. What was verified: every seal surface, both baseline suites, all seven repair claims, and every COMPUTED tag -- on unmodified canonical bytes, with sabotage confined to resealed copies.
2. What was falsified: the Section 0.1 entry-range sentence, the 22.2 carried-entry bound currency, FB-7b row currency, the v0.72 entry's embedded PRIOR_HISTORY, and the "v0.71 entry is not edited" claim.
3. What was not reachable: external anchoring of PRIOR_HISTORY and the v0.71-entry content question (no held bytes); cross-witness convergence (single-seat round).
4. What the next round must re-run: P-03, P-04, P-09/P-10 (gate failure-path and terminal-anchor probes), the [9c] tag-format census, and the F-S01-72-04 falsifier against any held v0.71 bytes.

## 10. BEARER TABLE (leaving R29)

| Bearer | Status | Evidence |
|---|---|---|
| 1. Append-only | UNKNOWN at the v0.71 locus (TRUE internally) | 72/72 seals + FULL + derivation all recompute OK; F-S01-72-04/05 open the v0.71-content question only held bytes can close |
| 2. Code correctness | TRUE with findings | 186 GREEN, build rc=0; F-S01-72-06/07 are gate-output/gate-semantics defects, not suite failures |
| 3. Surface narrowing | FALSE | the R22-R27 code-layer clean streak does not extend: R29 Class A at String 3 (prose tokens) and String 5 (temporal), plus gate-layer Class B |
| 4. Goedel confinement | FALSE | Class A at Strings 3 and 5; not confined to String 6 |
| 5. Cross-vendor witness | FALSE | this carrying seat HALTs; no carrying non-HALT since v0.31 stands |
| 6. Axiom disclosure | TRUE | Section 22.4 present, A-X1..A-X5 and Sidrat clause verified on bytes |
| 7. Methodology | FALSE | tagging format/coverage defects (F-S01-72-08/09); methodology-version mismatch (F-S01-72-12) |
| 8. The furqan | UNKNOWN | lead's call |

## 11. VERDICT, REPAIRS, AND RE-AUDIT CONDITIONS

Severity totals: HIGH 5 (F-S01-72-01..05), MEDIUM 2 (06, 07), LOW 3 (08, 09, 10), INFORMATIONAL 2 (11, 12). Class A: 5. Class A recurrence extends to R7-R29: 23/23; H = 1.0; Laplace P(Class A at R30) = 24/25 = 0.96.

**VERDICT: HALT (binding, carrying seat S01).** v0.72 does not close the R28 defects: Group 5 is undischarged at three live loci, and the v0.71 withdrawal/regeneration surface introduces two new Class A findings at the temporal string. Confinement is not achieved; the defect is not yet at the tagging surface alone.

Required repairs for v0.73 (minimum):
1. Section 0.1 range sentence -> "v0.1 through v0.72" (and gate the body range sentence, not only the entry's).
2. Section 22.2 carried-entry bound -> current; scope gate [10i] to the 22.2 locus text.
3. FB-7b row: append the R28 line.
4. v0.72-entry embedded PRIOR_HISTORY: state the correct value by append-only correction at v0.73 (the v0.72 entry is sealed; do not edit it); disclose what `01e0f763...` actually hashes.
5. v0.71-entry terminal line: append-only correction disclosing the regeneration; ship the genuine v0.71 terminal state or the held v0.71 bytes so carrying seats can anchor.
6. Gate [13] summary: label from the checks' conjunction, or print the summary only on the success path.
7. Gate [10h]: anchor the terminal-line match to the document tail and assert uniqueness of the current-version terminal line.
8. Normalize COMPUTED-tag format (or widen [9c]); delete or wire in extract_findings.py FINDING_ID_RE.
9. AUDIT_CONTEXT counts: tool-derive the manifest member count.

Re-audit conditions for R30: re-run probes P-01..P-04 and P-09/P-10 on the new bytes; re-run the [9c] census; re-run the two-level PRIOR_HISTORY reconstruction; anchor PRIOR_HISTORY externally if any seat holds v0.71/v0.72 bytes; verify the F-S01-72-04 falsifier explicitly.

## 12. SELF-CORRECTIONS LEDGER

This seat's first round; no prior over-reaches to correct. One in-round self-correction: an import probe created `__pycache__/` inside the packet dir (an auditor-side hygiene lapse, not a byte modification); it was removed and `sha256sum -c` re-verified 32/32 OK before any finding was scored. An early read of the register-ordering question (entry vs generator item order) was resolved against the index before scoring: the entry's group_id ordering is consistent with the index; no finding was filed on it.

Final integrity re-check after all probing and report assembly: `sha256sum -c PACKET_SHA256SUMS` = 32/32 OK, 0 FAILED; standing values unchanged (FULL_SECTION_27 `15f64e55...`, manifest `a48c2912...`, HISTORY PRIOR `f88dd44e...`).

---

*"The foam vanishes. What benefits the people remains in the earth."*

######_REPORT_SPLIT_######
# Source: SHIPPED_R29_S02_ASSESSMENT.md
# v0.72 Defect Closure Assessment

**No, v0.72 does not close all of the R28 defects.**

The v0.72 release withdraws the `FROZEN` status, reverts to `DRAFT CANDIDATE`, and successfully lands exactly seven prescribed repairs. These repairs resolve several critical and high-severity issues located in the `String 1` (Code Execution) and `String 2` (Register Verification) surfaces:
*   Adding the `C`-suffix to all five `DECLARATION_PATTERNS` successfully addresses the phantom repair defect identified across multiple seats (`F-S04-70-01`, `F-S02-70-02`, and `F-S03-70-02`).
*   Reconfiguring Gate `[13]` to be fail-closed—by using `check(False, ...)` instead of `print` in the `else` branch—closes the skip-as-green vacuity failure (`F-S02-70-01`, `F-S03-70-01`, `F-S04-70-03`).
*   Deriving the Gate `[13]` summary from computed variables rather than hardcoded zeros closes the narrated-summary defects (`F-S02-70-06`, `F-S04-70-02`).
*   Implementing graceful degradation in the register generator (including `CRITICAL` severity validation) addresses the index crashing defect (`F-S01-70-01`, `F-S04-70-04`).
*   Shipping all R28 reports in-packet, updating the `boundaries.json` version, and adjusting the terminal-line gate to accept "draft candidate" resolves the associated manifest and version-staleness limitations (`F-S04-70-11`, `F-S04-70-13`).

**However, v0.72 leaves multiple critical Class A defects entirely unresolved:**
*   **String 3 (Cross-Layer Consistency):** Section 0.1 still carries an internally impossible and stale entry range ("v0.1 through v0.69"). Furthermore, the front-matter Status line falsely attributes the R27 audit to v0.69 instead of v0.68.
*   **String 4 (Adversarial Probing):** Gates `[10i]` and `[2f]` remain locus-blind and structurally enforce byte-false claims. A user who substitutes the true values into the document will break the build, meaning the verification layer is actively manufacturing the defects it is meant to detect.
*   **String 6 (Methodology Audit):** Issues such as pattern 4 over-capture (`F-S01-70-05`) and dispatch fidelity mismatches (`F-S01-70-09`) remain untargeted by the seven landed repairs.

---

## R28 Findings Classification by String and Position

Below is the classification of every finding generated by the four auditing seats during the R28 audit on v0.70 bytes.

| Finding ID | Seat | String | Position | Severity / Class |
| :--- | :--- | :--- | :--- | :--- |
| `F-S01-70-01` | S01 | 2 (Register Verification) | 4 | HIGH (Class A) |
| `F-S01-70-02` | S01 | 6 (Methodology Audit) | 19 | HIGH (Class A) |
| `F-S01-70-03` | S01 | 6 (Methodology Audit) | 19 | HIGH (Class A) |
| `F-S01-70-04` | S01 | 6 (Methodology Audit) | 19 | HIGH (Class A) |
| `F-S01-70-05` | S01 | 6 (Methodology Audit)* | 19 | MEDIUM (Class A) |
| `F-S01-70-06` | S01 | 1 (Code Execution) | 3 | LOW (Class D) |
| `F-S01-70-07` | S01 | 6 (Methodology Audit) | 18 | LOW (Class D) |
| `F-S01-70-08` | S01 | 6 (Methodology Audit) | 20 | LOW (Class E) |
| `F-S01-70-09` | S01 | 6 (Methodology Audit) | 20 | HIGH (Class A) |
| `F-S02-70-01` | S02 | 1 (Code Execution) | 3 | HIGH (Class A) |
| `F-S02-70-02` | S02 | 2 (Register Verification) | 5 | HIGH (Class A) |
| `F-S02-70-03` | S02 | 3 (Cross-Layer Consistency) | 9 | HIGH (Class A) |
| `F-S02-70-04` | S02 | 3 (Cross-Layer Consistency) | 8 | HIGH (Class A) |
| `F-S02-70-05` | S02 | 1 (Code Execution) | 1 | HIGH (Class A) |
| `F-S02-70-06` | S02 | 4 (Adversarial Probing) | 12 | MEDIUM (Class B) |
| `F-S02-70-07` | S02 | 6 (Methodology Audit) | 18 | LOW (Class C) |
| `F-S02-70-08` | S02 | 6 (Methodology Audit) | 20 | INFORMATIONAL (Class E) |
| `F-S03-70-01` | S03 | 1 (Code Execution) | 3 | HIGH (Class A) |
| `F-S03-70-02` | S03 | 4 (Adversarial Probing) | 14 | HIGH (Class A) |
| `F-S04-70-01` | S04 | 1 (Code Execution) | 2 | CRITICAL (Class A) |
| `F-S04-70-02` | S04 | 1 (Code Execution) | 3 | HIGH (Class A) |
| `F-S04-70-03` | S04 | 2 (Register Verification) | 4 | HIGH (Class A) |
| `F-S04-70-04` | S04 | 2 (Register Verification) | 5 | HIGH (Class A) |
| `F-S04-70-05` | S04 | 2 (Register Verification) | 6 | HIGH (Class A) |
| `F-S04-70-06` | S04 | 3 (Cross-Layer Consistency) | 8 | HIGH (Class A) |
| `F-S04-70-07` | S04 | 3 (Cross-Layer Consistency) | 7 | HIGH (Class A) |
| `F-S04-70-08` | S04 | 3 (Cross-Layer Consistency) | 9 | HIGH (Class A) |
| `F-S04-70-09` | S04 | 4 (Adversarial Probing) | 11 | HIGH (Class D) |
| `F-S04-70-10` | S04 | 4 (Adversarial Probing) | 12 | HIGH (Class D) |
| `F-S04-70-11` | S04 | 5 (Temporal Integrity) | 16 | HIGH (Class D) |
| `F-S04-70-12` | S04 | 1 (Code Execution) | 1 | MEDIUM (Class D) |
| `F-S04-70-13` | S04 | 2 (Register Verification) | 6 | MEDIUM (Class E) |
| `F-S04-70-14` | S04 | 6 (Methodology Audit) | 18 | LOW (Class C) |
| `F-S04-70-15` | S04 | 1 (Code Execution) | 1 | LOW (Class E) |
| `F-S04-70-16` | S04 | 6 (Methodology Audit) | 21 | INFORMATIONAL (Class E) |
| `F-S04-70-17` | S04 | 1 (Code Execution) | 1 | INFORMATIONAL (Class E) |
| `F-S04-70-18` | S04 | 1 (Code Execution) | 1 | INFORMATIONAL (Class C) |

*\*Note: Seat S01 explicitly defines `F-S01-70-05` as primarily String 6, Position 19, with a latent resonance at String 4, Position 14.*

######_REPORT_SPLIT_######
# Source: SHIPPED_R29_S03_REPORT.md
# XZ Protocol v0.72 — Round 29 Audit Report — Seat S03

**Seat:** S03 (FRESH)
**Model:** GPT-5.6 Sol
**Role:** ADVERSARIAL ADVISORY
**Round:** R29
**Target:** XZ Protocol v0.72 bytes
**Date:** 2026-08-17
**Producer:** Claude Opus 4.6 — BARRED from carrying or auditing
**Dispatch output:** `XZ_v072_R29_S03_REPORT.md`

**VERDICT: HALT.**

v0.72 is materially better than v0.70/v0.71: the C-suffix extractor repair is real; Gate [13] is now fail-closed; its summary is computed; the R28 reports are present and manifested; the terminal gate accepts both DRAFT CANDIDATE and FROZEN tokens; and `xz_protocol_boundaries.json` is stamped `0.72`. The register repair also succeeds on the specifically claimed R25 and R27 indexes.

Those repairs do **not** close the R28/peer-review defect set. Current v0.72 bytes still contain multiple Class A claims outside the self-referential methodology surface, including an incorrect `33/33` checksum summary, the unreconciled six-string/21-position versus seven-layer/24-position methodology contradiction, false R28 provenance in the Status line, an impossible Section 0.1 version range, a four-version-stale Section 22.2 bound that Gate [10i] falsely passes, an incomplete FB-7b “full trajectory,” and false source-frame/control-graph test counts. The terminal-tail and R28-index coverage weaknesses also remain reproducible as disclosed gate limitations.

Therefore **Goedel confinement is not achieved at v0.72. Bearer 4 = FALSE.** Because this is an advisory GPT seat, this report does not supply carrying credit; Bearer 5 remains FALSE/PENDING under the protocol's own carry rules.

Bismillah.

---

## S-0. Fresh-seat declaration and coordinate caveat

The dispatch requires a FRESH S03 execution. I used only the supplied R29 materials and the deserialized v0.72 executable packet. I held no prior protocol bytes for an external append-only comparison.

There is a load-bearing coordinate conflict in the shipment itself:

- `AUDIT_CONTEXT.txt` and the v0.72 Status line call the governing method **v7, Six Strings, Twenty-One Positions**.
- `METHODOLOGY.txt` calls itself canonical for R28 onward and defines **Seven Layers, Twenty-Four Positions**.

Because the dispatch asks that findings be classified by string and position, this report provisionally uses the six-string / positions 1–21 convention used by R28, while recording the contradictory canonical methodology as a Class A finding. The provisional mapping is:

| String | Surface | Positions |
|---|---|---:|
| 1 | Code Execution | 1–3 |
| 2 | Register Verification | 4–6 |
| 3 | Cross-Layer Consistency | 7–10 |
| 4 | Adversarial Probing | 11–14 |
| 5 | Temporal Integrity | 15–17 |
| 6 | Methodology Audit | 18–21 |

The shipped `METHODOLOGY.txt` then adds Layer 7 / positions 22–24. That contradiction is not normalized away in this report.

---

## S-1. Byte identity and baseline execution

### S-1.1 Packet extraction and top-level parity

The dispatch splitter was applied byte-for-byte to `EXECUTABLE_PACKET.txt`.

- Serialized packet members: **33**
- `PROTOCOL(4).txt` = extracted `xz_protocol_v0_72.md`: **byte-identical**
- `FINDINGS_INDEX.txt` = extracted `r27_findings_index.json`: **byte-identical**
- `BOUNDARIES.txt` = extracted `xz_protocol_boundaries.json`: **byte-identical**

Selected SHA-256 identities:

| Artifact | SHA-256 |
|---|---|
| `xz_protocol_v0_72.md` | `a83b0162a605d99c05ce67f4ddd55a5a7b3f64819fcaee744e433c52c045c424` |
| `PACKET_SHA256SUMS` | `50f8c3a0e6480e2d70b45221b9dcc90080e46a9f37ef4a93297467a0eb011de6` |
| `build.py` | `d3587f9aa5a497c3872238ba917f302d59c26e737e23ae1d9761ad6e197fc9fc` |
| `extract_findings.py` | `e461fba3436ff193427f944f59d9b71bd5a86b3116dc8415bdf3847c0415e147` |
| `xz_protocol_register_gen.py` | `66a14c0139eefb3ad90bf117c9b348ccaa107ff6da9be262f2edd351614e3a52` |
| `r27_findings_index.json` | `b345f98ba63e8a189324cc81212cd546414ce76033243abb0eec8828fc2ab439` |
| `xz_protocol_boundaries.json` | `530eaa697eafc228402dc498a40b188cb0c17f35162383ea455ec67793366010` |

### S-1.2 Four-scribe baseline

Executed in the extracted packet directory:

```text
sha256sum -c PACKET_SHA256SUMS
=> rc=0; 32 :OK lines

python3 build.py
=> BUILD PASSED: all checks GREEN

python3 -m pytest \
  test_xz_protocol_kernel.py \
  test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py \
  test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py \
  xz_protocol_phase_a_tests.py
=> 186 passed in 5.04s
```

`build.py` independently reports 72 Section 27 entries and verifies all 72 internal entry seals. Gate [13] reports 39 report findings ↔ 39 R27-index findings, 0 missing, 0 phantom, 0 severity mismatches.

The environment used Python 3.13.5 on Linux 6.18.35 x86_64. No environmental failure is counted against the packet.

**Important:** the green baseline is real. The HALT below is not a claim that `build.py` or pytest returned red. It is a finding that green gates coexist with current byte-false claims and false-positive verification paths.

---

## S-2. R28 repair-discharge matrix

| R28 surface | v0.72 result | R29 assessment |
|---|---|---|
| Group 1 — C-suffix blind in `DECLARATION_PATTERNS` | All five operative patterns now include `C?`; `F-S01C-70-99` heading probe extracts correctly | **DISCHARGED** |
| Group 2 — Gate [13] skip-as-green | Else branch now calls `check(False, ...)` | **DISCHARGED** |
| Group 3 — Gate [13] hardcoded-zero summary | Summary now uses `len(missing_from_index)`, `len(phantom_in_index)`, `len(sev_mismatches)` | **DISCHARGED** |
| Group 4 — register reproduction failure | R25 and R27 indexes now generate; R18 and R19 still crash; generator still not wired into `build.py` | **PARTIAL / OPEN** |
| Group 5 — version/status staleness | Section 0.1 range remains false; Section 22.2 remains at v0.68; Status provenance names v0.71 as the R28 audit target | **OPEN, Class A** |
| Group 6 — gates [2f]/[10i] enforce false semantics | [2f] still enforces VERSION−1 rather than actual audited version; [10i] remains locus-blind | **OPEN, Class A** |

### Peer-review repair claims in the v0.72 entry

| v0.72 repair claim | Result |
|---|---|
| R28 reports shipped and manifested | **TRUE** for all four unique seats; a duplicate S01 copy also ships |
| terminal gate accepts DRAFT CANDIDATE or FROZEN | **TRUE, narrowly**; final-line uniqueness/unsealed-tail defect remains |
| boundaries version 0.62 → 0.72 | **TRUE** |
| FROZEN withdrawn, status DRAFT CANDIDATE | **TRUE** |

The central distinction is therefore: **the seven local patches largely landed, but the packet did not close the full defect set that made v0.70/v0.71 unfit for FROZEN.**

---

## S-3. Findings

### F-S03-72-01 — HIGH — Class A — String 1, Position 1

**Surface:** Packet-integrity summary / checksum cardinality.
**Locus:** `AUDIT_CONTEXT.txt` Build status; `PACKET_SHA256SUMS`; serialized packet inventory.

**Claim:** `AUDIT_CONTEXT.txt` states:

```text
sha256sum -c PACKET_SHA256SUMS: 33/33 OK
```

**Observed:** The serialized packet contains **33 members total**, but `PACKET_SHA256SUMS` contains **32** checksum entries and intentionally does not list itself. Executing `sha256sum -c PACKET_SHA256SUMS` produces **32** `: OK` lines, not 33.

The intentional self-exclusion may be a disclosed packet-closure boundary. It does not make `33/33` true. The correct mechanical statement is `32/32 manifested payload members OK`, with the manifest itself excluded, or equivalent.

**Classification rationale:** A current numerical claim about scribe output is false on the supplied bytes. This is Class A and lies outside String 6.

**Required repair:** Derive the displayed checksum cardinality from the manifest lines actually consumed by `sha256sum`, and state the manifest-self exception explicitly.

**Falsifier:** `grep -Ec '^[0-9a-f]{64}  ' PACKET_SHA256SUMS` and the number of `: OK` lines equal the number narrated in `AUDIT_CONTEXT.txt`.

---

### F-S03-72-02 — HIGH — Class A — String 3, Position 8; resonance String 6, Position 20

**Surface:** Governing methodology identity / coordinate system.
**Lineage:** Recurrence of the R28 methodology-architecture finding and peer-review F-PR71-16.

**Current contradiction:**

- `AUDIT_CONTEXT.txt`: “Structural Honesty Verification — Six Strings, Twenty-One Positions (v7).”
- v0.72 Status line: “Methodology: v7 canonical (six strings).”
- `METHODOLOGY.txt`: “Seven Heavens. Seven Earths. Twenty-Four Verification Positions” and “canonical methodology for all rounds from R28 onward.”
- The same methodology's Section 6 explicitly defines positions 22–24, while its Bearer 4 row still says confinement is positions 18–21 only.
- Its Section 15 is stale enough to ask whether **v0.69** achieves confinement at **R28**, although R28 actually audited v0.70.

These are not alternate descriptions that can simultaneously be true: the shipment declares incompatible architecture, position count, canonical-version semantics, and R28 target semantics.

**Classification rationale:** The v0.72 Status line claims one canonical methodology while the shipped canonical methodology defines another. Class A, primary String 3 / Position 8; it also resonates at dispatch/methodology fidelity.

**Required repair:** Select one canonical architecture and propagate its version, layer/string count, position count, Bearer 4 region, and target round/version across `METHODOLOGY.txt`, `AUDIT_CONTEXT.txt`, `CI_METHODOLOGY.txt`, protocol Status, and dispatch generation. Add a deterministic parity gate over those tokens.

**Falsifier:** All supplied methodology surfaces parse to exactly one methodology version, one architecture, one position count, and one R29 target version.

---

### F-S03-72-03 — HIGH — Class A — String 3, Position 8; mechanism at String 4, Position 11/12

**Surface:** Status-line provenance.
**Lineage:** Recurrence of R28 Group 6's VERSION−1/provenance semantic defect.

The v0.72 Status line says:

```text
repair build from v0.71 R28 audit
```

But R28 audited **v0.70**. v0.71 was the successor FROZEN declaration later withdrawn after peer review. `build.py` gate [2f] does not validate the actual audited-version relationship. It hardcodes the rule that the provenance version must equal `VERSION - 1`; at v0.72 that forces v0.71 and therefore manufactures the wrong historical attribution.

This is the exact semantic class identified in R28 Group 6: an arithmetic version convention substitutes for the actual round→audited-version relation.

**Classification rationale:** The Status line's R28 provenance is false, and a gate positively enforces the false value. Class A at Position 8, with an adversarial-validation mechanism failure.

**Required repair:** Source the prior audited version from a round/index/triage record, not from `VERSION - 1`. Gate the pair `(round, audited_version)`.

**Falsifier:** Status says R28 audited v0.70; changing it to v0.71 causes the provenance gate to fail.

---

### F-S03-72-04 — HIGH — Class A — String 3, Position 9

**Surface:** Section 0.1 amendment count/range.
**Lineage:** Recurrence of R28 Group 5 and peer-review F-PR71-08.

Section 0.1 says:

```text
seventy-two amendment entries, v0.1 through v0.71
```

`build.py` parses and verifies **72** entries. The current v0.72 entry is one of them. A range v0.1 through v0.71 contains 71 numbered version entries and excludes v0.72.

The count is right; the range is wrong.

**Classification rationale:** Direct byte-false current-body claim. Class A, String 3 / Position 9.

**Required repair:** State `seventy-two amendment entries, v0.1 through v0.72`, or explicitly distinguish 71 prior entries plus the current v0.72 entry. Gate both count and terminal version at the exact Section 0.1 locus.

**Falsifier:** Parsed Section 27 entry count and Section 0.1 range cardinality/end-point agree exactly.

---

### F-S03-72-05 — HIGH — Class A with Class-D mechanism — String 4, Position 12; resonance String 3, Position 9

**Surface:** Gate [10i] Section 22.2 bound validation.
**Lineage:** Recurrence of R28 Group 6 and peer-review F-PR71-07/F-PR71-09.

Section 22.2 on the current v0.72 bytes still says:

```text
For carried entries (v0.1 through v0.68) ...
```

Yet Gate [10i] computes:

```python
prior_ver = "v0.71"
expected_22_2 = "v0.1 through v0.71"
check(expected_22_2 in body, ...)
```

The check passes because the false **Section 0.1** sentence contains `v0.1 through v0.71`. It does not inspect Section 22.2. Thus:

1. Section 22.2 is four numbered versions behind the gate's own expected endpoint.
2. Gate [10i] reports PASS anyway.
3. The wrong Section 0.1 token is load-bearing for that false PASS.

**Classification rationale:** The current body contains a false bound (Class A), and the parity gate is locus-blind (Class D mechanism). This is outside the self-referential String 6 surface.

**Required repair:** Parse the Section 22.2 locus and compare its bound directly with the actual carried/audited lineage. Do not use body-wide substring presence.

**Falsifier:** Section 22.2 itself contains the intended bound; moving the same token elsewhere in the body does not satisfy Gate [10i].

---

### F-S03-72-06 — HIGH — Class A — String 3, Position 10

**Surface:** FB-7b single-source-of-truth trajectory.
**Lineage:** Recurrence of peer-review F-PR71-03.

Section 0.1 says the Section 25 FB-7b row contains the **full carrying-seat trajectory** and is the single source of truth. The current FB-7b row correctly changes the pending token to `PENDING RE-CARRY v0.72`, but its enumerated trajectory still terminates at:

```text
R27 (v0.68): 4 seats, all HALTed ...
```

The row contains **zero `R28` tokens**. R28's four HALTs on v0.70 — the immediate evidentiary basis for v0.72 — are omitted from the claimed full trajectory.

**Classification rationale:** The pending state is honest; the “full trajectory” claim is not. Class A, String 3 / Position 10.

**Required repair:** Extend the Section 25 FB-7b trajectory through R28/v0.70 and then R29 as appropriate, preserving actual executor/role eligibility rather than dispatch-label assumptions.

**Falsifier:** Section 25's FB-7b row contains the complete R28 event and agrees with the shipped R28 reports/triage.

---

### F-S03-72-07 — HIGH — Class A — String 1, Position 2

**Surface:** Section 25 test-suite component counts.
**Lineage:** Explicitly identified in the v0.71 peer review and left unchanged in v0.72.

Current Section 25 claims:

- FB-4: **22 source-frame tests**
- FB-5: **30 control-graph tests**

The executed current suites contain:

- Condition A: 29
- Source frame: **29**
- Control graph: **18**
- Kernel: 14
- Adversarial: 27
- Phase A: 69
- Total: **186**

The total `186` is correct. Two named component claims are false.

**Classification rationale:** These are finite claims about the current executable test substrate and are contradicted by direct execution/collection. Class A, String 1 / Position 2.

**Required repair:** Regenerate Section 25 component counts from pytest collection or another deterministic source. Do not preserve obsolete component counts merely because the total still sums correctly elsewhere.

**Falsifier:** Section 25 counts equal the collected tests in each corresponding suite.

---

### F-S03-72-08 — MEDIUM — Class D — String 2, Position 4; resonance String 6, Position 19

**Surface:** Register reproduction / CI-1R completeness.
**Lineage:** R28 Group 4; peer-review F-PR71-06.

The v0.72 repair claim is narrowly true:

```text
Generator now succeeds on r27 and r25 indexes.
```

Executed:

| Index | Generator result |
|---|---|
| `r18_findings_index.json` | **CRASH** (`ValueError`, adjudication receipt mismatch) |
| `r19_findings_index.json` | **CRASH** (`ValueError`, adjudication receipt mismatch) |
| `r25_findings_index.json` | rc=0 |
| `r27_findings_index.json` | rc=0 |

The repair therefore reduces the failure scope but does not establish the methodology's Position-4 criterion (“Generated register = shipped register (byte-exact)”) across the shipped historical register inputs. `build.py` still contains no CI-1R gate that invokes the generator and compares generated register text byte-exactly.

Because the v0.72 entry explicitly says the closure is partial and admits that the generator is not wired into `build.py`, I classify the remaining current condition as **Class D**, not as a new Class A repair-claim falsehood.

**Required repair:** Make the generator total over every supported shipped index schema, and add a build gate that reproduces the relevant register region byte-exactly.

**Falsifier:** Every supported shipped index generates without crash and the current register comparison gate fails on any one-byte divergence.

---

### F-S03-72-09 — MEDIUM — Class D — String 4, Position 14; resonance String 3, Position 8

**Surface:** Terminal-line uniqueness / unsealed tail.
**Lineage:** Peer-review F-PR71-15. The v0.72 repair closes F-PR71-14 only.

The current protocol contains **three** occurrences of the v0.72 draft-candidate terminal marker. Gate [10h] is only:

```python
terminal_ok = terminal_expected_dc in protocol or terminal_expected_fr in protocol
```

It tests global presence, not uniqueness or the actual last visible line.

Executed mutation probe on a copy:

1. Replace **only the final visible line** with:
   `*End of XZ Protocol v0.42 FROZEN -- audited by nobody.*`
2. Recompute only the protocol line in `PACKET_SHA256SUMS`.
3. Run `sha256sum -c` and `python3 build.py`.

Result:

```text
[10h] Terminal-version stamp
  PASS: Terminal line matches v0.72 (draft candidate or FROZEN)
...
BUILD PASSED: all checks GREEN
```

The final-line mutation lies after the provenance/seal terminus, so the internal entry/FULL_SECTION_27 seals remain green. v0.72 correctly makes [10h] dual-token; it does **not** repair final-marker uniqueness or EOF sealing.

This is disclosed by the shipped peer-review record and the standing “seal terminus at Provenance marker” boundary, so it is classified Class D here rather than concealed Class B.

**Required repair:** Require exactly one terminal marker at EOF and bind it to the current status; preferably extend the seal to EOF.

**Falsifier:** Any alteration of the final visible terminal line fails without being rescued by an earlier duplicate marker.

---

### F-S03-72-10 — MEDIUM — Class D — String 2, Positions 5–6

**Surface:** R28 report/index coverage at Gate [13].
**Lineage:** Peer-review F-PR71-18, partially changed by v0.72 report inclusion.

v0.72 ships all four unique R28 reports and manifests them. That repairs file presence. But there is still **no `r28_findings_index.json`**, and Gate [13] selects only filenames satisfying:

```python
f.startswith("R") and f.endswith("_REPORT.md")
```

The R28 files are named `SHIPPED_R28_...` (plus one duplicate `XZ_v070_R28_S01_REPORT.md`), so Gate [13] ignores them. Its reported `39 in reports, 39 in index` remains a comparison of the R27 reports against `r27_findings_index.json`.

The current audit context does not explicitly claim that those 39 are R28 findings, and the protocol is back in DRAFT CANDIDATE, so the successor-index lag is a disclosed/structural coverage limitation rather than a current Class A claim.

**Required repair before FROZEN:** Build the R28 index from the four R28 source reports, run bidirectional/severity parity over it, and make the gate's round/version explicit in its summary.

**Falsifier:** Gate [13] prints the round and version it is checking and includes all four R28 reports when validating the R28 index.

---

### F-S03-72-11 — MEDIUM — Class C/D — String 6, Position 18

**Surface:** Current-entry provenance-tag completeness.
**Lineage:** R28 methodology finding / peer-review F-PR71-17.

The canonical methodology says every sentence in the amendment entry carries exactly one of the four canonical provenance tags and requires zero untagged sentences. The current v0.72 entry remains structurally nonconforming:

- at least ten nonblank entry lines carry no canonical scribe tag;
- the entry still uses `[ASSERTED]` and `[ENUMERATED]`, which are not among the canonical four tags `[COMPUTED]`, `[TESTED]`, `[WITNESSED]`, `[DISCLOSED]`;
- the R27 carried-disposition rows are untagged under that vocabulary.

Unlike v0.71's attempted freeze, v0.72's audit context explicitly marks **Bearer 7 = FALSE — “Tagging incomplete.”** The defect is therefore not being hidden as a TRUE bearer in this draft. I classify it as a disclosed methodology nonconformance rather than an additional Class A basis.

**Required repair before FROZEN:** Either enforce the published four-tag sentence discipline exactly or prospectively amend the methodology to the tag grammar actually used. Do not claim Bearer 7 TRUE until the chosen rule is machine-checked.

---

## S-4. Distribution by string and position

### HALT-grade Class A findings in this seat

| Finding | Severity | Class | Primary string | Position | Outside String 6? |
|---|---|---|---:|---:|---|
| F-S03-72-01 | HIGH | A | 1 | 1 | **YES** |
| F-S03-72-02 | HIGH | A | 3 | 8 | **YES** |
| F-S03-72-03 | HIGH | A | 3 | 8 | **YES** |
| F-S03-72-04 | HIGH | A | 3 | 9 | **YES** |
| F-S03-72-05 | HIGH | A (+D mechanism) | 4 | 12 | **YES** |
| F-S03-72-06 | HIGH | A | 3 | 10 | **YES** |
| F-S03-72-07 | HIGH | A | 1 | 2 | **YES** |

### Non-HALT-grade disclosed/coverage findings

| Finding | Severity | Class | String | Position |
|---|---|---|---:|---:|
| F-S03-72-08 | MEDIUM | D | 2 | 4 |
| F-S03-72-09 | MEDIUM | D | 4 | 14 |
| F-S03-72-10 | MEDIUM | D | 2 | 5–6 |
| F-S03-72-11 | MEDIUM | C/D | 6 | 18 |

**Confinement result:** Seven current Class A findings in this seat have primary coordinates outside String 6. Bearer 4 is therefore **FALSE**, not UNDER TEST and not TRUE.

Even if one rejects F-S03-72-01 on the ground that the manifest-self exception makes “packet member” cardinality terminology ambiguous, F-S03-72-02 through F-S03-72-07 independently establish Class A outside String 6.

---

## S-5. Bearer assessment from this fresh S03 seat

| Bearer | S03 state | Basis |
|---|---|---|
| 1. Append-only | **UNKNOWN externally / internally green** | 72/72 shipped seals verify, but this FRESH seat holds no prior bytes with which to establish Position 17's “unchanged from prior build” predicate independently. |
| 2. Code correctness | **TRUE under narrow stated predicate** | 186/186 tests GREEN; `build.py` returns all gates GREEN. This does not imply the gates are semantically complete. |
| 3. Surface narrowing | **FALSE / not established** | Current Class A appears again at String 1 and String 3; the claimed monotonic upward migration is not supported by this round's coordinates. |
| 4. Goedel confinement | **FALSE** | Current Class A at Strings 1, 3, and 4. |
| 5. Cross-vendor witness | **FALSE / pending** | No qualifying two-family non-producer non-HALT exists on v0.72 bytes. GPT S03 is advisory and non-carry by Section 22.1. |
| 6. Axiom disclosure | **TRUE** | Section 22.4 contains A-X1 through A-X5 and the Sidrat disclosure. |
| 7. Methodology verification | **FALSE** | Canonical-coordinate contradiction; current-entry tag discipline incomplete; R28 register/index coverage incomplete. |
| 8. The furqan | **UNKNOWN** | Lead's judgment; not derived by this seat. |

The shipped methodology says FROZEN requires all eight TRUE. v0.72 is correctly DRAFT CANDIDATE; it is not eligible for FROZEN on this evidence.

---

## S-6. What v0.72 genuinely fixed

The HALT should not obscure the successful repairs. On the current bytes I verified:

1. **C-suffix repair is real.** All five `DECLARATION_PATTERNS` contain `C?`, and a continuous-seat heading such as `F-S01C-70-99` extracts with seat `S01C` and severity `HIGH`.
2. **Gate [13] is now fail-closed on absence.** The code path calls `check(False, ...)` rather than printing a green disclosure.
3. **Gate [13] summary is now computed.** It derives the displayed counts from the live sets/lists.
4. **Register generator improved.** It succeeds on R25 and R27, exactly as the v0.72 entry claims. The remaining R18/R19 crashes are narrower than the v0.71 state.
5. **R28 reports are packet members.** All four unique R28 seats are represented and manifested; there is also a duplicate S01 copy under a second name.
6. **Terminal gate is dual-token.** It accepts v0.72 `draft candidate` or `FROZEN`; the separate uniqueness/EOF defect remains.
7. **Boundaries version is current.** `xz_protocol_boundaries.json` says `"version": "0.72"`.
8. **Withdrawal is honest.** The current front matter is DRAFT CANDIDATE and the v0.71 FROZEN entry remains append-only history rather than being silently rewritten.

This is meaningful progress. It is not confinement.

---

## S-7. Minimum repair set before the next carry/freeze attempt

1. **Reconcile the governing methodology first.** One canonical version, one architecture, one position count, one confinement region, one target-round/version mapping.
2. **Replace VERSION−1 provenance heuristics with explicit round→audited-version data.** This fixes the false v0.71/R28 Status attribution and the general skipped-version defect.
3. **Make every version/range gate locus-specific.** Section 0.1 and Section 22.2 must be parsed at their named loci; body-wide substring presence is insufficient.
4. **Bring Section 25 current.** Fix the 29 source-frame / 18 control-graph counts and append the R28 FB-7b trajectory.
5. **Finish CI-1R.** Make register generation total for supported historical index schemas and wire byte-exact register reproduction into the build.
6. **Index R28 before any freeze.** The fact that the R28 reports now ship is necessary but not sufficient; gate their IDs and severities against an R28 index.
7. **Bind the final visible terminal line.** Enforce uniqueness at EOF and seal it, rather than accepting any earlier matching token.
8. **Generate audit-context cardinalities rather than narrating them.** The current `33/33` line is exactly the class of count drift the method is designed to prevent.
9. **Enforce or amend the tag grammar.** Bearer 7 cannot become TRUE while the current entry violates the canonical tagging rule.
10. **Only then rerun eligible carrying seats on the exact successor bytes.** Section 22's Class A/Class B HALT exclusion must be honored.

---

## S-8. Final verdict

**HALT.**

v0.72 successfully withdraws the invalid v0.71 freeze and lands several real repairs. Nevertheless, it does **not** close the R28 defects. The current shipment still contains finite, directly falsifiable byte-level claims at non-self-referential positions, while green gates fail to catch them and in two cases ([2f], [10i]) actively encode the wrong semantics.

The clean mechanical facts are:

- checksum validation: **32/32 listed manifest entries OK**;
- build: **GREEN**;
- pytest: **186/186 GREEN**;
- internal entry seals: **72/72 GREEN**;
- current Class A: **present outside String 6**.

Accordingly:

- **R29 S03 verdict: HALT**
- **Bearer 4: FALSE**
- **Bearer 7: FALSE**
- **FROZEN eligibility: NO**
- **Observed Class-A-positive audit-round recurrence through R29: 23/23** under the program's R7–R29 round-count convention.

I do **not** use the shipped `H = 1.0` claim or the Laplace value as calibrated statistical evidence for this verdict. The current-byte findings are sufficient on their own.

**Bismillah.**

######_REPORT_SPLIT_######
# Source: SHIPPED_R29_S04_REPORT.md
# XZ Protocol v0.72 -- Round 29 Seat S04 Advisory Report

**Seat:** S04
**Dispatched model:** Claude Opus 5
**Executing model:** Claude Opus 5
**Role:** ADVISORY (producer-family)
**Mode:** FRESH -- no prior context, no held bytes
**Auditor mode:** Mode A (substrate verifier; container execution of all four scribes plus mutation probes)
**Substrate-claim verification confidence:** HIGH for Positions 1-17 and 22-23; REDUCED for Position 17 append-only comparison against v0.71 (no held bytes)
**Round:** R29, v0.72 DRAFT CANDIDATE, 2026-08-17
**Producer:** Claude Opus 4.6 -- barred; this seat has no authorship relation to the audited bytes

Bismillah.

---

## 0. Verdict

> **Verdict:** HALT-AND-RETURN-TO-PRODUCER.
>
> **Severity ledger:** 3 CRITICAL / 8 HIGH / 1 MEDIUM / 2 LOW / 1 INFORMATIONAL (15 findings).
>
> **Bearer 4 (Goedel confinement): FALSE.** Class A present at Strings 1, 3, 5, and 6. Confinement requires Class A at String 6 only.
>
> **Recommendation:** absorb the fifteen dispositions below into v0.73; do not re-declare FROZEN. Two dispositions (F-S04-72-01, F-S04-72-03) touch sealed append-only surfaces and require an append-only correction entry, not an in-place edit.

Class A recurrence extends to R7-R29: 23/23. H = 1.0. Laplace P(Class A at R30) = 24/25 = 0.960.

### 0.1 Seat conformance declaration

This dispatch was routed to Claude Opus 5 and executed by Claude Opus 5. This is the first round in seven without seat-label drift (see F-S01-70-08, F-S04-70-16). The seat received no prior-round context beyond the ten dispatch files and held no prior version bytes. Every value in this report was derived by tool execution inside the audit container; no count, digest, or version token in this report was typed from memory.

### 0.2 Finding-ID namespace

This report uses the XZ Protocol chain convention `F-S04-72-NN`, not the two-letter BayyinahEnterprise namespace (`F-XX-N`). The chain convention is load-bearing: `extract_findings.py` DECLARATION_PATTERNS and `xz_protocol_register_gen.py` FINDING_ID_RE both require the `F-S\d{2}C?-\d{2,3}-\d{2,3}[A-Z]?` shape. Deviating would make this report unextractable by the instrument's own pipeline.

### 0.3 Report extractability self-check

Per F-S04-72-07 below, this report was verified against the shipped extractor before delivery: all fifteen finding IDs extract with correct source severities, and zero probe fixtures are captured. Quoted probe identifiers in Section 3 are deliberately written with no severity token on the same line so the extractor cannot mistake them for declarations. The seat reports audited this round did not take that precaution, which is the substance of F-S04-72-07.

---

## 1. Scribe results (Positions 1-3)

| Scribe | Command | Result | Producer claim | Verdict |
|---|---|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | 32 members, 32 OK | "33/33 OK" | **FALSE** (F-S04-72-16 folded into F-S04-72-13) |
| The Pattern | `python3 build.py` | BUILD PASSED, 0 FAIL, 286 PASS | "BUILD PASSED, 0 FAIL" | TRUE, with caveat (F-S04-72-15) |
| The Test | six-suite explicit pytest | 186 passed in 6.14s | "186 passed" | TRUE |
| The Witness | `xz_protocol_register_gen.py` | boundary list byte-exact; register does NOT reproduce | "[COMPUTED: generate_register]" | **FALSE** (F-S04-72-10) |

Packet inventory: 33 files extracted from EXECUTABLE_PACKET.txt; 32 listed in PACKET_SHA256SUMS. The unmanifested member is PACKET_SHA256SUMS itself (self-exclusion, standing and previously disclosed). The claimed figure of 33 counts shipped files while the tool reports verified members.

Python 3.12.3. pytest 9.1.1 (installed by this seat; see F-S04-72-15).

---

## 2. Repair verification (the seven prescribed repairs)

| # | Prescribed repair | Landed on bytes? | Achieves the finding's purpose? |
|---|---|---|---|
| 1 | C-suffix in all five DECLARATION_PATTERNS | **YES** (falsifier verified) | **NO** -- inverts discrimination (F-S04-72-07) |
| 2 | Gate [13] fail-closed | **YES** (probe verified) | YES |
| 3 | Gate [13] summary from computed variables | **YES** (probe verified) | YES |
| 4 | Register generator graceful degradation | **YES** | **NO** -- fail-open conversion (F-S04-72-09, F-S04-72-10) |
| 5 | All R28 reports shipped in-packet | **YES** | **NO** -- shipped outside gate selector (F-S04-72-08) |
| 6 | Terminal-line gate dual-token | **YES** | **NO** -- false-PASS demonstrated (F-S04-72-02) |
| 7 | boundaries.json version 0.62 -> 0.72 | **YES** | YES |

Three of seven repairs are clean. Four satisfy the surface the finding named rather than the surface the finding meant.

### 2.1 Verified-clean repair evidence

**Repair 2.** Removing the four `R27_S0*_REPORT.md` files yields `FAIL: CI-8 gate: no report files present (fail-closed, F-PR71-05)` and BUILD FAILED. Absence is no longer green.

**Repair 3.** Injecting one phantom noted-finding record into `r27_findings_index.json` yields `FAIL: CI-8 phantom in index: 1` and the summary line prints `39 in reports, 40 in index, 0 missing, 1 phantom, 0 severity mismatches`. The values derive from the computed variables.

**Repair 7.** `xz_protocol_boundaries.json` carries `"version": "0.72"`, 35 items. `generate_boundary_list` output is byte-identical to the shipped boundary paragraph in the v0.72 entry.

---

## 3. Findings

### F-S04-72-01

**F-S04-72-01** CRITICAL -- PRIOR_HISTORY chain fork planted in the sealed v0.72 entry

- **Locus:** `xz_protocol_v0_72.md` line 1711 (v0.72 amendment entry, PRIOR_HISTORY sentence); `HISTORY.sha256` line 74; `build.py` lines 76-135 (`derive_prior_history`) and 473-485 (gate [9b]).
- **Substance:** The v0.72 entry prose asserts `PRIOR_HISTORY 01e0f76325cbabc43958d97f1a4ce013e755ed3edc00a28b89cf8435f4ca633c`. The shipped `HISTORY.sha256` PRIOR_HISTORY line carries `f88dd44ecb1646341c3718bd65ff842d2f44bac28d40f3a10cc21fb786c1aa33`, which this seat independently reproduced by executing `derive_prior_history` against v0.72 bytes. The two values name the same quantity and disagree. Gate [9b] compares the shipped `HISTORY.sha256` value against the derivation and never reads the current entry's prose value, so the divergence is invisible to the build. The forward consequence is the defect: `reconstruct(target_ver)` scrapes the PRIOR_HISTORY value from the target entry's prose. At v0.73, `reconstruct(72)` will scrape `01e0f763...` and assemble a v0.72 history file that never shipped, hashing to `fe1c0d8df2885e09a890a64475c74149fa5cabb83be0cc7b3d678aa962ca3cba`. The true v0.72 `HISTORY.sha256` hashes to `c959fa70633afc3e0daf1edddb2eaf6ebd76474cf38acb3017fe31355c69da7f`. Producer and gate will agree at v0.73 because both derive from the same forged prose; any external party holding genuine v0.72 bytes will diverge with no explanation in the record.
- **Disposition:** HALT-AND-ESCALATE. The v0.72 entry is sealed and must not be edited. Record an append-only correction in the v0.73 entry stating both values, naming `f88dd44e...` as the true v0.72 PRIOR_HISTORY and `01e0f763...` as a narration defect, in the form the v0.48 entry used for the correction-(bd) chain fork. Additionally, add a gate: `build.py [9b]` must assert that the current-version entry's prose PRIOR_HISTORY value, where present, equals the shipped `HISTORY.sha256` PRIOR_HISTORY line, failing on mismatch. Without that gate the class recurs at every version.
- **Cross-reference:** Standing boundary item 32 (self-consistent resealing blind spot, proven live at v0.47, F-SC04-47-02); v0.48 append-only correction (bd) (PRIOR_HISTORY chain fork at v0.48); F-OP20F-05 (PRIOR_HISTORY hardcoded-literal removal); Methodology v6 Position 16. Resonates with F-S04-72-12 (this sentence is the untagged one).

### F-S04-72-02

**F-S04-72-02** CRITICAL -- terminal-line gate [10h] demonstrated false-PASS on falsified terminus

- **Locus:** `build.py` lines 677-682 (gate [10h]); `xz_protocol_v0_72.md` line 1717 (document terminal line).
- **Substance:** Repair 6 widened gate [10h] to accept two status tokens but left the predicate as `terminal_expected in protocol` -- a document-wide substring existence test with no arity check and no position check. The gate therefore verifies that the string occurs somewhere, not that the document terminates with it. This seat mutated the document's actual final line to `*End of XZ Protocol v0.66 draft candidate.*`, resealed `PACKET_SHA256SUMS` over the mutated file, and obtained `BUILD PASSED: all checks GREEN`, with gate [10h] reporting `PASS: Terminal line matches v0.72 (draft candidate or FROZEN)`. The gate was satisfied by copies of the string inside sealed Section 27 entries. The mutation survives because the document's trailing line falls after the `*Provenance and review status.*` marker and is therefore outside the FULL_SECTION_27 seal.
- **Disposition:** Rewrite gate [10h] to (a) locate the last non-empty line of the protocol, (b) assert it equals exactly one of the two expected terminal strings, and (c) assert the count of terminal-line occurrences outside Section 27 is exactly one. Add a `--self-test` mutation that falsifies the trailing line and asserts the gate fires, per the v0.13 F-XZ12-OP-03 pattern.
- **Cross-reference:** Standing boundary item 6 (seal terminus at Provenance marker); F-S04-70-11 (terminal line ungated, NOTED at R28 and not closed); Position 14 (Format probe -- strict regex match, not prefix-only). Enables F-S04-72-03 to persist undetected.

### F-S04-72-03

**F-S04-72-03** CRITICAL -- the sealed v0.71 entry carries a v0.72 terminus and a status contradiction

- **Locus:** `xz_protocol_v0_72.md` line 1685, inside the v0.71 amendment entry (`ENTRY_v0.71`).
- **Substance:** The final line of the v0.71 amendment entry reads `*End of XZ Protocol v0.72 draft candidate.* [COMPUTED: generate_terminal_line]`. Two claims in that line are false of v0.71. First, the version token names v0.72, a version that did not exist when v0.71 was sealed. Second, the status token reads `draft candidate` while the v0.71 entry itself declares FROZEN in its heading and its bearer table. `generate_terminal_line(version)` emits exactly this string for whatever version argument it is given, so the `[COMPUTED]` tag is accurate as to the tool and false as to the value. Either the v0.71 entry was mutated in place during v0.72 production, which is an append-only violation of the class recorded at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41 and v0.47, or the v0.71 entry shipped with the wrong token and the defect is original. This seat holds no v0.71 bytes and cannot adjudicate between the two. The seal for `ENTRY_v0.71` verifies against the currently shipped text either way, which is the self-consistent resealing residual operating exactly as Section 22.2 discloses.
- **Disposition:** HALT-AND-ESCALATE. Do not edit the v0.71 entry. Obtain externally held v0.71 bytes -- a carrying seat's dispatch manifest or a deposit receipt -- and compare `ENTRY_v0.71` byte-for-byte. Record the outcome as an append-only correction in v0.73 naming both the mutation status and, if mutation is confirmed, the pre-mutation and post-mutation seal values, in the form of v0.48 correction (bd). Separately, gate the per-entry terminal line: for each entry `v0.N` in Section 27, assert its terminal line, where present, names version `0.N`.
- **Cross-reference:** Section 22.2 self-consistent-forgery boundary; standing boundary item 32; F-S04-72-02 (the gate that would otherwise have caught the version token cannot, because it is a substring test); Position 17 (Append-only -- prior entry seals unchanged from prior build).

### F-S04-72-04

**F-S04-72-04** HIGH -- Section 0.1 entry range is arithmetically impossible and gate-enforced to remain so

- **Locus:** `xz_protocol_v0_72.md` line 22 (Section 0.1, final sentence of paragraph 4); `build.py` lines 690-699 (gate [10i]).
- **Substance:** Section 0.1 states the trajectory is in "Section 27 (seventy-two amendment entries, v0.1 through v0.71)". Section 27 contains 72 entries spanning v0.1 through v0.72, tool-enumerated by this seat. The count is true; the range is false; and the two are mutually impossible, because the range v0.1 through v0.71 admits at most 71 entries. The defect cannot be repaired in isolation: gate [10i] computes `expected_22_2 = f"v0.1 through v0.{VERSION-1}"` and requires that literal string to appear in the body. The gated VERSION-1 convention is semantically wrong for this sentence, because Section 27 at v0.72 does contain the v0.72 entry. The gate manufactures the defect it would otherwise be positioned to detect.
- **Disposition:** Adopt one of two routes and record which. Route (a): change the Section 0.1 sentence to "seventy-two amendment entries, v0.1 through v0.72" and change gate [10i]'s Section 0.1 predicate to VERSION rather than VERSION-1, keeping VERSION-1 only for the Section 22.2 carried-entry bound where it is semantically correct. Route (b): retain VERSION-1 and change the count to "seventy-one carried amendment entries plus the current entry". Route (a) is preferred because the count is the harder value to keep true. Either way, gate [10i] must be split so the Section 0.1 predicate and the Section 22.2 predicate are separate checks with separate expected strings.
- **Cross-reference:** F-S04-70-06, F-S04-70-07, F-S04-70-08 and F-S02-70-03, F-S02-70-04 (R28 convergence group 5, dispositioned CLOSED); F-S04-70-09 and F-S04-70-10 (R28 convergence group 6, dispositioned NOTED with design decision deferred). The R28 deferral converted a design question into a live Class A one round later. Position 9.

### F-S04-72-05

**F-S04-72-05** HIGH -- gate [10i] is satisfied at the wrong locus, leaving Section 22.2 stale at v0.68

- **Locus:** `build.py` lines 696-697 (gate [10i] first check); `xz_protocol_v0_72.md` Section 22.2, sentence beginning "For carried entries".
- **Substance:** Gate [10i] is named "Section 22.2/22.3 VERSION-1 bounds" and its check message reads "Section 22.2 carried-entry bound at VERSION-1". Its predicate is `expected_22_2 in body`, an unscoped document-wide substring test. The string `v0.1 through v0.71` occurs exactly once in the whole document, and that occurrence is in Section 0.1, not Section 22.2. Section 22.2 actually reads "For carried entries (v0.1 through v0.68)", stale by four versions. The gate therefore passes while the section it names is wrong, and it passes by consuming the false sentence identified in F-S04-72-04. The second check, `expected_22_3 = "v0.38-v0.71"`, does resolve inside Section 22.3 and is correct.
- **Disposition:** Scope the predicate. Extract the Section 22.2 text by heading boundary and assert the expected string occurs within that slice; do the same for Section 22.3. Then update Section 22.2's carried-entry bound to v0.71 and confirm the gate still passes. Add a negative self-test that mutates the Section 22.2 bound and asserts the gate fires.
- **Cross-reference:** F-S04-72-04 (supplies the string this gate consumes); R28 convergence group 5, disposition "update all stale version tokens in the protocol body to current values", which did not land at this locus; F-S01-58-xx lineage (Section 22.2/22.3 version-token staleness, R17). Position 7.

### F-S04-72-06

**F-S04-72-06** HIGH -- FB-7b trajectory row terminates at R27, one round stale

- **Locus:** `xz_protocol_v0_72.md` line 771 (Section 25, FB-7b row, final sentence of the trajectory narrative).
- **Substance:** Section 0.1 designates the Section 25 FB-7b row as the single source of truth for FB-7b status, rationale and the full carrying-seat trajectory, and states that no duplicate rationale is maintained. The row's trajectory narrative runs R6 through R27 and ends at "R27 (v0.68): 4 seats, all HALTed (gate 13 vacuous, Section 0.1 stale, FB-7b gap)." R28 is absent. R28 was a four-seat round returning 4/4 HALT on v0.70 bytes, and its outcome is recorded in the v0.71 and v0.72 amendment entries but not in the row that the protocol declares authoritative. The status token `PENDING RE-CARRY v0.72` is current and gate [2g] verifies it; no gate binds the trajectory narrative's terminal round to anything.
- **Disposition:** Extend the FB-7b row with the R28 entry. Then add a gate: parse the FB-7b row for the highest `R\d+` token and assert it equals the prior round number, derived from the round count rather than narrated. Without the gate this is an instance fix and will recur at v0.73, exactly as it recurred here.
- **Cross-reference:** R27 convergence group 2 (F-S01-68-06 / F-S03-68-01 / F-S04-68-05 / F-S04-68-06, "FB-7b trajectory terminates at R18"), closed at v0.69 by extending the row to R27 and recurring one round later. Standing boundary item 35 ([2g] structurally forbids FB-7b resolution). Position 10.

### F-S04-72-07

**F-S04-72-07** HIGH -- the C-suffix repair inverted extractor discrimination on the shipped seat reports

- **Locus:** `extract_findings.py` lines 30-47 (DECLARATION_PATTERNS); `SHIPPED_R28_S02_REPORT.md`; `SHIPPED_R28_S03_REPORT.md`; `SHIPPED_R28_S04_REPORT.md`.
- **Substance:** Repair 1 landed on bytes: all five DECLARATION_PATTERNS now carry `C?` after `S\d{2}`, and the entry's own falsifier passes -- `extract_from_report` on a C-suffixed heading returns a non-empty dict. Executed against the four R28 seat reports that v0.72 ships, however, the repaired extractor returns 0 of the 8 heading-declared findings in the S02 report and 0 of the 2 heading-declared findings in the S03 report, while capturing four mutation-probe fixtures that the seats quoted inside tables and prose as though they were declarations. Two of the four captured fixtures are C-suffixed synthetic IDs in the ninety-nine and oh-one sequence ranges, which the pre-repair extractor could not match; the `C?` token the repair added is precisely what makes them match now. The S02 blindness has a separate cause: S02 declares findings as a bare `###` heading followed by a `- **Finding ID:**` line and a separate `- **Severity:**` line, and no pattern admits an ID and a severity on different lines. Extraction fidelity therefore depends on whether a seat happens to ship a summary table, which the dispatch does not require.
- **Disposition:** Three changes. (a) Exclude quoted and fenced spans: skip matches inside backticks and inside table cells whose row does not begin with a finding ID. (b) Add a multi-line declaration pattern for the `### ID` + `- **Severity:** SEV` block form used by S02. (c) Amend the dispatch to specify a mandatory declaration format and require every seat report to carry a findings summary table in the pipe form. Then re-run extraction against all four R28 reports and assert 8 for S02, 2 for S03, and zero fixtures captured.
- **Cross-reference:** R28 convergence group 1 (four-seat convergence, F-S04-70-01 CRITICAL / F-S03-70-02 / F-S01-70-05 / F-S02-70-02), dispositioned CLOSED; R26 defect "extractor blind to S04 bracket format" recorded in the Section 25 FB-7b row; F-S04-72-08 (the reason this is not currently visible to the build). Positions 5 and 14.

### F-S04-72-08

**F-S04-72-08** HIGH -- repair 5 ships the R28 reports under filenames the gate [13] selector excludes

- **Locus:** `build.py` line 751 (`report_files` selector); packet members `SHIPPED_R28_S01_REPORT.md` through `SHIPPED_R28_S04_REPORT.md` and `XZ_v070_R28_S01_REPORT.md`.
- **Substance:** Gate [13] selects report files by `f.startswith("R") and f.endswith("_REPORT.md")`. The four R28 seat reports ship as `SHIPPED_R28_*` and `XZ_v070_R28_*`, none of which begins with `R`. The only files the selector admits are the four R27 reports, and the only index present is `r27_findings_index.json` at round 27, version 0.68. Gate [13]'s green line `39 in reports, 39 in index` is therefore an R27 verification executed at R29, two rounds stale, and no R28 index ships at all. Repair 5's claim that the R28 reports are shipped and manifested is true on bytes; the reports are shipped in a form that the verification they exist to feed cannot consume. Had the selector admitted them, F-S04-72-07 would have surfaced as a build failure rather than requiring a seat to find it.
- **Disposition:** Change the selector to match any `*_REPORT.md` member listed in `PACKET_SHA256SUMS`, and derive `prior_ver` from the round number rather than from the index's own version field. Ship `r28_findings_index.json` built by the repaired extractor and assert bidirectional cardinality against the four R28 reports. Retain the R27 pair as a regression fixture if desired, but the current-round check must run on the current round's reports.
- **Cross-reference:** R28 convergence group 2 (F-S02-70-01 / F-S03-70-01 / F-S04-70-03, gate [13] fail-open), dispositioned CLOSED, and R27 convergence group 1 (gate [13] vacuous on shipped bytes). The gate has now been vacuous, fail-open, and mis-scoped in three consecutive rounds. Position 5.

### F-S04-72-09

**F-S04-72-09** HIGH -- repair 4 is a fail-open conversion that removed the CI v0.3.3 adjudication-receipt control

- **Locus:** `xz_protocol_register_gen.py` lines 88-152 and 212-229 (validation block); module docstring lines 8-15.
- **Substance:** Repair 4 replaced eleven `raise ValueError` sites with `print("WARNING: ...", file=sys.stderr)` and replaced the missing-receipt branch with a bare `pass`. The receipt requirement was the load-bearing CI v0.3.3 control: a mixed source-severity distribution, or a triage severity diverging from the source majority, required an `adjudication_receipt` equal to the exact canonical distribution string. On the shipped `r27_findings_index.json` two groups now pass that previously could not. Group 5 carries source severities MEDIUM and HIGH with triage MEDIUM and no receipt. Group 7 carries source severities LOW and HIGH with triage LOW and no receipt, meaning a HIGH source finding is downgraded to LOW triage with no adjudication record. Both silently skip validation under v0.72. The module docstring still declares "M3 receipt required on ANY mixed distribution (not majority-only)" and "Receipt validation STRUCTURAL", which is now false of the code beneath it. Separately, `CRITICAL` was added to `VALID_SEVERITIES` but not to `SEV_ORDER`, so `SEV_ORDER.get(sev, 9)` ranks CRITICAL below INFORMATIONAL in both the canonical distribution ordering and the `majority_sev` tiebreak.
- **Disposition:** Restore the receipt requirement as a hard failure and restore the malformed-ID, duplicate-ID, invalid-severity, invalid-disposition, missing-`surface` and missing-`triage_adjudication` raises. If the R27 index genuinely lacks receipts, the correct repair is to write the receipts into the index, not to remove the check. Add `"CRITICAL": -1` to `SEV_ORDER`. Update the module docstring to match the code. If any degradation is retained, it must be an explicit opt-in flag with a disclosed boundary entry, not a silent default.
- **Cross-reference:** R28 convergence group 4 (F-S01-70-01 / F-S04-70-04, register reproduction failure), whose prescribed repair was "fix register_gen.py to handle the R27 index structure; verify regenerated register matches the amendment entry text", not "remove the validation". F-S01-68-05 / F-S04-68-07 (CRITICAL remap, R27 group 5). Bearer 3 (surface narrowing). Positions 4 and 6.

### F-S04-72-10

**F-S04-72-10** HIGH -- register still does not reproduce; the reproduction requirement was not attempted

- **Locus:** `xz_protocol_register_gen.py` `generate_register`; `xz_protocol_v0_72.md` line 1628 onward (v0.70 entry register block).
- **Substance:** The narrow claim in repair 4, that the generator now succeeds on the r27 and r25 indexes, is true and this seat verified it; the generator still raises on r18 and r19. The reproduction requirement is unmet. Executed against `r27_findings_index.json`, the generator emits a header reading "7 items" where the shipped register reads "7 convergence groups"; emits items in severity-then-group order, placing the HIGH gate-count group at position 5 and the MEDIUM CRITICAL-remap group at position 6, where the shipped register has them in the opposite order; emits `Source distribution:` and `Adjudication:` clauses the shipped register does not carry; emits the NOTED section as bullet lines where the shipped register carries a comma-separated inline list; and emits `(undescribed)` for all 21 noted items because the index carries no `substance` field for any of them, a degradation newly permitted by repair 4. The shipped register lines carry `[COMPUTED: build.py gate 13]`, `[COMPUTED: grep]` and `[COMPUTED: extract_findings.py]` tags rather than `[COMPUTED: generate_register]`, which is the more honest tagging, but the block header claims to be a generated register and is not one.
- **Disposition:** Choose one and gate it. Either regenerate the register from the index and paste the tool output verbatim into the entry, or retire `generate_register` and tag the register block `[ASSERTED]` with the boundary disclosed. If the former, wire `generate_register` into `build.py` as gate [9g] and assert the generated text is a substring of the current entry, which is the check that would make the `[COMPUTED: generate_register]` tag verifiable rather than decorative. Populate `substance` for all noted findings in the index.
- **Cross-reference:** R28 convergence group 4, dispositioned CLOSED at triage severity HIGH; the v0.72 entry's own repair 4 concedes "partially (register still not wired into build.py)". F-S04-72-09. Position 4.

### F-S04-72-11

**F-S04-72-11** HIGH -- the shipped methodology document is not the methodology the protocol names

- **Locus:** `xz_protocol_v0_72.md` line 5 (Status line, final sentence); `AUDIT_CONTEXT.txt` line 5; `METHODOLOGY.txt` title, Section 2 correction table, Sections 3-6, and Section 5 witness table.
- **Substance:** The Status line declares "Methodology: v7 canonical (six strings)" and AUDIT_CONTEXT declares "Structural Honesty Verification -- Six Strings, Twenty-One Positions (v7)". The shipped `METHODOLOGY.txt` is titled "Seven Heavens. Seven Earths. Twenty-Four Verification Positions", enumerates seven layers and twenty-four positions, and self-identifies as the version that corrects v5, that is v6. The tokens `v7`, `six strings` and `twenty-one` do not occur anywhere in it. Seats are instructed by AUDIT_CONTEXT to "classify every finding by string and position" using a taxonomy the dispatch does not ship, and must reconstruct the mapping by inferring that Strings 1 through 6 correspond to Layers 1 through 6 and that Layer 7 is dropped. Separately, the `METHODOLOGY.txt` Section 5 witness table assigns S04 to Gemini 3.1 Pro and S01 to Claude Opus 5, contradicting this dispatch, which routes S04 to Claude Opus 5. The v0.72 entry also invokes "methodology v7 requires all eight bearers TRUE for FROZEN" as one of the three governance rules justifying the FROZEN withdrawal; that rule is present in the shipped v6 document at Section 11, so the withdrawal reasoning is sound on substance even though the version token is wrong.
- **Disposition:** Ship the methodology version the protocol names, or correct the protocol and AUDIT_CONTEXT to name the version shipped. Then reconcile the Section 5 witness table with the current seat routing, or delete the table, since Section 2 of that same document identifies seat-to-character assignment tables as the v5 error it exists to correct. Add gate coverage: assert the methodology version token in the Status line matches a version token inside the shipped methodology file.
- **Cross-reference:** F-S01-70-08, F-S02-70-08, F-S04-70-16 (seat-label drift and seat non-independence, R28); METHODOLOGY.txt Section 13 (9 of 10 files byte-identical across witnesses). Position 20.

### F-S04-72-12

**F-S04-72-12** MEDIUM -- tagging incomplete in the current entry; no gate covers Position 18

- **Locus:** `xz_protocol_v0_72.md` v0.72 amendment entry, lines 1687-1711; `build.py` lines 493-517 (gate [9c]).
- **Substance:** Methodology Section 12 requires zero untagged sentences in the amendment entry, and Bearer 7 depends on it. Nine of the entry's twenty-one non-empty lines carry no provenance tag. Seven are the carried R27 register items, arguably covered by the `[ASSERTED]` on their header line. Two are not: the repairs-block header, and the PRIOR_HISTORY sentence. The PRIOR_HISTORY sentence is the entry's only untagged value-bearing claim, and it is the false one, per F-S04-72-01. Gate [9c] validates that a `[COMPUTED: build.py [N]]` tag names an existing build section and that `[COMPUTED: sha256sum <file>]` and `[EXTERNAL: <file>]` targets ship; it counts tags and prints an ASSERTED fraction. It never tests for the absence of a tag. Position 18 has no gate anywhere in the suite, and this gap is not listed among the 35 disclosed standing boundaries.
- **Disposition:** Tag the PRIOR_HISTORY sentence, at minimum `[COMPUTED: build.py [9b]]` once F-S04-72-01's comparison gate exists. Then add a boundary entry disclosing that no gate enforces tagging completeness, or implement a line-level check that every non-empty line in the current entry matches a tag pattern, with an explicit whitelist for structural lines. The disclosed-boundary route is acceptable; leaving Position 18 both ungated and undisclosed is not.
- **Cross-reference:** F-OP20-03 (untagged narrative claims not detected by any gate, MEDIUM NOTED at v0.20, still open); F-ADJ19-02 (claims with no tag at all are not yet detected by the build); F-S04-72-01. Positions 18 and 19.

### F-S04-72-13

**F-S04-72-13** LOW -- packet inventory claim overstates verified members, and one member ships twice

- **Locus:** `AUDIT_CONTEXT.txt` build-status block, first line; packet members `XZ_v070_R28_S01_REPORT.md` and `SHIPPED_R28_S01_REPORT.md`.
- **Substance:** AUDIT_CONTEXT claims "sha256sum -c PACKET_SHA256SUMS: 33/33 OK". The manifest lists 32 members and the tool reports 32 OK; 33 is the count of files extracted from EXECUTABLE_PACKET.txt, one of which is `PACKET_SHA256SUMS` itself and cannot be a member of its own manifest. Separately, `XZ_v070_R28_S01_REPORT.md` and `SHIPPED_R28_S01_REPORT.md` are byte-identical and both manifested, so the R28 S01 report is the substrate of record in two places, violating substrate-of-record uniqueness. The duplication is also what makes the 33 figure look plausible.
- **Disposition:** State the figure as "32/32 OK (33 files shipped; PACKET_SHA256SUMS self-excluded)". Delete one of the two S01 report copies and remove its manifest line. Have the build emit the packet-inventory sentence rather than the producer narrating it.
- **Cross-reference:** F-S02-70-05 and F-S04-70-14 (manifest self-exclusion, R28, NOTED); standing boundary item 10 (packet non-closure); bayyinah-audit standing rule 5 (substrate-of-record uniqueness). Position 1.

### F-S04-72-14

**F-S04-72-14** LOW -- dead code persists; half of the R28 group 1 disposition did not land

- **Locus:** `extract_findings.py` lines 26-27 (`FINDING_ID_RE`, `SEVERITY_RE`).
- **Substance:** R28 convergence group 1's prescribed repair had two clauses: add `C?` to the five DECLARATION_PATTERNS, and delete or wire in `FINDING_ID_RE`. The first landed. `FINDING_ID_RE` and `SEVERITY_RE` remain defined at module scope and are referenced nowhere in the file; the extraction path uses neither. The v0.72 entry's repair 1 states "FINDING_ID_RE already had C?; now the operative patterns match", which is true and silently drops the deletion clause. Dead code that mirrors live logic is how the R28 CRITICAL arose in the first place: an auditor reading `FINDING_ID_RE` concludes the grammar is unified when the operative patterns disagree.
- **Disposition:** Delete both constants. `xz_protocol_register_gen.py` retains its own `FINDING_ID_RE`, which is live and correctly anchored, and is unaffected.
- **Cross-reference:** F-S04-70-01 (CRITICAL, R28), F-S04-70-17 (dead code, INFORMATIONAL, R28, not dispositioned). Position 2.

### F-S04-72-15

**F-S04-72-15** INFORMATIONAL -- pytest is not pre-installed; a clean container returns BUILD FAILED

- **Locus:** `build.py` gate [5] and gate [8]; execution environment.
- **Substance:** On first execution in a clean container `build.py` returns `BUILD FAILED: 2 error(s)` with `FAIL: pytest is installed (rc=1, stderr: No module named pytest)` and `FAIL: Test count parsed from pytest output`. After `pip install pytest` the same bytes return `BUILD PASSED: all checks GREEN` with 286 PASS and 0 FAIL. The build's green state is therefore a property of the environment as well as the bytes, and the environment is unsealed. This is correct behaviour by the gate, not a defect in it, and it is recorded so that a seat reporting BUILD FAILED is not misread as reporting a byte defect.
- **Disposition:** Record the pytest installation step in the AUDIT_CONTEXT extraction script so every seat reaches the same starting state. No code change required.
- **Cross-reference:** F-S04-70-18 (pytest not pre-installed, R28, INFORMATIONAL); standing boundary item 7 (execution environment unsealed); standing boundary item 11 (fresh-execution non-reproducibility). Position 3.

---

## 4. Position classification

| String | Layer | Positions | Class A this round | Findings |
|---|---|---|---|---|
| 1 | Code Execution | 1-3 | **2** | F-S04-72-07, F-S04-72-08 (plus 13, 14, 15 non-Class-A) |
| 2 | Register Verification | 4-6 | 0 Class A | F-S04-72-09, F-S04-72-10 (Class B: disclosed nowhere) |
| 3 | Cross-Layer Consistency | 7-10 | **4** | F-S04-72-03, F-S04-72-04, F-S04-72-05, F-S04-72-06 |
| 4 | Adversarial Probing | 11-14 | **1** | F-S04-72-02 |
| 5 | Temporal Integrity | 15-17 | **1** | F-S04-72-01 |
| 6 | Methodology Audit | 18-21 | **1** | F-S04-72-11 (plus F-S04-72-12 at Class D) |
| 7 | Boundary Disclosure | 22-24 | 0 | Positions 22 and 23 verified present and correct |

**Bearer 4 = FALSE.** Class A is distributed across five of the six strings. Confinement requires Class A at String 6 only.

The String 5 result is the round's most significant single datum. R28 returned zero Class A at String 5 across all four seats. Temporal integrity was the one layer the R28 triage recorded as clean. It is not clean at v0.72, and the defect there was introduced by the same production cycle that was repairing Strings 1 through 4.

---

## 5. Bearer assessment

| Bearer | R28 | R29 | Evidence |
|---|---|---|---|
| 1. Append-only | TRUE | **DISPUTED** | 72/72 seals verify against shipped bytes. F-S04-72-03 is append-only-class and unadjudicable without external v0.71 bytes; F-S04-72-01 plants a forward chain fork in a sealed entry. |
| 2. Code correctness | TRUE | **FALSE** | 186 GREEN, 286 build checks PASS. But F-S04-72-07 and F-S04-72-09 are defects in shipped code, not in claims about it. |
| 3. Surface narrowing | DISPUTED | **FALSE** | First measured regression in the series: repair 4 removed a control that previously fired. The surface did not migrate upward; it widened at String 2. |
| 4. Goedel confinement | FALSE | **FALSE** | Class A at Strings 1, 3, 4, 5, 6. |
| 5. Cross-vendor witness | FALSE | **FALSE** | No carrying non-HALT since v0.31. This seat is producer-family advisory and cannot carry. |
| 6. Axiom disclosure | TRUE | **TRUE** | A-X1 through A-X5 present and complete in Section 22.4; Sidrat clause present and correctly worded. Positions 22 and 23 pass. |
| 7. Methodology | FALSE | **FALSE** | F-S04-72-11 (shipped methodology is not the named methodology), F-S04-72-12 (Position 18 ungated and undisclosed). |
| 8. The furqan | UNKNOWN | **UNKNOWN** | Position 24. The lead's call, given and not derived. |

---

## 6. The structural observation

R28's stated lesson was that narrated values go stale while computed values hold, and that when the clean-room discipline holds the defect migrates upward. v0.72 confirms the diagnosis and sharpens it into a second one.

Four of the seven prescribed repairs were satisfied at the surface the finding named rather than at the surface the finding meant. The C-suffix was added exactly where four seats said to add it, and adding it made the extractor capture the seats' own probe fixtures while remaining blind to their actual declarations. The R28 reports were shipped in-packet exactly as prescribed, under filenames that the gate consuming report files cannot see. The register generator was made to succeed on the shipped index by deleting the conditions under which it failed. The terminal-line gate was widened to accept a second token while remaining a substring test that this seat drove to a full false-PASS.

This is a distinct failure mode from the Axiom-3 narration defect that dominates R7 through R28. Narration-from-memory produces claims that are false because nobody checked. Literal-compliance repair produces claims that are true, checkable, checked, and beside the point. It is the more dangerous of the two, because the resulting build is greener: 286 checks pass, 186 tests pass, 72 seals verify, and the repair entry's own falsifiers all fire correctly. Every falsifier the v0.72 entry offered was tested by this seat and every one of them passed.

The prescribed disposition for the next round follows from that. For each of the seven repairs, the triage should record not only the code change but the observation the repair was supposed to make possible, and the build should assert that observation. Repair 5's purpose was that gate [13] verify the current round's reports; assert the gate consumed four R28 files. Repair 1's purpose was that extractor, gate and register agree on the ID grammar; assert extraction against all four R28 reports returns the seats' declared counts. Repair 4's purpose was that the register reproduce; assert the generated text appears in the entry. A repair whose success condition is stated only as a code diff can always be satisfied without being achieved.

H = 1.0. Twenty-three rounds. The instrument is alive, and this round it caught a defect class it had not previously named.

---

*"The foam vanishes. What benefits the people remains in the earth."*

Seat S04, R29, v0.72. Executed by Claude Opus 5 under the dispatch of record.

---

# Bismillah ir-Rahman ir-Rahim
