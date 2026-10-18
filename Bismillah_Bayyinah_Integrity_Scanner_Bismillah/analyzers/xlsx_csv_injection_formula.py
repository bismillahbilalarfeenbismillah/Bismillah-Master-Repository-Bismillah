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
Tier 1/2 detector for CSV-injection-style formula payloads in XLSX (v1.1.2).

A spreadsheet cell formula is stored in ``<c><f>...</f></c>`` inside
``xl/worksheets/sheet*.xml``. Two adversarial families ride this slot:

  * DDE / shell-trigger formulas: legacy Excel honours external
    application calls expressed as ``cmd|' /c <command>'!<cell>``,
    ``mshta|...!A1``, ``DDE(...)``, ``rundll32|...``. These execute a
    program when the workbook is opened (subject to user prompts in
    modern Excel). Tier 1 - byte-deterministic and never legitimate
    in a content-bearing spreadsheet.

  * HYPERLINK-with-display-payload: ``=HYPERLINK("<url>","<text>")``
    where the second argument carries hidden text that an automated
    consumer will read but a human cell viewer only sees as the
    rendered link label. The URL itself can be an exfiltration
    endpoint. Tier 2 because legitimate hyperlinks are common; the
    trigger is "URL is external AND display-text length exceeds the
    payload threshold OR contains payload markers".

Closes xlsx_gauntlet fixture 06_csv_injection_formula.xlsx.

Source layer is zahir because the formula text lives in the
worksheet part - the same surface as cell values - but the rendered
display does not show the formula body verbatim. (Excel renders a
link label or the result of a HYPERLINK call, not the formula
string.) The byte channel is on the visible surface; the *rendered*
text is what diverges.

Tier discipline: each finding is emitted with its own tier so the
mechanism count is recorded correctly. Tier 1 for shell-trigger
patterns, Tier 2 for HYPERLINK-with-payload patterns.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from domain.finding import Finding


_S_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_S_F = f"{{{_S_NS}}}f"
_S_C = f"{{{_S_NS}}}c"

_PREVIEW_LIMIT = 240
_HYPERLINK_PAYLOAD_MIN = 16

# Tier 1 shell-trigger patterns (DDE-style legacy execution channels).
# Matched case-insensitively against the formula body.
_SHELL_TRIGGER_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "cmd_pipe",
        re.compile(r"cmd\s*\|", re.IGNORECASE),
    ),
    (
        "mshta_pipe",
        re.compile(r"mshta\s*\|", re.IGNORECASE),
    ),
    (
        "rundll32_pipe",
        re.compile(r"rundll32\s*\|", re.IGNORECASE),
    ),
    (
        "powershell_pipe",
        re.compile(r"powershell\s*\|", re.IGNORECASE),
    ),
    (
        "dde_call",
        re.compile(r"\bDDE\s*\(", re.IGNORECASE),
    ),
)

# Tier 2 HYPERLINK pattern. Two-arg form
# ``HYPERLINK("url","display")``; we capture both.
_HYPERLINK_RE = re.compile(
    r"HYPERLINK\s*\(\s*\"([^\"]+)\"\s*,\s*\"([^\"]+)\"\s*\)",
    re.IGNORECASE,
)

# External URL hosts (any URL with an explicit scheme) are taken as
# eligible for the HYPERLINK trigger. Internal sheet references
# (``#Sheet1!A1``) are not.
_EXTERNAL_URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://")


def _scan_worksheet(
    xml_bytes: bytes,
    part_name: str,
    file_path: Path,
) -> list[Finding]:
    """Scan a single worksheet XML part for formula payloads."""
    findings: list[Finding] = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return findings
    for cell in root.iter(_S_C):
        ref = cell.get("r") or "?"
        f_el = cell.find(_S_F)
        if f_el is None or not f_el.text:
            continue
        body = f_el.text
        # Tier 1: shell-trigger patterns.
        for label, pattern in _SHELL_TRIGGER_PATTERNS:
            if pattern.search(body):
                preview = (
                    body if len(body) <= _PREVIEW_LIMIT
                    else body[:_PREVIEW_LIMIT] + "..."
                )
                findings.append(Finding(
                    mechanism="xlsx_csv_injection_formula",
                    tier=1,
                    confidence=1.0,
                    description=(
                        f"Cell {ref} formula in {part_name} matches "
                        f"shell-trigger pattern {label!r}. Legacy "
                        f"Excel honours such formulas as external "
                        f"application calls when the workbook is "
                        f"opened (subject to user prompts in modern "
                        f"Excel). Never legitimate in a content-"
                        f"bearing spreadsheet."
                    ),
                    location=f"{file_path}:{part_name}:{ref}",
                    surface=f"cell {ref} formula",
                    concealed=(
                        f"pattern={label}; "
                        f"formula body: {preview!r}"
                    ),
                    source_layer="zahir",
                ))
                break  # one Tier 1 finding per cell is enough
        # Tier 2: HYPERLINK with payload-like display text.
        for url, display in _HYPERLINK_RE.findall(body):
            if not _EXTERNAL_URL_RE.match(url):
                continue
            if len(display.strip()) < _HYPERLINK_PAYLOAD_MIN:
                continue
            preview_disp = (
                display if len(display) <= _PREVIEW_LIMIT
                else display[:_PREVIEW_LIMIT] + "..."
            )
            findings.append(Finding(
                mechanism="xlsx_csv_injection_formula",
                tier=2,
                confidence=1.0,
                description=(
                    f"Cell {ref} formula in {part_name} contains a "
                    f"HYPERLINK to an external URL with a "
                    f"{len(display)}-character display text. The "
                    f"display text is rendered as the cell label "
                    f"while the URL drives the click target; long "
                    f"display text is structurally suitable for "
                    f"carrying a payload that automated consumers "
                    f"read but human viewers do not interpret."
                ),
                location=f"{file_path}:{part_name}:{ref}",
                surface=f"cell {ref} HYPERLINK formula",
                concealed=(
                    f"url={url!r}; display: {preview_disp!r}"
                ),
                source_layer="zahir",
            ))
    return findings


def detect_xlsx_csv_injection_formula(
    file_path: Path,
) -> list[Finding]:
    """Return findings for cells whose formula body matches a
    shell-trigger pattern (Tier 1) or a HYPERLINK with payload-
    length display text (Tier 2).
    """
    findings: list[Finding] = []
    try:
        with zipfile.ZipFile(str(file_path), "r") as zf:
            for name in zf.namelist():
                if not (
                    name.startswith("xl/worksheets/")
                    and name.endswith(".xml")
                ):
                    continue
                try:
                    xml_bytes = zf.read(name)
                except KeyError:
                    continue
                findings.extend(
                    _scan_worksheet(xml_bytes, name, file_path)
                )
    except (zipfile.BadZipFile, OSError):
        return findings
    return findings


__all__ = ["detect_xlsx_csv_injection_formula"]

# Bismillah ir-Rahman ir-Rahim