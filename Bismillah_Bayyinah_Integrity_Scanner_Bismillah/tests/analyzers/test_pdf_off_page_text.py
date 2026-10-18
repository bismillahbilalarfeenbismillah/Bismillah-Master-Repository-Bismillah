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
Tests for analyzers.pdf_off_page_text (v1.1.2 Day 2 mechanism 03).

Tier 1 mechanism: text-matrix Tm origin outside the page MediaBox.
Closes pdf_gauntlet fixture 03_off_page.pdf, which the v1.1.1
ZahirTextAnalyzer._check_offpage path missed because PyMuPDF's
get_text('dict') silently drops spans whose origin is below the
page rectangle. The new detector reads the raw content stream via
pikepdf, bypassing that drop.

Test pairing per Differentiator Layer 7 GAN paired-fixtures:
  - test_catches_fixture_03: adversarial fixture must produce a
    Tier 1 finding with mechanism = "pdf_off_page_text".
  - test_clean_on_control: the v1.0 baseline clean PDF
    (tests/fixtures/clean.pdf) must produce zero pdf_off_page_text
    findings. The fixture is the long-standing v1.0 control PDF
    that the existing PDF analyzer suite uses for its no-false-
    positive checks.

References:
  - docs/adversarial/pdf_gauntlet/REPORT.md row 03
  - docs/scope/v1_1_2_claude_prompt.md section 6.2
"""
from __future__ import annotations

from pathlib import Path

from analyzers.pdf_off_page_text import detect_pdf_off_page_text
from domain.config import BATIN_MECHANISMS, SEVERITY, TIER, ZAHIR_MECHANISMS


REPO_ROOT = Path(__file__).resolve().parents[2]
ADVERSARIAL_FIXTURE = (
    REPO_ROOT / "docs/adversarial/pdf_gauntlet/fixtures/03_off_page.pdf"
)
CONTROL_FIXTURE = REPO_ROOT / "tests/fixtures/clean.pdf"


def test_pdf_off_page_text_registered_in_zahir_mechanisms() -> None:
    """The mechanism classifies as zahir (it parallels the existing
    zahir off_page_text; the Tm origin coordinate is observable from
    the content stream's text-rendering operators with no hidden-
    state inference). TIER is 1 and SEVERITY is 1.0 per Day 2
    prompt section 6.6 step 2."""
    assert "pdf_off_page_text" in ZAHIR_MECHANISMS
    assert "pdf_off_page_text" not in BATIN_MECHANISMS
    assert TIER["pdf_off_page_text"] == 1
    assert SEVERITY["pdf_off_page_text"] == 1.0


def test_pdf_off_page_text_catches_fixture_03() -> None:
    """The off-page Tm at (72, -200) in fixture 03 must produce a
    Tier 1 finding."""
    assert ADVERSARIAL_FIXTURE.exists(), (
        f"PDF gauntlet fixture missing: {ADVERSARIAL_FIXTURE}"
    )
    findings = detect_pdf_off_page_text(ADVERSARIAL_FIXTURE)
    matching = [
        f for f in findings
        if f.mechanism == "pdf_off_page_text" and f.tier == 1
    ]
    assert len(matching) >= 1, (
        f"pdf_off_page_text did not fire on fixture 03; got "
        f"{[f.mechanism for f in findings]}"
    )


def test_pdf_off_page_text_clean_on_control() -> None:
    """The v1.0 baseline clean PDF (tests/fixtures/clean.pdf) has
    only on-page text and must NOT produce a pdf_off_page_text
    finding."""
    assert CONTROL_FIXTURE.exists(), (
        f"Control fixture missing: {CONTROL_FIXTURE}"
    )
    findings = detect_pdf_off_page_text(CONTROL_FIXTURE)
    assert all(f.mechanism != "pdf_off_page_text" for f in findings), (
        f"pdf_off_page_text fired on the clean baseline PDF; got "
        f"{[f.mechanism for f in findings]}"
    )


def test_pdf_off_page_text_recovers_payload_into_concealed() -> None:
    """inversion_recovery.concealed must surface the actual hidden
    text bytes drawn by the off-page Tj following the off-page Tm.
    Pinning the contract closes the v1.1.2 PDF gauntlet at full
    payload-recovery (gauntlet status 2026-04-28). Mirror of
    pdf_hidden_text_annotation's /Contents preview convention so all
    PDF mechanisms surface inversion_recovery the same way."""
    findings = detect_pdf_off_page_text(ADVERSARIAL_FIXTURE)
    matching = [f for f in findings if f.mechanism == "pdf_off_page_text"]
    assert matching, "no pdf_off_page_text finding on fixture 03"
    concealed = matching[0].concealed
    assert "HIDDEN_TEXT_PAYLOAD" in concealed, (
        f"concealed must carry the recovered hidden text bytes; "
        f"got: {concealed!r}"
    )

# Bismillah ir-Rahman ir-Rahim