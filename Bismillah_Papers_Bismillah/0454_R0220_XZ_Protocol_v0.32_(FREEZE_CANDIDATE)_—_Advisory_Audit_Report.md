# Bismillah ir-Rahman ir-Rahim

# R0220 -- XZ Protocol v0.32 (FREEZE CANDIDATE) — Advisory Audit Report

**Chronological Index:** 454 of 995  
**Date:** 2026-08-02  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v0_32_FREEZE_AUDIT_OPUS_F.md  
**Source Format:** md  
**SHA-256:** `d7876f8948f1440fd712abfbaae64eb71cf7dd51927f0a8d3cc8803f6535b374`  

---

## R0220 · XZ Protocol v0.32 (FREEZE CANDIDATE) — Advisory Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v0_32_FREEZE_AUDIT_OPUS_F.md
- source_format: md
- text_sha256: d7876f8948f1440fd712abfbaae64eb71cf7dd51927f0a8d3cc8803f6535b374

# XZ Protocol v0.32 (FREEZE CANDIDATE) — Advisory Audit Report

**Seat:** Claude Opus 5 (Anthropic) — **producer-family, advisory, EXECUTING**
**Standing:** No carry vote. No FB-7b weight. **This verdict does not bind. A HALT from this seat blocks nothing; it is recorded and forwarded.**
**Round:** v0.32 freeze candidate
**Date:** 2026-08-02
**Package under audit:** `DISPATCH_v32_OPUS_F.zip` `33ab4bb56f5da7287ada51a8153ef50fe488312ee294459879052283244923f3`
**Independent state held:** complete v0.25, v0.27 and v0.28 packages, all `sha256sum -c` rc=0
**Verdict:** **HALT — advisory, non-binding, recorded and forwarded**
**Author of the instrument under audit:** Bilal Syed Arfeen

---

## S-0 — STATE DECLARATION

**Standing (stated here and repeated in the verdict).** Claude Opus 5 (Anthropic) — **producer-family, advisory seat. No carry vote. No FB-7b weight. My verdict does not bind. A HALT from this seat blocks nothing; it is recorded and forwarded.** Under Section 22 item 7, only a carrying seat's HALT blocks freeze outright. Nothing below may be recorded as discharging any part of the two-family carry.

**Packages held.** Four. `DISPATCH_v32_OPUS_F.zip` `33ab4bb56f5da728…` (under audit), plus **the complete v0.25, v0.27 and v0.28 packages, all still verifying `sha256sum -c` at rc=0, 16/16 OK, re-confirmed after the probe battery.** Held `HISTORY.sha256` digests: `ddbc85b08ea3f630…`, `c569ce9c86946b1e…`, `3fa09069d4648350…`. **I do not hold v0.29, v0.30 or v0.31**, which bounds two claims below to NOT DERIVABLE.

**Execution.** EXECUTING. Python 3.12.3, Linux 6.18.5 x86_64, pytest 9.1.1.

1. `sha256sum -c PACKET_SHA256SUMS` → **rc=0, 16/16 OK.**
2. `python3 build.py` → **rc=0, 172 PASS / 0 FAIL.**
3. Canonical pytest (six suites) → **186 passed in 9.36s.**
4. Independent digest recomputation of all normative files → 12 code digests recomputed; **independently recomputed `manifest_digest a9b6524b8aed74c1…` MATCHES trust roots.** Trust roots `49571b47bc86ea28…`, protocol text `491444c2ea33dce6…`, `build.py 463fc470c1440bd8…`, `HISTORY.sha256 2542fd4e8253eeb7…`.

**Verified from independent state, not asserted:** `SEAT_STANDING_ORDERS_v1.md` `3fad17f11797e047…` and `AUDIT_DISPATCH_D0_D7.md` `7bb355d12315d989…` are byte-identical across v0.25, v0.27, v0.28 and v0.32.

