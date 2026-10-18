# Bismillah ir-Rahman ir-Rahim

# R0235 -- XZ Protocol v0.62 -- Round 21 Advisory Audit Report

**Chronological Index:** 497 of 995  
**Date:** 2026-08-11  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v062_R21_S01_OPUS5_REPORT.md  
**Source Format:** md  
**SHA-256:** `8cedde639fb149c00c8895ce9b7e09deccac16060fffe13661e5a3b9225c2a5a`  

---

## R0235 · XZ Protocol v0.62 -- Round 21 Advisory Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v062_R21_S01_OPUS5_REPORT.md
- source_format: md
- text_sha256: 8cedde639fb149c00c8895ce9b7e09deccac16060fffe13661e5a3b9225c2a5a

# XZ Protocol v0.62 -- Round 21 Advisory Audit Report

**Seat:** S01 (FRESH) | **Model:** Claude Opus 5 | **Role:** ADVISORY (producer-family, barred from carry)
**Framework:** Biomedical Fractal + Seven-Layer Verification
**Round:** 21 | **Version under audit:** 0.62 | **Date:** 2026-08-16
**Producer:** Claude Opus 4.6 -- BARRED
**Verdict:** **HALT** (advisory; zero carry weight)

---

## S0. Identity, mode, execution surface

| Field | Value |
|---|---|
| Seat ID | S01 |
| Mode | FRESH -- no prior context, no held bytes, no prior-seat reports consulted |
| Carry weight | ZERO. Producer-family (Claude). Section 22.1 excludes this family from carrying-seat eligibility. |
| Dispatch bundle SHA-256 | `d5eac710d71809d925d02d63b8932dd240cf6198013c91b7f4ba8b90947c5661` |
| OS | Ubuntu 24.04.4 LTS |
| Kernel | 6.18.5-fc-v20 x86_64 |
| Python | 3.12.3 |
| pytest | 9.1.1 |
| Environment | Ephemeral container, network-enabled, unsealed (standing boundary 7) |

**Seat-conformance declaration.** This seat was dispatched FRESH. No memory file, prior seat report, or lineage record was read before execution. `R20_REPORTS.txt` was consulted only at S3 and only to determine that the R20 raw reports are not shipped (the file contains R19 reports, as AUDIT_CONTEXT discloses). `METHODOLOGY_v2.txt` and `CI_METHODOLOGY.txt` were read as methodology, not as prior-round findings. Prediction outcomes at S9 were computed from executed evidence, not from the dispatch's stated confidences.

---

## S1. Staging and byte verification

### S1.1 Extraction -- DEFECT FOUND AT THE FIRST STEP

The extraction procedure shipped verbatim in `AUDIT_CONTEXT.txt` was executed exactly as given. Result:

```
sha256sum -c PACKET_SHA256SUMS
  4 files OK, 15 files FAILED
sha256sum: WARNING: 15 computed checksums did NOT match
```

Root cause, established by byte-level diagnosis: the shipped splitter uses the delimiter `######_XZPACKET_FILE_SPLIT_######\n` and writes `b[nl+1:]` as the file body. The packet places a newline *before* each delimiter, so every file except the terminal member receives one extra trailing `\n`. Confirmation -- for all 15 failing members, `sha256(body[:-1])` matches the manifest digest exactly; the sole passing packet member, `xz_protocol_trust_roots_PUBLIC.json`, is last in the packet and therefore has no trailing delimiter to absorb.

| Member | As-shipped extraction | After removing one trailing byte |
|---|---|---|
| `HISTORY.sha256` | FAILED | OK |
| `build.py` | FAILED | OK |
| 13 further `.py` members | FAILED | OK |
| `xz_protocol_trust_roots_PUBLIC.json` | OK | (terminal member; unaffected) |

After repairing the splitter (strip one trailing newline from all non-terminal members), `sha256sum -c PACKET_SHA256SUMS` returns **19/19 OK**. Every subsequent section of this report was executed against the repaired, digest-verified bytes.

See **F-S01-62-08**.

### S1.2 Baseline green (on repaired bytes)

| Check | Claimed (AUDIT_CONTEXT) | Observed | Status |
|---|---|---|---|
| `sha256sum -c PACKET_SHA256SUMS` | 19/19 OK | 19/19 OK | MATCH (post-repair only) |
| `python3 build.py` | 248 PASS, 0 FAIL | **247 PASS**, 0 FAIL, rc=0 | **MISMATCH** |
| pytest (6-suite explicit) | 186 GREEN | 186 passed in 11.09s | MATCH |
| `HISTORY.sha256` | 62 ENTRY + FULL_SECTION_27 + PRIOR_HISTORY | 62 ENTRY (lines 1-62), FULL_SECTION_27 (63), PRIOR_HISTORY (64) | MATCH |

The 247 figure is stable across three consecutive runs. `build.py` emits no self-total; the count is the cardinality of lines matching `^  PASS:`. Neither `247` nor `248` appears anywhere in `xz_protocol_v0_62.md`, so the claim is dispatch-layer metadata with no gated body counterpart. See **F-S01-62-09**.

### S1.3 Evidence digests

```
6f7c2762d781445ff3da03dfe9b27d446510c65fb178fc8d81edb5e127fa0eec  xz_protocol_v0_62.md
20586393bb95fe07e2ad9866832f93cc4f50290607ce25f3fdd84c7ccf44dbc6  xz_protocol_register_gen.py
56541021f1685d42815c037a3a07347ae91eb70d5f5683087b5a2cb495ef140e  r20_findings_index.json
ee1c133e98883a1f858a03e8866ccee05424ec42bc5a9f2bfe94d328011b8ce3  HISTORY.sha256
```

---

## S2. CI-1R reproduction (byte-exact register comparison)

`generate_register`, `generate_boundary_list`, and `generate_terminal_line` were invoked against the shipped `r20_findings_index.json` and `xz_protocol_boundaries.json` at version `0.62`, and each output was tested for byte-exact containment in `xz_protocol_v0_62.md`.

| Generated artifact | Length (bytes) | Byte-exact present in shipped protocol |
|---|---|---|
| Defect register (header + 4 CLOSED items + NOTED block) | 1919 | **YES** |
| Boundary list (35 items) | 1797 | **YES** |
| Terminal line | 78 | **YES** |

**CI-1R: PASS.** The register prose in the v0.62 amendment entry is byte-reproducible from the machine-readable inputs. The producer did not hand-write register prose. P1 CONFIRMED.

This is a genuine architectural achievement and it should be stated plainly: the mechanical layer is sound. Every Class A finding below sits in the hand-written prose *about* the mechanism, not in the mechanism.

---

## S3. R20 finding discharge

