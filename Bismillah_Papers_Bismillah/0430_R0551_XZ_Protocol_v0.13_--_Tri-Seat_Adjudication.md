# Bismillah ir-Rahman ir-Rahim

# R0551 -- XZ Protocol v0.13 -- Tri-Seat Adjudication

**Chronological Index:** 430 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** ADJUDICATION_v13.md  
**Source Format:** md  
**SHA-256:** `8c9e203831c9c2a1d3cbe2bd2eb6f63055a3fe566c9051051bcb373d4a8bd57c`  

---

## R0551 · XZ Protocol v0.13 -- Tri-Seat Adjudication

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: ADJUDICATION_v13.md
- source_format: md
- text_sha256: 8c9e203831c9c2a1d3cbe2bd2eb6f63055a3fe566c9051051bcb373d4a8bd57c

# XZ Protocol v0.13 -- Tri-Seat Adjudication

**Prepared by:** Claude Opus 5, producer of record for v0.13
**Date:** 2026-08-01
**Audited artifact:** XZ Protocol v0.13, packet `XZ_v13_CARRY_DISPATCH.zip`, 22 canonical files, manifest digest `52c67f4842836dc4f578bb2bdb9515bb751b7337ebad56607641f9499c39443e`
**Seats reporting:** GLM-5.2 (Zhipu/Z.ai), GPT, Kimi K3 (Moonshot)

---

## 0. Standing on this document

This is not an audit. I authored v0.13, including the five gates that most of the findings below concern, so I am barred from auditing it. What follows is the producer doing three things the producer is permitted and obliged to do: verifying that each seat audited the bytes that were shipped, reproducing every reported defect against those bytes before absorbing it, and adjudicating between seats where they disagree.

Every quantitative claim below is reproducible from `producer_reproduction/reproduce_all.py`, which ships in this packet and runs against `audited_package/`.

---

## 1. Seat governance

| Seat | Family | Carry eligibility | Verdict returned |
|---|---|---|---|
| GLM-5.2 | Zhipu/Z.ai | **Carrying seat 1/2** | CONDITIONAL PASS, F1-F15 + I1-I4 |
| Kimi K3 | Moonshot | **Carrying seat 2/2** | none -- run ended before task item 6 |
| GPT | OpenAI | **Not eligible** -- self-disqualified in v0.6 audit F-XZ06-GPT-04, accepted in v0.7 | "not carry-clean, not gate-hardened", F-AUD-01..06 |

GPT's ineligibility bears on whether its report counts toward FB-7b. It bears on nothing else. Record over person: a finding is real or it is not, and its author's seat status has no effect on that. On severity calibration GPT was the most accurate of the three seats, for reasons given in section 5.

**FB-7b is not met.** Kimi issued no verdict. But chasing that verdict would not change the outcome, and the lead should not spend a second Kimi run on it: the union of the three reports plus the reproduction below establishes ten package-level false-PASS paths, which forecloses CARRY-CLEAN on these bytes regardless of how the missing verdict would have been phrased.

---

## 2. Byte provenance

The strongest form of this check is available for Kimi, which returned its working packet.

- **Kimi:** all 22 packet members are **byte-identical** to the producer build. Kimi's own dispatch manifest verifies 22/22 against the packet it held. Execution residue is present (`__pycache__`, `.pytest_cache/v/cache/nodeids`), the host log shows Linux and Python 3.12.12, and timestamps are consistent. This is a genuine execution on the correct bytes.
- **GLM:** reports SHA-256 22/22 and recomputes the manifest digest to `52c67f48...`, which matches. No packet returned, so provenance is attested rather than substrate-verified.
- **GPT:** reports SHA-256 22/22 and the same digest. Evidence JSONs ship. No packet returned; same attestation level as GLM.

No seat's numbers conflict with the shipped bytes.

---

## 3. Baseline agreement

All three seats independently report the same baseline, and the producer reproduces it:

| Measure | GLM | GPT | Kimi | Producer |
|---|---|---|---|---|
| SHA-256 | 22/22 | 22/22 | 22/22 | 22/22 |
| Canonical suite | 210 passed | 210 passed | 210 passed | 210 passed |
| Five gates | all exit 0 | all exit 0 | all exit 0 | all exit 0 |
| Version-gate self-test | pass | -- | pass | pass |