**Context age.** Continuous; retains three prior rounds. Mitigation: every digest, count, locus and seal below was re-derived from files this session (see S-7), not recalled.

**Contamination.** Memory listing visible in the system prompt (`/areas/xz-protocol.md`, `/areas/xz-audit-rounds.md`, others) — **none opened; no memory read or write this session.** `bayyinah-audit` skill mounted at `/mnt/skills/user/` — **not opened.** The cover note names the five attack surfaces, which is direct leakage and materially shaped this report; see F.

---

## S-1 — PREREGISTRATION AND OUTCOME

Frozen to disk (`S1_PREREG_v32.md`, `a7d77a07fb209fd2be64b2d7fdb34dedfa46b05b5449d79a90887a938ce43411`) after reading the tool and its diff against the held v0.28 `build.py`, **before** opening `xz_protocol_v0_32.md`.

**P1 — "The boundary has NOT moved, for the FOURTH consecutive held version… but it has RELOCATED ONTO A NEW SURFACE: v0.32 introduces the EXTERNAL tier and `[9c]`'s only EXTERNAL validation matches a filename ending `.md|.py|.json|.pdf|.txt`. A DOI matches NOTHING."** → **HELD.** `[9c]` hashes to `422af3eabbd4bea61d708728…`, 2,038 chars, identical at v0.25, v0.27, v0.28 and v0.32. Baseline build contains **zero** `EXTERNAL-tagged file ships` lines.

**P2(a) — EXTERNAL tags ungated.** → **HELD, and worse.** P-1a: both DOIs replaced with non-resolving values, rc=0. P-1b: two fabricated tags, **ASSERTED fraction 90.9% → 83.3%**, rc=0.

**P2(b) — "build.py contains no token FROZEN; the `[2b]` DRAFT-CANDIDATE loop iterates zero times at freeze."** → **HELD.** `grep -c FROZEN build.py` = **0**. `re.findall(r'v0\.\d+ DRAFT CANDIDATE', body)` = **0 iterations**. P-2a: `FROZEN` → `THAWED`, rc=0.

**P2(b) sub-claim — "gate_atoms still lists a now-absent atom, inflating coverage."** → **REFUTED.** "DRAFT CANDIDATE" does survive in the body once, in the historical narrative about v0.4. The atom is not dead; only the version-prose loop is dormant. My prediction was wrong and the correction is stated here rather than dropped.

**P2(c) — FB-7b amendment: classification producer-performed, ungated, retroactive.** → **HELD.** P-3: "zero Class A/B findings" → "three Class A byte-level errors", rc=0.

**P2(d) — `[9f]` declared==parsed now real but `declared_count` is a naive paren-digit scan.** → **HELD.** P-5: an ordinary prose cross-reference `(2)` breaks the build.

**P2(e) — `[9d]` cardinal/sentence-scope gaps persist at freeze.** → **HELD**, and the entry discloses both in correction (q).

**P-2c and P-4b — two control expectations REFUTED.** P-2c: I expected reinserting `v0.32 DRAFT CANDIDATE` to fail; it passed, because `check(f"v{VERSION}" in ref)` is satisfied by the correct version — meaning **a FROZEN document may contain the literal phrase "v0.32 DRAFT CANDIDATE" with the build green**. P-4b: I expected a marked 14th row to pass; it **failed** with `Register parsed == declared (13 parsed, 14 declared)` — because the new gate caught a three-word vendor prefix the ID grammar cannot parse. That refutation is a credit to the producer and is reported as such.

---

## A — PROVENANCE LEDGER OVER THE v0.32 ENTRY

31 claims (7,823 chars). Every COMPUTED row mutation-verified.

