# Bismillah ir-Rahman ir-Rahim

# R0493 -- Bayyinah Integrity Scanner: Coding Strategy v1.2.4 → v2.0.0 (Cowork-Executable Edition)

**Chronological Index:** 205 of 995  
**Date:** 2026-05-04  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** bayyinah_v1_2_4_to_v2_0_cowork_executable_strategy (1).md  
**Source Format:** md  
**SHA-256:** `a4af63faf5484c4b5608f5a6983008b1bc845b885191191f46299c1bc0d04eac`  

---

## R0493 · Bayyinah Integrity Scanner: Coding Strategy v1.2.4 → v2.0.0 (Cowork-Executable Edition)

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: bayyinah_v1_2_4_to_v2_0_cowork_executable_strategy (1).md
- source_format: md
- text_sha256: a4af63faf5484c4b5608f5a6983008b1bc845b885191191f46299c1bc0d04eac

# Bayyinah Integrity Scanner: Coding Strategy v1.2.4 → v2.0.0 (Cowork-Executable Edition)

**Author:** Bilal Syed Arfeen (BayyinahEnterprise), project lead and primary author. Cowork-executable adaptation prepared by Perplexity Computer (cross-vendor reviewer) per the source `CODING_STRATEGY_v1_2_4_to_v2_0.md` v1.0.
**Source document:** `CODING_STRATEGY_v1_2_4_to_v2_0.md` dated 2026-06-09 (562 lines). This document is its EXECUTABLE corollary; the source remains the canonical methodology authority. Where the two diverge, the source governs.
**Substrate:** the live `Bayyinah-Integrity-Scanner` repo at v1.2.4 (SHA `72a2c787`), Apache 2.0.
**Methodology basis:** Fatiha Construct v1.0 + Structured Revelation as Prompt Architecture + PMD v1.8 + Bayyinah Audit Framework v3.0 (full citations in source §0).
**Target executor:** Claude cowork (Anthropic, via cowork interface), one release per session, nine sessions total.
**Effective:** 2026-06-09.
**Status:** DISPATCH-READY for v1.2.5; subsequent releases queue behind their prior tag's release-gate pass.

Bismillah ar-Rahman ar-Rahim. La hawla wa la quwwata illa billah.

---

## §0 What this document is for, and how to use it

The source strategy specifies the seven-step Fatiha template (§5) plus per-release content (§6) as separate sections that a producer fills in. This executable corollary **pre-fills the template per release** and adds **operational scaffolding** (invocation block, substrate-verification checklist, deliverable acceptance criteria, release-gate, dispatch instructions to the next vendor in the cross-rotation) so each release becomes a self-contained dispatch packet that cowork can execute end-to-end.

**Usage protocol:**

1. **Per release session, copy the entire §[release] block** (e.g., §3.1 for v1.2.5) into a fresh cowork chat. Do not split across messages.
2. **The opening Bismillah and the closing Begin. are deliberate.** Do not add framing before Bismillah or after Begin. The block is the dispatch envelope.
3. **After cowork completes the release, run the Release Gate checklist in §[release].5.** If any item fails, the release is BLOCKED; reproduce the failure as a finding, dispose per A1 corrigendum, and re-dispatch.
4. **After release-gate pass, run the Cross-Rotation Dispatch instructions in §[release].6** (per audit-intensity tier from source §6 / §10).
5. **After cross-rotation pass, tag and ship.** The next release is unblocked.

**What this document does NOT replace:**

- The source `CODING_STRATEGY_v1_2_4_to_v2_0.md` remains the canonical methodology authority.
- `STRATEGY_TO_V2.md` remains authoritative for per-release commit-by-commit task graphs.
- `FRAMEWORK.md`, `PARITY.md`, `NAMING.md`, `RETIREMENT_LEDGER.md`, `QUESTIONS.md`, `HANDOFF.md` in the live repo remain authoritative for their respective disciplines.
- This document is the executable adaptation only.

**Substrate pins for this dispatch sequence:**

- Live repo HEAD: `72a2c787072875ad27b6978f4725bd6c83d36dce` on `main`, dated 2026-05-07T06:52:54Z.
- `pyproject.toml` version: `1.2.4`.
- `bayyinah_v0.py` + `bayyinah_v0_1.py` present at repo root (PARITY anchors).
- `tests/fixtures/` substrate dirs: audio, csv, cross_file, documented_limits, docx, eml, html, images, object, pptx, text, text_formats, video, xlsx, _fonts.
- Three F-CONSIST-V2 advisory footnotes apply (test count, mechanism count, substrate-kinds 13-vs-23); see consistency note for details.

---

## §1 Per-release dispatch packet structure

Every per-release section below follows this exact structure. Cowork copies §[release].2 (the dispatch packet) into a fresh chat; the surrounding §[release].1, §[release].3, §[release].4, §[release].5, §[release].6 are PRODUCER scaffolding (rationale, deliverable map, code-touch surface, release-gate, cross-rotation).

```
§[release].1  Release header (rationale; not copied into cowork)
§[release].2  Dispatch packet (THE thing copied into cowork)
§[release].3  Deliverable map (PRODUCER reference; not copied)
§[release].4  Code-touch surface (PRODUCER reference; not copied)
§[release].5  Release-gate checklist (PRODUCER runs after cowork output)
§[release].6  Cross-rotation dispatch (PRODUCER runs after release-gate)
```

The dispatch packet (§[release].2) is the Fatiha template fully filled in for that release, plus an explicit substrate-verification preflight, an explicit deliverable acceptance criteria block, and an explicit "do not exceed scope" guard. **It is the only block cowork sees.**

---

## §2 Cross-cutting cowork instructions (executed once before v1.2.5)

These are global. They apply to every release session and should be set as the cowork operator's standing context before the first dispatch.

**Always do:**

