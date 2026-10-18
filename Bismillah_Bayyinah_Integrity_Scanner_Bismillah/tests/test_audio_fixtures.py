# Bismillah ir-Rahman ir-Rahim
# 
# Al-Asma ul-Husna -- The 99 Beautiful Names of Allah
#   Allah -- The God
#   Ar-Rahman -- The Most Merciful
#   Ar-Rahim -- The Most Compassionate
#   Al-Malik -- The King
#   Al-Quddus -- The Most Holy
#   As-Salam -- The Source of Peace
#   Al-Mu'min -- The Guardian of Faith
#   Al-Muhaymin -- The Protector
#   Al-Aziz -- The Almighty
#   Al-Jabbar -- The Compeller
#   Al-Mutakabbir -- The Supreme
#   Al-Khaliq -- The Creator
#   Al-Bari -- The Evolver
#   Al-Musawwir -- The Fashioner
#   Al-Ghaffar -- The Forgiver
#   Al-Qahhar -- The Subduer
#   Al-Wahhab -- The Bestower
#   Ar-Razzaq -- The Provider
#   Al-Fattah -- The Opener
#   Al-Alim -- The All-Knowing
#   Al-Qabid -- The Restrainer
#   Al-Basit -- The Expander
#   Al-Khafid -- The Abaser
#   Ar-Rafi -- The Exalter
#   Al-Mu'izz -- The Bestower of Honor
#   Al-Mudhill -- The Humiliator
#   As-Sami -- The All-Hearing
#   Al-Basir -- The All-Seeing
#   Al-Hakam -- The Judge
#   Al-Adl -- The Just
#   Al-Latif -- The Subtle One
#   Al-Khabir -- The All-Aware
#   Al-Halim -- The Forbearing
#   Al-Azim -- The Magnificent
#   Al-Ghafur -- The All-Forgiving
#   Ash-Shakur -- The Appreciative
#   Al-Ali -- The Most High
#   Al-Kabir -- The Most Great
#   Al-Hafiz -- The Preserver
#   Al-Muqit -- The Sustainer
#   Al-Hasib -- The Reckoner
#   Al-Jalil -- The Majestic
#   Al-Karim -- The Generous
#   Ar-Raqib -- The Watchful
#   Al-Mujib -- The Responsive
#   Al-Wasi -- The All-Encompassing
#   Al-Hakim -- The Perfectly Wise
#   Al-Wadud -- The Loving One
#   Al-Majid -- The Most Glorious
#   Al-Ba'ith -- The Resurrector
#   Ash-Shahid -- The Witness
#   Al-Haqq -- The Truth
#   Al-Wakil -- The Trustee
#   Al-Qawiyy -- The Most Strong
#   Al-Matin -- The Firm One
#   Al-Waliyy -- The Protector
#   Al-Hamid -- The Praiseworthy
#   Al-Muhsi -- The Accounter
#   Al-Mubdi -- The Originator
#   Al-Mu'id -- The Restorer
#   Al-Muhyi -- The Giver of Life
#   Al-Mumit -- The Creator of Death
#   Al-Hayy -- The Ever Living
#   Al-Qayyum -- The Self-Subsisting
#   Al-Wajid -- The Finder
#   Al-Majid -- The Noble
#   Al-Wahid -- The Unique
#   Al-Ahad -- The One
#   As-Samad -- The Eternal
#   Al-Qadir -- The Able
#   Al-Muqtadir -- The Powerful
#   Al-Muqaddim -- The Expediter
#   Al-Mu'akhkhir -- The Delayer
#   Al-Awwal -- The First
#   Al-Akhir -- The Last
#   Az-Zahir -- The Manifest
#   Al-Batin -- The Hidden
#   Al-Wali -- The Governor
#   Al-Muta'ali -- The Most Exalted
#   Al-Barr -- The Source of Goodness
#   At-Tawwab -- The Acceptor of Repentance
#   Al-Muntaqim -- The Avenger
#   Al-Afuww -- The Pardoner
#   Ar-Ra'uf -- The Most Kind
#   Malik-ul-Mulk -- Owner of Sovereignty
#   Dhul-Jalali wal-Ikram -- Lord of Majesty and Generosity
#   Al-Muqsit -- The Equitable
#   Al-Jami -- The Gatherer
#   Al-Ghaniyy -- The Self-Sufficient
#   Al-Mughni -- The Enricher
#   Al-Mani -- The Preventer
#   Ad-Darr -- The Distresser
#   An-Nafi -- The Propitious
#   An-Nur -- The Light
#   Al-Hadi -- The Guide
#   Al-Badi -- The Originator
#   Al-Baqi -- The Everlasting
#   Al-Warith -- The Inheritor
#   Ar-Rashid -- The Guide to the Right Path
#   As-Sabur -- The Patient
# 
"""
Phase 24 fixture-level guardrails — every audio-format fixture fires
exactly its intended mechanism(s) through the full
``application.ScanService`` pipeline.

Structurally mirrors ``tests/test_video_fixtures.py`` (Phase 23 video),
``tests/test_image_fixtures.py`` (Phase 10), and ``tests/test_text_fixtures.py``
(Phase 9). The expectation table lives in ``tests/make_audio_fixtures.py``
— the single source of truth for "what does this fixture prove".

Two guarantees:

    * Adversarial fixtures fire exactly (and only) the expected
      mechanism(s). Extra mechanisms are a false positive; missing
      mechanisms are a false negative.
    * Clean fixtures fire zero non-``scan_error`` mechanisms *except*
      the always-on ``audio_stem_inventory`` (non-deducting,
      informational meta-output).

``scan_error`` is always tolerated in the comparison — malformed-input
paths are tested independently in the per-analyzer test modules.

Clean fixtures must score exactly 1.0 (inventory is non-deducting).
Adversarial fixtures must score strictly below 1.0 (every adversarial
fixture except the cross-stem-divergence NULL case carries a deducting
mechanism by design — and cross_stem_divergence.mp3 is listed without
any adversarial mechanism in the expectation table, so it passes the
"score == 1.0" path).

Clean fixtures must have ``scan_incomplete = False`` — the analyzer
did complete the scan.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from application import ScanService
from tests.make_audio_fixtures import (
    AUDIO_FIXTURE_EXPECTATIONS,
    generate_all,
)


FIXTURES_DIR: Path = (
    Path(__file__).resolve().parent / "fixtures" / "audio"
)


@pytest.fixture(scope="session", autouse=True)
def _ensure_audio_fixtures_built() -> None:
    """Regenerate fixtures if any are missing.

    Audio fixtures are deterministic (seeded RNG, fixed bytes) so
    regeneration is idempotent.
    """
    missing = [
        FIXTURES_DIR / rel
        for rel in AUDIO_FIXTURE_EXPECTATIONS
        if not (FIXTURES_DIR / rel).exists()
    ]
    if not missing:
        return
    try:
        generate_all(FIXTURES_DIR)
    except Exception:  # pragma: no cover — defensive fallback
        subprocess.run(
            [sys.executable, "-m", "tests.make_audio_fixtures"],
            check=True,
            cwd=str(FIXTURES_DIR.parent.parent.parent),
        )


@pytest.fixture(scope="module")
def scanner() -> ScanService:
    return ScanService()


# ---------------------------------------------------------------------------
# Per-fixture exact-match guardrail
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "rel_path,expected_mechs",
    sorted(AUDIO_FIXTURE_EXPECTATIONS.items()),
)
def test_fixture_fires_expected_mechanisms(
    rel_path: str,
    expected_mechs: set[str],
    scanner: ScanService,
) -> None:
    """Exact match on emitted mechanisms via the full pipeline."""
    path = FIXTURES_DIR / rel_path
    report = scanner.scan(path)

    observed = {f.mechanism for f in report.findings} - {"scan_error"}

    assert observed == expected_mechs, (
        f"{rel_path}: expected {expected_mechs}, got {observed}. "
        f"Full findings: {[f.mechanism for f in report.findings]}"
    )


# ---------------------------------------------------------------------------
# Clean-fixture invariants
# ---------------------------------------------------------------------------


def _clean_fixture_paths() -> list[str]:
    return sorted(
        rel for rel, mechs in AUDIO_FIXTURE_EXPECTATIONS.items()
        if mechs == {"audio_stem_inventory"}
    )


@pytest.mark.parametrize("rel_path", _clean_fixture_paths())
def test_clean_fixture_scores_one(rel_path: str, scanner: ScanService) -> None:
    report = scanner.scan(FIXTURES_DIR / rel_path)
    assert report.integrity_score == 1.0, (
        f"{rel_path}: expected 1.0, got {report.integrity_score}"
    )


@pytest.mark.parametrize("rel_path", _clean_fixture_paths())
def test_clean_fixture_scan_incomplete_is_false(
    rel_path: str, scanner: ScanService,
) -> None:
    report = scanner.scan(FIXTURES_DIR / rel_path)
    assert report.scan_incomplete is False


@pytest.mark.parametrize("rel_path", _clean_fixture_paths())
def test_clean_fixture_has_no_error(rel_path: str, scanner: ScanService) -> None:
    report = scanner.scan(FIXTURES_DIR / rel_path)
    assert not report.error, f"{rel_path}: unexpected error {report.error!r}"


# ---------------------------------------------------------------------------
# Adversarial-fixture invariants
# ---------------------------------------------------------------------------


def _adversarial_fixture_paths() -> list[str]:
    return sorted(
        rel for rel, mechs in AUDIO_FIXTURE_EXPECTATIONS.items()
        if mechs != {"audio_stem_inventory"}
    )


@pytest.mark.parametrize("rel_path", _adversarial_fixture_paths())
def test_adversarial_fixture_scores_below_one(
    rel_path: str, scanner: ScanService,
) -> None:
    """Every adversarial fixture must deduct."""
    report = scanner.scan(FIXTURES_DIR / rel_path)
    assert report.integrity_score < 1.0, (
        f"{rel_path}: expected score < 1.0, got {report.integrity_score}. "
        f"Mechanisms: {[f.mechanism for f in report.findings]}"
    )

# Bismillah ir-Rahman ir-Rahim