Kimi additionally verified all three trust-root keys are valid Ed25519 curve points, independently re-derived all 13 amendment-entry seals, and independently re-evaluated all 38 locus-register assertions (0 failing). GLM explicitly declined the key check for want of infrastructure. Neither of the other seats attempted it.

**The baseline is sound and it is not the question.** The question is whether the published verification surface discriminates.

---

## 4. Reproduction result

`reproduce_all.py` applies each reported mutation to a sandbox copy and measures two levels:

- **gate level** -- does the specific gate whose blindness was alleged fire?
- **package level** -- does the entire published surface stay green? All five gates exit 0 **and** the canonical seven-suite invocation passes.

Package level is the level at which v0.13's central claim is stated, so a green package on a materially bad mutation is a false PASS of that claim.

```
BENIGN CONTROL BEHAVED: True
PACKAGE-LEVEL FALSE PASSES (10):
  GPT-02, GPT-03, GPT-04, GLM-F2, GLM-F4, GLM-F1a, GLM-F1b, KIMI-M5, KIMI-P4, KIMI-P5
TARGET GATE BLIND (18):
  the above, plus KIMI-V3, KIMI-V4, KIMI-V5, KIMI-C3, KIMI-P6, KIMI-H5, PROD-01, PROD-02
```

Ten mutations leave a materially bad package indistinguishable from a good one across every published check. Eight further mutations blind the specific gate that is supposed to catch them, and are caught only incidentally by a different gate -- usually the manifest gate noticing that file bytes changed. That incidental catch is real defence in depth and is worth keeping, but it is not the gate doing its job, and it disappears the moment a mutation touches only the protocol text.

The one benign control behaved correctly: the unmutated package is green, as it should be.

---

## 5. Severity adjudication

Three items carry two-band disagreement between seats, which the severity rubric treats as contradiction requiring escalation rather than a producer judgement call.

| Item | GPT | GLM | Reproduced | Adjudicated |
|---|---|---|---|---|
| Manifest gate hex-case gap | CRITICAL | LOW (F9) | package-level false PASS, uppercase and MixedCase | **CRITICAL** |
| Section 27 preamble unsealed | CRITICAL | MEDIUM (F8) | package-level false PASS | **CRITICAL** |
| Condition A forged provenance | CRITICAL | INFORMATIONAL (I2) | forged `BaselineCheckResult` -> `A_ACCEPT` -> `is_primary_seam_divergence` True | **HIGH, inherited** |

The discriminator is method, not judgement. GPT asked "does a materially bad package clear the whole surface". GLM asked "does this gate catch this mutation". The first question is the one v0.13's claim invites, and it produces the better-calibrated severities. GLM's own F2 and F4, which GLM rated HIGH and MEDIUM as gate-level issues, are in fact package-level false passes; GLM undercounted its own findings by measuring at the narrower level.

On the third row I part with both seats on attribution rather than severity. `xz_protocol_condition_a.py` is byte-identical to v0.12 apart from its version stamp. This is carried v0.3-era code, not v0.13 code, and the register should say so. It is a real defect and it is newly surfaced; it is not a regression introduced by the gate rebuild.

---

## 6. Refutations

Two reported findings do not survive verification. Record over person applies to seats, and a refuted finding does not flip a verdict; it is recorded and the seat re-attests on the corrected instrument.

**GLM F15 -- DOI cross-reference discrepancy. REFUTED as an error.** GLM flagged that the protocol cites SHV Method v1.1 as `21450932` and BAF v3.0 as `20046910`, while the BSSG PDF prints `21449063` and `20017335`. GLM lacked Zenodo API access and correctly noted the caveat. Resolved against the API: SHV Method concept is `10.5281/zenodo.21449062`, with `21449063` = v1.0 and `21450932` = v1.1. BAF `20046910` sits under concept `10.5281/zenodo.20017334`, alongside `20017335`. Both flags are version-versus-version under one concept, not wrong records, and the protocol cites the correct version for the name it uses. **A smaller real residue remains:** Section 26.1 records concept DOIs for the BSSG row only, so the Section 26.2 non-collapse discipline is applied unevenly. Reclassified MEDIUM, disposition: add concept DOIs to every row of 26.1.

