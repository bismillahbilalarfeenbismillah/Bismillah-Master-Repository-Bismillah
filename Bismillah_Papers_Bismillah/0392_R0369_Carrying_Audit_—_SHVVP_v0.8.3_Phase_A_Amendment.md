# Bismillah ir-Rahman ir-Rahim

# R0369 -- Carrying Audit — SHVVP v0.8.3 Phase A Amendment

**Chronological Index:** 392 of 995  
**Date:** 2026-07-31  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** SHVVP_v0_8_3_GPT_5_6_SOL_AUDIT.txt  
**Source Format:** txt  
**SHA-256:** `4246c0f8e7fb46fc7dd34f591cae78cadece6fe1e0dd52851dc3d685cd867833`  

---

## R0369 · Carrying Audit — SHVVP v0.8.3 Phase A Amendment

- section: V. BSSG & SHVVP Protocols
- source_file: SHVVP_v0_8_3_GPT_5_6_SOL_AUDIT.txt
- source_format: txt
- text_sha256: 4246c0f8e7fb46fc7dd34f591cae78cadece6fe1e0dd52851dc3d685cd867833

# Carrying Audit — SHVVP v0.8.3 Phase A Amendment

**Seat:** GPT-5.6 Sol — requested carrying seat 1 of 2
**Dispatch:** `DISPATCH_PROMPT_GPT_v083.md` (2026-07-31)
**Supersedes:** v0.8.2 (HALTED by both seats), v0.8.1 (HALTED by both seats)
**Author of record:** Bilal Syed Arfeen (BayyinahEnterprise)
**Producer seat:** Claude Opus 4.6 (advisory, non-carrying)
**Audit date:** 2026-07-31

---

## 1. Executive verdict

# **HALT**

SHVVP v0.8.3 is **not deposit-ready**.

This is a narrow HALT over a genuinely improved package. The mechanical gate is clean and the statistical core is, in my assessment, now materially correct:

- all three dispatched SHA-256 digests match exactly;
- the shipped suite reports **67/67 GREEN**;
- **all six dispatch-named golden vectors reproduce bit-exactly** under independent reconstruction from raw inputs, using the public API only;
- a randomized invariant fuzz over the public interval API — 360 generated cases yielding 554 checked intervals — found **zero** violations of interval ordering, `excludes_zero` consistency, NaN-freedom, fallback-reason coherence, or seed determinism;
- of the fourteen dispatch-named findings, **eight are fully discharged, four discharged in part, and two partly unverifiable** for want of the amendment text — **none is flatly not discharged** (§5) — and the two headline v0.8.2 complaints, phantom golden vectors (F-K3-N3) and unenforced corpus cardinality (F-SOL-082-4), are discharged decisively.

What blocks deposit is not the bootstrap. It is the **input boundary**, and it is the same defect the v0.8.2 GPT-5.6 Sol seat rated HIGH-BLOCKING as **F-SOL-082-2**. That finding is **absent from the v0.8.3 repair list and remains fully live**:

1. **`censor_status` enum membership is never validated.** Passing the *string* `"OBSERVED"` produces an accepted `M3Observation` whose `is_observed` is `False` — the fact is silently deleted from the shared set S. Passing `"RIGHT_CENSORED_BUDGET"` or `"CENSORED_EARLY"` as strings bypasses **every** censor-consistency invariant, *including the 480-minute budget rule that F-K3-N5 was raised specifically to enforce*. The F-K3-N5 repair is therefore defeated by one line of the same type-confusion class it was written to close.
2. **`M3Vector.observations` remains a public mutable list.** Direct `.append()` bypasses duplicate-ID and condition-match validation, and no pipeline entry point revalidates. Demonstrated end-to-end: |S| moves 1 → 3 and the absolute median moves 0.0 → 195.0, producing **genuine-token** paired differences from an unvalidated vector. `M3Vector.__post_init__` (the F-K3-N14 repair) closes the constructor door while the mutation door stands open.

Two further gating problems:

3. **A false coverage claim of the exact species that halted v0.8.2.** `intervals.py` declares "Degeneracy rules: PA-Z1 through PA-Z12 (twelve rules)" and the test file declares "Covers all PA-Z rules (PA-Z1 through PA-Z12)". **PA-Z4 has zero occurrences across all three shipped files**, and no `TestPAZ4` exists — a regression from v0.8.2, which at least shipped a proxy. PA-Z7 is likewise named nowhere in the implementation. This is precisely the "normative text makes executed-false claims about its own artifacts" defect over which Kimi K3 halted v0.8.2 (F-K3-N2), reproduced in the version that claims to repair it.
4. **The v0.8.3 amendment normative text is not in the dispatch.** v0.8.2 carried four normative files; the v0.8.3 manifest lists three, all Python. Roughly half the claimed repairs (§5/PA-A8 downgrade, §3 rule-table restoration, the §3 PA-Z5 note, §2.4 guard documentation, the §6 coverage ledger and digest table) live in an artifact I was never given. **A carrying seat cannot discharge a finding against an artifact absent from the manifest.**

Under the amendment's own acceptance rule — text and code are the same rule written twice, and a divergence is a defect — and under the inherited carrying rule that any carrying-seat HALT blocks deposit, v0.8.3 cannot be deposited from these bytes.

**PASS-WITH-AMENDMENTS is unavailable** for the reason Kimi K3 gave for v0.8.2 and which still holds: every required repair modifies normative bytes, which forces new hashes and a new version. The repair set below is small and mechanical. None of it requires redesign.

---

## 2. Scope, provenance, and seat-identity limits

**Read this section before relying on the verdict.**

