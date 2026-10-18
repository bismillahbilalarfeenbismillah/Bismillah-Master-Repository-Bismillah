# Bismillah ir-Rahman ir-Rahim

# R0224 -- XZ Protocol v0.19 Adversarial Audit

**Chronological Index:** 675 of 995  
**Date:** Undated  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v19_GPT_ADVERSARIAL_REPORT.md  
**Source Format:** md  
**SHA-256:** `2c78fdc8aa00aabe8018d3a3a06944d833a4984e8896644154ef55e897785522`  

---

## R0224 · XZ Protocol v0.19 Adversarial Audit

- section: IV. XZ Protocol
- source_file: XZ_v19_GPT_ADVERSARIAL_REPORT.md
- source_format: md
- text_sha256: 2c78fdc8aa00aabe8018d3a3a06944d833a4984e8896644154ef55e897785522

# XZ Protocol v0.19 Adversarial Audit

## 1. Standing, state, and verdict header

- **Role:** adversarial audit seat.
- **Family relative to producer:** non-producer family. The producer named in the dispatch is Claude/Anthropic; this audit was executed from a GPT-family seat.
- **Binding status:** advisory only. This verdict does **not** bind freeze and does **not** count toward FB-7b carry.
- **Independent state held:** only the current packet bytes and the historical reports shipped inside this packet. I do **not** hold any prior packet outside the archive, so any claim about earlier packages that is not reproducible from the shipped members remains bounded by that absence.
- **Execution status:** EXECUTING. Commands were run locally against the unpacked packet and against isolated mutation copies under `/home/user/workspace/audit_xz_v19/`.
- **Context-age note:** fresh session on this packet only.

**Positive delta before findings.** The normative file digests match the dispatch manifest. The canonical pytest command passes on the untouched package (`186 passed`). The controlled-path build passes on clean bytes. The v2 discipline docs do incorporate several of the Rev B recommendations, including the leakage matrix, mutation-landed requirement, and the removal of the recurrence count from the discipline headers. The false-PASS paths I found are not in the normative code plane; they remain in the amendment-record and methodology layer.

## 2. Findings

### F-GPT19-01 — HIGH — `PRIOR_HISTORY` closure is recorded as COMPUTED, but `build.py` only checks line presence; a false digest passes

- **Location:** `xz_protocol_v0_19.md:869`; `build.py:254-257`
- **Why this matters:** The v0.19 entry closes F-OP18-05 and tags it as `[COMPUTED: build.py [9b] PRIOR_HISTORY check, once implemented.]`, claiming that the `PRIOR_HISTORY` line now enables chained verification without shipping the prior package. But the shipped code does not compare the line's digest to anything. It only checks whether a `PRIOR_HISTORY` line exists and prints a note when present. That leaves the chain anchor decorative rather than executable.
- **Evidence:** `build.py` performs no digest validation after collecting `prior_lines`; it only executes:
  - `prior_lines = [l for l in history_lines if l.startswith("PRIOR_HISTORY")]`
  - `if prior_lines: print("  PRIOR_HISTORY line present (chained control)")`
- **Mutation proof:** In `/home/user/workspace/audit_xz_v19/probe_prior_history`, I replaced the `PRIOR_HISTORY` digest with `000...000`, re-sealed `ENTRY_v*` and `FULL_SECTION_27`, and re-ran the controlled-path build. The build still returned `BUILD PASSED: all checks GREEN` with rc=`0`.
  - Evidence files:
    - `/home/user/workspace/audit_xz_v19/evidence/probe_prior_history_false_pass.txt`
    - `/home/user/workspace/audit_xz_v19/evidence/probe_prior_history_false_pass.rc`
- **Discrimination control:** Corrupting `ENTRY_v0.19` in `HISTORY.sha256` without resealing correctly fails `[9b]`.
  - Evidence files:
    - `/home/user/workspace/audit_xz_v19/evidence/control_history_entry_fail.txt`
    - `/home/user/workspace/audit_xz_v19/evidence/control_history_entry_fail.rc`
- **Suggested fix:** Parse `PRIOR_HISTORY`, require exactly one line, and compare its digest against a shipped or embedded previous-history anchor. If the project wants prior-package-free chaining, ship the prior `HISTORY.sha256` digest in a machine-checked field and fail on mismatch or absence.

