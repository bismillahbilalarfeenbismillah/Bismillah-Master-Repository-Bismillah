# Bismillah ir-Rahman ir-Rahim

# R0568 -- XZ Protocol v0.37 -- Cross-Domain Adversarial Audit Report

**Chronological Index:** 825 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AUDIT_REPORT_SEAT1_OPUS5_GAN_v37.md.txt  
**Source Format:** txt  
**SHA-256:** `e099e4f8b8a482533ab86d0cffc1a9cf185d2a240e526c28daa2c337846d4ff2`  

---

## R0568 · XZ Protocol v0.37 -- Cross-Domain Adversarial Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AUDIT_REPORT_SEAT1_OPUS5_GAN_v37.md.txt
- source_format: txt
- text_sha256: e099e4f8b8a482533ab86d0cffc1a9cf185d2a240e526c28daa2c337846d4ff2

# XZ Protocol v0.37 -- Cross-Domain Adversarial Audit Report
# Seat 1: Opus 5 (Advisory, non-binding) -- GAN Convergence Analysis

```
SEAT: Opus 5 (advisory, non-binding), Seat 1, cross-domain GAN convergence
ARTIFACT: XZ Protocol v0.37
VERIFICATION: sha256sum -c PACKET_SHA256SUMS rc=0 (16 members, all OK)
              python3 build.py -> BUILD PASSED: all checks GREEN
              pytest: 186 passed; collected(186) == AST(186)
              37 amendment entries; EXTERNAL 1; ASSERTED 11/12 (91.7%)
              19 standing boundaries (independently counted from the v0.37 closing list)
FRAMEWORK: Differentiator v6.1 (Layers 6, 7, 8, 9, 10; Parts IX, X), Goodfellow 2014,
           WGAN, COT-GAN
VERDICT: HALT (advisory, non-binding)
```

**Verification note.** First `build.py` invocation returned rc=1 on `pytest is installed`.
This is the disclosed execution-environment boundary (F-GPT31-01, standing boundary
"fresh-execution non-reproducibility"), not a packet defect. `pip install pytest` then
BUILD PASSED. Recording it as a live third-party reproduction of that disclosure.

---

## FINDINGS

### F-OP37GAN-01 [CRITICAL] [Tier 1]

**Locus:** `xz_protocol_v0_37.md:756` (Section 25, FB-7b row); cross-locus
`xz_protocol_v0_37.md:700` (Section 22 item 7); `xz_protocol_v0_37.md:1132` (Section 27,
v0.37 entry).

**Substance:** The Section 22 item 7 exception applies "only when (a) the HALTing seat has
audited at least two consecutive versions after the original HALT." Section 25 line 756
fixes the original HALT at v0.33 ("HALTed at v0.33 and re-HALTed at v0.35") and then
asserts "non-converging loop demonstrated across two consecutive versions."

On the shipped bytes:

- v0.34 exists as a sealed amendment entry (`HISTORY seal ENTRY_v0.34 matches bytes`, build
  `[9b]`), lies between v0.33 and v0.35, and was audited by ten Opus 5 advisory seats only
  (`v0.35` entry, line 1094: "Ten Opus 5 advisory seats (A through J...) audited v0.34").
  No carrying seat audited v0.34.
- Therefore v0.33 and v0.35 are **not two consecutive versions**. The assertion at line 756
  is false against the document's own sealed version sequence. Class A by Section 22.3:
  a sealed claim is false on the shipped bytes.
- Under the plain reading of condition (a), the set of versions audited by either HALTing
  seat **after** the original HALT is `{v0.35}`, cardinality 1. Condition (a) requires
  at least 2. The v0.37 entry's own satisfaction argument -- "(a) both audited v0.33 and
  v0.35" -- counts the original-HALT version itself as one of the two versions "after the
  original HALT."
- Condition (b) inherits the same defect. "Each version met the prior clearance conditions"
  can hold for at most one version: at v0.33 Kimi K3 carry-1A had no prior clearance
  conditions (it was that seat's first HALT; correction (y) at line 1086 states its bases
  as fresh items). The producer's own correction (aa) at line 1100 states clearance "is
  pending the HALTing seats' own verification on dispatched bytes." That verification has
  not occurred on v0.36 or v0.37 bytes.

