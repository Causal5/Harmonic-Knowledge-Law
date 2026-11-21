# Layer 1 / implementation consistency audit

**TL;DR.** This is a checklist of specific mismatches already sitting in the
repository, not a rewrite of the science and not a claim that the whole
framework is false. The official AEF, HKL, and current Sahel *papers* are
not internally rewritten here and are not the source of the main defects
below. The strongest issue is in the experimental Python: a function named
as if it applies Absorbic Effort treats “effort” as automatically shrinking
an error score, which the 16 October definitions explicitly say not to do.
Two other code problems (import names, random scores) are also recorded.
The unpromoted Sahel logistic addendum has a broader stale-citation problem
than the first draft of this audit stated: besides still using withdrawn
sign-change wording as an empirical anchor, it cites “Sahel §5.1” and
“HKL §5.1” material that the current papers do not contain, and it treats
PAE as a number.

**Status:** accepted-with-revisions (Round 2). No Layer 1 paper body is
edited here. `src/README.md` now carries a status notice.

## Scope and authority

Searched, on `ai/evolution`, the established papers under `Release/Papers/`,
`Release/HKL/`, `Release/Examples/` (except treating `Release/archive/` as
non-governing), the current registry decision records, and `src/`. This is
not a complete-corpus proof.

`README.md` already lists `src/` as experimental implementation material.
Findings F1–F3 are about that experimental code drifting from the current
definitions. They are not defects in the official PAE paper. Finding F4–F5
are about an *unpromoted* in-tree example draft, already marked
“Unpromoted source; calibration and model decisions pending” in
`Release/Examples/README.md`. That draft is not current Sahel authority,
but it can still be misread as extending the current papers.

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

The mismatch is in experimental code, not in the official definition. The
function name still invites citation as if it implemented current PAE.

### F2 — Import names do not match filenames

`src/test_giln_combined.py` imports `from giln_ai import GILNNetworkAI`.
`src/GILN_AI.py` and `src/giln_network.py` import `from iif_evaluator import IIFEvaluator`.
The files are named `GILN_AI.py` and `IIF_Evaluator.py`.

**Verifier check (2026-11-21, Linux, case-sensitive filesystem).** With
`src/` on `sys.path`: `giln_ai` and `iif_evaluator` raised
`ModuleNotFoundError`. `IIF_Evaluator` imported. `GILN_AI` failed because
it still does `from iif_evaluator import IIFEvaluator`.

### F3 — Several “scores” are random draws

In `src/IIF_Evaluator.py`, `_score_foresight`, `_score_creativity`,
`_score_impact`, `_score_adaptability`, `_score_coherence`, and
`_score_efficiency` each `return np.random.uniform(0.5, 1.0)`. Those
outputs cannot be evidence for HKL, PAE, or cognition. (`_score_reasoning`
is not in that list: it returns `min(len(node.connections) / 10, 1.0)`.)
This agrees with the cautious status already given to experimental code,
and should be stated next to any future citation of `hkl_ai_score`.

### F4 — Unpromoted Sahel logistic addendum still uses withdrawn completion wording as an anchor

The current Sahel paper,
`Release/Examples/sahel_worked_example.md` §5, withdraws the wording that
`dV/dt` “measurably flipped sign” and that the framework “passed” a
falsification test. The unpromoted
`Release/Examples/sahel-logistic-addendum-section9-draft.md` still treats
that sign change as the example’s “empirical anchor” and “falsification
anchor,” and later says directional claims are “consistent with … Sahel
§4.3’s empirical anchor.” `Release/Examples/README.md` already marks the
addendum unpromoted. The risk is reuse, not hidden current-paper authority.

### F5 — Same addendum cites section numbers and formulas the current papers do not contain (Round 2 revision)

Added after challenge CH-layer1-consistency-03-stale-section-citations
(hit). In `Release/Examples/sahel-logistic-addendum-section9-draft.md`:

1. The header lists “HKL Lyapunov v2” and “AEF v2” among sources, and an
   “Authoritative chain: Worldline → Extension → Sahel (this addendum
   extends Sahel §§5–8).” Current `Release/HKL/hkl-lyapunov.md` §7 says
   the recovered v2 draft is historical and does not override the current
   definitions.
2. The draft says “Sahel §5.1 already commits OIE to being a measure over
   \(S_\Phi\),” with an integral \(OIE_\int\). Current
   `Release/Examples/sahel_worked_example.md` has no §5.1; §5 withdraws
   completion claims; the migration table says OIE is a process.
3. The draft defines a “basin-maintenance margin from HKL §5.1,”
   \(M(t) := \mathcal{F}_{PAE}-\mathcal{F}_{OIE}-\frac{1}{w_0}\sum_{k\ge1}w_k\dot B_k(t)\),
   and states \(M(t)>0\iff dV/dt<0\). Current HKL has no §5.1; §5 is
   “Effect accounting”; the current margin is
   \(M_{V,\Omega}=V_{max,\Omega}-V_\Omega\), not that flux difference.
   The formula resembles superseded `Release/Working/hkl-lyapunov-v2.md` §5.1.
4. The gain function includes a term written \(\lambda_{PAE}(t)\,PAE(t)\),
   treating PAE as a number, which current AEF §2 and the 16 October
   record reject.

These are defects in an unpromoted in-tree draft relative to the current
papers, not defects in the current official Sahel or HKL texts themselves.

## What this audit does not do

It does not rewrite AEF, HKL, or the current Sahel paper. It does not
compute empirical scores. It does not promote or demote Registry v0.3.2.
It does not patch experimental function bodies in this cycle; `src/README.md`
is a status notice only.
