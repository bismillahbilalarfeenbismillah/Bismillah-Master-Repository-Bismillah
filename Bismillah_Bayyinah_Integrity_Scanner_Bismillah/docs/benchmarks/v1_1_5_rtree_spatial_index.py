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
v1.1.5 spatial-index benchmark.

Reruns the four-density panel from v1.1.4 to measure the impact of the
overlapping_text spatial pre-filter (uniform grid candidate generator).
P50 over 5 measured runs (preceded by a single warm-up run discarded).

Densities measured:
  - white_paper: 19-page typeset Bayyinah white paper (native text, light)
  - clean_50p:   50-page synthesized native-text PDF (medium density)
  - safety_220p: 220-page international AI safety report (dense, native text)
  - gauntlet_metadata: adversarial fixture (Tier 1 severity-1.0 metadata
    anomaly), measured in forensic mode and production mode for the
    early-return delta.

Outputs Markdown report at docs/benchmarks/v1_1_5_rtree_spatial_index.md.

Run
---
    python3 docs/benchmarks/v1_1_5_rtree_spatial_index.py
"""
import statistics
import sys
import time
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import bayyinah  # noqa: E402

assert Path(bayyinah.__file__).resolve().is_relative_to(_REPO_ROOT), (
    f"bayyinah imported from {bayyinah.__file__} but expected a path "
    f"under {_REPO_ROOT}. Uninstall any pip-installed bayyinah."
)


PANEL = [
    ("white_paper_19p",
     "papers/Bayyinah_White_Paper.pdf",
     "19-page typeset white paper (native text)"),
    ("clean_50p_native",
     "docs/benchmarks/clean_50pg.pdf",
     "50-page synthesized native-text PDF"),
    ("safety_report_220p",
     "/home/user/workspace/international-ai-safety-report-2026_1.pdf",
     "220-page native-text dense report"),
]

GAUNTLET_FIXTURE = (
    "gauntlet_metadata_severity_1",
    "docs/adversarial/pdf_gauntlet/fixtures/04_metadata.pdf",
    "Adversarial Tier 1 severity-1.0 metadata anomaly",
)

RUNS = 5


def time_one(path: str, mode: str | None = None) -> float:
    t0 = time.perf_counter()
    if mode is None:
        bayyinah.scan_file(path)
    else:
        bayyinah.scan_file(path, mode=mode)
    return (time.perf_counter() - t0) * 1000.0


def measure(path: Path, mode: str | None = None) -> dict:
    """One warm-up + RUNS measured iterations. Returns p50/min/max/mean."""
    if not path.exists():
        return {"error": f"not found: {path}"}
    # Warm-up.
    time_one(str(path), mode=mode)
    samples = [time_one(str(path), mode=mode) for _ in range(RUNS)]
    samples_sorted = sorted(samples)
    return {
        "samples_ms": samples,
        "p50_ms": statistics.median(samples),
        "min_ms": min(samples),
        "max_ms": max(samples),
        "mean_ms": statistics.mean(samples),
        "stdev_ms": statistics.stdev(samples) if len(samples) > 1 else 0.0,
    }


def fmt_row(label: str, desc: str, r: dict) -> str:
    if "error" in r:
        return f"| {label} | {desc} | _{r['error']}_ |"
    return (
        f"| {label} | {desc} | "
        f"{r['p50_ms']:.0f} | "
        f"{r['min_ms']:.0f} | "
        f"{r['max_ms']:.0f} | "
        f"{r['mean_ms']:.0f} | "
        f"{r['stdev_ms']:.0f} |"
    )


def main() -> None:
    print(f"bayyinah version: {bayyinah.__version__}")
    print(f"runs per fixture: {RUNS} (plus 1 warm-up)\n")

    panel_results = []
    for label, rel, desc in PANEL:
        path = Path(rel) if not Path(rel).is_absolute() else Path(rel)
        if not path.is_absolute():
            path = _REPO_ROOT / rel
        print(f"-- {label}: {path}")
        r = measure(path)
        if "error" not in r:
            print(f"   p50={r['p50_ms']:.0f}ms  min={r['min_ms']:.0f}ms  "
                  f"max={r['max_ms']:.0f}ms  stdev={r['stdev_ms']:.0f}ms")
        else:
            print(f"   {r['error']}")
        panel_results.append((label, desc, r))

    # Production-mode delta on the gauntlet fixture.
    g_label, g_rel, g_desc = GAUNTLET_FIXTURE
    g_path = _REPO_ROOT / g_rel
    print(f"\n-- {g_label} (forensic mode): {g_path}")
    forensic = measure(g_path, mode="forensic")
    if "error" not in forensic:
        print(f"   p50={forensic['p50_ms']:.0f}ms  "
              f"stdev={forensic['stdev_ms']:.0f}ms")
    print(f"-- {g_label} (production mode): {g_path}")
    production = measure(g_path, mode="production")
    if "error" not in production:
        print(f"   p50={production['p50_ms']:.0f}ms  "
              f"stdev={production['stdev_ms']:.0f}ms")

    # Write report.
    lines = [
        f"# v{bayyinah.__version__} spatial-index benchmark",
        "",
        "Reruns the v1.1.4 four-density panel after the v1.1.5 ",
        "`overlapping_text` spatial pre-filter ships, to measure the ",
        "impact on dense-PDF scan time.",
        "",
        "## Methodology",
        "",
        f"Single-threaded `bayyinah.scan_file` wall-clock measured with "
        f"`time.perf_counter()`. {RUNS} measured runs per fixture preceded "
        "by one discarded warm-up run. Same code path as the `/scan` HTTP "
        "endpoint minus FastAPI request decode and network round-trip.",
        "",
        "## Four-density panel (forensic mode)",
        "",
        "| Fixture | Description | P50 ms | Min ms | Max ms | Mean ms | Stdev ms |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for label, desc, r in panel_results:
        lines.append(fmt_row(label, desc, r))

    lines += [
        "",
        "## Production-mode early return on Tier 1 severity-1.0 finding",
        "",
        f"Fixture: `{g_rel}` ({g_desc})",
        "",
        "| Mode | P50 ms | Min ms | Max ms | Stdev ms |",
        "|---|---:|---:|---:|---:|",
    ]
    if "error" not in forensic:
        lines.append(
            f"| forensic | {forensic['p50_ms']:.0f} | "
            f"{forensic['min_ms']:.0f} | {forensic['max_ms']:.0f} | "
            f"{forensic['stdev_ms']:.0f} |"
        )
    if "error" not in production:
        lines.append(
            f"| production | {production['p50_ms']:.0f} | "
            f"{production['min_ms']:.0f} | {production['max_ms']:.0f} | "
            f"{production['stdev_ms']:.0f} |"
        )
    if "error" not in forensic and "error" not in production:
        delta_pct = 100.0 * (1.0 - production["p50_ms"] / forensic["p50_ms"])
        lines += [
            "",
            f"Production mode returns early on the first Tier 1 severity-1.0 "
            f"finding. P50 reduction: **{delta_pct:.0f}%** "
            f"({forensic['p50_ms']:.0f}ms to {production['p50_ms']:.0f}ms).",
        ]

    lines += [
        "",
        "## Reproduction",
        "",
        "```",
        "python3 docs/benchmarks/v1_1_5_rtree_spatial_index.py",
        "```",
        "",
    ]

    out = _REPO_ROOT / "docs/benchmarks/v1_1_5_rtree_spatial_index.md"
    out.write_text("\n".join(lines))
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()

# Bismillah ir-Rahman ir-Rahim