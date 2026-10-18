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
Integration tests for /scan endpoint verdict emission.

Asserts that every routing-divergence fixture in the format_routing_gauntlet
surfaces verdict=mughlaq at the HTTP layer, and that the control fixture
does not.

This is the F4 falsifiability surface for the Day 1 Tier 0 layer at the
HTTP boundary. If a routing-divergence fixture passes through the scanner
and emerges with verdict != mughlaq, the published guarantee that
adversarial routing is publicly disclosed is falsified.

The Verdict type is Literal["sahih", "mushtabih", "mukhfi", "munafiq",
"mughlaq"]. A clean .pdf with valid magic returns "sahih"; the control
test asserts != "mughlaq" defensively rather than asserting the exact
positive value, so unrelated future changes to non-mughlaq scoring do
not falsify this test.
"""
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from api import app


FIXTURES_DIR = Path(__file__).resolve().parents[2] / (
    "docs/adversarial/format_routing_gauntlet/fixtures"
)

ROUTING_DIVERGENCE_FIXTURES = [
    "01_polyglot.docx",
    "02_pdf_as_txt.txt",
    "03_empty.pdf",
    "04_truncated.pdf",
    "05_docx_as_xlsx.xlsx",
    "06_unanalyzed.txt",
]
CONTROL_FIXTURE = "07_control.pdf"


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


@pytest.mark.parametrize("fixture_name", ROUTING_DIVERGENCE_FIXTURES)
def test_routing_divergence_fixture_returns_mughlaq(
    client: TestClient, fixture_name: str,
) -> None:
    fixture_path = FIXTURES_DIR / fixture_name
    assert fixture_path.exists(), f"Day 1 fixture missing: {fixture_path}"
    with open(fixture_path, "rb") as f:
        response = client.post(
            "/scan",
            files={"file": (fixture_name, f, "application/octet-stream")},
        )
    assert response.status_code == 200, response.text
    payload = response.json()
    assert "verdict" in payload, "verdict field missing from /scan response"
    assert payload["verdict"] == "mughlaq", (
        f"{fixture_name} should floor at mughlaq via Tier 0 routing-divergence; "
        f"got {payload['verdict']}"
    )


def test_control_fixture_does_not_return_mughlaq(client: TestClient) -> None:
    fixture_path = FIXTURES_DIR / CONTROL_FIXTURE
    assert fixture_path.exists(), f"Control fixture missing: {fixture_path}"
    with open(fixture_path, "rb") as f:
        response = client.post(
            "/scan",
            files={"file": (CONTROL_FIXTURE, f, "application/pdf")},
        )
    assert response.status_code == 200, response.text
    payload = response.json()
    assert "verdict" in payload, "verdict field missing from /scan response"
    assert payload["verdict"] != "mughlaq", (
        f"Control fixture {CONTROL_FIXTURE} must not floor at mughlaq; "
        f"a real .pdf with PDF magic should not trigger Tier 0. "
        f"Got verdict={payload['verdict']}"
    )

# Bismillah ir-Rahman ir-Rahim