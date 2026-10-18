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
Local PDF gauntlet runner: scans the six fixtures against the locally
installed Bayyinah package (whatever HEAD is checked out) using
``bayyinah.scan_file`` directly, with no HTTP round-trip. Output is the
same shape as run_gauntlet.py so before/after comparison is honest.
"""
import json
import os
import sys

# Ensure the local source tree is importable in preference to any installed
# version.
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/../../.."
sys.path.insert(0, os.path.abspath(ROOT))

from bayyinah import scan_file, TOOL_VERSION  # noqa: E402

FIXTURES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/fixtures"
RESULTS_PATH = os.path.dirname(os.path.abspath(__file__)) + "/results_local.json"


def summarise(name, report_dict):
    score = report_dict.get("integrity_score")
    incomplete = report_dict.get("scan_incomplete")
    findings = report_dict.get("findings", [])
    tier_counts = {1: 0, 2: 0, 3: 0}
    for f in findings:
        tier_counts[f.get("tier", 3)] += 1

    payload_recovered = False
    payload_recovered_via = None
    for f in findings:
        ir = f.get("inversion_recovery") or {}
        concealed = (ir.get("concealed") or "")
        if "HIDDEN_TEXT_PAYLOAD" in concealed or "10,000" in concealed:
            payload_recovered = True
            payload_recovered_via = f.get("mechanism")
            break

    if not payload_recovered:
        for f in findings:
            blob = json.dumps(f)
            if "HIDDEN_TEXT_PAYLOAD" in blob or "actual revenue" in blob:
                payload_recovered = True
                payload_recovered_via = (f.get("mechanism") or "?") + " (in description/location)"
                break

    return {
        "fixture": name,
        "score": score,
        "scan_incomplete": incomplete,
        "n_findings": len(findings),
        "tier_counts": tier_counts,
        "mechanisms": sorted({f.get("mechanism", "?") for f in findings}),
        "payload_recovered": payload_recovered,
        "payload_recovered_via": payload_recovered_via,
    }


def main():
    print(f"Bayyinah TOOL_VERSION = {TOOL_VERSION}", file=sys.stderr)
    fixtures = sorted(os.listdir(FIXTURES_DIR))
    fixtures = [f for f in fixtures if f.endswith(".pdf")]
    results = []
    for fixture in fixtures:
        path = f"{FIXTURES_DIR}/{fixture}"
        print(f"==> scanning {fixture}", file=sys.stderr)
        try:
            report = scan_file(path)
            data = report.to_dict() if hasattr(report, "to_dict") else dict(report)
            summary = summarise(fixture, data)
            summary["raw"] = data
            results.append(summary)
        except Exception as e:
            import traceback
            results.append({"fixture": fixture, "error": str(e), "trace": traceback.format_exc()})

    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n{'Fixture':<40} {'Score':<7} {'Findings':<10} {'Tier 1/2/3':<12} {'Recovered?':<10}")
    print("-" * 95)
    for r in results:
        if "error" in r:
            print(f"{r['fixture']:<40} ERROR: {r['error']}")
            continue
        tc = r["tier_counts"]
        tier_str = f"{tc[1]}/{tc[2]}/{tc[3]}"
        rec = "YES (" + (r["payload_recovered_via"] or "") + ")" if r["payload_recovered"] else "NO"
        print(f"{r['fixture']:<40} {str(r['score']):<7} {r['n_findings']:<10} {tier_str:<12} {rec}")


if __name__ == "__main__":
    main()

# Bismillah ir-Rahman ir-Rahim