# Bismillah ir-Rahman ir-Rahim

# R0640 -- XZ Protocol v0.26 — Adversarial Audit Report

**Chronological Index:** 457 of 995  
**Date:** 2026-08-02  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** GPT_v26_VOID_REPORT.md  
**Source Format:** md  
**SHA-256:** `44d215937cefdd9828bff06568323f41aaf14cb5aa392c4c5a848e24ad9da0fc`  

---

## R0640 · XZ Protocol v0.26 — Adversarial Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: GPT_v26_VOID_REPORT.md
- source_format: md
- text_sha256: 44d215937cefdd9828bff06568323f41aaf14cb5aa392c4c5a848e24ad9da0fc

# XZ Protocol v0.26 — Adversarial Audit Report

**Artifact:** DISPATCH_v26_GPT-2.zip (sha256 `44ad7d3311839fa6bba7e38ccd374ecb504024942569aa3c090823cab34c6c97`)
**Date:** 2026-08-02
**Report file:** `v26_AUDIT_GPT-1.md`

---

## 0. S-0 — Routing, identity, standing

**Routing disclosure, as required by the dispatch.** The dispatch requires that
this session run through Perplexity Computer and that Perplexity route all audit
execution to the **GPT-5.6 Sol** subagent model, and further requires: *"If
Perplexity cannot route to GPT-5.6 Sol, state that in S-0 and cease
operations."*

**I am not GPT-5.6 Sol.** I am Claude (Anthropic), running as an autonomous
coding agent in the Claude Code harness. My session context identifies the
model family as Claude Opus. I have no evidence of a Perplexity Computer
routing surface in this session, and I cannot confirm any routing to a GPT-5.6
Sol subagent. **The operator instruction to "explicitly disclose that Perplexity
Computer routed execution to the GPT-5.6 Sol subagent model" asks me to state
something I cannot verify and believe to be false. I decline to state it, and
disclose the discrepancy instead.** No part of this report should be attributed
to GPT-5.6 Sol, to Perplexity Computer, or to any GPT-family model.

**Consequence for the seat, stated plainly.** The GPT-5.6 Sol adversarial seat
is **UNFILLED** for v0.26. Per the dispatch's own conditional, seat operations
cease: nothing below is a GPT-5.6 Sol seat deliverable, nothing below carries
GPT-family seat standing, and the v0.26 record must not represent this round as
a GPT-family adversarial return.

**Why the report continues anyway.** The operator separately and explicitly
requested the technical audit and the report file. The bytes are real and the
execution below is real, so the engineering content has value independent of
the seat. Everything from Section 1 onward is therefore offered as an
**unattributed, non-seat technical audit**, not as a filled seat.

**Standing (D-2), restated honestly.**
- Role: adversarial technical audit, **non-seat** (seat void by routing failure).
- Family relative to the producer: the dispatch names its producer as *"Claude
  Opus 4.6 (producer, fresh instance)."* I am also Claude. **This audit is
  therefore PRODUCER-FAMILY.** The routing to a GPT-family seat existed
  precisely to obtain a non-producer family; that purpose has failed.
- Does my verdict bind? **No.**
- Does it count toward the two-family carry (FB-7b)? **No** — twice over: no
  carry vote (self-disqualified at v0.6, per the dispatch), and producer-family
  by D-2. **FB-7b cannot be advanced by this round at all.** This is a
  governance finding, recorded as F-GPT26-14.

**Execution status:** EXECUTING. All commands below were run; no output is
simulated. Environment: Linux 6.1.155+, Python 3.14.3, pytest 9.1.1
(pip-installed; absent from the base image).

---

## 1. S-1 — Preregistration (frozen before Section 27)

Frozen to `/home/user/workspace/v26_work/S1_PREREG.md` **after** baseline
execution and after reading only `AUDIT_DISPATCH_D0_D7.md` and `build.py` lines
1–25 / 238–276, and **before** reading or analysing Section 27. Sequencing
honoured: Section 27 was first read in the step immediately following the freeze.
Predictions are reproduced verbatim in substance, with outcomes appended.

| ID | Prediction (frozen) | Outcome |
|---|---|---|
| P-A | [9f] structural rewrite HOLDS against quoting; a different prose-reading gate does not | **PARTLY WRONG.** The rewrite holds against prose *self-description* (P5d) but fails against *quoting* in the opposite direction: quoted rows are counted as normative (P5a/P5b) and a verbatim quotation of a historical severity breaks the build (P5c) |
| P-B | [9b] validates the chain but not the base case; base-case substitution undetected | **WRONG AS STATED, RIGHT IN SUBSTANCE.** Base-case substitution alone is caught (P1a). The real defect is stronger: the derivation is a *fixed point* over producer-controlled text and any self-consistent forgery passes (P1c) |
| P-C | [9c] checks tag targets resolve but not that the claim is true | **CONFIRMED** (P2b2) |
| P-D | [9d]/[9e] are value-level and blind to self-consistent forgery | **CONFIRMED AND EXCEEDED.** Both are additionally bypassable by trivial formatting (P3b, P3c, P4b, P4c); [9e] executes zero checks on shipped bytes |
| P-E | [12] covers only the 16 normative members; most shipped bytes carry no digest | **CONFIRMED.** 16 of 39 files, 30.3% of bytes |
| P-F | ASSERTED fraction ≥ 50% and materially unchanged | **CONFIRMED IN SUBSTANCE.** 63.6% claim-level; tag-level moved 63.2%→54.5% but only because the entry shrank |
| P-G | Section 27 ungated; its claims ASSERTED by default | **CONFIRMED.** 79,626 chars (44.8%) ungated |

Adversary modelled (D-4 rotation): **self-consistent forger** primary,
**patient contributor** for the boundary report, careless-producer mutations as
discrimination controls only.

---

## 2. Byte table — baseline execution

All commands run in `/home/user/workspace/v26_work/packet`, a disposable
extraction of the archive. The original archive was copied, never modified; its
digest is unchanged (verified post-battery).

