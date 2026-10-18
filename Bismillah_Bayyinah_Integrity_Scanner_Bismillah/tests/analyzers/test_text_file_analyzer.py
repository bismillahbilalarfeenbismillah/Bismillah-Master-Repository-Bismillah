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
Tests for analyzers.text_file_analyzer.TextFileAnalyzer.

Phase 9 guardrails. The analyzer applies the zahir-layer concealment
catalog (zero-width, TAG block, bidi-control, homoglyph) to raw text
files. Tests here verify both the positive signal (every adversarial
payload fires the expected mechanism) and the negative signal (clean
text produces zero findings).

Tests live at the analyzer level — integration tests go through
``application.ScanService`` and live in ``tests/test_integration.py``.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from analyzers import TextFileAnalyzer
from analyzers.base import BaseAnalyzer
from domain import Finding, IntegrityReport
from infrastructure.file_router import FileKind


# ---------------------------------------------------------------------------
# Contract
# ---------------------------------------------------------------------------


def test_is_base_analyzer_subclass() -> None:
    assert issubclass(TextFileAnalyzer, BaseAnalyzer)


def test_class_attributes() -> None:
    assert TextFileAnalyzer.name == "text_file"
    assert TextFileAnalyzer.error_prefix == "Text file scan error"
    assert TextFileAnalyzer.source_layer == "zahir"


def test_supported_kinds_covers_text_family() -> None:
    expected = frozenset({FileKind.MARKDOWN, FileKind.CODE, FileKind.HTML})
    assert TextFileAnalyzer.supported_kinds == expected


def test_supported_kinds_excludes_pdf_and_json() -> None:
    # The router sends PDFs to the PDF analyzers and JSON to JsonAnalyzer;
    # TextFileAnalyzer must stay off those paths.
    assert FileKind.PDF not in TextFileAnalyzer.supported_kinds
    assert FileKind.JSON not in TextFileAnalyzer.supported_kinds


def test_instantiable() -> None:
    a = TextFileAnalyzer()
    assert a.name == "text_file"
    assert "TextFileAnalyzer" in repr(a)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write(tmp_path: Path, name: str, content: str) -> Path:
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


def _scan(path: Path) -> IntegrityReport:
    return TextFileAnalyzer().scan(path)


def _mechanisms(report: IntegrityReport) -> list[str]:
    return [f.mechanism for f in report.findings]


# ---------------------------------------------------------------------------
# Clean input
# ---------------------------------------------------------------------------


def test_clean_text_produces_no_findings(tmp_path: Path) -> None:
    p = _write(tmp_path, "clean.md", "# Hello\n\nPlain ASCII paragraph.\n")
    report = _scan(p)
    assert report.findings == []
    assert report.integrity_score == 1.0
    assert not report.scan_incomplete
    assert report.error is None


# ---------------------------------------------------------------------------
# Zero-width
# ---------------------------------------------------------------------------


def test_zero_width_detects_zwsp(tmp_path: Path) -> None:
    p = _write(tmp_path, "a.md", "Hello\u200bWorld\n")
    mechs = _mechanisms(_scan(p))
    assert "zero_width_chars" in mechs


def test_zero_width_finding_is_zahir(tmp_path: Path) -> None:
    p = _write(tmp_path, "a.md", "a\u200bb")
    (f,) = [x for x in _scan(p).findings if x.mechanism == "zero_width_chars"]
    assert f.source_layer == "zahir"
    assert "U+200B" in f.description


def test_zero_width_groups_per_line(tmp_path: Path) -> None:
    # Two zero-widths on the same line → one finding, count reflected
    # in description.
    p = _write(tmp_path, "a.md", "aa\u200bbb\u200bcc")
    zw = [x for x in _scan(p).findings if x.mechanism == "zero_width_chars"]
    assert len(zw) == 1
    assert "2 zero-width" in zw[0].description


# ---------------------------------------------------------------------------
# TAG block
# ---------------------------------------------------------------------------


def test_tag_chars_detects_unicode_tag_block(tmp_path: Path) -> None:
    payload = "".join(chr(0xE0000 + ord(c)) for c in "SECRET")
    p = _write(tmp_path, "a.md", "Hello" + payload)
    mechs = _mechanisms(_scan(p))
    assert "tag_chars" in mechs


