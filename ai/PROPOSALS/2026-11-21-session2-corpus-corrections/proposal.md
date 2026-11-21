# Proposal: Session 2 corpus corrections (Round 7)

**TL;DR.** This cycle applies the four corrections Jordan approved after
Session 1: stop treating “effort” as a successful correction in the
experimental Python, make the `src/` imports run on Linux and stop
inventing random scores, put a status banner and dead-cite marks on the
unpromoted Sahel addendum, and reword the mussel example so the *severed*
flag is provisional until a renewal ratio is actually computed. No new
empirical numbers are invented.

## Parent documents

- Session 1 audit `ai/AUDITS/2026-11-21-layer1-consistency.md` and verdict
  `ai/LEDGER/verdicts/V-2026-11-21-layer1-consistency-audit.md`
- Round 3 ebonyshell protocol and verdict
- `Release/Registry/definition-decisions-2026-10-16.md`
- `Release/Registry/definition-decisions-2026-10-30.md`
- `Release/Papers/absorbic-effort-framework.md` §2
- Current `Release/Examples/sahel_worked_example.md` §5
- Current `Release/HKL/hkl-lyapunov.md` §5, §7

## Deliverables (patched in this proposal)

- `src/IIF_Evaluator.py`, `src/GILN_AI.py`, `src/giln_network.py`,
  `src/human_node.py`, `src/Libra_Model.py`, `src/test_giln_combined.py`,
  `src/test_giln_human.py`, `src/README.md`
- `Release/Examples/sahel-logistic-addendum-section9-draft.md`
- `Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md` §8 item 3 only

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-s2-corrections-01 | `_apply_pae` records expenditure separately from achieved correction and does not reduce `delta` by a term built from effort, in line with the 16 October record and current AEF §2. | The helper still subtracts a term built from effort from `delta`, or it fails to record expenditure and correction as separate fields. |
| C-s2-corrections-02 | Imports use the actual filenames and run on case-sensitive Linux; previously random placeholder scores in `src/` return `None` (not implemented) rather than invented numbers; the test scripts run without crashing. | The lowercase imports are still the call sites, a `np.random` placeholder score remains, or the scripts fail to run on this Linux box. |
| C-s2-corrections-03 | The Sahel logistic addendum carries a status banner stating the withdrawal and stale section cites, and the dead cites are marked in place without invented replacement section numbers. | The banner is missing, a listed dead cite is left unmarked in the body, or a new section number is invented as a replacement. |
| C-s2-corrections-04 | Mussel example §8 item 3 no longer assigns the *severed* flag from a qualitative “effectively zero”; the assignment is provisional pending a computed $\eta$, citing the 30 October record; no renewal ratio is computed. | Item 3 still assigns the flag from the qualitative wording, omits the 30 October citation, or invents a computed $\eta$. |

## Suggested verifier checks

- Read `_apply_pae` and run a numeric-delta unit check: expenditure must leave `delta` unchanged.
- On this Linux box, run `src/test_giln_human.py`, `src/test_giln_combined.py`, and `src/Libra_Model.py`.
- Grep `src/` for `np.random`, `from giln_ai`, and `from iif_evaluator`.
- Confirm addendum banner and [DEAD CITE] / [STALE / WITHDRAWN] marks; confirm current Sahel and HKL still lack those section numbers.
- Confirm only §8 item 3 of the mussel example was reworded, and that no $\eta$ value was filled.
