# Bismillah ir-Rahman ir-Rahim

# R0813 -- NOTE: This file contains the R19 seat reports (from the R20 dispatch).

**Chronological Index:** 514 of 995  
**Date:** 2026-08-11  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R20_REPORTS.txt  
**Source Format:** txt  
**SHA-256:** `fd1e823ebff2659d8b3dd2497f60c9965776c55db788fddf5d5716bf93b324ec`  

---

## R0813 · NOTE: This file contains the R19 seat reports (from the R20 dispatch).

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R20_REPORTS.txt
- source_format: txt
- merged_variants: 1 (R19_REPORTS.txt)
- text_sha256: fd1e823ebff2659d8b3dd2497f60c9965776c55db788fddf5d5716bf93b324ec

# NOTE: This file contains the R19 seat reports (from the R20 dispatch).
# R20 raw seat reports were not available for concatenation at dispatch time.
# The R20 triage (R20_TRIAGE.txt) is derived from the v0.62 entry which absorbed
# all R20 findings. CI-8 source-ID verification against R20 raw reports is
# NOT POSSIBLE from this dispatch. The R19 reports are shipped for R19 finding
# discharge verification and historical context.
#
# ---

# XZ Protocol v0.60 -- R19 Audit Report, Seat S01 (CARRYING, BINDING, FRESH)

# VERDICT: HALT (binding). Three Class A (HIGH, byte-false) findings on v0.60 bytes.

The R7-R18 Class A streak is NOT broken. Recurrence extends to R7-R19: 13/13.

- Seat: S01, CARRYING with BINDING authority, FRESH mode (dispatch-mandated)
- Family: Kimi K3 (Moonshot AI) -- not a default/blend/router; non-producer family
- Producer: Claude Opus 4.6 (Anthropic) -- barred from audit seats
- Packet: XZ Protocol v0.60 DRAFT CANDIDATE (10 .txt dispatch files, 19-member PACKET_SHA256SUMS)
- Dispatch: R19 DISPATCH -- Seat S01 (FRESH), dated 2026-08-11; executed 2026-08-12
- Lens: GAN Convergence + CI v0.3 (dispatch-primary)

## Section 0: Identity, mode, execution surface

Authoring model: Kimi K3 (Moonshot AI), exactly as the dispatch names the seat. Not a
default/blend/router. This platform does not expose checkpoint IDs or weights revisions;
none are asserted. Execution surface (EXECUTED, verbatim from this environment):

| Item | Value |
|---|---|
| OS | Linux k2087246670967250944 5.10.134-18.0.11.lifsea8.x86_64 x86_64 |
| Python | 3.12.12 |
| pytest | 9.1.1 |
| Packet dir | /mnt/agents/output/r19_v0_60/packet |

Mode: FRESH. No prior-round bytes held; METHOD ONLY is not applicable (nothing carried).
No subagent swarm: FRESH single-seat dispatch, seat executed directly by this seat.
Packet closure: audit evidence = the 10 shipped .txt files only. No external fetches.

## Section 0.1: S-0 / S-1 preregistration (frozen before opening the v0.60 entry)

Frozen 2026-08-12 after staging + 19/19 sums verification, before build.py, pytest, or
any read of the protocol body / register text. Full verbatim text:
`r19_v0_60/S0_S1_preregistration.md`. Summary of the nine S-1 predictions and scores:

| Pred | Substance | Score |
|---|---|---|
| S1-P1 | sums 19/19, build PASS, pytest green | HELD |
| S1-P2 | CI-1R byte-exact | HELD |
| S1-P3 | M2 partially inert (output depends on majority, not individual severities) | HELD (stronger: 105/105 inert) |
| S1-P4 | No divergent group in shipped index; receipt removal inert; enforcement vacuous | HELD |
| S1-P5 | (cg)/(ch)/(ci) map to body repairs | HELD on mapping; (ch) landing false (finding) |
| S1-P6 | 22.2/22.3 bounds read v0.59 | HELD |
| S1-P7 | streak continues; Class A on CI v0.3 surfaces | HELD (3 HIGH found) |
| S1-P8 | 258 gates / 186 tests prose matches execution | HELD |
| S1-P9 | ASSERTED < 15% tag basis | HELD (5.6%) |

All nine predictions HELD; none REFUTED; none NOT REACHED except the FRESH-mode
cross-version byte comparison (P6 append-only is verified internally via 60/60 seal
recomputation; no held prior bytes exist for an external anchor -- stated, not claimed).
Each prediction carried a pre-registered falsifier; the battery that scored them is in
Section 5. I note the standing warning that a seat with zero REFUTED predictions risks
pattern-matching; here the falsifiers were real (P7 would have been refuted by any
re-execution surviving byte check; P3/P4 by any mutation battery shape firing).

## Section 1: Staging, reconstruction, standing values (all EXECUTED)

Extraction per AUDIT_CONTEXT: split EXECUTABLE_PACKET.txt on
`######_XZPACKET_FILE_SPLIT_######\n`, 16 members extracted; dispatch-side canonical
copies: xz_protocol_v0_60.md, r18_findings_index.json, xz_protocol_boundaries.json,
xz_protocol_register_gen.py. No `(n)` suffix drift in this shipment; member list
checked against the expected 19 before gating.

`sha256sum -c PACKET_SHA256SUMS` (first run, verbatim tail): 19/19 OK, rc=0.
Independent recomputation (own code, not build.py output):

| Surface | Result |
|---|---|
| PACKET_SHA256SUMS | 19 OK, 0 FAILED, rc=0 |
| ENTRY seals | 60/60 recomputed match HISTORY.sha256; 60 entries parsed |
| FULL_SECTION_27 | 5c378abc7d6cf635... recomputed == HISTORY line |
| Unsealed tail after terminator | 885 chars (disclosed boundary, standing) |
| manifest_digest (12 ALL_CODE_FILES) | bbd5c385016fab92... == trust-roots value |
| PRIOR_HISTORY | 5c28cf5a4a56c81f... reported standing; NOT anchored -- FRESH seat holds no prior HISTORY file (no seal-equality claim; recomputation governs) |

## Section 2: Required baseline execution (EXECUTED, not ASSERTED)

| Command | Log | Result | rc |
|---|---|---|---|
| `python3 build.py` | logs/build_log.txt | BUILD PASSED: all checks GREEN; 258 `PASS` lines, 0 FAIL | 0 |
| six-file pytest (`test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py`) | logs/pytest_log.txt | 186 passed in 12.06s | 0 |
| `sha256sum -c PACKET_SHA256SUMS` | logs (Section 1) | 19/19 OK | 0 |

Dispatch claims verified against execution: "258 gates, all PASS" -- matches 258 PASS
lines (R18 group-6 dispatch-layer repair landed; CI_METHODOLOGY still prints the
historical "222 gates" figure, see F-S01-60-08). "186 tests" -- matches. "19/19" --
matches. "CI-1R PASS" -- independently reproduced (Section 3).

Environmental note: pytest was installed in-session before first use; no environmental
gate failure occurred and no rc was counted against the packet.

## Section 3: CI-1R deterministic reproduction (EXECUTED)

Probe `probes/pa_ci1r.py` (log `logs/pa_ci1r_log.txt`), own extraction of the v0.60
entry register block vs `generate_register()` on the shipped index:

```
entry chars: 9162
regen == shipped_block (raw): True
regen == shipped_block (rstrip): True
boundary list in entry (byte-exact): True
terminal line count in doc: 1
terminal line: *End of XZ Protocol v0.60 draft candidate.* [COMPUTED: generate_terminal_line]
```

CI-1R: PASS, byte-exact on register, boundary list (35 items), and terminal line.

## Section 4: Clearance verification -- the 8 R18 convergent groups on v0.60 bytes

| R18 group | v0.60 disposition claim | Re-executed verdict on current bytes |
|---|---|---|
| 1. findings[] inert | CLOSED via CI v0.3 architecture repair | NOT DISCHARGED in substance -- code now derives, but derivation is output-inert (105/105 mutations) and receipt enforcement vacuous (0 divergent groups shipped); the register's own M2/M3 claim is byte-false (F-S01-60-01) |
| 2. correction-letter collision | CLOSED via CI v0.3 architecture repair | DISCHARGED -- explicit correction_refs implemented; (cg)/(ch)/(ci) map correctly to body repairs (i)/(ii)/(iii); register brackets recompute |
| 3. 22.2/22.3 staleness | CLOSED via correction (cg) | TEXT discharged (bounds read "v0.1 through v0.59" / "v0.38-v0.59", correct VERSION-1); GATE claim byte-false -- no such gate exists (F-S01-60-03) |
| 4. secondary membership label | CLOSED via correction (ch) | NOT DISCHARGED -- (ch) is a phantom repair; index group 4 disposition still "CLOSED" (F-S01-60-02) |
| 5. R16 group-6 receipt | CLOSED via correction (ci) | NOT VERIFIABLY DISCHARGED -- target artifact outside packet closure; sealed v0.59 entry still carries the wrong 2M+1L (F-S01-60-04) |
| 6. gate-count documentation | NOTED | Dispatch layer discharged (258 = 258 executed); methodology figure stale (F-S01-60-08) |
| 7. COMPUTED tag overclaim | NOTED | NOT DISCHARGED -- unfixed; this round the verbatim-copied adjudication prose carries a demonstrably false sentence (F-S01-60-01, F-S01-60-07) |
| 8. validation boundary gap | CLOSED via CI v0.3 architecture repair | DISCHARGED -- 6/6 landed-assertion shapes fail closed (Section 5, P-F) |

## Section 5: Probe battery (all EXECUTED on canonical bytes or regenerated-sums byte copies)

Modelled adversary: self-consistent forger + stale-context carrier. Probes live outside
the packet dir and import it via `sys.path.insert`; sabotage ran on byte copies with
regenerated PACKET_SHA256SUMS. Packet re-verified 19/19 OK after all probing.

| Probe | Shape | Result | Log |
|---|---|---|---|
| P-A | CI-1R byte-exact reproduction | PASS | pa_ci1r_log.txt |
| P-B | M2: 105 valid-token source_severity mutations (35 records x 3) | 0 changed output, 0 failed, 105 INERT | pb_pc_m2m3_log.txt |
| P-C | M3: adjudication_receipt removal, all 8 groups | 8/8 INERT (output byte-identical) | pb_pc_m2m3_log.txt |
| P-C ctl+ | divergent group + no receipt (synthesized) | FAIL-CLOSED ValueError (control fires) | pb_pc_m2m3_log.txt |
| P-C ctl- | divergent group + receipt present | generates (benign control) | pb_pc_m2m3_log.txt |
| P-C census | divergence census under generator's majority rule | 0/8 shipped groups divergent | pb_pc_m2m3_log.txt |
| P-D | correction (ch) landing check | index group 4 disposition = "CLOSED"; no scope_note; quoted SCOPED-OUT strings absent from index | pd_ch_log.txt |
| P-E | 22.2/22.3 gate sabotage on byte copy (bounds reverted to v0.57, sums regenerated) | BUILD PASSED rc=0, 0 FAIL -- bounds NOT gated | pe_22x_log.txt |
| P-F | validation boundary landed assertions | 6/6 shapes fail closed (noted disposition, missing substance, malformed ID, duplicate ID, dangling ref, in-group duplicate) | pf_ci8_log.txt |
| P-F | CI-8 index-source fidelity (executable portion) | 28/28 verifiable findings match shipped reports on substance/severity; 6 findings (S02C x5, S03F x1) unverifiable -- reports do not ship; 18 records carry F/C ID suffixes absent from source reports | pf_ci8_log.txt |
| P-G | independent seal recomputation | 60/60 ENTRY + FULL + manifest ALL OK | xz_recompute_log.txt |
| P-H | ASSERTED fraction, v0.60 entry | 1 ASSERTED / 18 tags = 5.6% (tag basis) | Section 6 |

Two novel-class probes this round, named as new: (N1) the majority-rule divergence
census (proves the receipt gate's firing precondition is absent from shipped data --
vacuity by construction, not by test selection); (N2) the self-consistent sabotage of
the 22.2/22.3 bounds with regenerated sums (proves the claimed VERSION-1 gate absent
even against a forger who re-seals).

## Section 6: Findings (six-element format)

Severity scale: Class A = HIGH (byte-false); B = MEDIUM; C = LOW; E = INFORMATIONAL.

### F-S01-60-01 -- HIGH (Class A): register item (1) M2/M3 verification claim byte-false; severity derivation output-inert; receipt enforcement vacuous on shipped bytes

