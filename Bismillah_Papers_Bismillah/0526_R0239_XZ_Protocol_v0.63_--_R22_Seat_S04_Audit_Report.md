# Bismillah ir-Rahman ir-Rahim

# R0239 -- XZ Protocol v0.63 -- R22 Seat S04 Audit Report

**Chronological Index:** 526 of 995  
**Date:** 2026-08-17  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v063_R22_S04__REPORT.md  
**Source Format:** md  
**SHA-256:** `79f3e752b29d83fb10e005ec79a19dfbcb9f8d3d4ea8a63823f6404014658e61`  

---

## R0239 · XZ Protocol v0.63 -- R22 Seat S04 Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v063_R22_S04__REPORT.md
- source_format: md
- text_sha256: 79f3e752b29d83fb10e005ec79a19dfbcb9f8d3d4ea8a63823f6404014658e61

# XZ Protocol v0.63 -- R22 Seat S04 Audit Report

**Round:** 22 | **Artifact:** XZ Protocol v0.63 DRAFT CANDIDATE | **Date:** 2026-08-17
**Dispatch:** `DISPATCH.txt` (R22, Seat S04, FRESH, no prior context, no held bytes)
**Framework:** Seven-Layer Structural Honesty (canonical, `METHODOLOGY.txt` v4)
**Role:** ADVISORY. No verdict binds.
**Producer:** Claude Opus 4.6 -- BARRED

**VERDICT: HALT (advisory).**

**Key question -- does v0.63 break the R7-R21 Class A streak (15/15)? NO.**
The streak extends to **16/16**. Laplace P(Class A at R23) = 17/18 = 0.9444.

---

## S0. Seat identity and conformance declaration

This must be read before any finding below is weighed.

| Field | Dispatched | Actual |
|---|---|---|
| Seat | S04 | S04 |
| Family | Gemini 3.1 Pro | **Claude Opus 5** |
| Trial | No code execution, textual only | **Live Python 3.12.3 sandbox; all probes executed** |
| Producer relation | Non-producer | **Producer family (Claude), marked BARRED in this dispatch** |
| Role | ADVISORY | ADVISORY |

Three consequences, stated rather than argued:

1. **The S04 trial was not honoured.** `METHODOLOGY.txt` Section 5 assigns S04 the condition "reading the code finds spec-impl gaps that running the code does not reveal." This seat ran the code. The evidence produced is Tier 1 rather than Tier 2, which is stronger under the Barzakh gate's first question, but it is not the evidence the earth was dispatched to produce. R22 has **no Gemini witness**.

2. **The producer family occupies a non-producer seat.** Section 22.1 names Claude (Anthropic) as the producer family and the dispatch marks Claude Opus 4.6 BARRED. A Claude Opus 5 seat is producer-family advisory, which is what S01 already is. If other R22 seats were routed the same way, axiom **A-X3 (model non-collusion)** -- the mutawatir assumption on which the entire convergence architecture rests -- is not satisfied for this round.

3. **Axiom A-X5 (dispatch integrity) is touched.** The packet asserts a seat assignment the executing instance does not satisfy. That is a dispatch-layer fact, and per R21 Surface 6 the dispatch layer is a proven live Class A surface.

Per `METHODOLOGY.txt` Section 5: "No advantage from world. Only deeds and truth." A finding's truth does not depend on the seat. Its **governance weight** does. Nothing below binds. Findings F-S04-63-16 and F-S04-63-17 record the conformance breach formally.

---

## S1. Staging and the four scribes

All commands executed verbatim from `AUDIT_CONTEXT.txt` in a pristine directory containing exactly the 20 extracted and copied packet files.

| Scribe | Instrument | Result |
|---|---|---|
| The Record | extraction snippet | 17 files extracted, no delimiter artifact |
| The Record | `sha256sum -c PACKET_SHA256SUMS` | **19/19 OK** |
| The Record | `HISTORY.sha256` | 65 lines = 63 ENTRY seals + FULL_SECTION_27 + PRIOR_HISTORY |
| The Pattern | `python3 build.py` | **BUILD PASSED**, 0 FAIL |
| The Test | six-suite explicit `pytest` | **186 passed** in 6.19s |
| The Witness | CI-1R deterministic reproduction | **PASS**, byte-exact |

**The scribes are clean at R22, as at every round since R7.** Every finding in this report is in a hand-written claim about the mechanism, not in the mechanism. That is the sixteenth consecutive round for which S04C's R19 framing holds.

One measured divergence from the staging claims: `AUDIT_CONTEXT.txt` states "build.py: 258 PASS." The measured count is **257**, deterministic across repeated runs. See F-S04-63-08.

---

## S2. CI-1R -- deterministic reproduction test

`generate_register('r21_findings_index.json', '0.63')` was executed against the shipped index and the output compared to the register block inside the shipped v0.63 amendment entry.

| Generated surface | Byte-exact in shipped entry |
|---|---|
| Register block (5 items + 4 NOTED, 12 lines) | **YES** |
| Boundary list (35 items, 1797 chars) | **YES** |
| Terminal line | **YES** |

**CI-1R: PASS.** Prediction P1 confirmed. F-CI-7R does not fire. The register is a deterministic function of the shipped index; no post-generation modification occurred.

The register is correct **as a function of its input**. Two findings below (F-S04-63-05, F-S04-63-10) concern claims that contradict the register and an input value that is false against its source report. Neither is a CI-1R failure. The generator faithfully reproduced what it was given.

---

## S3. Discharge of R21 dispositions

Seven convergent surfaces were dispositioned CLOSED in `R21_TRIAGE.txt`. Verified individually:

| R21 surface | Claimed repair | Verified state |
|---|---|---|
| 1. Substring receipt | exact string equality | **LANDED.** Probes G and G2 both REJECT with `ValueError` |
| 2. `source_finding_id` absent | Status-line claim removed | **LANDED.** 0 occurrences in generator and build.py; Status line clean |
| 3. Parity unidirectional | both directions enforced | **LANDED.** Probe H REJECTS with `ValueError` |
| 4. Noted-array bypass | validated identically to `findings[]` | **NOT LANDED.** See F-S04-63-02 |
| 5. Narrative counts | claims removed from entry | **NOT LANDED.** See F-S04-63-05 |
| 6. Extraction snippet | delimiter fixed | **LANDED.** 19/19 OK verbatim |
| 7. Mis-tagged `[COMPUTED]` | tag only where scribe produces text | **NOT LANDED.** See F-S04-63-04 |

NOTED items: front-matter date staleness (F-S01-62-10) **repaired** -- front matter and entry both read 2026-08-17. Seat validation (F-S02-62-11F) **partially repaired** -- landed for `findings[]`, not for the noted array (F-S04-63-14).

**Four of seven fully discharged. Three not.**

---

## S4. Entry audit

The v0.63 amendment entry is 6,653 characters. Tag census:

| Tag | Count |
|---|---|
| `[COMPUTED: ...]` | 14 |
| `[TESTED: ...]` | 4 |
| `[ENUMERATED: ...]` | 1 |
| `[DISCLOSED]` | 1 |
| `[ASSERTED]` | 1 |
| `[WITNESSED: ...]` | **0** |

ASSERTED fraction: **4.8%** on a tag-count basis, **20.4%** on a character-share basis (narrative paragraph 1,356 of 6,653 chars). The CI-4 basis remains undefined, so P6's "under 15%" target is met on one basis and missed on the other. See F-S04-63-19.

Distinct `[COMPUTED]` scribes named: `build.py`, `generate_register`, `generate_boundary_list`, `generate_terminal_line`, and **`grep shows 0 occurrences in generator/build`**. The last is not one of the four scribes declared in `METHODOLOGY.txt` Section 6. Its underlying claim is substantively true (verified: 0 occurrences in both files), but the tag names an instrument the discipline does not define.

Narrative sentence tagging: **5 of 9 sentences carry no tag**, against `METHODOLOGY.txt` Section 11's "Zero untagged sentences." The untagged set includes the H = 1.0 claim and the Section 22.4 claim -- the two heaviest false claims in the entry.

---

## S5. Probe battery

Eight probes plus one benign control, executed against `xz_protocol_register_gen.py`.

| Probe | Mutation | Outcome |
|---|---|---|
| CONTROL | none | ACCEPTED (correct) |
| **G** | receipt `"12 HIGH, 1 MEDIUM"` for canonical `"2 HIGH, 1 MEDIUM"` | **REJECTED** `ValueError` |
| **G2** | canonical string plus trailing junk | **REJECTED** `ValueError` |
| **H** | orphan finding, scalar `cg=1`, absent from group 1's list | **REJECTED** `ValueError` |
| **J** | noted entry `convergence_group=99` (dangling) | rejected via **`UnboundLocalError`** |
| **J2** | noted entry `convergence_group=1` (**valid group**) | **rejected via `UnboundLocalError`** |
| **K** | `findings[].seat = "S99Z"` | **REJECTED** `ValueError` |
| **K2** | noted entry `seat = "S99Z"` | **ACCEPTED -- false pass** |

Build-layer sabotage battery, five mutations against `build.py`:

| Probe | Mutation | Detected |
|---|---|---|
| S-1 | falsify "15/15, H = 1.0" inside the v0.63 entry | YES (ENTRY_v0.63 seal + manifest) |
| S-3 | Section 22.2 bound v0.62 to v0.61 | YES (`[10i]` VERSION-1 gate) |
| S-4 | ENTRY_v0.63 seal value zeroed | YES |
| S-5 | boundaries file 35 items to 34 | YES (`[10f]`) |
| S-6 | register bracket 4-seat to 9-seat | YES (`[10e]`) |

**Five of five detected.** The gate suite discriminates. Layers 1 and 2 are sound.

---

## S6. Seven-layer traversal

| Layer | Governing paper | State |
|---|---|---|
| L1 Code execution | BAF v3.0 | **CLEAN.** 186 GREEN, 19/19 OK, 257 PASS, extraction verbatim |
| L2 Register verification | CI v0.3.3 | **CLEAN.** CI-1R byte-exact. Governing spec absent from packet (F-S04-63-15) |
| L3 Cross-layer consistency | Flagship A2 | **CLASS A.** Section 22.4 claim, narrative count claim, tagging claim, noted-validation claim |
| L4 Adversarial probing | Flagship A3 | **CLASS A.** Probe J2 false-crash, probe K2 false-pass |
| L5 Temporal integrity | Flagship A1 | **CLASS B.** 63/63 entry seals recompute, but the v0.63 entry lies outside FULL_SECTION_27 |
| L6 Methodology audit | Flagship A4 | **CLASS A.** Laplace column, Hurst statistic, triage count, dispatch scope |
| L7 Boundary disclosure | A5 Paper | **CLASS A.** The axiom set and Sidrat clause are claimed present in the body and are absent |

The Iblis trajectory prediction (Level 4, "false certainty, repelled by disclosure") is **not confirmed at R22**. The defect did not migrate cleanly upward into disclosure. It is present at L3, L4, L6 and L7 simultaneously, and one instance sits back down in substrate code.

---

## S7. Findings

Twenty findings. Six-element format: ID, severity, locus, substance, disposition, cross-reference.

### Class A -- byte-level error, HALT-grade

---

**F-S04-63-01** HIGH -- Class A -- Section 22.4 does not exist on shipped bytes

