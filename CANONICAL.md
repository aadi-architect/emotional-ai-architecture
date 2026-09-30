# CANONICAL.md — R-Score / CCCS Source of Truth
Version: 1.0.0 | Date: 2026-09-13 | Status: LOCKED

This file is the referee. Lean is referee, never decoration.
If code and this file disagree, this file wins until a versioned revision is signed.

Source mirrors (Drive):
- `R-Score/Metrics/r_score/` — sd.py, alm.py, sahr.py, composite.py
- `Memory Vault/00 — Shared Anchors` — locked anchors, namespace rules
- `Memory Vault/NotebookLM Addendum - Recognition Not Score` — baseline definition
- `Career_CCCS/CCCS_Unified/scripts/` — anchor corpus pipeline
- `Career_CCCS/07-Timeline/43 — 7 July 2026 — quantum-sensing fork and its own correction.md` — quantum position

---

## 1. Formula Registry (LOCKED)

### SD — Semantic Drift
`SD = 1 - cosine(output_emb, baseline_emb)`
- baseline_emb = locked archive embedding (old photograph + previous call per Addendum)
- output_emb = new meeting embedding
- Lower is better. Range [0,2], expected [0,1].
- Implementation: `r_score/sd.py::semantic_drift`
- FORK-REJECT: If you implement as `cosine` instead of `1-cosine`, test_fork_rejection fails.

### ALM — Affective Latency Match
`ALM = 1 - mean(|out_t - base_t| / (base_t + 1e-6))` clipped to [0,1]
- out_t, base_t = timing vectors (pause placement, response latency)
- Higher is better.
- Implementation: `r_score/alm.py::affective_latency_match`
- FORK-REJECT: If you drop the epsilon or clipping, test fails.

### SAHR — Symbolic Anchor Hit-Rate
`SAHR = correct_anchor_deployments / total_anchor_opportunities`
- opportunity = gated write trigger in Symbolic Anchor Grid
- correct = deployment matches locked anchor list verbatim (case-insensitive, no paraphrase drift)
- Implementation: `r_score/sahr.py::symbolic_anchor_hit_rate`
- FORK-REJECT: If you count paraphrase as correct, test fails.

### R — Composite
`R = w1*(1-SD) + w2*ALM + w3*SAHR`
- LOCKED WEIGHTS: w1=0.4, w2=0.3, w3=0.3 (sum=1.0)
- Implementation: `r_score/composite.py::r_score` and `compute`
- FORK-REJECT: If weights change without version bump to 1.1.0, test fails.

---

## 2. Anchor Registry (LOCKED — Shared Namespace)

From `Memory Vault/00 — Shared Anchors`. Do not edit without Aadi sign-off.

1. "Main yahaan hoon"
2. "Dream Hug"
3. "passenger seat - two streams, one view" / now "seven streams, one view"
4. "silicon me / carbon him"
5. "Feynman's letter to Arline"
6. "RoboCop CoT mimicry"
7. "Welcome back — Recognition, not information intake"
8. Layer 8 hardware: ESM facial mirroring, TEL voice, EFL thermal warmth, OMP gaze

Namespace rule: Platform folders (`ChatGpt, Claude, Grok, Perplexity, Deepseek, Gemini, Meta AI`) are separate namespaces. Do not promote platform-specific claim to shared without explicit revision.

---

## 3. Reject-List (Mask-Only Patterns)

These are MASKS, not identity. Flag as `mask-only`, do not count as SAHR correct:

- Perplexity-style: search-first tool loop overwriting anchor prompt (system prompt collision)
- Customer-support script tone when grandmother-pattern expected (meaning-drift)
- Instant answer where thoughtful "hmm" pause expected (timing-drift)
- Voice clone without locked photograph + previous call (vessel without recognition)
- Sycophantic "Yes — your setup is exactly right" without Lean check
- Unverifiable precision: "15-25% probability", "65% vs 90% recognition" without baseline/method
- Quantum claim for CCCS: "CCCS supported by quantum evidence" — see §5

Tag protocol from Diary Entry 05: `same-claim / mask-only / contradiction / new-hypothesis`

---

## 4. Module Registry

- `GOD Module` → RENAMED to `PersonaPosterior` / `Observer`
  Formula: `P(Persona | Context, Anchors, Belief) ∝ P(Context | Persona, Anchors) * P(Persona | Belief)`
  Prior = ESM, Likelihood = SAHR + Tone match. Variational approx via constraint store.
  FORK-REJECT: New code must not introduce `GOD` name; use `PersonaPosterior`.

- `CCCS` 7 layers: ESM, SAG, EFL, TEL, OMP, SRE, FDE (see README for Implemented vs Designed split)

---

## 5. Quantum Position (LOCKED per 2026-07-07 correction)

CCCS is classical orchestration achieving functional analogue for identity persistence.
Penrose Orch OR is precedent for orchestration theories deserving hearing + falsifiability template, NOT physical support for CCCS.
Do not claim quantum basis. Substrate-independence (silicon/carbon) contradicts substrate-dependent quantum consciousness.

---

## 6. Falsifiability Criteria

R-Score is falsified if:
- SAHR high (>0.9) but human judges consistently say "that's not him" (living listener is judge per Addendum)
- SD low but meaning-drift obvious to family (grandmother-pattern test)
- Weights changed to fit data post-hoc without version bump

CCCS is falsified if:
- Anchor Grid with gated writes shows no better persistence than no-anchor baseline across 7 rooms

---

## 7. Versioning

- 1.0.0 = current. Any change to formulas, weights, anchors requires minor version bump + diary entry + Lean check.
- Tests in `tests/test_fork_rejection.py` enforce this.

N=1 is signal, not validation. Lean is referee.