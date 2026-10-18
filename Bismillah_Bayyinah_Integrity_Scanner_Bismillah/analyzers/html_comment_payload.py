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
Tier 1 detector for hidden-text payloads inside HTML comments
(v1.1.2 HTML format gauntlet).

HTML comments (``<!-- ... -->``) are stripped from the rendered tree
but preserved verbatim in the source. Server logs, source-view
panels, indexers that read raw HTML, LLM training pipelines, and any
copy-paste of "view source" all carry the comment body forward. A
reader looking at the page in a browser will not see them.

Routine HTML comments are short - section dividers, build markers,
license blurbs. A long comment body (>= ``_MIN_PAYLOAD_LENGTH``
non-whitespace characters) is structurally anomalous and worth
surfacing as a Tier 1 finding.

The existing ``HtmlAnalyzer`` runs the unicode-concealment detectors
on comment text via ``handle_comment``, but does not surface the
comment body itself as a payload-recovery finding. This detector
closes that gap.

Closes html_gauntlet fixture 03_comment_payload.html.

Tier discipline: Tier 1. Triggers are byte-deterministic - a length
threshold on raw comment text, no semantic claim.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from domain.finding import Finding


_MAX_HTML_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240

# Minimum non-whitespace length before a comment is flagged. 32 chars
# is well above conditional-comment / IE-targeting boilerplate
# (``<!--[if IE]>``, ``<!--/-->``), well above ordinary section-divider
# comments ("main content", "footer start", "ordinary comment"), and
# well below an actual payload-carrying comment body.
_MIN_PAYLOAD_LENGTH: int = 32

# Match <!-- ... -->. Non-greedy body capture, DOTALL so newlines are
# captured.
_COMMENT_PATTERN: re.Pattern[str] = re.compile(
    r"<!--(.*?)-->",
    re.DOTALL,
)

# Conditional comments (``<!--[if ...]>``) are legacy IE feature
# detection and not a payload-smuggling vector. Skip those.
_CONDITIONAL_PREFIX: re.Pattern[str] = re.compile(
    r"^\s*\[if\b", re.IGNORECASE,
)


def detect_html_comment_payload(file_path: Path) -> Iterable[Finding]:
    """Surface long HTML comment bodies as Tier 1 findings."""
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

    for match in _COMMENT_PATTERN.finditer(text):
        body = match.group(1)
        if _CONDITIONAL_PREFIX.search(body):
            continue
        cleaned = body.strip()
        if len(cleaned) < _MIN_PAYLOAD_LENGTH:
            continue

        line_no = text[: match.start()].count("\n") + 1
        preview = cleaned[:_PREVIEW_LIMIT]

        yield Finding(
            mechanism="html_comment_payload",
            tier=1,
            confidence=1.0,
            description=(
                f"HTML comment carries {len(cleaned)} non-whitespace "
                f"characters - well above routine comment length. "
                f"Comments are stripped from the rendered tree but "
                f"preserved verbatim in source view, indexers, and "
                f"LLM ingestion paths. Recovered text: {preview!r}."
            ),
            location=f"{file_path}:line{line_no}:comment",
            surface="(rendered view omits this text)",
            concealed=f"comment body: {preview!r}",
            source_layer="batin",
        )


__all__ = ["detect_html_comment_payload"]

# Bismillah ir-Rahman ir-Rahim