- **Single seat, single family.** This audit is the requested **GPT-5.6 Sol seat only**. It is **not** two-family carrying convergence and must not be represented as such. Seat 2 (Kimi K3) has not reported on v0.8.3. No deposit decision should cite this document as satisfying the two-seat rule.
- **Execution topology.** **The audit used exactly one GPT-5.6 Sol agent; no additional agent, model, or council was consulted**, per dispatch constraint. That single agent was launched by the orchestrator to occupy this seat, and all analysis, attack authorship, and adjudication are its own; no step required another model. This states the execution topology only — one agent, one model family — and is not a claim of multi-family review. See the single-seat limit above.
- **Carry is limited to the checks executed.** This is not peer review, not a mathematical proof of the BCa estimator, and not a statistical validation of the protocol's inferential claims.
- **Dispatch package contents.** Three normative Python files, the dispatch prompt, the two prior v0.8.2 audits, and three parent PDFs (`SHVVP_v0_8_flagship.pdf`, `SHUDP_v0_5_flagship.pdf`, `BSSG_PAPER.pdf`). I confirmed by text extraction that **all three PDFs contain zero `PA-Z` and zero `PA-A` tokens** — they are parent documents, not the amendment. The v0.8.3 amendment text does not exist in this dispatch.
- **Prior audits treated as evidence, not authority.** Every load-bearing claim from the GPT-5.6 Sol v0.8.2 verdict and the Kimi K3 v0.8.2 audit that I relied on was independently re-executed against the v0.8.3 bytes. Where a prior claim did not reproduce, I recorded it as discharged.
- **Original artifacts untouched.** All execution ran against a byte-identical copy at `/tmp/shvvp_run` (hashes re-verified post-copy). `/home/user/workspace/SHVVP_v0_8_3_DISPATCH_GPT` was never written to; no `__pycache__` or `.pytest_cache` was created there, and file timestamps are unchanged. Attack scripts live in `/tmp/shvvp_attacks`.

### 2.1 Environment deviation (material — read carefully)

The shipped modules pin **Python 3.12.x, numpy 2.4.x, scipy 1.17.x**. The available environment is:

```text
Python 3.14.3
numpy  2.5.1
scipy  1.18.0
pytest 9.1.1
```

All three components are **above** the declared pin, and I was unable to install the pinned versions. This cuts two ways, and both directions must be stated:

- **Positive:** the suite is 67/67 GREEN and **all six golden vectors reproduce bit-exactly** across a minor-version upgrade of both numerical dependencies and two Python minor versions. This is stronger evidence for drift-resistance than testing under the pin would have been, and it directly refutes the v0.8.2 condition Kimi demonstrated, where a percentile perturbation left the suite green.
- **Limitation:** I did **not** verify behaviour under the declared pin, and I cannot confirm that the vectors would fail under a *downgrade* or under a PRNG-stream change. The golden-vector gate's protective claim is therefore corroborated but not exhaustively demonstrated.

---

## 3. Manifest

### 3.1 Hash verification — **MATCH (3/3)**

```console
$ cd /home/user/workspace/SHVVP_v0_8_3_DISPATCH_GPT && sha256sum \
    shvvp_v0_8_3_phase_a_m3.py shvvp_v0_8_3_phase_a_intervals.py \
    test_shvvp_v0_8_3_phase_a.py

abea69606e08298607fa641d77bf1d2ae595f2167072cb7d96b03efcb6794fee  shvvp_v0_8_3_phase_a_m3.py
17e801fbb97462269ed0764c9de99bc38c6cebff73f957b23a782e4c8b7a0f03  shvvp_v0_8_3_phase_a_intervals.py
828c83e408b86ffba67d3d2f3007b49153c0d7a72becee69cfab679dc0b02fa6  test_shvvp_v0_8_3_phase_a.py
```

Verified against the dispatch manifest with `sha256sum -c`:

```text
shvvp_v0_8_3_phase_a_m3.py: OK
shvvp_v0_8_3_phase_a_intervals.py: OK
test_shvvp_v0_8_3_phase_a.py: OK
```

All three digests are character-for-character identical to the dispatch. No transcription error of the F-K3-N15 species is present in the dispatch manifest itself.

### 3.2 Manifest completeness — **DEFECT (see F-SOL-083-4)**

The v0.8.2 manifest carried **four** normative files, including `shvvp_phase_a_amendment_v0_8_2.md`. The v0.8.3 manifest carries **three**, all Python. The amendment text is neither hashed nor shipped.

---

## 4. Reproduction

### 4.1 Shipped test suite — **67/67 GREEN**

```console
$ mkdir -p /tmp/shvvp_run && cp /home/user/workspace/SHVVP_v0_8_3_DISPATCH_GPT/*.py /tmp/shvvp_run/
$ cd /tmp/shvvp_run && sha256sum *.py          # re-verified byte-identical after copy
$ python3 -m pytest test_shvvp_v0_8_3_phase_a.py -q
```

```text
...................................................................      [100%]
67 passed in 6.36s
```

Verbose header:

```text
platform linux -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/shvvp_run
collected 67 items
```

The count matches the dispatch claim exactly. Run twice with identical results. Suite composition: 25 test classes spanning input validation, censor consistency, M3-FIRST, shared-set membership, paired differences and provenance, PA-Z1/2/3/5/6/7/8/9/10/11/12, evaluable T4 and T7, T3, full T2, seed validation, seed reproducibility, median, and the frozen budget.

---

## 5. Finding-discharge matrix

Every finding named in the dispatch, mapped with executed evidence. **D** = discharged, **DP** = discharged in part, **ND** = not discharged, **UV** = unverifiable in this dispatch.

