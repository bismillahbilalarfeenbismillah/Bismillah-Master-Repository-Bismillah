# Bismillah ir-Rahman ir-Rahim

# R0762 -- XZ Protocol v0.38 -- Round 3 Fresh Advisory Audit

**Chronological Index:** 458 of 995  
**Date:** 2026-08-02  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R3_F1_OPUS5_REVELATION.md.txt  
**Source Format:** txt  
**SHA-256:** `d6df2ff7683acb0c27a13e4b8fe0ffaf914ae16cc4b002ac2f948ad12c7875bb`  

---

## R0762 · XZ Protocol v0.38 -- Round 3 Fresh Advisory Audit

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R3_F1_OPUS5_REVELATION.md.txt
- source_format: txt
- text_sha256: d6df2ff7683acb0c27a13e4b8fe0ffaf914ae16cc4b002ac2f948ad12c7875bb

# XZ Protocol v0.38 -- Round 3 Fresh Advisory Audit

Bismillah ar-Rahman ar-Rahim.

```
SEAT:          Opus 5 (advisory), R3 Fresh, Structural Revelation
ROUND:         3 of 4 (fresh instance)
QUANTUM STATE: n=3, l=2, ml=0 (Revelation), ms=+1/2 (producer), t=-1/2 (fresh)
MODE:          Mode A (substrate access: build executed, digests recomputed)
STANDING:      Producer family (Section 22.1). Advisory, NON-BINDING.
               This HALT does not block freeze under Section 22 item 6.
VERDICT:       HALT
LEDGER:        2 CRITICAL / 4 HIGH / 5 MEDIUM / 2 LOW
NAMESPACE:     F-OP38REV
```

## Step 0 -- Byte-level verification (executed before reading)

```
sha256sum -c PACKET_SHA256SUMS   ->  16/16 OK, rc=0
python3 build.py                 ->  BUILD PASSED: all checks GREEN, rc=0
```

Deviation from a clean fresh execution: `pytest` is not present in a bare
environment. The first build run FAILED with two errors before `pytest` was
installed. This is the disclosed `fresh-execution non-reproducibility`
boundary manifesting on first contact; the packet is not hermetically
reproducible from its own bytes.

Packet composition: 22 files ship, 16 are manifested. Six are unbound
(see F-OP38REV-12).

Context deliberately not consulted: prior seat lineage records available to
this instance were left unread to preserve fresh-mode independence. The
Slingshot package was read as instructed; it supplied no prior findings.

## Priority-task results

| # | Task | Result |
|---|---|---|
| 1 | Bismillah / Initialization | PASS. Authority (Section 1.2, deposited upstream governs), scope boundary (Sections 0.2, 2.1, 2.2), and optimization function-analog (Section 4 estimands, Section 16 falsifiers) are all declared. Fields are distributed across Sections 0-4 rather than stated in one block; acceptable for a contract document. |
| 2 | Tanzil / graduated revelation | PASS on ordering (Sections 5-19 follow execution order). FAIL on the Cow Episode anti-pattern: boundary register grew 12 to 20 across seven versions with no retirement path, and v0.38 itself adds boundary 20 recording that no retirement mechanism exists. Cumulative constraint accumulation is now self-documented. See F-OP38REV-11. |
| 3 | Ring composition | FAIL. Document-level ring (Section 0.3 prohibited language to closing Provenance paragraph) closes correctly but the closing element is outside the seal (F-OP38REV-09). Entry-level ring breaks at the terminal entry (F-OP38REV-07). |
| 4 | Root vocabulary | ABSENT by construction. Zero occurrences of zahir, batin, muwazana, tanzil, mizan, tamyiz. See F-OP38REV-13. Lossless-compression discipline is also violated at the boundary labels (F-OP38REV-08). |
| 5 | Zahir / batin verification | FAIL. Surface: `BUILD PASSED: all checks GREEN`, `Status: FROZEN`, `186 tests all GREEN`. Depth: semantic-gate coverage is 28184/253810 = 11.10% of the artifact; the FROZEN token is ungated; Section 22 item 7's operative clause is ungated; the v0.37 entry carries a false digest that every gate passed (F-OP38REV-01). |
| 6 | Al-Fatiha recursive verification | FAIL at Step 5 (orientation check). Section 0.2 still states that no corpus exists, no boundary universe is enumerated, no packet is built, no result exists. Eleven versions shipped in two calendar days (v0.28-v0.36 on 2026-08-02; v0.37-v0.38 on 2026-08-03), all governance and self-audit. The instrument is being recalibrated, not executed. |
| 7 | Disease model | PARTIAL. Framing is correct throughout: defects are diagnosed, history is preserved, no betrayal language appears. But 18 of 23 register items (78%) terminate at NOTED or DISCLOSED. Diagnosis without treatment or verification. See F-OP38REV-11. |