`R20_REPORTS.txt` contains R19 seat reports, not R20 reports, as `AUDIT_CONTEXT.txt` discloses. R20 raw reports are unavailable at this seat. Discharge is therefore verified against `R20_TRIAGE.txt`, `r20_findings_index.json`, and the v0.62 shipped code, not against R20 source reports. That limitation is stated, not worked around.

| R20 group | Claimed disposition | Verified against v0.62 bytes | Outcome |
|---|---|---|---|
| **1** -- M3 receipt enforcement + validation | CLOSED via CI v0.3.2: receipt on any mixed distribution; validation "structural ... not substring" | Enforcement half CONFIRMED (`has_mixed = len(source_dist) > 1 or sev != majority_sev`, `xz_protocol_register_gen.py:126`). Validation half **REFUTED**: `if dist_str not in receipt` (line 136) is substring containment. Probe P-3 lands. | **PARTIAL -- not discharged** (F-S01-62-02, F-S01-62-07) |
| **2** -- `_unique_seat_count` from ID parsing | CLOSED via CI v0.3.2: seat count from `findings_by_id[fid]["seat"]` | Mechanism CONFIRMED (line 34-36) and load-bearing. But the `seat` field is never validated against the finding_id it accompanies, and the ID-parsing branch remains live as a fallback (lines 37-40). Probe P-1 lands: one corrupted `seat` value silently moves the register from 6-seat to 5-seat. | **RELOCATED -- not discharged** (F-S01-62-03) |
| **3** -- CI-8 source-ID fidelity | NOTED; "R21 will add `source_finding_id`" | `source_finding_id` appears **zero times** in `EXECUTABLE_PACKET.txt`, zero times in the shipped index findings records, zero times in the generator. The index's own group-3 adjudication states it as a future R21 action. The Status line states it as done. | **NOTED disposition is honest; the Status line is byte-false** (F-S01-62-01) |
| **4** -- Noted-finding dangling bypass | CLOSED via CI v0.3.2: bypass removed; ungrouped must be null | CONFIRMED. Probe P-9 rejected with the correct diagnostic. No noted-status branch survives in the cross-layer validation block (lines 158-168). | **DISCHARGED** |
| **5** -- Bidirectional membership parity | CLOSED via CI v0.3.2: scalar `convergence_group` must equal containing group | One direction CONFIRMED (probe P-10 rejected). Reverse direction **REFUTED**: the parity loop iterates only findings present in `fid_to_group` (lines 175-185), so a finding pointing at an existing group but contained in *no* group's `finding_ids` passes both checks. Probe P-2 lands. | **UNIDIRECTIONAL -- not discharged** (F-S01-62-04) |

Also verified as claimed and holding: source distribution is load-bearing and emitted into the register; dangling `convergence_group` references are rejected; the VERSION-1 gate is sabotage-proven (S5, sabotage S-1); PRIOR_HISTORY is present as exactly one line and derives.

---

## S4. Amendment-entry audit

Every substantive claim in the v0.62 entry and Status line, adjudicated against shipped bytes.

| # | Claim (locus) | Verdict | Evidence |
|---|---|---|---|
| 1 | Status line: "source_finding_id field added for CI-8 literal resolution" (`xz_protocol_v0_62.md:5`) | **REFUTED** | Zero occurrences in packet code, index schema, or generator. Index group 3 says R21 *will* add it. |
| 2 | Status line + entry item (1): receipt validation "structural (exact canonical distribution string, not substring)" | **REFUTED** | `register_gen.py:136` is `dist_str not in receipt` -- substring containment. Probe P-3 lands a fabricated receipt. |
| 3 | Status line + item (2): "seat count from authoritative findings[].seat (not ID parsing)" | **CONFIRMED (mechanism)** | Line 34-36. Probe P-1 proves it load-bearing. Field itself unvalidated (F-S01-62-03). |
| 4 | Item (1): "receipt required on any mixed distribution (not majority-only)" | **CONFIRMED** | Line 126. Probe P-7 rejected on flip to mixed. |
| 5 | Item (3): "bypass removed; ungrouped findings must have convergence_group=null" | **CONFIRMED** | Lines 158-168; probe P-9 rejected. |
| 6 | Item (4): "each finding's scalar convergence_group must equal the group whose finding_ids contains it" | **CONFIRMED where a containing group exists; VACUOUS otherwise** | Lines 175-185; probe P-2 lands. |
| 7 | Entry prose: "Defect 1, 8/10 seats" | **NOT VERIFIABLE, and contradicted in-entry** | Index supports 6 seats; the same entry's COMPUTED bracket reads `[6-seat / 7-finding convergence:]`. The "+2 others" of `R20_TRIAGE.txt` are unenumerated. |
| 8 | Entry prose: "Defect 2, 3/10" | **NOT VERIFIABLE, and contradicted in-entry** | COMPUTED bracket reads `[2-seat convergence:]`. |
| 9 | Entry prose: "Defect 3, 6/10" | **NOT VERIFIABLE, and contradicted in-entry** | COMPUTED NOTED bracket reads `[5-seat:]`. |
| 10 | Entry prose: "Defect 4, 1/10" | **CONFIRMED** | COMPUTED bracket reads `[1-seat convergence:]`. |
| 11 | Entry prose: "16/25 index finding IDs absent from source reports" | **NOT VERIFIABLE** | Shipped index has 17 findings. The R19 index that R20 audited is not shipped. Recorded as unverifiable, not as false. |
| 12 | Item (4): triage severity MEDIUM for the parity group | **CONTRADICTED by a shipped artifact** | `R20_TRIAGE.txt` Surface 4 reads "Triage severity: HIGH (elevated from 1H+1M per convergence)". Index and register read MEDIUM. Ungated. |
| 13 | Entry: "Disclosed standing boundaries -- 35 items" `[ENUMERATED: 35 items]` | **CONFIRMED** | `boundaries.json` count 35, `len(items)` 35, 35 emitted, byte-exact. |
| 14 | `HISTORY.sha256` 62 ENTRY seals + FULL_SECTION_27 + PRIOR_HISTORY | **CONFIRMED** | Line census 62/1/1; sabotage S-2 detected a one-character seal mutation. |
| 15 | Front matter: "**Version:** 0.62, draft candidate, 2026-08-11" | **REFUTED** | Section 27 dates the v0.62 entry 2026-08-15. 2026-08-11 is v0.61's and v0.60's date, carried forward. |
| 16 | Section 22.2 bound "v0.1 through v0.61" | **CONFIRMED** | `build.py:696`; sabotage S-1 fires on mutation. |
| 17 | Section 22.3 bound "v0.38-v0.61" | **CONFIRMED** | `build.py:698`. |
| 18 | Section 22.2: "nine recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, and v0.47" | **NOT VERIFIABLE** | Cardinal nine over a seven-locus list with no per-locus multiplicity stated. `[9e]` covers only "N consecutive (v0.X through v0.Y)" in the current entry, so this is out of gate scope. |
| 19 | AUDIT_CONTEXT: "build.py: 248 PASS, 0 FAIL" | **REFUTED** | 247 PASS, stable across three runs. |
| 20 | AUDIT_CONTEXT: "PACKET_SHA256SUMS: 19/19 OK" | **REFUTED as shipped; CONFIRMED after undocumented repair** | 15/19 FAILED using the shipped extraction procedure. |

