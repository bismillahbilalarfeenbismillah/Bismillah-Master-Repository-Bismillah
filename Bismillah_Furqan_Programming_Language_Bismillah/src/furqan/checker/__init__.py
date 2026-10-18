# Bismillah ir-Rahman ir-Rahim
"""Furqan checker layer — public entry points for each primitive's checker."""

from .bismillah import (
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
    PRIMITIVE_NAME as BISMILLAH_PRIMITIVE_NAME,
    check_module as check_bismillah,
    check_module_strict as check_bismillah_strict,
)
from .zahir_batin import (
    PRIMITIVE_NAME as ZAHIR_BATIN_PRIMITIVE_NAME,
    VERIFY_FUNCTION_NAME,
    check_module as check_zahir_batin,
    check_module_strict as check_zahir_batin_strict,
)
from .additive import (
    PRIMITIVE_NAME as ADDITIVE_ONLY_PRIMITIVE_NAME,
    Result as AdditiveOnlyResult,
    check_additive,
    check_module as check_additive_module,
    check_module_strict as check_additive_module_strict,
)
from .incomplete import (
    PRIMITIVE_NAME as SCAN_INCOMPLETE_PRIMITIVE_NAME,
    REQUIRED_INCOMPLETE_FIELDS,
    INTEGRITY_TYPE_NAME,
    INCOMPLETE_TYPE_NAME,
    check_incomplete,
    check_incomplete_strict,
)
from .mizan import (
    PRIMITIVE_NAME as MIZAN_PRIMITIVE_NAME,
    REQUIRED_MIZAN_FIELDS,
    check_mizan,
    check_mizan_strict,
)
from .tanzil import (
    PRIMITIVE_NAME as TANZIL_PRIMITIVE_NAME,
    check_tanzil,
    check_tanzil_strict,
)
from .ring_close import (
    BUILTIN_TYPE_NAMES as RING_CLOSE_BUILTIN_TYPE_NAMES,
    PRIMITIVE_NAME as RING_CLOSE_PRIMITIVE_NAME,
    check_ring_close,
    check_ring_close_strict,
)
from .status_coverage import (
    PRIMITIVE_NAME as STATUS_COVERAGE_PRIMITIVE_NAME,
    check_status_coverage,
    check_status_coverage_strict,
)
from .return_type_match import (
    PRIMITIVE_NAME as RETURN_TYPE_MATCH_PRIMITIVE_NAME,
    check_return_type_match,
    check_return_type_match_strict,
)
from .all_paths_return import (
    PRIMITIVE_NAME as ALL_PATHS_RETURN_PRIMITIVE_NAME,
    check_all_paths_return,
    check_all_paths_return_strict,
)

__all__ = [
    # Bismillah scope (Phase 2.3)
    "BISMILLAH_PRIMITIVE_NAME",
    "check_bismillah",
    "check_bismillah_strict",
    # Zahir/batin (Phase 2.4)
    "ZAHIR_BATIN_PRIMITIVE_NAME",
    "VERIFY_FUNCTION_NAME",
    "check_zahir_batin",
    "check_zahir_batin_strict",
    # Additive-only module (Phase 2.5)
    "ADDITIVE_ONLY_PRIMITIVE_NAME",
    "AdditiveOnlyResult",
    "check_additive",
    "check_additive_module",
    "check_additive_module_strict",
    # Scan-incomplete (Phase 2.6)
    "SCAN_INCOMPLETE_PRIMITIVE_NAME",
    "REQUIRED_INCOMPLETE_FIELDS",
    "INTEGRITY_TYPE_NAME",
    "INCOMPLETE_TYPE_NAME",
    "check_incomplete",
    "check_incomplete_strict",
    # Mizan well-formedness (Phase 2.7)
    "MIZAN_PRIMITIVE_NAME",
    "REQUIRED_MIZAN_FIELDS",
    "check_mizan",
    "check_mizan_strict",
    # Tanzil build-ordering (Phase 2.8)
    "TANZIL_PRIMITIVE_NAME",
    "check_tanzil",
    "check_tanzil_strict",
    # Ring-close structural completion (Phase 2.9)
    "RING_CLOSE_PRIMITIVE_NAME",
    "RING_CLOSE_BUILTIN_TYPE_NAMES",
    "check_ring_close",
    "check_ring_close_strict",
    # Status-coverage / consumer-side exhaustiveness (D11, v0.8.0)
    "STATUS_COVERAGE_PRIMITIVE_NAME",
    "check_status_coverage",
    "check_status_coverage_strict",
    # Return-expression type matching (D22, v0.8.1)
    "RETURN_TYPE_MATCH_PRIMITIVE_NAME",
    "check_return_type_match",
    "check_return_type_match_strict",
    # All-paths-return analysis (D24, v0.8.2)
    "ALL_PATHS_RETURN_PRIMITIVE_NAME",
    "check_all_paths_return",
    "check_all_paths_return_strict",
]

# Bismillah ir-Rahman ir-Rahim