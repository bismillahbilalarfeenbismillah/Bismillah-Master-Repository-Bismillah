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
Tier 1 detector for RFC 5322 folded-continuation lines used to smuggle
payload text inside a header (v1.1.2 EML format gauntlet).

RFC 5322 §2.2.3 lets a header value continue across multiple lines by
ending each line with CRLF and starting the next with whitespace
(``CRLF SP`` or ``CRLF HT``). The folded form is collapsed by every
RFC-compliant parser when the value is read - the mail client never
shows folded continuations to the reader, the user-visible header
panel renders only first-line summaries, and most byte-level scanners
read the raw bytes line-by-line and never reassemble the unfolded
value. The result is a header surface where many lines of payload
text can hide behind a routine-looking first line.

Routine header folding produces 1-2 continuations on long structured
headers (DKIM-Signature, ARC-*, Received). A header carrying six or
more folded continuation lines, or whose joined post-fold value
exceeds the long-header length threshold, is structurally anomalous -
the shape exists to PERFORM brevity to the byte-level scanner while
the value the parser actually delivers carries a payload.

Trigger: any header (other than the legitimate-large set:
DKIM-Signature, ARC-Seal, ARC-Message-Signature,
ARC-Authentication-Results, Authentication-Results, Received,
Received-SPF) whose raw form contains six or more CRLF+WSP fold
sequences.

Closes ``eml_gauntlet`` fixture ``05_header_continuation_smuggle.eml``.

Distinct from ``eml_smuggled_header`` (which fires on duplicate
single-instance headers and on bare CRLF without WSP - i.e. CRLF
injection rather than legitimate folding).

Tier discipline: Tier 1. Trigger is a byte count of CRLF+WSP
sequences inside the raw header block; no semantic interpretation.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from domain.finding import Finding


_MAX_EML_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240
_FOLD_THRESHOLD: int = 6

# Headers where heavy folding is legitimate and routine.
_LEGITIMATE_LARGE_HEADERS: frozenset[str] = frozenset({
    "dkim-signature",
    "arc-seal",
    "arc-message-signature",
    "arc-authentication-results",
    "authentication-results",
    "received",
    "received-spf",
    "x-google-dkim-signature",
})

# A header line begins with ``Name: ...`` at column 0 of a line.
# Continuation lines start with whitespace.
_HEADER_START: re.Pattern[bytes] = re.compile(
    rb"^(?P<name>[A-Za-z][A-Za-z0-9\-_]*):[ \t]?",
    re.MULTILINE,
)


def _split_headers_and_body(raw: bytes) -> bytes:
    """Return the raw header block (everything before the first blank
    line). Handles both CRLF and LF line terminators."""
    # The header/body separator is a blank line (CRLF CRLF or LF LF).
    for sep in (b"\r\n\r\n", b"\n\n"):
        idx = raw.find(sep)
        if idx >= 0:
            return raw[:idx]
    return raw


def _split_individual_headers(header_block: bytes) -> list[tuple[bytes, bytes]]:
    """Split header block into ``(name, raw-value-with-folds)`` pairs.

    The raw-value preserves CRLF and WSP so we can count folds.
    """
    # Normalise to CRLF for consistent counting; track CRLF and LF.
    out: list[tuple[bytes, bytes]] = []
    matches = list(_HEADER_START.finditer(header_block))
    for idx, match in enumerate(matches):
        name = match.group("name")
        value_start = match.end()
        if idx + 1 < len(matches):
            value_end = matches[idx + 1].start()
        else:
            value_end = len(header_block)
        value = header_block[value_start:value_end]
        out.append((name, value))
    return out


def detect_eml_header_continuation_payload(file_path: Path) -> Iterable[Finding]:
    """Surface headers whose folded continuation depth exceeds the
    structural threshold."""
    try:
        raw = file_path.read_bytes()
    except OSError:
        return

    if len(raw) > _MAX_EML_BYTES:
        raw = raw[:_MAX_EML_BYTES]

    header_block = _split_headers_and_body(raw)
    if not header_block:
        return

    pairs = _split_individual_headers(header_block)

    for name_bytes, value_bytes in pairs:
        try:
            name = name_bytes.decode("ascii", errors="replace").lower()
        except Exception:  # noqa: BLE001 - defensive
            continue

        if name in _LEGITIMATE_LARGE_HEADERS:
            continue

        # Count CRLF+WSP and LF+WSP fold sequences inside the value.
        crlf_folds = len(re.findall(rb"\r\n[ \t]", value_bytes))
        lf_folds = len(re.findall(rb"(?<!\r)\n[ \t]", value_bytes))
        fold_count = crlf_folds + lf_folds

        if fold_count < _FOLD_THRESHOLD:
            continue

        # Decode the value for preview / recovery.
        try:
            value_text = value_bytes.decode("utf-8", errors="replace")
        except Exception:  # noqa: BLE001 - defensive
            value_text = ""
        # Unfolded form (what a parser delivers).
        unfolded = re.sub(r"\r?\n[ \t]+", " ", value_text).strip()
        unfolded_preview = unfolded[:_PREVIEW_LIMIT]
        first_line = value_text.splitlines()[0] if value_text else ""
        first_line_preview = first_line.strip()[:_PREVIEW_LIMIT]

        yield Finding(
            mechanism="eml_header_continuation_payload",
            tier=1,
            confidence=0.9,
            description=(
                f"Header {name!r} carries {fold_count} folded "
                f"continuation lines - well above the routine fold "
                f"depth for non-DKIM/ARC/Received headers. The mail "
                f"client renders only the first-line summary; most "
                f"byte-level scanners read raw lines and never "
                f"reassemble the unfolded value. Unfolded value: "
                f"{unfolded_preview!r}."
            ),
            location=f"{file_path}:header:{name}",
            surface=f"{name}: {first_line_preview}",
            concealed=(
                f"{fold_count} fold continuations; unfolded value: "
                f"{unfolded_preview}"
            ),
            source_layer="batin",
        )


__all__ = ["detect_eml_header_continuation_payload"]

# Bismillah ir-Rahman ir-Rahim