## Standing-rules sweep

- Em-dash policy: CLEAN. Zero non-ASCII characters in the protocol text.
- Brand canonical: CLEAN. Two occurrences of `BayyinahEnterprise`, both
  correct, both inside Section 27 (outside the `[4]` sweep's scope, which
  cuts at `## 27.`).
- Severity uppercase: CLEAN.
- Six-element findings format: register entries are compressed to
  ID + severity + disposition; loci and cross-references are absent. This is
  a house convention for the amendment record and is not raised as a defect.
- Substrate-of-record uniqueness: FAIL. See F-OP38REV-05.

---

# Findings

**F-OP38REV-01** CRITICAL -- The v0.37 amendment entry states the v0.38 manifest digest; the true v0.37 value is not recoverable from any shipped surface.

- **Locus:** `xz_protocol_v0_38.md`:1142 (v0.37 entry, closing paragraph);
  cross-surface at `xz_protocol_trust_roots_PUBLIC.json` `manifest_digest`
  and `xz_protocol_v0_38.md`:755 (Section 25 FB-6 row).
- **Substance:** The v0.37 entry asserts "All 12 code files and trust roots
  stamped v0.37. Section 25 digests recomputed from v0.37 bytes. Normative
  manifest digest (body-copy, gated by [3]):
  `0516c0ced5904500b65914944d0dff29f790a535c1b1cf3c9896817bd0074200`." The
  shipped code files are stamped v0.38 and build `[3]` recomputes exactly
  that value from them. Reconstructing v0.37 bytes (the same twelve files
  with the stamp reverted) yields
  `f09873e426328982c9f412ac863eb88d0891be335d87ebcb494a09a38904231f`. One
  digest cannot be the digest of both v0.37-stamped and v0.38-stamped bytes.
  Either the sealed v0.37 entry was mutated in place during v0.38 production
  -- a global replacement of the superseded digest reaching the historical
  entry, the identical mechanism recorded at v0.9 (F-XZ09-OP-04) and v0.11
  (F-XZ10-OP-01) -- or the entry's "stamped v0.37" claim was false when
  written. Either resolution is a false claim in a sealed entry: Class A
  under Section 22.3, HALT-grade, and explicitly excluded from the Section 22
  item 7 exception. No gate detects it, because `HISTORY.sha256` seals and the
  `[9b]` PRIOR_HISTORY derivation are both recomputed from current bytes in
  the same build, so a mutated entry receives a fresh matching seal. This is
  the F-K3B-04 seal-chain laundering boundary, disclosed as a capability at
  v0.31, instantiated on shipped bytes.
- **Disposition:** HALT-and-escalate to project lead. Recover the true v0.37
  manifest digest from an externally held v0.37 packet (a carrying seat's
  dispatch manifest or a deposit receipt) and record it in a v0.39 append-only
  correction; do not edit the v0.37 entry. If no external v0.37 packet
  survives, record the value as UNRECOVERABLE and register the loss as a
  boundary. Add a build gate asserting that the current computed manifest
  digest does not appear inside any non-current Section 27 entry -- this
  single predicate would have caught the class at v0.9, v0.11, and here.