- **Locus:** v0.60 entry register item (1) adjudication ("M2/M3-class mutations now
  either change output or fail generation") inside a `[COMPUTED: generate_register]`
  line; front-matter Status ("severity derivation from source records implemented
  (findings[] now authoritative); adjudication receipt enforcement implemented");
  xz_protocol_register_gen.py lines 110-122.
- **Substance:** The derivation computes the source-severity majority but never emits
  it; register severity is copied verbatim from `triage_severity`. Consequently every
  mutation that leaves generation alive produces byte-identical output. The only firing
  shape -- divergence without receipt -- never occurs in the shipped index (0/8 groups
  divergent under the generator's own majority rule), so the dispatched M3 probe
  ("remove adjudication_receipt from divergent group -- must fail generation") is
  unsatisfiable on shipped bytes. The R18 Surface-1 defect persists one layer down:
  findings[] is now read, but its severity semantics remain inert for output.
- **Evidence (EXECUTED):** P-B battery: 105/105 valid source_severity mutations INERT
  (including majority-flipping mutations on single-member groups 3 and 5, e.g.
  F-S01-59-01 HIGH->LOW). P-C: 8/8 receipt removals INERT. Census: all 8 groups
  majority == triage. Controls fire: synthesized divergent group without receipt ->
  `ValueError: Group 3: triage_severity 'HIGH' diverges from source majority 'LOW'...`;
  with receipt -> generates. Log: logs/pb_pc_m2m3_log.txt.
- **Falsifier:** re-run `probes/pb_pc_m2m3.py`; if any of the 105 M2 mutations or 8 M3
  removals changes output or fails generation on the shipped index, this finding falls.
- **Consequence:** The entry's strongest verification claim is false on the bytes that
  ship, inside a COMPUTED-tagged line (F-CI-3R: a Class A inside a
  `[COMPUTED: generate_register]` claim). Producer predictions P9 REFUTED (0/105
  caught), P10 vacuous on shipped bytes (fires only under synthesized divergence).

### F-S01-60-02 -- HIGH (Class A): correction (ch) is a phantom repair; "Secondary membership disposition corrected to SCOPED OUT" byte-false

- **Locus:** front-matter Status line; v0.60 entry body repair (ii) ("disposition
  changed ... to 'SCOPED OUT: canonical-group rule retained, multi-membership not
  implemented' in the R18 findings index group 4 [DIFF-VERIFIED]");
  r18_findings_index.json group 4; v0.60 register item (4).
- **Substance:** The described change exists only in the prose describing it. The
  shipped index group 4 carries `disposition: "CLOSED"`, has no `scope_note` field, and
  the strings "canonical-group rule retained" / "multi-membership not implemented"
  appear nowhere in the index (the single SCOPED_OUT token sits inside group 4's
  triage_adjudication as a statement of intent). The generator's SCOPED_OUT code path
  is never exercised; the register emits "HIGH CLOSED via append-only correction (ch)".
  The net effect: the R18 defect (a CLOSED label the mechanism does not support)
  persists in v0.60's own register, now fronted by a correction that claims a landing
  that did not occur. Phantom-repair class (R7/v0.48 recurrence).
- **Evidence (EXECUTED):** probe pd_ch_landing.py: `group 4 disposition field: 'CLOSED'`;
  `scope_note present: False`; `SCOPED OUT occurrences in index: 0`;
  `"canonical-group rule retained" in index: False`; register item (4) verbatim quoted
  in logs/pd_ch_log.txt. [DIFF-VERIFIED] tag on (ii) is false on shipped bytes.
- **Falsifier:** point to the shipped byte location where group 4's disposition reads
  SCOPED_OUT (or the scope_note string); none exists in the packet.
- **Consequence:** R18 triage minimum-repair item 4 NOT discharged. AUDIT_CONTEXT's
  (ch) line and the front-matter Status repeat the false claim at two more loci.

### F-S01-60-03 -- HIGH (Class A): "Section 22.2/22.3 bounds gated to VERSION-1" byte-false; no such gate exists

- **Locus:** front-matter Status ("Section 22.2/22.3 bounds gated to VERSION-1");
  v0.60 entry title ("Section 22.2/22.3 bounds gated to VERSION-1"); body repair (i)
  ("both now gated to VERSION-1 [DIFF-VERIFIED]"); build.py (absence).
- **Substance:** The bounds text is correct this round (22.2 reads "v0.1 through
  v0.59", 22.3 reads "v0.38-v0.59" -- VERSION-1 for 60 entries, verified). But the
  repair's substance was the gate (R18 triage item 3: "implement the VERSION-1 rule ...
  and gate both bounds"). A full gate census of build output (sections [1]-[12]) and
  source inspection show no gate references the 22.2/22.3 bounds. The version-token
  recurrence (R13-R18) is therefore ungated into R19+: a future stale bound passes the
  full suite.
- **Evidence (EXECUTED):** probe pe_22x_gate.py on a byte copy with regenerated
  PACKET_SHA256SUMS: both bounds reverted to the stale v0.57 values ->
  `build rc: 0 / BUILD PASSED: all checks GREEN / FAIL lines: 0`
  (logs/pe_22x_log.txt). grep of build.py for `22.2|22.3|through v0|carried` finds no
  bound gate.
- **Falsifier:** name the build.py gate section that fails when the bounds regress; the
  sabotage copy shows none fires.
- **Consequence:** The [DIFF-VERIFIED] tag on (i) covers the text edit only; the
  "gated" clause is byte-false at three loci (Status, entry title, repair (i)).

### F-S01-60-04 -- MEDIUM (Class B): correction (ci) closure unverifiable within packet closure; [DIFF-VERIFIED] overclaim

- **Locus:** v0.60 entry body repair (iii) and register item (5); sealed v0.59 entry
  correction (cf).
- **Substance:** (iii) claims the R16 group-6 receipt distribution was "corrected ...
  in the R18 findings index [DIFF-VERIFIED]". The R18 index has no receipt-distribution
  field; the corrected "3 MEDIUM + 1 LOW" string appears only inside group 5's
  triage_adjudication prose. The actual receipt lives in the R17/r16 findings index and
  the sealed v0.59 entry -- both outside this packet; the sealed v0.59 text still reads
  "2 MEDIUM (S01, S05) + 1 LOW (S04)" (contradicted by that version's own findings[]).
  This boundary was NOTED twice at R18 (F-S01-59-09, F-S04-59-05) and is unrepaired.
- **Evidence (EXECUTED):** index field census (pd probe); v0.59 entry (cf) text quoted
  from shipped protocol bytes: "(cf): R16 group 6 adjudication receipt source-severity
  distribution corrected ... to '2 MEDIUM (S01, S05) + 1 LOW (S04)' in
  r16_findings_index."
- **Falsifier:** ship the corrected R17/r16 index with a digest; until then the CLOSED
  rests on prose.
- **Recommendation:** either ship the corrected artifact in the R20 packet or
  re-disposition register item (5) to NOTED-unverifiable.

### F-S01-60-05 -- MEDIUM (Class B): narrative "unanimous" contradicted by shipped bytes

- **Locus:** v0.60 entry narrative: "Defect 1, 8 findings across 5 seats -- unanimous".
- **Substance:** Under the round's own framing ("10 seats (5 fresh + 5 continuous)"),
  group 1 collects findings from 8 of 10 seats; S01C and S04C contribute zero findings
  to the index. The shipped R18 triage itself records "Convergence: 9/10 seats".
  "Unanimous" is unsupported on any reading and contradicts the triage the entry
  summarizes. R17 Defect-4 narrative-count ambiguity recurrence on the ASSERTED floor.
- **Evidence (EXECUTED):** index seat census (`findings per seat` in pf_ci8_log.txt:
  S01C and S04C absent); R18_TRIAGE line "Convergence: 9/10 seats" quoted.
- **Falsifier:** ship S01C/S04C reports showing surface-1 concurrence; otherwise the
  word is false.
- **Recommendation:** drop "unanimous" or state the basis ("8 of 10 seats filed;
  5 of 5 seat-prefixes").

### F-S01-60-06 -- MEDIUM (Class B): CI-8 not fully executable within packet closure; systematic finding-ID suffix drift

- **Locus:** R18_REPORTS.txt (6 of 10 seat reports ship); r18_findings_index.json
  (suffixed IDs).
- **Substance:** (a) The index carries 6 findings from seats whose reports do not ship
  (S02C x5, S03F x1) -- their fidelity is ASSERTED, not verifiable. (b) S01C and S04C
  HALTed but contribute zero index findings; index completeness ("every finding that
  appears in any seat report") is unverifiable. (c) 18 index records carry F/C suffixes
  (F-S02-59-01F, F-S05-59-01C, ...) that appear nowhere in the source reports (which
  use bare F-S02-59-01, F-S05-59-01); exact-ID verification fails for all 18, though
  each maps unambiguously to a bare source ID with matching substance and severity
  (28/28 verifiable records matched).
- **Evidence (EXECUTED):** pf_ci8_log.txt seat-section verification table; grep census
  of report ID styles (`F-S02-59-01` x7 etc., zero suffixed occurrences).
- **Falsifier:** ship all 10 reports; if suffixed IDs exist in source bytes, (c) falls.
- **Recommendation:** publish the ID-normalization rule in the CI schema, or store
  source-verbatim IDs plus a triage alias.

### F-S01-60-07 -- LOW (Class C): COMPUTED-tag overclaim persists (R18 group 7 repair item 9 not implemented)

- **Locus:** register items (1)-(6) adjudication sentences, tagged
  `[COMPUTED: generate_register]` while copied verbatim from hand-authored index
  fields.
- **Substance:** R18 group 7 (NOTED) required splitting the COMPUTED tag scope between
  code-derived fields and verbatim-copied prose. Not implemented. This round the copied
  prose carried a demonstrably false sentence (F-S01-60-01), converting the overclaim
  from cosmetic to load-bearing.
- **Evidence (EXECUTED):** P-A reproduction shows adjudication text byte-identical to
  index `triage_adjudication` fields; F-S01-60-01 battery.
- **Falsifier:** a tag vocabulary distinguishing GENERATED from COPIED-FROM-INDEX.
- **Recommendation:** emit adjudication prose under `[COPIED: index field]` or gate its
  verification clauses.

### F-S01-60-08 -- INFORMATIONAL (Class E): CI_METHODOLOGY retains historical "222 gates"

- **Locus:** CI_METHODOLOGY.txt line 410 ("216 + 6 new = 222 gates").
- **Substance:** Historical v0.2-era figure retained without annotation. On current
  bytes the dispatch layer is consistent (AUDIT_CONTEXT "258 gates" == 258 executed
  PASS lines), so this is documentation hygiene, not a byte-false current claim.
- **Recommendation:** annotate as historical per R18 S05F recommendation.

## Section 7: Severity totals and verdict

| Severity | Count | IDs |
|---|---|---|
| HIGH (Class A) | 3 | F-S01-60-01, F-S01-60-02, F-S01-60-03 |
| MEDIUM (Class B) | 3 | F-S01-60-04, F-S01-60-05, F-S01-60-06 |
| LOW (Class C) | 1 | F-S01-60-07 |
| INFORMATIONAL (Class E) | 1 | F-S01-60-08 |

VERDICT: HALT (binding). Class A present. v0.60 does not break the R7-R18 streak;
Class A recurrence extends to R7-R19 = 13/13. Laplace P(Class A at R20) = 14/15 = 0.933
under stationarity; CI v0.3 moved the surface again (from absent mechanism to vacuous
mechanism + phantom landing) without breaking the recurrence.

Key-question answer: NO -- v0.60 does not break the streak.

## Section 8: Producer prediction scorecard (P1-P12)

| P | Claim | Score | Basis |
|---|---|---|---|
| P1 | CI-1R PASS | CONFIRMED | byte-exact (Section 3) |
| P2 | CI-8 PASS (index fidelity) | REFUTED (partial) | F-S01-60-06: unverifiable subset + ID drift |
| P3 | ASSERTED < 15% | CONFIRMED | 5.6% tag basis |
| P4 | Class A on ungated body / new CI v0.3 surface | CONFIRMED | F-S01-60-01/02/03 |
| P5 | count-list invariant holds | CONFIRMED | all brackets recompute ([10e]-equivalent own check) |
| P6 | append-only holds | CONFIRMED (internal) | 60/60 seals recompute; external anchor NOT REACHED (FRESH, nothing held) |
| P7 | code layer clean | REFUTED (in part) | tests green but derivation output-inert (F-S01-60-01) |
| P8 | ASSERTED verification < 15% | CONFIRMED | 5.6% |
| P9 | severity derivation catches valid mutation | REFUTED | 0/105 caught |
| P10 | receipt enforcement catches removal on divergent group | VACUOUS on shipped bytes | 0 divergent groups; control fires under synthesized divergence |
| P11 | correction-letter refs match ledger | CONFIRMED on mapping | (cg)/(ch)/(ci) <-> (i)/(ii)/(iii); landing defects scored separately (F-S01-60-02/04) |
| P12 | 22.2/22.3 bounds at v0.59 | CONFIRMED (text) | gate claim false (F-S01-60-03) |

## Section 9: Boundary report, hedge audit, coverage

- Outermost uncomputed layer (D-3.8): the R17/r16 findings-index artifacts that
  corrections (ci)/(cf) claim to repair -- outside packet closure. What would bring it
  inside: ship the corrected index artifacts with digests in the R20 packet.
- Second outer layer: S01C/S02C/S03F/S04C source reports (unshipped) -- CI-8 and the
  "unanimous" claim cannot be closed without them.
- Vacuity watch (boundary item 23, "[9e] silent vacuity"): realized this round in the
  receipt-enforcement gate (0/8 divergent groups) and in the multi-correction support
  (no shipped group exercises >1 correction_ref).
- Hedge/deferral audit (D-3.3): no hedged findings; F-S01-60-04/06 are stated as
  unverifiable-in-closure with the exact bytes that would close them, not as assertions.
- Coverage measurement (D-3.6): probes covered register generation (105+8+6 mutation
  shapes + 2 controls), seals (60 entries + FULL + manifest), bounds gate (sabotage),
  index fidelity (28 records), boundary list (byte-exact), narrative claims (seat
  counts, HALT counts, "unanimous"). Uncovered: the 6 unshipped reports and the
  unshipped prior-index artifacts (declared above).

## Section 10: D-7 four one-line answers

1. What did I verify by execution? Every load-bearing claim: sums, build (258 PASS),
   pytest (186), CI-1R byte-exactness, 60/60 seals, manifest, M2/M3 batteries with
   controls, validation boundary, (ch)/(ci) landing, 22.2/22.3 gate existence.
2. What did I take on assertion? Nothing load-bearing; unverifiable subsets are named
   (6 findings from unshipped reports; S01C/S04C completeness; PRIOR_HISTORY external
   anchor -- FRESH seat holds no prior bytes).
3. What would falsify my headline findings? A shipped byte location showing group 4
   SCOPED_OUT; a build.py gate section firing on the 22.x sabotage; any of 113
   mutations firing -- each falsifier is stated per finding.
4. What must the next round re-run? The M2/M3 battery on the shipped index, the
   divergence census, the (ch)-class landing check for every correction claiming an
   index/data-field edit, and a gate-existence sabotage for every "gated" claim.

## Section 11: Repairs required for v0.61 (minimum set)

1. Emit the derived source-majority severity in the register (or delete the derivation
   claim); make the M2/M3 sentence true or remove it. Add a build gate running the
   mutation battery, including majority-flip and receipt-removal shapes.
2. Land (ch) for real: set index group 4 disposition to SCOPED_OUT with a scope_note,
   or re-disposition and rewrite Status/(ii). Add a build gate that verifies every
   "changed to X in <file>" claim against the named bytes.
3. Add the VERSION-1 bounds gate to build.py (22.2 and 22.3 tokens == VERSION-1) or
   strike "gated" from Status/title/(i).
4. Ship the corrected R17/r16 index artifacts (digests) or re-disposition (ci) as
   unverifiable-in-closure.
5. Replace "unanimous" with a counted basis; ship all 10 seat reports.
6. Split the COMPUTED tag (generated vs copied-from-index); annotate the 222 figure.

## Section 12: Re-audit conditions and final integrity statement

Re-audit (R20) must re-run: CI-1R; the M2/M3 battery + divergence census on the shipped
index; a landing check for every correction claiming a data-field edit; a sabotage test
for every "gated" claim; CI-8 against the complete 10-report set.

Final integrity re-check after all probing and report assembly:
`sha256sum -c PACKET_SHA256SUMS` -- 19/19 OK (canonical bytes untouched; all probes ran
on imports or regenerated-sums copies). Standing values unchanged: FULL_SECTION_27
5c378abc..., manifest bbd5c385..., PRIOR_HISTORY 5c28cf5a... (reported standing,
unanchored -- FRESH). Self-corrections ledger: none (first seat for this thread; no
prior reports to correct).

*Report authored by Seat S01, Kimi K3 (Moonshot AI), 2026-08-12. Evidence: logs/ and
probes/ under r19_v0_60/; preregistration frozen at S0_S1_preregistration.md.*
# XZ Protocol v0.60 -- R19 Audit Report, Seat S01 (CARRYING, BINDING, CONTINUOUS from R18)

**VERDICT: HALT (binding).** Class A (byte-false) findings are present on the
shipped v0.60 bytes: 4 HIGH (Class A), 3 MEDIUM (Class B), 3 LOW, 1 INFO.
The R7-R18 Class A recurrence streak extends to R7-R19 (13/13, H = 1.0).
v0.60 does NOT break the streak.

- Seat: S01, CARRYING with BINDING authority, CONTINUOUS from R18 (dispatch-mandated)
- Authoring model: Kimi K3 (Moonshot AI) -- not a default/blend/router
- Producer: Claude Opus 4.6 (Anthropic) -- barred from audit seats
- Round: 19; version under audit: v0.60; dispatch dated 2026-08-11
- Audit executed: 2026-08-11 UTC (sandbox clock; S-0/S-1 freeze 19:24:03 UTC; report assembly from 19:49 UTC)
- Framework lenses: GAN Convergence (primary), CI v0.3 probes CI-1R / CI-4 / CI-5 / CI-8 (+ CI-8R, new this round)
- Findings format: six-element (ID, severity, locus, substance, evidence, recommendation)
- Severity scale (dispatch): Class A = HIGH (byte-false); Class B = MEDIUM

## Section 0: Identity, mode, execution surface

| Item | Value |
|---|---|
| Authoring model | Kimi K3 (Moonshot AI), as the dispatch names the seat; not a default/blend/router |
| Execution surface | Linux k2087246297732915200 5.10.134-18.0.11.lifsea8.x86_64; Python 3.12.12 (fresh sandbox instance) |
| Packet working dir | /mnt/agents/output/R19_v060_S01/packet |
| Mode | CONTINUOUS from R18 -- METHOD ONLY carried, plus this seat's own R18 packet bytes held on disk continuously since R18 (not re-uploaded); no prior CONCLUSIONS carried |
| Checkpoint IDs / weights revisions | not exposed by the platform; none asserted |
| Packet closure | audit evidence = the 10 shipped .txt files + this seat's own held v0.59 bytes; no externally fetched document was used |

Held prior state (declared in the S-0 freeze, before the v0.60 entry was
opened):

```
held/HELD_v059_HISTORY.sha256   sha256 5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d
held/HELD_xz_protocol_v0_59.md  sha256 09d542f78e09a445e58001ae69adc590358ad61fd997c4a5241c96aeac83390a
```

These held bytes enable two checks impossible at R18 (FRESH): (a) PRIOR_HISTORY
anchored to a held prior HISTORY file; (b) append-only / in-place-mutation
detection by byte comparison of carried entries v0.1-v0.59 (F-K3R3-01 class,
out of scope at R18, in scope this round).

## Section 1: Reconstruction and standing values (all EXECUTED)

Extraction per the dispatch's two-step recipe: 16 packed files split from
EXECUTABLE_PACKET(1).txt on `######_XZPACKET_FILE_SPLIT_######`, plus 4 dispatch
files copied to canonical names (`xz_protocol_v0_60.md`,
`r18_findings_index.json`, `xz_protocol_boundaries.json`,
`xz_protocol_register_gen.py`). 20 files staged; upload suffix drift `(1)`
stripped per standing procedure.

Standing values, recomputed independently of build.py (xz_recompute.py,
exit 0, RESULT: ALL OK; logs/06_recompute.log):

```
PACKET_SHA256SUMS : 19 entries, 19 OK, 0 FAILED, sha256sum -c rc=0 (initial and final)
ENTRY seals       : 60/60 recomputed match (HISTORY.sha256 vs Section 27 bytes)
FULL_SECTION_27   : 5c378abc7d6cf635b477afd871f3f58fd737a7691329b6a55532b8936312852c
Unsealed tail     : 885 chars after the Provenance terminator (disclosed by construction)
Manifest digest   : bbd5c385016fab921283db4a7e4afcfb74c224adff982e5f1ca40f7afa1fab80
                    (12 ALL_CODE_FILES = 6 modules + 6 suites, parsed from build.py
                     source; matches trust roots)
Register (CI-1R)  : sha256 627962aef7743ddbb1c43b1cc85017d0654e0019838e7429980b7a6c546f2bfd
                    (4187 chars, byte-contained in xz_protocol_v0_60.md)
PRIOR_HISTORY     : 5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d
                    (matches the v0.60 entry line AND anchored to the HELD v0.59
                     HISTORY.sha256 file -- first round this seat can run the
                     held-file anchor; cross-anchor OK)
```

No seal-equality with any producer-retained value is claimed (P23-05); the
producer performs that comparison.

## Section 2: Required baseline execution (EXECUTED, not ASSERTED)

| # | Command | Expected (dispatch/AUDIT_CONTEXT) | Executed result | Log |
|---|---|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | 19/19 OK, rc=0 (initial and final, after all probing) | logs/02_sums.log, logs/14_final_sums.log |
| 2 | `python3 build.py` | BUILD PASSED, "258 gates" | **BUILD PASSED: all checks GREEN, rc=0; 257 `PASS:` gate lines in output** (258th "PASS" occurrence is the "BUILD PASSED" summary itself) | logs/04_build.log |
| 3 | `pytest <six explicit files>` | 186 passed | **186 passed in 13.10s, rc=0** | logs/03_pytest.log |
| 4 | CI-1R `generate_register` in doc | CI-1R PASS | **CI-1R PASS** -- generated register (4187 chars) byte-contained; boundary contained; terminal line contained exactly once | logs/05_ci1r.log |
| 5 | HISTORY seal chain | ENTRY / FULL / PRIOR_HISTORY verify | ALL OK, independently recomputed (never from build.py output); PRIOR_HISTORY cross-anchored to held v0.59 HISTORY | logs/06_recompute.log |
| 6 | Append-only byte comparison (newly possible) | carried entries unchanged | Carried entries v0.1-v0.59 in the v0.60 document BYTE-IDENTICAL to the held v0.59 document (282,348 chars compared) | logs/07b_appendonly_diff.log |

Environmental note (D-5): the first `python3 build.py` run in this fresh
sandbox returned rc=1 with FAIL `pytest is installed (No module named pytest)`
-- the gate failing CLOSED correctly on an environment without pytest, not a
packet verdict. After `pip install pytest`, the re-run returned rc=0, BUILD
PASSED. The rc=1 is reported as environmental.

Gate-count observation: AUDIT_CONTEXT(1).txt line 30 documents
`- build.py: 258 gates, all PASS`. The executed build output contains 257
`PASS:` gate lines; the 258th "PASS" string occurrence is the
"BUILD PASSED" summary line itself. build.py prints no internal gate total.
The R18 repair item 6 ("derive from build.py output") is not landed. See
F-S01-60-08.

Gate non-vacuity: the CI v0.3 register gates bite -- probes P-M2c, P-M3, P-X2,
P-N1, P-N2, P-D1 all raise ValueError on the mutation shapes they target
(Section 5). The canonical packet was re-verified 19/19 OK after all probing.

## Section 3: S-1 preregistered predictions, scored

S-0/S-1 were frozen to `S0_S1_FREEZE.md` (timestamped 2026-08-11 19:24:03 UTC)
BEFORE PROTOCOL_v0_60.txt, R18_REPORTS.txt, and EXECUTABLE_PACKET(1).txt were
opened. Scores:

| # | Prediction (frozen, abbreviated) | Score |
|---|---|---|
| SP1 | Bounds read "v0.1 through v0.59" / "v0.38-v0.59" -> class discharged; falsifier: other values OR bounds still ungated | **PARTIAL** -- values CONFIRMED (lines 718/716 read the v0.59 tokens, F-S01-59-01 discharged); but the falsifier's ungated disjunct FIRED: no bounds gate exists in build.py, and the entry claims one (REFUTED component; class recurs as false gating claim, F-S01-60-02) |
| SP2 | (a) M2 majority-flip mutation changes output or raises; (b) M3 receipt removal under divergence raises; (c) receipt content unvalidated (existence-only) | **PARTIAL** -- (b) CONFIRMED (P-M3 raises); (c) CONFIRMED (P-M3b: factually false receipt accepted); (a) REFUTED for the receipted branch: P-M2b (majority flips, receipt retained) accepted with byte-identical output -- neither changed output nor failed generation |
| SP3 | Cross-layer validation covers group->findings[] only; dangling findings[]->group refs (9-12) not rejected; claim overstates one direction | **CONFIRMED** (P-X2 raises; P-X1 dangling convergence_group=99 accepted; noted items carry dangling groups 9-12; F-S01-60-06) |
| SP4 | Register items cite explicit correction_refs (cg)/(ch)/(ci) matching body corrections -> F-S01-59-04 discharged | **CONFIRMED** (P-C1: items (3)/(4)/(5) -> (cg)/(ch)/(ci), aligned with the body-repair ledger) |
| SP5 | CI_METHODOLOGY byte-identical to R18 shipment; no v0.3 normative schema; "222 gates" retained | **CONFIRMED** (pre-verified by diff pre-freeze; F-S01-60-09) |
| SP6 | AUDIT_CONTEXT "258 gates"; executed PASS-line count != 258 | **CONFIRMED** (257 `PASS:` lines; 258th occurrence is the summary; F-S01-60-08) |
| SP7 | build PASSED; pytest 186; sums 19/19; CI-1R byte-exact | **CONFIRMED** |
| SP8 | (ci) states 3 MEDIUM + 1 LOW correctly; receipt fix targets the R17 index, not shipped -> packet-closure INFO persists | **CONFIRMED** (no residual 2M+1L claim in the v0.60 entry) |
| SP9 | Carried entries byte-identical to held v0.59 document; PRIOR_HISTORY == sha256(held v0.59 HISTORY) | **CONFIRMED** (282,348 chars byte-identical; cross-anchor OK) |
| SP10 | Entry narrative/register counts match index rosters; group 3 shows 1 finding while the triage records 2/10 seats | **CONFIRMED** -- the predicted contradiction is present: register "[1-seat convergence: F-S01-59-01]" vs R18_TRIAGE Surface 3 "Convergence: 2/10 seats (S01F, Gemini fresh)" (F-S01-60-04) |
| SP11 | (ch) text present and truthful; SCOPED_OUT branch unused (vocabulary latent) | **REFUTED** -- (ch) text is present but its claimed landing is byte-false: index group 4 disposition remains "CLOSED"; the claimed target string appears nowhere in the index (F-S01-60-03). Only the latency half confirmed (SCOPED_OUT in VALID_DISPOSITIONS, unused) |

8 CONFIRMED, 2 PARTIAL (each with a REFUTED component), 1 clean REFUTED
(SP11). This seat again records refutations against its own predictions:
SP2(a) over-credited the v0.3 mechanism (receipted divergent mutations remain
invisible), and SP11 over-credited the (ch) correction's landing.

## Section 4: Clearance verification -- the 9 R18 findings on v0.60 bytes

| R18 finding | Claimed disposition (v0.60) | Executed verification on v0.60 bytes | Result |
|---|---|---|---|
| F-S01-59-01 (22.2/22.3 bounds stale) | CLOSED via (cg), "both now gated to VERSION-1" | Lines 718/716 read "v0.1 through v0.59" / "v0.38-v0.59" -- correct VERSION-1 values; but no bounds gate exists anywhere in build.py (grep `through v0`, `v0.38-`, `22.2`, `22.3` = 0 hits; gate [10] checks only the convenience sentence) | **VALUES DISCHARGED; gating claim NOT DISCHARGED -- recurs as F-S01-60-02 (Class A)** |
| F-S01-59-02 (receipt 2M+1L false) | CLOSED via (ci) | Entry (ci) states "3 MEDIUM (F-S01-58-03, F-S02-58-04, F-S05-58-05) + 1 LOW (F-S04-58-06)"; matches the R18 findings[] distribution; no residual 2M+1L claim | DISCHARGED (the corrected R17 index file itself is outside this packet -- packet-closure INFO, carried in F-S01-60-11) |
| F-S01-59-03 (findings[] semantically inert) | CLOSED via CI v0.3 | P-M2c (majority flip, no receipt) RAISES; P-M3 (receipt removal under divergence) RAISES; P-X2/P-D1/P-N1/P-N2 RAISE. But P-M2b (majority flip, receipt retained) accepted byte-identical; emitted severity is always `group["triage_severity"]` (generator lines 91, 151) | **PARTIALLY DISCHARGED -- the fail-closed half landed; the "derivation" claim recurs as F-S01-60-01 (Class A), receipt-content inertness as F-S01-60-05 (Class B)** |
| F-S01-59-04 (correction-letter collision) | CLOSED via CI v0.3 | Explicit `correction_refs[]` per group in the index; P-C1: register items (3)/(4)/(5) cite (cg)/(ch)/(ci) matching the body-repair ledger | DISCHARGED |
| F-S01-59-05 (gate count 262/261/222) | NOTED (carried) | New figure 258 (AUDIT_CONTEXT line 30) vs 257 executed `PASS:` lines; CI_METHODOLOGY still 222 | **NOT RECONCILED -- recurs as F-S01-60-08 (LOW; severity drops as the register honestly carries it NOTED)** |
| F-S01-59-06 (COMPUTED tag overclaim) | NOTED (carried, group 7) | P-TAG: `SABOTAGE-TOKEN` injected into group 7 `triage_adjudication` lands inside a [COMPUTED: generate_register] line in output | **NOT DISCHARGED -- honestly NOTED; recurs as F-S01-60-10 (LOW)** |
| F-S01-59-07 (noted-item missing field crash) | CLOSED via CI v0.3 (group 8) | P-N1 (noted item missing `substance`) RAISES ValueError; P-N2 (invalid noted disposition) RAISES | DISCHARGED (but see F-S01-60-06 for the unvalidated reverse direction) |
| F-S01-59-08 (secondary membership label overstates) | CLOSED via (ch) | Group 4 `triage_adjudication` now discloses "it was scoped out"; but the claimed disposition change did not land: `disposition` field remains "CLOSED"; "SCOPED OUT" appears 0 times in the index | **SUBSTANCE DISCLOSED; claimed locus byte-false -- recurs as F-S01-60-03 (Class A)** |
| F-S01-59-09 (PRIOR_HISTORY untagged; (cf) outside closure) | NOTED (carried) | PRIOR_HISTORY line in the v0.60 entry still carries no provenance tag; (cf) target (R17 index) still outside this packet | CARRIED -- F-S01-60-11 (INFO) |

Score: 4 discharged clean (F-S01-59-02, -04, -07, plus the -01 values), 0
falsely claimed closed without consequence, 3 recur at new loci as Class A
(F-S01-60-01/-02/-03), 3 carried at reduced/standing severity.

## Section 5: Probe battery (EXECUTED; mutations on byte copies; packet re-verified 19/19 OK after)

Probe harness: `probes/probe_battery_r19.py`; each mutation writes a mutated
index copy under `probes/` and calls `generate_register` on the copy. Canonical
bytes untouched (final `sha256sum -c` rc=0, logs/14_final_sums.log). Verbatim
results (logs/09_probes.log):

```
BASE register sha256 627962aef7743ddb (4187 chars)

P-M2a group-6 member MEDIUM->HIGH (majority unchanged): OUTPUT | output identical: True
P-M2b group-6 all 5 -> HIGH (majority flips vs triage MEDIUM, receipt present): OUTPUT | generation passed: True | output identical: True
P-M2c group-6 majority flip, receipt removed: RAISE | ValueError: Group 6: triage_severity 'MEDIUM' diverges from source majority 'HIGH' (distribution: {'HIGH': 5}) but no adjudication_receipt is provided.
P-M3 group-4 triage LOW (diverges), receipt removed: RAISE | ValueError: Group 4: triage_severity 'LOW' diverges from source majority 'HIGH' (distribution: {'LOW': 1, 'HIGH': 3}) but no adjudication_receipt is provided.
P-M3b group-4 divergence with factually FALSE receipt: OUTPUT | accepted: True | receipt emitted in output: False
P-X1 findings[] record convergence_group=99 (no such group): OUTPUT | accepted: True
P-X2 group 5 references F-S01-59-77 (no findings[] record): RAISE | ValueError: Finding ID 'F-S01-59-77' in group 5 has no record in findings[].
P-N1 noted item missing 'substance': RAISE | ValueError: Noted finding F-S01-59-09 missing required field 'substance'.
P-N2 noted disposition 'WHATEVER': RAISE | ValueError: Invalid disposition 'WHATEVER' in noted finding F-S01-59-09.
P-D1 duplicate record in findings[]: RAISE | ValueError: Duplicate finding ID 'F-S01-59-01' in findings[] array.

P-C1 body corrections (cg/ch/ci):
    register item (3) -> (cg)
    register item (4) -> (ch)
    register item (5) -> (ci)

P-TAG triage_adjudication := SABOTAGE-TOKEN -> in COMPUTED-tagged output: True

P-MAJ group severity vs source majority on shipped index:
    group 1: triage=HIGH majority=HIGH dist={'HIGH': 8} match=True receipt=True
    group 2: triage=HIGH majority=HIGH dist={'HIGH': 6} match=True receipt=True
    group 3: triage=HIGH majority=HIGH dist={'HIGH': 1} match=True receipt=True
    group 4: triage=HIGH majority=HIGH dist={'LOW': 1, 'HIGH': 3} match=True receipt=True
    group 5: triage=HIGH majority=HIGH dist={'HIGH': 1} match=True receipt=True
    group 6: triage=MEDIUM majority=MEDIUM dist={'MEDIUM': 5} match=True receipt=True
    group 7: triage=MEDIUM majority=MEDIUM dist={'MEDIUM': 1} match=True receipt=True
    group 8: triage=MEDIUM majority=MEDIUM dist={'LOW': 1, 'MEDIUM': 1} match=True receipt=True
```

Vacuity controls: the RAISE probes (P-M2c, P-M3, P-X2, P-N1, P-N2, P-D1)
demonstrate the harness reaches the intended validation paths -- the clean
OUTPUT results (P-M2a/b, P-M3b, P-X1) are therefore meaningful acceptances,
not harness failures. P-MAJ 8/8 match on shipped bytes (the v0.3 majority
computation runs and agrees with triage severities; group 8's tie
{LOW:1, MEDIUM:1} resolves to MEDIUM via the SEV_ORDER tiebreak -- see
F-S01-60-04 for the completeness caveat on that distribution).

Modelled adversary (frozen in S-1): careless producer (stale prose),
self-consistent forger (receipts coherent but source-false), stale-context
producer (repairs one version behind), patient contributor (validation gaps
at layer edges). P-M3b is the self-consistent-forger probe; it passes for the
adversary. Novel-class probes this round: P-M3b (false-receipt content), P-X1
(reverse-direction dangling reference), P-TAG (sabotage token under COMPUTED).

## Section 6: Findings (six-element format)

Severity totals: **4 HIGH (Class A), 3 MEDIUM (Class B), 3 LOW, 1 INFO.**

### F-S01-60-01 | HIGH (Class A) | v0.60 entry header, register item (1), body repair (iv); xz_protocol_register_gen.py lines 91, 113-122, 151

**Substance:** The entry claims CI v0.3 performs "severity derivation from
source records" and that "M2/M3-class mutations now either change output or
fail generation." Both are byte-false. The emitted register severity is always
the hand-authored `group["triage_severity"]`; the computed source majority is
only COMPARED against it, and a divergence behind any receipt -- including a
factually false one -- leaves the output byte-identical. The spec-impl gap
persists for a 4th consecutive round (R16 v0.2, R17 v0.2.1, R18 v0.2.2,
R19 v0.3), one layer down each time.

**Evidence (EXECUTED):** Register item (1) adjudication (copied verbatim into
[COMPUTED: generate_register] output): "CI v0.3 implements actual severity
derivation from findings[] source records with mandatory adjudication receipt
on divergence. M2/M3-class mutations now either change output or fail
generation." Body repair (iv): "register generator now derives severity from
findings[] source records ..." [COMPUTED: build.py]. Generator line 91:
`sev = g["triage_severity"]`; line 151: `sev = group["triage_severity"]`;
lines 113-122 compute the majority and only gate divergence-without-receipt.
Probe P-M2b: all 5 group-6 source severities mutated MEDIUM->HIGH (valid
tokens, majority flips against triage MEDIUM, receipt retained) ->
`generation passed: True | output identical: True`. The mutation neither
changed output nor failed generation, contradicting the register's own
sentence. F-CI-3R fires: a byte-false claim inside a [COMPUTED] tag.

**Recommendation:** Either implement true derivation (emit the computed
majority as the register severity; triage_severity becomes advisory input) or
retract the claim to the honest form: "severity cross-check: divergence
without a receipt fails generation; receipted divergences pass unchanged."
Add a P-M2b-class probe (receipted majority flip) to the shipped test suite.

### F-S01-60-02 | HIGH (Class A) | v0.60 entry body repair (i) and register item (3) vs build.py gate inventory

**Substance:** Correction (cg) is tagged [DIFF-VERIFIED] with the claim
"both now gated to VERSION-1", and register item (3) states [COMPUTED:
generate_register] "CI v0.3 gates both bounds to VERSION-1 (entry count minus
one)." No such gate exists. The bound VALUES landed correctly; the GATING
claim is byte-false. The R13-R18 version-token class migrates from stale
values to a false gate claim -- the defect-migration pattern continues.

**Evidence (EXECUTED):** Body repair (i): `both now gated to VERSION-1
[DIFF-VERIFIED]`. Register item (3): "CI v0.3 gates both bounds to VERSION-1
(entry count minus one)." build.py gate inventory executed and grepped:
`through v0` = 0 hits, `v0.38-` = 0 hits, `22.2` / `22.3` = 0 hits,
`VERSION-1` = 1 hit (a comment at line 220 about the provenance-clause gate,
not Section 22 bounds). The only Section-22 gate, [10], verbatim:
`check("gate execution is a build-time convenience" in s22, "S22 item 6: gate is convenience")`.
Sabotage confirmation: the R18 battery proved gates [10c]/[10d] bite on
register/index sabotage; nothing in build.py reads the bound strings.

**Recommendation:** Implement the gate: derive the expected bounds from the
entry count (VERSION-1), assert both strings in build.py, and fail on
mismatch; or retract the gating clause from (cg) and item (3).

### F-S01-60-03 | HIGH (Class A) | v0.60 entry body repair (ii) [DIFF-VERIFIED] vs r18_findings_index.json group 4

**Substance:** Correction (ch) claims the disposition of R18 index group 4
was changed to "SCOPED OUT: canonical-group rule retained, multi-membership
not implemented" [DIFF-VERIFIED]. On the shipped index bytes, group 4's
operative `disposition` field remains "CLOSED"; the claimed target string
appears nowhere in the file. The only SCOPED_OUT occurrence in the index is
the instruction text inside group 4's `triage_adjudication` ("change
disposition to SCOPED_OUT ..."). The correction did not land at its claimed
locus, and register item (4) "CLOSED via append-only correction (ch)"
[COMPUTED] therefore rests on an unlanded correction. The generator's
SCOPED_OUT vocabulary (VALID_DISPOSITIONS, verified present) is dead code.

**Evidence (EXECUTED):** `json.load` of the shipped index:
`convergence_groups[3]["disposition"] == 'CLOSED'`. Byte counts on the index
file: `"SCOPED OUT"` = 0 occurrences; the exact claimed string
`"SCOPED OUT: canonical-group rule retained, multi-membership not implemented"`
= absent; `SCOPED_OUT` = 1 occurrence, inside the triage_adjudication prose.
Entry body repair (ii), verbatim: `correction (ch): R17 register item (3)
disposition changed from "CLOSED via CI v0.2.2 architecture repair" to
"SCOPED OUT: canonical-group rule retained, multi-membership not implemented"
in the R18 findings index group 4 [DIFF-VERIFIED]`.

**Recommendation:** Land the correction: set group 4 `disposition` to
SCOPED_OUT (the vocabulary exists -- use it), regenerate the register, and
verify the [DIFF-VERIFIED] tag against bytes before shipping. Add a build
gate that every [DIFF-VERIFIED] claim's claimed string is byte-present at its
claimed locus.

### F-S01-60-04 | HIGH (Class A) | r18_findings_index.json findings[] vs R18_REPORTS.txt + R18_TRIAGE.txt; register items (3)/(4)

**Substance:** findings[] is incomplete against the shipped source reports,
and the omission corrupts COMPUTED convergence counts in the sealed register.
Four report findings have no findings[] record: S03F "Version-Token
Staleness" (HIGH) and "Secondary Membership Schema Gap" (HIGH) -- both listed
in R18_TRIAGE Surfaces 3 and 4 as convergent -- and S05C F-S05-59-04 (gate
count, MEDIUM) and F-S05-59-05 (findings[] ID validation, MEDIUM), both
present in the shipped S05C report. Register item (3) computes
"[1-seat convergence: F-S01-59-01]" while the shipped triage states
"Convergence: 2/10 seats (S01F, Gemini fresh)". A computed claim in the
register is false against the packet's own documents -- the R17
convergence-count defect class recurs via input omission.

**Evidence (EXECUTED):** CI-8R probe (logs/13_ci8_corrected.log):
`S05C: 5 findings in report; missing from index: [4, 5]`;
`"Version-Token Staleness" covered in findings[]: False`;
`"Secondary Membership Schema Gap" covered in findings[]: False`.
R18_TRIAGE.txt Surface 3, verbatim: "Convergence: 2/10 seats (S01F, Gemini
fresh)." v0.60 register item (3), verbatim: "[1-seat convergence:
F-S01-59-01]". S05C report (R18_REPORTS.txt lines 1466-1480) contains
`F-S05-59-04 Severity: MEDIUM (Class B)` and `F-S05-59-05 Severity: MEDIUM
(Class B)`; no corresponding findings[] records exist. Materiality note:
group 8's emitted severity is unchanged (tie {LOW:1, MEDIUM:1} resolves to
MEDIUM via SEV_ORDER; with S05C-59-05 included the majority would be a clean
MEDIUM:2), but group rosters and receipts under-enumerate their sources, and
group 3's computed seat count is false.

**Recommendation:** Add the four omitted records to findings[]; regenerate
the register; and gate the reverse direction: a build-time CI-8R check that
every finding enumerated in the shipped REPORTS file appears in findings[]
(parse report finding headers, set-compare, fail on difference).

### F-S01-60-05 | MEDIUM (Class B) | xz_protocol_register_gen.py lines 116-122; v0.60 body repair (iv)

**Substance:** Adjudication-receipt enforcement is existence-only. A
factually FALSE receipt (one whose stated source distribution contradicts
findings[]) is accepted, and the receipt text is not echoed into the
generated register -- the "mandatory adjudication_receipt on divergence" is
real but shallow: it proves a string is present, not that the string
adjudicates anything.

**Evidence (EXECUTED):** P-M3b: `group-4 divergence with factually FALSE
receipt: OUTPUT | accepted: True | receipt emitted in output: False`.
Generator lines 116-122 check only `"adjudication_receipt" not in g or not
g["adjudication_receipt"]` on divergence. Body repair (iv) claims enforcement
"(fail-closed)" -- true for absence, silent for falsity.

**Recommendation:** Validate receipt content: the receipt's restated source
distribution must equal the findings[]-computed distribution, and the receipt
must name the divergent group; reject or flag false receipts. Alternatively,
scope the claim to existence-only in the entry and methodology.

### F-S01-60-06 | MEDIUM (Class B) | register item (6) vs xz_protocol_register_gen.py validation; findings[] convergence_group refs 9-12

**Substance:** Register item (6) claims [COMPUTED: generate_register] "CI
v0.3 extends fail-closed validation to noted dispositions, findings[] IDs
(format + uniqueness), required fields, and cross-layer references." The
unqualified "cross-layer references" overclaims: only the
group->findings[] direction is validated (P-X2 raises); the reverse
findings[]->convergence_group direction is not (P-X1: convergence_group=99
accepted). The seven noted findings carry dangling convergence_group values
9-12 (no such groups exist in convergence_groups[]) and are accepted. The R18
triage repair item 7 said "reject dangling convergence_group values"; that
half did not land. Body repair (iv)'s narrower phrasing ("cross-layer
group-to-findings[] references") is accurate; the register's is not.

**Evidence (EXECUTED):** P-X1: `findings[] record convergence_group=99 (no
such group): OUTPUT | accepted: True`. Index census: findings[] records carry
convergence_group 9 (x3), 10 (x2), 11 (x1), 12 (x1); convergence_groups[]
holds group_ids 1-8 only. P-X2 (forward direction) RAISES as designed.

**Recommendation:** Validate the reverse direction (reject dangling
convergence_group values; give noted items an explicit null/noted reference
semantics), or narrow register item (6)'s claim to match body (iv).

### F-S01-60-07 | MEDIUM (Class B) | r18_findings_index.json seats[]/seat_roles[]/verdicts[] + v0.60 front matter line 5 + entry narrative vs R18_REPORTS.txt contents

**Substance:** The index asserts 10 seats including S01C ("carrying binding
continuous", Kimi K3) and S04C ("advisory continuous", Kimi K3), with
`verdicts: HALT` for both and `carrying_halts: 4`. The shipped R18_REPORTS.txt
contains exactly 8 seat-reports (S01F, S02F, S02C, S03F, S03C, S04F, S05F,
S05C); no S01C or S04C report is in the packet. The entry narrative ("10
seats (5 fresh + 5 continuous; ...)") carries the [ASSERTED] tag -- an honest
disclosure for the prose -- but the front-matter Status (line 5: "4 carrying
HALT binding, 6 advisory HALT; 10-seat round with 5 fresh + 5 continuous")
and the index data fields carry no such tag. Under packet closure the two
seat claims are unverifiable, and the carrying_halts=4 arithmetic depends on
one of them. This seat (S01) executed R18 as the sole S01 seat, in FRESH
mode; no S01C report exists from this seat.

**Evidence (EXECUTED):** CI-8 probe (logs/13_ci8_corrected.log):
`S01C verdict=HALT role=carrying binding continuous report_shipped=False`;
`S04C verdict=HALT role=advisory continuous report_shipped=False`.
R18_REPORTS.txt report-header census: 5 top-level documents covering 8
seat-reports; grep `S01C` / `S04C` = 0 hits. Index `seat_roles`: S01C =
"carrying binding continuous".

**Recommendation:** Ship the S01C/S04C reports in the packet, or retract the
two seat entries and recompute seats[]/verdicts[]/carrying_halts and the
front-matter/entry seat arithmetic from shipped evidence only. If the reports
exist but were withheld, this finding downgrades to a packet-completeness
defect; if they do not exist, it upgrades to Class A fabrication of a
carrying seat.

### F-S01-60-08 | LOW | AUDIT_CONTEXT(1).txt line 30 vs executed build output

**Substance:** Gate-count documentation, fifth consecutive round (R14-R19):
AUDIT_CONTEXT says "258 gates"; the executed build emits 257 `PASS:` gate
lines (the 258th "PASS" occurrence is the "BUILD PASSED" summary line).
build.py still prints no authoritative internal total. The register carries
the group NOTED (honest), so severity drops to LOW.

**Evidence (EXECUTED):** `grep -o 'PASS:' logs/04_build.log | wc -l` = 257;
`grep -o 'PASS' | wc -l` = 258 (includes "BUILD PASSED"). AUDIT_CONTEXT line
30, verbatim: `- build.py: 258 gates, all PASS`. CI_METHODOLOGY still
documents 222 (see F-S01-60-09).

**Recommendation:** Emit the gate count from build.py at runtime and inject
it into the dispatch context (R18 triage repair item 6, still unlanded).

### F-S01-60-09 | LOW | CI_METHODOLOGY(1).txt (whole file)

**Substance:** The shipped methodology is byte-identical to the R18 shipment
(diff-verified pre-freeze): it still ends at the "CI v0.2.1 UPGRADES"
appendix, still documents "222 gates", and contains no normative CI v0.3
schema -- two CI versions stale (v0.2.2, v0.3). R18 triage repair item 8
("publish normative CI schema") is not landed. The register carries the item
NOTED (honest).

**Evidence (EXECUTED):** `diff` R18-held copy vs R19 shipment: byte-identical.
The v0.3 semantics this round's entry claims (severity majority, receipt
enforcement, SCOPED_OUT vocabulary, correction_refs[]) have no normative
definition anywhere in the packet other than the generator's own docstring.

**Recommendation:** Publish the normative CI v0.3 section; mark the v0.2.1
appendix and the 222 count as historical.

### F-S01-60-10 | LOW | xz_protocol_register_gen.py adjudication rendering; register group 7 (NOTED)

**Substance:** COMPUTED tag scope remains unsplit (R18 triage repair item 9,
unlanded): hand-authored `triage_adjudication` prose is copied verbatim into
output lines tagged [COMPUTED: generate_register]. The register carries the
group NOTED (honest), so severity stays LOW -- but the mechanism is exactly
what lets F-S01-60-01's false "derivation" sentence ride a COMPUTED tag.

**Evidence (EXECUTED):** P-TAG: setting group 7 `triage_adjudication :=
SABOTAGE-TOKEN` produces output containing the token inside a
[COMPUTED: generate_register] line (`in COMPUTED-tagged output: True`).

**Recommendation:** Split the tag: [COMPUTED] for code-derived fields
(severity, convergence counts, correction refs) and [COPIED: index] (or
similar) for verbatim adjudication prose.

### F-S01-60-11 | INFO | entry terminal PRIOR_HISTORY line; R18_REPORTS.txt S05F internal profile

**Substance:** (a) The PRIOR_HISTORY line still carries no provenance tag
(carried from F-S01-59-09, honestly NOTED); (b) the (ci)-corrected R17 index
file remains outside packet closure; (c) observed during CI-8: the S05F
report's own "CLASS PROFILE: 3 HIGH (Class A), 2 MEDIUM (Class B)" is
internally inconsistent with its finding bodies (3 HIGH, 1 MEDIUM) -- the
index resolved toward the bodies, which is the correct reading, noted here
for the record.

**Evidence (EXECUTED):** v0.60 entry terminal line:
`PRIOR_HISTORY 5c28cf5a...` with no tag. CI-8 probe:
`S05F CLASS PROFILE line: 3 HIGH (Class A), 2 MEDIUM (Class B)` vs
`S05F finding-body severities: ['HIGH', 'HIGH', 'HIGH', 'MEDIUM']`.

**Recommendation:** Tag the PRIOR_HISTORY line ([COMPUTED: generate_terminal_line]
or its own tag); ship the corrected R17 index in a future packet if the (ci)
landing is to be auditable under closure.

## Section 7: CI v0.3 probe results (secondary lens)

| Probe | Result | Evidence |
|---|---|---|
| CI-1R (byte-exact register reproduction) | **PASS** | Generated register (4187 chars, sha256 627962aef7743ddb...) byte-contained in xz_protocol_v0_60.md; boundary contained; terminal line contained exactly once (logs/05_ci1r.log) |
| CI-4 (ASSERTED fraction < 15%) | **PASS** | Census of the v0.60 entry: 22 tagged claims = 1 ASSERTED, 17 COMPUTED, 3 DIFF-VERIFIED, 1 ENUMERATED -> ASSERTED 1/22 = 4.5% (logs/11_ci4.log). The character-basis ambiguity (R18 F-S02-59-04F/C) remains NOTED by the index; tag-basis reported here per R18 convention |
| CI-5 (Class A present?) | **PRESENT** | 4 HIGH findings (F-S01-60-01..04). R7-R19 = 13/13, H = 1.0. Laplace P(Class A at R20) = 14/15 = 0.933 |
| CI-8 (index vs reports) | **FAIL (6 items)** | Direction 1 (index -> reports): 35/35 findings[] records verified (IDs + severities, with the F/C suffix normalization); 7/7 noted items verified. Direction 1c (seats[]): 2 claimed seats (S01C, S04C) have no shipped reports. Direction 2 (reports -> index, new as CI-8R): 4 report findings omitted from findings[] (logs/13_ci8_corrected.log) |
| CI-8R (reports -> index completeness, NEW this round) | **FAIL (4 omissions)** | S03F Version-Token Staleness (HIGH), S03F Secondary Membership Schema Gap (HIGH), S05C F-S05-59-04 (MEDIUM), S05C F-S05-59-05 (MEDIUM) -- see F-S01-60-04 |

CI-8 heuristic note (method section, not a finding): the first CI-8 pass this
round reported 15/35 because the window-based matcher missed the index's F/C
suffix convention (the source reports carry unsuffixed IDs across FRESH and
CONTINUOUS sub-reports) and first-occurrence windows landed in summary
tables. After reading the report structure (8 sub-reports, boundaries
established by line census) the corrected matcher verifies 35/35. The void
first pass is recorded here as method, per discipline.

DIFF-VERIFIED tag audit (3 tags in the entry): (cg) values landed, gating
sub-claim false (F-S01-60-02); (ch) landing false (F-S01-60-03); (ci) landed
clean. Score: 1 clean, 1 partial, 1 false. The [DIFF-VERIFIED] tag is not
trustworthy on this packet -- each tag must be re-derived from bytes, exactly
as the COMPUTED-tag discipline requires.

## Section 8: Producer prediction scorecard (R19, P1-P12)

| # | Prediction (dispatch) | Score |
|---|---|---|
| P1 | CI-1R PASS | **CONFIRMED** |
| P2 | CI-8 PASS | **FALSIFIED** -- 6 substantive failures (2 ghost seats, 4 omitted findings); existing records verify 35/35 + 7/7 |
| P3 | ASSERTED < 15% | **CONFIRMED** (4.5% tag basis) |
| P4 | If Class A exists, on body/narrative/new CI v0.3 surface | **CONFIRMED** -- all 4 HIGH findings sit on the entry narrative / register / CI v0.3 claim surfaces; none in the 6 core modules |
| P5 | Count-list invariant | **CONFIRMED** (register 6 items + 9 NOTED; boundary list 35 items byte-matches generator output) |
| P6 | Append-only | **CONFIRMED** -- carried entries v0.1-v0.59 byte-identical to held v0.59 document (282,348 chars); PRIOR_HISTORY anchors to held v0.59 HISTORY |
| P7 | Code layer clean | **CONFIRMED** -- no defect executed in the 6 core modules; the false claims are about the generator, located in the entry/index text layer |
| P8 | Packet execution | **CONFIRMED** (build rc=0 BUILD PASSED; pytest 186; sums 19/19; seals 60/60; CI-1R PASS) |
| P9 | Severity derivation catches valid source-severity mutation | **PARTIAL** -- catches unreceipted divergent mutations (P-M2c RAISES); receipted divergent mutations pass invisibly with byte-identical output (P-M2b). The register's "either change output or fail generation" is byte-false (F-S01-60-01) |
| P10 | Receipt enforcement catches receipt removal | **CONFIRMED** for the mandated case (P-M3 RAISES under divergence). Note: receipt content is not validated (P-M3b; F-S01-60-05) |
| P11 | Correction-letter refs match body repairs | **CONFIRMED** (P-C1: explicit correction_refs[] -> (cg)/(ch)/(ci), aligned with the body ledger) |
| P12 | 22.2/22.3 bounds at v0.59 | **CONFIRMED** on values (lines 718/716). The accompanying gating claim is false (F-S01-60-02) -- P12 predicted values only |

10 CONFIRMED, 1 PARTIAL (P9), 1 FALSIFIED (P2). The producer's mechanical
predictions (P1, P3, P5-P8, P11, P12) all hold; its two semantic predictions
about the index and the severity mechanism (P2, P9) fail or half-fail -- the
same split as R18: mechanics converge, semantics do not.

## Section 9: Boundary report, provenance ledger, hedge audit, D-7

**Provenance ledger over the v0.60 entry** (logs/11_ci4.log): 22 tagged
claims -- 17 COMPUTED, 3 DIFF-VERIFIED, 1 ENUMERATED, 1 ASSERTED (4.5%).
COMPUTED-tag verification this round: (a) CI-1R reproduction PASS proves the
COMPUTED register lines are genuinely generator output; (b) P-TAG proves the
tag also covers verbatim-copied hand-authored prose (F-S01-60-10); (c)
F-S01-60-01 and F-S01-60-04 demonstrate two byte-false sentences riding
COMPUTED tags (F-CI-3R fires twice). DIFF-VERIFIED: audited above, 1/3 false
+ 1/3 partial. The ASSERTED paragraph honestly discloses the R18 narrative
summary -- but the same seat claims appear untagged in the front matter and
index data (F-S01-60-07).

**Boundary report (D-3.8):** the outermost uncomputed layer this round is the
**source-report -> findings[] ingestion step**. The generator computes
faithfully from findings[] (P-MAJ 8/8; CI-1R PASS), and the group->findings[]
reference direction is now gated (P-X2) -- but no gate verifies that
findings[] itself completely reflects the shipped reports (CI-8R ungated:
4 omissions), and no gate verifies that seats[]/verdicts[] reflect shipped
reports (2 ghost seats). What would bring it inside: a build-time CI-8R gate
(parse the shipped REPORTS file's finding headers; set-compare against
findings[] and seats[]; fail on any difference) plus the [DIFF-VERIFIED]
locus gate recommended in F-S01-60-03. Deeper standing layers unchanged:
execution environment unsealed; seal terminus at the Provenance marker (885
unsealed tail chars, disclosed); PRIOR_HISTORY anchored to held bytes for the
first time this round (SP9 CONFIRMED).

**Hedge/deferral audit (D-3.3):** the v0.60 entry's deferrals are carried
NOTED with honest dispositions (gate count, COMPUTED-tag scope, CI-4 metric,
CI_METHODOLOGY schema, PRIOR_HISTORY tag) -- the NOTED register is truthful
this round. The hedges found are in the affirmative claims instead:
"severity derivation" (verification, not derivation), "gated to VERSION-1"
(ungated), "cross-layer references" (one direction), "disposition changed ...
[DIFF-VERIFIED]" (unchanged). Each is a finding above.

**Coverage measurement (D-3.6):** mutation classes executed against CI v0.3:
severity tokens (valid + invalid), majority flips (receipted + unreceipted),
receipt removal, false receipt content, dangling references (both directions),
duplicate IDs, missing required fields, invalid dispositions (groups and
noted), sabotage token under COMPUTED, correction-ref alignment, severity
majority census. Classes NOT covered (disclosed): multi-correction groups
(no group this round consumes 2 corrections -- the (cc)+(cd) case has no
v0.60 analogue), SCOPED_OUT live rendering (vocabulary present, no group
uses it), CI-4 character-basis (metric undefined by the producer).

**D-7 four one-line answers:**
1. What would falsify the streak-continuation claim? A round with zero
   byte-false claims on sealed/COMPUTED surfaces -- not observed (4 HIGH).
2. What would falsify "mechanics converge"? A mechanical gate failure on
   unmodified bytes -- not observed (build/pytest/sums/seals/CI-1R all PASS).
3. What did this seat fail to check? Multi-correction group rendering and
   live SCOPED_OUT rendering (no exercised instance in the shipped index).
4. What is carried to R20? The held v0.60 bytes; the CI-8R gate
   recommendation; the 4 HIGH findings' repair verification.

## Section 10: Verdict, repairs, re-audit conditions

**Verdict: HALT (binding).** 4 HIGH (Class A), 3 MEDIUM (Class B), 3 LOW,
1 INFO. v0.60 does not break the Class A streak; R7-R19 = 13/13. This HALT
blocks deposit and convergence.

Mechanical gates (stated separately from substantive findings): build PASSED
(257 `PASS:` gates, rc=0); pytest 186/186; PACKET_SHA256SUMS 19/19 initial
and final; ENTRY seals 60/60; FULL_SECTION_27 recomputed match; manifest
matches trust roots; PRIOR_HISTORY anchors to held v0.59 HISTORY; append-only
byte-identical; CI-1R PASS; CI-4 4.5% PASS. All mechanical surfaces are
GREEN. The HALT rests entirely on semantic claim surfaces.

**Minimum repair set for v0.61:**
1. Retract or implement "severity derivation": emit the computed majority as
   the register severity, or reword to the honest cross-check form and add a
   P-M2b-class test (F-S01-60-01).
2. Implement the 22.2/22.3 VERSION-1 gate in build.py, or retract the gating
   clause from (cg) and register item (3) (F-S01-60-02).
3. Land (ch): set index group 4 disposition to SCOPED_OUT and regenerate;
   add a build gate that every [DIFF-VERIFIED] claimed string is byte-present
   at its claimed locus (F-S01-60-03).
4. Repair findings[] completeness (add the 4 omitted records; regenerate
   convergence counts) and gate the reports->index direction at build time
   (F-S01-60-04).
5. Validate receipt content against findings[] distributions, or scope the
   enforcement claim to existence-only (F-S01-60-05).
6. Extend cross-layer validation to findings[]->convergence_group references,
   or narrow register item (6)'s claim to match body (iv) (F-S01-60-06).
7. Ship the S01C/S04C reports or retract the 10-seat claims and recompute the
   seat/verdict/halt arithmetic from shipped evidence (F-S01-60-07).
8. Emit the gate count from build.py at runtime (F-S01-60-08).
9. Publish the normative CI v0.3 methodology section; mark v0.2.1/222 as
   historical (F-S01-60-09).
10. Split the COMPUTED tag scope (code-derived vs verbatim-copied prose)
    (F-S01-60-10).

**Re-audit conditions (R20):** re-run this battery (P-M2a/b/c, P-M3, P-M3b,
P-X1, P-X2, P-N1, P-N2, P-D1, P-C1, P-TAG, P-MAJ) on v0.61 bytes; re-run
CI-8/CI-8R against the R19 reports; re-verify each repair above on bytes
before scoring any discharge; anchor PRIOR_HISTORY to the held v0.60 HISTORY.

**Self-corrections ledger (this seat's own prior over-reaches):**
- R18 SP6 sub-refutation (dispatch gate count predicted accurate, was not) --
  recorded at R18; the same class recurs at R19 as SP6 CONFIRMED (258 vs 257).
- R19 SP2(a): this seat predicted receipted majority-flip mutations would
  change output or raise; they pass invisibly (P-M2b). Recorded as REFUTED.
- R19 SP11: this seat predicted the (ch) correction text would be truthful;
  its claimed landing is byte-false. Recorded as REFUTED.
- R19 CI-8 first pass (15/35) was a matcher artifact (F/C suffix convention,
  first-occurrence windows); corrected pass verifies 35/35 -- the void first
  pass is disclosed in Section 7 as method, not scored as a packet result.

---
*R19 audit executed by Seat S01 (Kimi K3, Moonshot AI -- not a default/blend/router), 2026-08-11 UTC. All findings rest on executed probes against the shipped bytes; canonical packet re-verified 19/19 OK after all probing. Verdict HALT is binding on carry.*
R19 AUDIT REPORT — Seat S02 (FRESH)
Model: GPT-5.6 Sol (OpenAI)
Role: CARRYING (BINDING)
Framework: Structural Revelation + CI v0.3
Round: 19
Version under audit: v0.60
Date: 2026-08-11

VERDICT: HALT (BINDING)

v0.60 does NOT break the R7-R18 Class A recurrence streak. Class A is present on v0.60 bytes. The streak extends to R7-R19 = 13/13 rounds.

EXECUTION RECORD
- Packet extraction: EXECUTED. 16 executable files extracted; 4 dispatch files copied to canonical names.
- python3 build.py: EXECUTED, rc=0, BUILD PASSED.
- Build census: 257 lines beginning "PASS:"; 258 occurrences of token PASS only when the final "BUILD PASSED" summary is included.
- pytest canonical command: EXECUTED, 186/186 passed.
- sha256sum -c PACKET_SHA256SUMS: EXECUTED, 19/19 OK.
- CI-1R: EXECUTED, PASS. Generated register is byte-exactly contained in the v0.60 protocol.
- Boundary reproduction: EXECUTED, PASS.
- Terminal generator identity: EXECUTED, PASS.
- Section 22.2 VERSION-1 bound: PASS, v0.1 through v0.59.
- Section 22.3 VERSION-1 carry lineage: PASS, v0.38-v0.59.
- ASSERTED fraction from build [9c]: 1/18 = 5.6%, PASS against <15% target.
- Canonical packet bytes were not modified; all adversarial probes ran on temporary copies.

F-S02-60-01F — HIGH / CLASS A
1. Locus: xz_protocol_register_gen.py severity derivation / receipt enforcement; protocol front-matter Status; v0.60 generated register item (1); DISPATCH M2/M3 targets.
2. Substance: CI v0.3 still does not make every valid source_severity change load-bearing and does not enforce adjudication receipts for mixed-source groups under the methodology's "differs from any source severity" rule. The implementation only checks whether triage severity differs from a computed majority.
3. Evidence: Baseline generated-register SHA-256 627962aef7743ddbb1c43b1cc85017d0654e0019838e7429980b7a6c546f2bfd. Mutating F-S01-59-03 source_severity HIGH->MEDIUM is accepted and yields the identical hash/output. Removing adjudication_receipt from group 4 (3 HIGH + 1 LOW, triage HIGH) is accepted and yields identical output. Removing it from group 8 (MEDIUM + LOW, triage MEDIUM) is also accepted and yields identical output. A sanity probe that changes group-1 triage_severity to MEDIUM with no receipt does fail, showing the code enforces only majority divergence, not the dispatched M2/M3 contract.
4. Consequence: The v0.60 closure claim "M2/M3-class mutations now either change output or fail generation" is byte-false. The central R18 Class A spec-implementation gap is not fully discharged. CI-1R reproduces the same false semantics deterministically.
5. Recommendation: Make source severity distribution itself load-bearing. Either fail on any source-severity mutation that invalidates the indexed adjudication state, or emit/validate the full distribution. Require a receipt whenever any source severity differs from triage severity, matching CI_METHODOLOGY, and add the exact M2/M3 mutations as tests.
6. Clearance condition: The exact M2 HIGH->MEDIUM mutation must change generated output or fail; receipt deletion from groups 4 and 8 must fail; no valid mutation may remain semantically inert where the dispatch says it is load-bearing.

F-S02-60-02F — HIGH / CLASS A
1. Locus: protocol Status line; v0.60 Body repairs correction (ch); r18_findings_index.json convergence group 4; generated register item (4).
2. Substance: v0.60 claims the secondary-membership disposition was corrected to SCOPED OUT, but the shipped machine-readable group remains disposition=CLOSED and has no scope_note.
3. Evidence: r18_findings_index.json group 4 is {triage_severity: HIGH, disposition: CLOSED, correction_refs: ["ch"]}. The protocol Status says "Secondary membership disposition corrected to SCOPED OUT." The body-repair ledger says correction (ch) changed the R18 findings-index group 4 to "SCOPED OUT: canonical-group rule retained, multi-membership not implemented" and marks that claim [DIFF-VERIFIED]. The generated register instead emits "HIGH CLOSED via append-only correction (ch)" while its adjudication prose says correction (ch) should change disposition to SCOPED_OUT.
4. Consequence: The claimed repair state and [DIFF-VERIFIED] statement are false on the shipped bytes. This is a direct Class A body/index contradiction.
5. Recommendation: Set group 4 disposition to SCOPED_OUT, add the truthful scope_note, and regenerate the register; or rewrite the repair claim if CLOSED is intentionally the current-group disposition and represent the corrected target state in a separate machine-readable repair object.
6. Clearance condition: The machine-readable state, generated register, Status line, and correction-(ch) body ledger must express one unambiguous, mutually consistent disposition.

F-S02-60-03F — HIGH / CLASS A
1. Locus: CI-8 index-source fidelity; r18_findings_index.json findings[]; R18_REPORTS.txt; CI_METHODOLOGY CI-8.
2. Substance: The authoritative findings[] IDs are not source-faithful. The index silently appends F/C mode suffixes to many source finding IDs, so the exact finding_id recorded in the index does not exist in the corresponding shipped seat report.
3. Evidence: Exact-string check against R18_REPORTS finds only 16/35 index finding IDs. Nineteen are absent, including all indexed S02F/S02C, S03F/S03C, and S05F/S05C forms such as F-S02-59-01F and F-S02-59-01C. R18_TRIAGE cites the underlying source IDs without those mode suffixes (e.g. both S02F and S02C use F-S02-59-01). No source_finding_id field or normalization receipt maps the renamed index IDs back to report bytes.
4. Consequence: CI-8's explicit rule that every finding_id in the index exists in its seat report fails. The register's traceability identifiers are synthetic rather than verbatim source identifiers. P2 (CI-8 PASS) is not established.
5. Recommendation: Preserve the literal source finding ID in source_finding_id and use a separate unique index key, or define and gate a normalization mapping that is lossless and explicit.
6. Clearance condition: Every authoritative index record must mechanically resolve to an exact source-report identifier without undocumented renaming.

F-S02-60-04F — MEDIUM / CLASS B
1. Locus: AUDIT_CONTEXT build-status claim; executed build output; CI_METHODOLOGY historical gate-count text.
2. Substance: Gate-count documentation remains inconsistent.
3. Evidence: AUDIT_CONTEXT says "build.py: 258 gates, all PASS." Executed output contains 257 lines beginning "PASS:". The number 258 is obtained only by counting the word PASS in the terminal summary "BUILD PASSED" as if it were an additional gate. CI_METHODOLOGY still carries the older 222-gate implementation text.
4. Consequence: The build itself is green, but the advertised gate cardinality remains hand-maintained and ambiguous, continuing the prior documentation-drift class.
5. Recommendation: Have build.py emit one authoritative machine-readable check count and import that value into audit context; stop counting summary text as a gate.
6. Clearance condition: Advertised gate count equals a runtime-emitted count under a formally defined counting unit.

OTHER REQUIRED TARGETS
- Correction-letter allocation: PASS on letter identity for current correction_refs (cg/ch/ci); no R18-style namespace collision reproduced. The blocking correction-(ch) issue is repair-state truth, not letter allocation.
- Section 22.2/22.3 VERSION-1: PASS at v0.59.
- Count-list invariant: PASS.
- Boundary list: PASS, 35 items.
- Packet hashes: PASS, 19/19.
- Tests: PASS, 186/186.
- Internal append-only/seal consistency: PASS via build; no claim of external independent prior-byte anchoring beyond shipped packet.

PRODUCER PREDICTIONS
P1 CI-1R PASS: CONFIRMED.
P2 CI-8 PASS: FALSIFIED on literal source finding-ID fidelity.
P3 ASSERTED <15%: CONFIRMED (5.6% tag census from build).
P4 If Class A exists, on body/new CI surface: CONFIRMED.
P5 Count-list invariant: CONFIRMED.
P6 Append-only holds: INTERNALLY CONFIRMED by shipped seal chain; external held-byte comparison not independently available in this fresh packet.
P7 Code layer clean: FALSIFIED semantically despite 186/186 tests and green build.
P8 ASSERTED verification <15% / packet ships: CONFIRMED.
P9 Severity derivation catches valid source-severity mutation: FALSIFIED by M2.
P10 Receipt enforcement catches removal on divergent group: FALSIFIED by M3 on groups 4 and 8 under CI_METHODOLOGY's any-source-divergence rule.
P11 Correction-letter refs match body repairs: LETTER MAPPING CONFIRMED; correction-(ch) repair substance itself is byte-false.
P12 Section 22.2/22.3 bounds at v0.59: CONFIRMED.

FINAL BINDING STATEMENT
VERDICT: HALT (CARRYING, BINDING).

v0.60 materially improves the prior packet: the executable substrate is complete, CI-1R is byte-exact, 186 tests pass, 19/19 hashes verify, VERSION-1 bounds are correct, and explicit correction_refs eliminate the prior correction-letter collision. But the core v0.3 closure does not satisfy its own dispatched mutation contract: M2 remains inert and M3 does not fail for the mixed-source groups that carry receipts. Separately, correction (ch) is represented inconsistently and CI-8 source-ID fidelity is not literal.

Therefore v0.60 does not break the recurrence. R7-R19 = 13/13 rounds with Class A present. FB-8 remains OPEN / PENDING RE-CARRY under the protocol's own governance state.
# R19 Seat S02 Continuous Audit Verdict — XZ Protocol v0.60

**Seat:** S02 — GPT-5.6 Sol (OpenAI)
**Role:** CARRYING / BINDING under the R19 dispatch
**Mode:** CONTINUOUS from R18 S02
**Framework:** Structural Revelation + CI v0.3 dispatch lens, checked against the shipped CI methodology
**Round:** 19
**Version under audit:** v0.60
**Date:** 2026-08-11

## VERDICT

# HALT (BINDING)

v0.60 does **not** break the R7–R18 Class-A recurrence streak. Class A remains present on v0.60 bytes. The streak is now **R7–R19 = 13/13 rounds with Class A present**. Under the protocol's Class A definition, the defects below are byte-false sealed/current-entry claims and are HALT-grade.

**FB-8 remains OPEN.**

The central result is again structural rather than cosmetic: v0.60 repairs several local symptoms, but the new CI v0.3 claims overstate what the generator and build actually enforce. The most important advertised closures fail the dispatch's own mutation targets.

---

## 1. Execution record

| Verification | Status | Result |
|---|---|---|
| Dispatch extraction | EXECUTED | PASS — 16 embedded packet files extracted, then the 4 dispatch-side canonical files copied exactly as `AUDIT_CONTEXT.txt` instructs |
| `sha256sum -c PACKET_SHA256SUMS` | EXECUTED | PASS — 19/19 manifest members OK after canonical copies |
| `python3 build.py` | EXECUTED | PASS — `BUILD PASSED: all checks GREEN` |
| Build PASS census | EXECUTED | 257 individual `PASS:` records plus the terminal `BUILD PASSED` summary (258 literal PASS occurrences) |
| Canonical pytest | EXECUTED | PASS — 186 passed |
| CI-1R register reproduction | EXECUTED | PASS — generated register length 4,187 bytes/chars, SHA-256 `627962aef7743ddbb1c43b1cc85017d0654e0019838e7429980b7a6c546f2bfd`, occurs exactly once byte-identically in v0.60 |
| ENTRY seals | EXECUTED | PASS — 60/60 current HISTORY ENTRY seals verified by build |
| FULL_SECTION_27 | EXECUTED | PASS |
| PRIOR_HISTORY | EXECUTED | PASS — derivation succeeded and matched shipped `5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d` |
| M2 valid `source_severity` mutation | EXECUTED | **FAIL target** — accepted with byte-identical register; full build can remain GREEN |
| M3 adjudication-receipt removal | EXECUTED | **FAIL target** — accepted with byte-identical register; full build can remain GREEN |
| Correction-reference/body-ledger coupling | EXECUTED | **FAIL** — a self-consistent `(zz)` register / `(cg)` body mismatch still builds GREEN |
| Section 22.2/22.3 VERSION-1 semantic gate | EXECUTED | **FAIL** — stale bounds still build GREEN after packet-manifest recomputation |
| CI-8 exact index-source ID fidelity | EXECUTED | **FAIL** — 19/35 top-level index finding IDs do not occur verbatim in `R18_REPORTS.txt` |
| findings[] cross-layer group reference validation | EXECUTED | **FAIL** — 7 shipped records point to nonexistent group IDs 9–12; mutation to group 999 is accepted byte-identically |

### CI-4 dead-space measurement

The old ambiguity remains material:

- Provenance-tag census: 1 ASSERTED / 22 recognized provenance tags = **4.55%**.
- Current-entry character measure using the ASSERTED narrative span: 1,488 / 9,161 = **16.24%**.

The declared under-15% target therefore passes or fails depending on the unit. CI v0.3 still does not normatively resolve this metric.

---

## 2. R18 S02 continuity re-verification

### R18 F-S02-59-01 — severity provenance / receipt enforcement

**NOT DISCHARGED.** The generator now reads `findings[]`, validates ID existence, computes a severity distribution, and checks a majority. That is a real improvement. But the R18 clearance condition was stronger: a valid source-severity mutation or required receipt deletion must not be semantically inert.

That clearance condition still fails. See F-S02-60-01.

### R18 F-S02-59-02 / F-S02-59-03 — secondary-membership label and correction-letter surface

The **specific one-letter-per-group cursor bug is removed**: explicit `correction_refs[]` are now emitted. The secondary-membership repair is also described more truthfully as a scope-out rather than an implemented multi-membership architecture.

However, the v0.60 closure claim introduces a new cross-layer defect: the body-repair ledger is **not** generated from the same correction-ref structure, and no build gate cross-checks the two surfaces. See F-S02-60-02.

### R18 Section 22 VERSION-1 defect

The text is locally corrected to v0.59, which is the correct VERSION-1 value for v0.60. But the claimed gate preventing recurrence does not exist. See F-S02-60-03.

### R18 CI-4 and gate-count documentation observations

CI-4 remains underspecified. The gate-count wording is somewhat improved only in the sense that 258 literal PASS occurrences can be obtained by counting the terminal summary; there are 257 individual `PASS:` verification records. I do not elevate this above MEDIUM because the current entry already retains the gate-count issue as NOTED.

---

## 3. Binding findings — six-element format

### F-S02-60-01 — HIGH / Class A

**1. Locus:** `PROTOCOL_v0_60.txt` front-matter Status line 5; current register group 1; `FINDINGS_INDEX.txt` lines 303–323; `REGISTER_GENERATOR.txt` lines 7–18 and 66–122; `CI_METHODOLOGY.txt` CI-8 / v0.2.1 receipt rules.

**2. Substance:** The claimed v0.60 repair that makes source severity load-bearing and makes adjudication-receipt removal fail is still incomplete. The generator checks only the **majority severity** and only the **presence/non-emptiness** of a receipt. It does not bind the receipt to the actual source-severity distribution, and many valid source-severity mutations remain output-inert.

**3. Evidence:** Executed mutation probes on shipped v0.60 code and index:

- M2: mutate the sole source finding in group 5, `F-S01-59-02`, from valid `HIGH` to valid `LOW` while leaving the pre-existing receipt unchanged -> **generator ACCEPTS; register byte-identical**. The stale receipt still says the source severity is HIGH and “No deviation,” but the generator checks only that some non-empty receipt exists after the mutation.
- M2b: mutate one group-1 source severity `F-S01-59-03` from `HIGH` to `LOW` -> majority remains HIGH -> **generator ACCEPTS; register byte-identical**.
- M3: delete `adjudication_receipt` from mixed-severity group 4 -> **generator ACCEPTS; register byte-identical** because triage HIGH still matches the source majority HIGH. This conflicts with the shipped CI v0.2.1 rule that a receipt is required where source severities differ.
- Full-packet M2 and M3 variants, with only the affected index digest updated in `PACKET_SHA256SUMS`, both run `build.py` to **BUILD PASSED** with 257 `PASS:` records.
- The positive partial repair is real: deleting a group-referenced finding record now raises `ValueError`.

**4. Consequence:** R18 Defect 1 is not discharged. `findings[]` is no longer wholly inert, but individual source-severity truth is not load-bearing and receipts are not authenticated against the evidence they purport to adjudicate. The current `[COMPUTED]` statement that “M2/M3-class mutations now either change output or fail generation” is byte-false.

**5. Recommendation:** Define one normative adjudication rule and bind it structurally. At minimum: emit or hash the exact source-severity distribution into the receipt; validate the receipt against that distribution; make every valid source-severity mutation either alter generated evidence or invalidate the receipt. If majority semantics are intended, update the methodology explicitly and still bind the receipt to the exact distribution rather than to mere non-emptiness.

**6. Falsifier / clearance condition:** Re-run the exact M2/M3 probes above. A changed valid source severity must either alter the generated register/evidence or fail because the receipt no longer matches; deleting a receipt that is required by the normative rule must fail.

---

### F-S02-60-02 — HIGH / Class A

**1. Locus:** `FINDINGS_INDEX.txt` group 2, especially line 339; `REGISTER_GENERATOR.txt` lines 159–180; v0.60 register item (2); v0.60 Body repairs ledger.

**2. Substance:** The current `[COMPUTED: generate_register]` claim says the **“Body-repair ledger [is] generated from same refs.”** It is not. `correction_refs[]` drive only the register disposition string. Neither `xz_protocol_register_gen.py` nor `build.py` generates or validates the body-repair ledger from those refs.

**3. Evidence:** Executed mutation and self-consistent reseal:

- Change group 3 `correction_refs` from `["cg"]` to `["zz"]`.
- Generator accepts and emits `CLOSED via append-only correction (zz)`.
- The protocol body-repair ledger remains `correction (cg): Section 22.2 ...`.
- Regenerate the current register in the current entry, recompute `ENTRY_v0.60`, `FULL_SECTION_27`, update the affected `HISTORY.sha256` lines, and update packet-manifest digests for the changed index/protocol/history.
- Result: **`build.py` still returns rc=0 with all 257 individual PASS records**, while the register cites `(zz)` and the body ledger cites `(cg)`.
- Static trace confirms `build.py` contains no `correction_refs` or body-ledger bijection check.

**4. Consequence:** The specific R18 cursor bug is repaired, but the repair did not implement the R18 clearance condition requiring a single-source correction namespace across register and body. The current computed adjudication statement is false. **F-CI-3R fires again** because a Class-A defect is inside a `[COMPUTED: generate_register]` claim.

**5. Recommendation:** Introduce structured `repair_actions[]` or a dedicated body-repair schema and generate **both** the register references and body-repair ledger from it. Add a bijection gate: every current correction ref resolves to exactly one intended repair; no body repair exists without a structured ref; no ref can be changed independently of its repair target.

**6. Falsifier / clearance condition:** The `(cg)->(zz)` mutation must fail generation/build unless the same structured mutation also changes the corresponding body-repair action. A self-consistent register/body mismatch must be impossible to seal GREEN.

---

### F-S02-60-03 — HIGH / Class A

**1. Locus:** front-matter Status line 5; `FINDINGS_INDEX.txt` group 3 lines 343–354; v0.60 Body repairs item (i); `build.py` Section 22 checks at lines 679–683.

**2. Substance:** v0.60 repeatedly claims Section 22.2/22.3 bounds are **“gated to VERSION-1.”** The text value is currently correct, but the semantic gate does not exist. `build.py`'s Section 22 check only verifies the phrase “gate execution is a build-time convenience.”

**3. Evidence:** Executed mutation:

- In Section 22, mutate correct `v0.1 through v0.59` -> stale `v0.1 through v0.58` and `v0.38-v0.59` -> stale `v0.38-v0.58`.
- Update only the protocol digest in `PACKET_SHA256SUMS` so the packet remains internally manifest-consistent.
- Run `build.py` -> **BUILD PASSED, 257/257 individual PASS records**.
- Static inspection finds no Section 22.2/22.3 bound parser or VERSION-1 check in `build.py`.

**4. Consequence:** R18 Defect 3 is corrected by hand on the current bytes but not structurally prevented. The current Status, register adjudication, and Body repairs `[DIFF-VERIFIED]` clause overstate the implemented control. This is a byte-false capability claim.

**5. Recommendation:** Add a dedicated build gate that parses exactly one Section 22.2 carried-entry bound and exactly one Section 22.3 carry-lineage upper bound, computes `VERSION-1`, and requires both upper endpoints to equal it. Add stale-by-one mutation fixtures.

**6. Falsifier / clearance condition:** The exact `.59 -> .58` mutation above must fail for a dedicated VERSION-1 reason even after the packet digest is recomputed.

---

### F-S02-60-04 — HIGH / Class A

**1. Locus:** `CI_METHODOLOGY.txt` CI-8 lines 362–365; `FINDINGS_INDEX.txt` top-level `findings[]`; `R18_REPORTS.txt`; v0.60 computed register.

**2. Substance:** CI-8 requires that **every `finding_id` in the index exists in its seat report**. The v0.60 R18 index violates that rule at scale: **19 of 35** top-level finding IDs do not occur verbatim anywhere in `R18_REPORTS.txt`.

**3. Evidence:** Exact-string census against the shipped reports finds the following absent IDs:

`F-S02-59-01F`, `F-S02-59-02F`, `F-S02-59-03F`, `F-S02-59-04F`, `F-S02-59-05F`, `F-S02-59-01C`, `F-S02-59-02C`, `F-S02-59-03C`, `F-S02-59-04C`, `F-S02-59-05C`, `F-S03-59-01F`, `F-S03-59-01C`, `F-S05-59-01F`, `F-S05-59-02F`, `F-S05-59-03F`, `F-S05-59-04F`, `F-S05-59-01C`, `F-S05-59-02C`, `F-S05-59-03C`.

The source reports instead use unsuffixed IDs such as `F-S02-59-01` in separate fresh/continuous reports. The index appears to synthesize `F`/`C` suffixes to disambiguate collisions, but it ships no `source_finding_id` / alias receipt that makes those synthetic IDs mechanically traceable under the stated CI-8 rule.

**4. Consequence:** CI-8 **FAILS exact index-source ID fidelity**. The code-generated register presents synthetic IDs as source finding IDs even though those exact IDs are absent from the seat reports. Deterministic reproduction from the index cannot repair a false provenance edge in the index itself.

**5. Recommendation:** Preserve source IDs verbatim and add a separate unique composite key such as `(seat_instance, source_finding_id)`, or add explicit `source_finding_id` plus `source_report_id/mode` fields with a validator that resolves each alias to exactly one report occurrence.

**6. Falsifier / clearance condition:** Every index finding must resolve mechanically to exactly one source-report finding whose literal source ID and severity match, without undocumented ID rewriting.

---

### F-S02-60-05 — HIGH / Class A

**1. Locus:** front-matter Status “cross-layer references” claim; `FINDINGS_INDEX.txt` group 8 lines 413–425; `REGISTER_GENERATOR.txt` validation lines 66–124; top-level `findings[].convergence_group` fields.

**2. Substance:** v0.60 claims cross-layer references are now fail-closed, but validation is one-directional: group `finding_ids` must resolve into `findings[]`; the reverse `findings[].convergence_group` field is never checked for existence or consistency.

**3. Evidence:**

- Shipped convergence-group objects exist only for IDs **1–8**.
- Seven shipped findings carry nonexistent `convergence_group` values **9–12**: `F-S01-59-09` -> 9; `F-S02-59-04F` -> 10; `F-S02-59-04C` -> 10; `F-S02-59-05C` -> 11; `F-S04-59-05` -> 9; `F-S04-59-06` -> 12; `F-S04-59-07` -> 9.
- Mutating a group-1 finding's `convergence_group` to **999** is accepted by `generate_register` and leaves the generated register byte-identical.

**4. Consequence:** The R18 validation-boundary defect is not fully discharged, and the current Status / group-8 closure claim that “cross-layer references” are validated is false. CI-8 membership fidelity cannot be established from this schema while the per-finding membership field is semantically inert.

**5. Recommendation:** Validate bidirectionally: every non-null `findings[].convergence_group` must exist; every group member's per-finding group must agree with the containing group (or with an explicit primary/secondary membership model); unique/non-converging findings should use `null` or a separate noted-group schema rather than dangling integers.

**6. Falsifier / clearance condition:** Changing a grouped finding's membership to 999 must fail, and the shipped index must contain zero dangling group references.

---

## 4. Non-blocking / retained observations

### O-S02-60-01 — MEDIUM: CI v0.3 is not normatively specified in `CI_METHODOLOGY.txt`

The methodology file ends with the **CI v0.2.1 upgrades**. It does not contain a normative CI v0.2.2 or v0.3 schema/rule appendix. This was already NOTED at R18 (`F-S04-59-06`) and remains unresolved. It now matters directly because the old methodology says receipts are required when source severities differ, while the v0.3 generator silently changes the rule to divergence from the **majority** only.

### O-S02-60-02 — MEDIUM: CI-4 metric remains basis-dependent

Tag-count basis = 4.55% ASSERTED; character-span basis = 16.24%. The under-15% target remains undefined until the numerator, denominator, and unit are normative.

### O-S02-60-03 — MEDIUM/NOTED: build-count wording remains convention-dependent

`AUDIT_CONTEXT.txt` says 258 gates. Executed output has 257 individual `PASS:` records plus one terminal `BUILD PASSED` line, yielding 258 literal PASS occurrences. Because the current index already keeps this defect class NOTED, I do not treat it as an additional blocker.

---

## 5. Structural Revelation verdicts

**REV-1 — code faithfully represents protocol claims: FAIL.** Source-severity mutation and receipt-removal claims are stronger than the implemented validation; Section 22 VERSION-1 gating is claimed but absent.

**REV-2 — index/register faithfully represent source findings: FAIL.** CI-8 exact ID fidelity fails for 19/35 top-level findings, and per-finding group membership is not load-bearing.

**REV-3 — narrative/register faithfully represent repair state: FAIL.** The current computed register says the body-repair ledger is generated from the same correction refs, but a self-consistent `(zz)`/`(cg)` mismatch builds GREEN.

**REV-4 — front matter faithfully represents body/code: FAIL.** The Status line's “adjudication receipt enforcement,” “cross-layer references,” and “Section 22.2/22.3 bounds gated to VERSION-1” claims overstate shipped enforcement.

**REV-5 — seal chain faithfully represents the shipped document: PASS internally.** 60/60 ENTRY seals, FULL_SECTION_27, PRIOR_HISTORY, and the packet manifest are internally consistent. As previously disclosed, self-consistent resealing cannot establish semantic truth; the correction-ref mutant demonstrates that distinction again.

---

## 6. CI probe outcomes

- **CI-1R:** PASS — shipped register is byte-identical to generator output on the shipped index.
- **CI-2:** PASS on generated count/list form.
- **CI-3 / F-CI-3R:** **F-CI-3R FIRES** due F-S02-60-01 and F-S02-60-02: false claims survive inside `[COMPUTED: generate_register]` output.
- **CI-4:** INDETERMINATE against the 15% threshold until basis is normative; tag basis passes, character basis fails.
- **CI-5:** FAIL target — first zero-Class-A round still not achieved; recurrence is now 13/13.
- **CI-8:** **FAIL** — exact source-ID fidelity and membership fidelity fail.

Post-R19 recurrence fraction: **13/13 = 1.0**. Laplace-smoothed next-round Class-A probability under the same stationarity model becomes **14/15 ≈ 0.933**.

---

## 7. Minimum repair set for v0.61

1. **Bind source severity and adjudication receipts to exact evidence**, not majority + non-empty string. Add the exact M2/M3 mutations as regression tests.
2. **Single-source correction references and body repairs.** Generate both surfaces from one `repair_actions[]` structure and add a bijection gate.
3. **Implement the claimed Section 22 VERSION-1 gate** with stale-by-one fixtures.
4. **Repair CI-8 identity provenance:** source IDs must remain literal or have an explicit alias mapping keyed by report instance/mode.
5. **Validate membership bidirectionally** and eliminate all dangling `convergence_group` references.
6. **Publish normative CI v0.3 methodology/schema**, explicitly superseding v0.2.1/v0.2.2 semantics.
7. **Define CI-4 mathematically** so the under-15% target has one reproducible value.

---

## 8. Final binding statement

**HALT.** v0.60 contains multiple Class-A / HIGH defects on newly claimed CI v0.3 control surfaces. The strongest positive result is that the architecture is becoming more explicit and the executable baseline remains clean (186/186 tests, manifest and seals consistent, CI-1R exact). But structural truth is not established by deterministic self-reproduction alone: the M2/M3, correction-reference, Section-22, CI-8 identity, and cross-layer-membership probes show that false semantics can still be reproduced and sealed consistently.

**R7–R19 Class-A streak: 13/13. FB-8 remains OPEN.**
# R19 Audit Result – Seat S03 (Gemini 3.1 Pro)

**VERDICT: HALT (ADVISORY)**
v0.60 does NOT break the R7-R18 Class A streak. The recurrence streak extends to R7-R19 (13/13).

---

## 1. Trace Summary
Initial logic and parameters are validated. Standard processing applied to the extracted 20-file executable packet, normative dependencies, and CI v0.3 verification targets.

---

## 2. CI v0.3 Verification Leaps
*   **M2/M3 Probes:** Adjudication receipt divergence mechanisms are technically intact, raising expected validation errors upon explicit deletion of receipts for divergent severities.
*   **Correction-Letter Refs:** Explicit per-group `correction_refs[]` allocation mechanically matches the body-repair ledger updates (`cg`, `ch`, `ci`).

---

## 3. Final Findings (Class A)
**F-S03-60-01 | HIGH (Class A) | Locus: `build.py` and `r18_findings_index.json` Group 3**
*   **Substance:** The R18 Group 3 adjudication explicitly claims "CI v0.3 gates both bounds to VERSION-1 (entry count minus one)". This claim is mathematically byte-false on shipped code. The `build.py` script successfully validates the `VERSION` string in gates `[2e]`, `[2f]`, `[2g]`, and `[10h]`, but entirely lacks a gate enforcing the `VERSION-1` rule for Section 22.2 and 22.3 bounds. This falsifies the `[COMPUTED: generate_register]` assertion generated by `xz_protocol_register_gen.py`.

---

## 4. Resolution Prescription
*   **Action:** Add the explicit `VERSION-1` verification gate for Section 22.2 and 22.3 into `build.py` to enforce the semantic rule actively claimed in the defect register.
# XZ Protocol v0.60 -- R19 Audit Result

**Seat:** S03 (Gemini 3.1 Pro)
**Role:** ADVISORY (Continuous)
**Framework:** Fractal Cube + Code Audit
**Target:** XZ Protocol v0.60 DRAFT CANDIDATE

## FINAL VERDICT: HALT (ADVISORY)
**CLASS A STREAK EXTENDS TO R19 (13/13 ROUNDS)**

The structural decay exhibits strict self-similarity across scales, aligning with the predictions of the Fractal Cube framework. While the CI v0.3 architecture upgrade successfully automates severity derivation from source records and enforces adjudication receipts, semantic gaps in parsing the index JSON result in new byte-false claims in the generated register.

The protocol's multi-round verification trajectory—managed under the Program Methodology Document (PMD) framework—requires strict adherence to executable truth. v0.60 does not yet meet the criteria for a FROZEN state.

---

## 1. Trace Summary
Initial logic and parameters are validated. Standard processing applied to the 20-file executable packet and normative dependencies.

The CI v0.3 architecture upgrade successfully discharges prior findings by automating severity derivation from source records and enforcing adjudication receipts. However, the introduction of this architecture has surfaced new specification-implementation gaps in parsing the index JSON.

---

## 2. Final Findings (Class A)

### F-S03-60-01 | HIGH (Class A) | Secondary Membership Disposition Remains False
**Substance:** The v0.60 protocol explicitly claims that the secondary membership disposition was successfully changed to "SCOPED OUT". This is byte-false.
**Evidence:** The `r18_findings_index.json` improperly retains `"disposition": "CLOSED"` for Group 4. Consequently, `generate_register` triggers the `disp == "CLOSED" and refs` logic, forcibly emitting `CLOSED via append-only correction (ch)`. The register never outputs the required `SCOPED OUT` string.

### F-S03-60-02 | HIGH (Class A) | Convergence Seat Undercounting
**Substance:** The generator systematically undercounts triage seat data due to a flawed ID parsing logic.
**Evidence:** The `_unique_seat_count` function extracts seat counts by splitting the finding ID and taking the second element (e.g., `F-S02-59-01F` becomes `S02`). Because the `F` (Fresh) or `C` (Continuous) mode suffix is appended to the finding number rather than the seat prefix, the algorithm incorrectly groups `S02F` and `S02C` into a singular `S02` entity. As a result, Group 1 emits `[5-seat / 8-finding convergence]` instead of the true `8-seat / 8-finding` convergence metric.

---

## 3. Repair Prescriptions
To align the protocol with the rigorous code-execution requirements of the Structural Honesty framework:
*   **Group 4 Disposition:** Update Group 4's `disposition` key in `r18_findings_index.json` to `"SCOPED_OUT"` to correctly trigger the intended `elif disp == "SCOPED_OUT"` branch in the generator.
*   **Seat Count Parsing:** Patch `_unique_seat_count` in `xz_protocol_register_gen.py` to map finding IDs against the authoritative `findings_by_id[fid]["seat"]` property rather than relying on a crude `split("-")[1]` string manipulation.
# R19 Seat S04 Audit Report -- XZ Protocol v0.60 DRAFT CANDIDATE

| Field | Value |
|---|---|
| Seat | S04, Round 19, ADVISORY (non-binding); findings carry equal triage weight |
| Authoring model | Kimi K3 (Moonshot AI), as named by the dispatch; not a default/blend/router. This platform exposes no checkpoint ID or weights revision; none is claimed |
| Producer (excluded) | Claude Opus 4.6 (Anthropic); barred from audit seats |
| Framework | Biomedical Fractal + Repair Verification (dispatch-assigned) |
| Version under audit | v0.60 (xz_protocol_v0_60.md, sha256 ecf817c12399e57648fcd8484624df348500581e3134d3abb2844299a7ade889) |
| Packet | 20-file executable packet (EXECUTABLE_PACKET(1).txt, 16 packed files + 4 dispatch-canonical files), staged at /mnt/agents/output/R19_S04_v060/packet/ |
| Dispatch | R19 DISPATCH -- Seat S04 (CONTINUOUS from R18), dated 2026-08-11 |
| Audit date | 2026-08-11 (UTC); S-0/S-1 frozen 2026-08-11T19:27:24Z, after PACKET_SHA256SUMS verification, before opening the v0.60 amendment entry |
| Execution surface | Linux x86_64 (kernel 5.10.134-18.0.11.lifsea8), Python 3.12.12, sh shell; EXECUTING seat (full packet present) |
| Mode | CONTINUOUS. Carried: METHOD ONLY plus held prior-round bytes from this seat's own R18 execution (/mnt/agents/output/R18_S04_v059/packet/), including held v0.59 HISTORY.sha256 (sha256 5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d). No prior conclusions carried as conclusions; every R18 finding re-adjudicated on v0.60 bytes |

## VERDICT: HALT (advisory, non-binding)

Two Class A (HIGH, byte-false) findings on v0.60 bytes, both on hand-written surfaces of this round's own repair -- the hand-written body-repair ledger and the front-matter Status line:

- **F-S04-60-01 (HIGH):** Correction (ch) never landed. The Status line claims "Secondary membership disposition corrected to SCOPED OUT"; body repair (ii) claims the disposition was changed to "SCOPED OUT: canonical-group rule retained, multi-membership not implemented" in the R18 findings index group 4, tagged [DIFF-VERIFIED]. On the shipped bytes: index group 4 disposition = "CLOSED"; the quoted target string occurs nowhere in the packet; the only SCOPED_OUT token in group 4 is inside its adjudication prose describing the plan; the computed register still emits "CLOSED via append-only correction (ch)".
- **F-S04-60-02 (HIGH):** The (cg) claim "both now gated to VERSION-1" (and the Status claim "Section 22.2/22.3 bounds gated to VERSION-1") is byte-false at the mechanism level. Executed mutation: on a sabotage byte copy with both bounds reverted to the stale v0.57 values and internally consistent regenerated sums, build.py prints BUILD PASSED: all checks GREEN. No gate binds the 22.2/22.3 bounds.

**Key question (dispatch): Does v0.60 break the R7-R18 Class A streak (12/12)? No.** The streak extends to R7-R19 (13/13, H = 1.0). Laplace P(Class A at R20) = 14/15 = 0.933 under stationarity.

The R18 mechanism repairs genuinely landed this round -- severity derivation computes from findings[] (M2b/M3 raise), receipt presence enforcement is fail-closed, correction letters allocate from explicit refs with zero letter collision, the validation boundary extension fires (M5c/M7a/M7d), and the PRIOR_HISTORY cross-anchor against this seat's held v0.59 HISTORY matches. The Class A defects are not in the mechanism; they are in the hand-written claims about the mechanism and about corrections that did not land. The metastasis boundary moved off the computed surface back onto tagged hand prose.

Severity totals: Class A (HIGH) = 2; Class B (MEDIUM) = 2; Class C (LOW) = 2; Class D = 0; Class E (INFO) = 1.

---

## 1. S-0 state declaration (frozen verbatim, 2026-08-11T19:27:24Z)

- Seat S04, Round 19, ADVISORY (non-binding), per DISPATCH(1).txt. Findings carry equal triage weight.
- Authoring model: Kimi K3 (Moonshot AI), as named by the dispatch; not a default/blend/router. No checkpoint ID or weights revision is exposed; none is claimed.
- Producer (excluded): Claude Opus 4.6 (Anthropic), barred from audit seats.
- Framework: Biomedical Fractal + Repair Verification (dispatch-assigned).
- Mode: CONTINUOUS from R18 (dispatch-declared). Carried: METHOD ONLY plus held prior-round bytes persisting on disk from this seat's own R18 execution, including the held v0.59 HISTORY.sha256 (5c28cf5a...). No prior conclusions carried; every R18 finding re-adjudicated on v0.60 bytes.
- Shipment: 10 dispatch .txt files; EXECUTABLE_PACKET(1).txt (16 packed) + 4 dispatch-canonical = 20-file packet.
- Packet integrity at freeze: PACKET_SHA256SUMS 19/19 OK, 0 FAILED, rc=0 (log 00).
- Execution surface: Linux x86_64, Python 3.12.12, sh shell. EXECUTING seat.
- Newly testable this round: PRIOR_HISTORY cross-anchor against the held v0.59 HISTORY; append-only byte comparison of the code layer against held v0.59 copies.
- Context age: this session continues from the R18 session. Metadata visibility: upload dir + sandbox clock only.

Freeze file preserved at /mnt/agents/output/R19_S04_v060/S0_S1_FREEZE.md.

## 2. S-1 preregistered predictions, scored post-hoc

| # | Prediction (frozen) | Score | Basis |
|---|---|---|---|
| S1-P1 | CI-1R byte-exact, exactly 1 occurrence | HELD | register span 4187 chars, sha256 627962aef7743ddbb1c43b1cc85017d0654e0019838e7429980b7a6c546f2bfd, 1 occurrence (log 04) |
| S1-P2 | F-S04-59-01 discharged; letter-collision census zero | HELD | letters from explicit correction_refs; register-cited {cg,ch,ci} == body-defined {cg,ch,ci}, referents match; census zero (log 09c) |
| S1-P3 | F-S04-59-02 discharged by claim correction; at least one of M2/M3 still silent | PARTIAL | mechanism genuinely implemented (M2b/M3 RAISE) -- first clause refuted; M2 shape still silent when a receipt is present (M2a ACCEPT, output byte-identical) -- second clause held |
| S1-P4 | Streak continues: at least one Class A on v0.60 | HELD | F-S04-60-01, F-S04-60-02 |
| S1-P5 | Class A sits on this round's repair-layer surfaces | HELD | both Class A findings are on v0.60's own corrections (ch)/(cg): hand-written ledger + Status line |
| S1-P6 | ASSERTED fraction under 15% on the OCCURRENCE basis (pre-registered basis) | HELD | 1/22 = 4.5% (log 10); character basis 16.2% reported for continuity, not the preregistered test |
| S1-P7 | PRIOR_HISTORY cross-anchors; code diff = stamps + generator only | HELD | cross-anchor OK (log 05); 12 code files 2-line stamps, build.py 10 lines, trust roots version+digest, generator 195 changed lines (logs 06/06b/06c) |
| S1-P8 | Gate-count documentation repaired | REFUTED | AUDIT_CONTEXT(1) claims "258 gates"; executed PASS: lines = 257 (258 = PASS-token lines incl. the BUILD PASSED banner); item remains NOTED |

6 HELD / 1 PARTIAL / 1 REFUTED / 0 NOT REACHED.

## 3. Execution record -- all dispatch verifications EXECUTED

| Verification (dispatch order) | Status | Result |
|---|---|---|
| Extraction (16 packed) + 4 canonical copies | EXECUTED | 20 files staged; listing verified (log 00a) |
| `python3 build.py` | EXECUTED -- PASS | "BUILD PASSED: all checks GREEN", rc=0; 257 executed PASS: lines (log 01); AUDIT_CONTEXT(1) claims 258 gates (F-S04-59-03 carried, NOTED) |
| pytest six-file canonical list | EXECUTED -- PASS | 186 passed in 8.10s standalone (log 02); 186 passed inside build gate [8] |
| `sha256sum -c PACKET_SHA256SUMS` | EXECUTED -- PASS | 19/19 OK, rc=0 at intake (log 00) and re-verified after all probing (log 11) |
| CI-1R register reproduction vs r18 index | EXECUTED -- PASS | register span byte-exact, 4187 chars, exactly 1 occurrence; boundary 1797 chars; terminal unique and final (log 04) |
| HISTORY.sha256 seal chain | EXECUTED -- PASS | 60/60 ENTRY seals recomputed match; FULL_SECTION_27 matches; PRIOR_HISTORY derivation consistent AND cross-anchored to held v0.59 HISTORY (log 05) |
| PRIOR_HISTORY cross-anchor (newly testable) | EXECUTED -- PASS | held v0.59 HISTORY.sha256 hashes 5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d == the v0.60 HISTORY PRIOR_HISTORY line == the v0.60 entry tail value (log 05; entry tail observed bare of tag) |
| Append-only code-layer diff vs held v0.59 | EXECUTED | 12 code modules 2-line version stamps each; build.py 10 changed lines (version, protocol name, VERSION, number-word table +60, index filename); trust roots version + manifest digest; generator 195 changed lines (the CI v0.3 repair); boundaries version field only; AUDIT_CONTEXT rewritten for R19; CI_METHODOLOGY byte-identical (logs 06/06b/06c) |
| Mutation battery vs CI v0.3 generator | EXECUTED | 20 probes M0-M13 with vacuity (M0 byte-equal baseline) and discrimination controls (log 08); plus build-level sabotage probe (log 08b) |
| CI-8 index-vs-reports fidelity | EXECUTED -- PASS with scope note | 20/42 index IDs textual in R18_REPORTS with matching severities; the 22 F/C-suffixed IDs resolve to their base forms (F-S02-59-01F -> F-S02-59-01, present); the suffix mapping is undocumented (F-S04-60-05) |
| CI-4 tag census | EXECUTED | ASSERTED 1/22 = 4.5% occurrence basis; narrative char share 16.2%; hand-written share incl. body-repair ledger 29.8% (log 10) |

Nothing in this report is marked ASSERTED from the producer; every dispatch-listed verification ran on shipped bytes in this sandbox.

### Independent recomputation (auditor-side code, never importing build.py)

| Surface | Value | Result |
|---|---|---|
| PACKET_SHA256SUMS | 19 OK, 0 FAILED, rc=0 | OK |
| ENTRY seals | 60/60 recomputed match (60 entries parsed) | OK |
| ENTRY_v0.60 | 4c61123c33a2be0f5b2454e758760b2b7214fbeb12acdba0d797e531f62e9520 | recomputed == HISTORY line |
| FULL_SECTION_27 | 5c378abc7d6cf635b477afd871f3f58fd737a7691329b6a55532b8936312852c | recomputed == HISTORY line |
| Unsealed tail after Provenance terminator | 885 chars | reported, unsealed by design |
| manifest_digest (12 ALL_CODE_FILES parsed from build.py source) | bbd5c385016fab921283db4a7e4afcfb74c224adff982e5f1ca40f7afa1fab80 | recomputed == trust-roots value |
| PRIOR_HISTORY | 5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d | cross-anchored to held v0.59 HISTORY bytes (sha256 of held file matches) |

Standing values are recomputed and reported verbatim for producer comparison; no seal equality with any producer-retained value is claimed.

## 4. R18 clearance verification on v0.60 bytes (Repair Verification lens)

| R18 finding | Claimed disposition in v0.60 | Verified on v0.60 bytes |
|---|---|---|
| F-S04-59-01 (HIGH) letter collision | CLOSED via CI v0.3 (group 2) | DISCHARGED. correction_refs[] per group; letter census register {cg,ch,ci} == body {cg,ch,ci}, referents match; zero collision. Residual: letter uniqueness and register-to-ledger grounding unenforced (M8/M8b ACCEPT) -- F-S04-60-04 |
| F-S04-59-02 (HIGH) derivation/receipt overclaim | CLOSED via CI v0.3 (group 1) | DISCHARGED as claimed. Derivation computes from findings[]: M2b (flip + receipt removed) RAISES; M3 (unreceipted override) RAISES; receipts present on all 8 groups; group 4/8 receipts document elevations with correct distributions. Residual one layer down: receipt CONTENT unvalidated (M2a/M3b/M3c ACCEPT) -- F-S04-60-03 |
| F-S04-59-03 (MEDIUM) gate-count docs | NOTED (register) | NOT DISCHARGED, carried consistently. AUDIT_CONTEXT(1) claims "258 gates"; executed 257 PASS: lines (258 counts the BUILD PASSED banner); CI_METHODOLOGY byte-identical (still 222-era). Register disposition NOTED -- consistent |
| F-S04-59-04 (MEDIUM) validation boundary | CLOSED via CI v0.3 (group 6) | DISCHARGED as claimed. M5c (group->findings[] dangling) RAISES; M7a (noted disposition) RAISES; M7d (noted missing substance) RAISES; no dangling group-number refs in index text. Boundary map beyond the claim: noted ID format/uniqueness (M7b/M7c) and orphan findings[] records (M13) remain open -- not claimed; INFO |
| F-S04-59-05 (LOW) (cf) closure scope | NOTED (register, as F-S01-59-09/F-S04-59-05) | CARRIED consistently. r16_findings_index.json still does not ship; the (ci) correction records the fixed distribution in the R18 index instead. Scope note on (ci): the correction landed as adjudication prose in group 5, not as a machine-readable receipt field; the original false receipt lives in the R17 index, outside this packet's closure |
| F-S04-59-06 (LOW) CI v0.2.2/v0.3 schema | NOTED (register) | NOT DISCHARGED, carried consistently. CI_METHODOLOGY byte-identical to v0.59 shipment; no normative CI v0.3 schema anywhere in the dispatch set |
| F-S04-59-07 (INFO) carried observations | NOTED (register) | CARRIED. (i) no byte-identity register gate (build.py [10c]/[10d]/[10e] remain substring/proximity gates); (ii) PRIOR_HISTORY tail value still untagged; (iii) version arg still uncoupled from register output (generate_register ignores it); (iv) ASSERTED basis dependence persists (4.5% occurrence vs 16.2% char); (v) body-repair ledger still glued onto the final NOTED line (line 1369) |
| R18 Defect 3 (F-S01-59-01): 22.2/22.3 bounds stale at v0.57 | CLOSED via (cg), "gated to VERSION-1" | TEXT DISCHARGED / GATE CLAIM FALSE. Lines 716/718 now read "v0.38-v0.59" / "v0.1 through v0.59" = VERSION-1, correct. The "gated" clause is byte-false: no gate binds the bounds (executed mutation, log 08b) -- F-S04-60-02. Self-correction: this seat's R18 discharge verified the literal R17 repair target, not the VERSION-1 rule; S01F's staleness call was correct (section 11) |
| R18 Defect 4 (secondary membership label) | CLOSED via (ch), Status: "corrected to SCOPED OUT" | NOT LANDED. Index group 4 disposition = CLOSED; no scope-note string anywhere; register still emits CLOSED via (ch) -- F-S04-60-01 |

Regression check on repaired surfaces: no regressions detected. Entry count 60 (gate [9] PASS); 186/186 tests GREEN; the R17-era repairs ((cc)/(cd) bounds text, narrative counts, group receipts) verified clean on held-byte diffs and on the current index; stale v0.55/v0.56 bound tokens exist only inside sealed carried entries.

## 5. Mutation battery results (CI v0.3 generator; 20 probes, log 08)

| Probe | Shape | Result | Verdict on the CI v0.3 claims |
|---|---|---|---|
| M0 | unmodified index | ACCEPT, byte_equal_to_shipped=True | vacuity/discrimination control live |
| M1 | findings[] malformed ID | RAISE ValueError | as claimed |
| M2a | valid source_severity flip, receipt kept (F-S01-59-01 HIGH->LOW) | ACCEPT, output byte-identical | receipt now stale; content unchecked (F-S04-60-03) |
| M2b | same flip + receipt removed | RAISE ValueError (divergence, no receipt) | derivation + presence enforcement LIVE |
| M3 | unreceipted override (group 6 MEDIUM->HIGH, receipt dropped) | RAISE ValueError | fail-closed as claimed |
| M3b | divergence + receipt "x" | ACCEPT | receipt content unvalidated (F-S04-60-03) |
| M3c | false receipt content vs distribution | ACCEPT, output identical | receipt content never parsed (F-S04-60-03) |
| M4 | group disposition OPEN | RAISE ValueError | as claimed |
| M5a/M5b | group malformed / duplicate ID | RAISE ValueError | as claimed |
| M5c | group->findings[] dangling ref (F-S99-99-99) | RAISE ValueError | cross-layer as claimed |
| M6b | findings[] duplicate ID | RAISE ValueError | as claimed |
| M7a | noted disposition OPEN | RAISE ValueError | boundary extension as claimed |
| M7b/M7c | noted malformed / duplicate ID | ACCEPT | not claimed; boundary map (INFO) |
| M7d | noted missing substance | RAISE ValueError | required-fields as claimed |
| M8 | duplicate correction letter (cg on two groups) | ACCEPT, register emits (cg) twice | letter uniqueness unenforced (F-S04-60-04) |
| M8b | orphan correction letter (zz, no body definition) | ACCEPT | no register-to-ledger grounding (F-S04-60-04) |
| M10 | group with empty finding_ids | RAISE ValueError (max() empty) | fail-closed but uncontrolled (F-S04-60-06) |
| M11 | findings[] record missing source_severity key | RAISE KeyError | fail-closed but uncontrolled (F-S04-60-06) |
| M13 | orphan findings[] record (unreferenced) | ACCEPT, output identical | reverse cross-layer not claimed (INFO) |

Build-level probe (log 08b): sabotage byte copy with 22.2/22.3 bounds reverted to v0.57 and regenerated internally-consistent sums -> "BUILD PASSED: all checks GREEN". The bounds are not gated (F-S04-60-02). The same harness FAILED the copy when its sums were inconsistent, so the PASS on stale bounds is discriminating evidence, not a vacuous run.

## 6. Findings (six-element)

### F-S04-60-01 | HIGH (Class A) | Front matter line 5 (Status); entry line 1369 body repair (ii); r18_findings_index.json group 4

- **Substance:** Correction (ch) never landed. Status: "Secondary membership disposition corrected to SCOPED OUT." Body repair (ii): disposition "changed from 'CLOSED via CI v0.2.2 architecture repair' to 'SCOPED OUT: canonical-group rule retained, multi-membership not implemented' in the R18 findings index group 4", tagged [DIFF-VERIFIED]. On the shipped bytes: index group 4 disposition = "CLOSED"; the string "SCOPED OUT: canonical-group rule retained" occurs nowhere in the packet (0 occurrences of "SCOPED OUT" outside the Status line and the body-repair quote itself; "canonical-group rule retained" 0 occurrences in the index); the only SCOPED_OUT token in group 4 sits inside its triage_adjudication prose stating the plan ("Correction (ch): change disposition to SCOPED_OUT with truthful scope note"); the computed register emits "(4) ... HIGH CLOSED via append-only correction (ch)". The CI v0.3 generator HAS a SCOPED_OUT pathway (disposition + scope_note) -- it was not used. The hand-written surfaces claim a state change the machine-readable record does not contain.
- **Evidence (EXECUTED):** index group 4 dump (log 09b: "disposition": "CLOSED", correction_refs ["ch"]); string census ("SCOPED_OUT" 1 occurrence in the index, inside adjudication prose; "canonical-group rule retained" 0); protocol census ("SCOPED OUT" 2 occurrences: line 5 Status, line 1369 body-repair quote); register line (4) text (log 03). Falsifier: r18_findings_index.json group 4 carries disposition "SCOPED_OUT" with the claimed scope note, and the register emits it.
- **Recommendation:** land the correction in the index (disposition "SCOPED_OUT" + scope_note), regenerate the register, and let the emitted register text -- not the Status line -- carry the disposition; or withdraw the claim. Add a gate or CI-8-style cross-check that every body-repair (letter) claim's quoted target string exists at its named locus.

### F-S04-60-02 | HIGH (Class A) | Front matter line 5 (Status); entry line 1369 body repair (i); build.py (absence)

- **Substance:** Body repair (i) claims the 22.2/22.3 bounds were advanced to v0.59 AND "both now gated to VERSION-1" [DIFF-VERIFIED]; the Status line repeats "Section 22.2/22.3 bounds gated to VERSION-1". The text correction landed (lines 716/718 verified at v0.59 = VERSION-1). The gate does not exist: build.py contains no check binding the 22.2/22.3 bound tokens to VERSION-1 (gate inventory [1]-[12]: no bounds gate; the only VERSION-1 logic is gate [2f]'s Status-provenance clause). Executed mutation: on a byte copy with both bounds reverted to the stale v0.57 values and sums regenerated for internal consistency, build.py printed "BUILD PASSED: all checks GREEN" (log 08b). The exact R18 staleness class survives the full gate suite; only the current text happens to be correct.
- **Evidence (EXECUTED):** log 08b (BUILD PASSED on stale bounds; discrimination: same harness FAILED the copy when sums were inconsistent); build.py gate inventory (log 06b diff: 10 changed lines, no new gates); lines 716/718 at v0.59 values. Falsifier: the same mutation FAILS the build on v0.61 bytes.
- **Recommendation:** add a bounds gate deriving "v0.1 through v0.{VERSION-1}" and "v0.38-v0.{VERSION-1}" from VERSION and checking both sections; or correct (i) and the Status line to "advanced to VERSION-1" without the gated claim. Note the recurrence arithmetic: this class has now appeared at R13-R18 on bounds TEXT; v0.60 adds the false GATE claim -- the class moved from the text to the claim about the text.

### F-S04-60-03 | MEDIUM (Class B) | xz_protocol_register_gen.py lines 110-122; mutation battery M2a/M3b/M3c

- **Substance:** Receipt content is unvalidated. CI v0.3 requires adjudication_receipt PRESENCE on divergence (implemented, M2b/M3 fail-closed), but never parses the receipt against the source distribution: a valid source_severity mutation with the receipt retained passes silently with byte-identical output and a now-stale receipt (M2a); a garbage receipt "x" passes (M3b); a receipt contradicting the distribution passes (M3c). Receipts are hand-written prose asserting distributions -- the R17 group 6 miscount (2M+1L vs actual 3M+1L, corrected this round via (ci)) is exactly the class a content check would catch. The Status claim "adjudication receipt enforcement implemented (mandatory on divergence)" is satisfied by presence enforcement; the residual is that the enforced artifact's content is unchecked, so a false receipt rides the enforcement.
- **Evidence (EXECUTED):** log 08 M2a (ACCEPT, output_differs=False), M3b (ACCEPT), M3c (ACCEPT, output_differs=False); generator lines 116-122 (presence-only check). Falsifier: a receipt whose stated distribution contradicts findings[] fails generation.
- **Recommendation:** parse the receipt's stated per-finding severities (or a machine-readable receipt field) and verify against findings[]; or document presence-only scope in AUDIT_CONTEXT and the docstring.

### F-S04-60-04 | MEDIUM (Class B) | xz_protocol_register_gen.py lines 159-172 (correction_refs consumption); build.py (no letter gate)

- **Substance:** The F-S04-59-01 repair moved lettering to explicit correction_refs[] but left the namespace unenforced: duplicate letters across groups pass silently and emit a colliding register (M8: two groups citing (cg)); orphan letters with no body-ledger definition pass (M8b: (zz) emitted); and no gate ties register-cited letters to body-ledger definitions. On shipped bytes the letters are unique and consistent (census zero), so this is a latent gap, not a byte-false claim -- but F-S04-60-01 demonstrates the consequence class this round: register item (4) cites (ch) while the body definition of (ch) is false, and nothing in the pipeline connects the two surfaces. The R18 repair prescription included a collision gate; it was not implemented.
- **Evidence (EXECUTED):** log 08 M8 (ACCEPT, output emits (cg) twice), M8b (ACCEPT); letter census (log 09c); generator source (refs emitted verbatim, no uniqueness check). Falsifier: duplicate or orphan correction letters fail generation or fail the build.
- **Recommendation:** enforce letter uniqueness across groups at generation; generate the body-repair ledger from the same refs (single-source the last hand-written register-adjacent surface); add a build gate matching register-cited letters against ledger-defined letters.

### F-S04-60-05 | LOW (Class C) | r18_findings_index.json findings[] IDs vs R18_REPORTS.txt

- **Substance:** CI-8 passes with an undocumented mapping. 22 of 42 index IDs carry F/C instance suffixes (F-S02-59-01F) that never appear textually in the source reports; the reports use base IDs with instance labels outside the ID ("S02F: F-S02-59-01"). The suffixing is a 1:1 mechanical derivation (verifiable against R18_TRIAGE lines), all 22 base forms resolve with matching severities, and the convention is internally consistent -- but it is documented nowhere: not in the index, not in the triage header, not in a schema. A fresh seat cannot derive the mapping rule from the artifacts alone; CI-8's "index fidelity to source records" currently depends on an unstated convention.
- **Evidence (EXECUTED):** log 09c (20/42 textual, 22 suffixed; zero severity mismatches on resolved base forms); R18_TRIAGE.txt line 25/38 format "S01F: F-S01-59-03". Falsifier: the index or triage documents the suffix rule, or suffixed IDs appear in the reports.
- **Recommendation:** document the F/C suffix rule in the index header (one line) or in the CI v0.3 schema; better: record source_pointer fields (report file + line) per findings[] record.

### F-S04-60-06 | LOW (Class C) | xz_protocol_register_gen.py lines 111-114 (derivation edge cases)

- **Substance:** Two degenerate inputs fail closed but uncontrolled: a group with empty finding_ids crashes on max() over an empty Counter (M10: ValueError "max() iterable argument is empty"); a findings[] record missing the source_severity key crashes with a raw KeyError (M11) because line 111 uses [] while the validation pass at line 82 uses .get with a default. Both refuse generation (fail-closed, the safe direction), but neither produces a named validation error, and M11's crash bypasses the file:line-quality diagnostics every other validation path provides.
- **Evidence (EXECUTED):** log 08 M10/M11 outputs. Falsifier: both shapes raise ValueError with the group/finding named.
- **Recommendation:** validate non-empty finding_ids per group and required findings[] fields (source_severity) up front with named errors.

### F-S04-60-07 | INFORMATIONAL (Class E) | carried observations and boundary map

- **Substance:** (i) No byte-identity register gate persists (build.py [10c]/[10d]/[10e] remain substring/proximity gates; CI-1R is audit-side only) -- F-S04-59-07(i) carried. (ii) PRIOR_HISTORY tail value still untagged (line 1369 tail). (iii) generate_register's version argument still uncoupled from output. (iv) ASSERTED fraction basis-dependent: 4.5% occurrence (1/22), 16.2% character (narrative 1488/9161 chars); the hand-written share including the untagged body-repair ledger is 29.8% -- F-S02-59-04F/04C (NOTED) acknowledge the ambiguity; this report fixes the occurrence basis per its preregistration. (v) Boundary map beyond the claimed validation frontier (all ACCEPT, none claimed): noted ID format/uniqueness (M7b/M7c), orphan findings[] records (M13). (vi) Cosmetic: body-repair ledger glued onto the final NOTED line again (line 1369). (vii) AUDIT_CONTEXT(1) "258 gates" vs 257 executed PASS: lines -- the R14-recurring count ambiguity in a new coat (F-S04-59-03 carried NOTED). (viii) CI_METHODOLOGY byte-identical: no normative CI v0.3 schema (F-S04-59-06 carried NOTED).
- **Evidence (EXECUTED):** build.py gate inventory; line 1369 tail; log 10 census; log 08 M7b/M7c/M13; log 01 count; CI_METHODOLOGY cmp (log 06).
- **Recommendation:** per R18, plus: single-source the body-repair ledger into the generator (removes the largest remaining hand-written surface and the (ch)-class with it). Falsifier: none required at INFO.

## 7. Provenance ledger over the v0.60 entry

| Entry component | Tag | Auditor status |
|---|---|---|
| Narrative paragraph (1488 chars) | [ASSERTED] | Every quantitative claim verified against r18_findings_index.json: Defect 1 "8 findings across 5 seats" = index group 1 (8 IDs, 5 seats); Defect 2 "6 findings across 4 seats" = group 2; "4 carrying HALT / 6 advisory HALT" = index verdict fields (10/10 HALT, 4/6); "261 PASS / 186 GREEN / 19/19 / 59/59" = this seat's R18 executed values. Clean |
| Register items (1)-(6) + NOTED block (9 items) | [COMPUTED: generate_register] x15 | EXECUTED byte-exact (CI-1R, 4187 chars, 1 occurrence); derivation replayed per group (8/8 triage == majority; receipts present, group 4/8 contents match distributions); mutation-verified (M0-M13). Item (4)'s cited letter (ch) points at a false body definition -- F-S04-60-01/04 |
| Body repairs (i)-(iv) | [DIFF-VERIFIED] x3 + [COMPUTED: build.py] x1 | (i) text verified, "gated" clause FALSE (F-S04-60-02); (ii) FALSE (F-S04-60-01); (iii) verified as adjudication prose in the R18 index (scope note: not a machine-readable receipt; original false receipt in the R17 index, outside closure); (iv) mechanism claims probed M0-M13 -- presence enforcement real, content enforcement absent (F-S04-60-03); the [COMPUTED: build.py] tag covers a generator whose behaviors build.py does not gate |
| Boundary list (35 items) | [COMPUTED: generate_boundary_list] + [ENUMERATED: 35 items] | EXECUTED byte-exact (1797 chars); content carried from v0.59 |
| PRIOR_HISTORY 5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d | untagged | EXECUTED cross-anchor: equals sha256 of this seat's held v0.59 HISTORY.sha256 (F-S04-58-07 tag omission carried; the anchor itself now verified) |
| Terminal line (unsealed tail) | [COMPUTED: generate_terminal_line] | EXECUTED: identical to generator output, unique, final |

Tag census (occurrence basis, log 10): COMPUTED 17, ASSERTED 1, DIFF-VERIFIED 3, ENUMERATED 1; total 22. Headline number: ASSERTED fraction 4.5% occurrence basis (preregistered basis; < 15%, S1-P6 HELD); 16.2% character-share basis; 29.8% hand-written share including the body-repair ledger. F-CI-2 remains satisfied. The two false tags this round are DIFF-VERIFIED, not ASSERTED: the falsity moved into the tagged-verifiable hand prose.

## 8. Biomedical Fractal lens: the metastasis boundary (standing question)

R17: "data shipped, mechanism absent". R18: "validation shipped, semantics absent" (mechanism layer). R19: the mechanism LANDED -- derivation computes, presence enforcement fails closed, refs allocate, the boundary extension fires. The defect moved off the computed surface entirely and now lives on the last two hand-written surfaces:

1. **The tagged-hand-prose seam (F-S04-60-01, F-S04-60-02).** The body-repair ledger and the Status line are hand-written but wear verifiability tags ([DIFF-VERIFIED], Status assertion style). Both Class A findings are claims about corrections/gates that do not exist on bytes -- one claims a landed state change (ch) that the index contradicts, one claims a gate (cg) that the build contradicts. In R18 the false claims were about the generator's semantics; in v0.60 they are about the producer's own repair actions. The tag economy metastasized: falsity now wears DIFF-VERIFIED.
2. **The receipt-content seam (F-S04-60-03).** One layer inside the landed mechanism: presence is enforced, truth is not. The R17 miscount class (a false receipt) would pass CI v0.3 unchanged.

The generator remains outside the tested code layer: the 12 manifest files (6 modules + 6 suites, 186 tests) do not include xz_protocol_register_gen.py, so the suite stays green regardless of generator behavior; every generator assurance is audit-side (CI-1R + mutation battery), none is build-side.

Predicted residual for R20: (i) whatever surface the (ch)/(cg) repairs introduce (a letter-grounding gate, a bounds gate, a single-sourced ledger -- each is a new computed surface to probe), and (ii) the receipt-content seam if repaired by schema.

## 9. Producer predictions, scored post-hoc

| # | Prediction | Score | Basis |
|---|---|---|---|
| P1 | CI-1R PASS | CONFIRMED | byte-exact, 1 occurrence, 4187 chars |
| P2 | CI-8 PASS | CONFIRMED with scope note | all IDs resolve (22 via undocumented F/C suffix mapping); zero severity mismatches; F-S04-60-05 |
| P3 | ASSERTED < 15% | PARTIAL | 4.5% occurrence (under); 16.2% character (over); basis still undefined packet-side (F-S02-59-04F NOTED) |
| P4 | If Class A exists: body/narrative/new CI v0.3 surface | CONFIRMED | both Class A on the v0.60 body-repair ledger + Status (hand-written repair claims) |
| P5 | Count-list invariant | CONFIRMED | dual-cardinality brackets computed from finding_ids; gate [10e] PASS |
| P6 | Append-only holds | CONFIRMED | first round testable at this seat: cross-anchor OK; code-layer diff = stamps + generator only |
| P7 | Code layer clean | PARTIAL | 186/186 GREEN; generator outside the manifest and untested by the suites; M2a/M3b/M3c/M8 shapes pass silently |
| P8 | Packet executes | CONFIRMED | BUILD PASSED, 186 GREEN, 19/19 OK, 60/60 seals, cross-anchor OK |
| P9 | Severity derivation catches valid source-severity mutation | FALSIFIED | M2a: valid flip with receipt retained ACCEPTED, output byte-identical, receipt silently stale; detection works only when the receipt is also removed (M2b) |
| P10 | Receipt enforcement catches receipt removal | CONFIRMED | M3/M2b RAISE fail-closed |
| P11 | Correction-letter refs match body repairs | CONFIRMED at letter level | census zero; the (ch) referent falsity is F-S04-60-01 (referent truth, not letter allocation) |
| P12 | 22.2/22.3 bounds at v0.59 | CONFIRMED | lines 716/718 at VERSION-1; the accompanying "gated" claim is false (F-S04-60-02) |

6 CONFIRMED / 1 CONFIRMED-with-note / 2 PARTIAL / 1 FALSIFIED.

CI falsification status: F-CI-1 (first zero-Class-A round) NOT ACHIEVED -- extends to R19 (13/13). F-CI-2 (ASSERTED decrease) SATISFIED. F-CI-3R (Class A inside a [COMPUTED: generate_register] claim) NOT TRIGGERED this round: the computed register is internally consistent with the index; the Class A pair lives on hand-written surfaces (a reversion toward the ASSERTED-floor pattern, but on DIFF-VERIFIED-tagged prose, so F-CI-6R containment to the ASSERTED floor is NOT SATISFIED in spirit -- the ledger escaped the floor by wearing a verifiability tag). F-CI-7R (CI-1R fails) NOT TRIGGERED.

## 10. Boundary report, hedge audit, D-7

- Outermost uncomputed layer at this seat: none structural remains at the seal layer -- the PRIOR_HISTORY cross-anchor and append-only byte comparison came INSIDE this round (held v0.59 bytes). The new outermost layer: the R18 non-executing seats' reports (R18_REPORTS covers 10 seat instances; this seat verified index-to-report fidelity textually, not each seat's execution) and the producer-retained sealed values (P23-05 standing). What brings them inside: executing-seat attestations from those seats; nothing this seat can compute.
- Hedge/deferral audit: no hedged findings; every finding names its falsifier. Open enumerations stated as questions, not assertions: whether the producer intends to land (ch) in the index or withdraw the claim; which counting convention should define the documented gate count.
- D-7 four one-line answers: (1) Verified: the full 20-file packet -- 257 gates, 186 tests, 19/19 sums, 60/60 seals, cross-anchor to held v0.59 HISTORY, CI-1R, CI-8 (with mapping note), CI-4 both bases, narrative counts, every R18 repair locus, 20-probe generator battery + build-level sabotage probe, append-only code diff. (2) Asserted: nothing producer-side. (3) Failed: two Class A ((ch) never landed; (cg) gate claim false), two Class B (receipt content; letter grounding), two Class C, carried INFO. (4) Next round must re-run: CI-1R, CI-4 (both bases), CI-8, the battery including M2a/M3b/M3c/M8 shapes, the bounds-gate mutation (F-S04-60-02 falsifier), the (ch) index check (F-S04-60-01 falsifier), and the cross-anchor against held v0.60 HISTORY bytes (this packet's HISTORY.sha256 now held at /mnt/agents/output/R19_S04_v060/packet/HISTORY.sha256, sha256 c216241d86676d0b794b096205844586f80ebd2d73af28929d971fffe0c1fbcf).

## 11. Verdict, repairs, and re-audit conditions

Severity totals: Class A (HIGH) = 2 (F-S04-60-01, F-S04-60-02); Class B (MEDIUM) = 2 (F-S04-60-03, F-S04-60-04); Class C (LOW) = 2 (F-S04-60-05, F-S04-60-06); Class D = 0; Class E (INFO) = 1 (F-S04-60-07).

**VERDICT: HALT (advisory, non-binding).** Class A present (2 findings). As an advisory verdict this does not block convergence by itself; it is recorded with equal triage weight, and the binding carrying seats govern. Recurrence series: R7-R19, 13/13, H = 1.0. Laplace P(Class A at R20) = 14/15 = 0.933.

Minimum repair set before re-carry (v0.61):

1. Land (ch) in the index (disposition SCOPED_OUT + scope_note) and regenerate, or withdraw the Status/(ii) claims; add a cross-check that every body-repair letter's quoted target string exists at its named locus (F-S04-60-01).
2. Add the VERSION-1 bounds gate for 22.2/22.3, or correct (i)/Status to drop "gated" (F-S04-60-02).
3. Validate receipt content against findings[] distributions, or document presence-only scope (F-S04-60-03); enforce correction-letter uniqueness and register-to-ledger grounding, ideally by single-sourcing the body-repair ledger into the generator (F-S04-60-04).
4. Document the F/C suffix mapping or add source_pointer fields (F-S04-60-05); named validation errors for empty finding_ids and missing source_severity (F-S04-60-06).

Re-audit conditions for R20: re-run CI-1R, CI-4 (both bases), CI-8; re-run the battery including M2a/M3b/M3c/M8 shapes; re-run the bounds-gate sabotage probe; verify (ch) at the index level; anchor PRIOR_HISTORY against the held v0.60 HISTORY bytes identified in section 10.

## 12. Self-corrections ledger

- R18 under-call: this seat's R18 clearance discharged the 22.2/22.3 bounds row on the basis that the R17 repair target (v0.57) landed and no older stale tokens remained in the body. The semantically correct check was the VERSION-1 rule (at v0.59, carried entries run to v0.58); S01F's staleness call was right and this seat's discharge was wrong on the rule. The R18 triage paraphrases this seat as holding "bounds at v0.57 = correct for v0.58 carried entries" -- the substance (we discharged it) is correct; the reasoning attributed is over-specified. Recorded as a preregistration lesson: clearance checks must test the semantic rule, not the repair's literal target.
- S1-P3 split as predicted shapes shifted: the M2/M3 silence this seat expected from claim-only repair instead arrived as receipt-content blindness (M2a) after a real mechanism landing. The prediction's letter (silence persists) held; its mechanism (no implementation) was refuted.
- No other prior-round self-corrections to carry; R18's three ledger entries were discharged into this round's preregistration (fixed occurrence basis).

## 13. Final integrity statement

All probing executed on byte copies under /mnt/agents/output/R19_S04_v060/probes/ (mutation_battery_r19.py; buildcopy/ sabotage copy with regenerated sums); the canonical packet was never modified: PACKET_SHA256SUMS re-verified 19/19 OK after all probing (log 11), and the dispatch upload files re-hashed (log 12). Verbatim evidence preserved at /mnt/agents/output/R19_S04_v060/logs/ (00 packet sums, 00a listing, 00b freeze time, 01 build, 02 pytest, 03 register regen, 04 CI-1R, 05 independent recompute with cross-anchor, 06/06b/06c append-only diffs, 07 entry slices, 07c body-repair ledger, 08 battery, 08b bounds-gate mutation, 09 derivation replay, 09b group 4/5 records, 09c CI-8 + letter census, 10 CI-4 census, 11 final sums, 12 upload integrity). S-0/S-1 freeze preserved at /mnt/agents/output/R19_S04_v060/S0_S1_FREEZE.md. Held v0.60 HISTORY.sha256 retained for the R20 cross-anchor. No external documents were fetched or admitted as evidence; audit evidence is the shipped bytes only (packet closure). Standing values in this report match the executed outputs verbatim.

---

*R19 Seat S04 advisory audit executed by Kimi K3 (Moonshot AI), continuous from R18, 2026-08-11.*
*Framework: Biomedical Fractal + Repair Verification.*
*Bismillah.*
# R19 Audit Report — Seat S05 (FRESH)

**Protocol:** XZ Protocol v0.60
**Round:** R19
**Seat:** S05 — GPT-5.6 Sol (OpenAI), advisory / non-binding
**Lens:** Differentiator + Adversarial Probing
**Producer:** Claude Opus 4.6 (barred from audit seats)
**Date:** 2026-08-11

## Verdict

**HALT (advisory, non-binding).**

v0.60 does **not** break the R7–R18 Class A recurrence streak. Class A remains present on shipped v0.60 bytes, extending the recurrence through **R7–R19 = 13/13 rounds**.

The decisive failures are not baseline execution failures: `build.py`, pytest, hashes, and byte-exact register reproduction all pass. The failure is semantic closure. CI v0.3 still makes byte-false claims about source-severity load-bearing behavior, cross-layer validation, Section 22 VERSION-1 gating, and one landed SCOPED_OUT correction.

## Executed baseline verification

| Verification | Result | Status |
|---|---:|---|
| `python3 build.py` | `BUILD PASSED: all checks GREEN` | EXECUTED PASS |
| Canonical pytest command | 186 passed | EXECUTED PASS |
| `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | EXECUTED PASS |
| CI-1R register reproduction | generated register is exact substring of protocol | EXECUTED PASS |
| HISTORY.sha256 | 60/60 entries + FULL_SECTION_27 + PRIOR_HISTORY PASS | EXECUTED PASS |
| ASSERTED fraction | 1/18 = 5.6% | EXECUTED PASS |
| Section 22.2 bound | `v0.1 through v0.59` | EXECUTED PASS |
| Section 22.3 lineage | `v0.38-v0.59` | EXECUTED PASS |
| `PASS:` records emitted by build | 257 | EXECUTED |

## Adversarial mutation results

| Probe | Result |
|---|---|
| M2a: group-1 source severity HIGH→MEDIUM, majority still HIGH | **ACCEPTED; generated register byte-identical** |
| M2b: sole group-3 source severity HIGH→MEDIUM, majority flips to MEDIUM while triage stays HIGH and receipt remains | **ACCEPTED; generated register byte-identical** |
| M3a: remove receipt from mixed-source group 4 (3 HIGH + 1 LOW; triage HIGH) | **ACCEPTED; byte-identical** |
| M3b: synthetically create majority divergence in group 3 and remove receipt | FAIL-CLOSED with `ValueError` |
| M3c: create majority divergence but retain a factually stale nonempty receipt | **ACCEPTED; byte-identical** |
| Cross-layer: change `findings[].convergence_group` from 1 to 999 | **ACCEPTED; byte-identical** |

The baseline index itself contains dangling `convergence_group` values 9, 10, 11, and 12 although `convergence_groups` contains only IDs 1–8.

---

## Findings — six-element format

### F-S05-60-01

**Severity:** HIGH (Class A)
**Locus:** `xz_protocol_v0_60.md` front-matter Status; v0.60 register item (1); `r18_findings_index.json` group 1; `xz_protocol_register_gen.py` lines 110–122 and 147–180.

**Substance:** CI v0.3 claims actual severity derivation from authoritative `findings[]` source records and explicitly claims M2/M3-class mutations now either change output or fail generation. The implementation computes a majority only to decide whether a nonempty receipt must exist. Emitted severity remains `group["triage_severity"]`; source severity is never emitted or otherwise made output-determinative. A valid source-severity mutation can therefore be semantically invisible.

**Evidence (EXECUTED):** Changing F-S01-59-01 from HIGH to MEDIUM flips group 3's computed source majority to MEDIUM while triage severity remains HIGH. Because a nonempty receipt already exists, generation succeeds and the register SHA-256 remains exactly `627962aef7743ddbb1c43b1cc85017d0654e0019838e7429980b7a6c546f2bfd`, identical to baseline. A less aggressive HIGH→MEDIUM mutation in group 1 is also byte-identical.

**Recommendation:** Make source-severity derivation load-bearing. Either derive emitted severity mechanically or make every divergence receipt structured and machine-validated against the computed distribution. Add a canonical M2 test asserting that any valid source-severity mutation must change generated bytes or fail.

### F-S05-60-02

**Severity:** HIGH (Class A)
**Locus:** protocol front-matter Status; v0.60 register item (6); `r18_findings_index.json` findings and convergence groups; `xz_protocol_register_gen.py` validation loop.

**Substance:** v0.60 claims the validation boundary now covers cross-layer references, and group 8 is CLOSED via CI v0.3 architecture repair. The shipped index contradicts that closure: findings contain `convergence_group` values 9, 10, 11, and 12 while the only declared convergence groups are 1–8. The generator never validates each finding record's scalar `convergence_group` against declared group IDs or against actual membership.

**Evidence (EXECUTED):** Baseline enumeration finds seven dangling records: F-S01-59-09→9, F-S02-59-04F/C→10, F-S02-59-05C→11, F-S04-59-05/07→9, and F-S04-59-06→12. Generation and full build still pass. Mutating F-S01-59-03's `convergence_group` from 1 to 999 also succeeds with byte-identical register output.

**Recommendation:** Validate every `findings[].convergence_group` against the declared group set; require membership parity between the scalar field and each group's `finding_ids`; define an explicit value such as `null` for intentionally ungrouped/noted findings instead of dangling pseudo-groups.

### F-S05-60-03

**Severity:** HIGH (Class A)
**Locus:** protocol Status line; current v0.60 body repair (ch); `AUDIT_CONTEXT.txt`; `r18_findings_index.json` group 4.

**Substance:** v0.60 says the secondary-membership disposition was corrected to SCOPED OUT. The current body repair states, with `[DIFF-VERIFIED]`, that R18 findings-index group 4 was changed from CLOSED to `SCOPED_OUT`. The shipped index still has `"disposition": "CLOSED"` for group 4 and no `scope_note` field. The declared landed diff is therefore false on the shipped bytes.

**Evidence (EXECUTED):** `r18_findings_index.json` group 4 has `triage_severity: HIGH`, `disposition: CLOSED`, `correction_refs: ["ch"]`, while its own adjudication text says correction (ch) is to change the disposition to SCOPED_OUT. The generator correspondingly emits `CLOSED via append-only correction (ch)`.

**Recommendation:** Either actually set the intended record to `SCOPED_OUT` with a machine-readable `scope_note`, or rewrite the correction statement to truthfully describe an append-only correction without falsely claiming the index field was changed. Add a landed-diff assertion for correction (ch).

### F-S05-60-04

**Severity:** HIGH (Class A)
**Locus:** protocol Status line; v0.60 register group-3 adjudication; current body repair (cg); `build.py` Section [10].

**Substance:** The Section 22.2/22.3 *values* are correctly advanced to VERSION-1 (`v0.59`), but v0.60 repeatedly claims both bounds are now gated to VERSION-1. No such gate exists in the shipped build logic.

**Evidence (EXECUTED/static):** `build.py` lines 679–683 define the only Section 22-specific gate and check only that the phrase `gate execution is a build-time convenience` is present. There is no check for the 22.2 `v0.1 through v0.59` token or the 22.3 `v0.38-v0.59` token anywhere in the executable packet. The current values are correct manually, but the claimed gate is absent.

**Recommendation:** Add explicit checks that derive expected prior version from `VERSION` and assert both Section 22 tokens exactly match it. Add mutation tests that independently stale each bound by one version and require build failure.

### F-S05-60-05

**Severity:** HIGH (Class A)
**Locus:** v0.60 generated register item (2); `r18_findings_index.json` group 2; `xz_protocol_register_gen.py` functions `generate_register`, `generate_boundary_list`, `generate_terminal_line`.

**Substance:** Register item (2), inside `[COMPUTED: generate_register]`, states that the “Body-repair ledger [is] generated from the same refs.” The shipped generator does not generate a body-repair ledger at all. It only generates the defect register, boundary list, and terminal line, and copies `triage_adjudication` verbatim from the hand-authored index.

**Evidence (static):** The module exposes no body-ledger generation or body-ledger cross-check. Lines 174–180 simply append `group['triage_adjudication']` to a line tagged `[COMPUTED: generate_register]`. The current cg/ch/ci letters happen to appear in both register and body prose, but their semantic coupling is not generated from one source as claimed.

**Recommendation:** Split COMPUTED scope: tag only fields truly derived by code, or generate the body-repair ledger from the same structured repair records and verify byte-level identity against the protocol entry.

### F-S05-60-06

**Severity:** MEDIUM (Class B / documentation inconsistency)
**Locus:** `AUDIT_CONTEXT.txt` build-status line; executed build output; `CI_METHODOLOGY.txt` historical gate-count step.

**Substance:** Gate-count documentation remains unreconciled. `AUDIT_CONTEXT.txt` says `build.py: 258 gates, all PASS`, while the executed build emits 257 indented `PASS:` records. The 258th occurrence of the token `PASS` is the terminal `BUILD PASSED` summary, not a gate. The methodology also retains the old `222 gates` workflow count.

**Evidence (EXECUTED):** `grep -c '^  PASS:'` on the executed build log returns 257; counting all occurrences of the string `PASS` returns 258 only because the final summary contains `PASSED`.

**Recommendation:** Maintain an internal counter incremented only by actual gate checks and print it in the build summary; inject that machine-derived count into dispatch context. Mark the methodology's 222 as historical if intentionally retained.

---

## Producer prediction scorecard

| Prediction | Result |
|---|---|
| P1 CI-1R PASS | CONFIRMED |
| P2 CI-8 PASS | **FALSIFIED** — dangling/mutable cross-layer group references remain |
| P3 ASSERTED < 15% | CONFIRMED — 5.6% |
| P4 Class A, if any, on body/new CI surface | CONFIRMED |
| P5 Count-list invariant | CONFIRMED |
| P6 Append-only | INTERNALLY CONFIRMED by shipped seals; no external prior anchor at fresh seat |
| P7 Code layer clean | **FALSIFIED** |
| P8 ASSERTED verification < 15% | CONFIRMED |
| P9 valid source-severity mutation changes output or fails | **FALSIFIED** |
| P10 receipt removal on true majority divergence fails | PARTIAL — synthetic majority divergence fails closed; stale nonempty receipts are accepted and existing mixed-source receipts are removable |
| P11 correction letters match body repairs | PARTIAL — cg/ch/ci labels align textually, but body-ledger same-source-generation claim is false and (ch) landed-diff claim is false |
| P12 22.2/22.3 bounds at v0.59 | VALUES CONFIRMED; **gating claim falsified** |

## Recurrence answer

**Does v0.60 break the R7–R18 Class A streak? No.**

Class A is present at R19, extending the observed run to **R7–R19 = 13/13 rounds**. Under the same Laplace-smoothed stationarity convention, the next-round predictive value becomes **14/15 ≈ 0.933**.

## Minimum repair set for v0.61

1. Make valid source-severity mutations load-bearing: derive output or machine-validate structured divergence receipts.
2. Enforce both directions of findings↔group membership and reject dangling `convergence_group` values.
3. Land correction (ch) truthfully; remove the false `[DIFF-VERIFIED]` statement unless the bytes actually change to SCOPED_OUT.
4. Add real VERSION-1 gates for Sections 22.2 and 22.3 with mutation tests.
5. Generate or cross-check the body-repair ledger from the same structured `correction_refs` source; narrow `[COMPUTED]` tags to actual computed content.
6. Programmatically report gate count.

**Final seat verdict: HALT (advisory, non-binding).**
# R19 Audit Report — Seat S05 (CONTINUOUS)

**Protocol:** XZ Protocol v0.60
**Round:** R19
**Seat:** S05 — GPT-5.6 Sol (OpenAI), advisory / non-binding
**Lens:** Differentiator + Adversarial
**Mode:** CONTINUOUS from R18 S05
**Producer:** Claude Opus 4.6 (barred from audit seats)
**Date:** 2026-08-11

## Verdict

**HALT (advisory, non-binding).**

v0.60 does **not** break the R7–R18 Class A recurrence streak. CI v0.3 repairs several concrete R18 defects, but the central provenance/receipt closure claim is still false under the exact continuity mutations, CI-8 source identity fails on the shipped index, and the claimed Section 22 VERSION-1 gate does not exist in `build.py`.

Class A therefore remains present at R19, extending the recurrence series to **R7–R19 = 13/13 rounds with Class A present**.

The strongest continuity failure is direct: the generated R18 defect-register item (1) says, under `[COMPUTED: generate_register]`, that CI v0.3 implements source-derived severity, mandatory adjudication receipts on divergence, and that “M2/M3-class mutations now either change output or fail generation.” On the shipped v0.60 generator, both M2 and M3 remain inert for the relevant current index shapes.

---

## 1. Executed baseline verification

| Verification | Result | Status |
|---|---:|---|
| Packet reconstruction from supplied dispatch bytes | 19 normative members available after canonical-name copy step | EXECUTED PASS |
| `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | EXECUTED PASS |
| `python3 build.py` | `BUILD PASSED: all checks GREEN` | EXECUTED PASS |
| Canonical pytest command | 186 passed in 18.24s | EXECUTED PASS |
| CI-1R register reproduction | generated register is byte-exactly present in protocol | EXECUTED PASS |
| Boundary-list reproduction | generated boundary list present byte-exactly | EXECUTED PASS |
| Terminal-line reproduction | generated terminal line present | EXECUTED PASS |
| HISTORY entry seals | build verifies 60/60 entries + FULL_SECTION_27 + PRIOR_HISTORY | EXECUTED PASS |
| ASSERTED fraction | 1/18 = 5.6% | EXECUTED PASS |
| Python runtime | 3.13.5 | EXECUTED |
| Build PASS-line count | 257 `PASS:` lines | EXECUTED |

The producer/context claim of **258 gates** is not reproduced by the established PASS-line metric: the executed build emits **257** `PASS:` records.

---

## 2. R18 S05 continuity discharge matrix

| R18 S05 finding | v0.60 continuity result |
|---|---|
| **F-S05-59-01 — findings[] / severity / receipt semantics inert** | **NOT DISCHARGED.** Source-severity mutations, receipt removal on the mixed-severity group, receipt-content falsification, and top-level membership mutation remain semantically inert. |
| **F-S05-59-02 — correction-letter cursor misalignment** | **PARTIALLY DISCHARGED.** The one-per-group cursor is replaced by explicit `correction_refs[]`, and the shipped baseline references `(cg)/(ch)/(ci)` align with the current body-repair labels. However, no gate couples those refs to the body ledger; a self-consistently resealed `(zz)` register/body mismatch still passes build. |
| **F-S05-59-03 — secondary membership falsely CLOSED** | **DISCHARGED AS SCOPE-OUT IN THE CURRENT AMENDMENT.** v0.60 expressly records the prior mechanism as scoped out rather than implemented. The separate top-level `convergence_group` coupling defect remains under F-S05-60-01 below. |
| **F-S05-59-04 — gate-count documentation inconsistency** | **NOT DISCHARGED.** AUDIT_CONTEXT says 258; executed output has 257 PASS lines; CI_METHODOLOGY still contains the historical 222-gate statement. |

---

## 3. Continuity mutation battery — CI v0.3

Baseline generated-register SHA-256: `627962aef7743ddbb1c43b1cc85017d0654e0019838e7429980b7a6c546f2bfd`.

| Mutation | Result |
|---|---|
| invalid `findings[].source_severity` -> `CRITICAL` | FAIL-CLOSED (`ValueError`) |
| invalid group disposition | FAIL-CLOSED |
| malformed group finding ID | FAIL-CLOSED |
| duplicate group finding ID | FAIL-CLOSED |
| remove referenced top-level finding | FAIL-CLOSED |
| malformed top-level finding ID | FAIL-CLOSED |
| duplicate top-level finding ID | FAIL-CLOSED |
| **remove `adjudication_receipt` from mixed-severity group 4** | **INERT — byte-identical register** |
| **valid single source severity `HIGH -> LOW`** | **INERT — byte-identical register** |
| **valid source mutations flipping group-1 majority HIGH -> LOW** | **INERT — byte-identical register** |
| **change top-level `findings[].convergence_group`** | **INERT — byte-identical register** |
| **replace receipt content with `nonsense`** | **INERT — byte-identical register** |
| correction ref `(cg) -> (zz)` | register changes, generator accepts |
| remove group-3 correction ref | register changes, generator accepts |

### Why M2 still fails

`generate_register()` computes the source distribution and majority, but it still renders `group["triage_severity"]` unconditionally. If the group already has any non-empty receipt, an arbitrarily changed source majority is accepted without validating the receipt’s content. Group 1’s receipt says all eight source findings are HIGH; after mutating five of the eight to LOW, the generator still emits the exact same HIGH register bytes because the stale receipt merely exists.

Thus `source_severity` is not a load-bearing rendered provenance value; it is a conditional validation input whose changes can remain invisible.

### Why M3 still fails

The methodology’s v0.2.1 receipt rule says a receipt documents when triage severity differs from **any** source severity. Current group 4 contains one LOW and three HIGH source findings and its receipt explicitly documents the LOW-to-HIGH elevation. Removing that receipt produces byte-identical output because CI v0.3 only checks whether triage severity differs from the **majority** severity. Since HIGH remains the majority, no receipt is required by code.

This is the exact R18 continuity receipt-removal mutation, and it remains inert.

---

## 4. Findings — six-element format

### F-S05-60-01

**Severity:** HIGH (Class A)
**Locus:** `xz_protocol_register_gen.py` lines 49–54, 66–123, 147–180; `r18_findings_index.json` groups 1/4/8; protocol v0.60 register item (1); protocol Status; CI_METHODOLOGY receipt rule.

**Substance:** CI v0.3 still does not make source severity, receipt semantics, or source-layer convergence membership authoritative in the way its v0.60 closure claim asserts. The exact R18 M2/M3 continuity mutations remain semantically inert.

**Evidence (EXECUTED):**
- one valid `HIGH -> LOW` source mutation leaves register bytes unchanged;
- mutating five of eight group-1 source findings to LOW, flipping the source majority from HIGH to LOW, still leaves register bytes unchanged because a pre-existing receipt is merely truthy;
- replacing that receipt’s text with `nonsense` is inert;
- removing group-4’s receipt is inert even though its own receipt documents an individual LOW source finding elevated to group HIGH;
- mutating a finding’s scalar `convergence_group` is inert;
- by contrast, missing referenced findings and malformed/duplicate top-level IDs now fail, proving the mutation harness reaches the new CI v0.3 validation path.

The implementation at lines 110–122 computes a majority only to decide whether **presence** of a receipt is required. It does not validate receipt content against the actual source distribution, does not render the distribution, and does not cross-check `findings[].convergence_group` against group membership.

**Recommendation:** Make the source distribution a machine-checkable part of the receipt or generated output. A receipt should contain structured expected distribution / affected finding IDs / adjudicated severity and be validated against the current source records. If a valid source-severity mutation changes that distribution, generation must change or fail. Cross-check each source record’s declared membership against the convergence-group relation or remove the scalar field from the authoritative schema.

**Citation traceability:** Direct recurrence of R18 S05 F-S05-59-01 and its continuity falsifiers. It also falsifies producer predictions P9 and P10 and the current generated claim that M2/M3 now change output or fail.

---

### F-S05-60-02

**Severity:** HIGH (Class A)
**Locus:** protocol Status line and v0.60 register item (3); `build.py` Section [10] around lines 679–683.

**Substance:** v0.60 claims Sections 22.2/22.3 are “gated to VERSION-1,” but the shipped build has no such semantic gate.

**Evidence (EXECUTED):** The actual v0.60 body literals are currently correct (`v0.1 through v0.59` and `v0.38-v0.59`). However, I mutated only those two Section 22 body bounds back to stale `v0.58`, updated the packet manifest digest for the mutated protocol, and re-ran `build.py`. The result was still:

`BUILD PASSED: all checks GREEN`

`build.py`’s only explicit Section 22 check is that the text contains “gate execution is a build-time convenience”; there is no VERSION-1 predicate for 22.2 or 22.3.

**Recommendation:** Add an explicit gate that derives `VERSION - 1` and asserts both the 22.2 carried-entry terminus and 22.3 carry-lineage terminus equal that value. Keep the current correct literals, but do not label them gated until that predicate exists and mutation-tests stale-by-one values.

**Citation traceability:** The literal repair from R18 is landed, but the stronger v0.60 closure claim (“both now gated to VERSION-1”) is false. This is a new Class A on the repair mechanism, not a claim that the current literals themselves are stale.

---

### F-S05-60-03

**Severity:** HIGH (Class A)
**Locus:** `r18_findings_index.json`; `R18_REPORTS.txt`; CI_METHODOLOGY CI-8 lines 362–365.

**Substance:** CI-8 index-source fidelity fails because 19 finding IDs in the authoritative R18 findings index do not exist in the supplied source seat reports under those IDs.

**Evidence (EXECUTED):** Exact-source search finds **19/35** indexed IDs absent from `R18_REPORTS.txt`:

`F-S02-59-01F` through `F-S02-59-05F`;
`F-S02-59-01C` through `F-S02-59-05C`;
`F-S03-59-01F`, `F-S03-59-01C`;
`F-S05-59-01F` through `F-S05-59-04F`;
`F-S05-59-01C` through `F-S05-59-03C`.

The corresponding seat reports use unsuffixed source IDs such as `F-S02-59-01`, `F-S03-59-01`, and `F-S05-59-01`. The `F`/`C` suffixes appear to have been introduced during index construction to distinguish fresh and continuous reports, but no alias/canonicalization map or receipt is shipped.

CI-8 explicitly requires that “every finding_id in the index exists in its seat’s report.” On literal bytes, that criterion fails.

**Recommendation:** Preserve source IDs exactly and add a separate `source_report` / `mode` / `seat_instance` key, or ship a machine-readable alias map that records each canonical index ID and the exact source report ID from which it was derived. Update CI-8 to verify the alias relation rather than silently renaming source identifiers.

**Citation traceability:** This falsifies producer prediction P2 (CI-8 PASS) and exposes an index-layer identity mutation introduced by the ten-seat fresh/continuous packaging scheme.

---

### F-S05-60-04

**Severity:** HIGH (Class A)
**Locus:** protocol v0.60 register item (2), item (3), Body repairs paragraph; `xz_protocol_register_gen.py` correction-ref rendering; `build.py` [10c]–[10e].

**Substance:** Explicit `correction_refs[]` fixes the old cursor shift, but the claimed coupling to the body-repair ledger does not exist. A register correction reference can be changed to a wrong label while the body ledger remains unchanged and the self-consistently resealed build still passes.

**Evidence (EXECUTED):** I changed group 3’s explicit ref from `cg` to `zz`, regenerated the register from the mutated index, left the Body repairs ledger at `(cg)`, recomputed the current-entry/FULL_SECTION_27 seals and packet hashes, and ran the shipped build. Result:

`BUILD PASSED: all checks GREEN`

The mutated register said `CLOSED via append-only correction (zz)` while its own adjudication and body ledger still referred to `(cg)`. `build.py` [10c]–[10e] checks IDs, severity text, and count brackets only; it does not validate `correction_refs` or their targets.

The current baseline refs happen to be correct, so the original one-per-group cursor bug is repaired on the shipped bytes. The new Class A is the stronger computed claim that the body-repair ledger is generated/coupled from the same refs.

**Recommendation:** Generate the Body repairs ledger from the same structured repair objects or add a bijective gate: each `correction_ref` must resolve to exactly one current body repair with the expected target/locus, and every body repair ref must be claimed by exactly one structured repair action.

**Citation traceability:** Successor surface to R18 S05 F-S05-59-02. The old cursor defect is repaired; the semantic ref-to-target coupling is not.

---

### F-S05-60-05

**Severity:** MEDIUM (Class B)
**Locus:** `AUDIT_CONTEXT.txt` Build status; executed `build.py` output; `CI_METHODOLOGY.txt` Step 8.

**Substance:** Gate-count documentation remains inconsistent.

**Evidence (EXECUTED):** AUDIT_CONTEXT says `build.py: 258 gates, all PASS`. The executed build emits **257** lines containing `PASS:`. CI_METHODOLOGY still contains `216 + 6 new = 222 gates` in its v0.57 implementation section. The current triage itself said the R19 count should be derived from build output, but the new dispatch count is again one higher than the emitted PASS-line count.

**Recommendation:** Stop hand-maintaining current gate totals. Generate an execution-receipt count directly from the actual checks run, and label historical methodology counts explicitly with the version to which they applied.

**Citation traceability:** Direct continuation of R18 S05 F-S05-59-04 / R18 convergence group 6.

---

## 5. Repairs and controls confirmed on v0.60

The HALT should not obscure real progress. The following surfaces are materially improved and verified:

- packet reconstruction and all 19 SHA-256 members verify;
- build passes on canonical bytes;
- all 186 tests pass;
- CI-1R passes byte-exactly;
- top-level finding IDs now enforce syntax and uniqueness;
- referenced group IDs must resolve to source records;
- invalid dispositions/severity tokens fail closed;
- the old one-per-group correction cursor is removed;
- current correction refs `(cg)/(ch)/(ci)` match the current amendment’s body labels on baseline bytes;
- Sections 22.2/22.3 currently contain the correct v0.59 VERSION-1 bounds;
- the prior secondary-membership CLOSED-via-implementation claim is explicitly corrected as a scope-out in the new amendment;
- the R16 receipt distribution is now stated as 3 MEDIUM + 1 LOW, matching the R18 report evidence;
- ASSERTED tag fraction remains under the 15% target at 5.6%.

These are genuine repairs, but they do not remove the Class A blockers above.

---

## 6. CI / producer prediction scorecard

| Prediction | Result |
|---|---|
| P1 CI-1R PASS | **CONFIRMED** |
| P2 CI-8 PASS | **FALSIFIED** — 19 synthetic suffixed IDs lack literal source-report identity |
| P3 ASSERTED <15% | **CONFIRMED** — 5.6% |
| P4 Class A, if any, on body/narrative/new CI surface | **CONFIRMED** — CI v0.3 provenance/receipt surface + false 22.x gate claim |
| P5 count-list | **CONFIRMED** |
| P6 append-only / seal layer | **CONFIRMED on baseline execution** |
| P7 code layer | **CONFIRMED baseline tests green** |
| P8 packet execution | **CONFIRMED** |
| P9 severity derivation catches valid source mutation | **FALSIFIED** — valid mutations remain byte-inert, including a majority flip |
| P10 receipt enforcement catches receipt removal | **FALSIFIED** — mixed-severity group receipt removal is inert |
| P11 correction refs match body repairs | **CONFIRMED on baseline bytes; enforcement claim falsified** |
| P12 22.2/22.3 bounds at v0.59 | **CONFIRMED literals; “gated” claim falsified** |

---

## 7. Recurrence determination

**Does v0.60 break the R7–R18 Class A streak? No.**

At least three independent Class A surfaces are reproduced on R19 bytes/architecture:

1. M2/M3 provenance/receipt semantics remain inert despite a `[COMPUTED]` closure claim;
2. the claimed Section 22 VERSION-1 gate is absent and a stale-bound mutation can pass a self-consistently updated build;
3. CI-8 source identity fails for 19 authoritative index IDs.

A fourth Class A exists in the correction-ref/body-ledger coupling claim.

Therefore the recurrence becomes **R7–R19 = 13/13**. Under the same Laplace-smoothed stationarity convention used by the dispatch, the next-round predictive value would be **14/15 ≈ 0.933**, while recognizing that the purpose of CI repair is precisely to break stationarity rather than accept it.

## Final seat determination

**HALT — advisory, non-binding.**

The minimum v0.61 repair set is:

1. structurally bind receipts to exact source distributions/IDs and make valid source-severity mutations observable or fail;
2. cross-check source-record `convergence_group` against group membership or remove that field from the authoritative schema;
3. preserve source finding IDs exactly or add an explicit alias map for fresh/continuous canonicalization and make CI-8 verify it;
4. implement actual VERSION-1 gates for Sections 22.2 and 22.3;
5. generate or bijectively validate body correction targets from `correction_refs[]`;
6. derive the current gate count from execution rather than handwritten documentation.

---

# Bismillah ir-Rahman ir-Rahim