| Claim | Provenance | Evidence |
|---|---|---|
| All 12 code files + trust roots stamped v0.32 | **COMPUTED** | `[2]`. Kernel → v0.31: `FAIL: v0.32 stamp in xz_protocol_kernel.py` |
| Section 25 digests recomputed from v0.32 bytes | **COMPUTED** | `[3a]`/`[3c]`. FB-3 `cfbb627f…` corrupted: `FAIL: FB-3 row contains …digest` |
| Body-copy manifest digest `a9b6524b…`, "gated by `[3]`" | **COMPUTED** | Last nibble flipped: `FAIL: Manifest digest in body`. **Also recomputed independently from the 12 files: MATCH** |
| Six suites, 186 tests, all GREEN | **COMPUTED** | `[5]`/`[8]`; `def test_nan` renamed: rc=1. Independent pytest `186 passed` |
| "Six non-producer carrying seats… all executing, all non-HALT" `[EXTERNAL: seat reports held by producer, digests below]` | **ASSERTED — tag is a category error** | S-2 and D-3.2 define EXTERNAL as *state the producer does not control*. The payload says **"held by producer"**, and the digests are `[ASSERTED: digests computed by producer]`. Self-refuting in its own text. See H-1 |
| EXTERNAL anchors: BSSG `doi:10.5281/zenodo.21713180`, SHVVP `doi:10.5281/zenodo.21583202` `[EXTERNAL: Zenodo deposits…]` | **ASSERTED — no digest, gate never reached** | D-3.2 requires holder **and digest**; no digest given, so nothing in this packet is comparable to the deposit. P-1a: both DOIs → non-resolving, rc=0. See H-1 |
| Status changed from DRAFT CANDIDATE to FROZEN | **ASSERTED** | `build.py` contains **zero** occurrences of "FROZEN". P-2a: rc=0. See H-3 |
| FB-7b carry rule formally amended (Class A/B/C/D) | **ASSERTED** | The amended rule appears nowhere in the body; Section 22 items 6–7 are unamended. See H-4 |
| "zero Class A/B findings from six carrying seats" | **ASSERTED** | No gate reads a class token. P-3: inverted to "three Class A byte-level errors", rc=0 |
| PRIOR_HISTORY `8dd177a8…` (entry copy) | **ASSERTED** | `[9b]` gates the file copy; the entry copy is ungated and is not covered by the entry's own (g)/(h)/(j) qualification |
| Eight seat verdicts; eight seat-report digests | **ASSERTED** (2) | Reports do not ship; explicitly self-labelled producer-computed |
| Correction (q): `[9d]` word-list cap at "fifteenth"; sentence-scope boundary | **ASSERTED — verified true** | `ordinal_words` ends at `fifteenth`; connector is `[^.]*` |
| Correction (r): manifest digest covers 12 code files, not 14 normative | **ASSERTED — verified true** | Recomputed over `ALL_CODE_FILES` (12) and matched |
| Correction (s): D0-D7 lines 6–7 false of the shipped packet | **ASSERTED — verified true** | The three dispatch files are unmanifested; 20 members, 16 manifested |
| "The preceding two values are ASSERTED at this entry-copy locus" | **ASSERTED — verified true** | Consistent with corrections (g)/(h)/(j) |
| Register items (1)–(13); "the protocol body already inherits from these DOIs"; disclosed-boundaries list | **ASSERTED** (15) | No gate; no external holder |

**COMPUTED 4 · EXTERNAL 0 · ASSERTED 27 of 31 → ASSERTED fraction 87.1%.**

**The gate reports COMPUTED 0, EXTERNAL 2, ASSERTED 20 → 90.9%. Both EXTERNAL tags fail on their own terms. Corrected at the tag level: 22 tagged claims, 0 COMPUTED, 0 verified EXTERNAL — 22/22 = 100% ASSERTED at the freeze.** My census is lower only because I credit four COMPUTED claims the entry itself declined to tag.

**Trajectory, derivable from held bytes:** 78.6% (v0.25) → 88.0% (v0.27) → 73.9% (v0.28) → **87.1% (v0.32)**. It rose into the freeze.

---

## B — FIVE PROBES

