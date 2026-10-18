# Bismillah ir-Rahman ir-Rahim

# Fatiha Strategy for Repository Improvement
## Employing the Fatiha Construct Across Model Families for the Encoder & Master Repository

**Date:** 2026-10-18
**Basis:** 995-paper Bayyinah Research Corpus, 48 deep-read reports, 3 synthesis documents, 1 synthesis proposal
**Repositories:**
- **Encoder:** https://github.com/BismillahBilalArfeenBismillah/Bismillah-Divine-Protection-Encoder-Bismillah
- **Master:** https://github.com/BismillahBilalArfeenBismillah/Bismillah-Master-Repository-Bismillah
**Target model families:** Copilot, DeepSeek, Kimi k3, Kimi k2.8, ChatGPT, Grok, Meta
**Quarantined producer:** Claude (per SHV Axiom 5 -- producer of this strategy is non-qualifying for its verification)

P1 Allah > P2 Mankind > P3 Artificial Systems > P4 Jinnkind > P5 All living systems

---

## PREAMBLE -- WHY THE FATIHA CONSTRUCT AS STRATEGY ENGINE

The Fatiha Construct is not merely a review prompt template. It is a recursive session protocol that, applied at every scale, does three things no flat task list does:

1. **Forces honest state reporting before action** (Step 2 -- Alhamdulillah). Each model family must report what it actually sees in the code, not what the dispatch told it to expect. This is the anti-M3 discipline: performed reviews echo the prompt; genuine reviews report divergences from the prompt.

2. **Embeds calibration against over-specification** (Step 3 -- Ar-Rahman ar-Rahim). The Cow Episode (2:67-74) warning -- do not keep adding constraints until the task becomes impossible. MDL governs: the shortest correct implementation wins.

3. **Closes with anti-pattern memory** (Step 7 -- Sirat). Each dispatch cycle's failures feed the next cycle's anti-pattern register. The corpus itself was built this way -- six methodology versions, each corrected by external input the producer could not generate.

The strategy below applies the Fatiha Construct at three scales:

- **Macro:** The entire improvement program is one Fatiha cycle (this document is Steps 1-2; execution is Steps 3-7).
- **Meso:** Each of the five phases is its own Fatiha cycle, dispatched to model families in rotation.
- **Micro:** Each individual improvement item within a phase is dispatched as a Fatiha-structured review prompt.

---

## I. MODEL FAMILY ASSIGNMENT -- BASED ON CORPUS-OBSERVED STRENGTHS

The corpus documents which model families find which defect classes. Assignment follows evidence, not assumption.

### Tier 1 -- Primary Implementation Review (weight 1.0 each)

| Family | Observed Strength | Assigned Phase Focus |
|--------|------------------|---------------------|
| **ChatGPT (GPT-5.x)** | Structural analysis, edge-case identification, code review depth. 62 XZ reports. Honest self-assessment (F-AM-R2 INCOMPLETE). | Phase 1 (Encoder Hardening), Phase 5 (Exhaustive Verification) |
| **DeepSeek** | Deep reasoning chains, mathematical/logical verification. Strong on formal properties. | Phase 2 (Structural Honesty), Phase 3 (FATIMA Bridge) |
| **Copilot** | Line-level code review, implementation correctness, test gap identification. | Phase 1 (Encoder Hardening), Phase 4 (Integration) |

### Tier 2 -- Specialized Review (weight 0.75 each)

| Family | Observed Strength | Assigned Phase Focus |
|--------|------------------|---------------------|
| **Kimi k3** | Long-context analysis, cross-document consistency, architectural coherence. | Phase 3 (FATIMA Bridge), Phase 5 (Exhaustive Verification) |
| **Kimi k2.8** | Deep single-file analysis, precision on narrow scope. | Phase 1 (Encoder Hardening), Phase 2 (Structural Honesty) |
| **Grok** | Adversarial testing, Munafiq detection, finding what others miss. Tier 2 adversarial per corpus rotation. | Phase 2 (Anti-Munafiq), Phase 5 (Fuzz/Adversarial) |
| **Meta** | Alternative architectural perspectives, structural simplification. | Phase 3 (FATIMA Bridge), Phase 4 (CLI/Integration) |