### F-GPT19-02 — HIGH — the claimed provenance ledger is not implemented; tags are decorative, incomplete, and one shipped `EXTERNAL` tag is invalid

- **Location:** `xz_protocol_v0_19.md:865,869,871`; `build.py:265-273`
- **Why this matters:** The v2 discipline makes the provenance ledger the headline metric for the round. The v0.19 entry claims: `The claim provenance ledger (COMPUTED/EXTERNAL/ASSERTED tags on every entry claim) is implemented in this entry. [COMPUTED: build.py [11].]` That is false in three ways:
  1. `build.py [11]` prints only total/body/Section-27 character counts; it does not parse, count, or validate provenance tags.
  2. The v0.19 entry contains many untagged factual claims.
  3. The only shipped `EXTERNAL` tag points to `XZ_v18_SEAT_A_REPORT_REV_B.md`, which is an in-packet member with no digest in any shipped text, so it is not "state the producer does not control" under D-3.2.
- **Evidence:**
  - D-3.2 definition requires `EXTERNAL -- verified against state the producer does not control; name the holder and digest.` See `AUDIT_DISPATCH_DISCIPLINE_v2.md:79-87`.
  - `build.py` contains no logic for `COMPUTED`, `EXTERNAL`, or `ASSERTED`; the only occurrences of those strings are in `xz_protocol_v0_19.md`.
  - Packet coverage check: 33 shipped members total, 16 digested anywhere in shipped text, 17 undigested. The undigested set includes `XZ_v18_SEAT_A_REPORT_REV_B.md`, `build.py`, `HISTORY.sha256`, `AUDIT_DISPATCH_DISCIPLINE_v2.md`, `SEAT_STANDING_ORDERS_v1.md`, and `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md`.
- **Mutation proof:** In `/home/user/workspace/audit_xz_v19/probe_provenance_tags`, I changed `[COMPUTED: build.py [9a].]` to `[ASSERTED: build.py [9a].]`, re-sealed Section 27, and re-ran the controlled-path build. The build still returned `BUILD PASSED: all checks GREEN` with rc=`0`.
  - Evidence files:
    - `/home/user/workspace/audit_xz_v19/evidence/probe_provenance_tag_false_pass.txt`
    - `/home/user/workspace/audit_xz_v19/evidence/probe_provenance_tag_false_pass.rc`
- **Discrimination control:** A genuine body-gated mutation still fails: changing Section 22 item 6 from `gate execution is a build-time convenience` to `gate execution is the carry check` correctly trips `[10]`.
  - Evidence files:
    - `/home/user/workspace/audit_xz_v19/evidence/control_s22_phrase_fail.txt`
    - `/home/user/workspace/audit_xz_v19/evidence/control_s22_phrase_fail.rc`
- **Suggested fix:** Move the amendment entry to structured claim data, generate the prose from that structure, require exactly one provenance tag per claim unit, forbid `EXTERNAL` unless it carries a holder plus an independently anchored digest, and make `build.py` fail on missing, duplicate, or invalid tags. Also print the `COMPUTED/EXTERNAL/ASSERTED` counts and the ASSERTED fraction from the parsed structure, not from prose.

### F-GPT19-03 — MEDIUM — v0.19 reintroduces the forbidden recurrence ordinal and contradicts its own "no ordinal asserted" disclosure

- **Location:** `xz_protocol_v0_19.md:865,869`; `AUDIT_DISPATCH_DISCIPLINE_v2.md:8-11`; `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md:9-14`
- **Why this matters:** The new v2 discipline documents explicitly say not to narrate a recurrence ordinal until a recurrence table exists. The v0.19 entry nevertheless states `The twelfth Axiom-3 recurrence...` in its opening sentence. Later in the same entry, under the disposition of F-OPUS5-17-06, it says the ordinal is not derivable from the record and that `this entry does not assert one.` Those two statements cannot both be true.
- **Evidence:**
  - `AUDIT_DISPATCH_DISCIPLINE_v2.md:8-11`: `Where a count is needed, cite the recurrence table; if the table does not yet exist, say the count is not derivable and stop.`
  - `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md:9-14`: same correction, directed at the producer side.
  - No recurrence table ships in the packet; only prior reports recommending one are present.
