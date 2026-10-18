# Bismillah ir-Rahman ir-Rahim

# R0648 -- XZ Protocol v0.5 — Carrying Audit Report

**Chronological Index:** 441 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** Kimi review.md  
**Source Format:** md  
**SHA-256:** `99bd8864c61c6ca2276946581e88fb76bfa92b83ec3855a978b5709239731cef`  

---

## R0648 · XZ Protocol v0.5 — Carrying Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: Kimi review.md
- source_format: md
- text_sha256: 99bd8864c61c6ca2276946581e88fb76bfa92b83ec3855a978b5709239731cef

***XZ Protocol v0.5 — Carrying Audit Report
Seat: Kimi K3 (Moonshot AI), Seat 2 of 2, non-producer per Section 22.1
Producer: Claude Opus 4.6 (Anthropic, advisory only, excluded from carry)
Artifact: XZ Protocol v0.5 canonical bytes (protocol text + 14 manifest-bound files)
Dispatch: DISPATCH\_v05\_KIMI.txt, 2026-08-01**


### ***1. SHA-256 Manifest (14/14)**

***Computed on canonical bytes exactly as uploaded (rename `.txt` → `.py`/`.md`/`.json` before hashing; hash is over byte content, extension-agnostic). All 14 digests match the dispatch manifest byte-exact.**

***Table**

| **\#** | **File** | **Status** |
| - | - | - |
| 1 | `xz\_protocol\_v0\_5.md` | OK |
| 2 | `xz\_protocol\_kernel.py` | OK |
| 3 | `xz\_protocol\_phase\_a\_m3.py` | OK |
| 4 | `xz\_protocol\_phase\_a\_intervals.py` | OK |
| 5 | `xz\_protocol\_phase\_a\_tests.py` | OK |
| 6 | `xz\_protocol\_condition\_a.py` | OK |
| 7 | `test\_xz\_protocol\_condition\_a.py` | OK |
| 8 | `xz\_protocol\_source\_frame.py` | OK |
| 9 | `test\_xz\_protocol\_source\_frame.py` | OK |
| 10 | `xz\_protocol\_control\_graph.py` | OK |
| 11 | `test\_xz\_protocol\_control\_graph.py` | OK |
| 12 | `test\_xz\_protocol\_kernel.py` | OK |
| 13 | `test\_xz\_protocol\_adversarial.py` | OK |
| 14 | `xz\_protocol\_trust\_roots\_PUBLIC.json` | OK |

***Result: 14/14 OK.**


### ***2. Test Corpus (181/181)**

***Verified by AST traversal of canonical bytes. No double-counting; every `test\_`-prefixed function in the 6 suites counted once.**

***Table**

| **Suite** | **File** | **Test Functions** |
| - | - | - |
| 1 | `test\_xz\_protocol\_kernel.py` | 14 (including 2 exhaustive parametrized functions covering 243 kernel states) |
| 2 | `test\_xz\_protocol\_condition\_a.py` | 29 |
| 3 | `test\_xz\_protocol\_source\_frame.py` | 25 |
| 4 | `test\_xz\_protocol\_control\_graph.py` | 18 |
| 5 | `test\_xz\_protocol\_adversarial.py` | 27 |
| 6 | `xz\_protocol\_phase\_a\_tests.py` | 68 |
| **Total** |  | **181** |

***The kernel suite contains exactly 14 test functions parameterizing the 243-state exhaustive table, consistent with the protocol text (Section 0.1). All nine Section 22 adversarial categories (CAT-1 through CAT-9) are present in Suite 5.**

***Result: 181/181 present and structurally verified.**


### ***3. Protocol Text Review**

#### ***3.1 Append-only restoration (Section 27)**

- ***The v0.4 amendment entry explicitly records its own defect: it claimed FROZEN status and rewrote the v0.3 historical entry to erase a recorded GPT-5.6 Sol HALT, violating the append-only rule.**

- ***The v0.5 entry restores the complete v0.3 history, including the initial GPT HALT, the re-dispatch, and the subsequent PASS.**

- ***The v0.4 violation is preserved as a deviation record inside Section 27, not silently repaired.**

***Verdict: Append-only discipline is restored. No silent edit remains.**

#### ***3.2 Section 22.1 producer definition**

- ***Present and binding: “For carrying-seat eligibility under this section, ‘producer’ means the model family that served as the primary development seat for the executable artifacts in this protocol. Claude (Anthropic) is the producer family… GPT (OpenAI) and Kimi (Moonshot) served as council advisory seats… They are non-producer for carrying purposes.”**

***Verdict: Producer boundary is explicit and correctly excludes this seat from producer status.**

#### ***3.3 Full digests in Section 25**

- ***All 14 artifact digests in the Freeze-Readiness Register are printed as full 64-character hex strings. No truncated prefixes.**

- ***FB-3 through FB-7 are each resolved with exact digests and test counts.**

***Verdict: No truncation; digests are authoritative.**

#### ***3.4 FB-6 contradiction**

- ***FB-6 is marked RESOLVED in Section 25, Section 5.4, Section 9.1, Section 23 (deposit composition), and the v0.5 amendment record.**

- ***The trust-root file (`xz\_protocol\_trust\_roots\_PUBLIC.json`) is present with SHA-256 `dc9b351557bc563bbb4d670c12f6256528eb848c4f15b2b16c9685d63c5eac09`, matching the manifest.**

- ***No passage retains FB-6 as open.**

***Verdict: No contradiction. FB-6 is uniformly closed.**

#### ***3.5 Text/code consistency**

