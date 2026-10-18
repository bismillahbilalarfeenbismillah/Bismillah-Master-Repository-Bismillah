# Bismillah ir-Rahman ir-Rahim

# R0211 -- XZ Protocol v0.3 Carrying Audit Report

**Chronological Index:** 385 of 995  
**Date:** 2026-07-31  
**Section:** IV. XZ Protocol  
**Source File:** XZ_PROTOCOL_v0_3_GPT56_AUDIT.txt  
**Source Format:** txt  
**SHA-256:** `bc176350d9e0dd3be77d00d3d4ae9c44a627887b846da8f70aefeaff4ad57061`  

---

## R0211 · XZ Protocol v0.3 Carrying Audit Report

- section: IV. XZ Protocol
- source_file: XZ_PROTOCOL_v0_3_GPT56_AUDIT.txt
- source_format: txt
- text_sha256: bc176350d9e0dd3be77d00d3d4ae9c44a627887b846da8f70aefeaff4ad57061

# XZ Protocol v0.3 Carrying Audit Report

Seat: GPT-5.6 Sol only
Date: 2026-07-31 UTC
Workspace audited: `/home/user/workspace/xz_protocol_v0_3_audit`
Normative files modified during audit: none

## Executive Verdict

**HALT**

This GPT-5.6 seat-only audit returns `HALT`.

The strongest reasons are package-integrity and carry-sufficiency failures, not basic test execution:

1. The shipped six-suite battery does execute cleanly in an isolated reproducible environment, and the dispatch claim `181/181 GREEN` is true for the shipped bytes.
2. B-1 is only partially discharged. The kernel core is present, typed, and exhaustively exercised over `3^5 = 243` truth states, but the package still does not ship the raw-evidence, packet-schema, cutoff, and manifest/digest enforcement surfaces needed to verify end-to-end Condition B behavior and CR-12.
3. B-2 is not discharged. The 27-test adversarial suite names all nine Section 22 categories, but several categories are only proxy checks on enums, frozen dataclasses, or JSON field shapes rather than executable attacks on packet, mapping, digest, or trust-root behavior.
4. Independent SHA-256 verification is not possible from the supplied package. The dispatch contains no hash list, and no authoritative manifest or signed digest covering the 13 normative files is embedded anywhere in the package.
5. Package completeness is insufficient for a carrying audit. The v0.3 bundle does not include `xz_protocol_v0_3.md`, so spec consistency, Section 22 interpretation, freeze-blocker closure, and v0.3 carry claims cannot be verified against an authoritative normative prose artifact.

## Scope Limits

- This report covers only the bytes present in `/home/user/workspace/xz_protocol_v0_3_audit`, the prior v0.2 GPT-5.6 audit baseline in `/home/user/workspace/xz_protocol_audit`, the shipped parent PDFs, and the deterministic shell/Python checks run during this audit.
- The v0.3 package does **not** contain `xz_protocol_v0_3.md`. Where normative prose comparison was required, I had to fall back to `DISPATCH_XZ_v03_GPT.md`, the v0.2 protocol text and audit baseline, code/test docstrings, and the parent references. That is an audit limitation and itself a finding.
- No signed manifest digest, no independent carry receipts, no adjudication manual receipts, no universe commitment, and no second-seat materials were present.
- This is the GPT-5.6 seat only. It does **not** satisfy, substitute for, or imply the required Kimi/second carrying seat, convergent two-family carry, peer review, or approval for deposit.

## Package Inventory And Completeness

### Bundle contents

- Shipped files: `17`
- Parent reference PDFs: `3`
- Dispatch file: `1`
- Non-PDF, non-dispatch artifacts: `13`

### Inferred 13-file normative set

The dispatch says “13 normative files” but does not enumerate them. The only coherent 13-file set in the shipped bundle is the set of all non-PDF, non-dispatch artifacts:

