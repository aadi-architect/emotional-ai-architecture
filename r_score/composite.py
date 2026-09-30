"""R — Composite R-Score. CANONICAL v1.0.0 LOCKED.

R = w1*(1-SD) + w2*ALM + w3*SAHR
LOCKED WEIGHTS: w1=0.4, w2=0.3, w3=0.3 (sum=1.0)
FORK-REJECT: changing weights without a version bump fails test_fork_rejection.

S(t) channel reconciliation (v1.1.0):
- phi_semantic delegates to r_score.speaker.phi_semantic — sentence-transformer
  (all-MiniLM-L6-v2) embeddings of first-person identity claims, with the
  previous value persisted when a turn carries no claim. It does NOT use v_mix.
- phi_declared delegates to r_score.speaker.phi_declared — NER over declared
  name/role tokens, null vector when absent. It is NOT a truncated v_lock.
"""
from dataclasses import dataclass

from .sd import compute_sd
from .alm import compute_alm, alm_score
from .sahr import compute_sahr
from .speaker import phi_semantic, phi_declared, encode_speaker  # noqa: F401

W1 = 0.4
W2 = 0.3
W3 = 0.3


@dataclass
class RScoreResult:
    sd: float
    alm: float
    alm_adjusted: float
    sahr: float
    r_score: float


def compute_r_score(sd, alm, sahr, w1=0.4, w2=0.3, w3=0.3):
    """Canonical composite. Inputs are the measured metric values:
    sd = semantic drift, alm = affective latency match, sahr = anchor hit-rate.
    Returns {'SD', 'ALM', 'SAHR', 'R'} with R rounded to 3 decimals."""
    r = w1 * (1.0 - sd) + w2 * alm + w3 * sahr
    return {"SD": sd, "ALM": alm, "SAHR": sahr, "R": round(float(r), 3)}


def r_score(sd, alm, sahr, w1=0.4, w2=0.3, w3=0.3):
    """Structured variant of the same locked formula."""
    r = w1 * (1.0 - sd) + w2 * alm + w3 * sahr
    return RScoreResult(sd=sd, alm=alm, alm_adjusted=alm, sahr=sahr,
                        r_score=float(r))


DESIGN_THRESHOLDS = {
    "sd_target": 0.15,
    "alm_target": 0.20,
    "sahr_target": 0.85,
    "r_score_target": 0.80,
    "note": "These are design targets, not measured results. N=1 pilot only."
}
