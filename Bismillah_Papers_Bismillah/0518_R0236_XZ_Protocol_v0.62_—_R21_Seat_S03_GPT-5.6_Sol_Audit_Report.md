# Bismillah ir-Rahman ir-Rahim

# R0236 -- XZ Protocol v0.62 — R21 Seat S03 GPT-5.6 Sol Audit Report

**Chronological Index:** 518 of 995  
**Date:** 2026-08-16  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v062_R21_S03_GPT_REPORT.md  
**Source Format:** md  
**SHA-256:** `c0dff238cea69218f1a8fae5850b38ef8f654bf2ed1c8ce4a527a503efadfc2a`  

---

## R0236 · XZ Protocol v0.62 — R21 Seat S03 GPT-5.6 Sol Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v062_R21_S03_GPT_REPORT.md
- source_format: md
- text_sha256: c0dff238cea69218f1a8fae5850b38ef8f654bf2ed1c8ce4a527a503efadfc2a

# XZ Protocol v0.62 — R21 Seat S03 GPT-5.6 Sol Audit Report

**Dispatch:** R21 / v0.62 / Seat S03 FRESH
**Model:** GPT-5.6 Sol
**Role:** ADVERSARIAL ADVISORY — self-disqualified from carry
**Framework:** Structural Revelation + Seven-Layer Structural Honesty
**Audit date:** 2026-08-16
**Verdict:** **ADVISORY HALT — Class A present**
**Key question:** **NO. v0.62 does not break the R7–R20 Class A streak. The recurrence extends through R21: 15/15 rounds with Class A present.**

---

## S0: Identity, mode, execution surface

I executed this seat as a fresh adversarial audit against only the shipped R21 packet and the files deterministically extracted from `EXECUTABLE_PACKET.txt` using the dispatch-provided extraction recipe. No prior held bytes were used as evidence. The producer is Claude Opus 4.6 and is barred from carry by the dispatch; this report therefore treats all producer statements as hypotheses until reproduced from shipped bytes.

Shipped archive contents:

- `AUDIT_CONTEXT.txt`
- `BOUNDARIES.txt`
- `CI_METHODOLOGY.txt`
- `DISPATCH.txt`
- `EXECUTABLE_PACKET.txt`
- `FINDINGS_INDEX.txt`
- `METHODOLOGY_v2.txt`
- `PROTOCOL_v062.txt`
- `R20_REPORTS.txt`
- `R20_TRIAGE.txt`

The executable packet extracted 15 execution files plus the protocol-side working copies required by the dispatch. Runtime: Python 3.13.5.

Primary audit lenses used:

1. Code execution and hash reproduction.
2. CI-1R deterministic register reproduction.
3. Cross-layer claim-to-byte comparison.
4. Mutation-based adversarial probing of CI v0.3.2.
5. Temporal seal and append-only verification.
6. Dispatch/methodology self-audit.
7. Boundary sufficiency and disclosure review.

---

## S1: Staging and byte verification (baseline green before attacking)

### S1.1 Dispatch-prescribed extraction

The exact extraction recipe from `AUDIT_CONTEXT.txt` was used against `EXECUTABLE_PACKET.txt`, followed by:

```text
cp PROTOCOL_v062.txt xz_protocol_v0_62.md
cp FINDINGS_INDEX.txt r20_findings_index.json
cp BOUNDARIES.txt xz_protocol_boundaries.json
python3 build.py
pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py
sha256sum -c PACKET_SHA256SUMS
```

### S1.2 Baseline results

| Surface | Dispatch claim | Executed result | Status |
|---|---|---|---|
| `build.py` | `248 PASS, 0 FAIL` | **BUILD FAILED: 35 errors** | **REFUTED** |
| pytest | `186 GREEN` | **186 passed** | CONFIRMED |
| packet checksums | `19/19 OK` | **15/19 mismatched; 4/19 OK** | **REFUTED** |
| current protocol file | included in checksum set | checksum OK | CONFIRMED |
| findings index | included in checksum set | checksum OK | CONFIRMED |
| boundaries JSON | included in checksum set | checksum OK | CONFIRMED |
| trust-roots JSON file bytes | included in checksum set | checksum OK | CONFIRMED |