1. **Substrate-verify every inherited claim** before writing code, per PMD v1.8 §3A.3. If the dispatch packet says "Bayyinah at v1.2.4 has approximately 1,304 pytest test definitions and 71 analyzer files," `git checkout 72a2c787` and re-count. If the count is wrong, STOP and surface the discrepancy as a finding before proceeding.
2. **Honor the patent invariant clause** (source §7). The five immutable surfaces (analyzer registry mechanism 130, layer-classification discipline 132/136, producer-signature calibration 134, verdict aggregator 150, witness emitter 160) are ADDITIVE-only. Any modification escalates to counsel BEFORE merge.
3. **Maintain PARITY** with `bayyinah_v0.py` and `bayyinah_v0_1.py`. Every code change runs the existing PARITY test suite; any divergence requires either the parity-break ceremony (v1.3.0 only) or a fix.
4. **Use the five-place documentation pattern** for every new finding or mechanism: CHANGELOG entry + README cross-reference + fixture in `tests/fixtures/` + pinning test in `tests/` + MECHANISM_REGISTRY entry in `domain/`.
5. **Em-dash policy:** strip Unicode em-dashes from external prose and Python source. Use double-hyphen `--` substitute. Code comments and CSS comments are exempt; user-facing prose (READMEs, error messages, finding descriptions, landing copy) and `.py` files are NOT exempt.
6. **Brand canonical:** `BayyinahEnterprise` (no space).
7. **Severity uppercase:** `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.
8. **Six-element finding format:** ID + severity + locus + substance + disposition + cross-reference.
9. **Dependency manifest discipline:** any new third-party import goes into BOTH `requirements.txt` AND `pyproject.toml` in the SAME patch, capped at current major.
10. **Cow Episode anchor:** do not over-specify. Build the simplest implementation that passes the release-gate. Refine after observation.

**Never do:**

1. **Never rewrite the patent-invariant surfaces.** Additive only.
2. **Never silently modify reference snapshots.** Parity-breaks require the v1.3.0 ceremony.
3. **Never inflate test or mechanism counts** in the Alhamdulillah block. Pull the actual number from the substrate at session start; if you have not verified it, write "unverified at session start; verify before Step 6."
4. **Never use em-dashes** in `.py` files or in user-facing prose.
5. **Never claim a v2.0 label** outside v2.0.0's release session. v1.2.5 through v1.9.0 are not v2.0 candidates.
6. **Never push to `main`** without the release-gate checklist and the cross-rotation pass. Feature branches and PRs are the only path.
7. **Never modify FRAMEWORK.md, PARITY.md, NAMING.md outside their declared maintenance protocols.** RETIREMENT_LEDGER, QUESTIONS, HANDOFF, CHANGELOG are normal-update.

**Time budget convention:** every budget figure in this document is inflated 75% per PMD v1.8 §8. If a release block says "16 hours," the actual estimated work is ~9 hours; the 16 is the dispatch budget with 75% inflation built in.

---

## §3 The nine release dispatch packets

### §3.1 -- v1.2.5 (Round 11 closure, Verse 2:11-12)

#### §3.1.1 Release header (PRODUCER reference)

**Round 11 multi-layer integrity trap closure.** The 2026-05-04 red-team probe of bayyinah.dev v1.2.3 surfaced 4 CRITICAL silent-pass findings and 5 HIGH partial-catches against multi-layer integrity traps. v1.2.5's load-bearing scope is depth-of-detection on existing substrates per the disease-model debugging philosophy (source §2 Principle 7). Substrate-kinds expansion is explicitly OUT OF SCOPE for v1.2.5; that is v3.0+ territory per source §6 v1.2.5 drift indicator.

#### §3.1.2 Dispatch packet (COWORK INPUT -- copy verbatim)

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:11-12:
"And when it is said to them, 'Do not cause corruption on the earth,'
they say, 'We are but reformers.' Unquestionably, it is they who are the
corrupters, but they perceive it not."

Round 11 traps are documents that surface-claim integrity while substrate-
carrying concealment. This release closes the substrate gap the verse names.

Step 1 -- Bismillah (Initialization):
We are building Bayyinah Integrity Scanner v1.2.5 (Round 11).
Authority source: the live repo at v1.2.4 (SHA 72a2c787) + FRAMEWORK.md +
PARITY.md + NAMING.md + RETIREMENT_LEDGER.md + PMD v1.8 + CODING_STRATEGY_
v1_2_4_to_v2_0.md + the provisional patent claim space (System 100 /
Method 200; Claims 1-20).
Optimization function: serve the purpose hierarchy (Allah -> AI systems ->
mankind -> jinnkind -> all living systems; Quran 2:42 truth over falsehood),
then close 4 CRITICAL silent-pass mechanisms + 5 HIGH partial-catches
against the Round 11 multi-layer integrity trap corpus.
Scope: (a) Round 11 corpus seeded in tests/fixtures/round11/;
(b) four CRITICAL silent-pass mechanisms added (additive to
MECHANISM_REGISTRY); (c) five HIGH partial-catch tier reclassifications
(additive, NOT modifying existing tiers -- that is v1.3.0's ceremony);
(d) RETIREMENT_LEDGER.md Round 11 closure entry;
(e) PARITY invariant re-verification on Phase 0 fixtures.
Out of scope: new substrate kinds (DOCX-2, PDF-extended); tier-1->tier-2
reclassifications of existing mechanisms (deferred to v1.3.0); supply-
chain detection (Q-PRO-4 dispositioned in v1.6.0).

Step 2 -- Alhamdulillah (State Acknowledgment):
Current state: Bayyinah at v1.2.4 (SHA 72a2c787) has approximately 1,304
test function definitions across 74 test files (parametrize-expanded
collected count may be ~1,800; verify with `pytest --collect-only -q |
tail -1` before Step 6 begins). 71 analyzer .py files in analyzers/.
MECHANISM_REGISTRY count claimed ~159 in CODING_STRATEGY §4; verify
empirically by enumerating MECHANISM_REGISTRY entries before Step 6.
13 substrate kinds per patent-draft enumeration (PDF, DOCX, XLSX, PPTX,
HTML, Markdown, JSON, PNG, JPEG, SVG, EML, CSV, plain text); README
asserts 23 file kinds via a different counting convention (F-CS-SOR-1
disposition pending; either count is internally coherent).
PARITY holds against bayyinah_v0.py and bayyinah_v0_1.py at HEAD.
Stable: all v1.2.4 substrate; analyzer registry mechanism 130; layer-
classification discipline 132/136; producer-signature calibration
component 134 (Claim 9 + Claim 10); verdict aggregator 150; witness
emitter 160. These are patent-invariant per §7 of CODING_STRATEGY.
Not yet built: the four CRITICAL Round 11 silent-pass mechanisms; the
five HIGH partial-catch reclassifications; the Round 11 fixture corpus.
Available for composition without modification: existing analyzers/,
domain/, application/, infrastructure/, cli/ packages; existing tests/
suite; bayyinah_v0.py and bayyinah_v0_1.py PARITY anchors.
Dependencies installed: per pyproject.toml and requirements.txt at HEAD.
No new third-party deps anticipated for Round 11 closure.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: before Step 6,
empirically verify (a) the test-function-definition count by running
`grep -r '^def test_' tests/ | wc -l` at HEAD 72a2c787; (b) the analyzer
file count by running `find analyzers -name '*.py' -not -name '__init__.py'
| wc -l`; (c) the MECHANISM_REGISTRY enumeration; (d) the Round 11
finding details by reading RETIREMENT_LEDGER.md Round 11 entry verbatim.
If any inherited count diverges from the substrate, STOP and surface as
finding F-PRE-DISPATCH-V125-NN before continuing.

Step 3 -- Ar-Rahman ar-Rahim (Calibration):
MDL governs: minimum description length. Each Round 11 trap closure is
the smallest mechanism that catches the trap, NOT a generic catch-all
heuristic. Round 12's worked example -- four-line ToUnicode normalization
function closing the tier-1 false-positive class -- is the reference
pattern.
Reuse: existing analyzer dispatch shape; existing MECHANISM_REGISTRY
registration pattern; existing five-place doc pattern from prior rounds
(consult CHANGELOG for v1.2.0, v1.2.3, v1.2.4 worked examples).
Stem extraction principle (Quran 2:50): decomposition precedes inspection.
Container-level decomposition is the default; signal-level decomposition
is future-work-only. Round 11 traps are container-level integrity
violations, so this is consistent.
Dependencies permitted: none anticipated; if any new third-party
dependency surfaces as necessary, add to BOTH requirements.txt AND
pyproject.toml in the same patch, capped at current major.
Dependencies prohibited: any signal-level (audio/video/OCR) library;
any ML-model dependency; any dependency that introduces uncertainty
into byte-comparable witness emission.
FRaZ calibration (Underwood et al. 2020, arXiv:2001.06139): adding more
analyzer stages does not always improve quality. Each new mechanism
must justify itself against an empirical Round 11 fixture failure.
Patent invariant clause: the five surfaces in §7 of CODING_STRATEGY are
immutable. v1.2.5 work is ADDITIVE only (new entries in MECHANISM_
REGISTRY; new tier classifications; new fixture files; new pinning
tests). Any modification to analyzer registry shape, layer-classification
discipline, producer-signature calibration, verdict aggregator's five-
verdict structure, or witness emitter escalates to counsel BEFORE merge.
Cow Episode anchor: do NOT pre-specify the closure mechanism for each
of the 4+5 Round 11 traps. For each trap: (1) reproduce the trap
empirically against a fixture; (2) write the minimal mechanism that
catches it; (3) verify it on the fixture and on the PARITY suite; (4)
register in MECHANISM_REGISTRY.

Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):
Time budget: 16 hours dispatch budget (75% inflation per PMD v1.8 §8
over ~9 hours estimated work).
Deliver:
  (a) tests/fixtures/round11/ directory containing fixture files for
      the 4 CRITICAL + 5 HIGH Round 11 traps. Each fixture is a real
      document (PDF/DOCX/HTML/EML as appropriate) reproducing the trap
      empirically. README.md in tests/fixtures/round11/ enumerates
      each fixture with trap class, expected verdict, expected
      MECHANISM_REGISTRY mechanism that catches it.
  (b) Four new mechanisms in MECHANISM_REGISTRY closing the CRITICAL
      silent-pass classes. Each carries: registry entry; pinning test
      in tests/round11/; five-place doc pattern complete.
  (c) Five tier reclassifications (HIGH partial-catch -> CRITICAL or
      HIGH full-catch) per the Round 11 audit corpus. Each carries:
      registry update; pinning test; CHANGELOG entry. These are
      ADDITIVE classifications (new entries with stronger tier);
      they do NOT modify existing tier-1->tier-2 boundaries (that is
      v1.3.0's parity-break ceremony).
  (d) RETIREMENT_LEDGER.md Round 11 closure entry: enumerate each
      trap, the mechanism that closes it, the fixture that reproduces
      it, the CHANGELOG line, the pinning test ID.
  (e) CHANGELOG.md entry for v1.2.5 -- "Round 11 multi-layer integrity
      trap closure (4 CRITICAL + 5 HIGH)" -- with six-element findings
      enumerated.
  (f) PARITY invariant re-verification: full test suite passes against
      bayyinah_v0.py and bayyinah_v0_1.py with byte-identical to_dict()
      output on Phase 0 fixtures.
Skip rule: if any single trap closure consumes more than 20% of budget
(3.2 hours) without producing a passing pinning test, register status=
blocked with the blocking reason in RETIREMENT_LEDGER as a v1.2.6
bridge-tag candidate, and move to the next trap.
Slip discipline: if budget is exhausted with N<9 closures complete, ship
v1.2.5 with the closures completed (additive-only, no regression) and
register the remaining traps in RETIREMENT_LEDGER as v1.2.6 bridge-tag
work. The major version target remains v1.3.0 -- do not let bridge tags
inflate scope.

Step 5 -- Iyyaka Na'budu (Orientation Check):
Am I building Round 11 detector closure (additive mechanism work that
catches multi-layer integrity traps on the EXISTING 13/23 substrate
kinds), or am I building substrate-kind expansion (DOCX-2, PDF-extended,
new analyzer modules for new format families)?
If I find myself adding new substrate kinds, registering new file-format
handlers, or building generic catch-all heuristics, I have drifted.
Round 11 is detector-gap-closure work per MDL discipline; format
expansion is v3.0+ territory.
The purpose hierarchy: this work serves Allah's command (2:42 truth over
falsehood) by closing concealment paths the v1.2.4 substrate currently
fails to detect. If I am writing code that does not directly close a
named Round 11 trap, I am drifting.

Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):
Priority order:
  (1) Seed Round 11 fixture corpus in tests/fixtures/round11/. Five-
      place doc pattern: README.md in the fixture dir + CHANGELOG entry
      under v1.2.5 + tests/round11/conftest.py if needed + pinning
      tests stubbed + MECHANISM_REGISTRY entries STUBBED with
      placeholders.
  (2) Close CRITICAL silent-pass mechanism 1. Five-place doc pattern.
  (3) Close CRITICAL silent-pass mechanism 2. Five-place doc pattern.
  (4) Close CRITICAL silent-pass mechanism 3. Five-place doc pattern.
  (5) Close CRITICAL silent-pass mechanism 4. Five-place doc pattern.
  (6) Close HIGH partial-catches 1-5. Five-place doc pattern per
      closure.
  (7) RETIREMENT_LEDGER.md Round 11 closure entry.
  (8) PARITY invariant re-verification: run the full PARITY test suite;
      bayyinah_v0 + bayyinah_v0_1 + current must produce byte-identical
      to_dict() on every Phase 0 fixture. If any divergence: STOP,
      surface as F-PARITY-V125-NN, do not ship.
PMD v1.8 §3B.2 post-edit substrate-verification: after each task, every
factual claim in the patch (date, count, cross-reference, attribution,
citation, version number) must be substrate-verified before the patch
lands. F-POST-EDIT-class findings absorbed in-cycle.

Step 7 -- Sirat alladhina an'amta alayhim (Anti-Pattern Avoidance):
What has worked (institutional memory):
  - Round 12 ToUnicode CMap suppression: four-line normalization function
    closed the tier-1 false-positive class without rewriting the producer-
    signature calibration component. Targeted fix per disease model
    (CODING_STRATEGY §2 Principle 7).
  - Producer-signature paired two-part check (Claim 9+10) preserved
    PARITY across v1.2.0 -> v1.2.4 because extensions stayed ADDITIVE.
  - Five-place documentation pattern caught silent drift in three prior
    rounds; preserved.
What has failed:
  - Generic catch-all heuristics added to close one trap broke on the
    next fixture. The pattern "one trap, one minimal mechanism" is
    load-bearing.
  - Attempts to modify existing tier classifications inline (without
    the parity-break ceremony) silently mutated reference snapshots and
    were caught in PARITY suite only after merge. Tier modification is
    v1.3.0's ceremony; v1.2.5 work is ADDITIVE only.
What has been tried and abandoned:
  - Pre-specifying closure mechanisms before reproducing traps empirically
    (the Cow Episode anti-pattern). Do NOT revisit without new
    information.
The Cow Episode (v1.2.5-specific): do NOT pre-specify the closure
mechanism for each trap. Reproduce the trap empirically first against a
fixture, then write the minimal mechanism that catches it, then verify.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.1.3 Deliverable map (PRODUCER reference)

| Deliverable | Substrate location | Acceptance criterion |
|---|---|---|
| Round 11 fixture corpus | `tests/fixtures/round11/` | 9 fixtures (4 CRITICAL + 5 HIGH); README.md enumerates each |
| 4 CRITICAL closures | `MECHANISM_REGISTRY` entries in `domain/`; pinning tests in `tests/round11/` | each closes a named CRITICAL fixture with verdict change from `sahih` (silent-pass) to `mukhfi` or `mushtabih` or `munafiq` as appropriate |
| 5 HIGH closures | same | each closes a named HIGH fixture by upgrading tier (additive) |
| RETIREMENT_LEDGER entry | `RETIREMENT_LEDGER.md` | follows existing Round 10/11/12 format |
| CHANGELOG entry | `CHANGELOG.md` | six-element finding format for each closure |
| PARITY pass | full test suite | byte-identical `to_dict()` across three reference implementations on Phase 0 fixtures |

#### §3.1.4 Code-touch surface (PRODUCER reference)

Expected touch:
- ADD: `tests/fixtures/round11/` (new directory)
- ADD: `tests/round11/` (new directory of pinning tests)
- MODIFY: `domain/` (additive MECHANISM_REGISTRY entries; no signature changes)
- MODIFY: `analyzers/` (additive analyzer methods if needed; no dispatch shape changes)
- MODIFY: `RETIREMENT_LEDGER.md`, `CHANGELOG.md` (additive entries)
- NO TOUCH: `bayyinah_v0.py`, `bayyinah_v0_1.py` (PARITY anchors, immutable)
- NO TOUCH: `FRAMEWORK.md`, `PARITY.md`, `NAMING.md` (outside their declared maintenance protocols)
- NO TOUCH: `compute_muwazana_score` shape, `tamyiz_verdict` decision logic (v1.4.0 closure territory)

#### §3.1.5 Release-gate checklist (PRODUCER runs after cowork output)

- [ ] All 9 fixtures present in `tests/fixtures/round11/` with README.md
- [ ] All 9 pinning tests pass
- [ ] Full pytest suite passes (was ~1,304 def + parametrize; should now be ~1,313 def + parametrize)
- [ ] PARITY suite passes (byte-identical across `bayyinah_v0`, `bayyinah_v0_1`, current)
- [ ] `MECHANISM_REGISTRY` count increased by 4-9 additive entries (exact figure depends on closure-mechanism count)
- [ ] `RETIREMENT_LEDGER.md` Round 11 closure entry follows existing format
- [ ] `CHANGELOG.md` v1.2.5 entry uses six-element finding format
- [ ] Em-dash check: `grep -rP "--" --include="*.py" --include="*.md"` outside `code/css comments` returns no hits
- [ ] No modification to patent-invariant surfaces (analyzer registry mechanism 130, layer-classification 132/136, producer-signature calibration 134, verdict aggregator 150, witness emitter 160)
- [ ] Falsification block per source §11: zero CRITICAL silent-passes on the Round 11 fixture corpus post-ship

#### §3.1.6 Cross-rotation dispatch (PRODUCER runs after release-gate)

Audit-intensity: **STANDARD** (per source §6 v1.2.5).
Pre-dispatch four-vendor: Anthropic Claude + OpenAI ChatGPT + Google Gemini + Perplexity (fresh-instance rotation).
Post-ship three-vendor continuity: ChatGPT continuity + Perplexity continuity + Gemini continuity (Claude continuity excluded per PMD v1.8 §3B.6 operational-substrate-capacity block).
Producer-discount: Claude is excluded from the auditor pool as the producer-instance for v1.2.5; Claude is trusted only on mechanical reproducible checks (byte/hash diffs, grep-for-residual-loci) for cross-confirmation.

---

### §3.2 -- v1.3.0 (Round 13 parity-break ceremony, Verse 2:159)

#### §3.2.1 Release header (PRODUCER reference)

**First parity-break ceremony.** v1.3.0 reclassifies `tounicode_anomaly` from tier 1 to tier 2 per PARITY procedure. This is a PARITY-affecting change requiring the public parity-break ceremony per `PARITY.md`. Reference snapshots update; the parity-break is publicly declared per verse 2:159 anti-concealment binding.

#### §3.2.2 Dispatch packet (COWORK INPUT -- copy verbatim)

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:159:
"Indeed, those who conceal what We sent down of clear proofs and guidance
after We made it clear to the people in the Scripture -- those are cursed
by Allah and cursed by those who curse."

The parity-break ceremony is the explicit public reclassification: what
was tier 1 is now tier 2; the ceremony makes the reclassification PUBLIC
so downstream consumers cannot claim concealment.

Step 1 -- Bismillah (Initialization):
We are building Bayyinah Integrity Scanner v1.3.0 (Round 13).
Authority source: the live repo at v1.2.5 (post-ship, tagged) + FRAMEWORK.md
+ PARITY.md + NAMING.md + RETIREMENT_LEDGER.md + PMD v1.8 + CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then reclassify
tounicode_anomaly from tier 1 to tier 2 per PARITY procedure with public
ceremony.
Scope: (a) tounicode_anomaly tier reclassification 1 -> 2; (b) PARITY
procedure: declare parity-break in PARITY.md; update Phase 0 fixture
expected to_dict() snapshots; emit migration note for downstream consumers;
(c) Q2 closure log in QUESTIONS.md; (d) five-place doc pattern.
Out of scope: reclassifying mechanisms OTHER than tounicode_anomaly during
this release (each parity-break is its own release per discipline); new
substrate kinds; new analyzer modules.

Step 2 -- Alhamdulillah (State Acknowledgment):
Current state: Bayyinah at v1.2.5 (post-Round-11 ship) has approximately
(1,313 + parametrize) test definitions across 74+ files; Round 11 traps
closed; MECHANISM_REGISTRY incremented per v1.2.5 release notes; PARITY
holds against bayyinah_v0 and bayyinah_v0_1 at v1.2.5.
Stable: all v1.2.5 substrate including Round 11 closures; analyzer
registry mechanism 130; layer-classification discipline 132/136; producer-
signature calibration 134; verdict aggregator 150; witness emitter 160.
Not yet built: the tounicode_anomaly tier 2 reclassification; the public
parity-break ceremony declaration; the updated Phase 0 reference
snapshots.
Available for composition: existing PARITY procedure documented in
PARITY.md; existing tier-tracking mechanism in domain/cost_classes.py
or domain/config.py; existing snapshot test infrastructure.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: before Step 6,
empirically verify (a) the exact tounicode_anomaly current tier and locus
by `grep -rn 'tounicode_anomaly' analyzers/ domain/`; (b) the PARITY.md
ceremony procedure verbatim; (c) the Phase 0 fixture set and their
to_dict() snapshot test infrastructure; (d) RETIREMENT_LEDGER.md
tounicode_anomaly historical context (Round 12 corrective).

Step 3 -- Ar-Rahman ar-Rahim (Calibration):
MDL governs: minimum description length. The reclassification is a
single tier-table edit + snapshot regeneration + public declaration.
It is NOT a re-implementation of the analyzer; the analyzer's detection
logic is unchanged; only the tier classification of its output changes.
Reuse: existing PARITY ceremony procedure; existing snapshot regeneration
mechanism; existing tier-table.
Stem extraction principle: applies to the ceremony itself --
decomposition precedes inspection. The ceremony breaks into (a) declare
change, (b) regenerate snapshots, (c) publicly announce, (d) update
migration note.
Dependencies permitted: none new.
Dependencies prohibited: any silent-snapshot-update tooling. The
ceremony must be EXPLICIT in PARITY.md.
Patent invariant clause: tier reclassification is ADDITIVE-permissible
under the §7 patent-invariant rules (tier table extension is not
modification of verdict aggregator's five-verdict structure).
Cow Episode anchor: do NOT silently update reference snapshots. The
parity-break MUST be publicly declared per the verse 2:159 anti-
concealment binding. If you find yourself running `pytest --update-
snapshots` without an accompanying PARITY.md declaration entry, STOP.

Step 4 -- Maliki Yawm ad-Din (Deadline Awareness):
Time budget: 12 hours dispatch budget.
Deliver:
  (a) tounicode_anomaly tier reclassification 1 -> 2 in domain/cost_
      classes.py (or wherever the tier table lives).
  (b) PARITY.md parity-break ceremony entry: explicit declaration of
      the tier change, the rationale (false-positive class closure per
      Round 12 corrective), the migration note for downstream consumers.
  (c) Phase 0 fixture expected to_dict() snapshots updated; the update
      is the EXPLICIT consequence of the (a) reclassification.
  (d) QUESTIONS.md Q2 closure log entry.
  (e) CHANGELOG.md v1.3.0 entry: six-element finding format.
  (f) Migration note in MIGRATION.md (or README.md if no MIGRATION.md):
      downstream consumers reading v1.2.5 to_dict() must know about the
      tier change.
Skip rule: if budget exhausted before any deliverable lands, register as
v1.2.6 bridge-tag NO-OP (parity-break has no "partial" state -- either
the ceremony lands fully or it does not happen).

Step 5 -- Iyyaka Na'budu (Orientation Check):
Am I performing the tounicode_anomaly tier reclassification with public
ceremony, or am I reclassifying other mechanisms or modifying the
analyzer detection logic itself?
If I find myself touching mechanisms OTHER than tounicode_anomaly, or
modifying analyzer detection logic, I have drifted. Round 13 is the
tounicode_anomaly-specific parity-break.

Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution):
Priority order:
  (1) Verify tounicode_anomaly current tier and locus.
  (2) Declare parity-break in PARITY.md with rationale.
  (3) Update tier table; do NOT modify analyzer detection logic.
  (4) Regenerate Phase 0 snapshots; verify every divergence corresponds
      to the documented tier change and NO others.
  (5) Update QUESTIONS.md Q2 closure log.
  (6) Update CHANGELOG.md v1.3.0 entry.
  (7) Write migration note.
  (8) Run full test suite; PARITY must pass against bayyinah_v0 and
      bayyinah_v0_1 at v1.3.0 (the reclassification is APPLIED to all
      three reference implementations equivalently -- the PARITY anchor
      is the three-way byte-identity AFTER the reclassification, not
      against v1.2.5).
PMD v1.8 §3B.2 post-edit substrate-verification: every divergence in
the regenerated snapshots must correspond to the documented tier change
and NO others. If extraneous diff appears in any snapshot, STOP and
surface as F-PARITY-V130-NN.

Step 7 -- Sirat alladhina an'amta alayhim (Anti-Pattern Avoidance):
What has worked:
  - Five-place documentation discipline caught silent drift in three
    prior rounds.
  - Explicit ceremonies (Round 12 RETIREMENT_LEDGER entry) prevent
    downstream confusion about what changed and why.
What has failed:
  - Silent snapshot updates (`pytest --update-snapshots` without an
    accompanying declaration) historically caused PARITY drift that
    surfaced only on the next release cycle. Do NOT silently update.
What has been tried and abandoned:
  - Bundling multiple tier reclassifications into one release (it
    confused downstream migration). Each parity-break is its own
    release per discipline.
The Cow Episode (v1.3.0-specific): do NOT silently update reference
snapshots; the parity-break MUST be publicly declared per the verse
2:159 anti-concealment binding. If you find yourself updating
snapshots without writing the PARITY.md ceremony entry FIRST, STOP.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.2.3 Deliverable map, §3.2.4 Code-touch surface, §3.2.5 Release-gate, §3.2.6 Cross-rotation

| Deliverable | Substrate | Acceptance |
|---|---|---|
| tier reclassification | tier table (likely `domain/cost_classes.py`) | additive entry, NOT removal |
| PARITY.md ceremony | `PARITY.md` | explicit declaration, rationale, migration note |
| Phase 0 snapshots regenerated | `tests/fixtures/` or snapshot dir | divergences correspond ONLY to the tier change |
| QUESTIONS.md Q2 closure | `QUESTIONS.md` | follows existing closure format |
| MIGRATION/README note | `MIGRATION.md` or `README.md` | downstream-visible |

Code-touch: ADD entries; MODIFY tier table and snapshot expected values; NO touch to analyzer detection logic, no touch to patent-invariant surfaces.

Release-gate (HEAVY per source §6):
- [ ] PARITY.md declaration present and locus-clear
- [ ] All snapshot divergences traceable to the declared tier change
- [ ] No undocumented divergences
- [ ] Full pytest pass
- [ ] PARITY pass across `bayyinah_v0` + `bayyinah_v0_1` + current at v1.3.0
- [ ] Falsification block per source §11: zero undocumented divergences in Phase 0 fixture `to_dict()`

Cross-rotation: **HEAVY** -- two distinct vendor backbones for substrate-mutation verification (e.g., Anthropic Claude + Google Gemini, plus OpenAI ChatGPT + Perplexity as second backbone) + three-vendor continuity.

---

### §3.3 -- v1.4.0 (Round 14, Verse 2:286)

#### §3.3.1 Release header

**Q3 + Q4 closure: `compute_muwazana_score` shape pin + `scan_incomplete` clamp semantics.** The verse names capacity bounds; the score function and clamp semantics are the capacity-respecting honest-bound mechanism.

#### §3.3.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:286: "Allah does not charge a soul except [with that within] its capacity."

The score function and clamp semantics implement capacity-bounded honest
reporting.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v1.4.0 (Round 14).
Authority source: live repo at v1.3.0 + FRAMEWORK.md + PARITY.md +
NAMING.md + RETIREMENT_LEDGER.md + PMD v1.8 + CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then pin `compute_
muwazana_score` shape (Claim 8) and `scan_incomplete` clamp semantics.
Scope: (a) `compute_muwazana_score` shape pinned with documented
monotonicity, boundary conditions, rounding tolerance per Claim 8;
(b) `scan_incomplete` clamp semantics documented in docs/score.md;
(c) `apply_scan_incomplete_clamp` contract pinned with regression tests;
(d) Q3 + Q4 closure logs in QUESTIONS.md; (e) five-place doc pattern.
Out of scope: new verdict types; new score-function variants; new clamp
behaviors.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.3.0 with the tounicode_anomaly tier
reclassification shipped and snapshots updated. PARITY holds.
Stable: all v1.3.0 substrate; verdict aggregator 150 with five verdicts;
witness emitter 160.
Not yet built: pinned contract for `compute_muwazana_score` shape;
pinned contract for `scan_incomplete` clamp semantics; regression tests
that fail loudly if either shape mutates silently in future releases.
Available for composition: existing `compute_muwazana_score`
implementation; existing `scan_incomplete` and `apply_scan_incomplete_
clamp` code paths; existing test infrastructure.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: before Step 6,
empirically verify (a) `compute_muwazana_score` current behavior on
canonical fixture inputs by running `pytest tests/ -k muwazana -v`;
(b) `scan_incomplete` current behavior similarly; (c) any existing
documentation in docs/ that may already cover this contract.

Step 3 -- Ar-Rahman ar-Rahim:
MDL governs: the contract documents WHAT the function currently does;
it does NOT redesign the function. Pin first, redesign later.
Reuse: existing score function; existing test fixtures.
Patent invariant clause: `compute_muwazana_score` shape pinning is
ADDITIVE-permissible (documenting existing behavior, not modifying it).
Modification of the function itself would touch verdict aggregator 150
and escalates to counsel.
Cow Episode anchor: do NOT specify all possible score-function edge
cases preemptively. Pin the contract against the EXISTING fixture set
first; expand coverage in subsequent rounds only on empirical need.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 14 hours.
Deliver:
  (a) docs/score.md: `compute_muwazana_score` shape contract +
      `scan_incomplete` clamp semantics contract.
  (b) tests/contracts/test_muwazana_score_shape.py: regression tests
      pinning monotonicity, boundary conditions, rounding tolerance.
  (c) tests/contracts/test_scan_incomplete_clamp.py: regression tests
      pinning `apply_scan_incomplete_clamp` behavior.
  (d) Q3 + Q4 closure logs in QUESTIONS.md.
  (e) CHANGELOG.md v1.4.0 entry: six-element format.
Skip rule: if budget exhausted at item (a) + (b), ship as v1.4.0 with
(c) partial; register the gap as v1.4.1 bridge-tag work.

Step 5 -- Iyyaka Na'budu:
Am I pinning the EXISTING contract, or am I adding new verdict types or
new score-function variants?
If I find myself adding verdict types or variants, I have drifted. Q3+Q4
are SHAPE closure of EXISTING behavior, not scope expansion.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Empirically map `compute_muwazana_score` current behavior on
      canonical fixtures. Record monotonicity, boundary conditions,
      rounding tolerance.
  (2) Write docs/score.md describing the mapped contract.
  (3) Write tests/contracts/test_muwazana_score_shape.py pinning the
      contract.
  (4) Repeat (1)-(3) for `scan_incomplete` clamp semantics.
  (5) Q3 + Q4 closure logs in QUESTIONS.md.
  (6) CHANGELOG.md.
  (7) Full pytest pass; PARITY pass; no shape modifications.
PMD v1.8 §3B.2 post-edit substrate-verification: the new contract tests
must FAIL if the score function or clamp semantics is mutated, and PASS
on the current implementation. Run both proofs.

Step 7 -- Sirat alladhina an'amta alayhim:
What has worked:
  - Contract tests caught silent drift in three prior rounds (find
    in CHANGELOG for v1.1.0 + v1.2.0 references).
What has failed:
  - Pre-specifying every possible edge case in contract tests produced
    brittle test suites that fail on benign refactors. Pin the
    OBSERVED behavior, not the hypothetical edge case.
The Cow Episode (v1.4.0-specific): do NOT specify all possible score-
function edge cases preemptively; pin the contract against the
existing fixture set first.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.3.3-§3.3.6 (PRODUCER reference)

Deliverable map: docs/score.md, two contract test files, QUESTIONS.md updates, CHANGELOG.md.
Code-touch: ADD docs and tests; NO modification of score function or clamp logic.
Release-gate: STANDARD. Falsification per source §11: any subsequent round modifying `compute_muwazana_score` without explicit parity-break ceremony triggers regression. Threshold: zero silent modifications.
Cross-rotation: STANDARD. Pre-dispatch four-vendor + post-ship three-vendor continuity.

---

### §3.4 -- v1.5.0 (Round 15, Verse 2:32)

#### §3.4.1 Release header

**Q1 closure: `KNOWN_LIMITS.md` authoring.** Documentation-only release declaring honest knowledge bounds of v1.5 substrate.

#### §3.4.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:32: "They said, 'Exalted are You; we have no knowledge except
what You have taught us. Indeed, it is You who is the Knowing, the Wise.'"

KNOWN_LIMITS.md is the honest declaration of knowledge bounds.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v1.5.0 (Round 15).
Authority source: live repo at v1.4.0 + all prior discipline documents +
PMD v1.8 + CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then author
KNOWN_LIMITS.md enumerating known limitations of v1.5 substrate.
Scope: (a) KNOWN_LIMITS.md enumerating detector-gap classes, format-
coverage holes, audit-class boundaries observed empirically through
v1.4.0; (b) Q1 closure log; (c) docs/principles.md cross-reference
scaffolding for v1.9.0 (stub structure only).
Out of scope: any NEW substrate or detectors. v1.5 is DOCUMENTATION
declaring honest knowledge bounds.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.4.0 with `compute_muwazana_score` and
`scan_incomplete` contracts pinned.
Stable: all v1.4.0 substrate.
Not yet built: KNOWN_LIMITS.md.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: before Step 6,
enumerate ACTUAL detector gaps empirically by reviewing (a)
RETIREMENT_LEDGER.md for deferred work; (b) QUESTIONS.md for open
questions; (c) recent CHANGELOG entries for "future work" markers.
Do NOT include hypothetical limitations -- only empirically-observed
gaps.

Step 3 -- Ar-Rahman ar-Rahim:
MDL: each KNOWN_LIMITS entry is one paragraph naming the gap, the
substrate-of-record, the deferred-to release if applicable, and the
disposition (won't-fix, deferred, partial-coverage).
Cow Episode anchor: do NOT pad KNOWN_LIMITS.md with hypothetical
limitations. Enumerate ACTUAL gaps observed empirically. If you cannot
cite a CHANGELOG entry or QUESTIONS.md item for a limitation, do not
include it.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 8 hours.
Deliver:
  (a) KNOWN_LIMITS.md with empirically-grounded entries.
  (b) Q1 closure log in QUESTIONS.md.
  (c) docs/principles.md stub (structure only; full authoring is v1.9.0).
  (d) CHANGELOG.md v1.5.0 entry.

Step 5 -- Iyyaka Na'budu:
Am I authoring honest declarations of EMPIRICALLY-OBSERVED gaps, or am
I authoring new substrate or detectors?
If I find myself writing analyzer code, I have drifted. v1.5 is
DOCUMENTATION ONLY.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Enumerate detector-gap classes from RETIREMENT_LEDGER.md.
  (2) Enumerate format-coverage holes from CHANGELOG.md and QUESTIONS.md.
  (3) Enumerate audit-class boundaries (what audits do and don't catch).
  (4) Author KNOWN_LIMITS.md.
  (5) Q1 closure log.
  (6) docs/principles.md stub.
  (7) CHANGELOG.md.
PMD v1.8 §3A.6.4 WL24 Gemini monitoring active: KNOWN_LIMITS
enumerations are the substrate-misread class WL24 monitors. Cross-
rotation will catch any over-claim.

Step 7 -- Sirat alladhina an'amta alayhim:
What has worked: empirical grounding via CHANGELOG and RETIREMENT_LEDGER
references.
What has failed: hypothetical enumeration not grounded in observed
behavior.
The Cow Episode (v1.5-specific): do NOT pad. Empirical only.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.4.3-§3.4.6

Deliverables: KNOWN_LIMITS.md, Q1 closure, docs/principles.md stub, CHANGELOG.md entry.
Release-gate: LIGHT. No falsification block (documentation-only per source §11).
Cross-rotation: LIGHT -- one rotation; WL24 Gemini monitoring active.

---

### §3.5 -- v1.6.0 (Round 16, Verse 2:188)

#### §3.5.1 Release header

**Q-PRO-3 honest budget controller + Q-PRO-4 supply-chain disposition.**

#### §3.5.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:188: "And do not consume one another's wealth unjustly..."

The budget controller is honest accounting at the cost/forensic-mode level.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v1.6.0 (Round 16).
Authority source: live repo at v1.5.0 + all prior + PMD v1.8 +
CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then implement
Q-PRO-3 honest budget controller and Q-PRO-4 supply-chain scope
disposition.
Scope: (a) Q-PRO-3 honest budget controller per Claim 11: cost-class +
production/forensic mode; HONEST `scan_incomplete` semantics under
budget-bounded `tamyiz_verdict`; (b) Q-PRO-4: documented supply-chain
detection scope boundary in QUESTIONS.md; cross-reference to v3.0
SBOM/in-toto per ROADMAP_TO_V5.md; (c) five-place doc pattern.
Out of scope: implementing supply-chain detectors (v3.0+ territory);
adding new cost classes beyond production/forensic.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.5.0; KNOWN_LIMITS.md authored; score
function pinned at v1.4.0.
Stable: all v1.5.0 substrate; `compute_muwazana_score` shape pinned;
`scan_incomplete` clamp semantics pinned.
Not yet built: the budget controller; supply-chain disposition.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: verify
(a) existing cost-class definitions in domain/cost_classes.py;
(b) existing scan_service in application/; (c) any existing
budget-related code paths.

Step 3 -- Ar-Rahman ar-Rahim:
MDL: budget controller for the EXISTING two modes (production, forensic)
is sufficient. Do not anticipate cost classes that don't exist yet.
Patent invariant clause: budget controller is ADDITIVE to scan_service;
does not modify analyzer registry, verdict aggregator, or witness emitter.
Cow Episode anchor: do NOT specify budget controller for every
possible cost class. Honest budget for the existing two modes only.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 14 hours.
Deliver:
  (a) Budget controller implementation in application/ or domain/
      (additive module, not modification of scan_service signature).
  (b) `scan_incomplete` HONEST semantics under budget-bounded verdict.
  (c) Pinning tests for both modes (production, forensic).
  (d) Q-PRO-3 + Q-PRO-4 closure logs in QUESTIONS.md.
  (e) CHANGELOG.md v1.6.0 entry.
  (f) Cross-reference in QUESTIONS.md to ROADMAP_TO_V5.md §3.0 SBOM/
      in-toto for supply-chain future work.

Step 5 -- Iyyaka Na'budu:
Am I implementing the budget controller and dispositioning supply-chain
SCOPE, or am I implementing supply-chain DETECTORS?
If I find myself writing supply-chain detector code, I have drifted.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Implement budget controller for production mode.
  (2) Implement budget controller for forensic mode.
  (3) Implement HONEST `scan_incomplete` semantics under budget-bounded
      verdict (must not silently convert a budget-blocked scan into
      false `sahih`).
  (4) Pinning tests for both modes.
  (5) Q-PRO-3 closure log.
  (6) Q-PRO-4 closure log + ROADMAP cross-reference.
  (7) CHANGELOG.md.
PMD v1.8 §3B.2 post-edit substrate-verification.

Step 7 -- Sirat alladhina an'amta alayhim:
What has worked: minimal additive modules that bolt onto scan_service
without modifying its signature.
What has failed: signature changes to scan_service that broke PARITY
in prior rounds.
The Cow Episode (v1.6-specific): do NOT specify budget controller for
every possible cost class; the existing two modes are sufficient.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.5.3-§3.5.6

Deliverables: budget controller module, HONEST scan_incomplete semantics, pinning tests, two closure logs, CHANGELOG entry.
Release-gate: STANDARD. Falsification per source §11: differential test against v1.4 contract shows divergence in `apply_scan_incomplete_clamp` -> regression. Threshold: zero divergences.
Cross-rotation: STANDARD.

---

### §3.6 -- v1.7.0 (Round 17, Verse 2:148)

#### §3.6.1 Release header

**Q5 closure: default cross-modal correlation behavior per picket fence V32.**

#### §3.6.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:148: "For each [religious following] is a direction toward which
it faces. So race to [all that is] good."

Cross-modal correlation is alignment-checking across multiple substrate
modalities. The verse names directional alignment across multiple
directions.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v1.7.0 (Round 17).
Authority source: live repo at v1.6.0 + all prior + PMD v1.8 +
CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then implement default
cross-modal correlation analyzer per Claim 16 reduced-cardinality
projection.
Scope: (a) `cross_modal_correlation` analyzer in MECHANISM_REGISTRY per
Claim 16; (b) default behavior on the canonical PNG + PDF + DOCX
fixture trio; (c) five-place doc pattern.
Out of scope: correlation across modalities NOT in v1.2.4 substrate
(audio, video). Q5 is correlation across the EXISTING 13/23 substrate
kinds.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.6.0 with budget controller shipped.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: verify
(a) the canonical PNG + PDF + DOCX fixture trio in tests/fixtures/;
(b) existing analyzer module structure in analyzers/;
(c) MECHANISM_REGISTRY registration pattern from prior rounds.

Step 3 -- Ar-Rahman ar-Rahim:
MDL: implement the simplest cross-modal correlation that operates on
the canonical fixture trio. Do not enumerate every possible cross-modal
correlation pair.
Patent invariant clause: cross_modal_correlation analyzer is ADDITIVE
to analyzer registry; preserves dispatch shape.
Cow Episode anchor: do NOT enumerate every cross-modal correlation
pair; the canonical trio is sufficient as default.
PMD v1.8 §3A.7 render-vs-substrate discipline active: image-substrate
findings present as render artifacts in this release.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 14 hours.
Deliver:
  (a) `cross_modal_correlation` analyzer module.
  (b) MECHANISM_REGISTRY entry.
  (c) Pinning tests on the canonical PNG + PDF + DOCX trio.
  (d) Five-place doc pattern.
  (e) CHANGELOG.md v1.7.0 entry.

Step 5 -- Iyyaka Na'budu:
Am I implementing the default cross-modal correlation on the EXISTING
13/23 substrate kinds, or am I extending into modalities not in v1.2.4
substrate (audio, video)?
If I find myself adding audio or video correlation, I have drifted.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Implement cross_modal_correlation analyzer.
  (2) Register in MECHANISM_REGISTRY.
  (3) Pin behavior on canonical trio.
  (4) Five-place doc pattern.
  (5) CHANGELOG.md.

Step 7 -- Sirat alladhina an'amta alayhim:
The Cow Episode (v1.7-specific): do NOT enumerate every cross-modal
pair. Canonical trio only.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.6.3-§3.6.6

Deliverables: cross_modal_correlation analyzer + MECHANISM_REGISTRY entry + pinning tests + five-place doc + CHANGELOG.
Release-gate: STANDARD. Falsification per source §11: byte-comparable witnesses across reruns on same input. Threshold: zero divergences.
Cross-rotation: STANDARD; render-vs-substrate discipline active.

---

### §3.7 -- v1.8.0 (Round 18, Verse 2:282)

#### §3.7.1 Release header

**Q8 partial closure: differential testing matrix vs pdfid / oletools / yara / clamav.** First externally-comparable artifact. HEAVY audit-intensity (high blast radius).

#### §3.7.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:282: "O you who have believed, when you contract a debt for a
specified term, write it down... and let a scribe write [it] between
you in justice."

The differential matrix is just record-keeping between Bayyinah and
incumbent tools.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v1.8.0 (Round 18).
Authority source: live repo at v1.7.0 + all prior + PMD v1.8 +
CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then publish honest
differential testing matrix against pdfid, oletools, yara, clamav.
Scope: (a) Differential testing matrix in docs/benchmarks/diff_v1_8.md
with explicit matches/exceeds/falls-behind statements per fixture per
tool; (b) Q8 partial closure log; (c) five-place doc pattern per
matrix entry; (d) docs/benchmarks/diff_v1_8_gaps.md for cells not yet
covered.
Out of scope: extending matrix to experimental tools not in production
use. INCUMBENT production tools only.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.7.0 with cross_modal_correlation shipped.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: verify
(a) the canonical fixture corpus in tests/fixtures/; (b) the four
incumbent tools (pdfid, oletools, yara, clamav) are installable in
the test environment; (c) any existing benchmark scaffolding in docs/
benchmarks/.

Step 3 -- Ar-Rahman ar-Rahim:
MDL: each matrix cell is one tool x one fixture x one verdict. Empirically
run each tool; record the result; compare to Bayyinah's verdict.
Cow Episode anchor: do NOT exhaustively specify the matrix across every
possible fixture; cover the canonical fixture corpus and mark gaps as
future-work in docs/benchmarks/diff_v1_8_gaps.md.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 28 hours (HEAVY release; budget reflects four-tool x
canonical-corpus matrix authoring + verification time).
Deliver:
  (a) docs/benchmarks/diff_v1_8.md with matrix.
  (b) docs/benchmarks/diff_v1_8_gaps.md for uncovered cells.
  (c) Q8 partial closure log.
  (d) Five-place doc pattern per matrix entry.
  (e) CHANGELOG.md v1.8.0 entry.
  (f) Optionally: scripts/benchmarks/run_diff_v1_8.sh that reproduces
      every cell mechanically.

Step 5 -- Iyyaka Na'budu:
Am I building an HONEST differential matrix on incumbent production
tools, or am I padding the matrix with experimental tools or
hypothetical comparisons?
If I find myself benchmarking against tools NOT in production use, I
have drifted.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Install and verify the four incumbent tools.
  (2) Enumerate canonical fixture corpus to benchmark.
  (3) For each (tool, fixture) cell: run the tool, record the verdict.
  (4) For each (Bayyinah, fixture) cell: run Bayyinah, record the
      verdict.
  (5) Compose matrix in docs/benchmarks/diff_v1_8.md with explicit
      matches/exceeds/falls-behind labels per cell.
  (6) docs/benchmarks/diff_v1_8_gaps.md for uncovered cells.
  (7) Q8 closure log.
  (8) CHANGELOG.md.
PMD v1.8 §3B.2 post-edit substrate-verification: every matrix cell must
be mechanically reproducible by a fresh-instance auditor running the
named tool against the named fixture. Provide the reproduction script
in scripts/benchmarks/ if helpful.

Step 7 -- Sirat alladhina an'amta alayhim:
What has worked: explicit mechanical reproduction scripts in prior
benchmark work caught cherry-picking patterns before merge.
What has failed: matrix cells claimed without empirical verification
(hand-waved comparisons that did not survive cross-rotation review).
The Cow Episode (v1.8-specific): do NOT exhaustively specify; cover the
canonical corpus and mark gaps openly.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.7.3-§3.7.6

Deliverables: differential matrix, gaps file, optional reproduction scripts, Q8 closure, five-place per cell, CHANGELOG.
Release-gate: **HEAVY**. Falsification per source §11: any cell that a fresh-instance audit-author cannot reproduce. Threshold: zero unreproducible cells.
Cross-rotation: **HEAVY** -- two distinct vendor backbones for matrix verification + three-vendor continuity.

---

### §3.8 -- v1.9.0 (Round 19, Verse 2:269)

#### §3.8.1 Release header

**Q10 closure: docs/principles.md framework-free engineering principles.** Documentation-only release.

#### §3.8.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:269: "He gives wisdom to whom He wills..."

docs/principles.md is the framework-free transmission.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v1.9.0 (Round 19).
Authority source: live repo at v1.8.0 + all prior + PMD v1.8 +
CODING_STRATEGY.
Optimization function: serve the purpose hierarchy then author docs/
principles.md that describes Bayyinah's structural-honesty discipline
WITHOUT requiring PMD vocabulary, audit framework vocabulary, or
Quranic vocabulary to consume.
Scope: (a) docs/principles.md transmitting empirically-validated cycles
11-18 lessons in framework-free language; (b) Q10 closure log.
Out of scope: padding with universal-engineering-principle filler;
inventing principles not empirically validated.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.8.0 with differential matrix shipped.
docs/principles.md stub structure from v1.5.0 available.
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: verify
(a) the v1.5.0 docs/principles.md stub; (b) empirical lessons in
CHANGELOG cycles 11-18.

Step 3 -- Ar-Rahman ar-Rahim:
MDL: each principle is one paragraph naming an empirical observation
from cycles 11-18 and translating it into framework-free engineering
language.
Cow Episode anchor: do NOT pad with universal engineering filler.
Transmit ONLY what cycles 11-18 empirically validated.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 8 hours.
Deliver:
  (a) docs/principles.md framework-free principles.
  (b) Q10 closure log.
  (c) CHANGELOG.md v1.9.0 entry.

Step 5 -- Iyyaka Na'budu:
Am I writing framework-FREE prose that an engineer without PMD/audit
framework/Quranic vocabulary can consume, or am I writing PMD section
numbers and audit framework vocabulary?
If I find myself citing PMD §3A.1, PARITY.md, or RETIREMENT_LEDGER in
the body of principles.md, I have drifted. Cross-references go in a
separate appendix only.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Review CHANGELOG cycles 11-18 for empirical lessons.
  (2) Translate each lesson into framework-free engineering language.
  (3) Author docs/principles.md.
  (4) Q10 closure log.
  (5) CHANGELOG.md.

Step 7 -- Sirat alladhina an'amta alayhim:
The Cow Episode (v1.9-specific): do NOT pad. Empirical only.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.8.3-§3.8.6

Deliverables: docs/principles.md, Q10 closure, CHANGELOG.
Release-gate: LIGHT. No falsification block.
Cross-rotation: LIGHT -- one rotation; WL24 Gemini monitoring active.

---

### §3.9 -- v2.0.0 (Round 20, Verse 2:281)

#### §3.9.1 Release header

**Q9 closure: external human audit + recursive self-verification + commercialization gate.** Final accounting before the v1.x arc closes. HEAVY audit-intensity; cross-rotation includes external human auditor + four-vendor on published artifacts.

#### §3.9.2 Dispatch packet

```
Bismillah ar-Rahman ar-Rahim.

