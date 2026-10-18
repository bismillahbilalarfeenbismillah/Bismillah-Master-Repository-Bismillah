# Bismillah ir-Rahman ir-Rahim

# R0241 -- XZ Protocol v0.64 -- Round 23 Seat S04 Report

**Chronological Index:** 528 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v064_R23_S04_REPORT (1).md  
**Source Format:** md  
**SHA-256:** `6213d535a534ee6ef58528a6298180178e02ea3dbcfc7cfa88f40237181e322c`  

---

## R0241 · XZ Protocol v0.64 -- Round 23 Seat S04 Report

- section: IV. XZ Protocol
- source_file: XZ_v064_R23_S04_REPORT (1).md
- source_format: md
- text_sha256: 6213d535a534ee6ef58528a6298180178e02ea3dbcfc7cfa88f40237181e322c

# XZ Protocol v0.64 -- Round 23 Seat S04 Report

**Round:** R23 ("Confinement Verification")
**Artifact:** XZ Protocol v0.64 DRAFT CANDIDATE
**Seat:** S04 | **Role:** ADVISORY | **Mode:** FRESH (no prior context, no held bytes)
**Dispatched family:** Gemini 3.1 Pro | **Executing family:** Claude Opus 5 (Anthropic)
**Date:** 2026-08-17
**Methodology:** Structural Honesty Verification Methodology (canonical, v4)
**Finding namespace:** F-S04-64-NN

> Auditor operated in **Mode A** with full substrate access: packet extraction, `sha256sum -c`,
> `python3 build.py`, `pytest`, direct mutation probes against `xz_protocol_register_gen.py`,
> and byte-offset computation on the shipped protocol.
> Substrate-claim verification confidence: **high** for L1--L4 and L6.
> Substrate-claim verification confidence: **reduced** for L5 -- no held v0.63 bytes were supplied,
> so temporal claims are verified against the artifact's own admissions, not against external bytes.

---

## S0. Seat identity, conformance, and disqualifying conditions

Three conformance defects are disclosed before any finding, because they bear on how this
report's evidence should be weighted.

**S0.1 -- Identity mismatch.** DISPATCH.txt addresses seat S04 to Gemini 3.1 Pro. This seat
was executed by Claude Opus 5. This is the same class as F-S01-63-07 at R22 and is logged
here as F-S04-64-14. The audit is valid; the seat label is wrong.

**S0.2 -- Producer-family contamination.** AUDIT_CONTEXT.txt states the producer is Claude
Opus 4.6 and is BARRED. The executing model is Claude Opus 5 -- same vendor, same family, one
generation forward. The canonical methodology's standing rule 7 (cross-vendor rotation)
excludes the producer instance from the auditor pool, and axiom A-X3 (model non-collusion)
is a cross-**family** assumption. This seat therefore **cannot serve as the non-producer
witness** contemplated by Bearer 5, and its non-findings carry no clearance weight.
Its positive findings retain full weight under the "no advantage from world" principle:
per METHODOLOGY Section 5, defects found despite architectural similarity to the producer
are precisely the producer's systematic misses. Logged as F-S04-64-15.

**S0.3 -- Seat trial not reproduced.** The canonical seat table assigns S04 the trial "no code
execution, textual only," whose value is that reading the code finds spec-implementation gaps
that running the code does not reveal. This seat had code execution and used it. The findings
below are stronger in evidence tier (Tier 1 executed rather than Tier 2 textual) but the R23
seat lattice has lost its textual-only cell. Logged as F-S04-64-16.

**S0.4 -- Fresh-instance discipline.** This instance holds a persistent memory store containing
prior XZ seat lineages. Under FRESH dispatch those files were **not** read. Only the ten
dispatched packet files and the canonical audit skill were loaded. No prior-round finding IDs
were carried in from memory; every cross-reference below to a prior finding comes from
FINDINGS_INDEX.txt or R22_TRIAGE.txt as shipped.

---

## S1. Staging and reproduction

Extraction snippet from AUDIT_CONTEXT.txt executed verbatim. 17 files extracted, plus the three
renamed copies (`xz_protocol_v0_64.md`, `r22_findings_index.json`, `xz_protocol_boundaries.json`).