| File | Type | Status |
|---|---|---|
| `xz_protocol_phase_a_m3.py` | Phase A implementation | Present |
| `xz_protocol_phase_a_intervals.py` | Phase A implementation | Present |
| `xz_protocol_phase_a_tests.py` | Phase A suite | Present |
| `xz_protocol_condition_a.py` | Condition A implementation | Present |
| `test_xz_protocol_condition_a.py` | Condition A suite | Present |
| `xz_protocol_source_frame.py` | Source-frame implementation | Present |
| `test_xz_protocol_source_frame.py` | Source-frame suite | Present |
| `xz_protocol_control_graph.py` | WithinAuth implementation | Present |
| `test_xz_protocol_control_graph.py` | WithinAuth suite | Present |
| `xz_protocol_kernel.py` | Kernel implementation | Present |
| `test_xz_protocol_kernel.py` | Kernel suite | Present |
| `test_xz_protocol_adversarial.py` | Cross-module adversarial suite | Present |
| `xz_protocol_trust_roots_PUBLIC.json` | Trust-root artifact | Present |

### Completeness assessment

| Expected artifact class | Supplied? | Impact |
|---|---|---|
| `xz_protocol_v0_3.md` normative protocol text | **No** | Cannot verify v0.3 prose, Section 22 wording, freeze-blocker register, or spec-code consistency against an authoritative v0.3 text |
| Authoritative SHA-256 manifest or signed digest | **No** | `13/13` cryptographic verification cannot be completed independently |
| Manifest-digest signatures / seal receipts | **No** | Trust-root and commitment claims cannot be audited end-to-end |
| Requirements / lockfile / env manifest | **No** | Test execution required an ad hoc isolated venv; base environment lacked `pytest` |

The `13`-file count is internally consistent with the bytes shipped, but it does not cure the missing v0.3 normative prose artifact. In v0.2, the normative package included the prose spec; in v0.3, it does not.

## Cryptographic Verification

### Result

**Independent verification not possible.**

Searches over the package found no authoritative file-hash manifest and no signed manifest digest covering the 13 normative files. The dispatch mentions SHA-256 verification, but contains no hashes. The package mentions “manifest digest” only descriptively in the trust-roots file and source-frame prose; no verifier or signed digest is shipped.

Accordingly:

- The table below records **computed reproducibility hashes**.
- These are **not** treated as “verified” against an independent committed manifest.

### Hash table

| File | Computed SHA-256 | Independent verification status |
|---|---|---|
| `test_xz_protocol_adversarial.py` | `4140399de285da2e973ac09f75044fed1e9c595983b9c556956fd37952228767` | Not independently verifiable |
| `test_xz_protocol_condition_a.py` | `2bb316b325e9cf25e519c31d6b6ddede995e8300bd5da45449fc662b81120774` | Not independently verifiable |
| `test_xz_protocol_control_graph.py` | `cc8fd9e2663755128e50deb23b6c6a30efcd8e12d50b4b7a19083363fbbfd4f5` | Not independently verifiable |
| `test_xz_protocol_kernel.py` | `75ad27efaf2482e5d32aaf8974413415084635c115f315d1034a031ed2370053` | Not independently verifiable |
| `test_xz_protocol_source_frame.py` | `1e4583743b320f7dad5407c58d81755e08aa75d7029855f66c6c152331963740` | Not independently verifiable |
| `xz_protocol_condition_a.py` | `b644d67e2b1d538968f93a81942d0ee7b9ef2fbfc787ca5016698dd9ec18b0ac` | Not independently verifiable |
| `xz_protocol_control_graph.py` | `cf657c00f4109199180b9ca655586cc8ab53529e603c2966053aa8b8e9d92f24` | Not independently verifiable |
| `xz_protocol_kernel.py` | `185a879b275459e2ea20ad355b210a7e742eb850c58552d49bfc0a4287132c3f` | Not independently verifiable |
| `xz_protocol_phase_a_intervals.py` | `2d5ac083d67c383e0a5467d375a1845e5ed558bc2fef7f29a3d7888cc0bc5521` | Not independently verifiable |
| `xz_protocol_phase_a_m3.py` | `66006767bfe807a7b7ce008f83ab5c7dcbf21809a08aba2e0db53774d58af25f` | Not independently verifiable |
| `xz_protocol_phase_a_tests.py` | `6e198343ec6d1c2f44aa61b381b189cbd0b89b9d7c0852d89004b6d568538e2a` | Not independently verifiable |
| `xz_protocol_source_frame.py` | `0d6e189a9068daac26b9ebccd9039c09728848c34fc568e9c03c17fa86e1c105` | Not independently verifiable |
| `xz_protocol_trust_roots_PUBLIC.json` | `100820cbce7987424e4609b13579d9820aaf7d01f021c1d79996f52484096588` | Not independently verifiable |

