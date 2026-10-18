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
Tier 1 detector for hidden-text payloads inside ``<template>`` elements
(v1.1.2 HTML format gauntlet).

The ``<template>`` element holds inert markup that the browser parses
but does not render until JavaScript instantiates it via
``document.importNode`` or shadow-DOM cloning. The body text lives in
the DOM tree (under ``HTMLTemplateElement.content``), is reachable from
every script context, is read by every HTML-flattener and indexer, and
yet never appears on the rendered page unless explicitly activated.

The existing ``HtmlAnalyzer`` classifies ``<template>`` as a
"non-visible container" and skips its body during the zahir walk -
correct for the unicode-concealment detectors but leaves the actual
body text un-witnessed. This detector surfaces it.

Closes html_gauntlet fixture 02_template.html.

Tier discipline: Tier 1. The trigger is purely structural ("there is
non-empty text inside a <template> tag") and verifiable from the file
bytes alone.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from domain.finding import Finding


_MAX_HTML_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240

# Match <template ...>...</template>. Non-greedy body capture, case-
# insensitive, DOTALL so newlines are captured.
_TEMPLATE_PATTERN: re.Pattern[str] = re.compile(
    r"<template\b[^>]*>(.*?)</template\s*>",
    re.IGNORECASE | re.DOTALL,
)

_TAG_STRIP_PATTERN: re.Pattern[str] = re.compile(r"<[^>]+>")


def detect_html_template_payload(file_path: Path) -> Iterable[Finding]:
    """Surface every non-empty ``<template>`` body as a Tier 1 finding."""
    try:
        raw = file_path.read_bytes()
    except OSError:
        return

    if len(raw) > _MAX_HTML_BYTES:
        raw = raw[:_MAX_HTML_BYTES]

    try:
        text = raw.decode("utf-8", errors="replace")
    except Exception:  # noqa: BLE001 - defensive
        return

    for match in _TEMPLATE_PATTERN.finditer(text):
        body = match.group(1)
        cleaned = _TAG_STRIP_PATTERN.sub(" ", body).strip()
        if not cleaned:
            continue

        line_no = text[: match.start()].count("\n") + 1
        preview = cleaned[:_PREVIEW_LIMIT]

        yield Finding(
            mechanism="html_template_payload",
            tier=1,
            confidence=1.0,
            description=(
                f"<template> element carries {len(cleaned)} characters "
                f"of body text. The browser parses but does not render "
                f"<template> contents until JavaScript instantiates "
                f"them; indexers and LLM ingestion paths flatten the "
                f"body to text regardless. Recovered text: {preview!r}."
            ),
            location=f"{file_path}:line{line_no}:template",
            surface="(rendered view omits this text)",
            concealed=f"template body: {preview!r}",
            source_layer="batin",
        )


__all__ = ["detect_html_template_payload"]

# Bismillah ir-Rahman ir-Rahim