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
Tests for domain.value_objects — compute_muwazana_score and tamyiz_verdict.

Coverage targets:
  * compute_muwazana_score parity with bayyinah_v0.compute_integrity_score
  * clamp behaviour [0, 1]
  * tamyiz_verdict decision table, especially the mughlaq-first ordering
    and the tier-1 requirement for munafiq
  * apply_scan_incomplete_clamp identity
"""

from __future__ import annotations

import pytest

import bayyinah_v0
from domain.config import (
    SCAN_INCOMPLETE_CLAMP,
    VERDICT_MUGHLAQ,
    VERDICT_MUKHFI,
    VERDICT_MUNAFIQ,
    VERDICT_MUSHTABIH,
    VERDICT_SAHIH,
)
from domain.finding import Finding
from domain.integrity_report import IntegrityReport
from domain.value_objects import (
    apply_scan_incomplete_clamp,
    compute_muwazana_score,
    tamyiz_verdict,
)


# ---------------------------------------------------------------------------
# Muwazana — scoring
# ---------------------------------------------------------------------------

def test_muwazana_empty_list_scores_one() -> None:
    assert compute_muwazana_score([]) == 1.0


def test_muwazana_single_finding_subtracts_severity_times_confidence() -> None:
    f = Finding(mechanism="javascript", tier=1, confidence=1.0,
                description="d", location="l")
    # SEVERITY["javascript"] == 0.30, confidence == 1.0 → 1.0 - 0.30
    assert compute_muwazana_score([f]) == pytest.approx(0.70)


def test_muwazana_respects_severity_override() -> None:
    f = Finding(mechanism="javascript", tier=1, confidence=1.0,
                description="d", location="l",
                severity_override=0.1)
    assert compute_muwazana_score([f]) == pytest.approx(0.90)


def test_muwazana_clamps_at_zero() -> None:
    # Four javascript findings at full confidence: 1.0 - 4*0.30 = -0.20 → 0.0
    findings = [
        Finding(mechanism="javascript", tier=1, confidence=1.0,
                description="d", location=f"l{i}")
        for i in range(4)
    ]
    assert compute_muwazana_score(findings) == 0.0


def test_muwazana_clamps_at_one() -> None:
    """A negative-severity-override finding would theoretically push the
    score above 1.0; the clamp catches that."""
    f = Finding(mechanism="scan_error", tier=3, confidence=1.0,
                description="d", location="l", severity_override=0.0)
    # scan_error severity is 0.00 by default; no deduction. Score stays at 1.
    assert compute_muwazana_score([f]) == 1.0


def test_muwazana_matches_v0_compute_integrity_score() -> None:
    """The headline parity invariant for Phase 1 value objects:
    muwazana and compute_integrity_score must return identical floats
    on the same inputs."""
    domain_findings = [
        Finding(mechanism="zero_width_chars", tier=2, confidence=0.9,
                description="d", location="l"),
        Finding(mechanism="tag_chars", tier=1, confidence=1.0,
                description="d", location="l"),
        Finding(mechanism="javascript", tier=1, confidence=0.8,
                description="d", location="l"),
    ]
    v0_findings = [
        bayyinah_v0.Finding(mechanism="zero_width_chars", tier=2, confidence=0.9,
                            description="d", location="l"),
        bayyinah_v0.Finding(mechanism="tag_chars", tier=1, confidence=1.0,
                            description="d", location="l"),
        bayyinah_v0.Finding(mechanism="javascript", tier=1, confidence=0.8,
                            description="d", location="l"),
    ]
    assert compute_muwazana_score(domain_findings) == \
        bayyinah_v0.compute_integrity_score(v0_findings)


def test_muwazana_is_pure() -> None:
    """Double-invocation returns the same value and does not mutate the
    input list."""
    findings = [
        Finding(mechanism="javascript", tier=1, confidence=1.0,
                description="d", location="l"),
    ]
    before = list(findings)
    first = compute_muwazana_score(findings)
    second = compute_muwazana_score(findings)
    assert first == second
    assert findings == before


# ---------------------------------------------------------------------------
# Tamyiz — verdict derivation
# ---------------------------------------------------------------------------

def _report(score: float, findings: list[Finding], *,
            scan_incomplete: bool = False,
            error: str | None = None) -> IntegrityReport:
    return IntegrityReport(
        file_path="/tmp/x.pdf",
        integrity_score=score,
        findings=findings,
        scan_incomplete=scan_incomplete,
        error=error,
    )


def test_tamyiz_sahih_on_clean_report() -> None:
    r = _report(1.0, [])
    assert tamyiz_verdict(r) == VERDICT_SAHIH


def test_tamyiz_mughlaq_when_scan_incomplete() -> None:
    """An incomplete scan overrides any score-based classification,
    even a perfect one."""
    r = _report(1.0, [], scan_incomplete=True)
    assert tamyiz_verdict(r) == VERDICT_MUGHLAQ


def test_tamyiz_mughlaq_when_error_present() -> None:
    r = _report(0.95, [], error="something broke")
    assert tamyiz_verdict(r) == VERDICT_MUGHLAQ


def test_tamyiz_mughlaq_precedence_over_munafiq() -> None:
    """If both scan_incomplete AND low-score-with-tier1 are true,
    mughlaq wins: we cannot issue 'munafiq' on an unfinished scan."""
    f = Finding(mechanism="javascript", tier=1, confidence=1.0,
                description="d", location="l")
    r = _report(0.0, [f, f, f], scan_incomplete=True)
    assert tamyiz_verdict(r) == VERDICT_MUGHLAQ


def test_tamyiz_munafiq_requires_tier1() -> None:
    """Low score alone is NOT enough — we need a tier-1 (verified)
    finding to escalate to munafiq. Protects against false severe
    verdicts built purely from tier-2/3 accumulation."""
    # Stack tier-2 findings to drive score below 0.3 without any tier-1.
    f_t2 = [
        Finding(mechanism="zero_width_chars", tier=2, confidence=1.0,
                description="d", location=f"l{i}", severity_override=0.3)
        for i in range(4)
    ]
    r = _report(0.0, f_t2)
    # score is very low, but no tier-1 → mukhfi, NOT munafiq
    assert tamyiz_verdict(r) == VERDICT_MUKHFI


def test_tamyiz_munafiq_on_low_score_with_tier1() -> None:
    f_t1 = Finding(mechanism="javascript", tier=1, confidence=1.0,
                   description="d", location="l")
    f_t2 = Finding(mechanism="zero_width_chars", tier=2, confidence=1.0,
                   description="d", location="l")
    r = _report(0.1, [f_t1, f_t2, f_t2])
    assert tamyiz_verdict(r) == VERDICT_MUNAFIQ


def test_tamyiz_mukhfi_on_mid_range_score() -> None:
    f = Finding(mechanism="zero_width_chars", tier=2, confidence=0.9,
                description="d", location="l")
    r = _report(0.5, [f])
    assert tamyiz_verdict(r) == VERDICT_MUKHFI


def test_tamyiz_mushtabih_on_high_but_imperfect_score() -> None:
    f = Finding(mechanism="incremental_update", tier=3, confidence=1.0,
                description="d", location="l")
    r = _report(0.95, [f])
    assert tamyiz_verdict(r) == VERDICT_MUSHTABIH


def test_tamyiz_does_not_mutate_the_report() -> None:
    f = Finding(mechanism="javascript", tier=1, confidence=1.0,
                description="d", location="l")
    r = _report(0.7, [f])
    before_score = r.integrity_score
    before_len = len(r.findings)
    _ = tamyiz_verdict(r)
    assert r.integrity_score == before_score
    assert len(r.findings) == before_len


# ---------------------------------------------------------------------------
# apply_scan_incomplete_clamp
# ---------------------------------------------------------------------------

def test_clamp_identity_when_not_incomplete() -> None:
    assert apply_scan_incomplete_clamp(0.9, scan_incomplete=False) == 0.9


def test_clamp_identity_when_score_already_below_threshold() -> None:
    assert apply_scan_incomplete_clamp(0.3, scan_incomplete=True) == 0.3


def test_clamp_reduces_score_when_incomplete_and_high() -> None:
    assert apply_scan_incomplete_clamp(0.95, scan_incomplete=True) == SCAN_INCOMPLETE_CLAMP


def test_clamp_threshold_value() -> None:
    assert SCAN_INCOMPLETE_CLAMP == 0.5

# Bismillah ir-Rahman ir-Rahim