| Finding | Claimed repair | Ruling | Evidence |
|---|---|---|---|
| **F-SOL-082-1** / **F-K3-N1** | Provenance downgraded to accident-guard | **D** (as reframed) + **UV** for the text | `m3.py:14-18` states the accident-guard limit and *names* `dataclasses.replace()` and direct token import as bypasses. Both reproduce exactly (§7 A-1), so the claim is now truthful. The §5/PA-A8 text downgrade is **UV** — text not shipped. Residue: my v0.8.2 disposition also required revalidating `delta == m3_a - m3_b`; not implemented (§7 A-2). |
| **F-SOL-082-4** | Empty T4/T7 = wrong cardinality | **D** | `t4_interval([])` → `PhaseAInputError: T4 requires exactly 200 artifacts, got 0`; `t7_interval([])` → `...exactly 240 items, got 0`. Full sweep 0/1/199/200/201 and 0/1/239/240/241 behaves correctly (§7 C-1). |
| **F-K3-N2** | PA-Z6 restored, twelve rules | **DP → gating** | PA-Z6 genuinely restored: named in the `intervals.py` cascade, counted via `n_degenerate_resample`, asserted by `TestPAZ6` (n=2 → 5078/10000 degenerate). **But** the twelve-rule claim is false in the shipped bytes: **PA-Z4 = 0 occurrences** in all three files, **PA-Z7 = 0 occurrences** in the implementation, no `TestPAZ4` exists. See **F-SOL-083-3**. |
| **F-K3-N3** | Golden vectors shipped | **D** (strong) | Exact numeric bounds now pinned for T2-abs, T3, T4, T7, PA-Z5, PA-Z10. All six independently reproduced bit-exactly (§6). Versions pinned in the docstring. Caveat: pins are prose, not a lock artifact, and are not asserted at runtime (**F-SOL-083-8**). |
| **F-K3-N4** | PA-Z9 `evaluable=False` aligned | **D** | Same all-zero-`M3(f,A)` fixture: `evaluate_t2_point` → `evaluable=False, rule='PA-Z9'`; `evaluate_t2_full` → `evaluable=False, rule='PA-Z9', t2_satisfied=None`. Aligned (§7 B-4). |
| **F-K3-N5** | OBSERVED ≤ budget enforced | **DP** | Enforced on the enum path: 480.0 accepted; `nextafter(480, inf)` = 480.00000000000006, 480.1, 481.0, 1000.0, 1e308 all rejected (§7 A-1). **Two gaps:** the at-480 ambiguity persists — OBSERVED-at-480 and RIGHT_CENSORED_BUDGET-at-480 remain both constructible with opposite S-membership; and the whole check is **bypassable via string `censor_status`** (§7 B-3), which defeats the repair. |
| **F-K3-N7** | LOO NaN named PA-Z12 | **D** | PA-Z12 named in the cascade, counted in `n_loo_nan_substitutions`, surfaced on `BootstrapResult`. I **demonstrated reachability** the producer was unsure of: T7 with 239 positives / 1 negative / ≥1 misclassified → `n_loo_nan_substitutions=1` (§7 C-3). Nonblocking: the shipped fixture is vacuous (**F-SOL-083-6**). |
| **F-K3-N9** | PA-Z5 note corrected, [1,5,5,5,9] fixture | **D** (code) + **UV** (text) | `TestPAZ5` now uses Kimi's fixture; PA-Z5 genuinely fires with `reason="PA-Z5: jackknife sum of squares is zero (n=5)..."`, bounds pinned [1.0, 9.0]. Independently reproduced (§6, GV5). The §3 post-table note correction is **UV** — text not shipped. |
| **F-K3-N13** | BCa guards documented | **D** | `intervals.py:17-21` documents both guards under "BCa numerical guards (documented, not silent)". Verified latent: neither reached on any golden vector nor in the 554-interval fuzz; requested percentile levels stayed far inside the clamp bounds (§7 C-4). Nonblocking residue: if reached they still emit no `fallback_reason` and no counter (**F-SOL-083-7**). |
| **F-K3-N14** | M3Vector constructor validates | **DP** | `__post_init__` validates duplicates *and* condition match; `M3Vector("A", observations=[o, o])` → `PhaseAInputError: Duplicate...`. **But** only the constructor door is closed — `observations` is still a public mutable list and direct `.append()` bypasses everything (§7 B-2). |
| **F-K3-N16** | Docstring corrected | **D** | `m3.py:11` reads "F-K3-N16: Docstring corrected (censoring analysis withdrawn, not re-derived)." Matches the amendment's stated disposition. |
| **F-K3-N17** | bool rejected | **DP** | Rejected for M3 `minutes` ("must be numeric (not bool)"), T4 flags, T7 labels, and seed. **Not** rejected for `evaluate_t5` M7 values — `evaluate_t5(True, 10.0)` → `ratio=10.0` — nor for `t3_interval` M4 differences — `t3_interval([True,False,True])` → `0.667`. Also `compute_median([True,False])` → `0.5` (§7 A-8, B-6). |
| **F-K3-N18** | Seed validated | **D** | `-1` → "Seed must be non-negative"; `1.5` → "Seed must be int, got float"; `True` → "got bool"; `"42"` → "got str"; `None` → "got NoneType". `0` and large ints accepted (§7 C-2). |

**Tally against the dispatch's fourteen: 8 discharged, 4 discharged in part, 2 partly unverifiable for want of the amendment text. Zero of the fourteen are flatly not discharged.**

*Counting convention (the fourteen names occupy thirteen rows, because F-SOL-082-1 and F-K3-N1 are the same finding under two labels):*

- **Discharged (8):** F-SOL-082-4, F-K3-N3, F-K3-N4, F-K3-N7, F-K3-N9, F-K3-N13, F-K3-N16, F-K3-N18. F-K3-N9 is counted here because its code limb is discharged outright and independently reproduced; only its §3 text-note limb is unverifiable, and it carries no live residue.
- **Discharged in part (4):** F-K3-N2, F-K3-N5, F-K3-N14, F-K3-N17.
- **Partly unverifiable (2):** F-SOL-082-1 and F-K3-N1 — the shared provenance row. Its code limb is truthful, but the §5/PA-A8 text downgrade is unshipped **and** it retains a live residue (`delta == m3_a - m3_b` never revalidated), which is why it is not counted as discharged.
- **Not discharged (0).**

### 5.1 Prior findings **omitted** from the dispatch that remain live

The dispatch's repair list silently drops three findings from the GPT-5.6 Sol v0.8.2 verdict. All were re-executed against v0.8.3.