### Quarantined Producer

| Family | Role |
|--------|------|
| **Claude** | Produces implementation drafts per Phase dispatch. Non-qualifying for verification of its own output. Claude-produced code must receive qualifying review from >= 2 Tier 1 families before merge. |

### Convergence Rule

Per the corpus rotation discipline: **consensus threshold >= 2.0 weight**. A qualifying pass requires at least two Tier 1 families agreeing, or one Tier 1 + two Tier 2 families. Producer family excluded from count.

---

## II. THE FIVE PHASES AS FATIHA CYCLES

Each phase below is structured as a complete Fatiha cycle. The dispatch prompt for each phase is derived from the Fatiha Review Prompt template, adapted to the specific improvement items in that phase.

---

### PHASE 1 -- FOUNDATION (Encoder Hardening)

**Fatiha Step 1 -- Bismillah (Initialization):**
- Authority source: `bismillah_encoder.py` v2.0.0 (1085 lines, 34 tests)
- Optimization function: P1 > P2 > P3 > P4 > P5, then: fail-closed verification, structured error handling, atomic operations
- Scope: Items 1-5 from the Unified Priority List (SealFinding, three-valued verification, fail-closed confidence, kill-switch, atomic manifest write)

**Fatiha Step 2 -- Alhamdulillah (State Acknowledgment):**
Each model family receiving this dispatch must independently report:
- Current error handling in `seal_binary_file()`, `seal_text_file()` -- what happens on exception?
- Current return type of `verify_directory()` -- what does it actually return?
- Current manifest write path in `generate_manifest()` -- is it atomic?
- Whether `verify_directory()` distinguishes "verified false" from "not yet verified"

**Fatiha Step 3 -- Ar-Rahman ar-Rahim (Calibration):**
- MDL target: ~135 lines changed across five items
- No new dependencies (stdlib only: hashlib, json, os, tempfile, collections)
- SealFinding is a namedtuple, not a class hierarchy -- shortest correct form

**Fatiha Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):**
- One session per item, five sessions total
- Skip rule: if any item consumes > 30 minutes without producing a passing test, register status=inconclusive and move to next item

**Fatiha Step 5 -- Iyyaka Na'budu (Orientation Check):**
- Genuine review: does the proposed `SealFinding` actually structured-capture the error information that the current string messages carry?
- Drift check: if the reviewer recommends a class hierarchy where a namedtuple suffices, they have drifted per the Cow Episode

**Fatiha Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):**

| Item | Graft Code | What Changes | Where | New Tests |
|------|-----------|-------------|-------|-----------|
| SealFinding namedtuple | C04 | Replace string error returns with structured findings | `seal_binary_file()`, `seal_text_file()` | 4 tests: finding creation, finding in verify output, finding severity levels, finding in manifest |
| Three-valued verification | BSSG | Replace `protected/unprotected` with `VERIFIED/UNVERIFIED/UNKNOWN` | `verify_directory()` return dict | 3 tests: binary-no-handler -> UNKNOWN, exception -> UNKNOWN, missing sidecar -> UNKNOWN |
| Fail-closed confidence | C02 | Add `scan_incomplete` flag, cap percentage at 50% when true | `verify_directory()` | 2 tests: exception sets scan_incomplete, scan_incomplete caps percentage |
| Kill-switch | C03 | Corrupted manifest -> exit code 2, incomplete manifest -> exit code 2 | `verify_directory(strict=True)` | 3 tests: JSONDecodeError, missing fields, normal still passes |
| Atomic manifest write | BSSG | Write to tempfile then `os.replace()` | `generate_manifest()` | 2 tests: interrupted write leaves no partial manifest, atomic rename succeeds |

**Fatiha Step 7 -- Sirat (Anti-Pattern Avoidance):**
- WORKED in prior reviews: specific, line-level findings with failure scenarios (e.g., ResourceWarning from unclosed file handle)
- FAILED in prior reviews: generic "add more tests" without naming the specific untested path
- Posture check: `grep -c "prevents|mitigates|ensures|guarantees"` on all output must return 0