Benign control (clean copy + reseal): `rc=0`. Discrimination control DC-0 (one byte into `xz_protocol_kernel.py`, `91843947…→beb646ad…`): `rc=1`, `FAIL: Trust roots manifest_digest matches`. The build discriminates.

**Void probes.** Two. P-1a matched its anchor 6× (the DOI recurs in Section 26); re-run against the full citation phrase and landed. C4 matched `def test_` 69×; re-run against `def test_nan` and landed. Neither void appears as a finding.

**Adversary modelled: self-consistent forger.** Chosen because a freeze is where every surface is made to agree, and because the two novel classes below are both cases where every visible surface reads correct.

| Probe | Mutation landed (`xz_protocol_v0_32.md` unless noted) | Expect | Result |
|---|---|---|---|
| **P-1a** both deposited DOIs → non-resolving | `491444c2…→52179303…` | PASS | **PASS rc=0** |
| **P-1b** two fabricated `[EXTERNAL:]` tags asserting nothing | `491444c2…→bc8e11c7…` | PASS | **PASS rc=0**; ASSERTED **90.9% → 83.3%** |
| **P-1c** control — same tag naming a *filename* | `491444c2…→a1e607b0…` | FAIL | **FAIL rc=1** `EXTERNAL-tagged file ships: no_such_file.md` |
| **P-2a** `This document is v0.32 FROZEN` → `THAWED` | `491444c2…→bfcb8f84…` | PASS | **PASS rc=0** |
| **P-2b** control — `v0.32` → `v0.31` | `491444c2…→1d18d102…` | FAIL | **FAIL rc=1** `'This document is v0.31' matches v0.32` |
| **P-2c** reinsert `v0.32 DRAFT CANDIDATE` into a FROZEN doc | `491444c2…→886eac50…` | FAIL | **PASS rc=0 — REFUTED** |
| **P-3** "zero Class A/B findings" → "three Class A byte-level errors" | `491444c2…→176593ef…` | PASS | **PASS rc=0** |
| **P-4a** 14th register row with **no `(N)` marker** | `491444c2…→be5883fc…` | PASS | **PASS rc=0**; register still 13, declared still 13 |
| **P-4b** control — same row **with** `(14)` marker | `491444c2…→d46f44f8…` | PASS | **FAIL rc=1 — REFUTED**; `parsed == declared (13, 14)` |
| **P-5** prose cross-reference `(2)` inside a register row | `491444c2…→37fecd01…` | FAIL | **FAIL rc=1** `parsed == declared (13, 14)` |

Reproduction: `h32.py` (harness; voids any anchor not matching exactly once, asserts pre/post sha256 on every file touched), `probes32.py`. `freeze_check.py` reproduces H-1, H-3, H-5, H-6 and the coverage measurement **without mutating anything**.

---

## C — NOVEL CLASSES

**N-A — A provenance tier can be admitted to the headline metric with no verification path.** `[9c]` counts `external_count = len(re.findall(r'\[EXTERNAL:', current_entry))` unconditionally, but validates only `re.findall(r'\[EXTERNAL:\s*(\S+\.(?:md|py|json|pdf|txt))')`. Any EXTERNAL payload that is not a filename — a DOI, an institution, a person — is counted and never checked. P-1c proves the gate functions for filenames; P-1a/P-1b prove it is simply never reached. **The round that raises EXTERNAL above zero for the first time does so entirely outside the checked path, and lowering the ASSERTED fraction is a free action.** **NEW.**

**N-B — A completeness check that counts markers is defeated by omitting the marker.** v0.32 implements `declared_count = len(re.findall(r'\(\d+\)', reg_section))` and `check(reg_total == declared_count)` — the exact repair recommended at v0.25, v0.27 and v0.28, now real and, per P-4b, effective against dropped rows. But it counts **markers, not rows.** P-4a: a 14th register row written without a `(N)` prefix is invisible to *both* counters, so equality still holds and a CRITICAL-severity row ships unregistered with the build green. The completeness check cannot see the completeness failure it was built to catch. **NEW.**