### Four-scribe tag census (v0.62 entry)

| Tag | Count |
|---|---|
| `[COMPUTED: ...]` | 7 |
| `[ENUMERATED: ...]` | 1 |
| `[ASSERTED]` | 1 |
| **Total** | **9** |

ASSERTED share: **11.1%**, below the 15% threshold. P3 CONFIRMED.

The tagging discipline is working as designed at the level of provenance. It is worth stating the limit precisely: the `[ASSERTED]` tag discloses that a claim was not computed. It does not license the claim to contradict a `[COMPUTED]` value printed two sentences later in the same entry. Items 7-9 above are exactly that -- disclosed provenance, undisclosed contradiction.

---

## S5. Probe battery

Ten register-generator mutations plus four build-gate sabotages. Each landed mutation is paired with a benign control or a rejecting control that proves the harness is not simply inert.

### S5.1 Register-generator battery

Baseline: generates, byte-exact against shipped protocol.

| ID | Mutation | Gate | Landed effect |
|---|---|---|---|
| **P-1** | `findings[F-S05-61-01C].seat`: `S05C` -> `S05F` | **none fired** | **LANDED.** Register silently emits `[5-seat / 7-finding convergence: ...]` in place of `[6-seat / 7-finding ...]`. |
| P-1b | BENIGN CONTROL: same field rewritten to its existing value `S05C` | none fired (correct) | No change. Byte-identical to shipped. |
| **P-2** | Remove `F-S05-61-01C` from group 1's `finding_ids`; leave its scalar `convergence_group=1` | **none fired** | **LANDED.** `[6-seat / 7-finding]` -> `[5-seat / 6-finding]`. Orphan-but-pointing finding accepted. |
| **P-3** | Group 5 receipt -> `"Source distribution: 1 HIGH, 1 MEDIUM. Triage severity HIGH. Distribution is actually 2 LOW. Receipt fabricated."` | **none fired** | **LANDED.** Passes the "structural" validator. Register regenerates **byte-identically to the shipped protocol** while the receipt contradicts itself, contradicts `triage_severity`, and self-declares as fabricated. |
| **P-4** | Group 1 (uniform 7 HIGH) receipt -> `"Distribution: 3 LOW, 1 INFORMATIONAL. Triage severity INFORMATIONAL. No deviation."` | **none fired** | **LANDED.** Uniform-distribution groups receive zero receipt validation. Register byte-identical to shipped. 4 of 5 shipped groups sit in this unvalidated state. |
| P-5 | REJECTING CONTROL: `F-S03-61-01F` added to group 2's list, scalar set to 2 | fired | `ValueError: scalar convergence_group=2 does not match containing group 4` |
| **P-6** | Delete the `seat` key from a findings record | fired, **badly** | `KeyError: 'seat'` -- an uncaught exception, not a validation `ValueError`. `findings[]` has no required-field validation, unlike `noted[]` which requires `substance`. |
| P-7 | REJECTING CONTROL: flip one group-1 `source_severity` HIGH -> LOW (uniform becomes mixed, receipt now stale) | fired | `ValueError: adjudication_receipt does not contain the exact canonical distribution '6 HIGH, 1 LOW'` |
| **P-8** | Group 5 `triage_severity`: MEDIUM -> HIGH, receipt untouched (still reads "Triage severity MEDIUM.") | **none fired** | **LANDED.** Register emits `HIGH CLOSED` for the parity group while its own receipt says MEDIUM. Severity is settable independently of the receipt. |
| P-9 | REJECTING CONTROL: `convergence_group=99` (dangling) | fired | `ValueError: references convergence_group 99 which does not exist ... Use null for ungrouped/noted findings.` |
| P-10 | REJECTING CONTROL: scalar `cg=2` while contained in group 1 | fired | `ValueError: Bidirectional parity requires these to match.` |

**Battery result: 5 landed (P-1, P-2, P-3, P-4, P-8), 1 crashed uncleanly (P-6), 4 correctly rejected.** The four rejecting controls confirm the harness exercises the live gates rather than a stub.

### S5.2 Build-gate sabotage battery

| ID | Sabotage | rc | Diagnostic |
|---|---|---|---|
| S-0 | Baseline | 0 | 0 FAIL |
| S-1 | Section 22.2 bound `v0.61` -> `v0.60` | 1 | `FAIL: Section 22.2 carried-entry bound at VERSION-1 (v0.1 through v0.61)` -- VERSION-1 gate sabotage-proven |
| S-2 | `HISTORY.sha256` ENTRY_v0.62 first hex char flipped | 1 | `FAIL: HISTORY seal ENTRY_v0.62 matches bytes` -- append-only seal detects mutation |
| S-3 | Front-matter date `2026-08-11` -> `2999-01-01` | 1 | `FAIL: PACKET_SHA256SUMS digest matches: xz_protocol_v0_62.md` -- caught **only** by the digest gate, which is tautological on any byte change and which the producer regenerates in normal workflow. No semantic date gate exists. |
| S-4 | BENIGN CONTROL: all sabotages reverted | 0 | 0 FAIL |

S-3 is the informative one. The date staleness at F-S01-62-10 is not caught by any semantic check; it survives precisely because the producer reseals. That is standing boundary 32 (self-consistent resealing blind spot) operating live on a body-copy semantic value.

---

## S6. Seven-layer traversal