- **Impact:** This is not just an unsupported aside. It directly undercuts the v0.19 claim that the v2 discipline was integrated into the amendment-entry practice.
- **Suggested fix:** Remove the ordinal sentence entirely, or ship a machine-maintained recurrence table and make the entry derive its count from that table. Also reconcile the opening sentence with the later `this entry does not assert one` disclosure.

## 3. S-1 preregistration note

I did **not** freeze S-1 predictions before opening the amendment entry. That is a method miss on my side, and I am recording it rather than backfilling a fake preregistration. I therefore do **not** claim a valid HELD/REFUTED preregistration result for this round.

## 4. Execution proof

### Environment

- Working root: `/home/user/workspace/audit_xz_v19/`
- Untouched audit tree: `/home/user/workspace/audit_xz_v19/repo/`
- Python:
  - `/usr/local/bin/python3` -> `Python 3.14.3`
  - `/usr/bin/python3` -> imports `pytest`
- `pytest` CLI: `/usr/bin/pytest`, version `9.0.2`

### Baseline commands

1. Digest verification on the 14 normative files:
   - Output: `/home/user/workspace/audit_xz_v19/evidence/baseline_sha256.txt`
2. Canonical pytest command:
   - Command: `pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py -q`
   - Result: `186 passed`
   - Output: `/home/user/workspace/audit_xz_v19/evidence/baseline_pytest.txt`
3. Build on clean bytes:
   - `python build.py` -> rc=`1` in this environment
   - `PATH=/usr/bin:$PATH /usr/bin/python3 build.py` -> rc=`0`
   - Outputs:
     - `/home/user/workspace/audit_xz_v19/evidence/baseline_build_default_path.txt`
     - `/home/user/workspace/audit_xz_v19/evidence/baseline_build_default_path.rc`
     - `/home/user/workspace/audit_xz_v19/evidence/baseline_build_controlled_path.txt`
     - `/home/user/workspace/audit_xz_v19/evidence/baseline_build_controlled_path.rc`

### Verbatim environment exception

The default-path build fails because `build.py` shells out to `python3 -m pytest` and `python3` resolves to `/usr/local/bin/python3`, which does not have `pytest` installed:

```text
ModuleNotFoundError: No module named 'pytest'
```

This is a tooling-harness defect in the shipped build path, not a normative-file integrity defect. I did **not** grade it as a primary finding because the controlled-path build passes and the user asked to prioritize the audit boundary with minimal spend.

### Sealed nonce

I did not find a sealed nonce or challenge value in `DISPATCH_v19_ADVERSARIAL.md`. D-5 references one, but the current dispatch file does not expose it.

## 5. Claim provenance ledger

### Method

I used a **conservative atomic-claim ledger** over the v0.19 amendment entry. I split the entry into 36 claim units. I only credited `COMPUTED` where a shipped check on current bytes directly enforces the claim in a way that would fail on contradiction. I credited **no** `EXTERNAL` rows because the entry's only `EXTERNAL` tag points at an in-packet, unhashed report rather than independent state with holder plus digest.

### Headline number

- **Claim units:** 36
- **COMPUTED:** 3
- **EXTERNAL:** 0
- **ASSERTED:** 33
- **ASSERTED fraction:** **91.7%**

This is the round's headline number. The amendment-entry boundary is still overwhelmingly asserted.

### Ledger

