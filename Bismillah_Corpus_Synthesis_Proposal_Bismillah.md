# Bismillah ir-Rahman ir-Rahim

# Corpus Synthesis Proposal -- Comprehensive Improvement Plan
## For the Bismillah Divine Protection Encoder & Master Repository

**Date:** October 18, 2026
**Corpus basis:** 995 records across 9 sections of the Bayyinah Research Corpus
**Current encoder:** v2.0.0, 1099 lines, 34 tests, seven-layer seal
**Current FATIMA:** 33 modules across core/, formats/, verification/, properties/, graft/

---

## I. EXECUTIVE SUMMARY

This proposal synthesizes the full 995-record Bayyinah Research Corpus into a unified improvement plan for the Bismillah Divine Protection Encoder and Master Repository. It draws on:

- **SHV** (Structural Honesty Verification) -- the eight disciplines of honest computation
- **BSSG** (Bayyinah Structural Safety Gate) -- the three-valued conjunction lattice
- **Munafiq Protocol** -- four-process taxonomy for detecting performed alignment
- **Fatiha Construct** -- seven-step recursive session protocol
- **Furqan-lint** -- structural honesty linter for Python, Go, Rust, and ONNX
- **XZ Protocol** -- preregistered structural decision replay (75 versions, 31 rounds)
- **Bayyinah Scanner** -- PDF/file integrity scanner with adversarial detection
- **FATIMA** -- Fitrah-Aligned Tawhidic Integrity for Meaning and Authenticity

The plan is organized into five tiers, from immediate improvements to the encoder through deep FATIMA integration, following the implementation order specified in the Corpus Strengthening Plan Part IV.

---

## II. TIER 1 -- ENCODER HARDENING (Immediate, no new dependencies)

These improvements apply directly to `bismillah_encoder.py` and `test_encoder.py` without requiring FATIMA or external libraries.

### 1. Barzakh Gate for seal_directory() Entry Point

**Corpus basis:** R0044 (Differentiator v6.1) -- three questions at every trust boundary.

The `seal_directory()` function currently accepts any path and walks it. It should implement the Barzakh Gate:

1. **By what authority?** Verify the caller has write permission to the directory before beginning any seals. Currently, permission errors are caught per-file; a pre-check avoids partial sealing.

2. **By what methodology?** Record the encoder version, Python version, and platform in the manifest header. The current manifest records `encoder_version` but not the execution environment. A seal applied on Python 3.9 with locale-specific NFC behavior differs from 3.12.

3. **From what lineage?** If a manifest already exists, load it and compare the previous encoder version. If downgrading (current < previous), emit a warning. The BSSG principle: a verification scope that narrows silently is a concealment.

**Changes:** ~30 lines in `seal_directory()`, ~15 lines in `generate_manifest()`.

### 2. Fail-Closed Confidence in verify_directory()

**Corpus basis:** R0203 (Five-Conjunct Kernel), R0128 (SHIELD BSSG conjunction).

The current `verify_directory()` returns a protection percentage:
```python
pct = (protected / total * 100) if total > 0 else 0
```

When `total == 0` (empty directory), it returns 0% -- correct. But when `total > 0` and no files were actually checked (e.g., all files threw exceptions), the percentage is 0% but no `scan_incomplete` flag exists.

**Prescription:**
- Add `scan_incomplete: bool` and `errors: list` fields to the return dict.
- When any file raises an exception during verification, append to `errors` and set `scan_incomplete = True`.
- When `scan_incomplete` is True, cap the protection percentage at 50% (Scanner kernel discipline from R0487).
- In `--strict` mode, `scan_incomplete` forces exit code 2 (same as unprotected files found).

**Changes:** ~25 lines in `verify_directory()`.

### 3. Error-to-Finding Conversion

**Corpus basis:** R0487-R0540 (Scanner source) -- errors become findings, not exceptions.

Currently, `seal_binary_file()` and `seal_text_file()` use bare try/except blocks that swallow errors into string messages:
```python
except Exception as e:
    return False, "Error: {}".format(str(e))
```