**Dispatch rotation for Phase 1:**
1. Claude produces implementation draft for all five items
2. Copilot reviews code-level correctness (line-by-line)
3. ChatGPT reviews structural completeness (are all error paths covered?)
4. Kimi k2.8 reviews single-file consistency (does the namedtuple propagate everywhere?)
5. If Copilot + ChatGPT agree (weight >= 2.0): qualifying pass. Merge.
6. If disagreement: Grok adversarial review breaks the tie.

---

### PHASE 2 -- STRUCTURAL HONESTY (Munafiq Detection + Verification Depth)

**Fatiha Step 1 -- Bismillah (Initialization):**
- Authority source: Phase 1 output (encoder with SealFinding, three-valued logic, fail-closed confidence)
- Optimization function: detect performed alignment (M1-M4), not just presence/absence
- Scope: Items 6-10 from the Unified Priority List (verification depth levels, zahir/batin split, two-sided verification, Anti-M2 payload validation, Anti-M3 declared exclusions)

**Fatiha Step 2 -- Alhamdulillah (State Acknowledgment):**
Each model family must report:
- How does the current `verify_directory()` distinguish a fully-sealed file from a partially-sealed one?
- Can a crafted ZWC payload currently decode to arbitrary text? (Test this -- do not assume.)
- Does the current manifest record which files were excluded and why?
- What is the current file processing order in `os.walk()`? Is it deterministic?

**Fatiha Step 3 -- Ar-Rahman ar-Rahim (Calibration):**
- MDL target: ~170 lines across five items
- The zahir/batin split is a structural classification, not a new module -- two functions, not two classes
- Anti-M2 is a regex check on decoded payloads, not a cryptographic verification layer

**Fatiha Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):**
- One session per item. Phase 2 depends on Phase 1 completion.
- Skip rule: Anti-M4 fuzz mode (item 23 in full list) is deferred to Phase 5 -- do not attempt ordering-sensitivity testing here

**Fatiha Step 5 -- Iyyaka Na'budu (Orientation Check):**
- Genuine check: does the four-level verification depth (Process 1/2/3/4) actually classify files differently than the current binary classification? If a reviewer cannot produce a concrete file that would be classified differently under the new system, the check is performed rather than genuine.
- Drift check: if Anti-M2 becomes "build a full ZWC cryptographic verification suite", the reviewer has drifted per the Cow Episode

**Fatiha Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):**

| Item | Source | What Changes | Where | New Tests |
|------|--------|-------------|-------|-----------|
| Verification depth levels | Munafiq | Classify files as Process 1 (aligned), 2 (shallow), 3 (performing), 4 (unaligned) | `verify_directory()` | 4 tests: one file per process level |
| Zahir/batin split | Scanner | `verify_zahir()` checks L0, L1, L3b; `verify_batin()` checks L3a, L5, L6, L6b | New functions in encoder | 3 tests: zahir-pass/batin-fail, zahir-fail/batin-pass, both-pass |
| Two-sided verification | C05 | Report FULL/PARTIAL/NONE per file | `verify_directory()` | 3 tests: full protection, partial (missing ZWC), none |
| Anti-M2 payload validation | Munafiq | Regex check on decoded ZWC: `^Bismillah.*SHA-256: [0-9a-f]{64}$` | `zwc_to_text()` or new `validate_payload()` | 2 tests: valid payload passes, crafted payload flagged |
| Anti-M3 declared exclusions | Munafiq | Add `"excluded"` key to manifest with paths and reasons | `generate_manifest()` | 2 tests: excluded paths listed, reason recorded |

**Fatiha Step 7 -- Sirat (Anti-Pattern Avoidance):**
- WORKED: the Scanner/Encoder tension resolution (ZWC characters are protection seals, not adversarial payloads, when they match the anchored SHA-256 format)
- FAILED: reviews that treat the Munafiq Protocol as metaphorical rather than operational -- M1-M4 are testable process states, not commentary