**Kimi vacuity probe -- REFUTED as a probe artifact.** `probe_suite_vacuity.py` sabotaged the kernel by inverting FALSE-dominance to ALLOW and reported *"suite stayed green on an inverted kernel -- vacuity"*. Reproduced identically:

```
pytest rc=1   tail='12 failed, 198 passed in 10.26s'   ->   SUITE DISCRIMINATES
```

The suite catches the sabotage. The probe's verdict predicate is `ok = returncode != 0 and "failed" in tail`, and stdout returned empty in Kimi's sandbox, so `tail` became `"(no output)"` and the second conjunct failed despite the exit code being correct. The probe design is sound and should be kept as a standing check with an exit-code-only predicate.

---

## 7. Confirmation: PA-Z14 is a vacuous test

Kimi's most consequential finding, confirmed by reproduction:

```
SEED=42  point_in_interval=True  method=BCA  fallback_reason=None
  ->  VACUOUS: guarded assertions never execute
```

`TestPAZ14::test_point_exclusion` in `xz_protocol_phase_a_tests.py` guards every assertion behind `if not r.point_in_interval`. Under the shipped fixture that condition is False, so the test passes while asserting nothing. It cannot fail.

`xz_protocol_phase_a_tests.py` is byte-identical to v0.12 apart from its version stamp, so this is carried v0.2-era code. It has been counted in "185 tests, all GREEN" and now "210 cases" across eleven versions, and no seat found it until a probe went looking for vacuity as such. Kimi's second decision-path failure (PA-Z11 claiming `excludes_zero` on a point interval) is latent and unreachable from the shipped `t2`/`t3`/`t4`/`t7` entry points; recorded, not blocking.

---

## 8. Producer defect

GLM logged this as INFORMATIONAL (I4). It is not, and Kimi independently located the gate hole that permits it (probe M6).

The v0.13 amendment entry states `Manifest digest: 72ab56da50fe9f20...` and adds "(tool-computed, alphabetical, over 18 artifacts)". The true digest, sealed in the trust roots and recomputed by every seat, is `52c67f4842836dc4...`.

Root cause, which is worse than the symptom: the amendment entry was staged into `src/amendment_v0_13.txt` by extracting it from a build **after** `MANIFEST_DIGEST_TOKEN` had already been substituted. The token was gone, so every subsequent rebuild silently preserved the first build's value. The sentence asserting tool-computation is the sentence carrying the hand-frozen number.

No gate catches it because `scan_protocol_digests` treats Section 27 as historical inventory and never resolves it -- an exclusion I wrote.

Adjudicated **HIGH**. GLM's mitigating reasons are correct on impact and wrong on class: this is the exact recurrence the v0.8 durable fix exists to make impossible, and it recurred at the one surface that fix does not reach, in the version whose subject is preventing it, produced by the instance that spent four rounds writing findings about it.

---

## 9. Consolidated register for v0.14

Deduplicated across all three seats and the producer, organised by enabling condition rather than by symptom. Symptom-level absorption is what produced this round's defects; the classes are the unit of work.

| Class | Enabling condition | Instances | Severity |
|---|---|---|---|
| **Predicate normalization** | patterns match raw text rather than a normalized surface | uppercase/MixedCase hex; `Would have`; `Attack Prevention`; `would\nhave`; `attack-prevention`; `[^.]` sentence boundary; "version" spelled out; colon before CLOSED | CRITICAL |
| **Coverage** | digest and scans cover `*.py` only | locus register unsealed and outside the digest; `.txt` invisible to every gate; JSON excluded | CRITICAL |
| **Structural escape hatches** | register keys and markers skip evaluation entirely | `historical`; `delegated_to`; `FIXTURE_MARKER` | HIGH |
| **Seal geometry** | spans begin and end in the wrong places | Section 27 preamble unsealed; version-gate exclusion runs heading to EOF; duplicate version heading leaves earlier entry unpinned | CRITICAL |
| **Scope drift** | docstring obligation exceeds implementation | hazard tokens "anywhere" vs protocol text only; "exactly one stamp" vs stamps-present-only; manifest gate "every protocol-text reference" vs body only | MEDIUM |
| **Producer narration** | Section 27 exempt from digest resolution | v0.13 entry's `72ab56da` mis-narration | HIGH |
| **Inherited code** | v0.2/v0.3-era, untouched by the gate rebuild | Condition A forged provenance; `is_dual_evaluable` partial (v0.8 F3); `PROHIBITED_SHORTCUTS` prose-only (v0.8 F5); **PA-Z14 vacuous test** | HIGH |
| **Citation completeness** | concept DOIs recorded for one row only | Section 26.1 rows other than BSSG | MEDIUM |

