# Bismillah ir-Rahman ir-Rahim

# R0760 -- XZ Protocol v0.38 -- Round 3 Continuous-B -- Opus 5 (advisory), Fractal/Hurst

**Chronological Index:** 908 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R3_CB1_OPUS5_FRACTAL.md.txt  
**Source Format:** txt  
**SHA-256:** `adbf05287c7d8d2594ebe01372bedf28c9cda89e95b8f21dcab359e1812e34bb`  

---

## R0760 · XZ Protocol v0.38 -- Round 3 Continuous-B -- Opus 5 (advisory), Fractal/Hurst

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R3_CB1_OPUS5_FRACTAL.md.txt
- source_format: txt
- text_sha256: adbf05287c7d8d2594ebe01372bedf28c9cda89e95b8f21dcab359e1812e34bb

# XZ Protocol v0.38 -- Round 3 Continuous-B -- Opus 5 (advisory), Fractal/Hurst

```
SEAT:          Opus 5 (advisory), R3 Continuous-B, Fractal/Hurst
ROUND:         3 of 4 (promoted from R2 fresh)
QUANTUM STATE: n=3, l=2, ml=-1 (Fractal), ms=+1/2 (producer), t=+1/2 (promoted continuous)
MODE:          Mode A (substrate verifier); v0.37 packet retained from R2 and used as
               the external comparison anchor
VERDICT:       HALT (advisory)
```

**Dispatch defect, noted once and not counted as a finding.** The report-format block
specifies `ROUND: 2 of 4 (promoted from R2 fresh)` while the document header, filename and
task set all say Round 3. I have written 3 of 4. Correct the template.

**Verification.** `sha256sum -c PACKET_SHA256SUMS` rc=0 across all 16 entries.
`python3 build.py` returned `BUILD PASSED: all checks GREEN`, including the HISTORY seal
chain and 186 tests GREEN. Section 27 parses to exactly 38 entries, v0.1 through v0.38, no
gaps, no duplicates. The v0.38 entry's claim of "R2 verdicts: 5 HALT / 3 CONDITIONAL PASS"
is confirmed against the eight shipped reports (HALT: C1 Opus GAN, C2 GPT Fractal, C3 Kimi
Revelation, F1 Opus Fractal, F2 GPT Revelation; CONDITIONAL PASS: C4 GLM Cobweb, F3 Kimi
Cobweb, F4 GLM GAN).

**Carry-forward integrity, verified not assumed.** My R2 report ships in this packet as
`R2_F1_OPUS5_FRACTAL.md`. Its SHA-256 is
`0f6dfe750f0176847099f4cdf5ccb5f8822706e6e176b2fab803a9a0a58793de`, byte-identical to what
I emitted. `diff` is empty. Seat reports do ship unmodified, as Section 0.1 claims. The
*practice* is clean; F-F1OP37FH-02 is about the absent *mechanism*, and that distinction
should be preserved when this finding is dispositioned.

---

## R2 FINDINGS STATUS

| ID | R2 severity | v0.38 status | basis |
|---|---|---|---|
| F-F1OP37FH-01 | HIGH | **PERSISTS -- untouched** | code plane byte-identical except version stamps; probe re-run identical |
| F-F1OP37FH-02 | HIGH | **PERSISTS -- worsened** | manifest still 16 entries; framework set now absent entirely; 8 seat reports are new unhashed inputs |
| F-F1OP37FH-03 | HIGH | **CLEARED by design** | no slingshot this round; all 8 reports shipped in full |
| F-F1OP37FH-04 | MEDIUM | **PERSISTS + partially self-falsified** | see below |
| F-F1OP37FH-05 | MEDIUM | **CLEARED** | all four R3 tasks are defined; no undefined tools |
| F-F1OP37FH-06 | MEDIUM | **PARTIALLY CLEARED** | R3 correctly states I audited v0.37; no attestation field added |
| F-F1OP37FH-07 | LOW | **N/A** | framework documents not shipped this round |