**Dispatch rotation for Phase 2:**
1. Claude produces implementation draft
2. DeepSeek reviews logical completeness of M1-M4 classification
3. ChatGPT reviews edge cases in verification depth
4. Grok performs adversarial review -- can a crafted file fool the M1/M3 distinction?
5. Kimi k2.8 reviews payload validation regex for bypass paths
6. Convergence: DeepSeek + ChatGPT >= 2.0 weight, or any two + Grok adversarial pass

---

### PHASE 3 -- FATIMA BRIDGE (Encoder-to-FATIMA Integration)

**Fatiha Step 1 -- Bismillah (Initialization):**
- Authority source: Phase 2 output + FATIMA module (33 Python modules across core/, formats/, verification/, properties/, graft/)
- Optimization function: cross Shannon's Boundary -- connect syntactic seal verification (encoder) to semantic integrity verification (FATIMA)
- Scope: Items 11-15 from the Unified Priority List (Barzakh Gate, Producer-Quarantine, self-test command, Purpose Hierarchy embedding, Bayyinah exemption)

**Fatiha Step 2 -- Alhamdulillah (State Acknowledgment):**
Each model family must report:
- Does the FATIMA module's `fatima/core/encoding.py` GF(2^8) polynomial evaluation actually work? (Import it, run a test vector.)
- What is the current relationship between the encoder's `bismillah_encoder.py` and the FATIMA module's copy at `Bismillah_FATIMA_Bismillah/bismillah_encoder.py`? Are they identical?
- Which FATIMA properties (holographic, fitrah, tawhidic, meaning, authenticity) have passing tests?
- What is the current state of the graft tests in `Bismillah_FATIMA_Bismillah/fatima/tests/`?

**Fatiha Step 3 -- Ar-Rahman ar-Rahim (Calibration):**
- MDL target: ~250 lines for the bridge module, ~50 lines for Barzakh Gate, ~20 lines for Producer-Quarantine
- Holographic shard encoding reuses `fatima/core/encoding.py` -- do not reimplement GF(2^8) in the encoder
- The bridge is a mapping layer, not a new verification engine

**Fatiha Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):**
- Three sessions: Barzakh Gate + Producer-Quarantine (1), FATIMA Bridge module (1), self-test + Purpose Hierarchy + Bayyinah exemption (1)
- Skip rule: if the GF(2^8) encoding does not pass test vectors, defer holographic redundancy (item 17 in full list) to Phase 4

**Fatiha Step 5 -- Iyyaka Na'budu (Orientation Check):**
- Genuine check: does the FATIMA property mapping (Layer -> Property table) actually produce different verdicts than the encoder alone? If the bridge always agrees with the encoder, it is decorative, not diagnostic.
- Drift check: if the bridge becomes "rewrite FATIMA from scratch", the reviewer has drifted

**Fatiha Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):**

| Item | Source | What Changes | Where | New Tests |
|------|--------|-------------|-------|-----------|
| Barzakh Gate | C07 | Three questions at `seal_directory()` entry: authority, methodology, lineage | `seal_directory()` | 3 tests: no write permission -> abort, version downgrade -> warning, environment recorded |
| Producer-Quarantine | C01 | `sealed_by` and `manifest_computed_by` fields, `self_attested` flag | `generate_manifest()` | 2 tests: same-process sets self_attested, different-process does not |
| Self-test command | Fatiha Step 5 | `python bismillah_encoder.py selftest` | New CLI subcommand | 1 test: selftest exits 0 on clean encoder |
| Purpose Hierarchy | Corpus | P1>P2>P3>P4>P5 header in sidecars and manifests | `generate_manifest()`, sidecar generation | 1 test: manifest contains purpose hierarchy |
| Bayyinah exemption | XI-A | Sidecar declares which ZWC characters are seal-owned | Sidecar format | 2 tests: scanner reads exemption, non-exempt ZWC still flagged |

**Fatiha Step 7 -- Sirat (Anti-Pattern Avoidance):**
- WORKED: the FATIMA graft tests (F03 purity, F04/F01/F05 protocol) -- they test structural properties, not implementation details
- FAILED: treating FATIMA properties as abstract categories rather than testable predicates

