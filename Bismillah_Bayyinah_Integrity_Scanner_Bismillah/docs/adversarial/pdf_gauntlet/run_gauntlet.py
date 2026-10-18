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
Run the six PDF hidden-text fixtures against the live API and capture
the full structured response. Output: results.json + a printable summary.
"""
import json
import os
import subprocess
import sys

FIXTURES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/fixtures"
RESULTS_PATH = os.path.dirname(os.path.abspath(__file__)) + "/results.json"
URL = "https://bayyinah.dev/scan"
RESOLVE = "bayyinah.dev:443:104.21.33.67"


def scan(path):
    out = subprocess.check_output([
        "curl", "-s", "--resolve", RESOLVE,
        "-X", "POST", "-F", f"file=@{path}", URL,
    ])
    return json.loads(out)


def summarise(name, data):
    score = data.get("integrity_score")
    incomplete = data.get("scan_incomplete")
    findings = data.get("findings", [])
    tier_counts = {1: 0, 2: 0, 3: 0}
    for f in findings:
        tier_counts[f.get("tier", 3)] += 1

    # Did any finding's inversion_recovery.concealed contain our payload?
    payload_recovered = False
    payload_recovered_via = None
    for f in findings:
        ir = f.get("inversion_recovery") or {}
        concealed = (ir.get("concealed") or "")
        if "HIDDEN_TEXT_PAYLOAD" in concealed or "10,000" in concealed:
            payload_recovered = True
            payload_recovered_via = f.get("mechanism")
            break

    # Or did any finding's location/description mention the payload?
    if not payload_recovered:
        for f in findings:
            blob = json.dumps(f)
            if "HIDDEN_TEXT_PAYLOAD" in blob or "actual revenue" in blob:
                payload_recovered = True
                payload_recovered_via = f.get("mechanism") + " (in description/location)"
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
    fixtures = sorted(os.listdir(FIXTURES_DIR))
    fixtures = [f for f in fixtures if f.endswith(".pdf")]
    results = []
    for fixture in fixtures:
        path = f"{FIXTURES_DIR}/{fixture}"
        print(f"==> scanning {fixture}", file=sys.stderr)
        try:
            data = scan(path)
            summary = summarise(fixture, data)
            summary["raw"] = data
            results.append(summary)
        except Exception as e:
            results.append({"fixture": fixture, "error": str(e)})

    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'Fixture':<40} {'Score':<7} {'Findings':<10} {'Tier 1/2/3':<12} {'Recovered?':<10}")
    print("-" * 95)
    for r in results:
        if "error" in r:
            print(f"{r['fixture']:<40} ERROR: {r['error']}")
            continue
        tc = r["tier_counts"]
        tier_str = f"{tc[1]}/{tc[2]}/{tc[3]}"
        rec = "YES (" + (r["payload_recovered_via"] or "") + ")" if r["payload_recovered"] else "NO"
        print(f"{r['fixture']:<40} {r['score']:<7} {r['n_findings']:<10} {tier_str:<12} {rec}")


if __name__ == "__main__":
    main()

# Bismillah ir-Rahman ir-Rahim