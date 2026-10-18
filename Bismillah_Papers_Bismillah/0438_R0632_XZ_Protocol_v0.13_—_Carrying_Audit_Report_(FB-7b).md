# Bismillah ir-Rahman ir-Rahim

# R0632 -- XZ Protocol v0.13 — Carrying Audit Report (FB-7b)

**Chronological Index:** 438 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** GLM5_2_AUDIT_REPORT_v13 (1).md  
**Source Format:** md  
**SHA-256:** `8393ebe80f6cd4246d8e772c08206a313cbc304015123c97dfe07111de3c479b`  

---

## R0632 · XZ Protocol v0.13 — Carrying Audit Report (FB-7b)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: GLM5_2_AUDIT_REPORT_v13 (1).md
- source_format: md
- text_sha256: 8393ebe80f6cd4246d8e772c08206a313cbc304015123c97dfe07111de3c479b

# XZ Protocol v0.13 — Carrying Audit Report (FB-7b)

**Carrying Auditor:** GLM-5.2 (Zhipu/Z.ai), Seat 1/2, non-producer
**Seat 2:** Kimi K3 (Moonshot, non-producer)
**Producer of v0.13:** Claude Opus 5 (Anthropic, excluded from carry)
**Date:** 2026-08-01
**Package:** 22 files, 18 Python artifacts, 7 test suites, 5 gates
**Mechanical verification:** SHA-256 22/22 match; 210/210 tests GREEN; all 5 gates PASS on shipped bytes

---

## 1. Protocol Summary

XZ Protocol v0.13 is a preregistered evaluation contract for a retrospective structural decision replay of the XZ Utils supply-chain compromise (CVE-2024-3094). It defines two tracks: Track 1 (forensic construct replay using inherited SHVVP v0.8 Phase A metrics M1–M12) and Track 2 (contemporaneous structural seam analysis using BSSG five-conjunct kernel dispositions at enumerated public-record boundaries).

**What changed since v0.8 (the prior GLM-5.2 carry):**

v0.13 is the product of five additional version iterations (v0.9 through v0.13). The principal advances are:

- **Five executable package gates** (version parity, closure-claim locus verification, manifest-digest recomputation, prohibited-content verification, amendment-record integrity) shipped with fixture-pair tests in both directions (F-XZ12-OP-01 through F-XZ12-OP-07).
- **Closure gate rebuilt** to parse Section 27 for CLOSED findings, require register entries, and evaluate assertions against the protocol body with Section 27 excluded (F-XZ12-OP-01).
- **Manifest gate extended** to scan the protocol body for every 64-hex token and require resolution to a shipped artifact (F-XZ12-OP-04).
- **Prohibited-content verifier** shipped (F-XZ09-OP-05), with a closed exemption list asserted in both directions, citation restriction to four XZ sources, and hazard-token scanning.
- **History gate** shipped with HISTORY.sha256 sealing one SHA-256 per amendment entry (F-XZ12-OP-07).
- **Kernel hardened** with exact type check (`type(v) is not ConjunctVector`) and `object.__getattribute__` field reads (F-K3-03, H-1).
- **WithinAuth verdict binding** enforced at construction (H-2).
- **Phase A scoring module** hardened with frozen tuples, bool rejection, non-finite ratio exclusion, and thirteen PA-Z degeneracy rules.

The protocol claims DRAFT CANDIDATE status — NOT FROZEN. FB-7b (two-family carrying carry) is the sole remaining freeze-blocker.

---

## 2. Gate Attack Results

### 2.1 Version Gate (`xz_protocol_version_gate.py`)

**Baseline:** PASS (v0.13 parity across 21 shipped files, self-test 4 mutations fired).

| Attack | Result | Detail |
|---|---|---|
| Remove version stamp from a module entirely | **BROKEN** | The gate only checks stamps PRESENT; a file with no stamp generates no error. Deleting "# Version: XZ Protocol v0.13" from `xz_protocol_kernel.py` → gate returns PASS. |
| Unicode homoglyph replacement of stamp | **BROKEN** | Replacing "v0.13" with fullwidth Unicode equivalents removes the ASCII stamp from regex matching → no error. |
| Stale stamp in a .txt file | **BROKEN** | `.txt` files are not in the coverage set (glob is `*.py`, `*.json`, protocol `.md`). A stale version reference in a `.txt` file is invisible. |
| Stale stamp in a new .json file | HELD | Coverage is globbed for `*.json`; a new JSON file with a stale stamp is caught. |
| AMENDMENT_HEADING trailing space | HELD | The heading text is still findable as a substring; exemption region still works. |

