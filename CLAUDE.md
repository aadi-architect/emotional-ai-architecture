# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository actually contains

`README.md`, `CANONICAL.md` (v1.0.0 LOCKED source of truth), the `r_score/` reference
implementation (SD, ALM, SAHR, composite R, S(t) speaker vector, EFL), and
`tests/test_fork_rejection.py` — 14 tests that enforce the canonical formulas, weights, and
anchors. The remaining layers are an **architecture specification**. Treat any file layout
described in older drafts beyond this as aspirational, not present.

Check what exists before assuming it does:

```sh
git ls-files
```

## Scope

Three CCCS layers are specified here:

| Layer | Name | Responsibility |
| --- | --- | --- |
| L3 | Emotional Feedback Loop (EFL) | Bi-directional affective state adaptation across turns |
| L4 | Tone Engine Layer (TEL) | Real-time mood and personality state simulation |
| L6 | Self-Reference Engine (SRE) | Checks output against symbolic anchors to prevent identity drift |

The other layers are specified elsewhere and are out of scope for changes made here:

- L2 Symbolic Anchor Grid, L5 Observer Mirror Protocol → [cognitive-pattern-tools](https://github.com/aadi-architect/cognitive-pattern-tools)
- SIM Core decision modeling → [decision-simulation-framework](https://github.com/aadi-architect/decision-simulation-framework)
- Framework overview, R-Score definitions → [aadi-architect](https://github.com/aadi-architect/aadi-architect)

## The EFL state update

`E(t+1) = αE(t) + βF(t) + γP(t)`

`E` is affective state, `F` is the feedback signal from the current turn, `P` is the persistent
pattern contribution from long-term memory. `α` controls momentum, `β` responsiveness, `γ` the
pull of stored patterns. If you change this formula, change it in `README.md` too — the two
must not diverge.

## House rules for anything published from here

These are not style preferences. Getting them wrong has cost real rework.

1. **Measured and target numbers are never blurred.** R-Score thresholds are *design targets*.
   Do not present one as an achieved result. If a number is quoted as measured, it ships with
   the inputs it was computed from, or it does not ship.
2. **No clinical, therapeutic, or mental-health framing.** No "trauma-informed", no
   "counseling", no "mental-health decision-support". The work is affective computing and
   memory architecture. This applies to prose, examples, use-case lists, and identifiers.
3. **No quantum-physics metaphors.** They were retired deliberately. Use cognitive-science
   terminology.
4. **Label capability honestly.** Where this repository holds only specification, it says so.
   Do not describe planned components in the present tense.
5. **The `+250%` conceptual-complexity figure is source-reported**, not reconstructible — its
   calculation and comparative dataset were not preserved. Do not cite it as a measurement.

## Naming

The public 7-layer stack uses these names, and only these:

ESM · SAG · EFL · TEL · OMP · SRE · FDE
(Emotional Seed Memory, Symbolic Anchor Grid, Emotional Feedback Loop, Tone Engine Layer,
Observer Mirror Protocol, Self-Reference Engine, Feedback-Driven Evolution)

L3 appears as both EFL (Emotional Feedback Loop) and MLS (Memory Loop Simulator). The split
is by document class, not by date: MLS in research and theory documents, EFL in professional
and public-facing ones. This repository is public-facing, so use EFL here. Do not rewrite MLS
where it appears in research documents — it is correct there.

Internal research notes use a longer, function-named decomposition. That is deliberate, not
a contradiction, and it does not belong in public-facing material.

## Author

Published under **Aadi Adarsh** (legal name Adarsh Kumar) — [aadiadarsh.dev](https://aadiadarsh.dev).
Use "Aadi Adarsh" in anything public.