# Bismillah ir-Rahman ir-Rahim

# Deep Read Report -- Section V-C2: BSSG & SHVVP (Batch 8)
## Papers Read: 22

## Total Size: 368,811 characters across 8,541 lines

---

## Per-Paper Summaries

### R0366 -- shvvp_v0_8_1_phase_a_m3.txt — shvvp_v0_8_1_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, and paired differences.
- **Date:** Undated
- **Source:** shvvp_v0_8_1_phase_a_m3.txt
- **Size:** 303 lines, 9,651 chars
- **SHA-256:** `a2751e221f13698e...`

**Structure:**
  - Check for duplicate fact_id
  - PA-Z1: S is empty
  - Relative gate: Delta-M3(f) / M3(f, A) for facts where M3(f, A) > 0
  - All M3(f, A) = 0 -- relative gate is NOT-EVALUABLE

**Key Concepts:** FIRST, SHVVP, BUDGET, CENSORED, EARLY, OBSERVED, RIGHT

**Content Summary:**
- source_format: txt - text_sha256: a2751e221f13698ebb3ff0a6594ee0cfbaba7c6e2a7ae3903d95d9d5e74a5925
""" shvvp_v0_8_1_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, and paired differences.
Rules implemented: - M3(f, c) = wall-clock minutes from corpus access to first immutable saved evidence record identifying f under condition c. - Right-censored at BUDGET if c did not identify f. - CENSORED-EARLY flag if session terminated before budget. - M3-FIRST(c) = min over all consequential facts f of M3(f, c). - Delta-M3(f) = M3(f, A) - M3(f, B) for shared facts. - Tie handling: secondary sort by fact_id ascending.

---

### R0370 -- shvvp_v0_8_3_phase_a_intervals.txt — shvvp_v0_8_3_phase_a_intervals.py -- Phase A BCa bootstrap intervals.
- **Date:** Undated
- **Source:** shvvp_v0_8_3_phase_a_intervals.txt
- **Size:** 586 lines, 20,190 chars
- **SHA-256:** `358366c932d76a6a...`

**Structure:**
  - ---------------------------------------------------------------------------
  - Constants
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - Core BCa (PA-2), with all fallback paths declared and named
  - ---------------------------------------------------------------------------
  - PA-Z2: n=1 -> percentile fallback immediately
  - Bootstrap replicates
  - PA-Z11: NaN resamples counted, discarded, reported
  - Bias correction z0 (PA-2 step 1)
  - PA-Z10: z0-undefined
  - Jackknife acceleration (PA-2 step 2)
  - PA-Z5: acceleration undefined when sum_sq == 0
  - BCa-adjusted percentile levels (PA-2 step 3)
  - Documented boundary guard: near-zero denom -> level 0.5

**Key Concepts:** SHVVP, THE CODE IS THE SOLE NORMATIVE DEFINITION, PRNG, FINITE, CORPUS STABILITY SUMMARIES, ACCIDENT GUARD, BOOTSTRAP, CONFIDENCE, LEVEL, CORPUS

**Content Summary:**
- source_format: txt - merged_variants: 1 (shvvp_v0_8_2_phase_a_intervals.txt) - text_sha256: 358366c932d76a6add6eef425241ab94d23f886712e6bdb79c5595c9bb2bf880
""" shvvp_v0_8_3_phase_a_intervals.py -- Phase A BCa bootstrap intervals.
THE CODE IS THE SOLE NORMATIVE DEFINITION of the interval computation. Golden-vector receipts in the test suite pin exact numerical outputs for every statistic and fallback path under the pinned dependency versions below. A dependency upgrade that changes PRNG streams or percentile interpolation will fail the golden-vector tests.

---

### R0371 -- shvvp_v0_8_3_phase_a_m3.txt — shvvp_v0_8_3_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.
- **Date:** Undated
- **Source:** shvvp_v0_8_3_phase_a_m3.txt
- **Size:** 440 lines, 16,058 chars
- **SHA-256:** `cd36ea1a4d95ca14...`

**Structure:**
  - ---------------------------------------------------------------------------
  - Frozen constants
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - Enums
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - Errors
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - Validation
  - ---------------------------------------------------------------------------
  - ---------------------------------------------------------------------------
  - M3 Observation
  - ---------------------------------------------------------------------------

**Key Concepts:** FIRST, SHVVP, GPT, SOL, OBSERVED, FROZEN, BUDGET, MINUTES, API, ACCIDENT GUARD

