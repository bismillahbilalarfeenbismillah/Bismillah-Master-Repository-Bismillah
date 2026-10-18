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
Tests for infrastructure.report_formatter.

Coverage targets:
  * ReportFormatter ABC contract — cannot instantiate, empty name
    subclass rejected
  * TerminalReportFormatter produces the exact v0.1 text format
    (parity with bayyinah_v0_1.format_text_report)
  * JsonReportFormatter serialises to valid JSON equivalent to
    bayyinah_v0_1's json.dumps(to_dict(), indent=2, default=str)
  * PlainLanguageFormatter returns the one-paragraph summary alone
  * FormatterRegistry register / unregister / lookup / collision
  * default_formatter_registry contains the three Phase 3 formatters
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

import bayyinah_v0_1
from domain import Finding, IntegrityReport
from infrastructure.report_formatter import (
    FormatterRegistrationError,
    FormatterRegistry,
    JsonReportFormatter,
    PlainLanguageFormatter,
    ReportFormatter,
    TerminalReportFormatter,
    default_formatter_registry,
    plain_language_summary,
    registered,
)


# ---------------------------------------------------------------------------
# Report builders
# ---------------------------------------------------------------------------

def _clean_report() -> IntegrityReport:
    return IntegrityReport(file_path="/tmp/clean.pdf", integrity_score=1.0)


def _one_finding_report() -> IntegrityReport:
    f = Finding(
        mechanism="zero_width_chars",
        tier=1,
        confidence=0.95,
        description="2 zero-width char(s) embedded in rendered text",
        location="page 1, span 3",
        surface="Hello",
        concealed="H\u200be\u200bl\u200bl\u200bo",
    )
    return IntegrityReport(
        file_path="/tmp/a.pdf",
        integrity_score=0.73,
        findings=[f],
    )


def _incomplete_report() -> IntegrityReport:
    return IntegrityReport(
        file_path="/tmp/broken.pdf",
        integrity_score=0.5,
        error="Object layer scan error: pypdf could not open",
        scan_incomplete=True,
    )


# ---------------------------------------------------------------------------
# ABC contract
# ---------------------------------------------------------------------------

def test_report_formatter_cannot_be_instantiated_directly() -> None:
    with pytest.raises(TypeError):
        ReportFormatter()  # type: ignore[abstract]


def test_concrete_subclass_with_empty_name_is_rejected() -> None:
    with pytest.raises(TypeError, match="name"):
        class _NoName(ReportFormatter):
            # name omitted intentionally
            def format(self, report: IntegrityReport) -> str:
                return ""


def test_intermediate_abstract_subclass_is_exempt() -> None:
    from abc import abstractmethod

    class _Intermediate(ReportFormatter):
        # no name — fine because still abstract
        @abstractmethod
        def format(self, report: IntegrityReport) -> str:  # type: ignore[override]
            ...

    class _Leaf(_Intermediate):
        name = "leaf"

        def format(self, report: IntegrityReport) -> str:
            return "leaf"

    assert _Leaf().format(_clean_report()) == "leaf"


# ---------------------------------------------------------------------------
# PlainLanguageFormatter
# ---------------------------------------------------------------------------

def test_plain_formatter_returns_summary_paragraph() -> None:
    fmt = PlainLanguageFormatter()
    assert fmt.format(_clean_report()) == plain_language_summary(_clean_report())
    assert "No concealment mechanisms detected" in fmt.format(_clean_report())


def test_plain_formatter_matches_v0_1_summary() -> None:
    """Byte-for-byte parity check against v0.1's plain_language_summary."""
    for report in (_clean_report(), _one_finding_report(), _incomplete_report()):
        ours = PlainLanguageFormatter().format(report)
        v0_1_shape = _build_v0_1_report(report)
        theirs = bayyinah_v0_1.plain_language_summary(v0_1_shape)
        assert ours == theirs