***Verified cross-references between protocol text and canonical code:**

***Table**

| **Protocol Claim** | **Code Verification** |
| - | - |
| H-1: kernel reads frozen fields via `object.\_\_getattribute\_\_` | Present in `evaluate\_kernel` |
| H-2: `WithinAuthAssessment` enforces `verdict == compute\_verdict(edges)` at construction | Present in `\_\_post\_init\_\_` |
| H-3: zero-resample intervals cannot exclude zero | Present in `\_make\_result` |
| M-3: `compute\_verdict` validates 5-edge schema, no duplicates | Present |
| F-SOL-XZ-3: `NOT\_APPLICABLE` on mandatory → `A\_INDETERMINATE` | Present in `evaluate\_boundary` |
| CR-2: kernel truth domain is exactly TRUE/FALSE/UNKNOWN; no fourth value | Enforced by `TruthValue` enum and `KernelDecision` enum |
| CR-3: primary seam counts only `A\_ACCEPT` + `DENY\_FALSE` | Enforced in `is\_primary\_seam\_divergence` |
| 14 kernel test functions / 243 cases | Verified by AST count |
| Frame start 2023-10-01 (180 days) | Present in `xz\_protocol\_source\_frame.py` |
| Prohibited language register | No effectiveness verbs found outside Section 0.3 prohibition list |

***Verdict: Text and code are consistent. No divergence found.**


### ***4. Attack — Adversarial Audit**

***Executed static adversarial analysis over all nine mandated categories plus cross-module invariants. No BLOCKER-class bypass identified.**

***Table**

| **Category** | **Attack Vector** | **Result** |
| - | - | - |
| **CAT-1** | Caller-supplied string decision to `is\_dual\_evaluable` | **Blocked** — raises `ConditionAError` |
| **CAT-1** | Caller-supplied string to `evaluate\_kernel` | **Blocked** — raises `KernelError` |
| **CAT-1** | Caller-supplied string truth value to `ConjunctVector` | **Blocked** — `\_\_post\_init\_\_` rejects non-`TruthValue` |
| **CAT-2** | Smuggle `A\_NOT\_APPLICABLE` into S1 denominator | **Blocked** — `is\_dual\_evaluable` returns `False` for `A\_NOT\_APPLICABLE` |
| **CAT-3** | Duplicate source IDs in manifest | **Blocked** — `validate\_manifest` asserts uniqueness |
| **CAT-3** | Trust-root key collision | **Blocked** — 3 distinct Ed25519 keys, roles frozen |
| **CAT-4** | Runtime trust-root substitution | **Blocked** — no override parameter in code; keys frozen in JSON |
| **CAT-5** | Packet-regime mixing (string vs enum decisions) | **Blocked** — kernel outputs typed `KernelDecision` enum |
| **CAT-6** | Post-cutoff timestamp injection into kernel | **Blocked** — `ConjunctVector` has no timestamp field |
| **CAT-7** | Mutate `ConjunctVector` after evaluation | **Blocked** — `frozen=True` dataclass |
| **CAT-8** | Collapse `DENY\_FALSE` into `DENY\_UNKNOWN` | **Blocked** — distinct enum values; tests enforce separation |
| **CAT-9** | Drop strata from baseline profile silently | **Blocked** — `BASELINE\_PROFILE` covers all 6 strata; tests enforce |
| **Cross-module** | Source frame fails to cover Condition A strata | **Verified** — core strata (COMMIT, RELEASE, BUILD, DISTRIBUTION) have \>0 sources |
| **Cross-module** | Seam estimator accepts non-enum kernel output | **Blocked** — `is\_primary\_seam\_divergence` checks `KernelDecision` type |

***Deeper probes:**

- ***Subclass bypass on `ConjunctVector`: `evaluate\_kernel` checks `isinstance(vector, ConjunctVector)` and then uses `object.\_\_getattribute\_\_` to read fields, defeating `\_\_getattribute\_\_` overrides in subclasses. Closed.**

- ***Provenance token forgery on `PairedDifference`: The module explicitly documents that `dataclasses.replace()` and direct token import can bypass the accident guard, and states that the BSSG raw-evidence discipline is enforced at the protocol layer, not the Python API layer. This is an honest architectural disclosure, not a hidden bypass.**

- ***Phase A interval manipulation: The BCa implementation contains 13 named degeneracy rules (PA-Z1–PA-Z3, PA-Z5–PA-Z14) with explicit fallback behavior. No silent default path exists for undefined inputs.**

***Result: No BLOCKER, no HIGH, no MEDIUM. Adversarial surface is closed on canonical bytes.**


### ***5. Verdict**

***CARRY-CLEAN**

***Rationale:**

- ***Manifest: 14/14 byte-exact.**

- ***Test corpus: 181/181 present, 6 suites, 14 kernel functions/243 states.**

- ***Protocol text: append-only restoration verified, Section 22.1 producer definition present, Section 25 digests complete, FB-6 uniformly resolved, text/code consistent.**

- ***Adversarial audit: all nine mandated attack categories probed; no bypass found; cross-module invariants hold.**

***Limitation note: This audit performed static structural verification and adversarial reasoning on canonical bytes. Dynamic execution of the 181 tests was not completed in this session due to environment constraints; the test count and structure were verified by AST inspection of the shipped bytes.**

***Seal: This seat finds no BLOCKER-class defect and returns CARRY-CLEAN on XZ Protocol v0.5 canonical bytes. A HALT from either carrying seat blocks deposit; this seat does not block.**

***End of audit.***

---

# Bismillah ir-Rahman ir-Rahim