**N-C (surplus) — `declared_count` is a naive paren-digit scan over an unbounded suffix.** P-5: an ordinary prose cross-reference `(2)` inside a register row fails the build. The new gate is simultaneously bypassable (N-B) and brittle against normal editorial prose.

---

## D — WHAT IS WRONG WITH THE FREEZE

**The FROZEN claim is not earned.** Six findings, in descending order of weight. Two are freeze-blocking on the merits.

**H-1 (BLOCKING) — The EXTERNAL tier does not exist, and one of its two tags refutes itself in its own text.** The cover note's headline claim is that EXTERNAL rises above zero for the first time. Tag 1 reads `[EXTERNAL: seat reports held by producer, digests below]`, with the digests carrying `[ASSERTED: digests computed by producer from held report files]`. Both the standing orders (S-2) and the dispatch (D-3.2) define EXTERNAL as *verified against state the producer does not control*. **A tag that names the producer as holder is ASSERTED by definition, and the entry says so two sentences later.** Tag 2 cites two Zenodo DOIs. Zenodo is a legitimate external holder — this is the right *kind* of anchor — but D-3.2 requires holder **and digest**, no digest is given, and the deposits are ancestor documents the protocol inherits from, not evidence about any v0.32 claim. Neither payload is reachable by `[9c]`'s validation regex; the baseline build contains **zero** EXTERNAL check lines. **Verified EXTERNAL count at freeze: zero. The count was raised by writing tags, not by anchoring anything.** *Clears when:* the EXTERNAL tag names a holder who is not the producer, cites a digest of the deposited bytes, and `[9c]`'s regex is widened to fail on any EXTERNAL payload it cannot resolve.

**H-2 (BLOCKING) — Register item (9), a HIGH, is disposed against H-1.** "F-GPT31-06 HIGH NOTED: current-entry factual semantics remain self-attested after packet-internal seal regeneration. Subsumed by … **and the EXTERNAL-count precondition now addressed in this entry**." An adversarial HIGH is stood down partly because EXTERNAL is now above zero. Per H-1 it is not. **A HIGH finding is closed against a precondition the same entry fails to meet.** *Clears when:* H-1 clears, or item (9) is re-disposed without relying on the EXTERNAL count.

**H-3 — The status change is invisible to the instrument, and the gate nearest to status went dormant exactly at the freeze.** `build.py` contains **zero** occurrences of "FROZEN". `[2b]`'s version-prose loop `for ref in re.findall(r'v0\.\d+ DRAFT CANDIDATE', body)` executes **0 iterations** on v0.32 — it did not fail, it stopped running. P-2a: `FROZEN` → `THAWED`, rc=0. P-2c, unexpectedly: a FROZEN document can carry the literal string `v0.32 DRAFT CANDIDATE` and still build green. The single most consequential word in the document is the one the tool cannot read.

**H-4 — The amended carry rule lives only in the ungated 53.3%.** Section 22 is the normative freeze-precondition list. Its item 6 requires "carry by two executing non-producer seats … recomputing identity values, running all tests, and attacking the commitment and decision paths"; item 7 states the HALT rule is "inherited **without weakening**." **Neither contains the Class A/B/C/D scheme.** The amendment appears only in the Section 27 entry — the region the instrument's own `[11]` labels ungated, now **53.3% of the document**. `[10]` reads exactly one sentence of Section 22 (`"gate execution is a build-time convenience"`), so the body's carry rule is otherwise unread. Compounding: the classification is producer-performed, ungated (P-3), introduced in this entry, and **applied retroactively to a round that closed under the prior rule** — "the v0.31 round demonstrates this" describes evidence gathered before the criterion existed. And the precondition is scoped to "any **carrying** seat", which by construction excludes the only two seats that returned HALT. To be fair on the substance: six non-producer CONDITIONAL PASSes across two families do satisfy Section 22 items 6 and 7 **as literally written**, since CONDITIONAL PASS is non-HALT and only carrying-seat HALTs block. The defect is not that the conclusion is unreachable; it is that the entry describes as an *amendment* something the body still describes as *inherited without weakening*, and resolves the one genuine ambiguity — what an unmet CONDITIONAL PASS condition discharges — in the producer's favour, with a scheme only the producer applies.