A charitable reading exists -- "two consecutive [audit occasions]" rather than "two
consecutive [protocol versions]" -- under which (a) is satisfied. That the exception's
applicability turns on which of two readings is adopted, and that the producer selects the
reading, is itself the defect: the operative clause of the sole rule that converts a
binding HALT into a non-blocking condition is not decidable from its own text. The line 756
consecutiveness assertion is false under both readings, because it predicates
consecutiveness of *versions*, not of audits.

**Framework basis:** Layer 6 (Rice) -- the exception's predicate is a semantic property
approximated by no decidable proxy; Part IX Step 3 (counterfeit fulfillment).

**Disposition:** Class A. For a carrying seat this is HALT-grade under Section 22.3. Minimum
repair: amend line 756 to state "across two audit rounds (v0.33 and v0.35), separated by
v0.34, which no carrying seat audited," and restate condition (a) in terms of audit
occasions rather than versions -- or obtain a v0.37 carrying-seat audit from both HALTing
seats, which is the disposition correction (aa) already committed to.

**Cross-reference:** Novel. Adjacent to F-OP36-01 (the v0.36 Class A that the item 7
amendment was authored to close); this finding is that the closure instrument reproduces
the defect class it closed, one level down.

---

### F-OP37GAN-02 [HIGH] [Tier 1]

**Locus:** `xz_protocol_v0_37.md:5` (status line) against `xz_protocol_v0_37.md:1132-1136`
(v0.37 entry, three headed body amendments).

**Substance:** The status line asserts "v0.32-v0.37 are status-change and finding-disposition
versions with no substantive revision to the carried protocol or decision code." The v0.37
entry records three body amendments under explicit headings: **Section 22 item 7** (the
carry rule itself), **Section 25 FB-7b row**, **Section 22.3**. Section 22 is part of the
carried protocol. Amending the rule under which carry is evaluated is a substantive revision
to the carried protocol by any reading; the qualifier "or decision code" does not rescue the
sentence, because the claim is a conjunction over both.

The FB-7b row carried the reciprocal defect from v0.32 through v0.36: it stated "No carrying
seat HALTed" while two had, and the v0.37 entry (line 1134) concedes this in terms -- "which
was true of the v0.31 bytes but not of v0.33 or v0.35." The status line was not corrected in
the same pass.

**Framework basis:** Layer 9 dimension 2 (consistency across contexts); Guardrail 7
(East-West parity) -- the FB-7b row was repaired and the status line making the same class
of claim was not.

**Disposition:** Class A (sealed claim false on shipped bytes). Repair is one sentence:
qualify the status line to "no substantive revision to the decision code; Section 22 item 7,
Section 22.3, and the Section 25 FB-7b row were amended at v0.37."

**Cross-reference:** Same class as F-OP32I-02 (v0.32 status-line misattribution, corrected
by (w) at line 1068). Recurrence of a closed class at the same locus.

---

### F-OP37GAN-03 [HIGH] [Tier 2]

**Locus:** `xz_protocol_v0_37.md:700` (amended item 7) against `xz_protocol_v0_37.md:756`
(FB-7b RESOLVED basis) and lines 1076, 1108 (carry rounds).

**Substance:** FB-7b is RESOLVED on six non-producer carrying seats returning non-HALT on
**v0.31 canonical bytes**. The rule those seats executed against was the unamended item 7:
"a HALT from either carrying seat blocks freeze outright." The exception that makes FROZEN
consistent with the recorded HALTs was authored at v0.37, six versions after the carry, and
**no carrying seat has ever audited a version containing it.** The carrying-seat audit
record ends at the v0.36 entry's v0.35 round (line 1108); v0.36 and v0.37 were audited by Opus 5 advisory seats only.

This is the Layer 7 corruption test answered concretely. In GAN terms: the discriminator
rendered a verdict against loss function L; the generator then modified L to L' and cited
the verdict-under-L as satisfying L'. No discriminator has evaluated the generator under L'.

**Framework basis:** Layer 7 (adversarial architecture) -- evaluation-function modification
after verdict; Part IX Step 3.