| Layer | Reached | Result |
|---|---|---|
| **1 -- Code execution** | YES | build.py rc=0 / 247 PASS (claimed 248); pytest 186/186 GREEN; `sha256sum -c` 15/19 FAILED as shipped, 19/19 after repairing the shipped extraction procedure. |
| **2 -- Register verification** | YES | CI-1R byte-exact on all three generated artifacts. The mechanical layer is clean. |
| **3 -- Cross-layer consistency** | YES | Version tokens agree (0.62 front matter, Status, terminal line, 22.2/22.3 at VERSION-1). Boundary count 35 agrees across JSON, generator, and entry. **Failures:** front-matter date vs entry date; ASSERTED seat counts vs COMPUTED brackets (3 of 4); `R20_TRIAGE.txt` group-5 severity vs index/register; Status-line `source_finding_id` vs absent field. |
| **4 -- Adversarial probing** | YES | 10 register mutations + 4 build sabotages. 5 landed, 1 unclean crash, 4 correct rejections, 2 benign controls clean. |
| **5 -- Temporal integrity** | YES | 62 ENTRY seals + FULL_SECTION_27 + exactly 1 PRIOR_HISTORY; derivation succeeds; S-2 sabotage detected. Append-only holds. |
| **6 -- Methodology audit** | YES | Dispatch and AUDIT_CONTEXT claims audited against shipped bytes: two refuted (248 PASS; 19/19 OK as shipped), one refuted at the schema layer (`source_finding_id` "added"). The audit-support layer is now itself a Class A surface. |
| **7 -- Boundary disclosure** | YES | 35 boundaries enumerated and byte-exact. `[9e]` cardinal-range gate matched zero range claims in the v0.62 entry -- vacuous this round, correctly pre-disclosed as boundary 23. No boundary covers the four Class A surfaces below; that is the substantive gap. |

**Biomedical Fractal reading.** The defect is not diffuse; it has a single histology at three sites. In every Class A finding below, the *tissue* is identical: a hand-written sentence that describes the mechanism more completely than the mechanism implements. `register_gen.py:136` performs containment; the entry says "not substring matching." The seat field is read; the entry says "authoritative." The parity check runs one direction; the entry says "must equal." The schema lacks a field; the Status line says "added." The generated register -- the part no human wrote -- is byte-perfect. The lesion is exclusively at the prose-code interface, and it is now confined to a margin of roughly one sentence per repair. That is a narrowing lesion, not a resolving one: the surface shrank from R20 (four defect classes) to R21 (four claims about four repairs), but it did not clear.

---

## S7. Findings

Ordered by severity, then locus. Six elements each (ID, severity, class, locus, substance, evidence), plus disposition and cross-reference.

---

**F-S01-62-01** HIGH -- Class A -- Status line asserts a schema field that does not exist on shipped bytes

- **Locus:** `xz_protocol_v0_62.md:5` (Status line, gated BODY region).
- **Substance:** The Status line states "source_finding_id field added for CI-8 literal resolution." The field is absent from every shipped byte: zero occurrences in `EXECUTABLE_PACKET.txt`, zero in the 17 `findings[]` records of `r20_findings_index.json`, zero in `xz_protocol_register_gen.py`. The shipped index contradicts the Status line directly: group 3's `triage_adjudication` reads "R21 **will** add source_finding_id field to the findings schema." The register's own disposition for that group is NOTED, not CLOSED -- the machine-generated layer is honest; the hand-written Status line is not.
- **Evidence:** `grep -c source_finding_id EXECUTABLE_PACKET.txt` -> `0`. `python3 -c "..."` over the index shows finding-record keys `['finding_id','seat','source_severity','defect_class','convergence_group']`. `r20_findings_index.json:199`. `xz_protocol_v0_62.md:5`.
- **Disposition:** Either implement the field in the findings schema and add a generator-side resolution check before v0.63, or amend the Status line to future tense ("`source_finding_id` deferred to R22 per group-3 NOTED disposition"). Do not ship both a NOTED disposition and a completed-tense Status claim for the same item.
- **Cross-reference:** `METHODOLOGY_v2.txt:92` names this exact class -- "The Status line that says 'VERSION-1 gate implemented' when build.py has no such gate." R20 group 3 (NOTED). Section 22.3 Class A ("contradicted status").

---

**F-S01-62-02** HIGH -- Class A -- Receipt validation described as structural is substring containment

- **Locus:** `xz_protocol_register_gen.py:130-142`; claim at `xz_protocol_v0_62.md:5` (Status line) and in the v0.62 entry item (1) adjudication text.
- **Substance:** Both the Status line and the entry's `[COMPUTED: generate_register]` adjudication state that receipt validation requires "the exact canonical distribution string verbatim (not substring matching)." The shipped implementation is `if dist_str not in receipt: raise ValueError(...)`. That is substring matching -- the canonical string as a substring of an otherwise unconstrained free-text field. A receipt containing the canonical string alongside arbitrary contradictory content passes. The R20 defect was substring matching on severity tokens; CI v0.3.2 narrowed the needle and kept the haystack.
- **Evidence:** Probe P-3. Group 5 receipt replaced with `"Source distribution: 1 HIGH, 1 MEDIUM. Triage severity HIGH. Distribution is actually 2 LOW. Receipt fabricated."` -- no gate fired, and the register regenerated **byte-identically to the shipped protocol**. Probe P-8: `triage_severity` raised MEDIUM -> HIGH with the receipt untouched (still reading "Triage severity MEDIUM.") -- no gate fired, severity changed in the emitted register.
- **Disposition:** Replace containment with structural equality against a canonical receipt grammar: parse the receipt into `(distribution, triage_severity, deviation_flag)` and assert each against the computed values. Minimum viable: require `receipt.strip()` to equal a generator-produced canonical receipt string, making the receipt a computed artifact rather than a producer-written one. Until then, amend the entry and Status line to read "receipt must contain the canonical distribution string" -- which is what the code does.
- **Cross-reference:** R20 group 1 (CLOSED -- disposition not sustained). F-S01-62-07 (uniform-group vacuity). `METHODOLOGY_v2.txt:92`, "The docstring that says 'receipt is structural' when the code checks by substring." Section 22.3 Class A.

---

**F-S01-62-03** HIGH -- Class A -- Seat count moved to an authoritative field that is never validated; wrong-count defect relocated, not closed

- **Locus:** `xz_protocol_register_gen.py:30-40` (`_unique_seat_count`), 60-82 (findings lookup construction).
- **Substance:** R20 group 2 was CLOSED on the ground that seat identity would come from `findings_by_id[fid]["seat"]` rather than from parsing the finding_id. The field is now read, but nothing validates it: no schema check that `seat` is present, no cross-check that `seat` is consistent with the seat encoded in the finding_id it accompanies (`F-S05-61-01C` -> `S05C`), no uniqueness or vocabulary constraint against the declared `seats[]` list. The defect class named in the R20 triage -- "a finding with a non-standard ID format produces a wrong seat count silently" -- survives verbatim with the substrate changed from the ID string to the `seat` field. The superseded ID-parsing branch also remains live as a fallback at lines 37-40.
- **Evidence:** Probe P-1. Setting `findings[F-S05-61-01C].seat = "S05F"` -- a value that is a legitimate member of the declared `seats[]` list and contradicts its own finding_id -- produced no gate fire and silently emitted `[5-seat / 7-finding convergence: ...]` in place of the shipped `[6-seat / 7-finding ...]`. Benign control P-1b (same field rewritten to `S05C`) produced a byte-identical register, confirming the harness discriminates. Probe P-6: deleting the key raises an uncaught `KeyError: 'seat'`, not a validation error.
- **Disposition:** Add three validations to the findings-lookup loop before v0.63: (a) `seat` is a required non-empty field, raising `ValueError` not `KeyError`; (b) `seat` is a member of `index["seats"]`; (c) `seat` matches the seat token parsed from `finding_id`, since the ID regex already guarantees the token's shape. Then delete the ID-parsing fallback branch rather than leaving a superseded code path resident.
- **Cross-reference:** R20 group 2 (CLOSED -- disposition not sustained). F-S01-62-11 (unclean failure mode). F-S01-62-12 (no vendor field on the same records). R20_TRIAGE Surface 2.

