# Bismillah ir-Rahman ir-Rahim

# R0817 -- R20 Audit Report — Seat S05 (FRESH)

**Chronological Index:** 930 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** R20_v061_S05_GPT56_SOL_FRESH_AUDIT.md  
**Source Format:** md  
**SHA-256:** `80e576e0c175e9db5fd8b33957765b28e4b59cb838eab9341a2fd2426f35fde6`  

---

## R0817 · R20 Audit Report — Seat S05 (FRESH)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: R20_v061_S05_GPT56_SOL_FRESH_AUDIT.md
- source_format: md
- text_sha256: 80e576e0c175e9db5fd8b33957765b28e4b59cb838eab9341a2fd2426f35fde6

# R20 Audit Report — Seat S05 (FRESH)

**Protocol:** XZ Protocol v0.61
**Round:** R20
**Seat:** S05 — GPT-5.6 Sol, advisory / non-binding
**Framework:** Differentiator + Adversarial
**Verdict: HALT (ADVISORY)**

**v0.61 does not break the Class-A recurrence.** The run extends from **R7–R19 = 13/13** to **R7–R20 = 14/14 rounds with Class A present**.

## Baseline execution

| Verification | Result |
|---|---|
| `python3 build.py` | **PASS — all checks GREEN** |
| Canonical pytest | **186/186 passed** |
| `PACKET_SHA256SUMS` | **19/19 OK** |
| CI-1R | **PASS — generated register byte-exactly present in protocol** |
| Current register SHA-256 | `bb4dbe3f0ecae8d0b59e95439b7e6ed89b4d72ed6aa4cb45929d7df3381ab7f4` |
| ASSERTED fraction | **1/10 = 10.0% — PASS** |
| Section 22.2 | **v0.1 through v0.60 — PASS** |
| Section 22.3 | **v0.38-v0.60 — PASS** |
| VERSION-1 mutation test | **PASS as a control:** staling either 22.2 or 22.3 causes `[10i]` to fail |
| Dangling `convergence_group=999` | **Rejected with `ValueError`** |

The major v0.61 repairs are therefore real: M2 is materially more load-bearing, VERSION-1 gating exists, and dangling convergence references are now rejected.

## Blocking findings

| Finding | Severity | Result |
|---|---|---|
| **F-S05-61-01 — M3 receipt enforcement remains semantically incomplete** | **HIGH / Class A** | **BLOCKING** |
| **F-S05-61-02 — CI-8 literal source identity still fails** | **HIGH / Class A** | **BLOCKING** |
| **F-S05-61-03 — cross-layer membership parity remains ungated** | MEDIUM / Class B | Residual control gap |

### F-S05-61-01 — HIGH / CLASS A

The decisive v0.61 claim is still false:

> `receipt removal on mixed groups fails`

The implementation at `xz_protocol_register_gen.py` lines 119–138 requires a receipt only when **triage severity differs from the computed majority**. It calculates `has_mixed`, but does not require a receipt merely because `has_mixed` is true.

I converted group 1 from `6 HIGH` to a valid mixed distribution of **5 HIGH + 1 MEDIUM**, keeping triage severity HIGH, then removed the receipt entirely.

**Result: generation succeeded.**

The mutation produced register SHA-256:

`4550855b9b58081632be644c70faa62a850dc8f9569b1469c8ea38a48e3d11ab`

Thus the exact R20 M3 contract in `DISPATCH.txt` lines 6–8 and prediction P10 is falsified.

There is a second defect in the claimed receipt-content validation. For a true distribution of **4 HIGH + 2 MEDIUM**, I supplied the deliberately false receipt:

`2 HIGH, 4 MEDIUM`

**The generator accepted it.**

The reason is structural: lines 133–138 independently check whether the string contains `"4"` and `"HIGH"`, and whether it contains `"2"` and `"MEDIUM"`. They do not verify the **association** `4↔HIGH` and `2↔MEDIUM`.

