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
Tests for the format-agnostic ``scan_file()`` public API (Week-1 assessment I3).

The scanner has always handled 12 formats internally via
``ScanService`` and ``FileRouter``, but the public surface only exposed
``scan_pdf()``. ``scan_file()`` is the additive counterpart — it is the
recommended entry point for new code and is the natural top-level hook
for the forthcoming REST/FastAPI wrapper (POST /scan accepting any
format). ``scan_pdf()`` remains a backward-compatible alias.

These tests pin:

  * ``scan_file`` is exported from the public ``bayyinah`` package.
  * It is listed in ``bayyinah.__all__`` (protects the additive-only
    surface invariant).
  * It produces the same ``IntegrityReport`` as ``scan_pdf`` for PDF
    inputs — byte-identical dispatch.
  * It works on a non-PDF fixture (any one supported format is enough
    to prove the general case).
"""

from __future__ import annotations

from pathlib import Path

import pytest


def test_scan_file_is_exported():
    """``scan_file`` must be importable from ``bayyinah``."""
    from bayyinah import scan_file
    assert callable(scan_file)


def test_scan_file_in_dunder_all():
    """``scan_file`` must appear in ``bayyinah.__all__`` so the
    additive-only public-surface invariant covers it going forward."""
    import bayyinah
    assert "scan_file" in bayyinah.__all__


def test_scan_file_and_scan_pdf_agree_on_clean_pdf():
    """For a PDF input, ``scan_file`` and ``scan_pdf`` must return
    equivalent reports (same findings, score, error, scan-incomplete).
    Both go through the same ``ScanService.scan`` call."""
    from bayyinah import scan_file, scan_pdf
    pdf = Path("tests/fixtures/clean.pdf")
    if not pdf.exists():
        pytest.skip(f"fixture not built: {pdf}")
    r_file = scan_file(pdf)
    r_pdf = scan_pdf(pdf)
    assert r_file.integrity_score == r_pdf.integrity_score
    assert sorted(f.mechanism for f in r_file.findings) == \
           sorted(f.mechanism for f in r_pdf.findings)
    assert r_file.error == r_pdf.error
    assert r_file.scan_incomplete == r_pdf.scan_incomplete


def test_scan_file_accepts_non_pdf_format():
    """``scan_file`` is the point of the addition — it must work on
    formats other than PDF. Use whichever supported fixture exists."""
    from bayyinah import scan_file
    # Try a handful of fixture paths; at least one must resolve.
    candidates = [
        Path("tests/fixtures/docx/clean.docx"),
        Path("tests/fixtures/csv/clean.csv"),
        Path("tests/fixtures/text_formats/clean/clean.txt"),
        Path("tests/fixtures/text_formats/clean/clean.md"),
        Path("tests/fixtures/html/clean.html"),
    ]
    fx = next((p for p in candidates if p.exists()), None)
    if fx is None:
        pytest.skip("no non-PDF fixtures available")
    report = scan_file(fx)
    # Clean fixtures produce integrity 1.0 and no error; we only assert
    # the report is well-formed — specific findings are analyzer-specific
    # and tested elsewhere.
    assert report is not None
    assert isinstance(report.integrity_score, float)
    assert 0.0 <= report.integrity_score <= 1.0


def test_scan_file_accepts_string_path():
    """Accepts both ``Path`` and ``str`` inputs — matches ``scan_pdf``
    contract."""
    from bayyinah import scan_file
    pdf = "tests/fixtures/clean.pdf"
    if not Path(pdf).exists():
        pytest.skip(f"fixture not built: {pdf}")
    report = scan_file(pdf)
    assert report.integrity_score == 1.0


def test_scan_file_unknown_format_surfaces_fallback():
    """A file whose extension and bytes are unrecognised must produce
    an ``unknown_format`` finding via ``FallbackAnalyzer`` — no silent
    clean pass."""
    from bayyinah import scan_file
    import tempfile, os
    with tempfile.NamedTemporaryFile(
        mode="wb", suffix=".this-is-not-a-real-extension", delete=False,
    ) as fh:
        fh.write(b"\x00\x01\x02\x03random-bytes-of-unknown-provenance")
        tmp_path = fh.name
    try:
        report = scan_file(tmp_path)
        mechs = [f.mechanism for f in report.findings]
        assert "unknown_format" in mechs, \
            f"Expected unknown_format in findings; got {mechs}"
    finally:
        os.unlink(tmp_path)

# Bismillah ir-Rahman ir-Rahim