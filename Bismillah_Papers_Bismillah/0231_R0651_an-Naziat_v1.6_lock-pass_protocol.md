# Bismillah ir-Rahman ir-Rahim

# R0651 -- an-Naziat v1.6 lock-pass protocol

**Chronological Index:** 231 of 995  
**Date:** 2026-05-11  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** LOCK_PASS_PROTOCOL.md  
**Source Format:** md  
**SHA-256:** `f1484d0320a287607ad6a7ea6563e5011830b1054ab0467a4380a606a9474c64`  

---

## R0651 · an-Naziat v1.6 lock-pass protocol

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: LOCK_PASS_PROTOCOL.md
- source_format: md
- text_sha256: f1484d0320a287607ad6a7ea6563e5011830b1054ab0467a4380a606a9474c64

# an-Naziat v1.6 lock-pass protocol

**Subject prompt**: `PHASE_G11_3_AN_NAZIAT_v1_6_PENDING_LOCK.md`
**Lock target**: transition from AUTHORED-FOR-AUDIT to AUTHORED-FOR-DISPATCH
**Substrate-truth gate**: tag `bf02995` (canonical v0.12.0) at local clone
**Project lead**: Bilal Syed Arfeen (BayyinahEnterprise)
**Time estimate**: 15-25 minutes

---

## Prerequisites

You need a local clone of `furqan-lint` checked out at canonical v0.12.0:

```bash
cd ~/path/to/furqan-lint
git fetch --tags
git checkout bf02995
pip install -e ".[dev,rust,go,onnx,onnx-runtime,onnx-profile,gate11,gate11-rust]" --quiet
```

Confirm the checkout:

```bash
git rev-parse HEAD
# Expected: a621faf... (peeled commit; bf02995 annotated tag points to this)
```

---

## Step 1: Execute all 10 verification commands

Run this script from inside the furqan-lint repo (checked out at bf02995). It captures all 10 outputs to a single file you can reference when pasting:

```bash
{
echo "=== CMD 1 (§0.5.1: _CHECKER_SOURCE_FILES length; paste into line 1967) ==="
python3 -c "from furqan_lint.gate11 import checker_set_hash as csh; print(len(csh._CHECKER_SOURCE_FILES))"

echo ""
echo "=== CMD 2 (§0.5.2: _CHECKER_SOURCE_FILES enumeration; paste into line 2010) ==="
python3 -c "
from furqan_lint.gate11 import checker_set_hash as csh
for i, p in enumerate(csh._CHECKER_SOURCE_FILES, 1):
    print(f'{i:2d}  {p.relative_to(p.parent.parent.parent)}')"

echo ""
echo "=== CMD 3 (§0.5.3: pytest collected count; paste into line 2041) ==="
pytest --collect-only -q 2>&1 | tail -3

echo ""
echo "=== CMD 4 (§0.5.4-a: _LANGUAGE_DISPATCH pattern; paste into line 2075) ==="
git show bf02995:src/furqan_lint/gate11/verification.py | grep -nE "_LANGUAGE_DISPATCH:|from furqan_lint.gate11.python_verification import _verify_python"

echo ""
echo "=== CMD 5 (§0.5.4-b: _VERIFIER_DISPATCH absence; paste into line 2095; expected: empty) ==="
git show bf02995:src/furqan_lint/gate11/verification.py | grep -nE "^_VERIFIER_DISPATCH"
echo "(if no output above, paste literal empty result: '(no matches; substrate-actual absence confirms function-local dispatch)')"

echo ""
echo "=== CMD 6 (§0.5.5: cmd_manifest_verify + cmd_check_gate11 signatures; paste into line 2125) ==="
git show bf02995:src/furqan_lint/gate11/cli.py | grep -nE "^def cmd_manifest_verify|^def cmd_check_gate11"

echo ""
echo "=== CMD 7 (§0.5.6-a: import sys presence; paste into line 2158) ==="
git show bf02995:src/furqan_lint/gate11/cli.py | grep -nE "^import sys"

echo ""
echo "=== CMD 8 (§0.5.6-b: _print_error + _walk_bundles absence; paste into line 2177; expected: empty) ==="
git show bf02995:src/furqan_lint/gate11/cli.py | grep -nE "^def _print_error|^def _walk_bundles"
echo "(if no output above, paste literal empty result: '(no matches; substrate-actual helper-symbol absence confirms Option-i idiom)')"

echo ""
echo "=== CMD 9 (§0.5.7: onnx_verification.py absence; paste into line 2197) ==="
git show bf02995:src/furqan_lint/gate11/onnx_verification.py 2>&1 | head -1

echo ""
echo "=== CMD 10 (§0.5.8: SUPPORTED_LANGUAGES whitelist; paste into line 2225) ==="
git show bf02995:src/furqan_lint/gate11/manifest_schema.py | grep -nE 'SUPPORTED_LANGUAGES|"python".*"rust".*"go"'

echo ""
echo "=== END OF LOCK-PASS CAPTURE ==="
} 2>&1 | tee ~/an_naziat_v1_6_lock_pass_capture.txt
```

The script outputs to both stdout and a file (`~/an_naziat_v1_6_lock_pass_capture.txt`) for reference while pasting.

---

## Step 2: Expected outputs (sanity-check against §7 canonical)

If any output materially diverges from the Round 39 chain log §7 canonical, **HALT** — that's a substrate-uniqueness violation worth investigating before dispatch. Otherwise proceed.