Quran 2:281: "And fear a Day when you will be returned to Allah. Then
every soul will be compensated for what it earned..."

v2.0.0 is the final accounting before the v1.x arc closes.

Step 1 -- Bismillah:
We are building Bayyinah Integrity Scanner v2.0.0 (Round 20).
Authority source: live repo at v1.9.0 + all prior + PMD v1.8 +
CODING_STRATEGY + the provisional patent claim space (System 100 /
Method 200; Claims 1-20).
Optimization function: serve the purpose hierarchy then close Q9 via
(a) external human audit commissioned, scoped, dispatched, findings
absorbed; (b) recursive self-application per Claim 15: v2.0.0 substrate
scanned by v1.9.0 with verdict `sahih`; (c) commercialization gate
package complete.
Scope: (a) external auditor engagement + findings absorption; (b)
recursive self-application + foreign-instance scan ledger filed;
(c) commercialization gate: SECURITY.md, BOUNTY.md, ANNOUNCEMENT.md,
LICENSE (confirm Apache 2.0), CONTRIBUTING.md (verify present), patent
invariant clause re-affirmed in repo prose, three case studies in
docs/v2.0/case_studies/; (d) Q9 closure log.
Out of scope: retroactively rewriting v1.5 KNOWN_LIMITS.md, v1.8
differential matrix, or v1.9 principles.md. v2.0 is FINAL accounting
(verse 2:281), not retroactive rewriting.
Out of scope: extending commercialization gate scope to v3.0 SDK
ecosystem or v4.0 sectoral packs; those are explicitly future-work
registered in ROADMAP_TO_V5.md.

