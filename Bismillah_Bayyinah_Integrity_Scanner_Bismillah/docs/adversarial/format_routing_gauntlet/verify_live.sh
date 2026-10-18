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
#!/usr/bin/env bash
# Day 1 live-curl verification gate (v1.1.2 prompt section 3.2).
#
# Runs after deploying v1.1.2 to bayyinah.dev. All three commands
# below must return `true` for Day 1 to be considered complete and
# Day 2 (PDF) to begin. From the prompt:
#
#   "All three must return `true`. If any return `false`, Day 1 is
#    not complete and Day 2 does not begin."
#
# Cannot run from the build sandbox - bayyinah.dev is the live
# Cloudflare-fronted Railway deployment, and the v1.1.2 code in
# this branch has not been pushed yet. Run this on the deploy
# machine after `git push` and Railway rolls v1.1.2 forward.

set -euo pipefail

GAUNTLET="docs/adversarial/format_routing_gauntlet/fixtures"

echo "v1.1.2 Day 1 live-curl gate -> https://bayyinah.dev/scan"
echo "================================================================"

echo
echo "V1: polyglot must return mughlaq with Tier 0 finding"
v1=$(curl -s https://bayyinah.dev/scan \
        -F "file=@$GAUNTLET/01_polyglot.docx" \
     | jq -e '.verdict == "mughlaq" and (.findings | any(.tier == 0))')
echo "  result: $v1"

echo
echo "V2: PDF-as-txt must return mughlaq with Tier 0 finding"
v2=$(curl -s https://bayyinah.dev/scan \
        -F "file=@$GAUNTLET/02_pdf_as_txt.txt" \
     | jq -e '.verdict == "mughlaq" and (.findings | any(.tier == 0))')
echo "  result: $v2"

echo
echo "V5: 4-byte text must return mughlaq (not sahih)"
printf 'aaaa' > /tmp/v5.txt
v5=$(curl -s https://bayyinah.dev/scan \
        -F "file=@/tmp/v5.txt" \
     | jq -e '.verdict == "mughlaq"')
echo "  result: $v5"
rm -f /tmp/v5.txt

echo
echo "================================================================"
if [[ "$v1" == "true" && "$v2" == "true" && "$v5" == "true" ]]; then
    echo "  ALL PASS - Day 1 complete; Day 2 (PDF) may begin."
    exit 0
else
    echo "  AT LEAST ONE FAIL - Day 1 NOT complete."
    echo "  v1=$v1  v2=$v2  v5=$v5"
    exit 1
fi

# Bismillah ir-Rahman ir-Rahim