---

**F-S01-62-04** HIGH -- Class A -- "Bidirectional" membership parity is unidirectional

- **Locus:** `xz_protocol_register_gen.py:170-185`.
- **Substance:** The entry's item (4) adjudication states that "each finding's scalar convergence_group must equal the group whose finding_ids contains it." The implementation builds `fid_to_group` from the groups' membership lists and then checks parity only `if fid in fid_to_group`. When no group's `finding_ids` contains the finding, the loop body is skipped entirely and the cross-layer check at lines 158-168 accepts the scalar because the referenced group exists. A finding may therefore claim membership in a real group that does not claim it back. The direction the repair covers (contained but disagreeing) fires; the direction that produces silent under-counting does not.
- **Evidence:** Probe P-2. Removing `F-S05-61-01C` from group 1's `finding_ids` while leaving its scalar `convergence_group=1` produced no gate fire, and the register silently moved from `[6-seat / 7-finding convergence]` to `[5-seat / 6-finding convergence]`. Rejecting control P-10 (scalar `cg=2` while contained in group 1) fired correctly, confirming the covered direction works.
- **Disposition:** After building `fid_to_group`, assert the reverse containment: for every finding with a non-null `convergence_group`, require `fid in fid_to_group` and `fid_to_group[fid] == cg`. One added conditional closes it. Alternatively derive `finding_ids` from the scalars and eliminate the dual representation entirely -- the redundancy is the defect surface.
- **Cross-reference:** R20 group 5 (CLOSED -- disposition not sustained). Note that R20 group 5's own source distribution is the mixed one at F-S01-62-06. Section 22.3 Class A.

---

**F-S01-62-05** HIGH -- Class A -- Three of four asserted seat counts contradict the computed brackets in the same entry

- **Locus:** `xz_protocol_v0_62.md:1383`, v0.62 amendment entry, `[ASSERTED]` prose paragraph versus the `[COMPUTED: generate_register]` register items immediately following.
- **Substance:** The entry's narrative paragraph states "Defect 1, 8/10 seats", "Defect 2, 3/10", "Defect 3, 6/10". The register items generated from the same index, printed in the same entry, read `[6-seat / 7-finding convergence]`, `[2-seat convergence]`, and `[5-seat:]`. Only Defect 4 (1/10 vs `[1-seat]`) agrees. `R20_TRIAGE.txt` sources the asserted figures via unenumerated tails ("+ 2 others", "+ 1 other") that have no corresponding records in the shipped index, so the asserted counts are not verifiable on shipped bytes and are contradicted by the verifiable ones. The `[ASSERTED]` tag discloses that the figures were not computed; it does not reconcile them with the computed figures sitting beside them, and no gate compares the two.
- **Evidence:** Regex extraction over the isolated v0.62 entry: asserted `['8/10','3/10','6/10','1/10']`; computed brackets `['6','2','1','2','5']` (register order: groups 1, 2, 4, 5, then NOTED group 3). Index census: 17 findings across 6 distinct seats (`S02F, S02C, S03F, S03C, S05F, S05C`); the declared `seats[]` list has 10 members, 4 of which contributed no findings.
- **Disposition:** Either enumerate the missing seat records in the index so the asserted and computed figures converge, or replace the narrative seat counts with the generator's computed values and delete the hand-written fractions. A build gate comparing every `N/10` in the current entry against the corresponding computed bracket would make the class mechanically unrepeatable.
- **Cross-reference:** F-S01-62-03 (the seat-count substrate). F-S01-62-12 (unrecorded seats). Section 22.3 Class A ("wrong count"). `METHODOLOGY_v2.txt:94`, "confining the producer's claims to only what the scribes can verify."

---

**F-S01-62-06** MEDIUM -- Class A -- Shipped triage document and shipped index disagree on a disposition severity

- **Locus:** `R20_TRIAGE.txt` Surface 4 versus `r20_findings_index.json` group 5 `triage_severity` and the emitted register item (4).
- **Substance:** `R20_TRIAGE.txt` states for the bidirectional-parity group: "Triage severity: HIGH (elevated from 1H+1M per convergence)." The index records `"triage_severity": "MEDIUM"` and the register emits `MEDIUM CLOSED`. Two shipped artifacts assert different severities for the same adjudicated group, and the entry's own history shows the elevation reasoning was considered and then not applied. Nothing gates the pair: probe P-8 confirms `triage_severity` is freely settable with the receipt untouched, so no mechanism would have caught the divergence in either direction.
- **Evidence:** `R20_TRIAGE.txt` Surface 4 block; `r20_findings_index.json` group 5; register item (4) reads `MEDIUM CLOSED via CI v0.3.2 architecture repair: Bidirectional membership parity`. Probe P-8 landed MEDIUM -> HIGH with no gate fire.
- **Disposition:** Reconcile to one value and state which document is the substrate of record for triage severity. If the elevation was intentional, the index is stale; if the index is correct, the triage narrative is stale. Then derive `triage_severity` from a stated rule over the source distribution rather than as a free field, so the receipt constrains it.
- **Cross-reference:** F-S01-62-02 (receipt does not constrain triage severity). R20 group 5. Section 22.3 Class A ("contradicted status").

---

**F-S01-62-07** MEDIUM -- Class D -- Uniform-distribution groups receive no receipt validation at all

- **Locus:** `xz_protocol_register_gen.py:126-142`.
- **Substance:** `has_mixed` is true only when the source distribution has more than one severity or the triage diverges from the majority. For a uniform group whose triage equals the majority, the entire receipt block is skipped -- the receipt is neither required nor read. Four of the five shipped groups are in this state, and all four ship receipts asserting distributions ("All 7 source findings are HIGH. Distribution: 7 HIGH."). Those assertions are unvalidated and could be arbitrarily false. This is a defensible reading of the CI v0.3.2 rule as written; it is a gate limitation the entry does not name, so it is Class D only because the entry makes no claim about uniform groups -- but the Status line's phrase "receipt validation structural" reads as unconditional.
- **Evidence:** Probe P-4. Group 1's receipt replaced with `"Distribution: 3 LOW, 1 INFORMATIONAL. Triage severity INFORMATIONAL. No deviation."` -- against an actual distribution of 7 HIGH -- produced no gate fire and a register byte-identical to the shipped protocol.
- **Disposition:** Validate the receipt on every group with a receipt present, not only on mixed ones. The canonical distribution string is computed for all groups already (`_computed_dist_str` is assigned unconditionally at line 121), so the check costs one dedented conditional.
- **Cross-reference:** F-S01-62-02 (validation strength on the groups that are checked). R20 group 1. Boundary 23 (silent vacuity) is the nearest disclosed analogue but does not cover this locus.

