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
Bayyinah domain layer.

Pure data types and pure operations. No I/O, no parser dependencies,
no global state. This package is the language in which the rest of
Bayyinah describes what it found — analyzers build ``Finding`` objects,
the scan service assembles them into an ``IntegrityReport``, the
reporting layer reads the report and renders it.

Phase 1 of the Al-Baqarah refactor. Additive-only: the legacy
``bayyinah_v0`` and ``bayyinah_v0_1`` modules continue to define their
own internal Finding / IntegrityReport shapes until later phases
migrate the analyzers onto this domain contract.
"""

from __future__ import annotations

from domain.config import (
    BATIN_MECHANISMS,
    CONFUSABLE_TO_LATIN,
    DEFAULT_LIMITS,
    MECHANISM_REGISTRY,
    ROUTING_MECHANISMS,
    SEVERITY,
    ScanLimits,
    TIER,
    TIER_LEGEND,
    TOOL_NAME,
    TOOL_VERSION,
    VERDICT_DISCLAIMER,
    VERDICT_MUGHLAQ,
    VERDICT_MUKHFI,
    VERDICT_MUNAFIQ,
    VERDICT_MUSHTABIH,
    VERDICT_SAHIH,
    ZAHIR_MECHANISMS,
    SourceLayer,
    Verdict,
    get_current_limits,
    limits_context,
    set_current_limits,
)
from domain.exceptions import (
    BayyinahError,
    InvalidFindingError,
    PDFParseError,
    ScanError,
)
from domain.content_index import (
    AnnotInfo,
    ContentIndex,
    DrawingInfo,
    FontInfo,
    PikepdfAnnotInfo,
    SpanInfo,
    content_index_context,
    get_current_content_index,
    set_current_content_index,
)
from domain.cost_classes import CostClass, MECHANISM_COST_CLASS, cost_class
from domain.finding import Finding, ROUTING_DISCLOSURE_KEYS
from domain.integrity_report import IntegrityReport
from domain.value_objects import (
    apply_scan_incomplete_clamp,
    compute_muwazana_score,
    tamyiz_verdict,
)

__all__ = [
    # Dataclasses
    "Finding",
    "IntegrityReport",
    # Pure functions
    "compute_muwazana_score",
    "tamyiz_verdict",
    "apply_scan_incomplete_clamp",
    # Exceptions
    "BayyinahError",
    "InvalidFindingError",
    "PDFParseError",
    "ScanError",
    # Config — most frequently imported members
    "MECHANISM_REGISTRY",
    "SEVERITY",
    "TIER",
    "TIER_LEGEND",
    "VERDICT_DISCLAIMER",
    "TOOL_NAME",
    "TOOL_VERSION",
    "ZAHIR_MECHANISMS",
    "BATIN_MECHANISMS",
    "ROUTING_MECHANISMS",
    "ROUTING_DISCLOSURE_KEYS",
    "CONFUSABLE_TO_LATIN",
    "SourceLayer",
    "Verdict",
    "VERDICT_SAHIH",
    "VERDICT_MUSHTABIH",
    "VERDICT_MUKHFI",
    "VERDICT_MUNAFIQ",
    "VERDICT_MUGHLAQ",
    # Phase 21 — configurable safety limits.
    "ScanLimits",
    "DEFAULT_LIMITS",
    "get_current_limits",
    "set_current_limits",
    "limits_context",
    # v1.1.4 — content index + cost-class taxonomy
    "ContentIndex",
    "SpanInfo",
    "FontInfo",
    "AnnotInfo",
    "PikepdfAnnotInfo",
    "DrawingInfo",
    "get_current_content_index",
    "set_current_content_index",
    "content_index_context",
    "CostClass",
    "MECHANISM_COST_CLASS",
    "cost_class",
]

# Bismillah ir-Rahman ir-Rahim