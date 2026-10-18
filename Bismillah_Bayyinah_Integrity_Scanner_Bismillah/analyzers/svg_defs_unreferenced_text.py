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
Tier 1 batin detector for SVG ``<text>`` elements nested inside
``<defs>`` with no matching ``<use>`` reference (v1.1.2 image
format gauntlet).

The SVG ``<defs>`` element is the template surface: graphical
content placed inside ``<defs>`` is not rendered until a
``<use href="#id">`` (or legacy ``xlink:href``) elsewhere in the
document references it. Legitimate uses include reusable filters,
gradients, symbols, and re-instantiated shape templates.

A ``<text>`` element inside ``<defs>`` whose ``id`` is never
referenced by any ``<use>`` element therefore carries text content
that is not rendered as glyph content but is fully readable by
indexers, LLMs, and other XML-aware consumers. This is a textbook
batin surface: the human reader of the rendered SVG sees only the
canvas content, while a machine reading the source observes the
embedded payload.

Closes ``image_gauntlet`` fixture ``06_svg_defs_text.svg``.

Tier discipline: Tier 1. The classification is byte-deterministic:
the ``<text>`` element exists inside ``<defs>``, has an ``id``, and
no ``<use>`` element in the document carries an ``href`` (or
``xlink:href``) pointing to that ``id``. The fact-claim is
"unreferenced text node inside defs", verifiable by re-parsing the
file. ``<text>`` without an ``id`` is also flagged because it
cannot be rendered via ``<use>`` at all (``<use>`` requires an
``id`` target), making it permanently hidden.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET

from domain.finding import Finding


_MAX_IMAGE_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240

_SVG_DEFS: str = "defs"
_SVG_TEXT: str = "text"
_SVG_USE: str = "use"

# xlink namespace for legacy <use xlink:href="...">.
_XLINK_HREF: str = "{http://www.w3.org/1999/xlink}href"


def _strip_ns(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def _gather_text(elem: ET.Element) -> str:
    """Concatenate all descendant text content of an element."""
    parts: list[str] = []
    if elem.text:
        parts.append(elem.text)
    for child in elem.iter():
        if child is elem:
            continue
        if child.text:
            parts.append(child.text)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def _collect_use_targets(root: ET.Element) -> set[str]:
    """Collect every id referenced by a ``<use>`` element via its
    ``href`` or ``xlink:href`` attribute. Strips the leading ``#``.
    """
    targets: set[str] = set()
    for elem in root.iter():
        if _strip_ns(elem.tag) != _SVG_USE:
            continue
        href = elem.attrib.get("href")
        if href is None:
            href = elem.attrib.get(_XLINK_HREF)
        if href is None:
            continue
        ref = href.strip()
        if ref.startswith("#"):
            ref = ref[1:]
        if ref:
            targets.add(ref)
    return targets


def detect_svg_defs_unreferenced_text(file_path: Path) -> Iterable[Finding]:
    """Surface ``<text>`` elements nested inside ``<defs>`` whose
    ``id`` is never referenced by any ``<use>`` (or which lack an
    ``id`` entirely, making them unrenderable).
    """
    try:
        raw = file_path.read_bytes()
    except OSError:
        return

    if len(raw) > _MAX_IMAGE_BYTES:
        raw = raw[:_MAX_IMAGE_BYTES]

    text_doc = raw.decode("utf-8", errors="replace")
    try:
        root = ET.fromstring(text_doc)
    except ET.ParseError:
        return

    if _strip_ns(root.tag) != "svg":
        return

    use_targets = _collect_use_targets(root)

    for defs_elem in root.iter():
        if _strip_ns(defs_elem.tag) != _SVG_DEFS:
            continue

        for elem in defs_elem.iter():
            if elem is defs_elem:
                continue
            if _strip_ns(elem.tag) != _SVG_TEXT:
                continue

            content = _gather_text(elem).strip()
            if not content:
                continue

            text_id = elem.attrib.get("id", "").strip()
            if text_id and text_id in use_targets:
                # Legitimate reuse via <use href="#id">; the text
                # will render at every <use> instantiation.
                continue

            preview = (
                content if len(content) <= _PREVIEW_LIMIT
                else content[:_PREVIEW_LIMIT] + "..."
            )

            if text_id:
                reason = (
                    f"id={text_id!r} is not referenced by any <use> "
                    f"element"
                )
            else:
                reason = (
                    "no id attribute, so the element cannot be "
                    "instantiated by any <use> reference"
                )

            yield Finding(
                mechanism="svg_defs_unreferenced_text",
                tier=1,
                confidence=0.90,
                description=(
                    f"SVG <text> element nested inside <defs> with "
                    f"unrendered content: {reason}. <defs> is the "
                    f"SVG template surface; its children render only "
                    f"when instantiated via <use href=\"#id\">. "
                    f"Unreferenced text in <defs> is read by "
                    f"indexers and LLMs but never appears as glyph "
                    f"content for the human reader. Recovered text: "
                    f"{preview!r}."
                ),
                location=f"{file_path}@svg:defs/text",
                surface="(SVG <defs>/<text> not rendered as glyph content)",
                concealed=preview,
                source_layer="batin",
            )


__all__ = ["detect_svg_defs_unreferenced_text"]

# Bismillah ir-Rahman ir-Rahim