---

**F-S01-62-08** MEDIUM -- Class A -- Shipped extraction procedure produces 15 of 19 digest failures; dispatch asserts 19/19 OK

- **Locus:** `AUDIT_CONTEXT.txt` "Extraction (copy-paste and run)" block; claim in the same file's "Build status" block and in `DISPATCH.txt`.
- **Substance:** The extraction snippet writes `b[nl+1:]` for each split segment. The packet places a newline before each delimiter, so every non-terminal member is written with one surplus trailing `\n`. Executing the procedure exactly as shipped yields `15 computed checksums did NOT match` against `PACKET_SHA256SUMS`, while the audit-support files assert "PACKET_SHA256SUMS: 19/19 OK". The claim is reachable only after a repair the packet does not document. Every byte-anchored claim in the round depends on this step, so the defect sits upstream of the entire verification chain -- an auditor who trusted the shipped procedure would have reported a false 15-file digest failure, and one who trusted the shipped claim would never have run it.
- **Evidence:** As-shipped run: `sha256sum: WARNING: 15 computed checksums did NOT match`. Diagnostic: for all 15 failing members, `sha256(body[:-1])` equals the manifest digest; the single passing packet member is the terminal one. After stripping one trailing newline from all non-terminal members: `19/19 OK`, `build.py` rc=0, pytest 186/186.
- **Disposition:** Correct the snippet to `body = b[nl+1:]; body = body[:-1] if body.endswith(b"\n\n") else body`, or emit the packet with the delimiter immediately following each file's final byte. Then add the extraction procedure itself to the packet's verified surface -- it is currently the only load-bearing step with no gate over it.
- **Cross-reference:** Boundary 10 (packet non-closure) and boundary 11 (fresh-execution non-reproducibility) are adjacent disclosures but neither covers a deterministic, reproducible defect in the shipped procedure. Section 22.3 Class A.

---

**F-S01-62-09** LOW -- Class A -- Dispatch build-check count off by one

- **Locus:** `AUDIT_CONTEXT.txt` "Build status" block; `build.py` output.
- **Substance:** The audit-support files claim "build.py: 248 PASS, 0 FAIL". Observed: 247 PASS, 0 FAIL, rc=0, stable across three consecutive runs on digest-verified bytes. `build.py` emits no self-total, so the figure has no computed source and no gated body counterpart -- neither `247` nor `248` appears in the protocol.
- **Evidence:** `python3 build.py | grep -c "^  PASS:"` -> `247`, `247`, `247`.
- **Disposition:** Have `build.py` print its own PASS total and gate the dispatch figure against it, or drop the count from the dispatch. A hand-maintained gate count is the same class of surface as a hand-maintained seat count.
- **Cross-reference:** F-S01-62-05 (hand-maintained counts). `METHODOLOGY_v2.txt:40` cites "gate counts rising from 222 to 258+" as a trajectory metric, which makes this figure load-bearing for the methodology paper, not merely cosmetic.

---

**F-S01-62-10** LOW -- Class B -- Front-matter version date is v0.61's, four days stale, and semantically ungated

- **Locus:** `xz_protocol_v0_62.md:4` versus `xz_protocol_v0_62.md:1383`.
- **Substance:** Front matter reads "**Version:** 0.62, draft candidate, 2026-08-11". The Section 27 v0.62 entry is dated 2026-08-15. 2026-08-11 is the date carried on both the v0.60 and v0.61 entries -- the token was not advanced with the version. The Status-provenance gate at `build.py:208-234` validates the version tokens on this line but not the date. The only check that reacts to the date is the packet digest, which fires on any byte change whatsoever and which the producer regenerates as a matter of course.
- **Evidence:** Entry dates: v0.60 2026-08-11, v0.61 2026-08-11, v0.62 2026-08-15. Sabotage S-3: mutating the date to 2999-01-01 failed only `PACKET_SHA256SUMS digest matches: xz_protocol_v0_62.md`, with no semantic diagnostic.
- **Disposition:** Extend the `[2f]` Status-provenance gate to assert that the front-matter date equals the date on the current version's Section 27 entry. One regex, one `check()`.
- **Cross-reference:** Boundary 32 (self-consistent resealing blind spot) operating on a body-copy semantic value. Section 22.3 Class B (an error the entry does not disclose).

---

**F-S01-62-11** LOW -- Class D -- Missing required field raises `KeyError` rather than a validation error

- **Locus:** `xz_protocol_register_gen.py:34-36` and the findings-validation loop at 66-82.
- **Substance:** The findings-validation loop checks `finding_id` format, uniqueness, and `source_severity` vocabulary, but does not check that `seat` is present. A record omitting it produces an uncaught `KeyError: 'seat'` at generation time. By contrast the `noted[]` validator explicitly raises `ValueError(f"Noted finding {fid} missing required field 'substance'.")`. The asymmetry means the newly-authoritative field is the least-validated one in the schema.
- **Evidence:** Probe P-6 -> `KeyError: 'seat'`.
- **Disposition:** Add `seat` to the required-field checks in the findings loop with a `ValueError` carrying the finding_id, matching the `noted[]` pattern. Fold into the same change as F-S01-62-03.
- **Cross-reference:** F-S01-62-03. R20 group 2.

---

**F-S01-62-12** MEDIUM -- Class D -- The index has no field recording seat family, so the carry split is unverifiable on shipped bytes

