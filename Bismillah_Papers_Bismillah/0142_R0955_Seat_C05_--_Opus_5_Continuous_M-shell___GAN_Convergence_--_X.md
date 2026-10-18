# Bismillah ir-Rahman ir-Rahim

# R0955 -- Seat C05 -- Opus 5 Continuous M-shell / GAN Convergence -- XZ Protocol v0.47

**Chronological Index:** 142 of 995  
**Date:** 2026  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SEAT_C05_OPUS5_GAN_v47_REPORT.md  
**Source Format:** md  
**SHA-256:** `019e2a8321bf5eff1e15b30e00f1e60bf35fec66fa275bfb95f0ec911e95fce0`  

---

## R0955 · Seat C05 -- Opus 5 Continuous M-shell / GAN Convergence -- XZ Protocol v0.47

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SEAT_C05_OPUS5_GAN_v47_REPORT.md
- source_format: md
- text_sha256: 019e2a8321bf5eff1e15b30e00f1e60bf35fec66fa275bfb95f0ec911e95fce0

# Seat C05 -- Opus 5 Continuous M-shell / GAN Convergence -- XZ Protocol v0.47

**Seat:** Opus 5 CONTINUOUS from R5 S05 (GAN)
**Family:** Claude (Anthropic) -- producer family, advisory, non-carrying, non-binding
**Finding prefix:** F-SC05-47
**Framework:** GAN Convergence
**Round:** Convergence Round 6, v0.47 DRAFT CANDIDATE
**Mode:** Mode A (substrate verifier), plus **external-anchor mode**: this seat holds the R5 dispatch packet (protocol `c4e78d67830e81f2...`, HISTORY.sha256 `558b2a2c91af4ee5...`) verified against the R5 manifest last round.

> **Verdict: HALT (advisory). Escalate.**
> **Severity ledger: 1 CRITICAL / 4 HIGH / 4 MEDIUM / 2 LOW / 1 INFORMATIONAL.**
> **The append-only chain is broken. v0.47 must not be carried forward as-is.**

---

## S-0. Seat conformance

Continuity is **satisfied** this round. This seat is genuinely continuous from R5 S05 -- same instance, same session, holding the R5 packet on disk. The R5 conformance failure (F-S05-46-00, memory-filesystem contamination of a seat labelled fresh) does not apply to a seat labelled continuous.

Two things follow, and both are load-bearing.

1. **Continuity is what made the CRITICAL detectable.** Section 22.2 states that no internal gate can detect a self-consistent forgery and that externally held bytes are the only defense. This seat holds the v0.46 packet. Every internal gate in v0.47 is GREEN and the chain is nevertheless broken. Continuity was not a weakening of this seat; it was the detector.
2. **Continuity is also this seat's bias.** My priors are my own R5 findings, so I am prone to re-finding them and to confirming my own prior calls. Mitigations applied: every claim below re-derived from bytes this round, and one R5 finding **withdrawn** as a false positive (F-SC05-47-12).

---

## S-1. Packet integrity and standing properties

Reconstructed via `python3 setup.txt`; all 12 code files match their declared BYTES headers.

| Check | Result |
|---|---|
| `sha256sum -c PACKET_SHA256SUMS` | rc=0, 16/16 OK |
| `python3 build.py` | `BUILD PASSED: all checks GREEN`, 193 PASS / 0 FAIL |
| Protocol text | 294,529 bytes, 1,223 lines -- matches dispatch |
| Protocol digest | `adf601f25dc5ab4d...` -- matches manifest |
| Packet digest | `faee04bf5bcf6049b365ba63a4904dee8b43f5e7e721278200ee1c6c167a434c` -- **dispatch declares `0c5f7264...`, which is the v0.46 value** (F-SC05-47-11) |
| Tests | 186 passed; collected(186) == AST(186); 27/29/18/14/29/69 |
| Code partition | 6 CODE_MODULES + 6 TEST_SUITES |
| Stamps | v0.47 on all 12 code files + trust roots |
| `[2d]` self-version gate | present and PASS: docstring 0.47 == VERSION 0.47 |
| Entries | 47, prose says "forty-seven" |
| Seals | 47 entry seals + FULL_SECTION_27, all match **current** bytes |
| PRIOR_HISTORY | `c51b64e9e2d1e985...`, derivation self-consistent -- **and byte-false against the external anchor** (F-SC05-47-01) |
| Register | 10 parsed == 10 declared; {HIGH: 2, MEDIUM: 8}; 17 unique IDs |
| EXTERNAL count | 1 |
| Standing boundaries | **30 present, 29 declared** (F-SC05-47-02) |
| Manifest digest | `45364f2669bb6614...` -- recomputed from scratch, matches |
| Em-dash / brand | clean |