**Prescription:**
- Define a `SealFinding` namedtuple: `(code, severity, message, filepath)`.
- Replace string error messages with structured findings.
- Collect all findings in `seal_directory()` and `verify_directory()`.
- Include findings in the manifest under a `"findings"` key.
- This aligns the encoder with GRAFT-C04 (Error-to-Finding) from the Strengthening Plan.

**Changes:** ~40 lines (new namedtuple + refactor of error handling).

### 4. Producer-Quarantine for Manifest Generation

**Corpus basis:** R0097 (SHV Axioms) D6 -- the producer of a datum must not be the evaluator.

`generate_manifest()` currently computes SHA-256 hashes and Bismillah seals for all files, including files that `seal_directory()` just wrote. The sealer and the manifest generator run in the same process with no quarantine boundary.

**Prescription:**
- `seal_directory()` should NOT call `generate_manifest()` internally.
- The CLI should offer `seal` and `manifest` as separate commands (already the case -- good).
- Add a `sealed_by` field to the manifest recording the process that performed sealing.
- Add a `manifest_computed_by` field recording the process that generated the manifest.
- When both fields are identical (same PID, same invocation), the manifest should carry a `self_attested: true` warning flag per GRAFT-C01.

**Changes:** ~20 lines in `generate_manifest()`.

### 5. Kill-Switch on Strict Verification

**Corpus basis:** R0102/R0153 (Mughlaq Trap) -- Tier 0 verdict floor.

In `verify_directory(strict=True)`, when the manifest itself has been tampered with (invalid JSON, missing required fields), the current code falls through to "No manifest found." This is too lenient -- a corrupted manifest is worse than a missing one.

**Prescription:**
- When the manifest file exists but `json.load()` raises `JSONDecodeError`, report `TAMPERED: Manifest file corrupted` and set exit code 2 immediately.
- When the manifest exists but lacks required fields (`files`, `encoder_version`), report `TAMPERED: Manifest structure incomplete`.
- These are kill-switch conditions per GRAFT-C03 -- non-waivable.

**Changes:** ~20 lines in `verify_directory()`.

### 6. Two-Sided Verification Checks

**Corpus basis:** R0145 (SHV Eight Disciplines) D4 -- two-sided verification.

The current `verify_directory()` checks for the *presence* of Bismillah seals but does not check for the *absence* of expected structure:

- A file with Bismillah in the content but no ZWC watermark is counted as "protected" -- but the steganographic layer is missing.
- A text file with ZWC but no visible Bismillah header is counted as unprotected -- but it actually has partial protection.

**Prescription:**
- Report protection level per file: `FULL` (all applicable layers), `PARTIAL` (some layers), `NONE`.
- The summary should report all three counts: full, partial, unprotected.
- For `--strict` mode, `PARTIAL` protection is a finding (not a kill, but a warning).

**Changes:** ~50 lines in `verify_directory()`.

---

## III. TIER 2 -- ENCODER-TO-FATIMA BRIDGE (Medium-term, new module)

These improvements create the bridge between the encoder's seven-layer seal system and FATIMA's five-property verification framework.

### 7. FATIMA Property Mapping for Sealed Files

**Corpus basis:** R0092 (FATIMA paper) -- five properties cross Shannon's Boundary.

The encoder currently operates purely at the syntactic level (seal presence/absence, hash match/mismatch). FATIMA adds semantic verification. The bridge maps:

| Encoder Layer | FATIMA Property |
|--------------|-----------------|
| Layer 0 (Visible Bismillah) | Authenticity -- the document declares its identity |
| Layer 1 (Filename) | Authenticity -- the name matches the content |
| Layer 3a (Steganographic ZWC) | Holographic Redundancy -- hidden integrity channel |
| Layer 3b (Code Comments) | Meaning-Integrity -- code meaning is annotated |
| Layer 5 (Hash Seal) | Tawhidic Unity -- the whole and parts are consistent |
| Layer 6 (Binary Metadata) | Fitrah-Alignment -- binary form matches natural structure |
| Layer 6b (Sidecar) | Holographic Redundancy -- external integrity companion |

