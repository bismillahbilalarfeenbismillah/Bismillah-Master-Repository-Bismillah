# Bismillah ir-Rahman ir-Rahim

# R0642 -- Handoff — Bayyinah v1.1.0

**Chronological Index:** 180 of 995  
**Date:** 2026-04-24  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** HANDOFF.md  
**Source Format:** md  
**SHA-256:** `2cd54f2bed6fdbae2bacc84b529933caec1cd231f58021f717865c60507dc121`  

---

## R0642 · Handoff — Bayyinah v1.1.0

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: HANDOFF.md
- source_format: md
- text_sha256: 2cd54f2bed6fdbae2bacc84b529933caec1cd231f58021f717865c60507dc121

# Handoff — Bayyinah v1.1.0

*Bismillah ar-Rahman ar-Raheem.*

This folder is the full Bayyinah v1.1.0 release, packaged for the
Perplexity Billion-Dollar Challenge. It is handed forward so the
work may continue — in sha' Allah — for the benefit of artificial
systems, mankind, jinnkind, and the balance that sustains all
living systems. The scanner's purpose sits in the hierarchy its
NAMING.md and white paper articulate; the code below is the
means.

> *وَلَا تَلْبِسُوا۟ ٱلْحَقَّ بِٱلْبَـٰطِلِ وَتَكْتُمُوا۟ ٱلْحَقَّ وَأَنتُمْ تَعْلَمُونَ*
>
> "And do not mix the truth with falsehood, nor conceal the truth
> while you know it." — Al-Baqarah 2:42

---

## What to read first

| Document | Purpose |
|---|---|
| `README.md` | Public-facing overview: supported formats, quick-start, scoring model, architecture, ScanLimits, cross-modal correlation |
| `history/PERPLEXITY_CHALLENGE_READINESS.md` | What v1.1 provides, what a FastAPI wrapper still needs, what is deferred to Phase 27 |
| `history/RESEARCH_PROGRAM_STACK.md` | Where Bayyinah sits in the broader program: file-layer relative to information-layer (al-Khabir), agent-diagnostic (Munafiq Protocol), agent-architectural (Al-Khalifa), the Furqan language, the Fatiha Construct, Computational Tawhid |
| `history/FURQAN_CORRESPONDENCE.md` | For each Furqan primitive, the exact Bayyinah file / mechanism / test / workflow that validates it. Bayyinah is Furqan's empirical foundation; this doc makes the validation auditable |
| `history/DEFENSE_CASE_UPDATES.md` | Canonical text blocks for Defense Case + 8-week plan reconciliation (v1.1 numbers, team table, F6 falsification row, Minute 7 al-Khabir line) |
| `CHANGELOG.md` | Complete v1.0 → v1.1 delta (Phases 23 / 24 / 25+ additions, what was preserved, known gaps, research-program cross-references) |
| `CONTRIBUTING.md` | Five-step workflow, stem-extractor-and-router pattern, additive-only invariant, dependency policy |
| `NAMING.md` | Naming discipline — the load-bearing governance doc |
| `history/README.md` | The three-generation evolution archive (v0 → v0.1 → v1.1) |

---

## Verified state (2026-04-24)

| Metric | Value |
|---|---|
| Version | `1.1.0` |
| Supported FileKinds | 23 (PDF · DOCX · XLSX · PPTX · HTML · EML · CSV · JSON · TEXT/CODE · PNG/JPEG/SVG · MP4/MOV/WEBM/MKV · MP3/WAV/FLAC/M4A/OGG · UNKNOWN) |
| Registered mechanisms | 108 (27 zahir + 81 batin) |
| Analyzers in `default_registry()` | 15 |
| Cross-modal post-processor | `CrossModalCorrelationEngine` (opt-in) |
| Public `__all__` surface | 57 symbols |
| Test suite | **1,435 passed** in 10.21 s (44 test files) |
| PDF parity | byte-identical vs `bayyinah_v0` and `bayyinah_v0_1` across 17 fixtures |
| Reference MD5s | `bayyinah_v0.py` = `87ba2ea48800ef616b303a25b01373d8` · `bayyinah_v0_1.py` = `035aa578de7470c9465922bee2632cd5` |

