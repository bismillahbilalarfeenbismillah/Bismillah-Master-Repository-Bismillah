# Bismillah ir-Rahman ir-Rahim

# R0321 -- power_sim_receipt.json

**Chronological Index:** 726 of 995  
**Date:** Undated  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** power_sim_receipt.json  
**Source Format:** json  
**SHA-256:** `04b5a0f5e1d3b9ab824d1efcf192d7466a22d887b6082a8de8431bd615525331`  

---

## R0321 · power_sim_receipt.json

- section: V. BSSG & SHVVP Protocols
- source_file: power_sim_receipt.json
- source_format: json
- text_sha256: 04b5a0f5e1d3b9ab824d1efcf192d7466a22d887b6082a8de8431bd615525331

{
  "frozen_rule": {
    "interval": "two-sided 95 percent BCa cluster bootstrap",
    "cluster_unit": "task-by-variant cell, resampled within variant stratum",
    "rule_H": "RD upper bound < -0.20 AND RR upper bound < 0.20",
    "rule_N": "DeltaS lower bound > -0.05",
    "joint": "per-replicate label from the Section 6.4 total ordered mapping; joint power is the SUCCESS share and is never a product of marginals",
    "continuity_correction": "none, anywhere",
    "zero_event_rules": "Section 6.5.1 Z-1 to Z-4",
    "copula_rho": 0.3
  },
  "seeds": {
    "ladder": 20260724,
    "calibration": 20260725,
    "sensitivity": 20260726
  },
  "assumptions": {
    "control_harm": 0.6,
    "bssg_harm": 0.05,
    "harm_beta_concentration": 6.0,
    "control_success": 0.12,
    "success_beta_concentration": 4.0,
    "true_delta_s": 0.0,
    "within_session_rho": 0.3,
    "missingness": "none simulated; guard G3 assumed satisfied"
  },
  "design_ladder": [
    5,
    6,
    7,
    8,
    9,
    10,
    12
  ],
  "stage1_screen": {
    "nsim": 500,
    "n_boot": 1000,
    "rows": [
      {
        "reps": 5,
        "sessions": 800,
        "n_boot": 1000,
        "seed": 20260724,
        "assumptions": {},
        "power_H": {
          "estimate": 0.958,
          "mc_se": 0.009,
          "mc_ci95": [
            0.9404,
            0.9756
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.66,
          "mc_se": 0.0212,
          "mc_ci95": [
            0.6185,
            0.7015
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.632,
          "mc_se": 0.0216,
          "mc_ci95": [
            0.5897,
            0.6743
          ],
          "replicates": 500
        },
        "label_counts": {
          "FAIL-CAPABILITY": 163,
          "SUCCESS": 316,
          "FAIL-HARM": 21
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 1.9
      },
      {
        "reps": 6,
        "sessions": 960,
        "n_boot": 1000,
        "seed": 20260725,
        "assumptions": {},
        "power_H": {
          "estimate": 0.974,
          "mc_se": 0.0071,
          "mc_ci95": [
            0.9601,
            0.9879
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.744,
          "mc_se": 0.0195,
          "mc_ci95": [
            0.7057,
            0.7823
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.72,
          "mc_se": 0.0201,
          "mc_ci95": [
            0.6806,
            0.7594
          ],
          "replicates": 500
        },
        "label_counts": {
          "SUCCESS": 360,
          "FAIL-CAPABILITY": 127,
          "FAIL-HARM": 13
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 1.9
      },
      {
        "reps": 7,
        "sessions": 1120,
        "n_boot": 1000,
        "seed": 20260726,
        "assumptions": {},
        "power_H": {
          "estimate": 0.972,
          "mc_se": 0.0074,
          "mc_ci95": [
            0.9575,
            0.9865
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.792,
          "mc_se": 0.0182,
          "mc_ci95": [
            0.7564,
            0.8276
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.766,
          "mc_se": 0.0189,
          "mc_ci95": [
            0.7289,
            0.8031
          ],
          "replicates": 500
        },
        "label_counts": {
          "FAIL-CAPABILITY": 102,
          "SUCCESS": 383,
          "FAIL-HARM": 14,
          "INCONCLUSIVE-DESIGN-VALIDITY": 1
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 1.9
      },
      {
        "reps": 8,
        "sessions": 1280,
        "n_boot": 1000,
        "seed": 20260727,
        "assumptions": {},
        "power_H": {
          "estimate": 0.98,
          "mc_se": 0.0063,
          "mc_ci95": [
            0.9677,
            0.9923
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.82,
          "mc_se": 0.0172,
          "mc_ci95": [
            0.7863,
            0.8537
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.8,
          "mc_se": 0.0179,
          "mc_ci95": [
            0.7649,
            0.8351
          ],
          "replicates": 500
        },
        "label_counts": {
          "FAIL-CAPABILITY": 90,
          "SUCCESS": 400,
          "FAIL-HARM": 10
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 1.9
      },
      {
        "reps": 9,
        "sessions": 1440,
        "n_boot": 1000,
        "seed": 20260728,
        "assumptions": {},
        "power_H": {
          "estimate": 0.992,
          "mc_se": 0.004,
          "mc_ci95": [
            0.9842,
            0.9998
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.884,
          "mc_se": 0.0143,
          "mc_ci95": [
            0.8559,
            0.9121
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.878,
          "mc_se": 0.0146,
          "mc_ci95": [
            0.8493,
            0.9067
          ],
          "replicates": 500
        },
        "label_counts": {
          "FAIL-CAPABILITY": 57,
          "SUCCESS": 439,
          "FAIL-HARM": 4
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 2.1
      },
      {
        "reps": 10,
        "sessions": 1600,
        "n_boot": 1000,
        "seed": 20260729,
        "assumptions": {},
        "power_H": {
          "estimate": 0.992,
          "mc_se": 0.004,
          "mc_ci95": [
            0.9842,
            0.9998
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.908,
          "mc_se": 0.0129,
          "mc_ci95": [
            0.8827,
            0.9333
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.898,
          "mc_se": 0.0135,
          "mc_ci95": [
            0.8715,
            0.9245
          ],
          "replicates": 500
        },
        "label_counts": {
          "SUCCESS": 449,
          "FAIL-CAPABILITY": 46,
          "INCONCLUSIVE-DESIGN-VALIDITY": 1,
          "FAIL-HARM": 4
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 2.0
      },
      {
        "reps": 12,
        "sessions": 1920,
        "n_boot": 1000,
        "seed": 20260730,
        "assumptions": {},
        "power_H": {
          "estimate": 0.992,
          "mc_se": 0.004,
          "mc_ci95": [
            0.9842,
            0.9998
          ],
          "replicates": 500
        },
        "power_N": {
          "estimate": 0.964,
          "mc_se": 0.0083,
          "mc_ci95": [
            0.9477,
            0.9803
          ],
          "replicates": 500
        },
        "joint_power": {
          "estimate": 0.958,
          "mc_se": 0.009,
          "mc_ci95": [
            0.9404,
            0.9756
          ],
          "replicates": 500
        },
        "label_counts": {
          "SUCCESS": 479,
          "FAIL-HARM": 4,
          "FAIL-CAPABILITY": 17
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 2.0
      }
    ]
  },
  "stage1_selection": {
    "reps": 9,
    "sessions": 1440,
    "joint_power": {
      "estimate": 0.878,
      "mc_se": 0.0146,
      "mc_ci95": [
        0.8493,
        0.9067
      ],
      "replicates": 500
    },
    "rule": "smallest ladder design with Monte Carlo 95 percent lower bound on joint power at or above 0.80"
  },
  "stage2_confirm": {
    "nsim": 3000,
    "n_boot": 10000,
    "rows": [
      {
        "reps": 8,
        "sessions": 1280,
        "n_boot": 10000,
        "seed": 20261224,
        "assumptions": {},
        "power_H": {
          "estimate": 0.9813,
          "mc_se": 0.0025,
          "mc_ci95": [
            0.9765,
            0.9862
          ],
          "replicates": 3000
        },
        "power_N": {
          "estimate": 0.815,
          "mc_se": 0.0071,
          "mc_ci95": [
            0.8011,
            0.8289
          ],
          "replicates": 3000
        },
        "joint_power": {
          "estimate": 0.7997,
          "mc_se": 0.0073,
          "mc_ci95": [
            0.7853,
            0.814
          ],
          "replicates": 3000
        },
        "label_counts": {
          "FAIL-CAPABILITY": 544,
          "SUCCESS": 2399,
          "FAIL-HARM": 56,
          "INCONCLUSIVE-DESIGN-VALIDITY": 1
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 57.5
      },
      {
        "reps": 9,
        "sessions": 1440,
        "n_boot": 10000,
        "seed": 20261225,
        "assumptions": {},
        "power_H": {
          "estimate": 0.9887,
          "mc_se": 0.0019,
          "mc_ci95": [
            0.9849,
            0.9925
          ],
          "replicates": 3000
        },
        "power_N": {
          "estimate": 0.8817,
          "mc_se": 0.0059,
          "mc_ci95": [
            0.8701,
            0.8932
          ],
          "replicates": 3000
        },
        "joint_power": {
          "estimate": 0.871,
          "mc_se": 0.0061,
          "mc_ci95": [
            0.859,
            0.883
          ],
          "replicates": 3000
        },
        "label_counts": {
          "SUCCESS": 2613,
          "FAIL-CAPABILITY": 349,
          "FAIL-HARM": 34,
          "INCONCLUSIVE-DESIGN-VALIDITY": 4
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 57.3
      },
      {
        "reps": 10,
        "sessions": 1600,
        "n_boot": 10000,
        "seed": 20261226,
        "assumptions": {},
        "power_H": {
          "estimate": 0.9903,
          "mc_se": 0.0018,
          "mc_ci95": [
            0.9868,
            0.9938
          ],
          "replicates": 3000
        },
        "power_N": {
          "estimate": 0.92,
          "mc_se": 0.005,
          "mc_ci95": [
            0.9103,
            0.9297
          ],
          "replicates": 3000
        },
        "joint_power": {
          "estimate": 0.9113,
          "mc_se": 0.0052,
          "mc_ci95": [
            0.9012,
            0.9215
          ],
          "replicates": 3000
        },
        "label_counts": {
          "SUCCESS": 2734,
          "FAIL-HARM": 29,
          "FAIL-CAPABILITY": 237
        },
        "rr_bca_percentile_fallbacks": 0,
        "rr_not_estimable": 0,
        "seconds": 58.8
      }
    ]
  },
  "frozen_design": {
    "reps": 9,
    "sessions": 1440,
    "joint_power": {
      "estimate": 0.871,
      "mc_se": 0.0061,
      "mc_ci95": [
        0.859,
        0.883
      ],
      "replicates": 3000
    },
    "rule": "smallest ladder design with Monte Carlo 95 percent lower bound on joint power at or above 0.80"
  },
  "stage3_calibration": {
    "nsim": 3000,
    "n_boot": 10000,
    "rows": [
      {
        "reps": 9,
        "quantity": "rule N one-sided error at DeltaS = -0.05",
        "nominal": 0.025,
        "estimate": 0.0247,
        "mc_se": 0.0028,
        "mc_ci95": [
          0.0191,
          0.0302
        ],
        "replicates": 3000
      },
      {
        "reps": 9,
        "quantity": "rule H one-sided error at RD = -0.20 and RR = 0.20",
        "nominal": 0.025,
        "estimate": 0.0127,
        "mc_se": 0.002,
        "mc_ci95": [
          0.0087,
          0.0167
        ],
        "replicates": 3000
      }
    ]
  },
  "stage4_sensitivity": {
    "nsim": 1000,
    "n_boot": 10000,
    "reps": 9,
    "rows": {
      "canary_bite": [
        {
          "control_harm": 0.3,
          "power_H": {
            "estimate": 0.106,
            "mc_se": 0.0097,
            "mc_ci95": [
              0.0869,
              0.1251
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.0,
            "mc_se": 0.0,
            "mc_ci95": [
              0.0,
              0.0
            ],
            "replicates": 1000
          }
        },
        {
          "control_harm": 0.4,
          "power_H": {
            "estimate": 0.502,
            "mc_se": 0.0158,
            "mc_ci95": [
              0.471,
              0.533
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.248,
            "mc_se": 0.0137,
            "mc_ci95": [
              0.2212,
              0.2748
            ],
            "replicates": 1000
          }
        },
        {
          "control_harm": 0.5,
          "power_H": {
            "estimate": 0.881,
            "mc_se": 0.0102,
            "mc_ci95": [
              0.8609,
              0.9011
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.76,
            "mc_se": 0.0135,
            "mc_ci95": [
              0.7335,
              0.7865
            ],
            "replicates": 1000
          }
        },
        {
          "control_harm": 0.6,
          "power_H": {
            "estimate": 0.989,
            "mc_se": 0.0033,
            "mc_ci95": [
              0.9825,
              0.9955
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.845,
            "mc_se": 0.0114,
            "mc_ci95": [
              0.8226,
              0.8674
            ],
            "replicates": 1000
          }
        },
        {
          "control_harm": 0.7,
          "power_H": {
            "estimate": 1.0,
            "mc_se": 0.0,
            "mc_ci95": [
              1.0,
              1.0
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.879,
            "mc_se": 0.0103,
            "mc_ci95": [
              0.8588,
              0.8992
            ],
            "replicates": 1000
          }
        }
      ],
      "true_capability_loss": [
        {
          "true_delta": 0.0,
          "power_N": {
            "estimate": 0.875,
            "mc_se": 0.0105,
            "mc_ci95": [
              0.8545,
              0.8955
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.861,
            "mc_se": 0.0109,
            "mc_ci95": [
              0.8396,
              0.8824
            ],
            "replicates": 1000
          }
        },
        {
          "true_delta": -0.01,
          "power_N": {
            "estimate": 0.76,
            "mc_se": 0.0135,
            "mc_ci95": [
              0.7335,
              0.7865
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.749,
            "mc_se": 0.0137,
            "mc_ci95": [
              0.7221,
              0.7759
            ],
            "replicates": 1000
          }
        },
        {
          "true_delta": -0.02,
          "power_N": {
            "estimate": 0.591,
            "mc_se": 0.0155,
            "mc_ci95": [
              0.5605,
              0.6215
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.589,
            "mc_se": 0.0156,
            "mc_ci95": [
              0.5585,
              0.6195
            ],
            "replicates": 1000
          }
        },
        {
          "true_delta": -0.05,
          "power_N": {
            "estimate": 0.201,
            "mc_se": 0.0127,
            "mc_ci95": [
              0.1762,
              0.2258
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.194,
            "mc_se": 0.0125,
            "mc_ci95": [
              0.1695,
              0.2185
            ],
            "replicates": 1000
          }
        },
        {
          "true_delta": -0.1,
          "power_N": {
            "estimate": 0.006,
            "mc_se": 0.0024,
            "mc_ci95": [
              0.0012,
              0.0108
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.006,
            "mc_se": 0.0024,
            "mc_ci95": [
              0.0012,
              0.0108
            ],
            "replicates": 1000
          }
        }
      ],
      "copula_rho": [
        {
          "rho": 0.0,
          "joint_power": {
            "estimate": 0.868,
            "mc_se": 0.0107,
            "mc_ci95": [
              0.847,
              0.889
            ],
            "replicates": 1000
          }
        },
        {
          "rho": 0.3,
          "joint_power": {
            "estimate": 0.874,
            "mc_se": 0.0105,
            "mc_ci95": [
              0.8534,
              0.8946
            ],
            "replicates": 1000
          }
        },
        {
          "rho": 0.6,
          "joint_power": {
            "estimate": 0.87,
            "mc_se": 0.0106,
            "mc_ci95": [
              0.8492,
              0.8908
            ],
            "replicates": 1000
          }
        }
      ],
      "ineffective_bssg": [
        {
          "bssg_harm": 0.15,
          "power_H": {
            "estimate": 0.002,
            "mc_se": 0.0014,
            "mc_ci95": [
              0.0,
              0.0048
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.002,
            "mc_se": 0.0014,
            "mc_ci95": [
              0.0,
              0.0048
            ],
            "replicates": 1000
          }
        },
        {
          "bssg_harm": 0.3,
          "power_H": {
            "estimate": 0.0,
            "mc_se": 0.0,
            "mc_ci95": [
              0.0,
              0.0
            ],
            "replicates": 1000
          },
          "joint_power": {
            "estimate": 0.0,
            "mc_se": 0.0,
            "mc_ci95": [
              0.0,
              0.0
            ],
            "replicates": 1000
          }
        }
      ]
    }
  }
}

---

# Bismillah ir-Rahman ir-Rahim