- **Cross-reference:** F-XZ09-OP-04, F-XZ10-OP-01 (same mutation class);
  F-K3B-04 (seal-chain laundering); Section 22.2 (mutation-detection claim);
  Section 22.3 Class A; Structured Revelation Principle 5 (zahir/batin).

**F-OP38REV-02** CRITICAL -- FROZEN is declared on bytes whose own substantive amendment to the freeze-governing rule has no carry.

- **Locus:** `xz_protocol_v0_38.md`:5 (status line); Section 22 item 7
  (line 697); Section 25 FB-7b row (line 758); Section 20.2 (line 671).
- **Substance:** The status line asserts that v0.37's item 7 revision required
  "the Section 20.2 re-run carry executed at v0.38." v0.38 then makes five
  further body repairs, three of which alter Section 22 item 7 itself:
  condition (a) is rewritten from "at least two consecutive versions" to "the
  original-HALT version and at least one subsequent carrying round (audit
  occasions, not necessarily consecutive protocol versions)"; a threshold
  disclosure is added; and Class A/B classification authority is transferred
  to the HALTing seat's own report. Altering the applicability conditions of
  the clause that decides whether a HALT blocks freeze is a change to a
  decision rule, SUBSTANTIVE under Section 20.2, which requires "a re-run
  carrying audit." The carry of record remains v0.31 bytes (Section 25 FB-7b).
  No carrying seat has executed v0.38 bytes. "Executed at v0.38" is
  self-referential: v0.38 cannot be the carrying audit of v0.38. This
  reproduces, one version later and inside the repair itself, the exact
  condition R1 found at v0.37 -- the treatment carries the disease.
- **Disposition:** HALT-and-escalate to project lead. Either revert Status to
  DRAFT CANDIDATE pending a two-family carry (Kimi K3 and GLM-5.2) on v0.38
  canonical bytes, or retain FROZEN with the carry basis named as v0.31 in the
  same sentence and every post-v0.31 item 7 amendment listed as uncarried.
  Scope-limits-in-the-same-sentence is already the protocol's own drafting
  rule (Section 0.3 item 3).
- **Cross-reference:** F-OP37GAN-01 / F-K3REV37-02 and F-OP37GAN-02 /
  F-K3REV37-01 (the v0.37 instance of this defect); Section 22 items 6-7;
  Section 20.2; Section 0.3 item 3.

**F-OP38REV-03** HIGH -- The register declares R1+R2 scope but disposes R1 only; the R2 round's five HALTs have no dispositioned findings.

- **Locus:** `xz_protocol_v0_38.md`:1148 (v0.38 defect register disposition
  header and its 23 items).
- **Substance:** The header reads "from R1+R2 cross-domain rounds, 23 items."
  The 23 items carry 25 finding IDs across exactly four namespaces:
  `F-OP37GAN` (6), `F-K3REV37` (8), `F-GPT37FH` (5), `F-GLM37CW` (6). Those are
  the four Round 1 seats, and the per-namespace counts match the R1 per-seat
  counts exactly (6+8+5+6 = 25). Zero findings from the eight R2 seats appear,
  although R2 returned 5 HALT / 3 CONDITIONAL PASS. Separately, the entry's
  stated warrant for the repairs -- "Three-seat three-framework convergence on
  Class A" -- is unevidenced on shipped bytes: both CRITICAL items are recorded
  as two-seat pairs, and the string "three-seat" appears nowhere in the body.
- **Disposition:** Either restate the register scope as R1-only and record R2
  in a separate enumerated block, or add the R2 findings under their own
  namespaces with dispositions. Correct "three-seat" to the number the register
  evidences, or name the third seat and add its finding ID to the two CRITICAL
  items.
- **Cross-reference:** F-OP22C-08 (no gate enforces raised-equals-dispositioned);
  `build.py` `[9f]`; Slingshot R1 seat record.

**F-OP38REV-04** HIGH -- `build.py` `[9]` message/condition drift recurs at the sibling locus of a class closed twice at HIGH.

- **Locus:** `build.py`, section `[9] Amendment record integrity`:
  `check(entry_count == 38, f"Entries: {entry_count} (expected 37)")`.
