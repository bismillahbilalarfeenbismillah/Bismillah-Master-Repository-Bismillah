# Bismillah ir-Rahman ir-Rahim
"""
Bismillah scope checker — Furqan Phase 2.3 primitive #1.
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

Per the Furqan thesis paper §3.1, every module opens with a Bismillah
block declaring four fields: authority, serves, scope, not_scope. The
compiler verifies that no code in the module body operates outside
the declared scope. The Phase-2 prototype enforces a sharper subset of
this rule that is mechanically decidable from the AST alone:

    For every CallRef ``c`` reachable from any FunctionDef in the
    module, ``c.head`` must NOT appear in the module's
    ``BismillahBlock.not_scope`` list.

This is the language-level instantiation of the M1 principle (Ashraf):
*silent violations are the worst failure mode*. A function that
invokes a name the module has explicitly excluded is a silent
violation of the module's own declared scope. The checker makes the
violation loud.

What this checker does NOT do (out of scope for this primitive — see
the soundness note in thesis §3.1):

* It does not verify that the implementation matches the *semantic
  intent* of the scope clause. A module declaring
  ``scope: scan, report`` and implementing only ``scan`` passes; the
  thesis paper §7 reflexivity analysis names this Failure Mode 1
  (dishonest Bismillah declarations) and the safeguard is human
  review, not the compiler.
* It does not perform name resolution beyond the head identifier of a
  call path. ``stdlib.io.read()`` is checked against the head
  ``stdlib``. The full namespace-aware checker is a Phase-3 surface.
* It does not check that scope-listed operations are actually
  *performed* — that is the ring_close primitive's responsibility
  (Furqan thesis §3.6), implemented in a later session.
"""

from __future__ import annotations

from typing import Iterable

from furqan.errors.marad import Marad, MaradError, raise_marad
from furqan.parser.ast_nodes import (
    BismillahBlock,
    CallRef,
    FunctionDef,
    Module,
)


PRIMITIVE_NAME: str = "bismillah"


def check_module(module: Module) -> list[Marad]:
    """Run the Bismillah scope check over a parsed :class:`Module`.

    Returns a list of :class:`Marad` records, one per violation. An
    empty list means the module is structurally compliant with its
    own Bismillah declaration.

    The function is fail-soft (returns rather than raises) so a Phase-3
    multi-error reporter can aggregate diagnostics across primitives.
    Callers that prefer fail-fast semantics should use
    :func:`check_module_strict`.
    """
    not_scope_set = frozenset(module.bismillah.not_scope)
    if not not_scope_set:
        # An empty not_scope is permitted — the module declares no
        # exclusions. The thesis paper does not require not_scope to
        # be non-empty; a module that intentionally allows everything
        # has nothing for this checker to verify.
        return []

    diagnostics: list[Marad] = []
    for fn in module.functions:
        diagnostics.extend(_check_function(fn, module.bismillah, not_scope_set))
    return diagnostics


def check_module_strict(module: Module) -> None:
    """Fail-fast variant: raises :class:`MaradError` on the first
    violation.

    Equivalent to ``check_module(module)`` followed by raising the
    first marad. Preserves the rendered diagnosis on the exception's
    ``.marad`` attribute for callers that need structured access.
    """
    diagnostics = check_module(module)
    if diagnostics:
        raise MaradError(diagnostics[0])


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------

def _check_function(
    fn: FunctionDef,
    bismillah: BismillahBlock,
    not_scope_set: frozenset[str],
) -> Iterable[Marad]:
    for call in fn.calls:
        if call.head in not_scope_set:
            yield _scope_violation_marad(call, fn, bismillah)


def _scope_violation_marad(
    call: CallRef,
    fn: FunctionDef,
    bismillah: BismillahBlock,
) -> Marad:
    """Construct the diagnostic for a single not_scope violation.

    The message names the offending symbol, the function it was found
    in, the Bismillah block that excluded it, and the alias the user
    used to write the block (``bismillah`` or ``scope_block``). A
    reader of the diagnostic should be able to point to the exact
    line of the source text the rule violates.
    """
    return Marad(
        primitive=PRIMITIVE_NAME,
        diagnosis=(
            f"function {fn.name!r} invokes {call.qualified!r}, but "
            f"{call.head!r} appears in the {bismillah.alias_used} block "
            f"{bismillah.name!r}'s not_scope. Per Furqan thesis §3.1 "
            f"the module excluded this operation by declaration; the "
            f"call is a silent scope violation that the compiler "
            f"makes loud."
        ),
        location=call.span,
        minimal_fix=(
            f"either remove {call.qualified!r} from {fn.name!r}, or "
            f"remove {call.head!r} from {bismillah.name!r}'s not_scope "
            f"list (and accept that the module's stated exclusions are "
            f"weaker than they were)."
        ),
        regression_check=(
            f"after the fix, re-run the Bismillah scope check; the "
            f"module must produce zero diagnostics, and any test that "
            f"relied on the prior exclusion of {call.head!r} must "
            f"still pass."
        ),
    )


__all__ = [
    "PRIMITIVE_NAME",
    "check_module",
    "check_module_strict",
]

# Bismillah ir-Rahman ir-Rahim