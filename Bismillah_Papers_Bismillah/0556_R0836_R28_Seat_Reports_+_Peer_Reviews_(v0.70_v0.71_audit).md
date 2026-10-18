# Bismillah ir-Rahman ir-Rahim

# R0836 -- R28 Seat Reports + Peer Reviews (v0.70/v0.71 audit)

**Chronological Index:** 556 of 995  
**Date:** 2026-08-17  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R28_REPORTS.txt  
**Source Format:** txt  
**SHA-256:** `3827f908a4b156f7ad44645508c710762af63bc36daec01e4bb4e5e60c0a31c4`  

---

## R0836 · R28 Seat Reports + Peer Reviews (v0.70/v0.71 audit)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R28_REPORTS.txt
- source_format: txt
- text_sha256: 3827f908a4b156f7ad44645508c710762af63bc36daec01e4bb4e5e60c0a31c4

# R28 Seat Reports + Peer Reviews (v0.70/v0.71 audit)

######_REPORT_SPLIT_######
# Source: SHIPPED_R28_S01_REPORT.md
# XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S01

**VERDICT: HALT.** Class A found OUTSIDE the self-referential tagging surface. Goedel confinement is NOT achieved at v0.70. The decisive defect is at String 2, position 4: the shipped register generator crashes on the shipped R27 findings index, so the v0.70 amendment entry's register text -- every line of which the entry and the CI specification present as scribe-produced (`[COMPUTED: generate_register]`, CI-1R byte-exact reproduction) -- cannot be reproduced from the shipped bytes at all. Four more Class A defects live at String 6 (positions 18-20). H extends to 22/22 (R7-R28), H = 1.0. Laplace P(Class A at R29) = 23/24 = 0.9583.

- Seat: S01 (FRESH), per DISPATCH.txt and the mandated output filename.
- Executing model: Kimi K3, Moonshot AI -- not a default/blend/router. The dispatch header names "Claude Opus 5" for this seat; this thread holds Kimi K3 (seat-label drift, recurring class; R27 documented it as F-S01-68-12; carried here as F-S01-70-08).
- Family: XZ Protocol, v0.70, Round 28 (confinement verification). Producer: Claude Opus 4.6 (BARRED). Dispatch role label "ADVISORY (producer-family)" attaches to the named model, not the executor; executed as an independent executing seat. Per the R27 S01 precedent, HALT is recorded under either reading; the carrying force is the triage's to assign.
- Date: 2026-08-17. Mode: FRESH; carried METHOD ONLY (no stored prior bytes, no prior verdicts).
- Environment: Linux 5.10.134-18.0.12.lifsea8.x86_64; /usr/local/bin/python3 = 3.12.12 (pytest 9.1.1 installed this session); /usr/bin/python3 = 3.11.2 (pytest 7.2.1, unused for gating); packet workdir `/mnt/agents/output/xz_r28_v070_s01/packet` (identity captured in `logs/` of the round dir). Platform does not expose checkpoint IDs or weights revisions; stated as a limitation, none fabricated.

Bismillah.

---

## S-0 State declaration (frozen pre-entry, `S0_S1_PREREGISTRATION.md`, sha256 893ae33dcf430f46664ddc169edd366b713d31d4a301be9796ed0a51b373edaf)