**Content Summary:**
- source_format: txt - merged_variants: 1 (shvvp_v0_8_2_phase_a_m3.txt) - text_sha256: cd36ea1a4d95ca149387bf58317c02e1149f41fb358e77bc8cc1d60d3b91d6eb
""" shvvp_v0_8_3_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.
v0.8.3 repairs from v0.8.2 carrying audit (GPT Sol + Kimi K3): F-SOL-082-1/F-K3-N1: Provenance downgraded to accident-guard. F-SOL-082-2/F-K3-N5: OBSERVED <= FROZEN_BUDGET_MINUTES enforced. F-SOL-082-8/F-K3-N4: PA-Z9 evaluable=False in both APIs. F-K3-N14: M3Vector validates on construction. F-K3-N16: Docstring corrected (censoring analysis withdrawn, not re-derived). F-K3-N17: bool rejected as numeric input.

---

### R0373 -- shvvp_v0_8_4_phase_a_intervals.txt — shvvp_v0_8_4_phase_a_intervals.py -- Phase A BCa bootstrap intervals.
- **Date:** Undated
- **Source:** shvvp_v0_8_4_phase_a_intervals.txt
- **Size:** 424 lines, 15,022 chars
- **SHA-256:** `82eb117656a5954b...`

**Structure:**
  - PA-Z14: if BCa and point not in interval, revert to percentile
  - This is a named state, not silent
  - Recalculate with the _stored_ bootstrap replicates? No -- we
  - flag and report. The interval bounds remain as computed but the
  - method is marked PERCENTILE and excludes_zero is re-evaluated
  - conservatively as False (the BCa correction is unreliable).
  - === T2 ===
  - === T3 ===
  - === T4 ===
  - === T7 ===
  - === T5 ===
  - Need to import _validate_numeric
  - === Full T2 ===

**Key Concepts:** SHVVP, THE CODE IS THE SOLE NORMATIVE DEFINITION, INDETERMINATE, ADJUDICATION, FINITE, CORPUS STABILITY SUMMARIES, ACCIDENT GUARD, BOOTSTRAP, CONFIDENCE, LEVEL

**Content Summary:**
- source_format: txt - merged_variants: 2 (xz_protocol_phase_a_intervals.py; xz_protocol_phase_a_intervals.py.txt) - text_sha256: 82eb117656a5954b8f31ab8e650ab820551f141fd6481952089547e883532b7c
""" shvvp_v0_8_4_phase_a_intervals.py -- Phase A BCa bootstrap intervals.
THE CODE IS THE SOLE NORMATIVE DEFINITION of the interval computation. Golden-vector receipts in the test suite pin exact numerical outputs.

---

### R0374 -- shvvp_v0_8_4_phase_a_m3.txt — shvvp_v0_8_4_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.
- **Date:** Undated
- **Source:** shvvp_v0_8_4_phase_a_m3.txt
- **Size:** 315 lines, 12,206 chars
- **SHA-256:** `4a0b055e2f88db44...`

**Structure:**
  - Enum membership FIRST (F-SOL-083-2)

**Key Concepts:** FIRST, SHVVP, GPT, SOL, FROZEN, SUBSTANTIVE, OBSERVED, SUBSTANTIVE ENDPOINT CHANGE, ACCIDENT GUARD, NOT