| # | Claim unit | Provenance | Evidence / reason |
|---|---|---|---|
| 1 | Rev A findings F-OP18-01..10 absorbed | ASSERTED | No shipped check reads the amendment-entry narrative |
| 2 | Rev B findings F-OP18-11..13 plus five discipline defects absorbed | ASSERTED | Same |
| 3 | Rev A verdict/severity was HALT, 0/3/4/3 | ASSERTED | In-packet report only; no independent holder/digest |
| 4 | Rev B added 0/0/2/1 and retracted one void probe | ASSERTED | In-packet report only |
| 5 | `The twelfth Axiom-3 recurrence ...` / uncovered-surface characterization | ASSERTED | No recurrence table ships; no gate |
| 6 | The v0.18/Claude contradiction described in the opening sentence | ASSERTED | Depends on non-shipped v0.17 Claude report |
| 7 | Governance: four consecutive producer-family advisory cycles, none non-producer since v0.14 | ASSERTED | No machine-maintained governance table ships |
| 8 | F-OP18-01 is correctly dispositioned CLOSED here | ASSERTED | Cross-document truth claim; no gate |
| 9 | F-OP18-02 is CLOSED | ASSERTED | I did not rely on an independently re-run FB-row mutation for the ledger |
| 10 | F-OP18-03 is CLOSED IN PART | ASSERTED | Amendment-entry narrative only |
| 11 | F-OP17-06 disclosure reason is accurate | ASSERTED | No gate reads this disposition |
| 12 | F-OP17-09 disclosure reason is accurate | ASSERTED | Same |
| 13 | F-OPUS5-17-06 disclosure reason is accurate and no ordinal is asserted | ASSERTED | Contradicted by row 5 in the same entry |
| 14 | F-OPUS5-17-07 is dispositioned by build `[11]` | ASSERTED | Coverage print exists; disposition semantics are narrative |
| 15 | F-OPUS5-17-09 is CLOSED via `get_body()` | ASSERTED | No direct mutation evidence included in this audit |
| 16 | F-OPUS5-17-10 is DISCLOSED because `build.py` is tooling outside the manifest | ASSERTED | Narrative classification |
| 17 | F-OPUS5-17-11 needs no disposition | ASSERTED | Narrative classification |
| 18 | F-OP18-04 note on attribution/routing is accurate | ASSERTED | In-packet reports only; no external anchor |
| 19 | F-OP18-05 deferral reason in v0.18 was false because prior `HISTORY.sha256` shipped | ASSERTED | v0.17 packet itself not shipped here |
| 20 | `HISTORY.sha256` now carries a `PRIOR_HISTORY` line with the stated digest | ASSERTED | The line exists, but no shipped gate fails if it is wrong |
| 21 | That line enables chained verification without shipping the prior package | ASSERTED | Probe falsified this; wrong digest passes |
| 22 | F-OP18-06 tally should be eight; entry asserts no ordinal | ASSERTED | No machine-derived tally table ships |
| 23 | F-OP18-07 reconciliation rule and `94353b3c...` residual are correctly stated | ASSERTED | No gate or external receipt in packet |
| 24 | F-OP18-08 surjectivity route exists | ASSERTED | `build.py` checks it on clean bytes, but I did not classify this row as computed without a dedicated mutation in the ledger |
| 25 | F-OP18-10 route exists | ASSERTED | Same conservative rule |
| 26 | F-OP18-11 prose-citation verifier exists; full packet manifest does not | ASSERTED | Route exists in code; packet-manifest absence verified by inspection |
| 27 | F-OP18-12 coverage measurement exists | ASSERTED | `build.py` prints it, but does not fail if the prose about the ledger is false |
| 28 | The claim provenance ledger is implemented in this entry | ASSERTED | Probe falsified this; tags are decorative and incomplete |
| 29 | F-OP18-13 ordering assertion exists | ASSERTED | Conservative classification; no dedicated mutation in ledger |
| 30 | v2 discipline framework is integrated | ASSERTED | Prose claim about methodology absorption |
| 31 | All 12 code files and trust roots are stamped `v0.19` | COMPUTED | `build.py [2]` checks stamps on clean bytes and would fail on stale stamp |
| 32 | Section 25 digests were recomputed by targeted body-only replacement | ASSERTED | No shipped route checks the replacement method |
| 33 | Normative manifest digest equals `c4937e...dcc40d` | COMPUTED | Independently recomputed; `build.py [3]` checks the actual digest against current bytes/body |
| 34 | Six suites, 186 tests, all GREEN | COMPUTED | Canonical pytest run passed; `build.py [5]` and `[8]` enforce current count/result |
| 35 | Status is DRAFT CANDIDATE -- NOT FROZEN | ASSERTED | Prose claim only |
| 36 | FB-7b is OPEN | ASSERTED | Section 25 row states it, but no machine-checked carry state exists |

## 6. Hedge and deferral audit

