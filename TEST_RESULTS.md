# Test Results — CCCS-R Reference Implementation

- **Date:** 2026-10-02
- **Command:** `python3 -m pytest tests/ -v`
- **Environment:** Python 3.12.12, pytest 9.1.1, Linux
- **Code under test:** `r_score/` @ commit `5dec116` (code unchanged by README update `8324d446`)

## Result: 14/14 PASSED (2.06s)

| # | Test | Status |
|---|------|--------|
| 1 | `test_weights_locked` | PASSED |
| 2 | `test_sd_formula_sig` | PASSED |
| 3 | `test_sahr_strict` | PASSED |
| 4 | `test_alm_clipping` | PASSED |
| 5 | `test_god_rename` | PASSED |
| 6 | `test_anchor_list_immutable` | PASSED |
| 7 | `test_reject_list_present` | PASSED |
| 8 | `test_quantum_position_locked` | PASSED |
| 9 | `test_falsifiability_present` | PASSED |
| 10 | `test_speaker_thresholds_locked` | PASSED |
| 11 | `test_speaker_vector_shape` | PASSED |
| 12 | `test_efl_backward_compat_at_sigma_1` | PASSED |
| 13 | `test_efl_hard_reset_at_sigma_0` | PASSED |
| 14 | `test_speaker_ema_half_life` | PASSED |

Suite: `tests/test_fork_rejection.py` — enforces CANONICAL.md v1.0.0 (locked weights 0.4/0.3/0.3, locked anchors, formula signatures).
