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
Shared style-resolution helper for XLSX zahir detectors (v1.1.2).

OOXML cells reference a style index via the ``s`` attribute on
``<c>`` elements. The index points into ``xl/styles.xml`` ``cellXfs``,
which in turn references a font via ``fontId``. The font record
carries ``<color>`` and ``<sz>``. Two surface concealment vectors
ride this chain: a near-white font color renders the cell invisible
on the default white fill, and a microscopic ``sz`` renders the cell
unreadable. Both vectors share the same resolver, so the resolver is
hoisted into a single helper module that ``xlsx_white_text`` and
``xlsx_microscopic_font`` both import.

XLSX color values use ``rgb="AARRGGBB"`` (8-hex with alpha) or
``rgb="RRGGBB"`` (6-hex no alpha) depending on the writer. The
resolver strips a leading 2-hex alpha before comparing, so both
forms compare cleanly against the near-white set.

Sizes use the ``val`` attribute on ``<sz>``, expressed in points
directly (unlike DOCX which uses half-points). A value of ``1`` is
1.0pt rendered.
"""
from __future__ import annotations

import zipfile
from xml.etree import ElementTree as ET
from typing import NamedTuple


_S_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_S_FONTS = f"{{{_S_NS}}}fonts"
_S_FONT = f"{{{_S_NS}}}font"
_S_COLOR = f"{{{_S_NS}}}color"
_S_SZ = f"{{{_S_NS}}}sz"
_S_CELL_XFS = f"{{{_S_NS}}}cellXfs"
_S_XF = f"{{{_S_NS}}}xf"


class CellFont(NamedTuple):
    """Resolved font properties for one font record.

    color: 6-hex RGB string (alpha stripped if present), or None when
        no rgb color is set on this font (theme/indexed colors map to
        None to avoid false positives; the detector's near-white
        check is intentionally conservative against them).
    size_pt: float font size in points, or None when unset.
    """
    color: str | None
    size_pt: float | None


def _strip_alpha(rgb: str) -> str:
    """Return the 6-hex RGB portion of an ``rgb=`` value.

    Accepts 6-hex (``RRGGBB``) and 8-hex (``AARRGGBB``) forms; for
    8-hex the leading two hex digits are the alpha and stripped.
    Returns the value uppercased for direct frozenset lookup.
    Non-conforming values are returned as-is so the caller's
    near-white check fails closed.
    """
    if not rgb:
        return ""
    rgb = rgb.upper()
    if len(rgb) == 8:
        return rgb[2:]
    return rgb


def parse_styles(xml_bytes: bytes) -> tuple[list[CellFont], list[int]]:
    """Parse ``xl/styles.xml`` into (fonts, cellXfs_to_fontId).

    Returns:
      fonts: list of CellFont, indexed by fontId (0-based).
      cellXfs_to_fontId: list of int, indexed by cell ``s`` value;
        each entry is the fontId of that style.

    Both lists are empty on parse failure so callers fail closed.
    """
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return [], []

    fonts: list[CellFont] = []
    fonts_el = root.find(_S_FONTS)
    if fonts_el is not None:
        for font in fonts_el.findall(_S_FONT):
            color: str | None = None
            color_el = font.find(_S_COLOR)
            if color_el is not None:
                rgb = color_el.get("rgb")
                if rgb:
                    color = _strip_alpha(rgb)
            size_pt: float | None = None
            sz_el = font.find(_S_SZ)
            if sz_el is not None:
                raw = sz_el.get("val")
                if raw:
                    try:
                        size_pt = float(raw)
                    except ValueError:
                        size_pt = None
            fonts.append(CellFont(color=color, size_pt=size_pt))

    cell_xfs: list[int] = []
    cell_xfs_el = root.find(_S_CELL_XFS)
    if cell_xfs_el is not None:
        for xf in cell_xfs_el.findall(_S_XF):
            try:
                font_id = int(xf.get("fontId") or "0")
            except ValueError:
                font_id = 0
            cell_xfs.append(font_id)

    return fonts, cell_xfs


def resolve_cell_font(
    cell_style_id: int | None,
    fonts: list[CellFont],
    cell_xfs_to_font_id: list[int],
) -> CellFont:
    """Resolve a cell's effective font properties from its ``s`` value.

    cell_style_id: the integer value of the cell's ``s`` attribute,
      or None when ``s`` is absent (then the default cellXfs[0] is
      used, the OOXML rendering default).
    Returns a CellFont. When indices are out of range (malformed
    file), returns CellFont(None, None) so the detector's check fails
    closed rather than firing on garbage.
    """
    idx = cell_style_id if cell_style_id is not None else 0
    if idx < 0 or idx >= len(cell_xfs_to_font_id):
        return CellFont(color=None, size_pt=None)
    font_id = cell_xfs_to_font_id[idx]
    if font_id < 0 or font_id >= len(fonts):
        return CellFont(color=None, size_pt=None)
    return fonts[font_id]


def load_styles_from_zip(
    zf: zipfile.ZipFile,
) -> tuple[list[CellFont], list[int]]:
    """Read and parse ``xl/styles.xml`` if present.

    Returns ([], []) when the part is absent or unreadable, so
    callers fail closed on malformed packages.
    """
    if "xl/styles.xml" not in zf.namelist():
        return [], []
    try:
        xml_bytes = zf.read("xl/styles.xml")
    except KeyError:
        return [], []
    return parse_styles(xml_bytes)


__all__ = [
    "CellFont",
    "parse_styles",
    "resolve_cell_font",
    "load_styles_from_zip",
]

# Bismillah ir-Rahman ir-Rahim