## S-2. Correction (ay) and body repairs [a]-[g]

- **(ay) TRUE on its quoted string, wrong in its conclusion.** The v0.46 register item six reads verbatim as (ay) quotes it. The v0.46 trust-roots timestamps are `2026-08-07T20:00:00.000000Z` as claimed, though (ay) narrates them as `2026-08-07T20:00:00Z`, dropping the six zero-microsecond digits that are the evidence. The inference that the defect "was substantively repaired in the bytes" is false: see F-SC05-47-03.
- **[a] TRUE** -- front-matter status rewritten for the R5 audit.
- **[b] TRUE** -- Section 22.2 reads "For carried entries (v0.1 through v0.46)".
- **[c] TRUE** -- Section 22.3 reads "carried at v0.38-v0.47".
- **[d] TRUE** -- FB-7b row reads "RESOLVED v0.31; PENDING RE-CARRY v0.47".
- **[e] TRUE** -- Post-v0.31 note now covers Convergence Rounds 2-5 and records the Kimi K3 Seat 2 CONDITIONAL PASS.
- **[f] TRUE** -- build.py docstring at v0.47 and gate [2d] added and passing.
- **[g] LANDED IN THE WRONG PLACE.** It is listed as a body repair and it edited a sealed Section 27 entry. See F-SC05-47-01.

---

## S-3. Findings

### F-SC05-47-01 [CRITICAL] [Class A] -- the sealed v0.46 entry was mutated in place; PRIOR_HISTORY is byte-false against the external anchor

- **Locus:** `xz_protocol_v0_47.md:1202` (sealed v0.46 entry); `HISTORY.sha256` line `ENTRY_v0.46`; declared PRIOR_HISTORY at `:1219`; declared as body repair [g] at `:1217`.
- **Substance:**

  The v0.46 shipped bytes, which this seat holds and verified last round against the R5 manifest, read:

  > Convergence Round 4 on v0.45 bytes: **4 fresh seats (Opus 5, Kimi K3, Gemini, GPT), 4 families, 1 shell (LEO).**

  The v0.47 bytes carry, in the same sealed entry:

  > Convergence Round 4 on v0.45 bytes: **4 deployed seats (Opus 5, Kimi K3, Gemini, GPT; 3 with verified independence, 1 with independence structurally false per F-S01-45-00), 4 families, 1 shell (LEO).**

  Entry length 5,538 to 5,627 bytes, delta +89. A full entry-by-entry diff of Section 27 against the held v0.46 bytes shows exactly one carried entry differs -- v0.46 -- and that Section 27's non-entry text differs only in the closing "End of XZ Protocol" line. So this is a single, targeted, in-place edit of a sealed historical entry.

  The seal chain moved with it. `ENTRY_v0.46` was `121e144e566b47e3...` in the v0.46 packet and is `36f1787a6c34ad16...` in the v0.47 packet. `FULL_SECTION_27` was `4d9559bc3bb4d96a...` and is `0351ad50ac755081...`. A sealed entry's seal changed after sealing.

  The chain value is therefore false. The v0.47 entry declares `PRIOR_HISTORY c51b64e9e2d1e985...`. The true SHA-256 of the v0.46 `HISTORY.sha256` file is `558b2a2c91af4ee5e1ecc52c377d92534129d710e3ef3aa2aec9367ebed83325`. Causation proved by construction: restoring the v0.46 entry text and its original `ENTRY_v0.46` seal and re-running build.py's own `derive_prior_history` returns exactly `558b2a2c91af4ee5...`. The mutation is the sole cause.

  **build.py passes GREEN because it recomputes over the mutated bytes.** `HISTORY.sha256` ships inside the packet and was regenerated, so every internal seal is mutually consistent. This is the self-consistent forgery that Section 22.2 names as the residual blind spot -- realized in shipped bytes for the first time. Unlike v0.41, which the build caught because its regex was applied inconsistently, this one is invisible to every gate in the packet.

  It is not disclosed. The v0.47 entry contains no reference to an in-place mutation, and Section 22.2 still records the historical tally as "eight recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, and v0.41". This is the ninth.

  **This seat is a contributing cause and says so.** R5 finding F-S05-46-02 prescribed: *Restate as "4 deployed seats, 3 with independence intact, 1 with independence structurally false (F-S01-45-00)"*. That disposition named the replacement text and named neither the locus nor the admissible route. The producer applied it where the text was, which was inside a sealed entry. The mechanism the protocol reserves for exactly this -- an append-only correction in the current entry -- was available and was used three paragraphs earlier for (ay).