So the current `[COMPUTED: generate_register]` claim that the receipt “must match the computed distribution exactly” is false.

**Clearance:** require a receipt whenever `has_mixed` is true, and validate a structured/canonical distribution—not independent substring presence.

### F-S05-61-02 — HIGH / CLASS A

**CI-8 still fails its own literal criterion.**

`CI_METHODOLOGY.txt` lines 362–365 requires:

> every `finding_id` in the index exists in its seat's report.

I checked the **25 authoritative R19 `findings[]` records** against their corresponding source-seat sections in `R19_REPORTS.txt`.

Result:

**9/25 literal IDs present; 16/25 absent.**

The absent identifiers include the synthetic mode-qualified forms such as `F-S01C-60-*`, `F-S02-60-*C`, `F-S03-60-*F/C`, and `F-S05-60-*F/C`, where the source reports frequently use the unsuffixed original identifier.

This is not a newly discovered namespace issue: R19 triage explicitly identified it as Surface 5 and put **“Preserve literal source finding IDs”** in the minimum v0.61 repair set. v0.61 carries it forward as NOTED rather than repairing it.

Therefore producer prediction **P2: “CI-8 PASS” is falsified**. Under the shipped CI-8 definition, an unresolved index→source identity failure remains Class A.

**Clearance:** preserve the original source finding ID verbatim and use a separate unique record/seat-instance key, or ship and gate an explicit lossless normalization map.

### F-S05-61-03 — MEDIUM / CLASS B

The new dangling-reference control works, but cross-layer membership is only partially validated.

Changing:

`F-S01-60-01: convergence_group 1 → 999`

correctly raises `ValueError`.

But changing the same scalar from group **1 → 2**, where group 2 legitimately exists, is accepted and produces a **byte-identical register**. The finding remains physically listed in group 1's `finding_ids`, while its own authoritative scalar says group 2.

This does not falsify the narrowly worded v0.61 claim that *dangling* references are rejected, so I do not use it as a Class-A basis. It does show that the stronger CI-8 requirement that convergence membership match triage remains mechanically ungated.

## R20 target disposition

| Target | Audit result |
|---|---|
| **P1 — CI-1R PASS** | **CONFIRMED** |
| **P2 — CI-8 PASS** | **FALSIFIED** |
| **P3 — ASSERTED <15%** | **CONFIRMED: 10.0%** |
| **P4 — Class A on new/body surface if present** | **CONFIRMED** |
| **P5 — count-list** | **CONFIRMED** |
| **P6 — append-only** | Internally consistent via shipped seals; fresh seat lacks an independently held v0.60 protocol anchor |
| **P7 — code layer** | **FALSIFIED by M3 receipt logic** |
| **P8 — packet** | **CONFIRMED: 19/19** |
| **P9 — M2 distribution load-bearing** | **CONFIRMED** — valid mutation + repaired receipt changes generated bytes |
| **P10 — mixed-group receipt removal fails** | **FALSIFIED** |
| **P11 — VERSION-1 stale bounds fail** | **CONFIRMED by executed mutations** |
| **P12 — 22.2/22.3 at v0.60** | **CONFIRMED** |

## Final determination

v0.61 is a substantial improvement over v0.60. The VERSION-1 gate is genuinely implemented, source-severity distributions are emitted and therefore load-bearing, the prior dangling group references are cleaned up, and the executable baseline is clean.

But the central M3 repair is **not complete**. A mixed distribution whose majority agrees with triage needs no receipt, and a materially false receipt can satisfy the supposed exact-distribution validator. Separately, CI-8's known literal source-ID defect remains unresolved.

Accordingly:

**FINAL SEAT VERDICT: HALT (ADVISORY, NON-BINDING).**

**R7–R20: 14/14 rounds with Class A present.** Under the same Laplace convention used by the protocol, the next-round value becomes **15/16 = 0.9375**.

---

# Bismillah ir-Rahman ir-Rahim