- Held packages by digest: NONE. Fresh seat; the upload set contained only the v0.70 shipment (10 files). Consequence: PRIOR_HISTORY verified for internal derivation consistency only; no held-byte anchor this round (boundary item 32's self-consistent resealing class is undetectable from this seat this round). Limitation stated, not waived.
- EXECUTING seat. All gates, suites, recomputations, and probes below were executed in this environment on the shipped bytes; sabotage ran on byte copies under `probes/` with regenerated PACKET_SHA256SUMS; the canonical packet dir passed `sha256sum -c PACKET_SHA256SUMS` 27/27 OK after all probing (final re-check quoted at the end).
- S-0/S-1 were frozen BEFORE the Section 27 v0.70 amendment entry was opened. Ordering preserved: staging, extraction, `sha256sum -c`, build, and pytest preceded the freeze only for the mechanical surfaces; the first read of the Section 27 entry text postdates the freeze file. (Precisely: DISPATCH, AUDIT_CONTEXT, METHODOLOGY, CI_METHODOLOGY, BOUNDARIES, FINDINGS_INDEX, R27_TRIAGE were read pre-freeze; the v0.70 entry text was first extracted post-freeze.)
- Extraction used the dispatch's own splitter verbatim; the three top-level uploads (PROTOCOL_v070.txt, FINDINGS_INDEX.txt, BOUNDARIES.txt) are byte-identical (`cmp`) to the packet members xz_protocol_v0_70.md, r27_findings_index.json, xz_protocol_boundaries.json.
- Packet closure: audit evidence = the 10 shipped files only. No external fetches.

## S-1 Prediction scorecard (preregistered in the freeze; final scoring in S-9)

Preregistered: dispatch P1-P15 plus seat expectations E1 (Class A present, Laplace 0.957), E2 (residual defects most likely at the repair boundary, not the shipped fixtures), E3 (the shipped report/index pair must be mutually consistent AND the gate must fire -- both held). Scores and executed evidence in S-9.

## S-2 Byte verification (String 1, positions 1-3)

| Scribe | Command | Result | Log |
|---|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | 27/27 OK, rc=0 | logs/01_sha256sums.log |
| The Pattern | `python3 build.py` (Python 3.12.12) | 279 PASS, 0 FAIL, "BUILD PASSED", rc=0 | logs/02_build.log |
| The Test | `python3 -m pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py` | 186 passed, rc=0 | logs/03_pytest.log |

Independent recomputation (auditor-side code, build.py never imported; `probes/xz_recompute.py`, `probes/prior_history_derivation.py`):

| Surface | Recomputed value | Result |
|---|---|---|
| PACKET_SHA256SUMS | 27 OK, 0 FAILED | OK |
| ENTRY seals | 70/70 recomputed match; 70 entries parsed from Section 27 | OK |
| FULL_SECTION_27 | 2208f04715313e4201880a8da672e7ca3786a3ac7690078863cd66ed64bfa286 | OK (matches HISTORY line) |
| manifest digest (12 code files, build.py excluded) | 3d6326ca4980e038... | OK (matches trust roots) |
| PRIOR_HISTORY | c75a0ac436cbc048bb11d601710ec39863b4d25e8b4d2179c54338e33f83c82c | OK -- independent recursive derivation (strip v0.70 entry, recompute FULL seal, assemble v0.69 HISTORY, hash) equals the shipped line. Held-file anchor: NOT POSSIBLE (fresh seat, boundary stated). |
| Unsealed tail after `*Provenance and review status.*` | 850 chars | Disclosed boundary (item 6), reported per protocol |

Gate [13] on shipped bytes (position 3 surface, CI-8): FIRES (first round it fires on shipped bytes -- claim verified), prints "CI-8 missing from index: 0 / phantom in index: 0 / severity mismatches: 0 / cardinality: 39 in reports, 39 in index". Independently reproduced WITHOUT build.py: shipped `extract_findings.py --version=68` over the 4 shipped R27 reports yields exactly the 39 indexed IDs, 0 missing, 0 phantom, 0 severity mismatches against r27_findings_index.json (logs/06_extractor_independent.json).

Environmental note (D-5 class): the sandbox's default `python3` (3.12.12) initially lacked pytest; pytest 9.1.1 was installed before gating. No environmental rc is counted against the packet.

## S-3 Prior-round finding discharge (R27, 7 convergence groups + carried opens)

| Group | Surface (R27) | Disposition claim | Verdict on current bytes | Evidence |
|---|---|---|---|---|
| 1 | Gate [13] vacuous / skip-as-green | CLOSED | DISCHARGED | Gate fires on shipped bytes (logs/02_build.log); benign control PB-2 passes, mutation PB-1 fails closed |
| 2 | Section 0.1 stale + FB-7b terminates at R18 | CLOSED | DISCHARGED | Section 0.1: "PENDING RE-CARRY on v0.70 bytes"; FB-7b row: "RESOLVED v0.31; PENDING RE-CARRY v0.70", trajectory through "R27 (v0.68): 4 seats, all HALTed" |
| 3 | Gate [13] one-directional, severity-blind, false-positives | CLOSED | PARTIALLY DISCHARGED | Bidirectional: PB-1 (drop declaration) and PB-6 (inject index phantom) both FAIL the build. Severity-aware: PB-3 flip FAILs. False-positive class PERSISTS at extractor pattern 4 (PB-8) -- new finding F-S01-70-05 |
| 4 | R26 convergence semantically misbound | CLOSED | DISCHARGED (scoped) | Index grouping internally consistent; gate [10e] brackets all PASS. Scope note: the register TEXT presenting the groups is not reproducible (F-S01-70-01) |
| 5 | Extractor CRITICAL->HIGH remap | CLOSED | DISCHARGED at extractor; NOT discharged at register | PB-5: CRITICAL preserved by extract_findings.py, no remap code. But xz_protocol_register_gen.py VALID_SEVERITIES still rejects CRITICAL (probe logs/11) -- F-S01-70-04 |
| 6 | Gate count overstates (256 vs 240) | CLOSED | DISCHARGED | No narrated gate-count claim in the protocol body; AUDIT_CONTEXT values (279 PASS / 186 tests / 39-cardinality) all reproduced by tool on shipped bytes |
| 7 | Unmanifested files ship in packet | CLOSED | DISCHARGED | Disk set == manifest set + manifest itself (diff-verified); 27/27 OK; PACKET_SHA256SUMS self-exclusion gated at [12] |
| carried | F-S01-68-08: no shipped gate performs CI-1R | (NOTED at R27) | STILL OPEN, now load-bearing | build.py contains no register-regeneration gate (source read); F-S01-70-01 proves the missing gate matters |
| carried | F-S04-68-08: C-suffix ID grammar | v0.70 entry repair (5) claims CLOSED | NOT DISCHARGED -- claim byte-false | PB-4 landed; F-S01-70-02 |

## S-4 Amendment-entry claim audit (v0.70 entry; provenance ledger)

Provenance ledger over the v0.70 entry (gate [9c] counts, verified against my own parse): COMPUTED 16, EXTERNAL 0, ASSERTED 1, DISCLOSED 1, ENUMERATED 1. ASSERTED fraction (tagged claims, gate definition): 1/17 = 5.9%. **Headline: 2 of 16 COMPUTED tags are byte-false on the shipped bytes (mutation-verified below); the tag surface, not the tagged values, is where the residual Class A at String 6 lives.**

| # | Entry claim (tag) | Verdict | Evidence |
|---|---|---|---|
| (1) | Gate [13] rebuilt: bidirectional, severity-aware, declaration-context extraction, "not raw regex" [COMPUTED: build.py gate 13] | TRUE except "not raw regex" | build.py:748-789 read; PB-1/PB-3/PB-6 landed; PB-8 refutes "not raw regex" (F-S01-70-05) |
| (2) | R27 reports shipped in-packet and manifested; gate [13] fires [COMPUTED: sha256sum] | TRUE | 27/27 OK; gate fires; R27_REPORTS.txt == concatenation of the 4 packet reports (part-by-part diff, 4/4 MATCH) |
| (3) | Index rebuilt: 7 groups, 18 convergent, 21 noted [COMPUTED: extract_findings.py] | Counts TRUE; register text NOT derivable | Index recount: 7/18/21. But generate_register crashes on this index (F-S01-70-01) and the entry's own NOTED list enumerates 20 (F-S01-70-03) |
| (4) | CRITICAL remap removed; CRITICAL valid [COMPUTED: extract_findings.py] | TRUE at extractor; FALSE at register | PB-5 vs logs/11 (F-S01-70-04) |
| (5) | C-suffix pattern added; extractor/gate/register agree on ID grammar; closes F-S04-68-08 [COMPUTED: extract_findings.py] | BYTE-FALSE | PB-4 landed (F-S01-70-02); register_gen severity grammar disagrees (F-S01-70-04) |
| (6) | All shipped files manifested [COMPUTED: sha256sum] | TRUE | diff disk-vs-manifest, 27/27 OK |
| dispositions | 7 groups CLOSED as stated [COMPUTED: various] | Substance verified per S-3; presentation not reproducible | F-S01-70-01 |
| NOTED | "21 items" [COMPUTED: generate_register] | BYTE-FALSE (20 enumerated; tag cannot have produced it) | F-S01-70-03, F-S01-70-01 |
| boundaries | 35 items [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] | TRUE | All 35 BOUNDARIES.json item texts verbatim in the entry list |
| terminal | [COMPUTED: generate_terminal_line] | TRUE | "*End of XZ Protocol v0.70 draft candidate.*" present, gate [10h] PASS |
| PRIOR_HISTORY | "PRIOR_HISTORY c75a0ac4..." sentence | Value TRUE; UNTAGGED | Derivation matches; the sentence carries no provenance tag (F-S01-70-07) |

## S-5 Probe battery (all on byte copies with regenerated sums; canonical packet untouched)

Modelled adversary: careless/stale-context producer and self-consistent forger. Landed-assertion probes record hash before/after; benign and discrimination controls included.

| Probe | Class | Mutation / input | Expected | Observed | Verdict |
|---|---|---|---|---|---|
| PB-2 | Benign control | none (fresh copy, sums re-verified) | BUILD PASSED, gate [13] fires | rc=0, 39/39, 0/0/0 | Control valid |
| PB-1 | Landed assertion (direction 1) | deleted `### F-S01-68-01 -- HIGH ...` heading from R27_S01_REPORT.md (hash 42590199... -> 678a1a44...), resealed | gate [13] FAIL | rc=1, "FAIL: CI-8 phantom in index: 1 (F-S01-68-01)" | Gate discriminates |
| PB-3 | Landed assertion (severity) | S02 report heading "F-S02-68-01 — HIGH" -> "— LOW" (hash -> b554c6d2...), resealed | severity FAIL | rc=1, "FAIL: CI-8 severity mismatches: 1 (F-S02-68-01: report=LOW index=HIGH)" | Gate severity-aware |
| PB-6 | Landed assertion (direction 2) | injected F-S03-68-99 into index noted[], resealed | phantom FAIL | rc=1, "FAIL: CI-8 phantom in index: 1 (F-S03-68-99)" | Bidirectionality confirmed |
| PB-7 | Novel (version-lock vacuity) | index "version": "0.68" -> "0.70", resealed | must NOT pass vacuously | rc=1, "FAIL: CI-8 phantom in index: 39 (...)" | Fails CLOSED, not vacuous |
| PB-4 | Novel (ID-grammar asymmetry) | appended `### F-S01C-68-01 -- HIGH --` declaration to a report copy, resealed | gate [13] must FAIL (unindexed finding) | rc=0, BUILD PASSED; extractor total unchanged (12), C-suffix ID invisible | LANDED DEFECT (F-S01-70-02) |
| PB-5 | Claim verification | synthetic `### F-S02-68-97 -- CRITICAL --` | CRITICAL preserved | extracted with source_severity CRITICAL; no remap code in source | Claim (4) true at extractor |
| PB-8 | Novel-as-executed (pattern-4 surface; recurrent lineage F-S01-68-03) | prose lines: "Discussion of F-S03-68-77 LOW priority items", "For example a line like F-S03-68-78 MEDIUM would be a declaration." | context-free mentions must NOT be captured | both captured as declarations; cross-round and out-of-range-seat controls correctly rejected | LANDED DEFECT (F-S01-70-05) |
| RG-1 | Novel (CI-1R executability) | `python3 xz_protocol_register_gen.py r27_findings_index.json xz_protocol_boundaries.json 0.70` on SHIPPED bytes (read-only execution, no mutation) | register text | ValueError: "Group 5: source distribution is mixed (1 HIGH, 1 MEDIUM) or triage 'MEDIUM' diverges from majority 'HIGH', but no adjudication_receipt is provided." | LANDED DEFECT (F-S01-70-01) |
| RG-2 | Novel, stage 2 | index copy + exact canonical receipts injected for groups 5/7 | register text | ValueError: "Noted finding F-S01-68-04 missing required field 'substance'." | Second missing-field layer |
| RG-3 | Novel (severity grammar) | index copy + receipts + one CRITICAL source_severity | accepted per claim (4)/(5) | ValueError: "Invalid source_severity 'CRITICAL' in findings[] record F-S01-68-01." | LANDED DEFECT (F-S01-70-04) |

Void probes: none (every probe produced a discriminating output). Vacuity controls: PB-1/PB-3/PB-6/PB-7 prove gate [13] fires and fails on mutated inputs; PB-2 proves the shipped pair passes -- so PB-4's PASS is meaningful evidence of extractor blindness, not gate vacuity.

## S-6 String-by-string traversal

| String (positions) | Reached | Found |
|---|---|---|
| 1 -- Code Execution (1-3) | 1, 2, 3 | Clean on shipped bytes: 27/27 OK; 186 passed; 279 PASS / 0 FAIL. One cosmetic gate-print defect (F-S01-70-06, position 3, LOW). |
| 2 -- Register Verification (4-6) | 4, 5, 6 | Position 4 FAILS: register reproduction impossible on shipped bytes (F-S01-70-01, Class A). Position 5: 39 == 39 on shipped bytes; latent blindness to C-suffix IDs (F-S01-70-02). Position 6: 0 severity mismatches on shipped bytes; register-side CRITICAL grammar rejection (F-S01-70-04). |
| 3 -- Cross-Layer Consistency (7-10) | 7, 8, 9, 10 | Title v0.70 == VERSION; status tokens consistent; Section 0.1 current to v0.70; FB-7b current through R27. Clean. (The front-matter Status line repeats the byte-false "C-suffix added" claim -- folded into F-S01-70-02's locus list.) |
| 4 -- Adversarial Probing (11-14) | 11-14 via PB-1..PB-8, RG-1..RG-3 | Gate discriminates in both directions, fails closed on version-lock mutation; format surface defective (C-suffix blindness, pattern-4 over-capture). |
| 5 -- Temporal Integrity (15-17) | 15, 16; 17 NOT REACHED | 70/70 ENTRY seals; FULL_SECTION_27 match; PRIOR_HISTORY derivation matches shipped value. Position 17 (append-only vs HELD bytes) unreachable from a fresh seat -- boundary stated, not waived. |
| 6 -- Methodology Audit (18-21) | 18, 19, 20, 21 | Position 18: untagged sentences in the current entry (F-S01-70-07). Position 19: two byte-false [COMPUTED] tags + one byte-false count + one overstated "not raw regex" claim (F-S01-70-02/03/04/05). Position 20: seat-label drift (F-S01-70-08); methodology-corpus conflict 21-vs-24 positions and stale v0.69 key question (F-S01-70-09). Position 21: triage discipline is the lead's phase, outside seat scope -- noted. |
| body (22-24) | 22, 23 reached | Section 22.4 present with A-X1..A-X5; Sidrat clause present. Position 24 (the furqan) is the lead's. |

## S-7 Findings (mandatory format)

### F-S01-70-01 -- HIGH -- Class A -- String 2, position 4 (register reproduction)

- Finding ID: F-S01-70-01
- Severity: HIGH (class-to-severity mapping A=HIGH, boundary item 30)
- String: 2 (Register Verification). Cross-layer resonance: String 6, position 19 (the byte-false `[COMPUTED: generate_register]` tag); CI_METHODOLOGY.txt lists CI-1R among the String-1 scribes -- under either assignment the defect is outside String 6.
- Position: 4 (Generated register = shipped register, byte-exact)
- Class: A (byte-false claim on shipped bytes)
- Locus: packet/xz_protocol_register_gen.py lines 128 and 153 (validation raises); packet/r27_findings_index.json (missing `adjudication_receipt` on groups 5 and 7; missing `substance`/`disposition` on all 21 `unique_findings_noted` items); v0.70 entry NOTED paragraph tagged `[COMPUTED: generate_register]`.
- Substance: On the shipped bytes, `python3 xz_protocol_register_gen.py r27_findings_index.json xz_protocol_boundaries.json 0.70` raises `ValueError: Group 5: source distribution is mixed (1 HIGH, 1 MEDIUM) or triage 'MEDIUM' diverges from majority 'HIGH', but no adjudication_receipt is provided.` (logs/07_registergen.log). With exact canonical receipts injected into a COPY (probes/index_with_receipts.json), generation advances one layer and raises `ValueError: Noted finding F-S01-68-04 missing required field 'substance'.` (logs/08c_registergen_stage3.log). The v0.70 entry's register section is tagged as tool-produced and the CI specification (CI_METHODOLOGY.txt, "CI-1R (The Witness): register reproduction, byte-exact") presents byte-exact register reproduction as a standing scribe; on the shipped index the generator cannot run at all, and the shipped register text additionally lacks the `Source distribution:` clauses the generator always emits (compare the v0.64 entry's generated lines, which carry them). The register in the v0.70 entry was therefore not produced by the tagged scribe from the shipped index. No shipped gate performs CI-1R (F-S01-68-08, still open), so nothing catches this.
- Required repair: (a) add `adjudication_receipt` (exact canonical distribution string) to groups 5 and 7 and `substance`/`disposition` fields to all noted items in the index, or relax the generator's validation deliberately and disclose the relaxation; (b) regenerate the register from the repaired index and ship byte-exact output in the entry; (c) add a build gate that regenerates the register from the shipped index and compares byte-exact (close F-S01-68-08 as a class).
- Falsifier: the generation command above exits 0 on the shipped index and its stdout's register section is byte-identical to the entry's register section; a mutation of any index severity flips the gate to FAIL.

### F-S01-70-02 -- HIGH -- Class A -- String 6, position 19 (tag accuracy)

- Finding ID: F-S01-70-02
- Severity: HIGH
- String: 6 (Methodology Audit -- the byte-false claim lives in the v0.70 entry and the front-matter Status line). Latent resonance: String 2, position 5 (index cardinality would silently omit a continuous seat's findings).
- Position: 19 (a [COMPUTED] tag cites a scribe that did not produce the claimed behavior)
- Class: A
- Locus: v0.70 entry repair (5): "C-suffix seat identifier pattern added (F-SnnC-). Extractor, gate, and register now agree on the ID grammar. Closes F-S04-68-08. [COMPUTED: extract_findings.py]"; front-matter Status line: "C-suffix added". packet/extract_findings.py: line 26 `FINDING_ID_RE` carries `C?` but is never used; the five DECLARATION_PATTERNS (lines 31-42) are `F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?` with no `C?`.
- Substance: PB-4 (logs/pb4_csuffix.log): a report copy augmented with `### F-S01C-68-01 -- HIGH -- continuous-seat finding declaration (probe)` and resealed yields `extracted total: 12` (unchanged; C-suffix absent) and `BUILD PASSED` with gate [13] printing 39/39, 0 missing. A continuous seat's entire finding set would be invisible to the extractor, the gate, and the index. The claim that the grammar was unified, and the closure claim on F-S04-68-08, are byte-false.
- Required repair: add `C?` to all five declaration patterns (or route all matching through FINDING_ID_RE); add a gate [13] test fixture containing a C-suffix declaration.
- Falsifier: extractor on the PB-4 input returns F-S01C-68-01; gate [13] on the same input FAILs missing-from-index until the ID is indexed.

### F-S01-70-03 -- HIGH -- Class A -- String 6, position 19

- Finding ID: F-S01-70-03
- Severity: HIGH
- String: 6
- Position: 19 (tag/count accuracy); ungated aspect: gate [10e] checks convergence-group brackets only, never the NOTED count (Class D shadow)
- Class: A
- Locus: v0.70 entry: "NOTED (non-converging or deferred, 21 items): F-S01-68-04 MEDIUM, ... F-S04-68-17 INFORMATIONAL. [COMPUTED: generate_register]"
- Substance: The enumeration contains exactly 20 finding IDs (programmatic count, unique 20). The omitted ID is F-S04-68-08 -- the same ID repair (5) claims to close. The shipped r27_findings_index.json lists 21 noted items INCLUDING F-S04-68-08 (source_severity HIGH). So the entry's count (21) matches the index, its enumeration (20) does not, and its repair claim (5) contradicts both. One of the three surfaces is byte-false against the other two; as shipped, the count claim is false against the entry's own list.
- Required repair: make count == enumeration == index noted-set, and gate it (extend [10e] or a new gate to recompute the NOTED count from the index).
- Falsifier: a gate recomputes `len(unique_findings_noted)` and the enumerated list from the entry and compares all three; mutating any one flips the build to FAIL.

### F-S01-70-04 -- HIGH -- Class A -- String 6, position 19

- Finding ID: F-S01-70-04
- Severity: HIGH
- String: 6 (claim locus); latent String 2 (register validity)
- Position: 19
- Class: A
- Locus: v0.70 entry repair (4): "CRITICAL-to-HIGH silent remap removed. CRITICAL is a valid severity." and repair (5) "Extractor, gate, and register now agree on the ID grammar." packet/xz_protocol_register_gen.py line 22: `VALID_SEVERITIES = {"HIGH", "MEDIUM", "LOW", "INFORMATIONAL"}`.
- Substance: The extractor now accepts CRITICAL (PB-5, verified). The register generator does not: probe logs/11_critical_register_probe.log shows `register_gen REJECTS CRITICAL: ValueError: Invalid source_severity 'CRITICAL' in findings[] record F-S01-68-01.` The claimed grammar agreement is byte-false; any future CRITICAL finding makes the index unregistrable. Same claim sentence as F-S01-70-02, distinct technical root, distinct falsifier -- recorded separately per the Barzakh lineage question.
- Required repair: add CRITICAL to VALID_SEVERITIES and SEV_ORDER in register_gen; add a CRITICAL fixture to the test suites.
- Falsifier: an index containing a CRITICAL-severity finding generates without error and the severity survives byte-exact into the register.

### F-S01-70-05 -- MEDIUM -- Class A (claim) -- String 6, position 19; latent String 4, position 14

- Finding ID: F-S01-70-05
- Severity: MEDIUM (claim byte-false; operational direction is fail-CLOSED -- phantom declarations FAIL the build -- so availability noise, not silent pass)
- String: 6 primary; latent 4
- Position: 19 primary; 14 latent
- Class: A (the "(not raw regex)" claim); lineage: recurrence of R27 F-S01-68-03 (false-positive class, claimed closed by repair (1))
- Locus: v0.70 entry repair (1): "declaration-context extraction via shipped extract_findings.py (not raw regex)". packet/extract_findings.py line 39: pattern 4 `(F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?)\s*\(?(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b` -- optional paren, no declaration context, line-wise raw regex.
- Substance: PB-8 (logs/09_pb8_inline_pattern4.log): the prose line "Discussion of F-S03-68-77 LOW priority items continues here." and the quoted example "For example a line like F-S03-68-78 MEDIUM would be a declaration." are both captured as finding declarations. The docstring documents `F-SNN-VV-NN (SEVERITY)` with parentheses; the implementation makes the paren optional. Controls behaved (cross-round version and out-of-range seat correctly rejected). The "not raw regex" claim is byte-false; the R27 false-positive class is narrowed, not closed.
- Required repair: require the parenthesised form (make `\(` mandatory and add `\)`), or restrict pattern 4 to declaration contexts; add PB-8's lines as negative fixtures.
- Falsifier: PB-8's two prose lines extract zero findings while a true `F-SNN-VV-NN (SEVERITY)` declaration still extracts.

### F-S01-70-06 -- LOW -- Class D -- String 1, position 3

- Finding ID: F-S01-70-06
- Severity: LOW
- String: 1
- Position: 3 (build gates)
- Class: D (gate defect, cosmetic)
- Locus: packet/build.py lines 788-789.
- Substance: The gate [13] summary line is an unconditional print with literal zeros: `PASS: CI-8 cardinality: {n} in reports, {m} in index, 0 missing, 0 phantom, 0 severity mismatches` -- printed even when the constituent checks FAIL. Verbatim from PB-1 (a FAILING build, rc=1): "FAIL: CI-8 phantom in index: 1 (F-S01-68-01)" immediately followed by "PASS: CI-8 cardinality: 38 in reports, 39 in index, 0 missing, 0 phantom, 0 severity mismatches". The build still fails overall (errors list non-empty, rc=1), so soundness holds; the print is a false-green line inside failing output.
- Required repair: compute the summary line from the actual counts, or print it only when all three checks passed (and without the hardcoded PASS token otherwise).
- Falsifier: re-run PB-1; the summary line shows the real counts and no PASS token appears on a failing gate.

### F-S01-70-07 -- LOW -- Class D -- String 6, position 18

- Finding ID: F-S01-70-07
- Severity: LOW
- String: 6
- Position: 18 (tagging completeness -- "zero untagged sentences in current entry")
- Class: D (tagging discipline; the values stated are true)
- Locus: v0.70 entry: the sentence "PRIOR_HISTORY c75a0ac436cbc048bb11d601710ec39863b4d25e8b4d2179c54338e33f83c82c." carries no provenance tag; the lead-in lines "v0.70 repairs (from R27 four-seat audit):" and "R27 defect register disposition (from R27 four-seat audit, 7 convergence groups):" carry none.
- Substance: Methodology section 12 requires exactly one provenance tag per sentence in the amendment entry. Three sentences/lines in the v0.70 entry are untagged. No gate checks sentence-level tagging (gate [9c] validates tag references and counts, not coverage) -- the position-18 criterion is ungated.
- Required repair: tag the three lines ([COMPUTED: build.py gate 9b] fits the PRIOR_HISTORY line) or disclose a structural-line exemption explicitly; consider a coverage gate.
- Falsifier: every sentence in the next entry matches a tag pattern; an untagged-sentence fixture FAILs a coverage gate.

### F-S01-70-08 -- LOW -- Class E -- String 6, position 20

- Finding ID: F-S01-70-08
- Severity: LOW
- String: 6
- Position: 20 (dispatch fidelity)
- Class: E (process); lineage: recurrence of F-S01-68-12 (R27) and earlier rounds
- Locus: DISPATCH.txt line 2: "Model: Claude Opus 5 | Role: ADVISORY (producer-family)"; executing thread is Kimi K3, Moonshot.
- Substance: The dispatch header's model field names a model this thread does not hold -- same drift as R27 (documented in the R27 S01 report as the sixth consecutive round for S01). The R27 S01 report's handling (state the discrepancy, execute the held seat, take the namespace from the dispatch) is followed again. Cross-witness dispatch identity (9/10 byte-identical) is not verifiable from a single seat; stated as scope limit.
- Required repair: producer-side dispatch generation should bind the model field to the actual seat assignment, or the drift should be disclosed as a standing boundary.
- Falsifier: the R29 S01 dispatch header's model field matches the executing seat's identity declaration.

### F-S01-70-09 -- HIGH -- Class A -- String 6, position 20

- Finding ID: F-S01-70-09
- Severity: HIGH
- String: 6
- Position: 20 (dispatch fidelity / corpus consistency)
- Class: A (two normative documents in the same shipment contradict on the round's coordinate system; at least one is byte-false)
- Locus: METHODOLOGY.txt (header: "Twenty-Four Verification Positions"; section 3: "Seven Layers, Seven Witnesses, Twenty-Four Positions"; "This document is the canonical methodology for all rounds from R28 onward") vs DISPATCH.txt line 3 and AUDIT_CONTEXT.txt ("Six Strings, Twenty-One Positions (v7)"; positions 1-21; confinement defined over positions 18-21 of 21). Additionally METHODOLOGY.txt section 15: "The key question at R28: does v0.69 achieve Goedel confinement?" -- R28 audits v0.70 (DISPATCH.txt line 7: "R28 audits v0.70 bytes"); the shipped methodology's key question is stale by one version.
- Substance: The dispatch instructs "Classify every finding by string and position. The triage needs coordinates." The shipment carries two incompatible coordinate systems (21 positions over six strings vs 24 positions over seven layers; the methodologies disagree even on whether layer 7/positions 22-24 exist). This report classifies under the dispatch's six-string/21-position scheme (dispatch is authoritative); the conflict itself is reported as a finding on the corpus. The stale v0.69 key-question sentence compounds it.
- Required repair: align METHODOLOGY.txt to the six-string/21-position v7 model (or re-issue the dispatch corpus under one scheme) and update section 15 to v0.70.
- Falsifier: one methodology document in the R29 shipment, internally consistent on position count, with the current version in its key-question sentence.

## S-8 Barzakh self-check (three questions per finding)

| Finding | Authority (tier) | Methodology (position criterion met?) | Lineage |
|---|---|---|---|
| F-S01-70-01 | Tool output, Tier 1 (executed tracebacks, verbatim) | Yes -- position 4 criterion (byte-exact reproduction) fails by crash | Novel as executed at R28; root rhymes with R22's noted-crash (F-S01-63-03 class) but distinct locus and cause |
| F-S01-70-02 | Tool output, Tier 1 (PB-4 landed + benign/discrimination controls) | Yes -- position 19 (tag cites scribe that cannot produce the value) | Recurrent surface (extractor grammar), new axis (C-suffix); R27's F-S04-68-08 claimed closed -- closure refuted |
| F-S01-70-03 | Tool output, Tier 1 (programmatic count) | Yes -- position 19 | Recurrent class (count-list divergence; R16 count-list invariant) |
| F-S01-70-04 | Tool output, Tier 1 (probe logs/11) | Yes -- position 19 | Same claim sentence as F-S01-70-02, distinct root (severity set) -- kept separate |
| F-S01-70-05 | Tool output, Tier 1 (PB-8 with negative controls) | Yes -- position 19 claim-level; consequence fail-closed | Recurrence of F-S01-68-03 (false-positive class), narrowed not closed |
| F-S01-70-06 | Tool output, Tier 1 (verbatim failing-build log) | Yes -- position 3 cosmetic | Novel (this print shape) |
| F-S01-70-07 | Tool output, Tier 1 (entry text read; absence verified by inspection) | Yes -- position 18 | Recurrent class (tagging discipline; R22 F-S02-63-02 family) |
| F-S01-70-08 | Shipped bytes + executor identity, Tier 1/2 | Yes -- position 20 | Recurrent (F-S01-68-12 and prior) |
| F-S01-70-09 | Shipped bytes, Tier 1 (verbatim quotes of both documents) | Yes -- position 20 | Novel as a corpus conflict; staleness axis recurrent |

No finding rests on methodology-corpus narration alone; every Class A above carries executed evidence on the shipped bytes.

## S-9 Prediction scorecard -- results

| # | Prediction | Score | Evidence |
|---|---|---|---|
| P1 | sha256sum all OK (HIGH) | HELD | 27/27 OK, rc=0 |
| P2 | pytest 186 GREEN (HIGH) | HELD | 186 passed, rc=0 |
| P3 | build 0 FAIL (HIGH) | HELD | 279 PASS, 0 FAIL, rc=0 |
| P4 | Gate [13] FIRES (HIGH) | HELD | Fires on shipped R27 reports |
| P5 | Gate [13] 0 missing / 0 phantom (HIGH) | HELD | Independently reproduced via shipped extractor |
| P6 | Gate [13] 0 severity mismatches (HIGH) | HELD | Independently reproduced |
| P7 | 70 ENTRY seals verify (HIGH) | HELD | 70/70 recomputed match |
| P8 | PRIOR_HISTORY derivation matches (HIGH) | HELD | Derived == shipped; held-anchor impossible (fresh seat, stated) |
| P9 | Section 22.4 present (HIGH) | HELD | A-X1..A-X5 + Sidrat clause present |
| P10 | If Class A, ONLY at String 6 (MEDIUM) | REFUTED | F-S01-70-01 is Class A at String 2, position 4 |
| P11 | Zero Class A at String 1 (HIGH) | HELD | String-1 surfaces clean; F-S01-70-06 is cosmetic Class D |
| P12 | H = 1.0 continues (MEDIUM) | HELD | Class A present (6 findings) |
| P13 | Section 0.1 current to v0.70 (HIGH) | HELD | "PENDING RE-CARRY on v0.70 bytes" |
| P14 | FB-7b current through R27 (HIGH) | HELD | Trajectory ends "R27 (v0.68): 4 seats, all HALTed" |
| P15 | All shipped files manifested (HIGH) | HELD | disk == manifest + self; self-exclusion gated |
| E1 | Class A present (seat, Laplace 0.957) | HELD | -- |
| E2 | Residual defects at the repair boundary | HELD | F-S01-70-01/02/04 all live in the v0.70 repair machinery (index rebuild, extractor grammar) |
| E3 | Shipped report/index pair consistent AND gate fires | HELD | 39/39 both directions; gate fires |

Score: 14 HELD, 1 REFUTED (P10) of P1-P15; seat expectations 3/3 HELD.

## S-10 Verdict, key-question answer, Bearer 4 assessment

**Verdict: HALT.**

**Key question -- does v0.70 achieve Goedel confinement (every Class A at positions 18-21, zero at 1-17)? NO.** F-S01-70-01 is a Class A defect at String 2, position 4: the register shipped in the v0.70 entry cannot be reproduced from the shipped index -- the tagged scribe crashes on the shipped bytes, and no gate performs CI-1R. Confinement requires zero Class A outside String 6; one suffices to refute. The remaining Class A findings (F-S01-70-02/03/04/05, F-S01-70-09) do live at String 6 -- the tagging/corpus surface, exactly where the methodology predicts the defect migrates -- but the register-reproduction crash is not self-referential tagging; it is a String-2 scribe failure.

**Bearer 4: FALSE (not merely UNDER TEST).** The v0.70 repair closed every R27 String-1 gate-logic defect on the shipped fixtures (bidirectionality, severity-awareness, vacuity -- all probe-verified), and Strings 3 and 5 are clean on shipped bytes. But the confinement-repair build introduced a new String-2 defect in its own repair machinery: the rebuilt index does not satisfy the shipped register generator's validation, and the register text presented as scribe output is not scribe output. The defect migration pattern (code -> structure -> provenance -> automation -> prose) continues: the defect now lives in the automation's data schema, one layer below the tagging surface.

Severity totals: 5 HIGH (F-S01-70-01, -02, -03, -04, -09), 1 MEDIUM (F-S01-70-05), 3 LOW (F-S01-70-06, -07, -08). Class A: 6. Class D: 2. Class E: 1.

H = 1.0 continues: R7-R28, 22/22. Laplace P(Class A at R29) = 23/24 = 0.9583.

**Boundary report (D-3.8):** the outermost uncomputed layer this round is CI-1R itself -- register reproduction is claimed as a scribe but executed by no gate (F-S01-68-08 open since R27). What would bring it inside: a build gate that runs xz_protocol_register_gen.py on the shipped index and compares the entry's register section byte-exact, plus the index schema repairs of F-S01-70-01. Position 17 (append-only against held bytes) remains unreachable from fresh seats; a continuous seat holding the v0.69 HISTORY.sha256 must anchor PRIOR_HISTORY (c75a0ac4...) against held bytes.

**Re-audit conditions for R29 (v0.71):** (1) re-run F-S01-70-01's generation command on the new shipped index -- must exit 0 and match the entry byte-exact; (2) re-run PB-4 (C-suffix) -- extractor must capture and the gate must fail until indexed; (3) re-run PB-8 -- prose mentions must not extract; (4) count the NOTED enumeration against the index noted-set; (5) feed a CRITICAL finding through register_gen; (6) check the dispatch header's model field against the executing seat; (7) check the methodology corpus for one coordinate system and a current key-question version.

**Self-corrections ledger:** none owed -- fresh seat, no prior reports from this thread this round.

---

## Appendix A -- Standing values (recomputed, verbatim)

- PACKET_SHA256SUMS: 27 members, 27 OK, 0 FAILED (auditor re-run; final post-probe re-check below)
- ENTRY seals: 70/70 recomputed match
- FULL_SECTION_27: 2208f04715313e4201880a8da672e7ca3786a3ac7690078863cd66ed64bfa286
- PRIOR_HISTORY: c75a0ac436cbc048bb11d601710ec39863b4d25e8b4d2179c54338e33f83c82c (derivation MATCH; no held-file anchor -- fresh seat)
- manifest digest (12 code files): 3d6326ca4980e038... (matches xz_protocol_trust_roots_PUBLIC.json)
- build.py: 279 PASS, 0 FAIL, rc=0; pytest: 186 passed, rc=0; gate [13]: 39 in reports, 39 in index, 0/0/0
- S-0/S-1 freeze: sha256 893ae33dcf430f46664ddc169edd366b713d31d4a301be9796ed0a51b373edaf (frozen before the v0.70 entry was opened)
- Unsealed tail after the Provenance marker: 850 chars

Per the program's no-seal-equality rule, these are recomputed standing values for the producer to compare against its retained sealed values; equality is the producer's to assert, not this seat's.

## Appendix B -- Final post-probe integrity re-check

Executed after all probing and report assembly, canonical packet dir:

```
$ sha256sum -c PACKET_SHA256SUMS   ->   27 lines, all ": OK", rc=0   (probe caches removed; disk set == manifest set + manifest self)
```

Probe and log evidence preserved under /mnt/agents/output/xz_r28_v070_s01/ (logs/, probes/); the canonical packet bytes were never modified (all sabotage on copies with regenerated sums).

---

*R28, v0.70. Seat S01 (executing: Kimi K3, Moonshot). The record is the evidence. The foam vanishes; what benefits the people remains.*

######_REPORT_SPLIT_######
# Source: SHIPPED_R28_S02_REPORT.md
# XZ Protocol v0.70 — R28 Audit Report — Seat S02 Execution

**Report file:** `XZ_v070_R28_S02_GPT56_SOL_REPORT.md`
**Audited package:** `XZ_v070_R28_S02.zip`
**Audited version:** v0.70
**Round:** R28
**Execution date:** 2026-08-17
**Actual executing family:** GPT-5.6 Sol (OpenAI)
**Dispatch-declared family/role:** Kimi K3 / CARRYING (binding)
**Mode:** FRESH substrate audit
**Verdict:** **HALT**
**Key-question answer:** **NO — v0.70 does not achieve Goedel confinement.**

---

## S-0. Identity, mode, execution surface

The dispatch identifies this packet as **S02 / Kimi K3 / CARRYING**. The actual executing model is **GPT-5.6 Sol**. The protocol itself states at §22.1 that GPT-5.6 Sol is retained as an adversarial record but does not count toward the two-family carrying requirement. Accordingly, this report is technically dispositive as an audit of the bytes, but it **cannot be counted as a Kimi-family carrying witness** and does not advance Bearer 5.

The 10-file outer dispatch package was unpacked. `EXECUTABLE_PACKET.txt` was deserialized exactly by the shipped extraction procedure, then the canonical copies were created:

- `PROTOCOL_v070.txt` → `xz_protocol_v0_70.md` (byte-identical)
- `FINDINGS_INDEX.txt` → `r27_findings_index.json` (byte-identical)
- `BOUNDARIES.txt` → `xz_protocol_boundaries.json` (byte-identical)

The executable packet contains 28 serialized members, one of which is `PACKET_SHA256SUMS`. The manifest contains 27 entries and intentionally omits itself.

---

## S-1. Prediction scorecard (P1–P15)

| Pred. | Result | Evidence |
|---|---|---|
| P1 | **PASS** | `sha256sum -c PACKET_SHA256SUMS`: 27/27 listed members OK. |
| P2 | **PASS** | Canonical pytest command: **186 passed**. |
| P3 | **PASS** | `python3 build.py`: **279 PASS, 0 FAIL; BUILD PASSED**. |
| P4 | **PASS** | Gate [13] executed on four shipped `R27_Sxx_REPORT.md` files; it did not skip. |
| P5 | **PASS on shipped corpus** | 39 report IDs, 39 index IDs, 0 missing, 0 phantom. Missing/phantom mutation probes both fail closed. |
| P6 | **PASS on shipped corpus** | 0 severity mismatches. Severity-mutation probe fails closed. |
| P7 | **PASS** | All **70/70 ENTRY seals** verify; FULL_SECTION_27 also verifies. |
| P8 | **PASS** | PRIOR_HISTORY derivation succeeds and matches the shipped value. |
| P9 | **PASS** | Section 22.4 is present with A-X1 through A-X5 and the irreducible-residual disclosure. |
| P10 | **FAIL** | Class A exists outside String 6: Findings 70-01 through 70-05 include Strings 1–3. |
| P11 | **FAIL** | String 1 is not Class-A clean: the v0.70 “declaration-context extraction” repair claim is false on the shipped extractor and Gate [13] path. |
| P12 | **PASS** | Class A is present at R28, so the R7–R28 recurrence remains present; H remains 1.0 for the binary recurrence series. |
| P13 | **FAIL** | Section 0.1 still says “seventy amendment entries, v0.1 through v0.69”; the actual record has 70 entries through v0.70. |
| P14 | **PASS** | FB-7b trajectory is extended through R27 and current status token is v0.70. |
| P15 | **FAIL (literal claim)** | 28 executable-packet members exist but only 27 are manifested; `PACKET_SHA256SUMS` is intentionally excluded from itself. “All shipped files manifested / zero unmanifested members” is unqualified and false. |

**Prediction score: 11 / 15.**

---

## S-2. Byte verification — String 1, positions 1–3

### Position 1 — packet integrity

Canonical manifest verification:

```text
27/27 listed manifest members: OK
```

Independent serialized-member census:

```text
EXECUTABLE_PACKET members: 28
PACKET_SHA256SUMS entries: 27
Unmanifested serialized member: PACKET_SHA256SUMS
Phantom manifest members: 0
```

This does **not** invalidate P1: every member the manifest lists hashes correctly. It **does** invalidate the stronger v0.70 entry/P15 claim that *all shipped files* are manifested and that there are *zero unmanifested members*.

### Position 2 — test suite

Canonical command:

```text
pytest -q test_xz_protocol_kernel.py \
  test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py \
  test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py \
  xz_protocol_phase_a_tests.py
```

Result:

```text
186 passed
```

### Position 3 — build gates

Canonical build result:

```text
PASS lines: 279
FAIL lines: 0
BUILD PASSED: all checks GREEN
```

Gate [13] on the shipped corpus:

```text
PASS: CI-8 missing from index: 0 ()
PASS: CI-8 phantom in index: 0 ()
PASS: CI-8 severity mismatches: 0 ()
PASS: CI-8 cardinality: 39 in reports, 39 in index, 0 missing, 0 phantom, 0 severity mismatches
```

The canonical green state is genuine. The adversarial probe results in S-5 show that two specific repair claims about the extractor are nevertheless false.

---

## S-3. Prior-round finding discharge — R27 convergence groups

| R27 group | v0.70 discharge | R28 assessment |
|---|---|---|
| 1. Gate [13] vacuous / skip-as-green | Reports now ship and Gate [13] fires | **PARTIAL/CLOSED for vacuity**, but the same repair paragraph falsely claims declaration-context extraction; see F-S02-70-01. |
| 2. Section 0.1 stale + FB-7b stale | PENDING token and FB-7b row updated | **PARTIAL**: FB-7b is current, but Section 0.1 still carries a stale entry-range statement; see F-S02-70-03. |
| 3. One-directional, severity-blind, false-positive Gate [13] | Set equality and severity comparison landed | **PARTIAL**: bidirectionality and severity landed; false-positive declaration-context bug remains; see F-S02-70-01. |
| 4. Convergence semantically misbound | Index rebuilt to 7 groups / 18 convergent / 21 noted | **CLOSED on inspected bytes**. |
| 5. CRITICAL→HIGH silent remap | Remap removed | **CLOSED**. Direct CRITICAL probes preserve CRITICAL. |
| 6. Gate-count overstatement | Context says 279; canonical build emits 279 PASS lines | **CLOSED**. |
| 7. Unmanifested shipped files | Prior unmanifested payload files are now listed | **INSTANCE CLOSED, CLAIM OVERSTATED**: the new “all shipped files / zero unmanifested members” sentence ignores the manifest’s mandatory self-exclusion; see F-S02-70-05. |

Notably, the R27 **C-suffix ID grammar defect was NOTED rather than one of the seven convergence groups**, but v0.70 expressly claims it is closed. That repair did not land in the actual extraction patterns; see F-S02-70-02.

---

## S-4. Amendment-entry claim audit — v0.70 entry

The v0.70 amendment entry is sealed and the protocol file is manifested. Its substantive repair claims were checked against the current source.

### Claims that verify

- Four R27 report files are shipped inside the executable packet and manifested.
- Gate [13] fires on those shipped report files.
- The shipped index has 7 convergence groups, 18 convergent findings, and 21 noted findings.
- CRITICAL is preserved as CRITICAL by the extractor.
- Missing/phantom set equality is implemented.
- Per-ID severity comparison is implemented.
- Canonical build count is 279 PASS / 0 FAIL.

### Claims that do not verify

1. **“declaration-context extraction … (not raw regex)”** — false. `extract_findings.py` line 39 contains a fallback pattern matching bare `F-Snn-vv-id HIGH` text anywhere on a line. Inline prose and blockquoted references are extracted as declarations.
2. **“C-suffix seat identifier pattern added … Extractor, gate, and register now agree”** — false. The generic ID regex and register accept `SnnC`, but every `DECLARATION_PATTERNS` regex at lines 33–41 omits `C?`; the extractor therefore drops a real `F-S02C-68-99` declaration and Gate [13] remains green.
3. **“All shipped files manifested … Zero unmanifested members”** — false without an explicit self-manifest exception. The executable serialization has 28 members and the manifest has 27 entries; `PACKET_SHA256SUMS` is the unmanifested member by design.
4. **Section 0.1 currentness** — false as a whole. Protocol line 22 says “seventy amendment entries, v0.1 through v0.69,” while the build counts 70 entries through v0.70.
5. **“Methodology: v7 canonical (six strings)”** in the protocol Status line — contradicted by the shipped `METHODOLOGY.txt`, whose canonical architecture is seven layers / twenty-four positions and whose own text describes the current corrected form as v6 and still asks whether v0.69 achieves confinement.

---

## S-5. Probe battery — landed assertion + benign control

### A. Canonical control

**Input:** untouched shipped packet.
**Expected:** Gate [13] fires and passes.
**Observed:** PASS; 39 reports / 39 index / 0 missing / 0 phantom / 0 severity mismatch.
**Assessment:** control passes.

### B. Bidirectional missing-ID probe

**Mutation:** remove real `F-S01-68-04` from the index.
**Observed:** build rc=1; Gate [13] reports one missing ID.
**Assessment:** bidirectional missing detection landed.

### C. Bidirectional phantom-ID probe

**Mutation:** add phantom `F-S02-68-99` to the index.
**Observed:** build rc=1; Gate [13] reports one phantom ID.
**Assessment:** phantom detection landed.

### D. Severity-fidelity probe

**Mutation:** change `F-S01-68-01` source severity from HIGH to LOW in the index.
**Observed:** build rc=1; Gate [13] reports one severity mismatch.
**Assessment:** severity fidelity landed.

### E. C-suffix landed-assertion probe

Direct extractor input:

```text
### F-S02C-68-99 — HIGH — synthetic continuous-seat declaration
```

Observed extractor output:

```text
{}
```

Then the same declaration was appended to a report file without adding it to the index. If C-suffix support were actually landed, Gate [13] should detect one missing report finding and fail. Instead:

```text
RC=0
PASS: CI-8 cardinality: 39 in reports, 39 in index, 0 missing, 0 phantom, 0 severity mismatches
BUILD PASSED
```

**Assessment:** **landed assertion fails.** This is F-S02-70-02.

### F. Benign inline-reference control

Direct extractor input:

```text
This sentence merely cites F-S02-68-99 HIGH as an example, not as a finding declaration.
```

Observed extractor output:

```text
F-S02-68-99 => HIGH
```

A quoted-reference form is also extracted. Appending the benign inline sentence to a report causes Gate [13] to fail with a fake missing finding:

```text
RC=1
FAIL: CI-8 missing from index: 1 (F-S02-68-99)
```

**Assessment:** **benign control fails.** This is F-S02-70-01.

### G. Gate-summary truthfulness probe

On missing, phantom, and severity mutations, the gate correctly emits a specific `FAIL:` line and the build exits nonzero, but line 788–789 unconditionally prints:

```text
PASS: CI-8 cardinality: ... 0 missing, 0 phantom, 0 severity mismatches
```

For example, the missing-ID mutation prints both:

```text
FAIL: CI-8 missing from index: 1 (F-S01-68-04)
PASS: CI-8 cardinality: 39 in reports, 38 in index, 0 missing, 0 phantom, 0 severity mismatches
```

**Assessment:** detection is fail-closed, but the summary line is internally false on failure paths. See F-S02-70-06.

---

## S-6. String-by-string traversal

| String | Positions | Reached? | Result |
|---|---:|---|---|
| **1 — Code Execution** | 1–3 | Yes | Canonical checks green, but Class A repair claim survives at Position 3; packet-manifest overclaim also lands at Position 1. |
| **2 — Register Verification** | 4–6 | Yes | Shipped 39↔39 cardinality/severity is green, but the C-suffix parser/gate grammar remains incomplete and can silently omit a legitimate report finding (Position 5). |
| **3 — Cross-Layer Consistency** | 7–10 | Yes | **Class A present**: Status-methodology mismatch (P8) and stale Section 0.1 entry range (P9). |
| **4 — Adversarial Probing** | 11–14 | Yes | Missing/phantom/severity probes fail closed. C-suffix and benign-inline probes expose parser defects; gate summary is false on failure paths. |
| **5 — Temporal Integrity** | 15–17 | Yes | 70/70 entry seals, FULL_SECTION_27, and PRIOR_HISTORY all verify. |
| **6 — Methodology Audit** | 18–21 | Yes | Tagging remains incomplete as already disclosed; dispatch/methodology architecture also diverges. This is not the only defect surface. |
| **Body** | axiom / sidrat / furqan | Yes | Section 22.4 and Sidrat disclosure present. Furqan remains the lead’s decision. |

Because Class A is present at positions **1, 3, 5, 8, and 9**, confinement to positions 18–21 is refuted.

---

## S-7. Findings

### F-S02-70-01

- **Finding ID:** F-S02-70-01
- **Severity:** HIGH
- **String:** 1 — Code Execution
- **Position:** 3 — Build gates
- **Class:** A — byte-false mechanism/repair claim
- **Locus:** `xz_protocol_v0_70.md` line 1621: “declaration-context extraction … (not raw regex)”; `extract_findings.py` lines 38–41, especially line 39; docstring lines 50–53 promises exclusion of inline references and quoted examples.
- **Substance:** The shipped extractor still contains a fallback regex that matches a bare finding ID followed by a severity anywhere on a line. A benign inline reference and a blockquoted reference are both extracted as findings. Appending such benign text to a report makes Gate [13] falsely fail. Therefore the sealed v0.70 repair claim that declaration-context extraction closes the false-positive class is false on the shipped implementation.
- **Required repair:** Remove or structurally constrain the bare fallback. Require an explicit finding declaration context (heading, defined bold declaration form, or exact table row) and add negative fixtures for prose, quotations, probe tables, and cross-reference lists.
- **Falsifier:** `extract_from_report("This cites F-S02-68-99 HIGH as an example", version_filter="68") == {}`; quoted forms also return `{}`; real heading declarations continue to extract; canonical and benign-control builds both remain rc=0.

### F-S02-70-02

- **Finding ID:** F-S02-70-02
- **Severity:** HIGH
- **String:** 2 — Register Verification
- **Position:** 5 — Index cardinality
- **Class:** A — byte-false repair claim
- **Locus:** `xz_protocol_v0_70.md` line 1625: “C-suffix seat identifier pattern added (F-SnnC-). Extractor, gate, and register now agree”; `extract_findings.py` lines 26–28 accept `C?` generically, but declaration patterns at lines 33–41 all use `F-S\d{2}-` without `C?`.
- **Substance:** C-suffix support was added only to generic ID/seat regexes, not to the actual declaration patterns used by `extract_from_report`. A valid `### F-S02C-68-99 — HIGH — ...` declaration is dropped. When that declaration is appended to a shipped report without an index entry, Gate [13] still reports 39↔39 and BUILD PASSED. The extractor, gate, and register therefore do not agree on the ID grammar.
- **Required repair:** Add `C?` consistently to every declaration regex and add end-to-end Gate [13] tests using a continuous-seat finding in heading, bold, table, and bracket declaration formats.
- **Falsifier:** All supported `F-SnnC-...` declaration forms extract with correct seat/severity; a report-only C-suffix finding causes Gate [13] missing-from-index failure; the same ID in the index/report pair passes.

### F-S02-70-03

- **Finding ID:** F-S02-70-03
- **Severity:** HIGH
- **String:** 3 — Cross-Layer Consistency
- **Position:** 9 — Section 0.1
- **Class:** A — byte-false count/range claim
- **Locus:** `xz_protocol_v0_70.md` line 22: “The full defect trajectory is in Section 27 (seventy amendment entries, v0.1 through v0.69).” Build gate [9] independently counts 70 entries and verifies v0.70 exists.
- **Substance:** `v0.1` through `v0.69` contains 69 versioned entries and excludes the current v0.70 entry. The same sentence says “seventy amendment entries.” Thus Section 0.1 is not fully current to v0.70 even though its PENDING RE-CARRY token is current. Gate [9] only searches for the phrase “seventy amendment entries” somewhere in the protocol and does not bind the stated range endpoint to VERSION.
- **Required repair:** Change the Section 0.1 range to `v0.1 through v0.70` (or explicitly distinguish 69 prior entries + current v0.70), and add a gate that parses the Section 0.1 range endpoint and asserts it equals VERSION.
- **Falsifier:** Section 0.1 count and range parse to exactly 70 entries ending in v0.70; mutating the endpoint to v0.69 makes build fail.

### F-S02-70-04

- **Finding ID:** F-S02-70-04
- **Severity:** HIGH
- **String:** 3 — Cross-Layer Consistency
- **Position:** 8 — Status line
- **Class:** A — contradicted methodology/status claim
- **Locus:** `xz_protocol_v0_70.md` line 5 says “Methodology: v7 canonical (six strings).” `DISPATCH.txt` line 3 and `AUDIT_CONTEXT.txt` lines 5–16 repeat six strings / twenty-one positions. `METHODOLOGY.txt` lines 3, 66–76, and 154 onward state the canonical R28 architecture is **seven layers / twenty-four positions**; line 62 calls the corrected form **v6**; lines 359–361 still target **v0.69** for R28.
- **Substance:** The shipped packet contains mutually incompatible declarations of the governing methodology’s version, architecture, position count, and R28 target version. The protocol Status line’s “v7 canonical (six strings)” is therefore not consistent with the shipped canonical methodology it names.
- **Required repair:** Select one canonical methodology/version and propagate it byte-consistently across `METHODOLOGY.txt`, protocol Status, `DISPATCH.txt`, `AUDIT_CONTEXT.txt`, and `CI_METHODOLOGY.txt`. Add a deterministic token/parity gate for methodology version, layer/string count, position count, and target protocol version.
- **Falsifier:** All five surfaces parse to one identical methodology version, one architecture, one position count, and v0.70 target; any single-surface mutation causes build/dispatch validation failure.

### F-S02-70-05

- **Finding ID:** F-S02-70-05
- **Severity:** HIGH
- **String:** 1 — Code Execution
- **Position:** 1 — Packet integrity
- **Class:** A — byte-false manifest-closure claim
- **Locus:** `xz_protocol_v0_70.md` lines 1626 and 5: “All shipped files manifested … Zero unmanifested members” / “all files manifested.” `EXECUTABLE_PACKET.txt` deserializes to 28 members. `PACKET_SHA256SUMS` contains 27 entries. `build.py` lines 732–733 explicitly require that `PACKET_SHA256SUMS` **not list itself**.
- **Substance:** Manifest verification is internally sound for the 27 listed payload members, but the stronger closure claim is literally false: the shipped manifest file is itself a serialized packet member and is intentionally unmanifested. The self-exclusion is reasonable; the unqualified “all/zero” prose is not.
- **Required repair:** Replace the claim with “all manifestable payload members other than `PACKET_SHA256SUMS` itself are manifested” and make the exception explicit, or introduce an external dispatch-level manifest if literal all-file closure is required.
- **Falsifier:** Serialized-member set minus the explicitly declared self-manifest exception equals the manifest filename set exactly; the prose states that exception and no longer claims zero absolute unmanifested members.

### F-S02-70-06

- **Finding ID:** F-S02-70-06
- **Severity:** MEDIUM
- **String:** 4 — Adversarial Probing
- **Position:** 12 — Parity probe
- **Class:** B — concealed output inconsistency
- **Locus:** `build.py` lines 774–789. The three `check(...)` calls correctly emit failures, but line 788 unconditionally prints a `PASS:` summary with hard-coded zeros.
- **Substance:** On missing, phantom, or severity-mismatch mutations, Gate [13] prints both a correct `FAIL:` and a false `PASS: ... 0 missing, 0 phantom, 0 severity mismatches` summary. Exit status remains fail-closed, so the control function is not bypassed, but the emitted audit log is self-contradictory and machine consumers can ingest the wrong summary.
- **Required repair:** Compute the actual counts into the summary and prefix the aggregate line `FAIL` or neutral `RESULT` whenever any constituent predicate fails.
- **Falsifier:** Each mutation produces no false PASS aggregate; reported counts equal the actual set/severity differences and rc remains nonzero.

### F-S02-70-07

- **Finding ID:** F-S02-70-07
- **Severity:** LOW
- **String:** 6 — Methodology Audit
- **Position:** 18 — Tagging completeness
- **Class:** C — disclosed limitation
- **Locus:** `METHODOLOGY.txt` lines 299–310 requires exactly one provenance tag per amendment-entry sentence and zero untagged sentences. The v0.70 entry at protocol line 1618 contains multiple sentences after one `[ASSERTED]` tag; line 1626 has two sentences after one `[COMPUTED]` tag. `AUDIT_CONTEXT.txt` explicitly enters R28 with Bearer 7 FALSE: “Tagging incomplete; the Goedel surface.”
- **Substance:** The sentence-level tagging criterion is not satisfied. This is not treated as a concealed Class A because the audit context explicitly discloses tagging incompleteness, but it keeps Bearer 7 FALSE.
- **Required repair:** Tag each sentence exactly once and add a current-entry sentence-level tag-completeness gate rather than only tag counting.
- **Falsifier:** A parser over the current entry reports zero untagged and zero multiply-tagged sentences; build fails on a deliberately untagged sentence.

### F-S02-70-08

- **Finding ID:** F-S02-70-08
- **Severity:** INFORMATIONAL
- **String:** 6 — Methodology Audit
- **Position:** 20 — Dispatch fidelity
- **Class:** E — process observation
- **Locus:** `DISPATCH.txt` identifies S02 as Kimi K3 / CARRYING. Actual executor is GPT-5.6 Sol. Protocol §22.1 states GPT is adversarial-only and does not count toward two-family carry.
- **Substance:** This report cannot truthfully be credited as the Kimi-family binding carrying witness named by the dispatch. Technical byte findings remain valid; witness-family accounting must use the actual executor.
- **Required repair:** Route the S02 carrying packet to Kimi K3, or relabel this execution/report as GPT-5.6 Sol advisory/adversarial and obtain a separate eligible carrying report.
- **Falsifier:** The recorded report family matches the actual executing family and Bearer-5 accounting excludes ineligible GPT execution.

---

## S-8. Barzakh self-check

| Finding | Authority — “Who is your Lord?” | Method — “What is your religion?” | Lineage — “Where does this come from?” | Survives Barzakh? |
|---|---|---|---|---|
| 70-01 | Tier 1 source + executed benign probe | String 1 P3; resonance at adversarial format parsing | Direct recurrence of R27 false-positive extractor surface | **YES** |
| 70-02 | Tier 1 source + executed C-suffix probe + end-to-end build | String 2 P5; resonance at String 4 P14 | Direct recurrence of F-S04-68-08, claimed closed | **YES** |
| 70-03 | Tier 1 protocol bytes + build entry census | String 3 P9 | Recurrence of Section 0.1 staleness in a new field | **YES** |
| 70-04 | Tier 1 cross-file byte comparison | String 3 P8; resonance at String 6 P20 | New R28 methodology-propagation divergence | **YES** |
| 70-05 | Tier 1 serialized-member/manifest census | String 1 P1 | R27 manifest-closure class; prior payload instances fixed, self-exclusion prose overclaim remains | **YES** |
| 70-06 | Tier 1 executed missing/phantom/severity mutations | String 4 P12 | New output-semantics defect in rebuilt gate | **YES** |
| 70-07 | Tier 1 current-entry text + explicit audit-context disclosure | String 6 P18 | Recurrent tagging incompleteness, explicitly disclosed | **YES, non-Class-A** |
| 70-08 | Session identity + protocol governance rule | String 6 P20 | Recurrent routing/witness-family drift | **YES, informational** |

No finding above depends on producer authority. Findings 70-01 through 70-06 are independently falsifiable from the shipped bytes and local execution.

---

## S-9. Prediction scorecard results

**Passed:** P1, P2, P3, P4, P5, P6, P7, P8, P9, P12, P14.
**Refuted:** P10, P11, P13, P15.
**Score:** **11 / 15**.

The most consequential refutations are P10/P11/P13: Class A remains below String 6, including code/register/cross-layer surfaces. P15 is additionally false as literally written because the manifest self-exclusion is not stated.

---

## S-10. Verdict, key-question answer, and Bearer 4 assessment

# VERDICT: HALT

**Key question: Does v0.70 achieve Goedel confinement (Bearer 4)?**
**Answer: NO. Bearer 4 = FALSE.**

Confinement requires every Class A finding to live only at positions 18–21 and zero Class A at positions 1–17. R28 finds Class A at:

- **String 1 / Position 3:** false “declaration-context extraction” repair claim.
- **String 2 / Position 5:** C-suffix finding silently omitted from extractor/Gate [13].
- **String 3 / Position 9:** Section 0.1 count/range stale at v0.69.
- **String 3 / Position 8:** protocol Status says v7/six strings while shipped canonical methodology says seven layers/twenty-four positions and internally describes v6/v0.69.
- **String 1 / Position 1:** unqualified “all shipped files manifested / zero unmanifested members” contradicted by the manifest’s intentional self-exclusion.

Therefore the defect surface is **not confined to String 6**. The R28 Class A recurrence remains present, so the binary R7–R28 recurrence series remains all-present and H remains 1.0.

### Bearer assessment

| Bearer | R28 S02 assessment | Basis |
|---|---|---|
| 1. Append-only | **TRUE** | 70/70 entry seals, FULL_SECTION_27, PRIOR_HISTORY all verify. |
| 2. Code correctness | **TRUE under the methodology’s narrow gate/test predicate** | 186/186 tests green and canonical build green; however adversarial probes expose untested extractor behavior. |
| 3. Surface narrowing | **FALSE** | Class A persists in Strings 1–3 rather than only String 6. |
| 4. Goedel confinement | **FALSE** | Multiple Class A findings at positions 1–9. |
| 5. Cross-vendor witness | **FALSE / not advanced here** | Actual executor is GPT, not eligible Kimi carrying witness; no current two-family non-HALT established by this report. |
| 6. Axiom disclosure | **TRUE** | Section 22.4 present with A-X1–A-X5 and Sidrat residual. |
| 7. Methodology verification | **FALSE** | Tagging incomplete; methodology/dispatch architecture inconsistent. |
| 8. The furqan | **UNKNOWN / lead** | Human sufficiency judgment remains outside this seat. |

**Bearer state from this execution: 3 TRUE / 4 FALSE / 1 UNKNOWN.**

### Minimum repair set before R29 re-carry

1. Fix declaration extraction so inline/quoted references are negative controls.
2. Add `C?` to every declaration format and end-to-end C-suffix Gate [13] tests.
3. Bind Section 0.1 amendment-range endpoint to VERSION.
4. Reconcile canonical methodology version/architecture/position count across all dispatch surfaces.
5. Qualify manifest closure with the self-manifest exception, or externally manifest the manifest.
6. Make Gate [13] aggregate summary truthful on failure paths.
7. If Bearer 7 is to advance, enforce sentence-level provenance tagging mechanically.
8. Obtain an actually eligible non-producer carrying execution for S02/Bearer-5 accounting.

---

**Final:** **HALT. Goedel confinement not achieved. Bearer 4 remains FALSE.**

######_REPORT_SPLIT_######
# Source: SHIPPED_R28_S03_REPORT.md
# XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S03

**VERDICT: HALT (ADVISORY)**. Goedel confinement is NOT achieved at v0.70. Two distinct Class A (byte-false) defects remain outside the self-referential tagging surface, squarely in String 1 (Code Execution) and String 4 (Adversarial Probing). The headline repairs claimed in the v0.70 entry are byte-false: Gate `[13]` claims to be "fail-closed" but silently skips as green when reports are absent, and the extractor claims to unify the `C`-suffix grammar but hardcodes its absence in the exact patterns used for extraction. The defect trajectory extends to 22/22 (H = 1.0).

---

## S-0: Identity, Mode, and Execution Surface

*   **Seat Identity:** S03 (Gemini). Note: The R28 dispatch for S03 lists "GPT-5.6 Sol", continuing the seat-label drift identified in R26/R27. I execute this seat as Gemini.
*   **Mode:** FRESH.
*   **Execution Surface:** Full verification executed against canonical v0.70 shipped bytes and artifacts, including `build.py`, `extract_findings.py`, and `r27_findings_index.json`.

---

## S-1: Prediction Scorecard

Evaluated against the shipped v0.70 bytes:

| # | Prediction | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **P1** | `sha256sum -c` all OK (HIGH) | **CONFIRMED** | 27/27 OK per tool output. |
| **P2** | `pytest` 6 suites GREEN (HIGH) | **CONFIRMED** | 186 passed. |
| **P3** | `build.py` 0 FAIL (HIGH) | **CONFIRMED** | 279 PASS check-lines executed. |
| **P4** | Gate `[13]` FIRES on shipped reports (HIGH) | **CONFIRMED** | Report files now shipped in-packet. |
| **P5** | Gate `[13]` bidirectional: 0 missing/phantom (HIGH) | **CONFIRMED** | 39 in reports, 39 in index, 0 missing/phantom. |
| **P6** | Gate `[13]` severity-aware: 0 mismatches (HIGH) | **CONFIRMED** | 0 severity mismatches. |
| **P7** | All 70 ENTRY seals verify (HIGH) | **CONFIRMED** | Evaluated as 70/70 OK. |
| **P8** | `PRIOR_HISTORY` derivation matches (HIGH) | **CONFIRMED** | Derived correctly against seal chain. |
| **P9** | Section 22.4 present (HIGH) | **CONFIRMED** | Present in protocol body. |
| **P10** | If Class A, ONLY at String 6 (MEDIUM) | **FALSIFIED** | Class A found in String 1 / Pos 3 and String 4 / Pos 14. |
| **P11** | Zero Class A at String 1 (HIGH) | **FALSIFIED** | Gate `[13]` logic and `extract_findings.py` regex contain byte-false implementations. |
| **P12** | H = 1.0 continues (MEDIUM) | **CONFIRMED** | Class A present; streak unbroken. |
| **P13** | Section 0.1 current to v0.70 (HIGH) | **CONFIRMED** | Prose repaired at v0.69, carried to v0.70. |
| **P14** | FB-7b trajectory current through R27 (HIGH) | **CONFIRMED** | Prose repaired at v0.69, carried to v0.70. |
| **P15** | All files manifested in `PACKET_SHA256SUMS` (HIGH) | **CONFIRMED** | 27/27 closure achieved. |

---

## S-2: Byte Verification

Direct verification of String 1, positions 1-3 confirms:
*   **Pos 1 (The Record):** `sha256sum -c PACKET_SHA256SUMS` yields 27/27 OK, confirming manifest closure for the previously unmanifested index files.
*   **Pos 2 (The Test):** `pytest` yields 186 GREEN across the 6 canonical suites.
*   **Pos 3 (The Pattern):** `build.py` yields 279 PASS check-lines and 0 FAIL. However, this "GREEN" status conceals a fatal logic flaw in Gate `[13]`, detailed in S-7.

---

## S-3: Prior-Round Finding Discharge

Evaluating R27 convergence groups and triage claims against v0.70 bytes:
1.  **Gate `[13]` Rebuild:** The triage claims Gate `[13]` is "fail-closed". This is **FALSE**. The code explicitly bypasses failure on missing inputs.
2.  **ID Grammar Unification:** The claim "Extractor, gate, and register now agree on the ID grammar" (Closes F-S04-68-08) is **FALSE**. The `DECLARATION_PATTERNS` in `extract_findings.py` reject the `C`-suffix entirely.
3.  **Prose Staleness (Section 0.1 & FB-7b):** Carried repairs verified. Current to v0.70.

---

## S-4: Amendment-Entry Claim Audit

The v0.70 entry claims to achieve "Goedel confinement (Bearer 4)" by migrating all Class A defects strictly to the self-referential tagging surface (String 6). This claim is byte-false. The core automation tools (`build.py` and `extract_findings.py`) still contain byte-false implementations of their declared repairs, placing Class A squarely in Strings 1 and 4.

---

## S-5: Probe Battery

| Probe | Mutation / Input | Expected | Observed | Landed? |
| :--- | :--- | :--- | :--- | :--- |
| **M1 (Vacuity Test)** | Delete `*_REPORTS.md` files from CWD | `BUILD FAILED` (fail-closed constraint) | `BUILD PASSED`; Gate `[13]` prints `(no report files -- CI-8 gate skipped)` | **NO.** Gate remains fail-open. |
| **M2 (C-Suffix Capture)** | Inject synthetic `### F-S03C-70-99 -- HIGH --` | Extractor captures ID | Dropped entirely. Regex misses `C`. | **NO.** ID grammar not unified. |

---

## S-6: String-by-String Traversal

*   **String 1 (Low E - Code Execution):** Reached Pos 1-3. **DEFECT FOUND.** Gate `[13]` skips rather than failing when inputs are absent.
*   **String 2 (A - Register Verification):** Reached Pos 4-6. Index matching passes on shipped bytes.
*   **String 3 (D - Cross-Layer Consistency):** Reached Pos 7-10. Section 0.1 and FB-7b prose are current.
*   **String 4 (G - Adversarial Probing):** Reached Pos 11-14. **DEFECT FOUND.** The extractor regex `DECLARATION_PATTERNS` hardcode the exclusion of continuous seats.
*   **String 5 (B - Temporal Integrity):** Reached Pos 15-17. Manifest closure achieved.
*   **String 6 (High E - Methodology Audit):** Reached Pos 18-21. Tagging discipline is overshadowed by fundamental L1/L4 failures.

---

## S-7: Findings

### F-S03-70-01
*   **Severity:** HIGH
*   **String:** 1 (Code Execution)
*   **Position:** 3 (Build Gates)
*   **Class:** A (byte-false)
*   **Locus:** `build.py` lines 848-852; R27 Triage Convergence Group 1.
*   **Substance:** The R27 triage explicitly claims Gate `[13]` is "fail-closed". However, `build.py` implements an `else` branch that prints `(no report files -- CI-8 gate skipped)` and `[DISCLOSED] Gate [13] requires report files...` without invoking `check(False, ...)`. If the report files are missing, the build silently skips the gate and emits `BUILD PASSED`. This is the exact vacuity failure identified in R27, disguised by an unverified disclosure print.
*   **Required repair:** Replace the `else` branch prints in `build.py` with `check(False, "CI-8 gate: no report files present")`. Absence is not green.
*   **Falsifier:** Deleting the report files must result in a hard `BUILD FAILED` with a non-zero exit code.

### F-S03-70-02
*   **Severity:** HIGH
*   **String:** 4 (Adversarial Probing)
*   **Position:** 14 (Format Probe)
*   **Class:** A (byte-false)
*   **Locus:** `extract_findings.py` lines 26-31 (`DECLARATION_PATTERNS`); AUDIT_CONTEXT.txt claim (5).
*   **Substance:** AUDIT_CONTEXT claims "Extractor, gate, and register now agree on the ID grammar" regarding the `C`-suffix. While `FINDING_ID_RE` was updated to `F-S\d{2}C?`, the actual `DECLARATION_PATTERNS` used to scrape the Markdown text hardcode `(F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?)` without the optional `C?`. Consequently, any continuous seat (e.g., `F-S01C-70-01`) will be completely ignored during declaration extraction.
*   **Required repair:** Update all five `DECLARATION_PATTERNS` in `extract_findings.py` to include `C?` immediately following `\d{2}`.
*   **Falsifier:** Injecting `### F-S01C-70-99 -- HIGH -- Test` into a report file must successfully extract into the JSON index.

---

## S-8: Barzakh Self-Check

| Question | Assessment |
| :--- | :--- |
| **Q1 (Authority):** | Both findings rely on Tier 1 evidence: direct code execution and regex verification against shipped bytes. |
| **Q2 (Methodology):** | F-S03-70-01 meets Pos 3 failure (Gate vacuity). F-S03-70-02 meets Pos 14 failure (Format blindspot). |
| **Q3 (Lineage):** | Both are novel manifestations of R27 defects explicitly claimed "CLOSED" in the v0.70 documentation. |

---

## S-9: Prediction Scorecard Results

The primary assertion of v0.70 was Goedel confinement—that the only remaining Class A defects would reside in String 6 (the self-referential tagging surface). **Prediction P10 is conclusively FALSIFIED.** Structural, byte-false defects persist in the core automation scripts at String 1 and String 4.

---

## S-10: Verdict and Key-Question Answer

**VERDICT: HALT.**

**Answer to Key Question:** Does v0.70 achieve Goedel confinement (Bearer 4)? **NO.**

The migration of the defect to String 6 failed because the mechanisms built to secure Strings 1 and 4 contain byte-false implementation logic. Gate `[13]` is not fail-closed, and the extractor still cannot read continuous-seat identifiers. Because these defects reside in the code layer and contradict explicit documentation claims, Bearer 4 remains FALSE. The methodology requires a HALT. Return to producer.

######_REPORT_SPLIT_######
# Source: SHIPPED_R28_S04_REPORT.md
# XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S04

**VERDICT: HALT.** Goedel confinement is NOT achieved at v0.70. Bearer 4 remains FALSE. Class A is live at String 1 (2 findings), String 2 (3 findings), and String 3 (3 findings). Zero Class A at String 6. Class A recurrence extends to 22/22 (R7-R28), H = 1.0. Laplace P(Class A at R29) = 23/24 = 0.958.

The round's structural result is not that a repair failed. It is that **two build gates ([2f] and [10i]) now enforce byte-false claims and fail when the true claim is substituted**, proven by mutation on shipped bytes. The verification layer has begun manufacturing the defects it exists to detect.

---

## S-0 Identity, mode, execution surface

- **Seat:** S04, per DISPATCH.txt and the mandated output filename.
- **Dispatch label vs. executor:** DISPATCH.txt names **Gemini 3.1 Pro, Mode FRESH, no prior context, no held bytes**. This seat was executed by **Claude Opus 5**. Seat-label drift, sixth consecutive occurrence in the S04 lineage (see F-S04-70-16).
- **FRESH is nominal, not actual.** This executor carries persistent cross-session memory of the R7-R27 lineage. The dispatch's independence assumption does not hold for this seat. Declared, not waived. Findings below were derived byte-first: extraction, tool execution, and all ten probes preceded any consultation of lineage material, and every finding cites a locus in the shipped bytes rather than a prior-round recollection.
- **Mode:** **A (substrate verifier).** Packet extracted per AUDIT_CONTEXT.txt; `sha256sum`, `build.py`, `pytest`, `extract_findings.py`, and ten mutation probes executed in this environment. Substrate-claim verification confidence: **high** for shipped bytes, **reduced** for cross-version claims.
- **Environment:** Linux container, Python 3.12.3. `pytest` was **absent at intake** and installed by this seat (9.1.1). Consequence recorded at F-S04-70-18.
- **Held bytes:** NONE. No v0.69 or v0.68 packet held. PRIOR_HISTORY verified for internal derivation only; **boundary item 32 (self-consistent resealing) is undetectable from this seat this round.** Stated as a limitation, not waived.
- **Producer bar:** Producer is Claude Opus 4.6 (BARRED). This seat is Opus 5. Family separation is by version only; a same-family advisory reading is the conservative one, and HALT is binding under either.
- **Probe hygiene:** All mutations ran on copies under `/tmp/p*`. The canonical packet directory passed `sha256sum -c PACKET_SHA256SUMS` 27/27 OK after all probing.

---

## S-1 Prediction scorecard (declared before findings)

Predictions P1-P15 were taken from DISPATCH.txt and evaluated against shipped bytes. Results in S-9.

---

## S-2 Byte verification (String 1, positions 1-3)

| Scribe | Command | Result |
|---|---|---|
| The Record | `sha256sum -c PACKET_SHA256SUMS` | **27/27 OK** |
| The Pattern | `python3 build.py` | **279 PASS, 0 FAIL, BUILD PASSED** |
| The Test | 6 suites, explicit invocation | **186 passed** |
| The Witness | `[9b]` seal + PRIOR_HISTORY derivation | **70/70 ENTRY seals, FULL_SECTION_27 match, PRIOR_HISTORY `c75a0ac4...` derived** |

Extraction produced **28 files**; 27 are manifested. The unmanifested member is `PACKET_SHA256SUMS` itself (F-S04-70-14).

Out-of-packet dispatch copies verified byte-identical to their manifested members:

| Dispatch file | Packet member | Result |
|---|---|---|
| `PROTOCOL_v070.txt` | `xz_protocol_v0_70.md` | IDENTICAL (462298 bytes) |
| `FINDINGS_INDEX.txt` | `r27_findings_index.json` | IDENTICAL (8117 bytes) |
| `BOUNDARIES.txt` | `xz_protocol_boundaries.json` | IDENTICAL (2664 bytes) |

Section 27 structure: **70 amendment entries, v0.1 through v0.70**, no duplicates, ascending. `HISTORY.sha256`: 70 ENTRY lines + FULL_SECTION_27 + PRIOR_HISTORY = 72 lines. Cardinality gate: 70 == 70.

Gate [11] coverage measurement on these bytes: body 108108 chars, semantic-gate coverage **30.0%**; Section 27 **76.6% ungated**. The claim surface remains predominantly ungated by construction.

---

## S-3 Prior-round finding discharge (R27 convergence groups)

The v0.70 entry and `r27_findings_index.json` both mark all seven R27 convergence groups CLOSED. Independent assessment on shipped bytes:

| Group | Surface | Producer disposition | This seat |
|---|---|---|---|
| 1 | Gate [13] vacuous / skip-as-green | CLOSED "fail-closed" | **NOT CLOSED.** Gate fires only because reports are currently shipped; the gate itself remains fail-open. F-S04-70-03 |
| 2 | Section 0.1 stale, FB-7b terminates R18 | CLOSED | **CLOSED IN PART.** FB-7b now terminates at R27 (v0.68), correct. Section 0.1 carries a new byte-false range. F-S04-70-07 |
| 3 | Gate [13] one-directional, severity-blind | CLOSED | **CLOSED.** Verified by three mutation probes; all three axes land. |
| 4 | R26 convergence misbound in index | CLOSED | **CLOSED.** Index groups reconcile to reports: 18 convergent + 21 noted = 39; gate [13] 39/39. |
| 5 | CRITICAL-to-HIGH silent remap | CLOSED | **CLOSED for the remap.** CRITICAL is a valid severity in `SEVERITY_RE` and all five declaration patterns. |
| 5b | C-suffix ID grammar (F-S04-68-08) | CLOSED | **NOT CLOSED. Phantom repair.** F-S04-70-01 |
| 6 | Gate count overstated (256 vs 240) | CLOSED | **CLOSED.** No gate-count claim survives in the protocol body; count is tool-derived at build time. |
| 7 | Unmanifested files ship | CLOSED | **CLOSED IN PART.** Zero unmanifested packet members except the manifest itself. F-S04-70-14 |

Regression check on retired surfaces: the append-only chain, boundary-count enumeration ([2h] 35 == 35), finding-ID uniqueness ([10b] 18/18), and register-index coupling ([10c], [10d]) all hold. No absorption-induced regression detected at previously retired loci.

---

## S-4 Amendment-entry claim audit (v0.70 entry)

The v0.70 entry makes six repair claims and disposes seven convergence groups plus a NOTED list. Claim-by-claim:

| Claim | Tag | Verdict |
|---|---|---|
| (1) Gate [13] bidirectional, severity-aware, extractor-based | [COMPUTED] | **TRUE** on all three axes (probes 2, 3) |
| (2) R27 reports shipped and manifested; gate fires | [COMPUTED] | **TRUE** on these bytes; contingent, not enforced (F-S04-70-03) |
| (3) Index rebuilt: 7 groups, 18 convergent, 21 noted | [COMPUTED] | **TRUE** of the index; the entry's own NOTED list contradicts it (F-S04-70-04) |
| (4) CRITICAL remap removed | [COMPUTED] | **TRUE** |
| (5) C-suffix pattern added; extractor/gate/register agree | [COMPUTED] | **FALSE on shipped bytes** (F-S04-70-01) |
| (6) All shipped files manifested; zero unmanifested members | [COMPUTED] | **FALSE as stated**; true of members other than the manifest (F-S04-70-14) |
| "NOTED (non-converging or deferred, 21 items)" | [COMPUTED: generate_register] | **FALSE**; 20 enumerated (F-S04-70-04) |
| "Disclosed standing boundaries -- 35 items" | [ENUMERATED: 35] | **TRUE**; matches `xz_protocol_boundaries.json` |
| Front matter: "confinement repair build from v0.69 R27 audit" | (untagged) | **FALSE**; R27 audited v0.68 (F-S04-70-08) |
| Section 0.1: "seventy amendment entries, v0.1 through v0.69" | (untagged) | **FALSE and internally impossible** (F-S04-70-07) |

The entry's opening sentence -- "R27 returned 4/4 HALT on **v0.68** bytes" -- directly contradicts the front-matter Status line thirteen hundred lines above it. Both ship sealed in the same file.

---

## S-5 Probe battery

Ten probes. Each pairs a landed assertion with a benign control where the surface admits one.

| # | Probe | Expected | Observed | Reading |
|---|---|---|---|---|
| 1 | Remove 4 report files, keep manifest lines | fail | FAIL x4 at manifest-member-exists | Protection comes from the manifest gate, not gate [13] |
| 1b | Remove reports **and** their manifest lines | fail | **BUILD PASSED, all checks GREEN** | Gate [13] is **fail-open** |
| 2 | Delete `F-S02-68-02` from index | fail | FAIL: missing 1 | Bidirectionality lands |
| 3 | Add phantom `F-S02-68-99`; flip `F-S01-68-01` HIGH to LOW | fail | FAIL: phantom 1; FAIL: severity 1 | Phantom + severity axes land |
| 4 | **Benign control:** trailing newline in `R27_S03_REPORT.md` + manifest resync | pass | BUILD PASSED, 39/39 | No false positive |
| 5 | **Correct** Section 0.1 range to `v0.1 through v0.70` | pass | **FAIL: Section 22.2 carried-entry bound at VERSION-1** | Gate [10i] rejects the true claim |
| 6 | In-place mutate carried entry v0.12 | fail | FAIL x3: ENTRY seal, FULL_SECTION_27, PRIOR_HISTORY | Append-only chain sound |
| 7 | Corrupt the **sealed** terminal line to v0.99 | fail | FAIL: ENTRY_v0.70 seal, FULL_SECTION_27 | Sealed terminus protected |
| 8 | Rewrite the **unsealed tail** terminal line to v0.42 | fail | **BUILD PASSED**; `[10h] PASS: Terminal line matches v0.70` | Last visible line is ungated |
| 9 | Declare `### F-S05C-70-01 -- HIGH --`; control `F-S05-70-02` | both extract | C-suffix **not extracted**; control extracted | C-suffix repair is phantom |
| 10 | **Correct** Status provenance to `from v0.68 R27 audit` | pass | **FAIL: Status provenance v0.68 == v0.70 - 1** | Gate [2f] rejects the true claim |

Probes 5 and 10 are the round's centre of gravity. In both, substituting the **true** claim for the shipped false one breaks the build.

---

## S-6 String-by-string traversal

| String | Layer | Positions | Reached | Result |
|---|---|---|---|---|
| 1 (Low E) | Code Execution | 1-3 | yes | **Class A x2.** Code layer is no longer clean. Six-round clean streak (R22-R27) ends at R28. |
| 2 (A) | Register Verification | 4-6 | yes | **Class A x3.** Fail-open claim, NOTED count, dual disposition. |
| 3 (D) | Cross-Layer Consistency | 7-10 | yes | **Class A x3.** Section 0.1, Section 22.2, front-matter Status. |
| 4 (G) | Adversarial Probing | 11-14 | yes | **Class D x2.** Two gates enforce false claims. |
| -- | Mercy gap | -- | -- | Technique change observed: the defect at Strings 1-3 is no longer logic error but *claim about logic*. |
| 5 (B) | Temporal Integrity | 15-17 | yes | **Class D x1.** Unsealed terminal line. Seals, ordering, PRIOR_HISTORY otherwise sound. |
| 6 (High E) | Methodology Audit | 18-21 | yes | **Zero Class A.** Two Class C/E items only (F-S04-70-14, -16). |
| body | Axioms, Sidrat, furqan | -- | disclosed | Section 22.4 present, five axioms, irreducible residual disclosed. Not tested. |

**The R27 prediction inverted.** R27 forecast the defect would remain in prose and packaging. Prose defects persist (String 3), but the code layer re-opened -- and it re-opened in the *self-referential* mode that String 6 was supposed to monopolise: a repair that names itself, a gate that narrates its own result. String 1 and String 6 are the same note at different octaves. At v0.70 the octave collapsed downward rather than upward.

---

## S-7 Findings

### F-S04-70-01 [CRITICAL] -- C-suffix seat-ID repair never entered the extractor (phantom repair)

- **String:** 1 (Code Execution) | **Position:** 2 | **Class:** A (byte-false)
- **Locus:** `extract_findings.py:32-42` (`DECLARATION_PATTERNS`); claim at `xz_protocol_v0_70.md`, v0.70 entry, repair (5); AUDIT_CONTEXT.txt repair (5).
- **Substance:** All five declaration patterns match `F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?`. None accepts the C suffix. The `C?` token appears only in module-level `FINDING_ID_RE` (which is never referenced after definition -- one occurrence in the file) and in `SEAT_RE` (applied *after* a match is already made). The entry's claim -- "C-suffix seat identifier pattern added (F-SnnC-). Extractor, gate, and register now agree on the ID grammar. Closes F-S04-68-08" -- is false of the shipped bytes. Probe 9: `### F-S05C-70-01 -- HIGH -- test finding` extracts nothing; the control `### F-S05-70-02 -- HIGH --` extracts. Operationally, any continuous seat dispatched at R29 with C-suffix IDs is invisible to gate [13]: absent from both sides of the comparison, the gate reports clean.
- **Required repair:** Add `C?` after `S\d{2}` in all five `DECLARATION_PATTERNS`. Delete or wire in `FINDING_ID_RE`.
- **Falsifier:** `python3 -c "import extract_findings as e; print(e.extract_from_report('### F-S05C-70-01 -- HIGH -- x','t.md',version_filter='70'))"` returns a non-empty dict.
- **Cross-reference:** F-S04-68-08 (claimed closed by this repair); phantom-repair class first proven at R7/v0.48.

### F-S04-70-02 [HIGH] -- Gate [13] summary line narrates three hardcoded zeros

- **String:** 1 | **Position:** 3 | **Class:** A
- **Locus:** `build.py`, gate [13] terminal `print`: `f"  PASS: CI-8 cardinality: {len(report_fids)} in reports, {len(index_fids)} in index, 0 missing, 0 phantom, 0 severity mismatches"`.
- **Substance:** The first two values are computed; the last three are string literals inside a bare `print`, not a `check()`. Probe 2: with one finding removed from the index the build correctly FAILs *and the same line still prints* "0 missing, 0 phantom, 0 severity mismatches" beside a live count of 38-vs-39. AUDIT_CONTEXT.txt reproduces this exact line under the heading "Build status (tool-derived, not narrated)". The line is narrated. This is the Axiom-3 narration-from-memory class inside the automation that was built to end it.
- **Required repair:** Interpolate the three counts, or delete the summary line and let the three `check()` calls speak.
- **Falsifier:** Re-run probe 2; the summary line must report `1 missing`.
- **Cross-reference:** R19/R20 mechanism-claim Class A; F-S01-68-01 lineage.

### F-S04-70-03 [HIGH] -- Gate [13] is fail-open; the shipped "fail-closed" adjudication is false

- **String:** 2 (Register Verification) | **Position:** 4 | **Class:** A
- **Locus:** `r27_findings_index.json`, `convergence_groups[0].triage_adjudication`: "Gate [13] rebuilt: bidirectional, severity-aware, extractor-based, **fail-closed**. Reports shipped in-packet." Mechanism at `build.py` gate [13] `else` branch.
- **Substance:** The `else` branch prints `(no report files shipped -- CI-8 cardinality gate cannot fire)` and a `[DISCLOSED]` note. It calls no `check()` and appends no error. Probe 1b: with the four reports deleted and their four manifest lines removed, the build returns **BUILD PASSED: all checks GREEN**. The R27 skip-as-green defect is structurally intact; it is masked only by the contingent fact that the reports are manifest members this round. A producer who ships no reports at v0.71 reproduces R27 exactly, and nothing fails.
- **Required repair:** Replace the `else` branch with `check(False, "CI-8 gate requires report files")`, or add a build-time assertion that at least one `R*_REPORT.md` is a manifest member.
- **Falsifier:** Re-run probe 1b; build must FAIL.
- **Cross-reference:** F-S01-68-01 / F-S02-68-01 / F-S04-68-01 (group 1, claimed CLOSED).

### F-S04-70-04 [HIGH] -- NOTED count byte-false: 21 claimed, 20 enumerated

- **String:** 2 | **Position:** 5 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md`, v0.70 entry: "NOTED (non-converging or deferred, **21 items**): F-S01-68-04 ... F-S04-68-17. [COMPUTED: generate_register]".
- **Substance:** The enumerated list contains 20 finding IDs. `r27_findings_index.json.unique_findings_noted` contains 21. The omitted ID is `F-S04-68-08`. The claim carries a `[COMPUTED]` provenance tag; on shipped bytes the count and the list disagree, so at most one of them was computed. No gate covers the NOTED count: [10e] verifies convergence brackets only, [10b] covers the 18 convergent IDs only, and [9e] Cardinal-range consistency emitted **no checks at all** on these bytes (boundary item 23, silent vacuity).
- **Required repair:** Restore `F-S04-68-08` to the list or correct the count to 20; extend [10e] to assert `len(enumerated NOTED ids) == len(index.unique_findings_noted)`.
- **Falsifier:** Gate output shows a NOTED-count check that fires when the tally is desynchronised.
- **Cross-reference:** F-S04-70-05; count-list invariant class at R16/v0.57.

### F-S04-70-05 [HIGH] -- `F-S04-68-08` holds two contradictory dispositions in one sealed entry

- **String:** 2 | **Position:** 6 | **Class:** A
- **Locus:** v0.70 entry repair (5) ("Closes F-S04-68-08") vs. `r27_findings_index.json.unique_findings_noted[12]` (`convergence_group: null`) and the entry's own NOTED framing.
- **Substance:** The same finding ID is simultaneously declared CLOSED by a landed repair and filed as a non-converging deferred item. Because it is absent from the entry's enumerated NOTED list, the contradiction is invisible to a reader of either surface alone. One of the two dispositions is false; on the evidence of F-S04-70-01, the CLOSED one is.
- **Required repair:** Reclassify `F-S04-68-08` as OPEN pending the real C-suffix repair, and state its disposition once, in one canonical position.
- **Falsifier:** Grep of the shipped bytes returns exactly one disposition for the ID.
- **Cross-reference:** F-S04-70-01, F-S04-70-04; substrate-of-record uniqueness (no "settled and pending" duplication).

### F-S04-70-06 [HIGH] -- Section 22.2 carried-entry bound stale at v0.68

- **String:** 3 (Cross-Layer Consistency) | **Position:** 8 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md:718`: "For carried entries (**v0.1 through v0.68**), the PRIOR_HISTORY derivation in build.py [9b] detects retroactive mutation".
- **Substance:** At v0.70 the carried set is v0.1 through v0.69; v0.70 is the current entry. The bound was correct at v0.69 and was not advanced. Section 22.3 one line above **was** advanced ("v0.38-v0.69"), so this is a single-locus miss, not a convention change. Gate [10i] is named for this exact bound and passes anyway -- see F-S04-70-09.
- **Required repair:** Advance to "v0.1 through v0.69".
- **Falsifier:** `grep -c "v0.1 through v0.68" xz_protocol_v0_70.md` returns 0 outside Section 27.
- **Cross-reference:** Section 22.2/22.3 version-token staleness, R17/v0.58 recurrence.

### F-S04-70-07 [HIGH] -- Section 0.1 entry range is internally impossible

- **String:** 3 | **Position:** 7 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md:22`: "The full defect trajectory is in Section 27 (**seventy amendment entries, v0.1 through v0.69**)."
- **Substance:** Section 27 contains 70 entries spanning v0.1 through v0.70 (verified: 70 headings, 70 ENTRY seals, no duplicates). Seventy entries cannot span v0.1 to v0.69, which is sixty-nine. The count is right and the terminus is stale, so the sentence is false on its face without reference to any other document. P13 (Section 0.1 current to v0.70) fails on this locus.
- **Required repair:** "seventy amendment entries, v0.1 through v0.70". Note that this correction **breaks the build** until F-S04-70-09 is repaired.
- **Falsifier:** Terminus token equals VERSION and entry count equals the span.
- **Cross-reference:** F-S04-70-09 (the gate that forbids the repair); group 2 (claimed CLOSED at v0.69).

### F-S04-70-08 [HIGH] -- Front-matter Status attributes R27 to the wrong audited version

- **String:** 3 | **Position:** 9 | **Class:** A
- **Locus:** `xz_protocol_v0_70.md:5`: "**Status:** v0.70 DRAFT CANDIDATE -- confinement repair build from **v0.69** R27 audit (4/4 HALT; 4-seat round)."
- **Substance:** R27 audited v0.68. Four independent shipped surfaces say so: `r27_findings_index.json` (`"version": "0.68"`), the FB-7b row ("R27 (v0.68): 4 seats, all HALTed"), AUDIT_CONTEXT.txt ("Prior: R27 on v0.68"), and the v0.70 entry's own first sentence ("R27 returned 4/4 HALT on v0.68 bytes"). v0.69 was an unaudited interim prose-repair build. The Status line and the entry contradict each other inside one sealed file.
- **Required repair:** "confinement repair build from v0.68 R27 audit", or a reworded provenance clause that names both the audited version and the interim build. Note this correction **breaks the build** until F-S04-70-10 is repaired.
- **Falsifier:** Status provenance version equals the `version` field of the shipped findings index.
- **Cross-reference:** F-S04-70-10; front-matter Status staleness class at R16/v0.57.

### F-S04-70-09 [HIGH] -- Gate [10i] is locus-blind and enforces the false Section 0.1 claim

- **String:** 4 (Adversarial Probing) | **Position:** 11 | **Class:** D (gate)
- **Locus:** `build.py`, gate [10i]: `check(expected_22_2 in body, f"Section 22.2 carried-entry bound at VERSION-1 ({expected_22_2})")`.
- **Substance:** The predicate is `in body` -- a whole-document substring test carrying the name of a specific section. On these bytes the string "v0.1 through v0.69" occurs **only at line 22 (Section 0.1)**, not in Section 22.2. The gate therefore passes on a locus it does not name while the locus it does name is stale. Probe 5: correcting Section 0.1 to the true value produces `FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.69)`. The gate does not merely miss the defect; it **requires** it. This is the F-XZ12-OP-01 class -- a gate returning PASS precisely when the fix is absent -- recurring at v0.70 in inverted form.
- **Required repair:** Slice Section 22.2 and Section 22.3 from the body and assert the bound within each slice.
- **Falsifier:** Probe 5 rerun passes; a stale Section 22.2 fails.
- **Cross-reference:** F-S04-70-06, F-S04-70-07; F-XZ12-OP-01 (v0.13).

### F-S04-70-10 [HIGH] -- Gate [2f]'s VERSION-1 convention mandates a false provenance claim

- **String:** 4 | **Position:** 12 | **Class:** D
- **Locus:** `build.py`, gate [2f]: `prov_match = re.search(r'repair build from v(\d+\.\d+)\s+R(\d+)\s+audit', status_text)` followed by an assertion that `prov_ver == VERSION - 1`.
- **Substance:** The gate captures both the version and the round number, then validates only the version, and only against VERSION-1. It never checks that round R actually audited that version. The convention holds only while every version is audited before its successor. The v0.69/v0.70 two-step broke that assumption, so the gate now compels "from v0.69 R27 audit" and rejects the truth. Probe 10: substituting v0.68 yields `FAIL: Status provenance v0.68 == v0.70 - 1`.
- **Required repair:** Validate the provenance version against `r27_findings_index.json["version"]` and the round number against `["round"]`, not against a positional arithmetic assumption.
- **Falsifier:** Probe 10 rerun passes; a Status line naming a version the index does not name fails.
- **Cross-reference:** F-S04-70-08; F-S01-54-02 (the finding that created gate [2f]).

### F-S04-70-11 [HIGH] -- The document's last visible line is outside every seal and every gate

- **String:** 5 (Temporal Integrity) | **Position:** 16 | **Class:** D
- **Locus:** `xz_protocol_v0_70.md`, final line, after the Provenance block. `*End of XZ Protocol v0.70 draft candidate.*` occurs **twice**: once inside the sealed v0.70 entry (tagged `[COMPUTED: generate_terminal_line]`) and once in the unsealed tail.
- **Substance:** Entry sealing and the FULL_SECTION_27 computation both terminate at the `*Provenance and review status.*` marker (`build.py` lines 58, 66, 260, 460). Everything after it is unsealed. Gate [10h] tests `terminal_expected in protocol` with no uniqueness or position constraint, so the sealed copy alone satisfies it. Probe 8: rewriting the tail line to `*End of XZ Protocol v0.42 draft candidate.*` yields 70/70 seals verified, PRIOR_HISTORY derived, `[10h] PASS: Terminal line matches v0.70`, and **BUILD PASSED: all checks GREEN**. The last thing a reader sees can name any version at all. Probe 7 confirms the sealed copy *is* protected, so the exposure is specific to the duplicate.
- **Required repair:** Assert the terminal marker occurs exactly once, and that its offset precedes the Provenance marker; or extend the seal terminus past the tail.
- **Falsifier:** Probe 8 rerun fails the build.
- **Cross-reference:** Boundary item 6 (seal terminus at Provenance marker) discloses the unsealed region but not the duplicated claim inside it; substrate-of-record uniqueness.

### F-S04-70-12 [MEDIUM] -- Declaration pattern 4 admits bare references as declarations; attribution is file-order dependent

- **String:** 1 | **Position:** 1 | **Class:** D
- **Locus:** `extract_findings.py`, `DECLARATION_PATTERNS[3]`: `(F-S\d{2}-\d{2,3}-\d{2,3}[A-Z]?)\s*\(?(HIGH|MEDIUM|LOW|INFORMATIONAL|CRITICAL)\b`.
- **Substance:** The pattern requires only whitespace and an optional paren between an ID and a severity token, so an inline cross-seat reference of the form "F-S01-70-04 HIGH" in *any* report is captured as a declaration. `build.py` iterates `sorted(report_files)` and takes first-occurrence-wins, so a seat whose filename sorts earlier can define another seat's finding severity. On these bytes no attribution mismatch occurs (checked: every captured ID's seat number matches its source file), so the exposure is latent, not live.
- **Required repair:** Require declaration context -- line start, heading, bold, or table cell -- for pattern 4, or reject captures whose seat number does not match the source filename.
- **Falsifier:** A report containing only a bare reference to another seat's ID yields no extraction from that file.
- **Cross-reference:** F-S04-70-01 (same module).

### F-S04-70-13 [MEDIUM] -- `xz_protocol_boundaries.json` version field stale at 0.62 and ungated

- **String:** 2 | **Position:** 6 | **Class:** E (process)
- **Locus:** `xz_protocol_boundaries.json:2`: `"version": "0.62"`.
- **Substance:** The file ships as a manifested member of the v0.70 packet carrying a version field eight versions behind. Gates [2h] and [10f] verify the item count (35 == 35) and the ENUMERATED tag, and nothing verifies the version field. A reader cannot tell from the file whether the boundary set was reviewed at v0.70 or merely carried. This seat holds no v0.62 bytes and cannot determine whether the set is genuinely unchanged.
- **Required repair:** Stamp the file at each version that ships it and add a version-parity check to gate [10f]; or state in the file that the version field records last substantive change, and gate that reading.
- **Falsifier:** Gate output includes a boundaries-version check.
- **Cross-reference:** Boundary item 20 (no boundary-retirement mechanism); boundary-30 staleness class at R15/v0.56.

### F-S04-70-14 [LOW] -- "Zero unmanifested members" is false of the manifest itself

- **String:** 6 (Methodology Audit) | **Position:** 18 | **Class:** C (disclosed)
- **Locus:** v0.70 entry repair (6); `PACKET_SHA256SUMS` (27 lines, 28 files extracted).
- **Substance:** The manifest cannot contain its own digest. The claim is therefore false as universally stated and true under the intended scope. Boundary item 10 (packet non-closure) discloses the class, so this is Class C rather than Class A. Separately, the ten dispatch-layer files (AUDIT_CONTEXT, DISPATCH, METHODOLOGY, CI_METHODOLOGY, R27_TRIAGE, R27_REPORTS, and the three duplicated packet members plus EXECUTABLE_PACKET) ship unmanifested; the three duplicates were verified byte-identical to their manifested counterparts.
- **Required repair:** Scope the claim ("every packet member other than the manifest") or publish the manifest digest in the entry text where the seal chain covers it.
- **Falsifier:** The entry states the scope, and the manifest digest appears inside a sealed entry.
- **Cross-reference:** Boundary items 7 and 10; F-S01-68-11 / F-S04-68-09.

### F-S04-70-15 [LOW] -- Em-dash characters in shipped `.py` tooling, no gate covers them

- **String:** 1 | **Position:** 1 | **Class:** E
- **Locus:** `extract_findings.py`: three U+2014 characters (docstring examples and the `[-\u2014]+` (hyphen or em-dash character class) character class in `DECLARATION_PATTERNS[0]`).
- **Substance:** The regex use is functional -- it lets the extractor read seat reports that use em-dashes -- but the shipped `.py` file carries characters the program's em-dash policy excludes from `.py` sources, and `build.py` implements no em-dash gate at all (the [4] Brand string sweep covers brand strings only). `R27_S02_REPORT.md` carries 47; those are covered by the Section 23 ship-unmodified rule and F-OPUS5-17-09, and are Class C.
- **Required repair:** Replace the docstring em-dashes with the escape `\u2014` in the character class and double hyphens in prose; add an em-dash gate over normative files and tooling.
- **Falsifier:** A codepoint sweep over `*.py` returns zero U+2013/2014/2015 outside escaped literals.
- **Cross-reference:** F-OPUS5-17-09 (reports, DISCLOSED NOT CLOSED).

### F-S04-70-16 [INFORMATIONAL] -- Seat non-independence: dispatch label, executor, and memory state all diverge

- **String:** 6 | **Position:** 21 | **Class:** E
- **Locus:** `DISPATCH.txt` header: "Model: Gemini 3.1 Pro | Mode: FRESH. No prior context. No held bytes."
- **Substance:** Executed by Claude Opus 5 carrying persistent lineage memory of R7-R27. Three independence assumptions in the dispatch header are false of this seat: model family, freshness, and absence of prior context. The A-X3 non-collusion axiom in Section 22.4 assumes cross-family seats; a round whose seats are relabelled rather than re-routed does not test what the axiom needs tested. Disclosed here so the triage can weight this seat correctly rather than as an independent Gemini observation.
- **Required repair:** Either route S04 to the named model or amend the dispatch header to name the executor and its memory state.
- **Falsifier:** Dispatch header and report S-0 agree on model, mode, and held-byte state.
- **Cross-reference:** Seat-label drift, sixth consecutive round; F-S01-68-12; seat-non-independence class at R9/v0.44.

### F-S04-70-17 [INFORMATIONAL] -- `FINDING_ID_RE` is dead code

- **String:** 1 | **Position:** 1 | **Class:** E
- **Locus:** `extract_findings.py:27`.
- **Substance:** Defined and never referenced (one occurrence in the file). It is the only extraction-shaped regex in the module that carries the C-suffix, which is plausibly why the repair was believed to have landed.
- **Required repair:** Delete it, or make it the single source of the ID grammar that the five declaration patterns compose from.
- **Falsifier:** Every regex in the module is either referenced or absent.
- **Cross-reference:** F-S04-70-01.

### F-S04-70-18 [INFORMATIONAL] -- Fresh-environment build is not reproducible without an out-of-packet install

- **String:** 1 | **Position:** 1 | **Class:** C
- **Locus:** `build.py` gate [5]/[8]; observed at intake.
- **Substance:** On a clean container `python3 build.py` returns `BUILD FAILED: 2 error(s)` -- `FAIL: pytest is installed (rc=1)` and `FAIL: Test count parsed from pytest output`. The advertised 279 PASS / 0 FAIL is conditional on a `pytest` install that ships neither in the packet nor in the extraction recipe. The gate behaviour is correct and fail-closed; the *instruction set* is incomplete. Boundary item 11 (fresh-execution non-reproducibility) discloses the class, so this is Class C.
- **Required repair:** Add the install step to the AUDIT_CONTEXT extraction recipe, and pin the version.
- **Falsifier:** A seat following AUDIT_CONTEXT verbatim on a clean container reaches BUILD PASSED without improvisation.
- **Cross-reference:** Boundary item 11; boundary item 7 (execution environment unsealed).

**Severity ledger: 1 CRITICAL / 10 HIGH / 2 MEDIUM / 2 LOW / 3 INFORMATIONAL = 18 findings.**

**Class ledger: A = 8 (F-01, -02, -03, -04, -05, -06, -07, -08) | B = 0 | C = 3 | D = 4 | E = 3.**

---

## S-8 Barzakh self-check

Three questions were put to each finding: (a) is the locus quoted from shipped bytes rather than recalled; (b) would the finding survive if this seat's lineage memory were deleted; (c) is the falsifier executable by a seat that disbelieves me.

- All 18 findings quote loci from the extracted packet. No finding rests on a prior-round recollection.
- Fifteen survive memory deletion outright. F-S04-70-16 is *about* the memory and cannot. F-S04-70-13 and F-S04-70-18 invoke prior-version context but are established from the shipped bytes alone.
- Every finding's falsifier is a command or a grep runnable on the packet. The seven load-bearing ones were run in this round and are recorded in S-5 with their outputs.
- **Where this seat could be wrong:** F-S04-70-13 assumes the boundaries version field should track the protocol version; if the field records last-substantive-change by design, the finding reduces to a documentation gap. F-S04-70-14 is scope-reading dependent and is filed at LOW for that reason. F-S04-70-05 assumes the index's `unique_findings_noted` list carries disposition semantics; if it carries only convergence semantics, the contradiction is between the entry's NOTED framing and the repair list rather than between entry and index, and the finding stands with a narrower locus.
- **What this seat could not test:** boundary item 32 (self-consistent resealing) -- no held prior bytes. The entire body layer (axioms, Sidrat clause, furqan) -- disclosed, not tested, by design. Whether the four shipped R27 reports are the authentic ones: gate [13] compares index to reports with no external anchor, so a producer controlling both surfaces satisfies it. That is boundary item 32 restated at the report layer, and it is the correct place to look at R29.

---

## S-9 Prediction scorecard results

| ID | Prediction | Confidence | Result | Evidence |
|---|---|---|---|---|
| P1 | sha256sum all OK | HIGH | **TRUE** | 27/27 OK |
| P2 | pytest 186 GREEN | HIGH | **TRUE** | 186 passed, 5.41s |
| P3 | build.py 0 FAIL | HIGH | **TRUE** (conditional) | 279 PASS / 0 FAIL after pytest install; see F-S04-70-18 |
| P4 | Gate [13] fires | HIGH | **TRUE** | fires on 4 shipped reports |
| P5 | 0 missing, 0 phantom | HIGH | **TRUE** | verified computed, not narrated, via probes 2-3 |
| P6 | 0 severity mismatches | HIGH | **TRUE** | mutation lands |
| P7 | 70 ENTRY seals verify | HIGH | **TRUE** | 70/70 |
| P8 | PRIOR_HISTORY matches | HIGH | **TRUE** | `c75a0ac4...` derived |
| P9 | Section 22.4 present | HIGH | **TRUE** | line 722, 5 axioms |
| P10 | Class A only at String 6 | MEDIUM | **FALSE** | 8 Class A at Strings 1, 2, 3; zero at String 6 |
| P11 | Zero Class A at String 1 | HIGH | **FALSE** | F-S04-70-01, -02 |
| P12 | H = 1.0 continues | MEDIUM | **TRUE** | 22/22, R7-R28 |
| P13 | Section 0.1 current to v0.70 | HIGH | **FALSE** | F-S04-70-07 |
| P14 | FB-7b current through R27 | HIGH | **TRUE** | row terminates "R27 (v0.68): 4 seats, all HALTed" |
| P15 | All shipped files manifested | HIGH | **PARTIAL** | 27/28; manifest unmanifested (F-S04-70-14) |

**Score: 11 TRUE, 3 FALSE, 1 PARTIAL.** The three failures are exactly the three the dispatch was built to test. The producer's HIGH-confidence predictions about the code layer (P11) and the prose layer (P13) both failed; every prediction about tool output passed. The gap between "the tools return green" and "the claims about the tools are true" is the whole of this round.

---

## S-10 Verdict, key question, Bearer 4

### Verdict

**HALT-AND-RETURN-TO-PRODUCER.** 1 CRITICAL, 10 HIGH.

### Key question: does v0.70 achieve Goedel confinement?

**No.** Confinement requires every Class A at positions 18-21 and zero at positions 1-17. Observed: **8 Class A, all at positions 1-9; zero at positions 18-21.** The distribution is not merely non-confined -- it is the *inverse* of confinement. String 6, the surface predicted to hold the residual, is the cleanest layer in the instrument this round, carrying only one Class C and one Class E.

The v0.70 build did what it said at the logic level. Gate [13] is genuinely bidirectional, genuinely severity-aware, genuinely extractor-based; three mutation probes confirm all three axes and a benign control confirms no false positive. That is real progress and should be recorded as such. What did not land is the layer above the logic: the claim that the logic is fail-closed (it is not), the claim that the C-suffix grammar was unified (it was not), the claim that three zeros were computed (they were literals), and the count of items in the entry's own NOTED list.

### Bearer 4 assessment

**Bearer 4: FALSE.** Not UNDER TEST -- tested and answered negatively, with 8 Class A findings outside String 6.

Recommended bearer table entering R29:

| Bearer | Status | Change |
|---|---|---|
| 1. Append-only | TRUE | unchanged; 70/70, probe 6 fires three detectors |
| 2. Code correctness | **FALSE** | changed. 186 GREEN holds, but a shipped repair is phantom and a gate narrates its result |
| 3. Surface narrowing | **FALSE** | changed. The defect did not stay in prose; it re-entered code |
| 4. Goedel confinement | **FALSE** | changed from UNDER TEST. Inverse distribution observed |
| 5. Cross-vendor witness | FALSE | unchanged, and see F-S04-70-16: seats are being relabelled, not re-routed |
| 6. Axiom disclosure | TRUE | unchanged; Section 22.4 intact |
| 7. Methodology | FALSE | unchanged; but String 6 is the only Class-A-free layer this round |
| 8. The furqan | UNKNOWN | lead's call |

### The finding to put in front of the lead

Two gates now enforce byte-false claims. Gate [10i] fails when Section 0.1 is corrected; gate [2f] fails when the Status line is corrected. Both were built to catch version-token staleness, and both have become its mechanism -- one because it tests a substring against the whole document while carrying a section's name, the other because it encodes positional arithmetic (`VERSION - 1`) in place of a lookup against the index that actually records what was audited.

This is not a new defect class so much as the old one turned inside out. The program's recurring failure has been *claims about mechanisms that do not hold*. What v0.70 shows is *mechanisms that enforce claims that do not hold*. A producer following the gates faithfully now produces a false document, and a producer correcting the document breaks the build. That is a closed loop, and it will not open by adding gates. The exit is to make every VERSION-1 gate read its expectation from a shipped artifact -- the findings index knows the round and the audited version -- rather than compute it from the current version number.

### Priority order for v0.71

1. F-S04-70-01 (CRITICAL) -- real C-suffix repair; reopen F-S04-68-08.
2. F-S04-70-09 and F-S04-70-10 -- de-arithmetise both gates, then land F-S04-70-06, -07, -08 in the same build.
3. F-S04-70-03 -- make gate [13] fail-closed.
4. F-S04-70-02 -- delete the narrated summary line.
5. F-S04-70-04 and F-S04-70-05 -- one disposition per finding, in one place, with a gate over the NOTED count.
6. F-S04-70-11 -- terminal-marker uniqueness and position.

### Cross-vendor recommendation for R29

The producer is Opus 4.6 and this seat executed as Opus 5. R29 needs at least two genuinely non-Claude carrying seats on the same bytes, actually routed rather than labelled, and at least one seat holding v0.70 bytes externally so boundary item 32 becomes testable. Until a seat holds prior bytes outside the producer's control, gate [13]'s comparison of index to reports proves only that the producer is consistent with itself.

---

*Report: R28, Seat S04, XZ Protocol v0.70. Verdict HALT. 18 findings, 8 Class A, zero at String 6.*
*Class A recurrence R7-R28: 22/22. H = 1.0. Laplace P(Class A at R29) = 23/24 = 0.958.*

######_REPORT_SPLIT_######
# Source: PEER_REVIEW
# Independent Peer Review -- XZ Protocol v0.71 FROZEN

**Artifact under review:** `XZ_PROTOCOL_v071_REVIEW_PACKAGE.zip`
**Canonical artifact:** `xz_protocol_v0_71.md` (inside `XZ_PROTOCOL_v071_FROZEN.zip`)
**Review date:** 2026-08-17
**Reviewer:** Claude Opus 5 (Anthropic)
**Mode:** A (substrate verifier) -- packet extracted, `build.py`, `pytest`, `extract_findings.py`,
`xz_protocol_register_gen.py` and eight mutation probes executed on the shipped bytes in a
Linux container, Python 3.12.3.
**Review namespace:** `F-PR71-NN`

---

## 0. Reviewer standing and conflict declaration (read first)

This review does **not** satisfy the independence the review package requests, and the
reader must discount it accordingly.

1. **Family conflict.** The producer of record is Claude Opus 4.6 (Anthropic), BARRED from
   review. This reviewer is Claude Opus 5 -- the same vendor family. Under Section 22.1 the
   producer bar is defined by *family*, not by version. A same-family reading is the
   conservative one. This review is therefore **ADVISORY ONLY** and carries **zero carry
   weight** toward Bearer 5.
2. **Lineage contamination.** This reviewer holds persistent cross-session memory of the
   R7--R28 audit lineage, including having executed the R28 Seat S04 report that ships in
   this package. This review is **not** a fresh reading. Every finding below was derived
   byte-first -- extraction, tool execution and all probes preceded any consultation of
   lineage material, and every finding cites a locus in the shipped bytes -- but the
   independence assumption does not hold and is not waived.
3. **Not the human review the package asks for.** The REVIEW_GUIDE describes this as "the
   first independent human examination of the complete artifact." It is not a human
   examination. It is a machine review by the producer family.

Given (1)--(3), the correct reading of this document is: *a producer-family advisory seat
executed one further round on the frozen bytes.* It is R29 in all but name.

---

## 1. Verdict

> **Verdict: HALT-AND-RETURN-TO-PRODUCER.**
>
> **Severity ledger: 2 CRITICAL / 15 HIGH / 5 MEDIUM / 3 LOW / 3 INFORMATIONAL = 28 findings.**
>
> **Class ledger: A = 17, B = 0, C = 2, D = 2, E = 7 = 28 primary classifications.**
> (`F-PR71-09` and `F-PR71-14` each carry a secondary Class D on the enforcing gate; counted
> once, at Class A, on the enforced false claim.)
>
> Both ledgers were derived by counting the enumerated findings in §3 and §4 after the
> document was written, not narrated while writing it.
>
> **Recommendation: WITHDRAW the FROZEN status token.** The freeze is not blocked by the
> Gödel residual it invokes. It is blocked by (a) three explicit governance rules in the
> frozen text and the shipped canonical methodology that the freeze contravenes without
> disclosing that it is doing so, and (b) eleven Class A byte-false claims inside the
> freeze entry itself, including five that were prescribed for repair by the R28 triage and
> marked CLOSED while shipping live and reproducible.

**The single most important sentence in this review:** the shipped canonical methodology
states, in its own words, *"FROZEN requires all eight TRUE"* (methodology v7 §11). The
v0.71 entry declares Bearers 4, 5 and 7 FALSE and declares FROZEN anyway, without
recording that it is overriding its own criterion.

---

## 2. What verifies cleanly (recorded as genuine progress)

These are not concessions. They are results I reproduced and they are the strongest part
of the artifact.

| # | Check | Result |
|---|---|---|
| V1 | `sha256sum -c PACKET_SHA256SUMS` | 28/28 OK |
| V2 | `python3 build.py` | 279 PASS / 0 FAIL, `BUILD PASSED` |
| V3 | Canonical six-suite `pytest` | 186 passed, rc=0 |
| V4 | ENTRY seals in `HISTORY.sha256` | 71/71 verify, plus `FULL_SECTION_27` |
| V5 | **Cross-version append-only** | **PROVEN, not asserted** (see below) |
| V6 | `PRIOR_HISTORY` chaining | `2e41e745...` equals the sha256 I independently computed over the v0.70 `HISTORY.sha256`. Correct. |
| V7 | Section 27 carried entry text | All 70 carried entries byte-identical v0.70 -> v0.71; Section 27 preamble byte-identical |
| V8 | Dispatch integrity | All four R28 dispatch packages byte-identical except `DISPATCH.txt`; `PROTOCOL_v070.txt` byte-identical to the v0.70 packet member; `METHODOLOGY.txt` byte-identical to `methodology_v7_canonical.md` |
| V9 | `generate_boundary_list` | Reproduces the entry's 35-item boundary paragraph **byte-exactly**. This `[COMPUTED]` tag is TRUE. |
| V10 | Boundary enumeration fidelity | All 35 items in `xz_protocol_boundaries.json` appear verbatim in the entry; declared count 35 = enumerated 35 |
| V11 | "No code changes" | TRUE at the semantic level. Every `.py` diff v0.70 -> v0.71 is a version-stamp line only. |
| V12 | Em-dash discipline (protocol) | 0 x U+2014, 0 x U+2013, 0 x U+2015 in `xz_protocol_v0_71.md` |
| V13 | Brand canonical | `BayyinahEnterprise` x2, zero spaced or plural variants |
| V14 | PDF vs source | No divergence detected on seven probe strings; PDF is a faithful rendering |

**On V5, which deserves emphasis.** Holding both the v0.70 and v0.71 packets, I compared
the seal files directly:

```
v0.70 HISTORY.sha256: 72 labels    v0.71 HISTORY.sha256: 73 labels
common labels: 71
CHANGED carried seals: ['FULL_SECTION_27']   <- expected, a new entry was appended
added: ENTRY_v0.71, PRIOR_HISTORY 2e41e745...
carried Section 27 entry TEXT that changed: none
```

Every one of the 70 carried ENTRY seals is byte-identical across the version boundary, the
carried entry text is byte-identical, and the `PRIOR_HISTORY` value chains correctly to an
independently recomputed digest. **Bearer 1 (Append-only) = TRUE is fully supported by the
bytes.** After the v0.4 and v0.41 append-only corruptions, this is a real and hard-won
property, and it is the property the program should be proudest of.

---

## 3. Class A findings -- byte-false claims in the sealed freeze entry

### F-PR71-01 [CRITICAL] -- The freeze contravenes the FROZEN criterion of its own canonical methodology

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` Section 27, v0.71 entry, "Bearer state at
  FROZEN" block, vs. `methodology_v7_canonical.md` §11 (`sha256 59aa6591d9...`, shipped
  byte-identical to `METHODOLOGY.txt` in all four R28 dispatches).
- **Substance:** Methodology v7 §11 states: *"BSSG three-valued kernel: TRUE, FALSE,
  UNKNOWN. UNKNOWN blocks until evidence resolves it. FALSE dominates. **FROZEN requires all
  eight TRUE.**"* The v0.71 entry declares Bearer 4 FALSE, Bearer 5 FALSE, Bearer 7 FALSE,
  and declares FROZEN. Under the kernel semantics the same paragraph invokes, three FALSE
  conjuncts yield DENY_FALSE, not ALLOW. The entry does not acknowledge that it is
  overriding the criterion, does not record an amendment to it, and does not state the
  authority under which the override occurs.
- **Aggravating detail:** The entry presents Bearer 8 (the furqan) = TRUE as if the lead's
  sufficiency judgment is an *override* of the other seven. Methodology §11 defines Bearer 8
  as one of eight conjuncts occupying Position 24 -- a member of the conjunction, not a
  solvent for it. The reframing of a conjunct as an override is undisclosed and is the
  load-bearing move of the entire freeze.
- **Required repair:** Either (a) withdraw FROZEN and return to DRAFT CANDIDATE, or
  (b) formally amend methodology v7 §11 to define a disclosed-residual freeze path, publish
  that amendment before the freeze, and state in the entry that the freeze proceeds under
  the amended rule with three bearers FALSE.
- **Falsifier:** The entry, read alone, states the criterion it is applying and that
  criterion matches the shipped methodology.
- **Cross-reference:** F-PR71-02, F-PR71-03; methodology v7 §11, §15.

### F-PR71-02 [CRITICAL] -- The freeze contravenes Section 22 item 7 of its own frozen text; the invoked exception is expressly inapplicable

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` Section 22 item 7 (line ~698) vs. the
  v0.71 entry's Bearer 5 line; corroborated by the Section 25 FB-7b row (line 771).
- **Substance:** Section 22 item 7 states that *"a HALT from either carrying seat blocks
  freeze outright and requires a new version."* The v0.71 entry invokes the
  persistent-architectural-HALT exception to disclose Bearer 5 = FALSE rather than treat it
  as blocking. The exception's own text, in the same sealed file, states: *"The exception
  does not apply to first-time HALTs, to HALTs whose original clearance conditions are
  unmet, or to **HALTs on Class A or Class B findings as classified by the HALTing seat's
  own published report** (not the producer)."*

  All four R28 seats returned HALT. All four classified Class A findings in their own
  published reports. The seat executed by the sole eligible carrying family (Kimi K3, S01)
  returned HALT on a Class A finding (`F-S01-70-01`, Class A, String 2, position 4). The
  exception therefore does not apply, and item 7's unweakened rule stands: freeze is blocked.

  The Section 25 FB-7b row states the same rule independently, in the frozen text:
  *"Class A is outside the item 7 exception."*

  Condition (c) of the exception -- *"six or more carrying seats across two families
  returned non-HALT on the same bytes"* -- is also unmet. Zero carrying seats returned
  non-HALT on v0.70 bytes.
- **Required repair:** Withdraw FROZEN. Either satisfy item 7, or amend item 7 by a
  recorded, pre-freeze amendment that narrows the Class A carve-out and states why.
- **Falsifier:** No carrying-family seat HALTed on a self-classified Class A finding on the
  audited bytes.
- **Cross-reference:** F-PR71-01, F-PR71-03, F-PR71-04.

### F-PR71-03 [HIGH] -- FREEZE-BLOCKER FB-7b is PENDING at the moment of freeze, and the FB-7b row is stale by one round

- **Class:** A | **Locus:** Section 0.1 (line 22); Section 25 FB-7b row (line 771).
- **Substance:** Two defects in one row.
  1. Section 0.1 states *"Current status: PENDING RE-CARRY on v0.71 bytes"* and Section 25
     records FB-7b as *"RESOLVED v0.31; PENDING RE-CARRY v0.71."* FB-7b is a
     FREEZE-BLOCKER by name (CR-5, Section 0.4). Section 22 opens *"Before any FROZEN
     status:"* and item 6 is the two-family carry. A document cannot be FROZEN while a
     named FREEZE-BLOCKER is PENDING, and the entry nowhere reconciles this.
  2. The FB-7b row is designated by Section 0.1 as the *"single source of truth"* for carry
     status. Its trajectory terminates at **"R27 (v0.68)."** R28 does not appear anywhere in
     Section 25 (`'R28' in Section 25 -> False`, `'v0.70' in Section 25 -> False`). The
     round on which the entire freeze rests is absent from the single source of truth for
     the blocker it must clear.
- **Aggravating detail:** A stale FB-7b trajectory row is precisely R27 convergence group
  (2) (`F-S01-68-06 / F-S03-68-01 / F-S04-68-05 / F-S04-68-06`), which the v0.71 entry
  itself lists as **"HIGH CLOSED at v0.70."** It has recurred at v0.71.
- **Required repair:** Extend the FB-7b row through R28. Resolve or formally re-scope FB-7b
  before any FROZEN token.
- **Falsifier:** `grep -c 'R28' Section 25` returns a nonzero count and FB-7b reads other
  than PENDING.
- **Cross-reference:** F-PR71-02; R27 group (2).

### F-PR71-04 [HIGH] -- Bearer 2's justification cites a "disclosed standing boundary" that does not exist

- **Class:** A | **Locus:** v0.71 entry, Bearer 2 line.
- **Substance:** The entry reads: *"Bearer 2 (Code correctness): TRUE -- 186 GREEN, all gates
  PASS (gate [13] fail-open is a disclosed standing boundary)."* The token `fail-open`
  occurs exactly **twice** in the entire 469,544-byte protocol: once in R28 convergence
  group (2), where it is an open HIGH finding, and once in this Bearer 2 parenthetical. It
  is **not** among the 35 enumerated standing boundaries and **not** in
  `xz_protocol_boundaries.json`. The claim manufactures a disclosure to license a TRUE.
- **Verification:**
  ```
  occurrences of 'fail-open' in protocol: 2
  'fail-open' in the 35-item boundary enumeration: False
  'fail-open' in xz_protocol_boundaries.json:     False
  ```
- **Required repair:** Either add gate [13] fail-open to `xz_protocol_boundaries.json` as
  boundary 36 (and regenerate the enumeration), or flip Bearer 2 to FALSE.
- **Falsifier:** The cited boundary appears in the boundary register.
- **Cross-reference:** F-PR71-05, F-PR71-13.

### F-PR71-05 [HIGH] -- Five of six R28 convergence groups are marked CLOSED by the triage and ship live and reproducible

- **Class:** A | **Locus:** `R28_CROSS_SEAT_TRIAGE.md` §3 (Groups 1--5, each
  *"Disposition: CLOSED"*) vs. shipped v0.71 bytes.
- **Substance:** The triage prescribes a concrete repair for each of Groups 1--5 and marks
  each CLOSED. No code file changed between v0.70 and v0.71 except version stamps
  (independently confirmed by file-by-file diff, and by the entry's own "No code changes").
  I reproduced every one of the five on v0.71 bytes:

  | Group | Claimed | Reproduced on v0.71 bytes |
  |---|---|---|
  | 1 C-suffix phantom repair | CLOSED | **LIVE.** `DECLARATION_PATTERNS` still contains zero `C?`. Probe: `### F-S01C-70-99 -- HIGH` extracts nothing; control `F-S01-70-98` extracts. |
  | 2 Gate [13] fail-open | CLOSED | **LIVE.** Deleted the five report files and their manifest lines: `[13]` prints *"(no report files shipped -- CI-8 cardinality gate cannot fire)"* and the build returns `BUILD PASSED: all checks GREEN`. |
  | 3 Gate [13] hardcoded zeros | CLOSED | **LIVE.** `build.py` still prints the literal `0 missing, 0 phantom, 0 severity mismatches` from a bare `print`, not from computed variables. |
  | 4 Register reproduction failure | CLOSED | **LIVE and worse.** See F-PR71-06. |
  | 5 Version-token staleness | CLOSED | **LIVE and worse.** See F-PR71-07, F-PR71-08, F-PR71-09. |

- **Required repair:** Reclassify all five as OPEN. "CLOSED" in a triage must mean "the
  repair landed on the successor bytes," not "a repair was prescribed."
- **Falsifier:** Each prescribed repair is present in the v0.71 code and text.
- **Cross-reference:** F-PR71-06 through F-PR71-09.

### F-PR71-06 [HIGH] -- `generate_register` crashes on **every** shipped findings index; 216 `[COMPUTED: generate_register]` tags are unreproducible

- **Class:** A | **Locus:** `xz_protocol_register_gen.py`; `r18/r19/r25/r27_findings_index.json`;
  216 sites in Section 27.
- **Substance:** R28 Group 4 recorded that the register generator "crashes on the shipped
  R27 index." The true scope is larger. I ran the generator against all four indexes shipped
  in the FROZEN packet:
  ```
  r18: CRASH  ValueError: Group 4: adjudication_receipt ...
  r19: CRASH  ValueError: Group 7: adjudication_receipt ...
  r25: CRASH  ValueError: Group 4: source distribution is mixed (2 HIGH, 1 LOW) ...
  r27: CRASH  ValueError: Group 5: source distribution is mixed (1 HIGH, 1 MEDIUM) ...
  ```
  It reproduces nothing. `[COMPUTED: generate_register]` appears **216 times** in the
  protocol; not one of them is reproducible from the shipped bytes.
- **Aggravating detail:** `build.py` contains **zero** references to `register_gen`,
  `generate_register`, `generate_boundary_list` or `generate_terminal_line`. The register
  generator is shipped, manifested, credited 216 times as the computation source, and never
  executed by any gate. Had any gate invoked it, the build would have failed.
- **Further:** No `r28_findings_index.json` exists in the packet. The v0.71 entry's NOTED
  list carries `[COMPUTED: generate_register]` -- a computation that had no input to run on.
  Its enumeration is wrong (F-PR71-10), which is exactly the signature of a hand-written
  list carrying a tool tag. **This is a false `[COMPUTED]` tag, which methodology v7 §12
  defines as the Class A signature of the String 6 / Position 18--21 surface.**
- **Required repair:** Fix the generator's adjudication-receipt logic, add a build gate that
  invokes it and asserts byte-exact reproduction of the register text, and downgrade every
  unverifiable `[COMPUTED: generate_register]` tag to `[ASSERTED]` until it is.
- **Falsifier:** `generate_register(index, version)` returns text byte-identical to the
  corresponding entry region for at least one shipped index.
- **Cross-reference:** F-PR71-10, F-PR71-18; R28 group (4).

### F-PR71-07 [HIGH] -- Section 22.2 carried-entry bound is now **two** versions stale

- **Class:** A | **Locus:** Section 22.2 (line ~718): *"For carried entries (v0.1 through
  v0.68)..."*
- **Substance:** At v0.70 this read v0.68 and should have read v0.69 (one stale;
  `F-S04-70-06`, triage Group 5, marked CLOSED). At v0.71 it still reads v0.68 and should
  read v0.70. The defect was not repaired and the gap has doubled.
- **Cross-reference:** F-PR71-09 (the gate that permits it).

### F-PR71-08 [HIGH] -- Section 0.1 entry range is internally impossible

- **Class:** A | **Locus:** Section 0.1, line 22: *"(seventy-one amendment entries, v0.1
  through v0.70)."*
