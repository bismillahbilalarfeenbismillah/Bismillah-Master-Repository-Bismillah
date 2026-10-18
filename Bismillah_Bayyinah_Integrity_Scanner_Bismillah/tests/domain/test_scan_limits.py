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
Tests for ``ScanLimits`` + the thread-local limits context
(``get_current_limits`` / ``set_current_limits`` / ``limits_context``).

Phase 21 contract (Al-Baqarah 2:286: "Allah does not burden a soul
beyond its capacity"). ``ScanLimits`` is the one place the scanner's
capacity ceilings are declared; analyzers read ``get_current_limits()``
to decide whether to halt a per-item loop. Limits are frozen
(immutable per instance), installed via a context manager scoped to
each ``ScanService.scan()`` call, and validated at construction
(``max_file_size_bytes`` must be positive; per-item ceilings must be
non-negative).

The tests here assert that contract; the per-analyzer integration
tests in ``tests/analyzers/test_fallback_analyzer.py`` and
``tests/application/test_scan_service.py`` assert the end-to-end
behaviour (``scan_limited`` findings on concrete oversized /
recursion-deep / row-bomb inputs).
"""

from __future__ import annotations

import threading

import pytest

from domain import (
    DEFAULT_LIMITS,
    ScanLimits,
    get_current_limits,
    limits_context,
    set_current_limits,
)


# ---------------------------------------------------------------------------
# Dataclass shape
# ---------------------------------------------------------------------------


def test_default_limits_values() -> None:
    """The shipped defaults match the documented ceilings. If these
    ever change the CHANGELOG / README must be updated — the test
    pins the numbers so that coupling is visible in code review."""
    assert DEFAULT_LIMITS.max_file_size_bytes == 256 * 1024 * 1024  # 256 MB
    assert DEFAULT_LIMITS.max_recursion_depth == 5
    assert DEFAULT_LIMITS.max_csv_rows == 200_000
    assert DEFAULT_LIMITS.max_field_length == 4 * 1024 * 1024        # 4 MiB
    assert DEFAULT_LIMITS.max_eml_attachments == 64


def test_scan_limits_is_frozen() -> None:
    """Frozen dataclass — reassigning a field raises."""
    lim = ScanLimits()
    with pytest.raises(Exception):
        lim.max_file_size_bytes = 1  # type: ignore[misc]


def test_scan_limits_equality_by_value() -> None:
    """Two instances with the same values compare equal (dataclass
    default). Used so test fixtures can assert the current limits are
    what they installed."""
    a = ScanLimits(max_csv_rows=100)
    b = ScanLimits(max_csv_rows=100)
    assert a == b
    c = ScanLimits(max_csv_rows=101)
    assert a != c


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def test_zero_file_size_bytes_raises() -> None:
    """A zero file-size ceiling would refuse every file. Reject at
    construction time with a message explaining the escape hatch."""
    with pytest.raises(ValueError, match="max_file_size_bytes"):
        ScanLimits(max_file_size_bytes=0)


def test_negative_file_size_bytes_raises() -> None:
    with pytest.raises(ValueError, match="max_file_size_bytes"):
        ScanLimits(max_file_size_bytes=-1)


@pytest.mark.parametrize(
    "field_name",
    [
        "max_recursion_depth",
        "max_csv_rows",
        "max_field_length",
        "max_eml_attachments",
    ],
)
def test_negative_per_item_ceilings_raise(field_name: str) -> None:
    """Per-item ceilings accept zero (the opt-out sentinel) but not
    negatives — a negative count has no sensible reading."""
    with pytest.raises(ValueError, match=field_name):
        ScanLimits(**{field_name: -1})


@pytest.mark.parametrize(
    "field_name",
    [
        "max_recursion_depth",
        "max_csv_rows",
        "max_field_length",
        "max_eml_attachments",
    ],
)
def test_zero_per_item_ceilings_allowed(field_name: str) -> None:
    """Zero means "no limit" — explicit opt-out for trusted corpora.
    Construction must succeed so a caller can write
    ``ScanLimits(max_csv_rows=0)`` when they know the input is safe."""
    ScanLimits(**{field_name: 0})  # does not raise


# ---------------------------------------------------------------------------
# Context manager + thread-local state
# ---------------------------------------------------------------------------


def test_get_current_limits_defaults_outside_context() -> None:
    """Outside ``limits_context`` and with no prior
    ``set_current_limits`` call, ``get_current_limits`` returns
    ``DEFAULT_LIMITS``."""
    # Clear any leakage from prior tests.
    import domain.config as _cfg
    state = _cfg._limits_state
    if hasattr(state, "current"):
        delattr(state, "current")
    assert get_current_limits() is DEFAULT_LIMITS


def test_limits_context_installs_and_restores() -> None:
    """Inside the context, ``get_current_limits`` returns the
    installed ceilings. On exit the prior value is restored — even on
    exception propagation."""
    tight = ScanLimits(max_csv_rows=10)

    import domain.config as _cfg
    state = _cfg._limits_state
    if hasattr(state, "current"):
        delattr(state, "current")

    assert get_current_limits() is DEFAULT_LIMITS
    with limits_context(tight):
        assert get_current_limits() is tight
    assert get_current_limits() is DEFAULT_LIMITS


def test_limits_context_nested() -> None:
    """Nested contexts stack correctly — the inner context's limits
    apply inside it, the outer's resume on exit."""
    outer = ScanLimits(max_csv_rows=100)
    inner = ScanLimits(max_csv_rows=5)

    with limits_context(outer):
        assert get_current_limits() is outer
        with limits_context(inner):
            assert get_current_limits() is inner
        assert get_current_limits() is outer


def test_limits_context_restores_after_exception() -> None:
    prior = ScanLimits(max_csv_rows=100)
    with limits_context(prior):
        with pytest.raises(RuntimeError):
            with limits_context(ScanLimits(max_csv_rows=5)):
                raise RuntimeError("boom")
        # After the inner context raises, the outer context's limits
        # must still be intact.
        assert get_current_limits() is prior


def test_set_current_limits_persists() -> None:
    """``set_current_limits`` is the long-lived setter — useful for
    test-fixture setup. Unlike ``limits_context`` it does not
    auto-restore, so every test that uses it should reset afterwards
    (done here with a finally)."""
    custom = ScanLimits(max_eml_attachments=1)
    try:
        set_current_limits(custom)
        assert get_current_limits() is custom
    finally:
        # Reset state so other tests are not affected.
        import domain.config as _cfg
        state = _cfg._limits_state
        if hasattr(state, "current"):
            delattr(state, "current")


def test_limits_are_thread_local() -> None:
    """Concurrent ``ScanService.scan`` calls with different limits
    must not clobber each other. The thread-local backing store is
    the guarantee."""
    observed: dict[str, ScanLimits] = {}

    def worker(name: str, limits: ScanLimits) -> None:
        with limits_context(limits):
            observed[name] = get_current_limits()

    t_a = ScanLimits(max_csv_rows=11)
    t_b = ScanLimits(max_csv_rows=22)
    threads = [
        threading.Thread(target=worker, args=("a", t_a)),
        threading.Thread(target=worker, args=("b", t_b)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert observed["a"] is t_a
    assert observed["b"] is t_b

# Bismillah ir-Rahman ir-Rahim