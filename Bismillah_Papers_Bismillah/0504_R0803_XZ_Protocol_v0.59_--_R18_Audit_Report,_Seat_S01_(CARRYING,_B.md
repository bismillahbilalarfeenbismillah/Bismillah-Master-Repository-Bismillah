# Bismillah ir-Rahman ir-Rahim

# R0803 -- XZ Protocol v0.59 -- R18 Audit Report, Seat S01 (CARRYING, BINDING, FRESH)

**Chronological Index:** 504 of 995  
**Date:** 2026-08-11  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R18_REPORTS.txt  
**Source Format:** txt  
**SHA-256:** `8e147b2074b6d18619162f98247e99d1d580e2383de753eebed8a506b93cd68b`  

---

## R0803 · XZ Protocol v0.59 -- R18 Audit Report, Seat S01 (CARRYING, BINDING, FRESH)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R18_REPORTS.txt
- source_format: txt
- text_sha256: 8e147b2074b6d18619162f98247e99d1d580e2383de753eebed8a506b93cd68b

# XZ Protocol v0.59 -- R18 Audit Report, Seat S01 (CARRYING, BINDING, FRESH)

**VERDICT: HALT (binding).** Class A (byte-false) findings are present on the
shipped v0.59 bytes: 4 HIGH (Class A), 2 MEDIUM (Class B), 2 LOW, 1 INFO.
The R7-R17 Class A recurrence streak extends to R7-R18 (12/12, H = 1.0).
v0.59 does NOT break the streak.

- Seat: S01, CARRYING with BINDING authority, FRESH mode (dispatch-mandated)
- Authoring model: Kimi K3 (Moonshot AI) -- not a default/blend/router
- Producer: Claude Opus 4.6 (Anthropic) -- barred from audit seats
- Round: 18; version under audit: v0.59; dispatch dated 2026-08-11
- Audit executed: 2026-08-11 UTC (sandbox clock, `date -u`: Tue Aug 11 17:50:50 UTC 2026)
- Framework lenses: GAN Convergence (primary), CI v0.2.2 probes CI-1R / CI-4 / CI-5 / CI-8 (secondary)
- Findings format: six-element (ID, severity, locus, substance, evidence, recommendation)
- Severity scale (dispatch): Class A = HIGH (byte-false); Class B = MEDIUM

## Section 0: Identity, mode, execution surface

| Item | Value |
|---|---|
| Authoring model | Kimi K3 (Moonshot AI), as the dispatch names the seat; not a default/blend/router |
| Execution surface | Linux k2087228216059011075 5.10.134-18.0.11.lifsea8.x86_64; Python 3.12.12 |
| Packet working dir | /mnt/agents/output/R18_v059_S01/packet |
| Mode | FRESH -- no held prior-round packets, no held HISTORY.sha256, no carried conclusions; METHOD ONLY |
| Checkpoint IDs / weights revisions | not exposed by the platform; none asserted |
| Packet closure | audit evidence = the 10 shipped .txt files only; no externally fetched document was used |

FRESH-mode consequence (declared in the S-0 freeze, before the v0.59 entry was
opened): the PRIOR_HISTORY anchor is verified for internal self-consistency
against the v0.58 chain embedded in the shipped packet only. No independently
held prior HISTORY file exists at this seat; the in-place-mutation detection
class (F-K3R3-01) is therefore out of scope this round and is disclosed, not
closed.

## Section 1: Reconstruction and standing values (all EXECUTED)

Extraction per the dispatch's two-step recipe: 16 packed files split from
EXECUTABLE_PACKET.txt on `######_XZPACKET_FILE_SPLIT_######`, plus 4 dispatch
files copied to canonical names (`xz_protocol_v0_59.md`,
`r17_findings_index.json`, `xz_protocol_boundaries.json`,
`xz_protocol_register_gen.py`). 20 files staged.

Standing values, recomputed independently of build.py (xz_recompute.py,
exit 0, RESULT: ALL OK):

```
PACKET_SHA256SUMS : 19 entries, 19 OK, 0 FAILED, sha256sum -c rc=0 (initial and final)
ENTRY seals       : 59/59 recomputed match (HISTORY.sha256 vs Section 27 bytes)
FULL_SECTION_27   : 4c613e0d0a661d08... (recomputed; OK)
Unsealed tail     : 885 chars after the Provenance terminator (disclosed by construction)
Manifest digest   : 06e6ee9c548b1d8027ddd3235196e5d7819024b30deb39c5d8b4c1b19a55c585
                    (12 ALL_CODE_FILES; matches trust roots)
PRIOR_HISTORY     : 4a79f22603c0931e383021f2ca3cda3d7fea96b0a31086f9808e558d13e2bfde
                    (self-consistent with the v0.59 entry line; NOT anchored to a held
                     prior file -- FRESH mode, declared)
```

No seal-equality with any producer-retained value is claimed (P23-05); the
producer performs that comparison.

## Section 2: Required baseline execution (EXECUTED, not ASSERTED)

| # | Command | Expected (dispatch) | Executed result | Log |
|---|---|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | 19/19 OK, rc=0 | logs/02_sums.log, logs/15_final_sums.log |
| 2 | `python3 build.py` | BUILD PASSED, 262 gates | **BUILD PASSED: all checks GREEN, rc=0; 261 `PASS:` gate lines counted in output** | logs/05_build_rerun.log |
| 3 | `pytest <six explicit files>` | 186 passed | **186 passed in 12.79s, rc=0** | logs/04_pytest.log |
| 4 | CI-1R `generate_register` in doc | CI-1R PASS | **CI-1R PASS** -- generated register (4494 chars) byte-contained in `xz_protocol_v0_59.md` | logs/06_ci1r.log |
| 5 | HISTORY seal chain | verify ENTRY / FULL / PRIOR_HISTORY | ALL OK, independently recomputed (not from build.py output) | logs/09_recompute.log |

Environmental note (D-5): the first `python3 build.py` run returned rc=1 with
exactly 2 FAILs -- `[8] pytest is installed (No module named pytest)` and its
downstream count parse. That is the gate failing CLOSED correctly on a fresh
environment, not a packet verdict. After `pip install pytest`, the re-run
returned rc=0, 261 PASS, 0 FAIL.

Gate-count observation: the dispatch and AUDIT_CONTEXT both document "262
gates". The executed build output contains 261 `PASS:` gate lines (262nd
"PASS" string occurrence is the "BUILD PASSED" summary itself). build.py
prints no internal gate total. See F-S01-59-05.

Gate non-vacuity (mutation-verified on byte copies; canonical packet
untouched): sabotage of one register finding ID in the document copy makes
gate [10c] FAIL and build rc=1; sabotage of index group-1 triage_severity
makes gate [10d] FAIL and build rc=1. The CI v0.2.2 register gates bite.

## Section 3: S-1 preregistered predictions, scored

S-0/S-1 were frozen to `S0_S1_FREEZE.md` (timestamped 2026-08-11 17:50:50 UTC)
BEFORE PROTOCOL_v0_59.txt, R17_REPORTS.txt, and EXECUTABLE_PACKET.txt were
opened. Scores:

| # | Prediction (frozen) | Score |
|---|---|---|
| SP1 | 22.2/22.3 bounds advanced to v0.57 but stale by one in a v0.59 document -> Class A recurrence | **CONFIRMED** (F-S01-59-01) |
| SP2 | Group-6 receipt correction propagates the triage's own miscount (2M+1L claimed vs 3M+1L in findings[]) -> Class A | **CONFIRMED** (F-S01-59-02) |
| SP3 | "findings[] load-bearing / severity derivation / receipt enforcement" claimed but not implemented -> Class A spec-impl gap | **CONFIRMED** (F-S01-59-03) |
| SP4 | build 262-documented gates PASS; pytest 186; sums OK; CI-1R PASS | **CONFIRMED** (gates PASS; documented count off by one, F-S01-59-05) |
| SP5 | Terminal line present and tagged [COMPUTED: generate_terminal_line] | **CONFIRMED** |
| SP6 | CI_METHODOLOGY retains stale "222 gates"; dispatch-layer count matches executed | **PARTIAL** -- 222 retained (CONFIRMED); but dispatch count 262 does NOT match executed 261 (REFUTED component, F-S01-59-05) |
| SP7 | Boundary list byte-identical to generator output, 35 items | **CONFIRMED** |
| SP8 | Narrative per-defect convergence counts match the triage (3/5, 4/5, 2->3/5, 2/5, 1/5) | **CONFIRMED** |

7 CONFIRMED, 1 PARTIAL (with one REFUTED component), 0 clean REFUTED. The seat
records the SP6 sub-refutation honestly: the dispatch's own gate count was
predicted accurate and was not.

## Section 4: Clearance verification -- the 11 R17 convergent defect groups on v0.59 bytes

| R17 group | Claimed disposition | Executed verification on v0.59 bytes | Result |
|---|---|---|---|
| 1. 22.2/22.3 version tokens | CLOSED via (cc)/(cd) | Lines 718/716 now read "v0.1 through v0.57" / "v0.38-v0.57" -- correct for v0.58, stale by one in a v0.59 document (carried entries run to v0.58) | **NOT DISCHARGED -- Class A recurrence (F-S01-59-01)** |
| 2. findings[] inert | CLOSED via CI v0.2.2 | P-1: findings[] source_severity mutation leaves output byte-identical; P-2: unreceipted group-severity contradiction silently accepted. findings[] is validated but inert for output | **NOT DISCHARGED -- mechanism persists (F-S01-59-03)** |
| 3. Secondary membership | CLOSED via CI v0.2.2 | `grep -c secondary` = 0 in register_gen and build.py; scalar `convergence_group` only. Scoping-out disclosed in AUDIT_CONTEXT only, not in the entry | **NOT DISCHARGED as "architecture repair"; disclosed at dispatch layer (F-S01-59-08)** |
| 4. Narrative count ambiguity | CLOSED via (ce) | Narrative now states per-defect counts individually (3/5; 4 and 3; 2/5; 1 seat) -- matches triage and index | DISCHARGED on bytes (but register cites the wrong correction letter, F-S01-59-04) |
| 5. Group-6 receipt false | CLOSED via (cf) | Corrected receipt "2 MEDIUM (S01, S05) + 1 LOW (S04)" contradicts shipped findings[] (3 MEDIUM + 1 LOW; S02 omitted) | **NOT DISCHARGED -- correction itself byte-false (F-S01-59-02)** |
| 6. Gate count 222/261/264 | NOTED | New figure 262 (dispatch/AUDIT_CONTEXT) vs 261 executed; CI_METHODOLOGY still 222 | **NOT RECONCILED (F-S01-59-05)** |
| 7. Terminal enzyme tag | CLOSED via CI v0.2.2 | Terminal line `*End of XZ Protocol v0.59 draft candidate.* [COMPUTED: generate_terminal_line]`, present exactly once | DISCHARGED |
| 8. Disposition silent-drop | CLOSED via CI v0.2.2 | P-4: unknown disposition `FIXED` raises ValueError (fail-closed) | DISCHARGED |
| 9. Hardcoded literals | CLOSED via CI v0.2.2 | P-8: seats 5->6 changes header to "six-seat"; P-9: prior_correction_end 53->50 moves first correction label cc->bz | DISCHARGED |
| 10. Malformed/duplicate IDs | CLOSED via CI v0.2.2 | P-5a/P-5b: `BOGUS-ID` and duplicate ID both raise ValueError | DISCHARGED |
| 11. CI_METHODOLOGY schema inconsistency | NOTED | NOTED stands; not re-audited as a closure claim | CARRIED NOTED |

6 of 11 groups discharged on bytes; 3 not discharged (1, 2, 5); 1 mislabeled
closure (3); 1 unreconciled documentation item (6, was NOTED).

## Section 5: Findings (six-element format)

Severity totals: **4 HIGH (Class A), 2 MEDIUM (Class B), 2 LOW, 1 INFO.**

---

### F-S01-59-01 | HIGH (Class A) | xz_protocol_v0_59.md line 718 (Section 22.2) and line 716 (Section 22.3)

- **Substance:** Sixth consecutive round of the version-token staleness class
  on the identical two loci. Section 22.2 reads "For carried entries (v0.1
  through v0.57)" and Section 22.3 reads "carried at v0.38-v0.57" in a v0.59
  document whose carried entries run v0.1 through v0.58 (Section 0.1 itself:
  "fifty-nine amendment entries, v0.1 through v0.59"). The v0.58 entry is a
  carried entry covered by the [9b] PRIOR_HISTORY derivation; the v0.58 carry
  of the item-7 exception is a fact of the record. Both parentheticals are
  byte-false by one version.