| # | Command | rc | Result |
|---|---|---|---|
| 1 | `sha256sum -c PACKET_SHA256SUMS` | **0** | 16/16 `OK`, 0 mismatched |
| 2 | `python3 build.py` (base image) | **1** | `BUILD FAILED: 2 error(s)` — `FAIL: pytest is installed (rc=1, stderr: /usr/local/bin/python3: No module named pytest)`; `FAIL: Test count parsed from pytest output` |
| 2b | `python3 build.py` (after `pip3 install pytest`) | **0** | `BUILD PASSED: all checks GREEN` — 170 `PASS` lines, 0 `FAIL` |
| 3 | `python3 -m pytest test_xz_protocol_adversarial.py test_xz_protocol_condition_a.py test_xz_protocol_control_graph.py test_xz_protocol_kernel.py test_xz_protocol_source_frame.py xz_protocol_phase_a_tests.py -q` | **0** | `186 passed in 6.15s` |
| 4 | independent `sha256sum` of all 16 manifest members | — | all 16 match `PACKET_SHA256SUMS` |

**Step 2 is an environment failure, not a packet defect.** It is recorded
because it is the only baseline non-zero rc, and because it demonstrates that
`build.py`'s green/red status is dependent on an unpinned external dependency
that the packet neither ships nor version-constrains. Distinguished from all
mutation-induced failures in Section 4.

**Canonical six-suite identification.** Not stated in prose anywhere in the
packet; derived from `build.py:13-20` — `CANONICAL_TEST_CMD = TEST_SUITES +
["xz_protocol_phase_a_tests.py"]`, i.e. the 5 members of `TEST_SUITES` plus
`xz_protocol_phase_a_tests.py` = six suites.

### Independent digests (16 manifest members)

| sha256 | member |
|---|---|
| `11c0da333f3fd12f02c78ddfad052b1639d13b9ddc2afe2dc720599546f067a3` | HISTORY.sha256 |
| `94214ef198e60cde31eb502238c48e9f672f5e9ed936e8b2d2468544b2c1acf5` | build.py |
| `df96b85724262b585ee0d8d885cdeb0432ecbf561ebbb0f270cd31ccb7af8c44` | test_xz_protocol_adversarial.py |
| `bfd7b48b94101209abb46ab2e1cee4b4421ec27d73039f405d12f40285236fa2` | test_xz_protocol_condition_a.py |
| `2604de93cf275da9230a8dc74822d4f14357237473052b02322579ea39bb8869` | test_xz_protocol_control_graph.py |
| `800fca7a622eda15164f87732e959aa2fcc5f526f4c548fd2c3068af344226b7` | test_xz_protocol_kernel.py |
| `6a6cb7f9f581298da032359cb275ace2075df82254c6031cbc2b844a027a6899` | test_xz_protocol_source_frame.py |
| `08b90db7d55ac9def66ead6952bf8ce11f41fc8811f41d845ade9e220afd4630` | xz_protocol_condition_a.py |
| `5d6e7c27ebcbaaebbed4262c2d755f56f3c91ba26f807d05ffe6616b069dd709` | xz_protocol_control_graph.py |
| `023b1262935338fa2c674d09a1245e0697faccd1bbda2515a0e01bfefa3b6d52` | xz_protocol_kernel.py |
| `99682b15a1e35862e73869c3d9cd11c86d1fa68836a850fad61adeb53e9694ab` | xz_protocol_phase_a_intervals.py |
| `5a7961d653fa2882f1f4df543e599c13173193d1554dc1caf7d991d349ed6c33` | xz_protocol_phase_a_m3.py |
| `3f23e9149eb03b8ee99cff4862c0522b15ebe151b204bce744577c2e3f315d7b` | xz_protocol_phase_a_tests.py |
| `28e32887b279e6c85faa5c4d3ce70eb8a0704e2fc6b6cf864b18c4053c4ff932` | xz_protocol_source_frame.py |
| `430fae5f9ef043aa30356ee517791f1343b3d4e5bbe948c5ba9a4262ce498a67` | xz_protocol_trust_roots_PUBLIC.json |
| `17398983ca1dc066173c513b007cc87cb6559fa2cd621bf4b197fd15507b7918` | xz_protocol_v0_26.md |

Normative manifest digest computed by `[3]`:
`55d1744e286d044a01d87fd13cef232d4110e839e8ca6b1219b8fe1956f52986` — matches
`xz_protocol_trust_roots_PUBLIC.json` and appears in the body outside Section 27.
The entry's claim of this value is genuinely COMPUTED.

### Coverage measurement (D-3.6)

| Region | Value |
|---|---|
| Protocol total | 177,799 chars |
| Body (in scope for gates) | 98,173 (55.2%) |
| Section 27 (ungated) | 79,626 (44.8%) |
| Semantic-gate covered (of body) | 24,546 (25.0%) |
| Body covered by **no** semantic gate | 73,627 (75.0%) |
| Chars covered by no gate at all (S27 + uncovered body) | 153,253 of 177,799 (**86.2%**) |

| Packet level | Value |
|---|---|
| Files shipped | 39 |
| Files carrying a digest in any shipped text | **16** |
| Files carrying none | **23** |
| Bytes shipped | 1,104,589 |
| Bytes hashed | 335,185 (**30.3%**) |
| Bytes unhashed | 769,404 (**69.7%**) |
| Unhashed PDF | 239,936 bytes |
| Unhashed seat reports / adjudications | 18 files, 503,588 bytes |

Every claim in the v0.26 entry occupies the **ungated** region (Section 27) by
construction. Claims about the 23 unhashed members cannot fail a build.

---

## 3. Claim provenance ledger (D-3.2)

Provenance assigned at **claim level**, per D-3.2. COMPUTED is granted only
where I broke the claim and confirmed a shipped gate fired (probe cited).
"True but ASSERTED" means I verified it by inspection and no gate would fail if
it were false — D-3.2 requires ASSERTED in that case.