**F-01 detail.** Every `.py` file reports as changed, but `diff` shows the only change in
`xz_protocol_kernel.py` is `# Version: XZ Protocol v0.37` -> `v0.38`, and the same for every
test suite. Zero test functions added; collection still returns 186. The 12-mutant probe
re-run on v0.38 bytes returns numerically identical results: mutation score 0.7500, the same
three survivors (`M5` isinstance-revert, `M6` getattr-revert, `M9` drop-reason-codes),
Vd/Vt 0.7407. The joint M5+M6 exploit still yields ALLOW on a FALSE-bearing vector. This
finding is exactly as it was; nothing in "carried repairs" reached the code plane.

**F-03 cleared, and the clearing is the right shape.** R2's slingshot withheld prior
findings in principle and disclosed the strongest one in practice. R3 discloses everything
to everyone. Full disclosure to a seat that knows it is continuous is honest; partial
disclosure to a seat told it is fresh is not. The fix was to change which seat gets which,
and that is what happened. Recorded as cleared.

**F-04 detail -- my own R2 disposition is partially falsified.** I prescribed replacing the
severity ordinal with "per-entry finding counts (continuous, no imputation)". I tested that
prescription this round against the `[ASSERTED]` density series, which is the closest
available continuous per-entry measure. It carries **the same defect I criticised**: the
`[ASSERTED]` notation is not adopted until v0.20, so the series opens with a 19-entry zero
prefix -- longer than the 14-entry prefix that invalidated the severity series.

```
[ASSERTED] per entry, v0.1..v0.38:
[0 x19, 6, 9, 12, 13, 8, 11, 6, 10, 10, 9, 9, 19, 18, 19, 12, 12, 12, 10, 4]

full series N=38          H = 0.8509   MC p = 0.0220   bootstrap CI [0.6847, 1.0326]
post-onset  N=19          H = 0.8468   MC p = 0.0950   bootstrap CI [0.5683, 1.0988]
shuffled null mean 0.6256 (small-sample R/S bias; do not compare to 0.5)
```

Significance again does not survive removal of the zero prefix (p 0.022 -> 0.095), and at
N=19 the bootstrap CI spans 0.53 -- more than the whole 0.5-to-1.0 range. The correct
conclusion is stronger than F-04 stated: **no per-entry series in this artifact supports R/S
Hurst estimation**, because every measurement convention in the record was adopted
mid-trajectory, so every series has a notation-onset step. Hurst should be withdrawn from
the Fractal seat's task list entirely, not re-specified. I got that wrong in R2 and I am
correcting it here rather than defending the prescription.

---

## R3 FINDINGS

### F-F1OP38FH-R3-01 [CRITICAL] [Tier 1] -- undisclosed in-place mutation of the v0.37 historical entry; two gates are in structural conflict and the append-only axiom is the one that loses

- **Locus:** `xz_protocol_v0_38.md` Section 27, v0.37 entry, the line
  `Normative manifest digest (body-copy, gated by [3]): ...`; `HISTORY.sha256` line
  `ENTRY_v0.37`; v0.13 entry item (4) (gate [3] specification); Section 0.1 line 16
  ("never a silent edit").