The build failure is not a test failure. The six test suites execute and pass 186/186. The build fails because the executable code/test bytes embedded in `EXECUTABLE_PACKET.txt` do not match the digests carried by `PACKET_SHA256SUMS`, the body digest citations, and the trust-roots manifest digest.

### S1.3 Packet checksum mismatch census

`PACKET_SHA256SUMS` contains 19 members. Four match and fifteen do not.

**Matching:**

- `r20_findings_index.json`
- `xz_protocol_boundaries.json`
- `xz_protocol_trust_roots_PUBLIC.json`
- `xz_protocol_v0_62.md`

**Mismatching:**

| File | Expected prefix | Actual prefix |
|---|---:|---:|
| `HISTORY.sha256` | `ee1c133e98883a1f` | `018f4c44c034d298` |
| `build.py` | `a8c4b1d820500747` | `cf1491eefd26d07c` |
| `test_xz_protocol_adversarial.py` | `fa48de505215c383` | `1359027e77309e99` |
| `test_xz_protocol_condition_a.py` | `67813d1843c7a2ff` | `2147665fae6386c6` |
| `test_xz_protocol_control_graph.py` | `240a82fe09c43565` | `0d13aca7d3f0210c` |
| `test_xz_protocol_kernel.py` | `9a29f1253fda9112` | `a428c1bb1f7a1791` |
| `test_xz_protocol_source_frame.py` | `10f39aa0bf2b6da1` | `a7453fe782977ead` |
| `xz_protocol_condition_a.py` | `5795a4f7527b6301` | `3dee5e739366c24f` |
| `xz_protocol_control_graph.py` | `e7bf22e035422544` | `94906af72407a650` |
| `xz_protocol_kernel.py` | `5323f22c3713ec34` | `75dcd572255d0b1d` |
| `xz_protocol_phase_a_intervals.py` | `72bfbfc73844a773` | `aa2bb938f95f72b8` |
| `xz_protocol_phase_a_m3.py` | `82d7e196254632e8` | `14efb1ce35da998a` |
| `xz_protocol_phase_a_tests.py` | `1ef31a3922a275c8` | `96c07ce5b645f2bc` |
| `xz_protocol_register_gen.py` | `20586393bb95fe07` | `3984b2cbbfed8bae` |
| `xz_protocol_source_frame.py` | `77b9eced19869579` | `a43ba44cbcbfe6d1` |

The expected packet hashes for multiple code files are also the stale hashes cited in the protocol body, while the extracted executable files contain different v0.62 bytes. This is a coherent stale-manifest/body-digest packaging failure, not a single corrupted member.

### S1 conclusion

**Baseline green is false on shipped bytes.** This alone prevents the dispatch from satisfying its own staging precondition.

---

## S2: CI-1R reproduction

I loaded the shipped `r20_findings_index.json`, executed `generate_register(index_path, "0.62")` from the shipped `xz_protocol_register_gen.py`, and compared the generated output to the v0.62 amendment entry.

Results:

- Generator execution: PASS.
- Generated register length: 1,919 bytes/characters in the decoded text surface.
- Generated register appears byte-for-byte as a contiguous substring of the shipped v0.62 protocol entry: **YES**.
- Four CLOSED register items reproduce exactly.
- The one NOTED group reproduces exactly.

**CI-1R: PASS.**

Important limitation: CI-1R proves that the shipped register is the deterministic output of the shipped index and generator. It does **not** prove that the generator's closure claims are true. Several reproduced `[COMPUTED: generate_register]` lines are themselves overclaims because the underlying architecture does not fully implement the described repair.

---

## S3: R20 finding discharge