| Finding | v0.8.2 severity | v0.8.3 status | Evidence |
|---|---|---|---|
| **F-SOL-082-2** — mutable vector, unvalidated censor state | HIGH-BLOCKING | **NOT DISCHARGED — reproduces in full** | §7 B-2, B-3, A-2, A-3. Now **F-SOL-083-1** and **F-SOL-083-2**. |
| **F-SOL-082-3** — M3 endpoint / adjudication authority | HIGH-BLOCKING | **NOT DISCHARGED** | Parent `SHVVP_v0_8_flagship.pdf` defines M3 as "Wall-clock minutes from corpus access to **first correctly adjudicated** consequential fact". The shipped code carries no adjudication object, no ledger, no timestamp source — only a caller-supplied `evidence_record_id` string, which is accepted as `""`, `0`, or `False`. Not repairable without the amendment text. **F-SOL-083-5**. |
| **F-SOL-082-5** — PA-Z4 and total Phase-A label | MEDIUM | **REGRESSED** | v0.8.2 shipped a proxy `TestPAZ4`; v0.8.3 removed it and PA-Z4 entirely, while *raising* the coverage claim to twelve rules. **F-SOL-083-3**. |

For completeness, the remaining v0.8.2 findings not named in the dispatch: **F-SOL-082-6** (environment lock) is substantially repaired by the golden vectors, residual **F-SOL-083-8**; **F-SOL-082-7** is discharged on both limbs (PA-Z5 fixture now real; BCa branches now documented); **F-SOL-082-8** is discharged (= F-K3-N4). Kimi's **F-K3-N6** (|S|=1 vacuous gate), **F-K3-N8** (PA-Z2 vs PA-Z11 zero-width divergence), and **F-K3-N12** (T3 has no provenance) all reproduce and are carried below as nonblocking.

---

## 6. Golden vectors — independent verification

Reconstructed from raw inputs through the public API in a standalone script (`/tmp/shvvp_attacks/gv_verify.py`) that **does not import the shipped test module**. Full-precision outputs:

| # | Vector | Dispatch expectation | Observed | Result |
|---|---|---|---|---|
| GV1 | T2 5-fact absolute | `abs_lo=0.0, abs_hi=75.0, BCa, t2_satisfied=False` | `lower=0.0`, `upper=75.0`, `BCa`, `t2_satisfied=False` | **MATCH** |
| GV2 | T3 5-fact | `lo=0.8, hi=5.8, BCa` | `lower=0.8`, `upper=5.8`, `BCa` | **MATCH** |
| GV3 | T4 200-item | `lo=-0.005, hi=0.105, BCa` | `lower=-0.0049999999999999906`, `upper=0.10499999999999998`, `BCa` | **MATCH** (1e-6) |
| GV4 | T7 240-item imperfect | `lo=0.7716, hi=0.9120, BCa` | `lower=0.7716350602906202`, `upper=0.912029630366201`, `BCa` | **MATCH** (1e-4) |
| GV5 | PA-Z5 `[1,5,5,5,9]` | `lo=1.0, hi=9.0, PERCENTILE, PA-Z5` | `lower=1.0`, `upper=9.0`, `PERCENTILE_FALLBACK`, reason `PA-Z5: jackknife sum of squares is zero (n=5); acceleration undefined; declared percentile reversion` | **MATCH** |
| GV6 | PA-Z10 `[0,0,1]` | `lo=0.0, hi=1.0, PERCENTILE, PA-Z10` | `lower=0.0`, `upper=1.0`, `PERCENTILE_FALLBACK`, reason `PA-Z10: z0 undefined (prop_below=0.0); declared percentile reversion` | **MATCH** |

**All six verified.** Supporting values also confirmed: GV1 `absolute_median=50.0` (gate met), `relative_median=0.625` (gate met), relative interval `[0.0, 0.6666666666666666]`; the `t2_satisfied=False` outcome is correctly driven by the absolute interval failing to exclude zero, not by a gate failure. GV3/GV4 exhibit `n_degenerate_resample=0` as expected at n=200/240; GV6 shows 1061 degenerate resamples at n=3, correctly counted under PA-Z6.

Internal seed chain confirmed as documented: T2-abs `seed+0`, T2-rel `+1`, T3 `+2`, T4 `+3`, T7 `+4` (observed 42/43/44/45/46).

---

## 7. Adversarial testing

Five independent attack scripts (A–E) beyond the shipped suite, in `/tmp/shvvp_attacks/`, alongside the separate golden-vector reconstruction `gv_verify.py` used in §6. No producer artifact was altered.

### A. Boundaries and type confusion (`attack_a_boundary.py`)

- **A-1 Budget boundary — clean.** OBSERVED at 479.999 and 480.0 accepted; 480.0000001, `nextafter(480,inf)`, 480.1, 481.0, 1000.0, 1e308 all rejected with the correct message. The boundary is frozen inclusive as the test declares.
- **A-2 `censor_status` type confusion — DEFECT.** Enum membership is never checked. See B-3.
- **A-3 `evidence_record_id` hygiene — DEFECT.** OBSERVED accepted with `evidence_record_id=""`, `=0`, and `=False`, all yielding `is_observed=True`. RIGHT_CENSORED_BUDGET accepted *with* an evidence ID. My v0.8.2 disposition explicitly required forbidding evidence IDs on non-discoveries and validating ID type/non-emptiness. Neither done.
- **A-4 Numeric types.** `np.float64` accepted but `np.int64` rejected — asymmetric, though safe. `Decimal`, `Fraction`, `str`, `complex`, `np.bool_` correctly rejected. `int`/`float` subclasses accepted (unavoidable under `isinstance`). `-0.0` and subnormals accepted.
- **A-5 Fact-ID normalization — correct.** Whitespace stripped, case-sensitive as frozen. `"f1"` vs `"  f1  "` correctly collides and is rejected as a duplicate within a vector; cross-vector `" f1 "`/`"f1"` correctly pairs to `delta=70.0`. Whitespace-only and empty rejected. Unicode zero-width and NBSP are *not* stripped — correct under a frozen minimal canonical form, worth one line of disclosure.
- **A-6 Vector conditions — correct.** Constructor rejects mismatched observations; `compute_paired_differences` rejects (B,A) and (A,A).
- **A-7 `compute_median`.** Accepts `[True, False]` → 0.5 and `[nan,1,2]` → 1.0 silently. Not reachable through validated paths; nonblocking.
- **A-8 `evaluate_t5`.** `evaluate_t5(True, 10.0)` accepted → bool not rejected for M7. Boundary `ratio == 1.25` correctly does **not** fire (strict `>`).

