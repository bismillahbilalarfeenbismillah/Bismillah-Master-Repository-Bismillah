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
"""Section index loading and lookup helpers."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from typing_extensions import TypedDict

from bayyinah_audit_mcp.config import BayyinahConfig, load_config, resolve_path


class SectionEntry(TypedDict):
    title: str
    summary: str


class SectionLookup(TypedDict, total=False):
    status: str
    requested_ref: str
    section_ref: str
    label: str
    title: str
    summary: str
    reason: str


SECTION_REF_RE = re.compile(
    r"(?:§\s*|section\s+)?(?P<ref>\d+(?:\.\d+)+)",
    flags=re.IGNORECASE,
)


def bundled_section_index_path() -> Path:
    return Path(__file__).parent / "data" / "section_index.json"


def normalize_section_ref(value: str) -> str:
    """Normalize values like '§9.1', 'Section 9.1', and '9.1' to '9.1'."""

    match = SECTION_REF_RE.search(value.strip())
    if not match:
        return value.strip().lstrip("§").strip()
    return match.group("ref")


def _section_sort_key(section_ref: str) -> tuple[int, ...]:
    try:
        return tuple(int(part) for part in section_ref.split("."))
    except ValueError:
        return (999999,)


@lru_cache(maxsize=16)
def _load_section_index_from_path(path_string: str) -> dict[str, SectionEntry]:
    path = Path(path_string)

    with path.open("r", encoding="utf-8") as handle:
        raw: dict[str, Any] = json.load(handle)

    normalized: dict[str, SectionEntry] = {}
    for key, value in raw.items():
        ref = normalize_section_ref(key)
        title = str(value.get("title", "")).strip()
        summary = str(value.get("summary", "")).strip()
        normalized[ref] = {"title": title, "summary": summary}

    return normalized


def load_section_index(config: BayyinahConfig | None = None) -> dict[str, SectionEntry]:
    """Load the configured or bundled section index.

    The parsed JSON is cached by resolved path to avoid repeated disk reads
    during multi-section tool calls.
    """

    cfg = config or load_config()
    if cfg.section_index is not None:
        path = resolve_path(cfg.section_index, cfg)
    else:
        path = bundled_section_index_path().resolve()

    return dict(_load_section_index_from_path(str(path)))


def lookup_section(
    section_ref: str,
    config: BayyinahConfig | None = None,
) -> SectionLookup:
    """Look up a section by reference."""

    requested = section_ref
    normalized_ref = normalize_section_ref(section_ref)
    index = load_section_index(config)

    if normalized_ref not in index:
        return {
            "status": "not_found",
            "requested_ref": requested,
            "section_ref": normalized_ref,
            "label": f"§{normalized_ref}",
            "reason": "Section reference is not in the loaded Bayyinah section index.",
        }

    entry = index[normalized_ref]
    return {
        "status": "ok",
        "requested_ref": requested,
        "section_ref": normalized_ref,
        "label": f"§{normalized_ref}",
        "title": entry["title"],
        "summary": entry["summary"],
    }


def list_sections(config: BayyinahConfig | None = None) -> list[SectionLookup]:
    """Return the full section index in numeric section order."""

    index = load_section_index(config)
    sections: list[SectionLookup] = []

    for ref in sorted(index.keys(), key=_section_sort_key):
        entry = index[ref]
        sections.append(
            {
                "status": "ok",
                "requested_ref": ref,
                "section_ref": ref,
                "label": f"§{ref}",
                "title": entry["title"],
                "summary": entry["summary"],
            }
        )

    return sections

# Bismillah ir-Rahman ir-Rahim