| R20 surface | v0.62 claimed disposition | R21 executed result | Discharge |
|---|---|---|---|
| Surface 1 — M3 receipt enforcement + structural validation | CLOSED via CI v0.3.2 | Receipt is required for mixed distributions, but validation remains string containment (`dist_str in receipt`); junk and negated receipts containing the canonical phrase are accepted | **NOT DISCHARGED** |
| Surface 2 — authoritative seat count | CLOSED via CI v0.3.2 | Generator uses `findings_by_id[fid]["seat"]`; ID-prefix changes do not control the count | **DISCHARGED** |
| Surface 3 — noted-finding dangling bypass | CLOSED via CI v0.3.2 | `findings[]` dangling non-existent groups are rejected, but `unique_findings_noted` can carry arbitrary/dangling `convergence_group` values and fake IDs without validation | **NOT DISCHARGED; migrated path** |
| Surface 4 — bidirectional membership parity | CLOSED via CI v0.3.2 | One direction is enforced (`group list -> scalar`); the reverse (`scalar -> listed membership`) is not. Removing a member from a group while retaining its scalar group is accepted | **NOT DISCHARGED** |
| CI-8 source-ID fidelity | NOTED, with `source_finding_id` claimed added in v0.3.2 | Shipped index has **0/17** `source_finding_id` fields; generator does not read or validate the field | **NOT DISCHARGED** |

R20's seat-count defect is the one major target cleanly discharged. The other three v0.3.2 closure surfaces either recur directly or migrate into adjacent schema paths.

---

## S4: Amendment-entry audit

Every auditable v0.62 entry/front-matter claim was classified as **CONFIRMED**, **NOT VERIFIABLE**, or **REFUTED** against the shipped packet.

| # | Claim | Result | Evidence |
|---:|---|---|---|
| 1 | Document is v0.62 DRAFT CANDIDATE | CONFIRMED | protocol/front matter and code version stamps |
| 2 | R20 index contains 10 seats | CONFIRMED | 10 entries in top-level `seats` |
| 3 | R20 was 5 fresh + 5 continuous across named vendors/frameworks | NOT VERIFIABLE | raw R20 reports are explicitly not shipped; index encodes F/C seat labels but not complete vendor/framework evidence |
| 4 | 4 carrying HALT / 6 advisory HALT | CONFIRMED | index fields `carrying_halts=4`, `advisory_halts=6` |
| 5 | M2 was exhaustively proven 75/75 at S02C | NOT VERIFIABLE | asserted by triage/context; raw R20 S02C report/logs absent |
| 6 | VERSION-1 gate was sabotage-proven at all executing seats | NOT VERIFIABLE historically | R20 raw execution logs absent; current gate exists but has a decoy bypass (S5) |
| 7 | dangling `convergence_group` rejection exists | CONFIRMED for `findings[]` | mutation to group 999 raises `ValueError` |
| 8 | source distribution is load-bearing and emitted | CONFIRMED | generated register emits `Source distribution:`; stale distribution mutation rejects |
| 9 | PRIOR_HISTORY was cross-anchored to held v0.60 HISTORY | NOT VERIFIABLE externally | held v0.60 bytes do not ship; internal derivation passes |
| 10 | R20 triage identified M3, seat parser, CI-8, noted bypass, and parity surfaces | CONFIRMED against shipped triage | `R20_TRIAGE.txt` |
| 11 | Register item (1) is deterministic output | CONFIRMED | CI-1R |
| 12 | Register item (2) is deterministic output | CONFIRMED | CI-1R |
| 13 | Register item (3): noted-finding bypass is closed and ungrouped findings must be null | **REFUTED** | separate `unique_findings_noted` path accepts dangling/non-null group metadata |
| 14 | Register item (4): bidirectional membership parity is enforced | **REFUTED** | reverse-direction membership omission accepted |
| 15 | CI-8 source-ID issue remains NOTED | CONFIRMED | group 3 is NOTED in index/register |
| 16 | M3 receipt required on any mixed distribution | CONFIRMED | removing group-5 receipt rejects |
| 17 | Receipt validation is structural, exact canonical, “not substring matching” | **REFUTED** | code uses `if dist_str not in receipt`; junk and negated strings containing the phrase pass |
| 18 | Seat count comes from authoritative `findings[].seat` | CONFIRMED | generator and [10e] use seat field |
| 19 | `source_finding_id` field added for CI-8 literal resolution | **REFUTED** | 0/17 findings contain field; no generator logic references it |
| 20 | Bidirectional finding-group parity added | **REFUTED** | only group->scalar direction is complete |
| 21 | Noted-finding bypass removed | **REFUTED** | bypass persists through `unique_findings_noted` schema path |
| 22 | Boundary list contains 35 items | CONFIRMED | JSON count = 35; generated list = 35 |
| 23 | Current `PRIOR_HISTORY` value matches internal derivation | CONFIRMED | build [9b] passes derivation |
| 24 | Current amendment register count/list coupling holds | CONFIRMED | 4 parsed = 4 declared; 12 unique CLOSED-item IDs |
| 25 | ASSERTED fraction <15% | CONFIRMED | 1/8 = 12.5% |
| 26 | Terminal v0.62 line matches generator | CONFIRMED | `generate_terminal_line("0.62")` matches |
| 27 | Build baseline is 248 PASS / 0 FAIL | **REFUTED** | 35 build errors |
| 28 | Packet is 19/19 checksum-clean | **REFUTED** | 15 checksum mismatches |

