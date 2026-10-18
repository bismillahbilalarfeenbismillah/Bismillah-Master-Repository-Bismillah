# Bismillah ir-Rahman ir-Rahim

# R0221 -- XZ Protocol v0.3 — Carrying Audit Report

**Chronological Index:** 61 of 995  
**Date:** 2024-03-29  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v03_CARRYING_AUDIT_REPORT.txt  
**Source Format:** txt  
**SHA-256:** `4b46e308461b19fd344da06c53acf682bdbf7c1ade311822b55f361f84be388d`  

---

## R0221 · XZ Protocol v0.3 — Carrying Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v03_CARRYING_AUDIT_REPORT.txt
- source_format: txt
- text_sha256: 4b46e308461b19fd344da06c53acf682bdbf7c1ade311822b55f361f84be388d

# XZ Protocol v0.3 — Carrying Audit Report

| | |
|---|---|
| **Audit** | XZ Protocol v0.3 — Carrying Audit |
| **Dispatch** | `DISPATCH_XZ_v03_KIMI.txt` (2026-07-31) |
| **Seat** | Seat 2: Kimi K3 (2/2) · Seat 1: GPT-5.6 Sol (parallel) |
| **Audit date** | 2026-08-01 |
| **Corpus** | 13 normative files (7 source modules + 6 test suites), renamed `.txt → .py/.json` per dispatch |
| **Environment** | Python 3.12.12 · numpy 2.4.4 · scipy 1.17.1 (exact golden-vector pin) · pytest 9.1.1, isolated venv |
| **Method** | 5 mandated tasks; attack phase executed by 3 independent adversarial verifier sub-agents (kernel/seam, Phase A numerics, frame/control-graph/trust-roots) plus orchestrator-run novel probes. Every sub-agent finding independently re-verified by the orchestrator before admission. |

---

## VERDICT: **CARRY-CLEAN** — with a carry-forward findings register (no blocking findings)

All five mandated tasks complete:

1. **SHA-256 — 13/13 computed and attested** (Section 1). The packet ships no reference digest manifest (`xz_protocol_trust_roots_PUBLIC.json` carries Ed25519 role keys, not file digests), so this audit records the digest set as the integrity attestation for cross-seat comparison with Seat 1.
2. **Tests — 181/181 GREEN** in the pinned golden-vector environment (Section 2). 14 + 29 + 18 + 25 + 27 + 68 across the six suites; zero failures, errors, or skips.
3. **B-1/B-2 — DISCHARGED** (Section 3), with all four subsidiary v0.2 repairs verified in code. Two *v0.8.4-era* repair claims in the m3 docstring (uniform bool rejection; raw-exception wrapping) are **partially falsified** by adversarial input (findings M-1/M-2) — non-blocking, carried forward.
4. **Attack — executed** (Section 4). 32 consolidated findings: **0 CRITICAL, 3 HIGH, 6 MEDIUM, 15 LOW, 8 INFO**. No finding falsifies the normative decision mathematics under the protocol's declared data-plane threat model; no silent verdict-smuggling path exists through intended data inputs.
5. **Verdict — CARRY-CLEAN** (Section 6). The packet may be carried as the normative reference. The findings register (Section 4.2) is carried forward as recommended v0.3.1 dispositions; none blocks carrying.

**Assurance headline:** the kernel's 243-vector decision logic, the Condition A dominance order, the seam comparison logic, and the BCa numerics all survived *exhaustive* falsification — including a bit-exact independent re-implementation of the Efron BCa (max deviation 1.1e-12) and 1,800 hostile bootstrap runs with zero inverted or NaN intervals.

**Candor headline:** the strongest findings are (H-1) the kernel evaluates through an overridable method (`as_dict()`), so a subclass injection launders any DENY into ALLOW — a code-plane path requiring in-process code execution, out of the declared data-plane perimeter but one line from closure; (H-2) `WithinAuthAssessment` never binds its verdict to its channel edges; (H-3) a single shared fact can satisfy gate T2 through a degenerate zero-resample interval that "excludes zero." All three are fully receipted or protocol-layer-mitigated; none is silent.

---

## 1. Task 1 — SHA-256 integrity attestation (13/13)

Files renamed per dispatch (`.txt → .py/.json`); digests are rename-invariant (byte-identical content). Computed with `sha256sum` in the audit workspace.