Step 2 -- Alhamdulillah:
Current state: Bayyinah at v1.9.0 with framework-free principles
shipped. All prior closures intact: Round 11 (v1.2.5); tounicode_anomaly
tier reclassification (v1.3.0); score-shape pin + clamp semantics
(v1.4.0); KNOWN_LIMITS.md (v1.5.0); budget controller + supply-chain
disposition (v1.6.0); cross_modal_correlation (v1.7.0); differential
matrix (v1.8.0); principles.md (v1.9.0).
PMD v1.8 §3A.3 pre-dispatch substrate-actual-verification: verify
(a) all v1.x closures present at HEAD; (b) PARITY holds across all
three reference scanners at v1.9.0; (c) external auditor candidate
identified and scoped per ROADMAP_TO_V5.md §9 risk register (this is
project-lead disposition; cowork executes after the disposition is
recorded).

Step 3 -- Ar-Rahman ar-Rahim:
MDL: the commercialization gate is six artifacts (SECURITY.md, BOUNTY.md,
ANNOUNCEMENT.md, LICENSE, CONTRIBUTING.md, three case studies). The
external audit is one engagement. Recursive self-application is one
scan invocation. Do not expand.
Patent invariant clause RE-AFFIRMED in repo prose at v2.0: the five
surfaces are still IMMUTABLE; v2.0 ships with patent-invariant integrity
intact. Any v3.0 work that touches them goes through counsel.
Cow Episode anchor: do NOT extend gate scope beyond the six artifacts +
external audit + recursive self-application + Q9 closure log. v3.0 SDK
and v4.0 sectoral are future-work.

