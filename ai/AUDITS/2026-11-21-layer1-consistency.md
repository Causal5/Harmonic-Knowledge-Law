# Layer 1 / implementation consistency audit

**TL;DR.** This is a checklist of specific mismatches already sitting in the
repository, not a rewrite of the science and not a claim that the whole
framework is false. The strongest issue is in the experimental Python:
a function named as if it applies Absorbic Effort treats “effort” as
automatically shrinking an error score, which the 16 October definitions
explicitly say not to do. Two other code problems (import names, random
scores) and one unpromoted Sahel addendum that still talks as if a sign
change had been measured are also recorded.

**Status:** proposed audit findings. No Layer 1 paper body is edited here.

## Scope

Searched, on `ai/evolution`, the established papers under `Release/Papers/`,
`Release/HKL/`, `Release/Examples/` (except treating `Release/archive/` as
non-governing), the current registry decision records, and `src/`. This is
not a complete-corpus proof.

## Findings

### F1 — Experimental PAE helper treats expenditure as correction

In `src/IIF_Evaluator.py`, `_apply_pae` is documented “Apply Principle of
Absorbic Effort, amplifying effect based on impact,” and computes
`f_e = k * effort * amplification` then `adjusted_delta = max(delta - f_e, 0)`.
That subtracts a quantity derived from the effort argument from an error
score. `Release/Registry/definition-decisions-2026-10-16.md` decided to
“Record allocation, expenditure, achieved correction, and side burden
separately,” because “a costly attempt can fail,” and rejected treating
spent effort as successful correction. `Release/Papers/absorbic-effort-framework.md`
§2: “expenditure alone does not establish corrective orientation.”

`README.md` already lists `src/` as experimental implementation material.
The mismatch is still in the tree, and the function name invites citation
as if it implemented current PAE.

### F2 — Import names do not match filenames

`src/test_giln_combined.py` imports `from giln_ai import GILNNetworkAI`.
`src/GILN_AI.py` and `src/giln_network.py` import `from iif_evaluator import IIFEvaluator`.
The files are named `GILN_AI.py` and `IIF_Evaluator.py`. On a case-sensitive
filesystem those imports are expected to fail. This finding is a filename
observation; a run check is requested of the verifier.

### F3 — Several “scores” are random draws

In `src/IIF_Evaluator.py`, `_score_foresight`, `_score_creativity`,
`_score_impact`, `_score_adaptability`, `_score_coherence`, and
`_score_efficiency` each `return np.random.uniform(0.5, 1.0)`. Those
outputs cannot be evidence for HKL, PAE, or cognition. This agrees with
the cautious status already given to experimental code, and should be
stated next to any future citation of `hkl_ai_score`.

### F4 — Unpromoted Sahel logistic addendum still uses withdrawn completion wording as an anchor

The current Sahel paper,
`Release/Examples/sahel_worked_example.md` §5, withdraws the wording that
`dV/dt` “measurably flipped sign” and that the framework “passed” a
falsification test. The unpromoted
`Release/Examples/sahel-logistic-addendum-section9-draft.md` still treats
that sign change as the example’s “empirical anchor” and “falsification
anchor” (passages around the audit-finding / gain-function discussion
already quoted in prior reviews, and in this draft’s own use of the
flipped-sign language). `Release/Examples/README.md` already marks the
addendum “Unpromoted source; calibration and model decisions pending.”
The risk is reuse, not hidden current-paper authority.

## What this audit does not do

It does not rewrite AEF, HKL, or the Sahel paper. It does not execute a
code patch in this proposal (a status notice is recommended if the
findings hold). It does not promote or demote Registry v0.3.2.
