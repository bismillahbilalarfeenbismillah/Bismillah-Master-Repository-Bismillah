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
#!/usr/bin/env python3
"""Build a clean PDF carrying a bare destination-array /OpenAction
([page_ref /XYZ null null null]) without any active content.

Reproduces Bug 1 (openaction false positive on benign navigation).
LibreOffice naturally emits this shape when re-exporting a document
with an "open at page N" hint; we synthesise it for determinism
because LibreOffice's export behavior varies across versions.

The producer string is set to LibreOffice for the Round 12 fixture's
producer-family coverage check.

Output: fixture_clean_libreoffice_destination_oa.pdf
"""
from __future__ import annotations
import io
from pathlib import Path
import pypdf
from pypdf.generic import (
    ArrayObject, NameObject, NullObject,
)

HERE = Path(__file__).parent
HTML_SOURCE = b"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Round 12 LibreOffice Fixture</title></head>
<body><h1>Round 12 Reproducer (LibreOffice synthetic OpenAction)</h1>
<p>This document carries a bare destination-array /OpenAction
that LibreOffice naturally emits. ISO 32000-1 section 12.6.3 defines
this as a navigation hint, not executable content.</p>
</body></html>
"""


def _build_seed_pdf(workdir: Path) -> Path:
    """Render minimal HTML to PDF via LibreOffice for the seed."""
    import os
    import subprocess
    seed_html = workdir / "seed.html"
    seed_html.write_bytes(HTML_SOURCE)
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = "0"
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "seed.html",
         "--outdir", str(workdir)],
        cwd=workdir, env=env, check=True, capture_output=True,
    )
    return workdir / "seed.pdf"


def build(output_path: Path) -> None:
    workdir = output_path.parent / "_build_libreoffice_oa"
    workdir.mkdir(parents=True, exist_ok=True)
    seed_pdf = _build_seed_pdf(workdir)

    reader = pypdf.PdfReader(seed_pdf)
    writer = pypdf.PdfWriter(clone_from=reader)
    first_page = writer.pages[0].indirect_reference
    destination = ArrayObject([
        first_page,
        NameObject("/XYZ"),
        NullObject(),
        NullObject(),
        NullObject(),
    ])
    writer._root_object[NameObject("/OpenAction")] = destination

    buf = io.BytesIO()
    writer.write(buf)
    output_path.write_bytes(buf.getvalue())

    for f in workdir.glob("*"):
        f.unlink(missing_ok=True)
    workdir.rmdir()


if __name__ == "__main__":
    out = HERE / "fixture_clean_libreoffice_destination_oa.pdf"
    build(out)
    print(f"wrote {out} ({out.stat().st_size} bytes)")

# Bismillah ir-Rahman ir-Rahim