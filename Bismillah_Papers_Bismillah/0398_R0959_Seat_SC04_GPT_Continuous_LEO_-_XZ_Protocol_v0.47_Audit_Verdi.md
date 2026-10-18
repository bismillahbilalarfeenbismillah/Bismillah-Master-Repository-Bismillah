# Bismillah ir-Rahman ir-Rahim

# R0959 -- Seat SC04 GPT Continuous LEO - XZ Protocol v0.47 Audit Verdict

**Chronological Index:** 398 of 995  
**Date:** 2026-07-31  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SEAT_SC04_GPT_CONTINUOUS_LEO_VERDICT_v0_47.md  
**Source Format:** md  
**SHA-256:** `deb1ba5a38f4ae3fe636449df1e25e7ecbee755ada7f37d102198cc21a02f53b`  

---

## R0959 · Seat SC04 GPT Continuous LEO - XZ Protocol v0.47 Audit Verdict

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SEAT_SC04_GPT_CONTINUOUS_LEO_VERDICT_v0_47.md
- source_format: md
- text_sha256: deb1ba5a38f4ae3fe636449df1e25e7ecbee755ada7f37d102198cc21a02f53b

# Seat SC04 GPT Continuous LEO - XZ Protocol v0.47 Audit Verdict

**Seat:** SC04 GPT Continuous LEO (Adversarial)
**Finding prefix:** `F-SC04-47`
**Artifact:** XZ Protocol v0.47 DRAFT CANDIDATE
**Audit posture:** Continuous from R5 Seat 04, LEO baseline, substrate-wins
**Final verdict:** **HALT**

## 1. Executive result

The v0.47 reconstructed packet is mechanically GREEN but structurally non-convergent.

Mechanical verification succeeded:

- `sha256sum -c PACKET_SHA256SUMS`: rc=0, 16/16 listed members OK.
- `python3 build.py`: rc=0, `BUILD PASSED: all checks GREEN`.
- Canonical six-suite pytest invocation: 186 passed.
- Protocol text: exactly 294,529 bytes and 1,223 lines.
- Reconstructed packet: 16 manifested members plus `PACKET_SHA256SUMS` = 17 shipped files.
- Code/test partition: 6 code modules + 6 test suites = 12 distinct Python files.
- All 12 Python files contain the v0.47 stamp; trust roots identifies `XZ Protocol v0.47`.
- 47 amendment entries are present and all 47 current HISTORY entry seals match the current protocol bytes.
- `FULL_SECTION_27` and the internally derived current `PRIOR_HISTORY` value pass the shipped build.
- Current register parses as 10 items: 2 HIGH, 8 MEDIUM.
- Current provenance tags parse as COMPUTED=0, EXTERNAL=1, ASSERTED=5.
- EXTERNAL count 1 is mechanically reproduced.

These GREEN gates do not establish append-only truth against the externally held prior packet. Four audit findings remain, including three independent Class A blockers. The immediate prior v0.46 historical entry was silently rewritten, the controlling v0.47 dispatch advertises the prior v0.46 packet digest, and the current standing-boundary cardinal is false.

## 2. Mechanical receipt

| Check | Result |
|---|---|
| `sha256sum -c PACKET_SHA256SUMS` | PASS, 16/16 |
| SHA-256 of current `PACKET_SHA256SUMS` | `faee04bf5bcf6049b365ba63a4904dee8b43f5e7e721278200ee1c6c167a434c` |
| SHA-256 of protocol | `adf601f25dc5ab4d1c62aacfb1b0912e257e643434150e317ce6096cdb1a37ae` |
| SHA-256 of current `HISTORY.sha256` | `13d3430913f6619719fea6dcfffc48f101167bfc2c48339f6355b84bd8b6124b` |
| Protocol size | 294,529 bytes |
| Protocol lines | 1,223 |
| `build.py` | BUILD PASSED |
| Canonical tests | 186 passed |
| Amendment entries | 47 |
| Register items | 10 |
| Current boundary declaration | 29 |
| Current boundary items actually enumerated | 30 |
| Current `PRIOR_HISTORY` | `c51b64e9e2d1e9855828970de200f324e117302b10fc972fc8a5edfa659e25bf` |