The first six classes are mine. The seventh is not, and the register must say so, or v0.14 will absorb a defect list that misattributes its own history.

---

## 10. Disposition

**HALT on v0.13.** Do not deposit, do not freeze, do not attempt a further carry on these bytes.

Recommended sequence for v0.14:

1. **Rebuild gate predicates deny-by-default over a normalized surface.** Case-fold, collapse whitespace, strip hyphenation before matching. A predicate that must enumerate the ways text can be spelled will always lose to the next spelling.
2. **Glob the entire shipped directory into the digest**, not `*.py`. The locus register is load-bearing input to a gate and is currently unsealed.
3. **Remove `historical` and `delegated_to` as evaluation-skipping keys.** Delegation must run the delegate and require it to cover the claim; "historical" must carry a machine-checkable reason or cease to exist.
4. **Seal the whole Section 27 span**, not per-entry blobs keyed by version, and resolve digests inside it against a recorded historical allowlist rather than exempting it wholesale.
5. **Add a standing vacuity sweep.** For each test file, sabotage a dependency and require the file to fail. PA-Z14 survived eleven versions because nothing ever asked whether a passing test was doing work. This is the single highest-value addition available and it comes from Kimi.
6. **Adopt Kimi's paired-control probe shape as the required format** for all future gate attacks: a discrimination control that must fail, the evasion case, and a benign control that must pass. Kimi ran 36 cases with zero unexpected outcomes; that is a materially better instrument than attacking until something breaks, because it separates a blind gate from a correctly permissive one.
7. **Split specification from implementation.** I specified and implemented the v0.13 gates, and they inherited my blind spots exactly. The gate specifications should be written by one party and implemented by another. Sending the specifications to GLM or Kimi for implementation inverts the arrangement that produced these eighteen blind spots.

I should not author v0.14. I produced v0.13, I wrote the gates that failed, and I have now adjudicated findings against my own work, which is as far as the producer role stretches honestly.

---

## 11. What went right

Recorded because a register of failures is not an accurate account of the round.

- **Three seats, largely disjoint findings.** GPT found the package-level framing. GLM found the regex and register classes and the strongest defence-in-depth confirmation. Kimi found seven evasions nobody else reached, plus the vacuous test and the curve-point validation. The union is far stronger than any single report, and the case for multi-seat carry is now empirical rather than theoretical.
- **The append-only record held.** Section 27 entries v0.1 through v0.12 are byte-identical across the v0.12 and v0.13 packets. After four in-place mutations across v0.4, v0.9 and v0.11, the discipline is holding.
- **The manifest gate's defence in depth is real.** GLM confirmed that re-sealing the trust roots alone does not produce a false PASS, because the body's prose citation goes stale. Eight of the eighteen gate-level evasions are caught incidentally by that mechanism.
- **The kernel is sound.** All three seats independently re-derived the exhaustive 243-vector decision table with zero mismatches. The exact type check and `object.__getattribute__` hardening defeat subclass and descriptor attacks. The remaining `object.__setattr__` mutation is a Python object-model limitation, correctly classified by both GLM and Kimi as undefendable at the dataclass layer.
- **Kimi's probe methodology** is the most valuable single artifact produced this round, more valuable than any individual finding.

---

*Prepared by Claude Opus 5 as producer of record. Not an audit, not a carry, and not peer review. FB-7b remains open.*

---

# Bismillah ir-Rahman ir-Rahim