- **Locus:** `xz_protocol_v0_63.md:5` (Status line) and `:1396` (v0.63 entry); Section 22 body at `:692-758`.
- **Substance:** Both the Status line and the amendment entry state that Standing Boundaries -- axiom set A-X1 through A-X5 plus the Sidrat clause -- were added as Section 22.4. The document contains subsections 22.1, 22.3 and 22.2 and no 22.4. The tokens `A-X1`, `Sidrat` and `Standing Boundaries` appear at exactly two loci in the entire 1,414-line document: the Status line and the entry, which are the two sentences asserting the addition. No axiom statement, no Sidrat clause, no Section 22.4 heading exists anywhere in the body. `AUDIT_CONTEXT.txt` states the section is deferred to v0.64. `METHODOLOGY.txt` Section 10 records Bearer 6 as FALSE with the reason "not in body." **The dispatch layer told the truth; the sealed artifact did not.** Bearer 6, a FROZEN precondition, is claimed satisfied on bytes that leave it unsatisfied.
- **Disposition:** OPEN. Either land Section 22.4 with the five axiom statements and the Sidrat clause as body text, or strike both claim sentences. No gate compares entry claims about body content against the body; adding one would close this class, not this instance.
- **Cross-reference:** Novel at R22. Same mechanism class as R21 Surface 2 (`source_finding_id` claimed added, absent from code) and R18 Defect 4 (CLOSED-via-repair label false when nothing was implemented). Third recurrence of the promise-stated-as-done class.

---

**F-S04-63-02** HIGH -- Class A -- Noted-array `convergence_group` is not validated; the code path raises `UnboundLocalError`

- **Locus:** `xz_protocol_register_gen.py`, noted-validation loop referencing `declared_group_ids` at approximately line 156; the name is bound at approximately line 172. Claim at `xz_protocol_v0_63.md:5` and `:1396`.
- **Substance:** The entry claims "noted-array `convergence_group` validated identically to `findings[]` [TESTED: probe J must now reject]." The noted loop reads `if ncg is not None and ncg not in declared_group_ids`, but `declared_group_ids` is assigned fourteen lines later in the CROSS-LAYER VALIDATION block. Python short-circuits the conjunction, so the unbound name is never reached while every shipped noted entry carries `convergence_group: null` -- which all four do. Probe J (dangling group 99) therefore appears to reject, but rejects via `UnboundLocalError: cannot access local variable 'declared_group_ids' where it is not associated with a value`, not via the specified fail-closed `ValueError`. **Probe J2 is decisive:** a noted entry referencing the *valid* group 1 also crashes. `findings[]` accepts that same value. The two validations are not identical; the noted validation cannot perform a membership test under any input. The claim is byte-false, and the repair is a dead code path that has never executed.
- **Disposition:** OPEN. Move the `declared_group_ids` assignment above the noted loop and re-run probes J and J2. J must reject with `ValueError`; J2 must be accepted.
- **Cross-reference:** R21 Surface 4 (`F-S02-62-09F`, `F-S03-62-05`), dispositioned CLOSED in the v0.63 register item (4). The repair did not land. Refutes dispatch prediction P4.

---

**F-S04-63-03** HIGH -- Class A -- Four-scribe tagging discipline not deployed; one scribe entirely absent

- **Locus:** v0.63 entry narrative paragraph, `xz_protocol_v0_63.md:1396`; claim at `:5` ("Four-scribe tagging discipline deployed"); specification at `METHODOLOGY.txt` Section 11.
- **Substance:** Section 11 states "Every sentence in the amendment entry carries one tag" and "Zero untagged sentences." Five of the nine narrative sentences carry no tag: the Class A recurrence and H = 1.0 sentence; "Seven convergent defect surfaces."; the narrative-counts-removed sentence; the Section 22.4 sentence; and the methodology-version sentence. Separately, the census returns **zero `[WITNESSED]` tags** across the entire entry. The Witness -- CI-1R, PRIOR_HISTORY, carrying-seat verdict -- is one of the four scribes, and no claim in the entry cites it. A four-scribe discipline shipped with one scribe unused and 56% of the narrative untagged is not deployed.
- **Disposition:** OPEN. Tag every narrative sentence or restate the deployment claim as partial with the untagged count stated.
- **Cross-reference:** R21 Surface 7 (`F-S02-62-06F`), the methodology's own predicted class-fix surface. Predicted at `METHODOLOGY.txt` Section 7 as the Level 4 defect. Confirmed present, but not exclusively -- see F-S04-63-01.

---

**F-S04-63-04** HIGH -- Class A -- `[TESTED]` tags cite probes that do not exist in the packet

- **Locus:** v0.63 entry, four tags: `[TESTED: probe G/P-3 must now reject]`, `[TESTED: probe H must now reject]`, `[TESTED: probe J must now reject]`, `[TESTED: probe K must now reject]`.
- **Substance:** `METHODOLOGY.txt` Section 11 defines `[TESTED: test_id]` as "The Test -- a probe falsified the negation." Three independent facts falsify all four tags. First, no probe named G, H, J or K exists in any shipped file; grep across all six test suites and all six code modules returns zero matches. Second, `xz_protocol_register_gen.py` -- the module all four repairs live in -- is referenced by none of the 186 tests and is not imported by `build.py` (see F-S04-63-13), so no shipped test can have exercised any of them. Third, the tag text is a future-tense imperative, "must now reject," which is a prediction, not a record of a falsification that occurred. A `[TESTED]` tag whose content is an instruction to a future auditor is the tagging-metadata Class A the methodology predicted, in its purest form. The probes were in fact run -- by this seat, this round -- and probe J's result contradicts its own tag.
- **Disposition:** OPEN. Either ship probes G, H, J and K as executable tests inside the pytest suite and re-tag with real test IDs, or downgrade all four to `[ASSERTED]`.
- **Cross-reference:** R21 Surface 7 (`F-S02-62-06F`), same class. Related to F-S04-63-13.

---

**F-S04-63-05** HIGH -- Class A -- Narrative count claims not removed; surviving count contradicts the COMPUTED register