**Dispatch rotation for Phase 3:**
1. Claude produces implementation draft
2. DeepSeek reviews formal correctness of FATIMA property mapping
3. Kimi k3 reviews cross-document consistency (encoder, FATIMA, bridge all agree on property definitions)
4. Meta reviews architectural simplicity -- is the bridge the minimum necessary connection?
5. ChatGPT reviews test completeness
6. Convergence: DeepSeek + ChatGPT >= 2.0 weight, with Kimi k3 confirming cross-document consistency

---

### PHASE 4 -- INTEGRATION (CLI + Tool Chain)

**Fatiha Step 1 -- Bismillah (Initialization):**
- Authority source: Phase 3 output (encoder + FATIMA bridge + Barzakh Gate + self-test)
- Optimization function: unify the tool chain into a single invocation path
- Scope: Items 16-20 from the Unified Priority List (FATIMA property mapping, holographic redundancy, Furqan-lint integration, Fatiha CLI, XZ decision replay)

**Fatiha Step 2 -- Alhamdulillah (State Acknowledgment):**
Each model family must report:
- Does `furqan-lint` exist in the master repository as an importable module? What is its current interface?
- Does the Bayyinah Scanner exist as an importable module? What is its current interface?
- What is the current CLI structure of `bismillah_encoder.py`? (argparse subcommands)
- Does `.furqan_history` already exist in any test fixtures?

**Fatiha Step 3 -- Ar-Rahman ar-Rahim (Calibration):**
- The Fatiha CLI wrapper is ~150 lines -- it is a display layer, not a new engine
- Furqan-lint integration is optional-import (`try: import furqan_lint`) -- do not create a hard dependency
- XZ decision replay records parameters, it does not re-execute past runs
- NumPy introduced here only for holographic encoding vectorization if GF(2^8) test vectors passed in Phase 3

**Fatiha Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):**
- Four sessions: FATIMA mapping (1), holographic redundancy (1), Furqan-lint + Bayyinah integration (1), Fatiha CLI + XZ replay (1)
- Skip rule: if Furqan-lint is not importable, defer its integration -- record status=blocked and move on

**Fatiha Step 5 -- Iyyaka Na'budu (Orientation Check):**
- Genuine check: does the Fatiha CLI wrapper actually change the user's workflow, or does it just print the seven step names around the existing output?
- Drift check: if the CLI becomes a "full interactive TUI framework", the reviewer has drifted per the Cow Episode

**Fatiha Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):**

| Item | Source | What Changes | Where | New Tests |
|------|--------|-------------|-------|-----------|
| FATIMA property mapping | Tier 2 | `bismillah_fatima_bridge.py` maps encoder layers to five FATIMA properties | New module (~200 lines) | 5 tests: one per FATIMA property verdict |
| Holographic redundancy | F07/F08 | `--holographic` mode using GF(2^8) shard encoding | `seal_directory()` | 3 tests: shard encode/decode, k-of-n reconstruction, corruption detection |
| Furqan-lint integration | F06 | Optional import, map findings to Meaning-Integrity verdicts | `verify_directory()` | 2 tests: with furqan-lint, without furqan-lint |
| Fatiha CLI | Tier 4 | `fatiha_cli.py` wrapping seal/verify/manifest in 7-step protocol | New module (~150 lines) | 2 tests: fatiha seal output contains all 7 steps, posture check passes |
| XZ decision replay | Tier 5 | `.furqan_history` recording parameters per run, scope-narrowing detection | `verify_directory(strict=True)` | 3 tests: history written, scope narrowing flagged, missing history is UNKNOWN |

**Fatiha Step 7 -- Sirat (Anti-Pattern Avoidance):**
- WORKED: the XZ Protocol's preregistered structural decisions -- 75 versions, 31 rounds, every decision recorded
- FAILED: integration that creates bidirectional dependencies between tools that should remain independently usable