The most consequential Level-3/Level-4 Iblis pattern is exact: the entry says a mechanism is “structural,” “bidirectional,” or “added,” while the shipped implementation is narrower or absent.

---

## S5: Exhaustive probe battery

### S5.1 Mutation methodology

Because the shipped baseline `build.py` is already red, it is impossible to truthfully classify a mutation as “passes the build” without first repairing the producer's package. I therefore did **not** manufacture a green baseline and call it shipped evidence. Instead:

- CI v0.3.2 generator mutations were executed directly against the shipped generator and index.
- Build-gate mutations were evaluated against the exact gate predicates in the shipped `build.py`.
- Unexpected acceptances are reported as architectural defects; where a full-build Class B label would require a green baseline, that limitation is stated explicitly.

### S5.2 Probe results — 30 generator/schema mutations

| # | Probe | Result | Interpretation |
|---:|---|---|---|
| 1 | Remove receipt from mixed group 5 | REJECT | M3 any-mixed requirement works |
| 2 | Flip source severity but keep stale receipt | REJECT | distribution phrase is load-bearing |
| 3 | Canonical distribution embedded in unrelated junk receipt | **ACCEPT** | structural receipt claim fails |
| 4 | Canonical distribution embedded in explicitly negated receipt | **ACCEPT** | semantic/structural receipt claim fails |
| 5 | Wrong-case distribution phrase | REJECT | exact case-sensitive phrase required |
| 6 | Valid changed distribution + updated receipt | ACCEPT | expected |
| 7 | Merge two findings' authoritative seat values | ACCEPT; emitted seat count changes | count is driven by `seat` field |
| 8 | Change finding-ID seat prefix while preserving authoritative seat | ACCEPT; seat count remains field-driven | seat repair works |
| 9 | Scalar `convergence_group=999` | REJECT | dangling group rejection works for findings[] |
| 10 | Scalar points to existing wrong group while still listed elsewhere | REJECT | group->scalar parity direction works |
| 11 | Remove one group member but retain its scalar group | **ACCEPT** | reverse parity absent |
| 12 | Put same finding in two groups, scalar matching later group | **ACCEPT** at generator | cross-group uniqueness absent in generator; build [10b] would catch regenerated duplicate register IDs if baseline were green |
| 13 | Duplicate `group_id` with disjoint members | **ACCEPT** | group-ID uniqueness absent |
| 14 | Add malformed fake noted finding ID | **ACCEPT** | noted ID regex/existence validation absent |
| 15 | Add noted finding with `convergence_group=999` | **ACCEPT** | noted dangling bypass persists |
| 16 | Duplicate a `unique_findings_noted` ID | **ACCEPT** | noted uniqueness absent |
| 17 | Invalid source severity `CRITICAL` | REJECT | severity validation works |
| 18 | Empty source severity plus crafted receipt | **ACCEPT** | non-empty source severity not enforced |
| 19 | Malformed group finding ID | REJECT | group ID regex works |
| 20 | Group finding absent from findings[] | REJECT | existence coupling works |
| 21 | Duplicate findings[] record ID | REJECT | findings[] uniqueness works |
| 22 | Duplicate ID inside one group | REJECT | intra-group uniqueness works |
| 23 | Invalid group disposition | REJECT | disposition enum works |
| 24 | Invalid group triage severity | REJECT | triage severity enum works |
| 25 | Noted finding missing `substance` | REJECT | required noted substance works |
| 26 | Duplicate top-level seat name while preserving list length | **ACCEPT** | audit-seat roster uniqueness not validated |
| 27 | Omit all `source_finding_id` fields | **ACCEPT** | field is not required |
| 28 | Add arbitrary bogus `source_finding_id` values | **ACCEPT; output unchanged** | field is ignored/not load-bearing |
| 29 | Reverse findings[] order | ACCEPT; deterministic output preserved | expected |
| 30 | Reverse convergence-group order | ACCEPT; closed groups sort deterministically | expected |