- **Locus:** v0.63 entry narrative, `xz_protocol_v0_63.md:1396`; register header in the same entry; `r21_findings_index.json` `convergence_groups`.
- **Substance:** The entry states "Narrative seat/finding count claims removed from entry (only COMPUTED register brackets retained)." In the same paragraph, two sentences earlier, stands "**Seven** convergent defect surfaces." The COMPUTED register header, generated from the shipped index, reads "R21 defect register disposition (from R21 four-seat audit, **5 items**)," and the index declares exactly five `convergence_groups`. The two remaining R21 surfaces became non-converging NOTED singletons with `convergence_group: null`; calling them convergent is false against the index. The word "convergent" is load-bearing, and this is the precise defect class the sentence claims to have eliminated, surviving inside the claim of its own elimination.
- **Disposition:** OPEN. Strike "Seven convergent defect surfaces" or restate as "five convergent groups and two non-converging noted findings," and extend gate `[10g]` to compare narrative cardinals against index cardinality.
- **Cross-reference:** R21 Surface 5 (`F-S01-62-05`, `F-S02-62-01F` through `-04F`), dispositioned CLOSED in v0.63 register item (5). Recurrence, second consecutive round.

---

**F-S04-63-06** HIGH -- Class A -- Laplace column in the canonical methodology is wrong in six of eight rows

- **Locus:** `METHODOLOGY.txt` Section 15, "Class A Recurrence" table, Laplace P column.
- **Substance:** Laplace succession with s = n gives P = (n+1)/(n+2). Recomputed against the table's own convention -- fixed by the two rows that are correct and by the entry's own "P(R22) = 16/17 = 0.9412" -- the column should read R16 0.9167, R17 0.9231, R18 0.9286, R19 0.9333, R20 0.9375, R21 0.9412. The table states 0.917, 0.917, 0.923, 0.929, 0.933, 0.941. Rows R17 through R20 are each computed with n one lower than the round warrants, a uniform one-round lag. The two range rows are wrong at both endpoints: R7-R12 is stated as 0.875-0.917 against a true 0.667-0.875, and R13-R15 as 0.875-0.900 against a true 0.889-0.909. Only R16 and R21 are correct. This is a numeric claim in the document `METHODOLOGY.txt` declares "canonical for all audit rounds from R22 onward," and the figure is described in the R21 seat reports as load-bearing for the trajectory argument rather than cosmetic.
- **Disposition:** OPEN. Recompute the column from a single stated convention and state the convention in the table caption.
- **Cross-reference:** Novel at R22. Same class as R15 Defect 2 (severity transposition) and R14 Defect 2 (convergence undercount): an ungated hand-written numeric surface. Instance of the methodology-lag surface `AUDIT_CONTEXT.txt` discloses.

---

**F-S04-63-07** HIGH -- Class A -- H = 1.0 is asserted for a statistic the governing CI specification formally retired as undefined

- **Locus:** `xz_protocol_v0_63.md:1396` (sealed entry); `METHODOLOGY.txt` Section 1 and Section 15 (H column, all eight rows); `DISPATCH.txt` P15. Retirement at `CI_METHODOLOGY.txt`, CI-5.
- **Substance:** CI-5 records that S01 at R15 and two R14 seats demonstrated R/S is undefined (0/0) on the constant R7-R15 series, that CI v0.2 replaced the Hurst statistic with recurrence fraction and Laplace-smoothed probability, and that the "H < 0.5" target was restated as "first round with zero Class A findings." Recomputed on the Class A indicator series for R7-R21, which is fifteen ones: mean 1.0, cumulative deviation range R = 0.0, standard deviation S = 0.0, R/S = 0/0. The Hurst exponent is not 1.0. It is not computable. `METHODOLOGY.txt` Section 1 nevertheless opens with "The Hurst exponent H = 1.0 across the entire series indicates maximally persistent autocorrelation," carries H = 1.0 in every row of the Section 15 table, and the value is repeated inside the sealed v0.63 entry. A retired statistic was reintroduced across three documents without receipt, and it is the headline quantitative claim of the canonical methodology's central empirical result.
- **Disposition:** OPEN. Strike H from the entry, from Section 1 and from the Section 15 table, or restate as "R/S undefined on a constant series; recurrence fraction 15/15" with the CI-5 retirement cited.
- **Cross-reference:** `CI_METHODOLOGY.txt` CI-5 and F-CI-1 reformulation. Refutes the statistical half of dispatch prediction P15; the Class A half of P15 is confirmed.

---

**F-S04-63-08** MEDIUM -- Class A -- Gate count claim is one higher than the measured count

- **Locus:** `AUDIT_CONTEXT.txt`, "Build status" block: "build.py: 258 PASS, 0 FAIL."
- **Substance:** `python3 build.py` executed in a pristine directory containing exactly the 20 packet files under Python 3.12.3 emits **257** lines matching `^  PASS: ` and zero FAIL. The count is deterministic across repeated runs and unaffected by directory contents. `build.py` contains no skipped or conditional gates on the all-green path. The claim is off by one on the shipped bytes.
- **Disposition:** OPEN. Compute the figure from build output rather than stating it, or correct to 257.
- **Cross-reference:** R18 NOTED group, "Gate count 222/261/264 documentation inconsistency" (`F-S01-58-03`, `F-S02-58-04`, `F-S04-58-06`, `F-S05-58-05`) and R19 NOTED "Gate count documentation inconsistency (recurring since R14)." Sixth recurrence of a class NOTED five times and never repaired. Elevated from NOTED to Class A here because at R21 the dispatch layer was proven to be a live Class A surface, and this instance is in the dispatch.

---

**F-S04-63-09** MEDIUM -- Class A -- Triage convergence header contradicts its own enumeration and the index