- **Substance:** Section 27 contains 71 entries spanning v0.1 through **v0.71** (verified by
  count). "v0.1 through v0.70" is 70 versions, not 71, and excludes the freeze entry that
  the sentence's own document contains. The count is right; the range endpoint is one
  version behind. This is a byte-exact recurrence of `F-S04-70-07` / `F-S02-70-03`, both in
  triage Group 5, both marked CLOSED.
- **Cross-reference:** F-PR71-07, F-PR71-09.

### F-PR71-09 [HIGH] -- Gate [10i] is locus-blind and **enforces** the false Section 0.1 claim; correcting the truth breaks the build

- **Class:** A (the enforced claim) + D (the gate limitation) | **Locus:** `build.py` [10i],
  lines 689--699.
- **Substance:** Gate [10i] computes `expected_22_2 = "v0.1 through v0.70"` and tests
  `expected_22_2 in body` -- presence anywhere in the body, not correctness at the Section
  22.2 locus whose name the gate bears. The string is satisfied by the **stale Section 0.1
  sentence**, so Section 22.2 may say anything (and does: v0.68).
- **Probe P1 (executed, mutation confirmed landed by digest change):** corrected Section 0.1
  to the true `"v0.1 through v0.71"`, single occurrence, nothing else touched:
  ```
  FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.70)
  BUILD FAILED: 2 error(s)
  ```
  **Writing the true value into the sealed text fails the build.** The verification layer
  now requires the byte-false claim in order to pass.