Environment used for executed verification: Python 3.13.5.

## 3. Continuity verification of the two prior Seat 04 findings

### F-S04-46-01 - build.py stale self-version

**CLOSED on current bytes.**

The v0.47 `build.py` docstring now identifies itself as the v0.47 build verifier, `VERSION = "0.47"`, and new gate `[2d]` extracts the docstring version and requires equality with `VERSION`. The repair is therefore both present and mechanically enforced.

### F-S04-46-02 - trust-roots timestamp disposition mismatch

**CLOSED in substance by correction (ay).**

Direct cross-version verification:

- v0.45 trust roots generated timestamps were dated `2026-07-31`.
- the actually shipped v0.46 trust roots had already been refreshed to `2026-08-07T20:00:00.000000Z`;
- the v0.46 register nevertheless called the timestamp stale and NOTED;
- v0.47 correction `(ay)` now records that the byte repair had landed and re-dispositions the stale-timestamp component CLOSED;
- the remaining fact that no gate binds the generated timestamps is disclosed as a standing boundary.

The prior Seat 04 timestamp finding is therefore substantively repaired. The separate boundary-cardinality defect in Finding `F-SC04-47-03` does not reverse this closure.

## 4. Correction and body-repair matrix

| Repair | Result | Byte verification |
|---|---|---|
| `(ay)` timestamp disposition | PASS | Actual v0.46 trust roots carry the refreshed 2026-08-07 timestamps; v0.47 now records the repair and preserves the ungated-timestamp residual as a disclosure. |
| `[a]` front-matter status | PASS | Front matter is v0.47 DRAFT CANDIDATE and matches Section 0.1. |
| `[b]` Section 22.2 range | PASS | Current text says carried entries `v0.1 through v0.46`. |
| `[c]` Section 22.3 lineage | PASS | Current text carries the exception at `v0.38-v0.47`. |
| `[d]` FB-7b version status | PASS | Section 25 states `PENDING RE-CARRY v0.47`. |
| `[e]` FB-7b post-v0.31 rationale | PASS | Section 25 now mentions Convergence Rounds 2-5 on v0.43-v0.46 and the v0.46 Kimi Seat 2 CONDITIONAL PASS. |
| `[f]` build self-version | PASS | Docstring changed to v0.47 and gate `[2d]` enforces parity. |
| `[g]` R4 seat qualification | **FAIL structurally** | The intended wording is present only because the already-sealed v0.46 amendment entry was changed in place. That is not an append-only repair. See `F-SC04-47-02`. |

## 5. Append-only comparison against the actual prior v0.46 Seat 04 packet

I compared the v0.47-carried Section 27 history directly against the prior `DISPATCH_S04_GPT_LEO_v46 (1).zip` supplied to this seat in the preceding round.

Results:

- v0.1 through v0.45 entries are byte-identical.
- v0.46 is **not** byte-identical.
- The prior v0.46 first line said:

```text
Convergence Round 4 on v0.45 bytes: 4 fresh seats (Opus 5, Kimi K3, Gemini, GPT), 4 families, 1 shell (LEO).
```

- The v0.47-carried historical v0.46 entry instead says:

```text
Convergence Round 4 on v0.45 bytes: 4 deployed seats (Opus 5, Kimi K3, Gemini, GPT; 3 with verified independence, 1 with independence structurally false per F-S01-45-00), 4 families, 1 shell (LEO).
```

The historical entry seal changed accordingly:

```text
actual prior v0.46 packet:
121e144e566b47e3bbdc998092849c179e32f3e1c73312f9862dec56747c57e7  ENTRY_v0.46

v0.47 current HISTORY:
36f1787a6c34ad16cba769f2d3610ad24e506184f456abc7c8eb2e21906d2f0a  ENTRY_v0.46
```

The external history anchor also fails:

```text
SHA-256(actual prior v0.46 HISTORY.sha256)
= 558b2a2c91af4ee5e1ecc52c377d92534129d710e3ef3aa2aec9367ebed83325

v0.47 shipped PRIOR_HISTORY
= c51b64e9e2d1e9855828970de200f324e117302b10fc972fc8a5edfa659e25bf
```

