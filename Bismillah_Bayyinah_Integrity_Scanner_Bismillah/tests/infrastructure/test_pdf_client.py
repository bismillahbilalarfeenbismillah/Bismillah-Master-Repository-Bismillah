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
Tests for infrastructure.pdf_client.PDFClient.

Exercised against the Phase 0 fixtures so every test runs on real PDFs
that v0.1 already handles — any behavioural difference would show up
here before it bit a downstream analyzer.

Coverage targets:
  * Opens clean.pdf with pymupdf
  * Opens clean.pdf with pypdf via try_pypdf
  * Caches the fitz Document across repeated .fitz accesses
  * try_pypdf replays captured error on repeated call after failure
  * raw_bytes reads whole-file contents, caches result
  * close() is idempotent and subsequent access raises PDFParseError
  * Context manager closes on exit, even when the body raises
  * Non-PDF / nonexistent paths wrap errors in PDFParseError
  * Repr is informative
"""

from __future__ import annotations

from pathlib import Path

import pytest

from domain.exceptions import PDFParseError
from infrastructure.pdf_client import PDFClient


FIXTURES_DIR = Path(__file__).resolve().parents[1] / "fixtures"
CLEAN_PDF = FIXTURES_DIR / "clean.pdf"
TEXT_FIXTURE_DIR = FIXTURES_DIR / "text"
OBJECT_FIXTURE_DIR = FIXTURES_DIR / "object"


# ---------------------------------------------------------------------------
# Fixture availability
# ---------------------------------------------------------------------------

def _require_fixtures() -> None:
    if not CLEAN_PDF.exists():
        pytest.skip(
            f"Phase 0 fixtures not built; expected {CLEAN_PDF}. "
            "Run: python tests/make_test_documents.py"
        )


# ---------------------------------------------------------------------------
# Open semantics
# ---------------------------------------------------------------------------

def test_opens_clean_fixture_with_pymupdf() -> None:
    _require_fixtures()
    with PDFClient(CLEAN_PDF) as client:
        doc = client.fitz
        assert doc is not None
        # pymupdf Documents expose len() == page count
        assert len(doc) >= 1


def test_fitz_handle_is_cached() -> None:
    _require_fixtures()
    with PDFClient(CLEAN_PDF) as client:
        a = client.fitz
        b = client.fitz
        assert a is b


def test_try_pypdf_returns_reader_on_success() -> None:
    _require_fixtures()
    with PDFClient(CLEAN_PDF) as client:
        reader, err = client.try_pypdf()
        assert err is None
        assert reader is not None


def test_try_pypdf_caches_reader() -> None:
    _require_fixtures()
    with PDFClient(CLEAN_PDF) as client:
        r1, _ = client.try_pypdf()
        r2, _ = client.try_pypdf()
        assert r1 is r2


def test_raw_bytes_returns_full_file_and_caches() -> None:
    _require_fixtures()
    with PDFClient(CLEAN_PDF) as client:
        b1 = client.raw_bytes()
        b2 = client.raw_bytes()
        assert b1 is b2  # cached
        assert b1 is not None
        assert b1.startswith(b"%PDF-")
        assert b1 == CLEAN_PDF.read_bytes()


# ---------------------------------------------------------------------------
# Failure paths
# ---------------------------------------------------------------------------

def test_fitz_open_on_missing_file_raises_pdfparseerror(tmp_path: Path) -> None:
    missing = tmp_path / "does_not_exist.pdf"
    client = PDFClient(missing)
    with pytest.raises(PDFParseError):
        _ = client.fitz


def test_fitz_open_on_non_pdf_raises_pdfparseerror(tmp_path: Path) -> None:
    junk = tmp_path / "not_a_pdf.pdf"
    junk.write_bytes(b"this is not a pdf at all\n")
    client = PDFClient(junk)
    with pytest.raises(PDFParseError):
        _ = client.fitz


def test_try_pypdf_on_non_pdf_returns_error_tuple(tmp_path: Path) -> None:
    """pypdf raises broadly on malformed input; try_pypdf must capture
    and return it, not propagate."""
    junk = tmp_path / "not_a_pdf.pdf"
    junk.write_bytes(b"still not a pdf\n")
    client = PDFClient(junk)
    reader, err = client.try_pypdf()
    assert reader is None
    assert err is not None
    # Second call replays the same exception — no retry.
    reader2, err2 = client.try_pypdf()
    assert reader2 is None
    assert err2 is err


def test_raw_bytes_on_missing_file_returns_none(tmp_path: Path) -> None:
    client = PDFClient(tmp_path / "nope.pdf")
    assert client.raw_bytes() is None


# ---------------------------------------------------------------------------
# Lifecycle
# ---------------------------------------------------------------------------

def test_close_is_idempotent() -> None:
    _require_fixtures()
    client = PDFClient(CLEAN_PDF)
    _ = client.fitz  # force open
    client.close()
    client.close()  # must not raise
    assert client.is_closed


def test_close_on_unused_client_is_safe(tmp_path: Path) -> None:
    """A client that never touched fitz still closes cleanly."""
    missing = tmp_path / "never_opened.pdf"
    client = PDFClient(missing)
    client.close()  # must not raise
    assert client.is_closed


def test_access_after_close_raises() -> None:
    _require_fixtures()
    client = PDFClient(CLEAN_PDF)
    _ = client.fitz
    client.close()
    with pytest.raises(PDFParseError):
        _ = client.fitz
    with pytest.raises(PDFParseError):
        client.try_pypdf()
    with pytest.raises(PDFParseError):
        client.raw_bytes()


def test_context_manager_closes_on_normal_exit() -> None:
    _require_fixtures()
    with PDFClient(CLEAN_PDF) as client:
        _ = client.fitz
    assert client.is_closed


def test_context_manager_closes_on_exception() -> None:
    _require_fixtures()

    class _Boom(Exception):
        pass

    client_ref: list[PDFClient] = []
    with pytest.raises(_Boom):
        with PDFClient(CLEAN_PDF) as client:
            client_ref.append(client)
            _ = client.fitz
            raise _Boom()
    assert client_ref[0].is_closed


# ---------------------------------------------------------------------------
# Cross-fixture smoke test — every built fixture can be opened
# ---------------------------------------------------------------------------

def test_all_text_fixtures_open_via_pdfclient() -> None:
    _require_fixtures()
    text_fixtures = sorted(TEXT_FIXTURE_DIR.glob("*.pdf"))
    if not text_fixtures:
        pytest.skip("No text fixtures built yet.")
    for fx in text_fixtures:
        with PDFClient(fx) as client:
            doc = client.fitz
            assert len(doc) >= 1, f"Empty document for {fx}"


def test_all_object_fixtures_open_via_pdfclient() -> None:
    _require_fixtures()
    object_fixtures = sorted(OBJECT_FIXTURE_DIR.glob("*.pdf"))
    if not object_fixtures:
        pytest.skip("No object fixtures built yet.")
    for fx in object_fixtures:
        with PDFClient(fx) as client:
            doc = client.fitz
            assert len(doc) >= 1, f"Empty document for {fx}"


# ---------------------------------------------------------------------------
# Repr
# ---------------------------------------------------------------------------

def test_repr_reports_state() -> None:
    _require_fixtures()
    client = PDFClient(CLEAN_PDF)
    r = repr(client)
    assert "PDFClient" in r
    assert "closed=False" in r
    assert "fitz_open=False" in r
    _ = client.fitz
    assert "fitz_open=True" in repr(client)
    client.close()
    assert "closed=True" in repr(client)

# Bismillah ir-Rahman ir-Rahim