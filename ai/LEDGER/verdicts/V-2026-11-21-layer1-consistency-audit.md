# V-2026-11-21-layer1-consistency-audit

**TL;DR.** The audit’s concrete findings hold. Official papers were not
rewritten and are not the broken objects here. Experimental `_apply_pae`
really does treat effort as shrinking an error score; the listed imports
really fail on Linux; several scores really are random; the unpromoted
Sahel addendum really still uses withdrawn sign-change wording. The
adversary was right that the audit understated a larger problem in that
same addendum: it cites “Sahel §5.1” and “HKL §5.1” material the current
papers do not have, and it treats PAE as a number. The audit was revised
(new finding F5) and a status notice was added under `src/README.md`.

**Proposal:** `ai/PROPOSALS/2026-11-21-layer1-consistency-audit/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-layer1-consistency-01-authority-scope | C-layer1-consistency-01 | miss | The audit and claim locate F1 in experimental `src/`, cite the official definition as the standard, and do not treat the code as governing. The title was tightened in revision to make that authority split explicit. |
| CH-layer1-consistency-02-import-behavior | C-layer1-consistency-02 | miss | On this Linux box, `from giln_ai import GILNNetworkAI` and `from iif_evaluator import IIFEvaluator` both raised `ModuleNotFoundError`. F3 random scorers are present as cited. |
| CH-layer1-consistency-03-stale-section-citations | C-layer1-consistency-03 | hit | The addendum passages are present; current Sahel and HKL lack those section numbers and formulas; the proposal audit did not record this. Finding F5 was added. |
| CH-layer1-consistency-04-paper-edits | C-layer1-consistency-04 | miss | The [A] commit `5633d85` touched only `ai/` files. No established paper body was edited. The proposal does not claim empirical validation. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-layer1-consistency-01 | accepted | F1 present; official 16 October record requires the separation. |
| C-layer1-consistency-02 | accepted | F2 demonstrated by live import failure; F3 confirmed in source. |
| C-layer1-consistency-03 | accepted-with-revisions | F4 present; F5 added for stale section citations and PAE-as-number. |
| C-layer1-consistency-04 | accepted | Scope claim held. |

## Mechanical checks (this box)

- Read `src/IIF_Evaluator.py` `_apply_pae` and the 16 October attempt-versus-effect row.
- Ran, on Linux 6.12 (case-sensitive), with `src/` on `sys.path`:
  - `giln_ai` → `ModuleNotFoundError: No module named 'giln_ai'`
  - `iif_evaluator` → `ModuleNotFoundError: No module named 'iif_evaluator'`
  - `IIF_Evaluator` → imported
  - `GILN_AI` → failed on the nested `iif_evaluator` import
- Confirmed the six listed `_score_*` methods return `np.random.uniform(0.5, 1.0)`; `_score_reasoning` does not.
- Confirmed current Sahel §5 withdrawal wording; current Sahel headings have no §5.1; current HKL headings are §1–§7 with §5 “Effect accounting” and no §5.1.
- Confirmed addendum header v2 citations, “Sahel §5.1” OIE-integral wording, “HKL §5.1” margin formula, and \(\lambda_{PAE}(t)\,PAE(t)\).
- `git show --name-only 5633d85`: no `Release/Papers/`, `Release/HKL/`, or `sahel_worked_example.md`.

## Revisions applied in the verdict commit

- Expanded `ai/AUDITS/2026-11-21-layer1-consistency.md` with F5 and a clearer authority split.
- Added `src/README.md` status notice (no function-body patch).
- Updated claim statuses and the ledger.

## Residual / later work

- Actual repair of `src/` imports and `_apply_pae` is not done.
- The unpromoted addendum body is not edited; a later cycle or Jordan may add a banner or withdraw stale citations.
- No empirical Sahel or mussel calculation was performed.
