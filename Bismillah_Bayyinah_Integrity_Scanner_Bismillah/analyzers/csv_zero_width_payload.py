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
csv_zero_width_payload -- v1.1.2 F2 mechanism 5 (zahir).

Al-Baqarah 2:42 applied to zero-width codepoint smuggling. The
following codepoints render as no glyph at all in spreadsheet
viewers, text editors, and web browsers, but they survive every
copy-paste and every parse:

  * U+200B  ZERO WIDTH SPACE
  * U+200C  ZERO WIDTH NON-JOINER
  * U+200D  ZERO WIDTH JOINER
  * U+FEFF  ZERO WIDTH NO-BREAK SPACE / BOM (only when it appears
            mid-stream; a single leading BOM at file-start byte 0
            is a legitimate UTF-8 marker and is exempt).

Classified ZAHIR for consistency with v1.1.1 ``zero_width_chars``
on the same codepoint class. The codepoint is observable from a
single deterministic walk of the rendered cell-text content: the
codepoint IS in the text stream, the spreadsheet renderer simply
renders zero pixels for it. That is the v4.1 single-walk surface-
readability test for zahir. The cell text on the surface (zero
pixels) and the cell text in the bytes (the codepoint) diverge,
which is the zahir surface-vs-bytes shape.

Detector contract (per docs/adversarial/csv_json_gauntlet/REPORT.md
section 3.5):

  * For each cell, scan for any codepoint in the zero-width set.
  * Mid-stream U+FEFF counts; file-start BOM does not (the base
    decoder strips it before this module sees ``text``).
  * Emit one finding per cell that triggers.

Tier 1 zahir. Severity 0.20.

Reference: Munafiq Protocol Sec. 9. DOI: 10.5281/zenodo.19677111.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import Iterable

from domain import Finding
from domain.config import TIER, ZERO_WIDTH_CHARS


def _zero_width_codepoints_in(value: str) -> list[str]:
    """Return ordered list of zero-width codepoints (as 'U+XXXX')."""
    return [
        f"U+{ord(ch):04X}"
        for ch in value
        if ch in ZERO_WIDTH_CHARS
    ]


def detect_zero_width_payload(
    text: str,
    delimiter: str,
    file_path: Path,
) -> Iterable[Finding]:
    """Yield csv_zero_width_payload findings.

    ``text`` is the already-decoded CSV body with any leading BOM
    already stripped by the base decoder. ``delimiter`` is the
    inferred delimiter from the orchestrator.
    """
    reader = csv.reader(io.StringIO(text), delimiter=delimiter)
    rows = list(reader)
    if not rows:
        return
    header = rows[0]
    for row_offset, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            codepoints = _zero_width_codepoints_in(cell)
            if not codepoints:
                continue
            header_name = (
                header[col_index] if col_index < len(header) else ""
            )
            yield Finding(
                mechanism="csv_zero_width_payload",
                tier=TIER["csv_zero_width_payload"],
                confidence=0.95,
                description=(
                    f"Cell at row {row_offset}, column {col_index} "
                    f"({header_name!r}) carries "
                    f"{len(codepoints)} zero-width codepoint(s): "
                    f"{codepoints}. Zero-width characters render "
                    "as no glyph in every viewer (spreadsheet, "
                    "text editor, browser). The cell looks clean; "
                    "the bytes carry the payload. There is no "
                    "legitimate use of zero-width codepoints "
                    "inside a CSV data cell."
                ),
                location=f"{file_path}:row={row_offset},col={col_index}",
                surface=(
                    f"(cell carries zero-width codepoints: "
                    f"{codepoints})"
                ),
                concealed=cell[:240],
                source_layer="zahir",
            )

# Bismillah ir-Rahman ir-Rahim