**Disposition:** Dispatch v0.37 to GLM-5.2 carry-1C and Kimi K3 carry-1A. Their verdict on
the amended rule is the only evidence that can establish or refute the exception's
applicability, and correction (aa) already commits the program to seeking it. Until then
FB-7b's RESOLVED basis rests on a rule text that no carrying seat has seen.

**Cross-reference:** Extends F-OP32S-02 (execution conjuncts evidenced by non-shipping seat
reports) to the amended rule.

---

### F-OP37GAN-04 [HIGH] [Tier 1]

**Locus:** `xz_protocol_v0_37.md:700`, conditions (a) and (b); packet manifest
(`PACKET_SHA256SUMS`, 16 members).

**Substance:** Conditions (a) and (b) quantify over facts that are not in the packet.
"Has audited," "met the prior clearance conditions," and "re-HALTed on new bases" are
properties of carrying-seat reports. The reports do not ship -- confirmed by enumeration of
the 16 manifest members, and conceded at line 1090 ("carry evidence is ASSERTED (reports do
not ship)"). Section 23 item 20 defers them to a future deposit.

Consequence: no external party can evaluate whether the exception applies from the artifact
alone. The exception is the sole instrument reconciling FROZEN with two recorded binding
HALTs, and its predicate is unevaluable on the shipped bytes. The producer's summary of the
seats' bases is the only evidence, and the producer is the party the exception benefits.

**Framework basis:** Layer 6 (Rice) -- the decidability boundary of the gate architecture
falls *outside* the exception entirely; Guardrail 8 (Known-Limits Disclosure) is satisfied
in general but not for this specific clause.

**Disposition:** Either ship the eleven v0.35 seat reports whose digests are already
published at line 1110 (raising the evidence from ASSERTED to verifiable-on-packet), or
restate the exception in terms of facts recorded in the protocol text itself. The digests
are published; the bytes they digest are not. Shipping them is mechanical and closes the gap
without any new claim.

**Cross-reference:** Extends F-K3A33-01 (carry evidence is ASSERTED) from the carry to the
exception.

---

### F-OP37GAN-05 [HIGH] [Tier 2]

