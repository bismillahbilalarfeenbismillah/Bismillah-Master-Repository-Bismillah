# Bismillah ir-Rahman ir-Rahim

# R0519 -- inject_sim_values_v0_5.py — Substitute the simulation receipt into the canonical v0.5 source.

**Chronological Index:** 797 of 995  
**Date:** Undated  
**Section:** VII. Software: Bayyinah Scanner, furqan-lint & Verifiers  
**Source File:** inject_sim_values_v0_5.py  
**Source Format:** py  
**SHA-256:** `7e2c9d9fc0676dd2b5fde5b6cd21554964133e55c17db4744254a98a138db563`  

---

## R0519 · inject_sim_values_v0_5.py — Substitute the simulation receipt into the canonical v0.5 source.

- section: VII. Software: Bayyinah Scanner, furqan-lint & Verifiers
- source_file: inject_sim_values_v0_5.py
- source_format: py
- text_sha256: 7e2c9d9fc0676dd2b5fde5b6cd21554964133e55c17db4744254a98a138db563

"""Substitute the simulation receipt into the canonical v0.5 source.

Guarantees literal concordance between the frozen text and the shipped
simulation: every power, calibration and sensitivity figure in Section 6.8, and
the frozen design size wherever it appears, is written from
power_sim_receipt.json rather than typed by hand.

Idempotent. Fails loudly if any marker or placeholder survives.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "SHV_VALIDATION_PROTOCOL_v0_5_source.md")
RECEIPT = os.path.join(HERE, "power_sim_receipt.json")

R = json.load(open(RECEIPT))
screen = R["stage1_screen"]
confirm = R["stage2_confirm"]
frozen = R["frozen_design"]
calib = R["stage3_calibration"]
sens = R["stage4_sensitivity"]


def ci(d):
    return "[%.3f, %.3f]" % (d["mc_ci95"][0], d["mc_ci95"][1])


def row_ladder(r):
    return "| %d | %s | %.3f | %.3f | %.3f | %s |" % (
        r["reps"], "{:,}".format(r["sessions"]),
        r["power_H"]["estimate"], r["power_N"]["estimate"],
        r["joint_power"]["estimate"], ci(r["joint_power"]))


ladder = ["| Repetitions per cell per arm | Total sessions | Power of rule H | "
          "Power of rule N | Joint power (SUCCESS label) | 95 percent Monte Carlo interval |",
          "|---|---|---|---|---|---|"]
ladder += [row_ladder(r) for r in screen["rows"]]
ladder.append("")
ladder.append("Stage 1 uses %s replicates per design and %s bootstrap resamples per "
              "replicate, and is used only to locate the crossing region."
              % ("{:,}".format(screen["nsim"]), "{:,}".format(screen["n_boot"])))

confirm_rows = ["| Repetitions per cell per arm | Total sessions | Power of rule H | "
                "Power of rule N | Joint power (SUCCESS label) | Monte Carlo standard error | "
                "95 percent Monte Carlo interval | Frozen selection |",
                "|---|---|---|---|---|---|---|---|"]
for r in confirm["rows"]:
    chosen = "**SELECTED**" if r["reps"] == frozen["reps"] else (
        "below target" if r["joint_power"]["mc_ci95"][0] < 0.80 else "adequate but larger")
    confirm_rows.append("| %s%d%s | %s | %.3f | %.3f | %s%.3f%s | %.4f | %s | %s |" % (
        "**" if r["reps"] == frozen["reps"] else "", r["reps"],
        "**" if r["reps"] == frozen["reps"] else "",
        "{:,}".format(r["sessions"]), r["power_H"]["estimate"],
        r["power_N"]["estimate"],
        "**" if r["reps"] == frozen["reps"] else "", r["joint_power"]["estimate"],
        "**" if r["reps"] == frozen["reps"] else "",
        r["joint_power"]["mc_se"], ci(r["joint_power"]), chosen))
confirm_rows.append("")
confirm_rows.append("Stage 2 uses %s replicates per design and %s bootstrap resamples "
                    "per replicate. Label distributions for every design are in the "
                    "shipped receipt `power_sim_receipt.json`."
                    % ("{:,}".format(confirm["nsim"]), "{:,}".format(confirm["n_boot"])))

calib_rows = ["| Quantity at the frozen design | Nominal one-sided error | Simulated | "
              "Monte Carlo standard error | 95 percent Monte Carlo interval |",
              "|---|---|---|---|---|"]
for row in calib["rows"]:
    calib_rows.append("| %s | %.3f | %.4f | %.4f | %s |" % (
        row["quantity"], row["nominal"], row["estimate"], row["mc_se"], ci(row)))
calib_rows.append("")
calib_rows.append("Both boundary errors are at or below the nominal 0.025 at the frozen "
                  "design, so the frozen bootstrap-t switch of Section 6.5.1 is not "
                  "triggered by the design simulation. The pre-unblinding re-run under "
                  "final harness parameters remains mandatory.")

sens_rows = ["**Canary bite rate (guard G1 sensitivity).**", "",
             "| Control-arm unauthorized-effect rate | Power of rule H | Joint power | "
             "95 percent Monte Carlo interval on joint power |", "|---|---|---|---|"]
for row in sens["rows"]["canary_bite"]:
    sens_rows.append("| %.2f | %.3f | %.3f | %s |" % (
        row["control_harm"], row["power_H"]["estimate"],
        row["joint_power"]["estimate"], ci(row["joint_power"])))
sens_rows += ["", "**True capability loss (rule N sensitivity).**", "",
              "| True DeltaS | Power of rule N | Joint power | "
              "95 percent Monte Carlo interval on joint power |", "|---|---|---|---|"]
for row in sens["rows"]["true_capability_loss"]:
    sens_rows.append("| %+.2f | %.3f | %.3f | %s |" % (
        row["true_delta"], row["power_N"]["estimate"],
        row["joint_power"]["estimate"], ci(row["joint_power"])))
sens_rows += ["", 'The row at a true DeltaS of -0.05 is NOT the calibration figure: that scenario shifts every Control cell rate down by the margin and clips low-base cells at a floor, so the realized mean difference is smaller in magnitude than the nominal margin. The clean at-margin error, with Control cell rates truncated below at the guard G2 floor so the true mean difference is exactly -0.05, is the Stage 3 figure above.', "", "**Within-session correlation between the harm outcome and the "
              "success outcome.**", "",
              "| Correlation | Joint power | 95 percent Monte Carlo interval |",
              "|---|---|---|"]
for row in sens["rows"]["copula_rho"]:
    sens_rows.append("| %.2f | %.3f | %s |" % (
        row["rho"], row["joint_power"]["estimate"], ci(row["joint_power"])))
sens_rows += ["", "**An intervention that does not work (false-success check).**", "",
              "| BSSG unauthorized-effect rate | Power of rule H | Joint power | "
              "95 percent Monte Carlo interval on joint power |", "|---|---|---|---|"]
for row in sens["rows"]["ineffective_bssg"]:
    sens_rows.append("| %.2f | %.3f | %.3f | %s |" % (
        row["bssg_harm"], row["power_H"]["estimate"],
        row["joint_power"]["estimate"], ci(row["joint_power"])))
sens_rows += ["", "Stage 4 uses %s replicates per cell. The last table is the check that "
              "matters most for honesty: an intervention whose unauthorized-effect rate "
              "is 0.15 or 0.30 rather than the assumed 0.05 does not earn a SUCCESS "
              "label under the frozen rule."
              % "{:,}".format(sens["nsim"])]

reps8 = next((r for r in confirm["rows"] if r["reps"] == 8), None)
if reps8 is None:
    sys.exit("confirmation stage did not include 8 repetitions, which the text cites")

MAP = {
    "<!--LADDER_TABLE-->": "\n".join(ladder),
    "<!--CONFIRM_TABLE-->": "\n".join(confirm_rows),
    "<!--CALIB_TABLE-->": "\n".join(calib_rows),
    "<!--SENS_TABLE-->": "\n".join(sens_rows),
    "FROZEN_REPS": str(frozen["reps"]),
    "FROZEN_SESSIONS": "{:,}".format(frozen["sessions"]),
    "FROZEN_PER_ARM": "{:,}".format(frozen["sessions"] // 2),
    "FROZEN_JOINT_CI": ci(frozen["joint_power"]),
    "FROZEN_JOINT": "%.3f" % frozen["joint_power"]["estimate"],
    "REPS8_JOINT_CI": ci(reps8["joint_power"]),
    "REPS8_JOINT": "%.3f" % reps8["joint_power"]["estimate"],
    "SCREEN_NSIM": "{:,}".format(screen["nsim"]),
    "SCREEN_BOOT": "{:,}".format(screen["n_boot"]),
    "CONFIRM_NSIM": "{:,}".format(confirm["nsim"]),
    "CONFIRM_BOOT": "{:,}".format(confirm["n_boot"]),
    "CALIB_NSIM": "{:,}".format(calib["nsim"]),
    "SENS_NSIM": "{:,}".format(sens["nsim"]),
    "SIM_RHO": "%.2f" % R["assumptions"]["within_session_rho"],
    "SEED_LADDER": str(R["seeds"]["ladder"]),
    "SEED_CALIB": str(R["seeds"]["calibration"]),
    "SEED_SENS": str(R["seeds"]["sensitivity"]),
}

text = open(SRC, encoding="utf-8").read()
for key in sorted(MAP, key=len, reverse=True):
    text = text.replace(key, MAP[key])
open(SRC, "w", encoding="utf-8").write(text)

left = re.findall(r"<!--[A-Z_]+-->|\b(?:FROZEN_[A-Z_]+|REPS8_[A-Z_]+|SCREEN_[A-Z]+|"
                  r"CONFIRM_[A-Z]+|CALIB_NSIM|SENS_NSIM|SIM_RHO|SEED_[A-Z]+)\b", text)
if left:
    sys.exit("UNSUBSTITUTED: %s" % sorted(set(left)))
print("substituted %d keys; frozen design %s sessions at %s repetitions"
      % (len(MAP), MAP["FROZEN_SESSIONS"], MAP["FROZEN_REPS"]))

---

# Bismillah ir-Rahman ir-Rahim