# ---------------------------------------------------------------------------
# TerminalReportFormatter — byte-identical to v0.1
# ---------------------------------------------------------------------------

def test_terminal_formatter_matches_v0_1_for_clean_report() -> None:
    report = _clean_report()
    ours = TerminalReportFormatter().format(report)
    theirs = bayyinah_v0_1.format_text_report(_build_v0_1_report(report))
    assert ours == theirs


def test_terminal_formatter_matches_v0_1_for_finding_report() -> None:
    report = _one_finding_report()
    ours = TerminalReportFormatter().format(report)
    theirs = bayyinah_v0_1.format_text_report(_build_v0_1_report(report))
    assert ours == theirs


def test_terminal_formatter_matches_v0_1_for_incomplete_report() -> None:
    report = _incomplete_report()
    ours = TerminalReportFormatter().format(report)
    theirs = bayyinah_v0_1.format_text_report(_build_v0_1_report(report))
    assert ours == theirs


def test_terminal_formatter_contains_banner_and_subbar() -> None:
    out = TerminalReportFormatter().format(_clean_report())
    assert "BAYYINAH v0.1" in out
    assert "=" * 76 in out
    assert "-" * 76 in out
    assert "PLAIN-LANGUAGE SUMMARY" in out


def test_terminal_formatter_lists_findings_section() -> None:
    out = TerminalReportFormatter().format(_one_finding_report())
    assert "FINDINGS  (1)" in out
    assert "zero_width_chars" in out
    assert "Inversion recovery" in out


# ---------------------------------------------------------------------------
# JsonReportFormatter — structurally equivalent to v0.1
# ---------------------------------------------------------------------------

def test_json_formatter_parses_back_to_to_dict_shape() -> None:
    report = _one_finding_report()
    emitted = JsonReportFormatter().format(report)
    parsed = json.loads(emitted)
    assert parsed == report.to_dict()


def test_json_formatter_matches_v0_1_json_shape_for_clean() -> None:
    """v0.1 keys are a prefix subset of the modular formatter's output;
    on the shared keys the values are byte-identical. The two
    additional v1.2.0 keys (scan_complete, coverage) are present and
    well-typed but not compared against v0.1 (which does not emit
    them). See PARITY.md and CHANGELOG.md.
    """
    report = _clean_report()
    ours = json.loads(JsonReportFormatter().format(report))
    theirs = json.loads(
        json.dumps(_build_v0_1_report(report).to_dict(), indent=2, default=str)
    )
    # Restrict to v0.1 keys for the byte-identical check.
    ours_v01_only = {k: ours[k] for k in theirs.keys()}
    assert ours_v01_only == theirs
    assert "scan_complete" in ours and isinstance(ours["scan_complete"], bool)
    assert "coverage" in ours


def test_json_formatter_matches_v0_1_json_shape_for_findings() -> None:
    """Same prefix-subset shape as the clean variant (see PARITY.md)."""
    report = _one_finding_report()
    ours = json.loads(JsonReportFormatter().format(report))
    theirs = json.loads(
        json.dumps(_build_v0_1_report(report).to_dict(), indent=2, default=str)
    )
    ours_v01_only = {k: ours[k] for k in theirs.keys()}
    assert ours_v01_only == theirs
    assert "scan_complete" in ours and isinstance(ours["scan_complete"], bool)
    assert "coverage" in ours


def test_json_formatter_indents_two_spaces() -> None:
    out = JsonReportFormatter().format(_clean_report())
    # 2-space indent — the first nested line starts with "  "
    lines = out.split("\n")
    # Find a nested line
    nested = [ln for ln in lines if ln.startswith("  ") and not ln.startswith("    ")]
    assert nested, "Expected at least one 2-space-indented line"


# ---------------------------------------------------------------------------
# FormatterRegistry
# ---------------------------------------------------------------------------