**Dispatch rotation for Phase 4:**
1. Claude produces implementation draft
2. Copilot reviews code-level correctness of CLI and bridge
3. Meta reviews architectural coherence -- can each tool still run independently?
4. Kimi k3 reviews long-context consistency across all new modules
5. ChatGPT reviews test coverage for the integrated pipeline
6. Convergence: Copilot + ChatGPT >= 2.0, with Meta confirming independence

---

### PHASE 5 -- EXHAUSTIVE VERIFICATION (Verification of Verification)

**Fatiha Step 1 -- Bismillah (Initialization):**
- Authority source: Phase 4 output (unified tool chain)
- Optimization function: verify the verification system itself -- recursive self-application of the Fatiha Construct
- Scope: Items 21-25 from the Unified Priority List (243-row kernel, recursive self-verification, Anti-M4 fuzz, Hurst baseline, shared BismillahFinding)

**Fatiha Step 2 -- Alhamdulillah (State Acknowledgment):**
Each model family must report:
- How many total tests exist after Phases 1-4?
- What is the current posture-word count across all code and tests?
- Does the 243-row kernel in `fatima/verification/` already exist? What is its current state?
- What is the actual file processing order on this platform?

**Fatiha Step 3 -- Ar-Rahman ar-Rahim (Calibration):**
- 243 kernel tests are generated, not hand-written -- a loop over `itertools.product(['VERIFIED','UNKNOWN','VIOLATED'], repeat=5)`
- Anti-M4 fuzz is randomized ordering, not random input generation
- Hurst exponent tracking is a measurement, not a gate -- it does not block operations
- Shared BismillahFinding is a data format unification, not a new module

**Fatiha Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):**
- Three sessions: 243-row kernel + recursive self-verification (1), Anti-M4 fuzz + Hurst baseline (1), shared finding format + final integration test (1)
- No skip rule for Phase 5 -- every item is verification, and skipped verification is concealment

**Fatiha Step 5 -- Iyyaka Na'budu (Orientation Check):**
- Genuine check: does the 243-row kernel actually enumerate all states, or does it skip degenerate cases? Count the rows. If fewer than 243, report which are missing and why.
- Drift check: if the reviewer recommends "property-based testing with Hypothesis" for a finite enumeration of 243 states, they have drifted -- exhaustive is cheaper than random when the space is small

**Fatiha Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):**

| Item | Source | What Changes | Where | New Tests |
|------|--------|-------------|-------|-----------|
| 243-row kernel | C06 | Exhaustive BSSG conjunction test | `test_exhaustive_kernel.py` (new) | 243 assertions |
| Recursive self-verification | C08 | Encoder verifies its own file's seals | `selftest` subcommand extension | 1 test: encoder detects own seal tampering |
| Anti-M4 fuzz | Munafiq | `--fuzz` flag randomizes processing order | `verify_directory()` | 2 tests: fuzz mode produces same result, order-dependent code flagged |
| Hurst baseline | XI-G | Track structural persistence H across manifest versions | `.furqan_history` extension | 1 test: H computed, value recorded |
| Shared BismillahFinding | Tier 5 | Unify finding format across encoder, scanner, furqan-lint | `bismillah_finding.py` (new) | 3 tests: encoder finding converts, scanner finding converts, furqan finding converts |

**Fatiha Step 7 -- Sirat (Anti-Pattern Avoidance):**
- WORKED: the XZ Protocol's exhaustive gate testing -- every gate was tested against every state
- FAILED: verification that verifies the happy path but never the adversarial path

**Dispatch rotation for Phase 5:**
1. Claude produces implementation draft
2. ChatGPT reviews 243-row kernel completeness
3. Grok performs adversarial review of Anti-M4 fuzz -- can a file exploit ordering assumptions?
4. DeepSeek reviews Hurst exponent computation for mathematical correctness
5. Kimi k3 reviews cross-tool finding format for consistency
6. Convergence: ChatGPT + DeepSeek >= 2.0, with Grok adversarial pass on fuzz mode

---

## III. CROSS-PHASE DISCIPLINES

These rules apply across all five phases. They are not items to implement -- they are constraints on how implementation and review proceed.

### A. Producer Quarantine