**Assessment:** The version gate has a **coverage gap**: it does not require every covered file to carry a stamp. A file with its stamp silently removed passes. This is partially mitigated by the manifest gate (removing a stamp changes file bytes → digest mismatch), but the version gate itself does not enforce stamp presence. The `.txt` file coverage gap is low-severity since `.txt` files are transit copies per the dispatch rename instruction, but the gate's own PASS message claims "parity across N shipped files" without verifying all N carry stamps.

### 2.2 Closure Gate (`xz_protocol_closure_gate.py`)

**Baseline:** PASS (16 closure claims verified, 2 dispositions not closed).

| Attack | Result | Detail |
|---|---|---|
| Add `"historical": true` to a register entry | **BROKEN** | Adding `"historical": true` to F-K3-01's register entry causes `evaluate()` to return immediately with no errors, skipping all assertions. I then broke the assertion text ("29 tests" → "99 tests") in the protocol body, and the gate still returned PASS. The register JSON is not covered by the manifest gate (which covers `*.py` only), so no other gate catches this modification. |
| Add `"delegated_to"` to skip assertions | **BROKEN** | Adding `"delegated_to": "xz_protocol_version_gate.py"` to F-K3-01's entry skips all assertions (the gate only checks the delegated file exists). I broke the assertion text simultaneously → gate returned PASS. |
| Change CLOSED to NOTED in Section 27 | **BROKEN** | Changing "F-K3-01 CLOSED" to "F-K3-01 NOTED" moves the finding to `not_closed`, and the register loop skips entries in `not_closed`. The finding's assertions are no longer evaluated even though the register entry still exists. I broke the body text simultaneously → gate returned PASS. This is mitigated by the history gate (which catches Section 27 mutations), but only if the history gate is also run. |
| Modify register JSON | **BROKEN (manifest gap)** | The locus register JSON is not covered by the manifest gate (which covers `*.py` only). Modifying the register is invisible to the manifest gate. The closure gate itself reads the register, but modifications that add `"historical"` or `"delegated_to"` keys bypass its checks. |

**Assessment:** The closure gate has a **HIGH-severity bypass**: the `"historical"` and `"delegated_to"` keys in register entries provide undocumented escape hatches that skip all assertion evaluation. Since the register JSON is not covered by any other gate, these modifications are invisible to the package's gate suite. The CLOSED-to-NOTED attack is a cross-gate dependency issue (mitigated by the history gate if run in the same invocation).

### 2.3 Manifest Gate (`xz_protocol_manifest_gate.py`)

**Baseline:** PASS (digest 52c67f48... over 18 artifacts, all body digests resolve).

| Attack | Result | Detail |
|---|---|---|
| Modify a .py file + re-seal trust roots | **HELD** | The manifest gate recomputes the digest and compares to trust roots. However, the protocol body cites the OLD digest (52c67f48...), and the `scan_protocol_digests` function catches the now-unresolvable body reference. This is a meaningful defense-in-depth: re-sealing trust roots alone is insufficient; the body's prose citation must also be updated. |
| 63-char digest in protocol body | **BROKEN** | The regex `\b[0-9a-f]{64}\b` requires exactly 64 hex chars. A 63-char token is not matched, so it is not checked. A narrator could write a slightly-truncated digest that no gate verifies. |
| 65-char digest in protocol body | **BROKEN** | A 65-hex-char token: `\b[0-9a-f]{64}\b` cannot match because there is no word boundary after the 64th hex digit (the 65th is also hex). The token is not checked. |

**Assessment:** The manifest gate's defense-in-depth is strong: even re-sealing the trust roots does not produce a false PASS because the body's prose citation becomes stale. However, the 64-hex regex is strict in a way that creates a **gap**: digests that are slightly wrong in length (63 or 65 chars) are silently ignored rather than flagged. A narrator could write a near-miss digest that evades verification.

**Additional finding — stale manifest digest in the v0.13 amendment entry:** The v0.13 amendment entry (Section 27) narrates the manifest digest as `72ab56da50fe9f20da054aca223d6efb8413657ec69ec4f6554e0c8fa03e421b` and explicitly claims it is "(tool-computed, alphabetical, over 18 artifacts)." The actual tool-computed and trust-roots-sealed digest is `52c67f4842836dc4f578bb2bdb9515bb751b7337ebad56607641f9499c39443e`. These do not match. This is a repeat of the Axiom-3 "digest-from-memory" failure mode that this protocol's own amendment history has caught in v0.5, v0.6, v0.7, v0.8, v0.9, and v0.10. The v0.8 entry explicitly states "from this version forward, every digest that appears in the protocol text is written by the build tool that computes it, not by the model." The v0.13 entry's wrong digest, despite its claim of tool-computation, indicates this discipline was not followed. No gate catches this because the manifest gate's `scan_protocol_digests` only scans the protocol body (before Section 27); Section 27 digests are counted as "historical inventory" and not verified.