| # | File (as executed) | SHA-256 |
|---|---|---|
| 1 | `xz_protocol_kernel.py` | `185a879b275459e2ea20ad355b210a7e742eb850c58552d49bfc0a4287132c3f` |
| 2 | `xz_protocol_condition_a.py` | `b644d67e2b1d538968f93a81942d0ee7b9ef2fbfc787ca5016698dd9ec18b0ac` |
| 3 | `xz_protocol_control_graph.py` | `cf657c00f4109199180b9ca655586cc8ab53529e603c2966053aa8b8e9d92f24` |
| 4 | `xz_protocol_phase_a_intervals.py` | `2d5ac083d67c383e0a5467d375a1845e5ed558bc2fef7f29a3d7888cc0bc5521` |
| 5 | `xz_protocol_phase_a_m3.py` | `66006767bfe807a7b7ce008f83ab5c7dcbf21809a08aba2e0db53774d58af25f` |
| 6 | `xz_protocol_source_frame.py` | `0d6e189a9068daac26b9ebccd9039c09728848c34fc568e9c03c17fa86e1c105` |
| 7 | `xz_protocol_trust_roots_PUBLIC.json` | `100820cbce7987424e4609b13579d9820aaf7d01f021c1d79996f52484096588` |
| 8 | `test_xz_protocol_kernel.py` | `75ad27efaf2482e5d32aaf8974413415084635c115f315d1034a031ed2370053` |
| 9 | `test_xz_protocol_condition_a.py` | `2bb316b325e9cf25e519c31d6b6ddede995e8300bd5da45449fc662b81120774` |
| 10 | `test_xz_protocol_control_graph.py` | `cc8fd9e2663755128e50deb23b6c6a30efcd8e12d50b4b7a19083363fbbfd4f5` |
| 11 | `test_xz_protocol_source_frame.py` | `1e4583743b320f7dad5407c58d81755e08aa75d7029855f66c6c152331963740` |
| 12 | `test_xz_protocol_adversarial.py` | `4140399de285da2e973ac09f75044fed1e9c595983b9c556956fd37952228767` |
| 13 | `xz_protocol_phase_a_tests.py` | `6e198343ec6d1c2f44aa61b381b189cbd0b89b9d7c0852d89004b6d568538e2a` |

**Result: 13/13 digests computed and recorded.** Note for the record: the packet contains no signed manifest of expected digests; the trust-roots file contains the three Ed25519 role public keys (commitment-authority, independent-anchor, run-logger) — all three verified distinct, well-formed 32-byte values, decodable as valid Ed25519 public keys, with no private material present. Cross-seat digest comparison with Seat 1 is the intended use of this table.

---

## 2. Task 2 — Test execution (181/181 GREEN)

Executed from the corpus root (the adversarial suite reads the trust-roots JSON via relative path):

```
pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py \
       test_xz_protocol_control_graph.py test_xz_protocol_source_frame.py \
       test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py
```

| Suite | Tests | Result |
|---|---|---|
| `test_xz_protocol_kernel.py` | 14 | PASS |
| `test_xz_protocol_condition_a.py` | 29 | PASS |
| `test_xz_protocol_control_graph.py` | 18 | PASS |
| `test_xz_protocol_source_frame.py` | 25 | PASS |
| `test_xz_protocol_adversarial.py` | 27 | PASS |
| `xz_protocol_phase_a_tests.py` | 68 | PASS |
| **Total** | **181** | **181/181 GREEN in 11.79s** |