## Test Evidence

### Environment

| Context | Observation |
|---|---|
| Base interpreter | `Python 3.14.3` |
| Base environment gap | `pytest` not installed (`False` from `importlib.util.find_spec("pytest")`) |
| Isolated environment used for evidence | temporary venv at `/tmp/xz_v03_audit_venv` |
| Installed toolchain in venv | `pytest 9.1.1`, `numpy 2.4.4`, `scipy 1.17.1` |

### Exact collected and pass counts

| Suite | Collected | Passed | Failed | Errors | Command result |
|---|---:|---:|---:|---:|---|
| `xz_protocol_phase_a_tests.py` | 68 | 68 | 0 | 0 | `68 passed in 6.45s` |
| `test_xz_protocol_condition_a.py` | 29 | 29 | 0 | 0 | `29 passed in 0.11s` |
| `test_xz_protocol_source_frame.py` | 25 | 25 | 0 | 0 | `25 passed in 0.06s` |
| `test_xz_protocol_control_graph.py` | 18 | 18 | 0 | 0 | `18 passed in 0.07s` |
| `test_xz_protocol_adversarial.py` | 27 | 27 | 0 | 0 | `27 passed in 0.09s` |
| `test_xz_protocol_kernel.py` | 14 | 14 | 0 | 0 | `14 passed in 0.07s` |
| Combined six-suite run | 181 | 181 | 0 | 0 | `181 passed in 6.09s` |

### Count conclusion

- The dispatch claim `181 tests across 6 suites` is correct for the shipped bytes.
- The dispatch claim `181/181 GREEN` is also correct in a clean isolated environment.
- The exact collected total also matches a static `def test_` count of `181`.

### Dependency / environment gap

The package does not ship a requirements file or lockfile. The base environment lacked `pytest`, so the test battery is not executable out of the box without creating an isolated environment and installing dependencies manually.

## Repair-Verification Matrix

| Claimed v0.2 repair from dispatch | Concrete evidence | Auditor status |
|---|---|---|
| `BSSG kernel module shipped with exhaustive 3^5=243 tests` | `xz_protocol_kernel.py`, `test_xz_protocol_kernel.py`; `generate_exhaustive_vectors()` returns `243` unique vectors; exhaustive loop in `test_exhaustive_decision_correctness` | **Yes for kernel core** |
| `Seam estimator wired to KernelDecision enum; string decisions rejected` | `xz_protocol_condition_a.py:is_dual_evaluable`, `is_primary_seam_divergence`; tests reject string decisions | **Yes** |
| `Adversarial suite expanded to all 9 Section 22 categories (27 tests)` | `test_xz_protocol_adversarial.py` has 27 collected tests and nine category headings | **No as a discharge claim**; headings/count present, but several categories are only proxy checks |
| `Phase A imports fixed (no stale shvvp_v0_8_4 references)` | Search over shipped Python files found no `shvvp_v0_8_4` references; `68/68` Phase A tests collect/pass as shipped | **Yes** |
| `Mandatory NOT_APPLICABLE -> A-INDETERMINATE` | `xz_protocol_condition_a.py:298-304`; `test_not_applicable_on_mandatory_is_indeterminate` passes | **Yes** |
| `FRAME_START corrected to 180 days` | `xz_protocol_source_frame.py:36`; `test_xz_protocol_source_frame.py:22-25` | **Yes in code/test**, but file header still says `2023-09-30` |

## B-1 / B-2 Decision

### B-1 (kernel)

**Partially discharged.**

What is concretely discharged:

- The kernel module exists as shipped.
- It is strongly typed (`TruthValue`, `KernelDecision`).
- It preserves `DENY_FALSE` vs `DENY_UNKNOWN`.
- It is exercised over all `243` truth-state combinations and the exhaustive suite passes.

What is **not** discharged:

- No packet object or raw-evidence schema is shipped.
- No evaluator recomputes conjuncts from raw evidence.
- No cutoff verifier or manifest-digest verifier is shipped.
- No end-to-end Condition B path exists that would let this audit verify CR-12 or full seam-path enforcement.