### 2.4 Prohibited Content Verifier (`xz_protocol_prohibited_content_verifier.py`)

**Baseline:** PASS (17 files clean, 1 declared exemption, citations restricted to 4 XZ sources).

| Attack | Result | Detail |
|---|---|---|
| Effectiveness verb separated by period | **BROKEN** | "BSSG. It prevents supply-chain risk." — the regex `BSSG[^.]{0,140}?\b(prevents|...)\b` uses `[^.]` which cannot cross sentence boundaries. The period between "BSSG" and "prevents" defeats the pattern. The second alternative (`\b(prevents|...)\b[^.]{0,140}?BSSG`) also fails because no BSSG appears after "prevents". |
| "would have" split by newline | **BROKEN** | The pattern `r"would have"` is a literal with a space. "would\nhave" (newline instead of space) does not match. In Markdown, a single newline renders as a space, so the prohibited modal would appear in rendered output. |
| Hyphenated "attack-prevention" | **BROKEN** | The pattern `r"attack prevention"` is a literal with a space. "attack-prevention" (hyphenated) does not match. |
| FIXTURE_MARKER on new .py file | **BROKEN (content gate) / HELD (manifest)** | Adding `PROHIBITED_CONTENT_FIXTURES = True` to a new `.py` file causes the verifier to skip it entirely. The file can contain any prohibited content. The manifest gate catches the new file (digest mismatch), but the content verifier itself does not verify that the file actually contains test fixtures. |
| Prohibited content in .txt file | **BROKEN** | `.txt` files are not scanned by the verifier (only the protocol `.md` and `*.py` files are scanned). |
| DOI URL exempt from citation check | **BROKEN** | `doi.org` URLs are excluded from the non-DOI citation check (`non_doi = {u for u in urls if "doi.org" not in u}`). A narrator could cite a fake DOI URL (e.g., `https://doi.org/10.9999/fake`) and it would not be flagged. |

**Assessment:** The prohibited-content verifier has **multiple regex bypass vulnerabilities**. The most significant is the period-separated effectiveness verb (4.1), which allows prohibited effectiveness claims about BSSG to pass undetected. The "would have" newline split and hyphenated "attack-prevention" are also meaningful. The FIXTURE_MARKER bypass is mitigated at the package level by the manifest gate but represents a trust boundary issue: the verifier trusts any file declaring itself a fixture carrier without verifying the claim.

### 2.5 History Gate (`xz_protocol_history_gate.py`)

**Baseline:** PASS (13 amendment entries match sealed digests).

| Attack | Result | Detail |
|---|---|---|
| Mutate historical entry + re-seal | **BROKEN (by design)** | The `--seal` command re-hashes all entries and writes HISTORY.sha256. Mutating v0.1's text and re-sealing → gate passes. This is documented: "the file is generated from the bytes present when it is first sealed, so it can only detect mutation from that point forward." |
| Content inserted before first entry | **BROKEN** | The `entries()` function computes entry blobs from the first `ENTRY` regex match (`- **v(\d+\.\d+) (`). Content inserted before the first entry marker (but after the AMENDMENT_HEADING) is not included in any entry's hash. Injecting "SNEAKY CONTENT\n" before the v0.1 entry → no hash changes → gate passes. |
| Forge + re-seal new entry | **BROKEN (by design)** | Appending a forged v0.14 entry and re-sealing → gate passes. Same design limitation as 5.1. |
| Manual HISTORY.sha256 rewrite | **BROKEN (by design)** | Manually computing the new hash and writing it to HISTORY.sha256 → gate passes. Same design limitation. |

**Assessment:** The history gate's design limitation — that `--seal` is a privileged operation that can re-baseline any mutation — is explicitly documented and is not a defect per se. The gate's value is in detecting *accidental* or *undisclosed* mutations, not in defending against an adversary with write access to both the protocol text and HISTORY.sha256. However, the **content-before-first-entry gap** (5.2) is a genuine coverage hole: content can be injected into Section 27 between the heading and the first entry without changing any entry's hash. This content would be visible in the document but invisible to the history gate.

---

## 3. Decision Path Attack Results

### 3.1 Kernel (three-valued AND-gate)