def test_registry_starts_empty() -> None:
    reg = FormatterRegistry()
    assert len(reg) == 0
    assert reg.names() == []


def test_register_accepts_formatter_subclass() -> None:
    reg = FormatterRegistry()
    reg.register(TerminalReportFormatter)
    assert "terminal" in reg
    assert reg.get("terminal") is TerminalReportFormatter
    assert reg.names() == ["terminal"]


def test_register_rejects_non_subclass() -> None:
    reg = FormatterRegistry()

    class NotAFormatter:
        name = "nope"

    with pytest.raises(FormatterRegistrationError, match="ReportFormatter subclass"):
        reg.register(NotAFormatter)  # type: ignore[arg-type]


def test_register_rejects_collision() -> None:
    reg = FormatterRegistry()
    reg.register(TerminalReportFormatter)
    with pytest.raises(FormatterRegistrationError, match="already registered"):
        reg.register(TerminalReportFormatter)


def test_register_can_be_used_as_decorator() -> None:
    reg = FormatterRegistry()

    @reg.register
    class MyFmt(ReportFormatter):
        name = "my"

        def format(self, report: IntegrityReport) -> str:
            return "my"

    assert "my" in reg
    assert reg.get("my") is MyFmt


def test_registered_decorator_factory_binds_registry() -> None:
    reg = FormatterRegistry()

    @registered(reg)
    class Another(ReportFormatter):
        name = "another"

        def format(self, report: IntegrityReport) -> str:
            return ""

    assert reg.get("another") is Another


def test_unregister_removes_formatter() -> None:
    reg = FormatterRegistry()
    reg.register(TerminalReportFormatter)
    reg.unregister("terminal")
    assert "terminal" not in reg


def test_unregister_missing_is_noop() -> None:
    reg = FormatterRegistry()
    reg.unregister("ghost")  # must not raise


def test_clear_drops_everything() -> None:
    reg = FormatterRegistry()
    reg.register(TerminalReportFormatter)
    reg.register(JsonReportFormatter)
    reg.clear()
    assert len(reg) == 0


def test_get_raises_keyerror_on_missing() -> None:
    reg = FormatterRegistry()
    with pytest.raises(KeyError, match="ghost"):
        reg.get("ghost")


def test_format_convenience_dispatches() -> None:
    reg = FormatterRegistry()
    reg.register(PlainLanguageFormatter)
    out = reg.format("plain", _clean_report())
    assert "No concealment mechanisms detected" in out


# ---------------------------------------------------------------------------
# default_formatter_registry
# ---------------------------------------------------------------------------

def test_default_registry_has_three_formatters() -> None:
    reg = default_formatter_registry()
    assert set(reg.names()) == {"terminal", "json", "plain"}


def test_default_registry_instances_are_independent() -> None:
    a = default_formatter_registry()
    b = default_formatter_registry()
    a.unregister("terminal")
    assert "terminal" not in a
    assert "terminal" in b  # unaffected


# ---------------------------------------------------------------------------
# Helpers: translate a domain.IntegrityReport into a bayyinah_v0_1 shape.
# ---------------------------------------------------------------------------

def _build_v0_1_report(report: IntegrityReport) -> bayyinah_v0_1.IntegrityReport:
    """Build a v0.1 IntegrityReport with identical visible state, so we
    can compare our Phase 3 formatter output to the original."""
    v01_findings = []
    for f in report.findings:
        v01_findings.append(
            bayyinah_v0_1.Finding(
                mechanism=f.mechanism,
                tier=f.tier,
                confidence=f.confidence,
                description=f.description,
                location=f.location,
                surface=f.surface,
                concealed=f.concealed,
            )
        )
    return bayyinah_v0_1.IntegrityReport(
        file_path=report.file_path,
        integrity_score=report.integrity_score,
        findings=v01_findings,
        error=report.error,
        scan_incomplete=report.scan_incomplete,
    )

# Bismillah ir-Rahman ir-Rahim