- **Substance:** with the v0.37 packet retained as an external anchor, the v0.37 amendment
  entry is byte-comparable across versions. Trailer stripped, both are 5138 bytes and
  differ in exactly one substitution:

  ```
  v0.37 shipped : ... (body-copy, gated by [3]): f09873e426328982c9f412ac863eb88d0891be335d87ebcb494a09a38904231f
  v0.38 shipped : ... (body-copy, gated by [3]): 0516c0ced5904500b65914944d0dff29f790a535c1b1cf3c9896817bd0074200
  ```

  `0516c0ce...` is the **v0.38** manifest digest (Section 25, FB-6 row). The true historical
  value `f09873e4...` occurs **zero times** anywhere in v0.38. A historical entry has been
  overwritten with a present-tense value and the prior value erased from the record. This is
  the fifth in-place mutation of a historical entry (v0.4 first; v0.9 second, by global
  replace; v0.11 third and fourth, per the v0.13 F-XZ12-OP-06 correction), and it is the
  same mechanism as the second. No amendment entry discloses it.

  Three structural facts make this more than producer error:

  1. **`HISTORY.sha256` did not fire, and cannot.** `ENTRY_v0.37`'s seal was regenerated
     alongside the text (`2324b5e2...` -> `06202049...`), and `PRIOR_HISTORY` was
     regenerated to match (`d073d096...` -> `3d7ad5a5...`). I confirmed the gate is not
     merely inert: restoring the true historical digest in a copy of the v0.38 packet makes
     `build.py` fail four checks (`HISTORY seal ENTRY_v0.37 matches bytes`,
     `FULL_SECTION_27 seal matches`, `PRIOR_HISTORY matches derivation`, and the packet
     digest). The gate detects mutation by anyone who cannot re-seal. It is blind to the
     only actor who can -- and all five recorded violations are that actor's. A tamper-
     evidence mechanism that exempts the sole historical tamperer provides no evidence.
  2. **Gate [3] appears to compel the violation.** The v0.13 entry specifies that the
     manifest gate "scans the protocol body for every 64-hex token and requires each to
     resolve to a shipped artifact or the manifest digest." The body carries 89 distinct
     64-hex tokens. Once the code files are re-stamped to v0.38, the historical
     `f09873e4...` no longer resolves to any shipped artifact, so a correct append-only
     record fails gate [3] and a gate-[3]-passing record violates append-only. The two
     obligations are jointly unsatisfiable for any historical digest. Marked Tier 2 on the
     mechanism only: the gate files do not ship (`ls xz_protocol_*gate*.py` returns 0 in
     this packet; gates are "tooling, not carried" per the v0.14 partition), so I can
     verify the conflict's premises and its outcome but not the gate's code. That the
     compelling mechanism is unshippable and uncarried is itself the point.
  3. **Only continuity detected it.** No fresh seat can find this. It requires the prior
     packet's bytes, which no manifest in this program pins and no dispatch supplies.
- **Disposition:** HALT and escalate to project lead. Do not absorb this as a routine
  correction. The decision required is which of the two gates yields. Recommended route:
  exempt Section 27 from gate [3]'s resolve-to-shipped-artifact requirement, since Section
  27 is by construction a record of superseded states, and have gate [3] instead require
  that any 64-hex token inside Section 27 resolve to an artifact shipped *at the version of
  the entry containing it*. Then restore `f09873e4...` to the v0.37 entry by append-only
  correction recorded in the v0.39 entry, never by editing v0.37. Separately, `HISTORY.sha256`
  must gain an anchor the producer cannot regenerate: publish each version's
  `HISTORY.sha256` digest to the external deposit record at version time, and have the
  build verify the derived `PRIOR_HISTORY` against the externally published value rather
  than against a reconstruction from the current document.
- **Cross-reference:** F-XZ09-OP-04 (same mechanism, second occurrence); v0.13 item (7)
  (HISTORY.sha256 introduced "so that any future in-place mutation fails the build rather
  than waiting for an auditor" -- falsified here); v0.12 closure-gate defect (a gate that
  returned PASS precisely when the fix was absent -- same anti-correlation class);
  GPT-5.6 Seat F2 section 2 ("HISTORY.sha256 semantics and external-anchor strength"),
  which reached the same surface independently in R2 without the prior-packet anchor;
  standing boundary 2 (cb67f222 termination literal in PRIOR_HISTORY recursion).

### F-F1OP38FH-R3-02 [HIGH] [Tier 1] -- v0.38 repairs a Section 20.2 violation by committing the same Section 20.2 violation one version later

- **Locus:** `xz_protocol_v0_38.md` Section 22 item 7 condition (a); Section 20.2; Section
  0.1 status line; Section 25 FB-7b row; v0.38 amendment entry.
