# V-2026-11-21-session2-corpus-corrections

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. Substance follows AEF and the 16/30 October records on `main`. The mussel-example and Sahel-addendum *edits* are not on `main`. On `main`, §8 item 3 still assigns *severed* qualitatively; the 30 October record controls the flag. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** The four Session 1 corrections Jordan asked for are in, and
they were checked on this Linux box. Expenditure is no longer subtracted
from delta; the `src/` imports run; random placeholders in `src/` return
`None`; the addendum has a status banner; mussel §8 no longer assigns
the severed flag from a qualitative line. Four leftover issues hit and
were fixed: invented scores still printed by `_score_reasoning` and
Libra, `np.random` placeholders in `CorePrinciples/Law_of_We_Full.md`,
an unmarked AEF §3.2 cite in the addendum body, and a stale “so …
severed” quote in the ebonyshell protocol. No empirical η or Sahel
series was invented, and no dead cite was given a made-up replacement
section.

**Proposal:** `ai/PROPOSALS/2026-11-21-session2-corpus-corrections/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-s2-corrections-01-pae-separation | C-s2-corrections-01 | miss | `_apply_pae(2.5, effort=10.0)` left `delta` at 2.5, recorded `expenditure` 10.0, and left `achieved_correction` as `None`. |
| CH-s2-corrections-02-residual-invented-scores | C-s2-corrections-02 | hit | `_score_reasoning` still returned a connection-count number; Libra still invented EGR, GDS, and an entropy score. Those helpers now return `None`. |
| CH-s2-corrections-02-coreprinciples-random | C-s2-corrections-02 | hit (corpus residual; does not falsify the `src/`-scoped wording) | `CorePrinciples/Law_of_We_Full.md` still used `np.random.uniform` for OIE impact and decision balance. Those two returns are now `None`. |
| CH-s2-corrections-03-unmarked-aef-32 | C-s2-corrections-03 | hit | The Approach 2 “defining feature” paragraph still cited “AEF §3.2, §5” unmarked. Marked in place; no replacement section invented. |
| CH-s2-corrections-04-severed-assignment | C-s2-corrections-04 | miss | Example §8 item 3 cites the 30 October record, treats the narrative as qualitative/provisional, does not assign the flag, and fills no η. |
| CH-s2-corrections-04-protocol-stale-example | C-s2-corrections-04 | hit | The ebonyshell protocol §1 still quoted the old “so … severed” assignment as current. It now records that wording as superseded. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-s2-corrections-01 | accepted | PAE field split holds on a numeric unit check. |
| C-s2-corrections-02 | accepted-with-revisions | Linux imports and `src/` `np.random` removal held; leftover invented numerics and the CorePrinciples placeholders were fixed. |
| C-s2-corrections-03 | accepted-with-revisions | Banner held; the last unmarked AEF §3.2 body cite was marked; no invented replacements. |
| C-s2-corrections-04 | accepted-with-revisions | Example item 3 held; protocol §1 was updated to the reworded example. |

## Mechanical checks (this box)

- `_apply_pae(2.5, effort=10.0)` → `delta` 2.5, `expenditure` 10.0, `achieved_correction` None.
- `src/test_giln_human.py` and `src/test_giln_combined.py` exit 0; HRS are all `None` (not implemented); unevaluated `ai2` is all-None.
- `src/Libra_Model.py` (3-input and 1000-input main) exit 0 with `not_implemented`; EGR and GDS print as `None`, not invented numbers.
- `from GILN_AI import GILNNetworkAI` and `from IIF_Evaluator import IIFEvaluator` succeed; `from giln_ai` / `from iif_evaluator` still raise `ModuleNotFoundError`.
- `rg` of `src/` and `CorePrinciples/` finds no remaining `np.random` or lowercase import call sites (README mentions the old pattern only in prose).
- Addendum banner is present; body “AEF §3.2” occurrences are marked; current Sahel headings still stop at §7, and current HKL §5 is still “Effect accounting.”
- Mussel example §8 item 3 fills no η. Protocol §1 no longer presents the old assignment as current.

## Remaining residuals (not treated as failures of the four claims)

- `GILN_AI.py` still scales hardcoded `resource_metrics` by 0.1 on “distill,” and still adds `+0.5` to connection weights. Those are not score placeholders, but they are still invented increments.
- `Release/Working/` drafts still cite “HKL §5.1” and “Sahel §5.3” without the addendum-style marks. Those drafts are not current papers.
- Work landed in two `[A]` commits because a single push may carry at most four large file substitutions. Cycle.md prefers one commit per role.