- **Evidence:** `grep -n` on the shipped document: line 718 contains "v0.1
  through v0.57"; line 716 contains "carried at v0.38-v0.57". The entry's own
  corrections state: "(i) correction (cc): Section 22.2 carried-entry bound
  advanced from 'v0.1 through v0.55' to 'v0.1 through v0.57'" and "(ii)
  correction (cd): Section 22.3 carry lineage advanced from 'v0.38-v0.56' to
  'v0.38-v0.57'" -- i.e., the producer applied the R17 round's literal repair
  target (v0.57, correct for a v0.58 document) to a v0.59 document, instead
  of the VERSION-1 semantics the defect class demands. No gate or generator
  binds these tokens (the R17 minimum repair set's "Gate or code-generate
  both bounds" was not implemented).
- **Recommendation:** advance 22.2 to "v0.1 through v0.58" and 22.3 to
  "v0.38-v0.58"; bind both tokens by gate to VERSION-1 (entry count minus
  one), the same discipline gate [10h] applies to the terminal line. Repair
  instructions must state the semantic rule, not a literal target version.
- **Falsifier:** grep of lines 716/718 on the repaired bytes shows bounds
  terminating at v0.58, and a gate derives both tokens from the entry count.

---

### F-S01-59-02 | HIGH (Class A) | v0.59 entry register item (5) and body correction (iv)/(cf); r17_findings_index.json group 6

- **Substance:** The R17 Defect 5 repair is itself byte-false. Register item
  (5) -- tagged `[COMPUTED: generate_register]` -- asserts "actual
  distribution from findings[] is 2 MEDIUM + 1 LOW". Correction (cf) asserts
  the distribution was corrected to "2 MEDIUM (S01, S05) + 1 LOW (S04)". The
  shipped findings[] records for group 6 enumerate **3 MEDIUM (F-S01-58-03,
  F-S02-58-04, F-S05-58-05) + 1 LOW (F-S04-58-06)**. S02's MEDIUM is omitted
  from both claims. The "correction" propagates the R17 triage's own
  miscount (the triage asserted "actual distribution is 2 MEDIUM + 1 LOW"
  against its own 4-member enumeration of 3M+1L). F-CI-3R fires: a Class A
  finding inside a [COMPUTED: generate_register] claim.
- **Evidence:** executed recount (probe P-0, logs/10_probes.log):
  `{'MEDIUM': 3, 'LOW': 1}` from `r17_findings_index.json` findings[]
  (F-S01-58-03 MEDIUM, F-S02-58-04 MEDIUM, F-S04-58-06 LOW, F-S05-58-05
  MEDIUM); the four severities individually match the R17 seat reports
  (CI-8, Section 7). The register line and correction (cf) quote 2M+1L.
- **Recommendation:** compute receipt distributions from findings[] records
  at generation time (the mechanism the entry claims exists); correct the
  receipt to 3 MEDIUM + 1 LOW; add a gate that compares any in-register
  severity-distribution claim against the index.
- **Falsifier:** a regenerated register whose item (5) distribution equals
  the coded recount of findings[] (3M+1L), verified by re-running P-0.

---

### F-S01-59-03 | HIGH (Class A) | front-matter Status (line 5); v0.59 entry item (v); xz_protocol_register_gen.py docstring vs code

- **Substance:** The Status line claims the CI v0.2.2 generator performs
  "findings[] consumption, severity derivation from source records,
  adjudication receipt enforcement". The generator docstring repeats
  "findings[] is now load-bearing" and "Adjudication receipt enforcement:
  group severity must match source distribution or carry a receipt".
  Neither is implemented. findings[] is read only to validate severity
  tokens; no register output is derived from findings[] records; group
  severity is copied from `triage_severity` regardless of the source
  distribution; receipts are neither required nor validated. This is the
  R17 Defect 2 spec-impl gap recurring one layer down: the array is now
  parsed, but remains inert for output.
- **Evidence:** probe P-1: mutating F-S02-58-01's findings[]
  source_severity HIGH->LOW leaves generate_register output byte-identical
  (no raise, no diff). Probe P-2: setting group 2 triage_severity to LOW
  -- contradicting its 3 HIGH + 1 MEDIUM source records, with the receipt
  unchanged -- is silently accepted and emitted. Positive control P-3
  (mutating group triage_severity changes output) proves the probes reach
  the live generation path. Gates [10c]/[10d] likewise read
  convergence_groups, never findings[] per-finding severities.
- **Recommendation:** derive each group's severity and receipt content from
  the referenced findings[] records; require a machine-checkable receipt
  for every group severity that deviates from the source distribution;
  reject unused or false receipts; or narrow the Status/docstring claims to
  what the code does (token validation only).
- **Falsifier:** re-run P-1/P-2 on the repaired generator: P-1 must change
  output or raise; P-2 must raise absent a valid receipt.

---

### F-S01-59-04 | HIGH (Class A) | v0.59 entry register items (4) and (5) vs the entry's own body corrections (cc)-(cf)

- **Substance:** The register's correction-letter cross-references are false
  against the entry's own correction list. The body executes FOUR
  corrections: (cc) 22.2 bound, (cd) 22.3 lineage [both Defect 1],
  (ce) narrative rephrase [Defect 4], (cf) group-6 receipt [Defect 5]. The
  code-generated register assigns letters sequentially per correction-type
  group and emits: item (1) "CLOSED via append-only correction (cc)",
  item (4) "CLOSED via append-only correction (cd)", item (5) "CLOSED via
  append-only correction (ce)". Item (4) points at the 22.3 lineage
  correction (part of Defect 1's repair); the narrative repair is (ce).
  Item (5) points at the narrative correction; the receipt repair is (cf).
  Two byte-false cross-references inside [COMPUTED: generate_register]-
  tagged lines, self-contradicted within the same entry.
- **Evidence:** probe P-12 extraction (logs/10_probes.log): body
  corrections (cc)=22.2, (cd)=22.3, (ce)=narrative, (cf)=receipt; register
  mapping item(1)->(cc), item(4)->(cd), item(5)->(ce). Root cause:
  `correction_idx` increments once per group while Defect 1 consumed two
  letters; the generator cannot represent a multi-correction group, and no
  gate checks letter alignment between register and body.
- **Recommendation:** let the index declare the correction label(s) per
  group (or generate the body corrections from the same cursor), and gate
  that every register-cited correction letter exists in the body with
  matching substance.
- **Falsifier:** on repaired bytes, every register "CLOSED via ... (XX)"
  citation resolves to a body correction of matching substance.

---

### F-S01-59-05 | MEDIUM (Class B) | DISPATCH.txt / AUDIT_CONTEXT.txt ("262 gates") vs executed build output (261); CI_METHODOLOGY.txt ("222")

- **Substance:** The gate-count documentation class continues for a fourth
  round with a fourth distinct figure. The dispatch and AUDIT_CONTEXT claim
  "262 gates" and the v0.59 Status line claims "Gate count documentation
  reconciled". The executed build emits 261 `PASS:` gate lines (0 FAIL)
  and prints no internal total; CI_METHODOLOGY.txt still carries "Run the
  full gate suite (216 + 6 new = 222 gates)". The documented count is off
  by one against the executed count; the "reconciled" claim does not hold
  on the shipped bytes.
- **Evidence:** `grep -c 'PASS:' logs/05_build_rerun.log` = 261; the 262nd
  "PASS" string occurrence is the "BUILD PASSED" summary line.
  DISPATCH.txt line 13: "build.py gates (262)". AUDIT_CONTEXT: "build.py:
  262 gates, all PASS". CI_METHODOLOGY step 8: "216 + 6 new = 222 gates".
- **Recommendation:** have build.py print its own gate total and generate
  every advertised count from that output; correct or annotate the
  methodology figure.
- **Falsifier:** documented count == executed count == build.py's
  self-printed total on the same bytes.

---

### F-S01-59-06 | MEDIUM (Class B) | [COMPUTED: generate_register] tag scope; register adjudication/receipt prose

- **Substance:** The [COMPUTED: generate_register] tag overclaims its
  scope. Each register line is wholesale-tagged COMPUTED, but the
  adjudication and receipt prose inside the line is copied verbatim from
  hand-authored index fields (`triage_adjudication`) and is neither
  computed nor validated. This is the mechanism that shipped F-S01-59-02:
  a hand-authored miscount enters the entry wearing a COMPUTED tag. The
  entry discloses no such scoping.
- **Evidence:** probe P-10: replacing group 5's `triage_adjudication` with
  the literal "SABOTAGE-TOKEN" lands the token verbatim in the
  [COMPUTED: generate_register]-tagged output. Controls P-3/P-8/P-9 show
  the genuinely computed fields (severity label, seat word, correction
  cursor) do mutate with the index -- the tag is accurate for those fields
  only.
- **Recommendation:** split the tag: `[COMPUTED: generate_register]` for
  code-derived fields and `[ASSERTED: triage author]` for copied
  adjudication prose; or compute the adjudication content from findings[]
  records (F-S01-59-03 repair).
- **Falsifier:** a tag-scope disclosure (or split tags) in the entry, and
  P-10-class mutations landing only under ASSERTED tags.

---

### F-S01-59-07 | LOW | xz_protocol_register_gen.py noted-item rendering

- **Substance:** R17 F-S01-58-05's second component persists: a noted item
  missing a required field crashes the generator instead of failing with a
  validation error.
- **Evidence:** probe P-11: removing `substance` from a
  unique_findings_noted item raises `KeyError: 'substance'` (not a
  ValueError with field/item context).
- **Recommendation:** validate noted-item required fields
  (finding_id/source_severity/substance/disposition) in the validation
  phase and fail with a named-field error.
- **Falsifier:** P-11 on the repaired generator raises ValueError naming
  the missing field.

---

### F-S01-59-08 | LOW | v0.59 entry register item (3) -- secondary membership "CLOSED via CI v0.2.2 architecture repair"

- **Substance:** Register item (3) marks the secondary-membership defect
  CLOSED via architecture repair, but no shipped artifact implements or
  formally scopes out multi-membership: `grep -c secondary` = 0 in
  xz_protocol_register_gen.py and build.py; the schema still has scalar
  `convergence_group` only. The scoping decision ("canonical-group rule
  remains") is disclosed in AUDIT_CONTEXT (dispatch layer) but not in the
  entry, whose closure label overstates the repair. Not byte-false at
  dispatch level (the disclosure exists in the bundle); mislabeled at
  entry level.
- **Evidence:** grep counts above; AUDIT_CONTEXT Defect 3 text: "The v0.2.2
  generator validates findings[] but does not implement multi-membership
  representation. The canonical-group rule from R16 remains."
- **Recommendation:** re-label the disposition (e.g., "CLOSED -> SCOPED
  OUT, canonical-group rule retained, disclosed") or implement
  secondary_groups[]; the entry should carry the scoping disclosure, not
  only the dispatch.
- **Falsifier:** entry text on repaired bytes states the scoping
  explicitly, or a secondary_groups field exists in the shipped schema.

---

### F-S01-59-09 | INFO | entry terminal PRIOR_HISTORY line; correction (cf) reference

- **Substance:** (a) The entry-terminal PRIOR_HISTORY value line ships
  untagged (R17 F-S04-58-07 component persists; the value itself recomputes
  correctly). (b) Correction (cf) is tagged [DIFF-VERIFIED] against
  `r16_findings_index.json`, which does not ship in this packet; under
  packet closure the diff-verification is not reproducible from shipped
  bytes (producer-side claim).
- **Evidence:** logs/14_ci4.log (PRIOR_HISTORY line tagged: False); packet
  member list (no r16_findings_index.json).
- **Recommendation:** tag the PRIOR_HISTORY line [COMPUTED: build.py [9b]]
  or exempt it explicitly; ship the prior index or downgrade the tag to
  ASSERTED.
- **Falsifier:** tag present (or exemption disclosed); referenced file
  shipped or tag downgraded.

---

## Section 6: CI v0.2.2 probe results (secondary lens)

| Probe | Claim | Executed result | Verdict |
|---|---|---|---|
| CI-1R | byte-exact register reproduction | generated register (4494 chars) byte-contained in the shipped document | **PASS** |
| CI-4 | ASSERTED fraction < 15% | tag census over the v0.59 entry: COMPUTED=20, DIFF-VERIFIED=4, ENUMERATED=1, ASSERTED=1 -> **1/26 = 3.8%** | **PASS** (with F-S01-59-06 tag-scope caveat) |
| CI-5 | Class A present? | 4 HIGH Class A findings | **Class A PRESENT -- streak extends to 12/12, H = 1.0** |
| CI-8 | index vs R17 reports | 29/29 findings[] records verified (ID present + source_severity match against R17_REPORTS); 5/5 noted items present; group membership consistent with the R17 triage table | **PASS** |

Falsification-criteria status: F-CI-1R (zero Class A in register surface)
NOT ACHIEVED -- F-S01-59-02/-04 live inside [COMPUTED: generate_register]
lines. F-CI-2 (ASSERTED decrease) SATISFIED (12.3% -> 3.8%). F-CI-3R
(Class A inside a COMPUTED register claim) FIRED (F-S01-59-02, F-S01-59-04)
-- per the methodology this is a code/architecture defect, addressable by
the code-layer repair process. F-CI-7R (CI-1R failure) not triggered.

## Section 7: Producer prediction scorecard (R18, P1-P10)

| # | Prediction | Score | Basis |
|---|---|---|---|
| P1 | CI-1R PASS | CONFIRMED | executed byte-exact |
| P2 | CI-8 PASS | CONFIRMED | 29/29 + noted 5/5 |
| P3 | ASSERTED < 15% | CONFIRMED | 3.8% |
| P4 | Class A in narrative/body/22.2-22.3/0.1 prose/new CI v0.2.2 surfaces | CONFIRMED | 22.2/22.3 bounds drifted again (F-S01-59-01); Status prose (F-S01-59-03); findings[] consumption path (F-S01-59-03); register correction/receipt surfaces (F-S01-59-02/-04) |
| P5 | Count-list invariant holds | CONFIRMED | dual cardinality computed; gate [10e] PASS; mutation-verified |
| P6 | Append-only holds | UNTESTABLE at this seat | FRESH: no held prior bytes; internal [9b] derivation PASS is self-consistency only |
| P7 | Code layer clean (186 GREEN) | PARTIAL | 186/186 GREEN confirmed; generator semantics defective (F-S01-59-03/-04) -- suites do not cover the claimed derivation path |
| P8 | ASSERTED < 15% because packet ships | CONFIRMED | packet shipped; all five critical verifications EXECUTED, none ASSERTED |
| P9 | Disposition validation catches unknown tokens | CONFIRMED | probe P-4 ValueError |
| P10 | Finding-ID validation catches malformed IDs | CONFIRMED | probes P-5a/P-5b ValueError |

7 CONFIRMED, 1 PARTIAL, 1 UNTESTABLE, 1 CONFIRMED-with-caveat (P4).

## Section 8: Boundary report and provenance ledger

Provenance ledger over the v0.59 entry (executed census): COMPUTED=20,
DIFF-VERIFIED=4, ENUMERATED=1, ASSERTED=1 (26 tagged claims). ASSERTED
fraction 3.8% -- the headline number meets target. However, 2 of the 20
COMPUTED tags cover lines containing byte-false content (F-S01-59-02,
F-S01-59-04), and every register line's adjudication prose is copied, not
computed (F-S01-59-06); the census therefore overstates verified surface.
COMPUTED-tag mutation verification executed: severity labels (P-3), header
seat word (P-8), correction cursor (P-9) all mutate with the index;
adjudication prose copies verbatim (P-10).

Outermost uncomputed layer (D-3.8): (1) the narrative paragraph (declared
ASSERTED floor -- verified clean this round); (2) the hand-authored
`triage_adjudication` / receipt prose inside index groups, which transits
into [COMPUTED]-tagged register lines unverified -- this is where two of
this round's four Class A findings live; (3) the extraction step itself
(triage document -> findings index), which remains a manual operation
outside every gate; (4) the PRIOR_HISTORY external anchor, unverifiable at
a FRESH seat. Bringing layer (2) inside requires computing adjudication
content from findings[] records; layer (3) requires a machine-readable
triage or an extraction gate.

D-7 four one-line answers: What was executed -- every dispatch-listed
verification plus a 13-probe battery, all on shipped bytes. What was
asserted -- nothing at this seat (0 ASSERTED verifications). What is the
outermost uncomputed claim -- the triage adjudication prose inside
COMPUTED-tagged register lines. What would falsify this report's central
claim -- a regenerated register whose item (5) distribution and correction
letters match a coded recount of findings[] (3M+1L; letters ce/cf), plus
22.2/22.3 bounds terminating at v0.58 on the repaired bytes.

## Section 9: Verdict, repairs, re-audit conditions

**VERDICT: HALT (binding).** Class A (byte-false) findings F-S01-59-01
through F-S01-59-04 stand on the shipped v0.59 bytes. Severity totals:
4 HIGH (Class A), 2 MEDIUM (Class B), 2 LOW, 1 INFO (9 findings).
G-loss (GAN lens): register-surface G-loss is near zero for code-derived
fields (CI-1R PASS, tags mutation-verified) but non-zero for the copied
adjudication layer and the manually maintained body prose; D-accuracy:
the gates catch ID/severity/count mutations (sabotage-verified) but no
gate covers version-bound prose tokens, receipt distributions, or
correction-letter alignment.

The CI v0.2.2 architecture is a real improvement: CI-1R, CI-4 (3.8%),
CI-8, disposition/ID/severity fail-closed validation, computed header and
cursor all verify clean on execution. But the R7-R18 Class A streak is
unbroken (12/12, H = 1.0), and the defect class has again migrated one
layer down -- from unvalidated data (R17) to unvalidated claims ABOUT the
data (R18).

Minimum repair set for v0.60 (re-audit conditions):

1. Advance 22.2/22.3 bounds to v0.58 and bind both tokens by gate to
   VERSION-1 (F-S01-59-01). State the repair as a semantic rule.
2. Correct the group-6 receipt to 3 MEDIUM + 1 LOW, computed from
   findings[] records, and gate any in-register distribution claim against
   the index (F-S01-59-02).
3. Implement severity derivation from source records with receipt
   enforcement, or narrow the Status/docstring claims to token validation
   (F-S01-59-03). P-1/P-2 must change behavior on repaired bytes.
4. Align register correction letters with the body corrections (declare
   labels in the index or generate the body from the same cursor) and gate
   the alignment (F-S01-59-04).
5. Print the gate total from build.py and regenerate all advertised counts
   (F-S01-59-05); split or scope the [COMPUTED] tag (F-S01-59-06).

Next round must re-run: CI-1R, the P-0 recount, P-1/P-2 (findings[]
load-bearing), P-4/P-5/P-6 (fail-closed validations), P-10 (tag scope),
P-12 (letter alignment), and a grep of lines 716/718 -- against the v0.60
bytes, under the continuous-mode METHOD ONLY rule.

Self-corrections ledger: none. This is the first report from this FRESH
seat instance; no prior-seat claims are carried.

Final integrity re-check after all probing and report assembly:
`sha256sum -c PACKET_SHA256SUMS` -> 19/19 OK, rc=0 (logs/15_final_sums.log);
standing values unchanged. Canonical packet bytes were never modified; all
probes ran on copies under probes/.

---

*R18 audit executed by Seat S01 -- Kimi K3 (Moonshot AI), carrying binding, FRESH mode.*
*All quoted values are byte-verbatim from the captured logs named in each section.*
# R18 Seat S02 Fresh Audit Verdict — XZ Protocol v0.59

**Seat:** S02 — GPT-5.6 Sol (OpenAI)
**Role:** CARRYING (BINDING)
**Mode:** FRESH
**Framework:** Structural Revelation (REV-1 through REV-5) + CI v0.2.2
**Round:** 18
**Version under audit:** v0.59
**Date:** 2026-08-11

## VERDICT

# HALT (BINDING)

v0.59 does **not** break the R7–R17 Class-A streak. Class A remains present on v0.59 bytes, including a new Class-A defect inside the `[COMPUTED: generate_register]` surface itself. Under the dispatch rule **Class A = HIGH (byte-false)**, S02 blocks carry.

**FB-8 remains OPEN.**

The key result is structural: CI-1R reproduces the shipped register byte-for-byte, but the reproduced register is not semantically faithful to the repair state beneath it. Deterministic reproduction proves identity to the generator; it does not prove truth of the generator's output.

---

## 1. Execution record

| Verification | Status | Result |
|---|---|---|
| Executable packet extraction | EXECUTED | PASS — 16 packed files extracted; 4 dispatch files copied to canonical names |
| `python3 build.py` | EXECUTED | PASS — `BUILD PASSED: all checks GREEN` |
| Build PASS-record census | EXECUTED | **261 PASS records**, not the 262 claimed in `AUDIT_CONTEXT.txt` |
| Canonical pytest command | EXECUTED | PASS — **186 passed** |
| `sha256sum -c PACKET_SHA256SUMS` | EXECUTED | PASS — **19/19 OK** |
| CI-1R register reproduction | EXECUTED | PASS — generated register occurs exactly once, byte-identical |
| Boundary reproduction | EXECUTED | PASS — 35-item generated boundary block matches shipped protocol |
| Terminal generator identity | EXECUTED | PASS — tagged v0.59 terminal line matches generator |
| R17 report/index ID fidelity | EXECUTED | PASS — **31/31** distinct R17 finding IDs represented in index union |
| R17 source-severity fidelity | EXECUTED | PASS — **31/31** source severities match seat reports |
| CI-8 membership fidelity | EXECUTED | **FAIL** — secondary/overlap membership remains lossy |
| ENTRY seals | EXECUTED | PASS — **59/59** recomputed |
| FULL_SECTION_27 | EXECUTED | PASS |
| PRIOR_HISTORY | EXECUTED | PASS — derived `4a79f226...e2bfde` matches shipped value |
| External append-only comparison to independently held v0.58 bytes | NOT AVAILABLE | Internal seal chain is clean, but prior external canonical v0.58 protocol bytes were not shipped as a separate comparison artifact |

### CI-4 dead-space measurement

Two reasonable implementations of the methodology's under-15% target both pass:

- Tag census: 1 ASSERTED / 21 tagged claims = **4.76%**.
- Character measure excluding the amendment heading: 1,226 ASSERTED narrative characters / 9,183 entry characters = **13.35%**.

CI-4 therefore **PASSES**.

---

## 2. Structural Revelation verdicts

**REV-1 — code faithfully represents protocol claims: FAIL.** The v0.59 front matter and generator docstring claim severity derivation from source records and adjudication-receipt enforcement, but the generator merely validates severity vocabulary. Removing all `findings[]` records leaves register output byte-identical; deleting receipts also leaves output unchanged. See F-S02-59-01.

**REV-2 — index/register faithfully represent source findings: FAIL.** ID and source-severity transcription are exact, but secondary membership remains unrepresented. The current index has one scalar `convergence_group` per finding and the generator does not implement overlap/collapse receipts. See F-S02-59-02.

**REV-3 — narrative/register faithfully represent repair state: FAIL.** The computed register assigns correction letters that contradict the body-repair ledger in the same v0.59 entry. See F-S02-59-03.

**REV-4 — front matter faithfully represents body: FAIL.** The Status line claims `severity derivation from source records`, `adjudication receipt enforcement`, and reconciled gate-count documentation; the shipped implementation/body does not support those claims completely. See F-S02-59-01 and F-S02-59-05.

**REV-5 — seal chain faithfully represents document: PASS internally.** All 59 ENTRY seals, FULL_SECTION_27, and PRIOR_HISTORY recompute. This establishes internal seal consistency, subject to the protocol's already-disclosed self-consistent-resealing boundary.

---

## 3. Findings — six-element format

### F-S02-59-01 — HIGH / Class A

**1. Locus:** `xz_protocol_v0_59.md` front-matter Status line 5; `xz_protocol_register_gen.py` lines 7–10 and 121–131; CI_METHODOLOGY R3 lines 176–179; R17 register group 2 closure at protocol line 1334.

**2. Substance:** The claimed v0.59 repair that makes `findings[]` load-bearing for severity derivation and enforces adjudication receipts is not implemented. `findings[]` is only scanned for invalid severity vocabulary. Its records are not required, not cross-linked to group members, not used to derive group/register severity, and receipts are not required before a valid triage-severity override.

**3. Evidence:** Executed mutation probes on shipped code:

- remove the entire `findings[]` array -> **ACCEPT; generated register byte-identical**;
- delete a group-referenced finding record -> **ACCEPT; byte-identical**;
- mutate a referenced `source_severity` from valid `HIGH` to valid `LOW` -> **ACCEPT; byte-identical**;
- remove `adjudication_receipt` from groups with severity divergence -> **ACCEPT; byte-identical**;
- change a group `triage_severity` to another valid token with no receipt -> accepted and emitted.

The source code builds `findings_by_id` but never uses it in generation. The front matter nevertheless states “severity derivation from source records, adjudication receipt enforcement.”

**4. Consequence:** R17 Defect 2 is not actually closed. The generator can reproduce a register whose severity claims are disconnected from the source-finding evidence while CI-1R still passes. This is a byte-false closure/capability claim and therefore Class A / HIGH.

**5. Recommendation:** Require `findings[]`; validate exact bijection/cross-reference between group `finding_ids` and finding records; derive each group severity from source records; require a typed adjudication receipt for every deviation; make missing/extra records fatal; add mutation tests for valid-token changes and receipt deletion.

**6. Falsifier / clearance condition:** Deleting a referenced finding, changing a valid source severity, or removing a required receipt must fail generation; generated severity must be demonstrably derived from the source records.

---

### F-S02-59-02 — HIGH / Class A

**1. Locus:** `AUDIT_CONTEXT.txt` lines 17–20; `FINDINGS_INDEX.txt` top-level `findings[]`; `xz_protocol_register_gen.py`; v0.59 register group 3 at protocol line 1335; R17 triage surfaces 2–3.

**2. Substance:** Secondary membership remains unimplemented while the v0.59 register marks the defect **CLOSED via CI v0.2.2 architecture repair**. The shipped schema still has exactly one scalar `convergence_group` per finding, no `secondary_groups[]` / `convergence_groups[]`, and no machine-enforced collapse receipt. The generator does not use per-finding `convergence_group` to validate membership at all.

**3. Evidence:** `AUDIT_CONTEXT.txt` itself admits that v0.2.2 “does not implement multi-membership representation.” R17 `F-S01-58-02` is explicitly related to the findings-array mechanism in Surface 2 and is also carried into Surface 3; the current index assigns it only to group 3. No secondary-membership field or overlap receipt records the lost relation. The claimed canonical-collapse rule is not implemented in the generator and is not present as a validated current schema rule.

**4. Consequence:** CI-8 fails on membership fidelity even though all 31 IDs and all 31 source severities match. R17 Defect 3 is therefore not structurally closed. The register's CLOSED claim is byte-false under the R17 clearance condition.

**5. Recommendation:** Either (a) implement lossless membership using `primary_group` + `secondary_groups[]` or `convergence_groups[]`, or (b) formally scope out secondary membership in the normative CI methodology and require a machine-readable collapse receipt for every overlap. Gate exact triage-to-index membership/collapse semantics.

**6. Falsifier / clearance condition:** Every triage overlap must either survive in the index or carry a validated collapse receipt under a normative canonicalization rule; CI-8 must reproduce this relation mechanically.

---

### F-S02-59-03 — HIGH / Class A

**1. Locus:** `xz_protocol_register_gen.py` lines 139–165; v0.59 computed register items (1), (4), and (5) at protocol lines 1333, 1336, 1337; v0.59 body-repair ledger at line 1350.

**2. Substance:** The computed correction cursor is semantically wrong when one defect group requires more than one append-only correction. The generator consumes exactly one correction letter per `repair_type == "correction"` group, but R17 Defect 1 requires **two** corrections, `(cc)` and `(cd)`. This shifts every later generated correction reference.

**3. Evidence:** The same v0.59 entry contains these mutually incompatible claims:

- register item (1): group 1 “CLOSED via append-only correction **(cc)**” while its own adjudication says the repair requires **(cc)/(cd)**;
- register item (4): narrative repair “CLOSED via append-only correction **(cd)**”;
- register item (5): receipt repair “CLOSED via append-only correction **(ce)**”;
- body-repair ledger: Section 22.2 = **(cc)**, Section 22.3 = **(cd)**, narrative = **(ce)**, receipt = **(cf)**.

Thus `(cd)` is simultaneously the second Defect-1 correction and the generated Defect-4 correction, while the latter two groups are each shifted one letter early.

**4. Consequence:** A `[COMPUTED: generate_register]` claim is Class A. This directly fires CI falsifier **F-CI-3R**: the register generator itself has a bug. CI-1R passes only because it deterministically reproduces the wrong mapping.

**5. Recommendation:** Encode repair actions explicitly, e.g. `correction_labels` / `corrections[]` per group, and consume one cursor position per actual correction—not per group. Generate the body-repair ledger and register closure references from the same structured repair-action source. Gate uniqueness and one-to-one correspondence of correction labels.

**6. Falsifier / clearance condition:** A group requiring N corrections must advance the cursor by N; every correction label in the register must map uniquely to the same labeled repair in the body ledger, with no collisions or shifts.

---

### F-S02-59-04 — MEDIUM / Class B

**1. Locus:** `xz_protocol_register_gen.py` validation phase and NOTED emission; `AUDIT_CONTEXT.txt` lines 35–36; protocol front-matter Status line 5.

**2. Substance:** The new disposition and finding-ID validation is only partial. Group records are validated, but `unique_findings_noted[]` dispositions are not validated; top-level `findings[]` IDs are not format-validated; noted IDs are not format-validated.

**3. Evidence:** Executed mutations:

- noted disposition `NOTED -> CLOSEDD` -> **ACCEPT**, and `CLOSEDD` is emitted into the register;
- top-level finding ID -> `BOGUS` -> **ACCEPT**, output unchanged;
- noted finding ID -> `BOGUS` -> **ACCEPT**, malformed ID emitted;
- group malformed ID -> correctly rejected;
- group unknown disposition -> correctly rejected;
- within-group duplicate -> correctly rejected.

**4. Consequence:** P9/P10 are only partial. The validation repair closes the exact group-level path but leaves adjacent record classes outside the validator, allowing malformed machine-readable evidence to survive or be emitted.

**5. Recommendation:** Validate the complete schema, not selected arrays: every record's finding ID, seat, severity, disposition, required fields, and cross-reference relation. Prefer one validation pass over a normalized union of all finding records.

**6. Falsifier / clearance condition:** Any malformed ID or unknown disposition anywhere in the index must fail closed before generation.

---

### F-S02-59-05 — MEDIUM / Class B

**1. Locus:** `AUDIT_CONTEXT.txt` line 43; front-matter Status line 5; executed `build.py` output.

**2. Substance:** Gate-count documentation is still not reconciled. `AUDIT_CONTEXT.txt` states “build.py: **262 gates, all PASS**,” while the executed v0.59 build emits **261 PASS records**. The underlying run contains 259 calls to `check()` plus 2 manually printed structural PASS records.

**3. Evidence:** `python3 build.py` exits 0 and is GREEN, but a direct census of the runtime output gives 261 `PASS:` records. Source instrumentation confirms 259 calls to `check()` and two additional manual PASS paths. No 262nd passing gate is emitted.

**4. Consequence:** R17 Defect 6 remains live as documentation/count drift. This does not by itself invalidate the successful build, but the shipped count claim is not faithful to the executable result.

**5. Recommendation:** Stop hand-maintaining the gate total. Have `build.py` count and print its own executed checks/PASS records, and import that value into dispatch metadata if a count is retained.

**6. Falsifier / clearance condition:** The advertised gate total must equal a machine-emitted runtime count under the canonical build command.

---

## 4. CI probe outcomes

### CI-1R — PASS

The generated register is byte-identical to the shipped register. This proves deterministic reproduction only. F-S02-59-03 demonstrates that the reproduced register contains a computed Class-A defect.

### CI-4 — PASS

ASSERTED fraction is below 15% by both tag-count and character-count implementations described above.

### CI-5 — FAIL target / Class A persists

Class A is present at R18. Therefore the “first round with zero Class A” target is not met.

- R7–R18 recurrence fraction: **12/12 = 1.0**.
- Under the same Laplace convention, the next-round smoothed probability would be **13/14 ≈ 0.929**.

### CI-8 — FAIL

- Finding-ID existence: PASS, 31/31.
- Source-severity fidelity: PASS, 31/31.
- Convergence/membership fidelity: FAIL due to unrepresented secondary/overlap membership and absent validated collapse receipts.

### F-CI-3R — FIRED

A Class-A defect exists in a `[COMPUTED: generate_register]` claim (F-S02-59-03), exactly matching the methodology's definition of a register-generator bug.

---

## 5. Producer prediction scorecard

| Prediction | Result | Basis |
|---|---|---|
| P1 CI-1R PASS | CONFIRMED | Byte-exact reproduction |
| P2 CI-8 PASS | FALSIFIED | Membership subcheck fails |
| P3 ASSERTED <15% | CONFIRMED | 4.76% tag / 13.35% chars |
| P4 Class A, if any, in named uncovered/new CI surfaces | CONFIRMED | New CI v0.2.2 consumption/cursor surfaces fail |
| P5 Count-list invariant holds | CONFIRMED | Dual cardinality on current register holds |
| P6 Append-only holds | UNTESTABLE externally / internally consistent | Seal chain passes; independently held prior v0.58 bytes not separately shipped |
| P7 Code layer clean | FALSIFIED | Register generator has semantic defects; 186 tests do not cover them |
| P8 ASSERTED <15% because packet ships | CONFIRMED | Full executable packet was usable |
| P9 Disposition validation catches unknown tokens | PARTIAL | Group tokens rejected; noted-item token accepted/emitted |
| P10 Finding-ID validation catches malformed IDs | PARTIAL | Group IDs rejected; top-level/noted malformed IDs accepted |

---

## 6. Minimum repair set for v0.60

1. **Fix severity provenance architecture:** make `findings[]` mandatory and semantically load-bearing; cross-link every group member; derive severity from source records; enforce adjudication receipts on every override.
2. **Resolve secondary membership honestly:** implement lossless multi-membership or normative canonical collapse with machine-readable receipts and a gate.
3. **Replace correction-group cursor with repair-action cursor:** one cursor increment per actual correction; generate register and body repair ledger from the same source.
4. **Extend validation to all record classes:** top-level findings, convergence groups, and unique/noted records; validate IDs, dispositions, required fields, and cross-links uniformly.
5. **Generate the gate count from runtime:** eliminate the 262/261 documentation drift.
6. Add adversarial tests for every mutation used in this audit: empty findings array, missing referenced finding, valid source-severity change, receipt deletion, malformed noted ID, unknown noted disposition, and multi-correction group cursor advancement.

---

## 7. Final binding statement

**VERDICT: HALT (CARRYING, BINDING).**

v0.59 does **not** break the Class-A streak. The strongest blocker is F-S02-59-03: the supposedly computed register contains false correction references because the correction cursor models groups rather than actual corrections. F-S02-59-01 and F-S02-59-02 independently show that the two central R17 architecture closures—severity provenance and secondary membership—are not structurally complete.

**R7–R18: 12/12 rounds with Class A present.**
**FB-8: REMAINS OPEN.**
R18 S02 — GPT-5.6 Sol — CARRYING (BINDING) — CONTINUITY AUDIT VERDICT
XZ Protocol v0.59 DRAFT CANDIDATE
Framework: Structural Revelation + CI v0.2.2
Date: 2026-08-11

VERDICT: HALT (BINDING)
FB-8: REMAINS OPEN
Carry consequence: S02 blocks carry on v0.59.

SEVERITY SUMMARY
- HIGH / Class A: 2
- MEDIUM / Class B: 3
- CI-5 recurrence: R7-R18 = 12/12 rounds with Class A present.

EXECUTION RECORD
- Outer dispatch: 10 files, readable.
- EXECUTABLE_PACKET.txt unpacked: 16 packed files + 4 canonical dispatch files = 20-file executable layout.
- build.py: EXECUTED, rc=0, BUILD PASSED.
- Dynamic build output: 261 PASS checks, 0 FAIL checks.
- pytest canonical command: EXECUTED, 186/186 passed.
- PACKET_SHA256SUMS: EXECUTED, 19/19 OK.
- HISTORY.sha256: ENTRY_v0.1-v0.59, FULL_SECTION_27, seal cardinality/uniqueness, and recursive PRIOR_HISTORY all PASS.
- CI-1R: PASS, byte-exact. Register SHA-256:
  3de61d0e462e809aee66be6f3f987ebaa4d3ca703d673d5ef82721e534dbdbc8
- Boundary reproduction: PASS.
- Terminal generator identity/tag: PASS.
- Section 22.2 bound: PASS ("v0.1 through v0.57").
- Section 22.3 bound: PASS ("v0.38-v0.57").

CONTINUITY SABOTAGE PROBES
1. Delete findings[] entirely -> ACCEPTED; register byte-identical.
2. Change F-S01-58-01 source_severity HIGH->LOW while its receipt still says all four source findings HIGH -> ACCEPTED; register byte-identical.
3. Remove group 2 adjudication_receipt despite mixed source severities HIGH/HIGH/MEDIUM/HIGH -> ACCEPTED; register byte-identical.
4. CLOSED->CLOSEDD -> REJECTED by ValueError.
5. Malformed finding ID -> REJECTED by ValueError.
6. Duplicate finding ID within group -> REJECTED by ValueError.
7. Invalid source severity CRITICAL -> REJECTED by ValueError.

F-S02-59-01 — HIGH / Class A
Locus: PROTOCOL front-matter Status; REGISTER_GENERATOR; CI_METHODOLOGY §§2.2/3.2 R3.
Substance: F-S02-58-01 is NOT discharged. v0.59's sealed front matter claims "severity derivation from source records" and "adjudication receipt enforcement." The generator does neither.
Evidence:
- findings[] source_severity tokens are validated, but findings_by_id is never used.
- Output severity is always group["triage_severity"].
- findings[] can be deleted entirely without error or output change.
- Valid source-severity mutation leaves output byte-identical.
- Deleting a load-bearing adjudication receipt leaves output byte-identical.
- The declared class-to-severity mapping is not enforced; build [10d] only checks group triage severity near a finding ID.
Consequence: sealed claim false on shipped bytes; Class A.
Recommendation: make findings[] mandatory; cross-reference every group ID to source records; derive source-severity distribution mechanically; require and validate a structured adjudication object; encode class as an enum and gate class-to-severity coupling.

F-S02-59-02 — HIGH / Class A
Locus: generated register items (1), (4), (5); correction cursor; v0.59 body repair ledger.
Substance: The computed correction cursor is deterministic but semantically wrong when one convergence group consumes more than one correction. R17 Defect 1 consumes both (cc) and (cd), but the generator increments once per correction-bearing group.
Evidence:
- Group 1 adjudication requires corrections (cc)/(cd), but item (1) says CLOSED via (cc) only.
- Item (4) says narrative ambiguity CLOSED via (cd), but body repair (cd) is Section 22.3; narrative repair is (ce).
- Item (5) says receipt defect CLOSED via (ce), but body repair says that repair is (cf).
Correct body mapping: Defect 1 -> (cc)+(cd); Defect 4 -> (ce); Defect 5 -> (cf).
Generated mapping: Defect 1 -> (cc); Defect 4 -> (cd); Defect 5 -> (ce).
Consequence: false repair references are tagged [COMPUTED: generate_register]. CI-1R passes because it reproduces the generator's wrong semantics. F-CI-3R fires.
Recommendation: store repair_labels[] explicitly per group and gate register-to-body repair-label fidelity.

F-S02-59-03 — MEDIUM / Class B
Locus: front-matter Status; AUDIT_CONTEXT; CI_METHODOLOGY; executed build.
Substance: Gate-count documentation is still unreconciled despite the front matter saying it is reconciled.
Evidence: AUDIT_CONTEXT says 262 gates; CI_METHODOLOGY says 222; executed build emits 261 PASS checks.
Recommendation: emit one authoritative machine-readable gate count from build.py and consume it everywhere.

F-S02-59-04 — MEDIUM / Class B
Locus: CI-4 dead-space metric.
Substance: The "<15%" CI-4 claim is metric-dependent and cannot be credited unqualified.
Evidence: amendment through PRIOR_HISTORY = 9,182 chars; sole [ASSERTED] paragraph = 1,601 chars, 17.44%. Tag-count interpretation gives 1/27 = 3.70% (or 1/22 = 4.55% using only ASSERTED/COMPUTED/EXTERNAL). CI_METHODOLOGY does not formalize the unit/boundaries.
Recommendation: define numerator, denominator, and unit mathematically.

F-S02-59-05 — MEDIUM / Class B
Locus: R17_TRIAGE aggregate severity totals versus R17_REPORTS/FINDINGS_INDEX.
Substance: R17_TRIAGE's aggregate is off by one class although individual index source severities match reports.
Evidence: R17_TRIAGE says 13 HIGH, 12 MEDIUM, 4 LOW, 2 INFO. The 31 distinct source findings are 13 HIGH, 11 MEDIUM, 5 LOW, 2 INFORMATIONAL.
Recommendation: generate triage totals from structured finding records.

HELD R17 FINDING DISPOSITION
- F-S02-58-01 severity provenance: NOT DISCHARGED -> F-S02-59-01.
- F-S02-58-02 secondary membership: exact prior false claim is discharged by explicit scope-out. v0.59 openly says multi-membership is not implemented. Lossless secondary membership remains absent, but R17 expressly allowed "implement or explicitly scope out"; no new Class A counted solely on this basis.
- F-S02-58-03 schema inconsistency: remains NOTED.
- F-S02-58-04 gate-count inconsistency: NOT DISCHARGED -> F-S02-59-03.
- F-S02-58-05 terminal tag: DISCHARGED.
- F-S02-58-06 disposition silent-drop: DISCHARGED.

MANDATORY PROBES
REV-1 code faithfully represents protocol claims: FAIL — F-S02-59-01, F-S02-59-02.
REV-2 register/index faithfully represent findings: PARTIAL — CI-1R PASS; 31/31 IDs and individual source severities match reports; explicit primary groups match triage; correction-label semantics fail; multi-membership scoped out.
REV-3 narrative faithfully represents register: PASS on repaired convergence wording; CI-4 remains metric-ambiguous.
REV-4 front matter faithfully represents body/code: FAIL — false severity-derivation, receipt-enforcement, and gate-count-reconciliation claims.
REV-5 seal chain faithfully represents document: PASS for byte integrity. The seal chain faithfully seals the false claims above; cryptographic consistency does not establish semantic truth.

CI SUMMARY
- CI-1R: PASS.
- CI-2: PASS on register count-list coupling.
- CI-3: FAIL at F-CI-3R because a [COMPUTED: generate_register] repair-reference claim is false.
- CI-4: FAIL under surface-character reading (17.44%); PASS under tag-count reading; metric underspecified.
- CI-5: Class A PRESENT; R7-R18 = 12/12.
- CI-8: PASS on distinct IDs, individual source severities, and explicit primary group mapping; secondary membership is explicitly scoped out. R17 triage aggregate severity arithmetic is nevertheless wrong.

PRODUCER PREDICTIONS
P1 CI-1R PASS: CONFIRMED.
P2 CI-8 PASS: SUBSTANTIALLY CONFIRMED on explicit ID/severity/primary-group checks.
P3 ASSERTED <15%: FALSIFIED under surface-character reading; confirmed only under tag-count reading.
P4 Class A only in narrative/body/new CI v0.2.2 surface: CONFIRMED.
P5 count-list invariant: CONFIRMED.
P6 append-only: PARTIAL; internal seal chain passes.
P7 code layer clean: FALSIFIED for register-generator semantics despite build/pytest GREEN.
P8 executable packet ships/executes: CONFIRMED; fraction portion remains metric-dependent.
P9 disposition validation: CONFIRMED.
P10 finding-ID validation: CONFIRMED.

FINAL
HALT (BINDING).

v0.59 materially improves the executable substrate: the full packet is present; 186 tests pass; checksums and seals verify; malformed dispositions/IDs now fail closed; stale Section 22 bounds and the terminal tag are repaired.

The carrying blocker remains structural. CI v0.2.2 still does not derive severity from source records or enforce adjudication receipts despite sealed claims that it does. Separately, its computed correction cursor emits false repair references because it counts correction-bearing groups instead of correction labels actually consumed.

CI v0.2.2 therefore does not break the Class-A streak. FB-8 MUST REMAIN OPEN.
# XZ Protocol v0.59 -- R18 Audit Result

**FINAL VERDICT: HALT**[cite: 1, 8]

---

## 1. Trace Summary

Initial logic and parameters are validated[cite: 1, 4]. Standard processing applied to the 20-file executable packet and normative dependencies[cite: 4, 5].

---

## 2. Final Findings (Class A)

*   **Version-Token Staleness:** The manual prose bounds in Sections 22.2 and 22.3 drifted and incorrectly reflect `v0.57` rather than the required `v0.58`[cite: 1, 7].
*   **Severity Provenance Failure:** The `generate_register` function validates string tokens but structurally fails to derive `triage_severity` from the `findings[]` array[cite: 4, 10].
*   **Secondary Membership Schema Gap:** The `r17_findings_index.json` relies on a singular scalar `convergence_group` integer, failing to implement the required array for secondary memberships[cite: 6, 7].

---

## 3. Repair Prescriptions

*   Advance the manual bounds in Sections 22.2 and 22.3 directly to `v0.58`[cite: 1, 7].
*   Update `xz_protocol_register_gen.py` to strictly calculate severity from source receipts and raise a `ValueError` upon unauthorized divergence[cite: 10].
*   Modify the `FINDINGS_INDEX` schema to structurally support a `secondary_groups` array[cite: 6].# R18 DISPATCH -- Seat S03 (Gemini 3.1 Pro) -- AUDIT VERDICT
# Framework: Fractal Cube + Code Audit
# Round: 18
# Artifact: XZ Protocol v0.59 DRAFT CANDIDATE

**VERDICT: HALT (ADVISORY)**

While the v0.59 draft successfully corrects the narrative conflation and false convergence counts via append-only corrections, the CI v0.2.2 architecture upgrade introduces a new byte-false claim. The generator's source code explicitly claims to enforce adjudication receipts but entirely lacks the logic to do so [cite: 18, 21]. The specification-implementation gap persists. The R7-R17 Class A recurrence streak is **not broken**.

As an AI system operating without a sandboxed code execution environment, I mark terminal build verifications as `ASSERTED` while executing logical static analysis on the provided code [cite: 15].

---

## S-0: State Declaration
*   **Seat:** S03, ADVISORY (non-binding) [cite: 15].
*   **Family:** Gemini 3.1 Pro (Google) [cite: 15].
*   **Mode:** CONTINUOUS (from R17) [cite: 15].
*   **Limitations:** No live code execution sandbox. External validations (`pytest`, `sha256sum`, and `build.py`) cannot be run dynamically and are marked `ASSERTED` [cite: 15]. The code modules were traced via static logic analysis [cite: 18, 21].

## S-1: Preregistered Predictions
*   **Prediction 1 (Correction Landing):** The narrative fixes for F-S03-58-01 and F-S03-58-02 will land successfully in v0.59 bytes. **Score: CONFIRMED.**
*   **Prediction 2 (Persistent Spec-Impl Gap):** The generator script will fail to faithfully implement the complex relational logic required for adjudication receipts. **Score: CONFIRMED.**
*   **Prediction 3 (Hurst Exponent Continuity):** The R18 update will fail to break stationarity, pushing the persistent autocorrelation sequence to 12/12. **Score: CONFIRMED.**

---

## 1. Re-verification of R17 Findings

| Finding ID | Status | Resolution / Notes |
| :--- | :--- | :--- |
| **F-S03-58-01** (Narrative Locus Conflation) | **CLOSED** | The v0.59 narrative correctly distinguishes the loci, separating Section 22.2/22.3 bounds from the findings inertness [cite: 18]. |
| **F-S03-58-02** (False Convergence Count) | **CLOSED** | The v0.59 narrative correctly individualizes the convergence counts, accurately reflecting 3/5 for Defect 1, 4/5 for Defect 2, etc. [cite: 18]. |
| **F-S03-58-03** (Spec-Impl Gap) | **OPEN** | Falsely claimed as CLOSED via CI v0.2.2 architecture repair. Static analysis reveals the `adjudication_receipt` enforcement is completely missing from `REGISTER_GENERATOR.txt` [cite: 21]. |
| **F-S03-58-04** (Terminal Tag) | **CLOSED** | The `generate_terminal_line` function now appends `[COMPUTED: generate_terminal_line]` [cite: 21]. |

---

## 2. Fractal Cube Lens Analysis

*   **Vertex 1 (Code):** The `xz_protocol_register_gen.py` script upgraded its validation logic, adding ID format checks and disposition fail-closed mechanisms [cite: 21]. However, it completely ignores the relational mapping required to verify source severity against triage severity, breaking the provenance chain it claims to establish [cite: 21].
*   **Vertex 2 (Register):** The register block correctly reflects the updated formatting and parsed values [cite: 18].
*   **Vertex 3 (Narrative):** The `[ASSERTED]` narrative paragraph successfully resolved the memory-transit failures and hallucinations from R17 via explicit corrections [cite: 18].

---

## 3. New Findings

### F-S03-59-01 | HIGH (Class A) | Locus: `REGISTER_GENERATOR.txt` | Byte-False Claim of Adjudication Receipt Enforcement
*   **Substance:** The v0.59 protocol and the `REGISTER_GENERATOR.txt` module docstring explicitly claim that CI v0.2.2 implements "Adjudication receipt enforcement: group severity must match source distribution or carry a receipt explaining the deviation" [cite: 18, 21]. Static tracing of the `generate_register` function reveals this claim is byte-false.
*   **Evidence:** The generator loads the `findings[]` array and strictly validates the strings against `VALID_SEVERITIES` (lines 83-91) [cite: 21]. However, it completely lacks the logic to group finding IDs, compute the source distribution, compare it against `group["triage_severity"]`, or assert the existence of an `adjudication_receipt` [cite: 21]. It blindly assigns `sev = group["triage_severity"]` during the generation phase (line 104) [cite: 21], precisely reproducing the R17 vulnerability while claiming it is fixed.
*   **Recommendation:** Either write the relational logic to enforce the adjudication receipts mechanically, or retract the claim from the methodology and protocol body.

---

## 4. Recurrence Question & Conclusion

**Key Question:** Does v0.59 break the R7-R17 Class A streak (11/11)? [cite: 15]
**Answer:** No. The LLM-authored narrative hallucination was contained, but the architecture's own spec-impl gap metastasized. A new Class A defect lives in the false closure claim of the CI v0.2.2 architecture.

The Class A recurrence streak extends to 12 consecutive rounds (R7-R18). Following the Laplace-smoothed probability logic utilized in the artifact, P(Class A at R19) = 13/14 ≈ 0.929.
# R18 Seat S04 Audit Report -- XZ Protocol v0.59 DRAFT CANDIDATE

| Field | Value |
|---|---|
| Seat | S04, Round 18, ADVISORY (non-binding); findings carry equal triage weight |
| Authoring model | Kimi K3 (Moonshot AI), as named by the dispatch; not a default/blend/router. This platform exposes no checkpoint ID or weights revision; none is claimed |
| Producer (excluded) | Claude Opus 4.6 (Anthropic); barred from audit seats |
| Framework | Biomedical Fractal + Repair Verification (dispatch-assigned) |
| Version under audit | v0.59 (PROTOCOL_v0_59.txt, sha256 09d542f78e09a445e58001ae69adc590358ad61fd997c4a5241c96aeac83390a) |
| Packet | 20-file executable packet (EXECUTABLE_PACKET.txt, 16 packed files + 4 dispatch-canonical files), staged at /mnt/agents/output/R18_S04_v059/packet/ |
| Dispatch | R18 DISPATCH -- Seat S04 (FRESH), dated 2026-08-11 |
| Audit date | 2026-08-11 (UTC); S-0/S-1 frozen 2026-08-11T17:50:39Z, after PACKET_SHA256SUMS verification, before opening the v0.59 amendment entry |
| Execution surface | Linux x86_64 (kernel 5.10.134-18.0.11.lifsea8), Python 3.12.12, sh shell; EXECUTING seat (full packet present) |
| Mode | FRESH. No prior-round bytes, reports, or conclusions held or carried. No held prior HISTORY.sha256; PRIOR_HISTORY verified for internal consistency only, not cross-anchored |

## VERDICT: HALT (advisory, non-binding)

Two Class A (HIGH, byte-false) findings on v0.59 bytes, both on surfaces introduced by this round's own CI v0.2.2 repair -- the metastasis boundary the dispatch asked about:

- **F-S04-59-01 (HIGH):** Correction-letter namespace collision on the computed register surface. The register assigns (cd) to the narrative repair and (ce) to the receipt repair; the same entry's body-repair list assigns (cd) to Section 22.3, (ce) to the narrative, and (cf) to the receipt. Same entry, same letters, different referents, inside [COMPUTED: generate_register] claims. F-CI-3R fires: a Class A inside a COMPUTED claim means the register generator itself has a bug.
- **F-S04-59-02 (HIGH):** Front-matter Status claims the CI v0.2.2 generator implements "severity derivation from source records, adjudication receipt enforcement." Neither exists in the code: `adjudication_receipt` appears only in the module docstring, group severity is emitted unconditionally from `triage_severity`, a valid unreceipted override is accepted and emitted (probe M3), and a valid source_severity mutation leaves output byte-identical (probe M2).

**Key question (dispatch): Does v0.59 break the R7-R17 Class A streak (11/11)? No.** The streak extends to R7-R18 (12/12, H = 1.0). Laplace P(Class A at R19) = 13/14 = 0.929 under stationarity.

Every R17 repair target verified LANDED on bytes: (cc) Section 22.2 at "v0.1 through v0.57", (cd) Section 22.3 at "v0.38-v0.57", (ce) narrative per-defect counts correct against the index, group 6 receipt computes 3 MEDIUM + 1 LOW, terminal line tagged and final, findings[] token validation live (M1 fires), disposition fail-closed on groups (M4 fires), group ID format/uniqueness enforced (M5a/M5b fire), header seat word and correction cursor computed (M8a/M8b). CI-1R byte-exact, 186/186 tests GREEN, 19/19 sums OK, 59/59 entry seals recomputed. The defects are not in what was repaired; they are in the repair.

Severity totals: Class A (HIGH) = 2; Class B (MEDIUM) = 2; Class C (LOW) = 2; Class D = 0; Class E (INFO) = 1.

---

## 1. S-0 state declaration (frozen verbatim, 2026-08-11T17:50:39Z)

- Seat S04, Round 18, ADVISORY (non-binding), per DISPATCH.txt. Findings carry equal triage weight.
- Family: Kimi K3 (Moonshot AI), as named by the dispatch; not a default/blend/router. This platform exposes no checkpoint ID or weights revision; none is claimed.
- Producer (excluded): Claude Opus 4.6 (Anthropic), barred from audit seats.
- Framework: Biomedical Fractal + Repair Verification (dispatch-assigned).
- Mode: FRESH. No prior-round bytes or conclusions held or carried.
- Shipment received: 10 dispatch .txt files, including EXECUTABLE_PACKET.txt (16 packed files) + 4 dispatch-canonical files = 20-file packet.
- Packet integrity at freeze: PACKET_SHA256SUMS 19/19 OK, rc=0 (log 00).
- Execution surface: Linux x86_64, Python 3.12.12, sh shell. EXECUTING seat.
- Held prior state: NONE. PRIOR_HISTORY checkable for internal consistency only; append-only across versions UNTESTABLE at byte level by this seat.
- Context age: this session began with this dispatch. Metadata visibility: upload dir + sandbox clock only.

Freeze file preserved at /mnt/agents/output/R18_S04_v059/S0_S1_FREEZE.md.

## 2. S-1 preregistered predictions, scored post-hoc

| # | Prediction (frozen) | Score | Basis |
|---|---|---|---|
| S1-P1 | CI-1R byte-exact | HELD | log 03/04: byte-exact, 4494 chars, 1 occurrence |
| S1-P2 | (cc)/(cd) landed; no stale current bounds in body | HELD | lines 716/718 at v0.57 bounds; stale v0.55/v0.56 tokens only inside sealed carried entries |
| S1-P3 | findings[] load-bearing (invalid raises; valid change moves output or is receipt-checked) | REFUTED in part | M1 RAISES (validation live); M2 valid mutation leaves output byte-identical; M3 unreceipted override accepted -- validation landed, derivation/receipt did not (F-S04-59-02) |
| S1-P4 | New validation surfaces (disposition, ID, seat word, cursor) each pass a targeted probe | PARTIAL | M4/M5a/M5b/M8a/M8b PASS on the group path; M6/M7a/M7b show noted/findings[] paths unvalidated; the cursor computation produced F-S04-59-01 |
| S1-P5 | Narrative per-defect claims corrected; group 6 receipt corrected | HELD | narrative counts verified against index (section 6); all 11 group receipts compute from findings[] (log 09) |
| S1-P6 | Streak BREAKS at R18 (zero Class A) | REFUTED | 2 Class A findings (F-S04-59-01, F-S04-59-02) |
| S1-P7 | Any Class A sits on CI v0.2.2 new-code surfaces or remaining hand prose, not the repaired register-reproduction surface | HELD | both Class A findings are on CI v0.2.2 surfaces: cursor lettering and findings[] consumption semantics |
| S1-P8 | ASSERTED fraction under 15%; terminal tagged | PARTIAL | occurrence basis 3.8% (< 15%); character basis 17.5% (> 15%); terminal tagged, unique, final |

4 HELD / 2 REFUTED / 2 PARTIAL / 0 NOT REACHED.

## 3. Execution record -- all dispatch verifications EXECUTED

| Verification (dispatch order) | Status | Result |
|---|---|---|
| Extraction (16 packed files) + 4 canonical copies | EXECUTED | 20 files staged; listing verified |
| `python3 build.py` | EXECUTED -- PASS | "BUILD PASSED: all checks GREEN", rc=0; 261 executed PASS lines counted (log 01); note AUDIT_CONTEXT claims 262 (F-S04-59-03) |
| pytest six-file canonical list | EXECUTED -- PASS | 186 passed in 8.15s standalone (log 02); 186 passed in 9.12s inside build gate [8] |
| `sha256sum -c PACKET_SHA256SUMS` | EXECUTED -- PASS | 19/19 OK, rc=0 at intake (log 00) and re-verified after all probing (log 11) |
| CI-1R register reproduction | EXECUTED -- PASS | byte-exact; register 4494 chars, sha256 3de61d0e462e809aee66be6f3f987ebaa4d3ca703d673d5ef82721e534dbdbc8, exactly 1 occurrence (logs 03/04) |
| HISTORY.sha256 seal chain | EXECUTED -- PASS (internal) | 59/59 ENTRY seals recomputed match; FULL_SECTION_27 matches; PRIOR_HISTORY derivation matches (build [9b] and independent recompute); cross-anchor to held prior HISTORY UNTESTABLE (fresh seat) |
| Boundary reproduction | EXECUTED -- PASS | byte-exact, 1797 chars, 35 items; mutation discriminates (B0/B1, log 08) |
| Terminal line | EXECUTED -- PASS | `*End of XZ Protocol v0.59 draft candidate.* [COMPUTED: generate_terminal_line]` -- unique, final line (T0, log 08) |
| CI-8 index-vs-reports fidelity | EXECUTED -- PASS with scope notes | 29/29 findings[] IDs in R17_REPORTS with matching severities; 5/5 noted IDs present; membership matches triage; all 11 receipts compute from findings[] (log 09) |
| CI-4 tag census | EXECUTED | ASSERTED 1/26 = 3.8% occurrence basis; narrative char share 17.5%; build.py's own census 1/20 = 5.0% (log 10, build log line 232) |
| Mutation battery vs CI v0.2.2 generator | EXECUTED | 16 probes M0-M13 + B0/B1 + T0 with vacuity and discrimination controls (log 08) |
| Append-only byte comparison vs held v0.58 | UNTESTABLE | no held prior bytes (fresh seat); not asserted |

Nothing in this report is marked ASSERTED from the producer; every dispatch-listed verification ran on shipped bytes in this sandbox.

### Independent recomputation (auditor-side code, never importing build.py)

| Surface | Value | Result |
|---|---|---|
| PACKET_SHA256SUMS | 19 OK, 0 FAILED, rc=0 | OK |
| ENTRY seals | 59/59 recomputed match (59 entries parsed) | OK |
| ENTRY_v0.59 | 86408984d5a0f069d09de5d088aa5428a707c08d27354c5967c6a743eb7a62e6 | recomputed == HISTORY line |
| FULL_SECTION_27 | 4c613e0d0a661d080a4be1d9543bafb5f14364874dc25b45b03167e1003f5d0a | recomputed == HISTORY line |
| Unsealed tail after Provenance terminator | 885 chars | reported, unsealed by design |
| manifest_digest (12 ALL_CODE_FILES parsed from build.py source) | 06e6ee9c548b1d8027ddd3235196e5d7819024b30deb39c5d8b4c1b19a55c585 | recomputed == trust-roots value |
| PRIOR_HISTORY | 4a79f22603c0931e383021f2ca3cda3d7fea96b0a31086f9808e558d13e2bfde | internal derivation consistent; NOT cross-anchored (no held v0.58 HISTORY) |

Standing values are recomputed and reported verbatim for producer comparison; no seal equality with any producer-retained value is claimed.

## 4. R17 clearance verification on v0.59 bytes (Repair Verification lens)

| R17 group | Claimed disposition | Verified on v0.59 bytes |
|---|---|---|
| 1. Section 22.2/22.3 version-token staleness (HIGH) | CLOSED via (cc)/(cd) | DISCHARGED. Line 718: "For carried entries (v0.1 through v0.57)"; line 716: "carried at v0.38-v0.57". Body-wide census: stale v0.55/v0.56 bound tokens survive only inside sealed carried entries (Section 27 history, legitimate) |
| 2. findings[] array inert (HIGH) | CLOSED via CI v0.2.2 | PARTIAL -- validation landed, semantics did not. M1: invalid findings[] token RAISES. M2: valid source_severity mutation leaves output byte-identical. M3: unreceipted valid override ACCEPTED and emitted. Front matter claims derivation + receipt enforcement (F-S04-59-02, Class A) |
| 3. Secondary membership not implemented (HIGH) | CLOSED via CI v0.2.2 | DISCHARGED as explicitly scoped out. The R17 byte-false claim ("secondary memberships tracked") is gone; R18 AUDIT_CONTEXT states "does not implement multi-membership representation. The canonical-group rule from R16 remains" -- the triage's own repair alternative ("implement or explicitly scope out") |
| 4. Narrative convergence-count ambiguity (HIGH) | CLOSED via (ce) | DISCHARGED. Narrative states per-defect counts: Defect 1 "3 seats: S01, S04, S05" (index: 3 seats / 4 findings), Defects 2-3 "4 and 3 seats respectively", Defect 4 "2 seats: S03, S04, disputed by S01", Defect 5 "1 seat" -- all verified against r17_findings_index.json |
| 5. Group 6 adjudication receipt false (HIGH) | CLOSED via (cf) | DISCHARGED on the current index: group 6 receipt computes 3 MEDIUM + 1 LOW from findings[] (log 09). Scope note: the (cf) DIFF-VERIFIED tag targets r16_findings_index.json, which is outside this packet's closure (F-S04-59-05) |
| 6. Gate count 222/261/264 documentation (MEDIUM) | NOTED | NOT DISCHARGED. Front matter claims "Gate count documentation reconciled" while the register carries the NOTED item; AUDIT_CONTEXT says 262, executed count is 261 PASS lines, CI_METHODOLOGY still says 222 (F-S04-59-03) |
| 7. Terminal line enzyme tag missing (MEDIUM) | CLOSED via CI v0.2.2 | DISCHARGED. Terminal line carries [COMPUTED: generate_terminal_line], unique, final (T0) |
| 8. Disposition silent-drop (MEDIUM) | CLOSED via CI v0.2.2 | DISCHARGED on the group path: M4 (disposition=OPEN) RAISES ValueError. Residual: noted-finding dispositions unvalidated (M7a) -- folded into F-S04-59-04 |
| 9. Hardcoded register literals (MEDIUM) | CLOSED via CI v0.2.2 | DISCHARGED as named: M8a 6-seat index emits "six-seat" header; M8b prior_correction_end=99 shifts cursor to (dw). But the computed cursor produced a new cross-surface collision (F-S04-59-01, Class A) |
| 10. Malformed/duplicate ID acceptance (MEDIUM) | CLOSED via CI v0.2.2 | DISCHARGED on the group path: M5a (BOGUS-X-THING) and M5b (duplicate) RAISE. Residual: findings[] and noted IDs unvalidated (M6/M7b/M10) -- F-S04-59-04 |
| 11. CI_METHODOLOGY schema inconsistency (MEDIUM) | NOTED | NOT DISCHARGED. Shipped CI_METHODOLOGY still terminates at the v0.2.1 appendix; no v0.2.2 normative schema exists; section 2.1 vs appendix divergence persists (F-S04-59-06) |
| R17 Defect 10 (no byte-identity register gate) | noted | CARRIED. build.py [10c]/[10d]/[10e] are substring/proximity gates; no gate asserts full register byte-identity against generator output (F-S04-59-07) |
| F-S04-58-05 Section 0.1 duplicate carry rationale | NOTED | CARRIED. Line 18 "no duplicate rationale maintained here" beside the line-22 carry paragraph and the FB-7b row, unchanged |
| F-S04-58-07 PRIOR_HISTORY untagged | NOTED | CARRIED. Entry tail "PRIOR_HISTORY 4a79f226..." still bare of its [COMPUTED: build.py] tag |
| F-S01-58-08 BOUNDARIES version field | NOTED | DISCHARGED. BOUNDARIES.txt now "version": "0.59"; packet cardinality consistent (20 files, 19 summed members + the sums file itself) |

Regression check on repaired surfaces: no regressions detected. Entry count 59 (gate [9] PASS, "fifty-nine amendment entries, v0.1 through v0.59"); Section 0.1 arithmetic re-verified (6+6 modules/suites + trust roots + protocol text = 14 normative files; 14+29+29+18+27+69 = 186 test functions; 3^5 = 243); FB-7b row at "PENDING RE-CARRY v0.59" (gate [2g] PASS); R17 trajectory row present in the FB-7b cell.

## 5. Probe battery (EXECUTED; mutations on byte copies; packet re-verified 19/19 OK after)

| Probe | Shape | Result |
|---|---|---|
| M0 vacuity control | clean generation | byte-exact vs entry register; in_protocol True |
| M1 | findings[0].source_severity = CRITICAL | RAISE ValueError -- findings[] token validation live |
| M2 | findings[0].source_severity HIGH to LOW (valid) | ACCEPT, output byte-identical -- findings[] content does not move output; no derivation (F-S04-59-02) |
| M3 | group 2 triage_severity HIGH to MEDIUM, adjudication_receipt removed | ACCEPT, emitted as MEDIUM with no receipt required -- no receipt enforcement (F-S04-59-02) |
| M4 | group 1 disposition = OPEN | RAISE ValueError -- fail-closed on group dispositions |
| M5a | group ID = BOGUS-X-THING | RAISE ValueError -- ID format validation on groups |
| M5b | duplicate ID within group | RAISE ValueError -- within-group uniqueness |
| M6 | findings[0].finding_id = BOGUS | ACCEPT, no output change -- findings[] IDs unvalidated (F-S04-59-04) |
| M7a | noted[0].disposition = BOGUS | ACCEPT, emitted -- noted dispositions unvalidated (F-S04-59-04) |
| M7b | noted[0].finding_id = BOGUS | ACCEPT, emitted -- noted IDs unvalidated (F-S04-59-04) |
| M8a | seats = 6 | header "from R17 six-seat audit" -- seat word computed |
| M8b | prior_correction_end = 99 | cursor shifts to (dw) -- cursor computed |
| M9 discrimination control | valid-format ID swap F-S01-58-01 to F-S01-58-09 | register differs, NOT in protocol -- probe discriminates |
| M10 | duplicate findings[] record ID | ACCEPT -- findings[] uniqueness unchecked (F-S04-59-04) |
| M11 | group ID with no findings[] record | ACCEPT -- no group-to-findings[] cross-check (F-S04-59-04) |
| M12 | orphan findings[] record | ACCEPT, no output change -- findings[]-to-group cross-check absent (F-S04-59-04) |
| M13 | generate_register version arg 0.59 vs 9.99 | outputs identical -- version arg uncoupled (carried observation) |
| B0/B1 | boundary clean / mutated | clean byte-exact in protocol; mutation differs and absent -- tag verified by discrimination |
| T0 | terminal line | tagged, unique, final line |

Modelled adversary: careless/stale-context producer (hand-maintained dispatch counts) and self-consistent repairer (validation shipped where semantics were claimed). Both materialized. No probe was void; vacuity and discrimination controls fired.

Additional static evidence (auditor-side reads of packet bytes):

- `adjudication_receipt` occurs in xz_protocol_register_gen.py ONLY in the docstring (line 9); no code path reads it. Group severity emission is unconditional: `sev = group["triage_severity"]` (line 150).
- build.py contains zero correction-letter gates (`grep -c correction build.py` = 0); nothing detects the F-S04-59-01 collision class.
- findings[] records F-S01-58-06, F-S01-58-07, F-S04-58-05 carry convergence_group 12/13/14; convergence_groups[] defines only groups 1-11 -- dangling references, accepted silently (consistent with M11/M12).

## 6. Findings (six-element format; severity per dispatch scale: A = HIGH byte-false, B = MEDIUM, C = LOW, D = LOW, E = INFO)

### F-S04-59-01 | HIGH (Class A) | v0.59 register items (1)/(4)/(5) (lines 1333, 1336, 1337) vs entry body-repair list (line 1350); xz_protocol_register_gen.py correction-cursor scheme (lines 79-80, 146-165)

- **Substance:** Correction-letter namespace collision on the computed register surface -- a Class A inside [COMPUTED: generate_register] claims (F-CI-3R fires). The entry's body-repair list enumerates four append-only corrections: (cc) = Section 22.2 bound, (cd) = Section 22.3 lineage, (ce) = narrative rephrase, (cf) = group 6 receipt. The computed register assigns letters per correction-type GROUP, three groups only: item (1) CLOSED via "(cc)", item (4) (narrative) CLOSED via "(cd)", item (5) (receipt) CLOSED via "(ce)". The same letters therefore denote different repairs on two surfaces of the SAME entry: register-(cd) = narrative vs body-(cd) = Section 22.3; register-(ce) = receipt vs body-(ce) = narrative; body-(cf) has no register referent at all. The collision is internal to the register block itself: item (1)'s own adjudication text says "Advance bounds to v0.57 via corrections (cc)/(cd)" -- using (cd) with the body's meaning -- while item (4) assigns (cd) to the narrative. The register's disposition for the narrative group cites a letter that the same entry's authoritative correction list assigns to the Section 22.3 repair; that cross-reference is byte-false. Root cause: the R17 Defect 9 repair (cursor computed from prior_correction_end) assigns one letter per group, but group 1 consumed two corrections in the body ((cc) 22.2 and (cd) 22.3), shifting the body sequence to (ce)/(cf) while the register sequence stays (cc)/(cd)/(ce). The repaired surface metastasized: a hardcoded cursor became a computed-but-wrong cursor. No build gate detects the class (zero correction-letter gates in build.py).
- **Evidence (EXECUTED):** register item (1) line 1333 verbatim: "HIGH CLOSED via append-only correction (cc): Section 22.2/22.3 version-token staleness. Adjudication: ... Advance bounds to v0.57 via corrections (cc)/(cd)."; register item (4) line 1336: "HIGH CLOSED via append-only correction (cd): Narrative convergence-count ambiguity."; register item (5) line 1337: "HIGH CLOSED via append-only correction (ce): Group 6 adjudication receipt factually false."; body-repair list line 1350: "(ii) correction (cd): Section 22.3 carry lineage advanced ... (iii) correction (ce): narrative convergence-count claims ... (iv) correction (cf): R16 group 6 adjudication receipt ...". Generator lines 79-80: `correction_start = index.get("prior_correction_end", 50) + 1`; lines 160-165: one `correction_idx` increment per correction-type group. M8b confirms the cursor computes (prior_correction_end=99 shifts to (dw)); the scheme itself is the defect. build.py `grep -c correction` = 0.
- **Recommendation:** make the letter namespace single-sourced and correction-granular: either the generator emits one letter per actual correction (group 1 emits a (cc)/(cd) pair or two sub-items) and the body-repair list is generated from the same cursor state, or the body list is amended to the register's lettering. Add a build gate asserting (i) every letter cited in the register resolves to exactly one repair in the entry's correction list and (ii) every correction in the list is cited by the register. **Falsifier:** on repaired bytes, a letter-census probe finds each of (cc)-(cf) denoting exactly one repair across both surfaces, and a gate fails the M8b-style collision shape.

### F-S04-59-02 | HIGH (Class A) | Protocol front-matter Status (line 5); xz_protocol_register_gen.py docstring (lines 9-10) and emission path (line 150); register item (2) (line 1334)

- **Substance:** The front-matter Status claims the CI v0.2.2 generator implements "findings[] consumption, severity derivation from source records, adjudication receipt enforcement, ...". The first is true (token validation, M1). The second and third are byte-false: no code derives group severity from findings[] source records, and no code enforces adjudication receipts. `adjudication_receipt` exists only in the module docstring, which repeats the overclaim ("Adjudication receipt enforcement: group severity must match source distribution or carry a receipt explaining the deviation"). Emission is unconditional from triage_severity. Probe M2: a valid source_severity mutation (HIGH to LOW on F-S01-58-01) is accepted and produces byte-identical output -- the "load-bearing" array is load-bearing only for token validity. Probe M3: a valid but unreceipted triage_severity override (HIGH to MEDIUM on group 2, receipt deleted) is accepted and emitted as MEDIUM -- the R17 F-S02-58-01 shape (unreceipted valid override) survives intact. Consequently register item (2)'s "CLOSED via CI v0.2.2 architecture repair" overstates the landed repair: the triage's repair item 2 required "validate per-finding source_severity; derive group severity from source records with mandatory adjudication receipt on divergence" -- the first clause landed, the second did not. This is the R17 Defect 2 class persisted one layer down: last round findings[] was wholly inert; this round it is validated-but-semantically-inert, while the Status line claims the full semantics.
- **Evidence (EXECUTED):** line 5 verbatim: "CI v0.2.2 register generator upgraded (findings[] consumption, severity derivation from source records, adjudication receipt enforcement, disposition validation, ID format validation, computed header seat word and correction cursor)."; docstring lines 9-10 verbatim; battery log 08: "M2 findings[0].source_severity HIGH->LOW (valid): ACCEPT (output_differs=False)"; M3 emitted line verbatim: "(5) [4-seat convergence: F-S02-58-01 / F-S03-58-03 / F-S04-58-04 / F-S05-58-01] MEDIUM CLOSED via CI v0.2.2 architecture repair: findings[] array inert (CI v0.2.1 spec-impl gap). [COMPUTED: generate_register]" (mutated input, no receipt, accepted); grep shows `adjudication_receipt` absent from all code logic; line 150 `sev = group["triage_severity"]`.
- **Recommendation:** either implement the claimed semantics -- derive each group's severity from its findings[] source records, require a machine-checkable adjudication_receipt for every divergence, and fail generation when a valid override lacks a receipt -- or correct the Status line and docstring to "findings[] token validation only" and re-scope register item (2)'s disposition. Add M2/M3-shaped mutation tests to the suite (they are currently absent: 186 tests GREEN while both shapes pass silently). **Falsifier:** M3 raises a generation error naming the unreceipted group, M2 either changes output or raises, or the Status/docstring text no longer claims derivation/enforcement.

### F-S04-59-03 | MEDIUM (Class B) | Protocol front matter (line 5) vs register NOTED item 1 (line 1344); AUDIT_CONTEXT.txt line 43; CI_METHODOLOGY.txt line 410

- **Substance:** R17 group 6 (gate-count documentation, NOTED, "reconcile in R18 dispatch documents; derive from build.py output") is not reconciled, and the front matter now asserts it is: "Gate count documentation reconciled." Three values coexist: CI_METHODOLOGY "216 + 6 new = 222 gates" (unchanged), AUDIT_CONTEXT "build.py: 262 gates, all PASS" (a new value), and the executed count on v0.59 bytes: 261 PASS lines (log 01; BUILD PASSED, rc=0). AUDIT_CONTEXT's 262 does not match the executed 261 under the natural PASS-line convention (open enumeration: which counting convention yields 262 -- the "BUILD PASSED" summary line is not a gate). The register's own NOTED item still reads "Gate count 222/261/264 documentation inconsistency. Disposition: NOTED." -- the entry simultaneously claims reconciliation in the Status line and non-repair in its computed register. R17's dispatch-layer count drift recurred with a fresh wrong value.
- **Evidence (EXECUTED):** `grep -o 'PASS:' logs/01_build_py.log | wc -l` = 261; AUDIT_CONTEXT.txt line 43 verbatim "- build.py: 262 gates, all PASS"; CI_METHODOLOGY.txt line 410 verbatim "Step 8: Run the full gate suite (216 + 6 new = 222 gates)."; line 5 "Gate count documentation reconciled."; register NOTED item verbatim (log 06).
- **Recommendation:** derive every advertised gate count from build.py output at dispatch construction (S05's R16 recommendation, third round standing); correct AUDIT_CONTEXT to the executed count; annotate CI_METHODOLOGY's 222 as historical or update it; align the Status claim with the register disposition (reconciled vs NOTED). **Falsifier:** all shipped documents state one gate count and it equals the executed PASS-line count on the same bytes.

### F-S04-59-04 | MEDIUM (Class B) | xz_protocol_register_gen.py validation phase (lines 82-131) vs noted/findings[] paths; r17_findings_index.json dangling group references

- **Substance:** The CI v0.2.2 validation boundary covers only the convergence-group path. Outside it: (i) noted-finding disposition tokens are unvalidated -- M7a emits a BOGUS disposition into the register, so entry item (v)'s unqualified claim "disposition tokens validated against {CLOSED, NOTED, DEFERRED} (fail-closed on unknown)" is overbroad for the NOTED surface; (ii) noted-finding IDs are unvalidated (M7b ACCEPT, emitted); (iii) findings[] record IDs are unvalidated (M6 ACCEPT, no output change) and not uniqueness-checked (M10 ACCEPT); (iv) no cross-layer referential check exists in either direction (M11: group ID with no findings[] record ACCEPT; M12: orphan findings[] record ACCEPT, silently unused); (v) the shipped index itself carries the consequence: findings[] records F-S01-58-06, F-S01-58-07, F-S04-58-05 reference convergence_group 12/13/14, but convergence_groups[] defines only groups 1-11 -- dangling references that no validator catches. The new validation layer is precise where it applies and absent just outside it; the boundary is exactly where the next drift class will live.
- **Evidence (EXECUTED):** battery log 08, M6/M7a/M7b/M10/M11/M12 verbatim ACCEPT lines; r17_findings_index.json: F-S01-58-06 "convergence_group": 12, F-S01-58-07: 13, F-S04-58-05: 14; convergence_groups last group_id 11.
- **Recommendation:** extend fail-closed validation to noted dispositions and noted/findings[] IDs (format + uniqueness); add bidirectional referential checks (every group ID resolvable in findings[] where the schema requires it; every findings[] group reference defined in convergence_groups[]); either define groups 12-14 or null the references with a receipt. Add the six mutation shapes as suite tests. **Falsifier:** M6/M7a/M7b/M10/M11/M12 all raise generation errors naming the offending record, and a schema validator rejects dangling group references.

### F-S04-59-05 | LOW (Class C) | Entry body-repair item (iv) (line 1350); packet closure

- **Substance:** Correction (cf) carries a [DIFF-VERIFIED] tag whose target is outside packet closure: "R16 group 6 adjudication receipt source-severity distribution corrected from '1 MEDIUM (S01) + 2 LOW (S04/S05)' to '2 MEDIUM (S01, S05) + 1 LOW (S04)' in r16_findings_index.json". The r16_findings_index.json file does not ship in this packet (r17_findings_index.json does), so the tagged claim is not reproducible from shipped bytes. The substance is verified where it matters -- the current index's group 6 receipt computes 3 MEDIUM + 1 LOW from findings[] (log 09) -- but the tag asserts diff-verifiability that the packet cannot support. Packet closure (audit evidence = shipped bytes only) makes this an evidence-scope defect, not a truth defect.
- **Evidence (EXECUTED):** line 1350 verbatim; packet listing (no r16_findings_index.json); log 09 group 6 computed distribution {'MEDIUM': 3, 'LOW': 1} matching the receipt.
- **Recommendation:** ship the corrected r16_findings_index.json in the R19 packet, or re-scope the (cf) tag to the shipped index ("verified on r17_findings_index.json group 6 receipt"), or mark the r16-file correction ASSERTED-by-producer. **Falsifier:** the (cf) evidence is reproducible from R19 packet bytes.

### F-S04-59-06 | LOW (Class C) | CI_METHODOLOGY.txt (whole file; ends at the v0.2.1 appendix); FINDINGS_INDEX group 11 (NOTED)

- **Substance:** R17 group 11 (schema inconsistency, NOTED, "reconcile in CI v0.2.2") persists: the shipped CI_METHODOLOGY documents CI v0.2 plus the v0.2.1 appendix and nothing of v0.2.2, while the protocol front matter and AUDIT_CONTEXT describe CI v0.2.2 behavior (disposition validation, ID validation, computed cursor, terminal tag). The standing section 2.1 schema (triage_severity, locus, substance, disposition per finding) and the v0.2.1 appendix schema (five fields) both remain live; shipped findings[] follows the shorter form. There is no normative v0.2.2 schema anywhere in the dispatch set -- the architecture version the entry cites is documented only in the generator docstring and AUDIT_CONTEXT prose.
- **Evidence (EXECUTED):** CI_METHODOLOGY.txt final section header "CI v0.2.1 UPGRADES" (no v0.2.2 section); section 2.1 vs appendix field lists; FINDINGS_INDEX group 11 disposition NOTED.
- **Recommendation:** publish a normative CI v0.2.2 appendix (schema + validation rules + the corrected correction-lettering rule per F-S04-59-01) and explicitly supersede the older of the two live schemas. **Falsifier:** one normative schema exists and the shipped index validates against it.

### F-S04-59-07 | INFORMATIONAL (Class E) | carried observations and tag-economy notes

- **Substance:** (i) No byte-identity register gate: build.py [10c]/[10d]/[10e] check membership, severity proximity (1500-char window), and bracket substrings; no gate compares full generate_register output against the entry -- R17 Defect 10 carried. (ii) The entry tail's PRIOR_HISTORY value is still bare of its [COMPUTED: build.py] tag (F-S04-58-07 carried; methodology Table 3 assigns seal values that tag). (iii) Section 0.1 duplicate carry rationale persists (lines 18/22 vs FB-7b row; F-S04-58-05 carried). (iv) generate_register's version argument remains uncoupled from output (M13: 0.59 vs 9.99 identical). (v) prior_correction_end (53) is itself hand-maintained index data -- the cursor is computed from a hand-kept field; an honest improvement with the hand-maintenance moved one level down. (vi) ASSERTED fraction is basis-dependent: 3.8% by tag-occurrence census (1/26), 5.0% by build.py's own tagged-claims census (1/20), but 17.5% by character share (narrative 1603 of 9182 entry chars) -- above the 15% cap on the R17 S04 char basis, up from 12.3%; the narrative grew while the register shrank proportionally. (vii) Cosmetic: the body-repair paragraph is glued onto the final NOTED line (line 1350) with no line break. (viii) Correction (cf)'s body text names "r16_findings_index.json" -- see F-S04-59-05 for the closure consequence.
- **Evidence (EXECUTED):** build.py lines 611-665; line 1350 tail; protocol lines 18/22; battery log 08 M13; log 10 census; build log line 232.
- **Recommendation:** add a full register byte-identity gate (or document substring-scope as accepted); tag or exempt the PRIOR_HISTORY value by documented convention; adopt the Section 0.1 deletion or qualify the single-source claim; couple or remove the version argument; document prior_correction_end provenance; report the ASSERTED fraction's basis explicitly each round. **Falsifier:** none required at INFO.

## 7. Provenance ledger over the v0.59 entry

| Entry component | Tag | Auditor status |
|---|---|---|
| Narrative paragraph (1603 chars) | [ASSERTED] | Confirmed LLM-authored; every quantitative claim verified against r17_findings_index.json (section 4, group 4 row) -- clean |
| Register items (1)-(9) + NOTED block (7 items) | [COMPUTED: generate_register] x16 | EXECUTED byte-exact (CI-1R); mutation-verified (M2/M9: output tracks the index; probe discriminates). BUT items (1)/(4)/(5) carry the F-S04-59-01 letter collision -- a COMPUTED tag does not certify the cross-reference semantics |
| Body repairs (i)-(v) | [DIFF-VERIFIED] x4 + [COMPUTED: build.py] x1 | (i)-(iii) EXECUTED verified on bytes; (iv) target outside packet closure (F-S04-59-05); (v) partially verified -- every claimed mechanism probed (M1, M4, M5a/b, M8a/b, T0), two claims false at the front-matter level (F-S04-59-02) |
| Boundary list (35 items) | [COMPUTED: generate_boundary_list] + [ENUMERATED: 35 items] | EXECUTED byte-exact; mutation discriminates (B0/B1) |
| PRIOR_HISTORY 4a79f22603c0931e383021f2ca3cda3d7fea96b0a31086f9808e558d13e2bfde | untagged | EXECUTED internal consistency (derivation matches, build [9b] + independent recompute); cross-anchor UNTESTABLE (fresh seat) |
| Terminal line (unsealed tail) | [COMPUTED: generate_terminal_line] | EXECUTED: identical to generator output, unique, final |

Tag census (occurrence basis, log 10): COMPUTED 20 (16 register + 1 boundary + 1 build.py + 1 terminal-line mention + 1 bare quotation inside register item 6's adjudication text), ASSERTED 1 (narrative), DIFF-VERIFIED 4, ENUMERATED 1; total 26. Headline number: ASSERTED fraction 3.8% occurrence basis (build.py's own census: 1/20 = 5.0%); 17.5% character-share basis. Down from 40.0% at v0.56 on any basis; F-CI-2 remains satisfied. On the character basis the fraction ROSE from 12.3% (R17 S04 method) to 17.5% -- recorded so the basis is explicit next round.

## 8. Biomedical Fractal lens: the metastasis boundary (dispatch question)

The R7-R17 pattern held again: the repair landed and the defect moved into the repair. R17's metastasis was "data shipped, mechanism absent" (findings[] inert). R18's is one layer finer, and it has two lobes:

1. **Validation-vs-semantics seam (F-S04-59-02).** CI v0.2.2 shipped the validation half of the findings[] repair (token whitelist) while the Status line and docstring claim the semantic half (derivation + receipt enforcement). The boundary between "checked" and "computed" is now the live surface: everything the generator validates is clean; everything it merely claims to compute is not.
2. **Cursor-granularity seam (F-S04-59-01).** The R17 Defect 9 repair computed the correction cursor from data, but at the wrong granularity (one letter per group vs one per correction). The first multi-correction group shifted the body lettering one position past the register lettering, and the two surfaces now cite each other's letters. The computed surface contradicts itself inside a single entry -- the first Class A to live inside a [COMPUTED: generate_register] claim (F-CI-3R).

The outer layer also persists: the dispatch-layer documents (AUDIT_CONTEXT 262 vs executed 261; CI_METHODOLOGY 222) remain the largest hand-maintained count surface, and the front matter's "reconciled" claim shows the Status line now overclaims repair status the way it once carried stale version tokens.

Predicted residual for R19: (i) whatever surface the F-S04-59-01/F-S04-59-02 repairs introduce (letter gates, derivation logic), and (ii) the noted/findings[] validation boundary (F-S04-59-04) if it is repaired by extension rather than by schema.

## 9. Producer predictions, scored post-hoc

| # | Prediction | Score | Basis |
|---|---|---|---|
| P1 | CI-1R PASS | CONFIRMED | byte-exact, 1 occurrence, register sha256 3de61d0e... |
| P2 | CI-8 PASS; schema edge cases may surface | CONFIRMED | 29/29 + 5/5 IDs, severities match, receipts compute; the hedged edge cases surfaced (dangling groups 12/13/14, no cross-layer checks -- F-S04-59-04) |
| P3 | ASSERTED fraction under 15% | PARTIAL | 3.8% occurrence / 5.0% build census -- under; 17.5% character-share -- over |
| P4 | If Class A exists: narrative, body bounds, Section 0.1, or a NEW CI v0.2.2 surface (findings[] consumption path, disposition validation, ID validation) | CONFIRMED | both Class A findings are on CI v0.2.2 surfaces: findings[] consumption semantics (F-S04-59-02) and the computed correction cursor (F-S04-59-01); narrative and 22.2/22.3 verified clean |
| P5 | Count-list invariant holds (dual cardinality computed) | CONFIRMED | [3-seat / 4-finding] and [2-seat / 3-finding] brackets computed; gate [10e] PASS |
| P6 | Append-only holds | UNTESTABLE | no held prior bytes at this seat (fresh); internal chain consistent; not asserted |
| P7 | Code layer clean (186 GREEN; v0.2.2 adds validation paths) | FALSIFIED for generator semantics | 186/186 GREEN, but M2/M3/M6/M7 shapes pass silently -- the suite does not cover the new validation claims; two Class A on generator-adjacent surfaces |
| P8 | ASSERTED verification fraction under 15% because the packet ships | CONFIRMED | packet shipped; all dispatch verifications EXECUTED; occurrence-basis ASSERTED 3.8% |
| P9 | Disposition validation catches unknown tokens | PARTIAL | group path fail-closed (M4 RAISES); noted path open (M7a ACCEPT, emitted) |
| P10 | Finding-ID validation catches malformed IDs | PARTIAL | group path enforced (M5a/M5b RAISE); findings[]/noted paths open (M6/M7b ACCEPT) |

4 CONFIRMED / 3 PARTIAL / 2 FALSIFIED / 1 UNTESTABLE.

CI falsification status: F-CI-1 (first zero-Class-A round) NOT ACHIEVED -- extends to R18 (12/12). F-CI-2 (ASSERTED decrease) SATISFIED. F-CI-3R (Class A inside a [COMPUTED: generate_register] claim) TRIGGERED for the first time (F-S04-59-01): the defect source is not only memory transit; the generator's own lettering scheme is wrong. F-CI-6R (containment to the ASSERTED floor) NOT SATISFIED this round -- the narrative verified clean and Class A lives on computed/code surfaces instead. F-CI-7R (CI-1R fails) NOT TRIGGERED.

## 10. Boundary report, hedge audit, D-7

- Outermost uncomputed layer at this seat: the PRIOR_HISTORY cross-anchor and append-only across versions -- both require externally held prior bytes; this fresh seat holds none. What brings them inside: a held v0.58 HISTORY.sha256 (or the R17 packet) at R19; this report's packet can serve as the held v0.59 anchor next round. One layer further in, everything executed: 261 gates, 186 tests, 19/19 sums, 59/59 seals, CI-1R, CI-8, 16-probe battery. Standing boundaries: 35 items, byte-exact, carried.
- Hedge/deferral audit: no hedged findings; every finding names its falsifier. Open enumerations stated as questions, not assertions: which counting convention yields AUDIT_CONTEXT's 262; whether the producer intends the register's or the body's lettering as canonical (F-S04-59-01).
- D-7 four one-line answers: (1) Verified: the full 20-file packet -- gates, tests, sums, seals, register, boundary, terminal, CI-8, narrative counts, every R17 repair locus, 16-probe mutation battery. (2) Asserted: nothing producer-side; PRIOR_HISTORY cross-anchor and append-only untestable (fresh seat, stated in S-0). (3) Failed: two Class A (letter collision; derivation/receipt overclaim), two Class B (gate-count docs; validation boundary), two Class C carried. (4) Next round must re-run: CI-1R, CI-4 (both bases), CI-8, the battery including M2/M3/M6/M7 shapes, a letter-collision census across register and body surfaces, gate-count derivation from build output, and the PRIOR_HISTORY anchor against held v0.59 bytes.

## 11. Verdict, repairs, and re-audit conditions

Severity totals: Class A (HIGH) = 2 (F-S04-59-01, F-S04-59-02); Class B (MEDIUM) = 2 (F-S04-59-03, F-S04-59-04); Class C (LOW) = 2 (F-S04-59-05, F-S04-59-06); Class D = 0; Class E (INFO) = 1 (F-S04-59-07).

**VERDICT: HALT (advisory, non-binding).** Class A present (2 findings). As an advisory verdict this does not block convergence by itself; it is recorded with equal triage weight, and the binding carrying seats govern. Recurrence series: R7-R18, 12/12, H = 1.0. Laplace P(Class A at R19) = 13/14 = 0.929.

Minimum repair set before re-carry (v0.60):

1. Single-source the correction-letter namespace at correction granularity; regenerate register and body-repair list from one cursor state; add a collision gate (F-S04-59-01).
2. Implement severity derivation + adjudication-receipt enforcement, or correct the Status line, docstring, and register item (2) disposition to the validation-only scope; add M2/M3 mutation tests (F-S04-59-02).
3. Derive documented gate counts from build output; fix AUDIT_CONTEXT (262 to the executed count); annotate CI_METHODOLOGY 222; align the "reconciled" claim with the register disposition (F-S04-59-03).
4. Extend fail-closed validation to noted dispositions/IDs and findings[] IDs/duplicates; add bidirectional referential checks; resolve dangling groups 12/13/14 (F-S04-59-04).
5. Ship r16_findings_index.json or re-scope the (cf) tag (F-S04-59-05); publish the normative CI v0.2.2 schema appendix (F-S04-59-06).

Re-audit conditions for R19: re-run CI-1R, CI-4 (occurrence AND character bases), CI-8; re-run the full battery including M2/M3/M6/M7 shapes; run a letter-collision census over register vs body surfaces; derive the gate count from build output and diff against every dispatch document; anchor PRIOR_HISTORY against held v0.59 HISTORY bytes.

## 12. Self-corrections ledger

- S1-P6 was REFUTED as designed: this seat preregistered a low-confidence streak-break prediction precisely so a continued streak would register as a refutation, not a rationalization. The streak continues.
- S1-P3 was REFUTED in part: this seat expected "load-bearing" to mean output-affecting; the producer landed validation-only consumption while claiming the full semantics. The prediction's disjunction (raises on invalid / moves output on valid) split: first clause HELD, second REFUTED.
- S1-P8 was basis-sensitive: this seat did not preregister the measurement basis for the ASSERTED fraction; both bases are now reported (3.8% occurrence, 17.5% character). Future freezes should fix the basis in advance.
- No prior-round self-corrections to carry (fresh seat, first round for this instance).

## 13. Final integrity statement

All probing executed on byte copies under /mnt/agents/output/R18_S04_v059/probes/ (mutation_battery.py, ci8_index_fidelity.py); the canonical packet was never modified: PACKET_SHA256SUMS re-verified 19/19 OK after all probing (log 11), and the 10 upload files re-hashed unchanged (log 12). Verbatim evidence preserved at /mnt/agents/output/R18_S04_v059/logs/ (00 packet sums, 01 build, 02 pytest, 03-04 CI-1R, 05 independent recompute, 06 register, 07 entry slice, 08 mutation battery, 09 CI-8, 10 CI-4 census, 11 final sums, 12 upload integrity). S-0/S-1 freeze preserved at /mnt/agents/output/R18_S04_v059/S0_S1_FREEZE.md. No external documents were fetched or admitted as evidence; audit evidence is the shipped bytes only (packet closure). Standing values in this report match the executed outputs verbatim.

---

*R18 Seat S04 advisory audit executed by Kimi K3 (Moonshot AI), fresh, 2026-08-11.*
*Framework: Biomedical Fractal + Repair Verification.*
*Bismillah.*
# R18 Audit Report — Seat S05 (FRESH)

**Protocol:** XZ Protocol v0.59
**Round:** R18
**Seat:** S05 — GPT-5.6 Sol (OpenAI), advisory / non-binding
**Lens:** Differentiator + Adversarial Probing
**Producer:** Claude Opus 4.6 (barred from audit seats)
**Date:** 2026-08-11

## Verdict

**HALT (advisory, non-binding).**

v0.59 does **not** break the R7–R17 Class A streak. At least two independent Class A defects remain on the shipped v0.59 bytes, so the recurrence extends to **R7–R18 = 12/12 rounds with Class A present**.

The strongest failure is in CI v0.2.2 itself: the generator claims adjudication-receipt enforcement and severity derivation from source records, but it only validates that `findings[].source_severity` is an allowed token. The source-layer record, membership, receipt, and valid-severity semantics are not coupled to register generation. A second independent Class A appears in the code-generated correction references: the generator advances one correction letter per convergence group even when one group consumes two corrections, shifting later references and producing byte-false `CLOSED via correction (...)` claims.

## Executed baseline verification

| Verification | Result | Status |
|---|---:|---|
| `python3 build.py` | `BUILD PASSED: all checks GREEN` | EXECUTED PASS |
| Canonical pytest command | 186 passed | EXECUTED PASS |
| `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | EXECUTED PASS |
| CI-1R register reproduction | PASS | EXECUTED PASS |
| HISTORY.sha256 entry seals | 59/59 + FULL_SECTION_27 + PRIOR_HISTORY PASS | EXECUTED PASS |
| ASSERTED fraction | 1/20 = 5.0% | EXECUTED PASS |
| Section 22.2 bound | `v0.1 through v0.57` | EXECUTED PASS |
| Section 22.3 lineage | `v0.38-v0.57` | EXECUTED PASS |
| FB-row digest swap mutation | build fails at FB-3 digest/locus gates | EXECUTED PASS |
| carried-entry edit mutation | build fails at ENTRY_v0.58, FULL_SECTION_27, PRIOR_HISTORY | EXECUTED PASS |

Python runtime was 3.13.5.

## Required mutation battery

| Mutation | Result |
|---|---|
| invalid `findings[].source_severity` (`CRITICAL`) | FAIL-CLOSED with `ValueError` |
| invalid group disposition | FAIL-CLOSED with `ValueError` |
| malformed group `finding_id` | FAIL-CLOSED with `ValueError` |
| duplicate group `finding_id` | FAIL-CLOSED with `ValueError` |
| remove `adjudication_receipt` from mixed-severity group | **INERT — byte-identical generated register** |
| valid source severity change (`HIGH -> LOW`) | **INERT — byte-identical generated register** |
| change top-level `convergence_group` | **INERT — byte-identical generated register** |
| remove a referenced top-level finding record | **INERT — byte-identical generated register** |
| malformed top-level `findings[].finding_id` | **INERT — byte-identical generated register** |
| duplicate top-level `findings[].finding_id` | **INERT — byte-identical generated register** |
| FB-3 digest swap | build FAIL |
| carried v0.58 entry edit | build FAIL |

The dispatch rule requires every mutation to change output or fail generation. The adjudication-receipt mutation fails that rule directly.

---

## Findings — six-element format

### F-S05-59-01

**Severity:** HIGH (Class A)
**Locus:** `xz_protocol_register_gen.py` lines 7–15, 121–132, 146–183; `CI_METHODOLOGY.txt` lines 145–178 and 524–527; protocol front-matter Status line 5; v0.59 entry item (2).

**Substance:** CI v0.2.2 claims `findings[]` is load-bearing, that severity is derived from source records, and that adjudication receipts are enforced. The implementation only validates that each top-level `source_severity` token is in an allow-list, stores records in `findings_by_id`, and never reads that dictionary again. Emitted severity is always `group["triage_severity"]`; `adjudication_receipt` is never checked for presence or consistency. This is a byte-false architecture-closure claim.

**Evidence (EXECUTED):** Removing the adjudication receipt from group 2 produces a byte-identical register. Changing a valid source severity from HIGH to LOW also produces byte-identical output. Changing a finding's `convergence_group`, deleting a referenced finding record, or corrupting/duplicating a top-level finding ID likewise leaves output unchanged. By contrast, an invalid source severity token raises `ValueError`, proving the mutation harness reached the intended validation path. The methodology explicitly requires the generator to use triage severity only when a receipt exists and source severity otherwise; the shipped implementation does not do this.

**Recommendation:** Make `findings[]` authoritative. Resolve every group `finding_id` through `findings_by_id`; reject missing, malformed, duplicate, or multiply inconsistent records; derive the source-severity distribution mechanically; require a structured adjudication receipt whenever group severity differs from the source distribution; and make receipt removal or a valid source-severity mutation either alter output or fail generation.

---

### F-S05-59-02

**Severity:** HIGH (Class A)
**Locus:** v0.59 generated register items (1), (4), and (5), protocol lines 1333–1337; body-repair ledger at line 1350; `xz_protocol_register_gen.py` lines 159–165; `r17_findings_index.json` `prior_correction_end=53` and group repair metadata.

**Substance:** The computed correction cursor is deterministic but semantically wrong for multi-correction defect groups. Group 1 consumes **two** append-only corrections, `(cc)` for Section 22.2 and `(cd)` for Section 22.3. The generator advances `correction_idx` only once per convergence group. It therefore emits `(cc)` for group 1, then incorrectly assigns `(cd)` to the narrative group and `(ce)` to the receipt group. The landed body-repair ledger shows the actual sequence is `(cc)`, `(cd)`, `(ce)`, `(cf)`.

**Evidence (EXECUTED):** Generated register mapping is: item 1 -> `(cc)` Section 22.2/22.3; item 4 -> `(cd)` narrative; item 5 -> `(ce)` receipt. Body repairs are: `(cc)` Section 22.2; `(cd)` Section 22.3; `(ce)` narrative; `(cf)` receipt. Item 1's own adjudication text says the repair requires corrections `(cc)/(cd)`, contradicting its disposition text `CLOSED via ... (cc)`. Items 4 and 5 therefore carry byte-false correction references inside `[COMPUTED: generate_register]` claims.

**Recommendation:** Do not infer one correction per convergence group. Add explicit `correction_refs` (array) or a structured repair list to each group and generate disposition references from those exact refs. Add a build gate that cross-checks every generated correction reference against the body-repair ledger and forbids reuse, omission, or left-shift.

---

### F-S05-59-03

**Severity:** HIGH (Class A)
**Locus:** v0.59 generated register item (3); `AUDIT_CONTEXT.txt` Defect 3; `r17_findings_index.json` top-level finding schema; `xz_protocol_register_gen.py` findings validation path.

**Substance:** The R17 secondary-membership defect is marked `CLOSED via CI v0.2.2 architecture repair`, while the current audit context itself states that v0.2.2 **does not implement multi-membership representation**. The only top-level membership field remains scalar `convergence_group`, and that field is not consumed by the generator. The claimed canonical-group-with-receipt alternative is not machine-represented or enforced, so the defect is dispositioned CLOSED without a verifiable closure mechanism.

**Evidence (EXECUTED):** Mutating a top-level finding's `convergence_group` to another group produces byte-identical register output. No `secondary_groups`, `convergence_groups`, `memberships`, component list, or equivalent field exists in the shipped findings records. The current AUDIT_CONTEXT explicitly acknowledges that multi-membership is not implemented. Register item (3) nevertheless says `HIGH CLOSED via CI v0.2.2 architecture repair: Secondary membership not implemented.`

**Recommendation:** Either implement multi-membership explicitly, or formally replace it with a canonical-assignment specification containing a machine-readable collapse receipt that names every discarded secondary relation. Then validate it during generation/CI-8. Until one of those mechanisms exists, disposition should not be CLOSED.

---

### F-S05-59-04

**Severity:** MEDIUM (Class B)
**Locus:** `AUDIT_CONTEXT.txt` build-status claim; protocol Status line 5; `CI_METHODOLOGY.txt` line 410; runtime build output.

**Substance:** Gate-count documentation is still not reconciled despite the front-matter claim that it is. AUDIT_CONTEXT says `build.py: 262 gates`; the executed build emitted **261 `PASS:` records**; CI_METHODOLOGY still contains `216 + 6 new = 222 gates`. The current register itself leaves the prior gate-count inconsistency NOTED.

**Evidence (EXECUTED):** `python3 build.py | grep -c 'PASS:'` returns `261`. AUDIT_CONTEXT line 43 says 262. CI_METHODOLOGY line 410 says 222. Protocol front matter says `Gate count documentation reconciled.`

**Recommendation:** Derive the build-check count programmatically at runtime and inject that value into dispatch context. Annotate the methodology's 222 as historical if that is the intended meaning. Do not claim reconciliation while current documents disagree.

---

## Repairs confirmed from R17

The following v0.59 repairs are verified effective on this seat:

- Section 22.2 current carried-entry bound advanced to v0.57.
- Section 22.3 carried lineage advanced to v0.57.
- Unknown group disposition tokens fail closed.
- Malformed and duplicate IDs **inside group `finding_ids` arrays** fail closed.
- Header seat word and correction start are computed from index fields.
- Terminal line is generated and tagged.
- Full executable packet shipped and verified.
- FB-row digest swaps are caught.
- Historical carried-entry edits are caught by HISTORY/FULL_SECTION_27/PRIOR_HISTORY checks.
- CI-1R byte reproduction passes.
- 186-test canonical suite is green.

## Producer prediction scorecard

| Prediction | Result |
|---|---|
| P1 CI-1R PASS | CONFIRMED |
| P2 CI-8 PASS | PARTIAL — source index is inspectable, but membership/receipt semantics are not generator-enforced |
| P3 ASSERTED fraction <15% | CONFIRMED (5.0%) |
| P4 Class A, if any, on narrative/body/new CI surface | CONFIRMED on new CI v0.2.2 computed surface |
| P5 count-list invariant | CONFIRMED |
| P6 append-only protection | CONFIRMED for shipped seal-chain and mutation probe |
| P7 code layer clean | FALSIFIED — semantic generator defect |
| P8 executable packet enables low ASSERTED fraction | CONFIRMED |
| P9 disposition validation catches unknown tokens | CONFIRMED |
| P10 finding-ID validation catches malformed IDs | PARTIAL — group-list IDs caught; top-level `findings[]` IDs inert |

## Recurrence answer

**Does v0.59 break the R7–R17 Class A streak? No.**

Class A is present at R18, extending the recurrence series to **12/12 rounds**. Under the same Laplace stationarity convention used by the dispatch, the next-round predictive value would be **13/14 ≈ 0.929**.

## Minimum repair set for v0.60

1. Implement actual source-severity derivation and adjudication-receipt enforcement from `findings[]`.
2. Validate top-level finding IDs, uniqueness, referenced-record existence, and membership consistency.
3. Implement or formally replace secondary membership with a machine-checkable canonical-collapse representation.
4. Replace one-letter-per-group correction allocation with explicit repair-reference arrays and cross-check against the body repair ledger.
5. Add mutation tests for: receipt removal, valid source-severity change, membership change, missing referenced finding, malformed/duplicate top-level ID, and multi-correction group allocation.
6. Reconcile gate-count documentation from runtime output, not hand-maintained prose.

**Final seat verdict: HALT (advisory, non-binding).**
R18 / SEAT S05 / GPT-5.6 SOL (OPENAI)
ADVISORY DIFFERENTIATOR + ADVERSARIAL CONTINUITY AUDIT
XZ Protocol v0.59
Date: 2026-08-11

VERDICT: HALT (ADVISORY, NON-BINDING)
CLASS PROFILE: 3 HIGH (Class A), 2 MEDIUM (Class B)
KEY QUESTION: Does v0.59 break the R7-R17 Class A recurrence streak (11/11)?
ANSWER ON THIS SEAT: NO. Class A remains on v0.59 bytes; the S05 recurrence extends through R18 (R7-R18 = 12/12).

================================================================
§0. AUDITOR SCOPE, CONTINUITY STATE, AND STRUCTURAL-HONESTY DISCIPLINE
================================================================

Role: Seat S05, advisory/non-binding, GPT-5.6 Sol, non-producer family.
Primary lens: Differentiator + adversarial probing.
Mode: CONTINUOUS from R17 S05. The appended R17 report was treated as held prior state, not as proof that any v0.59 repair succeeded.

S-0 INITIAL STATE: UNRESOLVED on receipt. Producer closure labels were hypotheses.

S-1 CONTINUITY FALSIFIERS CARRIED FROM R17:
1. A per-finding source_severity mutation must either alter downstream semantics or hard-fail; mere vocabulary validation is not full provenance coupling.
2. convergence_group and finding_id mutations in findings[] must not be semantically invisible if findings[] is declared load-bearing.
3. Removing an adjudication_receipt where source and triage severities diverge must hard-fail if receipt enforcement is claimed.
4. Malformed and duplicate IDs must fail at every authoritative ID layer, not only one duplicate representation of the IDs.
5. F-S05-58-04 is discharged only if both Sections 22.2 and 22.3 advance to the v0.57 carried bounds.
6. New v0.59 claims are independently diffed against v0.58; current generated surfaces are not presumed correct because CI-1R reproduces them.

Structural-honesty controls applied: substrate over narrative; exact landed-mutation checks; valid-token adversarial mutations in addition to invalid-token probes; cross-layer coupling checks; cross-locus repair propagation; current-entry reference consistency; historical-entry preservation; and strict EXECUTED versus ASSERTED separation.

Supplied R18 S05 ZIP SHA-256:
68424da602db5a82e0c4c71b94b4c67266040bc90a1e243ea9db5040af1144b1

Dispatch limitation: the supplied S05 archive contains the 10 reduced-audit .txt files. It does not contain build.py, the six protocol code modules, six test suites, HISTORY.sha256, PACKET_SHA256SUMS, or the trust-roots manifest. DISPATCH says the full packet ships separately. No such packet was supplied in this seat archive, so full-packet claims are not relabeled EXECUTED.

================================================================
§1. VERDICT
================================================================

HALT.

v0.59 contains genuine repairs, but the R17 Class-A architecture seam is not closed. The strongest current-byte failure is more specific than at R17: CI v0.2.2 now reads findings[] enough to reject an invalid severity token, yet it does not derive register severity from the source records and does not enforce adjudication receipts. A valid source-severity mutation is still semantically invisible; the entire findings[] key can be removed without changing the generated register; receipts can all be removed without error; and a group triage severity can be changed to a different valid severity with or without a receipt.

A second Class A recurs independently: secondary membership is still not represented or checked, even though the v0.59 generated register marks “Secondary membership not implemented” CLOSED via CI v0.2.2 architecture repair. AUDIT_CONTEXT itself concedes that v0.2.2 does not implement multi-membership representation. The only explicit canonical-group resolution carried in the protocol requires recording secondary memberships and a collapse receipt; current findings[] still has one scalar convergence_group field, and generator mutations of that field are invisible.

A third Class A is newly introduced into the [COMPUTED: generate_register] surface. Defect 1 requires two append-only corrections, (cc) and (cd), but generate_register increments the correction cursor once per convergence group, not once per actual correction. Consequently the generated register labels the narrative repair (cd) and receipt repair (ce), while the same current v0.59 entry’s body-repair ledger identifies them as (ce) and (cf). The generated Defect-1 line is internally inconsistent as well: its disposition says CLOSED via correction (cc), while its adjudication says the repair is via corrections (cc)/(cd). This triggers the methodology’s own F-CI-3R shape: a Class A inside a [COMPUTED: generate_register] claim.

Any one of these HIGH findings is sufficient for HALT.

================================================================
§2. EXECUTED / ASSERTED VERIFICATION MATRIX
================================================================

EXECUTED PASS
- CI-1R register reproduction: PASS. Generated register is byte-exactly present in PROTOCOL_v0_59.txt.
  SHA-256: 3de61d0e462e809aee66be6f3f987ebaa4d3ca703d673d5ef82721e534dbdbc8
- Boundary-list reproduction: PASS.
  SHA-256: 9ea98b840ff1287a4c9e876d4b8a17743ff84b08930553a8ec9d26da02de7a7b
- Terminal-line generation/tagging: PASS.
  SHA-256: 159d3eabc1b9b337710ed6c68aa7b57c9a9b9d0aa72cee36baaee9db4b02c2de
- F-S05-58-04 body repair: PASS. Section 22.2 now says carried entries v0.1 through v0.57; Section 22.3 now says carried at v0.38-v0.57. The old exact stale tokens have zero current occurrences.
- Unknown group disposition token: PASS. CLOSED -> CLOZED raises ValueError.
- Invalid group severity token: PASS. HIGH -> CRITICAL raises ValueError.
- Invalid findings[] source-severity token: PARTIAL PASS at the token layer. HIGH -> CRITICAL raises ValueError.
- Malformed group finding ID: PASS. Rejected with ValueError.
- Duplicate group finding ID: PASS. Rejected with ValueError.
- Header seat word: PASS as a computed dependency. Adding S06 to index["seats"] changes five-seat -> six-seat.
- Correction cursor source: PASS as a computed dependency. Incrementing prior_correction_end changes generated correction labels.
- Historical amendment content: PASS. v0.1-v0.58 entry contents are unchanged from v0.58 after excluding the separator newline required before the newly appended v0.59 entry.
  Normalized prior-entry content SHA-256: 2b2e75b31ab7d363f754256bbe44285acecbafba223e4776a301baa49166e710
- Current baseline group-to-findings scalar cross-links are internally self-consistent for groups 1-11.

EXECUTED FAIL / ADVERSE
- findings[0].source_severity HIGH -> MEDIUM (valid token): ACCEPTED; register byte-identical.
- findings[0].convergence_group -> 99: ACCEPTED; register byte-identical.
- findings[0].finding_id -> another syntactically valid ID: ACCEPTED; register byte-identical.
- findings[0].finding_id -> BOGUS-X-THING: ACCEPTED; register byte-identical.
- duplicate top-level findings[] ID: ACCEPTED; register byte-identical.
- remove group 2 adjudication_receipt: ACCEPTED; register byte-identical.
- remove every adjudication_receipt: ACCEPTED; register byte-identical.
- delete the entire findings[] key: ACCEPTED; register byte-identical.
- replace findings[] with []: ACCEPTED; register byte-identical.
- group 2 triage_severity HIGH -> LOW with receipt: ACCEPTED; generated register changes to LOW.
- same HIGH -> LOW mutation with receipt removed: also ACCEPTED; same generated result. Receipt presence has no enforcement effect.
- falsify receipt text to “all LOW”: ACCEPTED; register byte-identical.
- current correction references disagree: generated register uses cc / cd / ce across the three correction-type groups, while body repairs consume cc+cd / ce / cf.
- gate-count documentation remains inconsistent: AUDIT_CONTEXT says 262; CI_METHODOLOGY still says 222 despite current Status saying documentation was reconciled.
- top-level findings F-S01-58-06, F-S01-58-07, and F-S04-58-05 carry convergence_group values 12/13/14 even though convergence_groups contains only 1-11; the generator does not validate these references. They are also represented through unique_findings_noted.

ASSERTED / UNTESTABLE FROM THE SUPPLIED S05 ARCHIVE
- build.py: producer says 262 gates all PASS.
- pytest: producer says 186 tests GREEN.
- PACKET_SHA256SUMS.
- HISTORY.sha256 / PRIOR_HISTORY build-gate behavior.
- full executable code-module identity and trust-root checks.
- build-layer CI-8 implementation, including whether an absent full-packet gate would independently catch the generator-level provenance mutations above.
- correction (cf) claim that the old R16 r16_findings_index.json receipt was rewritten to the correct 2 MEDIUM + 1 LOW distribution; the corrected r16 index file is not in this reduced R18 archive.

================================================================
§3. FINDINGS -- SIX-ELEMENT FORMAT
================================================================

F-S05-59-01
Severity: HIGH (Class A)
Locus: PROTOCOL_v0_59.txt front-matter Status and v0.59 entry; REGISTER_GENERATOR.txt lines 7-16, 59-68, 121-131, 146-182; CI_METHODOLOGY §§2.1-3.2 and v0.2.1 upgrade 4; FINDINGS_INDEX.txt.
Substance: CI v0.2.2’s advertised findings[] consumption, “severity derivation from source records,” and adjudication-receipt enforcement are not implemented end-to-end. findings[] is only token-validated; it is not authoritative for group/register severity and can be removed entirely without changing output.
Evidence: The current Status explicitly says “findings[] consumption, severity derivation from source records, adjudication receipt enforcement.” REGISTER_GENERATOR step 5 validates only source_severity vocabulary and stores findings_by_id, but findings_by_id is never consulted after construction. Generation still unconditionally sets sev = group["triage_severity"]. A valid HIGH->MEDIUM source mutation is accepted with byte-identical register output; deleting findings[] or emptying it is accepted with byte-identical output. Removing one or all adjudication_receipt fields is accepted. Changing group 2 triage HIGH->LOW is accepted whether its receipt is present or absent. A deliberately false receipt is accepted. This contradicts both the generator docstring’s receipt-enforcement claim and CI_METHODOLOGY R3, which says triage severity is used only with an adjudication receipt and source severity otherwise.
Recommended remediation: Make findings[] mandatory and authoritative. Validate every group finding_id resolves exactly once into findings[]. Derive each group’s source distribution from those records. If triage_severity differs from the mechanically derived rule, require a typed receipt with machine-checkable source distribution and a non-computable rationale. Reject missing, stale, false, or superfluous receipts as appropriate. Add valid-token mutation tests, not just CRITICAL-token tests.
Citation traceability: R17 F-S05-58-01 and R17 S02 F-S02-58-01 are the direct predecessor findings; R17 TRIAGE minimum repair item 2 requires deriving group severity from source records with mandatory receipt on divergence.

F-S05-59-02
Severity: HIGH (Class A)
Locus: AUDIT_CONTEXT.txt Defect 3; PROTOCOL_v0_59.txt historical v0.58 item (5), current v0.59 register item (3), and Status; FINDINGS_INDEX findings[] and convergence_groups; REGISTER_GENERATOR validation/generation path.
Substance: Secondary convergence membership remains unimplemented and unverified, yet the current code-generated register marks the defect CLOSED via CI v0.2.2 architecture repair.
Evidence: AUDIT_CONTEXT expressly states v0.2.2 “does not implement multi-membership representation.” Current findings[] records still have only scalar convergence_group. No secondary_groups, convergence_groups[], memberships, or equivalent relation exists. The protocol’s carried canonical-group resolution states that secondary memberships are to be recorded in findings[] and a receipt added for collapsed overlaps. Current group-level adjudication receipts describe severity decisions, not the missing many-to-many relation. Mutating a findings[].convergence_group to 99, to another existing group, or deleting the field is accepted without changing the generated register. The current register nonetheless emits “Secondary membership not implemented” as HIGH CLOSED via CI v0.2.2 architecture repair.
Recommended remediation: Either (a) represent the full many-to-many relation with primary_convergence_group plus secondary_convergence_groups[] (or convergence_groups[]) and gate it against triage, or (b) normatively supersede the earlier lossless-membership requirement with an explicit scoped boundary and a machine-readable collapse receipt per affected finding. In either case, mutations of the membership relation must fail or alter verified output.
Citation traceability: Direct recurrence of R17 F-S05-58-02 / S02 F-S02-58-02. R17 TRIAGE minimum repair item 3 allowed implementation or explicit scope-out; the current protocol does not contain a normative secondary-membership boundary that replaces the prior recorded requirement.

F-S05-59-03
Severity: HIGH (Class A)
Locus: PROTOCOL_v0_59.txt current v0.59 register items (1), (4), (5) and Body repairs (i)-(iv); FINDINGS_INDEX prior_correction_end and repair_type; REGISTER_GENERATOR correction_idx logic.
Substance: The code-generated register misbinds append-only correction letters because it allocates one correction label per convergence group even when one group requires multiple distinct body corrections.
Evidence: prior_correction_end=53 makes the next label (cc). Group 1 is a single convergence group with repair_type=correction, so the generator consumes only (cc), even though its own adjudication says Sections 22.2/22.3 are repaired via corrections (cc)/(cd). The next correction-type group (narrative) is therefore emitted as correction (cd), and the receipt group as (ce). The same v0.59 entry’s Body repairs ledger states the actual sequence: (cc) Section 22.2; (cd) Section 22.3; (ce) narrative; (cf) receipt. Thus current generated item (4) points to (cd) while its repair ledger points to (ce), and item (5) points to (ce) while its ledger points to (cf). Item (1) is internally inconsistent between “via correction (cc)” and “via corrections (cc)/(cd).”
Recommended remediation: Model corrections explicitly rather than inferring one correction per group. A convergence group should carry correction_refs[] (e.g. ["cc","cd"]) or repair_actions[] with one generated correction reference per actual body mutation. Generate both the register disposition and Body repairs ledger from that same structured list. Add a bijection gate: every current correction label appears exactly once in the body-repair ledger and every register correction reference resolves to the intended repair action(s).
Citation traceability: New R18 defect. It is the current-round realization of CI_METHODOLOGY F-CI-3R: a Class A appears in a [COMPUTED: generate_register] claim.

F-S05-59-04
Severity: MEDIUM (Class B)
Locus: PROTOCOL_v0_59.txt front-matter Status; AUDIT_CONTEXT.txt Build status; CI_METHODOLOGY Step 8.
Substance: The gate-count documentation defect is still not reconciled despite the current Status explicitly saying “Gate count documentation reconciled.”
Evidence: AUDIT_CONTEXT states build.py has 262 gates. CI_METHODOLOGY Step 8 still says “216 + 6 new = 222 gates.” The full executable packet is absent here, so this seat cannot establish the true runtime count, but it can establish that the documentation remains internally contradictory.
Recommended remediation: Remove hand-maintained gate totals from methodology prose or code-generate a versioned execution receipt. If historical methodology text is intentionally frozen, mark 222 explicitly as “v0.57 historical count, superseded by current build count” so it cannot be mistaken for current documentation.
Citation traceability: Direct recurrence of R17 F-S05-58-05 / triage Defect 6.

F-S05-59-05
Severity: MEDIUM (Class B)
Locus: REGISTER_GENERATOR.txt validation steps 4-5; FINDINGS_INDEX top-level findings[]; PROTOCOL_v0_59.txt register item (9).
Substance: R17’s malformed/duplicate ID repair is complete only for convergence_groups[].finding_ids, not for the newly declared authoritative findings[] source layer.
Evidence: Group-level BOGUS-X-THING and within-group duplicate IDs now correctly raise ValueError. But changing findings[0].finding_id to BOGUS-X-THING is accepted with byte-identical output; replacing it with another syntactically valid ID is accepted; duplicating two top-level finding IDs is accepted. No global uniqueness check exists on findings[], and group IDs are not cross-resolved against findings_by_id. Because findings[] is advertised as load-bearing provenance, malformed or duplicate IDs remain valid at that source layer.
Recommended remediation: Validate FINDING_ID_RE over every findings[] record, enforce global uniqueness, verify seat matches ID prefix, require every group ID to resolve exactly once to a source record, reject orphan source records unless explicitly NOTED, and validate convergence_group references against existing groups or explicit null/noted semantics.
Citation traceability: Partial recurrence of R17 F-S05-58-06. The narrower group-list mutation is fixed; the source-record version of the same invariant is not.

================================================================
§4. R17 MUTATION MATRIX RE-RUN
================================================================

Probe                                                R17       v0.59 result
---------------------------------------------------------------------------------------------
findings[].source_severity -> CRITICAL                FAIL      HARD-FAIL (improved)
findings[].source_severity HIGH -> MEDIUM (valid)     n/a       ACCEPT / byte-identical (FAIL)
findings[].convergence_group mutate                   FAIL      ACCEPT / byte-identical (FAIL)
findings[].finding_id valid mutation                  FAIL      ACCEPT / byte-identical (FAIL)
findings[].finding_id malformed                       implicit  ACCEPT / byte-identical (FAIL)
top-level duplicate finding_id                        implicit  ACCEPT / byte-identical (FAIL)
remove adjudication_receipt                           FAIL      ACCEPT / byte-identical (FAIL)
remove entire findings[]                              n/a       ACCEPT / byte-identical (FAIL)
malformed group finding_id                            FAIL      HARD-FAIL (fixed)
duplicate group finding_id                            FAIL      HARD-FAIL (fixed)
unknown disposition token                             FAIL R17  HARD-FAIL (fixed)
group severity invalid token                          PASS R17  HARD-FAIL (still PASS)
header seat literal                                   FAIL R17  computed from seats (fixed)
correction cursor literal                             FAIL R17  computed from prior_correction_end (partially fixed; see F-S05-59-03)
terminal tag                                          FAIL R17  exact computed tag present (fixed)

The decisive continuity result is that v0.2.2 converts one weak mutation (invalid source-severity token) into a hard failure but still permits semantically valid provenance changes, receipt deletion, membership mutation, and even total findings[] removal. Therefore the R17 falsifier “source provenance mutation must alter verified semantics or fail” is not satisfied.

================================================================
§5. v0.58 -> v0.59 DIFFERENTIATOR RESULTS
================================================================

Verified improvements:
- Title, front-matter version, Section 0.1 current version, entry count, and FB-7b current token advanced to v0.59.
- Section 22.2 and 22.3 stale carried bounds are corrected.
- v0.59 terminal line is generated and [COMPUTED]-tagged.
- Unknown dispositions fail closed.
- Malformed/duplicate IDs fail closed inside convergence-group finding lists.
- Register header seat word is computed from index["seats"].
- Correction cursor begins from index["prior_correction_end"].
- CI-1R, boundary reproduction, and terminal reproduction all pass.
- Prior v0.1-v0.58 historical amendment entry contents are preserved.
- Current R17 narrative gives per-defect convergence counts rather than the ambiguous v0.58 aggregate wording.

Failed/new differences:
- Front Status overstates v0.2.2 as implementing source-derived severity and receipt enforcement (F-S05-59-01).
- Secondary membership is still not represented while marked CLOSED (F-S05-59-02).
- New correction-letter generation is not cardinality-aware when one defect group maps to two corrections, creating current-entry referential contradictions (F-S05-59-03).
- Gate-count “reconciled” claim remains false at documentation level (F-S05-59-04).
- ID validation is layer-incomplete at findings[] (F-S05-59-05).

No substantive append-only historical rewrite was found. The only raw comparison difference at the v0.58/v0.59 entry seam is the separator newline inserted before the appended v0.59 entry; prior entry content is unchanged.

================================================================
§6. R17 S05 FINDING DISCHARGE TABLE
================================================================

F-S05-58-01 severity provenance / receipt enforcement: NOT DISCHARGED. Partial token validation landed; source derivation and receipt enforcement did not. Recurs as F-S05-59-01.

F-S05-58-02 secondary membership: NOT DISCHARGED. AUDIT_CONTEXT admits multi-membership is not implemented; scalar membership remains semantically invisible. Recurs as F-S05-59-02.

F-S05-58-03 false group-6 receipt: PARTIAL / TARGET FILE UNTESTABLE. The current v0.59 entry states the correct distribution, 2 MEDIUM + 1 LOW, but the claimed corrected r16_findings_index.json is not in the reduced archive. More importantly, the new generator still cannot verify receipt truth (F-S05-59-01).

F-S05-58-04 Sections 22.2/22.3 stale: DISCHARGED. Both exact current tokens are correct and stale exact tokens are absent.

F-S05-58-05 gate count docs: NOT DISCHARGED. 262 vs 222 persists. Recurs as F-S05-59-04.

F-S05-58-06 malformed/duplicate IDs: PARTIALLY DISCHARGED. Group finding lists now fail closed; top-level findings[] IDs do not. Recurs in narrowed form as F-S05-59-05.

================================================================
§7. PRODUCER PREDICTION SCORECARD
================================================================

P1 CI-1R PASS: CONFIRMED (executed byte-exact reproduction).
P2 CI-8 PASS: FALSIFIED at the architecture/membership semantics required by this seat. Baseline scalar links are internally consistent, but membership mutations are not coupled and secondary relations remain unrepresented; the full build-layer CI-8 gate is unavailable.
P3 ASSERTED fraction under 15%: CONFIRMED by simple current-entry tag census proxy (1 ASSERTED vs 20 COMPUTED occurrences); exact build metric unavailable.
P4 If Class A exists, it may be in a new CI v0.2.2 surface: CONFIRMED. F-S05-59-01/02 are in the new consumption/membership path; F-S05-59-03 is in generated correction-reference logic.
P5 Count-list invariant holds: CONFIRMED on baseline register cardinalities; correction-reference cardinality is a separate new failure.
P6 Append-only holds: CONFIRMED for historical entry content.
P7 Code layer clean: FALSIFIED for the shipped register-generator tooling; six protocol modules remain untestable because absent.
P8 executable packet ships/included so seats can execute: FALSIFIED for the supplied S05 archive / otherwise UNTESTABLE as a separate artifact. The archive has 10 .txt files and no executable packet.
P9 disposition validation catches unknown tokens: CONFIRMED.
P10 finding-ID validation catches malformed IDs: PARTIAL. Confirmed for convergence-group finding lists; falsified for top-level findings[].finding_id.

================================================================
§8. RECOMMENDED REPAIR PATH
================================================================

1. Make findings[] truly mandatory and authoritative. There must be no fallback where missing/empty findings[] reproduces the same register.
2. Derive group severity from the source-record relation. Valid source-severity changes must change the derived state or force an adjudication path; invalid tokens are only the outermost validation layer.
3. Enforce adjudication receipts mechanically: source distribution, deviation, affected IDs, and chosen triage severity must be cross-checked. Receipt deletion or falsification must fail.
4. Resolve secondary membership explicitly. Either implement a many-to-many field and gate it, or normatively supersede that requirement with an explicit boundary and typed collapse receipts. Do not mark “secondary membership not implemented” CLOSED via architecture while the architecture remains scalar-only.
5. Replace one-correction-per-group sequencing with explicit repair_actions[] / correction_refs[]. Group 1 must consume both cc and cd before the next group receives ce. Generate the Body repairs ledger from the same structure.
6. Extend ID/schema validation to findings[]: regex, global uniqueness, seat-prefix match, group existence, exact cross-reference, orphan/noted rules.
7. Reconcile the 222/262 gate-count wording or label the 222 figure as historical/superseded.
8. Ship the full executable packet with the seat dispatch so build.py, pytest, PACKET_SHA256SUMS, HISTORY.sha256, CI-8 build gates, and seal mutations can be executed on the same audit turn.

Minimum falsifier for v0.60:
- delete findings[] -> generation MUST fail;
- change any valid source_severity -> derived group state MUST change or a receipt validation MUST fail;
- remove or falsify a required receipt -> generation/build MUST fail;
- mutate primary/secondary membership -> CI-8/generation MUST fail unless the verified relation changes correspondingly;
- mutate a top-level source finding ID -> global schema validation MUST fail unless all linked structures are coherently updated;
- every current correction label must resolve bijectively between the structured repair actions, generated register, and current Body repairs ledger.

================================================================
§9. AUDIT CHAIN INTEGRITY STATEMENT
================================================================

This is an advisory S05 continuity HALT, not a carrying/binding verdict. It credits the v0.59 repairs that actually landed and does not infer failure from the prior 11/11 recurrence prior. The HALT is based on current v0.59 substrate and executed mutations.

CI-1R proves that the shipped protocol contains the generator’s output; it does not prove the generator implements the provenance and repair semantics claimed for that output. Here, the byte-exact generated output itself contains a correction-reference contradiction, and the structured source layer remains only partially coupled.

No conclusion is drawn about build.py, pytest, PACKET_SHA256SUMS, HISTORY.sha256, or the six protocol code modules beyond “not executable from the supplied S05 reduced archive.”

END OF R18 S05 ADVISORY CONTINUITY AUDIT

---

# Bismillah ir-Rahman ir-Rahim
