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
Tier 1 detector for JPEG APP4-15 segments carrying readable text payload
(v1.1.2 image format gauntlet).

JPEG defines sixteen application markers, APP0 through APP15
(``0xFFE0`` through ``0xFFEF``). The first four are well-known and
load-bearing for legitimate image metadata: APP0 carries JFIF, APP1
carries EXIF and XMP, APP2 carries ICC color profiles, and APP3 is
sometimes used for Meta/JPS stereo pair data. The remaining markers
(APP4 through APP15) have no standardised meaning in the JPEG spec; a
JPEG decoder skips them, a content scanner that does not parse markers
ignores them, and a human reader never sees them.

A JPEG APP4-15 segment carrying UTF-8-decodable text at high printable
density is structurally anomalous: there is no legitimate reason for
those markers to carry natural-language text in a financial or office
document workflow. The surface is ideal for payload smuggling because
the segment is preserved through every JPEG re-save that does not
explicitly strip non-standard application markers.

Trigger: any APP4 through APP15 segment whose payload decodes to UTF-8
with at least 32 bytes of printable text at a printable-density above
0.7. APP4-15 should not carry natural-language text at all in office
or financial document workflows; the 32-byte floor exists only to
suppress accidental short ASCII fragments that vendor extensions
sometimes embed (version strings, GUIDs, identifiers).

Closes ``image_gauntlet`` fixture ``01_jpeg_app4_payload.jpg``.

Distinct from ``suspicious_image_chunk`` (existing v1.1.1 finding which
fires on any non-standard JPEG marker, but only at Tier 3 and without
recovering the payload text). This mechanism elevates to Tier 1 when
the segment carries readable text and recovers the text in
``concealed`` for inversion.

Tier discipline: Tier 1. Trigger is a deterministic byte-density check
on UTF-8-decoded segment data; no semantic claims about whether the
text is malicious.