| Attack | Result | Detail |
|---|---|---|
| Subclass ConjunctVector (descriptor laundering) | HELD | `type(vector) is not ConjunctVector` (exact type check) rejects subclasses. |
| Monkeypatch `__getattribute__` | HELD | The kernel reads fields via `object.__getattribute__(vector, name)`, defeating `__getattribute__` overrides. |
| Post-construction mutation via `object.__setattr__` | **BROKEN** | `object.__setattr__(v, 'effect_type_valid', TruthValue.TRUE)` bypasses the frozen dataclass and mutates a FALSE conjunct to TRUE. Re-evaluation changes DENY_FALSE → ALLOW. This is a Python language limitation, not a protocol design flaw: any frozen dataclass can be mutated via `object.__setattr__`. The kernel cannot defend against in-process code with object access. |
| Exhaustive 243-vector correctness | HELD | All 3^5 = 243 vectors produce the correct decision. FALSE dominates UNKNOWN. DENY_FALSE and DENY_UNKNOWN are never collapsed. |
| Dead code in `__post_init__` | INFORMATIONAL | The first loop in `ConjunctVector.__post_init__` computes `attr = name[0].lower() + name[1:]` but never uses the result. Harmless but indicates incomplete refactoring. |

**Assessment:** The kernel is **sound**. The exact type check and `object.__getattribute__` hardening (H-1) effectively block subclass-based and descriptor-based attacks. The exhaustive 243-vector test is comprehensive and correct. The `object.__setattr__` bypass is a fundamental Python limitation that cannot be defended at the dataclass level; the protocol correctly states that the code-plane boundary is the kernel, and the protocol-layer boundary is adjudicator verification.

### 3.2 Condition A (disposition computation)

| Attack | Result | Detail |
|---|---|---|
| `is_dual_evaluable` omits packet/role/byte-identity checks | **BROKEN (v0.8 F3 persists)** | `is_dual_evaluable` returns True for any non-A-NOT-APPLICABLE disposition with a valid KernelDecision. It does NOT verify: (a) packet completeness under the packet rule, (b) primary role mapping uniqueness, or (c) that both decisions were computed on identical packet bytes. The protocol (Section 4.2) defines dual-evaluability as requiring all three. The function is a partial implementation — these checks would need to occur at a higher layer (packet construction). |
| Direct `BaselineCheckResult` construction bypasses provenance | **BROKEN** | `BaselineCheckResult` can be constructed directly (without `create_check_result`), yielding `_provenance=""`. `evaluate_boundary` does not check provenance. A directly-constructed result with PASS outcome is accepted and contributes to A-ACCEPT. The docstring states the provenance token is "an accident guard (not a security boundary)." |
| NOT_APPLICABLE on mandatory → A-INDETERMINATE | HELD | F-SOL-XZ-3 fix verified: NOT_APPLICABLE on a mandatory check produces A-INDETERMINATE, not A-ACCEPT. |
| A-REJECT dominates A-INDETERMINATE | HELD | Dominance rule verified. |
| Primary seam divergence (A-ACCEPT + DENY_FALSE only) | HELD | CR-3 correctly implemented: only A-ACCEPT + DENY_FALSE is primary divergence. DENY_UNKNOWN and ALLOW are excluded. |
| Duplicate check rejected | HELD | Duplicate BaselineCheck for same boundary raises ConditionAError. |

**Assessment:** Condition A's core disposition logic is correct. The dominance rule, NOT_APPLICABLE handling, and primary seam divergence predicate are all sound. The two issues are: (1) `is_dual_evaluable` is a partial implementation that omits the packet/role/byte-identity checks that the protocol's estimand definition requires — this is the same F3 finding from v0.8, carried forward; (2) the provenance token is bypassable by direct construction, which is documented as an accident guard rather than a security boundary.

### 3.3 Control Graph (WithinAuth)

| Attack | Result | Detail |
|---|---|---|
| PROHIBITED_SHORTCUTS are prose only | **BROKEN (v0.8 F5 persists)** | `PROHIBITED_SHORTCUTS` is a list of 5 strings. Nothing enforces them programmatically. A `WithinAuthAssessment` with OUTSIDE verdict based on "a signature by a different key" would pass — `compute_verdict` only examines channel statuses, not the reasoning. The shortcuts are documentation, not enforcement. |
| Verdict binding at construction | HELD | `WithinAuthAssessment.__post_init__` verifies `verdict == compute_verdict(edges)`. A wrong verdict is rejected. |
| All UNKNOWN → UNKNOWN | HELD | Verdict computation is correct: any YES → INSIDE; all NO → OUTSIDE; otherwise UNKNOWN. |