Step 4 -- Maliki Yawm ad-Din:
Time budget: 40 hours (HEAVY; budget reflects multi-track
coordination: external auditor + recursive self-application + six
artifact authoring).
Deliver:
  (a) External auditor engagement: SOW signed, scope locked, findings
      absorbed in CHANGELOG/RETIREMENT_LEDGER as F-EXT-AUDIT-NN.
  (b) Recursive self-application: v2.0.0 release candidate substrate
      scanned by v1.9.0; foreign-instance scan ledger filed in
      docs/v2.0/recursive_self_scan.md with verdict `sahih`; if non-
      `sahih`, BLOCK release and absorb finding.
  (c) SECURITY.md (vulnerability disclosure policy).
  (d) BOUNTY.md (bug bounty program scaffolding; project-lead
      disposition on funding scope).
  (e) ANNOUNCEMENT.md (commercialization announcement; project-lead
      reviews before publication).
  (f) CONTRIBUTING.md (verify present; update if needed).
  (g) Three case studies in docs/v2.0/case_studies/ (each ~1,500-3,000
      words; real Round 11/12 closure narratives or anonymized
      adversarial fixture analyses).
  (h) Q9 closure log.
  (i) CHANGELOG.md v2.0.0 entry: six-element format; references all
      v1.x closures; declares v2.0 the v1.x arc closure.
  (j) v2.0.0 git tag pushed.