- **Locus:** `r20_findings_index.json` top-level keys and `findings[]` record schema; claim at `xz_protocol_v0_62.md:5` and in the v0.62 entry.
- **Substance:** Section 22.1 makes carrying-seat eligibility a function of model family -- producer-family (Claude) seats are advisory, Kimi and GLM are eligible, GPT self-disqualified. The index records `carrying_halts: 4` and `advisory_halts: 6` but ships no vendor or family field on either the seat list or the finding records, so the partition that determines what binds cannot be checked against the bytes. Separately, the index declares 10 seats and 10 HALT verdicts while only 6 seats contributed findings; the register header emits "ten-seat audit" from `len(seats)`, and 4 seats (`S01F, S01C, S04F, S04C`) carry HALT verdicts with no recorded finding basis.
- **Evidence:** Index top-level keys: `['round','version_under_audit','target_version','seats','triage_date','verdicts','carrying_halts','advisory_halts','findings','convergence_groups','unique_findings_noted']`. Finding-record keys: `['finding_id','seat','source_severity','defect_class','convergence_group']`. Distinct seats appearing in `findings[]`: 6. Substring search for vendor/family keys across the index: none.
- **Disposition:** Add a `family` (or `vendor`) field to the seat records and gate `carrying_halts` as the count of HALT verdicts from carry-eligible families per Section 22.1. Record at least one finding ID per HALT verdict, or record explicitly that a seat HALTed on a ground carried in another seat's finding.
- **Cross-reference:** Section 22.1. F-S01-62-05 (the 8/10 versus 6-seat gap has the same root: seats present in the verdict list but absent from the finding records). Boundary 34 (unbound execution attestation) is the nearest adjacent disclosure.

---

**F-S01-62-13** LOW -- Class C -- Cardinal-over-list claim in Section 22.2 is outside every gate's scope

- **Locus:** `xz_protocol_v0_62.md:718`, Section 22.2.
- **Substance:** The text reads "nine recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, and v0.47" -- a cardinal of nine over a seven-locus enumeration with no per-locus multiplicity stated. The claim may be correct (the v0.10 entry records two violations in the v0.4/v0.9 pair alone), but it is not checkable from the sentence, and no gate covers it: `[9d]` matches ordinals adjacent to "recurrence"/"round" in the current entry only, and `[9e]` matches only "N consecutive (v0.X through v0.Y)" patterns, of which the v0.62 entry contains zero. Recorded as unverifiable, not as false.
- **Evidence:** `grep -o "nine recorded in-place mutations[^)]*)"` returns the seven-locus list. `[9e]` `range_claims` over the v0.62 entry: empty set, gate vacuous this round.
- **Disposition:** Either state the multiplicity ("nine recorded in-place mutations across seven versions: two at v0.4, ...") or reduce the cardinal to the enumeration length. Optionally widen `[9e]` to cover cardinal-over-list constructions in the body, which would also cover the boundary-count pattern already gated by `[ENUMERATED]`.
- **Cross-reference:** Boundary 23 ([9e] silent vacuity) -- correctly pre-disclosed, and confirmed vacuous this round. Section 22.3 Class C.

---

### Finding summary

| Severity | Count | IDs |
|---|---|---|
| HIGH | 5 | F-S01-62-01, -02, -03, -04, -05 |
| MEDIUM | 4 | F-S01-62-06, -07, -08, -12 |
| LOW | 4 | F-S01-62-09, -10, -11, -13 |
| **Total** | **13** | |

| Class | Count | IDs |
|---|---|---|
| **A (byte-level error) -- HALT-grade** | **7** | -01, -02, -03, -04, -05, -06, -08 |
| B (concealed defect) -- HALT-grade | 1 | -10 |
| C (disclosed boundary) | 1 | -13 |
| D (gate limitation) | 4 | -07, -09*, -11, -12 |

\* F-S01-62-09 is classed A on substance (wrong count on shipped output) and is listed once above; it appears in the D column only as a note that its remedy is a gate addition. Canonical class: A.

---

## S8. Barzakh self-check

Each finding put through the three gate questions before entry into this record.

| Finding | Q1 Authority | Q2 Methodology | Q3 Lineage |
|---|---|---|---|
| -01 | Execution: `grep -c` -> 0 across packet, schema census, three cited loci. Not assertion. | Seven-Layer L6 (methodology audit) + L3 (cross-layer). Evidence matches: a claim at one surface, absence at three others. | Recurrent class, novel instance. `METHODOLOGY_v2.txt:92` names the class; the `source_finding_id` instance is new at v0.62. |
| -02 | Execution: probe P-3 applied, register regenerated, byte-comparison performed. Landed. | L4 (adversarial). GAN-convergence standard met: the generator's output is invariant to a mutation that should change it. | Recurrent class, explicitly named in `METHODOLOGY_v2.txt:92` ("receipt is structural ... checks by substring"). This seat did not read prior seat reports; the recurrence is established from the shipped methodology document. |
| -03 | Execution: probe P-1 landed with benign control P-1b clean; code lines cited. | L4 + L3. Discriminator failed to discriminate a semantically invalid seat value. | Recurrent substance, relocated substrate. Prior instance is R20 group 2 as recorded in the shipped triage. |
| -04 | Execution: probe P-2 landed; rejecting control P-10 fired, isolating the direction. | L4. The paired-direction design is what makes the finding a direction claim rather than a coverage guess. | Recurrent substance (R20 group 5), novel direction. |
| -05 | Execution: regex census over the isolated entry; index cardinality computed. | L3 (cross-layer consistency). Two surfaces in one entry, both cited. | Recurrent class (count claims), novel instance. |
| -06 | Execution: both shipped artifacts read and quoted; probe P-8 shows the pair is ungated. | L3 + L4. | Novel at this seat. |
| -07 | Execution: probe P-4 landed. | L4. | Adjacent to -02; separated because the mechanism differs (skip versus weak check). |
| -08 | Execution: as-shipped run, byte-level root-cause diagnosis, post-repair re-run. | L1 (code execution) + L6. | Novel. Boundaries 10 and 11 are adjacent but do not cover it. |
| -09 | Execution: three runs, stable count. | L1 + L6. | Novel instance of the count class. |
| -10 | Execution: entry-date census across three versions; sabotage S-3 to establish gate absence. | L3 + L4. | Novel instance; boundary 32 is the disclosed enabling condition. |
| -11 | Execution: probe P-6, exception type recorded verbatim. | L4. | Subordinate to -03. |
| -12 | Execution: schema census over index keys; distinct-seat count computed. | L3 + L7 (boundary disclosure). | Novel at this seat. |
| -13 | Execution: grep for the sentence; `[9e]` match set computed as empty. | L7. Correctly stated as unverifiable, not false -- the lens does not license a falsity claim without the underlying mutation record. | Boundary 23 pre-discloses the gate vacuity. |

**Self-check outcome:** 13 of 13 findings carry execution evidence with a cited command or code locus. Zero findings rest on "the code appears incorrect." Three findings (-05 item 11, -13, and the R20 group-3 discharge at S3) are recorded as NOT VERIFIABLE rather than REFUTED, because the artifacts needed to falsify them (the R19 index, the full mutation ledger, the R20 raw reports) are not shipped. Stating unverifiability where it exists is the Sidrat discipline; converting it into a falsity claim would be the wicked-soul answer to Q1.

