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
"""Build a clean pdfTeX article using \\usepackage{hyperref}, which
causes pdfTeX to emit /OpenAction = {/S: /GoTo, /D: [...]} (a GoTo
action wrapping a destination). This is the shape Bilal's resume
PDF carried in the incident report (Round 12 Bug 1, case 2).

Output: fixture_clean_pdftex_with_hyperref.pdf
"""
from __future__ import annotations
import os
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
TEX_SOURCE = r"""\documentclass[11pt]{article}
\usepackage{hyperref}
\hypersetup{pdfstartview={XYZ null null 1.0}}
\title{Round 12 Reproducer (pdfTeX with hyperref)}
\author{Test Author}
\date{}
\begin{document}
\maketitle
\section{Section A}
This document uses hyperref, which causes pdfTeX to emit
/OpenAction with a /GoTo subtype wrapping a destination array.
Per ISO 32000-1 \S12.6.3, /GoTo is navigation, not active
content. Office, file, fluffy ligatures.
\section{Section B}
More content. Quotes ``hello'' and `world'.
\end{document}
"""


def build(output_path: Path) -> None:
    workdir = output_path.parent / "_build_pdftex_hyperref"
    workdir.mkdir(parents=True, exist_ok=True)
    tex_path = workdir / "article.tex"
    tex_path.write_text(TEX_SOURCE)
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = "0"
    for _ in range(2):
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "article.tex"],
            cwd=workdir, env=env, check=True, capture_output=True,
        )
    (workdir / "article.pdf").rename(output_path)
    for ext in (".tex", ".aux", ".log", ".out"):
        for f in workdir.glob(f"*{ext}"):
            f.unlink(missing_ok=True)
    workdir.rmdir()


if __name__ == "__main__":
    out = HERE / "fixture_clean_pdftex_with_hyperref.pdf"
    build(out)
    print(f"wrote {out} ({out.stat().st_size} bytes)")

# Bismillah ir-Rahman ir-Rahim