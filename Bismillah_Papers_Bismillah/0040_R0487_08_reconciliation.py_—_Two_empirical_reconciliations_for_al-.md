# Bismillah ir-Rahman ir-Rahim

# R0487 -- 08_reconciliation.py — Two empirical reconciliations for al-Munāsabāt v1.0 revision:

**Chronological Index:** 40 of 995  
**Date:** 2024  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** 08_reconciliation.py  
**Source Format:** py  
**SHA-256:** `1639539fabc063743eb1488e019e4e70240b326611677ea55fc70cc6d6404e0e`  

---

## R0487 · 08_reconciliation.py — Two empirical reconciliations for al-Munāsabāt v1.0 revision:

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: 08_reconciliation.py
- source_format: py
- text_sha256: 1639539fabc063743eb1488e019e4e70240b326611677ea55fc70cc6d6404e0e

"""
Two empirical reconciliations for al-Munāsabāt v1.0 revision:

(1) Length-quartile shuffle test — addresses the compilation/length-sort
    confound from Cross-Text §6 Caveat 3. Preserve the approximate length-sort
    by shuffling within length quartiles; if autocorrelation persists, length-sort
    is not the dominant mechanism. If it collapses, length-sort accounts for most
    of the canonical signal and the §3 claim narrows substantially.

(2) Raw-cosine vs Fibonacci-additive autocorrelation reconciliation — addresses
    the +0.53 (Cross-Text) vs +0.80 (al-Munāsabāt) numerical discrepancy. The
    hypothesis is that Cross-Text computes autocorrelation on the consecutive-pair
    cosine similarity sequence while al-Munāsabāt computes it on the Fibonacci-
    additive similarity sequence; they are different statistical objects.
"""

import json, re, time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import qalsadi.lemmatizer as qlm

ARABIC_DIACRITICS = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
_lemmatizer = qlm.Lemmatizer()
_lemma_cache = {}

