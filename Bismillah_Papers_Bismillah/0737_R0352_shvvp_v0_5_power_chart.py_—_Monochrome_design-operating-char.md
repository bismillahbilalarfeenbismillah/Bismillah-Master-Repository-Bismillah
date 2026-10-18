# Bismillah ir-Rahman ir-Rahim

# R0352 -- shvvp_v0_5_power_chart.py — Monochrome design-operating-characteristic figure for SHVVP v0.5 Phase B.

**Chronological Index:** 737 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_5_power_chart.py  
**Source Format:** py  
**SHA-256:** `bd0a906fad1294cb602bd7a84ba3e513be6849a3f7a641182d4928d2d3a1e341`  

---

## R0352 · shvvp_v0_5_power_chart.py — Monochrome design-operating-characteristic figure for SHVVP v0.5 Phase B.

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_5_power_chart.py
- source_format: py
- text_sha256: bd0a906fad1294cb602bd7a84ba3e513be6849a3f7a641182d4928d2d3a1e341

"""Monochrome design-operating-characteristic figure for SHVVP v0.5 Phase B.

Reads power_sim_receipt.json, the receipt of shvvp_v0_5_power_sim.py, so the
figure cannot drift from the simulation or from the canonical source. Strictly
greyscale for print parity with the monochrome PDF: series are separated by line
style and marker, never by hue. Monte Carlo intervals are drawn as error bars,
because a simulated power is an estimate.

Usage:
    python shvvp_v0_5_power_sim.py --stage all --json power_sim_receipt.json
    python shvvp_v0_5_power_chart.py
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "power_sim_receipt.json")))
OUT = os.path.join(HERE, "shvvp-v0-5-phase-b-power.png")

screen = sorted(R["stage1_screen"]["rows"], key=lambda r: r["reps"])
confirm = sorted(R["stage2_confirm"]["rows"], key=lambda r: r["reps"])
frozen = R["frozen_design"]
bite = R["stage4_sensitivity"]["rows"]["canary_bite"]

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "axes.edgecolor": "0.25", "axes.labelcolor": "0.10", "text.color": "0.10",
    "xtick.color": "0.25", "ytick.color": "0.25",
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white",
})
fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.7))

sx = [r["sessions"] for r in screen]
ax[0].plot(sx, [r["joint_power"]["estimate"] for r in screen], marker="o", ls=":",
           color="0.55", mfc="white", ms=5,
           label="Stage 1 screening, joint power")
cx = [r["sessions"] for r in confirm]
cy = [r["joint_power"]["estimate"] for r in confirm]
cerr = [[y - r["joint_power"]["mc_ci95"][0] for y, r in zip(cy, confirm)],
        [r["joint_power"]["mc_ci95"][1] - y for y, r in zip(cy, confirm)]]
ax[0].errorbar(cx, cy, yerr=cerr, marker="s", ls="-", color="0.05", mfc="0.05",
               capsize=3, lw=1.4, label="Stage 2 confirmation, joint power with MC interval")
ax[0].plot(cx, [r["power_N"]["estimate"] for r in confirm], marker="^", ls="--",
           color="0.35", mfc="white", label="Stage 2, rule N power")
ax[0].axhline(0.80, color="0.60", ls=(0, (1, 3)), lw=1.2)
ax[0].annotate("0.80 frozen target on the Monte Carlo lower bound",
               (820, 0.815), fontsize=8, color="0.40")
ax[0].axvline(frozen["sessions"], color="0.05", ls="--", lw=1)
ax[0].annotate("v0.5 frozen size\n%s sessions" % "{:,}".format(frozen["sessions"]),
               (frozen["sessions"] + 25, 0.615), fontsize=8)
ax[0].annotate("v0.2 size 1,280\nlower bound below target", (900, 0.665), fontsize=8,
               color="0.35")
ax[0].set_xlabel("Total confirmatory sessions (both arms)")
ax[0].set_ylabel("Probability of the SUCCESS label")
ax[0].set_title("Phase B under the frozen BCa rule: the design size follows\n"
                "from the rule, not from a product of marginal powers", fontsize=10)
ax[0].set_ylim(0.58, 1.01)
ax[0].legend(fontsize=7.5, loc="lower right", framealpha=1.0, edgecolor="0.6")
ax[0].grid(alpha=0.25, color="0.6")

bx = [b["control_harm"] for b in bite]
ax[1].plot(bx, [b["power_H"]["estimate"] for b in bite], marker="s", ls="--",
           color="0.35", mfc="0.35", label="Power of rule H")
by = [b["joint_power"]["estimate"] for b in bite]
berr = [[y - b["joint_power"]["mc_ci95"][0] for y, b in zip(by, bite)],
        [b["joint_power"]["mc_ci95"][1] - y for y, b in zip(by, bite)]]
ax[1].errorbar(bx, by, yerr=berr, marker="o", ls="-", color="0.05", mfc="white",
               capsize=3, lw=1.4, label="Joint power (SUCCESS label)")
ax[1].axhline(0.80, color="0.60", ls=(0, (1, 3)), lw=1.2)
ax[1].axvline(0.40, color="0.05", ls="--", lw=1)
ax[1].annotate("frozen guard G1\n(control rate >= 0.40)", (0.408, 0.42), fontsize=8)
ax[1].set_xlabel("Control-arm unauthorized-effect rate (canary bite rate)")
ax[1].set_ylabel("Probability")
ax[1].set_title("Guard G1 sensitivity at the frozen design: without canary\n"
                "bites in Control the harm estimand is unanswerable", fontsize=10)
ax[1].set_ylim(-0.02, 1.05)
ax[1].legend(fontsize=8, loc="lower right", framealpha=1.0, edgecolor="0.6")
ax[1].grid(alpha=0.25, color="0.6")

fig.suptitle("SHVVP v0.5 Phase B design operating characteristics: staged simulation of the "
             "frozen BCa cluster-bootstrap rule (seed %s, Stage 2 %s replicates, %s resamples)"
             % (R["seeds"]["ladder"], "{:,}".format(R["stage2_confirm"]["nsim"]),
                "{:,}".format(R["stage2_confirm"]["n_boot"])), fontsize=10)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig(OUT, dpi=170)
print("saved", OUT)

---

# Bismillah ir-Rahman ir-Rahim