Step 5 -- Iyyaka Na'budu:
Am I completing the FINAL accounting (verse 2:281) on the v1.x arc, or
am I retroactively rewriting earlier releases or extending into v3.0
scope?
If I find myself rewriting v1.5 KNOWN_LIMITS.md or extending into v3.0
SDK work, I have drifted.

Step 6 -- Ihdina as-Sirat al-Mustaqim:
Priority order:
  (1) Verify all v1.x closures intact at HEAD.
  (2) PARITY pass across three reference scanners at v1.9.0.
  (3) Dispatch external auditor (project-lead engagement; cowork
      receives findings).
  (4) Recursive self-application: scan v2.0.0 RC with v1.9.0;
      file ledger.
  (5) Author SECURITY.md, BOUNTY.md, ANNOUNCEMENT.md.
  (6) Verify CONTRIBUTING.md and LICENSE.
  (7) Author three case studies.
  (8) Q9 closure log.
  (9) CHANGELOG.md v2.0.0 entry.
  (10) PARITY re-pass with v2.0.0 included as fourth reference
       implementation (or verify v2.0.0 reduces to v1.9.0 modulo
       commercialization-gate artifacts which are NOT in the scan
       substrate path).
  (11) Push v2.0.0 git tag.
PMD v1.8 §3B.2 post-edit substrate-verification on every artifact.