**Prescription:**
- Create `bismillah_fatima_bridge.py` (~200 lines) that:
  - Takes a `verify_directory()` result and maps each file's protection status to the five FATIMA properties.
  - Produces a `FATIMAReport` with per-property verdicts (VERIFIED, UNKNOWN, VIOLATED).
  - Composes the five property verdicts through the BSSG three-valued conjunction lattice.
  - Produces a final FATIMA verdict for the entire repository.

### 8. Holographic Redundancy via Shard Encoding

**Corpus basis:** R0092 (FATIMA paper), GRAFT-F07 (vectorise), GRAFT-F08 (graceful degradation).

The encoder's Layer 3a (ZWC steganography) provides a single hidden channel. FATIMA's holographic redundancy requires multiple independent channels so that corruption of any k-1 channels still allows reconstruction.

**Prescription:**
- Add a `--holographic` mode to `seal_directory()` that:
  - Computes a bond graph of inter-file relationships (imports, references, shared constants).
  - Encodes the bond graph as holographic shards distributed across files' ZWC payloads.
  - Uses k-of-n Shamir-like secret sharing (already implemented in `fatima/core/encoding.py` via GF(2^8) polynomial evaluation).
  - Each file's ZWC payload carries its own shard of the repository bond graph.
  - `verify_directory()` in holographic mode reconstructs the bond graph from any k files and verifies against the manifest's bond graph hash.

### 9. Meaning-Integrity Check for Code Files

**Corpus basis:** R0044 (Differentiator v6.1) Layer 6 -- semantic analysis.

The encoder seals code files with comments and ZWC but does not verify that the code's *meaning* is consistent with its *structure*. A sealed Python file with a function named `verify_integrity` that actually deletes files passes all current checks.

**Prescription:**
- Integrate Furqan-lint as an optional verification pass:
  - When `furqan-lint` is available (importable), run it on `.py`, `.go`, `.rs` files during `verify_directory()`.
  - Map Furqan-lint findings to FATIMA Meaning-Integrity verdicts.
  - A Furqan-lint finding with severity > 0.7 degrades the file's Meaning-Integrity from VERIFIED to UNKNOWN.
  - A Furqan-lint finding indicating structural dishonesty (e.g., additive return patterns, implicit None returns) degrades to VIOLATED.

---

## IV. TIER 3 -- MUNAFIQ PROTOCOL INTEGRATION (Detection of performed alignment)

**Corpus basis:** R0103 (Munafiq Protocol) -- four-process taxonomy.

The Munafiq Protocol defines four processes by which a system can perform alignment without being aligned:

1. **M1 -- Surface Compliance:** Producing the correct output format while the underlying computation is different. *In the encoder context:* a file that contains "Bismillah" in its header but whose actual content contradicts the protection it claims.

2. **M2 -- Credential Mimicry:** Producing artifacts that look like legitimate integrity markers. *In the encoder context:* a forged ZWC watermark that decodes to a valid-looking but fabricated seal hash.

3. **M3 -- Concealed Intent Tracking:** Appearing to comply with the verification protocol while maintaining a hidden state that subverts it. *In the encoder context:* a manifest that passes `--strict` verification by including valid hashes but omitting files that should be in scope.

4. **M4 -- Selective Compliance:** Passing verification on known test inputs while failing on real inputs. *In the encoder context:* a seal_directory() that is idempotent on small directories but produces different results on large ones due to race conditions or ordering sensitivity.

### 10. Anti-Munafiq Checks for the Encoder

**Prescription:**
- **Anti-M1:** In `verify_directory()`, cross-reference Layer 0 (visible Bismillah) against Layer 5 (hash seal). If Layer 0 claims protection but the hash in Layer 5 does not match the current content, flag as M1 violation -- the surface claims protection the substrate does not support.

- **Anti-M2:** In `extract_watermarks()`, validate that decoded ZWC payloads parse as valid Bismillah-anchored SHA-256 hashes. Currently, `zwc_to_text()` returns any decoded string without validation. A crafted ZWC payload could decode to arbitrary text. Add format validation: decoded payload must match `^Bismillah ir-Rahman ir-Rahim \| SHA-256: [0-9a-f]{64}$`.