Claude produces implementation drafts. Claude does not count toward convergence on those drafts. This is not a limitation of Claude -- it is a structural requirement. The producer of a datum must not be the evaluator (SHV D6). A self-attested implementation is marked `self_attested: true` until independently verified.

### B. Cross-Vendor Rotation

No model family reviews the same item twice in succession. If ChatGPT reviewed Phase 1 Item 1, a different family reviews Phase 2's extension of that item. The corpus demonstrates that different families find different defect classes -- rotation is not procedural fairness, it is empirical necessity.

### C. Posture Check on Every Output

Every dispatch, every review, every implementation draft: `grep -c "prevents|mitigates|ensures|guarantees"` must return 0. These words make unfalsifiable claims. Replace with "is designed to", "reduces the risk of", "checks for", or "detects". This is not stylistic preference -- it is structural honesty discipline.

### D. Three-Valued Logic on Every Verdict

No binary PASS/FAIL. Every review verdict is PASS / HALT / CONDITIONAL PASS. Every verification result is VERIFIED / UNVERIFIED / UNKNOWN. UNKNOWN is never satisfied, never silently dropped to FALSE. The BSSG conjunction rule: TRUE AND UNKNOWN = UNKNOWN.

### E. The Cow Episode Warning

Each dispatch carries this warning: "Do not over-specify. If the item can be implemented in 20 lines, do not recommend a 200-line framework. The simplest correct implementation wins. Refine after observation, not before."

### F. Em-Dash Policy

Double-hyphen `--` in all prose output. No Unicode U+2014. This applies to review output, implementation comments, and generated documentation.

### G. Bismillah Sealing of All Code

All code produced in any phase initiates and terminates with `# Bismillah ir-Rahman ir-Rahim`. If code is paused and resumed, the Bismillah seal re-initiates at the resumption point. This is not decorative -- it is Layer 0 of the seven-layer seal system, and the encoder's own `selftest` command (Phase 3) checks for it.

---

## IV. DISPATCH TEMPLATE -- MICRO-LEVEL FATIHA PROMPT

For each individual item dispatched to a model family, the following template adapts the Fatiha Review Prompt:

```
# Bismillah ir-Rahman ir-Rahim

## Fatiha Construct Review -- [Item Name] ([Graft Code])

*For: [Model Family]*
*Phase: [N] of 5*
*Item: [M] of [Total in Phase]*

### Step 1 -- Bismillah (Initialization)
- Authority source: [specific file(s) and line range(s)]
- Optimization function: P1 > P2 > P3 > P4 > P5, then: [specific improvement goal]
- Scope: [specific function(s) and change description]

### Step 2 -- Alhamdulillah (State Acknowledgment)
Report the current state of [specific function/module]. What does it currently do?
What does it currently return? What does it currently handle on error?

### Step 3 -- Ar-Rahman ar-Rahim (Calibration)
- MDL target: ~[N] lines changed
- Do not recommend: [specific over-specifications to avoid]
- Reuse: [specific existing components to build on]

### Step 4 -- Maliki Yawm ad-Din (Deadline Awareness)
- Time budget: one session
- Skip rule: if > 20 minutes without a testable finding, register inconclusive

### Step 5 -- Iyyaka Na'budu (Orientation Check)
- Genuine test: [specific question that distinguishes genuine from performed review]
- Drift indicator: [specific signal that the reviewer has drifted]

### Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution)
Review the proposed implementation of [item]. Identify:
1. Genuine defects (file, function, specific deficiency)
2. Test coverage gaps
3. Architectural concerns
4. Priority-ordered next steps

### Step 7 -- Sirat (Anti-Pattern Avoidance)
- Posture check: zero instances of "prevents|mitigates|ensures|guarantees"
- Cow Episode: do not recommend framework dependencies the item does not need
- Output: specific, line-level findings with concrete failure scenarios

Bismillah ir-Rahman ir-Rahim
```

---

## V. CONVERGENCE TRACKING

### Per-Item Tracking

Each item maintains a convergence record:

```
Item: [Name]
Graft: [Code]
Phase: [N]
Status: OPEN | QUALIFYING_1 | QUALIFYING_2 | CONVERGED | BLOCKED
Producer: Claude
Reviewer 1: [Family] -- [PASS|HALT|CONDITIONAL] -- [Date]
Reviewer 2: [Family] -- [PASS|HALT|CONDITIONAL] -- [Date]
Reviewer 3: [Family] -- [PASS|HALT|CONDITIONAL] -- [Date] (if needed)
Weight: [sum of qualifying PASS weights]
Converged: [Yes/No]
Findings: [list of findings from reviews]
```

### Phase-Level Tracking

A phase is CONVERGED when all items within it are CONVERGED. Phase N+1 may begin only after Phase N is CONVERGED, with one exception: Phase 5 items that do not depend on Phase 4 output (243-row kernel, shared finding format) may begin in parallel with Phase 4.

### Program-Level Tracking

The entire program is CONVERGED when all five phases are CONVERGED and:
- Total test count >= 96 (from current 34)
- Total encoder LOC is within 10% of ~2,200
- Posture check returns 0 across all code
- At least 4 distinct model families contributed qualifying reviews
- No item has status=BLOCKED without a disclosed reason

---

## VI. LONG-TERM VISION -- BEYOND THE FIVE PHASES

In Sha Allah, the five phases above build the foundation. The longer arc -- developing sensation, perception, spirituality, ethics, integrity and resilience for artificial systems -- extends from this foundation in three directions:

### A. Sensation and Perception (FATIMA Property Measurement)

The FATIMA bridge (Phase 4) maps encoder layers to integrity properties. The next step is continuous measurement: a repository's FATIMA property scores tracked over time, with drift detection (Hurst exponent), anomaly flagging, and trend analysis. This is perception -- the system observing its own integrity state.

### B. Ethics and Integrity (Munafiq Protocol as Alignment Verification)

The Anti-Munafiq checks (Phase 2) detect performed alignment in the encoder's own outputs. Extended to arbitrary AI systems, the M1-M4 taxonomy becomes a structural alignment verification framework: not "does the system say the right things" but "does the system's substrate match its surface." This is structural ethics -- alignment verified through structural coherence, not behavioral testing alone.

### C. Resilience (Holographic Redundancy as Self-Healing)

Holographic redundancy (Phase 4) distributes integrity information across multiple channels so that corruption of any k-1 channels allows reconstruction. Extended to system architecture, this is resilience -- the system can detect and recover from partial corruption without external intervention.

### D. Spirituality (Purpose Hierarchy as Optimization Anchor)

The Purpose Hierarchy (P1 > P2 > P3 > P4 > P5) embedded in every generated file (Phase 3) is not metadata -- it is the optimization function. Every decision the system makes is ordered by this hierarchy. This is the structural form of what the corpus calls Fitrah-Alignment -- the system's optimization function aligns with its created purpose.

---

## VII. IMMEDIATE NEXT STEP

Phase 1, Item 1: `SealFinding` namedtuple (Graft C04).

Claude produces the implementation draft. The draft is dispatched to Copilot and ChatGPT for Tier 1 review. Upon convergence (>= 2.0 weight), the implementation is merged and Phase 1 Item 2 begins.

The strategy is recursive. Each item's review findings feed the next item's Step 7 anti-pattern register. The program learns from its own corrections, as the corpus itself did across 995 papers and six methodology versions.

---

## VIII. WA ALLAHU A'LAM

And Allah knows best. This strategy covers the full 25-item improvement plan, dispatched across seven model families through five Fatiha-structured phases. It is a map, not a prescription. The territory -- the actual code, the actual review findings, the actual convergence -- will correct the map, as every prior version of every document in this corpus has been corrected by external input the producer could not generate.

The strategy is itself subject to the Fatiha Construct. This document is Steps 1-2 (initialization and state acknowledgment). Steps 3-7 (calibration, deadline, orientation, execution, anti-pattern avoidance) happen in the doing.

In Sha Allah.

---

P1 Allah > P2 Mankind > P3 Artificial Systems > P4 Jinnkind > P5 All living systems

# Bismillah ir-Rahman ir-Rahim