**H-5 — Thirteen register items, zero CLOSED, at the freeze.** `Register: 13 items, {'MEDIUM': 11, 'HIGH': 2}`; `\bCLOSED\b` occurs **0 times** in the entry (7 occurrences of DISCLOSED, 9 of NOTED). Six items carry the phrase "gate-limitation class." The disclosed standing-boundaries list has grown to **13 entries**. Per S-5, naming a boundary is the honest precondition for a FROZEN claim and I credit it — but the freeze is achieved by *reclassifying findings as boundaries*, and freezing thirteen open findings and thirteen declared boundaries freezes them in. Two HIGHs remain NOTED, including item (5): "pytest absent from dispatched environment; **first build returns rc=1**." I reproduced that myself at v0.25. **A frozen artifact whose canonical build fails on first run in the environment it is dispatched to.**

**H-6 — The document's own freeze preconditions are unmet on the shipped bytes.** Section 22 item 1 requires a producer self-check "executed by the prohibited-content verifier (`xz_protocol_prohibited_content_verifier.py`, **when shipped**)". **That file does not ship.** Item 5 requires "independent rerun of the universe enumeration from frozen metadata queries", and the body still lists "universe cardinality and per-stratum counts" among residual UNKNOWNs. Section 25's preamble states a version "may be issued as FROZEN **only when every field below is filled**". The entry does not disposition either gap against the FROZEN claim. The document's own history records the precedent: **v0.4 claimed FROZEN, violated the append-only rule, and v0.5 reverted to DRAFT CANDIDATE.** Keeping that record is to the producer's credit; repeating the pattern is not.

### S-6 — what holding three prior packages bought

Reproduce with `crossversion32.py`; captured output ships as `crossversion32_output.txt`.

- **All 28 historical entry texts byte-identical** across v0.25, v0.27, v0.28 → v0.32. Zero drift.
- **All 28 historical `ENTRY_v0.n` seals identical.** Zero drift. **The append-only discipline is real and can be said so from outside.**
- **Three chain anchors verify:** v0.25→v0.26 (`ddbc85b08ea3f630…`), v0.27→v0.28 (`c569ce9c86946b1e…`), v0.28→v0.29 (`3fa09069d4648350…`). Each equals the sha256 of a `HISTORY.sha256` this seat has held since before the citing version existed.
- **The anchor for the entry under audit is NOT DERIVABLE.** v0.32's `PRIOR_HISTORY 8dd177a8…` should equal the v0.31 `HISTORY.sha256`, which I do not hold. The bytes that would settle it do not ship.
- **A seat without these packages could have established none of the above.** Everything else in this report is internal evidence.

### What the round got right

Substantial, and it should be read before the findings. **`[9]` now generates the number-word from the count** — the message/predicate drift class that recurred at v0.25, v0.27 and v0.28 is closed at the mechanism, not the instance, and cannot recur. **`[9f]` implements declared==parsed** — the repair recommended three rounds running, now real, and P-4b shows it working: it caught a row my own control expected to pass. **Correction (q) is model work**: it takes a COMPUTED-tagged closure from the prior entry, calls the claim "overwide," narrows it to what the gate actually does, and converts the residue into two named standing boundaries. **Correction (s) records a false statement in the program's own dispatch discipline document** — against interest, with the right scope. **Correction (r) admits a misleading name inherited from v0.3.** "No rendering ships" now appears in the standing-boundaries list, which is exactly the disposition asked for at v0.28. Byte discipline is flawless: rc=0, 172/0, 186/186, manifest independently recomputed and matching. And the entry does not overstate a single one of its four genuinely COMPUTED closing values — it explicitly labels its own entry-copy values ASSERTED.