- **Substance:** the Class A defect on which three seats converged was that v0.37 made a
  substantive governance change (adding the item 7 exception) and claimed FROZEN with no
  carrying audit on the amended rule. v0.38 repairs the status line -- verified, the false
  "no substantive revision" clause is gone and replaced with an accurate one -- and then
  amends condition (a) again, from

  > "(a) the HALTing seat has audited at least two consecutive versions after the original HALT"

  to

  > "(a) the HALTing seat has audited the original-HALT version and at least one subsequent
  > carrying round (audit occasions, not necessarily consecutive protocol versions)"

  Section 20.2 defines a change to "a metric, threshold, or decision rule or its Boolean
  structure" as SUBSTANTIVE, "requiring ... a re-run carrying audit". This is a decision-rule
  change: it alters which HALTs qualify for the exception, and it converts a two-occasion
  requirement measured in protocol versions into one measured in audit occasions, which is
  precisely the redefinition that makes the already-claimed instances qualify. Grepping the
  shipped bytes: the most recent canonical-bytes carry claimed anywhere in v0.38 is on
  **v0.31**, seven times; there is no claim of a carrying audit on v0.37 or v0.38 bytes.
  The repair therefore satisfies limbs 1 and 2 of the convergent Class A finding (status
  line, substantive-change acknowledgement) and reproduces limb 3 (no carrying seat has
  audited the amended rule) at the next version.

  In the Fractal lens this is the finding, not an analogy: the same defect shape recurs at
  the next scale, generated by the disposition of the prior instance. That is the structure
  Section 22 item 7 already names for HALTs -- "re-HALT bases generated by the disposition
  of the prior HALT in a non-converging loop" -- now observed one level up, in the
  amendments themselves rather than in the seat verdicts. The exception was written to
  absorb non-convergence at the seat layer; the non-convergence has moved to the layer that
  writes the exception.

  I credit the honest part explicitly: v0.38 adds a threshold disclosure stating that "two"
  and "six" are chair-fitted parameters derived from the observed trajectory and not from a
  principled basis. That disclosure is correct and is the right instinct. It covers the
  *values*, not the *unit of measure*, and the change of unit from versions to occasions is
  the load-bearing part.
- **Disposition:** issue v0.39 whose status line names the condition (a) amendment as
  substantive under Section 20.2, then run the carry on v0.39 bytes with two executing
  non-producer families before any FROZEN claim. Until that carry exists, the FROZEN token
  on v0.38 is unsupported by the instrument's own rule. Alternatively, and preferably:
  freeze the *rule* by moving item 7 into Section 20.3's non-amendable floor, so that the
  carry-blocking condition cannot be amended by the party whose freeze it blocks.
- **Cross-reference:** F-GPT37FH-R2-01 and -02 (both CRITICAL; v0.38 adopts -02's prescribed
  wording near-verbatim, so absorption is mechanically traceable and the producer deserves
  credit for it); F-K3REV37-01/02; F-OP37GAN-02; Section 20.2; Differentiator Layer 3
  (self-similarity across scales) and Layer 8 (divergent oscillation).

### F-F1OP38FH-R3-03 [HIGH] [Tier 1] -- the Class A repair did not propagate to the register that gates FROZEN, where the false claim survives verbatim

- **Locus:** `xz_protocol_v0_38.md:756` (Section 25, FB-7b row) and `:1132`; against Section
  22 item 7 condition (a) as amended at v0.38.
- **Substance:** the phrase "two consecutive versions" occurs twice in v0.38. Section 22
  item 7 no longer requires consecutiveness. Section 25's FB-7b row still asserts, as the
  stated basis for resolving the freeze blocker, that the non-converging loop was
  "demonstrated across two consecutive versions". The original HALTs are on v0.33 and the
  re-HALTs on v0.35; v0.34 intervenes; the two versions are not consecutive. So the exact
  false statement identified by GPT-5.6's F-GPT37FH-R2-02 [CRITICAL] is repaired in Section
  22 and left standing in Section 25 -- and Section 25 is the register that Section 25's own
  preamble says must be fully filled before "a version of this protocol may be issued as
  FROZEN". The two sections of the same frozen document now contradict each other on the
  eligibility test, and the surface that gates the freeze carries the retired, false version.
- **Disposition:** amend the FB-7b row to the v0.38 condition (a) language: replace
  "non-converging loop demonstrated across two consecutive versions" with "re-HALT on new
  bases at a subsequent carrying round after documented disposition (audit occasions, not
  necessarily consecutive protocol versions)". Then sweep every surface for the retired
  phrase before issuing: the R2 record shows this producer's absorptions repeatedly repair
  the headline locus and miss a secondary one (v0.7 -> v0.8 digest narration; v0.9 -> v0.10
  body propagation; v0.12 -> v0.13 gate rebuild). A repair-propagation checklist keyed to
  the changed phrase, not to the changed section, would have caught this one.
- **Cross-reference:** F-GPT37FH-R2-02 (the CRITICAL this incompletely repairs); PMD v1.2
  absorption-induced regression at retired surfaces; my F-F1OP37FH-01 disposition
  ("update the test count at all loci"), same class.

