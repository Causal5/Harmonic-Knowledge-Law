# Proposal: Layer 1 / implementation consistency audit

**TL;DR.** Before inventing new theory, this cycle writes down concrete
mismatches already in the repo: experimental code that treats “effort”
as if it were successful correction, import names that probably will not
run on Linux, random numbers used as scores, and an unpromoted Sahel
addendum that still talks as if a measured sign-change test had been
passed. The current AEF, HKL, and Sahel *papers* are not being rewritten
here.

## Parent documents

- `ai/CHARTER.md`, `Release/ARCHITECTURE.md`
- `Release/Registry/definition-decisions-2026-10-16.md`
- `Release/Papers/absorbic-effort-framework.md`
- `Release/Examples/sahel_worked_example.md`
- `Release/Examples/sahel-logistic-addendum-section9-draft.md`
- `Release/Examples/README.md`
- `src/IIF_Evaluator.py`, `src/GILN_AI.py`, `src/giln_network.py`,
  `src/test_giln_combined.py`
- `README.md` (repository areas: `src/` is experimental)

## Scope and status

**Status proposed:** dated audit findings, to live at
`ai/AUDITS/2026-11-21-layer1-consistency.md`. Recommended later notice in
`src/` if findings F1–F3 hold. No change to established paper bodies.

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-layer1-consistency-01 | Finding F1 is present as described: `_apply_pae` in `src/IIF_Evaluator.py` reduces `delta` by a term built from the `effort` argument, which conflicts with the 16 October decision to keep expenditure separate from achieved correction. | The cited function does not so reduce `delta`, or the 16 October record does not require that separation. |
| C-layer1-consistency-02 | Findings F2 and F3 are present as described (import/filename mismatch; listed scorers return `np.random.uniform(0.5, 1.0)`). | The imports match the filenames on a case-sensitive import, or those scorers are not random as cited. |
| C-layer1-consistency-03 | Finding F4 is present as described, and the addendum is already labeled unpromoted; this audit does not treat it as current Sahel authority. | The addendum does not use the withdrawn sign-change wording as an anchor, or the current Sahel paper did not withdraw it. |
| C-layer1-consistency-04 | This proposal does not rewrite established Layer 1 papers and is not empirical validation of HKL or PAE. | The proposal edits those papers or claims a scientific validation result. |

## Suggested verifier checks

- Read the cited lines in `src/IIF_Evaluator.py` and the 16 October decision table.
- Run the imports on a case-sensitive system.
- Confirm the current Sahel paper’s withdrawal wording and the addendum’s status line in `Release/Examples/README.md`.
- Confirm this commit does not modify `Release/Papers/`, `Release/HKL/`, or the current Sahel paper body.