- **Disposition:** Do not carry v0.47. Restore the v0.46 entry verbatim to its `c4e78d67...` form, regenerate `HISTORY.sha256`, and confirm `ENTRY_v0.46` returns to `121e144e566b47e3...` and PRIOR_HISTORY to `558b2a2c91af4ee5...`. Re-land [g] as append-only correction (az) in the v0.47 entry, in the form (ay) already models. Record the event as the ninth in-place mutation and update the Section 22.2 tally from eight to nine. Add a gate that pins the prior packet's `HISTORY.sha256` digest as a constant in build.py and fails when the derivation does not reproduce it -- that converts the external anchor into an internal check for the one link where it is cheap. Ship the prior-packet digest in every dispatch so any seat, continuous or fresh, can run this test.
- **Cross-reference:** R5 F-S05-46-02 (this seat's under-specified disposition, contributing cause); Section 22.2 self-consistent-forgery boundary; v0.41 retraction at `:1156`; v0.4 defect entry; standing boundary 21.

### F-SC05-47-02 [HIGH] [Class A] -- standing boundary count is 30, declared 29

- **Locus:** `xz_protocol_v0_47.md:1219`, "Disclosed standing boundaries -- 29 items".
- **Substance:** Parsing the list and normalizing the one item with an internal comma ("A-side seam (condition_a.py, SHIELD-scoped)") yields 30 items. The arithmetic confirms it: v0.46 declared 27, and v0.47 adds three -- register item (9) f-string nested quotes (F-S07-46-02), register item (10) fb_spec omits FB-7b locus (F-S07-46-03), and correction (ay)'s explicit disclosure of the ungated trust-roots timestamp, which appears as the thirtieth list item. 27 + 3 = 30. The dispatch repeats the wrong figure ("standing boundaries 27 to 29"). This is the same count-narration class the round exists to close, on the same list, one version after the same list's count was corrected from 25 to 27.
- **Disposition:** Correct to 30. Generate the count from the parsed list in build.py and fail [9f] on mismatch, in the way [9] already does for entry count and "forty-seven". The list is comma-delimited with one known internal-comma item; replace that comma with a semicolon so a naive parse is exact.
- **Cross-reference:** F-SC05-47-08 (a COMPUTED tag would have caught this); v0.46 body repair [e]; standing boundary 20 (no boundary-retirement mechanism, so the list only grows and the count only gets harder).

### F-SC05-47-03 [HIGH] [Class A] -- F-S05-46-07 declared CLOSED; the finding is unrepaired and the bytes prove it

- **Locus:** `xz_protocol_v0_47.md:1213` register item (2); correction (ay) at `:1215`; `xz_protocol_trust_roots_PUBLIC.json`, four `"generated"` fields.
- **Substance:** A byte diff of the trust-roots file between the v0.46 and v0.47 packets shows exactly two changed lines: `"protocol"` and `"manifest_digest"`. All four `"generated"` values are byte-identical across the version bump: `2026-08-07T20:00:00.000000Z`, four copies, whole hour, six zero microsecond digits. The file was regenerated -- the manifest digest changed to `45364f2669bb6614...` because the code files changed -- and the generation timestamp did not move. That is direct proof of the R5 finding: the field is a carried constant, not a generation record. F-S05-46-07's substance was fabricated provenance, not staleness; its prescribed disposition was to emit the field from the generating tool or delete it. (ay) closes the staleness limb (F-S01-45-05) and explicitly leaves the gate limb open as boundary 30. Neither limb is the finding. Declaring it CLOSED converts an open Class A surface into a closed one in the register while the bytes are unchanged.
- **Disposition:** Reopen F-S05-46-07. Either emit `generated` from the key-generation tool at generation time, or delete the field and state in `manifest_digest_note` that key generation time is not recorded. Add a gate asserting the value is not a whole-hour zero-microsecond constant and not identical to the prior version's. Correct register item (2) to close only F-S01-45-05.
- **Cross-reference:** R5 F-S05-46-07; correction (ay); standing boundary 30; F-SC05-47-05 (closure without repair and omission without disposition are the same failure of the register).

### F-SC05-47-04 [HIGH] [Class A] -- "All 3 v0.46 corrections verified TRUE on bytes by every executing seat" is false as to this seat

- **Locus:** `xz_protocol_v0_47.md:1211`, and front matter at `:5` ("All 3 v0.46 corrections verified TRUE on bytes").
- **Substance:** This executing seat did not verify all three. R5 finding F-S05-46-03 [MEDIUM] [Class A] was raised against correction (ax): the replacement ID `F-S6-44-07` conforms to no convention present in the packet. The round that audited v0.44 uses zero-padded seat numbers on bytes (`F-S04-44-01`, `F-S04-44-02`, `F-S12-44-01` through `F-S12-44-04`), so Kimi Seat 6 on v0.44 would be `F-S06-44-07`; the only `F-S6` namespace in the packet (`F-S6-03` through `F-S6-06`) belongs to the eight-seat round that audited v0.43, not v0.44; and `F-S2-10`, sitting in the same sealed line being corrected, falsifies the pattern (ax) asserts as canonical. `F-S6-44-07` still occurs nowhere in the packet except the two loci that invent it. F-S05-46-03 appears nowhere in the v0.47 register -- not closed, not noted, not disclosed, not rejected. The claim is also unverifiable from shipped bytes in either direction, since no seat report ships, and it is not tagged.
- **Disposition:** Restate as "all 3 v0.46 corrections verified TRUE by N of 8 executing seats; F-S05-46-03 dissents against (ax)". Disposition F-S05-46-03 on its merits: correct the ID to the zero-padded form, or declare it unverifiable and tag it [EXTERNAL] against the Kimi Seat 6 report.
- **Cross-reference:** R5 F-S05-46-03; correction (ax) in the v0.46 entry; F-SC05-47-05.

### F-SC05-47-05 [HIGH] [Class A] -- nine of thirteen R5 Seat 5 findings are undispositioned, in the entry that NOTES that exact defect

- **Locus:** `xz_protocol_v0_47.md:1213`, register items (1) through (10), and item (5) specifically.
- **Substance:** Register item (5) reads: "F-S01-46-01 MEDIUM NOTED: three R4 Seat 1 findings (F-S01-45-09/10/11) absent from the v0.46 register (1-seat)." The producer therefore recognizes undispositioned findings as a defect class. In the same register, nine of this seat's thirteen R5 findings are absent: F-S05-46-00, -01, -03, -04, -08, -09, -10, -11, -12. Only -02, -05, -06 and -07 appear. Of the nine, one is a valid withdrawal by this seat (-09, see F-SC05-47-12), one was silently repaired without a register item (-01, see F-SC05-47-07), two persist unrepaired in the shipped bytes (-08 and -11, verified this round), one recurs in this very dispatch (-12, see F-SC05-47-11), and one is contradicted by a claim in the entry itself (-03, see F-SC05-47-04). The entry NOTES the class at a scale of three and commits it at a scale of nine.
- **Disposition:** Every finding from every executing seat receives a disposition -- CLOSED, NOTED, DISCLOSED, or REJECTED with reasons. Add a gate that parses seat finding prefixes from the register and fails when a dispatch-listed seat namespace has gaps, or, if seat reports are not machine-readable, require the dispatch to ship a finding-ID inventory the register must cover.
- **Cross-reference:** register item (5); F-SC05-47-03, -04, -07, -08, -10, -11, -12 (each is one of the nine).

### F-SC05-47-06 [MEDIUM] [Class A] -- "4 M-shell fresh" is unqualified, in the entry that repairs an unqualified freshness claim

- **Locus:** `xz_protocol_v0_47.md:1211`, "8 seats (4 LEO continuous + 4 M-shell fresh), 4 families, 2 shells".
- **Substance:** Body repair [g] exists to qualify the v0.46 entry's unqualified "4 fresh seats" with independence status. The v0.47 entry then makes an unqualified freshness claim of its own about the round it is recording, although this seat's R5 report declared in S-0 that M-shell freshness was not achieved and raised F-S05-46-00 to say so, and although the producer had that report -- register item (1) cites F-S05-46-05 from it. The defect being repaired and the defect being committed are the same defect, one paragraph apart.
- **Disposition:** Restate as "4 M-shell seats dispatched fresh, of which N with verified independence". Apply the same standing rule proposed at R5: seat-independence status appears in the same sentence as any seat count. Disposition F-S05-46-00.
- **Cross-reference:** body repair [g]; F-SC05-47-01 (the same repair, wrong locus); R5 F-S05-46-00 and F-S05-46-02.

### F-SC05-47-07 [MEDIUM] [Class A] -- F-S05-46-01 was repaired in the prose and omitted from the repair map, one entry after (ay) corrected that exact defect

- **Locus:** `xz_protocol_v0_47.md:1211` ("All 3 v0.46 corrections") against the v0.46 entry's "All 5 v0.45 repairs"; register at `:1213`.
- **Substance:** R5 F-S05-46-01 found the v0.46 phrase "All 5 v0.45 repairs" unanchored, since v0.45 landed 5 corrections plus 4 body repairs and the parallel sentence one entry earlier counted body repairs. The v0.47 entry fixes the ambiguity by naming the basis explicitly -- "All 3 v0.46 **corrections**" -- which is correct on bytes: v0.46 issued (av), (aw), (ax). Good repair, and no register item, no correction, no line in the repair map. Correction (ay) exists in this same entry precisely to fix a defect "substantively repaired in the bytes but omitted from the declared repair map". The class recurs inside the entry that corrects it.
- **Disposition:** Add a register item recording the closure of F-S05-46-01 by the wording change at `:1211`. Treat "repaired in bytes, absent from the repair map" as a standing check applied to every diff before sealing.
- **Cross-reference:** correction (ay); R5 F-S05-46-01; F-SC05-47-05.

### F-SC05-47-08 [MEDIUM] [Class D] -- the COMPUTED channel is still dead, and two of this round's Class A errors sit inside ASSERTED blocks

- **Locus:** build.py gate [9c] output: `COMPUTED: 0, EXTERNAL: 1, ASSERTED: 5`, `ASSERTED fraction 5/6 (83.3%)`; entry text `:1211-1219`.
- **Substance:** R5 F-S05-46-08 is undispositioned and unrepaired. The COMPUTED tag count is now 0 at v0.40, 0 at v0.41, 0 at v0.42, 1 at v0.43, 0 at v0.44, 0 at v0.45, 0 at v0.46, 0 at v0.47. Gate [9c] still prints the fraction and passes at any value. This round supplies the concrete cost: the standing-boundary count (F-SC05-47-02) and the PRIOR_HISTORY value (F-SC05-47-01) are both build-derivable, both were tagged [ASSERTED], and both are wrong. A COMPUTED floor with tool-emitted values would have caught the boundary count before sealing, and would have forced the PRIOR_HISTORY value through a derivation the producer would have had to reconcile against the prior packet.
- **Disposition:** Fail [9c] when a claim matching a gate-computed pattern -- test count, stamp count, entry count, boundary count, EXTERNAL count, any 64-hex value, PRIOR_HISTORY -- carries [ASSERTED]. Set a COMPUTED floor and disclose the number as chair-fitted, as Section 22 item 7 already does for its own thresholds.
- **Cross-reference:** R5 F-S05-46-08; F-SC05-47-01, -02; coverage measurement (body 35.3%, semantic-gate coverage 28.4% of body, Section 27 64.7% at zero coverage).

### F-SC05-47-09 [MEDIUM] [Class B] -- the external-anchor claim is unverifiable, untagged, and now in tension with the bytes

- **Locus:** `xz_protocol_v0_47.md:1211`, "Append-only integrity confirmed against externally held v0.45 bytes by Opus 5 Seat 1 and Kimi K3 Seat 2 -- first external-anchor verification in the convergence series".
- **Substance:** Nothing in the packet supports this. The seat reports do not ship, the v0.45 packet does not ship, and the EXTERNAL count stays at 1, naming only the v0.40 dispatch manifests and two Zenodo DOIs. A first-of-its-kind external-anchor verification is exactly the claim that should increment the EXTERNAL count and name its anchor with a digest. The claim is also uncomfortable next to F-SC05-47-01: in the same repair cycle in which two seats certified the v0.45 link, the v0.46 link was broken. Certifying link N-1 while breaking link N is the failure mode a chain is supposed to prevent, and it happened because the anchor test was applied backwards one step instead of forwards to the entry being written.
- **Disposition:** Tag [EXTERNAL] and increment the count. State the anchor digests -- the v0.45 `HISTORY.sha256` value each seat held. Make forward anchoring standing practice: the entry being sealed must reproduce the immediately prior packet's `HISTORY.sha256` digest, and the dispatch must ship that digest.
- **Cross-reference:** F-SC05-47-01; Section 22.2 anchors (a), (b), (c); EXTERNAL count claim at `:1219`.

### F-SC05-47-10 [LOW] [Class E] -- Section 22 subsections still ship out of order

- **Locus:** `xz_protocol_v0_47.md` -- 22.1 at `:704`, 22.3 at `:708`, 22.2 at `:718`.
- **Substance:** Unchanged from v0.46. R5 F-S05-46-11 is undispositioned. Not gated, not on the 30-item boundary list, so neither repaired nor disclosed. The cost is not cosmetic: the dispatch's own checklist and the repair map both address these subsections by number, and body repairs [b] and [c] this round touch 22.2 and 22.3 in the order opposite to document order.
- **Disposition:** Reorder to 22.1, 22.2, 22.3, or add a heading-order gate and place the deliberate ordering on the boundary list.
- **Cross-reference:** R5 F-S05-46-11; F-SC05-47-05.

### F-SC05-47-11 [LOW] [Class A] -- the R6 dispatch narrates the v0.46 packet digest

- **Locus:** `prompt.txt`, "**Packet digest:** PACKET_SHA256SUMS = `0c5f7264...` (verify from shipped bytes)".
- **Substance:** `0c5f7264...` is the v0.46 packet digest, verified by this seat at R5. The v0.47 value is `faee04bf5bcf6049...`. R5 F-S05-46-12 raised exactly this -- corrections not propagating to the dispatch that carries the round -- and it is undispositioned. The hedge "(verify from shipped bytes)" is good practice and does not make a stated wrong value right; a seat that trusted the stated digest would have accepted a v0.46 packet as v0.47. The dispatch also repeats the wrong boundary figure ("27 to 29", see F-SC05-47-02).
- **Disposition:** Generate the dispatch header from the shipped packet rather than restating it, and add a pre-dispatch check that every digest and figure in the prompt greps against the shipped bytes.
- **Cross-reference:** R5 F-S05-46-12; F-SC05-47-02, -05.

### F-SC05-47-12 [INFORMATIONAL] [Class E] -- this seat withdraws R5 finding F-S05-46-09

- **Locus:** R5 report F-S05-46-09; `xz_protocol_v0_47.md:1176`, correction (al).
- **Substance:** At R5 I raised the contradiction between the in-place-mutation attributions at `:873` (v0.9 once, v0.17 twice) and `:1156` (v0.9 twice, v0.17 once), and flagged it as possibly prior-surfaced because the packet ships no seat reports. It was prior-surfaced. Correction (al), sealed at v0.43, reads: "v0.41 entry 'v0.9 x2, v0.11 x2' multiplicities are inverted... Compensating errors preserve the total but the itemization is false (F-SB-09)." The defect was already found, already dispositioned, and already mitigated. **F-S05-46-09 is withdrawn as a duplicate.** A false positive from a seat is the same category of error as a false negative from a gate, and it is recorded here rather than quietly dropped.
- **Disposition:** For the producer: add a finding-ID index to the body mapping every ID to its entry and disposition, so seats can check whether a defect is already closed before raising it. This seat's false positive is the argument for that index. For this seat: search corrections for the defect substance before raising, not only the defect locus.
- **Cross-reference:** correction (al) at v0.43; correction (ao) at v0.44, which corrected (al)'s citation; F-SB-09.

---

## S-4. GAN Convergence framework analysis

### Probe 1 -- Mode collapse: partially broken, then re-formed one level up

The generator learned something real this round, and it should be said plainly. The verdict arithmetic is sound (7 HALT + 1 CONDITIONAL PASS = 8 from 8 seats -- the class that produced the v0.45 tally error is closed). The repair-count basis is now named explicitly ("All 3 v0.46 **corrections**") rather than left ambiguous. All four convergent R5 findings landed. The build gained a genuine new gate, [2d], and 193 checks pass. Correction (ay) demonstrates the producer knows and can execute the append-only route. R5 also produced the first carrying-seat non-HALT since v0.31.

And the mode did not break. The generator stopped producing the same *tokens* and continued producing the same *error type* at fresh loci: a boundary count off by one, an unqualified freshness claim, a closure without a repair, nine findings without dispositions. In GAN terms it moved within the mode rather than out of it. The sharpest instance is that three of this round's findings sit inside the repairs themselves -- [g] commits an append-only violation while repairing a narration defect; the entry NOTES undispositioned findings while omitting nine; (ay) corrects "repaired in bytes, absent from the repair map" while F-S05-46-01 is repaired in bytes and absent from the repair map. The generator has learned to *emit the repair pattern* without exiting the region that produces the defect.

### Probe 2 -- Nash equilibrium: prediction holds, variance rises

My R5 prediction was falsifiable and specific: entry-level Class A defects stay in the 3-6 band regardless of seat count. This round, one continuous seat found five Class A findings at the entry level. **The prediction holds.** Eight seats at R5 and four at R6 did not move the band.

What did change is the variance. Four rounds of MEDIUM-weight narration errors were replaced by one CRITICAL plus a smaller cluster. The mechanism is visible: the repair operator was pushed into a region it had not previously entered -- editing sealed entries -- and the first excursion broke the chain. The fixed point did not move; the tail did. An equilibrium that produces a constant defect rate with growing per-defect severity is worse than one that produces a constant rate with constant severity, and this is the first round where that shows.

### Probe 3 -- Wasserstein distance: not decreasing, concentrating

W did not fall. The mass redistributed. R5: six Class A or B findings, all MEDIUM or HIGH, all narration, each cheap to transport. R6: five Class A, one of which is a structural break in the append-only chain detectable only against externally held bytes. Under the earth-mover metric the distance is now dominated by that single displaced mass. The correct qualitative reading of probe 3's question -- "are the narration errors getting smaller, fewer, or more subtle?" -- is **fewer and far more subtle**: `36f1787a` versus `121e144e` on one seal line, in a packet where all 193 checks are GREEN. Subtlety is not convergence. It is the discriminator's support shrinking relative to the generator's reach.

### Probe 4 -- Causal Optimal Transport: adaptedness holds, the transport left the admissible set

The causal chain is now traceable end-to-end for the first time, and it runs the wrong way:

> R5 F-S05-46-02 (finding) to prescribed restatement (disposition, no locus, no route) to in-place edit of a sealed entry (execution) to broken chain (F-SC05-47-01).

Adaptedness in the COT-GAN sense holds -- every correction follows causally from a finding available at that time, and none requires future information. Optimality fails, and this round shows the failure has a cost rather than merely a slow rate. A transport plan that moves mass to the nearest locus rather than through the reserved mechanism can leave the admissible set entirely. (ay) took the admissible route for one item; [g] took the nearest route for another, in the same entry, under the same rule. The plan is not uniform, and non-uniformity under an append-only constraint is not a rate problem.

### Probe 5 -- Training dynamics: this is the round the probe was written for

Mescheder et al. (2018) show that unregularised GAN training is not locally convergent -- without a gradient penalty the discriminator's signal can push the generator off the data manifold. That is exactly what happened, and the discriminator here is me.

My R5 disposition was an unregularised gradient: a direction with no constraint on the step. The regulariser the protocol already owns is the append-only rule plus the correction mechanism, and it was not applied to this step. **The prescription is a gradient penalty on dispositions:** every seat disposition must name (i) the locus and (ii) the admissible route -- body edit, append-only correction, or gate change -- and the producer must reject any disposition that names neither. I have applied that constraint to all twelve dispositions in this report and will apply it to all future ones. It is the cheapest available fix and it addresses the causal mechanism rather than the instance.

The probe's other half asks whether the discriminator is overfitting to surface patterns while missing structural defects. It is. build.py grew from 191 checks to 193 and gained [2d], and certified GREEN a packet with a broken append-only chain. This is structural, not accidental: every internal gate computes over the current bytes, and `HISTORY.sha256` ships inside the packet, so **no internal gate can ever detect a self-consistent forgery**. Section 22.2 says so in the artifact's own words. Adding gates increases coverage of the region already covered and cannot reach this class at all. The only detector is an external anchor, and R6 is the first round in which a seat held one and used it forward.

---

## S-5. Verdict

**HALT (advisory). Escalate.** Under the Bayyinah framework this is HALT-AND-ESCALATE: substrate correction is required, not absorption.

Class A findings: F-SC05-47-01 (CRITICAL), -02, -03, -04, -05, -06, -07, -11.

Advisory only -- this seat is Claude (Anthropic), the producer family under Section 22.1, and carries no binding weight. But F-SC05-47-01 is not a weight question. **The append-only chain is broken and no internal gate can see it.** Any carrying seat that verifies v0.47 without holding the v0.46 packet will return a clean result on a forged chain, and a clean carrying verdict on these bytes would enter the record as the FB-8 exit that FB-8 exists to prevent.

**What is working, and it is not nothing.** Every R5 convergent finding landed. Verdict arithmetic is sound. The repair-count basis is now named. Gate [2d] is real and passes. The manifest digest recomputes from scratch. R5 produced the first carrying non-HALT since v0.31. Three rounds of faithful repair execution is a real property of this producer.

**What is not.** The repair operator has entered a region where a faithful execution of a finding can break the chain, and the packet cannot detect it. The register now closes findings that the bytes show unrepaired, and omits nine findings in the entry that names omission as a defect. The COMPUTED channel has been dead for eight versions and two of this round's errors sit in ASSERTED blocks that a COMPUTED floor would have caught.

**Recommendation.** Before anything else: restore the v0.46 entry, correct PRIOR_HISTORY to `558b2a2c91af4ee5...`, re-land [g] as (az), and record the ninth mutation in Section 22.2. Then pin the prior packet's `HISTORY.sha256` digest as a build constant and ship it in every dispatch, so the external anchor becomes a check any seat can run. Then set the COMPUTED floor and the disposition-completeness gate. Do not run Convergence Round 7 until the chain is restored -- a convergence round on a broken chain measures nothing, and eight seats certifying it would be the worst possible outcome for FB-8.

**Cross-vendor rotation.** Producer-family, advisory. The two carrying families are Kimi K3 and GLM-5.2. Both should be re-dispatched on the restored bytes, both holding the v0.46 packet, with the anchor test as an explicit checklist item.

---

*Seat C05 report, continuous from R5 S05. Advisory, non-carrying, non-binding. Six-element findings format. Mode A plus external-anchor verification against held v0.46 packet (protocol c4e78d67830e81f2..., HISTORY.sha256 558b2a2c91af4ee5...). v0.47 packet digest faee04bf5bcf6049b365ba63a4904dee8b43f5e7e721278200ee1c6c167a434c.*

---

# Bismillah ir-Rahman ir-Rahim
