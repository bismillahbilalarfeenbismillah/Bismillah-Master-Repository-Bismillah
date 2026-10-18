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
Tier 1 detector for hidden-text payloads injected via CSS ``content:``
property strings (v1.1.2 HTML format gauntlet).

CSS pseudo-elements (``::before``, ``::after``) accept a ``content``
property whose string value is rendered as generated content adjacent
to the matched element. Two adversarial uses combine on this surface:

  (a) The ``content`` string text lives inside a ``<style>`` block
      (a non-visible container the existing HtmlAnalyzer skips for
      zahir detection) - never seen by a casual reader of the source.
  (b) A neighbouring ``color: white`` (or ``color: #fff`` /
      ``color: transparent`` / ``opacity: 0``) declaration suppresses
      the rendered glyphs from view; the text exists in the DOM
      (accessible via ``getComputedStyle().content``), reaches every
      LLM that flattens HTML to text, and ships through copy-paste
      pipelines that ignore CSS.

The rendered grid shows nothing. The DOM carries the payload.

Triggers (any one is sufficient):

  (a) length: any ``content: "..."`` string exceeding
      ``_LENGTH_THRESHOLD`` chars;
  (b) suppressing-style: any ``content`` string of at least
      ``_MIN_PAYLOAD_LENGTH`` chars whose enclosing rule also carries
      a render-suppressing color / opacity declaration.

Closes html_gauntlet fixture 05_css_content.html.

Tier discipline: Tier 1. Triggers are byte-deterministic regex matches
on the ``<style>`` body; no semantic claim about user intent.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from domain.finding import Finding


_MAX_HTML_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240
_LENGTH_THRESHOLD: int = 64
_MIN_PAYLOAD_LENGTH: int = 16

# Match every <style>...</style> block body.
_STYLE_BLOCK_PATTERN: re.Pattern[str] = re.compile(
    r"<style\b[^>]*>(.*?)</style\s*>",
    re.IGNORECASE | re.DOTALL,
)

# Match every CSS rule {selector + body}. We only care about the body
# string between the curly braces. Non-greedy on the body so nested
# constructs (we don't care about them; CSS rules don't legally nest
# at this level outside of @-rules) end at the first '}'.
_RULE_PATTERN: re.Pattern[str] = re.compile(
    r"([^{}]+)\{([^{}]*)\}",
    re.DOTALL,
)

# Match a content: declaration with a single- or double-quoted string.
_CONTENT_DECL_PATTERN: re.Pattern[str] = re.compile(
    r"content\s*:\s*(?: \"([^\"]*)\" | '([^']*)' )",
    re.IGNORECASE | re.VERBOSE,
)

# Render-suppressing companions inside the same rule body. Any one of
# these alongside a content: string is the "doubly hidden" shape.
_SUPPRESS_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"color\s*:\s*white\b", re.IGNORECASE),
    re.compile(r"color\s*:\s*#fff(?:fff)?\b", re.IGNORECASE),
    re.compile(
        r"color\s*:\s*rgb\s*\(\s*255\s*,\s*255\s*,\s*255\s*\)",
        re.IGNORECASE,
    ),
    re.compile(r"color\s*:\s*transparent\b", re.IGNORECASE),
    re.compile(r"opacity\s*:\s*0(?:\.0+)?\b", re.IGNORECASE),
    re.compile(r"visibility\s*:\s*hidden\b", re.IGNORECASE),
    re.compile(r"display\s*:\s*none\b", re.IGNORECASE),
    re.compile(r"font-size\s*:\s*0(?:px|pt|em)?\b", re.IGNORECASE),
)


def _has_suppressing_style(rule_body: str) -> bool:
    for pattern in _SUPPRESS_PATTERNS:
        if pattern.search(rule_body):
            return True
    return False


def detect_html_style_content_payload(file_path: Path) -> Iterable[Finding]:
    """Surface CSS ``content:`` strings that smuggle text payloads."""
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

    for style_match in _STYLE_BLOCK_PATTERN.finditer(text):
        style_body = style_match.group(1)
        style_offset = style_match.start(1)

        for rule_match in _RULE_PATTERN.finditer(style_body):
            selector = rule_match.group(1).strip()
            rule_body = rule_match.group(2)

            for content_match in _CONTENT_DECL_PATTERN.finditer(rule_body):
                content = (
                    content_match.group(1)
                    if content_match.group(1) is not None
                    else (content_match.group(2) or "")
                )
                if len(content) < _MIN_PAYLOAD_LENGTH:
                    continue

                # Compute line number of the content: declaration.
                abs_offset = (
                    style_offset
                    + rule_match.start(2)
                    + content_match.start()
                )
                line_no = text[:abs_offset].count("\n") + 1
                preview = content[:_PREVIEW_LIMIT]

                length_hit = len(content) > _LENGTH_THRESHOLD
                suppress_hit = _has_suppressing_style(rule_body)

                if not (length_hit or suppress_hit):
                    continue

                if length_hit and suppress_hit:
                    reason = (
                        f"is {len(content)} characters AND lives in a "
                        f"rule body that also carries a render-"
                        f"suppressing declaration"
                    )
                elif length_hit:
                    reason = (
                        f"is {len(content)} characters - well above "
                        f"routine pseudo-element content length"
                    )
                else:
                    reason = (
                        f"lives in a rule body that also carries a "
                        f"render-suppressing declaration "
                        f"(white / transparent / opacity:0 / "
                        f"display:none / visibility:hidden)"
                    )

                yield Finding(
                    mechanism="html_style_content_payload",
                    tier=1,
                    confidence=1.0,
                    description=(
                        f"<style> block contains a CSS content: "
                        f"declaration on {selector!r} that {reason}. "
                        f"Pseudo-element content reaches the DOM via "
                        f"getComputedStyle and is read by indexers and "
                        f"LLM ingestion paths regardless of color or "
                        f"visibility. Recovered text: {preview!r}."
                    ),
                    location=(
                        f"{file_path}:line{line_no}:style:"
                        f"{selector[:40]}"
                    ),
                    surface="(rendered view suppresses or omits this text)",
                    concealed=(
                        f"CSS content payload on {selector!r}: {preview!r}"
                    ),
                    source_layer="batin",
                )


__all__ = ["detect_html_style_content_payload"]

# Bismillah ir-Rahman ir-Rahim