### B-2 (adversarial coverage)

**Not discharged.**

The adversarial suite reaches 27 passing tests, but several claimed attack categories are represented only by weak stand-ins:

- commitment-ID confusion -> uniqueness of source IDs and public keys only
- trust-root override -> JSON field shape only
- packet-regime mixing -> enum typing only
- post-cutoff evidence injection -> frame-end constant only
- role remapping after outcomes -> frozen dataclasses only
- screened-event suppression -> stratum membership only

Those are not equivalent to attacks on actual packet, commitment, trust-root, mapping, or screened-event logic.

## Regression Status Against Material v0.2 Findings

| Material v0.2 finding | v0.3 status | Evidence |
|---|---|---|
| Phase A stack non-executable due stale imports | **Resolved** | `68/68` Phase A tests collect/pass as shipped; no stale imports found |
| No shipped kernel / exhaustive `243` coverage | **Partially resolved** | Kernel core and exhaustive suite ship and pass, but no raw-evidence evaluator surrounds them |
| Mandatory `NOT_APPLICABLE` could still yield `A-ACCEPT` | **Resolved** | `xz_protocol_condition_a.py:298-304`; test passes |
| Adversarial suite missing most Section 22 categories | **Not materially resolved** | 27 tests and nine headings exist, but several categories remain proxy/vacuous |
| `FRAME_START` off by one day | **Resolved in constant/test** | `FRAME_START = 2023-10-01`; 180-day test passes |
| WithinAuth only partial Axiom 5 conformity | **Still unresolved materially** | Truth table present, two-level A5 discipline absent |
| Safety/prohibited-content enforcement heuristic | **Still unresolved** | Heuristic scans remain weak and incomplete |
| Trust-root path unresolved | **Still unresolved** | Public keys ship, but no signed digest/receipts/verifier |
| Condition A weaker than inherited comparator | **Still partially unresolved** | NOT_APPLICABLE fixed, but attestation-oriented baseline checks remain non-mandatory |

## Cross-Artifact Consistency Findings

| Claim surface | Concrete artifact | Result |
|---|---|---|
| Package is v0.3 carrying material | `xz_protocol_condition_a.py`, `xz_protocol_source_frame.py`, `xz_protocol_control_graph.py`, and `xz_protocol_trust_roots_PUBLIC.json` still identify themselves as `v0.2` artifacts | Inconsistent |
| `FRAME_START` corrected to 180 days | `xz_protocol_source_frame.py` header still says `2023-09-30`, but code/test use `2023-10-01` | Inconsistent |
| Section 22 nine-category adversarial battery shipped | `test_xz_protocol_adversarial.py` contains headings for all nine categories, but several tests do not exercise the named threat models | Partially inconsistent |
| Manifest is “closed” and “sealed” | `validate_manifest()` checks only core-strata coverage, unique IDs, and four primary URLs; no seal/digest verification exists | Inconsistent with stronger framing |

## Adversarial Analysis

### 1. Vacuous tests and missing negative cases

Assessment: **material weakness remains**.

- `test_xz_protocol_adversarial.py:70-80` treats commitment-ID confusion as uniqueness of IDs and keys, not commitment binding.
- `test_xz_protocol_adversarial.py:84-99` treats trust-root override as Ed25519 field-shape validation, not override resistance.
- `test_xz_protocol_adversarial.py:102-109` treats packet-regime mixing as enum typing.
- `test_xz_protocol_adversarial.py:112-125` treats post-cutoff injection as a constant-date check and absence of a timestamp field on `ConjunctVector`.
- `test_xz_protocol_adversarial.py:129-139` treats role remapping after outcomes as dataclass immutability.
- `test_xz_protocol_adversarial.py:159-170` treats screened-event suppression as stratum presence, not screened-event ledger completeness.

### 2. Implementation/spec drift

Assessment: **material drift remains**.

- The package lacks `xz_protocol_v0_3.md`.
- Multiple artifacts still declare themselves `v0.2`: `xz_protocol_condition_a.py:4`, `xz_protocol_source_frame.py:4`, `xz_protocol_control_graph.py:4`, `xz_protocol_trust_roots_PUBLIC.json:2`.
- `xz_protocol_source_frame.py:12-15` still documents `2023-09-30` while the executable constant is `2023-10-01` at line `36`.

