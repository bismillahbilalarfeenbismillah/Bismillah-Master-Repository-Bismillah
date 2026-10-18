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
"""Render page-1 thumbnails of the demo exhibit fixtures.

The demo page at /demo shows three "exhibit" cards that one-click upload
a fixture PDF through the live scan-then-summarize pipeline. Each card
opens with a thumbnail of the fixture's first page so users see the
actual document substrate (or, for the encrypted exhibit, an inline
SVG placeholder) before clicking. Without the thumbnail the cards read
as abstract verdict descriptions; with it the firewall thesis is
visible at a glance, especially for the concealment fixture, whose
near-empty visible surface contrasts with its 16 deterministic findings.

This script is the build step. Re-run it after editing any fixture in
docs/demo/fixtures/ that has a corresponding entry in TARGETS below.
The encrypted fixture is intentionally absent: encrypted PDFs cannot
be rendered, which is the point, and the demo card uses an inline
SVG illustration instead.

Output: docs/landing-mock-v2/exhibit-thumbnails/<stem>.jpg

Run: python scripts/render_exhibit_thumbnails.py
"""
from __future__ import annotations

from pathlib import Path

import fitz  # pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = ROOT / "docs" / "demo" / "fixtures"
THUMBS_DIR = ROOT / "docs" / "landing-mock-v2" / "exhibit-thumbnails"

# Fixtures whose first page can be rendered. Stems match the fixture
# filename without the .pdf extension; the demo serves thumbnails as
# /demo/exhibit-thumbnails/<stem>.jpg (whitelist enforced server-side).
TARGETS = [
    "clean_q3_report",
    "adversarial_invisible_text",
]

# Width chosen for ~240px display at 2x device pixel ratio. JPEG quality
# 82 keeps the financial-table fixture under 40KB while remaining
# legible at the rendered card size. Aspect ratio is preserved from
# the source page.
THUMB_WIDTH = 480
JPEG_QUALITY = 82
RENDER_DPI_MATRIX = fitz.Matrix(1.5, 1.5)


def render_one(stem: str) -> tuple[int, int, int]:
    src = FIXTURES_DIR / f"{stem}.pdf"
    if not src.is_file():
        raise FileNotFoundError(f"Fixture not found: {src}")
    doc = fitz.open(str(src))
    try:
        page = doc[0]
        pix = page.get_pixmap(matrix=RENDER_DPI_MATRIX)
    finally:
        doc.close()
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("RGB")
    new_h = int(pix.height * THUMB_WIDTH / pix.width)
    img = img.resize((THUMB_WIDTH, new_h), Image.LANCZOS)
    out = THUMBS_DIR / f"{stem}.jpg"
    img.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    return THUMB_WIDTH, new_h, out.stat().st_size


def main() -> int:
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Rendering exhibit thumbnails to {THUMBS_DIR}")
    for stem in TARGETS:
        w, h, n = render_one(stem)
        print(f"  {stem}.jpg  {w}x{h}  {n} bytes")
    print("Done. Encrypted exhibit uses inline SVG (see demo.html, no thumbnail rendered).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Bismillah ir-Rahman ir-Rahim