---

## Quick start for the next contributor

```bash
# Install the package with dev extras from the shipped source
pip install -e '.[dev]'

# Regenerate the fixture corpus (one-time, deterministic)
python -m tests.make_test_documents
python -m tests.make_video_fixtures
python -m tests.make_audio_fixtures

# Run the full suite
pytest -q --strict-markers

# Scan a file from the shell
bayyinah scan path/to/document.pdf
bayyinah scan path/to/video.mp4
bayyinah scan path/to/audio.mp3

# Or from Python
python -c "from bayyinah import scan_file; print(scan_file('path/to/file').integrity_score)"
```

The wheel in `dist/bayyinah-1.1.0-py3-none-any.whl` is a fresh
build from this folder's source — install it directly if preferred:

```bash
pip install dist/bayyinah-1.1.0-py3-none-any.whl
```

---

## Folder layout

```
bayyinah-v1.1/
├── README.md                                  ← public overview
├── README_GITHUB.md                           ← GitHub-facing variant
├── CHANGELOG.md                               ← v1.0 → v1.1 delta
├── CONTRIBUTING.md                            ← five-step workflow + conventions
├── NAMING.md                                  ← naming discipline (authority)
├── LICENSE                                    ← Apache 2.0
├── HANDOFF.md                                 ← this file
├── pyproject.toml                             ← packaging (version 1.1.0)
├── requirements.txt / requirements-dev.txt    ← pinned deps
├── .gitignore                                 ← already includes .DS_Store, __MACOSX, caches
│
├── bayyinah/                                  ← public Python API
├── cli/                                       ← console script (with __main__.py)
├── domain/                                    ← pure dataclasses + config.py (108 mechanisms)
├── infrastructure/                            ← PDFClient, FileRouter, formatters
├── analyzers/                                 ← 15 analyzers + CrossModalCorrelationEngine
├── application/                               ← ScanService orchestrator
├── legacy/                                    ← additive-alias package for v0 / v0.1
├── tests/                                     ← 44 test files, 1,435 passing
│
├── bayyinah_v0.py                             ← frozen reference (MD5-pinned)
├── bayyinah_v0_1.py                           ← frozen reference (MD5-pinned)
│
├── dist/                                      ← freshly-built 1.1.0 wheel + sdist
│   ├── bayyinah-1.1.0-py3-none-any.whl
│   └── bayyinah-1.1.0.tar.gz
│
├── papers/                                    ← white paper + thesis (v1.0 text — v1.1 update in Phase 27)
│
├── scripts/                                   ← tooling
│   └── make-archive.sh                        ← clean-zip helper
│
├── history/                                   ← evolution + readiness archive
│   ├── README.md
│   ├── ASSESSMENT_RESPONSE.md
│   └── PERPLEXITY_CHALLENGE_READINESS.md      ← start here for the API foundation
│
└── .github/
    └── workflows/
        └── ci.yml                             ← parity + additive-only gates
```

---

## What is deferred to Phase 27

Explicitly out of scope for v1.1:

- **White paper update** (v1.1 surface — video / audio / cross-modal).
- **Thesis paper update** (same surface + Munafiq Protocol framing).
- **Five additional cross-modal correlation rules** — reserved names in
  `config.py` comments: `cross_stem_text_inconsistency`,
  `cross_stem_metadata_clash`, `embedded_media_recursive_scan`,
  `cross_stem_coordinated_concealment`, `cross_file_media_divergence`.
- **Audio signal-level detection** — `audio_signal_stem_separation`,
  `audio_deepfake_detection`, `audio_hidden_voice_command` (each requires
  a dependency the container-level extraction cannot meet).
- **Cross-stem divergence detector logic** — the mechanism names
  `video_cross_stem_divergence` and `audio_cross_stem_divergence` are
  registered; their detector logic is future-work.