- **F-OP18-03 CLOSED IN PART:** mostly honest in form, but one constituent reason is false. The entry says F-OPUS5-17-06 remains disclosed because `this entry does not assert` an ordinal, while the opening sentence does assert `The twelfth Axiom-3 recurrence...`.
- **F-OP18-05 CLOSED:** the reason that the prior `HISTORY.sha256` shipped is plausible, but the stated closure basis is false. The shipped code does not perform chained verification; it checks only line presence.
- **F-OP18-11 CLOSED IN PART:** honest in part. The full-packet-manifest absence is disclosed accurately. The prose-citation verifier does exist for cited files in the protocol body.
- **F-OP18-12 CLOSED IN PART:** incorrect as written. Coverage measurement exists, but the `claim provenance ledger implemented` half is false.

## 7. Historical integrity and cross-version anchor

- Current-package seals reproduce on clean bytes: every `ENTRY_v*` and `FULL_SECTION_27` line in `HISTORY.sha256` matches the current `xz_protocol_v0_19.md`.
- The chained cross-version anchor does **not** reproduce as a computed control. The `PRIOR_HISTORY` line is present, but the build never validates its digest.
- Because the prior packet does not ship, I cannot independently compare the v0.18 `HISTORY.sha256` bytes against the declared digest from within this packet alone. That limitation is exactly why the missing executable chain check matters.

## 8. Coverage measurement

### Character-level

From the clean controlled-path build:

- Total protocol characters: `137056`
- Gated body characters: `96482` (`70.4%`)
- Ungated Section 27 characters: `40574` (`29.6%`)

### Packet-level

I computed member-digest coverage over all 33 shipped files:

- Members whose SHA-256 appears in some shipped text: `16`
- Members with no digest in any shipped text: `17`

**Undigested members:**

- `AUDIT_DISPATCH_DISCIPLINE_v2.md`
- `BAF_v3_0.pdf`
- `BSSG_PAPER.pdf`
- `DISPATCH_v19_ADVERSARIAL.md`
- `Dissertation_v1_4.pdf`
- `Flagship_v0_13.pdf`
- `HISTORY.sha256`
- `PMD_v1_8.pdf`
- `PRODUCER_SELF_DISCIPLINE_v2_DELTA.md`
- `SEAT_STANDING_ORDERS_v1.md`
- `SHUDP_v0_5_flagship.pdf`
- `SHVVP_v0_8_flagship.pdf`
- `SHV_Method_v1_1.pdf`
- `XZ_v17_OPUS5_ADVISORY_REPORT.md`
- `XZ_v17_OPUS5_ADVISORY_REPORT__1_.md`
- `XZ_v18_SEAT_A_REPORT_REV_B.md`
- `build.py`

This matters because the v0.19 entry relies on `XZ_v18_SEAT_A_REPORT_REV_B.md` for its only shipped `EXTERNAL` tag, but that file is itself outside any digest envelope in the shipped text.

## 9. Probe battery

### Benign control

- Clean controlled-path build on the untouched tree: rc=`0`
- Evidence:
  - `/home/user/workspace/audit_xz_v19/evidence/baseline_build_controlled_path.txt`
  - `/home/user/workspace/audit_xz_v19/evidence/baseline_build_controlled_path.rc`

### Probe P1 — new class — `PRIOR_HISTORY` line-presence spoof

- **Adversary model:** self-consistent forger
- **Mutation:** replace only the `PRIOR_HISTORY` digest with `000...000`, leave the line present, reseal `ENTRY_v*` and `FULL_SECTION_27`
- **Mutation-landed assertion:** probe tree differs from clean tree; controlled-path build still passes
- **Result:** **FALSE PASS**
- **Evidence:** `/home/user/workspace/audit_xz_v19/evidence/probe_prior_history_false_pass.*`
- **Discrimination control:** corrupt `ENTRY_v0.19` seal without reseal -> build fails
- **Benign control:** clean build passes

### Probe P2 — new class — provenance-tag spoof