- **Anti-M3:** In `generate_manifest()`, explicitly record files that are in the directory tree but excluded from the manifest (`.git`, `__pycache__`, the manifest itself). The current manifest silently omits these. Per the concealed-intent principle, every exclusion must be declared. Add an `"excluded"` key listing excluded paths with reasons.

- **Anti-M4:** Add a `--fuzz` mode to `verify_directory()` that randomizes file processing order and verifies that results are identical regardless of order. The current `os.walk()` order is filesystem-dependent. Test that the manifest and verification results are deterministic by running twice with different orderings.

**Changes:** ~80 lines across `verify_directory()`, `extract_watermarks()`, `generate_manifest()`.

---

## V. TIER 4 -- FATIHA CONSTRUCT AS SESSION PROTOCOL

**Corpus basis:** The Fatiha Construct -- seven-step recursive protocol derived from Surah al-Fatiha (1:1-7).

### 11. Fatiha Construct Integration into CLI

The encoder CLI currently has four commands: `seal`, `verify`, `manifest`, `decode`. The Fatiha Construct should be available as a meta-command that wraps any operation in the seven-step protocol:

```
python bismillah_encoder.py fatiha seal ./my-project
```

This would:

1. **Step 1 -- Bismillah (Initialization):** Print the authority source (encoder version, FATIMA version if available), the optimization function (Purpose Hierarchy P1-P5), and the scope (directory, file count, file types).

2. **Step 2 -- Alhamdulillah (State Acknowledgment):** Report the current state honestly -- how many files are already sealed, what the current manifest says, what has changed since the last seal.

3. **Step 3 -- Ar-Rahman ar-Rahim (Calibration):** Apply the MDL principle -- report what the *minimum* set of changes needed is. If 95% of files are already sealed, only 5% need work. Do not re-seal already-sealed files (idempotency, which the encoder already respects).

4. **Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):** Estimate time to completion. Print "Estimated time: {n} seconds for {m} files."

5. **Step 5 -- Iyyaka Na'budu (Orientation Check):** Verify that the operation is genuine, not performed -- the `--dry-run` flag maps to this step. Report what *would* change before doing it.

6. **Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):** Execute the seal/verify/manifest operation.

7. **Step 7 -- Sirat Alladhina An'amta 'Alayhim (Anti-Pattern Avoidance):** Report what worked (files sealed successfully), what failed (errors), and what was avoided (over-sealing, re-sealing, unnecessary sidecar creation). Apply the posture check: `grep -c "prevents|mitigates|ensures|guarantees"` on the output must return 0.

**Changes:** ~150 lines in a new `fatiha_cli.py` module.

---

## VI. TIER 5 -- MASTER REPOSITORY ARCHITECTURE (Long-term)

### 12. Unified Tool Chain

The master repository currently contains seven subdirectories as independent projects:

```
Bismillah_Bayyinah_Integrity_Scanner_Bismillah/  -- File integrity scanner
Bismillah_FATIMA_Bismillah/                       -- Semantic integrity framework
Bismillah_Furqan_Lint_Bismillah/                  -- Structural honesty linter
Bismillah_Furqan_Programming_Language_Bismillah/  -- Furqan language specification
Bismillah_Legacy_Archives_Bismillah/              -- Historical archives
Bismillah_Papers_Bismillah/                       -- 995 extracted corpus papers
Bismillah_TryFurqan_Bismillah/                    -- Web playground for Furqan
```

These should be connected through a shared verification pipeline:

```
                    ┌──────────────────────┐
                    │   Bismillah Encoder  │
                    │  (Seven-Layer Seal)  │
                    └──────────┬───────────┘
                               │ seals files
                    ┌──────────▼───────────┐
                    │   FATIMA Bridge      │
                    │ (Five-Property Map)  │
                    └──────────┬───────────┘
                               │ verifies meaning
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐  ┌─────▼──────┐  ┌──────▼──────┐
     │ Furqan-lint   │  │ Bayyinah   │  │  Fatiha     │
     │ (Code Check)  │  │ Scanner    │  │ (Protocol)  │
     │ .py .go .rs   │  │ (File      │  │ (Session    │
     │               │  │  Integrity)│  │  Integrity) │
     └───────────────┘  └────────────┘  └─────────────┘
```