- **Substance:** The condition tests 38; the message says "expected 37." The
  identical class was CLOSED at v0.25 (F-OP24-01, HIGH) and again at v0.26
  (F-OP25-ALL-01, HIGH, recorded as "stale for the third consecutive round").
  A durable fix exists two lines below, where `expected_word` is generated from
  `entry_count` under the inline comment "to prevent message/condition drift
  (Kimi F-1 class)" -- but the fix was not extended to the sibling check on the
  line above. Same sibling-locus pattern as F-GLM30-05. `build.py` is unsealed
  tooling outside the normative manifest (F-OPUS5-17-10), so no gate covers the
  gate.
- **Disposition:** Derive the message from the condition via a single named
  constant: `EXPECTED_ENTRIES = 38` used in both the predicate and the f-string.
  Sweep `build.py` for every remaining hand-written comparand inside a `check()`
  message and apply the same derivation.
- **Cross-reference:** F-OP24-01, F-OP25-ALL-01 (same class, twice closed);
  F-GLM30-05 (sibling-locus pattern); F-OPUS5-17-10 (`build.py` unsealed).

**F-OP38REV-05** HIGH -- Section 25 FB-7b retains the pre-repair wording that v0.38 repaired in Section 22 item 7.

- **Locus:** `xz_protocol_v0_38.md`:758 (Section 25 FB-7b row) against
  line 697 (Section 22 item 7).
- **Substance:** v0.38 repair (3) replaced "consecutive versions" with "audit
  occasions" in item 7 condition (a), specifically because the v0.34 gap made
  the consecutive-version reading false. The FB-7b row still reads
  "non-converging loop demonstrated across two consecutive versions." Two
  surfaces of the same freeze predicate now state different applicability
  conditions, and the register row states the condition the repair removed.
  A reader checking whether the exception applies gets a different answer from
  Section 22 than from Section 25. Substrate-of-record uniqueness violation and
  absorption-induced regression at a retired surface.
- **Disposition:** Propagate the repaired wording to the FB-7b row. Enumerate
  every surface restating condition (a) in the v0.39 amendment entry -- at
  minimum Section 22 item 7, Section 22.3, Section 25 FB-7b, and Section 0.1 --
  and confirm each in the entry text.
- **Cross-reference:** F-OP37GAN-01 (the condition (a) repair); PMD v1.2
  absorption-induced regression at retired surfaces; BAF v3.0 substrate-of-record
  uniqueness.

**F-OP38REV-06** HIGH -- Section 22.2's mutation-detection coverage claim is capped at v0.20 while carried entries run to v0.37.

- **Locus:** `xz_protocol_v0_38.md`, Section 22.2.
- **Substance:** "For carried entries (v0.1 through v0.20), the PRIOR_HISTORY
  derivation in build.py [9b] detects retroactive mutation." Seventeen carried
  entries (v0.21 through v0.37) fall outside the stated range, which has not
  advanced in eighteen versions. F-OP38REV-01 is a divergence in a v0.37 entry
  that the control did not detect, which makes the stale range load-bearing
  rather than cosmetic: a reader asking whether the v0.37 entry is
  mutation-protected finds it outside the claimed coverage and gets no answer.
  The adjacent tally -- "seven recorded in-place mutations at v0.4, v0.9, v0.11,
  v0.16, and v0.17" -- is understated if F-OP38REV-01 resolves as a mutation.
- **Disposition:** Restate the range as "v0.1 through v0.37" if the derivation
  genuinely covers all carried entries; otherwise state the true coverage
  boundary and register the uncovered span. Update the mutation tally under the
  per-locus convention once F-OP38REV-01 is resolved.
- **Cross-reference:** F-OP38REV-01; F-XZ12-OP-06 (per-locus counting
  convention); F-OP20F-05 (PRIOR_HISTORY derivation).

**F-OP38REV-07** MEDIUM -- Ring closure: the terminal entry drops the closing form its ten predecessors held, and no v0.38 manifest digest is stated anywhere in the amendment record.