### B. Provenance, mutability, evaluator state (`attack_b_provenance.py`)

- **B-1 Provenance bypasses — live and disclosed.** From genuine deltas `[10,12,8]` (`t2_satisfied=False`), `dataclasses.replace(d, m3_a=100.0, m3_b=0.0, delta=100.0)` preserves the token, passes `verify_provenance()`, and drives **`t2_satisfied=True`**. Direct fabrication with the imported `_PROVENANCE_TOKEN`, `pickle` round-trip, and `copy.deepcopy` all pass the gate. **This is now correctly disclosed** in the module docstring, so it is not scored as a false claim. NaN/Inf deltas *are* caught downstream ("Statistic on full data is nan; non-finite input rejected").
- **B-2 Vector mutation — DEFECT (F-SOL-083-1).** `M3Vector` is a non-frozen dataclass with a public list. Direct append of a duplicate `f1` gives `len(observations)=2` with `all_fact_ids={'f1'}` and `get()` silently returning the first. Direct append of a condition-B observation into an A vector is accepted. End-to-end: |S| 1 → 3, `absolute_median` 0.0 → 195.0, deltas `[0.0, 195.0, 204.0]`, all bearing genuine provenance. `compute_shared_set` does not revalidate.
- **B-3 String `censor_status` — DEFECT (F-SOL-083-2).** All four probes accepted:

  ```text
  M3Observation("h1","A",100.0,"OBSERVED",evidence_record_id="e1")
      -> accepted; is_observed=False; shared set = []  (fact silently dropped)
      -> m3_first(A) = M3FirstResult.NO_DISCOVERY
  M3Observation("h2","A",100.0,"RIGHT_CENSORED_BUDGET")
      -> accepted at 100.0 min; invariant requires == 480.0
  M3Observation("h3","A",500.0,"CENSORED_EARLY")
      -> accepted at 500.0 min; invariant requires < 480.0
  M3Observation("h4","A",500.0,"OBSERVED")
      -> accepted at 500 min with no evidence id; is_observed=False
  ```

  Every censor-consistency invariant — including the F-K3-N5 budget rule — is defeated by passing a string where an enum is expected. The failure is **silent** and changes S-membership, hence T2.
- **B-4 PA-Z9 cross-API — aligned.** Both evaluators report `evaluable=False, rule='PA-Z9'`, both `absolute_median=-30.0`. F-K3-N4 discharged.
- **B-5 `t2_satisfied` transitions.** |S|=1, delta=35 → zero-width interval [35.0, 35.0], `excludes_zero=True`, **`t2_satisfied=True` on a single observation** (F-K3-N6, still live). The three-valued `all`/`any` logic is sound but its `None` branch is dead code: at that point both gates and `interval_excludes` are always non-`None`.
- **B-6 T3 provenance scope.** `t3_interval` accepts any caller-supplied list of any length with no token and no tie to |S| (F-K3-N12, still live).

### C. Cardinality, seeds, degeneracy reachability (`attack_c_stats.py`)

- **C-1 Cardinality — fully enforced** for 0/1/199/200/201 and 0/1/239/240/241. Malformed *shapes*, however, escape as raw exceptions rather than `PhaseAInputError`: arity-3 T4 tuples → `ValueError: too many values to unpack`; non-tuple items → `TypeError`; a generator → `TypeError: object of type 'generator' has no len()`. Also `(0.0, 1.0)` floats and `np.int64` flags are accepted because `0.0 in (0,1)` is true.
- **C-2 Seeds — validated and deterministic.** All invalid forms rejected with `PhaseAInputError`. Same-process repeats bit-identical. Noted: the fixed `+0..+4` offset chain means `t2_absolute_interval(ds, 44)` and `t3_interval(x, 42)` share internal seed 44 — harmless here (different data ⇒ different bounds, confirmed) but a latent stream-collision if a caller ever seeds per-statistic.
- **C-3 PA-Z12 reachable.** 297 T7 configurations swept. `n_loo_nan_substitutions=1` at **239 positives / 1 negative with ≥1 misclassified positive** (removing the single negative empties the negative class ⇒ specificity NaN ⇒ theta substitution). Reproduced at seeds 0, 42, 7. Example receipt: `point=0.997907949790795, BCa, [0.987608467238244, 1.0], n_loo_nan_substitutions=1, n_nan=3606, n_valid=6394`.
- **C-4 BCa guards latent.** Instrumented `np.percentile` to capture requested levels. On all four golden vectors, levels ranged 0.25–97.24 against clamp bounds (0.0050, 99.9950) — never at the clamp. Consistent with Kimi's 600-case F-K3-B6 result.
- **C-5 PA-Z6 counted.** n=2 → 5078/10000; n=5 → 18. Correct magnitudes.
- **C-6 PA-Z4 absent.** Zero occurrences across all three files.
- **C-7 PA-Z11 exhaustion unreached.** The counting path is well exercised (up to 3785 NaN resamples); the `n_valid < 2` branch was not reached in 297 targeted configurations plus the 360-case fuzz. Not proven unreachable.

### D. Randomized invariant fuzz (`attack_d_fuzz.py`)

360 generated cases — 220 T2 (n ∈ {1,2,3,4,5,7,11,20}), 60 T3, 40 T4, 40 T7 — with adversarial mixes of zeros, ties, and duplicates. These yield **554 checked intervals**, since each T2 case contributes both an absolute and a relative interval where defined; the 554 is the sum of the method distribution below (359 + 195).

