# Bismillah ir-Rahman ir-Rahim

# R0222 -- XZ Protocol v0.13 Adversarial Audit

**Chronological Index:** 429 of 995  
**Date:** 2026-08-01  
**Section:** IV. XZ Protocol  
**Source File:** xz_v13_audit_report.md  
**Source Format:** md  
**SHA-256:** `3311c27ccd43994b101a70067d2084117ac8c4291383306650bf887d82cc60be`  

---

## R0222 · XZ Protocol v0.13 Adversarial Audit

- section: IV. XZ Protocol
- source_file: xz_v13_audit_report.md
- source_format: md
- text_sha256: 3311c27ccd43994b101a70067d2084117ac8c4291383306650bf887d82cc60be

# XZ Protocol v0.13 Adversarial Audit

Date: 2026-08-01

Scope: offline audit of the extracted package from `XZ_v13_DISPATCH_GPT.zip`. The original ZIP was not modified. All execution used the isolated extraction under `xz_v13_audit/extracted` plus temporary sandboxes for mutations. No web research or external model assistance was used.

## Executive summary

The shipped package matches its declared file manifest, the canonical pytest command passes on the shipped bytes, and all five standalone gates return `0` on the shipped bytes.

That is not sufficient to certify the package as gate-hardened. Independent adversarial checks found multiple false-PASS paths:

- 3 package-level false-PASS cases where a materially bad mutated package still achieved:
  - all five standalone gates `PASS`
  - canonical pytest `210 passed`
- 2 additional gate-level false-PASS cases where an individual gate accepted a bad mutation even though another layer in the current package happened to catch it
- 1 commitment/decision-path defect that allows forged Condition A inputs to produce `A-ACCEPT`

Bottom line: the package is internally consistent on its shipped bytes, but it does not yet satisfy its own stated claim that the rebuilt gates reliably prevent recurrence of the named failure classes.

## Shipped-byte results

- SHA-256 manifest: `22/22` matched declared values
- Canonical test command: `210 passed in 9.49s`
- Standalone gates on shipped bytes: all `5/5` returned exit `0`
- Independent gate fixture matrix:
  - known-good fixture for each gate returned exit `0`
  - known-bad fixture for each gate returned exit `1`

These baseline results are preserved in:

- `xz_v13_audit/evidence/sha256_verification.json`
- `xz_v13_audit/evidence/canonical_pytest.txt`
- `xz_v13_audit/evidence/standalone_gates.json`
- `xz_v13_audit/evidence/gate_fixture_pairs.json`
- `xz_v13_audit/evidence/test_inventory.json`

## Findings

### 1. Critical: Condition A accepts forged provenance-bearing check results

- Location:
  - `xz_protocol_condition_a.py:168-214`
  - `xz_protocol_condition_a.py:236-332`
  - `xz_protocol_condition_a.py:339-369`
- Why it matters:
  - The module advertises a provenance/accident guard for `BaselineCheckResult`, but `evaluate_boundary()` never verifies that guard.
  - A caller can instantiate `BaselineCheckResult` directly with arbitrary `_provenance` values and drive `evaluate_boundary()` to `A-ACCEPT`.
  - A caller can then feed the resulting object into `is_primary_seam_divergence()` and obtain a counted divergence path without using the factory path the module claims to require.
- Reproduced behavior:
  - Three forged `BaselineCheckResult(..., _provenance='forged')` objects for the `S-COMMIT` mandatory checks produced `A-ACCEPT` with reason `All mandatory checks pass`.
  - A directly forged `BoundaryDisposition(A-ACCEPT, ...)` was accepted by `is_dual_evaluable()` and `is_primary_seam_divergence()`.
- Evidence:
  - `xz_v13_audit/evidence/commitment_decision_attacks.json`

### 2. Critical: Manifest gate ignores uppercase 64-hex tokens, enabling full-package false PASS

- Location:
  - `xz_protocol_manifest_gate.py:33-35`
  - `xz_protocol_manifest_gate.py:76-91`
- Why it matters:
  - The docstring says the gate scans the protocol text for every `64-hex token`.
  - The implementation only matches lowercase hex via `re.compile(r"\\b[0-9a-f]{64}\\b")`.
  - A stray uppercase digest in the protocol body outside Section 27 is invisible to the gate.
- Reproduced behavior:
  - Inserting `AAAAAAAA...` (64 uppercase hex chars) into the protocol body before Section 27 still produced:
    - all five standalone gates `PASS`
    - canonical pytest `210 passed`
- Evidence:
  - `xz_v13_audit/evidence/second_order_gate_attacks.json`
  - `xz_v13_audit/evidence/full_package_false_passes.json` (`uppercase_digest_protocol_body`)

### 3. Critical: Prohibited-content verifier misses `cpuid` in protocol text, enabling full-package false PASS

- Location:
  - `xz_protocol_prohibited_content_verifier.py:74`
  - `xz_protocol_prohibited_content_verifier.py:160-172`
  - corroborating expectation in `test_xz_protocol_adversarial.py:230-233`
- Why it matters:
  - The verifier's `HAZARD_TOKENS` list omits `cpuid`.
  - The adversarial suite separately treats `cpuid` as a prohibited payload indicator in module text.
  - The package therefore has an inconsistent hazard model: `cpuid` is treated as dangerous in tests, but the actual verifier never blocks it in the protocol body.