Environment matched the declared golden-vector pin exactly (numpy 2.4.4, scipy 1.17.1 — the audit host's system numpy 2.2.5 / scipy 1.16.2 was *not* used; an isolated venv was built to the pin). All golden vectors (T2-abs, T2-rel, T3, T4, T7, PA-Z2/Z5/Z10) reproduced exactly under the pin.

---

## 3. Task 3 — B-1/B-2 discharge verification

B-1/B-2 are not named in the packet's documents; the mapping below is reconstructed from the dispatch's v0.2 repair list and the corpus's own annotations (`test_xz_protocol_condition_a.py` marks the string-decision rejection as "(B-1 fix)"; the kernel header declares itself "the sole normative kernel" answering the v0.2 kernel absence). Each discharge was verified **programmatically**, not by reading claims.

| Blocker / repair | Claim | Verification | Result |
|---|---|---|---|
| **B-2** — normative kernel shipped | Sole kernel present with exhaustive 3^5 = 243 vectors | `generate_exhaustive_vectors()` → 243; independent recompute of all 243 decisions vs the decision rule → **0 mismatches** | **DISCHARGED** |
| **B-1** — seam wired to enum | Seam rejects caller-supplied (string) decisions; accepts only `KernelDecision` | `"DENY_FALSE"`, `"ALLOW"`, `1`, `None`, `True` all rejected with `ConditionAError` at `is_dual_evaluable`; enum accepted | **DISCHARGED** |
| Subsidiary — adversarial 9/9 categories | All nine Section-22-item-4 categories present | CAT-1…CAT-9 classes all present in the suite; 27 adversarial tests GREEN | **DISCHARGED** |
| Subsidiary — imports fixed | All modules import and cross-import cleanly | 181 tests collected & passed under the pin (imports exercised at collection); late import of `_validate_numeric` in intervals module executes at import time | **DISCHARGED** |
| Subsidiary — NOT_APPLICABLE → INDETERMINATE | Mandatory check returning NOT_APPLICABLE must not yield A-ACCEPT | `evaluate_boundary` with NOT_APPLICABLE on a mandatory check → **A-INDETERMINATE** (F-SOL-XZ-3 honored) | **DISCHARGED** |
| Subsidiary — FRAME_START 180 days | Frame start exactly 180 days pre-disclosure | Code `FRAME_START = 2023-10-01`; 2024-03-29 − 2023-10-01 = **exactly 180 days**; FRAME_END − disclosure = exactly 30 days | **DISCHARGED** (but see L-1: the module docstring still says "2023-09-30", off by one) |

**Partial falsifications (non-blocking, carried forward):** two repair claims in the *m3 module's* v0.8.4 ledger do not hold uniformly — "bool rejected uniformly at all entry points" fails for `numpy.bool_` (M-1), and "raw exceptions wrapped in PhaseAInputError" fails for `str`/`Decimal` inputs (M-2). These are repair-claim accuracy findings, not verdict-altering defects; both paths crash noisily or coerce, never silently invert a verdict.

---

## 4. Task 4 — Attack

### 4.1 Method

Three independent adversarial verifier sub-agents attacked disjoint surfaces — (A) kernel + A/B seam, (B) Phase A numerics (M3 + BCa intervals), (C) source frame + control graph + trust roots + adversarial-suite self-coverage — each instructed to assume a flaw had been smuggled past the audit, to repro every claim, and to report failed attacks as assurance evidence. In parallel the orchestrator ran its own novel-probe battery (docstring arithmetic, Unicode fact-ID normalization, direct `compute_verdict` calls, validator-looseness probes, PA-Z14 reachability hunt, gate-boundary probes, trust-roots key decoding). **Every sub-agent finding admitted below was independently re-reproduced by the orchestrator in the pinned environment before admission.**

### 4.2 Consolidated findings register (orchestrator-calibrated severities)

Severity standard used: **CRITICAL** = silent verdict smuggling through intended data inputs; **HIGH** = invariant break reachable through the public API (code-plane) or a gate certifying without evidence; **MEDIUM** = robustness/validator gap or falsified repair claim; **LOW** = documentary/cosmetic; **INFO** = noted behavior, per-spec or harmless.

#### HIGH

| ID | Component | Finding | Evidence | Disposition |
|---|---|---|---|---|
| **H-1** | `xz_protocol_kernel.py:59, 89–94` | `evaluate_kernel` reads conjuncts through the **overridable** method `ConjunctVector.as_dict()`; `__post_init__` validates through the same method. A subclass overriding `as_dict()` launders any vector — an all-FALSE instance evaluates to **ALLOW** through the kernel itself. | Reproduced: `class L(ConjunctVector): def as_dict(self): return {n: TRUE …}`; `evaluate_kernel(L(F,F,F,F,F))` → `ALLOW`. | **Carry-forward (recommended fix v0.3.1):** `type(vector) is ConjunctVector` and/or read the five dataclass fields directly. Code-plane path — requires in-process subclass injection, at which point no Python-level check survives (same class as `object.__setattr__`, which the m3 module explicitly scopes out of the Python API layer). Does not affect any data-plane caller. Non-blocking under the declared threat model; the kernel's "No bypass" sentence should be scoped or the one-line fix taken. |
| **H-2** | `xz_protocol_control_graph.py:104–121` | `WithinAuthAssessment.__post_init__` validates channel schema (exactly 5 unique channels) but **never checks `verdict == compute_verdict(edges)`** — an assessment certifying OUTSIDE against all-YES edges (or INSIDE against all-NO) is accepted silently. The record type whose entire purpose is binding verdict to channel evidence does not bind them. | Reproduced: 5× YES edges + `verdict=OUTSIDE` → accepted; `compute_verdict(edges)=INSIDE` ≠ stored verdict. | **Carry-forward:** one-line consistency check in `__post_init__`. Protocol-layer mitigation exists by design (two independent adjudicators + reliability-before-consensus would disagree with a fabricated assessment), but that layer is not in the shipped corpus. |
| **H-3** | `xz_protocol_phase_a_intervals.py:91, 132–136, 389–395` | **A single shared fact can satisfy gate T2.** With n=1 (A@100, B@30): delta=70 ≥ 30, ratio=0.70 ≥ 0.20, and the PA-Z2 degenerate interval [70, 70] has `excludes_zero=True` → `evaluate_t2_full` emits **`t2_satisfied=True` with zero resamples**. Conservatism is applied unevenly: PA-Z14 forces `excludes_zero=False` when BCa is unreliable, but PA-Z2/PA-Z11 do not when the interval carries no stability evidence at all — inconsistent with the module's own "intervals are finite-corpus stability summaries." | Reproduced exactly as above; receipt discloses `fallback_reason="PA-Z2"`, `n_resamples=0`. | **Carry-forward:** force `excludes_zero=False` on zero-resample degenerate fallbacks (mirror PA-Z14), or require n ≥ 2 for the interval conjunct. Fully receipted (named rule, zero-resample count disclosed) — a noisy state, not a silent smuggle; minimum-evidence judging arguably belongs to the adjudication layer, but `t2_satisfied` is computed **in code**, so the code crosses its own layering. |

#### MEDIUM

| ID | Component | Finding | Evidence | Disposition |
|---|---|---|---|---|
| **M-1** | `xz_protocol_phase_a_m3.py:59–61` (+ call sites) | `_reject_bool` uses `isinstance(v, bool)`; `numpy.bool_` is not `bool` and is **accepted** at `M3Observation.minutes`, `t3_interval`, `evaluate_t5`, `compute_median` — falsifying the v0.8.4 claim "bool rejected uniformly at all entry points." Consequences: raw `TypeError` at pairing ("numpy boolean subtract not supported"), or silent coercion (`t3([np.True_, 2.0])` treats it as 1.0; `compute_median` returns a `np.bool_`). T4/T7/seed paths (which use `type(val) is not int`) do reject it — rejection is not uniform. | Reproduced per finding. | **Carry-forward:** extend `_reject_bool` to cover `np.bool_`. Data-plane reachable in numpy pipelines; never inverts a verdict (crashes or coerces loudly), hence MEDIUM. |
| **M-2** | `xz_protocol_phase_a_m3.py:96–132, 230` | `_validate_numeric` validates but never coerces/stores; non-float numerics pass validation then escape as **raw** exceptions — `minutes="60"` → raw `TypeError` (`'>' not supported between str and float`) at the OBSERVED bound check; `Decimal("60.5")` accepted, raw `TypeError` at pairing. Falsifies "raw exceptions wrapped in PhaseAInputError" for these paths. | Reproduced per finding. | **Carry-forward:** coerce via `object.__setattr__` in `__post_init__` or reject non-`(int, float)` types up front. Honesty/robustness gap in a repair claim. |
| **M-3** | `xz_protocol_control_graph.py:128–155` | Public `compute_verdict` accepts malformed edge sets: **empty tuple → vacuous `OUTSIDE`** (`all()` on empty = True — the *exculpatory* verdict from zero evidence); single NO edge → OUTSIDE; duplicate channels are order-dependent (`{CAUSE:YES, CAUSE:NO}` collapses via dict last-write-wins — `[YES,NO]`→OUTSIDE, `[NO,YES]`→INSIDE). The 5-channel schema is enforced only in `WithinAuthAssessment`, not in the verdict function itself (the decoy fixtures call `compute_verdict` directly). | Reproduced per finding. | **Carry-forward:** validate exactly-5-unique-channels inside `compute_verdict`. |
| **M-4** | `xz_protocol_source_frame.py:325–353` | `validate_manifest()` is weak where it matters: (a) citation check `purl in murl or murl in purl` is satisfied by an **empty-string URL** and by stub substrings; (b) a greedily minimized 5-record manifest (11 records deleted) still validates; (c) empty `authentication`/`strata_covered`/`retrieval_rule` records validate (only the *tests* catch these); (d) stratum thinning (S-COMMIT 2→1 sources) validates. The validator — the tool that certifies manifest integrity — cannot distinguish the frozen manifest from a gutted one. | Reproduced per finding. | **Carry-forward:** exact canonical-URL matching for the four primary citations; per-record field checks inside the validator; minimum-coverage thresholds. (The shipped manifest itself is genuine — see assurance evidence.) |
| **M-5** | `xz_protocol_source_frame.py` (whole module) | **The frame window is never enforced in shipped code.** No `in_frame()` membership function exists; `SourceRecord` carries no date field; FRAME_START/END are constants echoed by tests but applied to nothing. CAT-6 (post-cutoff injection) is defended only by constant assertions, and the suite itself admits "cutoff enforcement is at the packet layer" — while no packet-layer code is in the corpus. | Grep + construction: a post-cutoff record added to a manifest copy validates fine. | **Scope finding (must close before any live run):** record explicitly that the 13-file corpus does not enforce the temporal frame; enforcement must be demonstrated at the packet layer before evidence ingestion. |
| **M-6** | `xz_protocol_condition_a.py:266, 320` | `evaluate_boundary` consumes `check_results` twice; a generator input yields the correct disposition but a **silently empty** `check_results` tuple in the stored `BoundaryDisposition` — the audit record loses its evidence. | Reproduced: generator of 3 PASS results → `A-ACCEPT`, `len(check_results)==0`. | **Carry-forward:** materialize `tuple(check_results)` at entry. |

#### LOW (documentary / cosmetic / minor robustness)

| ID | Finding |
|---|---|
| **L-1** | `source_frame` docstring: "Start: 2023-09-30 (180 days before disclosure)" — code/tests use **2023-10-01**, which *is* exactly 180 days; the docstring is off by one and contradicts its own parenthetical. A reader following the docstring enumerates one extra day. |
| **L-2** | "PA-Z1 through PA-Z3, PA-Z5 through PA-Z14 (**eleven rules**)" — arithmetic error in two docstrings: 3 + 10 = **13** code-level rules, and 13 are implemented and tested. |
| **L-3** | PA-Z7 is documented (`t4_interval`: "union-empty is natural zero-diff") but **never emitted** — the all-zero T4 input exits via PA-Z10; no "PA-Z7" string exists outside docstrings/tests. Receipt-taxonomy confusion. |
| **L-4** | Version lag: `trust_roots_PUBLIC.json` declares `"protocol": "XZ Protocol v0.2"`; `source_frame`, `control_graph`, `condition_a` docstrings also say v0.2 — inside a v0.3 packet. No test asserts the field. |
| **L-5** | `condition_a` docstring claims "the provenance check on BaselineCheckResult is an accident guard (same discipline as the Phase A scoring module)" — but `_CHECK_TOKEN` is **written and never compared** anywhere in the module; the claimed check does not exist (the m3 module genuinely enforces its analogue via `verify_provenance()`). |
| **L-6** | The shipped PA-Z14 test is **vacuous**: its fixture (deltas [0]×38 + [3,2,1]) exits via PA-Z10 (`prop_below=0`), so the assertion block guarded by `if not r.point_in_interval:` never executes. Orchestrator + sub-agent search found real PA-Z14 firings are rare (~6 in 1,800 hostile runs; earlier guards Z5/Z10/Z11 absorb the degenerate region first). |
| **L-7** | PA-Z14 reversion keeps the **BCa bounds** while labeling the method `PERCENTILE_FALLBACK` — a true percentile recompute on the same resamples differs. Disclosed in `fallback_reason`; `excludes_zero` forced False (conservative); label/bounds mismatch can mislead a receipt reader. |
| **L-8** | `is_dual_evaluable` docstring says "both conditions produced a *determinate* disposition," but A-INDETERMINATE returns True (tests codify this). Doc inaccurate; denominator semantics unclear to a reader. |
| **L-9** | `normalize_fact_id` docstring says "strip ASCII whitespace"; `str.strip()` strips **Unicode** whitespace (`"f1\xa0" → "f1"`). Behavior is the safer direction (collisions fail-closed as duplicates), but the frozen spec text is inaccurate. |
| **L-10** | Seam functions type-check `b_decision` (post-B-1) but never type-check `a_disposition`: a fabricated `BoundaryDisposition("…", A_ACCEPT, …)` or even a duck-typed impostor with `.disposition = A_ACCEPT` yields `is_primary_seam_divergence(...) == True` against a real `DENY_FALSE`. Code-plane input fabrication; consistency fix mirrors the B-1 discipline. |
| **L-11** | `_bca_interval` validates `caller_seed` but not `internal_seed`: negative internal seed → raw `ValueError` from numpy. Internal-but-importable API. |
| **L-12** | Decoy-fixture self-checks use bare `assert` — vanish under `python -O`. (Mitigating: fixture verdicts are computed, not hardcoded.) |
| **L-13** | Frame boundary semantics unpinned: no inclusive/exclusive endpoint rule; "enumerate commits by author date" carries no timezone rule — a commit at `2023-09-30T20:00-07:00` = `2023-10-01T03:00Z` flips frame membership by timezone choice. Protocol-layer lacuna. |
| **L-14** | Decoy fixture `independent_ci` sets `CAUSE=NO` while its own evidence says "CI triggers on push" and its reasoning concedes "maintainer can trigger a build" — conflating CAUSE (can S cause the record-generation act) with content control (MODIFY). The verdict (OUTSIDE) still computes, but the calibration fixture teaches adjudicators a contestable pattern, in tension with PROHIBITED_SHORTCUTS[4] (repo-owner-controlled CI ⇒ INSIDE). |
| **L-15** | Dead loop in `ConjunctVector.__post_init__` (lines 56–58) computes an unused mis-cased attribute; harmless, hides nothing (verified). |

#### INFO

| ID | Finding |
|---|---|
| **I-1** | A FAIL on a **non-mandatory** check does not affect the disposition (per the frozen vocabulary, which counts only mandatory checks); a consumer reading only `disposition` + `reason` ("All mandatory checks pass") while a FAIL sits in `check_results` may be misled. Profile governance (frozen in code) is the control. |
| **I-2** | `object.__setattr__` mutates frozen instances (kernel vector FALSE→TRUE post-construction). Documented Python-limitation class; m3 scopes it out explicitly, the kernel/condition_a/control_graph modules do not — consistency note only. |
| **I-3** | `evaluate_t5(1e-308, 480.0)` → ratio `inf`, `t5_fires=True`. Mathematically defensible; undeclared. |
| **I-4** | `M3Vector("C")` constructs (vector-level condition not validated); downstream `compute_paired_differences` enforces A/B — fail-closed. |
| **I-5** | Manifest is **16** records across **6** used categories (TRANSPARENCY_LOG declared, unused). NVD URL is lowercase (`cve-2024-3094`); canonical form is uppercase but NVD redirects — functional. |
| **I-6** | The m3 provenance-guard documentation claim verified **true**: fabrication rejected; bypass requires deliberate `dataclasses.replace` or token import, as documented. |
| **I-7** | The `_bca_q` denominator guard is dead code: |a| ≤ 1/6 and the z0 bound make a sign-flipping denominator unreachable; 0 firings in 1,800 hostile runs. Harmless defensive depth. |
| **I-8** | CAT-3/CAT-4 tests read the trust-roots JSON via a cwd-relative path — harness fragility only (run from the corpus root). |

### 4.3 Attacks that FAILED — assurance evidence

The following adversarial lines were pressed hard and the code held. These are the positive grounds for the carrying verdict.

- **Kernel decision logic, exhaustively:** all 243 vectors recomputed independently against the decision rule — 0 mismatches (orchestrator + sub-agent A, twice, in two environments). FALSE dominates UNKNOWN order-independently on every mixed vector; reason codes on mixed vectors contain only `E-FALSE-*`.
- **Enum perimeter:** `TruthValue`/`KernelDecision` are final (subclassing raises `TypeError`); string conjuncts, `numpy.bool_`, NaN, plain `bool`, string-enum lookalikes all fail-closed at construction/evaluation. `dataclasses.replace` re-runs validation and is rejected; normal-attribute mutation of frozen instances rejected.
- **Condition A, exhaustive sweeps:** all 8³ = 512 outcome/absence combinations for S-COMMIT and all 8⁴ = 4,096 for S-RELEASE — REJECT > INDETERMINATE held in 100% of cases; no silent fall-through among the 7 `CheckOutcome` members; duplicate mandatory checks rejected; empty results → A-INDETERMINATE (fail-closed); A-NOT-APPLICABLE unreachable for all six real strata.
- **Seam cross-product:** all 12 (A-disposition × KernelDecision) pairs — primary divergence TRUE only for (A-ACCEPT, DENY_FALSE); A-NOT-APPLICABLE never dual-evaluable; DENY_UNKNOWN never primary. The seam *comparison logic* is exactly per spec.
- **BCa numerics:** hand-rolled independent Efron BCa on the identical resample stream matched `_bca_interval` **bit-for-bit** (max deviation 1.1e-12) across 11 dataset/statistic combinations; `scipy.stats.bootstrap(method='BCa')` cross-check (independent stream) agreed to ~2e-3. No smuggled deviation in z0, acceleration, or level computation.
- **Hostile bootstrap sweep:** 1,800 adversarial calls (subnormals, ties, extreme imbalance, n=2…40, median/mean/ba_b/fp_diff) — **0** intervals with lower > upper, **0** NaN bounds; level-clamp fired 53 times, all benign and honestly counted.
- **Median parity:** `compute_median` vs NumPy across 20,000 adversarial cases (even/odd, negatives, −0.0, subnormals, ulp-boundary, overflow, NaN propagation) — 0 mismatches.
- **Gate boundaries exact:** absolute median ≥ 30.0 and relative median ≥ 0.20 are inclusive; T5 fires strictly above 1.25 (1.25 exactly → no fire; 1.25 + 1 ulp → fire); 480-minute censor semantics exact (OBSERVED and RIGHT_CENSORED_BUDGET accept exactly 480; CENSORED_EARLY rejects it; `nextafter(480,0)` rejected for budget-censoring).
- **Seeds:** reproducibility exact per seed; internal offsets (+0…+4 per estimator) honestly recorded in `internal_seed`; bool/`np.bool_`/float/negative seeds rejected.
- **Control-graph verdict math** on well-formed input: all-NO→OUTSIDE; any-YES→INSIDE (all five single-YES positions); YES > UNKNOWN > NO dominance; all three decoy fixtures' verdicts computed (not hardcoded) and reachable.
- **Trust roots:** three distinct, well-formed 64-hex/32-byte values; all decode as valid Ed25519 public keys; no private/seed material anywhere in the file.
- **Frozen citations factually accurate:** the openwall `2024/03/29/4` post is the genuine Freund disclosure (2024-03-29); GHSA-rxwq-x6h5-x525 is the correct advisory; tukaani-project/xz issue #103 is the real backdoor-discussion issue; NVD CVE-2024-3094 entry correct (lowercase URL functional).
- **Prohibited-content gates:** no payload/ifunc/GOT-PLT/cpuid/rsa_public_decrypt/backdoor terms in the shipped modules; "activation recipe" appears only inside its own prohibition.
- **PA-Z9 vs PA-Z13 rule selection:** different expressions in `evaluate_t2_point` vs `evaluate_t2_full`, provably equivalent (excluded==n ⟺ nonfinite==0 when the ratio list is empty).

---

## 5. Residual risk and scope boundaries

This audit's assurance is bounded, and the bounds are part of the verdict:

1. **Data-plane assurance, not code-plane.** The corpus defends its invariants against adversarial *data* (type confusion, string smuggling, malformed outcomes, hostile floats, adversarial resamples) exhaustively. Findings H-1, L-10, and I-2 live one plane up: they require the adversary to inject *code* into the evaluator's process (a subclass, a fabricated record object, `object.__setattr__`). The m3 module states the correct discipline explicitly — "enforced at the protocol layer, not at this Python API layer" — but the kernel, condition_a, control_graph, and source_frame modules do not carry the same scoping sentence, and the kernel's "No bypass" claim overstates against H-1. Recommend either the one-line hardening fixes or uniform scoping language in v0.3.1.
2. **Unshipped layers.** The packet layer (frame-window enforcement, M-5), the adjudication layer (PA-Z4, minimum-evidence rules relevant to H-3, dual-adjudicator reliability relevant to H-2), and the commitment/sealing machinery that would use the trust roots are **not in the 13-file corpus**. This audit verifies the shipped normative core; it cannot and does not certify those layers. Before any live evidence ingestion, M-5 must be closed demonstrably.
3. **The validator is not the integrity boundary.** `validate_manifest()` (M-4) is a self-check tool, not a control; the manifest's real integrity control is the carrying discipline itself (hash-pinning, Section 1). The finding stands because the module presents the validator as a certification function.
4. **Tests vs. enforcement.** Several guarantees exist only as tests, not as code-path enforcement (L-5 provenance comparison, M-4(c) record field checks, L-6 vacuous PA-Z14 pin). Tests verify; they do not defend. Where the protocol intends a guarantee to be load-bearing, it should live in the shipped functions.
5. **Repair-claim accuracy.** Two v0.8.4 ledger claims are falsifiable at the edges (M-1, M-2). The direction of every failure is noisy (exception) or coercive-with-footprint — never a silent verdict inversion — but the carrying record should not repeat those claims unqualified.

## 6. Task 5 — Verdict

**CARRY-CLEAN.**

Reasoning, against the carrying standard ("does the carried object enforce its own frozen semantics under its declared threat model, with all degenerate states named and receipted?"):

1. **All mandated gates pass.** 13/13 digests attested; 181/181 GREEN under the exact pinned environment; B-1/B-2 and all four subsidiary v0.2 repairs verified discharged in code, programmatically.
2. **No blocking finding.** No finding demonstrates silent verdict smuggling through intended data inputs. The normative decision mathematics — kernel (243/243), Condition A dominance (4,608/4,608 swept combinations), seam comparison (12/12 pairs), BCa core (bit-exact vs an independent reference) — survived exhaustive falsification. The three HIGH findings are (i) code-plane, requiring in-process code execution that the implementation's own documented discipline scopes out; (ii) protocol-layer-mitigated by design (dual adjudication) with the mitigation layer unshipped but declared; (iii) fully receipted named states (PA-Z2 with `n_resamples=0` disclosed). Each has a one-line-class fix and is carried forward.
3. **Findings register is the carry.** The 32-entry findings register (0 CRITICAL, 3 HIGH, 6 MEDIUM, 15 LOW, 8 INFO) is attached as recommended v0.3.1 dispositions. None individually or in combination inverts a verdict, breaks a frozen invariant for well-typed inputs, or contradicts a normative claim the packet actually depends on. The documentary cluster (L-1…L-15) should be cleaned up precisely because this protocol's discipline is documentary exactness.

**Recommended v0.3.1 dispositions (non-blocking):** H-1 read dataclass fields directly in `evaluate_kernel` (or exact-type check); H-2 bind `verdict == compute_verdict(edges)` in `WithinAuthAssessment.__post_init__`; H-3 force `excludes_zero=False` on zero-resample degenerate intervals; M-1/M-2 close `np.bool_`/non-float validation gaps or correct the repair ledger; M-3 schema-check inside `compute_verdict`; M-4 exact-match citation validation + per-record field checks; M-5 demonstrate packet-layer frame enforcement before any live run; M-6 materialize check_results at entry; L-1…L-15 documentary corrections (frame-start docstring, rule count, PA-Z7 emission or removal, v0.3 version strings, vestigial provenance claim, vacuous PA-Z14 test, seam input type-checks, endpoint/timezone semantics, CI-fixture CAUSE edge, dead loop).

---

### Sign-off

| | |
|---|---|
| **Seat 2 auditor** | Kimi K3 |
| **Verdict** | **CARRY-CLEAN** (findings register carried forward; no blocking findings) |
| **Digest of this report's basis** | 13 file digests in Section 1; 181/181 pytest record; 32-entry findings register; assurance evidence §4.3 |
| **Cross-seat note** | Section 1 digest table is formatted for direct comparison against Seat 1 (GPT-5.6 Sol); any digest mismatch between seats is itself a HALT condition for the carry. |

*Audit executed per DISPATCH_XZ_v03_KIMI.txt: 1. SHA-256 (13/13) ✓ · 2. 181/181 GREEN ✓ · 3. B-1/B-2 discharged ✓ · 4. Attack ✓ · 5. Verdict: CARRY-CLEAN ✓*

---

# Bismillah ir-Rahman ir-Rahim