### S5.3 VERSION-1 gate attacks

The shipped gate computes the correct expected strings but checks only global presence in the entire pre-Section-27 body:

```text
check(expected_22_2 in body, ...)
check(expected_22_3 in body, ...)
```

Executed predicate probes:

| Mutation | Target gate result |
|---|---|
| Change Section 22.2 bound to v0.60, no decoy | FAIL — caught |
| Change Section 22.2 bound to v0.60 and insert `v0.1 through v0.61` elsewhere in body | **PASS — bypass** |
| Change Section 22.3 bound to v0.60 and insert `v0.38-v0.61` elsewhere in body | **PASS — bypass** |

Thus the VERSION-1 gate catches a simple stale token but does not establish that the **Section 22.2/22.3 loci** contain the expected values.

### S5.4 Entry ordering, seals, and packet probes

- Baseline amendment entries: 62; ascending: YES; unique: YES.
- Duplicate-current-version mutation: uniqueness predicate fails.
- `HISTORY.sha256`: 62 ENTRY lines, 62 unique ENTRY labels, one FULL_SECTION_27 line, one PRIOR_HISTORY line.
- Single-nibble change to an ENTRY seal is detected by the implemented byte-derived seal comparison.
- Duplicate `FULL_SECTION_27` line remains an acknowledged blind spot: build checks `any(exact_full_line)` but does not enforce FULL_SECTION_27 uniqueness. This is already disclosed as standing boundary #33, so it is **not a new finding**.
- `PACKET_SHA256SUMS` contains 19 members, excludes itself, and includes the findings index; self-entry/removal predicates are explicitly gated. The shipped package nonetheless starts with 15 digest mismatches.

### S5.5 Mutation conclusion

The battery confirms several genuine v0.3.2 improvements — mixed-receipt requirement, source-distribution coupling, findings[] dangling rejection, authoritative seat count, enum/ID validation — while falsifying the stronger claims of structural receipt validation, full bidirectional parity, noted-path closure, source-ID resolution, and locus-specific VERSION-1 enforcement.

---

## S6: Seven-layer traversal

### Layer 1 — Code execution

**FAIL overall.** pytest is 186/186 GREEN, but the mandatory build is red with 35 errors and packet checksum verification is 4/19, not 19/19.

### Layer 2 — Register verification

**PASS for CI-1R reproduction.** The shipped register is exactly generated from the shipped index. However deterministic reproduction faithfully reproduces several false closure statements; this is semantic failure above the reproduction layer, not a CI-1R mismatch.

### Layer 3 — Cross-layer consistency

**FAIL.** Code/test bytes disagree with packet hashes, body digest citations, and trust-root manifest data. The front matter claims `source_finding_id` was added, while the index and generator contain no operative implementation. CI version labels agree syntactically but the implemented semantics are narrower than claimed.

### Layer 4 — Adversarial probing

**FAIL.** Multiple invalid structural mutations are accepted, including junk/negated receipts, reverse membership loss, duplicate group IDs, malformed/dangling noted records, empty source severity with crafted receipt, and bogus ignored `source_finding_id` values.

### Layer 5 — Temporal integrity

**PARTIAL / FAIL overall.** The internal append-only entry chain is strong: 62/62 ENTRY seals match current protocol bytes; FULL_SECTION_27 matches; exactly one PRIOR_HISTORY line exists; internal PRIOR_HISTORY derivation succeeds. But the shipped `HISTORY.sha256` file itself does not match the packet checksum declared for it, so packet-level temporal binding is broken.

