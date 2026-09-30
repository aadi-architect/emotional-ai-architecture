"""ALM — Affective Latency Match. CANONICAL v1.0.0 LOCKED.

ALM = 1 - mean(|out_t - base_t| / (base_t + 1e-6)) clipped to [0,1]
Higher is better.
FORK-REJECT: dropping the 1e-6 epsilon or the clip fails test_fork_rejection.
"""
import numpy as np


def compute_alm(timing_output, timing_baseline):
    o = np.array(timing_output, dtype=float)
    b = np.array(timing_baseline, dtype=float)
    if len(o) != len(b) or len(o) == 0:
        return 1.0
    alm = 1.0 - np.mean(np.abs(o - b) / (b + 1e-6))
    return float(np.clip(alm, 0.0, 1.0))


# Canonical alias: r_score/alm.py::affective_latency_match
def affective_latency_match(timing_output, timing_baseline):
    return compute_alm(timing_output, timing_baseline)


def alm_score(alm_divergence):
    return 1.0 - alm_divergence