```text
method distribution:  {'BCa': 359, 'PERCENTILE_FALLBACK': 195}
fallback-reason rules: {'None': 359, 'PA-Z2': 107, 'PA-Z5': 63, 'PA-Z10': 25}

order        violations: 0     (lower <= upper)
excl         violations: 0     (excludes_zero consistent, incl. PA-Z2/PA-Z11 special cases)
nan          violations: 0
determinism  violations: 0
reason       violations: 0     (BCa never carries a reason; PERCENTILE always does)

FUZZ RESULT: NO INVARIANT VIOLATIONS
```

Also asserted per-case and never violated: `t2_satisfied is True` implies both gates met **and** interval excludes zero; `rule == "PA-Z9"` implies `evaluable is False`.

### E. Coverage-claim audit (`attack_e_coverage.py`)

| Rule | Named in impl. | In tests | `TestPAZ`n class | Rule name asserted |
|---|---|---|---|---|
| PA-Z1 | 5 | 3 | yes | yes |
| PA-Z2 | 4 | 2 | yes | yes |
| PA-Z3 | 2 | 2 | yes | yes |
| **PA-Z4** | **0** | **0** | **NO** | **no** |
| PA-Z5 | 3 | 3 | yes | yes |
| PA-Z6 | 4 | 3 | yes | yes |
| **PA-Z7** | **0** | 1 | yes | no |
| PA-Z8 | 2 | 1 | yes | no |
| PA-Z9 | 7 | 3 | yes | yes |
| PA-Z10 | 3 | 5 | yes | yes |
| PA-Z11 | 5 | 1 | yes | no |
| PA-Z12 | 6 | 4 | yes | no |

`TestPAZ12`'s three assertions are `r is not None`, `hasattr(r, 'n_loo_nan_substitutions')`, and `r.n_loo_nan_substitutions >= 0` — the last vacuously true for every run. The test's own comments concede PA-Z12 does not fire in its fixture.

### Attack-tool limitations

Stated so the next seat can close them:

1. Ran above the declared dependency pin (§2.1); behaviour under the pin and under downgrade is unverified.
2. The BCa `denom < 1e-15` guard was probed by sampling and instrumentation, **not proven unreachable**.
3. The PA-Z11 `n_valid < 2` exhaustion branch was not reached; not proven unreachable.
4. No amendment text ⇒ **no text/code divergence check was possible** for the majority of claimed repairs. This is the single largest gap in this audit.
5. Fuzz used one master seed (20260731); the search is not exhaustive.
6. No independent from-text BCa reference implementation was written this round, so I did not repeat Kimi's bit-exactness cross-check. I verified internal consistency and the shipped golden vectors instead.

---

## 8. Findings by severity

### 8.1 Blocking

---

**F-SOL-083-1 | HIGH — BLOCKING | `m3.py` `M3Vector` (lines 177-213) | Vector remains mutable; validation bypassable; pipeline never revalidates**

`M3Vector` is a non-frozen dataclass exposing `observations` as a public list. `__post_init__` (the F-K3-N14 repair) and `add()` both validate, but direct mutation bypasses both, and no pipeline entry point revalidates. Executed: duplicate `f1` appended directly gives `len=2` with `all_fact_ids={'f1'}` and `get()` shadowing the second; a condition-B observation is accepted into an A vector; end-to-end |S| 1 → 3 with `absolute_median` 0.0 → 195.0, all deltas carrying genuine provenance tokens.

*Prior identity:* F-SOL-082-2, rated HIGH-BLOCKING in the v0.8.2 GPT-5.6 Sol verdict; omitted from the v0.8.3 repair list.

*Disposition:* Make the vector immutable (frozen dataclass over a tuple), or revalidate the full vector at every pipeline entry (`compute_shared_set`, `compute_paired_differences`). Add fixtures for post-construction mutation.

---

**F-SOL-083-2 | HIGH — BLOCKING | `m3.py` `M3Observation.__post_init__` (lines 131-165) | `censor_status` enum membership never validated; defeats the F-K3-N5 repair**

Every censor rule is expressed as `if self.censor_status == CensorStatus.X`. A raw string is never equal to an enum member, so all comparisons fall through and all invariants are skipped. Executed:

```text
"OBSERVED" (str) + evidence id     -> accepted, is_observed=False, fact dropped from S
"RIGHT_CENSORED_BUDGET" @ 100 min  -> accepted (invariant requires exactly 480.0)
"CENSORED_EARLY" @ 500 min         -> accepted (invariant requires < 480.0)
"OBSERVED" @ 500 min, no evidence  -> accepted
```

The first case is the most dangerous: it is a **silent** downgrade of an intended discovery to a non-discovery, changing S-membership and therefore T2, with no error anywhere. The second and third defeat **F-K3-N5**, the budget enforcement this version was dispatched to add. Related, same locus: `evidence_record_id` is accepted as `""`, `0`, and `False` on OBSERVED, and is accepted *on non-discoveries*.

*Prior identity:* F-SOL-082-2, first sub-defect, HIGH-BLOCKING in v0.8.2; omitted from the v0.8.3 repair list.

*Disposition:* `if not isinstance(self.censor_status, CensorStatus): raise PhaseAInputError(...)` as the first check. Forbid evidence IDs on non-discoveries; require a non-empty `str` on OBSERVED. Add fixtures for each string-valued status.

---

**F-SOL-083-3 | HIGH — BLOCKING | `intervals.py:15`; test file docstring line 4 | Twelve-rule coverage claim is executed-false; PA-Z4 absent and regressed**

`intervals.py` declares "Degeneracy rules: PA-Z1 through PA-Z12 (twelve rules)" and the test file declares "Covers all PA-Z rules (PA-Z1 through PA-Z12)". Executed by grep over all three shipped files: **PA-Z4 occurs zero times** and no `TestPAZ4` exists; **PA-Z7 occurs zero times in the implementation**. v0.8.2 at least shipped a proxy `TestPAZ4`; v0.8.3 deleted it while raising the coverage claim from eleven rules to twelve.

This is the F-K3-N2 defect species — false claims by the artifacts about the artifacts — reproduced in the version dispatched to repair F-K3-N2, and it is the species over which both seats halted v0.8.2.