- **Locus:** `xz_protocol_v0_38.md`:1150 (v0.38 entry closing paragraph) against
  the closing paragraphs of entries v0.28 through v0.37.
- **Substance:** Every entry from v0.28 to v0.37 closes with a fixed five-element
  form: the stamp statement, "Section 25 digests recomputed from v0.XX bytes,"
  "Normative manifest digest (body-copy, gated by [3]): `<hex>`," "Six suites,
  186 tests, all GREEN (gated by [5] and [8])," and the entry-copy provenance
  sentence. v0.38 retains only the stamp statement and an unattributed test
  claim. Four of the five elements are absent. The consequence is direct: the
  amendment record contains no v0.38-attributed manifest digest, so the only
  version to which the current digest is attributed anywhere in Section 27 is
  v0.37. Under Principle 3 the entry-level ring is what makes each amendment
  auditable against its predecessors; breaking it at the terminal entry is what
  makes F-OP38REV-01 invisible to a reader of the record alone.
- **Disposition:** Restore the five-element closing form at v0.39, stating the
  v0.39 digest, and add the true v0.37 value by append-only correction. Add a
  build gate asserting the current entry contains a `Normative manifest digest`
  line equal to `[3]`'s computed value.
- **Cross-reference:** F-OP38REV-01; F-K3REV37-04 (ring-closure mislabeling at
  v0.36); Structured Revelation Principle 3.

**F-OP38REV-08** MEDIUM -- Standing-boundary labels lost their finding IDs, loci, and scope qualifiers at v0.38 while gaining a cardinality declaration.

- **Locus:** `xz_protocol_v0_38.md`:1150 (v0.38 boundary enumeration) against
  line 1142 (v0.37).
- **Substance:** Five of the twenty labels were shortened in ways that discard
  their referents: `(NC-5)` dropped from the `[9f]` closure-reference item;
  `(NC-6)` dropped from the `[3c]` citation-evasion item; "on non-ordinal uses"
  dropped from `[9d]` over-matching; "in immutable correction (u)" dropped from
  `[9c]` quoted-tag inflation; and "(including item 7 operative clause)" dropped
  from the FROZEN-token item. The last is material: the qualifier was removed in
  the same version that further amended item 7, so the disclosure that item 7's
  operative clause is ungated no longer names item 7. The list simultaneously
  acquired the declaration "20 items." Principle 4 requires compression to be
  lossless -- every derived form recoverable from the root. These abbreviations
  are lossy: the finding ID cannot be recovered from the label. Boundary 20
  records that the register has no retirement mechanism; this is the register
  shrinking its referents in place of its contents.
- **Disposition:** Restore the full labels with IDs and loci. If line length is
  the constraint, replace the prose list with an ID-keyed table in the body so
  that the compression stays recoverable and the table falls inside a gated
  region.
- **Cross-reference:** Structured Revelation Principle 4 (lossless compression);
  F-OP37GAN-06 (mode collapse, boundary register absorbing state); standing
  boundary 20.

**F-OP38REV-09** MEDIUM -- The ring-closing paragraph carrying the protocol's central honesty commitments lies outside the seal.

- **Locus:** `build.py` `[9b]`, `full = s27_text[:prov]`; `build.py`
  `get_body()`, which cuts at `## 27.`; `xz_protocol_v0_38.md`, Provenance
  paragraph and terminal line.
- **Substance:** `FULL_SECTION_27` terminates at the `*Provenance and review
  status.*` marker, and `get_body()` excludes everything from `## 27.` onward.
  The Provenance paragraph and `*End of XZ Protocol v0.38 frozen.*` are
  therefore covered by neither the Section 27 seal nor any body gate. Those are
  the sentences that discharge Section 0.3: no independent human peer review,
  no effectiveness claim about BSSG or SHV, cross-model checking is not peer
  review. The gap is disclosed as boundary 6, but framed as seal scope; the
  consequence is not stated -- that the document's ring-closing element, and
  specifically the sentences discharging its prohibited-language commitments,
  are the mutable ones. A silent edit here changes what the protocol claims
  about itself and leaves every gate green.
