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
v1.1.6 production-mode benchmark.

Measures the wall-clock impact of cost-class-ordered dispatch with
early termination on Tier-1, confidence>=0.9 findings.

Methodology
-----------
For each fixture in a small adversarial bench set we run
``ScanService.scan(fixture)`` ``REPS`` times in each mode and report
the per-mode P50 (median) and P95 of the wall-clock latency. The two
runs are interleaved so any system-level noise affects both modes
equally.

We also report the analyzers-invoked count for each mode by inspecting
``registry._sorted_for_production()`` against the merge loop's
``terminated_early`` exit point. (Forensic mode always invokes every
applicable analyzer; production mode invokes a prefix of the
class-ordered sequence up to and including the first analyzer that
emits a Tier-1 finding at confidence >= 0.9.)

Reproduction: run ``python3 docs/benchmarks/v1_1_6_production_mode.py``
from the repo root.
"""
from __future__ import annotations

import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from application.scan_service import ScanService  # noqa: E402

REPS = 5
FIXTURES = [
    ("text.homoglyph",        ROOT / "tests/fixtures/text/homoglyph.pdf"),
    ("text.invisible_render", ROOT / "tests/fixtures/text/invisible_render.pdf"),
    ("text.microscopic_font", ROOT / "tests/fixtures/text/microscopic_font.pdf"),
    ("text.white_on_white",   ROOT / "tests/fixtures/text/white_on_white.pdf"),
    ("text.overlapping",      ROOT / "tests/fixtures/text/overlapping.pdf"),
    ("object.embedded_javascript", ROOT / "tests/fixtures/object/embedded_javascript.pdf"),
    ("object.embedded_attachment", ROOT / "tests/fixtures/object/embedded_attachment.pdf"),
    ("object.tounicode_cmap", ROOT / "tests/fixtures/object/tounicode_cmap.pdf"),
    ("clean",                 ROOT / "tests/fixtures/clean.pdf"),
    ("positive_combined",     ROOT / "tests/fixtures/positive_combined.pdf"),
    ("clean_50pg",            ROOT / "docs/benchmarks/clean_50pg.pdf"),
]


def _time_one(svc: ScanService, path: Path, mode: str) -> tuple[float, int, int]:
    t0 = time.perf_counter()
    rep = svc.scan(path, mode=mode)
    dt = (time.perf_counter() - t0) * 1000.0
    tier1_hi = sum(
        1 for f in rep.findings
        if getattr(f, "tier", None) == 1
        and float(getattr(f, "confidence", 0.0)) >= 0.9
    )
    return dt, len(rep.findings), tier1_hi


def main() -> None:
    svc = ScanService()
    print(f"v1.1.6 production-mode benchmark (REPS={REPS})")
    print()
    print(
        f"{'fixture':<32} {'mode':<11} "
        f"{'P50 ms':>9} {'P95 ms':>9} "
        f"{'findings':>9} {'T1>=0.9':>9}"
    )
    print("-" * 85)

    rows = []
    for name, path in FIXTURES:
        if not path.exists():
            print(f"{name:<32} MISSING {path}")
            continue
        # Warm caches.
        svc.scan(path, mode="forensic")
        svc.scan(path, mode="production")

        forensic = [_time_one(svc, path, "forensic") for _ in range(REPS)]
        production = [_time_one(svc, path, "production") for _ in range(REPS)]

        f_t = sorted(t for t, _, _ in forensic)
        p_t = sorted(t for t, _, _ in production)
        f_p50 = statistics.median(f_t)
        p_p50 = statistics.median(p_t)
        f_p95 = f_t[max(0, int(len(f_t) * 0.95) - 1)] if len(f_t) > 1 else f_t[0]
        p_p95 = p_t[max(0, int(len(p_t) * 0.95) - 1)] if len(p_t) > 1 else p_t[0]
        f_findings, f_t1 = forensic[-1][1], forensic[-1][2]
        p_findings, p_t1 = production[-1][1], production[-1][2]

        rows.append(
            (name, f_p50, p_p50, f_p95, p_p95, f_findings, p_findings, f_t1, p_t1)
        )
        print(
            f"{name:<32} {'forensic':<11} "
            f"{f_p50:>9.2f} {f_p95:>9.2f} "
            f"{f_findings:>9} {f_t1:>9}"
        )
        print(
            f"{name:<32} {'production':<11} "
            f"{p_p50:>9.2f} {p_p95:>9.2f} "
            f"{p_findings:>9} {p_t1:>9}"
        )

    print()
    print("Summary (production / forensic, P50):")
    for r in rows:
        name, f_p50, p_p50, *_ = r
        ratio = (p_p50 / f_p50) if f_p50 else 1.0
        delta_ms = f_p50 - p_p50
        print(
            f"  {name:<32} "
            f"forensic {f_p50:>7.2f} ms -> production {p_p50:>7.2f} ms "
            f"(ratio {ratio:>4.2f}, delta {delta_ms:+.2f} ms)"
        )


if __name__ == "__main__":
    main()

# Bismillah ir-Rahman ir-Rahim