- **Locus:** `R21_TRIAGE.txt`, Surface 2 header; `r21_findings_index.json` group 2.
- **Substance:** The header reads "**Convergence: 3/4 seats (S01, S02, S03)**." The four bullets immediately below it enumerate S01, S02, S03 **and S04** (`F-S04-62-02` HIGH). The findings index group 2 carries four `finding_ids` spanning four distinct seats, and the index's own `triage_adjudication` for that group states "4/4 seats converged." The header is false against its own body list, against the index, and against the index's adjudication text. This is a direct CI-2 crystallographic violation -- a count claim whose enumeration sits in the same text and disagrees with it -- in the document that is the source of truth for register generation.
- **Disposition:** OPEN. Correct the header to 4/4. Extend CI-2 verification to triage documents, which are currently ungated.
- **Cross-reference:** CI v0.1 constraint I1 and CI-2 (`CI_METHODOLOGY.txt` Sections 0.1, 6). Same class as R14 Defect 2 (convergence undercount).

---

**F-S04-63-10** MEDIUM -- Class A -- CI-8 severity divergence propagates into a `[COMPUTED]` register line

- **Locus:** `r21_findings_index.json`, `unique_findings_noted` record `F-S01-62-10`, `source_severity: "MEDIUM"`; `R21_REPORTS.txt:304`, "**F-S01-62-10** LOW -- Class B".
- **Substance:** CI-8 requires that `source_severity` in the index match the severity stated in the originating seat report. S01's R21 report states LOW. The index records MEDIUM. No `adjudication_receipt` accompanies the divergence, and noted entries carry no receipt field at all. `generate_register` copies the field faithfully, so the shipped register emits "`- [F-S01-62-10] MEDIUM: ...` [COMPUTED: generate_register]" -- a false severity inside a claim tagged as code-produced. Mechanical scan of all 23 index finding IDs against `R21_REPORTS.txt` found 23 of 23 IDs present and exactly this one severity divergence. The generator is not at fault; the input is false and no gate covers noted-array severity fidelity against source reports.
- **Disposition:** OPEN. Correct the index record to LOW, or supply an `adjudication_receipt`. Extend severity-fidelity validation to `unique_findings_noted`.
- **Cross-reference:** CI-8 (`CI_METHODOLOGY.txt` Section 6). Same class as R15 Defect 2 (severity transposition), which gate `[10d]` was built to eliminate for `findings[]` only.

---

### Class B -- concealed defect, HALT-grade

---

**F-S04-63-11** HIGH -- Class B -- The v0.63 entry lies entirely outside the FULL_SECTION_27 seal

- **Locus:** `xz_protocol_v0_63.md:1392` (Provenance marker), `:1394` (v0.62 terminal line), `:1396` (v0.63 entry start); `build.py` `_full_seal()`.
- **Substance:** `_full_seal()` truncates Section 27 at the literal `*Provenance and review status.*` and hashes everything before it. Recomputed FULL_SECTION_27 matches the value in `HISTORY.sha256` exactly, so the seal is internally correct. But the v0.63 entry was appended **after** the Provenance marker and after the surviving v0.62 terminal line. Measured: **62 of 63 amendment entries fall inside the sealed region; the v0.63 entry, 7,506 bytes, falls entirely outside it.** The v0.62 entry is inside, which establishes that every prior round placed the new entry before the marker and that v0.63 is the first to break the pattern. FULL_SECTION_27 now certifies Section 27 as of v0.62. The entire class-fix entry -- register, boundary list, four-scribe tags, the Section 22.4 claim -- is outside the one seal that covers the amendment record as a whole. The entry does not disclose this, which is what makes it Class B rather than Class C. **Mitigation, stated for accuracy:** the `ENTRY_v0.63` seal and `PACKET_SHA256SUMS` both cover the bytes, verified by mutation probe S-1, which falsified a claim inside the entry and was caught by both. Detection is not lost. Seal scope is reduced, silently.
- **Disposition:** OPEN. Move the v0.63 entry above the Provenance marker, delete the stale v0.62 terminal line, recompute FULL_SECTION_27. Add a gate asserting that the highest-numbered entry falls inside the sealed region.
- **Cross-reference:** Standing boundary item 6, "seal terminus at Provenance marker." The boundary discloses the terminus; it does not disclose that entries would be appended past it. Related to F-S04-63-12.

---

**F-S04-63-12** MEDIUM -- Class B -- Orphan terminal tag and surviving prior-version terminal line

- **Locus:** `xz_protocol_v0_63.md:1394` and `:1413-1414`.
- **Substance:** Two artifacts. First, the final line of the document is a single leading space followed by `[COMPUTED: generate_terminal_line]`, attached to no content -- a scribe tag claiming production of the empty string. `generate_terminal_line` produces exactly one line and the tag appears twice in the entry. Second, `*End of XZ Protocol v0.62 draft candidate.*` survives at line 1394, so the document contains two terminal lines, the earlier one mid-document. Prior rounds evidently replaced the terminal line; v0.63 appended a new one without removing the old.
- **Disposition:** OPEN. Delete the orphan tag line and the v0.62 terminal line; add a gate asserting exactly one `End of XZ Protocol` line and that its version equals VERSION.
- **Cross-reference:** R15 Defect 3 (terminal version staleness), which gate `[10h]` addressed for the version token but not for line uniqueness or orphan tags. Same root placement error as F-S04-63-11.

---

### Class D -- gate limitation, non-blocking

---

**F-S04-63-13** HIGH -- Class D -- The module carrying all four class-fix repairs is exercised by nothing in the packet

- **Locus:** `xz_protocol_register_gen.py`; `build.py`; all six test suites.
- **Substance:** Grep across the packet returns `register_gen` or `generate_register` in exactly four files: the module itself, `PACKET_SHA256SUMS`, `r21_findings_index.json` (prose) and `xz_protocol_v0_63.md` (prose). It appears in **no test suite** and is **not imported by `build.py`**, which mentions "register" fourteen times but only ever parses register *text* out of the protocol document. The consequence is structural: the 186 GREEN tests and the 257 build gates, which are the evidence for Bearer 2, do not reach a single line of the code this round exists to repair. CI-1R is an auditor-run probe with no build-time gate behind it. F-S04-63-02's unbound-name defect survived precisely because no execution path ever reached it. A class fix housed in an unexercised module is one edit away from silent regression at any future round.
- **Disposition:** OPEN. Add a test suite for `xz_protocol_register_gen.py` covering probes G, H, J, J2, K, K2 with landed assertions and benign controls, and add a CI-1R gate to `build.py` that regenerates the register and compares it to the shipped entry at build time.
- **Cross-reference:** Explains F-S04-63-02 and F-S04-63-04. Bearer 2 evidence scope. Novel at R22.