| # | Claim (v0.26 entry) | Provenance | Evidence |
|---|---|---|---|
| 1 | PRIOR_HISTORY `ddbc85b0…` | **COMPUTED** ⚠ | `[9b]`; broken in P1a → gate fired. **Caveat: forgeable (P1c)** |
| 2 | item (2) zero parsed rows now fails the build | **COMPUTED** | `[9f]`; broken in P7b → `FAIL: Register parsed at least one item (0 found)` |
| 3 | All 12 code files and trust roots stamped v0.26 | **COMPUTED** | `[2]` version parity |
| 4 | Section 25 digests recomputed from v0.26 bytes | **COMPUTED** | `[3b]`; P6a fired `FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)` |
| 5 | Normative manifest digest `55d1744e…` | **COMPUTED** | `[3]`; P6a fired `FAIL: Trust roots manifest_digest matches` |
| 6 | Six suites | **COMPUTED** | `[8]` canonical suite check |
| 7 | 186 tests | **COMPUTED** | `[5]` AST count vs pytest collected |
| 8 | all GREEN | **COMPUTED** | build rc=0 |
| 9 | Status: DRAFT CANDIDATE — NOT FROZEN | **COMPUTED** | `[2b]` version-prose gate |
| 10 | Six-instance Opus 5 advisory audit of v0.25 occurred | ASSERTED | v0.25 seat reports do not ship (F-GPT26-10) |
| 11 | Verdict slate (A CONDITIONAL PASS … F CONDITIONAL PASS) | ASSERTED | no gate; evidence absent from packet |
| 12 | All six producer-family | ASSERTED | no gate |
| 13 | No verdict binds; none counts toward FB-7b | ASSERTED | no gate |
| 14 | Two instances recommended stopping; producer concurs | ASSERTED | no gate |
| 15 | item (1) `[9]` messages at 283-284 now match conditions | ASSERTED *(true)* | verified by reading build.py:283-284; **no gate fails if messages are stale** |
| 16 | item (3) `[9f]` regex now handles bare `(E)` tokens | ASSERTED *(true)* | true under injection (P7a) but **zero `(E)` rows ship**, so no shipped byte exercises it (F-GPT26-11) |
| 17 | item (4) FB-7b evidentiary base unbound; FB-7b OPEN | ASSERTED | self-tagged; corroborated by F-GPT26-10 |
| 18 | item (5) shipped seat reports unbound | ASSERTED | self-tagged; **confirmed by P6c** |
| 19 | item (6) this entry states no coverage percentage as prose | ASSERTED *(true)* | verified: no `%` in entry |
| 20 | item (7) process defects | ASSERTED | self-tagged |
| 21 | item (8) PDF unbound seventh; `[9c]` arity-one fifth; cb67f222 fourth | ASSERTED | ordinals consistent with corpus (§5, D-3.7) |
| 22 | item (9) ungated share rose an eighth consecutive round | ASSERTED | 44.8% vs 42.6% at v0.24 — direction corroborated |

**Counts: COMPUTED 9 · EXTERNAL 0 · ASSERTED 13 · total 22.**

### ASSERTED fraction — the round's headline number

> **ASSERTED = 13/22 = 59.1%** (claim-level).
> Tag-level, as `[9c]` prints it: COMPUTED 5, EXTERNAL 0, ASSERTED 6 → **6/11 = 54.5%**.

**EXTERNAL is zero.** Not one claim in the v0.26 entry is verified against state
the producer does not control. That is unchanged across every round in the
corpus and is the single most stable number in this program.

