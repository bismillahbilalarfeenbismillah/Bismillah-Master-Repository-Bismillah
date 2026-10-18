# Bismillah ir-Rahman ir-Rahim

# R0670 -- Model Council Seat Report -- BSSG v0.1 Convergence Review

**Chronological Index:** 861 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** model-council-claude_opus_5_0.md  
**Source Format:** md  
**SHA-256:** `f7309d873d4e7b841ff4b46c03da546926a3ed79ce1e9431ca8c5901136eb648`  

---

## R0670 · Model Council Seat Report -- BSSG v0.1 Convergence Review

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: model-council-claude_opus_5_0.md
- source_format: md
- text_sha256: f7309d873d4e7b841ff4b46c03da546926a3ed79ce1e9431ca8c5901136eb648

# Model Council Seat Report -- BSSG v0.1 Convergence Review

**Model:** Claude Opus 5 (`claude_opus_5_0`)
**Vendor family:** Anthropic
**Seat status: ADVISORY ONLY -- NON-CARRYING, NON-APPROVING.**

Anthropic is the **producer** vendor family for BSSG v0.1 (the specification's own AI-producer
disclosure records the first draft as "assembled by an AI producer agent (Claude, Anthropic)
operating inside Perplexity Computer", `BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md` line 7). Under
`methodology/bayyinah_cross-vendor-rotation.md` § *Producer-instance exclusion*, where the artifact
under audit was produced by Claude, Claude is either excluded from the auditor pool or "relegated to
advisory-only role (cannot HALT or assign CRITICAL / HIGH severities; can flag for human review)".
SHVVP v0.8 states the same rule for its own instrument: "Producer-lineage and editor-lineage review
of this document is ADVISORY and NON-CARRYING by construction; the producer of the artifact cannot
certify it" (`methodology/SHVVP_v0_8_flagship.pdf`, front matter, *Provenance and review status*),
and SHV Method v1.1 D6 states the governing principle without exception: "No party certifies its own
work" (`methodology/SHV_Method_v1_1.pdf`, D6).

Accordingly:

- Nothing in this report is a vote. My verdict below carries **zero weight** toward convergence.
- I assign **no CRITICAL and no HIGH severities**. Where my findings would, on my own reading, sit in
  those bands, I record them as **FLAGGED FOR PROJECT-LEAD / NON-PRODUCER-SEAT REVIEW** with an
  advisory band in parentheses, per the rotation document's advisory-role constraint.
- Consensus weighting in `bayyinah_cross-vendor-rotation.md` § *Vote weighting* lists Claude at 1.0,
  but that table governs Claude **as auditor of non-Claude output**; it does not survive the
  producer-exclusion rule for this artifact.

**Mode:** Mode B with Mode A spot-verification, per `methodology/bayyinah_audit-modes.md`
§ *Mixed-mode and Mode B with spot-verification*. I did **not** re-execute the five prescribed
commands -- the orchestrator's `COMMAND_OUTPUTS.txt` is canonical for this review by instruction. I
read the code and performed read-only static spot-checks (regex/arithmetic re-derivations over the
source and over `REPAIR_STATUS.md`; no gate execution, no test execution, no hashing). Substrate-claim
verification confidence: **high for arithmetic and selector claims I re-derived directly; reduced for
any claim that requires execution** (e.g. `allows=1603`, the 345 test outcomes, the 174 GREEN
outcomes), which I inherit single-sourced from `COMMAND_OUTPUTS.txt`. This annotation is itself
required: "Confidence annotation is itself a finding when absent" (`bayyinah_audit-modes.md`
§ *Confidence annotation*).

---

## 1. Sanity check on the ground-truth outputs

### 1.1 Affirmed consistencies (re-derived, not assumed)

| Output claim | Code substrate | Verdict |
|---|---|---|
| `MODEL CHECK ... kernel(243)` | `bssg_model_check.py` L44: 3^5 = 243 kernel truth states, `n == 243` asserted | Consistent |
| `antitone(729)` | `bssg_model_check.py` L51-63: for each subset `he` of `U_eff`, `de` ranges over subsets of `he`, so effect pairs = `(1+2)^3 = 27`; target pairs = 27; 27 * 27 = **729** contracts | Consistent |
| `bounded-auth-intro ... schedules=2800` | `bssg_model_check.py` L332-334: `_K = 4`, 7-op alphabet, `sum_{len=1..4} 7^len = 7+49+343+2401 = 2800`; `_bmc_sched` increments once per schedule | Consistent |
| `174/174 GREEN (0 RED)` | `bssg_counterexamples.py`: 350 `record("CE...")` call sites resolving to **174 unique CE ids**; 172 ids appear twice and 2 ids (CE1, CE6) three times, in every case as **mutually exclusive** try/except branches (L126-130, L198-202). One record per CE per run => `len(results) == 174` | Consistent |
| `OK (skipped=8)` on 345 tests | `test_bssg_gate.py` L1208: single `@unittest.skipUnless(HAVE_JSONSCHEMA, ...)` on `class SchemaTests`, which contains exactly **8** `def test_` methods | Consistent |
| `G2 WARN jsonschema not installed` | Same decorator/condition; the WARN and the 8 skips are the same fact | Consistent |
| `G1/G8/G9/G10 FAIL ... FileNotFoundError` | `verify_bssg_v0_1.py` `main()` wraps each gate in `try/except Exception` and records `"gate raised %s on non-total input"`. `gate_g8` reads every `REQUIRED_FILES` `.md`; `gate_g10` reads `OPEN_DECISIONS.md` and `BSSG_v0_1_DECISION_REGISTER.md` unguarded -- both are absent, so both raise. `gate_g10` would otherwise have recorded WARN | Consistent -- mechanism identified exactly |
| `G5`/`G7`/`G9`-unlisted FAILs | `source_files()` walks the **entire package directory recursively** (`os.walk(HERE)`, `.md/.py/.json`). The reviewer placed `methodology/` **inside** the package directory, so the methodology corpus entered every content gate's file universe. G5's `AUDIT_META` skip-list does not cover `bayyinah_*.md` | Consistent -- these FAILs are **review-harness contamination**, not artifact defects |
| Gate-count arithmetic | Brief expectation: 12 PASS / 2 WARN / 0 FAIL over 14 records (13 gates, G2 records twice). Observed: G1, G5, G7, G8, G9 move PASS->FAIL (12-5 = **7 PASS**) and G10 moves WARN->FAIL (2-1 = **1 WARN**, 5+1 = **6 FAIL**). 7+1+6 = 14 | Consistent -- the delta is fully accounted for |
| `DRAFT / NOT CARRIED` banner, no effectiveness claim | `bssg_gate.py` L5, L3127; spec L3-4, L27, L790 | Consistent |

**Cross-check of an audit-seat claim I could test on the record:** GLM's reported K=5 run
("19607 schedules") is exactly `sum_{len=1..5} 7^len = 19607` for this file's 7-op alphabet. The
arithmetic corroborates that GLM executed this specific enumeration rather than restating a number.
I cannot corroborate `allows=12475` without execution; it is recorded UNKNOWN, not favorable
(`SHVVP_v0_8_flagship.pdf` § *UNKNOWN discipline*: "Any required projection, provenance record, or
witness attestation that is absent, outside declared scope, or unverifiable is recorded as UNKNOWN.
It is never defaulted to the favorable value").

### 1.2 Inconsistency between the council packet and the canonical outputs -- FINDING C-01

`COUNCIL_INSTRUCTIONS.md` line 16 states: **"12 of 18 listed files verify OK."** The canonical
substrate says otherwise. `SHA256SUMS` contains **20** manifest entries; 6 are absent; **14** print
`OK` in `COMMAND_OUTPUTS.txt` (spec, REPAIR_STATUS, `bssg_attest.py`, `bssg_counterexamples.py`,
`bssg_gate.py`, `bssg_model_check.py`, six schemas, `test_bssg_gate.py`, `verify_bssg_v0_1.py`).
`COUNCIL_BRIEF.md` line 96 independently expects "20/20 OK", agreeing with the manifest, not with
the instructions.

- **Finding:** C-01. **Severity: MEDIUM** (methodology-fidelity, not gate soundness; per
  `bayyinah_severity-rubric.md` § *MEDIUM vs LOW*, a substrate-count divergence is a
  methodology-fidelity matter, and per § *CRITICAL vs HIGH* it causes no user-visible harm).
- **Locus:** `COUNCIL_INSTRUCTIONS.md:16` versus `SHA256SUMS` (20 lines) and
  `COMMAND_OUTPUTS.txt:2-28` (14 OK / 6 FAILED-open).
- **Substance:** the dispatch packet's restatement of the substrate is arithmetically wrong in both
  the numerator and the denominator. This is a textbook surface-substrate divergence
  (`PMD_v1_2_BAF_v3_0.md` §0.1) inside the review instrument itself, and it is the exact failure mode
  `bayyinah_audit-modes.md` § *Mode B -- Weaknesses* names: "Susceptible to absorbing substrate errors
  from the artifact's restatement (single-sourced substrate inheritance)." A seat that trusted the
  summary rather than `COMMAND_OUTPUTS.txt` would have propagated it. Compare Round 36's CRITICAL
  class in `bayyinah_severity-rubric.md`: "the prompt's enumerated test count did not match
  pytest-collected count".
- **Disposition:** correct the dispatch packet to 14/20 before any further seat is dispatched;
  re-derive from `SHA256SUMS`, not from prose.
- **Cross-reference:** `PMD_v1_2_BAF_v3_0.md` §0.1, §0.2 rule 5; `bayyinah_audit-modes.md`
  § *Mode B weaknesses*.

### 1.3 No other inconsistency found

Every other numeric and status claim in `COMMAND_OUTPUTS.txt` is reproducible from the code by static
derivation, and the six FAILs plus one WARN are fully explained by (a) the six deliberately omitted
manifest files and (b) the methodology corpus having been placed inside the scanned package
directory. **On the record as given, I affirm the ground-truth outputs as internally consistent with
the code.**

---

## 2. Convergence answer

> **QUALIFIED NO** -- decomposed as: **audit-convergence YES on the audit axis; carry NOT SATISFIED;
> therefore the artifact is not acceptable as *converged and carried*, and must retain
> DRAFT / NOT CARRIED.** Three-seat adversarial convergence does **not** substitute for the
> two-family carry. (Advisory only; this verdict carries no weight -- see § seat status.)

### 2.1 What the three-seat record *does* establish (PMD §0.4)

`PMD_v1_2_BAF_v3_0.md` §0.4 defines convergence by four conjuncts. On the audit axis:

- **Bullet 1 -- "Two consecutive cross-vendor rounds produce 0 CRITICAL findings":** V32-V34 is three
  consecutive rounds at 0 BLOCKER-class across GPT-5.6 (OpenAI), GLM-5.2 (Zhipu), Kimi K2.6
  (Moonshot). Three >= two. **Satisfied, with the vocabulary caveat in §2.6 and §4.**
- **Bullet 2 -- HIGH residual 0 or a project-lead-signed exception ledger entry:** claimed 0. But the
  exception-ledger substrate (`BSSG_v0_1_DECISION_REGISTER.md`, `OPEN_DECISIONS.md`,
  `ATTACK_AND_FALSIFIER_REGISTER.md`) is **absent from the reviewed package**, and the specification
  itself says blocking findings are "in some cases **still open** in
  `BSSG_v0_1_DECISION_REGISTER.md`" (spec L27). On this package the residual-HIGH state is therefore
  **UNKNOWN, not zero** -- SHVVP's UNKNOWN discipline and SHUDP's no-default prohibition
  (`SHUDP_v0_5_flagship.pdf` § *Axiom 5*: A5.3a "the no-default prohibition") forbid resolving it
  favorably. **NOT ESTABLISHED on the reviewed substrate.**
- **Bullet 3 -- MEDIUM/LOW absorbed or annotated non-operative:** the GPT MODERATE residual is
  characterized as documentation staleness. See Finding A-01: the staleness is real *and* the gate
  built to catch it is blind. **Partially satisfied at best.**
- **Bullet 4 -- "All standing-rule compliance checks pass (em-dash, brand, severity, six-element
  format, substrate uniqueness)":** `REPAIR_STATUS.md` states the counterexample count twice with two
  different values in the same document ("173/173 CE GREEN" at the repair34 battery block versus
  "This document claims 174 counterexamples" nineteen lines later), against a substrate of 174. That
  is a **substrate-of-record uniqueness** breach (`PMD_v1_2_BAF_v3_0.md` §0.2 rule 5, "each fact
  stated once") and a surface-substrate divergence (§0.1). **NOT satisfied.**

**Conclusion on §0.4:** the round-count conjunct is exceeded; two of the four conjuncts are not
demonstrated on the reviewed package. Under §0.4's own conjunctive construction, convergence is not
yet declarable **even before reaching the carry question**. Note also that `PMD` §0.4 and
`bayyinah_severity-rubric.md` § *Monotonic narrowing* state the bar slightly differently (the rubric
requires "0 CRITICAL and 0 HIGH"); on either reading the analysis above holds.

### 2.2 The carry is a separate, load-bearing gate -- it is not substitutable (SHVVP §0.3, §8.0)

The producer's framing asks whether three-family audit convergence can stand in for a two-family
carry. The corpus answers directly and repeatedly in the negative.

- **SHVVP §0.3, *Consequence for this version, frozen*:** "v0.5 has NOT been carried. It requires a
  fresh carrying audit by two non-producer seats of different vendor families ... before deposit.
  Producer-lineage, editor-lineage and chair review of v0.5 is ADVISORY and NON-CARRYING. **No claim
  of audit convergence attaches to v0.5 at the time of this freeze.**" Audit review and carry are
  distinct instruments; the absence of carry voids the convergence claim, it does not merely qualify
  it.
- **SHVVP §0.3, frozen carrying rule:** "a HALT from either carrying seat blocks deposit outright" --
  applied seven consecutive times (v0.1 through v0.7 all HALTED, "never deposited, never binding").
  The carry gate has, empirically in this corpus, never been discharged by seat count on the audit
  axis.
- **SHVVP v0.8 front matter -- the discharge condition, stated positively:** "v0.8 has now been
  carried. **Two executing non-producer families of different vendors, Kimi (Moonshot) and Qwen
  (Alibaba), converged on it**... The executable gate, signed vectors, and adversarial suite shipped
  here are **BYTE-IDENTICAL** to the release those two families executed ... **so the carry attaches to
  exactly these bytes**." Two elements are load-bearing: the seats must **execute**, and the carry
  attaches to **exact bytes**.
- **SHVVP §8.0 supplies the reason the substitution is invalid in principle.** §8.0's frozen record
  is that a *correct* computation under an *unjustified* model is still an invalid claim: "Correct
  arithmetic under an unjustified model is still an invalid claim, and it is the more dangerous kind,
  because it survives every check that only tests the arithmetic." The remedy §8.0 imposes is
  downgrading claims to what the design honestly supports, and §8 keeps in force "their
  zero-tolerance hard gates ... the conjunction-only combination across phases". The carry is a hard,
  **conjunctive** gate: extra evidence on one conjunct (a third audit family) cannot discharge a
  different conjunct. Reading three audit PASSes as a carry is precisely the postdictive
  re-justification §8.0 prohibits: "a sampling model invented to rescue a claim is exactly the
  postdiction that preregistration exists to prevent."
- **SHVVP §8.1a is the closest structural analogue to what is being proposed here.** Carrying finding
  F-P5-1 established that a gate "validated each record it received but never established that the
  record EXHAUSTS the evidence universe this contract freezes", and that "a favorable subset satisfied
  a fixed-denominator route". Substituting an available, favorable evidence set (three audit seats)
  for the frozen required set (two executing carry families) is the same move, one level up.

### 2.3 Why neither carry attempt counts -- even as partial credit (SHV D6, SHUDP Axiom 5)

**DeepSeek (Mode B, "CLEAN", non-executing, placeholder identity values, section header "Simulated
from Embedded Test Results"):**

- `SHV_Method_v1_1.pdf` D6 requires that each independent checker "**re-derive the load-bearing
  result from the primary source** rather than accept the producer's or another checker's number", and
  §8 restates the operational step as "have one independent party **re-derive** one result (D6)". A
  simulated identity value is not a re-derivation; it is acceptance of the producer's number. DeepSeek
  is therefore **not a checker under D6** for the executable claims, whatever its verdict.
- `SHUDP_v0_5_flagship.pdf` § *Axiom 5, canonical form* requires, for each covered event, a record
  whose "evidence-generation act is not within S's authority: not WithinAuth(gen(r), S)". Where the
  reported identity values originate in the producer-supplied embedded text rather than in an
  independent execution, the acting substrate can "cause, modify, suppress, reconfigure, or
  credential" that evidence -- WithinAuth holds, and **A5 is UNSATISFIED at the axiom level** while the
  event-level verdict remains UNKNOWN (SHUDP § *Two levels kept distinct*). Note SHUDP's fairness
  constraint, which I apply: "We do not infer failure from missing public disclosure" -- I infer
  UNKNOWN, not defect.
- SHVVP §0.3 already ruled on this exact pattern by annotation: in round 6 "the Gemini-class seat
  returned PASS on **a textual review that did not execute the gate**", and that PASS rescued nothing.
  A non-executing CLEAN is on the record as non-carrying.

**Qwen (Mode A attempted; delivery corrupted the bytes; SHA256 mismatch; ISSUES-FOUND):**

- Because the carry "attaches to exactly these bytes" and requires byte-identity (SHVVP v0.8 front
  matter), an execution over corrupted bytes attaches to **different bytes** and cannot carry the
  canonical artifact. Qwen's honest ISSUES-FOUND is correct behavior and is properly *not* an artifact
  finding -- but neither is it a carry. It is UNKNOWN with respect to canonical bytes.

**Net:** the carry pool produced **zero** admissible carrying records. Not one adverse record, and not
one favorable one -- the gate is **UNDISCHARGED**, which under the UNKNOWN discipline is not a pass.

### 2.4 Is a capability-shortfall carry failure a methodological blocker or a substrate limitation? (both -- and it still blocks)

It is genuinely an **execution-substrate limitation**, and the producer is right that it is not an
artifact defect. That distinction changes the **disposition** but not the **gate state**:

- `bayyinah_audit-modes.md` § *Mode selection rule* makes Mode A **mandatory** for "Test-count gate
  verification" and for "Post-ship audit against shipped artifact", and the same table lists Mode A
  capability per vendor. A seat lacking Mode A capability is not eligible for a Mode-A-mandatory cell.
  Selecting DeepSeek (no Python execution) for a carry role was therefore a **selection error against
  the mode-selection rule**, not bad luck -- and it is correctable by selecting an execution-capable
  non-producer family.
- The corpus supplies the fix, not an exemption. `bayyinah_cross-vendor-rotation.md` § *Tier 1* names
  Perplexity as the "load-bearing Mode A substrate verifier" with "Strong (tool-augmented)" Mode A
  capability, and SHVVP v0.8 discharged its own carry with **Kimi (Moonshot) and Qwen (Alibaba)** once
  delivery worked. Execution-capable non-producer families exist; two of them must execute canonical
  bytes.
- Framing an undischarged hard gate as excusable because the shortfall was environmental is exactly
  the favorable-default the UNKNOWN discipline forbids (SHVVP § *UNKNOWN discipline*; SHUDP A5.3a).

### 2.5 PMD M1.5 (mechanical-traceability exception) does not reach this case

`PMD_v1_2_BAF_v3_0.md` §0.5 item 5 (**M1.5**) states: "when an absorption cycle **exclusively**
executes prior audit's disposition-prescribed routes with **zero architectural latitude**,
cross-instance re-audit is recommended-but-not-blocking; project-lead signoff suffices."
`bayyinah_cross-vendor-rotation.md` § *Same-instance §0.1 named exception* makes the test binary: "did
the absorption cycle add ANY content beyond the remediation checklist? ... If yes: cross-instance audit
is blocking."

Two independent reasons M1.5 is unavailable here:

1. **The test fails on the substrate.** The V32->V33 absorption added a new counterexample
   (`CE174`, tagged `AUDIT-V33-01`, `bssg_counterexamples.py` L2608-2636) exercising new
   BaseException-totality behavior, and `REPAIR_STATUS.md` L15-16 records a "defense-in-depth clear at
   top of authorize". New code paths and new negative tests are architectural latitude. Answer to the
   binary test: **yes, content was added => cross-instance audit is blocking.**
2. **M1.5 relaxes the wrong gate.** M1.5 and the §0.1 exception both speak to **cross-instance
   re-audit**, and substitute **project-lead signoff** for it. Neither mentions the carry. Under
   SHV D6 the project lead is the producer's chain lead and "No party certifies its own work"; a
   producer-side signoff cannot discharge an evidence-independence gate (SHUDP Axiom 5). Using M1.5 to
   excuse a carry would convert a producer-quarantine rule into a producer self-certification.

### 2.6 Do MODERATE-only residuals cross the threshold? (severity rubric)

If MODERATE maps to MEDIUM, then `bayyinah_severity-rubric.md` § *MEDIUM* is permissive: "absorption-
route prescribed but ship-permissive ... The cycle **should not ship to production with open MEDIUM
findings**, but can ship to internal next-version absorption." Combined with § *Monotonic narrowing*
("Convergence is reached when two consecutive cross-vendor rounds produce 0 CRITICAL and 0 HIGH"),
MODERATE-only residuals **do not block convergence** but **do block production ship**. For a DRAFT /
NOT CARRIED artifact that is coherent. Two caveats: the mapping BLOCKER/SIGNIFICANT/MODERATE/MINOR ->
CRITICAL/HIGH/MEDIUM/LOW is nowhere declared in the corpus I was given (see §4), and per
`bayyinah_severity-rubric.md` § *Severity reconciliation*, an undeclared mapping across seats with
three different vocabularies is precisely the condition under which one-band disagreements go
undetected.

### 2.7 Does GLM's K=5 over-coverage strengthen or weaken the carry argument?

**It strengthens confidence in the invariant and weakens the carry argument.**

- Strengthens: 19607 is exactly `sum_{1..5} 7^len` for the shipped alphabet, so the run is
  arithmetically attached to this enumeration, and it directly addresses the V30 convergence event in
  which all three seats found K=3 insufficient because "the K=3 bound misses the minimal violating
  schedule (length 4)" (`REPAIR_STATUS.md` L33-35). Deeper bounded coverage is real assurance.
- Weakens: `_K = 4` is a **hardcoded literal** in `bssg_model_check.py` L332 with **no argv or
  environment override**. A K=5 run is therefore only reachable by **editing the canonical bytes**.
  Under SHVVP v0.8's byte-identity requirement ("BYTE-IDENTICAL ... so the carry attaches to exactly
  these bytes"), evidence produced on edited bytes does not attach to the shipped artifact, and it is
  not reproducible from the sealed package by a later seat. It is also audit-seat evidence, not carry
  evidence. Under SHVVP §0.2's frozen scope rule -- a claim "establishes only what a descriptive gate
  permits: that, in the single case or the single run in which it was observed" -- the K=5 result
  supports a statement about *GLM's modified copy*, not about the sealed K=4 artifact.
- **Constructive disposition:** expose the bound as `BSSG_MC_K` (env or argv, default 4) and record
  the K=5 run in the ledger. That converts a non-attaching favor into reproducible, byte-attached
  evidence.

### 2.8 Summary of the answer

| Gate | Instrument | State |
|---|---|---|
| Two consecutive 0-CRITICAL cross-vendor rounds | PMD §0.4 bullet 1 | **Exceeded** (three: V32-V34) |
| Fresh rotation | PMD §0.4 / rotation § *Rotation rule* | Not independently satisfied by round count -- see §4 |
| HIGH residual 0 or signed exception ledger | PMD §0.4 bullet 2 | **UNKNOWN** (register absent) |
| Standing-rule compliance (substrate uniqueness) | PMD §0.4 bullet 4, §0.2 rule 5 | **FAILED** (173 vs 174 in one document) |
| Two executing non-producer families, byte-identical | SHVVP §0.3, v0.8 front matter; SHV D6; SHUDP A5 | **UNDISCHARGED** |
| Producer excluded from certification | SHV D6; rotation § *Producer-instance exclusion* | Honored (this seat is advisory) |

The honest label for the artifact today is the one it already carries: **DRAFT / NOT CARRIED**. The
three-seat record is a real and hard-won result -- the first convergence events in the program's
history -- and it should be recorded as **audit-convergence achieved on the audit axis, carry
outstanding**. It is not acceptance of convergence *simpliciter*.

---

## 3. Independent findings against the code

All findings are advisory. Bands in parentheses are my reading only; per
`bayyinah_cross-vendor-rotation.md` § *Producer-instance exclusion* I do not assign CRITICAL or HIGH
and I do not HALT.

### A-01 -- G12's "current claim surface" selector silently mis-selects a four-pass-stale section
**FLAGGED FOR PROJECT-LEAD / NON-PRODUCER-SEAT REVIEW (advisory band: HIGH-class checker-precision
gap).** Six-element format per `bayyinah_findings-format.md`.

- **ID / severity:** A-01 / flagged, advisory HIGH-class (blocks ship, locally resolvable --
  `bayyinah_severity-rubric.md` § *HIGH*).
- **Locus:** `verify_bssg_v0_1.py` L1202, regex
  `r"# BSSG v0\.1 -- Repair Status \(pass-(\d+)"`, versus `REPAIR_STATUS.md` L1 and L27.
- **Substance:** G12 selects the "CURRENT claim surface" as the section with the highest matched pass
  number. The two newest sections are headed `# BSSG v0.1 -- repair34 / V32 adjudication...` (L1) and
  `# BSSG v0.1 -- repair33 / V30 adjudication...` (L27) -- lowercase `repair34`, no `Repair Status
  (pass-N` token -- so **neither matches the regex**. Static re-derivation of the selector confirms the
  matched pass numbers are 17-30 and the selected "current" section is
  `# BSSG v0.1 -- Repair Status (pass-30, post V28 audit)` at L132. Consequences: (i) G12 rule (6)'s
  unanchored-load-bearing-claim tripwire never scans the repair33/repair34 prose; (ii) G12 rule (5)'s
  numeric corpus-count check reads `174` from the **stale** section and passes, while the **actual
  current** battery block states `173/173 CE GREEN` against a 174-CE substrate -- the one wrong number
  in the file is the one number the gate cannot see; (iii) the 27 registered `{claim:ID}` tags are
  verified against pass-30 history rather than the current claim surface.
  This is precisely the defect class the code's own comment claims to have retired: "the CURRENT claim
  surface is the section with the HIGHEST pass NUMBER, selected semantically -- NOT 'whatever heading
  is physically first'. A section appended at the bottom, or a reordered file, can no longer
  mis-select a stale section as current." The fix is bound to a heading format the producer
  subsequently abandoned, so the guarantee lapsed silently. Under `PMD_v1_2_BAF_v3_0.md` §0.1 this is
  a surface-substrate divergence in a verification gate; under SHVVP §8.1a it is the
  caller-selectable-evidence-universe shape (the checked universe is chosen by a naming accident, and
  the unfavorable record falls outside it). It also bears directly on the producer's convergence
  framing: the residual GPT MODERATE is described as mere documentation staleness "NOT a gate
  defect" -- but the gate built to mechanically prevent that staleness is **blind by construction** on
  the current bytes. That upgrades the class from documentation to checker precision.
- **Disposition:** replace the format-bound regex with a format-agnostic newest-section selector
  (e.g. match `^# BSSG v0\.1 --` and derive the pass ordinal from `repair(\d+)` or `pass-(\d+)`,
  whichever is present), **and** add a gate that FAILs when a `# BSSG v0.1 --` heading exists that the
  selector cannot ordinal-parse (fail closed on unparseable headings rather than skipping them). Add a
  counterexample that renames the newest heading and asserts G12 FAILs.
- **Cross-reference:** supersedes the "one-CE-count staleness" characterization of the V32-V34 GPT
  MODERATE; same class as the retired pass-20 G12 recursion (GPT-P4 / GLM-01 / K20-G1) and the V27
  K28-VF-1 / V28 Kimi-A6 corpus-trust findings; `SHVVP_v0_8_flagship.pdf` §8.1a.

### A-02 -- `REPAIR_STATUS.md` has no V33 or V34 entry, while the code contains a V33 absorption
**Severity: MEDIUM** (methodology fidelity / append-only ledger).

- **Locus:** `REPAIR_STATUS.md` -- headings run repair34/V32, repair33/V30, pass-30 ... ; string search
  for `V33`, `V34`, `repair35`, `repair36` returns **zero** matches. Meanwhile
  `bssg_counterexamples.py` L2608 registers `CE174` tagged `AUDIT-V33-01`, and the corpus is at 174.
- **Substance:** the two rounds on which the convergence claim rests (V33, V34) have **no entry in the
  hash-verified ledger**, and a V33 repair is present in the executable with no ledger record.
  `PMD_v1_2_BAF_v3_0.md` §0.2 rule 6 requires an "append-only ledger" and §0.3 stage 6 makes the
  ledger a lifecycle stage; `bayyinah_substrate-of-record.md` and §0.2 rule 5 make the ledger the
  single place each cycle fact is stated. Convergence being asserted from rounds absent from the
  ledger of record inverts the substrate-of-record discipline. The AUDIT-V33-01 tag also has no
  `{claim:ID}` counterpart in the ledger, which G12 does not catch -- see A-01.
- **Disposition:** append repair35/V33 and repair36/V34 sections stating seat verdicts, absorbed
  findings, CE ids, and the battery state; correct `173/173` to `174/174`; re-seal `SHA256SUMS`.
- **Cross-reference:** A-01 (why no gate caught this); PMD §0.2 rules 5-6, §0.3 stage 6, §0.4
  bullet 4.

### A-03 -- the bounded model check can pass vacuously: no floor on `allows`, no assertion that establishment ALLOWed
**Severity: MEDIUM** (assurance-coverage; no known live defect).

- **Locus:** `bssg_model_check.py` L334-365, the `if _est.get("decision") != "ALLOW": continue` branch
  and the final `check(...)` call.
- **Substance:** `_bmc_sched` is incremented **before** the establishment ALLOW test, and schedules
  whose establishment fails are silently skipped. If a future regression made the fixed healthy
  establishment stop returning ALLOW, the check would print `schedules=2800 allows=0` and **PASS**,
  because the only assertion is `_bmc_violation is None`. `allows` is printed as descriptive detail
  and is not gated. This is the shape SHVVP §8.1a records as an accepted carrying finding -- "one of
  which produced support for a component with **0 of 100 passing raw items**" (SHVVP §0.3, round-4
  record) -- and the same shape as the already-absorbed K28-VF-1 / Kimi-A6 findings against the
  verifier's trust in the corpus. Under `PMD_v1_2_BAF_v3_0.md` §0.1 a check that can report PASS while
  exercising nothing is a surface claim without substrate.
- **Disposition:** pin a minimum: assert the establishment ALLOWed on every schedule (or count
  establishment failures and FAIL if non-zero), and add a frozen floor `allows >= 1603` (or a
  committed expected count) so a coverage collapse FAILs rather than passes. Add a counterexample that
  poisons establishment and asserts MODEL CHECK FAIL.
- **Cross-reference:** SHVVP §8.1a and §0.3 round-4 record; G13's analogous independent-count fix in
  `verify_bssg_v0_1.py` L1252-1291, which is the right pattern and should be mirrored here.

### A-04 -- G13 verifies the corpus's integrity but not its cardinality
**Severity: MEDIUM** (evidence-universe commitment).

- **Locus:** `verify_bssg_v0_1.py` L1265-1291.
- **Substance:** G13 correctly refuses to trust the corpus self-report and independently counts
  per-CE lines, checks for REDs, checks for duplicate ids, and cross-checks the summary -- a genuinely
  strong control. But its pass condition is `green_obs > 0 and red_obs == 0`. A corpus silently
  reduced from 174 to, say, 5 counterexamples would still PASS G13 with a self-consistent summary. By
  contrast G3 pins a floor (`if kernel < 243: FAIL`). SHVVP §8.1a is explicit that this is the
  defect: a gate that "validated each record it received but never established that the record
  EXHAUSTS the evidence universe this contract freezes", remedied by "a frozen scope manifest fixed
  before any outcome is inspected". The corpus's own denominator is `len(results)`, so a CE that dies
  before its `record()` call disappears from numerator **and** denominator rather than going RED.
- **Disposition:** commit a frozen `MIN_CE` floor (and ideally a committed CE-id set digest) in the
  verifier and FAIL when observed unique ids fall below it or when an id in the committed set is
  absent. This is the same discipline as `MANIFEST_SHA256` in SHVVP §8.1a.
- **Cross-reference:** SHVVP §8.1a; A-03.

### A-05 -- the verifier's totality wrapper catches `Exception`, not `BaseException`
**Severity: LOW** (hygiene; the artifact's own repair history makes this the salient class).

- **Locus:** `verify_bssg_v0_1.py` `main()`, `except Exception as _e:`.
- **Substance:** the wrapper exists to make the verifier total ("the verifier is TOTAL -- any gate
  that raises ... records FAIL and the run proceeds"). CE167 and CE174 (`AUDIT-V33-01`) exist precisely
  because `BaseException` totality in the gate was a live finding class. A `BaseException` from a gate
  (e.g. inside a subprocess-free probe) would escape `main()` before the summary, and the run would
  terminate with no `PACKAGE STATUS` line -- silent absence rather than FAIL. Under SHVVP's fail-closed
  discipline ("a verifier must treat a missing attestation as unproven rather than assume the missing
  statement was favorable", SHVVP § *UNKNOWN discipline*), a missing summary must not be readable as
  anything but failure.
- **Disposition:** catch `BaseException` in the per-gate wrapper (re-raising `KeyboardInterrupt`
  deliberately if desired), and print the summary from a `finally` block.
- **Cross-reference:** CE167, CE174 / AUDIT-V33-01.

### A-06 -- the verifier's file universe is directory-scoped, not manifest-scoped
**Severity: LOW** (structural note; it produced four of the six observed FAILs).

- **Locus:** `verify_bssg_v0_1.py` `source_files()` (`os.walk(HERE)`).
- **Substance:** content gates G5 and G7 scan whatever `.md/.py/.json` files happen to be under the
  package directory. Placing the methodology corpus inside the package directory therefore injected
  FAILs (G5 `outperform` in `bayyinah_cross-vendor-rotation.md:151`; G7 em/en/horizontal-bar
  characters inside `bayyinah_em-dash-policy.md`, a document that necessarily displays the characters
  it prohibits) and populated G9's "present but not in the manifest" list with eleven methodology
  files. The FAILs are review-harness contamination, exactly as the orchestrator states -- but the
  underlying property is that the evidence universe is ambient rather than committed, which is the
  same SHVVP §8.1a concern as A-04, and it also means these gates' verdicts are not reproducible
  across packaging environments.
- **Disposition:** scope G5/G7 to the manifest's file list (plus an explicit allow-list), and make an
  unlisted-file presence a distinct WARN rather than silently widening the content gates. Extend
  `AUDIT_META` to cover policy documents that must quote prohibited tokens.
- **Cross-reference:** C-01; SHVVP §8.1a.

### Non-findings I explicitly clear

- **The six absent files are not a code defect.** Every present manifest entry verifies, the FAIL
  mechanism is fully explained, and the omission is a stated packaging choice. But per §2.1 bullet 2
  the omission does have an **evidentiary** cost that the packet does not acknowledge: the omitted set
  is exactly the falsifier register, decision register, open-decisions list, and requirements
  traceability -- the primary sources SHV D6 requires an independent checker to re-derive from, and the
  substrate for PMD §0.4 bullets 2 and 3. Their absence is UNKNOWN, not clean.
- **G7's failure on the em-dash policy document is not an em-dash-policy breach by the artifact.** It
  is a scoping artifact (A-06).
- **The `173/173` figure is not evidence of a corpus regression.** The corpus substrate is 174 unique
  CE ids; the document is wrong, not the code (A-02).

---

## 4. Dissenting angle

**I dissent from the framing that "three consecutive zero-BLOCKER rounds" is a strictly stronger form
of the two-round convergence bar. It is a *longer* record on one axis, measured in a vocabulary the
methodology does not define, with the rotation conjunct unaddressed.**

Three specific objections.

1. **Round count and rotation are different conjuncts, and only one was exceeded.** The brief's own
   statement of the bar is "two consecutive clean rounds **with at least one seat rotated fresh**."
   V32, V33 and V34 were audited by the **same three seats** -- GPT-5.6, GLM-5.2, Kimi K2.6. Adding a
   third round with an unchanged panel adds depth on the round conjunct and **nothing** on the
   rotation conjunct. `bayyinah_cross-vendor-rotation.md` § *Rotation rule* is unambiguous that
   freshness is about seat identity: "The per-round cross-instance auditor **must differ from the
   prior round's auditor** AND from the producer instance", and the empirical record shows the
   program annotating the exception when it could not comply ("Round 37: Perplexity ... same-vendor
   consecutive permitted only when no other vendor available; **flagged in audit deliverable**").
   Three unrotated rounds do not satisfy a conjunct about rotation; they satisfy the same conjunct
   three times. Under SHVVP §8.0's logic this is the "correct arithmetic under an unjustified model"
   error in miniature: the count is right, the mapping from count to conclusion is not. There is also
   a diminishing-returns argument the producer should not want to leave implicit -- a panel that has
   already exhausted its search on these bytes is the panel least likely to find round-four findings,
   which is exactly why freshness is specified separately from depth.

2. **"Zero-BLOCKER" is not "0 CRITICAL and 0 HIGH", and the mapping is undeclared.**
   `PMD_v1_2_BAF_v3_0.md` §0.2 rule 3 fixes the severity vocabulary as "CRITICAL, HIGH, MEDIUM, LOW".
   The V32 verdicts as recorded in `REPAIR_STATUS.md` L11-13 use **three different vendor
   vocabularies** -- GPT "0 CRITICAL / 0 SIGNIFICANT / 2 MODERATE / 1 NOTE", GLM "0 BLOCKER / 0 MAJOR /
   4 MINOR / 6 INFO", Kimi "CONDITIONAL" -- and nothing in the corpus I was given declares the
   crosswalk. Convergence is being asserted across an untranslated vocabulary. Two consequences: (i)
   `bayyinah_severity-rubric.md` § *Severity reconciliation under cross-vendor disagreement* requires
   one-band disagreements to be detected and resolved upward ("adopt the higher severity and
   annotate"), which is impossible without a declared mapping -- is GPT's SIGNIFICANT the same band as
   GLM's MAJOR, and is either HIGH? (ii) GLM's "4 MINOR" at V32 and GPT's persistent MODERATE are
   being read as sub-threshold by assumption rather than by rule. A one-page severity crosswalk, frozen
   and applied retroactively to V29-V34, would convert this from assumption to record. Until it
   exists, "zero-BLOCKER across three rounds" is a claim about vendor labels, not about PMD bands.

3. **The residual MODERATE was mischaracterized, and my A-01 is the proof.** Across V32-V34 the
   residual is described as documentation staleness, "explicitly not gate defects". On the shipped
   bytes, the mechanism that is supposed to make that class mechanically impossible -- G12's
   current-claim-surface selector -- cannot see the current claim surface at all, because the producer
   renamed its own headings out of the selector's regex (A-01). The stale number therefore persists
   not because it is cosmetic but because **the gate is blind**, and G12 reports PASS while reading a
   four-pass-old section. Under `PMD_v1_2_BAF_v3_0.md` §0.1 that is a surface-substrate divergence
   located in a verification gate, which is the artifact's core subject matter; and under
   `bayyinah_severity-rubric.md` § *HIGH vs MEDIUM* it plausibly requires multiple surfaces (selector,
   ledger headings, battery counts) to be corrected before the package is internally consistent. I do
   not assign the band -- producer-family seats cannot (rotation § *Producer-instance exclusion*) -- but
   I flag it as the one finding in this review that, if a non-producer seat confirms it, should reset
   the convergence count rather than be absorbed as hygiene. Note the pattern the ledger itself names:
   "The 31st consecutive instance of the producer's own fix shipping incomplete one level deeper (SHV
   Axiom 3 / SHVVP §0.3 pattern)" (`REPAIR_STATUS.md` L46-47). A-01 has that exact shape -- the fix for
   the stale-section defect was itself stale -- and SHVVP §0.3 draws the corresponding conclusion about
   producer self-assessment: "The pattern is not bad luck; it is evidence that this producer's ...
   ambition exceeded what the frozen design can support."

**What I would accept, as advice.** Do not weaken the carry. Discharge it: select two
execution-capable non-producer families (SHVVP v0.8's own precedent is Kimi + Qwen; the rotation
document names Perplexity as a load-bearing Mode A verifier), deliver canonical bytes over a channel
that preserves SHA256, require each seat to re-derive the five command outputs from the primary source
rather than restate them (SHV D6), and record the carry as attaching to a named digest. Then append
the missing V33/V34 ledger sections, fix `173/173`, repair the G12 selector, and freeze a severity
crosswalk. On that package, a two-family carry plus the existing V32-V34 record would in my advisory
view clear PMD §0.4 in full -- and it would clear it on the record rather than on an argument.

---

## Methodology sources relied on

All citations are to the corpus supplied at `/home/user/workspace/bssg_review/methodology/`:

- `PMD_v1_2_BAF_v3_0.md` -- Predictive Modeling Discipline v1.2 / Bayyinah Audit Framework v3.0
  (Zenodo DOI 10.5281/zenodo.20017335): §0.1 surface vs substrate; §0.2 standing rules 3, 5, 6, 7;
  §0.3 six-stage lifecycle; §0.4 convergence definition; §0.5 item 5 (**M1.5**, mechanical-
  traceability exception); §0.6 empirical record.
- `bayyinah_cross-vendor-rotation.md` -- § *Rotation rule*; § *Producer-instance exclusion*;
  § *Same-instance §0.1 named exception* (binary mechanical-traceability test); § *Tier
  classification*; § *Vote weighting*; § *Audit-modes by tier*; § *Empirical record*.
- `bayyinah_severity-rubric.md` -- CRITICAL / HIGH / MEDIUM / LOW definitions and dispositions;
  § *Severity boundary calibration*; § *Severity reconciliation under cross-vendor disagreement*;
  § *Monotonic narrowing expectation*.
- `bayyinah_audit-modes.md` -- Mode A / Mode B definitions, strengths and weaknesses;
  § *Mixed-mode and Mode B with spot-verification*; § *Mode selection rule*; § *Confidence
  annotation*.
- `bayyinah_findings-format.md`, `bayyinah_substrate-of-record.md` -- six-element findings format;
  substrate-of-record uniqueness.
- `SHVVP_v0_8_flagship.pdf` -- front matter (carry discharge by two **executing** non-producer
  families, byte-identity of the carried bytes, producer-lineage review ADVISORY and NON-CARRYING);
  §0.1 UNKNOWN list; § *UNKNOWN discipline*; §0.2 (what a pass does and does not establish);
  **§0.3** (carrying-audit history, the frozen carrying rule "a HALT from either carrying seat blocks
  deposit outright", the round-6 non-executing PASS annotation, and "No claim of audit convergence
  attaches ... at the time of this freeze"); **§8.0** (withdrawal record; "Correct arithmetic under an
  unjustified model is still an invalid claim"); §8.1 (Class G gates); §8.1a (frozen scope manifest;
  favorable-subset and evidence-universe findings F-P5-1, F-P6-1).
- `SHV_Method_v1_1.pdf` -- **D6** ("Producer-quarantined, multi-chain convergence. No party certifies
  its own work"; independent checkers must "re-derive the load-bearing result from the primary
  source"); §7 worked patterns (certify by independent re-derivation); §8 ("stop certifying your own
  work and have one independent party re-derive one result (D6)").
- `SHUDP_v0_5_flagship.pdf` -- **Axiom 5** (evidence independence; canonical form and the
  `WithinAuth(gen(r), S)` predicate; A5.3a no-default prohibition; § *Two levels kept distinct*
  -- axiom-level UNSATISFIED versus event-level UNKNOWN; "We do not infer failure from missing public
  disclosure").
- Artifact substrate: `COMMAND_OUTPUTS.txt`, `COUNCIL_BRIEF.md`, `COUNCIL_INSTRUCTIONS.md`,
  `SHA256SUMS`, `REPAIR_STATUS.md`, `BSSG_v0_1_CANONICAL_SPEC_DRAFT.pplx.md`, `bssg_gate.py`,
  `bssg_counterexamples.py`, `bssg_model_check.py`, `test_bssg_gate.py`, `verify_bssg_v0_1.py`,
  `schemas/*.json`.

**Restated for the record:** this report is produced by a **producer-family (Anthropic) seat** and is
**ADVISORY and NON-CARRYING**. It assigns no CRITICAL or HIGH severity, casts no accept vote, and
cannot be counted toward convergence, carry, or deposit under
`bayyinah_cross-vendor-rotation.md` § *Producer-instance exclusion*, `SHV_Method_v1_1.pdf` D6, or
`SHVVP_v0_8_flagship.pdf` §0.3.

---

# Bismillah ir-Rahman ir-Rahim