**Producer-family disclosure.** This seat shares the producer's architecture. Findings -02, -03, and -04 are all instances of one habit -- writing a sentence that generalizes past what the code implements -- and I have no basis to claim immunity from it in this report. The concrete guard applied: every claim above is either a command with recorded output, a cited line number, or explicitly marked NOT VERIFIABLE.

---

## S9. Prediction scorecard

| # | Prediction | Outcome | Evidence |
|---|---|---|---|
| P1 | CI-1R PASS | **CONFIRMED** | All three generated artifacts byte-exact in the shipped protocol. |
| P2 | CI-8 `source_finding_id` resolves | **REFUTED** | Field absent from all shipped bytes; index defers it to R21. F-S01-62-01. |
| P3 | ASSERTED < 15% | **CONFIRMED** | 1 of 9 tags = 11.1%. |
| P4 | If Class A, on CI v0.3.2 entry claims (Iblis Level 3-4) | **CONFIRMED** | 5 of 7 Class A findings (-01, -02, -03, -04, -05) are claims about the CI v0.3.2 repairs. The remaining two (-06, -08) are at the triage and packet layers. |
| P5 | Count-list invariant holds | **CONFIRMED (gated scope)** | Boundary list 35 declared, 35 items, 35 emitted, byte-exact. Note that the invariant holds only where it is gated: F-S01-62-05 and -13 are count-list divergences outside `[9d]`/`[9e]` scope. |
| P6 | Append-only holds (62/62 seals) | **CONFIRMED** | 62 ENTRY + FULL_SECTION_27 + 1 PRIOR_HISTORY; derivation succeeds; sabotage S-2 detected. |
| P7 | Code layer clean (186 GREEN) | **CONFIRMED** | 186 passed in 11.09s, 6-suite explicit. |
| P8 | Packet 19/19 OK | **REFUTED as shipped** | 15/19 FAILED using the documented extraction procedure; 19/19 only after an undocumented repair. F-S01-62-08. |
| P9 | M3 receipt on any mixed group now structural | **REFUTED (split)** | "Any mixed group": CONFIRMED. "Structural": REFUTED -- substring containment. Probe P-3. |
| P10 | Seat count from `findings[].seat` | **CONFIRMED (mechanism), DEFECTIVE (validation)** | Probe P-1 proves the field load-bearing and proves it unvalidated. |
| P11 | VERSION-1 gate catches stale bounds | **CONFIRMED** | Sabotage S-1 fired with the correct diagnostic. |
| P12 | Section 22.2/22.3 at v0.61 | **CONFIRMED** | "v0.1 through v0.61" and "v0.38-v0.61" both present and gated. |
| P13 | Bidirectional membership parity enforced | **REFUTED** | Unidirectional. Probe P-2. F-S01-62-04. |
| P14 | Noted-finding bypass removed | **CONFIRMED** | No noted-status branch in cross-layer validation; probe P-9 rejected. |
| P15 | H = 1.0 continues (Class A present) | **CONFIRMED** | 7 Class A findings. |

**Scorecard totals:** 9 CONFIRMED, 4 REFUTED (P2, P8, P9, P13), 2 CONFIRMED-with-qualification (P5, P10). Zero VACUOUS.

The four refutations cluster: P2, P9, and P13 are each a CI v0.3.2 upgrade that the entry describes more completely than the code implements. P8 is the packet layer. Every one of the producer's HIGH-confidence predictions about the *mechanism* held; every refutation is a prediction about a *claim*.

---

## S10. Verdict

### **HALT** (advisory -- zero carry weight)

Seven Class A findings and one Class B finding. Section 22.3 makes both HALT-grade. Section 22 item 7's persistent-architectural-HALT exception is not invoked: none of these findings is architectural in the sense of boundaries 18, 19, or 35. All eight are repairable within the existing architecture, and five are single-conditional code changes.

This verdict binds nothing. This seat is producer-family (Claude), advisory under Section 22.1, and the finding above at F-S01-62-12 notes that the shipped index has no field by which a carrying/advisory partition could be checked at all.

### Key question: does v0.62 break the R7-R20 Class A streak?

**No. R7-R21 is now 15/15. H = 1.0 continues. Laplace P(Class A at R22) = 16/17 = 0.941.**

The observation worth recording is not that the streak held but *where* it held. Every finding in this report that carries Class A severity lives in a hand-written sentence describing a mechanism. The mechanisms themselves were clean at every point I could execute against them: CI-1R byte-exact on three artifacts, 186/186 pytest, 62/62 seals with mutation detection proven by sabotage, the VERSION-1 gate proven by sabotage, dangling references rejected, stale receipts on newly-mixed groups rejected, and the ID-parsing defect genuinely replaced by field lookup. Four rejecting controls fired with correct diagnostics. Not one scribe erred.

The four CI v0.3.2 upgrades and their fate at this seat:

| Upgrade | Mechanism | Claim about the mechanism |
|---|---|---|
| Receipt on any mixed distribution | Implemented | Accurate |
| Receipt validation structural | Implemented as containment | **Overstated** |
| Seat count from authoritative field | Implemented | **Overstated** ("authoritative" implies validated) |
| Bidirectional parity | Implemented one direction | **Overstated** ("bidirectional") |
| Noted-bypass removal | Implemented | Accurate |
| `source_finding_id` | **Not implemented** | **Stated as done** |

Three of six claims outrun their implementations by roughly one adjective each -- "structural", "authoritative", "bidirectional" -- and one claims a field that does not exist. This is the Level 3 Iblis surface that `METHODOLOGY_v2.txt:120` predicts: "The claim that the mechanism works IS the Class A, because the claim outstrips the implementation." The dispatch predicted its own defect class at P4 with HIGH confidence and was right.

The narrowing is real and should be credited. R20's four defect classes were *in the code*. R21's Class A findings are, with two exceptions at the packet and triage layers, *in four adjectives about the code*. The lesion migrated from the mechanism to the sentence describing the mechanism, and the sentence is now short enough to gate.

The residual that R21 exposes and that no CI version yet addresses: **the audit-support layer is now itself an ungated Class A surface.** `AUDIT_CONTEXT.txt` asserted 248 PASS (247), asserted 19/19 OK (15 failed as shipped), and asserted `source_finding_id` added (absent). Those three claims sit outside `PACKET_SHA256SUMS`, outside `build.py`, and outside `HISTORY.sha256`. The protocol's own verification surface has been hardened to the point where the dispatch that describes it is the weakest link -- and this round, the first thing that failed was the first command an auditor was told to run.

---

*Report produced by Seat S01 (Claude Opus 5), advisory, fresh-instance, XZ Protocol v0.62 Convergence Round 21. All verdicts derived from executed evidence on digest-verified bytes. Bismillah.*

---

# Bismillah ir-Rahman ir-Rahim
