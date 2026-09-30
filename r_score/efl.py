"""EFL — Emotional Feedback Loop (CCCS L3). v1.1.0 with S(t) gating.

Canonical v1.0.0 recurrence (additive, non-convex):
    E(t+1) = αE(t) + βF(t) + γP(t) + δ·(W_s @ S(t))
    α = 0.6, β = 0.25, γ = 0.15, δ = 0.10

sigma gates the recurrence:
    sigma = 1 → canonical update (speaker context active)
    sigma = 0 → hard reset: E(t+1) = F(t)
"""
import numpy as np

ALPHA = 0.6
BETA = 0.25
GAMMA = 0.15
DELTA = 0.10


def emotional_feedback_loop(E, F, P, sigma=1.0, S=None, W_s=None):
    """One EFL step.

    E, F, P: affective state, current-turn feedback, persistent pattern
        contribution (scalars or matching arrays).
    sigma:   1.0 → canonical v1.0.0 update; 0.0 → hard reset to F(t).
    S:       optional speaker context vector S(t) (480-dim). When absent,
             the δ·(W_s @ S(t)) term is zero and the update reduces to the
             canonical v1.0.0 form exactly.
    W_s:     optional projection matrix applied to S.
    """
    if sigma == 0.0:
        return np.asarray(F, dtype=float)

    update = ALPHA * np.asarray(E, dtype=float) \
        + BETA * np.asarray(F, dtype=float) \
        + GAMMA * np.asarray(P, dtype=float)

    if S is not None:
        s = np.asarray(S, dtype=float)
        if W_s is not None:
            s_proj = np.asarray(W_s, dtype=float) @ s
        else:  # mean-projection to a scalar drive
            s_proj = np.full_like(update, s.mean(), dtype=float)
        update = update + DELTA * s_proj

    return np.asarray(sigma * update + (1.0 - sigma) * np.asarray(F, dtype=float))