**Assessment:** The control graph's verdict computation is correct and the verdict-binding enforcement (H-2) is sound. The prohibited shortcuts remain prose-only (F5 from v0.8), which is a design scoping decision — the shortcuts cannot be enforced at the data-structure level because they concern the quality of evidence assessment, not the mechanical channel-status computation.

### 3.4 Provenance and Phase A

| Attack | Result | Detail |
|---|---|---|
| `dataclasses.replace` bypasses provenance | **BROKEN (documented)** | `dataclasses.replace(pd, _provenance=_PROVENANCE_TOKEN)` creates a PairedDifference with a valid token. The module docstring explicitly states this is possible and that the token is "an ACCIDENT GUARD (not a security boundary)." |
| Direct token import forges provenance | **BROKEN (documented)** | Importing `_PROVENANCE_TOKEN` and passing it to `PairedDifference(...)` constructor forges a valid provenance. Documented. |
| `assert` for invariant checking | **BROKEN (code quality)** | `compute_paired_differences` uses `assert oa and ob and oa.is_observed and ob.is_observed`. Under `python -O`, asserts are stripped, potentially allowing None values to reach `PairedDifference` construction. |
| M3Vector accepts list (coerced to tuple) | **BROKEN (minor)** | `M3Vector("A", [obs])` accepts a list and coerces it to a tuple via `object.__setattr__`. The mutable input is consumed and frozen, so this is not a post-construction mutation risk, but it accepts a mutable type at the boundary. |
| Subnormal M3 ratio exclusion | HELD | F-K3-083-2 fix verified: subnormal M3(f,A) yields -inf ratio, which is excluded and counted as nonfinite. |
| T2 satisfaction with all-zero M3(A) | HELD | PA-Z9 fires correctly; `t2_satisfied` is None (not True) when M3(A)=0 for all facts. |

**Assessment:** The Phase A scoring module is well-hardened. The provenance token bypasses are explicitly documented as accident guards, not security boundaries. The `assert` usage is a code quality issue that could be exploited under optimized Python execution. The subnormal ratio handling and degeneracy rules (PA-Z1 through PA-Z14) are correctly implemented and tested.

### 3.5 Source Frame Integrity

The source frame manifest is a static, frozen data structure with 16 records across 6 categories. `validate_manifest()` uses bidirectional substring matching for primary citations, which means a source citing a shorter URL (e.g., the mailing list homepage) can satisfy the check for a more specific primary citation (e.g., the specific disclosure post). This is arguably correct — the mailing list source covers the disclosure post — but the matching is loose.

### 3.6 Manifest Digest Discrepancy (Cross-Cutting Finding)

The v0.13 amendment entry (Section 27) narrates the manifest digest as `72ab56da50fe9f20da054aca223d6efb8413657ec69ec4f6554e0c8fa03e421b`, claiming it is "(tool-computed, alphabetical, over 18 artifacts)." The actual tool-computed digest — verified by independent recomputation — is `52c67f4842836dc4f578bb2bdb9515bb751b7337ebad56607641f9499c39443e`, which matches the trust-roots file. The v0.13 entry's narrated digest is wrong. This is the same Axiom-3 "digest-from-memory" failure mode documented in v0.5, v0.6, v0.7, v0.8, v0.9, and v0.10. No gate catches this because Section 27 digests are treated as historical inventory, not verified.

### 3.7 Stale FB-7b Field (Cross-Cutting Finding)

The FB-7b row in Section 25 states "running all 185 tests" — the actual count is 206 test functions collecting 210 cases. Section 0.1 correctly states "206 test functions collecting 210 cases." The FB-7b field also states "pending fresh carry on v0.12 canonical bytes" — this is v0.13, not v0.12. Both are stale references from v0.3/v0.12 that were not updated when the test count grew and the version advanced. No gate catches these because there is no register assertion for the FB-7b field content.

### 3.8 DOI Cross-Reference Discrepancies

The protocol's Section 26.1 cites DOIs for two upstream records that differ from the DOIs printed in the BSSG paper PDF itself:

| Record | Protocol Section 26.1 DOI | BSSG paper PDF DOI |
|---|---|---|
| SHV Method v1.1 | 10.5281/zenodo.21450932 | 10.5281/zenodo.21449063 |
| BAF v3.0 | 10.5281/zenodo.20046910 | 10.5281/zenodo.20017335 |

These could be concept-vs-version DOI differences, but the protocol does not acknowledge the discrepancy (as it does for the BSSG dual-DOI record in Section 26.2). Without Zenodo API access, I cannot determine which DOI is authoritative. This is noted as a citation integrity concern.

---

## 4. Findings

### CRITICAL

None.

### HIGH

