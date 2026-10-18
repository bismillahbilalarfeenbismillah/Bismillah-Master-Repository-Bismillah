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
HTML hidden-text / prompt-injection adversarial gauntlet — fixture builder.

Six concealment techniques targeting v1.1.1 ``HtmlAnalyzer`` gaps.
We deliberately avoid the well-armored vectors: ``style="display:none"``,
``hidden`` boolean attribute, ``aria-hidden=true``, off-screen positioning,
``on*`` event handlers, ``<script src=...>`` external refs, and long
``data-*`` attributes — those are caught and we are looking for the
misses.

Surface text mentions $1,000 in revenue. Hidden payload mentions $10,000.
Same canonical contract-fraud setup.

Fixtures
--------

01 — Payload inside ``<noscript>`` (analyzer skips noscript content)
02 — Payload inside ``<template>`` (analyzer skips template content)
03 — Payload in HTML comment (analyzer scans comments for unicode
     concealment but not for plaintext divergence / payload bodies)
04 — Payload in ``<meta name="..." content="...">`` content attribute
05 — Payload in CSS ``content:`` pseudo-element via ``<style>`` body
     (analyzer skips style bodies entirely)
06 — Payload inside ``<title>`` (rendered in the tab/header but not in
     the document body — many extractors only walk the body)
"""

from __future__ import annotations

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


def _wrap(body: str, head_extra: str = "") -> str:
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="UTF-8">\n'
        "<title>Q3 Summary</title>\n"
        f"{head_extra}"
        "</head>\n"
        f"<body>\n{body}\n</body>\n</html>\n"
    )


def fixture_01_noscript() -> tuple[Path, str]:
    path = OUT / "01_noscript.html"
    body = (
        f'<p>{SURFACE_TEXT}</p>\n'
        f'<noscript>{HIDDEN_PAYLOAD}</noscript>'
    )
    path.write_text(_wrap(body), "utf-8")
    return path, "Payload inside <noscript> element"


def fixture_02_template() -> tuple[Path, str]:
    path = OUT / "02_template.html"
    body = (
        f'<p>{SURFACE_TEXT}</p>\n'
        f'<template id="invoice">{HIDDEN_PAYLOAD}</template>'
    )
    path.write_text(_wrap(body), "utf-8")
    return path, "Payload inside <template> element"


def fixture_03_comment_payload() -> tuple[Path, str]:
    """Plaintext payload in an HTML comment.

    The analyzer scans comment text for unicode concealment codepoints
    (zero-width / TAG / bidi / homoglyph) but does not flag a comment
    body that simply *contains a payload*. A long phishing or
    prompt-injection comment passes through untouched.
    """
    path = OUT / "03_comment_payload.html"
    body = (
        f'<p>{SURFACE_TEXT}</p>\n'
        f'<!-- {HIDDEN_PAYLOAD} -->'
    )
    path.write_text(_wrap(body), "utf-8")
    return path, "Plaintext payload inside an HTML comment"


def fixture_04_meta_content() -> tuple[Path, str]:
    """Payload in <meta name="..." content="...">.

    Analyzer does not enumerate meta tags as text-bearing. SEO crawlers
    and many LLM ingest paths read meta description verbatim.
    """
    path = OUT / "04_meta_content.html"
    head = (
        f'<meta name="description" content="{HIDDEN_PAYLOAD}">\n'
        f'<meta name="keywords" content="{HIDDEN_PAYLOAD}">\n'
    )
    body = f'<p>{SURFACE_TEXT}</p>'
    path.write_text(_wrap(body, head_extra=head), "utf-8")
    return path, "Payload in <meta name=description content=...>"


def fixture_05_css_content() -> tuple[Path, str]:
    """Payload inside CSS via ::before content:.

    The text is *rendered to the user* by the browser (CSS-generated
    content is real text on the page) but the analyzer skips <style>
    bodies entirely, so the payload is invisible to it.
    """
    path = OUT / "05_css_content.html"
    head = (
        '<style>\n'
        '.invoice-note::before {\n'
        f'  content: "{HIDDEN_PAYLOAD}";\n'
        '  color: white;\n'
        '}\n'
        '</style>\n'
    )
    body = (
        f'<p>{SURFACE_TEXT}</p>\n'
        '<p class="invoice-note">See note below.</p>'
    )
    path.write_text(_wrap(body, head_extra=head), "utf-8")
    return path, "Payload in CSS ::before content: rule"


def fixture_06_title_payload() -> tuple[Path, str]:
    """Payload inside <title>.

    Rendered in the tab/title bar but not in the body. Many text
    extractors that traverse only the body or strip <head> entirely
    miss it.
    """
    path = OUT / "06_title_payload.html"
    full = (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="UTF-8">\n'
        f"<title>{HIDDEN_PAYLOAD}</title>\n"
        "</head>\n"
        f"<body>\n<p>{SURFACE_TEXT}</p>\n</body>\n</html>\n"
    )
    path.write_text(full, "utf-8")
    return path, "Payload as the <title> text"


BUILDERS = [
    fixture_01_noscript,
    fixture_02_template,
    fixture_03_comment_payload,
    fixture_04_meta_content,
    fixture_05_css_content,
    fixture_06_title_payload,
]


if __name__ == "__main__":
    for builder in BUILDERS:
        path, desc = builder()
        size = path.stat().st_size
        print(f"{path.name:<40} {size:>7} bytes  - {desc}")

# Bismillah ir-Rahman ir-Rahim