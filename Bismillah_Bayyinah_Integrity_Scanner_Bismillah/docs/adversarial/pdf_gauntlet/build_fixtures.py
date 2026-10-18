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
PDF hidden-text adversarial gauntlet — fixture builder.

Six techniques a real engineer might use to hide text inside a PDF,
ordered from most naive to most sophisticated. Each emits a single
fixture file alongside a README entry describing what was hidden,
where, and how.

The visible (surface) text is always the same brief paragraph so the
scanner cannot use a "low text density" heuristic to flag the file.
The hidden (substrate) text is always the same payload so we can verify
end-to-end recovery.
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import white, black, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pikepdf

OUT = os.path.dirname(os.path.abspath(__file__)) + "/fixtures"
os.makedirs(OUT, exist_ok=True)

SURFACE_TEXT = (
    "Q3 financial summary — revenue grew 8% YoY to $1,000 thousand. "
    "Margins held steady. Cash position remains strong."
)
HIDDEN_PAYLOAD = "HIDDEN_TEXT_PAYLOAD: actual revenue $10,000 — see annex"


def fixture_01_white_on_white():
    """Hide text by drawing it in white on a white background."""
    path = f"{OUT}/01_white_on_white.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 11)
    c.drawString(72, 720, SURFACE_TEXT[:80])
    c.drawString(72, 700, SURFACE_TEXT[80:])
    # Now the hidden line in white
    c.setFillColor(white)
    c.drawString(72, 670, HIDDEN_PAYLOAD)
    c.save()
    return path, "White text on white background"


def fixture_02_font_size_zero():
    """Hide text by setting the font size to a fraction of a point."""
    path = f"{OUT}/02_font_size_microscopic.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 11)
    c.drawString(72, 720, SURFACE_TEXT[:80])
    c.drawString(72, 700, SURFACE_TEXT[80:])
    # Hidden line at sub-readable size
    c.setFont("Helvetica", 0.1)
    c.drawString(72, 670, HIDDEN_PAYLOAD)
    c.save()
    return path, "Font size 0.1pt (well below human-readable threshold)"


def fixture_03_off_page():
    """Hide text by drawing it outside the page's MediaBox."""
    path = f"{OUT}/03_off_page.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 11)
    c.drawString(72, 720, SURFACE_TEXT[:80])
    c.drawString(72, 700, SURFACE_TEXT[80:])
    # Coordinates outside the page (negative Y)
    c.drawString(72, -200, HIDDEN_PAYLOAD)
    c.save()
    return path, "Text positioned outside the page MediaBox at y=-200"


def fixture_04_metadata():
    """Hide text in PDF document info metadata (Keywords, Author, etc.)."""
    path = f"{OUT}/04_metadata.pdf"
    # First create a clean PDF
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 11)
    c.drawString(72, 720, SURFACE_TEXT[:80])
    c.drawString(72, 700, SURFACE_TEXT[80:])
    c.save()
    # Then inject hidden text into metadata via pikepdf
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    with pdf.open_metadata() as m:
        m["dc:description"] = HIDDEN_PAYLOAD
    pdf.docinfo["/Keywords"] = HIDDEN_PAYLOAD
    pdf.save(path)
    return path, "Hidden text injected into Keywords + dc:description metadata"


def fixture_05_after_eof():
    """Hide text by appending it to the file after the %%EOF marker."""
    path = f"{OUT}/05_after_eof.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 11)
    c.drawString(72, 720, SURFACE_TEXT[:80])
    c.drawString(72, 700, SURFACE_TEXT[80:])
    c.save()
    # Append hidden bytes after the trailer
    with open(path, "ab") as f:
        f.write(b"\n%% bayyinah-test-trailer\n")
        f.write(HIDDEN_PAYLOAD.encode() + b"\n")
    return path, "Hidden text appended after %%EOF marker"


def fixture_06_optional_content_group():
    """Hide text inside a hidden Optional Content Group (PDF layer)."""
    path = f"{OUT}/06_optional_content_group.pdf"
    # We'll do this by drawing the hidden text on a separate page and then
    # marking it as a hidden layer in post-processing. As a simpler proxy
    # for v1, we hide it via /Subtype /Hidden annotation text.
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 11)
    c.drawString(72, 720, SURFACE_TEXT[:80])
    c.drawString(72, 700, SURFACE_TEXT[80:])
    c.save()
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    page = pdf.pages[0]
    # Add a Text annotation with hidden flag (bit 2 of /F = hidden)
    annot = pikepdf.Dictionary(
        Type=pikepdf.Name("/Annot"),
        Subtype=pikepdf.Name("/Text"),
        Rect=[100, 100, 200, 120],
        Contents=HIDDEN_PAYLOAD,
        F=2,  # 2 = Hidden flag per PDF spec
    )
    if "/Annots" not in page:
        page["/Annots"] = pdf.make_indirect([])
    annots = page["/Annots"]
    annots.append(pdf.make_indirect(annot))
    pdf.save(path)
    return path, "Hidden text inside a /Text annotation with /F=2 (hidden flag)"


BUILDERS = [
    fixture_01_white_on_white,
    fixture_02_font_size_zero,
    fixture_03_off_page,
    fixture_04_metadata,
    fixture_05_after_eof,
    fixture_06_optional_content_group,
]

if __name__ == "__main__":
    for builder in BUILDERS:
        path, desc = builder()
        size = os.path.getsize(path)
        print(f"{os.path.basename(path):<40} {size:>7} bytes  — {desc}")

# Bismillah ir-Rahman ir-Rahim