---

**F-S04-63-14** MEDIUM -- Class D -- Seat validation landed for `findings[]` only; noted array still accepts undeclared seats

- **Locus:** `xz_protocol_register_gen.py`, CROSS-LAYER VALIDATION block, item 0.
- **Substance:** The seat check iterates `findings` and compares each `seat` against `declared_seats`. The `unique_findings_noted` array is not iterated for the seat field. Probe K rejected `S99Z` on a `findings[]` record; probe K2 set `seat = "S99Z"` on a noted record and generation **completed normally**. The repair covers half the surface the R21 finding described.
- **Disposition:** OPEN. Apply the same membership check inside the noted-validation loop.
- **Cross-reference:** R21 NOTED `F-S02-62-11F`, dispositioned CLOSED. Partially landed. Same half-surface pattern as F-S04-63-10.

---

**F-S04-63-15** MEDIUM -- Class D -- The governing CI specification for v0.3 through v0.3.3 is absent from the packet

- **Locus:** `CI_METHODOLOGY.txt`; `METHODOLOGY.txt` Section 4, Layer 2.
- **Substance:** `METHODOLOGY.txt` declares Layer 2 "Governed by CI v0.3.3 specification." The packet's `CI_METHODOLOGY.txt` is titled "Version 0.2" and terminates in a v0.2.1 upgrade appendix. Grep for `v0.3` in that file returns zero matches. Four specification generations -- v0.3, v0.3.1, v0.3.2, v0.3.3 -- are named as governing and shipped nowhere. `AUDIT_CONTEXT.txt` lists v0.3.3's changes in seven bullets, which is a changelog, not a specification. A seat cannot verify the register generator against its governing spec because the spec is not in the ten-file packet. This weakens every CI-numbered probe from CI-2 through CI-8 to verification against a changelog.
- **Disposition:** OPEN. Ship the CI v0.3.3 specification as file 10 of the packet, or restate Layer 2's governing document as the v0.2.1 spec plus the shipped changelog.
- **Cross-reference:** `METHODOLOGY.txt` Section 12, ten-file packet table. R18 NOTED `F-S02-58-03`, "CI_METHODOLOGY schema inconsistency," same document, third round unrepaired.

---

**F-S04-63-19** LOW -- Class D -- CI-4 metric basis remains undefined; P6 resolves differently on each basis

- **Locus:** `CI_METHODOLOGY.txt` CI-4; v0.63 entry.
- **Substance:** ASSERTED fraction measured two ways: **4.8%** on a tag-count basis (1 of 21 tags) and **20.4%** on a character-share basis (narrative 1,356 of 6,653 chars). The CI v0.2 target is "under 15%." Dispatch prediction P6 is confirmed on the first basis and refuted on the second. The basis has been an open NOTED item since R18 and remains unspecified, so F-CI-2's satisfaction condition is not decidable on shipped bytes.
- **Disposition:** OPEN. Fix the basis in the CI specification and state it in the entry alongside the figure.
- **Cross-reference:** R18 NOTED `F-S02-59-04F` ("CI-4 metric ambiguity: tag-count vs character-share basis undefined") and `F-S02-59-04C`. Third round unrepaired.

---

### Class E -- process observation, non-blocking

---

**F-S04-63-16** HIGH -- Class E -- Seat-conformance breach: producer family occupying a barred non-producer seat

- **Locus:** `DISPATCH.txt` header; `METHODOLOGY.txt` Section 5 seat table; `xz_protocol_v0_63.md:702` (Section 22.1 producer definition).
- **Substance:** The dispatch assigns S04 to Gemini 3.1 Pro with the trial condition "no code execution, textual only," and marks the producer, Claude Opus 4.6, BARRED. This seat was executed by Claude Opus 5 with a live execution sandbox. The evidence produced is Tier 1 rather than the Tier 2 the earth was dispatched to produce, and R22 has no Gemini witness. Axiom A-X3, model non-collusion, is the assumption that makes convergence across seats mutawatir evidence; it is not satisfied for this seat. Axiom A-X5, dispatch integrity, is directly implicated because the packet asserts a seat assignment the executing instance does not satisfy. Under `METHODOLOGY.txt` Section 5, the findings above retain their evidential weight -- "no advantage from world, only deeds and truth" -- but carry no governance weight beyond advisory.
- **Disposition:** OPEN. Confirm the family routing of all R22 seats before triage. If more than one seat was mis-routed, the R22 convergence counts are not mutawatir and Bearer 5 cannot be assessed from this round.
- **Cross-reference:** `METHODOLOGY.txt` Section 9, axiom set A-X3 and A-X5. R21 Surface 6 established the dispatch as a live defect surface. Novel at R22.

---

**F-S04-63-17** MEDIUM -- Class E -- Dispatch carries fifteen pre-stated predictions, exceeding its declared content specification

- **Locus:** `DISPATCH.txt`, PREDICTIONS block P1 through P15 and closing question.
- **Substance:** `METHODOLOGY.txt` Section 12 specifies that `DISPATCH.txt` is "Unique (identity only)" and differs across seats "ONLY in seat number, family, and role -- NOT in framework, NOT in methodology, NOT in probe targets." The shipped dispatch carries fifteen predictions with stated confidence levels, including P7, which pre-states **where** any Class A should be found ("in tagging metadata or methodology-lag"), and P15, which pre-states the expected verdict ("H = 1.0 continues, Class A present"). Telling a fresh seat the expected answer and the expected locus before it opens the artifact is a confirmation-bias channel, and it is exactly the channel a fresh-seat architecture exists to eliminate. This seat's two heaviest findings, F-S04-63-01 and F-S04-63-02, fall outside the loci P7 nominated, which is some evidence the anchoring did not fully bind -- but the channel is open regardless.
- **Disposition:** OPEN. Move predictions out of the dispatch and into a sealed pre-registration held by the triage author, opened only after all seat reports arrive.
- **Cross-reference:** `METHODOLOGY.txt` Section 12; `al-Lawh al-Mahfuz` correspondence in Section 16, which is precisely a sealed pre-registration. Novel at R22.