- **Status in the entry:** listed as convergence Group (6), *"HIGH NOTED ... Design decision
  deferred."* Deferring a design decision on a gate that enforces falsehood, and then
  freezing the artifact permanently in that state, converts a deferral into a permanent
  property.
- **Required repair:** Every VERSION-1 gate must read its expectation from the shipped
  findings index (round + version fields) and assert it **at the named locus**, not by
  substring presence anywhere in the body.
- **Cross-reference:** F-PR71-07, F-PR71-08, F-PR71-12.

### F-PR71-10 [HIGH] -- "NOTED (19 items)" enumerates 17; two HIGH Class A findings vanish from the record entirely

- **Class:** A | **Locus:** v0.71 entry, NOTED block.
- **Substance:** The entry declares 19 NOTED items and lists 17 IDs. Reconciling the whole
  entry against the four seat reports:
  ```
  real R28 findings (S01 9 + S02 8 + S03 2 + S04 18) = 37
  cited anywhere in the v0.71 entry                  = 35
  in the six convergence groups                      = 18
  in the NOTED enumeration                           = 17   (declared: 19)
  ```
  **Unaccounted for anywhere in the sealed freeze record: `F-S02-70-02` and `F-S04-70-05`.**
  Both are **HIGH, Class A**:
  - `F-S02-70-02` (HIGH, Class A, String 2, position 5) -- the C-suffix repair claim is
    byte-false; this is S02's actual contribution to convergence Group 1.
  - `F-S04-70-05` (HIGH, Class A, String 2, position 6) -- `F-S04-68-08` holds two
    contradictory dispositions in one sealed entry. That finding's own text warned:
    *"Because it is absent from the entry's enumerated NOTED list, the contradiction is
    invisible to a reader of either surface alone."* It remains absent at freeze.