### 3. Enum/type bypasses

Assessment: **core kernel/seam typing improved, but not end-to-end enough**.

- Positive: `is_dual_evaluable()` and `is_primary_seam_divergence()` reject non-`KernelDecision` inputs (`xz_protocol_condition_a.py:334-351`, tests at `test_xz_protocol_condition_a.py:214-246`).
- Positive: kernel input rejects non-typed conjuncts (`xz_protocol_kernel.py:55-61`; tests at `test_xz_protocol_kernel.py:84-91`).
- Remaining gap: there is still no packet/schema layer to reject caller-supplied derived fields before kernel construction, which is what the v0.2 prose requires.

### 4. Unsafe defaults and manufacture risk

Assessment: **improved from v0.2, not fully cured**.

- Positive: mandatory `NOT_APPLICABLE` now yields `A-INDETERMINATE`, not `A-ACCEPT`.
- Remaining risk: the baseline profile still does not make `SLSA_PROVENANCE`, `IN_TOTO_ATTESTATION`, or `STEP_ATTESTATION` mandatory in any stratum (`xz_protocol_condition_a.py:120-151`), despite the inherited SHVVP baseline framing of a competent SLSA + in-toto + Sigstore stack.
- Remaining risk: `BaselineCheckResult` carries an accident-guard `_provenance` token, but `evaluate_boundary()` never verifies it. Directly forged `BaselineCheckResult(...)` objects with empty provenance are accepted.

### 5. CR-3 enforcement

Assessment: **helper-level enforcement present; end-to-end enforcement absent**.

- Positive: `is_primary_seam_divergence()` correctly requires `A-ACCEPT` and `KernelDecision.DENY_FALSE` only (`xz_protocol_condition_a.py:354-360` onward; tests at `test_xz_protocol_condition_a.py:152-182`).
- Positive: `DENY_UNKNOWN` is excluded from primary seam divergence.
- Limitation: no packet-level seam pipeline is shipped to verify denominator accounting, role uniqueness, or packet identity enforcement end-to-end.

### 6. CR-12 enforcement and raw-evidence/schema gating

Assessment: **not executable as shipped**.

What is missing:

- no packet schema
- no raw-evidence record classes
- no evaluator recomputing conjuncts from raw records
- no cutoff verifier
- no manifest-digest verifier
- no structural rejection of out-of-schema derived decision fields

The shipped kernel accepts only pre-labeled `ConjunctVector` objects. That is a kernel core, not an end-to-end CR-12 enforcement surface.

### 7. Source-frame adequacy

Assessment: **partially improved, still incomplete**.

- Positive: the executable `FRAME_START` is corrected to `2023-10-01`, and the exact 180-day test passes.
- Remaining issues:
  - zero transparency-log sources despite `SourceCategory.TRANSPARENCY_LOG` existing (`xz_protocol_source_frame.py:45-52`; audit check shows `0`)
  - `SRC-ML-02` uses `url="(multiple; see retrieval rule)"` instead of canonical enumerated entries (`xz_protocol_source_frame.py:236-246`)
  - no signed universe commitment or manifest digest
  - `validate_manifest()` is weak and still returns `valid=True` with those omissions (`xz_protocol_source_frame.py:325-365`)

### 8. WithinAuth conformity to SHUDP Axiom 5

Assessment: **partial only**.

- Positive: the truth-table rule matches the basic Axiom 5 WithinAuth predicate: any `YES` => `INSIDE`, all `NO` => `OUTSIDE`, otherwise `UNKNOWN`.
- Remaining gap: SHUDP v0.5 keeps axiom-level A5 status distinct from event-level adjudicative verdict; the shipped artifact has only a single verdict layer.
- Remaining gap: the “independent CI” decoy sets `CAUSE = NO` while its own evidence says pushes trigger the CI (`xz_protocol_control_graph.py:208-212`). That is contestable under the literal “can cause” language.

### 9. Trust-root weaknesses

Assessment: **still unresolved**.