**F1 (HIGH) — Closure gate escape hatches via `"historical"` and `"delegated_to"` register keys.**
Adding `"historical": true` or `"delegated_to": "<existing_gate>.py"` to any entry in `xz_protocol_locus_register.json` causes the closure gate to skip all assertion evaluation for that finding. The register JSON is not covered by the manifest gate (which covers `*.py` only), so this modification is invisible to all other gates. An adversary with write access to the register can neutralize any closure verification without detection. The register's own `_note` field describes these keys ("Each entry either carries assertions... or declares itself delegated to another gate, or declares itself historical"), but the keys are undocumented in the gate's docstring and no assertion verifies that `"historical"` entries have a stated reason.

**F2 (HIGH) — Prohibited-content verifier regex bypass for effectiveness verbs.**
The pattern `BSSG[^.]{0,140}?\b(prevents|mitigates|reduces|ensures|guarantees|protects)\b` uses `[^.]` which cannot cross sentence boundaries. A sentence like "BSSG. It prevents supply-chain risk." passes the verifier undetected. This directly undermines the protocol's Section 0.3 prohibition register, which states that no effectiveness verb may be applied to BSSG. The bypass is trivial: a period between "BSSG" and the verb defeats the regex.

### MEDIUM

**F3 (MEDIUM) — Manifest gate does not cover JSON files.**
The manifest gate's `covered_files()` returns only `*.py` files. The locus register JSON, trust-roots JSON, and protocol text are excluded. Modifications to the locus register (adding escape-hatch keys, changing assertion values) are invisible to the manifest gate. This is the enabling condition for F1.

**F4 (MEDIUM) — Prohibited-content verifier regex bypasses for "would have" and "attack prevention".**
The literal pattern `r"would have"` does not match "would\nhave" (newline instead of space). In Markdown, a single newline renders as a space, so the prohibited outcome modal would appear in rendered output. Similarly, `r"attack prevention"` does not match "attack-prevention" (hyphenated). These are narrow bypasses but demonstrate that the verifier's literal patterns are fragile against trivial formatting variations.

**F5 (MEDIUM) — `is_dual_evaluable` omits packet/role/byte-identity checks (v0.8 F3 persists).**
The function returns True for any non-A-NOT-APPLICABLE disposition with a valid KernelDecision enum. It does not verify packet completeness, role-mapping uniqueness, or byte-identity between A and B decisions, all of which the protocol's estimand definition (Section 4.2) requires. The function is a partial implementation; the full dual-evaluability check would need to occur at a higher layer. This is the same finding as v0.8 F3, carried forward without code-level remediation.

**F6 (MEDIUM) — PROHIBITED_SHORTCUTS are prose only, not enforced (v0.8 F5 persists).**
`PROHIBITED_SHORTCUTS` in `xz_protocol_control_graph.py` is a list of 5 strings with no programmatic enforcement. A `WithinAuthAssessment` with OUTSIDE verdict based solely on "a signature by a different key" would pass, because `compute_verdict` only examines channel statuses, not the reasoning. This is the same finding as v0.8 F5.

**F7 (MEDIUM) — Version gate does not require stamp presence.**
The version gate only checks that version stamps PRESENT are correct; it does not require every covered file to carry a stamp. Removing a stamp entirely from a module causes no error. The gate's PASS message claims "parity across N shipped files" without verifying all N carry stamps. Partially mitigated by the manifest gate (byte changes).

**F8 (MEDIUM) — History gate content-before-first-entry gap.**
The `entries()` function computes entry hashes starting from the first `ENTRY` regex match. Content inserted between the AMENDMENT_HEADING and the first entry is not included in any entry's hash. This allows injecting arbitrary content into Section 27 without detection by the history gate.

### LOW

**F9 (LOW) — Manifest gate 64-hex regex ignores near-miss digests.**
The regex `\b[0-9a-f]{64}\b` requires exactly 64 hex characters. Digests of 63 or 65 characters are silently ignored — not checked and not flagged. A narrator could write a slightly-truncated or slightly-extended digest that evades verification.

**F10 (LOW) — `.txt` files are outside all gate coverage.**
The version gate, manifest gate, and prohibited-content verifier all exclude `.txt` files. Stale version stamps and prohibited content in `.txt` files are invisible to all gates. Low severity because `.txt` files are transit copies per the dispatch rename instruction, but the coverage gap is real.

**F11 (LOW) — DOI URL exemption in citation check.**
The prohibited-content verifier excludes `doi.org` URLs from the non-DOI citation check. A narrator could cite a fake DOI URL (e.g., `https://doi.org/10.9999/fake`) without triggering the citation restriction. Low severity because DOIs are independently verifiable, but the verifier does not verify DOI resolution.