**Content Summary:**
- source_format: txt - merged_variants: 3 (xz_protocol_phase_a_m3.py; xz_protocol_phase_a_m3.py.txt; xz_protocol_phase_a_m3.txt) - text_sha256: 4a0b055e2f88db441775fc783e1b2ed9acda8e8c79eaf9e041cd384b8f84b268
""" shvvp_v0_8_4_phase_a_m3.py -- Per-fact M3 vector, M3-FIRST, paired differences.
v0.8.4 repairs from v0.8.3 carrying audit (GPT Sol + Kimi K3): F-SOL-083-1: M3Vector is now FROZEN with observations as tuple. F-SOL-083-2: censor_status enum membership validated first. F-SOL-083-5: M3 endpoint declared SUBSTANTIVE change from parent. F-SOL-083-9/F-K3-083-6: bool rejected uniformly at all entry points. F-SOL-083-10/F-K3-083-10: raw exceptions wrapped in PhaseAInputError. F-K3-083-2: non-finite ratios excluded and counted (PA-Z13). F-K3-083-5: provenance docstrings aligned with acciden...

---

### R0376 -- SHVVP v0.8 corr2 Focused Re-Audit Verdict
- **Date:** Undated
- **Source:** SHVVP_v0_8_corr2_GPT56_REAUDIT_VERDICT.md
- **Size:** 125 lines, 5,895 chars
- **SHA-256:** `55e05df8c77d1855...`

**Structure:**
  - SHVVP v0.8 corr2 Focused Re-Audit Verdict
  - Verdict: HALT
  -   Reopened-finding disposition
  -     F-R8-PUB-1 — CLOSED
  -     F-R8-PUB-10 — OPEN, LOW, BLOCKING
  -   Standard execution results
  -   Byte and manifest binds
  -   Sealed execution challenge
  - Challenge hash:
  -   Minimum corrective action
  - 1. In the source Status paragraph, replace `deposited here` with `prepared for deposit here` or `inc
  - 2. In the carrying record, replace `included in this deposit` with `included in this release packet`
  - 3. Replace present-tense `deposit archive timestamps independently` wording with release/freeze word
  - 4. Add an explicit verifier gate scanning the current source, README, carrying record, deposit metad
  - 5. Rebuild the flagship PDF and regenerate `SHA256SUMS.txt`; do not modify the gate, vectors, suite,

**Key Concepts:** SHVVP, REAUDIT, BRIEF, GPT, SHA, HALT, PUB, CLOSED, OPEN, RESULT

**Content Summary:**
- source_format: md - text_sha256: 55e05df8c77d185567e33a75328b4f00f978610c942fa345b61971cd19a6b098
**Dispatch:** `REAUDIT_BRIEF_v0_8_corr2.md` **Artifact:** `SHVVP_v0_8_release_packet.zip` **Executing seat:** GPT-5.6 Thinking **Family:** OpenAI GPT **Harness:** ChatGPT container execution environment; Linux x86_64; Python 3.13.5; `cryptography` 46.0.4 **Archive SHA-256:** `a60c17f3949d5143fcc580eba55c9f18f5501dc30748fde6841e71b2ce2e929d`
The executable and cryptographic checks pass, and F-R8-PUB-1 is CLOSED. However, F-R8-PUB-10 remains OPEN and blocking because a current v0.8 status surface still asserts completed deposit. The corr2 brief makes any reopened finding a mandatory HALT. Publication/deposit is therefore not authorized on this packet.

---

### R0379 -- SHVVP v0.8-rc1 audit-absorption changeset
- **Date:** Undated
- **Source:** SHVVP_v0_8_RC1_CHANGESET.md
- **Size:** 64 lines, 3,870 chars
- **SHA-256:** `9e385124e1dba51c...`

**Structure:**
  - SHVVP v0.8-rc1 audit-absorption changeset
  -   Disposition
  -   F-P7-1 - caller-selectable verification key
  -   F-P7-2 - no genuine pre-run commitment
  -   F-P7-3 - meaningless commitment ID
  -   F-P7-4 - contradictory denominator prose
  -   Verification state

**Key Concepts:** SHVVP, HIGH, BLOCKING, MEDIUM, API, REALIZED, UTC, SEALED, PDF

**Content Summary:**
- source_format: md - text_sha256: 9e385124e1dba51c87cfb97feaa0b2300f33f4c23a43ab768c2b8eb28d5895c8
The v0.7 Seat-A verdict is accepted in full: F-P7-1 and F-P7-2 are HIGH and BLOCKING; F-P7-3 and F-P7-4 are MEDIUM. This candidate changes the route-gate trust architecture and corresponding Section 8 text, while carrying the v0.5 decision and power modules unchanged.
The `trusted_pubkey` parameter is removed from `route_claims`, `evaluate_gate`, and every verifier path. Three exact Ed25519 public keys are embedded in the manifest envelope: commitment authority, run logger, and pre-run anchor. Every signature verifier references those constants directly. The result object reports only those manifest-bound keys. Tests A1-A8 cover API inspection, rejected keyword override, caller-generated sel...

---

### R0380 -- SHVVP v0.8 carrying-audit dispatch brief - DRAFT ONLY
- **Date:** Undated
- **Source:** SHVVP_v0_8_RC1_DISPATCH_DRAFT.md
- **Size:** 76 lines, 3,857 chars
- **SHA-256:** `bc2192c7efa7cdb4...`

**Structure:**
  - SHVVP v0.8 carrying-audit dispatch brief - DRAFT ONLY
  -   1. Standing
  -   2. Artifacts - TO-BE-FROZEN
  -   3. Mandatory executable closure checks
  -     F-P7-1 closure - fixed trust root
  -     F-P7-2 closure - pre-run and append history
  -     F-P7-3 closure - commitment identity
  -     F-P7-4 closure - prose parity
  -   4. Carried integrity

**Key Concepts:** SHVVP, DRAFT ONLY, FROZEN, GPT, PASS, HALT, WITH, AMENDMENTS, SEVERITY, SHV

**Content Summary:**
- source_format: md - text_sha256: bc2192c7efa7cdb44095d03d9160ed38815ba4d4bb001ad5b8d23842b38a25d5
# SHVVP v0.8 carrying-audit dispatch brief - DRAFT ONLY
**Do not dispatch this RC brief as a carrying audit.** Replace every `TO-BE-FROZEN` field after formal v0.8 promotion and recompute hashes from the immutable final bytes.

---

### R0382 -- SHVVP v0.8-rc1 SEAT 1 VERDICT
- **Date:** Undated
- **Source:** SHVVP_v0_8_rc1_SEAT_1_GEMINI_VERDICT.md
- **Size:** 58 lines, 3,501 chars
- **SHA-256:** `5241adf8bca97c19...`

**Structure:**
  - SHVVP v0.8-rc1 SEAT 1 VERDICT
  -   Provenance Block
  -   Execution Transcript Summary
  -   Attack Results Table
  -   Findings

**Key Concepts:** SHVVP, SEAT, VERDICT, MANIFEST, SHA, SUMS, SEALED, REJECTED, PASS, REALIZED

**Content Summary:**
- source_format: md - text_sha256: 5241adf8bca97c1970eaccd9bb6cf033049e960655b6cdebb533c064028ce7ad
## Provenance Block - Model: Gemini 3.1 Pro - Vendor family: Google - Execution harness: Perplexity Computer sandboxed subagent; bash; Python 3.14.3 - Recomputed MANIFEST_SHA256 observed: `f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c` - Command transcript: - `sha256sum -c SHA256SUMS.txt` -> All files OK (exit 0) - `python3 -c 'import shvvp_v0_8_route_gates as G; import hashlib; print("Imported MANIFEST_SHA256:", G.MANIFEST_SHA256); print("Recomputed:", hashlib.sha256(G._manifest_canonical().encode("utf-8")).hexdigest())'` -> `Imported MANIFEST_SHA256: f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c`, `Recomputed: f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0...

---

### R0383 -- SHVVP v0.8-rc1 — SEAT 2 (KIMI) CARRYING VERDICT
- **Date:** Undated
- **Source:** SHVVP_v0_8_rc1_SEAT_2_KIMI_VERDICT.md
- **Size:** 209 lines, 13,670 chars
- **SHA-256:** `be27224cfb8458d7...`

**Structure:**
  - SHVVP v0.8-rc1 — SEAT 2 (KIMI) CARRYING VERDICT
  -   Verdict-provenance block (mandatory)
  - 2. Manifest recompute:
  -   1. Execution transcript summary
  -   2. Findings (F-P8 namespace, six-part schema)
  - No CRITICAL, HIGH, or MEDIUM findings. No blocking findings.
  -   3. Attack results table (this seat's own scripts, fresh keys)
  -   4. Notes on scope of verification
  -   5. Final verdict

**Key Concepts:** SHVVP, SEAT, KIMI, CARRYING VERDICT, NON, PRODUCER, GPT, MANIFEST, SHA, DISPATCH

**Content Summary:**
- source_format: md - text_sha256: be27224cfb8458d7b190a541c9c3bfc85f484234c85c16f3e5c0e349e543b730
- **Model:** Kimi K3 (as configured for this run; carrying seat 2) - **Vendor family:** Moonshot AI — a NON-PRODUCER family (producer of record is the Anthropic family, excluded; GPT family is advisory). This verdict is authored and executed by the Moonshot-family seat. - **Execution harness:** Perplexity Computer sandboxed subagent; bash tool; `python3 --version` observed: **Python 3.14.3**; `cryptography` package pre-installed (Ed25519 via `cryptography.hazmat.primitives.asymmetric.ed25519`). Working directory: `/home/user/workspace/audit_seats/seat_2_kimi` (seat directory only; the other seat's directory was not read or modified). - **Recomputed MANIFEST_SHA256 observed (printed from exec...

---

### R0384 -- shvvp_v0_8_route_gates.py — Executable route-level DESCRIPTIVE GATES for SHVVP v0.8-rc1.
- **Date:** Undated
- **Source:** shvvp_v0_8_route_gates.py
- **Size:** 1042 lines, 51,088 chars
- **SHA-256:** `acd2e378229a9b1a...`

**Structure:**
  - 1. The three verification keys are frozen inside the canonical manifest. The public
  - 2. Channel B is raw evidence and may only carry a commitment_id reference.
  - 3. A SEALED commitment is signed by the frozen commitment authority and includes its
  - 4. A REALIZED universe requires all of: (a) a commitment-authority-signed pre-run
  - 5. Commitment bundles are indexed by commitment_id. Unknown, duplicate-by-alias,
  - Three independent public trust roots, frozen before evaluation. There is no
  - runtime override. Changing any key changes the canonical manifest digest.
  - ---------------------------------------------------------------- vocabulary
  - --------------------------------------------------------- frozen scope manifest
  - ---------------------------------------------------------------- validation
  - ---------------------------------------------------------------- route claims

**Key Concepts:** DESCRIPTIVE GATES, SHVVP, TRUST BOUNDARY, MANIFEST, SHA, SEALED, REALIZED, PROTOCOL, VERSION, RELEASE

**Content Summary:**
- source_format: py - merged_variants: 2 (shvvp_v0_7_route_gates.py; shvvp_v0_8_route_gates.py.txt) - text_sha256: acd2e378229a9b1af6af69a8852e4614b87f5fbe325557cffe06c0606744008a
"""Executable route-level DESCRIPTIVE GATES for SHVVP v0.8-rc1.
This revision absorbs the v0.7 carrying-audit findings F-P7-1 through F-P7-4. It remains descriptive only: no p-value, null, confidence bound, significance, false-discovery-rate procedure, generalization, or population-level novelty claim is produced by the route path.

