# `src/` — experimental implementation material

**TL;DR.** This folder is experimental code. It is not an official
implementation of current Absorbic Effort, HKL, or the 16 October / 30
October definitions. Do not cite scores from these files as evidence for
the framework. Several helpers that used to invent numbers now return
`None` (not implemented), and expenditure is recorded separately from
correction.

**Status (ai/evolution, 2026-11-21, Round 7, accepted-with-revisions).**

- The root `README.md` already lists `src/` as experimental implementation
  material.
- `IIF_Evaluator._apply_pae` now records `expenditure` separately from
  `achieved_correction` (default `None` / not implemented) and does **not**
  subtract effort from `delta`. That follows the 16 October 2026 decision
  record and current AEF §2: a costly attempt can fail.
- The previously random `_score_*` methods, and other `np.random`
  placeholder scores in `GILN_AI.py`, `giln_network.py`, and
  `Libra_Model.py`, now return `None` (not implemented). Initial `hrs`
  arrays are `None`, not zeros pretending to be scores.
- Round 7 verifier revisions: `_score_reasoning` now returns `None` (connection count is not a reasoning score). `Libra_Model` no longer invents EGR, GDS, or an entropy score from hardcoded constants or string length.
- Imports use the actual filenames: `from GILN_AI import GILNNetworkAI`
  and `from IIF_Evaluator import IIFEvaluator`. Test scripts print `None
  (not implemented)` instead of crashing on missing scores.

These scripts can be run, but their numeric “HKL-AI” outputs are not
measurements. A later cycle may implement real scorers against the
current registry; that work is not done here.