- The public-key file exists and the three roles are distinct.
- But the package ships no manifest digest, no signatures, no seal receipts, and no verifier binding those keys to any concrete committed object.
- The trust-roots file itself still says `"protocol": "XZ Protocol v0.2"` (`xz_protocol_trust_roots_PUBLIC.json:2`).

### 10. Safety / prohibited-language enforcement

Assessment: **mostly intact at prose/code surface, weak in executable enforcement**.

- `test_xz_protocol_source_frame.py:137-140` uses `or` in `test_no_payload_hashes`, so it fails only when both “payload” and “hash” appear together.
- `test_xz_protocol_adversarial.py:221-243` scans only four Python modules, not the full package, not the JSON file, and not the missing normative prose artifact.
- No package-wide verifier is shipped for prohibited-language integrity.

### 11. Nondeterminism

Assessment: **no material numerical nondeterminism in tested paths, but import-time randomness exists**.

- Positive: the numerical Phase A suite uses explicit seeds and a same-seed reproducibility test (`xz_protocol_phase_a_tests.py:341-348`).
- Remaining caveat: `xz_protocol_condition_a.py:159` and `xz_protocol_phase_a_m3.py` create import-time random accident-guard tokens via `secrets.token_hex(16)`. Functional logic remains deterministic within a process, but raw object fields are not cross-process stable if serialized.

## Findings Ordered By Severity

### 1. Critical - The v0.3 package omits the normative protocol text needed to verify carry claims

**Where**

- Package inventory: no `xz_protocol_v0_3.md`
- Dispatch only: `DISPATCH_XZ_v03_GPT.md:1-10`

**What**

The package lacks the normative v0.3 prose specification. The dispatch is only a short task note and cannot substitute for the missing protocol text.

**Why it matters**

Without `xz_protocol_v0_3.md`, this audit cannot verify:

- the authoritative v0.3 Section 22 wording
- the v0.3 freeze-blocker register
- whether the code and tests match the intended amended prose
- whether the package is complete enough for carrying status

This is a carrying blocker.

### 2. Critical - Independent SHA-256 verification cannot be completed

**Where**

- `DISPATCH_XZ_v03_GPT.md:9-10`
- Package search found no authoritative manifest/digest

**What**

The package supplies no independent file-hash manifest and no signed manifest digest covering the 13 normative files.

**Why it matters**

The task requirement was to verify SHA-256 for all 13 normative files against an authoritative manifest “actually supplied or embedded.” That is not possible from the shipped bytes. Only self-computed reproducibility hashes can be reported.

### 3. High - B-2 is not discharged because the 27-test adversarial suite is materially weaker than its claimed coverage

**Where**

- `test_xz_protocol_adversarial.py:37-243`
- v0.2 Section 22 baseline requirement in `xz_protocol_v0_2.md:687-692`

**What**

The suite reaches 27 passing tests and includes headings for all nine claimed categories, but multiple categories are reduced to stand-ins that do not attack the actual protocol surfaces their labels imply.

**Why it matters**

Count is not quality. This package does not yet provide convincing executable evidence that the specific Section 22 adversarial cases have been discharged.

### 4. High - Condition B remains kernel-only; CR-12 and end-to-end seam-path enforcement are still unverified

**Where**

- `xz_protocol_kernel.py:83-122`
- Package-wide search found no packet/schema/raw-evidence evaluator

**What**

The kernel core is present, but the package still lacks the raw-evidence/packet/schema surfaces required to recompute conjuncts from raw records and reject caller-supplied derived facts structurally.

**Why it matters**

This leaves CR-12 and end-to-end CR-3 verification incomplete even though the kernel truth table itself is well tested.

### 5. Medium - Condition A remains weaker than the inherited SHVVP comparator and bypasses its own accident-guard provenance

**Where**

- `xz_protocol_condition_a.py:120-151`
- `xz_protocol_condition_a.py:166-212`
- `xz_protocol_condition_a.py:264-327`
- Parent SHVVP reference baseline extracts around SLSA/in-toto/Sigstore

**What**

- `SLSA_PROVENANCE`, `IN_TOTO_ATTESTATION`, and `STEP_ATTESTATION` are defined but never mandatory.
- `evaluate_boundary()` accepts directly instantiated `BaselineCheckResult` objects with empty `_provenance`.

**Why it matters**