---

### R0388 -- test_shvvp_v0_5_rules.py — Deterministic and adversarial tests for the frozen SHVVP v0.5 rule modules.
- **Date:** Undated
- **Source:** test_shvvp_v0_5_rules.py
- **Size:** 792 lines, 38,711 chars
- **SHA-256:** `39d4b1aa2e5dfbeb...`

**Structure:**
  - Normalized SHA-256 of shvvp_v0_4_power_sim.py with its version string replaced by
  - vXX. Recomputable from the immutable v0.4 packet, whose hash is recorded in the
  - focused-delta addendum. This pins the claim that the simulation is carried
  - unchanged (amendment A-5.5) without re-running it.
  - A complete, perfect raw-evidence corpus. Used as the baseline that adversarial
  - cases mutate, so that every failure below is attributable to the mutation.
  - ---------------------------------------------------------------- Phase B
  - every frozen label is reachable
  - observed failure dominates discordance
  - unreadable data dominates observed failure
  - ---------------------------------------------------------------- Phase C
  - hard observed mechanical failure dominates UNKNOWN domination and low alpha
  - an adjudicated conjunct with inadmissible alpha cannot create a hard failure
  - but with admissible alpha it does
  - UNKNOWN domination outranks the tentative band

**Key Concepts:** SHVVP, TOTAL, ANNOTATIONS, CURRENT, VERSION PARITY, PDF, README, INFERENCE, ADVERSARIAL, WITHDRAWN