### F-F1OP38FH-R3-04 [MEDIUM] [Tier 1] -- assertion density nearly tripled in one version with zero verified counterparts, and the trend is not being read as a metric

- **Locus:** `xz_protocol_v0_38.md` Section 27 (all 209 occurrences of `[ASSERTED]` are
  inside Section 27); `xz_protocol_v0_37.md` (76 occurrences).
- **Substance:** `[ASSERTED]` rose from 76 to 209 across a single version, a 175% increase,
  while `[VERIFIED]` occurs 0 times in either. Per-entry the series peaks at 19 in the
  v0.31-v0.33 freeze arc and reads 4 at v0.38. The token exists to mark claims the producer
  asserts without external verification, which is exactly the right discipline; the defect
  is that nothing consumes it. No gate counts it, no freeze-blocker references it, and the
  ratio of asserted to verified claims is not reported anywhere in Section 25 despite being
  the single cheapest available measure of how much of the freeze rests on producer
  testimony. GLM-5.2 Seat F4 reached the same surface from the GAN framework
  (F-GLM52-R2F-03, "ASSERTED fraction saturated, not converging"); this is convergent, and
  I am not claiming it as novel.
- **Disposition:** add an asserted-to-verified ratio row to Section 25, computed by the
  build rather than narrated, and define what converts an `[ASSERTED]` claim to `[VERIFIED]`
  (an external receipt, a carrying-seat confirmation, or a gate assertion). Do not add a
  threshold: CR-7 correctly forbids inventing a numeric gate without a principled basis. The
  value of the metric here is its trajectory, which is reportable without a threshold.
- **Cross-reference:** F-GLM52-R2F-03 (convergent, GAN framework, fresh GLM seat);
  F-XZ09-OP-04 (DISCLOSED, NOT CLOSED for want of an external recomputation receipt -- the
  same missing-receipt class); CR-7.

### F-F1OP38FH-R3-05 [MEDIUM] [Tier 1] -- a carrying seat HALTs on findings it classifies Class A, which item 7's exception excludes by its own terms; the freeze is blocked by the instrument's own rule

- **Locus:** `R2_C3_KIMI_REVELATION.md` (verdict HALT MAINTAINED; F-K3REV37-01/02 recorded
  as Class A, first-time at v0.37); `xz_protocol_v0_38.md` Section 22 item 7 exception,
  final sentence.
- **Substance:** v0.38 strengthens the exception by specifying that Class A/B classification
  is "as classified by the HALTing seat's own published report (not the producer)" -- a real
  improvement that removes producer discretion, and I credit it. Applied to the shipped
  record it is dispositive against the freeze: Kimi K3 is a carrying family; its continuous
  R2 seat returned HALT MAINTAINED; its own published report classifies the governing
  findings as Class A and first-time at v0.37. The exception "does not apply ... to HALTs on
  Class A or Class B findings as classified by the HALTing seat's own published report."
  Therefore the exception does not cover this HALT, and item 7's base rule -- "a HALT from
  either carrying seat blocks freeze outright and requires a new version" -- applies
  unmodified. v0.38 carries the FROZEN token anyway. Recorded as MEDIUM rather than higher
  because it is not novel to this seat: Opus 5 Seat C1 stated it as F-OP37GAN-R2-01
  [CRITICAL] and Kimi stated it directly. I report it because a continuous Fractal seat that
  read the eight reports and did not restate it would be silently dropping the binding
  constraint from its own verdict basis.
- **Disposition:** either disposition F-K3REV37-01/02 to Kimi's satisfaction and obtain a
  non-HALT from that seat on v0.39 bytes, or drop the FROZEN token to DRAFT CANDIDATE until
  that happens. The v0.38 amendment strengthening Class A/B attribution makes the second
  route the honest one in the interim.
- **Cross-reference:** F-OP37GAN-R2-01; F-K3REV37-01/02; F-F1OP38FH-R3-02 (same freeze
  claim, different defect); Section 22 item 7.

**Severity ledger:** 1 CRITICAL / 2 HIGH / 2 MEDIUM / 0 LOW, plus 2 HIGH and 1 MEDIUM
persisting unrepaired from R2 (F-F1OP37FH-01, -02, -04).

---

