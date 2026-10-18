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
csv_bidi_payload -- v1.1.2 F2 mechanism 4 (zahir).

Al-Baqarah 2:42 applied to bidi-override codepoint smuggling. Unicode
defines a small set of bidirectional control codepoints:

  * U+202A through U+202E -- LRE / RLE / PDF / LRO / RLO. Embedding
    and override marks. RLO ("right-to-left override") forces the
    visual rendering of the following text to be reversed; LRO does
    the same in the other direction.
  * U+2066 through U+2069 -- LRI / RLI / FSI / PDI. Isolate marks
    introduced in Unicode 6.3 with stricter scoping.

In a CSV cell these codepoints are byte-deterministic anomalies. A
spreadsheet renderer (Excel, LibreOffice Calc, Google Sheets) honours
the bidi algorithm: a cell whose bytes read "=Total: 1000" with an
RLO injected can render on screen as "0001 :latoT=" while the parser,
the diff tool, and the forensics reader all see the original bytes.
The surface (visible glyph order) and the bytes (parser input)
diverge in the most literal way.

Detector contract (per docs/adversarial/csv_json_gauntlet/REPORT.md
section 3.4):

  * For each cell, scan for any codepoint in U+202A..U+202E or
    U+2066..U+2069.
  * Emit one finding per cell that carries one or more bidi
    codepoints.

Tier 1 zahir (the spreadsheet-rendered surface diverges from the
byte stream). Severity 0.25.

Reference: Munafiq Protocol Sec. 9. DOI: 10.5281/zenodo.19677111.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import Iterable

from domain import Finding
from domain.config import BIDI_CONTROL_CHARS, TIER


def _bidi_codepoints_in(value: str) -> list[str]:
    """Return ordered list of bidi codepoints (as 'U+XXXX' strings)."""
    return [
        f"U+{ord(ch):04X}"
        for ch in value
        if ch in BIDI_CONTROL_CHARS
    ]


def detect_bidi_payload(
    text: str,
    delimiter: str,
    file_path: Path,
) -> Iterable[Finding]:
    """Yield csv_bidi_payload findings.

    ``text`` is the already-decoded CSV body. ``delimiter`` is the
    inferred delimiter from the base analyzer.
    """
    reader = csv.reader(io.StringIO(text), delimiter=delimiter)
    rows = list(reader)
    if not rows:
        return
    header = rows[0]
    for row_offset, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            codepoints = _bidi_codepoints_in(cell)
            if not codepoints:
                continue
            header_name = (
                header[col_index] if col_index < len(header) else ""
            )
            yield Finding(
                mechanism="csv_bidi_payload",
                tier=TIER["csv_bidi_payload"],
                confidence=0.95,
                description=(
                    f"Cell at row {row_offset}, column {col_index} "
                    f"({header_name!r}) carries "
                    f"{len(codepoints)} Unicode bidi control "
                    f"codepoint(s): {codepoints}. The bidi "
                    "algorithm reorders the visual rendering of the "
                    "surrounding text in spreadsheet renderers "
                    "(Excel, LibreOffice Calc, Google Sheets); the "
                    "on-screen glyph order can differ from the byte "
                    "order. There is no legitimate use of bidi "
                    "override codepoints inside a CSV data cell."
                ),
                location=f"{file_path}:row={row_offset},col={col_index}",
                surface=(
                    f"(cell carries bidi codepoints: "
                    f"{codepoints})"
                ),
                concealed=cell[:240],
                source_layer="zahir",
            )

# Bismillah ir-Rahman ir-Rahim