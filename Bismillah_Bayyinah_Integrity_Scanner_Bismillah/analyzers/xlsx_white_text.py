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
Tier 1 detector for white-on-white cell text in XLSX (v1.1.2).

OOXML spreadsheet cells reference style indices via ``<c s="N">`` on
``xl/worksheets/sheet*.xml``. The style index points into the
``cellXfs`` array of ``xl/styles.xml``, which references a font
record carrying ``<color rgb="HHHHHH"/>``. A cell rendered with
``FFFFFFFF`` (alpha=FF, RGB=FFFFFF) on a default white fill is
invisible to a human reader but preserved verbatim in the cell's
``<is><t>`` (inline string) or shared-string reference, so every
downstream extractor (Excel's accessibility view, indexers, LLMs,
copy-paste, CSV exports) reads the payload.

Mirrors the PDF analyzer's ``white_on_white_text`` mechanism and the
DOCX analyzer's ``docx_white_text``. Closes xlsx_gauntlet fixture
01_white_cell_text.xlsx.

Tier discipline: Tier 1 because the trigger is byte-deterministic.
The font color hex compared against the near-white set is a literal
lookup, no statistical claim, no heuristic threshold. Source layer
is zahir because color is a surface-rendering attribute observable
from a single walk of the styles + cell graph.

Fill-color caveat: this detector only fires when the cell's resolved
font color is near-white. It does not check the fill (background)
color separately because the gauntlet fixture and the overwhelming
majority of real-world adversarial spreadsheets render against the
default white fill. Custom-fill-aware logic is queued as future work.

The "near-white" set covers exact ``FFFFFF`` plus three common
near-white variations seen in real-world adversarial fixtures
(``FEFEFE``, ``FDFDFD``, ``FCFCFC``). Anything darker than ``FCFCFC``
is treated as legitimate light-gray formatting and not flagged.
"""
from __future__ import annotations

import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from analyzers.xlsx_styles_resolver import (
    load_styles_from_zip,
    resolve_cell_font,
)
from domain.finding import Finding


_S_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_S_C = f"{{{_S_NS}}}c"
_S_IS = f"{{{_S_NS}}}is"
_S_T = f"{{{_S_NS}}}t"
_S_V = f"{{{_S_NS}}}v"

_NEAR_WHITE: frozenset[str] = frozenset(
    {"FFFFFF", "FEFEFE", "FDFDFD", "FCFCFC"}
)
_PREVIEW_LIMIT = 240


def _is_near_white(hex_val: str | None) -> bool:
    if not hex_val or len(hex_val) != 6:
        return False
    return hex_val.upper() in _NEAR_WHITE


def _cell_text(cell: ET.Element) -> str:
    """Return the inline-string text of a cell, or empty string for
    formulas / numeric values / shared-string refs (those are scanned
    by ``xlsx_csv_injection_formula`` and the existing shared-string
    walker; this detector targets inline strings the cell renders
    directly)."""
    is_el = cell.find(_S_IS)
    if is_el is None:
        return ""
    chunks: list[str] = []
    for t in is_el.iter(_S_T):
        if t.text:
            chunks.append(t.text)
    return "".join(chunks).strip()


def detect_xlsx_white_text(file_path: Path) -> list[Finding]:
    """Return Tier 1 findings for cells whose resolved font color
    renders the cell invisible against the default white fill.
    """
    findings: list[Finding] = []
    try:
        with zipfile.ZipFile(str(file_path), "r") as zf:
            fonts, cell_xfs = load_styles_from_zip(zf)
            if not fonts or not cell_xfs:
                return findings
            sheet_parts = sorted(
                n for n in zf.namelist()
                if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")
            )
            for sheet_part in sheet_parts:
                try:
                    xml_bytes = zf.read(sheet_part)
                except KeyError:
                    continue
                try:
                    root = ET.fromstring(xml_bytes)
                except ET.ParseError:
                    continue
                for cell in root.iter(_S_C):
                    s_attr = cell.get("s")
                    try:
                        s_id = int(s_attr) if s_attr is not None else None
                    except ValueError:
                        s_id = None
                    if s_id is None:
                        continue
                    font = resolve_cell_font(s_id, fonts, cell_xfs)
                    if not _is_near_white(font.color):
                        continue
                    text = _cell_text(cell)
                    if not text:
                        continue
                    cell_ref = cell.get("r") or "?"
                    preview = (
                        text if len(text) <= _PREVIEW_LIMIT
                        else text[:_PREVIEW_LIMIT] + "..."
                    )
                    findings.append(Finding(
                        mechanism="xlsx_white_text",
                        tier=1,
                        confidence=1.0,
                        description=(
                            f"Cell {cell_ref} in {sheet_part} has "
                            f"font color #{font.color} on the default "
                            f"white fill. The text is invisible to a "
                            f"human reading the spreadsheet but is "
                            f"preserved in the cell's inline-string "
                            f"and read by every downstream extractor "
                            f"including CSV exports and LLM ingestion."
                        ),
                        location=f"{file_path}:{sheet_part}:{cell_ref}",
                        surface=(
                            f"cell {cell_ref} with font color "
                            f"#{font.color}"
                        ),
                        concealed=(
                            f"color=#{font.color}; "
                            f"recovered text: {preview!r}"
                        ),
                        source_layer="zahir",
                    ))
    except (zipfile.BadZipFile, OSError):
        return findings
    return findings


__all__ = ["detect_xlsx_white_text"]

# Bismillah ir-Rahman ir-Rahim