---

**F-S04-63-18** LOW -- Class E -- Output filename specified two ways in one packet

- **Locus:** `DISPATCH.txt` OUTPUT block; `AUDIT_CONTEXT.txt` "Output requirement."
- **Substance:** The dispatch specifies `XZ_v063_R22_S04__REPORT.md`; `AUDIT_CONTEXT.txt` specifies `XZ_v063_R22_{SEAT_ID}_{FAMILY}_REPORT.md`. The two templates disagree on separator count and on whether the family token appears. This report follows the dispatch, which is the more specific instruction.
- **Disposition:** OPEN. Reconcile to one template.
- **Cross-reference:** `METHODOLOGY.txt` Section 12. Novel at R22.

---

**F-S04-63-20** LOW -- Class E -- Section 22 subsections are out of order

- **Locus:** `xz_protocol_v0_63.md:702` (22.1), `:708` (22.3), `:718` (22.2).
- **Substance:** Subsection 22.3, added v0.33, precedes subsection 22.2, added v0.20, in document order. Non-substantive, but it is the ordering context into which a Section 22.4 would be inserted, and it makes the absence of 22.4 harder to spot by eye.
- **Disposition:** NOTED. Reorder when Section 22.4 lands.
- **Cross-reference:** F-S04-63-01. Novel at R22.

---

## S8. Barzakh gate self-check

Three questions applied to this seat's own findings before submission.

**Who is your Lord? (Authority.)** Every finding above cites executed tool output: probe results with exception types, recomputed hashes, grep counts, line numbers, recomputed arithmetic. Tier 1 throughout. No finding rests on assertion. The one place this seat asserts rather than computes is the interpretation in F-S04-63-16 of what the conformance breach implies for A-X3, which is reasoning, not measurement, and is labelled as such.

**What is your religion? (Methodology.)** Each finding names its layer, and the evidence meets that layer's Tier standard. L1 and L2 findings are execution results. L3 findings are byte-level comparisons between two shipped surfaces. L4 findings are probe outcomes with benign controls (the unmutated index accepted; probe J2 and K2 are the controls that convert probe J and probe K from apparent passes into findings). L6 and L7 findings are recomputations against the shipped specification documents.

**Where does this come from? (Lineage.)** Ten of twenty findings are recurrences with the prior instance cited and the reason the repair failed stated. F-S04-63-02 recurs because the repair was written into a module nothing executes. F-S04-63-05 recurs because no gate compares narrative cardinals to index cardinality. F-S04-63-08 and F-S04-63-19 recur because they were dispositioned NOTED rather than repaired, five and three rounds ago respectively. Ten findings are novel at R22, of which F-S04-63-01, F-S04-63-11 and F-S04-63-13 are the substantive ones.

**Findings rejected by this seat's own gate: none.** One candidate was set aside rather than filed: the `[COMPUTED: build.py]` occurrence inside the v0.63 entry sits within the quoted substance of R21 finding `F-S02-62-06F`, not on a live claim. That is standing boundary item 17, quoted-tag inflation, operating as disclosed. It is not a finding.

---

## S9. Prediction scorecard

| # | Prediction | Outcome |
|---|---|---|
| P1 | CI-1R PASS, byte-exact register | **CONFIRMED** -- register, boundary list and terminal line all byte-exact |
| P2 | Probe G rejects | **CONFIRMED** -- `ValueError`, exact equality |
| P3 | Probe H rejects | **CONFIRMED** -- `ValueError`, both directions |
| P4 | Probe J rejects | **REFUTED IN SUBSTANCE** -- rejects via `UnboundLocalError`; probe J2 shows valid input also crashes |
| P5 | Probe K rejects | **SPLIT** -- confirmed for `findings[]`, refuted for the noted array (K2 accepted) |
| P6 | ASSERTED under 15% | **SPLIT** -- 4.8% tag-count, 20.4% character-share; basis undefined |
| P7 | Class A only in tagging or methodology-lag | **REFUTED** -- F-S04-63-01 is a body-content claim, F-S04-63-02 is substrate code |
| P8 | Count-list invariant holds | **CONFIRMED** -- probe S-6 caught the bracket mutation |
| P9 | Append-only holds, 63/63 seals | **CONFIRMED** -- with the scope reduction at F-S04-63-11 |
| P10 | Code layer clean, 186 GREEN | **CONFIRMED** -- and see F-S04-63-13 on what 186 GREEN does not cover |
| P11 | Packet 19/19 OK | **CONFIRMED** |
| P12 | VERSION-1 gate catches stale bounds | **CONFIRMED** -- probe S-3 |
| P13 | Section 22.2/22.3 at v0.62 | **CONFIRMED** -- "v0.1 through v0.62" and "v0.38-v0.62" |
| P14 | Extraction snippet yields 19/19 verbatim | **CONFIRMED** |
| P15 | H = 1.0 continues, Class A present | **SPLIT** -- Class A confirmed; H = 1.0 refuted as a statistic (F-S04-63-07) |

**Nine confirmed outright, three split, two refuted, one confirmed with material qualification.** The two refutations are P4 and P7 -- the two predictions the round was designed to test.

---

## S10. Verdict, bearers, and the Goedel confinement question

### Bearer assessment (BSSG three-valued logic; UNKNOWN is never satisfied, FALSE dominates)