| Cmd | §0.5.X | Expected (from §7 canonical) |
|---|---|---|
| 1 | §0.5.1 | `19` |
| 2 | §0.5.2 | 19-entry alphabetical-within-section enumeration; gate11/go_signature_canonicalization.py at #6, gate11/go_verification.py at #7, go_adapter/cmd/goast/main.go at #19 |
| 3 | §0.5.3 | `642 tests collected` (or `598 passed, 44 skipped, 0 failed` if run as `-q` not `--collect-only`) |
| 4 | §0.5.4-a | Two matches inside `verify()` function body; lines vary |
| 5 | §0.5.4-b | Empty (no matches; function-local dispatch confirmed) |
| 6 | §0.5.5 | Two def lines: `cmd_manifest_verify(args: list[str]) -> int` + `cmd_check_gate11(directory: Path, opts: dict[str, object]) -> int` |
| 7 | §0.5.6-a | One match: `import sys` |
| 8 | §0.5.6-b | Empty (no helpers present; Option-i idiom confirmed) |
| 9 | §0.5.7 | `fatal: path 'src/furqan_lint/gate11/onnx_verification.py' does not exist in 'bf02995'` |
| 10 | §0.5.8 | One match: `SUPPORTED_LANGUAGES: tuple[str, ...] = ("python", "rust", "go")` |

---

## Step 3: Paste outputs into the prompt

Open `PHASE_G11_3_AN_NAZIAT_v1_6_PENDING_LOCK.md` in your editor. For each of the 10 placeholders, replace `[PASTE COMMAND OUTPUT HERE VERBATIM]` with the captured output (no quotes, no fencing changes — just the verbatim terminal text):

| Cmd | Target line | Action |
|---|---|---|
| 1 | 1967 | Replace placeholder with output |
| 2 | 2010 | Replace placeholder with 19-line enumeration |
| 3 | 2041 | Replace placeholder with pytest tail-3 output |
| 4 | 2075 | Replace placeholder with grep output |
| 5 | 2095 | Replace placeholder with empty-result note |
| 6 | 2125 | Replace placeholder with grep output |
| 7 | 2158 | Replace placeholder with grep output |
| 8 | 2177 | Replace placeholder with empty-result note |
| 9 | 2197 | Replace placeholder with git fatal message |
| 10 | 2225 | Replace placeholder with grep output |

Line numbers may shift after each paste; use search-and-replace on `[PASTE COMMAND OUTPUT HERE VERBATIM]` working top-to-bottom, replacing one at a time in order.

---

## Step 4: Fill the prompter-lock signature block

Search for `Mechanically verified by:` in the prompt — there's a single signature block at the end of §0.5. Fill the four fields:

```
**Mechanically verified by**: Bilal Syed Arfeen / BayyinahEnterprise
**Verified against**: tag bf02995 (annotated) / commit a621faf (peeled)
**Verification date**: 2026-05-11
**Local clone path**: /your/actual/path/to/furqan-lint
**Outputs captured**: verbatim from terminal (no editing or summarization)
```

---

## Step 5: Flip the lock-state line

Find line 1916:

```
**Current lock state of this v1.6 prompt**: AUTHORED-FOR-AUDIT
```

Replace `AUTHORED-FOR-AUDIT` with `AUTHORED-FOR-DISPATCH`. That single edit transitions the prompt from audit-stage to dispatch-stage.

---

## Step 6: Archive as dispatch-locked

```bash
cp PHASE_G11_3_AN_NAZIAT_v1_6_PENDING_LOCK.md PHASE_G11_3_AN_NAZIAT_v1_6_dispatch_locked.md
```

`PHASE_G11_3_AN_NAZIAT_v1_6_dispatch_locked.md` is what Co-work executes.

---

## Step 7: Dispatch to Co-work

Send Co-work this packet:

1. `PHASE_G11_3_AN_NAZIAT_v1_6_dispatch_locked.md` (primary; the locked prompt)
2. Substrate access (local clone OR remote pointer to `furqan-lint` with `v0.13.0-an-naziat-v16` branch at HEAD `e174510`)
3. `SKILL.md` (bayyinah-audit methodology summary)
4. `round_39_chain_log_correction.md` (canonical §7 substrate-of-record)
5. AUTHORSHIP_REWRITE_NOTE (`Solid Snake` → `Bilal Syed Arfeen <[personal email redacted]>` on all authored commits)
6. Co-work session opener (the framing paragraph anchoring their role)

Co-work executes T01-T11 + §5 13-gate verification (~8-12 hours estimated) producing the v0.13.0 ship.

---

## Methodology note

The §0.5 lock-pass is the substrate-truth gate. Once the 10 captures are filled and the lock-state is flipped, the prompt asserts substrate-grounded claims rather than substrate-projected claims. Round 40 Perplexity Mode A post-ship audit verifies the actual v0.13.0 ship matches what the locked prompt specified.

If any of the 10 outputs materially diverges from §7 canonical (e.g., count is not 19; tests are not 642; signatures are different), do not flip the lock-state — pause and investigate. That divergence would be a real substrate-uniqueness violation surfaced by the protocol working correctly.

If all 10 outputs match §7 canonical (the expected case), the lock-pass completes in 15-25 minutes and v1.6 is dispatch-ready.

---

# Bismillah ir-Rahman ir-Rahim