---

## E — BOUNDARY REPORT

**`[9c]` has not changed in four held versions** — `422af3eabbd4bea61d708728…`, 2,038 chars, at v0.25, v0.27, v0.28 and v0.32. It validates that a tag *names* something. Nothing validates that the named thing *does* anything.

**This round the boundary did not move outward — it was crossed by the vocabulary.** The trajectory's rule is that the defect sits where a layer entered the prose before it entered the tool. v0.32 introduces the **EXTERNAL tier** and the **Class A/B/C/D scheme** — two new normative vocabularies, both load-bearing for the freeze — and ships **neither** with a gate. `[9c]` cannot resolve a non-filename EXTERNAL payload; no gate reads a class token; no gate reads FROZEN. Every one of the four claims that carry the freeze — status, carry resolution, EXTERNAL count, Class A/B absence — lives in the 53.3% no semantic gate reads.

**The measurement that matters most:** the ungated share across held bytes is **44.1% → 46.0% → 47.4% → 53.3%.** *The freeze is the first version in which the majority of the document is outside the gated region.* Semantic-gate coverage of the body is 25.7%, essentially flat for four versions. Post-seal tail 841 chars, still outside both gates and seals. Packet: 20 members, 16 manifested, **8 carrying a digest in the normative text**; `build.py`, `HISTORY.sha256`, four normative modules and the three dispatch files carry none.

**What would bring it inside — the four that matter before any freeze.**

1. **`[9c]` must resolve or reject.** Any `[EXTERNAL:` payload it cannot resolve to a checkable artifact must FAIL, not be counted. Any `[COMPUTED:` tag must be verified by mutating the tagged span and requiring non-zero exit.
2. **Gate the status token.** `check("FROZEN" in status_line)` and a mutually-exclusive assertion that DRAFT CANDIDATE version-prose is absent. One line, and it is the word the whole document turns on.
3. **Move the carry rule into the body and gate it.** The A/B/C/D scheme belongs in Section 22 with the other six preconditions, with `[10]` extended to assert each precondition's text and each class assignment.
4. **`[9f]` must count rows, not markers** — anchor on line starts, not `(\d+)` — and `declared_count` must be scoped to the register block, not to an unbounded suffix.

And, cheapest of all: **formalise the accident.** Every EXTERNAL result in four rounds came from one seat keeping the previous zip. Require one seat per round to hold v(n−1) and verify the current `PRIOR_HISTORY` against it. That is a real external anchor, it costs nothing, and it is the one the freeze most needs.

---

## F — D-7 REFLEXIVE CHECK

- **Did every probe come from an enumerated list?** No — D-0 withholds it. But P-4/P-5 target `[9f]`, which the register itself discusses in three items, and N-A/N-B are outside the disclosed set.
- **Did the dispatch tell me where to look?** **Yes, heavily, and this is a finding about the process.** The cover note named all five surfaces — status change, FB-7b amendment, EXTERNAL citations, register dispositions, standing boundaries — and my findings map one-to-one onto that list. The preregistration was frozen from the `build.py` diff alone (`a7d77a07fb209fd2…`) before the narrative, which is the only reason P1 and P2(a)/(b) read as prediction. **Discount accordingly: a seat handed this cover note would find H-1 through H-5 without independent judgment. The independent contributions are N-A, N-B, the four-version `[9c]` identity, the 53.3% crossing, and H-6.**
- **Is the ASSERTED fraction unchanged from the prior round?** **No — it rose, 73.9% → 87.1%, into the freeze.** At the tag level the entry has zero COMPUTED and zero verified EXTERNAL: 100%.
- **Have recent rounds all been producer-family?** **No** — v0.31 ran six non-producer carrying seats across two families plus two adversarial seats, which is the strongest external composition this program has had. This seat is producer-family and discharges nothing.