- **Aggravating detail:** This is a byte-exact recurrence of `F-S04-70-04` ("NOTED count
  byte-false: 21 claimed, 20 enumerated"), which this very entry cites in Group 4. The count
  error recurred in the entry that reports the count error. No gate covers the NOTED count;
  gate [9e] emits zero checks.
- **Cross-reference:** F-PR71-06, F-PR71-11.

### F-PR71-11 [HIGH] -- The convergence groups cite the wrong S02 finding IDs; the misattribution originates in the triage and is now sealed

- **Class:** A | **Locus:** v0.71 entry Groups (1) and (3); `R28_CROSS_SEAT_TRIAGE.md` §3
  Group 1 and Group 3 tables.
- **Substance:** Verified against `R28_S02_REPORT.md` finding blocks (lines 268--352):

  | Group | Entry cites | What that ID actually is | Correct ID |
  |---|---|---|---|
  | (1) C-suffix phantom repair | `F-S02-70-06` | MEDIUM, **Class B**, String 4, `build.py` parity-probe summary | `F-S02-70-02` (HIGH, Class A) |
  | (3) Gate [13] hardcoded zeros | `F-S02-70-07` | LOW, **Class C**, String 6, METHODOLOGY tagging completeness | `F-S02-70-06` (MEDIUM, Class B) |

  Group (1) is declared a **4-seat convergence at HIGH** while citing, for one of its four
  seats, a MEDIUM Class B finding about an unrelated surface. The genuine HIGH Class A that
  belongs there is `F-S02-70-02` -- one of the two findings that vanished (F-PR71-10). The
  mutawatir claim that carries the most weight in the round is built on a mis-cited ID.
- **Provenance:** the misattribution is present in `R28_CROSS_SEAT_TRIAGE.md` and propagated
  unchanged into sealed protocol text, so no gate or reviewer could catch it downstream.
- **Cross-reference:** F-PR71-10, F-PR71-12.

### F-PR71-12 [HIGH] -- The Bearer 4 Class A distribution is wrong in three of six cells; the total reconciles by compensating errors

- **Class:** A | **Locus:** v0.71 entry, Bearer 4 paragraph; `R28_CROSS_SEAT_TRIAGE.md` §2
  Position Distribution Table.
- **Substance:** I extracted String and Class from every finding block in all four reports.
  Counting only Class A, and following each seat's own primary String assignment:

  | String | Entry claims | Actual (from seat reports) | Delta |
  |---|---|---|---|
  | 1 Code Execution | 4 findings, 3 seats | **5 findings, 3 seats** | understated 1 |
  | 2 Register | 5, 3 seats | 5, 3 seats | correct |
  | 3 Consistency | 5, 2 seats | 5, 2 seats | correct |
  | 4 Adversarial | **3, 3 seats** | **1 finding, 1 seat** (`F-S03-70-02` only) | **overstated 2 findings, 2 seats** |
  | 5 Temporal | 0 | 0 | correct |
  | 6 Methodology | 4, 1 seat | 4, 1 seat (S01) | correct |
  | **Total** | **21** | **20** | overstated 1 |

  The String 4 cell is the serious one. The entry presents adversarial probing as a
  three-seat convergent Class A surface. Only one seat found Class A there. The other two
  cells the producer counted are `F-S02-70-06` (Class **B**) and S01's `F-S01-70-05`, whose
  primary assignment in its own report is String 6 with String 4 only *latent*. Class A was
  conflated with all classes.
- **Aggravating detail:** the source triage table is internally inconsistent with itself.
  Its §1 verdict table gives S01 five Class A; its §2 distribution table totals S01 at six,
  because §2 counts `F-S01-70-05` at String 4 while §1 counts it at String 6. The sealed
  entry inherits §2's arithmetic.
- **Why the error is invisible:** the total (21 vs 20) is nearly right because the String 1
  understatement partly offsets the String 4 overstatement. The program has named this class
  before, in its own v0.41 correction (al): *"Compensating errors preserve the total but the
  itemization is false."*
- **Cross-reference:** F-PR71-11, F-PR71-16.

### F-PR71-13 [HIGH] -- Front matter contradicts the freeze entry inside the same sealed file

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` line 5 (`**Status:**`) vs. Section 27
  v0.71 entry.
- **Substance:** The Status line is the v0.70 Status line with three token substitutions;
  the rest is carried verbatim and is now false:

  | Status line (line 5) | v0.71 entry (Section 27) |
  |---|---|
  | "Bearer 4 (Goedel confinement) **under test**" | "Bearer 4 (Goedel confinement): **FALSE**" |
  | "Class A recurrence **R7-R27: 21/21**" | "Class A recurrence **R7-R28: 22/22**" |
  | "Class A distributed across Strings 1/2/3/5 **at R27**, zero at String 6" | R28 distribution, four Class A **at** String 6 |
  | "**No code changes:** gate [13] rebuilt ..., CRITICAL remap removed, C-suffix added, R27 index rebuilt, reports shipped in-packet, all files manifested" | those are the **v0.70** repairs, verbatim from the v0.70 Status line's "Six defects closed:" list |

  The last row is the worst: after the substitution of "Six defects closed:" with "No code
  changes:", the sentence now reads as a list of what v0.71 did. It is a list of what v0.70
  claimed to do -- including "C-suffix added," which R28 proved byte-false with a CRITICAL
  and which remains byte-false at v0.71.
- **Required repair:** Regenerate the Status line from tool output, not by token
  substitution on the prior version.
- **Cross-reference:** F-PR71-05, F-PR71-14; recurrence of `F-S04-70-08`.

### F-PR71-14 [HIGH] -- A FROZEN document's terminal line calls itself a draft candidate, and the gate requires it to

- **Class:** A (the false claim) + D (the gate) | **Locus:** `xz_protocol_v0_71.md` lines
  1685 and 1689; `build.py` [10h] line 679; `xz_protocol_register_gen.py:generate_terminal_line`.
- **Substance:** The last visible line of the frozen artifact reads *"End of XZ Protocol
  v0.71 draft candidate."* Gate [10h] hardcodes the expectation:
  ```python
  terminal_expected = f"*End of XZ Protocol v{VERSION} draft candidate.*"
  ```
  and `generate_terminal_line('0.71')` returns the same literal. **Probe P2:** replacing both
  occurrences with `"*End of XZ Protocol v0.71 FROZEN.*"` produces
  `FAIL: Terminal line matches v0.71` plus two seal failures. The build forbids the
  document from correctly describing its own status.
- **Aggravating detail:** boundary item 16 in the register reads *"no gate checks FROZEN
  status token."* That disclosure was written when the document was a draft. Now that the
  document is FROZEN, the absence of a FROZEN gate combined with a gate that mandates
  "draft candidate" is not a passive gap -- it is active enforcement of a false status.
- **Cross-reference:** F-PR71-09, F-PR71-15.

### F-PR71-15 [HIGH] -- The last visible line of the frozen artifact is outside every seal; arbitrary rewrite passes all 279 checks

- **Class:** A | **Locus:** `xz_protocol_v0_71.md` line 1689 (after the Provenance marker);
  `build.py` [9b]; boundary item 6.
- **Probe P3 (executed):** the terminal marker occurs twice, bracketing the Provenance block.
  Seals and `FULL_SECTION_27` truncate at the Provenance marker. I rewrote **only** the final
  line to `*End of XZ Protocol v0.42 FROZEN -- audited by nobody.*` and resynced
  `PACKET_SHA256SUMS`:
  ```
  PASS: HISTORY seal ENTRY_v0.71 matches bytes
  PASS: FULL_SECTION_27 seal matches
  BUILD PASSED: all checks GREEN
  ```
  Gate [10h] passed because the *other* terminal marker still matched.
- **Substance:** The final line a human reader sees -- carrying a version number and a status
  token -- can assert anything, on a FROZEN artifact, with 71/71 seals green. `F-S04-70-11`
  raised this at R28; it was placed in NOTED and shipped. Boundary item 6 discloses the
  *mechanism* ("seal terminus at Provenance marker") but not the consequence, and freezing
  makes the consequence permanent.
- **Required repair:** Extend the seal to EOF, or assert terminal-marker uniqueness.

---

## 4. Structural and methodological findings

### F-PR71-16 [HIGH] -- The R28 round was executed against two mutually contradictory statements of the governing architecture, both inside the same dispatch

- **Class:** A | **Locus:** `AUDIT_CONTEXT.txt` line 5 vs. `METHODOLOGY.txt` line 3 -- both
  shipped byte-identically in all four R28 dispatch packages.
  ```
  AUDIT_CONTEXT.txt:5  "Methodology: Structural Honesty Verification -- Six Strings,
                        Twenty-One Positions (v7)"
  AUDIT_CONTEXT.txt:9  "Six strings (verification layers): E-A-D-G-B-E"

  METHODOLOGY.txt:3    "Seven Heavens. Seven Earths. Twenty-Four Verification Positions."
  METHODOLOGY.txt:66   "3. Architecture: Seven Layers, Seven Witnesses, Twenty-Four Positions"
  ```
  `METHODOLOGY.txt` is byte-identical to `methodology_v7_canonical.md` (sha256
  `59aa6591d9...`), which self-describes as *"the canonical methodology for all rounds from
  R28 onward."*
- **Substance:** Every R28 seat received both documents and audited under the six-string /
  twenty-one-position coordinates. The canonical methodology defines seven layers and
  twenty-four positions. **Bearer 4 is defined by position coordinates** -- methodology §11:
  *"Goedel confinement: Class A confined to self-referential surface only -- positions
  18--21."* Under the canonical seven-layer architecture the self-referential surface is
  Layer 7, positions 22--24. The entire Bearer 4 determination -- the headline result of the
  freeze -- is computed in coordinates the canonical methodology does not use.
- **Further staleness in the canonical methodology itself:** §1 states *"21 consecutive
  rounds (R7--R27) ... P = 22/23 = 0.957"* and §15 asks whether **v0.69** achieves
  confinement, while R28 audited v0.70. The canonical methodology for R28-onward was never
  updated for R28.
- **Mischaracterization in the entry:** `F-S02-70-04` raised exactly this and the entry files
  it under Group 5, *"Version staleness."* It is not a stale token. It is an architecture
  mismatch between a round and its governing methodology.
- **Required repair:** Reconcile `AUDIT_CONTEXT`, `METHODOLOGY`, `CI_METHODOLOGY`, the
  protocol Status line and `DISPATCH.txt` onto one architecture; recompute the Bearer 4
  distribution in the canonical coordinates; add a parity gate over methodology version,
  layer count, position count and target version.

### F-PR71-17 [HIGH] -- The four-scribe tagging discipline fails at the freeze decision itself; every Bearer determination is untagged

- **Class:** A | **Locus:** v0.71 entry; methodology v7 §12.
- **Substance:** Methodology §12 requires: *"Every sentence in the amendment entry carries
  exactly one provenance tag ... Zero untagged sentences."* Measured on the v0.71 entry:
  ```
  lines in entry:            32
  lines carrying >=1 tag:    14
  UNTAGGED lines:            18   (56%)
  canonical scribe tags:     [WITNESSED] x0,  [TESTED] x0
  non-canonical tags used:   [ASSERTED] x2,  [ENUMERATED] x1
  ```
  The 18 untagged lines include **all eight Bearer determinations** and all seven carried R27
  group dispositions -- that is, every load-bearing claim of the freeze.
- **Two compounding defects:**
  1. **Zero `[WITNESSED]` tags.** The entry makes six convergence-group claims about what
     four named seats found on specific bytes. `[WITNESSED: seat, round]` exists for exactly
     this. Using `[COMPUTED]` and `[ASSERTED]` instead evades the one tag whose falsity §12
     defines as the Bearer 4 confinement signature.
  2. **`[ASSERTED]` and `[ENUMERATED]` are not in the canonical four-scribe vocabulary**
     (`[COMPUTED]`, `[TESTED]`, `[WITNESSED]`, `[DISCLOSED]`). The entry's provenance ledger
     uses tokens the methodology does not define.
- **Understatement in the entry:** Bearer 7 is declared FALSE for *"tagging incomplete at
  String 6."* Tagging is incomplete at the freeze decision, which is not String 6.

### F-PR71-18 [MEDIUM] -- Freezing makes the disclosed CI-8 structural lag permanently unclosable, and leaves the freeze round entirely ungated

- **Class:** D | **Locus:** packet inventory; `build.py` [13].
- **Substance:** No `r28_findings_index.json` exists. Gate [13] therefore counts R27
  findings against `r27_findings_index.json` (39 vs 39) and covers R28 not at all. Every R28
  claim in the freeze entry -- six convergence groups, the NOTED enumeration, the Bearer 4
  distribution, the bearer determinations -- is outside every gate. This is the CI-8
  structural lag, honestly disclosed since v0.67 as *"inherent (each round creates findings
  the next index must include)."* The disclosure was sound while versions kept coming: v0.72
  would index R28. **Freezing at v0.71 removes the successor version and converts a disclosed
  lag into a permanent gap covering precisely the round the freeze rests on.** The entry does
  not disclose this consequence.
- **Required repair:** Build `r28_findings_index.json` and run gate [13] over the R28 reports
  before any freeze, or disclose that the freeze round is structurally ungatable.

### F-PR71-19 [MEDIUM] -- Three of four R28 seat reports do not ship inside the FROZEN packet

- **Class:** C | **Locus:** `XZ_PROTOCOL_v071_FROZEN.zip` vs. Section 23 items 18 and 20.
- **Substance:** The FROZEN packet ships `XZ_v070_R28_S01_REPORT.md` and the four R27
  reports. The S02, S03 and S04 R28 reports ship only in the outer, unmanifested review
  package. Section 23 requires *"all model-council seat reports, unmodified"* and *"carrying
  reports and execution receipts"* in the deposit. Three quarters of the evidentiary basis
  for the freeze sits outside the sealed, manifested artifact -- which also means gate [13]
  could not cover them even if an R28 index existed.

### F-PR71-20 [MEDIUM] -- Universal seat-label drift makes carry status undecidable, and the triage's dismissal of it is wrong

- **Class:** E | **Locus:** `R28_CROSS_SEAT_TRIAGE.md` §1; methodology v7 §5.
- **Substance:** All four seats were executed by a different model than their dispatch label
  (sixth consecutive round). The triage states: *"The drift does not affect findings -- each
  seat executed on the same bytes under the same methodology."* That is true of the findings
  and false of the governance. Methodology §5 binds **role** to the seat label: S01 ADVISORY
  (producer-family), S02 CARRYING (binding), S03 ADVERSARIAL ADVISORY, S04 ADVISORY. At R28
  the only carry-eligible family (Kimi K3) executed the seat labelled S01/ADVISORY, and the
  seat labelled S02/CARRYING was executed by GPT-5.6 Sol, which Section 22.1 records as
  self-disqualified from carry. **Which R28 seats were carrying is therefore undefined on the
  bytes** -- and Bearer 5 turns entirely on that question. S02's own report states this
  plainly and the triage does not carry it forward.
- **Also:** methodology §5 specifies seven witnesses. R28 ran four. The shortfall is not
  disclosed in the freeze entry.

### F-PR71-21 [MEDIUM] -- The independence conditions the methodology requires for mutawatir evidence were not met, and convergence is weighted as if they were

- **Class:** E | **Locus:** methodology v7 §5 ("The Mutawatir Principle") vs. R28 execution.
- **Substance:** §5 conditions: *"(a) no shared context window between seats, (b) dispatches
  differ only in seat identity, (c) findings cite tool output rather than prior findings,
  (d) the dispatch does not prescribe what to find."* Condition (b) holds (I verified all
  four dispatches byte-identical but for `DISPATCH.txt`). Condition (a) fails for S04, whose
  report declares *"FRESH is nominal, not actual. This executor carries persistent
  cross-session memory of the R7--R27 lineage."* Condition (d) is strained: the dispatch
  ships fifteen preregistered predictions (P1--P15) including *"If Class A, ONLY at String
  6,"* which names the finding shape under test. The entry treats 4-seat and 3-seat
  convergence as the strongest evidence class without discounting for these failures.

### F-PR71-22 [MEDIUM] -- H = 1.0 and P = 0.958 are presented as statistics; neither is well-defined on this series

- **Class:** E | **Locus:** v0.71 entry opening; methodology §1.
- **Substance:** Two quantitative claims carry rhetorical weight in the freeze.
  1. **H = 1.0.** The Hurst exponent is estimated from the rescaled range R/S over a series.
     The series here is 22 identical observations (Class A present, every round). Its
     variance is zero, so S = 0 and R = 0: R/S is 0/0 and the estimator is undefined, not
     1.0. A constant sequence has no autocorrelation structure to be "maximally persistent"
     about. No shipped code computes H (`grep -i hurst` over all `.py` returns nothing); the
     value appears only in prose.
  2. **Laplace P(R29) = 23/24 = 0.958.** The arithmetic is right. The rule of succession
     assumes exchangeable, independent Bernoulli trials. These rounds are neither: each
     round audits an artifact produced *in response to* the previous round's findings, by the
     same producer. The number is a description of the record, not a calibrated forecast, and
     should be labelled as such.
- **Why this matters:** these two numbers are the empirical warrant for the claim that the
  residual is *structural* rather than *remediable*. If they do not bear weight, the
  structural-coupling argument (§5 below) loses its quantitative support.

### F-PR71-23 [LOW] -- `xz_protocol_boundaries.json` ships at v0.71 with `"version": "0.62"`, ungated

- **Class:** E. Gates [2h] and [10f] check the item **count** only, never the version field.
  Recurrence of `F-S04-70-13`, NOTED at R28, unrepaired. Nine versions stale at freeze.

### F-PR71-24 [LOW] -- Em-dash discipline holds in the protocol and fails in shipped deposit-bound artifacts

- **Class:** E. Protocol text: clean (0/0/0). But `extract_findings.py` carries 3 x U+2014
  and `build.py` has no em-dash gate at all. Shipped reports, which Section 23 requires to
  deposit unmodified: `R27_S02_REPORT.md` 45 em + 2 en; `XZ_v070_R28_S01_REPORT.md` 2 em; and
  in the outer package `R28_S02_REPORT.md` 52 em + 29 en, `R28_S03_REPORT.md` 1 em. This is
  a known standing item (`F-S04-70-15`, `F-OP17-09`) that has now been open across roughly
  fifty versions.

### F-PR71-25 [LOW] -- Zero new standing boundaries were registered at freeze despite 37 findings

- **Class:** D. `xz_protocol_boundaries.json` is byte-identical between v0.70 and v0.71. The
  register stands at 35 items. R28's unrepaired HIGHs -- gate [13] fail-open, the C-suffix
  phantom, the extractor false-positive fallback, register non-reproducibility, the NOTED
  count error, the dual disposition of `F-S04-68-08` -- are neither repaired, nor registered
  as boundaries, nor gated. They exist only as prose in one sealed entry, five of them under
  a triage disposition of CLOSED that is false of the bytes.

### F-PR71-26 [INFORMATIONAL] -- Producer-family review presented as independent human review

- **Class:** E. See §0. The REVIEW_GUIDE frames this exercise as *"the first independent
  human examination."* It is not human and not independent of the producer family. Recording
  this so the freeze record does not later carry a stronger provenance claim than the event
  supports.

### F-PR71-27 [INFORMATIONAL] -- `build.py` retains a duplicated dict key

- **Class:** E. `build.py` line 422: `62: 'sixty-two', 62: 'sixty-two'` -- harmless in
  Python, carried unchanged from v0.70, indicative of hand-editing in a file whose thesis is
  that values should be tool-derived.

### F-PR71-28 [INFORMATIONAL] -- Fresh-environment build is not reproducible from the packet alone

- **Class:** C. On a clean container `build.py` returns `BUILD FAILED: 2 error(s)` --
  `pytest is installed (rc=1, No module named pytest)`. The 279 PASS result is conditional on
  an out-of-packet install. Disclosed as boundary item 11 and raised as `F-S04-70-18`; noted
  here because the frozen deposit now permanently ships a build that cannot self-verify.

---

## 5. Assessment of the freeze's central argument

The REVIEW_GUIDE poses two questions directly. Both deserve direct answers.

### 5.1 "Is the Gödel characterization accurate? Is it honest?"

**The sentence is accurate. The use made of it is not.**

The sentence itself -- *"This instrument cannot verify that it has no remaining byte-false
claims about its own verification properties"* -- is true, is properly `[DISCLOSED]`, and is
a real and non-trivial thing to have written down. An instrument that says this about itself
is doing something most artifacts do not.

But 22 rounds of Class A at H = 1.0 is offered as the *empirical evidence* for the
characterization, and the inference does not go through. The observation is: defects recur
every round. The claim is: defects recur every round **because** self-verification is
formally impossible. That inference requires ruling out the ordinary alternative -- that the
defects recur because the prescribed repairs are not being applied. On this round's evidence
the ordinary alternative is not merely unruled-out; it is demonstrated:

- Five of six R28 convergence groups have concrete, one-line, prescribed repairs.
- The triage marked all five CLOSED.
- **Zero of the five landed.** No code file changed except version stamps.
- Two of the five are now *worse* than at R28 (Section 22.2 two versions stale; the NOTED
  count error recurred inside the entry that reports it).

Nothing about Gödelian self-reference prevents adding `C?` to five regexes, replacing an
`else`-branch `print` with `check(False, ...)`, or typing `v0.71` where `v0.70` is written.
Those are the defects. Attributing them to a formal limit is a category error, and it is the
kind of category error the program's own methodology is built to catch: it is a claim about
the instrument's verification properties that the instrument's own record refutes.

**The honest form of the claim** is narrower and still worth making: *the instrument cannot
verify its own completeness; separately, the repair loop has not converged, and 22 rounds of
recurrence is evidence about the loop, not only about the limit.*

### 5.2 "Is the structural-coupling argument sound?"

The entry argues: Bearers 4, 5 and 7 are FALSE; *"these three conditions are structurally
coupled: resolving any one requires resolving all three, which requires the instrument to
verify its own completeness, which the Goedel sentence forbids."*

**The argument is not sound as stated.** Each conjunct fails independently:

- **Bearer 4 (confinement) does not require completeness verification.** It requires that
  observed Class A be confined to the self-referential surface. That is an empirical property
  of a finite finding set, checkable per round. It is currently FALSE for a mundane reason
  (Class A at Strings 1--3) and, separately, is currently **not well-defined**, because the
  round's coordinate system contradicts the canonical methodology's (F-PR71-16).
- **Bearer 5 (cross-vendor witness) is blocked by seat routing, not by logic.** At R28 the
  only carry-eligible family executed the seat labelled ADVISORY, and the seat labelled
  CARRYING was executed by a self-disqualified family (F-PR71-20). Whether a carrying seat
  could return non-HALT on clean bytes has not been tested, because carrying seats have not
  been *routed* correctly for six consecutive rounds. That is a dispatch-administration
  problem with a known fix.
- **Bearer 7 (methodology) fails at 56% untagged lines including every Bearer
  determination** (F-PR71-17). Tagging the eight bearer lines is a text edit. It requires no
  self-verification of completeness.

The coupling claim also runs backwards through Bearer 4. Bearer 4's own text says the
confinement target is reached when *the only* Class A is in the tagging metadata. Bearer 7
is precisely the tagging surface. So "fix the tagging" is a route to *both* -- which is the
opposite of the entry's claim that resolving one requires resolving all.

**What survives.** A genuinely irreducible residual does exist, and Section 22.4 states it
well: no instrument can certify the absence of unknown byte-false claims about itself, and
axioms A-X1..A-X5 are disclosed and not defended. That is the honest boundary. It is a much
smaller boundary than the one the freeze entry claims, and it does not reach the three
bearers.

### 5.3 What the methodology's own FROZEN prediction requires

Methodology §15 states the condition precisely:

> *"FROZEN is reached not because zero Class A is achieved, but because the Goedel sentence
> is disclosed, **every non-self-referential claim is scribe-verified**, multiple witnesses
> have independently examined the bytes, and the lead judges: this is enough."*

This is a four-conjunct test, and it is a fair one. Scored:

| Conjunct | Status |
|---|---|
| Gödel sentence disclosed | **MET.** Present, correctly tagged, five occurrences. |
| Every non-self-referential claim scribe-verified | **NOT MET.** F-PR71-04, -06, -07, -08, -10, -11, -12, -13: eight classes of non-self-referential claim narrated rather than derived, in the freeze entry itself. 216 `[COMPUTED: generate_register]` tags with a generator that crashes on every shipped input. |
| Multiple witnesses independently examined the bytes | **PARTIALLY MET.** Four seats, four HALTs, real execution, byte-identical dispatches -- genuine. But independence conditions (a) and (d) fail, seat routing is undefined, and the methodology specifies seven witnesses. |
| The lead judges: this is enough | **MET.** Bearer 8 is the lead's to exercise and this review does not contest it. |

The freeze fails the second conjunct on its own terms. **This is the cleanest statement of
why the artifact is not ready:** not because zero Class A was demanded and not achieved, but
because the specific, achievable condition the methodology set -- scribe-verify every claim
that is not self-referential -- was not met, in the very entry that declares it met.

---

## 6. What would make v0.72 freezable

Ordered by dependency. None of these requires the instrument to verify its own completeness.

1. **Withdraw FROZEN.** Return to DRAFT CANDIDATE. Record the withdrawal as a v0.72
   amendment entry; do not edit v0.71 (append-only is the program's best-verified property
   and must not be spent here).
2. **Land the five prescribed repairs** the R28 triage marked CLOSED: `C?` in all five
   `DECLARATION_PATTERNS`; `check(False, ...)` in gate [13]'s `else` branch; computed values
   in the [13] summary f-string; fix `generate_register`'s adjudication-receipt logic;
   correct Section 0.1's range and Section 22.2's bound.
3. **Reclassify the triage's disposition vocabulary.** CLOSED must mean "verified landed on
   successor bytes." Add a build gate that re-runs the prior round's falsifiers.
4. **Make the gates read loci, not substrings.** [10i] and [2f] must read expectations from
   the shipped findings index (round + version fields) and assert them at named loci. Correct
   values must pass; today they fail.
5. **Fix the terminal line and the seal terminus.** `generate_terminal_line` must emit the
   real status token; the seal must extend to EOF or assert marker uniqueness.
6. **Wire the register generator into `build.py`** and assert byte-exact reproduction of
   every `[COMPUTED: generate_register]` region. Downgrade tags that cannot be reproduced.
7. **Build `r28_findings_index.json`**, ship all four R28 reports inside the manifested
   packet, and let gate [13] cover the round the freeze rests on.
8. **Reconcile the architecture** onto seven layers / twenty-four positions across
   `METHODOLOGY`, `AUDIT_CONTEXT`, `CI_METHODOLOGY`, `DISPATCH` and the protocol Status line;
   recompute Bearer 4 in canonical coordinates; add a parity gate.
9. **Route the seats correctly.** Dispatch by seat *slot* with the executing family bound and
   attested, so that "carrying" is decidable from the bytes. This is the only route to
   Bearer 5, and it has never been tested under correct routing.
10. **Tag every line of the amendment entry**, using `[WITNESSED: seat, round]` for every
    claim about what a seat found. Start with the eight bearer lines.
11. **Re-scope or resolve FB-7b** before any FROZEN token, and extend its trajectory row
    through the current round.
12. **Re-state the quantitative claims** honestly: drop H, or compute it in code over a
    series with nonzero variance; label the Laplace figure as a description of a
    non-independent record.

---

## 7. Reproduction log

All commands executed on the shipped bytes, Python 3.12.3, Linux container. Probes ran on
copies; the canonical directory re-verified 28/28 OK afterward.

| # | Probe | Mutation landed | Result |
|---|---|---|---|
| P0 | Baseline `build.py` | n/a | `BUILD PASSED`, 279 PASS / 0 FAIL |
| P0b | Canonical six-suite `pytest` | n/a | 186 passed |
| P0c | `sha256sum -c PACKET_SHA256SUMS` | n/a | 28/28 OK |
| P1 | Section 0.1 range -> true value `v0.1 through v0.71` | yes (digest changed) | **BUILD FAILED** -- gate [10i]. Truth breaks the build. |
| P2 | Terminal marker -> `v0.71 FROZEN` (both loci) | yes | **BUILD FAILED** -- [10h] + 2 seals. Correct status forbidden. |
| P3 | Final line only -> `v0.42 FROZEN -- audited by nobody`, manifest resynced | yes | **BUILD PASSED**, 71/71 seals green. Last line unsealed. |
| P4 | Delete all 5 report files + manifest lines | yes | **BUILD PASSED**. Gate [13] fail-open live. |
| P5 | `extract_from_report` on `### F-S01C-70-99 -- HIGH` + control | n/a | C-suffix dropped; control extracted. Phantom repair live. |
| P6 | `generate_register` x r18/r19/r25/r27 | n/a | **4/4 CRASH.** No `[COMPUTED]` register tag reproducible. |
| P7 | `generate_boundary_list` vs entry text | n/a | **Byte-exact match.** Tag TRUE. |
| P8 | Cross-version seal + entry-text comparison, v0.70 vs v0.71 | n/a | **70/70 carried seals and all carried entry text byte-identical; `PRIOR_HISTORY` chains correctly.** Append-only PROVEN. |

Key digests (independently computed this session):

```
XZ_PROTOCOL_v071_FROZEN.zip   c4421cce3c3590c8826ad89952cf0e61708f553a88c20d165431a7fed8cfb273
XZ_PROTOCOL_v070_BUILD.zip    35f9be97c73b93013a97547051c3c8c54513a2fe7b0252dfd2f7afa9143df41c
v0.70 HISTORY.sha256          2e41e74578df7bd66f4d9de3307bc0f5423fd3e6390c90bf9a042a9893d354d6
  == PRIOR_HISTORY declared in v0.71 HISTORY.sha256   [MATCH]
methodology_v7_canonical.md   59aa6591d91233281b14ab47c4efa8a70fdcc24d94b74abca080975e78e4f98a
  == METHODOLOGY.txt in all four R28 dispatches       [MATCH]
```

---

## 8. Closing assessment

Two things are true at once and the record should hold both.

**The instrument works.** Four independent seats, executing real tools on identical bytes,
converged on real defects and all four returned HALT. The append-only chain is
cryptographically proven across a version boundary against externally held bytes -- after
two historical corruptions, that is a genuine repair. The boundary register reproduces
byte-exactly from its generator. 186 tests are green and the dispatch was byte-identical to
every seat. The Gödel sentence is written down, in public, by the party it constrains. Most
artifacts that claim rigor cannot show a tenth of this.

**The freeze is premature.** Not because it failed to reach zero defects -- the methodology
explicitly does not require that, and demanding it would be unfair. The freeze is premature
because the specific condition the methodology *did* set, *"every non-self-referential claim
is scribe-verified,"* is unmet inside the freeze entry itself; because three explicit rules
in the frozen text and canonical methodology are contravened without disclosure; and because
five defects the round's own triage marked CLOSED ship live and reproducible.

The deepest problem is not any single finding. It is that **the verification layer has begun
enforcing the defects it exists to detect.** Gate [10i] fails when Section 0.1 is corrected.
Gate [10h] forbids the FROZEN document from calling itself FROZEN. Gate [13] reports green on
absent evidence. A generator credited 216 times has never been run by any gate and crashes on
every input it is given. When the checker mandates the false value, "all gates PASS" stops
being evidence of correctness and becomes evidence only of conformity to the checker.

Freezing now writes that state into the permanent record. The program's own thesis --
structural honesty means the artifact's surface matches its substrate behaviour -- is best
served by withdrawing the FROZEN token, landing the twelve items in §6, and freezing a v0.72
whose front matter, terminal line, bearer states, and gates all say the same true thing.

The trajectory is the contribution. It is worth one more round.

---

*Reviewer: Claude Opus 5 (Anthropic), producer-family, ADVISORY ONLY, zero carry weight.
This review is not the independent human peer review the artifact requires and must not be
recorded as one.*

######_REPORT_SPLIT_######
# Source: PEER_REVIEW
# Prepublication peer review — XZ Protocol v0.71

**Recommendation: HALT / Major Revision. Do not publish or deposit v0.71 as “FROZEN” in its current form.**

I reviewed the canonical v0.71 source, the rendered 107-page PDF, executable package, build/test suite, R27/R28 reports, R28 cross-seat triage, methodology document, amendment/seal history, and supporting generators. I also executed the supplied build and tests.

This is an **independent technical/model-based peer review, not independent human peer review**. It therefore does not itself satisfy the manuscript's stated requirement for human peer review or its separate two-family carrying-seat requirement.

## Executive assessment

There is a substantial and potentially publishable methodological contribution here. The protocol has unusually strong practices around explicit UNKNOWN states, denominator discipline, preregistered decision rules, append-only amendment history, executable checks, adversarial testing, and explicit separation between protocol claims and later empirical claims.

The problem is that **the current v0.71 freeze decision is contradicted by the artifact itself**.

Mechanically, the package is healthy:

| Verification | Result |
|---|---|
| Canonical build | **PASS** |
| Explicit test suite | **186/186 PASS** |
| Packet SHA-256 verification | **PASS** |
| Amendment seals | **71/71 verify** |
| PDF | Readable; sampled critical sections correspond to source |
| PDF length | 107 pages |

Those facts establish reproducibility of the packaged state. They **do not establish semantic correctness of that state**. In fact, several publication-blocking semantic defects remain outside what the green build currently proves.

### Publication-blocking findings

1. **The document cannot consistently call itself FROZEN under its own governance rules. — CRITICAL**

   The contradiction is direct, not interpretive.

   `xz_protocol_v0_71.md:4–5` declares **“0.71, FROZEN”** and describes v0.71 as a FROZEN repair build. Yet `:18` says **“Current status: PENDING RE-CARRY on v0.71 bytes,”** and `:20` states **“FB-8 ... is OPEN.”**

   Section 25 is even more explicit. At `:760`, the manuscript says FROZEN status may be issued only when every freeze-blocker is satisfied **and** the Section 22 carry rule has been satisfied. But `:771` says FB-7b is **“PENDING RE-CARRY v0.71”**, and `:772` leaves FB-8 **OPEN**.

   Section 22 (`:701–702`) requires two executing non-producer seats from different vendor families and says that a carrying-seat **HALT blocks freeze**. Its special persistent-HALT exception explicitly says it **does not apply to Class A or Class B findings**.

   Yet the v0.71 entry itself records R28 as **4/4 HALT**, with Class A findings (`:1645–1647`).

   Finally, the canonical manuscript ends twice with:

   > `End of XZ Protocol v0.71 draft candidate.`

   at `:1685` and `:1689`.

   The manuscript is therefore simultaneously **FROZEN**, **PENDING RE-CARRY**, **FB-8 OPEN**, and a **draft candidate**.

   Under the protocol's own declared rules, the defensible current state is **DRAFT CANDIDATE / HALT**, not FROZEN.

2. **The R28 cross-seat triage incorporated into the frozen record is materially misbound. — CRITICAL**

   I compared the individual R28 reports against `R28_CROSS_SEAT_TRIAGE.md` and then against the v0.71 amendment entry at `:1649–1666`.

   R28 contains **37 actual findings**: 9 from S01, 8 from S02, 2 from S03, and 18 from S04.

   The published triage accounts for only **35 unique finding IDs**. Two actual R28 findings disappear from the synthesis:

   **`F-S02-70-02`**, a HIGH Class-A C-suffix extraction defect, and **`F-S04-70-05`**, a HIGH Class-A contradictory-disposition defect.

   The text claims **“NOTED (19 items)”** at `:1666`, but only **17 IDs are actually enumerated**.

   More seriously, several convergence groups bind the *wrong IDs* to the claimed substance. For example, Group 1 says the C-suffix convergence consists partly of `F-S01-70-05` and `F-S02-70-06`. The individual reports show that the actual C-suffix findings are **`F-S01-70-02` and `F-S02-70-02`**. `F-S01-70-05` concerns overbroad declaration-context matching; `F-S02-70-06` concerns a contradictory hardcoded gate summary.

   Likewise, Group 3 binds `F-S02-70-07` to hardcoded zero summaries, whereas that report's `F-S02-70-07` is the **tagging-completeness** finding; its hardcoded-summary finding is `F-S02-70-06`.

   Group 4 binds `F-S04-70-04` to register reproduction failure, although `F-S04-70-04` is actually the **NOTED 21-versus-20 count defect**.

   This is particularly damaging because v0.71 labels these synthesis statements `[COMPUTED: ...]`. The canonical amendment record therefore contains a **finding-ID/proposition transposition error of exactly the kind the protocol is designed to prevent**.

3. **Several R28 defects remain live in the actual v0.71 tooling. v0.71 is not a substantive R28 repair. — CRITICAL**

   I tested the current v0.71 bytes rather than relying on the prose claims.

   The C-suffix defect remains. `extract_findings.py:26` allows `S\d{2}C?` in the generic `FINDING_ID_RE`, but all five operative `DECLARATION_PATTERNS` at lines 33–41 still use `S\d{2}` without `C?`. A synthetic legitimate C-suffix declaration is still dropped by the extractor.

   The register generator also remains unreproducible from the shipped index. Running it on the supplied R27 index raises a `ValueError` concerning the mixed-severity group without an adjudication receipt.

   `xz_protocol_register_gen.py:22` still defines:

   `{"HIGH", "MEDIUM", "LOW", "INFORMATIONAL"}`

   and therefore still omits **CRITICAL**, despite the v0.71 front matter claiming the CRITICAL-remap problem has been removed.

   Gate [13] in `build.py:748–792` still has a fail-open absence branch: when reports are missing it prints a disclosure but never calls `check(False, ...)`.

   Its final summary at `build.py:788–789` still literally prints:

   `0 missing, 0 phantom, 0 severity mismatches`

   rather than deriving those displayed values.

   `xz_protocol_boundaries.json` also still declares `"version": "0.62"`.

   These are not merely historical R28 findings. They remain properties of the **current v0.71 bytes**.

4. **The canonical v0.71 body itself contains readily falsifiable current-byte claims. — HIGH**

   Section 25 says at `:767` that FB-4 is backed by **“22 source-frame tests.”** The actual suite has **29** source-frame tests.

   At `:768`, it says FB-5 has **“30 control-graph tests.”** The actual suite has **18**.

   The full executed distribution is 29 Condition-A, 29 source-frame, 18 control-graph, 14 kernel, 27 adversarial, and 69 Phase-A tests = **186 total**.

   The total is correct; the component claims are not.

   At `:22`, v0.71 additionally states that the defect trajectory contains **“seventy-one amendment entries, v0.1 through v0.70.”** A sequence v0.1 through v0.70 supplies 70 version entries, not 71. Seventy-one requires inclusion of v0.71.

   The status line at `:5` also remains stale: it describes Bearer 4 at **R27** and a 21/21 recurrence even though the same document records the R28 result as 22/22.

   These are exactly the sort of finite, byte-level claims that the manuscript argues should not survive into a frozen instrument.

5. **The proposed “Gödel confinement” does not justify overriding these failures. — MAJOR THEORETICAL ISSUE**

   The epistemic intuition is reasonable: no finite test suite should be treated as proving the total absence of all defects in itself.

   But the manuscript advances a much stronger statement. At `:1679`, it claims Bearers 4, 5, and 7 are “structurally coupled,” that resolving any requires resolving all three, and that this would require the instrument to verify its own completeness, “which the Goedel sentence forbids.”

   That conclusion has not been formally established.

   The manuscript supplies no formal theory, effective axiomatization, consistency assumptions, arithmetization, undecidable proposition, reduction, or theorem demonstrating that Gödel's incompleteness theorem applies to these particular software/governance predicates.

   More importantly, the three predicates are not obviously Gödel-coupled at all. Bearer 4's empirical confinement criterion can be tested over the findings of a specified audit. Bearer 5 is an **external witness condition**: two eligible parties either return non-HALT or they do not. Bearer 7's current-entry tagging completeness is a finite syntactic property that can be checked by an external parser.

   None of those requires proving that the protocol is universally complete or free of all possible errors.

   The manuscript should therefore retain the **epistemic limitation**—roughly, “our verifier cannot establish the universal absence of defects beyond its specified checks”—but withdraw the claim that the current unresolved finite defects are **formally irreducible by Gödel's theorem** unless a genuine formal result is supplied.

   Disclosure of a defect is not equivalent to proof that the defect is logically unavoidable.

6. **The Hurst-exponent claim should be removed. — MAJOR STATISTICAL ISSUE**

   The methodology states that 21 consecutive Class-A-positive rounds produce **H = 1.0**, interpreted as “maximally persistent autocorrelation”; v0.71 extends this to 22/22.

   For a constant binary sequence of all ones, ordinary variance is zero. Standard autocorrelation and classical rescaled-range/Hurst calculations are therefore degenerate or undefined, rather than providing a meaningful empirical estimate of \(H=1\).

   The manuscript itself already contains the relevant prior finding at `:1323`:

   > `H=1.0 re-asserted on undefined R/S statistic (constant series 0/0).`

   Yet the same statistic is reintroduced in v0.71.

   This is a particularly clear case where the amendment history already documents the correction that the current manuscript needs.

   The **23/24 Laplace probability** also needs qualification. It corresponds to a simple rule-of-succession/Beta-Bernoulli calculation after 22 successes, but interpreting it as a predictive probability assumes a form of exchangeability that is implausible here: every audit round changes the artifact, tooling, repair strategy, and sometimes witness configuration. These are adaptive interventions, not repeated draws from an unchanged Bernoulli process.

   The scientifically defensible quantity is simply the observed recurrence: **Class-A findings occurred in 22/22 specified audit rounds**. That is interesting enough without giving it an unsupported Hurst exponent or calibrated predictive probability.

7. **The methodology's own provenance-tag rule fails in the freeze entry. — HIGH**

   `methodology_v7_canonical.md:301` says:

   **“Every sentence in the amendment entry carries exactly one provenance tag.”**

   It permits `[COMPUTED]`, `[TESTED]`, `[WITNESSED]`, and `[DISCLOSED]`, and at `:310` requires **zero untagged sentences**.

   The v0.71 entry does not meet this rule. It uses unsupported forms including `[ASSERTED]` and `[ENUMERATED]`; numerous sentences are untagged; and some terminal tags appear to cover several preceding sentences rather than exactly one.

   The build's current tag gate is substantially weaker than the methodology's stated criterion. Consequently, the green build does not establish Bearer 7.

   The manuscript itself labels Bearer 7 **FALSE** at `xz_protocol_v0_71.md:1675`. That is an accurate diagnosis—but a FALSE mandatory bearer cannot simply become a frozen “structural residual” without first changing the governing rule in a transparent prospective amendment.

8. **Independent witness provenance is not sufficiently authenticated for the evidentiary weight assigned to it. — HIGH**

   The four R28 reports can be inspected as files, and their technical findings can be reproduced. But the package does not cryptographically establish that each report originated unmodified from the named model/vendor/session.

   Indeed, the triage itself admits that **all four dispatch labels differed from the actual executors**. S02's dispatch identifies Kimi while the report says GPT-5.6 Sol executed it; the protocol separately says GPT is ineligible for carrying-seat credit.

   The frozen packet's checksum manifest anchors the R28 S01 report, but it does not similarly anchor all four R28 reports as immutable third-party-origin artifacts. The review package contains them, but packaging by the producer is not third-party provenance.

   This does not invalidate their technical observations. It does mean terms such as “independent,” “cross-vendor,” and “unmodified report” should be framed as **recorded process claims**, not cryptographically authenticated facts, unless external receipts or signatures are supplied.

## Scientific design review beyond the freeze defects

Even after those byte-level problems are repaired, I would require methodological revisions before journal publication.

The manuscript is called a **preregistration**, but the focal XZ event is historical and already known. The later scoring exercise can certainly be prospectively frozen, and executor blinding can reduce some bias, but the overall research design was devised with knowledge of the case and its outcome. The authors therefore cannot obtain the strongest form of prospective-preregistration protection against hypothesis/design construction after outcome knowledge. I recommend describing this explicitly as a **retrospective case-study protocol with prospectively frozen replay rules**, or similar, and discussing author-level hindsight contamination separately from evaluator blinding.

The Condition A/B comparison also needs sharper causal language. Condition B appears to contain everything available to Condition A plus additional SHV/BSSG structure. That design may estimate the incremental yield of the augmented workflow under the chosen conditions, but it is not a capability-matched experiment. Differences could reflect extra information, time, procedural attention, or tooling rather than the specific structural theory. The protocol's current restrictions on causal/effectiveness claims are a strong safeguard and should remain.

The conventional-practice baseline also needs external validation. Because the same research program defines both the proposed method and much of the comparator, there is a risk—whether intentional or not—of constructing an underpowered conventional baseline. Independent supply-chain/security practitioners should validate the baseline workflow before execution.

The paper's literature context is currently too inward-looking for a journal methods article. It needs substantive engagement with established work on software supply-chain security, reproducible builds and provenance, registered reports/preregistration for retrospective datasets, inter-rater reliability, dependency-aware qualitative coding, formal verification, and the actual mathematical literature relevant to incompleteness/self-reference. The manuscript's internal reference canon can remain, but it cannot substitute for engagement with the external field.

The theological architecture is not itself a scientific defect. The methodology explicitly says the correspondences are parallels rather than proofs. For publication in a technical venue, however, the manuscript should more visibly separate the theological/narrative nomenclature from the normative computational propositions so that readers can determine exactly which claims depend on executable definitions and which constitute interpretive framing.

## What is strong enough to preserve

Several aspects should survive revision essentially intact. The separation of `DENY_UNKNOWN` from `DENY_FALSE` is methodologically valuable. The refusal to infer favorable facts when evidence is absent is strong. The prespecified eligibility strata, denominator rules, dependency clustering, anti-pseudoreplication rules, and prohibition on generalization beyond the single case are all defensible.

The package also demonstrates an unusual level of executable transparency. I could reproduce the 186-test green state, checksum verification, and amendment-seal verification directly. The limitations section is substantially more candid than is typical for methodological manuscripts, especially regarding the single-case design, constructed comparator, pretraining contamination, governance issues, and sample-collapse risk.

Most importantly, **R28 actually demonstrates that the adversarial-review architecture is useful**: four audits found defects that a green build did not detect. That is a compelling result. The publication would be stronger if it embraced that result rather than trying to reinterpret the remaining defects as proof that the protocol has reached a Gödelian terminal state.

## Required revision before publication

The minimum defensible path is to revert the current state from **FROZEN** to **DRAFT CANDIDATE**, rebuild the R28 triage directly from all 37 finding declarations, correct the finding-ID transpositions and missing findings, repair the still-live extractor/register/gate defects, regenerate the current amendment entry from reproducible tools, correct the Section 25 component test counts and all version/range claims, and enforce the methodology's actual sentence-level provenance rules.

After those repairs, the protocol should undergo the carry process it already specifies: **two eligible non-producer, different-family executions on the exact successor bytes, with no disqualifying HALT**. FB-8 then needs to satisfy its explicit exit condition rather than being declared an accepted residual.

Separately, the paper should replace the \(H=1.0\) analysis with straightforward recurrence reporting, characterize the 23/24 value—if retained—as a heuristic Bayesian calculation rather than a calibrated forecast, substantially narrow the Gödel claim, strengthen the external literature review, and explicitly characterize the retrospective nature of the XZ study design.

## Editorial verdict

**Current decision: HALT / reject in present form, with encouragement to resubmit after major revision.**

I would **not** recommend publication, archival deposit, or citation of **v0.71 as a frozen preregistration**.

I **would** encourage revision rather than abandonment. The underlying protocol contains serious, interesting work. But its strongest publication claim—namely that the verification process has legitimately reached a terminal FROZEN state despite Bearers 4, 5, and 7 being FALSE—is not supported by either its own rules or the current bytes.

The most consequential observation from this review is almost the inverse of the current conclusion: **the R28 process did what a rigorous audit process is supposed to do. It caught substantive errors that a 186/186 green build did not catch. Those errors should now be corrected, not converted into a theorem of irreducibility.**

---

# Bismillah ir-Rahman ir-Rahim
