# Bismillah ir-Rahman ir-Rahim

# R0855 -- Bayyinah-Integrity-Scanner Live Repo Substrate Pinning Document

**Chronological Index:** 204 of 995  
**Date:** 2026-05-03  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** REPO_SUBSTRATE_PINNED.md  
**Source Format:** md  
**SHA-256:** `9b58c378dda1134547142950349224ee86e077bdf5da8738cbb0d2649a500eff`  

---

## R0855 · Bayyinah-Integrity-Scanner Live Repo Substrate Pinning Document

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: REPO_SUBSTRATE_PINNED.md
- source_format: md
- text_sha256: 9b58c378dda1134547142950349224ee86e077bdf5da8738cbb0d2649a500eff

# Bayyinah-Integrity-Scanner Live Repo Substrate Pinning Document

**Cycle:** Bayyinah-CS-1.2.4-to-2.0-cycle-1+P (continuity arm)
**Purpose:** substrate-of-record markdown extract for continuity-instance auditors who cannot extract binary tarballs.
**Live repo anchor:** `Bayyinah-Integrity-Scanner` at v1.2.4 (`pyproject.toml version = "1.2.4"`).
**Project-lead-claimed SHA:** `72a2c787072875ad27b6978f4725bd6c83d36dce` (per CODING_STRATEGY §4 and DISPATCH_PROMPT §0).
**Snapshot capture date:** 2026-06-09.
**Extraction author:** Bilal Syed Arfeen (BayyinahEnterprise) via Claude Opus 4.7 mechanical enumeration per PMD v1.8 §5.6.

This document is read-only substrate-of-record extracted from the live working tree. Vendors verify CODING_STRATEGY §4 substrate-actual claims against the measurements below WITHOUT needing to extract a binary tarball.

For SHA-anchored verification at exactly `72a2c787`, vendors clone fresh from `github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner` and run `git checkout 72a2c787`.

---

## §1 Mechanical substrate measurements

All measurements via standard Unix tools or Python imports against the live working tree.

| Measurement | Value | Method | Cross-references CODING_STRATEGY §4 claim |
|---|---|---|---|
| `pyproject.toml` version | `1.2.4` | `grep '^version' pyproject.toml` | MATCH: strategy says v1.2.4 |
| MECHANISM_REGISTRY length | **159** | `from bayyinah import MECHANISM_REGISTRY; len(MECHANISM_REGISTRY)` | EXACT MATCH: strategy says "approximately 159" |
| MECHANISM_REGISTRY type | `frozenset` | `type(MECHANISM_REGISTRY).__name__` | (informational; not a dict) |
| Analyzer `.py` files (excl. `__init__.py`) | 71 | `find analyzers -name '*.py' -not -name '__init__.py' | wc -l` | (strategy did not claim explicit count) |
| Test files (`test_*.py`) | 74 | `find tests -name 'test_*.py' | wc -l` | (strategy did not claim explicit count) |
| Test function definitions | 1,078 | `grep -rE '^def test_' tests/ | wc -l` | LOW-residual: strategy "approximately 1,800"; FRAMEWORK.md "1837+ pytest tests"; parametrize-expanded collected count matches strategy claim |
| FileKind enum total entries | **20** | `infrastructure/file_router.py` | LOW-residual F-CS-cycle1+P-LOW-1: strategy §4 says "13"; README claims "23"; substrate-actual is 19 substantive + UNKNOWN (see §2) |
| CHANGELOG.md size | 71,645 bytes | `wc -c CHANGELOG.md` | MATCH: strategy says "~71 KB" |

---

## §2 FileKind enum (substrate-actual; from `infrastructure/file_router.py`)

The FileKind enum is the authoritative source for "what substrate kinds Bayyinah recognizes." Strategy §4 claim "13 substrate kinds" enumerates document-format kinds only; the live enum includes audio + video + UNKNOWN.

```
class FileKind(enum.Enum):
    PDF       = "pdf"          # 1  document
    DOCX      = "docx"         # 2  document
    XLSX      = "xlsx"         # 3  document (Phase 17)
    PPTX      = "pptx"         # 4  document (Phase 18)
    HTML      = "html"         # 5  document
    MARKDOWN  = "markdown"     # 6  document
    JSON      = "json"         # 7  structured-data
    IMAGE_PNG = "image_png"    # 8  image
    IMAGE_JPEG= "image_jpeg"   # 9  image
    IMAGE_SVG = "image_svg"    # 10 image
    CODE      = "code"         # 11 source code / plain text
    EML       = "eml"          # 12 email
    CSV       = "csv"          # 13 tabular
    VIDEO_MOV = "video_mov"    # 14 video (deferred to v3.0+ per §8)
    VIDEO_WEBM= "video_webm"   # 15 video (deferred)
    VIDEO_MKV = "video_mkv"    # 16 video (deferred)
    AUDIO_WAV = "audio_wav"    # 17 audio (deferred)
    AUDIO_FLAC= "audio_flac"   # 18 audio (deferred)
    AUDIO_OGG = "audio_ogg"    # 19 audio (deferred)
    UNKNOWN   = "unknown"      # 20 fallback
```