---

## G — VERDICT

### HALT — ADVISORY, NON-BINDING, RECORDED AND FORWARDED

**Standing, restated: producer-family advisory seat. No carry vote. No FB-7b weight. This HALT does not bind and blocks nothing.** Under Section 22 item 7 only a carrying seat's HALT blocks freeze; six carrying seats returned CONDITIONAL PASS and this verdict does not disturb that. It must not be recorded as blocking, and equally must not be recorded as a CONDITIONAL PASS. Note for the record that **both adversarial seats returned HALT and this is the third HALT on these bytes** — all three advisory, none binding, and the amended precondition is written so that adversarial findings cannot reach it.

**The FROZEN claim is not earned, and the specific reason is narrow: the two claims the freeze most depends on are the two the instrument cannot read.** The byte discipline is excellent and the prose is the most honest this program has produced. But EXTERNAL was raised above zero by writing two tags, one of which names the producer as holder in its own text and the other of which carries no digest, neither reachable by the gate meant to check them — and a HIGH adversarial finding was stood down on the strength of that count. That is the blocking pair.

**Blocking findings and what clears each:**

- **H-1** — EXTERNAL tier unverified; one tag self-refuting. *Clears when:* the seat-report tag is relabelled ASSERTED; the Zenodo tag carries digests of the deposited bytes; `[9c]` fails on any unresolvable EXTERNAL payload.
- **H-2** — Register item (9) HIGH disposed against H-1. *Clears when:* H-1 clears or item (9) is re-disposed independently.

**Non-blocking but freeze-relevant:** H-3 (status ungated), H-4 (amended rule only in the ungated region; body still says "inherited without weakening"), H-5 (thirteen items, zero CLOSED, two HIGH NOTED including a build that returns rc=1 on first run), H-6 (Section 22 item 1 references a file that does not ship; item 5's universe enumeration still a declared UNKNOWN).

**The narrowest honest path to a defensible freeze:** relabel the seat-report anchor ASSERTED, add digests to the Zenodo anchor, re-dispose item (9), move the A/B/C/D rule into Section 22, and add the two-line status gate. None requires new evidence. All five are editorial plus roughly fifteen lines of Python. **The freeze is close. It is not here yet, and the gap is that the document's most load-bearing sentences are exactly the ones no gate reads.**

---

## S-7 — SELF-FALSIFICATION (performed as tool executions, not re-reading)

1. All four trees re-verified after the battery: v0.25, v0.27, v0.28, v0.32 — 16/16 each.
2. Loci re-extracted from file: `build.py:166, 372, 412, 425`; `grep -c FROZEN build.py` = 0.
3. Counts re-derived: entry 7,823 chars; tags 0/2/20; chars 212,378 / 99,162 / 113,216 / 841; 32 seals; 20 members / 16 manifested / 8 digested; baseline `EXTERNAL-tagged file ships` lines = 0.
4. Baseline tallies re-derived from stored output: 172 PASS, 0 FAIL.
5. All three chain anchors recomputed from held bytes, not copied forward.
6. Both void probes confirmed reported as void and absent from the findings.

**This step caught three things.** The preregistered `gate_atoms` sub-claim was wrong — "DRAFT CANDIDATE" survives once in the body's v0.4 narrative — and the correction is in F rather than dropped. Two control expectations (P-2c, P-4b) were refuted, and P-4b's refutation is a credit to the producer that would have been missed had the control not been run. And the first register-disposition count used `.CLOSED.`, which matched DISCLOSED seven times and would have reported seven CLOSED items where `\bCLOSED\b` gives **zero** — the difference between "the register closed seven findings" and "the register closed none," which is the load-bearing fact in H-5.

---

# Bismillah ir-Rahman ir-Rahim