**Content Summary:**
- source_format: py - text_sha256: 39d4b1aa2e5dfbebc5744bd9ead38edfee1b2064cbd43fc3d8b11ed964374bcb
"""Deterministic and adversarial tests for the frozen SHVVP v0.5 rule modules.
Run with:  python test_shvvp_v0_5_rules.py Exit status 0 means every check passed. The suite runs offline with no input data.

---

### R0389 -- test_shvvp_v0_6_rules.py — Route-gate test suite for the frozen SHVVP v0.6 protocol.
- **Date:** Undated
- **Source:** test_shvvp_v0_6_rules.py
- **Size:** 475 lines, 24,582 chars
- **SHA-256:** `71137f09be15901d...`

**Structure:**
  - --------------------------------------------------------------- record binding
  - The canonical perfect corpus, every record bound and complete against its
  - committed universe. Note R4-C is now the full 216-injection universe (was a
  - 40-item subset under v0.5), and every record carries its manifest binding.
  - ---------------------------------------------------------------- no inference
  - ---------------------------------------------------------- raw evidence only
  - a catastrophic but well-bound record cannot support a route.
  - an injected decision field is rejected as an unexpected field.
  - a fabricated derived object is rejected as evidence.
  - dataclasses.replace on a genuine below-minimum report is rejected.
  - minimum evidence counts enforced at n-1, n, n+1 (realized components, where a
  - subset below the committed universe is not itself the point).
  - malformed or inconsistent records are rejected.
  - route_claims level rejections.
  - zero-tolerance violations dominate a passing share.

**Key Concepts:** SHVVP, ADDS, HERE, FAILURES, COUNT, COUNT
    COUNT, PASS, FAIL, MANIFEST, KEY

**Content Summary:**
- source_format: py - text_sha256: 71137f09be15901d26ea9749bb9684acb50900b6173f7ed57916d9e479bbaf20
"""Route-gate test suite for the frozen SHVVP v0.6 protocol.
Scope. v0.6 changes exactly one executable module relative to v0.5, the route gate, to close the blocking finding F-P5-1 (caller-selectable evidence universe and post-result omission). This suite therefore focuses on the route gate: it carries forward the v0.5 no-inference and raw-evidence-only tests, adapted to the v0.6 scope-binding record schema, and ADDS named adversarial regression tests that reproduce each of the three F-P5-1 attacks and assert the corrected outcome. The decision-rules, power-simulation and verifier suites are unchanged from v0.5 and are carried in the release packet as lineage.

---

### R0391 -- test_shvvp_v0_8_1_phase_a.txt — test_shvvp_v0_8_1_phase_a.py -- Adversarial test suite for SHVVP v0.8.1.
- **Date:** Undated
- **Source:** test_shvvp_v0_8_1_phase_a.txt
- **Size:** 529 lines, 18,380 chars
- **SHA-256:** `d8f24c36d02fefd0...`

**Structure:**
  - ===================================================================
  - FIXTURES
  - ===================================================================
  - ===================================================================
  - M3 OBSERVATION TESTS
  - ===================================================================
  - ===================================================================
  - SHARED SET AND PAIRED DIFFERENCES
  - ===================================================================
  - ===================================================================
  - T2 POINT STATISTICS
  - ===================================================================
  - Median of [0, 40, 50, 75, 170] = 50
  - Median of ratios [0.0, 0.333..., 0.625, 0.667..., 0.850] = 0.625
  - ===================================================================

**Key Concepts:** SHVVP, FIXTURES, SEED, BUDGET, MET, OBSERVED, OBSERVATION TESTS, SHARED SET AND PAIRED DIFFERENCES

