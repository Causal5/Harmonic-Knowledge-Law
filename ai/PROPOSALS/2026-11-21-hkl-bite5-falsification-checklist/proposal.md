# Proposal: HKL Bite 5 falsification checklist

**TL;DR.** Before anyone computes a burden index for the Central Valley
study, this cycle writes a blank score sheet that says what would count
as weakening Temporal Mining, what would count as an HKL index that adds
nothing, and what should *not* be called a failure (such as a temporary
rise in burden). No scores are filled. The exact comparison metric is
left blank on purpose and must be locked before any fitting.

## Deliverable

`Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md`

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-bite5-falsification-01 | The checklist separates Temporal Mining §10 items 1–5 from HKL incremental-value checks, records HKL §4 / §6.1 not-failures, and adds no new primitive or universal cutoff. | Those blocks are mixed or omitted, or a new primitive or cutoff is introduced. |
| C-bite5-falsification-02 | No weights, \(V_W\), or empirical results are computed; the comparison metric is UNFILLED-REQUIRED and must be locked before fitting. | A score, weight, or metric value is filled, or the checklist treats a post-hoc metric as valid. |
| C-bite5-falsification-03 | This is not Bite 5 execution or HKL validation; Round 1 official-boundary residuals remain open, and a blank check is `needs-evidence`, not a pass. | The checklist claims a completed test, fills official study bounds without evidence, or treats missing data as success. |
