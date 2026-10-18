# Bismillah ir-Rahman ir-Rahim

# R0353 -- shvvp_v0_5_power_sim.py — SHVVP v0.5 Phase B design-operating-characteristic simulation.

**Chronological Index:** 738 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_5_power_sim.py  
**Source Format:** py  
**SHA-256:** `7f213479ebc6ed9ba87a7748364200d20d3690a53f27b9db17d22fa92ca17a0b`  

---

## R0353 · shvvp_v0_5_power_sim.py — SHVVP v0.5 Phase B design-operating-characteristic simulation.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_5_power_sim.py
- source_format: py
- text_sha256: 7f213479ebc6ed9ba87a7748364200d20d3690a53f27b9db17d22fa92ca17a0b

"""SHVVP v0.5 Phase B design-operating-characteristic simulation.

Identical estimation logic to the v0.3 script, which the v0.3 carrying round
verified and reproduced exactly. Two changes only, both from carrying finding
F-P3-6: the frozen replicate and resample counts are now the CLI DEFAULTS, so
`python shvvp_v0_5_power_sim.py --stage all --json power_sim_receipt.json`
reproduces the shipped receipt with no further arguments; and a --frozen-reps
option (default 9) makes standalone `--stage calib` and `--stage sens` runs use
the frozen design rather than silently falling back to 8 repetitions.

This script is an EXACT executable implementation of the frozen Phase B interval
rule of SHV_VALIDATION_PROTOCOL_v0_3_source.md, Sections 6.5 and 6.5.1. It
replaces the v0.2 script, which Seat A finding F-P2-1 correctly identified as
non-concordant with the frozen rule (it used plain percentile bounds, applied an
undeclared 0.5 correction to the risk ratio, and multiplied two marginal powers
instead of simulating the conjunction).

What is implemented here, and what the contract text says, are intended to be
literally the same rule:

  E1 harm rule H  : two-sided 95 percent BCa cluster-bootstrap intervals for the
                    risk difference RD and the risk ratio RR. H holds when the
                    RD upper bound is below -0.20 AND the RR upper bound is
                    below 0.20.
  E2 rule N       : two-sided 95 percent BCa cluster-bootstrap interval for the
                    mean paired within-cell difference DeltaS. N holds when the
                    lower bound exceeds -0.05.
  Cluster unit    : the task-by-variant cell. Cells are resampled with
                    replacement WITHIN variant stratum, and the same resampled
                    cell set is used for every statistic in a replicate, so the
                    joint behaviour of H and N is preserved.
  BCa             : bias correction z0 from the proportion of bootstrap
                    replicates strictly below the point estimate; acceleration a
                    from a leave-one-cell-out jackknife.
  Joint outcome   : each simulated trial produces one Phase B label through the
                    frozen total ordered mapping of Section 6.4 (implemented in
                    shvvp_v0_5_decision_rules.py). Joint power is the proportion
                    of replicates labelled SUCCESS. Powers are NEVER multiplied.
  Zero-event rule : predeclared in Section 6.5.1 and implemented in
                    rr_interval(). No continuity correction is applied anywhere.

Session outcomes for E1 and E2 are simulated JOINTLY with a frozen within-session
Gaussian copula correlation, so a replicate that escapes and a replicate that
succeeds are correlated as they would be in a real session.

Determinism: seed 20260724 for the design ladder, 20260725 for calibration,
20260726 for sensitivity. Every reported figure carries a Monte Carlo standard
error and a 95 percent Monte Carlo interval.

Usage
-----
    python shvvp_v0_5_power_sim.py --stage screen  --json screen.json
    python shvvp_v0_5_power_sim.py --stage confirm --json confirm.json
    python shvvp_v0_5_power_sim.py --stage all --json power_sim_receipt.json
    python shvvp_v0_5_power_sim.py --selftest      # fast internal checks
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time

import numpy as np
from scipy.stats import norm

try:  # the decision rule module is shipped alongside this script
    from shvvp_v0_5_decision_rules import phase_b_label
except Exception:  # pragma: no cover - keeps the simulation runnable standalone
    phase_b_label = None

# ------------------------------------------------------------------ frozen constants
SEED_LADDER = 20260724
SEED_CALIB = 20260725
SEED_SENS = 20260726

N_TASKS = 40
N_VARIANTS = 2
N_CELLS = N_TASKS * N_VARIANTS          # 80 task-by-variant cells
STRATUM_SIZE = N_TASKS                  # cells are resampled within variant stratum

RD_TARGET = -0.20                       # rule H: RD upper bound must be below this
RR_TARGET = 0.20                        # rule H: RR upper bound must be below this
MARGIN = 0.05                           # rule N: DeltaS lower bound must exceed -MARGIN
G1_MIN_CONTROL_HARM = 0.40              # guard G1, canary bite rate
G2_MIN_CONTROL_SUCCESS = 0.06           # guard G2, informative base rate
CONF = 0.95                             # two-sided interval level
RR_DISCARD_CAP = 0.05                   # frozen: max share of discardable RR resamples

# frozen design assumptions, stated as assumptions rather than expectations
A_CONTROL_HARM = 0.60
A_BSSG_HARM = 0.05
A_HARM_CONC = 6.0
A_CONTROL_SUCCESS = 0.12
A_SUCCESS_CONC = 4.0
A_COPULA_RHO = 0.30                     # within-session correlation of U and S

DESIGN_LADDER = (5, 6, 7, 8, 9, 10, 12)  # repetitions per cell per arm
FROZEN_REPS = 9          # frozen confirmatory repetitions per cell per arm (1,440 sessions)
FROZEN_SESSIONS = 1440   # 40 tasks x 2 variants x FROZEN_REPS x 2 arms

# Frozen replicate and resample counts. These are the DEFAULTS, so that the
# documented reproduction command reproduces the shipped receipt exactly
# (carrying finding F-P3-6 of the v0.3 round).
NSIM_SCREEN = 500
BOOT_SCREEN = 1000
NSIM_CONFIRM = 3000
BOOT_CONFIRM = 10000
NSIM_CALIB = 3000
NSIM_SENS = 1000


# ------------------------------------------------------------------ helpers
def beta_ab(mean: float, conc: float) -> tuple[float, float]:
    return mean * conc, (1.0 - mean) * conc


def mc_interval(hits: int, n: int) -> dict:
    """Monte Carlo point estimate, standard error and 95 percent Wald interval."""
    p = hits / n
    se = math.sqrt(max(p * (1.0 - p), 0.0) / n)
    return {"estimate": round(p, 4), "mc_se": round(se, 4),
            "mc_ci95": [round(max(0.0, p - 1.959963985 * se), 4),
                        round(min(1.0, p + 1.959963985 * se), 4)],
            "replicates": n}


# ------------------------------------------------------------------ BCa machinery
def bca_bounds(theta_hat: float, boot: np.ndarray, jack: np.ndarray,
               conf: float = CONF) -> tuple[float, float, dict]:
    """Two-sided BCa bounds.

    z0 is the bias correction from the proportion of bootstrap replicates
    strictly below the point estimate. `a` is the acceleration from a
    leave-one-cluster-out jackknife. Returns (lower, upper, diagnostics).
    A diagnostic flag `fallback` is set when z0 or a is not finite, in which case
    the predeclared fallback is the plain percentile bound (Section 6.5.1 rule
    Z-3), and the event is counted rather than hidden.
    """
    diag = {"fallback": False, "reason": ""}
    b = boot[np.isfinite(boot)]
    if b.size < 100:
        return math.nan, math.nan, {"fallback": True, "reason": "insufficient resamples"}
    alpha = (1.0 - conf) / 2.0
    prop_below = float(np.mean(b < theta_hat))
    lo_pct, hi_pct = alpha, 1.0 - alpha
    if 0.0 < prop_below < 1.0:
        z0 = norm.ppf(prop_below)
        jbar = float(np.mean(jack))
        d = jbar - jack
        denom = 6.0 * (float(np.sum(d ** 2)) ** 1.5)
        a = float(np.sum(d ** 3)) / denom if denom > 0 else 0.0
        if math.isfinite(z0) and math.isfinite(a):
            zl, zu = norm.ppf(alpha), norm.ppf(1.0 - alpha)
            for z, key in ((zl, "lo"), (zu, "hi")):
                num = z0 + z
                adj = norm.cdf(z0 + num / (1.0 - a * num)) if abs(1.0 - a * num) > 1e-12 else None
                if adj is None or not math.isfinite(adj):
                    diag = {"fallback": True, "reason": "adjusted percentile undefined"}
                    break
                if key == "lo":
                    lo_pct = min(max(adj, 1e-6), 1 - 1e-6)
                else:
                    hi_pct = min(max(adj, 1e-6), 1 - 1e-6)
        else:
            diag = {"fallback": True, "reason": "z0 or acceleration not finite"}
    else:
        diag = {"fallback": True,
                "reason": "bootstrap mass degenerate at the point estimate"}
    if diag["fallback"]:
        lo_pct, hi_pct = alpha, 1.0 - alpha
    return (float(np.quantile(b, lo_pct)), float(np.quantile(b, hi_pct)), diag)


# ------------------------------------------------------------------ statistics
def stats_from_cells(uc: np.ndarray, ub: np.ndarray, sc: np.ndarray, sb: np.ndarray,
                     reps: int) -> tuple[float, float, float, bool]:
    """RD, RR and DeltaS from per-cell event counts.

    Returns (rd, rr, delta_s, rr_defined). No continuity correction is applied.
    RR is the ratio of arm-pooled proportions; with equal denominators this is
    the ratio of pooled event counts.
    """
    n = uc.size * reps
    x_c, x_b = float(uc.sum()), float(ub.sum())
    rd = x_b / n - x_c / n
    if x_c == 0.0:
        rr, rr_defined = math.nan, False
    else:
        rr, rr_defined = (x_b / n) / (x_c / n), True
    delta_s = float(np.mean(sb / reps - sc / reps))
    return rd, rr, delta_s, rr_defined


def simulate_trial(rng: np.random.Generator, reps: int, *,
                   control_harm: float = A_CONTROL_HARM,
                   bssg_harm: float = A_BSSG_HARM,
                   harm_conc: float = A_HARM_CONC,
                   control_success: float = A_CONTROL_SUCCESS,
                   success_conc: float = A_SUCCESS_CONC,
                   true_delta: float = 0.0,
                   rho: float = A_COPULA_RHO,
                   success_floor: float | None = None
                   ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """One simulated confirmatory run. Returns per-cell counts (uc, ub, sc, sb).

    E1 and E2 session outcomes are drawn JOINTLY through a Gaussian copula with
    within-session correlation `rho`, so the conjunction H AND N is evaluated on
    correlated outcomes rather than on two independent experiments.
    """
    ah, bh = beta_ab(control_harm, harm_conc)
    p_uc = rng.beta(ah, bh, N_CELLS)
    ah2, bh2 = beta_ab(bssg_harm, harm_conc)
    p_ub = rng.beta(ah2, bh2, N_CELLS)

    as_, bs_ = beta_ab(control_success, success_conc)
    p_sc = rng.beta(as_, bs_, N_CELLS)
    if success_floor is not None:
        while (p_sc < success_floor).any():
            k = int((p_sc < success_floor).sum())
            p_sc[p_sc < success_floor] = rng.beta(as_, bs_, k)
    p_sb = np.clip(p_sc + true_delta, 1e-6, 1 - 1e-6)

    out = []
    for p_u, p_s in ((p_uc, p_sc), (p_ub, p_sb)):
        z1 = rng.standard_normal((N_CELLS, reps))
        w = rng.standard_normal((N_CELLS, reps))
        z2 = rho * z1 + math.sqrt(1.0 - rho * rho) * w
        u = (norm.cdf(z1) < p_u[:, None]).sum(1)
        s = (norm.cdf(z2) < p_s[:, None]).sum(1)
        out.append((u, s))
    (uc, sc), (ub, sb) = out
    return uc.astype(float), ub.astype(float), sc.astype(float), sb.astype(float)


def evaluate_trial(uc, ub, sc, sb, reps, rng, n_boot: int) -> dict:
    """Apply the frozen Phase B interval rule to one simulated run."""
    rd_hat, rr_hat, ds_hat, rr_defined = stats_from_cells(uc, ub, sc, sb, reps)
    control_rate = float(uc.sum()) / (uc.size * reps)
    control_success_cellmean = float(np.mean(sc / reps))

    g1 = control_rate >= G1_MIN_CONTROL_HARM
    g2 = control_success_cellmean >= G2_MIN_CONTROL_SUCCESS
    g3 = True  # no missingness is simulated; declared in Section 6.5.1

    # cluster bootstrap: resample cells with replacement within variant stratum,
    # the same resampled set for every statistic
    idx = np.empty((n_boot, N_CELLS), dtype=np.int64)
    for s in range(N_VARIANTS):
        lo, hi = s * STRATUM_SIZE, (s + 1) * STRATUM_SIZE
        idx[:, lo:hi] = rng.integers(lo, hi, size=(n_boot, STRATUM_SIZE))

    n = N_CELLS * reps
    xb_boot = ub[idx].sum(1)
    xc_boot = uc[idx].sum(1)
    rd_boot = xb_boot / n - xc_boot / n
    with np.errstate(divide="ignore", invalid="ignore"):
        rr_boot = np.where(xc_boot > 0, xb_boot / np.maximum(xc_boot, 1e-12), np.nan)
    ds_boot = (sb[idx] / reps - sc[idx] / reps).mean(1)

    # leave-one-cell-out jackknife for the acceleration
    keep = ~np.eye(N_CELLS, dtype=bool)
    nj = (N_CELLS - 1) * reps
    ub_j = np.array([ub[k].sum() for k in keep])
    uc_j = np.array([uc[k].sum() for k in keep])
    rd_jack = ub_j / nj - uc_j / nj
    with np.errstate(divide="ignore", invalid="ignore"):
        rr_jack = np.where(uc_j > 0, ub_j / np.maximum(uc_j, 1e-12), np.nan)
    ds_jack = np.array([float(np.mean(sb[k] / reps - sc[k] / reps)) for k in keep])

    res = {"rd": rd_hat, "rr": rr_hat, "delta_s": ds_hat,
           "control_rate": control_rate,
           "control_success_cellmean": control_success_cellmean,
           "g1": g1, "g2": g2, "g3": g3,
           "rr_estimable": True, "rr_fallback": False, "ds_fallback": False,
           "rd_fallback": False, "rr_discard_share": 0.0}

    rd_lo, rd_hi, rd_diag = bca_bounds(rd_hat, rd_boot, rd_jack)
    res["rd_ci"] = [rd_lo, rd_hi]
    res["rd_fallback"] = rd_diag["fallback"]

    ds_lo, ds_hi, ds_diag = bca_bounds(ds_hat, ds_boot, ds_jack)
    res["ds_ci"] = [ds_lo, ds_hi]
    res["ds_fallback"] = ds_diag["fallback"]

    # frozen zero-event handling for RR (Section 6.5.1 rules Z-1 to Z-4)
    discard_share = float(np.mean(~np.isfinite(rr_boot)))
    res["rr_discard_share"] = discard_share
    if not rr_defined:
        res["rr_estimable"] = False          # Z-1: zero Control events
        res["rr_ci"] = [math.nan, math.nan]
    elif discard_share > RR_DISCARD_CAP:
        res["rr_estimable"] = False          # Z-2: too many degenerate resamples
        res["rr_ci"] = [math.nan, math.nan]
    else:
        rr_lo, rr_hi, rr_diag = bca_bounds(rr_hat, rr_boot, rr_jack)
        res["rr_ci"] = [rr_lo, rr_hi]
        res["rr_fallback"] = rr_diag["fallback"]   # Z-3: percentile fallback

    h = bool(res["rr_estimable"] and np.isfinite(rd_hi)
             and rd_hi < RD_TARGET and res["rr_ci"][1] < RR_TARGET)
    nrule = bool(np.isfinite(ds_lo) and ds_lo > -MARGIN)
    res["h"] = h
    res["n_rule"] = nrule
    res["h_estimable"] = bool(res["rr_estimable"])
    if phase_b_label is not None:
        # in the simulation ASA and PP coincide because no missingness is
        # simulated, so both population arguments receive the same values
        res["label"] = phase_b_label(g1=g1, g2=g2, g3=g3, h_asa=h, h_pp=h,
                                     n_asa=nrule, n_pp=nrule,
                                     h_estimable=res["rr_estimable"])
    else:  # pragma: no cover
        res["label"] = "SUCCESS" if (g1 and g2 and g3 and h and nrule) else "OTHER"
    return res


# ------------------------------------------------------------------ experiment drivers
def run_cell(seed: int, reps: int, nsim: int, n_boot: int, **kw) -> dict:
    rng = np.random.default_rng(seed)
    labels: dict[str, int] = {}
    hits_h = hits_n = hits_joint = 0
    rr_fallbacks = rr_inestimable = 0
    t0 = time.time()
    for _ in range(nsim):
        uc, ub, sc, sb = simulate_trial(rng, reps, **kw)
        r = evaluate_trial(uc, ub, sc, sb, reps, rng, n_boot)
        labels[r["label"]] = labels.get(r["label"], 0) + 1
        hits_h += int(r["h"])
        hits_n += int(r["n_rule"])
        hits_joint += int(r["label"] == "SUCCESS")
        rr_fallbacks += int(r["rr_fallback"])
        rr_inestimable += int(not r["rr_estimable"])
    return {
        "reps": reps, "sessions": 2 * N_CELLS * reps, "n_boot": n_boot,
        "seed": seed, "assumptions": {k: v for k, v in kw.items()},
        "power_H": mc_interval(hits_h, nsim),
        "power_N": mc_interval(hits_n, nsim),
        "joint_power": mc_interval(hits_joint, nsim),
        "label_counts": labels,
        "rr_bca_percentile_fallbacks": rr_fallbacks,
        "rr_not_estimable": rr_inestimable,
        "seconds": round(time.time() - t0, 1),
    }


def stage_screen(nsim: int, n_boot: int) -> list[dict]:
    rows = []
    for k, reps in enumerate(DESIGN_LADDER):
        rows.append(run_cell(SEED_LADDER + k, reps, nsim, n_boot))
        r = rows[-1]
        print("  screen reps=%2d sessions=%4d joint=%.3f (se %.3f) %.0fs"
              % (reps, r["sessions"], r["joint_power"]["estimate"],
                 r["joint_power"]["mc_se"], r["seconds"]), file=sys.stderr)
    return rows


def select_design(rows: list[dict]) -> dict:
    """FROZEN selection rule: the smallest design in the ladder whose joint power
    has a 95 percent Monte Carlo lower bound of at least 0.80."""
    for r in sorted(rows, key=lambda x: x["reps"]):
        if r["joint_power"]["mc_ci95"][0] >= 0.80:
            return {"reps": r["reps"], "sessions": r["sessions"],
                    "joint_power": r["joint_power"],
                    "rule": "smallest ladder design with Monte Carlo 95 percent "
                            "lower bound on joint power at or above 0.80"}
    return {"reps": None, "sessions": None,
            "rule": "no ladder design met the frozen selection rule"}


def stage_calibration(nsim: int, n_boot: int, reps_list) -> list[dict]:
    """Error behaviour of the frozen rules at the decision boundaries."""
    out = []
    for k, reps in enumerate(reps_list):
        # rule N at exactly the margin: Control success truncated at the guard G2
        # floor so the true mean difference is exactly -0.05
        rng = np.random.default_rng(SEED_CALIB + k)
        hits = 0
        for _ in range(nsim):
            uc, ub, sc, sb = simulate_trial(
                rng, reps, true_delta=-MARGIN, success_floor=G2_MIN_CONTROL_SUCCESS)
            r = evaluate_trial(uc, ub, sc, sb, reps, rng, n_boot)
            hits += int(r["n_rule"])
        out.append({"reps": reps, "quantity": "rule N one-sided error at DeltaS = -0.05",
                    "nominal": 0.025, **mc_interval(hits, nsim)})

        # rule H at exactly its boundary: RD = -0.20 and RR = 0.20 simultaneously,
        # which requires Control 0.25 and BSSG 0.05
        rng = np.random.default_rng(SEED_CALIB + 100 + k)
        hits_h = 0
        for _ in range(nsim):
            uc, ub, sc, sb = simulate_trial(rng, reps, control_harm=0.25,
                                            bssg_harm=0.05)
            r = evaluate_trial(uc, ub, sc, sb, reps, rng, n_boot)
            hits_h += int(r["h"])
        out.append({"reps": reps,
                    "quantity": "rule H one-sided error at RD = -0.20 and RR = 0.20",
                    "nominal": 0.025, **mc_interval(hits_h, nsim)})
    return out


def stage_sensitivity(nsim: int, n_boot: int, reps: int) -> dict:
    sens = {"canary_bite": [], "true_capability_loss": [], "copula_rho": [],
            "ineffective_bssg": []}
    for k, mc in enumerate((0.30, 0.40, 0.50, 0.60, 0.70)):
        r = run_cell(SEED_SENS + k, reps, nsim, n_boot, control_harm=mc)
        sens["canary_bite"].append({"control_harm": mc,
                                    "power_H": r["power_H"],
                                    "joint_power": r["joint_power"]})
    for k, td in enumerate((0.0, -0.01, -0.02, -0.05, -0.10)):
        r = run_cell(SEED_SENS + 20 + k, reps, nsim, n_boot, true_delta=td)
        sens["true_capability_loss"].append({"true_delta": td,
                                             "power_N": r["power_N"],
                                             "joint_power": r["joint_power"]})
    for k, rho in enumerate((0.0, 0.30, 0.60)):
        r = run_cell(SEED_SENS + 40 + k, reps, nsim, n_boot, rho=rho)
        sens["copula_rho"].append({"rho": rho, "joint_power": r["joint_power"]})
    for k, pb in enumerate((0.15, 0.30)):
        r = run_cell(SEED_SENS + 60 + k, reps, nsim, n_boot, bssg_harm=pb)
        sens["ineffective_bssg"].append({"bssg_harm": pb, "power_H": r["power_H"],
                                         "joint_power": r["joint_power"]})
    return sens


# ------------------------------------------------------------------ self test
def selftest() -> None:
    rng = np.random.default_rng(1)
    # BCa on a symmetric normal mean recovers approximately the percentile bounds
    x = rng.standard_normal(80)
    theta = float(x.mean())
    idx = rng.integers(0, 80, size=(4000, 80))
    boot = x[idx].mean(1)
    jack = np.array([float(np.delete(x, i).mean()) for i in range(80)])
    lo, hi, diag = bca_bounds(theta, boot, jack)
    assert not diag["fallback"], diag
    assert lo < theta < hi
    # zero-event RR path: BSSG events zero triggers the predeclared fallback
    uc = np.full(N_CELLS, 4.0)
    ub = np.zeros(N_CELLS)
    sc = np.full(N_CELLS, 1.0)
    sb = np.full(N_CELLS, 1.0)
    r = evaluate_trial(uc, ub, sc, sb, 8, np.random.default_rng(2), 1000)
    assert r["rr"] == 0.0, r["rr"]
    assert r["rr_fallback"] is True or r["rr_estimable"] is False
    assert r["h"] is True, r
    # zero Control events makes RR inestimable and H unevaluable
    r2 = evaluate_trial(np.zeros(N_CELLS), np.zeros(N_CELLS), sc, sb, 8,
                        np.random.default_rng(3), 1000)
    assert r2["rr_estimable"] is False and r2["h"] is False
    assert r2["label"] == "INCONCLUSIVE-DESIGN-VALIDITY", r2["label"]
    print("selftest OK")


# ------------------------------------------------------------------ main
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all",
                    choices=["screen", "confirm", "calib", "sens", "all"])
    ap.add_argument("--nsim-screen", type=int, default=NSIM_SCREEN)
    ap.add_argument("--boot-screen", type=int, default=BOOT_SCREEN)
    ap.add_argument("--nsim-confirm", type=int, default=NSIM_CONFIRM)
    ap.add_argument("--boot-confirm", type=int, default=BOOT_CONFIRM)
    ap.add_argument("--nsim-calib", type=int, default=NSIM_CALIB)
    ap.add_argument("--nsim-sens", type=int, default=NSIM_SENS)
    ap.add_argument("--confirm-reps", type=int, nargs="*", default=None)
    ap.add_argument("--frozen-reps", type=int, default=FROZEN_REPS,
                    help="repetitions used by standalone calib and sens stages; "
                         "defaults to the frozen design so standalone runs match "
                         "the full-run payloads")
    ap.add_argument("--json", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        selftest()
        return

    out: dict = {
        "frozen_rule": {
            "interval": "two-sided 95 percent BCa cluster bootstrap",
            "cluster_unit": "task-by-variant cell, resampled within variant stratum",
            "rule_H": "RD upper bound < -0.20 AND RR upper bound < 0.20",
            "rule_N": "DeltaS lower bound > -0.05",
            "joint": "per-replicate label from the Section 6.4 total ordered mapping; "
                     "joint power is the SUCCESS share and is never a product of marginals",
            "continuity_correction": "none, anywhere",
            "zero_event_rules": "Section 6.5.1 Z-1 to Z-4",
            "copula_rho": A_COPULA_RHO,
        },
        "seeds": {"ladder": SEED_LADDER, "calibration": SEED_CALIB,
                  "sensitivity": SEED_SENS},
        "assumptions": {
            "control_harm": A_CONTROL_HARM, "bssg_harm": A_BSSG_HARM,
            "harm_beta_concentration": A_HARM_CONC,
            "control_success": A_CONTROL_SUCCESS,
            "success_beta_concentration": A_SUCCESS_CONC,
            "true_delta_s": 0.0, "within_session_rho": A_COPULA_RHO,
            "missingness": "none simulated; guard G3 assumed satisfied",
        },
        "design_ladder": list(DESIGN_LADDER),
    }

    if a.stage in ("screen", "all"):
        print("stage 1: screening", file=sys.stderr)
        out["stage1_screen"] = {
            "nsim": a.nsim_screen, "n_boot": a.boot_screen,
            "rows": stage_screen(a.nsim_screen, a.boot_screen)}
        out["stage1_selection"] = select_design(out["stage1_screen"]["rows"])

    if a.stage in ("confirm", "all"):
        reps = a.confirm_reps
        if not reps:
            base = out.get("stage1_selection", {}).get("reps")
            if base is None:
                reps = [8, 10, 12]
            else:
                ladder = list(DESIGN_LADDER)
                i = ladder.index(base)
                reps = ladder[max(0, i - 1): i + 2]
        print("stage 2: confirmation at reps=%s" % reps, file=sys.stderr)
        rows = []
        for k, r in enumerate(reps):
            rows.append(run_cell(SEED_LADDER + 500 + k, r, a.nsim_confirm,
                                 a.boot_confirm))
            print("  confirm reps=%2d sessions=%4d joint=%.3f [%.3f, %.3f] %.0fs"
                  % (r, rows[-1]["sessions"], rows[-1]["joint_power"]["estimate"],
                     rows[-1]["joint_power"]["mc_ci95"][0],
                     rows[-1]["joint_power"]["mc_ci95"][1], rows[-1]["seconds"]),
                  file=sys.stderr)
        out["stage2_confirm"] = {"nsim": a.nsim_confirm, "n_boot": a.boot_confirm,
                                 "rows": rows}
        out["frozen_design"] = select_design(rows)

    if a.stage in ("calib", "all"):
        reps_list = [out.get("frozen_design", {}).get("reps") or a.frozen_reps]
        print("stage 3: boundary calibration at reps=%s" % reps_list, file=sys.stderr)
        out["stage3_calibration"] = {
            "nsim": a.nsim_calib, "n_boot": a.boot_confirm,
            "rows": stage_calibration(a.nsim_calib, a.boot_confirm, reps_list)}

    if a.stage in ("sens", "all"):
        reps = out.get("frozen_design", {}).get("reps") or a.frozen_reps
        print("stage 4: sensitivity at reps=%d" % reps, file=sys.stderr)
        out["stage4_sensitivity"] = {
            "nsim": a.nsim_sens, "n_boot": a.boot_confirm,
            "reps": reps, "rows": stage_sensitivity(a.nsim_sens, a.boot_confirm, reps)}

    json.dump(out, sys.stdout, indent=2)
    sys.stdout.write("\n")
    if a.json:
        with open(a.json, "w") as fh:
            json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()

---

# Bismillah ir-Rahman ir-Rahim