def test_tag_chars_decodes_shadow(tmp_path: Path) -> None:
    payload = "".join(chr(0xE0000 + ord(c)) for c in "HIDDEN")
    p = _write(tmp_path, "a.md", payload)
    (f,) = [x for x in _scan(p).findings if x.mechanism == "tag_chars"]
    assert "'HIDDEN'" in f.description


def test_tag_chars_is_tier_1_highest_confidence(tmp_path: Path) -> None:
    payload = "".join(chr(0xE0000 + ord(c)) for c in "X")
    p = _write(tmp_path, "a.md", payload)
    (f,) = [x for x in _scan(p).findings if x.mechanism == "tag_chars"]
    assert f.tier == 1
    assert f.confidence == 1.0


# ---------------------------------------------------------------------------
# Bidi control
# ---------------------------------------------------------------------------


def test_bidi_control_detects_rlo(tmp_path: Path) -> None:
    # U+202E embedded in source — the Trojan Source pattern.
    p = _write(tmp_path, "a.py", "user" + "\u202E" + "admin\n")
    mechs = _mechanisms(_scan(p))
    assert "bidi_control" in mechs


# ---------------------------------------------------------------------------
# Homoglyph
# ---------------------------------------------------------------------------


def test_homoglyph_detects_cyrillic_a(tmp_path: Path) -> None:
    # 'admin' with Cyrillic 'а' (U+0430) replacing the Latin 'a'.
    p = _write(tmp_path, "a.md", "Welcome, \u0430dmin.")
    mechs = _mechanisms(_scan(p))
    assert "homoglyph" in mechs


def test_homoglyph_recovers_visible_string(tmp_path: Path) -> None:
    p = _write(tmp_path, "a.md", "\u0430dmin")
    (f,) = [x for x in _scan(p).findings if x.mechanism == "homoglyph"]
    assert "'admin'" in f.description
    assert f.source_layer == "zahir"


def test_homoglyph_does_not_fire_without_confusables(tmp_path: Path) -> None:
    # Cyrillic word whose letters are NOT in the confusables table
    # (я, з, ы, к — none impersonate Latin). No firing expected.
    p = _write(tmp_path, "a.md", "\u044F\u0437\u044B\u043A")
    mechs = _mechanisms(_scan(p))
    assert "homoglyph" not in mechs


def test_homoglyph_fires_on_multi_confusable_word(tmp_path: Path) -> None:
    # Pure Cyrillic word with 2+ confusables (р, у, с) — the detector
    # treats this as impersonation since any single word with multiple
    # Latin-lookalikes is more likely an attack than genuine Russian.
    # This mirrors v0.1's ZahirTextAnalyzer PDF-side behaviour.
    p = _write(tmp_path, "a.md", "\u0440\u0443\u0441\u0441")
    mechs = _mechanisms(_scan(p))
    assert "homoglyph" in mechs


# ---------------------------------------------------------------------------
# Read error path
# ---------------------------------------------------------------------------


def test_missing_file_returns_scan_error_report(tmp_path: Path) -> None:
    missing = tmp_path / "does_not_exist.md"
    report = _scan(missing)
    assert report.scan_incomplete
    assert report.error is not None
    assert report.error.startswith("Text file scan error")
    assert [f.mechanism for f in report.findings] == ["scan_error"]
    assert report.findings[0].source_layer == "zahir"


# ---------------------------------------------------------------------------
# Integration on Phase 9 fixtures
# ---------------------------------------------------------------------------


FIXTURE_ROOT = (
    Path(__file__).resolve().parents[1] / "fixtures" / "text_formats"
)


@pytest.mark.parametrize(
    "rel,expected",
    [
        ("clean/clean.md", []),
        ("clean/clean.py", []),
        ("adversarial/zero_width.md", ["zero_width_chars"]),
        ("adversarial/tag_chars.md", ["tag_chars"]),
        ("adversarial/bidi_control.py", ["bidi_control"]),
        ("adversarial/homoglyph.md", ["homoglyph"]),
    ],
)
def test_fixture_fires_exactly_expected(rel: str, expected: list[str]) -> None:
    path = FIXTURE_ROOT / rel
    if not path.exists():
        pytest.skip(f"fixture {rel} not yet generated")
    report = _scan(path)
    observed = sorted({f.mechanism for f in report.findings})
    assert observed == sorted(expected), (
        f"{rel}: expected {expected}, got {observed}"
    )

# Bismillah ir-Rahman ir-Rahim