- **Adversary model:** self-consistent forger
- **Mutation:** change `[COMPUTED: build.py [9a].]` to `[ASSERTED: build.py [9a].]`, reseal Section 27
- **Mutation-landed assertion:** protocol digest changes from `d25350f0...` to `e3aaff01...`
- **Result:** **FALSE PASS**
- **Evidence:** `/home/user/workspace/audit_xz_v19/evidence/probe_provenance_tag_false_pass.*`
- **Discrimination control:** mutate a genuinely gated body sentence in Section 22 (`gate is convenience` -> `gate is the carry check`) -> build fails
- **Benign control:** clean build passes

### Additional controls

- `control_history_entry_fail`: corrupt `ENTRY_v0.19` seal -> fail at `[9b]`
- `control_s22_phrase_fail`: mutate Section 22 item 6 -> fail at `[10]`

### Void / discarded attempts

- I discarded an attempted FB-row swap setup and an attempted test-count body mutation because the mutation scripts did not land cleanly. They are **not** used as findings or as evidence. This is deliberate: a non-landed mutation is void under S-3/D-3.5.

## 10. Boundary report

The outermost layer the build still does **not** compute is:

> **Section 27 amendment-entry semantics about other documents, about the build and discipline documents themselves, and about the provenance status of those claims.**

What the build computes well enough:

- current-file digests and manifest digest
- current code/test version stamps
- current clean test execution
- some body-local structural checks outside Section 27

What remains outside:

- whether Section 27 claims about prior reports are true
- whether a claimed closure route is actually implemented rather than merely named
- whether provenance tags are present, correct, complete, and well-scoped
- whether in-packet artifacts cited as evidence are independently anchored
- whether the `PRIOR_HISTORY` digest matches anything real

**What would bring this boundary inside:**

1. A structured amendment-entry ledger that is parsed by the build.
2. One required provenance tag per atomic claim unit, generated from structure rather than handwritten prose.
3. Packet-wide digest coverage over every shipped member, including reports, discipline docs, `build.py`, and `HISTORY.sha256`.
4. Executable `PRIOR_HISTORY` comparison against an actual prior-history anchor.
5. A machine-maintained recurrence table if ordinals are to be printed at all.

## 11. D-7 process answers

- **Did every probe come from an enumerated prior list?** No. P1 (`PRIOR_HISTORY` line-presence spoof) and P2 (provenance-tag spoof) are new classes.
- **Did the dispatch tell me where to look such that findings were predetermined?** Partly. The v2 discipline specifically points at provenance and chain checks, but these exact false-PASS classes were not enumerated in the prior corpus shipped here.
- **Is the ASSERTED fraction unchanged from the prior round?** Direct numeric comparison is not possible because v0.18 did not ship a machine-readable ledger. Qualitatively, the boundary barely moved: the current entry still leaves the vast majority of its own claims asserted.
- **Have the recent rounds all been producer-family?** Yes, per the v0.19 governance note: v0.16 through v0.19 were producer-family advisory cycles.

## 12. Self-falsification

Before finalizing, I re-ran:

1. Normative digests on the clean tree.
2. Canonical pytest on the clean tree.
3. The build on the clean tree under both default and controlled interpreter paths.
4. The two reported false-pass probes into persisted evidence files.
5. The two reported failing controls into persisted evidence files.
6. The packet-coverage count and undigested-member list.
7. The cited line numbers for the three findings.

This self-falsification step **did** catch one real issue in my own process: two earlier probe setup attempts did not land cleanly. I excluded both as void rather than laundering them into findings.

## 13. Verdict

> **Verdict:** HALT.
>
> **Standing:** adversarial, advisory only; does **not** bind freeze and does **not** count toward two-family carry.
>
> **Blocking findings:** F-GPT19-01 and F-GPT19-02.
>
> **What clears them:**
> 1. Implement and demonstrate an actual `PRIOR_HISTORY` digest comparison that fails on a wrong line value.
> 2. Replace the decorative provenance tagging with a machine-checked structured claim ledger and packet-wide artifact coverage.
> 3. Remove the unsupported ordinal sentence or derive it from a shipped recurrence table.

## 14. Output paths

- **Report:** `/home/user/workspace/audit_xz_v19/report_v19_adversarial_audit.md`
- **Evidence directory:** `/home/user/workspace/audit_xz_v19/evidence/`
- **Probe helper (audit workspace only):** `/home/user/workspace/audit_xz_v19/reseal_history.py`

---

# Bismillah ir-Rahman ir-Rahim
