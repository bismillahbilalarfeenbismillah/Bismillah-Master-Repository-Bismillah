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
Phase 16 fixture-level guardrails — every HTML fixture fires exactly
its intended mechanism(s) through the full ``application.ScanService``
pipeline.

Structurally mirrors ``tests/test_docx_fixtures.py`` (DOCX corpus) and
``tests/test_text_fixtures.py`` (text/JSON corpus). The expectation
table ``HTML_FIXTURE_EXPECTATIONS`` lives next to the fixture builder
in ``tests/make_html_fixtures.py`` and is the single source of truth
for "what does this fixture prove".

Three guarantees enforced here:

    * Adversarial fixtures fire exactly (and only) the expected
      mechanism(s). Extra firings are false positives; missing firings
      are false negatives.
    * Clean fixtures score 1.0 and do not mark the scan incomplete.
    * Adversarial fixtures reduce the APS-continuous score below 1.0
      — a mechanism whose SEVERITY entry is missing or zero would
      silently pass otherwise; this guard makes that regression
      visible.

``scan_error`` is tolerated in the comparison because a single parse
failure in the future could surface as an incomplete scan rather than
as an assertion failure — but none of the current fixtures should
trigger it, and the explicit scan_incomplete test below catches the
case where scan_error would silently hide.

HTML fixtures are plain UTF-8 text and regenerate deterministically
from ``tests/make_html_fixtures.py`` — no fixed ZipInfo machinery
needed (unlike DOCX).
"""

from __future__ import annotations

import subprocess
import sys

import pytest

from application import ScanService
from tests.make_html_fixtures import (
    FIXTURES_DIR,
    HTML_FIXTURE_EXPECTATIONS,
)


@pytest.fixture(scope="session", autouse=True)
def _ensure_html_fixtures_built() -> None:
    """Regenerate fixtures if any are missing.

    Session-scoped so the regeneration happens at most once per test
    invocation. Running ``python -m tests.make_html_fixtures`` from
    the repo root produces the fixture corpus.
    """
    missing = [
        FIXTURES_DIR / rel
        for rel in HTML_FIXTURE_EXPECTATIONS
        if not (FIXTURES_DIR / rel).exists()
    ]
    if not missing:
        return
    subprocess.run(
        [sys.executable, "-m", "tests.make_html_fixtures"],
        check=True,
        cwd=str(FIXTURES_DIR.parent.parent),
    )


@pytest.fixture(scope="module")
def scanner() -> ScanService:
    return ScanService()


@pytest.mark.parametrize(
    "rel,expected",
    sorted(HTML_FIXTURE_EXPECTATIONS.items()),
)
def test_fixture_fires_exactly_expected(
    rel: str, expected: list[str], scanner: ScanService,
) -> None:
    path = FIXTURES_DIR / rel
    report = scanner.scan(path)
    observed = sorted(
        {f.mechanism for f in report.findings if f.mechanism != "scan_error"}
    )
    assert observed == sorted(expected), (
        f"{rel}: expected {expected}, got {observed}. "
        f"Findings: "
        + "; ".join(f"{f.mechanism}@{f.location}" for f in report.findings)
    )


def test_clean_fixtures_score_1_and_complete(scanner: ScanService) -> None:
    """Every clean HTML fixture must score exactly 1.0 and be a complete scan."""
    for rel, expected in HTML_FIXTURE_EXPECTATIONS.items():
        if expected:
            continue
        report = scanner.scan(FIXTURES_DIR / rel)
        assert report.integrity_score == 1.0, (
            f"{rel}: clean fixture did not score 1.0 "
            f"(score={report.integrity_score}, "
            f"findings={[f.mechanism for f in report.findings]})"
        )
        assert not report.scan_incomplete, (
            f"{rel}: clean fixture marked scan_incomplete"
        )


def test_adversarial_fixtures_all_reduce_score(scanner: ScanService) -> None:
    """Adversarial fixtures must reduce the APS score below 1.0.

    The analyzer's mechanism / severity wiring can regress silently — a
    mechanism name might be removed from ``SEVERITY`` without flipping
    any unit test, and the finding would still ship (with severity 0,
    contributing nothing to the score). This guard makes the regression
    visible: an adversarial fixture whose findings cost zero is not
    doing its job.
    """
    for rel, expected in HTML_FIXTURE_EXPECTATIONS.items():
        if not expected:
            continue
        report = scanner.scan(FIXTURES_DIR / rel)
        assert report.integrity_score < 1.0, (
            f"{rel}: adversarial fixture did not reduce score"
        )


def test_every_fixture_is_not_scan_incomplete(scanner: ScanService) -> None:
    """No fixture in the HTML corpus should trigger a scan-incomplete clamp.

    Every HTML fixture is a well-formed UTF-8 document. If any of them
    trips ``scan_incomplete``, the analyzer has a bug (or the fixture
    itself is malformed — both are signals worth catching explicitly).
    """
    for rel in HTML_FIXTURE_EXPECTATIONS:
        report = scanner.scan(FIXTURES_DIR / rel)
        assert not report.scan_incomplete, (
            f"{rel}: fixture unexpectedly marked scan_incomplete. "
            f"error={report.error!r}"
        )

# Bismillah ir-Rahman ir-Rahim