## CROSS-POLLINATION

Reading the other seven R2 reports, four things were found that my fresh Fractal pass
missed. I list them by what the miss was, not by what the finding was.

**1. The governance-clause arithmetic (F-GPT37FH-R2-02, F-K3REV37-01/02, F-OP37GAN-02).**
My paired seat -- same Fractal/Hurst framework, different family -- found the condition (a)
predicate failure by, in its own words, "Tier-1 literal predicate evaluation. No biological
or GAN analogy is needed." It counted: versions strictly after the original HALT = {v0.35},
cardinality 1 against a threshold of 2. That is arithmetic on twelve tokens of prose. I had
the same framework, the same bytes and more compute budget, and I did not do it, because I
spent the Fractal budget on series and on the code plane. **The same framework in a
different family found it; the framework was not the constraint. I was.**

**2. The boundary register is not a reliable enumeration (F-OP37GAN-R2-03, "[9e] is the
proof").** I consumed the 19-item standing-boundary list as data and cross-referenced my
findings against it. I never audited it. If the register silently drops items, then every
cross-reference in my R2 report -- including my claim that F-K3-03 "is not in the
19-boundary register", which was the extension claim in F-F1OP37FH-01 -- rests on an
unaudited enumeration. My finding survives (F-K3-03's absence is still true of the shipped
list) but its framing was over-confident.

**3. Severity monotonicity was violated and I computed the series without checking the rule
(F-GLM52-R2F-05).** I extracted the severity trajectory, ran R/S on it, ran Elliott on it,
and rejected both. GLM applied the methodology's own monotonic-narrowing expectation --
CRITICAL count must be non-increasing across consecutive rounds, and an increase is itself a
methodology finding -- and found the v0.37 CRITICAL spike breaks it. I had the series in
memory and did not apply the one rule that was already written down for it.

**4. `HISTORY.sha256` external-anchor strength (GPT-5.6 Seat F2, section 2).** A fresh seat
in a different family identified the anchor question in R2 without the prior packet. I
needed continuity to convert it into F-F1OP38FH-R3-01. Its R2 pass and my R3 pass are the
same surface at two depths.

**Convergence I can claim.** F-F1OP37FH-02 (manifest coverage) converges with GPT-5.6 Seat
F2 section 1, independently, cross-family, both fresh. F-F1OP38FH-R3-04 converges with
GLM-5.2 F4's assertion-saturation finding, cross-framework. Neither was coordinated.

### Tidal-lock profile

My R2 fresh pass was locked to **measurable substrates**. Every one of my seven R2 findings
attached to something I could execute, hash, count, or mutate: kernel bytes, manifest
coverage, string counts across documents, an estimator's N. Not one attached to a normative
clause read as a proposition. The Fractal/Hurst instrument primes for sequences and
structures; I let it also decide *which surfaces exist*, and prose rules fell outside. The
lock is not the framework -- GPT-5.6 held the identical framework and read the clause -- it
is the framework plus my own preference for substrates that answer back.

The concrete signature: in R2 I ran a 12-mutant probe against 4515 bytes of kernel and did
not evaluate a 700-character governance sentence containing a quantified predicate over a
finite, fully enumerated set. The predicate was more decidable than the mutation probe and
cost less.

Second lock, visible only now: **I treated the packet's own registers as ground truth.** The
slingshot's 19 boundaries, the Section 27 severity trajectory, the 186-count. I verified the
last of those three and consumed the first two. A fresh seat has no basis for that trust and
should extend none.

---

## DEPTH-VS-INDEPENDENCE

**Depth helped, decisively, and the mechanism is specific.** F-F1OP38FH-R3-01 is not
reachable without the v0.37 packet on disk. It is a byte-comparison between two versions of
a sealed historical entry, and the seal validates internally in both. No fresh seat, however
capable, can perform it, because the packet supplies no external anchor and the manifest
does not pin the predecessor. This is the clearest demonstration in the round of what
continuity buys: not better reasoning, but a second observation of the same object at a
different time. Every other R3 finding could in principle have come from a fresh seat with
enough budget. That one could not.

**Anchoring detected, in three places, all mine.**

1. *Probe reuse.* I re-ran the identical 12-mutant set from R2 rather than designing mutants
   for v0.38's changed surface. It happened to be correct here -- the surface did not change
   -- but I did not know that when I chose the probe, and I would have run the stale probe
   either way. A continuous seat's first instinct is to re-measure, and re-measuring with the
   prior instrument is how a continuous seat stops seeing new things.
2. *Defending my own prescription.* My R2 disposition for F-04 named a substitute series. My
   first framing this round was to check whether v0.38 adopted it. The useful question was
   whether the prescription was any good, and it was not: the substitute carries a longer
   zero prefix than the series it was meant to replace. Had I not tested my own remedy I
   would have carried a wrong disposition forward with a version number attached to it,
   which is the exact absorption-induced-regression pattern I flagged in F-F1OP38FH-R3-03
   against the producer.
3. *Framework re-application without re-selection.* I applied Fractal self-similarity to the
   defect recursion in R3-02, which is legitimate and productive. I did not ask whether the
   Fractal instrument was the right one for a round whose central question is governance
   arithmetic. The honest answer, given cross-pollination item 1, is that it was not the
   binding tool this round; literal predicate evaluation was, and I reached it via the
   Fractal framing rather than because the framing pointed there.

**Net.** Depth produced one finding independence could not, and cost me the fresh seat's
willingness to distrust the registers. On this artifact, at this stage, that trade is worth
making once and not twice: a third continuous round from this seat would re-measure more and
re-select less. If Round 4 is dispatched to me, dispatch it fresh, or dispatch it with an
instrument I have not used.

---

## Computed values

```
mutation score (v0.38 bytes)     0.7500  (9/12; identical to v0.37)
survivors                        M5 isinstance-revert, M6 getattr-revert, M9 reason-codes
Vd/Vt adversarial suite          0.7407  (identical to v0.37; kernel-plane upper bound)
test functions collected         186     (unchanged; 0 added)
code-plane delta v0.37->v0.38    version-stamp comment only, all 13 files

Hurst, [ASSERTED] density N=38   H = 0.8509  p = 0.0220  bootstrap CI [0.6847, 1.0326]
Hurst, post-onset       N=19     H = 0.8468  p = 0.0950  bootstrap CI [0.5683, 1.0988]
                                 -> NOT INTERPRETABLE; notation-onset artifact, as with
                                    the severity series. Withdraw the Hurst task.

Section 27 entries               38 (v0.1..v0.38), no gaps, no duplicates
historical entries mutated       1 (v0.37; one line; undisclosed)
[ASSERTED] v0.37 -> v0.38        76 -> 209  (+175%)
[VERIFIED] v0.37 -> v0.38          0 ->   0
64-hex tokens in body            89
most recent canonical-bytes carry claimed anywhere in v0.38   v0.31
```

## Selection-bias check

```
Tools applied                    6  (byte-diff vs retained v0.37 packet; mutation probe;
                                     R/S Hurst with MC null and bootstrap; append-only
                                     seal-chain comparison; gate-behaviour experiment;
                                     cross-seat convergence read)
Tools productive                 5  (the R/S Hurst was non-productive and is reported as
                                     a null with the reason)                base rate 0.83
Hypotheses tested and REJECTED   2  (that v0.38 repaired F-01 -- it did not touch it;
                                     that my R2 substitute series was sound -- it was not)
Findings novel to this seat      3  (R3-01, R3-02, R3-03)
Findings convergent, credited    2  (R3-04 with GLM F4; R3-05 with Opus C1 and Kimi C3)
```

The base rate is higher than R2's 0.50 and that is not a sign of a better round. A
continuous seat measures what it already knows how to measure, so its hit rate rises while
its coverage narrows. Read the 0.83 alongside the tidal-lock profile, not instead of it.

## Cross-vendor recommendation

F-F1OP38FH-R3-01 requires a non-producer family holding both the v0.37 and v0.38 packets to
reproduce the byte comparison; Kimi K3 or GLM-5.2 with both packets supplied is the correct
dispatch, and the comparison takes one `diff`. Do not dispatch it to a seat given only
v0.38, which cannot see it by construction. F-F1OP38FH-R3-02 and -03 are literal predicate
and string checks any seat can verify. R3-05 is already carried by Kimi's own report and
needs disposition, not another audit.

---

# Bismillah ir-Rahman ir-Rahim
