"""SD — Semantic Drift. CANONICAL v1.0.0 LOCKED.

SD = 1 - cos(output_emb, baseline_emb)
Lower is better. Range [0,2], expected [0,1].
FORK-REJECT: implementing `cos` instead of `1 - cos` fails test_fork_rejection.
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compute_sd(embedding_output, embedding_baseline):
    emb_o = np.array(embedding_output).reshape(1, -1)
    emb_b = np.array(embedding_baseline).reshape(1, -1)
    cos = cosine_similarity(emb_o, emb_b)[0][0]
    return float(1 - cos)


# Canonical alias: r_score/sd.py::semantic_drift
def semantic_drift(embedding_output, embedding_baseline):
    return compute_sd(embedding_output, embedding_baseline)