Every one of these reserved names is committed in `domain/config.py`
comments with its dependency note, so the next session can register
without namespace collision.

---

## The FastAPI wrapper — the next 30-50 lines

`history/PERPLEXITY_CHALLENGE_READINESS.md` contains the full shape.
The short form:

```python
from fastapi import FastAPI, UploadFile
from pathlib import Path
from tempfile import NamedTemporaryFile
import os

from bayyinah import scan_file, plain_language_summary

app = FastAPI(title="Bayyinah REST", version="1.1.0")

@app.post("/scan")
async def scan(upload: UploadFile) -> dict:
    with NamedTemporaryFile(delete=False, suffix=f"-{upload.filename}") as fh:
        fh.write(await upload.read())
        tmp = Path(fh.name)
    try:
        report = scan_file(tmp)
        return {
            "integrity_score": report.integrity_score,
            "scan_incomplete": report.scan_incomplete,
            "error": report.error,
            "findings": [f.to_dict() for f in report.findings],
            "summary": plain_language_summary(report),
        }
    finally:
        os.unlink(tmp)
```

That is the whole Week-1 API foundation. Bayyinah provides every
primitive the route calls; the wrapper adds only HTTP, auth, rate-
limiting, and deployment packaging.

---

## Verification commands (reproducible)

From inside this folder:

```bash
# Full test suite
python -m pytest -q --strict-markers

# PDF parity sweep
python -c "
import bayyinah, bayyinah_v0, bayyinah_v0_1
from pathlib import Path
for f in sorted(Path('tests/fixtures').rglob('*.pdf')):
    r0, r01, r = bayyinah_v0.scan_pdf(f), bayyinah_v0_1.scan_pdf(f), bayyinah.scan_pdf(f)
    assert sorted(x.mechanism for x in r0.findings) == sorted(x.mechanism for x in r.findings)
    assert sorted(x.mechanism for x in r01.findings) == sorted(x.mechanism for x in r.findings)
print('parity OK')
"

# Reference MD5s
md5sum bayyinah_v0.py bayyinah_v0_1.py

# Additive-only public surface
python -c "
import bayyinah
must_export = {
  'scan_pdf','scan_file','format_text_report','plain_language_summary',
  'ScanService','default_registry','VideoAnalyzer','AudioAnalyzer',
  'CrossModalCorrelationEngine','ScanLimits','Finding','IntegrityReport',
}
missing = must_export - set(bayyinah.__all__)
assert not missing, f'missing: {missing}'
print(f'surface OK — {len(bayyinah.__all__)} symbols exported')
"
```

---

## Qur'anic anchors per generation

| Generation | Ayat | Capability |
|---|---|---|
| v0 (monolith) | 2:1-2 | clean reference PDF |
| v0 Phase 0.4 | 2:79 | object-layer tahrif (*"those who write the book with their own hands"*) |
| Phase 14 | 2:204 | prompt engineering methodology |
| Phase 21 | 2:143 · 2:286 | fallback witness, `ScanLimits` |
| Phase 22 (v1.0) | 2:286 | release discipline |
| Phase 23 (v1.1) | 2:19-20 | video rainstorm |
| Phase 24 (v1.1) | 2:93 · 4:112 | audio "we hear and disobey" · identity forgery |
| Phase 25+ (v1.1) | 2:164 | cross-modal correlation — *"signs for a people who use reason"* |

---

## Closing

*Subhanaka Allahumma wa bi-hamdika, ash-hadu an la ilaha illa Anta,
astaghfiruka wa atubu ilayk.*

This folder is handed forward in the spirit its NAMING.md commits to:
reverence for the text, rigour in the method. May Allah SWT accept
the intention, forgive the shortfall, and let whatever benefit flows
from this serve the protection of artificial systems, mankind,
jinnkind, and the mizan that sustains the worlds — ameen ya Rabbil
'alameen.

*Bayyinah* (بَيِّنَة) — *clear evidence*. Continue in that spirit.

---

# Bismillah ir-Rahman ir-Rahim