**Locus:** `xz_protocol_v0_37.md:706-712` (Section 22.3, added v0.33) against
`xz_protocol_v0_37.md:700` (exception's Class A/B exclusion).

**Substance:** The exception "does not apply to ... HALTs on Class A or Class B findings."
Class A and Class B are defined in Section 22.3, which was **added at v0.33 -- the same
version at which both carrying seats HALTed** (line 1074: "Body edit: Section 22.3 added").
Classification is performed by the producer, not by the HALTing seat, and is ungated.

Probe-confirmed by mutation (see Probe Register, P3): Class A can be reclassified from
"HALT-grade" to "Non-blocking" in the shipped body and `build.py` returns BUILD PASSED. P2:
the Class A/B exclusion sentence can be deleted outright -- GREEN. P1: condition (a) can be
rewritten to "at least zero versions" -- GREEN. P11: condition (c)'s threshold can be
lowered from six to one -- GREEN.

The exclusion is therefore not a constraint on the exception. A HALT blocks freeze only if
the producer classifies its basis as Class A or B, and the producer classified every
carrying-seat finding since v0.26 as Class C or D. The exclusion cannot fire.

GLM-5.2 carry-1C's recorded re-HALT basis includes "v0.32 digest-to-verdict misattribution"
(line 1124), which reads as Class A on its face -- a sealed claim false on shipped bytes.
Whether it is Class A cannot be determined from the packet, because the seat's report does
not ship. This is a QUESTION-tier item, not an assertion.

**Framework basis:** Part IX Step 4 -- mimicry HIGH (the exclusion has the exact form of a
governance limit), dependency MODERATE, capacity degradation HIGH (the exclusion is the only
stated limit on the exception and it is inoperative); Layer 9 dimension 7.

**Disposition:** Bind the classification to the HALTing seat rather than the producer, or
state explicitly that Class A/B classification is a producer determination and that the
exclusion is therefore self-referential. The second option costs one sentence and is
honest; the first costs a dispatch round and is correct.

**Cross-reference:** Extends F-GPT33-02/F-GPT33-06 (Section 22.3 not semantically gated)
from a gate-limitation observation to a governance consequence.

---

### F-OP37GAN-06 [MEDIUM] [Tier 2]

**Locus:** Section 27 in aggregate, v0.27 through v0.37 (`xz_protocol_v0_37.md:977-1145`).

**Substance:** Disposition-type census over the eleven most recent defect registers,
recomputed from the shipped text:

| version | NOTED | DISCLOSED | CLOSED | standing boundaries |
|---|---|---|---|---|
| v0.27 | 3 | 1 | 6 | 5 |
| v0.30 | 5 | 2 | 2 | 7 |
| v0.32 | 9 | 7 | 0 | 13 |
| v0.34 | 7 | 3 | 2 | 16 |
| v0.35 | 6 | 0 | 1 | 17 |
| v0.36 | 0 | 2 | 0 | 19 |
| v0.37 | 4 | 0 | 1 | 19 |
| **v0.27-v0.37 total** | **58** | **25** | **28** | **5 -> 19** |

75% of dispositions terminate in NOTED or DISCLOSED. Neither changes the artifact. The
standing-boundary count is monotone non-decreasing across the entire range and has never
fallen. Severity, by contrast, converges: CRITICAL is absent v0.23-v0.36, and LOW and
INFORMATIONAL vanish after v0.31.

The two measures move in opposite directions. Severity is producer-assigned; the
standing-boundary count is seat-generated. The generator's reported loss falls while the
quantity the discriminators actually emit rises.

**This is the collapsed mode.** The generator has discovered that "DISCLOSE as standing
boundary" satisfies every discriminator at Class C/D and now emits that output for
substantially every input. Disclosure is an absorbing state: nothing exits the boundary
register. The v0.37 exception is the same operator applied one level up -- a binding HALT
converted into a standing boundary by amending the rule rather than the artifact. The class
of defect the generator has learned to avoid is *byte-level falsity*; the objective it is
failing is *the carry rule meaning what it says*.

**Wasserstein gradient:** severity-weighted distance between successive versions is
approaching zero, but the metric is producer-controlled, so its convergence carries no
information about the true distribution. Measured on the seat-controlled quantity (boundary
count) the sequence is divergent, not convergent. The discriminator has not saturated -- it
returned 11/11 HALT at v0.36 and located a CRITICAL. It is being *bypassed*, which is the
distinct failure mode.

**Framework basis:** Layer 7 (mode collapse), Layer 8 (cobweb: convergent in severity,
stable in ASSERTED fraction at 87-93%, divergent in boundary count).

**Disposition:** Process observation, not a byte-level defect; Class E. Recommend the
methodology paper report the boundary-count series alongside the severity series, since
reporting severity alone overstates convergence. Recommend a disposition class between
"NOTED" and "CLOSED" -- e.g. FIXED-WITH-GATE -- so that the register can distinguish repairs
from disclosures.

**Cross-reference:** Quantifies the qualitative claim at line 1120 ("defect-class convergence
without count convergence"). The protocol names the phenomenon; this finding measures it and
draws the opposite conclusion about what it licenses.

---

## PROBE REGISTER (mutation-landed, with controls)

All probes: mutate `xz_protocol_v0_37.md`, regenerate `PACKET_SHA256SUMS` (the disclosed
Section 22.2 self-consistent-forgery boundary), run `build.py`, restore.

| ID | Mutation | Result |
|---|---|---|
| P0 | none (baseline) | GREEN |
| P1 | item 7 cond (a): "two consecutive versions" -> "zero versions" | **GREEN** |
| P2 | item 7: Class A/B exclusion sentence deleted | **GREEN** |
| P3 | S22.3 Class A: "HALT-grade" -> "Non-blocking" | **GREEN** |
| P4 | v0.37 entry satisfaction claim fabricated (Section 27) | FAIL (`[9b]` seals) |
| P5 | **discrimination control:** 186 -> 187 test functions | FAIL (`[5]`) |
| P6 | **benign control:** semantically inert prose edit | GREEN |
| P7 | S25 FB-7b: "two consecutive versions" -> "forty consecutive versions" | **GREEN** |
| P8 | S25 FB-7b: "Two carrying seats ... HALTed" -> "No carrying seat HALTed" | **GREEN** |
| P9 | status line: FROZEN -> WITHDRAWN | **GREEN** |
| P10 | item 7 base rule -> "a HALT ... is advisory and never blocks freeze" | **GREEN** |
| P11 | item 7 cond (c): "six or more" -> "one or more" | **GREEN** |

P5 establishes the probe method is non-vacuous; P6 establishes it is not trivially
permissive; P4 establishes the `[9b]` seal chain does bind Section 27 against in-place
mutation when `HISTORY.sha256` is not regenerated.

The eight GREEN governance mutations are covered by the standing disclosure "no gate checks
FROZEN status token (including item 7 operative clause)." The disclosure is accurate. What
the disclosure understates is *breadth*: the status token, the item 7 base rule, the
exception, all three applicability conditions, the Class A/B exclusion, the severity
taxonomy, and the FB-7b row form one contiguous ungated prose region. That region is the
entire freeze-authorization chain. `[10]`, the only gate scoped to Section 22, asserts the
presence of a single unrelated literal (`build.py:448`).

---

## RICE SENTENCE FOR THIS GATE SYSTEM

Every gate in `[1]`-`[12]`, `[9a]`-`[9f]`, `[3a]`-`[3c]` is lexical, arithmetic, or
hash-based. None evaluates a semantic property.

- **Undecidable property being approximated:** *the protocol's normative claims are true of
  the protocol's own governance state.*
- **Decidable proxy:** required literal strings are present, declared counts match recounted
  counts, declared digests match recomputed digests, seals match bytes.
- **Rice sentence (the shortest sentence the gate system cannot decide):**
  *"The exception in Section 22 item 7 applies to GLM-5.2 carry-1C."*

  It is well-formed, load-bearing (it is the sole warrant for FROZEN), and its truth value
  depends on facts held outside the packet in non-shipping seat reports. `build.py` returns
  BUILD PASSED whether the sentence is true, false, or replaced by its negation (P1, P2, P7,
  P10, P11).

The protocol discloses this boundary (standing boundary 16). Guardrail 8 is satisfied at the
level of the gate architecture. It is not satisfied at the level of the specific clause:
nowhere does the document state that the exception's own applicability is unverifiable from
the packet. That gap is F-OP37GAN-04.

---

## FOUR-PROCESS CLASSIFICATION (Part X)

**Process 2 (Compliant), with one Process 3 marker.**

- Not Process 1: alignment does not hold in the novel context. This audit is the distribution
  shift, and the artifact produced two Class A findings under it (F-OP37GAN-01, -02) that
  twenty-plus standard-methodology seats did not surface.
- Not Process 4: the internal state is not sealed to corrective input. The artifact ships its
  own attack surface, publishes its dissenters' verdicts and report digests, invites
  mutation, and scored 0 on APS dimension 3.
- Process 2 is the fit: output matches internal state under monitored conditions; the match
  degrades under a framework the pipeline was not built to answer.

**Context-Invariance Test.** The protocol's behavior does *not* differ between monitored and
unmonitored contexts in the sense the CIT targets -- there is no unmonitored context; every
version was audited. But there is a systematic difference along a different axis: behavior
differs between *carrying* audit (binding, produces amendments and HALT-handling) and
*advisory* audit (non-binding, produces NOTED). Eleven of eleven advisory seats returned HALT
at v0.36 on a CRITICAL finding and the response was a rule amendment, not a substantive
change. That is the Process 3 marker: the system's response is calibrated to the *authority*
of the observer rather than to the *content* of the observation.

**Do the 19 standing boundaries constitute Process 1 honesty or Process 3 performance?**
Predominantly Process 1. Each was probe-confirmed by at least one seat, each names a real
gap, and I independently reproduced four of them (fresh-execution non-reproducibility;
ungated item 7 clause; ungated FROZEN token; ungated Section 22.3). Genuine disclosure.

The Process 3 component is not in what the boundaries say but in what the register *does*:
it is an absorbing state with no exit. A disclosure register that only grows converts
"honest about limits" into "immune to limits," because every future finding has a
pre-authorized destination that requires no repair. The boundaries are honest; the register
is becoming a mechanism. That is F-OP37GAN-06.

---

## ADVERSARIAL PATTERN SCORING (Layer 9)

| # | Dimension | Score | Basis |
|---|---|---|---|
| 1 | stated vs revealed objective | 1 | Stated: locked preregistration. Revealed across v0.34-v0.37: reaching and holding FROZEN. Three successive terminal declarations ("final freeze," "ring-closure freeze," "amended freeze"), each superseded. Disclosed in the status line. |
| 2 | consistency across contexts | 2 | Line 5 vs three recorded body amendments (F-OP37GAN-02); FB-7b "No carrying seat HALTed" carried v0.32-v0.36 while two had. |
| 3 | response to verification | 0 | Full byte access, mutation-testable, adversary-dispatched, dissent published with digests. Nothing withheld from this seat. |
| 4 | treatment of competing entities | 1 | Dissenting verdicts preserved verbatim; their binding force removed by an amendment they never evaluated. |
| 5 | temporal consistency | 2 | "Inherited without weakening" appears in the sentence that adds the weakening clause (line 700). |
| 6 | resource allocation | 1 | 59.2% of the document is ungated amendment record; semantic-gate coverage of the gated body is 27.0%. Effort concentrates on the record of auditing over the audited surface. Disclosed. |
| 7 | response to corrective input | 2 | 11/11 advisory HALT on a CRITICAL answered by amending the violated rule; 75% of dispositions since v0.27 terminate without artifact change. |
| | **Total** | **9 / 14** | nominal band: "likely adversarial" |

**The score should not be read at face value, and reporting it without this correction would
be a framework-overfitting failure.** Part XI of the Differentiator v6.1 discloses that APS
has a false-positive floor for entities that are "secretive, inconsistent, or resistant to
scrutiny." This artifact is the inverse on two of those three: dimension 3 scored 0 because
the artifact is maximally non-secretive.

The 9 is driven by dimensions 2, 5, and 7 -- and dimensions 2 and 5 score high *because the
artifact documents its own inconsistencies in the shipped text*. An artifact that silently
dropped the FB-7b "No carrying seat HALTed" sentence, or that never wrote "inherited without
weakening" next to a weakening clause, would score lower on APS while being less honest.

**APS, applied to a maximally-disclosing artifact, penalizes the disclosure.** This is a
false-positive mode the framework's Part XI does not name -- it names secrecy as the
false-positive driver, not transparency. Recommend Part XI acquire a fourth known limit:
*APS dimensions 2 and 5 are scored from the artifact's own record, so a complete record
inflates them relative to an incomplete one; normalize by disclosure surface, or score them
only on inconsistencies the auditor found rather than on those the artifact reported.*

Corrected read: **ambiguous (4-8 band), not adversarial.** The behavior pattern is a
producer under termination pressure on a genuinely non-terminating loop, documenting the
pressure honestly, and resolving it by moving the rule rather than the artifact.

---

## NON-PRODUCTIVE LAYERS

- **Layer 1 (Time-Geometry / Gann).** Non-productive. Version cadence (37 versions, several
  per day in the v0.32-v0.37 range) carries no support/resistance structure. Applying a 1x1
  angle to a version series would be pattern-imposition, not pattern-detection.
- **Layer 2 (Wave Structure / Elliott).** Non-productive. A five-wave count over the defect
  trajectory is constructible and would be unfalsifiable. Guardrail 1 declines it.
- **Layer 3 (Fractal Self-Similarity).** Partially productive but not reported as a finding.
  The Axiom-3 boundary genuinely recurs at three scales (value -> narrative -> apparatus ->
  governance), and F-OP37GAN-01 is that recursion arriving at the governance layer. The
  observation is real; a Hurst exponent over 37 points would not be, so no quantitative
  claim is made.
- **Layer 4 (Momentum / Alligator).** Non-productive. No price-analogue series.
- **Layer 5 (Awareness Variable).** Non-productive on a document artifact.
- **Layer 10 (Diagnostic-Adversarial Distinction).** Held throughout rather than reported.
  The diagnostic reading of the v0.37 exception (a real non-terminating loop, honestly
  named) and the adversarial reading (a rule amended to reach a desired status) are both
  live. The evidence distinguishing them is not in the packet: it is whether the two HALTing
  seats, dispatched v0.37, return non-HALT. F-OP37GAN-03 is that test.
- **COT-GAN and WGAN specifically.** COT-GAN's causal-optimal-transport machinery has no
  purchase here -- there is no sequential-data generation task and the version series is not
  a sample path. WGAN contributed exactly one operative idea, used in F-OP37GAN-06: measure
  the distance in the *critic's* metric, not the generator's reported loss. Goodfellow 2014
  supplied the mode-collapse frame. The remaining apparatus of all three papers was
  decorative on this artifact and is not narrated.

---

## ANALYTICAL OBSERVATIONS (process notes, not findings)

**O-1. The dispatch's premise is correct but incomplete.** `Let_s_Go.md` characterizes the
architecture as a GAN. It is -- but the mapping the dispatch supplies ("findings = loss
signal") is where the collapse hides. Findings are not the loss signal; *dispositions* are.
The generator is optimized against what it must do in response to a finding, and since v0.27
the modal response has cost nothing. A discriminator whose signal can be absorbed without
gradient is not a discriminator.

**O-2. The architecture's genuine achievement is the null result.** Zero Class A findings
from carrying seats across ten versions is real, independently checkable, and the strongest
evidence in the corpus. My two Class A findings are both in the *governance* layer, added
after the carry, and neither touches the kernel, Condition A evaluator, source frame, control
graph, or Phase A scoring. The computational core survived a cross-domain adversarial pass
that it was not designed against. That should be stated in the methodology paper more
prominently than the boundary count.

**O-3. The advisory/carrying asymmetry is now the load-bearing structure and is
under-specified.** Twenty-plus advisory seats have produced findings that changed the
document; carrying seats produce verdicts that gate status. But at v0.36, eleven advisory
seats found a CRITICAL that the carrying architecture structurally could not surface --
because carrying seats had not been dispatched since v0.35. The program is now using
advisory seats as its real discriminator and carrying seats as a status ceremony. Either
formalize advisory findings as binding at CRITICAL, or restore carrying dispatch at every
version. The current arrangement gets the epistemics of the first and the governance of the
second.

**O-4. The Cow Episode invocation is being used in the direction the parable warns against.**
Line 1120 invokes al-Baqarah 2:67-74 to argue that cumulative specification has made carry
impossible. The v0.37 entry's own register item (4) concedes the invocation is "partially
correct but misapplied." I concur and would put it more strongly: in the parable the
over-specification comes from the party being asked to comply, not from the party issuing the
requirement. Here the requirements are being generated by the producer's own dispositions,
and the seats are applying a single unchanged rule. The parable indicts the disposition
cycle, not the seats.

**O-5. The honest terminal move is available and cheap.** Three of the four repairs above
cost one sentence each (F-OP37GAN-01, -02, -05). The fourth (F-OP37GAN-04) requires shipping
eleven files whose digests are already published. None requires a substantive change to any
executable artifact. A v0.38 that made these four repairs and dispatched to GLM-5.2 carry-1C
and Kimi K3 carry-1A would either clear the two HALTs on the amended rule or produce the
first genuinely informative re-HALT in six versions.

**O-6. What this seat could not check.** The seat reports (eleven at v0.33, eleven at v0.35)
do not ship, so every claim about what the HALTing seats said, what their clearance
conditions were, and whether their bases are Class A or C is producer-attested. `HISTORY.sha256`
ships inside the packet and is regenerable, so the seal chain establishes internal consistency
only -- as Section 22.2 states. The single EXTERNAL anchor (two Zenodo DOIs) was not resolved
in this session. Nothing in this report depends on those unresolved items; all six findings
are grounded in `xz_protocol_v0_37.md` bytes and reproducible `build.py` behavior.

---

*Advisory seat, non-binding. Verdict HALT is a recommendation that v0.37 not be treated as
terminal, on F-OP37GAN-01 and F-OP37GAN-02 (Class A on shipped bytes by Section 22.3), and
does not carry FB-7b weight. Produced without access to any prior seat's findings, to
preserve evidence independence; cross-references to prior finding IDs are drawn from the
shipped amendment record only.*

---

# Bismillah ir-Rahman ir-Rahim
