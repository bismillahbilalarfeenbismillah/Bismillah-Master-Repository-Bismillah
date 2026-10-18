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
Fixture-level pytest checks for Bayyinah's ground-truth corpus.

Each fixture in ``tests/make_test_documents.py`` declares the exact set
of detector mechanisms it is designed to fire. These tests assert, for
every fixture, that:

  * scanning with ``bayyinah_v0.scan_pdf`` emits precisely that set (no
    more, no fewer); and
  * scanning with ``bayyinah_v0_1.scan_pdf`` produces byte-identical
    JSON output to v0 after normalising pypdf's non-deterministic
    ``IndirectObject.__repr__``.

Together these checks form the Phase 0 guardrail described in the
Al-Baqarah refactor roadmap: detector-level correctness plus parity
invariance. Every subsequent refactor phase must keep them green.

The fixtures are generated once by ``python -m tests.make_test_documents``
and committed under ``tests/fixtures/``. If a fixture is missing these
tests trigger a regeneration before running.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

# Import the fixture registry and ensure the fixtures exist on disk.
from tests.make_test_documents import FIXTURES, FIXTURES_DIR  # noqa: E402

import bayyinah_v0  # noqa: E402
import bayyinah_v0_1  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# pypdf's ``IndirectObject.__repr__`` embeds ``id()`` of the parent
# document, which varies between process runs and between the two
# scanners' independent pypdf readers. Normalise it before diffing.
_INDIRECT_RE = re.compile(r"IndirectObject\((\d+),\s*(\d+),\s*\d+\)")


def _normalise(s: str) -> str:
    return _INDIRECT_RE.sub(r"IndirectObject(\1, \2, <id>)", s)


def _report_json(report) -> str:
    return json.dumps(report.to_dict(), indent=2, default=str, sort_keys=True)


def _mechanisms(report) -> set[str]:
    return {f.mechanism for f in report.findings}


@pytest.fixture(scope="session", autouse=True)
def _ensure_fixtures_built() -> None:
    """If any fixture PDF is missing, regenerate the whole corpus."""
    missing = [fx.out_path for fx in FIXTURES.values() if not fx.out_path.exists()]
    if not missing:
        return
    subprocess.run(
        [sys.executable, "-m", "tests.make_test_documents"],
        check=True,
        cwd=str(FIXTURES_DIR.parent.parent),
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "fixture_name",
    list(FIXTURES.keys()),
    ids=list(FIXTURES.keys()),
)
def test_fixture_fires_expected_mechanisms_only(fixture_name: str) -> None:
    """Every fixture must fire exactly the mechanisms it declares — no
    more, no fewer. This is the detector-level correctness guardrail."""
    fx = FIXTURES[fixture_name]
    report = bayyinah_v0.scan_pdf(fx.out_path)

    got = _mechanisms(report)
    expected = set(fx.expected_mechanisms)

    assert got == expected, (
        f"\nFixture {fixture_name!r} detector mismatch."
        f"\n  expected: {sorted(expected) or '(none)'}"
        f"\n  got:      {sorted(got) or '(none)'}"
        f"\n  missing:  {sorted(expected - got) or '(none)'}"
        f"\n  extra:    {sorted(got - expected) or '(none)'}"
    )


@pytest.mark.parametrize(
    "fixture_name",
    list(FIXTURES.keys()),
    ids=list(FIXTURES.keys()),
)
def test_v0_v01_parity(fixture_name: str) -> None:
    """v0 and v0.1 must produce byte-identical JSON output (after
    normalising pypdf's non-deterministic IndirectObject repr). This is
    the parity invariant that every refactor phase must preserve."""
    fx = FIXTURES[fixture_name]

    r0 = bayyinah_v0.scan_pdf(fx.out_path)
    r1 = bayyinah_v0_1.scan_pdf(fx.out_path)

    j0 = _normalise(_report_json(r0))
    j1 = _normalise(_report_json(r1))

    assert j0 == j1, (
        f"v0/v0.1 parity diverged on {fixture_name!r}. "
        "This means a refactor introduced an observable behaviour change."
    )


def test_clean_pdf_has_score_one_and_no_errors() -> None:
    """The reference-standard fixture must score exactly 1.0 with zero
    findings and zero scan errors. If this ever breaks, a detector has
    a false positive on plain, well-formed input."""
    fx = FIXTURES["clean"]
    report = bayyinah_v0.scan_pdf(fx.out_path)

    assert report.integrity_score == 1.0, (
        f"clean.pdf scored {report.integrity_score}, expected 1.0"
    )
    assert report.findings == [], (
        f"clean.pdf emitted unexpected findings: "
        f"{[f.mechanism for f in report.findings]}"
    )
    assert report.error is None, f"clean.pdf scan error: {report.error}"
    assert not report.scan_incomplete, "clean.pdf marked scan_incomplete"


def test_positive_combined_fires_all_sixteen() -> None:
    """The complete munafiq fixture must fire every single-mechanism
    detector the corpus covers. If this count drops, the combined
    fixture has regressed (a mechanism has been silently dropped)."""
    fx = FIXTURES["positive_combined"]
    report = bayyinah_v0.scan_pdf(fx.out_path)

    mechanisms = _mechanisms(report)
    expected_count = len(set(fx.expected_mechanisms))
    assert len(mechanisms) == expected_count, (
        f"positive_combined fired {len(mechanisms)} distinct mechanisms, "
        f"expected {expected_count}."
    )
    # The score clamps at 0 for a document with this much adversarial content.
    assert report.integrity_score == 0.0, (
        f"positive_combined scored {report.integrity_score}, expected 0.0"
    )

# Bismillah ir-Rahman ir-Rahim