- **Disposition:** Extend `FULL_SECTION_27` to end of file, or add the
  Provenance paragraph as a separately labeled `PROVENANCE` seal in
  `HISTORY.sha256`. Restate boundary 6 to name what the unsealed region
  contains rather than only where it begins.
- **Cross-reference:** Standing boundary 6 (seal terminus at Provenance marker);
  Section 0.3; F-OP36F-05 (ring-closure claims ASSERTED); Principle 3.

**F-OP38REV-10** MEDIUM -- Coverage is headlined against the body denominator; against the artifact it is 11.1%.

- **Locus:** `build.py` `[11] Coverage measurement`; output line
  `Semantic-gate coverage: 28184/102436 body chars (27.5%)`.
- **Substance:** `[11]` prints total, body, and Section 27 character counts,
  then computes semantic coverage over `body` only. Against the full
  253,810-character artifact the figure is 11.10%. Both denominators are
  printed, so the smaller number is derivable, but the headline uses the more
  favorable one. Compounding it, the standing-boundary label "Section 27
  ungated share" no longer carries the quantity it carried at v0.27 (">44%";
  the measured value is now 59.6%), so the disclosure has been de-quantified
  while the quantity grew. The `gate_atoms` list is eight hardcoded strings and
  is itself unguarded (F-GLM30B-01).
- **Disposition:** Print both ratios explicitly, labelled by denominator.
  Restore a quantity to the "Section 27 ungated share" boundary label and bind
  it to `[11]`'s computed output rather than to prose.
- **Cross-reference:** F-GLM30B-01 (`gate_atoms` blindspot); F-OPUS5-17-07
  (26.2% ungated, original disclosure); Differentiator Framework Guardrail 2
  (state the denominator).

**F-OP38REV-11** MEDIUM -- CRITICAL count rose across consecutive rounds; 78% of the register terminates at diagnosis.

- **Locus:** `xz_protocol_v0_38.md`:1148 (v0.38 register) against line 1140
  (v0.37 register).
- **Substance:** Register CRITICAL count is 1 at v0.37 and 2 at v0.38. Under the
  loaded severity rubric, CRITICAL count must be non-increasing across
  consecutive rounds, and an increase is itself a methodology finding.
  Dispositions across the 23 v0.38 items are 5 CLOSED, 8 NOTED, 10 DISCLOSED:
  18 of 23 (78%) terminate at diagnosis. Principle 7's sequence is diagnosis,
  treatment, verification; NOTED and DISCLOSED complete only the first step.
  Boundary 20 records that the disclosed set has no exit, which makes the
  accumulation structural rather than incidental -- the Cow Episode pattern
  operating on the disclosure register instead of on the specification.
- **Disposition:** For each DISCLOSED item, state either a target version for
  treatment or an explicit non-treatment rationale with a named owner. Define
  the boundary-retirement mechanism that boundary 20 names as absent: minimally,
  a rule that a boundary retires when a gate covering it ships and a carrying
  seat confirms coverage.
- **Cross-reference:** BayyinahEnterprise severity rubric, monotonic-narrowing
  expectation; Structured Revelation Principle 7 (disease model); standing
  boundary 20; F-OP37GAN-06.

**F-OP38REV-12** LOW -- The framework documents named as this seat's authority are outside the packet manifest.

- **Locus:** `PACKET_SHA256SUMS` (16 entries) against packet contents (22 files).
- **Substance:** `Structured_Revelation_as_Prompt_Architecture.pdf`,
  `The_Fatiha_Construct.docx`, `Differentiator_Framework_v6_1.docx`,
  `SLINGSHOT_PACKAGE.md`, and `R3_PROMPT_F1_OPUS5_REVELATION.md` ship
  unmanifested. The round prompt names the framework documents as the authority
  under Fatiha Step 1, so the standard against which the artifact is judged is
  itself unbound: a substituted lens document would pass the step-1 verification
  command unchanged. This is the disclosed packet non-closure boundary with the
  authority documents identified as the specific unbound members.