### Layer 6 — Methodology audit

**FAIL.** `AUDIT_CONTEXT.txt` says `build.py: 248 PASS, 0 FAIL`, `PACKET_SHA256SUMS: 19/19 OK`, and `source_finding_id field added`; all three are refuted or absent on shipped bytes. The methodology correctly predicts this failure class: producer claims about verification outstrip the mechanism.

### Layer 7 — Boundary disclosure

**FAIL for sufficiency.** The 35 standing boundaries are accurately enumerated, and boundary #33 honestly discloses the FULL_SECTION_27 uniqueness gap. But the current Class A surfaces — stale packet/build claim, absent source_finding_id implementation, substring receipt validation, incomplete reverse parity, and noted-path bypass — are not disclosed as residuals; they are claimed repaired.

---

## S7: Findings (six-element format)

Severity mapping used by the program: Class A = HIGH (byte-false claim), Class B = MEDIUM, Class C = LOW, Class E = INFORMATIONAL.

### F-S03-62-01 — HIGH (Class A): baseline-green and 19/19 packet claims are byte-false

- **Locus:** `AUDIT_CONTEXT.txt` Build status; `PACKET_SHA256SUMS`; protocol body digest/trust-root surfaces.
- **Substance:** The dispatch context asserts `build.py: 248 PASS, 0 FAIL` and `PACKET_SHA256SUMS: 19/19 OK`. Following the dispatch's own extraction and execution recipe produces `BUILD FAILED: 35 error(s)` and fifteen checksum mismatches. The executable code/test files are newer/different bytes than the hashes carried by the packet/body/trust-root surfaces.
- **Evidence:** Executed `python3 build.py`, canonical six-suite pytest, and `sha256sum -c PACKET_SHA256SUMS`. pytest = 186 passed; build = 35 errors; packet = 15 failures / 4 OK.
- **Recommendation:** Rebuild the packet atomically from one byte set: regenerate all normative digests, body citations, trust-root manifest digest, HISTORY/packet seals, and `PACKET_SHA256SUMS` only after executable bytes are final. Add a final package-from-scratch extraction test as a release gate.

### F-S03-62-02 — HIGH (Class A): `source_finding_id` “added for CI-8 literal resolution” is absent and non-operative

- **Locus:** protocol front-matter Status; `AUDIT_CONTEXT.txt`; R20 triage disposition; `r20_findings_index.json`; `xz_protocol_register_gen.py`.
- **Substance:** v0.62 claims the `source_finding_id` field was added for CI-8 literal resolution. The shipped index has 0/17 such fields. The generator contains no read, validation, or coupling logic for the field. Adding arbitrary bogus values leaves output unchanged; omitting the field entirely is accepted.
- **Evidence:** recursive grep finds `source_finding_id` only in prose describing the future/claimed repair, not in operative generator logic; field census = 0/17; mutation probes #27–28 both ACCEPT.
- **Recommendation:** Add `source_finding_id` to every findings[] record that needs literal source mapping; validate format, non-emptiness, source-report existence, and uniqueness; make CI-8 compare the source ID against shipped report bytes. Until then, retract “added/resolves” to NOTED/PENDING.

### F-S03-62-03 — HIGH (Class A): “structural, not substring” receipt validation still uses substring containment

- **Locus:** v0.62 entry register item (1), body repair (i), `xz_protocol_register_gen.py` receipt gate.
- **Substance:** The entry says receipt validation is structural and not substring-based. The implementation is `if dist_str not in receipt`, which is substring containment. A receipt may contain unrelated or explicitly negating prose so long as the canonical distribution phrase appears somewhere.
- **Evidence:** probe #3 accepted `UNRELATED PREFIX :: 1 HIGH, 1 MEDIUM :: UNRELATED SUFFIX`; probe #4 accepted `This is NOT an adjudication. 1 HIGH, 1 MEDIUM.`. Both should fail under the claimed structural semantics.
- **Recommendation:** Replace free-text receipt validation with a structured field, e.g. `adjudication_receipt.source_distribution` as a machine object/list compared for exact equality to the computed distribution. If free text is retained, narrow the claim to “requires verbatim canonical distribution substring.”