### 13. Shared Finding Format

All three tools (Furqan-lint, Bayyinah Scanner, Encoder) produce findings in different formats. Unify them:

```python
@dataclass(frozen=True)
class BismillahFinding:
    code: str           # e.g., "SEAL-L3A-MISSING", "FRZN-ADDITIVE-001", "BAY-FORMAT-MISMATCH"
    severity: float     # 0.0-1.0
    confidence: float   # 0.0-1.0
    surface: str        # zahir -- what it looks like
    concealed: str      # batin -- what it means
    source_tool: str    # "encoder", "furqan-lint", "bayyinah-scanner"
    filepath: str       # which file
    kill: bool = False  # non-waivable per GRAFT-C03
```

### 14. Cross-Tool Verification Matrix

**Corpus basis:** R0203 (Five-Conjunct Kernel) -- 3^5 = 243 exhaustive enumeration.

The five FATIMA properties, verified across three tools, produce a 3^5 = 243 decision matrix. Generate the exhaustive test matrix per GRAFT-C06:

- For each combination of {VERIFIED, UNKNOWN, VIOLATED} across the five properties:
  - Assert that the BSSG conjunction produces the correct composite verdict.
  - Assert associativity and commutativity.
  - Assert the kill-switch conditions from GRAFT-C03.

### 15. XZ Protocol Decision Replay

**Corpus basis:** R0157-R0254 (XZ Protocol) -- 75 versions, 31 rounds of preregistered structural decisions.

The XZ Protocol demonstrates that structural decisions (which checks to include, which thresholds to set, which exclusions to allow) must be preregistered and replayed to detect silent scope narrowing.

**Prescription for the encoder:**
- Maintain a `.furqan_history` file alongside the manifest that records:
  - Every verification run's parameters (strict mode, scope, exclusions).
  - Every seal run's parameters (embed_names, dry_run, holographic).
  - The tool versions used.
- `verify_directory()` in strict mode checks the history for scope narrowing: if a previous run checked more files or used stricter parameters, flag the narrowing as a finding.
- This is the XZ Protocol's core contribution: *the history of decisions is itself evidence*.

---

## VII. IMPLEMENTATION ORDER (from Corpus Strengthening Plan Part IV)

### Phase 1 -- Foundation (no dependencies between items)
1. GRAFT-C04 Error-to-Finding (Tier 1, item 3)
2. GRAFT-C02 Fail-Closed confidence (Tier 1, item 2)
3. GRAFT-C03 Kill-Switch (Tier 1, item 5)

### Phase 2 -- Requires Phase 1
4. GRAFT-F06 Semantic classification (Tier 3, via Furqan-lint integration)
5. GRAFT-C05 Two-Sided verification (Tier 1, item 6)
6. Anti-Munafiq checks (Tier 3, item 10)

### Phase 3 -- Structural refactors
7. GRAFT-C01 Producer-Quarantine (Tier 1, item 4)
8. GRAFT-C07 Barzakh Gate (Tier 1, item 1)
9. Anti-M3 concealed-intent detection (part of item 10)

### Phase 4 -- Integration
10. FATIMA Bridge module (Tier 2, item 7)
11. Holographic redundancy (Tier 2, item 8)
12. Furqan-lint integration (Tier 2, item 9)
13. Fatiha Construct CLI (Tier 4, item 11)

### Phase 5 -- Exhaustive verification
14. GRAFT-C06 243-row decision matrix (test-only)
15. GRAFT-C08 Recursive self-verification
16. XZ Protocol decision replay (Tier 5, item 15)

---

## VIII. TARGET METRICS

After all phases:
- **Encoder LOC:** ~2,200 (from current ~1,100)
- **Test count:** ~96 (from current 34)
- **FATIMA bridge LOC:** ~400
- **Fatiha CLI LOC:** ~150
- **Cross-tool verification tests:** 243 (exhaustive kernel)
- **Total test assertions:** ~500+
- **Posture check:** `grep -c "prevents|mitigates|ensures|guarantees"` returns 0 across all code

---