| Check | Claimed (AUDIT_CONTEXT) | Observed | Result |
|---|---|---|---|
| `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | 19/19 OK, rc=0 | MATCH |
| `pytest` 6-suite explicit | 186 GREEN | 186 passed | MATCH |
| `build.py` | 253 PASS, 0 FAIL | **252 PASS, 0 FAIL** | **DIVERGENT** |
| HISTORY.sha256 | 64 ENTRY + FULL_SECTION_27 + PRIOR_HISTORY | 64 + 1 + 1 (66 lines) | MATCH |
| Section 22.4 | PRESENT, 5 axioms + Sidrat | PRESENT at line 722 | MATCH |
| CI-1R | PASS | PASS, byte-exact substring | MATCH |

Interpreter: CPython 3.12.3 (satisfies boundary item 28).
Environment note: on a first run without `pytest` installed, `build.py` emitted 249 PASS and
2 FAIL and exited non-zero. The 252/0 figure is post-install and is the deterministic value
across repeated runs.

Artifact digests (first 16 hex):
`c6d911a5422d8faf` protocol, `d415bb4ffc945f4c` build.py,
`9a8253b4ba424aa0` register_gen.py, `d1d5b969e7b4cbfc` HISTORY.sha256.

---

## S2. CI-1R -- deterministic register reproduction

`generate_register('r22_findings_index.json', '0.64')` produced 2224 characters. The shipped
v0.64 entry contains that string **verbatim and contiguously**. `generate_boundary_list` (1797
chars) and `generate_terminal_line` (78 chars) likewise appear verbatim.

**CI-1R: PASS.** F-CI-7R does not fire. The register was not modified after generation.

This is a real and non-trivial result. It is also the reason F-S04-64-01 below is serious:
CI-1R proves the register is a faithful function of the generator, and the generator is
reading the wrong field.

---

## S3. R22 discharge -- did the prescribed repairs land?

| R22 group | Prescribed route | Landed on v0.64 bytes? |
|---|---|---|
| 1 (entry outside seal span) | Move v0.63 entry above Provenance | **YES** -- entry at offset 410468, Provenance at 422846 |
| 2 (noted-array UnboundLocalError) | Move validation after `declared_group_ids` init | **YES** -- probe J now rejects via ValueError |
| 3 (Section 22.4 absent) | Add 22.4 + append-only correction | **YES** -- both present |
| 4 (four-scribe tagging) | Tag every sentence per discipline | **NO** -- see F-S04-64-03 |
| 5 (gate count 258 vs 257) | Count by tool | **NO** -- recurred as 253 vs 252, see F-S04-64-09 |

Three of five landed. Group 4 and group 5 are emitted as `CLOSED` in the shipped register while
the defects they name are live on the same bytes.

---

## S4. Probe battery

All probes executed against `generate_register` with mutated copies of the shipped index.

| Probe | Mutation | Result |
|---|---|---|
| G/P-3 | `adjudication_receipt` substring `1 HIGH` | REJECT (ValueError, exact-equality) |
| H | reverse membership parity | REJECT (ValueError) |
| J | noted `convergence_group` = 99 | **REJECT via VALIDATOR, not crash** |
| K | `findings[].seat` = "S99Z" | REJECT (ValueError) |
| K2 | noted `seat` = "S99Z" | **REJECT (ValueError)** -- new validation confirmed |
| N1 | noted missing `substance` | REJECT (ValueError) |
| N2 | noted `disposition` = "MAYBE" | REJECT (ValueError) |
| **N3** | noted `finding_id` = "XX-BOGUS" | **ACCEPTED -- FALSE PASS** |
| **N4** | noted `finding_id` duplicates a grouped ID | **ACCEPTED -- FALSE PASS** |
| **S1** | group `surface` key deleted | **ACCEPTED -- no output change** |
| **S2** | group `surface` replaced with fabricated text | **ACCEPTED -- no output change** |

Probes J and K2 confirm predictions P2 and P13. Probes N3, N4, S1, S2 are new false-PASS
discoveries at Layer 4.

---

## S5. Seven-layer traversal

**L1 (code execution).** 186 GREEN, 252 gates PASS, 19/19 digests OK. One live defect:
F-S04-64-01, in the register generator, on the shipped `[COMPUTED]` path.

**L2 (register verification).** CI-1R byte-exact PASS. Clean.

**L3 (cross-layer consistency).** Four defects: Status line versus tag census (F-S04-64-03),
Section 0.1 versus the FB-7b row it names as single source of truth (F-S04-64-04), FB-7b row
trajectory four rounds stale (F-S04-64-05), narrative count-list decoupling against the COMPUTED
bracket (F-S04-64-06), and dispatch gate count versus tool (F-S04-64-09).

**L4 (adversarial probing).** Four false-PASSes: F-S04-64-01 (surface field unread),
F-S04-64-07 (noted ID format and uniqueness unvalidated).

**L5 (temporal integrity).** Seals recompute, PRIOR_HISTORY derives. One structural finding:
F-S04-64-02, the R22 repair silently re-anchored the v0.63-era sealed surface.

**L6 (methodology audit).** Tagging discipline not deployed (F-S04-64-03); no gate enforces it
(F-S04-64-11); the ASSERTED-fraction metric measures tags rather than text (F-S04-64-08);
`[ASSERTED]` is outside the canonical tag set (F-S04-64-10).

**L7 (boundary disclosure).** Section 22.4 present, complete, and consistent with the canonical
methodology's axiom set. Sidrat clause present in both the entry and the body. **This layer is
clean.** Bearer 6 flips TRUE.

Standing-rules sweep: em-dash policy clean (no U+2013/2014/2015 in protocol, build.py, or
generator), brand canonical clean (2 occurrences, no spaced variant), severity casing clean.

---

## S6. Findings

### F-S04-64-01 [HIGH] -- Register generator reads a field the index does not supply; every register item ships with an empty defect-surface description

- **Locus:** `xz_protocol_register_gen.py` line ~264 (`group.get('label', '')`); shipped effect at `xz_protocol_v0_64.md` Section 27, v0.64 entry, register items (1)--(5).
- **Substance:** `FINDINGS_INDEX.txt` supplies each convergence group's defect description under the key `surface`. The generator emits `group.get('label', '')`, a key that appears nowhere in the index. Python's `.get` default silences the miss, so all five register items ship as `... HIGH CLOSED: . Source distribution: ...` with an empty string where the defect surface belongs. Probe S1 (delete `surface`) and probe S2 (replace `surface` with fabricated text) both produce byte-identical register output, proving the field is entirely unread. This is a Class A in a `[COMPUTED: generate_register]` claim, which is precisely the condition F-CI-3R names as a generator bug rather than a prose defect, and it is a **code-layer** defect on v0.64 shipped bytes.
- **Disposition:** Change the emission to `group['surface']` with subscript access (not `.get`) so a missing key raises. Add a validation pass requiring a non-empty `surface` on every group in `convergence_groups`, mirroring the existing `substance` requirement on noted entries. Add a probe fixture asserting that mutating `surface` changes generator output.
- **Cross-reference:** CI_METHODOLOGY F-CI-3R; R22 group 4 disposition (tagging), which shares the pattern of a repair that is asserted rather than gated; boundary item 23 ("[9e] silent vacuity") is the nearest disclosed class but does not cover this locus.

### F-S04-64-02 [HIGH] -- The R22 entry relocation silently re-anchored the v0.63 sealed surface, and no gate can detect it

- **Locus:** `build.py` `derive_prior_history` / `_full_seal` (lines 76--135); `HISTORY.sha256` PRIOR_HISTORY line; v0.64 entry repair clause (1).
- **Substance:** `_full_seal` computes FULL_SECTION_27 over Section 27 text truncated at the Provenance marker. R22 established, and the v0.64 entry itself admits, that the v0.63 entry previously sat **after** that marker and now sits **before** it. Those two layouts necessarily produce different FULL_SECTION_27 values. Computed on the shipped bytes: with the v0.63 entry inside the span the derived v0.63 seal is `e6f22478774b8734...`; with the entry relocated to its R22-reported position the same function yields `9e9eb33b534b4733...`. The v0.63-era anchor and the anchor `build.py` now derives cannot both be the historical value. Gate [9b] nonetheless reports `PRIOR_HISTORY matches derivation`, because `reconstruct()` rebuilds every prior level from **current** bytes rather than from held prior bytes -- the chain is self-consistent by construction. The R22 CRITICAL repair was correct and necessary; its append-only consequence is undisclosed in the entry, in the boundary list, and in Section 22.4.
- **Disposition:** Add an append-only correction sentence to the v0.65 entry recording that the v0.63 relocation changed the v0.63 FULL_SECTION_27 domain, stating both values. Add a standing boundary item naming derived-anchor self-consistency as a known non-detection. Longer term, publish an external anchor (the deposited DOI record) so that at least one level of the chain is verifiable against bytes the producer does not control.
- **Cross-reference:** Boundary item 32 (self-consistent resealing blind spot, proven live at v0.47) covers the class but not this instance; boundary item 6 (seal terminus at Provenance marker); axiom A-X4, which explicitly concedes non-detection before the first external anchor; R22 group 1 (F-S01-63-01).

### F-S04-64-03 [HIGH] -- "Four-scribe tagging corrected" is byte-false; the class fix did not land

- **Locus:** `xz_protocol_v0_64.md` line 5 (Status), and Section 27 v0.64 entry narrative paragraph.
- **Substance:** The Status line asserts four-scribe tagging is corrected, and register item (4) emits R22 group 4 as `HIGH CLOSED` with the adjudication "Fix: tag every sentence per canonical discipline." Tag census on the shipped entry: `[COMPUTED]` 14, `[DISCLOSED]` 1, `[ENUMERATED]` 1, `[ASSERTED]` 1, **`[TESTED]` 0, `[WITNESSED]` 0**. Sentence census on the narrative paragraph: 8 sentences, **5 carrying no tag of any kind**, including the load-bearing append-only correction sentence about Section 22.4. METHODOLOGY Section 11 requires one tag per sentence and zero untagged sentences, and R22's prescribed route explicitly required `[WITNESSED]` to be present. Both the Status claim and the register's CLOSED disposition are false on the bytes that carry them.
- **Disposition:** Tag all eight narrative sentences. Supply `[WITNESSED: seat, round]` on every claim about what R22 seats found, since those are precisely non-producer-verified claims. Either supply `[TESTED: test_id]` citing shipped test IDs or remove the claim that probes verify the repairs. Re-emit group 4 with disposition `OPEN` in the R23 index rather than inheriting `CLOSED`.
- **Cross-reference:** R22 group 4 (F-S01-63-05 / F-S02-63-02 / F-S04-63-03 / F-S04-63-04, 3/4 mutawatir); METHODOLOGY Section 11; F-S04-64-11 (no gate enforces this).

### F-S04-64-04 [HIGH] -- Section 0.1 restates an FB-7b status that contradicts the row it names as single source of truth

- **Locus:** `xz_protocol_v0_64.md` line 18 (Section 0.1) versus line 771 (Section 25 FB-7b row).
- **Substance:** Section 0.1 states that FB-7b status is recorded in the Section 25 row as "single source of truth; no duplicate rationale maintained here," and then in the next sentence duplicates it: "Current status: PENDING RE-CARRY on v0.62 bytes." The Section 25 row reads "RESOLVED v0.31; PENDING RE-CARRY v0.64." The document therefore both forbids the duplication and commits it, and the duplicate disagrees with the original by two versions. This is a substrate-of-record uniqueness violation compounded by a cross-layer contradiction.
- **Disposition:** Delete the duplicated status sentence from Section 0.1, leaving only the pointer, and let gate [2g] continue to assert the PENDING RE-CARRY token against the Section 25 row alone. If the token must remain in Section 0.1 for [2g] to pass, add a version-parity gate binding the two loci.
- **Cross-reference:** Boundary item 35 ([2g] structurally forbids FB-7b resolution); skill standing rule 5 (substrate-of-record uniqueness); boundary item 29.

### F-S04-64-05 [HIGH] -- The FB-7b row, declared the full carrying-seat trajectory, stops four rounds short

- **Locus:** `xz_protocol_v0_64.md` line 771, Section 25 FB-7b row, "Post-v0.31 note."
- **Substance:** Section 0.1 designates this row as the record of "the full carrying-seat trajectory." The row enumerates rounds through "R18 (v0.59)" and then stops. R19 (v0.60), R20 (v0.61), R21 (v0.62) and R22 (v0.63) are absent, including R22's 4/4 HALT which the v0.64 entry itself reports. A reader following the document's own routing instruction to the single source of truth receives a trajectory that ends before the four most recent rounds.
- **Disposition:** Append R19 through R22 to the row with verdicts and Class A characterization, matching the existing per-round format. Add a build gate asserting that the highest round number named in the FB-7b row equals the round number named in the current amendment entry minus one.
- **Cross-reference:** F-S04-64-04 (same locus pair); R22 group 3, which established the pattern of a body section lagging an entry claim.

### F-S04-64-06 [HIGH] -- Narrative count-list decoupling, at a surface v0.63 claimed retired

- **Locus:** `xz_protocol_v0_64.md` Section 27, v0.64 entry narrative, tagging clause.
- **Substance:** The narrative reads "four-scribe tagging not correctly deployed (F-S02-63-02/F-S04-63-03/F-S04-63-04, 3/4)". The three enumerated IDs span two seats (S02, S04), not three; the fourth member of the group, F-S01-63-05, is omitted; and the COMPUTED register bracket for the same group emits "[3-seat / 4-finding convergence: F-S01-63-05 / F-S02-63-02 / F-S04-63-03 / F-S04-63-04]". The count claimed is unsupported by the enumeration beside it, which is the CI-2 crystallographic projection constraint, and it diverges from the code-generated bracket in the same entry. The other four narrative clusters were checked and are internally consistent. Separately, the v0.63 entry claimed "narrative seat/finding count claims removed from entry (only COMPUTED register brackets retained)"; v0.64 reintroduces five such clusters. This is absorption-induced regression at a surface R22 recorded as closed.
- **Disposition:** Either delete the narrative citation clusters entirely, restoring the v0.63 commitment and letting the COMPUTED register carry all counts, or generate them from the index so they cannot drift. Do not hand-maintain them.
- **Cross-reference:** CI_METHODOLOGY CI-2 and CI-3 (I1 count-list coupling); R22 unique finding F-S04-63-05 (narrative count survived, HIGH, CLOSED).

### F-S04-64-07 [HIGH] -- Noted-array finding IDs are neither format-validated nor uniqueness-checked, unlike findings[]

- **Locus:** `xz_protocol_register_gen.py`, noted-findings validation loop (lines ~141--153) versus findings[] loop (lines ~70--86).
- **Substance:** Records in `findings[]` are checked against `FINDING_ID_RE` and against a duplicate set. Records in `unique_findings_noted[]` are checked for presence, severity, disposition, `substance`, `convergence_group`, and (new at v0.64) `seat` -- but never for ID format or ID uniqueness. Probe N3 (`finding_id` = "XX-BOGUS") is accepted and the malformed ID is emitted verbatim into the shipped register. Probe N4 (a noted ID duplicating a grouped ID) is accepted, allowing the same finding to appear twice in one register under two dispositions. The v0.63 entry claimed noted-array validation would be brought to parity with findings[]; parity is now close but incomplete on exactly these two checks.
- **Disposition:** Apply `FINDING_ID_RE` to noted `finding_id`, and add each noted ID to the same `all_finding_ids` set used by the findings[] loop so cross-array duplicates raise. Add probes N3 and N4 to the shipped adversarial suite with real test IDs so a future `[TESTED:]` tag can cite them.
- **Cross-reference:** R22 group 2 (noted-array repair); probe K / K2 lineage; F-S04-64-01 (same generator, same silent-default pattern).

### F-S04-64-08 [HIGH] -- The ASSERTED-fraction metric counts tags, not text, understating dead space roughly fourfold

- **Locus:** `build.py` lines 507--513, gate [9c] tag census; METHODOLOGY Section 1; CI_METHODOLOGY CI-4 and F-CI-2.
- **Substance:** The gate computes ASSERTED fraction as `asserted_count / (computed_count + external_count + asserted_count)`, reporting 1/15 = 6.7% for v0.64. That arithmetic treats one `[ASSERTED]` tag governing a 1616-character LLM-authored narrative as equal in weight to each of fourteen `[COMPUTED]` tags on code-generated text. Measured by character coverage against the three generator outputs, the v0.64 entry is 4099 of 5721 characters code-generated and **1622 characters (28.4%) LLM-authored**. CI-4 sets a target of under 15% and F-CI-2 declares the architecture complexity-increasing if the fraction does not decrease. As instrumented, the metric can be driven arbitrarily low by adding `[COMPUTED]` tags or by consolidating narrative under a single `[ASSERTED]` tag, neither of which reduces dead space. F-CI-2 is not falsifiable as currently measured.
- **Disposition:** Redefine the metric as character coverage: total entry characters minus the summed lengths of verbatim generator outputs, divided by total entry characters. Emit both numbers in gate [9c]. Restate the historical series under the new definition before comparing against the under-15% target.
- **Cross-reference:** CI_METHODOLOGY CI-4, F-CI-2, F-CI-6R; METHODOLOGY Section 1 ("ASSERTED fractions declining from 30% to 8%"); prediction P6.

### F-S04-64-09 [MEDIUM] -- Gate-count claim recurs one round after closure: 253 claimed, 252 observed

- **Locus:** `AUDIT_CONTEXT.txt`, "Build status" block, line 3.
- **Substance:** AUDIT_CONTEXT states "build.py: 253 PASS, 0 FAIL." Direct execution in a fully green environment produces 252 PASS lines and 0 FAIL, deterministically across repeated runs. R22 group 5 recorded the identical class (258 claimed, 257 observed) at MEDIUM with the disposition "count by tool," and the v0.64 entry emits that group as CLOSED with the repair clause "(4) [COMPUTED: build.py gate count] gate count verified by tool." The off-by-one recurred at the same locus one round after the tool-counting repair was claimed.
- **Disposition:** Generate the AUDIT_CONTEXT build-status block from `build.py` output rather than transcribing it, or drop the numeric claim and cite the exit code. Note that the claim lives in the dispatch packet, not the protocol, so no protocol gate can catch it -- the dispatch itself needs a generation step.
- **Cross-reference:** R22 group 5 (F-S02-63-04 / F-S04-63-08); prediction P14.

### F-S04-64-10 [MEDIUM] -- `[ASSERTED]` is not a canonical four-scribe tag, yet it is the entry's only narrative tag

- **Locus:** `xz_protocol_v0_64.md` v0.64 entry, first tag; `build.py` line 509.
- **Substance:** METHODOLOGY Section 11 defines exactly four tags: `[COMPUTED: scribe]`, `[TESTED: test_id]`, `[WITNESSED: seat, round]`, `[DISCLOSED]`. `[ASSERTED]` is CI v0.1/v0.2 vocabulary that the four-scribe discipline was designed to replace, and the discipline's stated endpoint is that every unverifiable claim carries `[DISCLOSED]` so that the only remaining Class A surface is the tagging itself. The entry opens with `[ASSERTED]` and the build gate's census is constructed on the superseded vocabulary, so the gate cannot observe the canonical set.
- **Disposition:** Replace the entry's `[ASSERTED]` with per-sentence canonical tags. Update gate [9c] to census the four canonical tags and to report untagged-sentence count as a first-class number.
- **Cross-reference:** METHODOLOGY Section 11; F-S04-64-03; F-S04-64-08.

### F-S04-64-11 [MEDIUM] -- No gate enforces the tagging discipline, which is why the class fix could be claimed without landing

- **Locus:** `build.py` -- absence; searched for `WITNESSED`, `TESTED`, `scribe`, and untagged-sentence logic, zero occurrences.
- **Substance:** The four-scribe tagging discipline is designated the class fix for a sixteen-round Class A trajectory. It is enforced by no gate. Gate [9c] validates that `[COMPUTED: build.py [section]]` references resolve and that `[COMPUTED: sha256sum file]` files ship, but nothing asserts zero untagged sentences, `[WITNESSED]` presence, or `[TESTED]` test-ID resolution. CI_METHODOLOGY Section 0.4 states the program's own diagnosis: gated claims stay clean, ungated prose claims carry Class A every round. The class fix was shipped ungated and duly failed to land, exactly as that diagnosis predicts.
- **Disposition:** Add gate [9g]: parse the current entry's narrative paragraph into sentences, assert every sentence matches one of the four canonical tags, assert `[WITNESSED:]` count is at least one whenever the entry makes claims about prior-round seat findings, and assert every `[TESTED: id]` resolves to a test function present in a shipped suite.
- **Cross-reference:** CI_METHODOLOGY Section 0.4; F-S04-64-03; F-S04-64-10.

### F-S04-64-12 [LOW] -- Generator emits double sentence terminators in the NOTED block

- **Locus:** `xz_protocol_register_gen.py` line ~282; shipped effect in the v0.64 entry NOTED block, all three items.
- **Substance:** The noted emission is `f"- [{fid}] {sev}: {substance}. Disposition: ..."`. Index `substance` values already end in a period, so the register ships "Disclosed in AUDIT_CONTEXT.." and two further double-period artifacts. Cosmetic, but it sits inside a `[COMPUTED: generate_register]` surface that the methodology holds out as the high-fidelity layer.
- **Disposition:** Strip a trailing period from `substance` before concatenation, or require index `substance` values to be unpunctuated and validate that.
- **Cross-reference:** F-S04-64-01 (same generator, same emission path).

### F-S04-64-13 [LOW] -- Build status is environment-conditional and the condition is undisclosed

- **Locus:** `AUDIT_CONTEXT.txt` "Build status"; `build.py` pytest-presence gates.
- **Substance:** In an environment without `pytest` installed, `build.py` reports 249 PASS / 2 FAIL and exits 1. The "253 PASS, 0 FAIL" claim therefore carries an unstated environment precondition. Boundary item 7 discloses that the execution environment is unsealed, but the specific dependency that flips the build from GREEN to FAILED is not named where the claim is made.
- **Disposition:** State the precondition in the AUDIT_CONTEXT build-status block, or have `build.py` emit the pytest-presence result as a distinguished environment banner rather than as two ordinary gates.
- **Cross-reference:** Boundary item 7; boundary item 11 (fresh-execution non-reproducibility); boundary item 28.

### F-S04-64-14 [HIGH] -- Seat identity mismatch: dispatched Gemini 3.1 Pro, executed Claude Opus 5

- **Locus:** `DISPATCH.txt` header versus this report's executing instance.
- **Substance:** DISPATCH.txt names the S04 family as Gemini 3.1 Pro. Execution was by Claude Opus 5. The R23 seat lattice as designed distributes four distinct model families across four seats; if other seats were dispatched as designed, R23's mutawatir convergence counts will be computed over a seat set whose actual family distribution differs from the recorded one. Axiom A-X3 (model non-collusion) is a claim about family independence and is weakened by any undisclosed family substitution.
- **Disposition:** Record the executing family, not the dispatched family, in the R23 findings index `seat_families` map. Recompute any two-family carry claim against executing families only.
- **Cross-reference:** F-S01-63-07 at R22 (identical class, MEDIUM, NOTED); METHODOLOGY Section 5 seat table; axiom A-X5 (dispatch integrity).

### F-S04-64-15 [HIGH] -- Producer-family seat: this report cannot discharge Bearer 5

- **Locus:** `AUDIT_CONTEXT.txt` ("Producer: Claude Opus 4.6 -- BARRED") versus this executing instance (Claude Opus 5, Anthropic).
- **Substance:** The producer and this auditor are the same vendor family, one generation apart. Standing rule 7 of the canonical audit methodology excludes the producer instance from the auditor pool, and Bearer 5 requires two **non-producer** families to return non-HALT on the same bytes. This seat's verdict is HALT, so no false clearance results, but the structural point stands independently of the verdict: had this seat returned non-HALT, that non-HALT would have carried no Bearer 5 weight. The findings above retain full evidential weight under the "no advantage from world" principle -- and, per METHODOLOGY Section 5, defects surfaced despite producer-family architectural similarity are the producer's systematic misses rather than seat artifacts.
- **Disposition:** Re-dispatch the S04 cell to a genuinely non-producer family before computing R23 convergence. Treat this report as an unnumbered supplementary advisory seat rather than as the S04 lattice cell.
- **Cross-reference:** Skill standing rule 7 (cross-vendor rotation); axiom A-X3; Bearer 5; boundary items 18, 19, 34.

### F-S04-64-16 [MEDIUM] -- The S04 trial condition was not reproduced

- **Locus:** `METHODOLOGY.txt` Section 5, seven-Bilals seat table, S04 row.
- **Substance:** The canonical seat table assigns S04 the trial "no code execution, textual only," whose stated value is that reading the code surfaces spec-implementation gaps that running the code does not reveal. This seat executed. The findings are stronger in evidence tier, but R23 has lost the reading-only cell, and any gap that only careful reading would have caught is unexamined this round. The methodology's design is that each seat's limitation is the condition under which its findings have value; removing the limitation removes that value.
- **Disposition:** Either re-dispatch a textual-only S04 cell, or amend the METHODOLOGY seat table to describe trials in terms the dispatch can actually enforce, since seat capability is not controllable from the packet.
- **Cross-reference:** METHODOLOGY Section 5; F-S04-64-14; F-S04-64-15.

**Severity ledger: 0 CRITICAL / 10 HIGH / 4 MEDIUM / 2 LOW.**

---

## S7. Barzakh self-check

Every finding was put to the three questions before entry.

**Who is your Lord? (Authority.)** F-S04-64-01, -02, -03, -06, -07, -08, -09, -12, -13 are Tier 1:
each rests on tool output executed in this session -- generator invocation, mutation probes,
character counts, byte-offset arithmetic, build output. F-S04-64-04 and -05 are Tier 1 by grep on
shipped bytes. F-S04-64-10 and -11 are Tier 1 by absence-search, which is the weaker form of Tier 1
and is flagged as such. F-S04-64-14, -15, -16 are Tier 1 on the dispatch text and self-report.

One premise is not Tier 1. F-S04-64-02 relies on the v0.63 entry having previously sat after the
Provenance footer. No held v0.63 bytes were supplied. The premise is taken from R22_TRIAGE
(Tier 2) **and** from the v0.64 entry's own repair clause, which states the entry was moved
(Tier 1 on the artifact's admission). The seal-divergence arithmetic is Tier 1 given that premise.
Held v0.63 bytes would convert the whole finding to Tier 1.

**What is your religion? (Methodology.)** L1 and L4 findings carry executed evidence, meeting the
Tier 1 standard those layers require. L3 findings carry byte-grep evidence. L5's finding carries
computed hashes on a documented premise. L6's findings carry census arithmetic and absence-search.
No finding is admitted at a tier below its layer's standard.

**Where does this come from? (Lineage.)** F-S04-64-03 is recurrent (R22 group 4); the repair
failed because it was prescribed as prose discipline and shipped ungated -- see F-S04-64-11.
F-S04-64-06 is recurrent (F-S04-63-05); the repair failed because the narrative counts were
hand-maintained rather than generated. F-S04-64-09 is recurrent (R22 group 5); the repair failed
because the claim lives in the dispatch packet, which no protocol gate covers. F-S04-64-14 is
recurrent (F-S01-63-07). The remaining findings are novel at this locus.

No finding failed all three questions. None set aside.

---

## S8. Prediction scorecard

| # | Prediction | Result | Evidence |
|---|---|---|---|
| P1 | CI-1R PASS byte-exact | **CONFIRMED** | generator output is a verbatim substring of the entry |
| P2 | Probe J rejects via validator, not crash | **CONFIRMED** | ValueError raised, no UnboundLocalError |
| P3 | Section 22.4 exists (grep A-X1) | **CONFIRMED** | line 726, five axioms + Sidrat clause |
| P4 | v0.64 entry before Provenance footer | **CONFIRMED** | 417122 < 422846 |
| P5 | Append-only correction present | **CONFIRMED** | v0.64 entry states the correction; v0.63 entry unedited |
| P6 | ASSERTED < 15% | **FALSIFIED** | 28.4% by character coverage; 6.7% only under a tag-count metric (F-S04-64-08) |
| P7 | Class A only in self-referential surface | **FALSIFIED** | F-S04-64-01 (L1/L4), -02 (L5), -07 (L4) |
| P8 | Count-list invariant holds | **FALSIFIED** | narrative cluster claims 3/4 over 2 seats (F-S04-64-06) |
| P9 | Append-only holds, 64/64 seals | **CONFIRMED with caveat** | 64 seals recompute; anchor derivation is self-referential (F-S04-64-02) |
| P10 | Code layer clean, 186 GREEN | **PARTIALLY CONFIRMED** | 186 GREEN, but two live generator defects (F-S04-64-01, -07) |
| P11 | Packet 19/19 OK | **CONFIRMED** | rc=0 |
| P12 | Extraction snippet works verbatim | **CONFIRMED** | 17 files, then 19/19 OK |
| P13 | Noted seat validation rejects "S99Z" | **CONFIRMED** | ValueError raised |
| P14 | Gate count matches tool | **FALSIFIED** | 253 claimed, 252 observed |
| P15 | H = 1.0 continues | **CONFIRMED** | Class A present at R23; 17/17, Laplace P(R24) = 18/19 = 0.9474 |

Scorecard: 9 confirmed, 1 confirmed with caveat, 1 partial, 4 falsified. All fifteen were
dispatched at HIGH or MEDIUM confidence; the four falsifications are the round's information.

---

## S9. Bearer assessment (BSSG three-valued logic)

| Bearer | v0.64 status | Evidence |
|---|---|---|
| 1. Append-only integrity | **UNKNOWN** | 64/64 seals recompute and PRIOR_HISTORY derives, but the derivation rebuilds every prior level from current bytes; F-S04-64-02 shows the v0.63 anchor changed under the R22 repair. No held bytes, no external anchor. Not FALSE -- nothing shows corruption. Not TRUE -- nothing could. |
| 2. Code-layer correctness | **FALSE** | 186 GREEN, but F-S04-64-01 ships an empty load-bearing field in the `[COMPUTED]` register and F-S04-64-07 admits malformed and duplicate IDs. Both are live on shipped bytes. |
| 3. Defect-surface narrowing | **FALSE** | R22 recorded zero code-level Class A and predicted continued upward migration. R23 finds code-level Class A again. The surface did not narrow; it re-broadened downward. |
| 4. Goedel confinement | **FALSE** | Class A is present in the code layer (F-S04-64-01, -07), the temporal layer (F-S04-64-02), and cross-layer prose (F-S04-64-04, -05, -06), not only in the self-referential surface. **This is the round's key question, and the answer is no.** |
| 5. Cross-vendor witness | **FALSE** | This seat HALTs, and per F-S04-64-15 it is producer-family and could not have discharged this bearer even had it cleared. |
| 6. Axiom disclosure | **TRUE** | Section 22.4 ships with A-X1 through A-X5 and the Sidrat clause, byte-verified at line 722, consistent with METHODOLOGY Section 9. **This bearer flips TRUE at v0.64, as predicted.** |
| 7. Methodology verification | **FALSE** | Tagging discipline not deployed (F-S04-64-03), unenforced by any gate (F-S04-64-11), and the CI-4 metric is not measuring what it names (F-S04-64-08). Not UNKNOWN: Layer 6 was audited and the answer is negative. |
| 8. The furqan | **UNKNOWN** | Lead's judgment. Given, not derived. |

**State: 1 TRUE, 5 FALSE, 2 UNKNOWN.**

Composition against v0.63 (3 TRUE / 3 FALSE / 2 UNKNOWN): Bearer 6 gained, Bearers 1, 2, 3 lost.
Bearer 1 moved TRUE to UNKNOWN not because evidence degraded but because this seat holds no prior
bytes and found the derivation to be self-referential -- an honest downgrade of confidence rather
than a discovery of corruption. Bearers 2 and 3 moved TRUE to FALSE on new executed evidence.

The honest summary of the round: **the structural repairs landed and the axioms landed; the
methodology repair did not, and the code layer that R22 declared clean is not.**

---

## S10. Verdict

> **Verdict: HALT-AND-RETURN-TO-PRODUCER (advisory).**
>
> Severity ledger: 0 CRITICAL / 10 HIGH / 4 MEDIUM / 2 LOW.
>
> **Does v0.64 achieve Goedel confinement (Bearer 4)? No.**
>
> Confinement requires that the only Class A live in the self-referential surface. Three findings
> sit outside it: the register generator reads a field the index does not supply and silently
> ships empty defect descriptions (F-S04-64-01, Layer 1/4); the noted-array admits malformed and
> duplicate finding IDs into the shipped register (F-S04-64-07, Layer 4); and the R22 entry
> relocation re-anchored the v0.63 sealed surface with no gate able to detect it (F-S04-64-02,
> Layer 5). Bearer 4 remains FALSE. Bearer 6 flips TRUE.

**Recommendation.** Repair in this order, because the order matters:

1. **F-S04-64-01 and F-S04-64-07** first. They are code, they are small, and until they are fixed
   the confinement question cannot even be asked cleanly. Ship the four new probes (N3, N4, S1, S2)
   as real test IDs in the adversarial suite in the same change.
2. **F-S04-64-11** next: gate the tagging discipline. Then **F-S04-64-03** becomes mechanically
   enforceable rather than a prose commitment that has now failed to land twice.
3. **F-S04-64-08**: redefine the ASSERTED metric before it is cited again. The current definition
   makes the program's central complexity claim unfalsifiable, which is the one thing this
   methodology exists to prevent.
4. **F-S04-64-04, -05, -06**: prose and cross-reference repairs, generated rather than hand-maintained.
5. **F-S04-64-02**: disclose in the v0.65 entry and add the boundary item. This one cannot be
   "fixed" -- it can only be disclosed, which is what the Sidrat clause is for.

**On the shape of the round.** R22 predicted that one more round of repair would complete the
migration to the Goedel surface. That prediction is not yet falsified as a trajectory claim, but
it is falsified as a v0.64 claim, and for a specific and repeatable reason: **every defect that
recurred this round recurred at a locus no gate covers.** Tagging: ungated. Narrative counts:
ungated. Dispatch gate count: outside the protocol entirely. The generator's `surface` field:
ungated because `.get` supplied a default. The program's own diagnosis in CI_METHODOLOGY 0.4 --
gated claims stay clean, ungated claims carry Class A every round -- held at R23 without exception.
Confinement will arrive when the self-referential surface is the last ungated surface, and it is
not yet the last.

**Cross-vendor recommendation.** This seat is producer-family (Claude auditing a Claude-produced
artifact). Under standing rule 7, R23 needs the S04 cell re-dispatched to a non-producer family
before convergence is computed, and Bearer 5 needs two non-producer families returning non-HALT
on the same bytes. Neither is satisfied by this report.

---

## Provenance

Executed 2026-08-17 in a Linux sandbox with CPython 3.12.3 and pytest 9.1.1.
All findings derive from the ten dispatched packet files as shipped. No prior-round memory was
consulted under the FRESH discipline. Fifteen dispatched predictions were scored before the
verdict was written.

Artifact digests (SHA-256, first 16 hex): protocol `c6d911a5422d8faf`, build.py `d415bb4ffc945f4c`,
register_gen.py `9a8253b4ba424aa0`, HISTORY.sha256 `d1d5b969e7b4cbfc`.

*Seat S04, Round 23, advisory. Verdict HALT. Bearer 4 FALSE, Bearer 6 TRUE.*

---

# Bismillah ir-Rahman ir-Rahim