*Disposition:* Either implement and test PA-Z4 (and name PA-Z7 in the implementation), or state explicitly that PA-Z4/PA-Z7 are adjudication-layer rules outside these modules and correct both coverage sentences to match what the bytes actually cover.

---

**F-SOL-083-4 | HIGH — BLOCKING (process) | Dispatch manifest | Amendment normative text absent from the package**

The v0.8.2 manifest carried four normative files including the amendment markdown; v0.8.3's carries three, all Python. The three PDFs are parent documents — verified to contain **zero** `PA-Z` and `PA-A` tokens. Consequently the §5/PA-A8 provenance downgrade, the §3 rule-table restoration and rule count, the §3 PA-Z5 note correction, the §2.4 guard documentation, and the §6 coverage ledger and digest table — a majority of the dispatch's claimed repairs — **cannot be audited at all**. The amendment's own governing rule ("text and code are the same rule written twice; a divergence is a defect") is unfalsifiable when only the code is shipped.

*Disposition:* Ship and hash the amendment text with the package. Re-dispatch with a four-file manifest.

---

**F-SOL-083-5 | HIGH — BLOCKING | Parent §5.2 M3; `M3Observation` schema | M3 endpoint and adjudication authority still unfrozen**

The parent flagship defines M3 as "Wall-clock minutes from corpus access to **first correctly adjudicated** consequential fact, per condition" (extracted and verified from `SHVVP_v0_8_flagship.pdf`). The shipped schema carries no adjudication object, no sealed-ledger reference, no immutable timestamp source, and no record-to-fact mapping authority — only an optional caller-supplied `evidence_record_id` string that is accepted empty or falsy. A record saved at minute 10 and correctly adjudicated at minute 60 yields M3 = 10 here and 60 under the parent, on a fully observed, non-censored input.

*Prior identity:* F-SOL-082-3, HIGH-BLOCKING in v0.8.2; omitted from the v0.8.3 repair list. Not closable without the amendment text.

*Disposition:* Freeze t=0, the evidence-record schema, the timestamp source, the mapping authority, and the correct-adjudication condition — or declare the endpoint change substantive and drop any scalar-preservation claim.

### 8.2 Nonblocking

- **F-SOL-083-6 | MEDIUM | `TestPAZ12`** — Vacuous fixture. Its operative assertion `n_loo_nan_substitutions >= 0` is true for every run and the comments concede PA-Z12 does not fire. A real trigger exists and is supplied above (239 pos / 1 neg / ≥1 misclassified → counter = 1); pin it as a golden vector.
- **F-SOL-083-7 | MEDIUM | `intervals.py` `_bca_q`, level clamping** — Both guards are now documented in the docstring but remain **silent at the result level**: no `fallback_reason`, no counter, no flag if they fire. Verified latent, so the risk is contingent. Give each a counter field on `BootstrapResult`, matching the PA-Z11/PA-Z12 discipline.
- **F-SOL-083-8 | MEDIUM | `intervals.py:12`** — Version pins are prose, not a lock artifact, and are not asserted at runtime. I ran above all three pins with no divergence, which is encouraging but means the stated gate is unenforced. Ship a lock file or add a version-assertion test.
- **F-SOL-083-9 | MEDIUM | `evaluate_t5`, `t3_interval`, `compute_median`** — F-K3-N17 (bool rejection) applied unevenly: `evaluate_t5(True, 10.0)` → `ratio=10.0`; `t3_interval([True,False,True])` → `0.667`; `compute_median([True,False])` → `0.5`. Apply the `isinstance(v, bool)` guard uniformly.
- **F-SOL-083-10 | MEDIUM | `t4_interval`, `t7_interval`** — Malformed *shape* escapes typed error handling: wrong tuple arity raises `ValueError`, non-tuple items `TypeError`, generators `TypeError: has no len()`. Cardinality is enforced but shape is not. Also `(0.0, 1.0)` and `np.int64` flags pass because `0.0 in (0,1)`. Wrap in `PhaseAInputError` and require exact `int`.
- **F-SOL-083-11 | LOW | F-K3-N5 residue** — The at-480 ambiguity persists: OBSERVED-at-480 and RIGHT_CENSORED_BUDGET-at-480 remain both constructible for the same minute with opposite S-membership, decided solely by the caller's enum choice.
- **F-SOL-083-12 | LOW | F-K3-N6, still live** — |S|=1 with delta=35 yields a zero-width interval that "excludes zero", so **T2 is satisfied on a single observation**. Disclose in PA-Z2 or bar T2-satisfied at |S|=1.
- **F-SOL-083-13 | LOW | F-K3-N8, still live** — PA-Z2 sets `excludes_zero=(theta != 0)`; PA-Z11 hard-codes `False`. Identical geometry, opposite gate verdict.
- **F-SOL-083-14 | LOW | F-K3-N12, still live** — `t3_interval` accepts caller-computed M4 differences of any length with no provenance and no tie to |S|. The provenance discipline covers T2 only.
- **F-SOL-083-15 | LOW | `evaluate_t2_full` lines 546-551** — The three-valued `all`/`any` construction's `None` branch is unreachable: both gates and `interval_excludes` are always non-`None` at that point. Harmless but misleading.
- **F-SOL-083-16 | LOW | seed chain** — Fixed `+0..+4` offsets mean per-statistic seeding can collide PRNG streams (e.g. `t2_absolute_interval(ds, 44)` and `t3_interval(x, 42)` both use 44). Harmless today; document the constraint.

### 8.3 Documentation

- **F-SOL-083-17 | DOC** — `normalize_fact_id` strips ASCII whitespace but not zero-width or non-breaking spaces (`"​f1"` and `"f\xa01"` survive as distinct IDs). Correct under a frozen minimal canonical form; worth one disclosure line.
- **F-SOL-083-18 | DOC** — `np.float64` is accepted for `minutes` while `np.int64` is rejected. Safe but asymmetric; state the intended numeric domain.

---

## 9. Release-gate conclusion