The shipped build reports the latter as valid because it reconstructs the previous history from the already-rewritten current Section 27 and the regenerated current seals. That proves internal self-consistency, not preservation of the externally held prior bytes.

## 6. Standing-boundary cardinality

The v0.46 current entry enumerated 27 standing boundaries. v0.47 retains all 27 and adds:

1. `build.py f-string nested quotes require Python 3.12+ (F-S07-46-02)`
2. `[3a] fb_spec omits FB-7b locus assertion (F-S07-46-03)`
3. `trust-roots generated timestamp ungated`

That produces **30**, not 29.

The dispatch says the boundary count goes from 27 to 29, and the v0.47 current entry says `Disclosed standing boundaries -- 29 items`. Both are false against the enumerated bytes.

## 7. Findings

### F-SC04-47-01

**Severity:** HIGH

**Locus:** `prompt.txt` packet-identity line; reconstructed v0.47 `PACKET_SHA256SUMS`; prior v0.46 `PACKET_SHA256SUMS`.

**Evidence:** The v0.47 prompt advertises `PACKET_SHA256SUMS = 0c5f7264...`. Direct SHA-256 of the current reconstructed v0.47 `PACKET_SHA256SUMS` is `faee04bf5bcf6049b365ba63a4904dee8b43f5e7e721278200ee1c6c167a434c`. The full stale value `0c5f7264f77db9054b03627c37d45d9153df9e195c97f1981a4d1a78d4a8a431` is exactly SHA-256 of the prior v0.46 `PACKET_SHA256SUMS`.

**Substance:** The controlling v0.47 dispatch carries forward the prior version's packet identity. The dispatch expressly tells the auditor to verify this value from shipped bytes, and the shipped bytes refute it. Member-level manifest verification remains GREEN, but the advertised packet anchor is byte-false.

**Class:** Class A - byte-false packet-identity O-CLAIM.

**Disposition:** OPEN / BLOCKING. Replace the stale packet-digest surface in a successor dispatch with a value computed from that successor's actual `PACKET_SHA256SUMS`. Do not preserve `0c5f...` as the v0.47 packet identity.

### F-SC04-47-02

**Severity:** CRITICAL

**Locus:** current protocol carried v0.46 entry; actual prior v0.46 protocol; current and prior `HISTORY.sha256`; current repair `[g]`.

**Evidence:** The prior v0.46 entry's `4 fresh seats` text was changed in v0.47 to `4 deployed seats ... 3 with verified independence, 1 ... false`. `ENTRY_v0.46` changed from `121e144e566b47e3bbdc998092849c179e32f3e1c73312f9862dec56747c57e7` to `36f1787a6c34ad16cba769f2d3610ad24e506184f456abc7c8eb2e21906d2f0a`. The actual prior v0.46 HISTORY hash is `558b2a2c91af4ee5e1ecc52c377d92534129d710e3ef3aa2aec9367ebed83325`, while v0.47 ships `PRIOR_HISTORY c51b64e9e2d1e9855828970de200f324e117302b10fc972fc8a5edfa659e25bf`.

**Substance:** Repair `[g]` was implemented by silently editing the already-sealed immediate-prior amendment entry instead of appending a v0.46 correction in the v0.47 entry. This violates the protocol's explicit append-only rule. It also demonstrates the disclosed self-consistent-regeneration blind spot in practice: the current build is GREEN because the rewritten entry, seals, FULL_SECTION_27, and PRIOR_HISTORY derivation were regenerated together, while the externally held prior packet disproves continuity.

**Class:** Class A - append-only provenance violation and external-anchor mismatch.

**Disposition:** OPEN / BLOCKING. Restore the v0.46 entry byte-for-byte to the actual prior v0.46 packet, restore its original `ENTRY_v0.46` seal, append the R4 independence qualification only as a new correction in a successor current entry, regenerate the successor HISTORY and packet manifest, and bind the successor `PRIOR_HISTORY` to the actual preceding HISTORY bytes rather than a reconstructed rewritten history.

### F-SC04-47-03

**Severity:** MEDIUM

**Locus:** current v0.47 standing-boundary sentence and `prompt.txt` standing-properties claim.

**Evidence:** A top-level parse of the current boundary sentence yields 30 items. The prior 27 are all retained, then three new items are appended: Python 3.12+ f-string requirement, missing FB-7b `[3a]` locus assertion, and ungated trust-root timestamps.

