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
Bayyinah analyzers package — the middle-community layer (Al-Baqarah 2:143).

Every analyzer inherits a uniform contract (``BaseAnalyzer``) and is
composed by a uniform registry (``AnalyzerRegistry``). That is the whole
package. Concrete analyzers for text and object layers arrive in later
phases; Phase 2 establishes only the contract and the composer.

Additive-only: nothing in this package is imported by
``bayyinah_v0.py`` or ``bayyinah_v0_1.py``. They continue to use their
own internal BaseAnalyzer / ScanService.
"""

from __future__ import annotations

from analyzers.audio_analyzer import AudioAnalyzer
from analyzers.base import BaseAnalyzer
from analyzers.registry import (
    AnalyzerRegistrationError,
    AnalyzerRegistry,
    registered,
)
from analyzers.correlation import CorrelationEngine, extract_payload
from analyzers.cross_modal_correlation import CrossModalCorrelationEngine
from analyzers.csv_analyzer import CsvAnalyzer
from analyzers.docx_analyzer import DocxAnalyzer
from analyzers.eml_analyzer import EmlAnalyzer
from analyzers.fallback_analyzer import FallbackAnalyzer
from analyzers.html_analyzer import HtmlAnalyzer
from analyzers.image_analyzer import ImageAnalyzer
from analyzers.json_analyzer import JsonAnalyzer
from analyzers.object_analyzer import BatinObjectAnalyzer
from analyzers.pptx_analyzer import PptxAnalyzer
from analyzers.svg_analyzer import SvgAnalyzer
from analyzers.text_analyzer import ZahirTextAnalyzer
from analyzers.text_file_analyzer import TextFileAnalyzer
from analyzers.video_analyzer import VideoAnalyzer
from analyzers.xlsx_analyzer import XlsxAnalyzer
# v1.1.2 - Tier 0 routing transparency (Mughlaq Trap closure).
from analyzers.format_routing import detect_format_routing_divergence

__all__ = [
    "BaseAnalyzer",
    "AnalyzerRegistry",
    "AnalyzerRegistrationError",
    "registered",
    "ZahirTextAnalyzer",
    "BatinObjectAnalyzer",
    "TextFileAnalyzer",
    "JsonAnalyzer",
    "ImageAnalyzer",
    "SvgAnalyzer",
    # Phase 12 — cross-modal correlation.
    "CorrelationEngine",
    "extract_payload",
    # Phase 15 — DOCX support.
    "DocxAnalyzer",
    # Phase 16 — HTML support (Al-Baqarah 2:42: do not mix truth with
    # falsehood). HTML is the format that most literally mixes visible
    # content (zahir) with concealed structure (batin).
    "HtmlAnalyzer",
    # Phase 17 — XLSX support (Al-Baqarah 2:79: "Woe to those who
    # write the book with their own hands..."). Spreadsheets are
    # structured, numerical, trustworthy-looking surfaces that can be
    # written with hidden macros, embedded objects, revision history,
    # and concealed payloads, then presented as clean input.
    "XlsxAnalyzer",
    # Phase 18 — PPTX support (Al-Baqarah 2:79, extended to the
    # presentation surface; Al-Baqarah 2:14: "When they meet those who
    # believe, they say, 'We believe,' but when they are alone with
    # their devils, they say, 'Indeed, we are with you'"). Presentations
    # ship three audiences at once — the room that watches the slides,
    # the presenter who reads the notes, and the AI ingestion pipeline
    # that reads both — and the format lets those three readers see
    # three different documents.
    "PptxAnalyzer",
    # Phase 19 — EML (email) support (Al-Baqarah 2:42: "Do not mix
    # truth with falsehood, nor conceal the truth while you know it").
    # Email is the canonical adversarial surface: a human reads the
    # rendered HTML body while the MIME tree carries a divergent
    # text/plain part, headers smuggle CRLF injection and RFC 2047
    # encoded-word subjects, display names impersonate trusted brands,
    # and attachments carry executables, macros, or nested .eml
    # payloads that recurse into the same integrity discipline.
    "EmlAnalyzer",
    # Phase 20 — CSV / TSV / delimited-data support (Al-Baqarah 2:42
    # applied to the tabular surface). Delimited-data files are the
    # format where the human reader and the automated parser most
    # literally disagree: the spreadsheet-app reader sees rendered cells
    # (where ``=HYPERLINK(...)`` displays as a clickable link and
    # exfiltrates on click), the text-editor reader sees the raw
    # formula source, and downstream data pipelines silently skip
    # comment rows, pad ragged columns, or truncate at null bytes.
    # CsvAnalyzer is the witness that surfaces those divergences.
    "CsvAnalyzer",
    # Phase 21 — the universal witness of last resort (Al-Baqarah 2:143).
    # Any file the router leaves unclassified (FileKind.UNKNOWN) would
    # otherwise slip through as silent-clean; FallbackAnalyzer guarantees
    # every such file produces an ``unknown_format`` finding with the
    # metadata a forensics reader needs (magic bytes, extension, size,
    # first-512-bytes preview). "Absence of findings in a file we could
    # not identify is not evidence of cleanness." The analyzer marks the
    # scan incomplete so the 0.5 clamp applies — honest about what was
    # not inspected.
    "FallbackAnalyzer",
    # Phase 24 — video containers (MP4 / MOV / WEBM / MKV).
    # Al-Baqarah 2:19-20: the rainstorm in which is darkness, thunder,
    # and lightning. The visible playback dominates attention while the
    # container's stems — subtitles, metadata atoms, attachments, cover
    # art, trailing bytes — carry concealment the viewer never sees.
    # VideoAnalyzer decomposes the container and routes each stem to
    # the analyzer that already handles its material (subtitle text →
    # ZahirTextAnalyzer's codepoint primitives; cover-art images →
    # ImageAnalyzer's LSB / trailing-data detectors). Composition, not
    # duplication, per the session prompt's Step 7.
    "VideoAnalyzer",
    # Phase 24 — audio containers (MP3 / WAV / FLAC / M4A / OGG).
    # Al-Baqarah 2:93: "They said: 'We hear and disobey.'" Audio
    # declares compliance at the surface (what the listener hears)
    # while the container's batin stems carry payloads the ear cannot
    # reach. Identity theft through voice cloning is tazwir and
    # iftira' (Al-Nisa 4:112). AudioAnalyzer follows the same stem-
    # extractor-and-router pattern as Phase 23 video: mutagen extracts
    # the stems the container already separates, and each stem is
    # routed to the analyzer that already knows how to read that
    # material (text → ZahirTextAnalyzer; embedded pictures →
    # ImageAnalyzer; WAV/FLAC PCM LSBs → stdlib statistics).
    "AudioAnalyzer",
    # Phase 25+ — cross-modal correlation post-processor. Reads the
    # stems the Phase 23/24 analyzers already separated (Al-Baqarah
    # 2:50) and applies reasoning logic across them (2:164 — "signs
    # for a people who use reason"). Opt-in invocation in session 1;
    # not wired into ScanService's default_registry while the rule
    # set is still being calibrated.
    "CrossModalCorrelationEngine",
    # v1.1.2 - Tier 0 routing transparency. Runs before any per-format
    # analyzer; emits a single Finding when the routing decision is
    # itself in dispute (extension/magic divergence, content-depth
    # below floor, unknown format, OOXML internal-path divergence).
    # The verdict resolver in domain.value_objects.tamyiz_verdict
    # floors at mughlaq when this finding is present. See
    # docs/adversarial/mughlaq_trap_REPORT.md.
    "detect_format_routing_divergence",
]

# Bismillah ir-Rahman ir-Rahim