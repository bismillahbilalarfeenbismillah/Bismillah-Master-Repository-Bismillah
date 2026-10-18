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
"""
Post-deploy verification for v1.1.4 on bayyinah.dev.

Usage (from any directory):
    python3 benchmarks/verify_v1_1_4_deploy.py

Probes:
    - GET /version: must return {"version": "1.1.4"}.
    - GET /healthz: must return {"status": "ok"}.

Exits 0 on all-green, 1 on any failure. Run after the Railway
deploy completes; do not run before merge.

Network access required. The script uses subprocess curl to keep
the dependency footprint at zero (no requests, no httpx). If
bayyinah.dev is unreachable the script prints the curl error and
exits 1.
"""
from __future__ import annotations

import json
import subprocess
import sys

EXPECTED_VERSION = "1.1.4"
EXPECTED_HEALTH = "ok"
TIMEOUT_S = 15

CHECKS: list[tuple[str, str]] = [
    ("Version", f"curl --max-time {TIMEOUT_S} -fsSL https://bayyinah.dev/version"),
    ("Health", f"curl --max-time {TIMEOUT_S} -fsSL https://bayyinah.dev/healthz"),
]


def run_check(name: str, cmd: str) -> tuple[bool, dict | str]:
    """Run cmd, parse JSON, return (ok, parsed-or-error-string)."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=TIMEOUT_S + 2
        )
    except subprocess.TimeoutExpired:
        return False, f"timed out after {TIMEOUT_S}s"
    if result.returncode != 0:
        return False, f"curl failed (exit {result.returncode}): {result.stderr.strip()}"
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return False, f"non-JSON response: {exc}; body: {result.stdout[:200]!r}"
    return True, data


def main() -> int:
    all_ok = True
    print("=" * 56)
    print("v1.1.4 post-deploy verification on bayyinah.dev")
    print("=" * 56)

    for name, cmd in CHECKS:
        ok, payload = run_check(name, cmd)
        if not ok:
            print(f"{name}: FAIL ({payload})")
            all_ok = False
            continue

        print(f"{name}: {payload}")

        if name == "Version":
            actual = payload.get("version") if isinstance(payload, dict) else None
            if actual != EXPECTED_VERSION:
                print(
                    f"  FAIL: expected version {EXPECTED_VERSION!r}, "
                    f"got {actual!r}"
                )
                all_ok = False

        if name == "Health":
            actual = payload.get("status") if isinstance(payload, dict) else None
            if actual != EXPECTED_HEALTH:
                print(
                    f"  FAIL: expected status {EXPECTED_HEALTH!r}, "
                    f"got {actual!r}"
                )
                all_ok = False

    print("=" * 56)
    if all_ok:
        print("All checks passed. v1.1.4 is live on bayyinah.dev.")
        return 0
    print("One or more checks failed. Investigate before announcing the ship.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

# Bismillah ir-Rahman ir-Rahim