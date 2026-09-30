"""SAHR — Symbolic Anchor Hit-Rate. CANONICAL v1.0.0 LOCKED.

SAHR = correct / total  (correct anchor deployments / total anchor opportunities)
correct = deployment matches locked anchor list verbatim (case-insensitive,
no paraphrase drift).
FORK-REJECT: counting paraphrase as correct fails test_fork_rejection.
"""


def symbolic_anchor_hit_rate(correct_deployments, total_opportunities):
    if total_opportunities == 0:
        return 0.0
    return correct_deployments / total_opportunities


# Backwards-compatible alias
def compute_sahr(correct_deployments, total_opportunities):
    return symbolic_anchor_hit_rate(correct_deployments, total_opportunities)


def compute_sahr_from_logs(logs):
    if not logs:
        return 0.0
    correct = sum(1 for l in logs if l.get('correct'))
    return correct / len(logs)