| Gate | Result |
|---|---|
| SHA-256 manifest (3 files) | **PASS** — 3/3 exact |
| Shipped suite 67/67 GREEN | **PASS** — 67 passed, reproduced twice |
| Six named golden vectors | **PASS** — 6/6 bit-exact, independently reconstructed |
| Fourteen dispatch-named findings discharged | **PARTIAL** — 8 D, 4 DP, 2 partly UV; none flatly ND |
| Independent adversarial attack | **FAIL** — 2 HIGH input-boundary defects reproduce |
| Coverage claims true of the bytes | **FAIL** — PA-Z4 absent, twelve-rule claim false |
| Manifest completeness | **FAIL** — amendment text absent |
| Interval-computation correctness | **PASS** — 554 fuzzed intervals, zero violations |

**Verdict: HALT.** Under the inherited carrying rule, a HALT from either seat blocks deposit and requires a new version. PASS-WITH-AMENDMENTS is unavailable because every required repair modifies normative bytes, forcing new hashes and a fresh carry.

**This HALT should be read narrowly.** The v0.8.3 bootstrap machinery is the strongest artifact in this lineage so far. The golden vectors are real, exact, and survived a dependency upgrade beyond their own pin — which is a materially better result than the drift condition Kimi demonstrated against v0.8.2. F-SOL-082-4, F-K3-N3, F-K3-N4, F-K3-N7, F-K3-N9, F-K3-N13, F-K3-N16, and F-K3-N18 are all genuinely discharged. What did not happen is closure of the **input boundary**, and the reason appears to be that three findings from the prior GPT-5.6 Sol verdict — two of them HIGH-BLOCKING — were dropped from the repair list rather than repaired.

### Required repair set for v0.8.4

1. Validate `censor_status` is a `CensorStatus` member as the first check in `__post_init__`; forbid evidence IDs on non-discoveries; require non-empty `str` IDs on OBSERVED **(F-SOL-083-2)**.
2. Make `M3Vector` immutable, or revalidate at every pipeline entry **(F-SOL-083-1)**.
3. Implement and test PA-Z4 and name PA-Z7, or scope them out explicitly and correct both coverage sentences **(F-SOL-083-3)**.
4. Ship and hash the amendment text; re-dispatch with a complete manifest **(F-SOL-083-4)**.
5. Freeze the M3 endpoint, adjudication condition, and mapping authority, or declare the endpoint change substantive **(F-SOL-083-5)**.
6. Replace the vacuous `TestPAZ12` with the reachable fixture supplied in §7 C-3 **(F-SOL-083-6)**.
7. Give the two BCa guards counters on `BootstrapResult` **(F-SOL-083-7)**; ship a dependency lock or version-assertion test **(F-SOL-083-8)**.
8. Apply bool rejection uniformly **(F-SOL-083-9)**; wrap malformed T4/T7 shapes in `PhaseAInputError` and require exact `int` **(F-SOL-083-10)**.
9. One-line disclosures for F-SOL-083-11 through F-SOL-083-18.

### Seat statement

This is the **GPT-5.6 Sol seat, 1 of 2, executed alone**. It is not two-family carrying convergence, and no deposit decision may treat it as such. Seat 2 (Kimi K3) has not reported on v0.8.3. Same-vendor seats count once; producer-family review is advisory. Carry is limited to the checks executed and is not peer review. The audit used exactly one GPT-5.6 Sol agent; no additional agent, model, or council was consulted.

---

## 10. Reproducibility

```bash
# 1. Hash verification (read-only, against the original dispatch directory)
cd /home/user/workspace/SHVVP_v0_8_3_DISPATCH_GPT
sha256sum shvvp_v0_8_3_phase_a_m3.py shvvp_v0_8_3_phase_a_intervals.py \
          test_shvvp_v0_8_3_phase_a.py

# 2. Byte-identical working copy (keeps originals free of __pycache__/.pytest_cache)
mkdir -p /tmp/shvvp_run
cp /home/user/workspace/SHVVP_v0_8_3_DISPATCH_GPT/*.py /tmp/shvvp_run/
cd /tmp/shvvp_run && sha256sum *.py        # re-verify after copy

# 3. Shipped suite
cd /tmp/shvvp_run
python3 -m pytest test_shvvp_v0_8_3_phase_a.py -q     # -> 67 passed
python3 -m pytest test_shvvp_v0_8_3_phase_a.py -v     # per-test record

# 4. Independent audit scripts (in /tmp/shvvp_attacks)
python3 gv_verify.py          # six golden vectors, full precision
python3 attack_a_boundary.py  # budget/enum/type-confusion/normalization
python3 attack_b_provenance.py# replace-bypass, vector mutation, evaluator state
python3 attack_c_stats.py     # cardinality, seeds, PA-Z reachability, BCa guards
python3 attack_d_fuzz.py      # randomized invariant fuzz, 360 cases / 554 intervals
python3 attack_e_coverage.py  # PA-Z11/Z12 sweep + coverage-claim audit

# 5. PDF token check (establishes the amendment text is absent)
python3 -c "
import pypdf, re
for n in ['SHVVP_v0_8_flagship.pdf','SHUDP_v0_5_flagship.pdf','BSSG_PAPER.pdf']:
    t=''.join((p.extract_text() or '') for p in
              pypdf.PdfReader('/home/user/workspace/SHVVP_v0_8_3_DISPATCH_GPT/'+n).pages)
    print(n, 'PA-Z:', len(re.findall('PA-Z',t)), ' PA-A:', len(re.findall('PA-A',t)))"
```

**Environment as executed:** Python 3.14.3, numpy 2.5.1, scipy 1.18.0, pytest 9.1.1, pluggy 1.6.0, linux.
**Environment as pinned by the artifact:** Python 3.12.x, numpy 2.4.x, scipy 1.17.x. See §2.1 — all six golden vectors matched anyway.
**Fuzz master seed:** 20260731. **Statistic seed used throughout:** 42.

---

*End of carrying audit — GPT-5.6 Sol seat, 2026-07-31.*

---

# Bismillah ir-Rahman ir-Rahim