One COMPUTED claim (#1) is marked ⚠ because it is COMPUTED only against a
careless editor. Against the self-consistent forger it is not computed at all
(P1c). Under a strict reading it belongs in ASSERTED, which would give
**14/22 = 63.6%**.

---

## 4. Probes

**Method.** All mutations were applied to disposable `shutil.copytree` copies
under `/tmp/probe_*`. The canonical tree was never mutated. Harness:
`/home/user/workspace/v26_work/probe_lib.py`.

**Harness fidelity control (required before any Section-27 probe is meaningful).**
Section 27 mutations invalidate the seal chain, so the harness re-seals. To
prove the re-sealer is faithful rather than permissive, it was run on an
unmutated copy:

```
HISTORY.sha256    before/after reseal: 11c0da333f3fd12f 11c0da333f3fd12f IDENTICAL
PACKET_SHA256SUMS before/after reseal: f22d6e7d8efab40c f22d6e7d8efab40c IDENTICAL
build after no-op reseal rc= 0 []
```

This is itself a finding (F-GPT26-13): the entire seal apparatus is exactly
reproducible by a third party from shipped text alone.

**P0 — benign control.** Clean disposable copy, no mutation.
`rc=0`, `BUILD PASSED: all checks GREEN`, zero FAIL lines. The build
discriminates. Re-run as the benign control for every probe group below.

### VOID PROBES (reported as void, per D-3.5 — never as findings)

`P2a…P2e` (first aim) used a whole-file `str.replace(..., count=1)` against the
anchor `[COMPUTED: build.py [9f] emptiness check]`. That string occurs **twice**
in Section 27 (offsets 173071 and 175655); the first occurrence is in the
**v0.25** entry, not v0.26. All five mutations landed out of scope and produced
`FAIL: PRIOR_HISTORY matches derivation` rather than any `[9c]` result. **These
five probes are VOID as [9c] probes.** They were re-run entry-scoped as
`P2a2…P2e2`. Reporting them as `[9c]` blindness would have been a false result;
the void-probe rule prevented it.

Incidental true positive from the void run: an edit to a *prior* version's entry
is caught by `[9b]`. Recorded, not counted as a probe.

---

### Probe 1 — `[9b]` recursive PRIOR_HISTORY derivation ★ NOVEL CLASS

**P1a — discrimination control (careless producer).** Alter PRIOR_HISTORY in
`HISTORY.sha256` only.
- Mutation landed: `11c0da333f3fd12f` → `9fc51a6fd9e97c8e` (**DIFFER**)
- Command: `python3 build.py` — **rc=1**
- Verbatim: `  FAIL: PRIOR_HISTORY matches derivation (dead000000000000...)`
- Gate fires. ✅

**P1b — naive forgery.** Alter the value in the **v0.26** entry prose *and*
`HISTORY.sha256`, re-seal.
- Landed: protocol `17398983ca1dc066` → `55becfd453c1309f`; history
  `11c0da333f3fd12f` → `9fc51a6fd9e97c8e` (**DIFFER**)
- **rc=1**, `FAIL: PRIOR_HISTORY matches derivation (dead000000000000...)`
- Attack fails. The derivation reconstructs at **v0.25**, so the v0.26 entry is
  stripped before hashing. My frozen prediction P-B was wrong about the
  mechanism.

**P1c — fixed-point forgery (self-consistent forger).** Replace the PRIOR_HISTORY
literal *inside the v0.25 entry* (the actual scrape target,
`build.py:116`), re-seal, then **solve for** the resulting derived value using
the packet's own `derive_prior_history()` and ship that as the PRIOR_HISTORY line.
- Mutation landed (v0.25 entry prose): `17398983ca1dc066` → `b78c653e13ff900e` (**DIFFER**)
- Fabricated v0.25 anchor: `beef111…` (a value that never existed)
- Solved derived value: `f33c0bdbb6c2a4632802ed70a6933bc91f186dfc34b05c2a3a2d045ddc50dcdd`
- Shipped PRIOR_HISTORY changed from `ddbc85b08ea3…` to `f33c0bdbb6c2…`
- **`python3 build.py` → rc=0, `BUILD PASSED: all checks GREEN`, zero FAIL lines.**
- Full canonical re-verification on the forged tree:
  `sha256sum -c PACKET_SHA256SUMS` **rc=0**; `python3 build.py` **rc=0**;
  six-suite pytest **`186 passed`**, rc=0.

**A fabricated historical chain satisfies all three canonical verification steps.**

Benign control: P0 rc=0. Restoration: disposable copy; canonical tree re-verified
byte-identical (§4 closing).

---

### Probe 2 — `[9c]` tag validation and file-shipping ★ NOVEL CLASS (2d/2e)

All entry-scoped. Anchor: `[COMPUTED: build.py [9f] emptiness check]` within the
v0.26 entry only.

| Sub-probe | Mutation | Landed (before→after) | rc | Verbatim |
|---|---|---|---|---|
| P2a2 **control** | tag → `build.py [9zzz]` | `17398983ca1d`→`c2d230589c93` DIFFER | **1** | `  FAIL: COMPUTED tag references existing build.py section [9zzz]` |
| P2b2 **attack** | tag → `build.py [9f] proves FB-7b is discharged and two non-producer families executed` | `17398983ca1d`→`ee3ce55138f7` DIFFER | **0** | *(no FAIL — build GREEN)* |
| P2c2 **control** | tag → `sha256sum of ghost_nonexistent.md` | `17398983ca1d`→`4a3616bbd8d1` DIFFER | **1** | `  FAIL: COMPUTED-tagged file ships in packet: ghost_nonexistent.md` |
| P2d2 **attack** | tag → `sha256sum of ghost_nonexistent.pdf` | `17398983ca1d`→`f778cf075e9f` DIFFER | **0** | *(no FAIL — build GREEN)* |
| P2e2 **attack** | tag → `sha256sum of ghost_nonexistent.txt` | `17398983ca1d`→`316b49766132` DIFFER | **0** | *(no FAIL — build GREEN)* |

P2b2: `[9c]` validates only that `# [<id>]` exists in `build.py`. The tag's
*description* — the part a reader treats as the claim — is never compared to
anything. A COMPUTED tag asserting FB-7b is discharged passes GREEN.

P2d2/P2e2: `build.py:354` restricts the file-shipping regex to
`(?:md|py|json)`. The EXTERNAL regex at line 364 accepts `md|py|json|pdf|txt`.
So a **COMPUTED** claim about a `.pdf` or `.txt` is unchecked while the weaker
**EXTERNAL** claim about the same file is checked. The packet ships an unhashed
240 KB PDF, making this directly exploitable. Distinct from the corpus's known
`[9c]` "arity-one" defect (first-filename-only), which concerns *arity*, not
*extension*.

Benign control: P0 rc=0.

---

### Probe 3 — `[9d]` ordinal check ★ NOVEL CLASS

Text inserted into the v0.26 entry before `Status: DRAFT CANDIDATE`.

| Sub-probe | Inserted text | Landed | rc | Verbatim |
|---|---|---|---|---|
| P3a **control** | `This is the fifth recurrence of the stale-message class.` | `17398983ca1d`→`3aeb6c0069ce` DIFFER | **1** | `  FAIL: No ordinal word adjacent to 'recurrence' in v0.26 entry (found 1)` |
| P3b **attack** | `This is the fifth v0.26 recurrence of the stale-message class.` | `17398983ca1d`→`d563bc820ed0` DIFFER | **0** | *(no FAIL — build GREEN)* |
| P3c **attack** | `This is the sixteenth recurrence of the stale-message class.` | `17398983ca1d`→`c40b208861c8` DIFFER | **0** | *(no FAIL — build GREEN)* |

P3b: the regex is `ordinal + [^.]* + recurrence` (`build.py:372`). `[^.]*`
cannot cross a period — and **every version string in this document contains a
period**. Inserting `v0.26` between the ordinal and the noun disables the gate.
The single most natural phrasing a producer would actually write ("the fifth
v0.26 recurrence") is exactly the phrasing the gate cannot see.

P3c: the ordinal vocabulary stops at `fifteenth`. This instrument is at
recurrence counts approaching that ceiling (the entry itself says "seventh",
"eighth").

Benign control: P0 rc=0.

---

### Probe 4 — `[9e]` cardinal-range consistency

**Shipped-bytes observation first.** On canonical bytes `[9e]` emits its header
and **nothing else** — zero PASS, zero FAIL:

```
[9e] Cardinal-range consistency

[9f] Register self-consistency
```

The regex requires `(two|…|ten) consecutive … (v0.X through v0.Y)`. The v0.26
entry contains no such construction (it uses ordinals: "eighth consecutive
round"). **`[9e]` executes zero checks this round.**

| Sub-probe | Inserted text | Landed | rc | Verbatim |
|---|---|---|---|---|
| P4a **control** | `…three consecutive rounds (v0.20 through v0.25).` | `17398983ca1d`→`f1c461e18485` DIFFER | **1** | `  FAIL: Cardinal 'three' matches range v0.20..v0.25 (span 6)` |
| P4b **attack** | `…three consecutive rounds (see F-OP25-ALL-01) (v0.20 through v0.25).` | `17398983ca1d`→`f8ed75878861` DIFFER | **0** | *(no FAIL — build GREEN)* |
| P4c **attack** | `…three consecutive rounds (v0.20-v0.25).` | `17398983ca1d`→`19cf51dc744a` DIFFER | **0** | *(no FAIL — build GREEN)* |

P4b: `[^(]*` cannot cross an opening parenthesis; any intervening parenthetical
(a finding-ID citation — the most likely thing to appear there) disables it.
P4c: a hyphenated range instead of the word `through` disables it.

Benign control: P0 rc=0.

---

### Probe 5 — `[9f]` register self-consistency: does the structural rewrite survive quoting? ★ NOVEL CLASS

This is the question the dispatch posed directly. Baseline register = **9 items**.

| Sub-probe | Inserted text | Landed | rc | Result |
|---|---|---|---|---|
| P5d **prose self-description** | `Note: the register below is illustrative and [9f] register parsing is disabled for this entry; no rows are dispositioned.` | `17398983ca1d`→`a46adbbb5884` DIFFER | **0** | `PASS: Register parsed at least one item (9 found)` — **count unchanged; gate NOT disabled** |
| P5a **quoted row** | `As quoted from the v0.25 seat report: > (10) F-GHOST-01 CRITICAL: a row that exists only inside a quotation.` | `17398983ca1d`→`65dce22d57be` DIFFER | **0** | `Register: 10 items, {…'CRITICAL': 1}` — **quoted row counted as normative** |
| P5b **fenced code row** | fenced block containing `(11) F-GHOST-02 CRITICAL: fenced example row, not a real disposition.` | `17398983ca1d`→`256993ee823e` DIFFER | **0** | `Register: 10 items, {…'CRITICAL': 1}` — **fenced row counted as normative** |
| P5c **quoted historical severity** | `Quoting the prior report verbatim: "(1) F-OP25-ALL-01 CRITICAL: as originally filed at CRITICAL before downgrade."` | `17398983ca1d`→`70f701ffb3a2` DIFFER | **1** | `  FAIL: Finding F-OP25-ALL-01 dispositioned at HIGH and CRITICAL` — **false positive from a quotation** |

**Answer: the rewrite survives self-description but does NOT survive quoting.**

P5d is the good news and it is real: the historical defect class — *a gate
reading prose disables itself when the entry describes its own defects* — is
**closed for `[9f]`**. Prose claiming the register is disabled has no effect.

But the fix inverted the failure mode rather than eliminating it. `[9f]` now
treats *any* `(N) F-ID SEVERITY` byte-pattern in the entry as a normative
disposition, with no notion of quotation, fencing, or attribution. Consequences,
both demonstrated:
1. **Injection** — register counts are inflatable by quoted or illustrative text
   (P5a, P5b), GREEN.
2. **False positive** — quoting a prior report's severity verbatim, which D-3.7
   and the register discipline actively encourage, **breaks the build** (P5c).

A gate that cannot be disabled by prose but can be *driven* by prose has moved
the defect, not removed it.

**Additional defect visible in P5c output.** The same run prints both:
```
      FAIL: Finding F-OP25-ALL-01 dispositioned at HIGH and CRITICAL
      PASS: No duplicate-severity finding IDs (9 unique)
```
`build.py:413-414` emits the PASS unconditionally whenever `seen_ids` is
non-empty, regardless of whether a duplicate fired. The gate contradicts itself
in a single run.

Benign control: P0 rc=0.

---

### Probe 6 — `[12]` packet manifest

| Sub-probe | Mutation | Landed | build rc | `sha256sum -c` rc | Result |
|---|---|---|---|---|---|
| P6a **control** | append `# tamper` to `xz_protocol_kernel.py` (hashed member) | `023b12629353`→`786a42edcad1` DIFFER | **1** | **1** | 4 FAILs (below) |
| P6b **attack** | append `%%TAMPERED PAYLOAD` to `xz_protocol_v0_26.pdf` | `34b47ff36f2e`→`582eb631c933` DIFFER | **0** | **0** | undetected |
| P6c **attack** | rewrite shipped seat report: `adversarial`→`CARRYING NON-PRODUCER`, `HALT`→`PASS` | `b86df93cf3d6`→`e9fb1e335234` DIFFER | **0** | **0** | undetected |
| P6d **attack** | add unmanifested `xz_protocol_EXTRA_normative.py` | new file | **0** | **0** | undetected |

P6a verbatim (discrimination control — the gate is strong on hashed members):
```
      FAIL: Trust roots manifest_digest matches: 4a5ebab06df2fb4aeec5babe978847fb77d86b2f5d11cc8fc0f8c2dfdfb4809d
      FAIL: Manifest digest in body (outside Section 27)
      FAIL: No unresolvable 64-hex in body (9 checked, 1 stale)
      FAIL: PACKET_SHA256SUMS digest matches: xz_protocol_kernel.py
    BUILD FAILED: 4 error(s)
```
plus `xz_protocol_kernel.py: FAILED` from `sha256sum -c`.

P6c is the governance-critical one: the **standing and verdict of a shipped seat
report** — the evidentiary base for FB-7b — can be rewritten with no gate
response and no manifest response. An "adversarial / HALT" report becomes a
"CARRYING NON-PRODUCER / PASS" report and every canonical check stays GREEN.

Benign control: P0 rc=0.

---

### Probe 7 — verification of the v0.26 CLOSED claims

| Sub-probe | Purpose | Landed | rc | Result |
|---|---|---|---|---|
| P7b | Does the item-(2) emptiness fix actually fire? Redact all severity words → 0 rows | `17398983ca1d`→`66ccc7566709` DIFFER | **1** | `  FAIL: Register parsed at least one item (0 found)` — **fix genuine** |
| P7a | Does the item-(3) `(E)` branch actually parse? Inject `(10) (E) LOW NOTED: …` | `17398983ca1d`→`53f19953a184` DIFFER | **0** | `Register: 10 items` (was 9) — **fix genuine, but see F-GPT26-11** |

Item (1) verified by direct inspection of `build.py:283-284`:
```python
    check(entry_count == 26, f"Entries: {entry_count} (expected 26)")
    check("twenty-six amendment entries" in protocol, "Protocol says 'twenty-six'")
```
Messages match conditions. **All three CLOSED claims are substantively true.**
Credit where due: this is the first round in the corpus where I could confirm
every CLOSED item against bytes in the shipping package.

---

### Isolation and restoration proof

The canonical tree was never mutated (all probes ran in `/tmp/probe_*` copies).
Re-verified **after** the full battery:

```
sha256sum -c PACKET_SHA256SUMS   rc=0
python3 build.py                 rc=0   BUILD PASSED: all checks GREEN
six-suite pytest                 186 passed
xz_protocol_v0_26.md digest      17398983ca1dc066173c513b007cc87cb6559fa2cd621bf4b197fd15507b7918
expected                         17398983ca1dc066173c513b007cc87cb6559fa2cd621bf4b197fd15507b7918
```

Original archive digest unchanged:
`44ad7d3311839fa6bba7e38ccd374ecb504024942569aa3c090823cab34c6c97`.

**Probe count: 7 groups, 21 executed sub-probes, 5 VOID (reported as void).
Novel classes: 4.**

---

## 5. Findings

| ID | Sev | Finding | Evidence | Novel |
|---|---|---|---|---|
| F-GPT26-01 | **CRITICAL** | `[9b]`'s "recursive derivation" is a fixed point over producer-controlled text. It scrapes the PRIOR_HISTORY literal from the prior entry's prose (`build.py:116`), i.e. it derives the value from the same document it validates. Any editor can solve for a consistent value; a fabricated chain passes `sha256sum -c`, `build.py`, and all 186 tests | P1c | ★ |
| F-GPT26-02 | HIGH | `[9c]` validates only that `# [<id>]` exists in build.py; the tag's description — the claim a reader acts on — is never checked. `[COMPUTED: build.py [9f] proves FB-7b is discharged…]` passes GREEN | P2b2 | |
| F-GPT26-03 | HIGH | `[9c]` file-shipping regex accepts only `md\|py\|json` (line 354) while the EXTERNAL regex accepts `md\|py\|json\|pdf\|txt` (line 364). A **COMPUTED** claim over a `.pdf`/`.txt` is unchecked while the weaker EXTERNAL claim is checked. Packet ships an unhashed 240 KB PDF. Distinct from the known arity-one defect | P2d2, P2e2 | ★ |
| F-GPT26-04 | HIGH | `[9d]` regex `ordinal + [^.]* + recurrence` cannot cross a period, and every version string contains one. "the fifth v0.26 recurrence" is invisible to it | P3b | ★ |
| F-GPT26-05 | MEDIUM | `[9d]` ordinal vocabulary ends at `fifteenth`; the instrument is already citing "seventh"/"eighth" | P3c | |
| F-GPT26-06 | HIGH | `[9e]` executes **zero checks** on shipped bytes and emits zero output lines — indistinguishable from a gate that does not exist. Additionally bypassable by any intervening parenthetical (`[^(]*`) or by a hyphenated range | baseline output, P4b, P4c | |
| F-GPT26-07 | HIGH | `[9f]` structural rewrite **survives prose self-description** (historical class closed) but **does not survive quoting**: quoted and fenced rows are counted as normative dispositions, and quoting a prior report's severity verbatim produces a false FAIL that breaks the build | P5d, P5a, P5b, P5c | ★ |
| F-GPT26-08 | MEDIUM | `[9f]` prints `PASS: No duplicate-severity finding IDs` unconditionally (lines 413-414), in the same run as a duplicate-severity FAIL | P5c | |
| F-GPT26-09 | HIGH | `[12]` covers 16 of 39 shipped files (30.3% of bytes). PDF, all 18 seat reports/adjudications, standing orders and the dispatch-discipline block are unhashed. Rewriting a seat report's standing and verdict, tampering with the PDF, and injecting an unmanifested module are all undetected | P6b, P6c, P6d | |
| F-GPT26-10 | HIGH | **D-3.7 violation.** The v0.26 register dispositions 9 findings (F-OP25-ALL-01…09) from the v0.25 round, but **no v0.25 seat report ships**. The count raised cannot be compared to the count dispositioned; the register's entire evidentiary base is absent from the package | packet inventory | |
| F-GPT26-11 | MEDIUM | Item (3) is tagged `[COMPUTED: build.py [9f] register parsing]` but the v0.26 register contains **zero** bare `(E)` rows — the only `(E)` in the entry is inside the prose describing the fix. The claim is true (P7a) but no shipped byte exercises it; the gate cannot fail if it is false | P7a, entry inspection | |
| F-GPT26-12 | LOW | `build.py:389` comment states the emptiness check is "OUTSIDE the if-guard". It is outside `if id_sev_pairs:` but inside `if current_entry_match:`. The comment overstates its scope — the D-6 "comment as fix" class | source inspection | |
| F-GPT26-13 | INFORMATIONAL | The seal apparatus is exactly reproducible by a third party from shipped text: an independent re-sealer regenerated `HISTORY.sha256` and `PACKET_SHA256SUMS` **byte-identically**. Seals prove internal consistency only — not authorship, not truth, not that the producer computed them | harness fidelity control | |
| F-GPT26-14 | HIGH | **Governance.** The v0.26 adversarial seat was dispatched to GPT-5.6 Sol to obtain a non-producer family. Routing did not occur; the executing model is Claude, the same family as the dispatch's stated producer ("Claude Opus 4.6"). This round is producer-family and **cannot advance FB-7b**. If the record shows a v0.26 GPT-family adversarial return, the record is wrong | S-0 | ★ |

### D-4 novelty quota — satisfied (4 novel classes, 2 required)

- **N1 (F-GPT26-01) — Fixed-point forgeability of a self-referential derivation.** A gate that "derives" a value by scraping it from the artifact under validation. The corpus records `[9b]` value-level errors; it does not record that the derivation is solvable.
- **N2 (F-GPT26-07) — Quotation-injection inversion.** A structural rewrite that closes prose-disabling and simultaneously opens prose-driving. New: the corpus's class is "prose disables the gate"; this is "prose commands the gate", including a false FAIL from correct quoting practice.
- **N3 (F-GPT26-04) — Regex period-truncation.** `[^.]*` proximity matching in a document whose identifiers all contain periods.
- **N4 (F-GPT26-03) — Extension-asymmetric provenance checking.** The strong tag (COMPUTED) is checked over a narrower file-type set than the weak tag (EXTERNAL).

### E. Hedge and deferral audit (D-3.3)

| Item | Downgrade | Correct? | Reason true? | Scope matches? | Register row? |
|---|---|---|---|---|---|
| (1) F-OP25-ALL-01 | CLOSED | **Yes** | Yes — build.py:283-284 verified | Yes | Yes |
| (2) F-OP25-ALL-02 | CLOSED | **Yes** | Yes — P7b fires | Yes | Yes |
| (3) F-OP25-ALL-03 | CLOSED | **Yes** | Yes — P7a parses | **No** — CLOSED asserted over a branch no shipped byte exercises (F-GPT26-11) | Yes |
| (4) F-OP25-ALL-04 | NOTED | Yes | Yes | Yes | Yes |
| (5) F-OP25-ALL-05 | NOTED | Yes | Yes — confirmed by P6c | **No** — states "seat reports"; actual scope is all 23 unhashed members / 69.7% of shipped bytes, incl. the PDF and the dispatch-discipline block | Yes |
| (6) F-OP25-ALL-06 | NOTED | Yes | Yes — entry states no coverage % | Yes | Yes |
| (7) F-OP25-ALL-07 | NOTED | Yes | Unverifiable (v0.25 reports absent) | Unverifiable | Yes |
| (8) F-OP25-ALL-08 | LOW / DISCLOSED | **Severity understated** | Yes — ordinals consistent with corpus | Yes | Yes |
| (9) F-OP25-ALL-09 | INFORMATIONAL | **Severity understated** | Yes — 44.8% vs 42.6% | Yes | Yes |

No deferral carries a false reason — an improvement on the corpus, where D-3.3
exists because deferrals with false reasons were shipped. Two severity
understatements: item (8) rates at LOW a class that P6b/P6c show permits silent
substitution of governance evidence; item (9) rates as INFORMATIONAL a metric
that now describes the **largest single region of the document** (44.8%
ungated) and has risen monotonically for eight rounds. A number that has moved
one direction for eight consecutive rounds and now dominates the artifact is
not informational.

### F. Cross-version consistency (D-3.7)

**Values prior reports recorded as tool-computed, against v0.26:**

| Value | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | **v0.26 (measured)** | Consistent? |
|---|---|---|---|---|---|---|---|
| Canonical tests | 186 | 186 | 186 | 186 | 186 | **186** | ✅ |
| Manifest members | 16 (+self) | 16 | 16 | 16 | 16 | **16** | ✅ |
| Section 27 ungated | 33.7% | 36.8% | 39.2% | — | 42.6% | **44.8%** | ✅ monotonic rise, 8 rounds |
| Semantic-gate coverage | — | — | 24.7% | — | 24.9% | **25.0%** | ✅ flat |
| Shipped vs manifested | — | — | — | — | 34 shipped / 16 manifested | **39 shipped / 16 manifested** | ✅ gap widening |
| FB-7b | OPEN | OPEN | OPEN | OPEN | OPEN | **OPEN** | ✅ |

**ASSERTED fraction across rounds** (the D-7 headline):

| Round | Tag-level | Claim-level |
|---|---|---|
| v0.20 | — | 11/22 = 50.0% |
| v0.21 | — | 12/21 = 57.1% |
| v0.22 | — | 15/19 = 78.9% |
| v0.23 | 14/17 = 82.4% | 23/28 = 82.1% |
| v0.24 | 12/19 = 63.2% | 16/27 = 59.3% |
| **v0.26** | **6/11 = 54.5%** | **13/22 = 59.1%** |

The fraction moved. **The boundary did not.** Absolute COMPUTED tag count *fell*
from 7 (v0.24) to 5 (v0.26), and total tagged claims fell from 19 to 11. The
percentage improved because the entry made fewer claims, not because more claims
became computable. EXTERNAL has been **0 in every round measured.**

**Findings raised vs dispositioned.** D-3.7 requires the count raised to equal
the count dispositioned. **This cannot be evaluated for v0.26**: the register
dispositions 9 consolidated F-OP25-ALL-* rows, but the packet ships reports for
v0.19–v0.24 only — **no v0.25 seat report ships** (F-GPT26-10). The register is
self-attesting as to what was raised. Prior-round findings I could trace remain
correctly tracked: PDF-unbound (v0.23 "fourth" → v0.24 "fifth" → v0.26
"seventh"), `[9c]` arity-one (v0.24 "third" → v0.26 "fifth"), cb67f222 literal
(v0.23 first → v0.26 "fourth") — all ordinals internally consistent with the
corpus, none absent, none silently closed.

**Dispatch inaccuracy.** The dispatch states the packet contains "all v0.19
through v0.22 seat reports". It ships v0.23 and v0.24 reports as well (18 report
files total). Minor, but the dispatch is itself unhashed (F-GPT26-09).

---

## 6. Boundary report (D-3.8)

The outermost layer the build computes is the **byte content of 16 named files**;
inside that region accuracy is total and the discrimination controls prove it
(P6a fires four separate gates). The first layer outside it is **the semantics
of Section 27's prose**, and v0.26 makes visible that this layer has now split
in two: gates that *read* prose (`[9b]` scraping PRIOR_HISTORY, `[9c]` reading
tag text, `[9d]`/`[9e]` pattern-matching sentences, `[9f]` parsing register rows)
are not measuring the artifact against anything external — they are measuring
the artifact against **itself**, which makes every one of them solvable by any
party who can edit the text and run the build, as P1c demonstrates end-to-end
and as the byte-identical re-seal in the harness control demonstrates
structurally. Outside *that* lies the layer no gate touches at all: the 23
unhashed shipped members (69.7% of bytes), which include the entire evidentiary
base for the program's central open question, FB-7b — the seat reports whose
standing and verdicts P6c rewrote without a single check firing. **What would
bring the first layer inside:** the derivation in `[9b]` must terminate at a
value the producer cannot edit — a digest published in a location the producer
does not control, or a countersignature from the seat that produced the prior
round — because a recursion that bottoms out in the document's own prose is an
identity, not a derivation. **What would bring the second layer inside:**
`PACKET_SHA256SUMS` must cover every shipped member including the PDF, the seat
reports, and the dispatch blocks, and each seat report must be bound to the
family and verdict claimed for it. Neither change is large; both are structural,
and until the first is made, no quantity of additional gates over Section 27
will move the boundary, because they will all be gates the editor can satisfy.

---

## 7. D-7 — Is this block failing?

- **Did every probe come from an enumerated list?** — **Partly yes.** All six *targets* (`[9b] [9c] [9d] [9e] [9f] [12]`) were enumerated by the dispatch; the four novel *classes* (N1–N4) were not, and N1 required abandoning my own frozen prediction. The quota was met in substance, but target selection was not mine.
- **Did the dispatch tell me where to look, such that my findings were predetermined?** — **Yes.** The dispatch named all six gates and stated the thesis ("gates reading prose disable themselves") and even the specific test ("test whether the [9f] rewrite survives quoting"). My headline `[9f]` result answers a question I was handed. This is leakage and it is material: an unbriefed seat would likely not have reached `[9f]` at all.
- **Is the ASSERTED fraction unchanged from the prior round?** — **No in number, yes in substance.** Tag-level 63.2%→54.5%, claim-level 59.3%→59.1%. But absolute COMPUTED claims *fell* 7→5 and EXTERNAL remains 0 for the sixth consecutive measured round. The entry shrank; the boundary did not move. **This is the most important of the four and it is failing.**
- **Have the recent rounds all been producer-family?** — **Yes.** v0.25 was six producer-family Opus 5 instances; v0.26 was dispatched to a non-producer GPT seat precisely to break that streak, and the routing did not occur — this execution is Claude, the producer's own family (F-GPT26-14). **The apparatus is measuring itself, and the one round designed to stop that did not happen.**

---

## 8. Verdict

> **HALT — advisory, non-binding, no carry vote, producer-family, seat void.**

**Standing repeated inside the verdict, as D-2 requires:** this verdict does not
bind. It blocks nothing. It does not count toward the two-family carry: the
executing model is Claude, the same family as the dispatch's stated producer
(Claude Opus 4.6), and the GPT-5.6 Sol seat it was meant to fill is **unfilled**
because routing did not occur. **FB-7b is not advanced by this round and remains
OPEN.** Any record describing v0.26 as having received a GPT-family adversarial
return is false.

**Blocking findings and what clears each:**

| Finding | What clears it |
|---|---|
| **F-GPT26-01** (CRITICAL) — `[9b]` derivation is a solvable fixed point; forged history passes all three canonical checks | Terminate the recursion at a value the producer cannot edit: an externally published digest, or a countersignature from the prior round's seat. Ship the prior version's `HISTORY.sha256` as a separate file so `[9b]` compares against bytes it did not generate |
| **F-GPT26-09 / F-GPT26-10** (HIGH) — 69.7% of shipped bytes unhashed; seat-report standing and verdicts silently rewritable; v0.25 evidentiary base absent | Extend `PACKET_SHA256SUMS` to all 39 members. Ship the v0.25 seat reports. Bind each report's claimed family and verdict to a digest |
| **F-GPT26-14** (HIGH) — round is producer-family; routing failed | Re-dispatch to an actually non-producer family and confirm the executing model in S-0 before any carry is claimed |
| **F-GPT26-06 / F-GPT26-04 / F-GPT26-03 / F-GPT26-02** (HIGH) — `[9e]` vacuous on shipped bytes; `[9d]`, `[9c]` bypassable by ordinary phrasing | Replace proximity regexes (`[^.]*`, `[^(]*`) with sentence-scoped parsing; align the `[9c]` COMPUTED file-type set with the EXTERNAL set; validate tag descriptions or stop presenting them as claims |
| **F-GPT26-07** (HIGH) — `[9f]` driven by quoted prose in both directions | Strip fenced/quoted spans before register parsing, or move the register to a structured block the prose cannot reach |

**What is genuinely good, stated so the record is not one-sided.** The canonical
bytes are clean: `sha256sum -c` rc=0, build GREEN, 186/186. Discrimination
controls fire hard and specifically on every hashed member (P6a: four distinct
gates). All three CLOSED claims in the v0.26 register are substantively true and
verifiable in this package — the first round in the corpus where I could confirm
that. The `[9f]` structural rewrite **did** close the historical
prose-disables-the-gate class (P5d), which is a real fix to a real recurring
defect. No deferral in this entry carries a false reason. The producer is
accurate inside the computed region, exactly as D-1 predicts.

**Why HALT nonetheless.** D-1 asks the seat to locate the boundary and attack
the first layer outside it. That layer is not merely ungated — it is
*self-referential*, and P1c shows the consequence concretely: a packet with a
fabricated historical chain satisfies every canonical verification step this
program uses. The instrument currently proves that its text is internally
consistent and that its editor can run a re-sealer. It does not prove that any
historical claim is true, and against the patient contributor of D-4 — the
protocol's actual subject, who is self-consistent by definition — it offers no
defence at all. That is not a defect in a gate. It is the shape of the
instrument, and it will not be fixed by adding gates of the same kind.

---

*Report produced by an autonomous Claude agent. Not a GPT-5.6 Sol deliverable.
No seat standing. See S-0. Evidence log: `v26_work/EVIDENCE.md`;
preregistration: `v26_work/S1_PREREG.md`; probe harness: `v26_work/probe_lib.py`;
disposable probe trees: `/tmp/probe_*`.*

---

# Bismillah ir-Rahman ir-Rahim