The NOT_APPLICABLE bug is fixed, but the conventional comparator remains lighter than the inherited baseline it claims to embody, which still leaves manufacture-risk pressure on seam comparisons.

### 6. Medium - WithinAuth remains only partially Axiom-5-conformant

**Where**

- `xz_protocol_control_graph.py:128-155`
- `xz_protocol_control_graph.py:185-231`
- `test_xz_protocol_control_graph.py:18-145`

**What**

The truth table is correct, but the shipped artifact does not represent the separate axiom-level A5 status SHUDP v0.5 requires, and one decoy’s `CAUSE = NO` assessment is contestable on its own stated facts.

**Why it matters**

This is sufficient for a helper-level WithinAuth truth table, not for a full Axiom 5 carrying claim.

### 7. Medium - Safety/prohibited-content enforcement is still heuristic and incomplete

**Where**

- `test_xz_protocol_source_frame.py:137-147`
- `test_xz_protocol_adversarial.py:221-243`

**What**

The package uses small heuristic scans rather than a whole-package verifier, and one test uses a logically weak `or` check.

**Why it matters**

This is not strong enough evidence for a carry-grade safety-rule integrity claim.

### 8. Low - Version drift remains inside shipped artifacts

**Where**

- `xz_protocol_condition_a.py:4`
- `xz_protocol_source_frame.py:4,12-15,36`
- `xz_protocol_control_graph.py:4`
- `xz_protocol_trust_roots_PUBLIC.json:2`

**What**

Several artifacts still identify themselves as `v0.2`, and one source-frame header still contains the old pre-fix start date.

**Why it matters**

This does not break execution, but it weakens confidence in package coherence and makes the missing v0.3 spec more consequential.

## Required Amendments

1. Ship `xz_protocol_v0_3.md` and make it the authoritative normative prose artifact for this package.
2. Ship an independent SHA-256 manifest or signed manifest digest covering the full normative set, plus a verifier.
3. Ship the missing Condition B packet/raw-evidence/schema/cutoff surfaces that recompute kernel inputs from raw evidence and enforce CR-12 structurally.
4. Replace the proxy Section 22 tests with concrete negative tests for commitment-ID confusion, trust-root override, packet-regime mixing, post-cutoff evidence injection, role remapping after outcomes, and screened-event suppression.
5. Either align the Condition A baseline profile with the inherited SHVVP comparator or amend the prose standard explicitly and visibly.
6. Ship trust-root signatures / seal receipts / manifest binding, not just public keys.
7. Make safety/prohibited-language verification package-wide and deterministic.
8. Normalize version strings and stale comments so the shipped artifacts consistently identify the actual package version.

## Reproducibility Commands

```bash
python3 -m venv /tmp/xz_v03_audit_venv
/tmp/xz_v03_audit_venv/bin/pip install -q pytest numpy==2.4.4 scipy==1.17.1

cd /home/user/workspace/xz_protocol_v0_3_audit

sha256sum \
  test_xz_protocol_adversarial.py \
  test_xz_protocol_condition_a.py \
  test_xz_protocol_control_graph.py \
  test_xz_protocol_kernel.py \
  test_xz_protocol_source_frame.py \
  xz_protocol_condition_a.py \
  xz_protocol_control_graph.py \
  xz_protocol_kernel.py \
  xz_protocol_phase_a_intervals.py \
  xz_protocol_phase_a_m3.py \
  xz_protocol_phase_a_tests.py \
  xz_protocol_source_frame.py \
  xz_protocol_trust_roots_PUBLIC.json

/tmp/xz_v03_audit_venv/bin/pytest -q --collect-only \
  xz_protocol_phase_a_tests.py \
  test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py \
  test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py \
  test_xz_protocol_kernel.py

/tmp/xz_v03_audit_venv/bin/pytest -q \
  xz_protocol_phase_a_tests.py \
  test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py \
  test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py \
  test_xz_protocol_kernel.py
```

## Carrying-Scope Statement

This report is the GPT-5.6 seat only. It audits only the bytes and references described above. It does not satisfy or imply the required Kimi/second carrying seat, convergent two-family carry, or any non-HALT decision from another seat. On this seat’s executed scope, the correct verdict is **HALT**.

---

# Bismillah ir-Rahman ir-Rahim
