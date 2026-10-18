# Bismillah ir-Rahman ir-Rahim

# R0488 -- 10_bonferroni_pvalues.py — Compute exact empirical p-values for the within-quartile residual finding."""

**Chronological Index:** 41 of 995  
**Date:** 2024  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** 10_bonferroni_pvalues.py  
**Source Format:** py  
**SHA-256:** `40a4f64c6a397763c2de3682b6c1dd7649cdbd404d02d0eca5196616a43915c1`  

---

## R0488 · 10_bonferroni_pvalues.py — Compute exact empirical p-values for the within-quartile residual finding."""

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: 10_bonferroni_pvalues.py
- source_format: py
- text_sha256: 40a4f64c6a397763c2de3682b6c1dd7649cdbd404d02d0eca5196616a43915c1

"""Compute exact empirical p-values for the within-quartile residual finding."""
import json, re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import qalsadi.lemmatizer as qlm

ARABIC_DIACRITICS = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
_lemmatizer = qlm.Lemmatizer()
_lemma_cache = {}

def normalize_arabic(t):
    t = ARABIC_DIACRITICS.sub('', t).replace('\u0640', '')
    t = re.sub('[إأآا]', 'ا', t).replace('ى', 'ي').replace('ة', 'ه')
    t = re.sub(r'[^\u0621-\u064A\s]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def lemmatize(t):
    out = []
    for w in t.split():
        if len(w) < 2: continue
        if w in _lemma_cache: out.append(_lemma_cache[w]); continue
        try:
            lem = _lemmatizer.lemmatize(w, return_pos=False)
            lem = ARABIC_DIACRITICS.sub('', lem) if lem else w
        except Exception:
            lem = w
        _lemma_cache[w] = lem
        out.append(lem)
    return ' '.join(out)

def fib_sims(V):
    n = V.shape[0]
    target = V[2:]
    add = V[1:n-1] + V[:n-2]
    dot = np.sum(target * add, axis=1)
    nt = np.linalg.norm(target, axis=1)
    na = np.linalg.norm(add, axis=1)
    denom = nt * na
    return np.where(denom > 1e-12, dot / np.where(denom > 1e-12, denom, 1.0), 0.0)

def lag_autocorr(s, lag):
    if lag >= len(s): return np.nan
    a, b = s[:-lag], s[lag:]
    if a.std() < 1e-12 or b.std() < 1e-12: return np.nan
    return np.corrcoef(a, b)[0, 1]

print("Loading Quran with Qalsadi...")
with open('quran-json/dist/quran.json') as f:
    data = json.load(f)
docs = [lemmatize(normalize_arabic(' '.join(v['text'] for v in s['verses']))) for s in data]
V = np.asarray(TfidfVectorizer(token_pattern=r'\S+').fit_transform(docs).todense())

# Canonical
canon = fib_sims(V)
canon_acs = {l: lag_autocorr(canon, l) for l in (5, 10, 20, 30)}
print(f"\nCanonical autocorrelations:")
for l, v in canon_acs.items():
    print(f"  lag{l:>2} = {v:+.4f}")

# 200 within-quartile shuffles, count exact ≥ events
quartile_bounds = [0, 28, 57, 85, 114]
rng = np.random.default_rng(2024)
N_SHUFFLES = 200
counts_geq = {l: 0 for l in (5, 10, 20, 30)}
all_wq = {l: [] for l in (5, 10, 20, 30)}

for _ in range(N_SHUFFLES):
    perm = np.arange(114)
    for i in range(4):
        s, e = quartile_bounds[i], quartile_bounds[i+1]
        sub = perm[s:e].copy()
        rng.shuffle(sub)
        perm[s:e] = sub
    fs = fib_sims(V[perm])
    for l in (5, 10, 20, 30):
        ac = lag_autocorr(fs, l)
        all_wq[l].append(ac)
        if ac >= canon_acs[l]:
            counts_geq[l] += 1

print(f"\nEmpirical p-values from {N_SHUFFLES} within-quartile Monte Carlo shuffles:")
print(f"  (one-sided: P(within-quartile shuffle ≥ canonical))")
print(f"\n  {'Lag':>4} {'Canonical':>10} {'WQ max':>8} {'#≥canon':>8} {'emp_p':>10} {'Bonf α/4':>11}")
print("-" * 60)
for l in (5, 10, 20, 30):
    arr = np.array(all_wq[l])
    p_emp = counts_geq[l] / N_SHUFFLES if counts_geq[l] > 0 else 1/(N_SHUFFLES + 1)
    pass_str = "PASS" if p_emp < 0.0125 else "FAIL"
    p_label = f"<{1/(N_SHUFFLES+1):.4f}" if counts_geq[l] == 0 else f"{p_emp:.4f}"
    print(f"  {l:>4} {canon_acs[l]:>+10.3f} {arr.max():>+8.3f} {counts_geq[l]:>8d} {p_label:>10} {pass_str:>11}")

print(f"\n  Family-wise α = 0.05; Bonferroni-corrected per-lag α = 0.0125")
print(f"  At Bonferroni-corrected α = 0.0125, the residual finding survives at lags where")
print(f"  the canonical exceeded all 200 within-quartile shuffles (empirical p < 0.005),")
print(f"  but may not survive at lags where some shuffles equaled or exceeded the canonical.")

---

# Bismillah ir-Rahman ir-Rahim