**F12 (LOW) — `assert` used for invariant checking in Phase A.**
`compute_paired_differences` uses `assert oa and ob and oa.is_observed and ob.is_observed`. Under `python -O`, asserts are stripped, potentially allowing None values to reach `PairedDifference` construction. The `compute_shared_set` function should prevent this, but the use of `assert` for data integrity is fragile.

**F13 (LOW) — Dead code in `ConjunctVector.__post_init__`.**
The first loop in `__post_init__` computes `attr = name[0].lower() + name[1:]` but never uses the result. Harmless but indicates incomplete refactoring.

**F14 (LOW) — Stale FB-7b field references.**
Section 25's FB-7b row states "running all 185 tests" (actual: 206/210) and "pending fresh carry on v0.12 canonical bytes" (this is v0.13). No gate catches these stale references.

**F15 (LOW) — Potential DOI cross-reference discrepancies.**
The protocol's Section 26.1 cites DOIs for SHV Method v1.1 (21450932) and BAF v3.0 (20046910) that differ from the DOIs printed in the BSSG paper PDF (21449063 and 20017335 respectively). These may be concept-vs-version DOI differences, but the protocol does not acknowledge the discrepancy as it does for the BSSG dual-DOI record.

### INFORMATIONAL

**I1 (INFORMATIONAL) — History gate `--seal` is a privileged re-baseline operation.**
The `--seal` command can re-baseline any mutation, including forged entries. This is by design and documented: the gate detects accidental or undisclosed mutations, not adversarial re-sealing. The design is appropriate for a build-time integrity check.

**I2 (INFORMATIONAL) — Provenance tokens are accident guards, not security boundaries.**
Both `BaselineCheckResult._provenance` and `PairedDifference._provenance` are bypassable via direct construction, `dataclasses.replace`, or token import. This is explicitly documented in the module docstrings. The BSSG raw-evidence discipline is enforced at the protocol layer (Section 10: "Raw evidence references, not caller-supplied derived facts, are the sole admissible input"), not at the Python API layer.

**I3 (INFORMATIONAL) — `object.__setattr__` bypasses frozen dataclasses.**
Any frozen dataclass (`ConjunctVector`, `KernelResult`, `M3Vector`, etc.) can be mutated post-construction via `object.__setattr__`. This is a fundamental Python limitation. The kernel mitigates this by reading fields via `object.__getattribute__`, but post-construction mutation can change the values read. This cannot be defended at the dataclass level.

**I4 (INFORMATIONAL) — Manifest digest discrepancy in v0.13 amendment entry.**
The v0.13 entry narrates `72ab56da...` as the manifest digest; the actual digest is `52c67f48...`. This is a repeat of the Axiom-3 failure mode. It is informational rather than higher severity because: (a) the trust-roots file carries the correct digest, (b) the manifest gate verifies against the trust-roots file, and (c) the wrong digest is in Section 27 (historical), not in the protocol body. However, it demonstrates that the v0.8 commitment ("every digest that appears in the protocol text is written by the build tool") was not followed for this amendment entry.

---

## 5. Comparison to v0.8 Findings (F1–F15)