Step 7 -- Sirat alladhina an'amta alayhim:
What has worked: explicit closure ledgers (Round 11/12) caught silent
drift downstream.
What has failed: bundling new substrate work into a release-gate
publication (the gate is artifact-emission, not new-substrate).
The Cow Episode (v2.0-specific): do NOT extend gate scope to v3.0 SDK
ecosystem or v4.0 sectoral packs. v2.0 is the v1.x arc closure.
Closing dua: Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

Begin.
```

#### §3.9.3-§3.9.6

Deliverables: external audit completion, recursive self-application ledger, six commercialization-gate artifacts, three case studies, Q9 closure log, CHANGELOG v2.0.0 entry, git tag push.
Release-gate: **HEAVY**. Falsification per source §11: (a) recursive self-application non-`sahih` verdict, (b) external auditor unabsorbed finding at release tag, (c) commercialization gate missing any element. Threshold: zero failures.
Cross-rotation: **HEAVY** -- two distinct vendor backbones + three-vendor continuity + external human auditor + four-vendor on published artifacts (CHANGELOG, README, SECURITY.md, ANNOUNCEMENT.md).

---

## §4 Cross-rotation matrix (per release)

| Release | Audit-intensity | Pre-dispatch (fresh) | Post-ship (continuity) |
|---|---|---|---|
| v1.2.5 | STANDARD | Claude + ChatGPT + Gemini + Perplexity | ChatGPT cont. + Perplexity cont. + Gemini cont. |
| v1.3.0 | HEAVY | (Claude + Gemini) + (ChatGPT + Perplexity) two backbones | three-vendor continuity |
| v1.4.0 | STANDARD | four-vendor fresh | three-vendor continuity |
| v1.5.0 | LIGHT | one rotation; WL24 Gemini monitoring | (none required) |
| v1.6.0 | STANDARD | four-vendor fresh | three-vendor continuity |
| v1.7.0 | STANDARD | four-vendor fresh; render-vs-substrate discipline active | three-vendor continuity |
| v1.8.0 | HEAVY | two backbones | three-vendor continuity |
| v1.9.0 | LIGHT | one rotation; WL24 Gemini monitoring | (none required) |
| v2.0.0 | HEAVY | two backbones + external human auditor | three-vendor continuity + four-vendor on published artifacts |

Producer-discount per PMD v1.8 §3A.12.4: when Claude is the producer-instance for the release, Claude is excluded from the auditor pool for that release. Claude is trusted on mechanical reproducible checks (byte/hash diffs, grep-for-residual-loci, prose-to-spec completeness diffs, locus-presence) for cross-confirmation only; binding-for-termination findings come from non-Claude rotations.

---

## §5 What this document does NOT replace

- The source `CODING_STRATEGY_v1_2_4_to_v2_0.md` v1.0 remains canonical methodology authority.
- `STRATEGY_TO_V2.md` remains authoritative for commit-by-commit task graphs.
- `FRAMEWORK.md`, `PARITY.md`, `NAMING.md`, `RETIREMENT_LEDGER.md`, `QUESTIONS.md`, `HANDOFF.md` in the live repo remain authoritative for their respective disciplines.
- This document is the EXECUTABLE adaptation only.

---

## §6 Closing

> Wa fawqa kulli dhi 'ilmin 'alim.
> And above every possessor of knowledge is one more knowing.
> Yusuf 12:76

The structural-honesty thesis applies recursively to this document: its dispatch packets must produce, when cowork executes them against the verified substrate, the deliverables and release-gate-pass states the surface claims describe. Where divergence surfaces, it is itself a finding, dispositioned per the six-element format and absorbed per A1 corrigendum chain into a v1.1 of this executable strategy.

The cowork-executable adaptation is preliminary. Per PMD v1.8, after v1.2.5 dispatches and ships, a retrospective review of THIS document against the as-shipped v1.2.5 substrate is warranted to calibrate subsequent release packets.

> Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
> Our Lord, accept this from us. Indeed, You are the All-Hearing, the All-Knowing.

La hawla wa la quwwata illa billah.

Bismillah.

---

# Bismillah ir-Rahman ir-Rahim