### F-S03-62-04 — HIGH (Class A): claimed bidirectional membership parity is only one-directional

- **Locus:** v0.62 register item (4), body repair (i), `xz_protocol_register_gen.py` cross-layer validation.
- **Substance:** The generator builds `fid_to_group` from group lists and checks that listed findings' scalar `convergence_group` equals the containing group. It never checks the reverse invariant: every finding with non-null scalar group must actually appear in that group's `finding_ids`. Removing a finding from a group while leaving its scalar unchanged is accepted.
- **Evidence:** probe #11 removes `F-S05-61-01C` from group 1 but leaves `findings[].convergence_group = 1`; generation ACCEPTS and emits a 5-seat/6-finding group. Probe #10 shows the implemented forward direction does reject an existing-but-wrong scalar for a still-listed finding.
- **Recommendation:** Enforce both directions explicitly: for each finding with `cg != null`, require exactly one group with that ID and require the finding ID to occur exactly once in that group's member list. Also enforce unique group IDs before building the membership map.

### F-S03-62-05 — HIGH (Class A): noted-finding bypass is not fully removed; separate noted path remains ungated

- **Locus:** v0.62 register item (3), body repair (i), `unique_findings_noted` validation in `xz_protocol_register_gen.py`.
- **Substance:** The entry claims ungrouped/noted findings must use `convergence_group=null` and any non-null dangling reference is rejected. That rule is applied to `findings[]` but not to the separate `unique_findings_noted` list. Noted entries can carry arbitrary group metadata, malformed/fake IDs, and duplicate IDs.
- **Evidence:** probe #14 malformed noted ID ACCEPT; #15 noted `convergence_group=999` ACCEPT; #16 duplicate noted ID ACCEPT. The generator ignores the dangling group field on this path.
- **Recommendation:** Eliminate the parallel noted schema or subject it to the same canonical finding validator as `findings[]`: ID regex, existence/source mapping, uniqueness, and `convergence_group is null` for ungrouped notes.

### F-S03-62-06 — MEDIUM (Class B): duplicate convergence-group IDs are accepted

- **Locus:** `xz_protocol_register_gen.py` group validation.
- **Substance:** Group IDs are collected into a set for dangling-reference checks but are never required to be unique. Two disjoint convergence groups can share the same `group_id`; after matching member scalars to that duplicated ID, generation succeeds.
- **Evidence:** probe #13 changes group 4's ID to 2 and its member's scalar group to 2; generation ACCEPTS with two distinct group records both identified as group 2.
- **Recommendation:** Reject duplicate `group_id` values before any membership processing. Assert `len(group_ids) == len(set(group_ids))`.

### F-S03-62-07 — MEDIUM (Class B): VERSION-1 gate is body-global, not Section-22-locus-bound

- **Locus:** `build.py` gate [10i].
- **Substance:** The gate claims to validate Section 22.2/22.3 bounds but checks only whether the expected strings occur anywhere in the pre-Section-27 body. A stale Section 22 value can pass if the current expected token is inserted elsewhere.
- **Evidence:** plain stale 22.2 mutation removes the only expected phrase and the predicate fails; stale 22.2 + body decoy phrase makes the predicate pass. Same result for 22.3.
- **Recommendation:** Parse and scope Section 22.2 and 22.3 separately, then assert the expected VERSION-1 value occurs exactly once in the correct subsection and stale alternatives are absent.

### Finding totals

| Severity | Count | IDs |
|---|---:|---|
| HIGH / Class A | **5** | F-S03-62-01 through F-S03-62-05 |
| MEDIUM / Class B | **2** | F-S03-62-06, F-S03-62-07 |
| LOW / Class C | 0 | — |
| INFORMATIONAL / Class E | 0 | — |

---

## S8: Barzakh self-check