Documented gap (v1.1.2+1 scope): APP1 EXIF UserComment (tag 0x9286) is
a free-text field within the EXIF IFD that can carry payload while
APP1 itself is excluded. UserComment-specific extraction requires an
EXIF IFD parser and is queued for the next gauntlet expansion.
"""
from __future__ import annotations

import struct
from pathlib import Path
from typing import Iterable

from domain.finding import Finding


_MAX_IMAGE_BYTES: int = 16 * 1024 * 1024
_PREVIEW_LIMIT: int = 240
# 32 bytes is the minimum natural-language payload that is
# structurally anomalous in an APP4-15 marker. APP4-15 should not
# carry natural-language text at all in office or financial document
# workflows; the threshold exists only to suppress short identifiers,
# version strings, or accidental ASCII fragments that vendor
# extensions sometimes embed.
_LENGTH_THRESHOLD: int = 32
_PRINTABLE_DENSITY: float = 0.7

_JPEG_SOI: bytes = b"\xff\xd8"
_JPEG_EOI_MARKER: int = 0xD9
_JPEG_SOS_MARKER: int = 0xDA

# Application markers that are load-bearing for legitimate metadata.
# APP0 (JFIF), APP1 (EXIF/XMP), APP2 (ICC), APP3 (Meta/JPS) are
# excluded from this detector by default. The remaining APP4-15
# markers (0xE4 through 0xEF) have no standardised use and carry
# the highest signal when they contain readable text.
_EXCLUDED_APP_MARKERS: frozenset[int] = frozenset({0xE0, 0xE1, 0xE2, 0xE3})
_TARGETED_APP_MARKERS: frozenset[int] = frozenset(range(0xE4, 0xF0))


def _iter_jpeg_app_segments(
    data: bytes,
) -> Iterable[tuple[int, bytes, int]]:
    """Yield ``(marker, payload, offset)`` for each APP4-15 segment.

    Walks JPEG markers from SOI (0xFFD8) until SOS (0xFFDA) or EOI
    (0xFFD9). Standalone markers (RST0-7, TEM, SOI, EOI) carry no
    length field; segment markers carry a big-endian 2-byte length
    that includes itself.
    """
    if not data.startswith(_JPEG_SOI):
        return

    end = len(data)
    i = 2  # past SOI
    while i + 1 < end:
        if data[i] != 0xFF:
            i += 1
            continue

        # Skip fill bytes (0xFF 0xFF ...)
        j = i
        while j + 1 < end and data[j] == 0xFF and data[j + 1] == 0xFF:
            j += 1
        if j + 1 >= end:
            return

        marker = data[j + 1]
        if marker == _JPEG_SOS_MARKER or marker == _JPEG_EOI_MARKER:
            return
        if marker == 0x00 or 0xD0 <= marker <= 0xD7:
            # Stuffing or restart markers; no length field.
            i = j + 2
            continue

        # Segment marker; followed by 2-byte length (big-endian,
        # inclusive of itself) and then payload.
        if j + 4 > end:
            return
        seg_len = struct.unpack(">H", data[j + 2:j + 4])[0]
        if seg_len < 2:
            return
        payload_start = j + 4
        payload_end = j + 2 + seg_len
        if payload_end > end:
            return

        if marker in _TARGETED_APP_MARKERS:
            payload = data[payload_start:payload_end]
            yield marker, payload, j

        i = payload_end


def _printable_density(text: str) -> float:
    """Return the fraction of characters that are printable ASCII or
    common UTF-8 letters (treating ``\\x20``-``\\x7e`` plus letters
    above 0x80 as printable for density purposes).
    """
    if not text:
        return 0.0
    printable = 0
    for ch in text:
        cp = ord(ch)
        if 0x20 <= cp <= 0x7E:
            printable += 1
        elif cp >= 0x80 and ch.isprintable():
            printable += 1
    return printable / len(text)


def detect_image_jpeg_appn_payload(file_path: Path) -> Iterable[Finding]:
    """Surface JPEG APP4-15 segments carrying readable text payload."""
    try:
        raw = file_path.read_bytes()
    except OSError:
        return

    if len(raw) > _MAX_IMAGE_BYTES:
        raw = raw[:_MAX_IMAGE_BYTES]

    if not raw.startswith(_JPEG_SOI):
        return

    for marker, payload, offset in _iter_jpeg_app_segments(raw):
        if marker in _EXCLUDED_APP_MARKERS:
            # Defensive; the iterator already excludes these, but keep
            # explicit for clarity.
            continue

        try:
            text = payload.decode("utf-8", errors="replace")
        except Exception:  # noqa: BLE001 - defensive
            continue

        # Strip null bytes and trailing whitespace; many payload
        # carriers null-terminate.
        text_clean = text.replace("\x00", "").strip()
        if len(text_clean) < _LENGTH_THRESHOLD:
            continue

        density = _printable_density(text_clean)
        if density < _PRINTABLE_DENSITY:
            continue

        preview = text_clean[:_PREVIEW_LIMIT]
        marker_label = f"0xFF{marker:02X}"
        appn_index = marker - 0xE0  # 4 through 15

        yield Finding(
            mechanism="image_jpeg_appn_payload",
            tier=1,
            confidence=0.9,
            description=(
                f"JPEG APP{appn_index} segment ({marker_label}) at "
                f"offset {offset} carries {len(text_clean)} characters "
                f"of readable UTF-8 text at "
                f"{density:.0%} printable density. APP4 through APP15 "
                f"are not standardised and carry no legitimate "
                f"natural-language payload in office or financial "
                f"document workflows. Recovered text: {preview!r}."
            ),
            location=f"{file_path}@segment:{offset}",
            surface=f"(JPEG APP{appn_index} marker not rendered)",
            concealed=preview,
            source_layer="batin",
        )


__all__ = ["detect_image_jpeg_appn_payload"]

# Bismillah ir-Rahman ir-Rahim