**Content Summary:**
- source_format: txt - text_sha256: d8f24c36d02fefd09486ddd8e2ea4e5da0eebde87e83ee8c58d63ea0af22e479
""" test_shvvp_v0_8_1_phase_a.py -- Adversarial test suite for SHVVP v0.8.1.
Covers: - Every PA-Z rule (PA-Z1 through PA-Z8) - T2 computation on a hand-constructed 5-fact shared set - T3 computation on the same 5-fact set - BCa-to-percentile fallback (PA-Z2, PA-Z5) - Censoring direction verification - Seed reproducibility - Caller-supplied statistic rejection - Input validation (non-numeric, negative, NaN, infinity)

---

### R0392 -- test_shvvp_v0_8_2_phase_a.txt — test_shvvp_v0_8_2_phase_a.py -- Adversarial test suite for SHVVP v0.8.2.
- **Date:** Undated
- **Source:** test_shvvp_v0_8_2_phase_a.txt
- **Size:** 648 lines, 25,282 chars
- **SHA-256:** `d546d1e3c1d9bb9f...`

**Structure:**
  - ===================================================================
  - HELPERS
  - ===================================================================
  - ===================================================================
  - INPUT VALIDATION
  - ===================================================================
  - ===================================================================
  - CENSOR-STATUS CONSISTENCY (F-K3-A3, F-K3-A5, F-K3-A10)
  - ===================================================================
  - ===================================================================
  - M3-FIRST: OBSERVED-ONLY (F-K3-A3)
  - ===================================================================
  - M3-FIRST should be 60 (the observed one), not 10 (censored)
  - ===================================================================
  - S-MEMBERSHIP: OBSERVED-SHARED-ONLY (F-K3-A1)

**Key Concepts:** SHVVP, GPT, FIRST, BUDGET, SOL, FROZEN, MINUTES, CORPUS, SIZE, SEED

**Content Summary:**
- source_format: txt - text_sha256: d546d1e3c1d9bb9fc927e7c365a24c9183590e86cc4b3b37c7b8f03d14ba9e06
""" test_shvvp_v0_8_2_phase_a.py -- Adversarial test suite for SHVVP v0.8.2.
Addresses every test-coverage gap identified by GPT Sol and Kimi K3: F-K3-B10: PA-Z4, PA-Z5, PA-Z7, evaluable-T7, non-degenerate-T4, z0-undefined, fabricated-delta rejection all have fixtures. F-K3-A6:  Provenance enforcement tested. F-K3-B5:  NaN resample handling tested. F-K3-B4:  z0-undefined tested. F-K3-B7:  Cardinality enforcement tested. F-K3-A1:  S-membership observed-only tested. F-K3-A2:  Censoring exclusion from S tested. F-K3-A3:  M3-FIRST observed-only tested. F-K3-A4:  All-zero relative gate tested. F-K3-A5:  BUDGET frozen tested. F-SOL-081-3: Censored non-discovery excluded from S. """

---

### R0393 -- test_shvvp_v0_8_3_phase_a.txt — test_shvvp_v0_8_3_phase_a.py -- Adversarial test suite for SHVVP v0.8.3.
- **Date:** Undated
- **Source:** test_shvvp_v0_8_3_phase_a.txt
- **Size:** 429 lines, 17,894 chars
- **SHA-256:** `a6a050b85af192b3...`

**Structure:**
  - ===== INPUT VALIDATION =====
  - ===== CENSOR CONSISTENCY =====
  - ===== M3-FIRST =====
  - ===== S-MEMBERSHIP: OBSERVED-SHARED-ONLY =====
  - ===== PAIRED DIFFERENCES + PROVENANCE =====
  - ===== PA-Z1: S empty =====
  - ===== PA-Z2: |S|=1 =====
  - ===== PA-Z3: T5 =====
  - ===== PA-Z5: sum_sq=0 with valid z0 -- Kimi's [1,5,5,5,9] fixture =====
  - Golden vector
  - ===== PA-Z6: all-identical resample (kept, counted) =====
  - ===== PA-Z7: T4 union-empty =====
  - ===== PA-Z8: T7 not computable =====
  - ===== PA-Z9: all-zero relative =====
  - ===== PA-Z10: z0-undefined =====

**Key Concepts:** SHVVP, FROZEN, BUDGET, MINUTES, CORPUS, SIZE, SEED, OBSERVED, INPUT VALIDATION, CENSOR CONSISTENCY

**Content Summary:**
- source_format: txt - text_sha256: a6a050b85af192b39399756fb5aacdcf2a09023c0d9dee099857750be3c1e2fb
""" test_shvvp_v0_8_3_phase_a.py -- Adversarial test suite for SHVVP v0.8.3.
Covers all PA-Z rules (PA-Z1 through PA-Z12), golden vectors for every statistic, and every gap identified by both v0.8.2 carrying seats.

---

### R0394 -- test_shvvp_v0_8_4_phase_a.txt — test_shvvp_v0_8_4_phase_a.py -- Adversarial test suite for SHVVP v0.8.4.
- **Date:** Undated
- **Source:** test_shvvp_v0_8_4_phase_a.txt
- **Size:** 400 lines, 16,372 chars
- **SHA-256:** `c7358ba6fcbc40a9...`

**Structure:**
  - === INPUT VALIDATION ===
  - === IMMUTABILITY (F-SOL-083-1) ===
  - === CENSOR CONSISTENCY ===
  - === M3-FIRST ===
  - === S-MEMBERSHIP ===
  - === PROVENANCE ===
  - === PA-Z1 ===
  - === PA-Z2 ===
  - === PA-Z3 ===
  - === PA-Z5 ===
  - === PA-Z6 ===
  - === PA-Z7 (named via T4 zero-diff behavior) ===
  - === PA-Z8 ===
  - === PA-Z9 ===
  - === PA-Z10 ===

