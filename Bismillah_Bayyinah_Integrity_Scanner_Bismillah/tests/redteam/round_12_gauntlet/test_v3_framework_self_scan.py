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
"""Round 12 framework self-scan: assert the v3.0 framework PDF
returns sahih against the v1.2.4 scanner.

Per v3 section 9.7 (Cross-Document Accounting Drift) applied
recursively: the framework's own publication artifact must not
mushtabih against the framework's own scanner. The locked Round
12 prompt anticipated this would surface as a CRITICAL finding
on v1.2.3; empirically (LibreOffice-rendered docx, this clone),
the framework PDF returned sahih on BOTH v1.2.3 and v1.2.4. The
recursive failure mode the prompt anticipated did not manifest
for this artifact under this rendering path.

The fixture and this regression test are still load-bearing: a
future commit could regress the framework PDF's verdict
(producer-string change, encoding shift in the OpenAction
emission path, tier reclassification) and this pinning test
catches that.
"""
from __future__ import annotations
from pathlib import Path
import pytest
from bayyinah import scan_pdf

FIXTURE = (
    Path(__file__).parent / "fixture_v3_framework_self_scan.pdf"
)


def test_v3_framework_pdf_self_scans_clean() -> None:
    """The v3.0 framework PDF must verdict sahih against the
    scanner. If this fails, the framework's own publication
    artifact is being flagged by the framework's own scanner -
    a v3 section 9.7 instance to surface and close."""
    if not FIXTURE.exists():
        pytest.skip(
            "framework PDF not mounted in corpus; render the docx "
            "with `soffice --headless --convert-to pdf` and copy to "
            "fixture_v3_framework_self_scan.pdf"
        )
    rd = scan_pdf(FIXTURE).to_dict()
    fires = sorted({f.get("mechanism") for f in rd.get("findings", [])})
    assert rd.get("integrity_score") == 1.0, (
        f"framework PDF score should be 1.0, got "
        f"{rd.get('integrity_score')}; fires={fires}"
    )
    assert fires == [], (
        f"framework PDF fires findings: {fires}"
    )


def test_v3_framework_pdf_provenance_recorded() -> None:
    """The fixture's provenance is documented: LibreOffice-rendered
    from bayyinah_audit_framework_v3.docx (Round 12 build,
    2026-05-07). Future renderings (different LibreOffice version,
    pdfTeX rendering of the same source) may produce different
    PDFs; this test pins the structural property of the current
    fixture - a LibreOffice-produced PDF without an /OpenAction
    key should not fire any batin-layer mechanism."""
    if not FIXTURE.exists():
        pytest.skip("framework PDF not mounted")
    import pypdf
    r = pypdf.PdfReader(FIXTURE)
    producer = r.metadata.get("/Producer", "")
    assert "LibreOffice" in producer, (
        f"fixture producer drift: expected LibreOffice, got {producer!r}. "
        f"If the v3.0 framework was re-rendered with a different "
        f"producer (pdfTeX, etc.), update the fixture and re-verify "
        f"that test_v3_framework_pdf_self_scans_clean still passes."
    )

# Bismillah ir-Rahman ir-Rahim