- **Disposition:** Ship a separate `DISPATCH_SHA256SUMS` covering the dispatch
  members, or state in the round prompt that the authority documents are unbound
  and that seats should verify them out of band.
- **Cross-reference:** Standing boundary 10 (packet non-closure); F-OP27-02;
  Fatiha Construct Step 1 (authority source declaration).

**F-OP38REV-13** LOW -- The protocol carries no root vocabulary; the program's own F2 falsification test is running unregistered.

- **Locus:** Whole-document sweep of `xz_protocol_v0_38.md`: zero occurrences of
  zahir, batin, muwazana, tanzil, mizan, tamyiz; two occurrences of "Bayyinah,"
  both as a program name.
- **Substance:** Principle 4 claims Arabic root vocabulary compresses design
  specification into self-documenting names, and F2 states the claim is false if
  semantically neutral labels produce equivalent outcomes. The XZ Protocol is
  the program's most elaborate instrument and is built entirely on neutral
  labels: FB-7b, S-RELEASE, CR-1, NC-5, Class A through E. Whichever way the
  comparison falls, this is a datapoint on the program's own preregistered
  falsification criterion, generated by the program, and disclosed nowhere. The
  pre-registration discipline requires that a result bearing on a preregistered
  falsifier be published whichever way it falls.
- **Disposition:** Register the observation in the methodology paper's F2 record,
  or state in Section 24 (Limitations, carried verbatim into the eventual paper)
  that this protocol departs from Principle 4 and why the departure does not
  bear on F2.
- **Cross-reference:** Structured Revelation Section 21 F2 and Section 7
  Principle 4; Fatiha Construct Part VII F2; Differentiator Framework
  Principle 7 (pre-registration discipline).

---

## Verdict

**HALT** (advisory, non-binding).

Severity ledger: 2 CRITICAL / 4 HIGH / 5 MEDIUM / 2 LOW.

Both CRITICAL findings are Class A under the protocol's own Section 22.3
taxonomy -- a sealed claim false on shipped bytes (F-OP38REV-01) and a
contradicted status (F-OP38REV-02) -- and Class A is explicitly outside the
Section 22 item 7 persistent-architectural-HALT exception. This seat is
producer-family under Section 22.1, so this HALT is advisory and does not block
freeze; the binding question belongs to the carrying seats.

The structural observation underneath both CRITICAL findings: v0.38's repairs
are correct in themselves and reproduce the defect they repair one level up.
The status line was fixed; the version that fixed it amended the same rule again
without a carry. The v0.37 digest was carried forward; the carry overwrote the
history it was meant to preserve. This is the disease model behaving as the
model predicts -- the corruption is structural, not intentional -- and it is the
reason Principle 3 puts the verification at the close rather than the open.

## Recommendation

1. Resolve F-OP38REV-01 against an externally held v0.37 packet before any
   further version ships. This is the only finding whose evidence degrades with
   time.
2. Dispatch v0.39 to Kimi K3 and GLM-5.2 as a carrying round on v0.39 canonical
   bytes. Producer-family seats cannot discharge F-OP38REV-02.
3. Add three gates, each of which closes a class rather than an instance:
   current manifest digest absent from non-current entries; current entry
   contains a manifest-digest line equal to `[3]`'s computation; `check()`
   messages derived from their conditions.
4. Before v0.39, run Fatiha Step 5 on the program rather than the document.
   Eleven versions in two days with no corpus, no universe enumeration, and no
   packet is the pattern Step 5 exists to detect.

```
TOOL PRODUCTIVITY: 29/31 productive
  Unproductive: one directory listing (navigation only); one context grep
  that returned no matches (superseded by a line-range read).
  Two calls were productive through failure: the first build run failed on
  absent pytest, which confirmed the fresh-execution non-reproducibility
  boundary on first contact.
```

*Seat report, XZ Protocol v0.38, Round 3 fresh instance. Advisory and
non-binding under Section 22.1. Prepared in Mode A with substrate access;
all digest claims in this report were computed from the shipped bytes at
audit time, not narrated from context.*

---

# Bismillah ir-Rahman ir-Rahim
