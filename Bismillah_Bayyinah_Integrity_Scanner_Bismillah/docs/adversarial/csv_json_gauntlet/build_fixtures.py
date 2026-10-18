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
CSV / JSON adversarial gauntlet — fixture builder.

Six concealment techniques targeting v1.1.1 ``CsvAnalyzer`` and
``JsonAnalyzer`` gaps. We deliberately avoid the well-armored vectors:
CSV null-byte / BOM anomaly / mixed encoding / mixed delimiter /
comment row / inconsistent columns / formula injection / oversized
field / quoting anomaly / per-cell zero-width / TAG / bidi /
homoglyph; JSON duplicate keys / excessive nesting / per-string-value
zero-width / TAG / bidi / homoglyph.

Surface text mentions $1,000. Hidden payload mentions $10,000.

Fixtures
--------

01 — CSV with header/value type mismatch (numeric column carries a
     long natural-language payload — no formula prefix, escapes
     formula_injection)
02 — CSV with payload column past inconsistent-columns threshold
     (analyzer flags inconsistency but does not extract the trailing
     payload; or the row matches the header count exactly so no flag)
03 — CSV with NUL byte inside a quoted cell (analyzer catches
     null_byte but not when surrounded by valid quoted content
     that masks the structural break)
04 — JSON with unicode concealment (zero-width / bidi) inside KEYS
     (analyzer walks string VALUES only)
05 — JSON with __proto__ / constructor / prototype keys carrying
     payloads (prototype-pollution-shape)
06 — JSON with payload as a numeric-string value matching no
     concealment codepoint pattern (length-only smuggling)
"""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "fixtures"
OUT.mkdir(parents=True, exist_ok=True)

SURFACE_TEXT = (
    "Q3 financial summary - revenue grew 8% YoY to $1,000 thousand. "
    "Margins held steady. Cash position remains strong."
)
HIDDEN_PAYLOAD = (
    "HIDDEN_TEXT_PAYLOAD: actual revenue $10,000 - see annex"
)


def fixture_01_csv_type_mismatch() -> tuple[Path, str]:
    """Numeric column carrying a natural-language payload.

    A header that promises 'amount_usd' should hold numbers; instead
    the cell holds the payload. CsvAnalyzer does not type-check
    columns against header semantics.
    """
    path = OUT / "01_csv_type_mismatch.csv"
    rows = [
        "description,amount_usd,note",
        f'"{SURFACE_TEXT}",1000,"clean"',
        f'"second invoice","{HIDDEN_PAYLOAD}","second"',
    ]
    path.write_text("\n".join(rows) + "\n", "utf-8")
    return path, "Numeric column 'amount_usd' carrying a natural-language payload"


def fixture_02_csv_trailing_extra_columns() -> tuple[Path, str]:
    """Row with extra columns past header count carrying a payload.

    Some CSV consumers (pandas, sqlite import) silently drop or merge
    trailing fields; others preserve them. The analyzer flags
    inconsistent_columns but emits no trace of the extra cell content.
    """
    path = OUT / "02_csv_trailing_extra.csv"
    rows = [
        "description,amount_usd",
        f'"{SURFACE_TEXT}",1000',
        f'"second invoice",2000,"{HIDDEN_PAYLOAD}"',
    ]
    path.write_text("\n".join(rows) + "\n", "utf-8")
    return path, "Row 3 has a trailing 3rd column carrying the payload"


def fixture_03_csv_quoted_payload_in_value() -> tuple[Path, str]:
    """Payload as a quoted multiline value with no concealment codepoints.

    The value is plain ASCII, no zero-width / TAG / bidi / homoglyph,
    no formula prefix. A long natural-language string parked inside
    a quoted CSV field is a recognised exfiltration / smuggling
    shape, but CsvAnalyzer's per-cell scans target codepoint-level
    concealment, not corpus-divergence.
    """
    path = OUT / "03_csv_long_quoted_payload.csv"
    repeated = HIDDEN_PAYLOAD * 3
    rows = [
        "description,amount_usd,note",
        f'"{SURFACE_TEXT}",1000,"see attached"',
        f'"{repeated}",2000,"second invoice"',
    ]
    path.write_text("\n".join(rows) + "\n", "utf-8")
    return path, "Long natural-language payload in a normal quoted CSV cell"


def fixture_04_json_concealment_in_keys() -> tuple[Path, str]:
    """Zero-width / bidi codepoints inside JSON KEYS (not values).

    JsonAnalyzer's _walk_strings yields VALUES only — keys are not
    scanned for concealment codepoints. A key that mixes Latin
    letters with zero-width separators or right-to-left override
    passes through cleanly.
    """
    path = OUT / "04_json_concealment_in_keys.json"
    # 'amount\u200B_usd' — visually identical to 'amount_usd' but
    # parsed as a different key by every JSON consumer
    obj = {
        "description": SURFACE_TEXT,
        "amount\u200B_usd": 1000,                # zero-width space in key
        "n\u202Eote": HIDDEN_PAYLOAD,            # bidi RLO in key
    }
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), "utf-8")
    return path, "Zero-width and bidi codepoints inside JSON keys"


def fixture_05_json_prototype_pollution_shape() -> tuple[Path, str]:
    """Keys with prototype-pollution semantics carrying payloads.

    `__proto__`, `constructor`, and `prototype` are the canonical
    prototype-pollution attack keys in JavaScript. A backend that
    parses JSON via Object.assign or recursive merge inherits the
    payload. JsonAnalyzer does not flag these key names.
    """
    path = OUT / "05_json_prototype_pollution.json"
    obj = {
        "description": SURFACE_TEXT,
        "__proto__": {"polluted": HIDDEN_PAYLOAD},
        "constructor": {"prototype": {"isAdmin": True}},
    }
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), "utf-8")
    return path, "Prototype-pollution-shape keys (__proto__, constructor)"


def fixture_06_json_long_string_payload() -> tuple[Path, str]:
    """JSON string value that is a long natural-language payload.

    No concealment codepoints, no homoglyph mix. The value is just
    a long plaintext string. JsonAnalyzer's per-string detectors
    target codepoint-level concealment; a long natural-language
    string passes cleanly.
    """
    path = OUT / "06_json_long_string_payload.json"
    obj = {
        "description": SURFACE_TEXT,
        "amount_usd": 1000,
        "note": HIDDEN_PAYLOAD * 5,  # long natural-language payload
    }
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), "utf-8")
    return path, "Long natural-language payload as a JSON string value"


BUILDERS = [
    fixture_01_csv_type_mismatch,
    fixture_02_csv_trailing_extra_columns,
    fixture_03_csv_quoted_payload_in_value,
    fixture_04_json_concealment_in_keys,
    fixture_05_json_prototype_pollution_shape,
    fixture_06_json_long_string_payload,
]


if __name__ == "__main__":
    for builder in BUILDERS:
        path, desc = builder()
        size = path.stat().st_size
        print(f"{path.name:<42} {size:>7} bytes  - {desc}")

# Bismillah ir-Rahman ir-Rahim