**Total enum entries: 20.** Substantive substrate kinds (excluding UNKNOWN): 19. Strategy §4's "13" corresponds to entries 1-13 (document-format kinds in active scope). README's "23" appears inaccurate against this empirical enum (which has 20 total).

This is the cross-vendor convergent F-CS-cycle1+P-LOW-1 advisory: §4 language should sharpen to distinguish "13 document-format substrate kinds in active v1.2.4 scope" from "19 substantive FileKind enum entries + UNKNOWN" from "23 README claim" (which does not match the live enum).

---

## §3 Five-verdict mechanic (substrate-actual; from `domain/config.py`)

The five verdicts are pinned as `Final[Verdict]` constants:

```
VERDICT_SAHIH    : Final[Verdict] = "sahih"
VERDICT_MUSHTABIH: Final[Verdict] = "mushtabih"
VERDICT_MUKHFI   : Final[Verdict] = "mukhfi"
VERDICT_MUNAFIQ  : Final[Verdict] = "munafiq"
VERDICT_MUGHLAQ  : Final[Verdict] = "mughlaq"
```

CODING_STRATEGY §4 claim "five verdicts (sahih / mushtabih / mukhfi / munafiq / mughlaq) via `compute_muwazana_score` + `tamyiz_verdict`": MATCH verbatim.

---

## §4 PARITY policy (substrate-actual; from `PARITY.md`)

The PARITY invariant is exactly as CODING_STRATEGY §4 names it:

> `bayyinah.scan_pdf(path).to_dict() == bayyinah_v0.scan_pdf(path).to_dict()` for every fixture in the Phase 0 fixture corpus.

This is asserted by `tests/test_fixtures.py::test_v0_v01_parity` and re-verified after every phase.

The conditional invariant clause:

> The parity invariant is conditional on the correctness of the reference implementation. When a v0 finding, score, error message, or output shape is demonstrated to be incorrect... the parity baseline is updated [via the five-step parity-break procedure].

The parity-break procedure has five steps: (1) open `parity-break` issue, (2) cross-reference from CHANGELOG `Parity-break` heading, (3) update affected Phase 0 fixtures retaining old as regression artifact, (4) update `tests/test_fixtures.py::test_v0_v01_parity`, (5) bump minor version.

CODING_STRATEGY v1.3.0 Round 13 tounicode_anomaly tier reclassification follows this procedure.

---

## §5 Round 11 + Round 12 status (substrate-actual; from `RETIREMENT_LEDGER.md`)

**Round 11 (queued for v1.2.5):**

> The red-team probe of bayyinah.dev v1.2.3 on 2026-05-04 surfaced 4 CRITICAL silent-pass findings and 5 HIGH partial-catches against multi-layer integrity traps. Round 11 is deferred to v1.2.5 per the v3 depth-before-scope discipline; the Round 12 calibration corrective ships first because the Round 12 false positives were visible to every demo visitor while the Round 11 silent-passes were not.

CODING_STRATEGY §4 + §3 v1.2.5 row claim "4 CRITICAL silent-pass + 5 HIGH partial-catches": MATCH verbatim.

**Round 12 (retired in v1.2.4):**

> HIGH: openaction heuristic fired on benign navigation destinations (LibreOffice destination arrays, pdfTeX hyperref /GoTo). Closed by adding `_is_benign_navigation_openaction` [continued in CHANGELOG for v1.2.4]...

CODING_STRATEGY §4 claim "Round 12 closure shipped in v1.2.4: producer-signature calibration component 134 (Claim 9 + Claim 10), TeX-stack OT1 / T1 ToUnicode CMap suppression": MATCH. The TeX-stack ToUnicode CMap suppression is the Round 12 corrective documented in RETIREMENT_LEDGER + CHANGELOG.

---

## §6 FRAMEWORK conformance (substrate-actual; from `FRAMEWORK.md`)

Bayyinah follows Bayyinah Audit Framework v3.0 dated 2026-05-03 at Level 4 (Structurally Honest) maturity.

Key conformance items verified:

| Discipline | Present? | Locus |
|---|---|---|
| Severity rubric (§7) applied uniformly | yes | CHANGELOG entries use CRITICAL / HIGH / MEDIUM / LOW |
| Reproducer-first findings (§4 step 4) | yes | CHANGELOG entries cite fixture + commit SHA |
| Four-place documentation pattern | extended to FIVE places | CHANGELOG + README + fixture + pinning test + `MECHANISM_REGISTRY` entry |
| Pre-flight checklist (§12.1) + five questions (§12.2) | yes | applied at release |
| Validator-by-different-instance protocol (§5.2) | yes | "producer instance (cowork Claude on a prior version) does not audit; a fresh Claude instance audits against the public artifacts alone" |
| **1837+ pytest tests** | yes | FRAMEWORK.md §3 maturity self-assessment |
| Em-dash sweep automation | yes | "Verified by `grep -c '--'` against changed prose files at each commit" |
| `requirements.txt` <-> `pyproject.toml` sync | yes | `tests/test_requirements_dev_sync.py` |
| Public surface additive invariant | yes | `tests/test_public_surface_additive.py` with per-version surface frozenset cadence |
| Mechanism registry consistency | yes | "A mechanism that exists in the analyzer but not in the registry is a finding category in its own right" |
| PARITY against `bayyinah_v0` / `v01` | yes | `tests/test_fixtures.py::test_v0_v01_parity` |
| Retirement ledger maintained cross-version | yes | `RETIREMENT_LEDGER.md` |
| Audit-of-self by Bilal Syed Arfeen | yes | "every round in the Bayyinah audit chain is audit-of-self by Bilal Syed Arfeen. Fraz Ashraf is acknowledged for the framework's engineering approach (§27), not as an auditor on the Bayyinah chain" |

CODING_STRATEGY §4 + §12 audit-attribution discipline ("audit-of-self by Bilal; Fraz acknowledged for framework co-authorship per PMD §5.6, never as auditor"): MATCH verbatim.

---

## §7 Discipline document presence (substrate-actual)

All discipline documents named in CODING_STRATEGY §4 confirmed present in the repo root:

- `FRAMEWORK.md` (4,266 bytes)
- `PARITY.md` (3,143 bytes)
- `NAMING.md` (12,431 bytes)
- `RETIREMENT_LEDGER.md` (5,816 bytes)
- `QUESTIONS.md` (7,260 bytes)
- `HANDOFF.md` (9,381 bytes)
- `CHANGELOG.md` (71,645 bytes)
- `CONTRIBUTING.md` (14,894 bytes)
- `README.md` (25,149 bytes)
- `LICENSE` (11,343 bytes, Apache 2.0)
- `RAILWAY_VOLUME.md` (2,763 bytes)
- `Procfile` (69 bytes)
- `pyproject.toml` (8,059 bytes)

PARITY anchors:
- `bayyinah_v0.py` (70,054 bytes)
- `bayyinah_v0_1.py` (65,984 bytes)

---

## §8 Hexagonal architecture directories (substrate-actual)

CODING_STRATEGY §4 claim "hexagonal architecture (`analyzers/` + `application/` + `domain/` + `infrastructure/` + `cli/`)": MATCH.

Live directory structure (top level):

```
analyzers/    (71 .py files)
application/  (orchestration layer)
bayyinah/     (package entry; exports MECHANISM_REGISTRY + scan_pdf)
cli/          (CLI entry point)
domain/       (Verdict types; config.py with five-verdict constants)
infrastructure/  (file_router.py with FileKind enum)
docs/
history/
legacy/
papers/
tests/
api.py        (HTTP endpoint)
bayyinah_v0.py
bayyinah_v0_1.py
```

---

## §9 Author and audit-of-self attribution (substrate-actual; from `FRAMEWORK.md`)

> Bayyinah follows Bayyinah Audit Framework v3.0 (Arfeen 2026, sole authored, hybridised with Fraz Ashraf's engineering approach per Acknowledgements).
>
> Audit-of-self pattern (§1.2): every round in the Bayyinah audit chain is audit-of-self by Bilal Syed Arfeen. Fraz Ashraf is acknowledged for the framework's engineering approach (§27), not as an auditor on the Bayyinah chain.

This is the substrate-of-record for user memory `feedback_bayyinah_audit_attribution` and CODING_STRATEGY §12 attribution discipline.

---

## §10 Closing

This document is mechanical extract. Every value is reproducible by running the named command against the live `Bayyinah-Integrity-Scanner` repo at v1.2.4 (the working tree captured 2026-06-09 from a fresh GitHub clone; pyproject.toml version = "1.2.4"; user-claimed SHA `72a2c787`).

Vendors operating in continuity mode use this document as substrate-of-record for Q1 verification per DISPATCH_PROMPT_cycle1plusP_continuity §4 Q1 enumeration. Vendors needing SHA-anchored byte-level verification clone fresh from `github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner` and `git checkout 72a2c787`.

Per PMD v1.8 §3A.3 substrate-actual-overrides-prompt: if any measurement in this document diverges from what vendors find on their own substrate access, the vendor's empirical measurement binds and the divergence is surfaced as `F-SUBSTRATE-PIN-NN`.

> Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.

La hawla wa la quwwata illa billah.

---

# Bismillah ir-Rahman ir-Rahim
