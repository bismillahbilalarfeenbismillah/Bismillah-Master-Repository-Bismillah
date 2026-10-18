# Bismillah ir-Rahman ir-Rahim

# R0837 -- XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S01

**Chronological Index:** 557 of 995  
**Date:** 2026-08-17  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R28_S01_REPORT.md  
**Source Format:** md  
**SHA-256:** `6531b90ace96faf29229e9985329bdd16807eeacd86faf5a92a909923568973f`  

---

## R0837 · XZ Protocol v0.70 -- Round 28 Audit Report -- Seat S01

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R28_S01_REPORT.md
- source_format: md
- text_sha256: 6531b90ace96faf29229e9985329bdd16807eeacd86faf5a92a909923568973f

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

---

# Bismillah ir-Rahman ir-Rahim