| Finding | Q1 Authority | Q2 Methodology | Q3 Lineage | Gate |
|---|---|---|---|---|
| F-S03-62-01 | direct build/hash execution | Layers 1/3/6 | recurrent packaging/claim-vs-byte class | PASS |
| F-S03-62-02 | field census + code grep + mutation | Layers 3/4/6 | direct continuation of R20 CI-8 NOTED surface | PASS |
| F-S03-62-03 | executed receipt mutations | Layer 4 Structural Revelation | direct recurrence of R20 M3 receipt surface | PASS |
| F-S03-62-04 | executed membership mutation | Layer 4 cross-layer parity | direct continuation of R20 parity surface | PASS |
| F-S03-62-05 | executed noted-path mutations | Layers 3/4 | migration of R20 noted-bypass surface | PASS |
| F-S03-62-06 | executed schema mutation | Layer 4 | novel adjacent schema invariant | PASS |
| F-S03-62-07 | exact gate predicate + stale/decoy mutation | Layers 3/4 | recurrence of VERSION-bound gate-scope family | PASS |

No finding above depends on appearance-only reasoning. Each has byte or execution evidence and an explicit lineage classification.

---

## S9: Prediction scorecard

| Prediction | Result | Reason |
|---|---|---|
| P1: CI-1R PASS | **CONFIRMED** | generated register is byte-identical substring |
| P2: CI-8 `source_finding_id` resolves | **REFUTED** | field absent 0/17 and ignored by generator |
| P3: ASSERTED <15% | **CONFIRMED** | 1/8 = 12.5% |
| P4: If Class A, on CI v0.3.2 entry claims | **CONFIRMED** | structural receipt, bidirectional parity, noted closure, source-ID claim |
| P5: Count-list invariant holds | **CONFIRMED** | 4 parsed/4 declared; current brackets reproduce |
| P6: Append-only holds (62/62 seals) | **CONFIRMED** | 62 ENTRY seals match current protocol bytes |
| P7: Code layer clean (186 GREEN) | **CONFIRMED** | 186 passed |
| P8: Packet 19/19 OK | **REFUTED** | 15/19 mismatch |
| P9: M3 receipt on any mixed group now structural | **REFUTED** | any-mixed requirement works; “structural” validation does not |
| P10: Seat count from `findings[].seat` | **CONFIRMED** | executed mutations verify field authority |
| P11: VERSION-1 gate catches stale bounds | **REFUTED** as a locus guarantee | stale + body decoy bypasses gate |
| P12: Sections 22.2/22.3 at v0.61 | **CONFIRMED** | shipped text has expected tokens |
| P13: Bidirectional membership parity enforced | **REFUTED** | scalar->membership direction absent |
| P14: Noted-finding bypass removed | **REFUTED** | separate noted path still accepts dangling metadata |
| P15: H = 1.0 continues / Class A present | **CONFIRMED** | R21 has five Class A findings |

**Score:** 9 CONFIRMED / 6 REFUTED / 0 VACUOUS.

---

## S10: Verdict and key-question answer

### Verdict

**ADVISORY HALT — HIGH / Class A present.**

This seat is non-carrying by dispatch, so the verdict is advisory rather than a binding carry decision. The evidence nevertheless meets the program's Class A definition: multiple producer claims are false on the shipped bytes.

The strongest positive result is that **CI-1R works**: the v0.62 register is deterministically reproduced, current count/list coupling is sound, the authoritative seat-count repair works, 186 tests pass, and the 62-entry internal seal chain verifies.

Those successes do not rescue the release because the self-description layer again outruns the implementation:

1. the package claims a green build and 19/19 packet hashes while shipping a red build and 15 mismatches;
2. `source_finding_id` is claimed added but is absent/non-operative;
3. “structural” receipt validation is still substring containment;
4. “bidirectional” membership parity is one-directional;
5. the noted-finding bypass survives on a parallel schema path.

### Key-question answer

**Does v0.62 break the R7–R20 Class A streak (14/14)?**

**No.** R21 contains Class A defects. The streak extends to **R7–R21 = 15/15**.

The observed migration remains consistent with the methodology's own Level-3/Level-4 warning: increasingly strong mechanisms are present, but the next Class A appears in the producer's claim that the mechanism is broader, more structural, or more complete than the shipped implementation actually is.

**Bismillah.**

---

# Bismillah ir-Rahman ir-Rahim
