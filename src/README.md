# `src/` — experimental implementation material

**TL;DR.** This folder is experimental code. It is not an official
implementation of current Absorbic Effort, HKL, or the 16 October / 30
October definitions. Do not cite scores from these files as evidence for
the framework.

**Status (ai/evolution, 2026-11-21, audit
`ai/AUDITS/2026-11-21-layer1-consistency.md`).**

- The root `README.md` already lists `src/` as experimental implementation
  material.
- `IIF_Evaluator.py` defines `_apply_pae`, which subtracts a term built
  from an `effort` argument from an error score. Current definitions keep
  expenditure and achieved correction separate: a costly attempt can fail.
- Several `_score_*` methods return `np.random.uniform(0.5, 1.0)`. Those
  values are not measurements.
- Imports such as `from giln_ai import GILNNetworkAI` and
  `from iif_evaluator import IIFEvaluator` do not match the filenames
  `GILN_AI.py` and `IIF_Evaluator.py`. On a case-sensitive Linux check
  (2026-11-21) those lowercase imports failed with `ModuleNotFoundError`.

No function bodies are patched in this notice. A later cycle may repair
imports or rewrite the helpers against the current registry; that work is
not done here.