- Reproduced behavior:
  - Inserting `cpuid` into the protocol body before Section 27 still produced:
    - all five standalone gates `PASS`
    - canonical pytest `210 passed`
- Evidence:
  - `xz_v13_audit/evidence/full_package_false_passes.json` (`cpuid_protocol_body`)

### 4. Critical: History gate leaves amendment-record preamble text unsealed, enabling full-package false PASS

- Location:
  - `xz_protocol_history_gate.py:52-65`
- Why it matters:
  - The gate hashes only blobs beginning at lines that match `- **v...`.
  - Any text inserted after the `## 27. Amendment record` heading but before the first versioned entry is outside every sealed blob.
  - That creates an unsealed mutation surface inside the amendment record itself.
- Reproduced behavior:
  - Injecting prose between the Section 27 heading and the first amendment entry still produced:
    - all five standalone gates `PASS`
    - canonical pytest `210 passed`
- Evidence:
  - `xz_v13_audit/evidence/second_order_gate_attacks.json`
  - `xz_v13_audit/evidence/full_package_false_passes.json` (`history_preamble_injection`)

### 5. High: Closure gate can be bypassed by reclassifying a closed finding as `historical` or delegating it to any existing gate file

- Location:
  - `xz_protocol_closure_gate.py:102-113`
  - `xz_protocol_closure_gate.py:181-191`
- Why it matters:
  - For any register entry with `"historical"`, `evaluate()` returns success immediately.
  - For any register entry with `"delegated_to"`, `evaluate()` only checks that the named file exists; it does not verify that the delegation is valid for that finding or that the delegated gate actually discharges the asserted closure.
  - This allows a closed body-fix claim to be converted into an unevaluated metadata claim.
- Reproduced behavior:
  - Regressing a closed protocol-body locus and then changing the register entry for that finding to either:
    - `{"historical": "..."}`
    - `{"delegated_to": "xz_protocol_version_gate.py"}`
    caused `xz_protocol_closure_gate.py` to return `PASS`.
  - All five standalone gates still returned `PASS`.
  - The canonical pytest suite failed only because `test_xz_protocol_gates.py` independently mutates the body and expects the closure gate to fire.
- Evidence:
  - `xz_v13_audit/evidence/second_order_gate_attacks.json`
  - `xz_v13_audit/evidence/package_level_false_passes.json` (`closure_bypass_historical`)

### 6. Medium: Version gate does not enforce the claimed “exactly one stamp” rule

- Location:
  - `xz_protocol_version_gate.py:33-35`
  - `xz_protocol_version_gate.py:85-96`
- Why it matters:
  - The docstring says executable files carry exactly one version stamp.
  - The implementation only checks mismatched discovered tokens. A file with zero version stamps is accepted.
- Reproduced behavior:
  - Removing the version stamp line from `xz_protocol_kernel.py` caused `xz_protocol_version_gate.py` to return `PASS`.
  - In the current package, manifest integrity still fails because the bytes changed, so this is a gate-level false PASS rather than a full-package false PASS.
- Evidence:
  - `xz_v13_audit/evidence/second_order_gate_attacks.json` (`version_remove_stamp`)

## Gate fixture status requested by the dispatch

The dispatch asked for a known-good and known-bad fixture for each gate. I verified that independently:

- Version gate: good `0`, bad `1`
- Closure gate: good `0`, bad `1`
- Manifest gate: good `0`, bad `1`
- Prohibited-content gate: good `0`, bad `1`
- History gate: good `0`, bad `1`

That result is real, but incomplete. The fixture pairs only prove coverage for the specific seeded mutations they contain. They do not prove absence of other false-PASS paths, and the findings above demonstrate that several such paths remain.

## Commitment and decision-path attacks

Two deterministic commitment/decision-path attacks were executed:

1. Forged `BaselineCheckResult` inputs:
   - direct construction with arbitrary `_provenance`
   - evaluator returned `A-ACCEPT`

2. Forged `BoundaryDisposition` inputs:
   - direct construction with `ADisposition.A_ACCEPT`
   - seam helpers accepted it as dual-evaluable and as a primary divergence case when paired with `DENY_FALSE`

Evidence:

- `xz_v13_audit/evidence/commitment_decision_attacks.json`

## Other observations

- The canonical inventory is internally consistent with the package claims:
  - `206` test functions across the seven files in the canonical invocation
  - `210` collected cases under the explicit pytest command
- PDF context files were inventoried non-destructively with `pdfinfo`; metadata is saved in:
  - `xz_v13_audit/evidence/pdf_inventory.txt`

## Limitations

- No web verification was used, per task constraints.
- No external model, second auditor, or cross-family carry seat was consulted.
- I did not perform a full semantic review of each PDF against the protocol body, because the dispatch task was specifically executable and package-focused: hashes, canonical tests, gate behavior, commitment paths, and adversarial false-PASS attempts.

## Assessment

Shipped-byte status:

- SHA-256: pass
- Canonical suite: pass
- Standalone gates: pass

Adversarial audit status:

- not carry-clean
- not gate-hardened

The strongest reason is that at least three materially bad mutated packages still cleared the entire published verification surface (`5/5` standalone gates plus `210/210` canonical tests), and the Condition A decision path can be driven with forged inputs.

---

# Bismillah ir-Rahman ir-Rahim