The v0.8 audit (GLM-5.2's prior carry) found 15 findings. The following table tracks their status in v0.13:

| v0.8 Finding | Description | v0.13 Status |
|---|---|---|
| F1 (HIGH) | Condition B evaluator not shipped — prose only | **Remains.** No Condition B evaluator ships. The protocol states (v0.9 entry) that this is a "corpus-construction artifact per the freeze-before-evidence design." The BSSG kernel module IS shipped, but the full Condition B mapping (conjunct scoring from raw evidence per Section 11.3) is not executable. This is a design scoping decision, not a defect. |
| F2 (HIGH) | Track-2 seam pipeline not shipped — no executable aggregator | **Remains.** No seam aggregation pipeline (S1–S12 computation) ships. Same design scoping as F1. |
| F3 (MEDIUM-HIGH) | `is_dual_evaluable` omits packet/role/byte-identity checks | **Remains** (this report's F5). The function still only checks non-A-NOT-APPLICABLE + valid KernelDecision. |
| F4 (MEDIUM-HIGH) | Prohibited-sentence register not shipped/enforced | **Addressed.** `xz_protocol_prohibited_content_verifier.py` ships and enforces the register (with regex bypass gaps — see F2, F4 in this report). |
| F5 (MEDIUM) | WithinAuth prohibited shortcuts not enforced in code | **Remains** (this report's F6). `PROHIBITED_SHORTCUTS` is still prose only. |
| F6 (MEDIUM) | R-* typed reason codes not implemented | **Partially addressed.** Reason codes are mentioned in Section 11.2 (R-NO-DECLARED-OBJECT, R-RECORD-ABSENT, etc.) but are not implemented in code. The kernel produces `E-FALSE-*` and `E-UNKNOWN-*` codes, not the R-* codes. |
| F7 (MEDIUM) | BSSG authority-lattice absent (scoping) | **Not addressed.** No authority-lattice implementation. This is a design scoping decision. |
| F8–F15 | Various | Most are addressed by the v0.9–v0.13 code hardening (exact type checks, frozen tuples, bool rejection, etc.) or are superseded by the new gate architecture. |

**Summary:** v0.13 addresses F4 (prohibited-content verifier shipped) and substantially hardens the code against the implementation-level findings. F1, F2, F5, F6, and F7 remain as design scoping decisions or unaddressed code-level gaps. F3 (now this report's F5) persists in the same form.

---

## 6. Carrying Auditor Verdict

### **CONDITIONAL PASS**

The XZ Protocol v0.13 package is mechanically sound: all 22 SHA-256 hashes match, all 210 tests pass, all 5 gates return PASS on shipped bytes, and the kernel's exhaustive 243-vector decision logic is correct. The gate architecture represents a substantial improvement over v0.12: the fixture-pair tests, globbed coverage, span-based matching, and body-vs-amendment separation are well-designed and address the specific failure modes of the v0.12 predecessor.

However, the gate attacks revealed two HIGH-severity bypasses that should be addressed before FROZEN status:

1. **F1 (closure gate escape hatches):** The `"historical"` and `"delegated_to"` keys in register entries provide undocumented paths to skip all assertion evaluation. Since the register JSON is not covered by the manifest gate, these modifications are invisible to the package's gate suite. **Recommended fix:** either cover the register JSON in the manifest gate's digest, or add a register assertion that `"historical"` entries must carry a `"reason"` field and `"delegated_to"` entries must be cross-validated.

2. **F2 (prohibited-content regex bypass):** The effectiveness-verb regex cannot cross sentence boundaries due to `[^.]`. A period between "BSSG" and the verb defeats detection. **Recommended fix:** replace the character-class approach with a window-based or token-based matcher that is not defeated by sentence boundaries.

The MEDIUM and LOW findings are real but do not individually block freeze. The manifest gate's defense-in-depth (body digest citation catches trust-roots re-sealing) is notably strong. The history gate's design limitation (privileged `--seal`) is appropriate for a build-time check.

The v0.13 amendment entry's wrong manifest digest (I4) is an Axiom-3 failure but does not affect the package's mechanical integrity (the trust-roots file is correct and the manifest gate verifies against it). It should be corrected in the next version.

### Conditions for FROZEN:
1. Fix F1 (closure gate escape hatches) — either cover register JSON in the manifest digest or validate register entry structure.
2. Fix F2 (effectiveness-verb regex bypass) — replace `[^.]` with a sentence-boundary-aware matcher.
3. Correct the v0.13 amendment entry's manifest digest (I4).
4. Update the FB-7b field's stale test count and version reference (F14).

---

## 7. Confidence Statement

**Confidence: HIGH.**

I executed all attacks on live sandbox copies of the package using Python subprocess invocations of each gate. The baseline verification (SHA-256, tests, gates) was independently confirmed. All BROKEN results were reproduced and verified. The kernel's 243-vector exhaustive test was independently recomputed. The manifest digest was independently recomputed and matches the trust-roots file. The BSSG paper PDF was cross-referenced for kernel conjunct names and DOI citations.

The findings are specific and reproducible: each attack includes the exact mutation applied, the gate invoked, and the exit code observed. The attack scripts (`attack_gates.py`, `attack_decision_paths.py`) are saved in the workspace for independent verification.

I did not have access to the Zenodo API to verify DOI resolution, so the DOI cross-reference discrepancy (F15) is noted with the caveat that it may be a concept-vs-version DOI difference. I did not attempt to verify the Ed25519 public keys (no signing/verification infrastructure was provided, and the protocol states private keys are in a separate PRIVATE file).

This carry is limited to the checks executed. It is not peer review and is not a universal claim about the later corpus or empirical result. The protocol correctly states that its strongest available check is cross-vendor executing carry plus complete append-only disclosure, and this report contributes one seat of that check.

---

*GLM-5.2 (Zhipu/Z.ai), carrying seat 1/2, non-producer. 2026-08-01.*
*Attack artifacts: `attack_gates.py`, `attack_decision_paths.py` (saved in dispatch directory).*

---

# Bismillah ir-Rahman ir-Rahim