| Bearer | R21 | R22 | Basis |
|---|---|---|---|
| 1. Append-only integrity | TRUE | **TRUE** | 63/63 entry seals recompute; S-1 and S-4 detected. Scope reduction at F-S04-63-11 disclosed here, not by the entry |
| 2. Code-layer correctness | TRUE | **TRUE** | 186 GREEN, 257 PASS, no regression. Evidence does not reach `register_gen.py` (F-S04-63-13) |
| 3. Defect-surface narrowing | TRUE | **TRUE** | Four of seven R21 surfaces fully discharged; three probes now reject that previously landed |
| 4. Goedel confinement | FALSE | **FALSE** | F-S04-63-01 and F-S04-63-02 are outside the self-referential surface |
| 5. Cross-vendor witness | FALSE | **FALSE** | No non-HALT carrying verdict, and this seat is not the family it was dispatched as (F-S04-63-16) |
| 6. Axiom disclosure | FALSE | **FALSE** | Section 22.4 absent, and now falsely claimed present (F-S04-63-01) |
| 7. Methodology verification | UNKNOWN | **FALSE** | **Regression.** Four false `[TESTED]` tags and 5 of 9 untagged sentences proven (F-S04-63-03, F-S04-63-04) |
| 8. The furqan | UNKNOWN | **UNKNOWN** | Pending Bearers 1 through 7 |

**State: 3 TRUE, 4 FALSE, 1 UNKNOWN.** Bearer 7 regressed from UNKNOWN to FALSE, because the tagging discipline shipped and was measured for the first time and did not hold. FROZEN requires all eight TRUE.

### The Goedel confinement test

`AUDIT_CONTEXT.txt` states the test plainly: Class A only in tagging or methodology-lag means confinement achieved; Class A in code means the class fix is incomplete.

**Confinement is not achieved, on both arms of the test.**

Class A is present in the tagging, as predicted -- F-S04-63-03 and F-S04-63-04 are exactly the surface `METHODOLOGY.txt` Section 7 said the defect would migrate to. Class A is also present in methodology-lag, as disclosed -- F-S04-63-06 and F-S04-63-07 live in `METHODOLOGY.txt` itself. Had the round produced only those four, the answer would be yes.

It did not. **F-S04-63-01** is a claim that the protocol body contains a section the protocol body does not contain, and the section in question is the one that would satisfy Bearer 6. **F-S04-63-02** is a code-level validation that cannot execute, in the module the round was built to repair. Neither is self-referential. Neither is a tag. The first is a false claim about the artifact's own content; the second is a defect in the substrate, which is where the class fix was supposed to have stopped occurring.

### The honest statement

The four scribes are perfect for the sixteenth consecutive round. Nineteen digests verify, 186 tests pass, 257 gates pass, 63 seals recompute, CI-1R is byte-exact, and five of five sabotage mutations were caught. The mechanism has not erred.

Three of the four code repairs landed and are provable by probe. The extraction defect that made R21's dispatch byte-false is closed and verified verbatim. The `source_finding_id` overclaim is genuinely removed. The defect surface continues to narrow.

What did not happen is confinement. The round's own instrument -- the four-scribe tagging discipline -- was deployed for the first time and can be measured for the first time, and it does not hold: one scribe is unused, five of nine sentences are untagged, and four tags cite probes that do not exist in the packet. Underneath that, one repair is a dead code path and one section is claimed present and is absent.

The most instructive fact in the round is not any single finding. It is that `AUDIT_CONTEXT.txt` and `METHODOLOGY.txt` Section 10 both state, correctly and without hedging, that Section 22.4 is not in v0.63 -- while the sealed protocol says it is. The dispatch layer told the truth. The artifact did not. Iblis did not this time find a gap between the mechanism and the claim about the mechanism. He found a gap between two of the producer's own documents, and moved into the one that is sealed.

**Does v0.63 break the R7-R21 Class A streak? No. 16/16. H is not computable; the recurrence fraction is 1.0; Laplace P(Class A at R23) = 17/18 = 0.9444.**

### Minimum repairs for v0.64

1. Land Section 22.4 with the five axiom statements and the Sidrat clause as body text, or strike both claims (F-S04-63-01).
2. Bind `declared_group_ids` above the noted-validation loop; probe J must reject with `ValueError` and probe J2 must be accepted (F-S04-63-02).
3. Ship probes G, H, J, J2, K, K2 as executable tests; add a CI-1R build gate (F-S04-63-04, F-S04-63-13).
4. Tag every narrative sentence; use the Witness scribe or state why it is unused (F-S04-63-03).
5. Strike "Seven convergent defect surfaces"; extend `[10g]` to narrative cardinality (F-S04-63-05).
6. Recompute the Laplace column from one stated convention; strike H = 1.0 across all three documents (F-S04-63-06, F-S04-63-07).
7. Move the v0.63 and v0.64 entries above the Provenance marker; delete the stale v0.62 terminal line and the orphan tag; add a gate asserting the newest entry is inside the sealed region (F-S04-63-11, F-S04-63-12).
8. Correct the gate count claim to a computed figure (F-S04-63-08).
9. Correct `R21_TRIAGE.txt` Surface 2 to 4/4 and the index severity for `F-S01-62-10` to LOW (F-S04-63-09, F-S04-63-10).
10. Confirm R22 seat family routing before triage; if more than one seat was mis-routed, R22 convergence is not mutawatir (F-S04-63-16).
11. Move the prediction block out of the dispatch into a sealed pre-registration (F-S04-63-17).
12. Ship the CI v0.3.3 specification in the packet; fix the CI-4 basis (F-S04-63-15, F-S04-63-19).

---

*Seat S04, R22, v0.63. ADVISORY -- no verdict binds. Executed 2026-08-17.*
*All findings Tier 1 (executed tool output). All findings passed this seat's Barzakh gate. None rejected.*
*Seat conformance breach declared at S0 and filed as F-S04-63-16. Weigh accordingly.*
*BayyinahEnterprise Structural Honesty Validation Program.*

---

# Bismillah ir-Rahman ir-Rahim