**Key Concepts:** SHVVP, CODE, LEVEL PA, FROZEN, BUDGET, MINUTES, CORPUS, SIZE, SEED, OBSERVED

**Content Summary:**
- source_format: txt - merged_variants: 3 (xz_protocol_phase_a_tests.py; xz_protocol_phase_a_tests.py.txt; xz_protocol_phase_a_tests.txt) - text_sha256: c7358ba6fcbc40a9451e79c8c5e7ecf64adb4dda827606b92bce54e296e51f55
""" test_shvvp_v0_8_4_phase_a.py -- Adversarial test suite for SHVVP v0.8.4.
Covers all CODE-LEVEL PA-Z rules (PA-Z1-Z3, PA-Z5-Z14; eleven rules). PA-Z4 (alpha undefined) is adjudication-layer and scoped out. Golden vectors pin exact bounds for T2-abs, T2-rel, T3, T4, T7, PA-Z2, PA-Z5, PA-Z10, PA-Z11, PA-Z14. """ import math, pytest, numpy as np from shvvp_v0_8_4_phase_a_m3 import ( CensorStatus, FROZEN_BUDGET_MINUTES, M3FirstResult, M3Observation, M3Vector, PairedDifference, PhaseAInputError, compute_median, compute_paired_differences, compute_shared_set, evaluate_t2_point, ...

---

### R0400 -- V34 ADJUDICATION -- CONVERGENCE ROUND 3
- **Date:** Undated
- **Source:** V34_ADJUDICATION_CONVERGENCE.md
- **Size:** 105 lines, 4,851 chars
- **SHA-256:** `8ec1515a89748bf8...`

**Structure:**
  - V34 ADJUDICATION -- CONVERGENCE ROUND 3
  -   Seat verdicts
  -   ZERO BLOCKERs -- THIRD CONSECUTIVE ROUND.
  -   The documentation-sync pattern
  -   Convergence ruling
  -   CONVERGENCE IS ACHIEVED.
  - Battery state (repair34 final):
  - What this convergence IS:
  - What this convergence IS NOT:

**Key Concepts:** ADJUDICATION, CONVERGENCE ROUND, GPT, ISSUES, FOUND, CRITICAL, SIGNIFICANT, MODERATE, NOTE, GLM

**Content Summary:**
- source_format: md - text_sha256: 8ec1515a89748bf876a973dd957fa711ae25b599ca8d38b3487c51e02253f082
| Seat | Verdict | Counts | |---|---|---| | GPT-5.6 | ISSUES-FOUND | 0 CRITICAL / 0 SIGNIFICANT / 1 MODERATE / 1 NOTE | | GLM-5.2 | **PASS** | 0 BLOCKER / 0 MAJOR / 0 MINOR / 4 INFO | | Kimi K2.6 | **PASS -- CONVERGENCE ACHIEVED** | 0 findings |
**GLM: PASS** (third consecutive). Zero findings at MINOR or above. CE174 independently verified load-bearing (revert -> RED, BaseException escapes). CE173 re-verified load-bearing. "No new finding at any severity was introduced this round. Convergence is achieved on the GLM seat."

---

### R0401 -- verifier_receipt.json
- **Date:** Undated
- **Source:** verifier_receipt.json
- **Size:** 137 lines, 4,403 chars
- **SHA-256:** `9e1b8042a7092f92...`

**Key Concepts:** PASS, ASCII, PDF, URL, JSON, HALTED, INCONCLUSIVE, DESIGN, VALIDITY, README

**Content Summary:**
- source_format: json - text_sha256: 9e1b8042a7092f9292abe7af5fce6bf0809077d81e74d1c8bc4fdb421a5214ab
[ { "gate": "G1", "status": "PASS", "detail": "40 members verified, manifest excludes itself" }, { "gate": "G2", "status": "PASS", "detail": "ASCII-only, zero long dashes, no doubled words, canonical brand, no placeholders, 19 controlled labels present" }, { "gate": "G3", "status": "PASS", "detail": "qpdf reports no syntax or stream encoding errors" }, { "gate": "G3b", "status": "PASS", "detail": "title, version and author parity across source and PDF; 38 pages" }, { "gate": "G4", "status": "PASS", "detail": "6 fonts, all embedded and subset" }, { "gate": "G5", "status": "PASS", "detail": "38 pages strictly monochrome, no ink outside the frame" }, { "gate": "G6", "status": "PASS", "detail"...

---

### R0403 -- verify_shvvp_v0_5.py — Independent verifier for the SHVVP v0.5 release packet.
- **Date:** Undated
- **Source:** verify_shvvp_v0_5.py
- **Size:** 1233 lines, 58,933 chars
- **SHA-256:** `6c38d9330bc202b0...`

**Structure:**
  - !/usr/bin/env python3
  - reproduction check (about 6 min)
  - ---------------------------------------------------------------- G1
  - ---------------------------------------------------------------- G2
  - ---------------------------------------------------------------- G3, G4
  - ---------------------------------------------------------------- G5
  - ---------------------------------------------------------------- G6
  - ---------------------------------------------------------------- G7, G7b
  - ---------------------------------------------------------------- G8
  - round 3 absorption strings
  - Phase B: every one of the eight labels defined and reachable in the order table
  - Phase C conjunct rows keep denominators and numeric thresholds
  - every route component row carries the frozen EVIDENCE fields
  - Phase B fixed values survive
  - ---------------------------------------------------------------- G9

**Key Concepts:** SHVVP, DEFAULT MODE IS VERIFY, ONLY, OPT, SHA, SUMS, ASCII, PDF, JSON, HALTED

**Content Summary:**
- source_format: py - text_sha256: 6c38d9330bc202b0f5e507ce34d6a817392b8b596f3bc3e46972e231e87aa897
#!/usr/bin/env python3 """Independent verifier for the SHVVP v0.5 release packet.
DEFAULT MODE IS VERIFY-ONLY: nothing is written, nothing is rebuilt, and no artifact in the packet is modified.

---

### R0405 -- verify_shvvp_v0_6_receipt.json
- **Date:** Undated
- **Source:** verify_shvvp_v0_6_receipt.json
- **Size:** 75 lines, 2,068 chars
- **SHA-256:** `5a77b22e3406db3c...`

**Key Concepts:** SHVVP, OOS, PDF

**Content Summary:**
- source_format: json - text_sha256: 5a77b22e3406db3ccd577a05bda98203a2ea32b9a6d3a0b69fa800812ddb9127
{ "artifact": "SHVVP v0.6 release", "manifest_sha256": "505bfc026b2896b5fbe65e5726874c95430838b86d431074c4946ace07d91831", "flagship_pdf_sha256": "37d0e5172a838b746798c23e79c1604e9c6afb96cea49f0b4c6da6c7a3793a1a", "flagship_pages": 56, "gates": [ { "name": "G1 manifest digest reproducible", "pass": true, "detail": "505bfc026b2896b5fbe65e5726874c95430838b86d431074c4946ace07d91831" }, { "name": "G2 manifest covers 11 components, R4-C universe = 216", "pass": true, "detail": "" }, { "name": "G3 F-P5-1 attacks a/b/c closed and R3 OOS preserved", "pass": true, "detail": "a=True b=True c=True r3=True" }, { "name": "G4 test_shvvp_v0_6_rules.py exits clean", "pass": true, "detail": "62 checks, 0 f...

---

### R0407 -- verify_shvvp_v0_7_receipt.json
- **Date:** Undated
- **Source:** verify_shvvp_v0_7_receipt.json
- **Size:** 76 lines, 2,327 chars
- **SHA-256:** `145b53f2746e175a...`

**Key Concepts:** SHVVP, OOS, INCOMPLETE, PDF

**Content Summary:**
- source_format: json - text_sha256: 145b53f2746e175a66e3788c98668704877092a003ad520100752bb0cf26f910
{ "artifact": "SHVVP v0.7 release", "manifest_sha256": "667753069e360da59f7e3ac68c4bd2f6eef86896aa94f77e56d843babc5e3eab", "commitment_authority_pubkey": "3b6a27bcceb6a42d62a3a8d02a6f0d73653215771de243a63ac048a18b59da29", "flagship_pdf_sha256": "5d20b56e122a38fa447ab9e7058e47e68b09cb45ae97a0ac7a5511f58e0370ba", "flagship_pages": 59, "gates": [ { "name": "G1 manifest digest reproducible and binds authority+version", "pass": true, "detail": "667753069e360da59f7e3ac68c4bd2f6eef86896aa94f77e56d843babc5e3eab" }, { "name": "G2 manifest covers 11 components, R4-C=216, one predeclared OOS", "pass": true, "detail": "" }, { "name": "G3 F-P6-1 self-seal closed inline (subset/forge/missing/smuggle rej...

---

## Cross-Paper Themes

**Recurring Concepts (appearing in multiple papers):**
  - shvvp: 20 papers
  - pass: 9 papers
  - sha: 8 papers
  - budget: 7 papers
  - observed: 7 papers
  - gpt: 7 papers
  - frozen: 7 papers
  - pdf: 7 papers
  - first: 6 papers
  - censored: 6 papers
  - early: 6 papers
  - right: 6 papers
  - realized: 6 papers
  - sealed: 6 papers
  - corpus: 5 papers
  - size: 5 papers
  - minutes: 5 papers
  - manifest: 5 papers
  - accident guard: 4 papers
  - sol: 4 papers

**Date Range:** Undated to Undated

**Source Formats:** json(3), md(6), py(4), txt(9)

## Key Findings

(See per-paper summaries above for detailed findings per paper.)

## Connections to Other Sections

**Cross-references found:** bayyinah, bssg, shv

# Bismillah ir-Rahman ir-Rahim