def normalize_arabic(text):
    text = ARABIC_DIACRITICS.sub('', text).replace('\u0640', '')
    text = re.sub('[إأآا]', 'ا', text).replace('ى', 'ي').replace('ة', 'ه')
    text = re.sub(r'[^\u0621-\u064A\s]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def lemmatize(text):
    out = []
    for w in text.split():
        if len(w) < 2: continue
        if w in _lemma_cache:
            out.append(_lemma_cache[w]); continue
        try:
            lem = _lemmatizer.lemmatize(w, return_pos=False)
            lem = ARABIC_DIACRITICS.sub('', lem) if lem else w
        except Exception:
            lem = w
        _lemma_cache[w] = lem
        out.append(lem)
    return ' '.join(out)

# --- Two different similarity sequences ---

def fib_sims(V):
    """Fibonacci-additive: cos(V[n], V[n-1]+V[n-2]) for n=2..N-1.
    This is what al-Munāsabāt and Cross-Text §3 build on."""
    n = V.shape[0]
    target = V[2:]
    add = V[1:n-1] + V[:n-2]
    dot = np.sum(target * add, axis=1)
    nt = np.linalg.norm(target, axis=1)
    na = np.linalg.norm(add, axis=1)
    denom = nt * na
    return np.where(denom > 1e-12, dot / np.where(denom > 1e-12, denom, 1.0), 0.0)

def consec_sims(V):
    """Raw consecutive cosine: cos(V[n], V[n-1]) for n=1..N-1.
    Hypothesis: Cross-Text's lag-20 = +0.53 is on this sequence."""
    n = V.shape[0]
    target = V[1:]
    prev = V[:n-1]
    dot = np.sum(target * prev, axis=1)
    nt = np.linalg.norm(target, axis=1)
    np_ = np.linalg.norm(prev, axis=1)
    denom = nt * np_
    return np.where(denom > 1e-12, dot / np.where(denom > 1e-12, denom, 1.0), 0.0)

def lag_autocorr(s, lag):
    if lag >= len(s): return np.nan
    a, b = s[:-lag], s[lag:]
    if a.std() < 1e-12 or b.std() < 1e-12: return np.nan
    return np.corrcoef(a, b)[0, 1]

# --- Load Quran ---
print("Loading Quran with Qalsadi...")
with open('quran-json/dist/quran.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
quran_docs = [lemmatize(normalize_arabic(' '.join(v['text'] for v in s['verses']))) for s in data]

# Length per surah (in lemmatized tokens)
lengths = np.array([len(d.split()) for d in quran_docs])
print(f"  Loaded {len(quran_docs)} surahs")
print(f"  Length range: {lengths.min()} to {lengths.max()} tokens")
print(f"  Surahs sorted by length descending - canonical match: ", end="")
sorted_by_len = np.argsort(-lengths)
canonical_idx = np.arange(114)
# Spearman-like correlation between canonical position and length-rank
length_rank = np.argsort(np.argsort(-lengths))
corr = np.corrcoef(canonical_idx, length_rank)[0, 1]
print(f"length-rank vs canonical-position correlation = {corr:+.3f}")

V = np.asarray(TfidfVectorizer(token_pattern=r'\S+').fit_transform(quran_docs).todense())

# ==========================================================
# RECONCILIATION TEST 1: Raw cosine vs Fibonacci-additive
# ==========================================================
print("\n" + "=" * 78)
print("TEST 1: Raw-cosine vs Fibonacci-additive autocorrelation reconciliation")
print("=" * 78)

fib_seq = fib_sims(V)
cos_seq = consec_sims(V)

print(f"\n{'Lag':>4} {'Fibonacci-additive':>20} {'Raw consecutive cosine':>26}")
print("-" * 56)
for lag in (5, 10, 15, 20, 30, 40, 50):
    fa = lag_autocorr(fib_seq, lag)
    rc = lag_autocorr(cos_seq, lag)
    print(f"{lag:>4} {fa:>+20.3f} {rc:>+26.3f}")

print(f"\nFibonacci-additive sequence: mean={fib_seq.mean():.3f}, std={fib_seq.std():.3f}, n={len(fib_seq)}")
print(f"Raw consecutive sequence:    mean={cos_seq.mean():.3f}, std={cos_seq.std():.3f}, n={len(cos_seq)}")

# ==========================================================
# RECONCILIATION TEST 2: Within-length-quartile shuffle
# ==========================================================
print("\n" + "=" * 78)
print("TEST 2: Within-length-quartile shuffle — addressing the length-sort confound")
print("=" * 78)

# Define quartiles based on length-rank in the canonical order
# Q1: positions 0-28 (longest surahs in canonical, which are the first ~25%)
# Q2: positions 29-56
# Q3: positions 57-85
# Q4: positions 86-113 (shortest surahs)
# Note: canonical is approximately length-sorted but not strictly; using canonical position for quartile assignment
# preserves the canonical's approximate length structure while shuffling within.

quartile_size = 114 // 4  # 28
quartile_bounds = [0, 28, 57, 85, 114]

print(f"\nQuartile structure (by canonical position, approximately by length):")
for i in range(4):
    start, end = quartile_bounds[i], quartile_bounds[i+1]
    qlens = lengths[start:end]
    print(f"  Q{i+1}: canonical positions {start}-{end-1} (n={end-start}), "
          f"length range {qlens.min()}–{qlens.max()} tokens")

print("\nBaselines (reference):")
canon_fib_lag20 = lag_autocorr(fib_seq, 20)
canon_cos_lag20 = lag_autocorr(cos_seq, 20)
print(f"  Canonical Quran      : Fibonacci-additive lag20 = {canon_fib_lag20:+.3f}, "
      f"Raw-cosine lag20 = {canon_cos_lag20:+.3f}")

# 200 within-quartile shuffles
rng = np.random.default_rng(2024)
fib_lag20_results = {l: [] for l in (5, 10, 20, 30)}
cos_lag20_results = {l: [] for l in (5, 10, 20, 30)}

n_shuffles = 200
for _ in range(n_shuffles):
    perm = np.arange(114)
    for i in range(4):
        start, end = quartile_bounds[i], quartile_bounds[i+1]
        sub = perm[start:end].copy()
        rng.shuffle(sub)
        perm[start:end] = sub
    fs = fib_sims(V[perm])
    cs = consec_sims(V[perm])
    for l in (5, 10, 20, 30):
        fib_lag20_results[l].append(lag_autocorr(fs, l))
        cos_lag20_results[l].append(lag_autocorr(cs, l))

# Also: full random shuffle for comparison
rng2 = np.random.default_rng(2025)
fib_random = {l: [] for l in (5, 10, 20, 30)}
cos_random = {l: [] for l in (5, 10, 20, 30)}
for _ in range(n_shuffles):
    perm = rng2.permutation(114)
    fs = fib_sims(V[perm])
    cs = consec_sims(V[perm])
    for l in (5, 10, 20, 30):
        fib_random[l].append(lag_autocorr(fs, l))
        cos_random[l].append(lag_autocorr(cs, l))

print(f"\n{'Lag':>4} | {'Canonical':>10} | {'Within-quartile':>17} | {'Full random':>13}")
print("     |   (Fib)    |   (Fib, mean±sd)  |   (Fib, mean±sd)")
print("-" * 60)
for l in (5, 10, 20, 30):
    canon = lag_autocorr(fib_seq, l)
    wq_arr = np.array(fib_lag20_results[l])
    fr_arr = np.array(fib_random[l])
    print(f"{l:>4} |  {canon:+8.3f}  |  {wq_arr.mean():+6.3f} ± {wq_arr.std():.3f}  |  {fr_arr.mean():+6.3f} ± {fr_arr.std():.3f}")

print(f"\n{'Lag':>4} | {'Canonical':>10} | {'Within-quartile':>17} | {'Full random':>13}")
print("     |   (Cos)    |   (Cos, mean±sd)  |   (Cos, mean±sd)")
print("-" * 60)
for l in (5, 10, 20, 30):
    canon = lag_autocorr(cos_seq, l)
    wq_arr = np.array(cos_lag20_results[l])
    fr_arr = np.array(cos_random[l])
    print(f"{l:>4} |  {canon:+8.3f}  |  {wq_arr.mean():+6.3f} ± {wq_arr.std():.3f}  |  {fr_arr.mean():+6.3f} ± {fr_arr.std():.3f}")

# Critical question: does within-quartile shuffle produce autocorrelation
# similar to canonical (length-sort dominant) or similar to full random (length-sort
# is not the dominant mechanism)?

print("\n" + "=" * 78)
print("INTERPRETATION")
print("=" * 78)

# Compute the gap closing ratio at lag 20 (Fibonacci)
canon_fib_20 = lag_autocorr(fib_seq, 20)
wq_fib_20_mean = np.mean(fib_lag20_results[20])
fr_fib_20_mean = np.mean(fib_random[20])
gap_canon_to_random = canon_fib_20 - fr_fib_20_mean
gap_canon_to_wq = canon_fib_20 - wq_fib_20_mean
ratio_wq = gap_canon_to_wq / gap_canon_to_random if gap_canon_to_random else float('nan')

print(f"\nFibonacci-additive at lag 20:")
print(f"  Canonical              : {canon_fib_20:+.3f}")
print(f"  Within-quartile shuffle: {wq_fib_20_mean:+.3f}")
print(f"  Full random shuffle    : {fr_fib_20_mean:+.3f}")
print(f"\nGap from canonical to full-random : {gap_canon_to_random:+.3f}")
print(f"Gap from canonical to wq-shuffle  : {gap_canon_to_wq:+.3f}")
print(f"Gap-closing ratio                 : {ratio_wq:.1%}")
print(f"\n  If wq-shuffle ≈ canonical: length-sort is the dominant mechanism.")
print(f"  If wq-shuffle ≈ full-random: length-sort is NOT the dominant mechanism.")
print(f"  Intermediate: length-sort is partly responsible.")

---

# Bismillah ir-Rahman ir-Rahim