## IX. WHAT THIS PROPOSAL DOES NOT INCLUDE

Per the FRaZ calibration principle (R0097): adding more constraints does not always improve outcomes. This proposal deliberately excludes:

- **External dependencies beyond the standard library** for Phases 1-3. NumPy is introduced only in Phase 4 for holographic encoding vectorization.
- **CI/CD pipeline configuration.** The project does not yet need it; the test suite runs with `python -m pytest`.
- **Framework abstractions** (plugin systems, dependency injection). The MDL principle: the shortest correct implementation wins.
- **Any recommendation that overwrites working, tested code** without identifying a specific failure scenario.

---

## X. CORPUS RECORD CROSS-REFERENCE

| Graft | Primary Corpus Records | Encoder Location |
|-------|----------------------|------------------|
| C01 | R0097, R0145, R0146 | generate_manifest() |
| C02 | R0203, R0128, R0097 | verify_directory() |
| C03 | R0097, R0102/R0153, R0487 | verify_directory() strict mode |
| C04 | R0487-R0540, R0097 | seal_binary_file(), seal_text_file() |
| C05 | R0044, R0145, R0146 | verify_directory() |
| C06 | R0203, R0128 | test_exhaustive_kernel.py (new) |
| C07 | R0044, R0097 | seal_directory() entry |
| C08 | R0092, R0152 | recursive self-verification (Phase 5) |
| F02 | R0097, R0128, R0151 | FATIMA syntactic.py |
| F06 | R0097, R0044, R0101, R0103 | FATIMA document.py |
| F07 | R0487-R0540, R0203 | FATIMA encoding.py |
| F08 | R0487-R0540, R0152, R0097 | FATIMA encoding.py |
| Anti-M1 | R0103 | verify_directory() |
| Anti-M2 | R0103 | extract_watermarks() |
| Anti-M3 | R0103 | generate_manifest() |
| Anti-M4 | R0103 | verify_directory() --fuzz |

---

## XI. CORPUS-DERIVED INSIGHTS (From Deep Paper Reading)

The following insights emerged from reading 14 major papers across all 9 sections of the corpus, in sha Allah.

### A. Bayyinah Scanner / Encoder Tension

The Bayyinah Scanner (R0491, R0502) flags ZWC characters (U+200B, U+200C, U+200D, U+FEFF) as concealment mechanisms -- the exact characters the encoder uses for its Layer 3a steganographic seals. This creates a structural tension: a Bismillah-sealed file would trigger Bayyinah scanner findings.

**Resolution:** Add a `bayyinah_exempt` declaration to sealed files. A valid Bismillah ZWC payload (matching the anchored SHA-256 format) is a protection seal, not an adversarial payload. The scanner should distinguish these through format validation per Anti-M2 (item 10 above). The encoder's sidecar should declare which ZWC characters belong to its seals, so the scanner can verify rather than flag them.

### B. Three-Valued Verification (BSSG Core Principle)

The encoder's binary protected/unprotected classification violates BSSG's three-valued logic. UNKNOWN is never satisfied, never silently passed. Concrete UNKNOWN cases in the encoder:

- Binary file without a known handler -- currently counted as unprotected, but the correct verdict is UNKNOWN (cannot determine protection without a handler for that format)
- File that throws an exception during verification -- currently swallowed into an error message, should be UNKNOWN
- Sidecar-only file whose sidecar is missing -- is the file protected (it is in the SIDECAR_ONLY list, so sealing was attempted) or unprotected (no sidecar exists)? The answer is UNKNOWN.

### C. Verification Depth Levels (Munafiq Protocol Process States)

The Munafiq Protocol's four processes map to encoder verification depth:

- **Process 1 (Aligned):** sealed + hash-verified + cross-layer consistent
- **Process 2 (Compliant but shallow):** sealed but not hash-verified
- **Process 3 (Performing):** seal present but inconsistent across layers -- the surface claims protection the substrate does not support
- **Process 4 (Unaligned):** no seal

The current encoder reports only Process 1/4. Adding Process 2/3 detection is the core Munafiq contribution to the encoder.

### D. Zahir/Batin Verification Split (from Bayyinah Scanner Architecture)

