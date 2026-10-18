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
"""Round 12 HIGH 1 closure: openaction destination-vs-action filter.

Per ISO 32000-1 section 12.6.3, /OpenAction values that are bare
destination arrays or /GoTo-family wrapped destinations are
navigation hints, not executable content. The v1.2.4 fix filters
them before emission. Executable subtypes (/JavaScript, /Launch,
/URI, /SubmitForm, /ImportData) still fire.
"""
from __future__ import annotations
import io
from pathlib import Path
import pypdf
from pypdf.generic import (
    ArrayObject, DictionaryObject, NameObject, NullObject,
    TextStringObject, ByteStringObject,
)
import pytest
from bayyinah import scan_pdf

CORPUS = Path(__file__).parent


def _build_minimal_seed_pdf() -> Path:
    """Build a minimal seed PDF; we modify its catalog for each test."""
    seed = CORPUS / "fixture_libreoffice_writer_native.pdf"
    return seed


def _scan_with_open_action(open_action_value) -> list[dict]:
    """Inject open_action_value into the catalog of the minimal seed
    and return the resulting finding list as dicts."""
    seed = _build_minimal_seed_pdf()
    reader = pypdf.PdfReader(seed)
    writer = pypdf.PdfWriter(clone_from=reader)
    writer._root_object[NameObject("/OpenAction")] = open_action_value
    buf = io.BytesIO()
    writer.write(buf)

    # Persist to a temp path because scan_pdf takes a Path.
    tmp = CORPUS / "_test_oa_tmp.pdf"
    tmp.write_bytes(buf.getvalue())
    try:
        rd = scan_pdf(tmp).to_dict()
        return rd.get("findings", [])
    finally:
        tmp.unlink(missing_ok=True)


def _fires_openaction(findings) -> bool:
    return any(f.get("mechanism") == "openaction" for f in findings)


def test_openaction_destination_array_does_not_fire():
    """Case 1: bare destination array such as
    [page_ref /XYZ left top zoom] is benign navigation."""
    seed = pypdf.PdfReader(_build_minimal_seed_pdf())
    first_page = seed.pages[0].indirect_reference
    dest = ArrayObject([
        first_page,
        NameObject("/XYZ"),
        NullObject(), NullObject(), NullObject(),
    ])
    findings = _scan_with_open_action(dest)
    assert not _fires_openaction(findings), (
        f"openaction fired on benign destination array; findings={findings}"
    )


def test_openaction_goto_wrapped_destination_does_not_fire():
    """Case 2: {/S: /GoTo, /D: [...]} wraps a destination."""
    seed = pypdf.PdfReader(_build_minimal_seed_pdf())
    first_page = seed.pages[0].indirect_reference
    action = DictionaryObject({
        NameObject("/S"): NameObject("/GoTo"),
        NameObject("/D"): ArrayObject([
            first_page,
            NameObject("/XYZ"),
            NullObject(), NullObject(), NullObject(),
        ]),
    })
    findings = _scan_with_open_action(action)
    assert not _fires_openaction(findings), (
        f"openaction fired on /GoTo-wrapped destination; findings={findings}"
    )


def test_openaction_gotor_does_not_fire():
    """/GoToR (remote-document GoTo) is also navigation only."""
    action = DictionaryObject({
        NameObject("/S"): NameObject("/GoToR"),
        NameObject("/F"): TextStringObject("other.pdf"),
    })
    findings = _scan_with_open_action(action)
    assert not _fires_openaction(findings)


def test_openaction_javascript_action_fires():
    """/JavaScript subtype is executable; openaction must still fire."""
    action = DictionaryObject({
        NameObject("/S"): NameObject("/JavaScript"),
        NameObject("/JS"): TextStringObject("app.alert('test');"),
    })
    findings = _scan_with_open_action(action)
    assert _fires_openaction(findings), (
        f"openaction failed to fire on /JavaScript; findings={findings}"
    )


def test_openaction_launch_action_fires():
    """/Launch subtype is executable; openaction must still fire."""
    action = DictionaryObject({
        NameObject("/S"): NameObject("/Launch"),
        NameObject("/F"): TextStringObject("/bin/echo test"),
    })
    findings = _scan_with_open_action(action)
    assert _fires_openaction(findings), (
        f"openaction failed to fire on /Launch; findings={findings}"
    )


def test_openaction_uri_action_fires():
    """/URI subtype is executable (network call); openaction fires."""
    action = DictionaryObject({
        NameObject("/S"): NameObject("/URI"),
        NameObject("/URI"): TextStringObject("https://attacker.example/"),
    })
    findings = _scan_with_open_action(action)
    assert _fires_openaction(findings), (
        f"openaction failed to fire on /URI; findings={findings}"
    )

# Bismillah ir-Rahman ir-Rahim