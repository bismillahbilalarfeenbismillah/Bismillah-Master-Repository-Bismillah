# Bismillah ir-Rahman ir-Rahim

# R0977 -- Test 2: Predict F26 from F22-F25 (predictions committed before reveal)

**Chronological Index:** 984 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** test2_F26_predictions.md  
**Source Format:** md  
**SHA-256:** `20443588c0226502ddde0f30ec20d958c19d6e1b918f7e0f01c82c2d6e1f83c9`  

---

## R0977 · Test 2: Predict F26 from F22-F25 (predictions committed before reveal)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: test2_F26_predictions.md
- source_format: md
- text_sha256: 20443588c0226502ddde0f30ec20d958c19d6e1b918f7e0f01c82c2d6e1f83c9

# Test 2: Predict F26 from F22-F25 (predictions committed before reveal)

## Input visible to predictor (F22-F25, F25 now in evidence)

| F | step | code | layer | scope | fix |
|---|---|---|---|---|---|
| F22 | 2-3 dispatch | CASM-V-001 | verifier_dispatch | whitelist_alignment | 21 LOC python |
| F23 | 4 install | CASM-V-021 | ci_install_matrix | extras_gap | 1 LOC yaml |
| F24 | 4 import | CASM-V-021 | sigstore_api_drift | api_path_drift | 3 LOC python |
| F25 | 6 identity | CASM-V-032 | policy_construction | literal_vs_regex | 1 LOC yaml |

## Updated structural regularities

**R1-R6 hold.** New observations:

**R7: Steps visited so far: 2-3, 4, 4, 6.** Step 5 was skipped (probably because step 5
is bytes-IO and the rust fixture never made it to a serialization mismatch). Step 7
is unknown. Step 8 is named in the verifier file structure (`extract_public_surface`,
`compare_public_surface`).

**R8: Two of four findings (F23, F25) are CI-workflow YAML issues, not Python substrate.**
The smoke-test workflow's authoring is itself an attack surface for findings. v0.11.7's
finding may again be in CI workflow OR in Python substrate.

**R9: When the substrate has a Python file matching the failing step, the substrate
finding lives in that file.** F22 lived in `verification.py:step2_3`. F24 lived in
`verification.py:step4` (TrustedRoot import). v0.11.7 may live in the file backing
step 7 or step 8.

**R10: ALL FOUR findings are LOW or LOW-MEDIUM severity. None CRITICAL/HIGH.** The
corrective discipline keeps each ship focused; severity stays bounded. v0.11.7 will
likely also be LOW.

**R11: Cross-language is the latent driver.** F22 was the original cross-language
finding (rust dispatch). F23 unmasked a CI install gap that was language-agnostic.
F24 unmasked a sigstore-API gap that was language-agnostic. F25 was a CI workflow
gap that was language-agnostic. **The next finding could re-encounter the
cross-language seam at a step that is Python-specific in implementation but
nominally language-agnostic in name.**

## Critical structural insight (the prediction the chain enables)

The verifier has 8 steps. Steps 2-3, 4, 6 have all been exercised against the rust
fixture. **Steps 7 and 8 have not.** Step 8 is `compare_public_surface`, which calls
`extract_public_surface(module_path)`. That function name is language-agnostic but the
implementation is plausibly Python-specific (the lint's primary surface extractor uses
`ast.parse`).

This is the cross-language seam from R11 reappearing at a different layer.

## Predictions (committed)

| Dimension | Prediction | Confidence |
|---|---|---|
| **P1 Step** | **step 7 OR step 8**. Strongest single bet = **step 8** (compare_public_surface). Step 7 is signature-bytes mismatch which is unlikely to fail on a rust fixture if step 6 passed | HIGH |
| **P2 Error code** | NEW code OR a Python-language exception leaking through (e.g. SyntaxError from ast.parse on rust source). Strongest single bet = **unhandled SyntaxError from Python's ast.parse** because the substrate file likely is `surface_extraction.py` or `additive.py` calling `ast.parse(rust_source)` | HIGH |
| **P3 Substrate layer** | **extractor_dispatch** — the language-agnostic-named function dispatches to a Python-specific extractor | HIGH |
| **P4 Fix-size class** | ~30 LOC dispatch table addition (per the cross-language pattern requiring routing logic, larger than 1-line fixes but still small) | MEDIUM |
| **P5 Root cause** | "extract_public_surface dispatches all files to Python ast.parse without routing by extension; rust source raises SyntaxError" | HIGH |

## Why I'm more confident on Test 2 than Test 1

Two reasons:
1. **Step monotonicity + skip-step-7 logic narrows the answer.** Steps 4, 6 visited
   (with step 5 likely skipped as IO). Step 7 is also IO-ish. Step 8 is the next place
   substantive logic happens.
2. **The cross-language seam (R11) is forced.** The smoke-test fixture is rust. Any
   language-agnostic-named function that has Python-specific implementation will fail
   on the rust fixture. The lint codebase has separate `_check_rust` paths for the
   linter, so the AUTHOR knew about the seam — but the verifier's step 8 may not have
   adopted the same dispatch table. This is a confidently-locatable gap.

## Ablation control (cold-start)

Without F22-F25, given just "v0.11.7 ships fixing a step-6 identity-policy literal-vs-regex
issue. What's the next bug?" the cold-start predictor would likely guess:
- "Identity workflow ref isn't pinned" — POSSIBLE but doesn't match step monotonicity
- "Sigstore-python continues to drift" — UNLIKELY because the audit chain shows F24 was the API drift round
- "Step 7 / step 8 cross-language gap" — UNLIKELY without the chain because there's no
  reason from cold-start to know step 8 has Python-specific extraction

The chain is doing real localization work for Test 2's P1, P3, P5.

---

# Bismillah ir-Rahman ir-Rahim