**Substance:** Both the dispatch and protocol claim 29 disclosed standing boundaries. The actual current list has 30. This is the recurrent cardinality-propagation failure class: adding three items to 27 was narrated as 29.

**Class:** Class A - byte-false current numeric O-CLAIM.

**Disposition:** OPEN / BLOCKING. Correct the count to 30, or remove/merge a real boundary with explicit semantic justification. Add a mechanical standing-boundary cardinality gate so the declared count is derived rather than narrated.

### F-SC04-47-04

**Severity:** MEDIUM

**Locus:** v0.47 defect register item (7), body-repair list `[a]-[g]`, bytewise v0.46-to-v0.47 body comparison.

**Evidence:** Register item (7) says `F-S08-46-01 HIGH CLOSED via body repair: boundary list description corrected`. The named body-repair list contains no boundary-list-description repair. A direct comparison of the v0.46 and v0.47 protocol bodies shows no standing-boundary-description correction, and comparison of the standing-boundary lists shows the prior 27 descriptions retained while three new items are appended. The source Seat 8 report is not shipped in this dispatch, so its underlying finding text cannot be independently reconstructed here.

**Substance:** The stated closure basis is not demonstrated by the shipped repair map or the byte delta. At minimum, the closure provenance is unbound. Because the source finding is absent, I do not silently infer what wording the producer intended to change.

**Class:** Class B - unverifiable closure O-CLAIM with a byte-unsupported stated repair basis.

**Disposition:** OPEN / BLOCKING unless specifically downgraded to a disclosed unverifiable claim. Ship/bind the source finding and identify the exact repaired locus, or correct the register disposition. This finding is not needed for the HALT because three independent Class A findings already exist.

## 8. Standing-property conclusions

- 17-file reconstructed packet: verified.
- 16 manifested members: verified.
- 6+6 code/test partition: verified.
- 186 canonical tests: verified.
- v0.47 stamps: verified.
- 47 current internal entry seals: verified against current bytes.
- `FULL_SECTION_27`: internally verified.
- `PRIOR_HISTORY`: internally self-consistent but **not externally faithful to the actual prior v0.46 HISTORY file**.
- Register count 10: verified.
- EXTERNAL count 1: verified.
- Standing-boundary count 29: **false; actual 30**.
- v0.1-v0.45 append-only preservation: verified against available prior packets.
- v0.46 append-only preservation: **failed**.
- F-S04-46-01: closed.
- F-S04-46-02: closed in substance via `(ay)`.
- Overall convergence gate: blocked.

## 9. Required successor repair set

A successor should, at minimum:

1. restore the exact prior v0.46 amendment entry instead of carrying the rewritten version;
2. restore the prior v0.46 entry seal and rebuild the successor chain from the authentic prior bytes;
3. append the R4 independence qualification as a new correction rather than editing v0.46;
4. bind successor `PRIOR_HISTORY` to the actual preceding `HISTORY.sha256` bytes and verify it against an externally held prior packet;
5. compute and publish the successor packet digest from the successor `PACKET_SHA256SUMS`, removing the stale v0.46 `0c5f...` identity;
6. correct the standing-boundary count from 29 to 30 unless the inventory itself is intentionally changed;
7. add a gate that parses and counts the standing-boundary inventory;
8. resolve or explicitly unverify the `F-S08-46-01` closure basis;
9. regenerate all affected current seals, FULL_SECTION_27, protocol hash, and packet manifest;
10. rerun a fresh external-anchor comparison before any non-HALT convergence claim.

## 10. Final disposition

**SEAT SC04 VERDICT: HALT.**

v0.47 improves the prior Seat 04 defects: the self-version gate is real and `(ay)` correctly records the trust-root timestamp repair. Those closures do not survive the higher-level provenance test. The immediate prior historical entry was silently rewritten, the current dispatch advertises the prior version's packet digest, and the current standing-boundary cardinal is wrong. The current GREEN build therefore establishes only self-consistency of the regenerated v0.47 packet, not append-only continuity from the actual v0.46 substrate.

---

# Bismillah ir-Rahman ir-Rahim