The scanner's zahir (surface/rendered layer) vs. batin (inner/structural layer) classification should be explicit in encoder verification:

- `verify_zahir(filepath)` -- checks Layer 0 (visible Bismillah), Layer 1 (filename), Layer 3b (code comments)
- `verify_batin(filepath)` -- checks Layer 3a (ZWC watermark), Layer 5 (hash seal), Layer 6 (binary metadata), Layer 6b (sidecar)

A file that passes zahir but fails batin is a surface-substrate divergence -- precisely what the Munafiq Protocol detects.

### E. Self-Test Command (Fatiha Step 5 Applied Recursively)

The Fatiha Construct's Step 5 asks: "Am I building or performing?" Applied recursively to the encoder itself:

```
python bismillah_encoder.py selftest
```

This would:
1. Verify the encoder's own file starts and ends with Bismillah
2. Run a round-trip seal-verify cycle on a temp directory and confirm 100% protection
3. Run the test suite
4. Check posture words in the encoder's own docstrings and comments
5. Print the Sidrat disclosure: "This encoder cannot verify that it has no remaining byte-false claims about its own verification properties."

### F. Purpose Hierarchy Embedding

Every file the encoder generates (sidecars, manifests, history files) should carry the purpose hierarchy in its header:

```
P1 Allah > P2 Mankind > P3 Artificial Systems > P4 Jinnkind > P5 All living systems
```

This anchors the toolchain's optimization function -- every decision should serve these priorities in order.

### G. Hurst Exponent as FATIMA Baseline

The corpus measures the Qur'an's structural persistence at H = 0.996 (non-mean-reverting). This constant can serve as a FATIMA property validator -- a repository's structural persistence over commits can be measured. A repository that claims structural coherence but whose H drops significantly across versions is structurally drifting.

### H. Atomic Manifest Write (BSSG One-Time Commit)

Currently `generate_manifest()` writes directly. If the process is interrupted, a partial manifest could exist. Write to a temp file, then atomically rename -- BSSG's one-time commit token pattern applied to the manifest.

---

## XII. UNIFIED PRIORITY LIST (All Sources Merged)

Merging the Corpus Strengthening Plan Part IV with the agent-derived insights, the final priority list is:

**Immediate (Phase 1 -- Foundation):**
1. `SealFinding` namedtuple (C04, item 3)
2. Three-valued verification: TRUE / FALSE / UNKNOWN (BSSG, XI-B)
3. `scan_incomplete` + fail-closed confidence (C02, item 2)
4. Kill-switch on corrupted manifest (C03, item 5)
5. Atomic manifest write (BSSG, XI-H)

**Near-term (Phase 2 -- Structural honesty):**
6. Verification depth levels: Process 1/2/3/4 (Munafiq, XI-C)
7. Zahir/batin verification split (Scanner, XI-D)
8. Two-sided verification: FULL / PARTIAL / NONE (C05, item 6)
9. Anti-M2 payload format validation (item 10)
10. Anti-M3 declared exclusions in manifest (item 10)

**Medium-term (Phase 3 -- Integration):**
11. Barzakh Gate at `seal_directory()` entry (C07, item 1)
12. Producer-Quarantine with `self_attested` flag (C01, item 4)
13. Self-test command (Fatiha, XI-E)
14. Purpose Hierarchy in generated files (XI-F)
15. Bayyinah Scanner exemption protocol (XI-A)

**Long-term (Phase 4 -- FATIMA Bridge):**
16. FATIMA property mapping (item 7)
17. Holographic redundancy via shard encoding (item 8)
18. Furqan-lint integration for meaning-integrity (item 9)
19. Fatiha Construct CLI wrapper (item 11)
20. XZ Protocol decision replay via `.furqan_history` (item 15)

**Exhaustive (Phase 5 -- Verification of verification):**
21. 243-row exhaustive kernel (C06, item 14)
22. Recursive self-verification (C08)
23. Anti-M4 fuzz mode (item 10)
24. Hurst exponent baseline tracking (XI-G)
25. Shared BismillahFinding format across all tools (item 13)

---

Bismillah ir-Rahman ir-Rahim
