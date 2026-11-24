# Verdict: Round 20 DWR head-sign stress test (Tulare Lake 5-022.12)

**TL;DR.** Accept with revisions. The pre-registered sign test **holds**: a clean `--offline` replay gives 15 Good-quality pairs and a median depth-to-water change of +19.03 feet for October–November 2019 vs 2025, the same direction as the v0.2 net storage loss. Revisions make two over-reads hard to miss: this is a median of 15 unweighted qualifying pairs, not a subbasin head or a confirmation of 468,635 acre-feet; and short summaries must name the locked fall window and the opposite-sign spring 2015–2024 companion. η, *severed*, buffer, \(V_W\), and Bite 5 remain unassigned.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-24-tulare-dwr-head-contrast/`

**Date:** 2026-11-24, America/New_York

## Checks run

- Re-ran `python3 scripts/compute_tulare_dwr_head_contrast.py --offline` on the committed extracts. Decision block: `n_G` 15, `median_delta_ft` 19.03, outcome `holds`. Summary SHA-256 remains `ebcc2af755045d57989648560ae6aefd07bc7950e5554c18c0d9d6ba7e4f7bac`.
- Confirmed `PREREG.md` locks the October–November 2019 vs 2025 decision window, the \(n_G \ge 5\) rule, and the spring contrast as not the decision.
- Confirmed the fill leaves η, *severed*, official buffer, \(V_W\), and Bite 5 unassigned.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-dwr-head-01 | accepted | CH-dwr-head-01-rerun **misses**. The offline replay matches the committed decision statistics. |
| C-dwr-head-02 | accepted-with-revisions | The sign test holds under the locked rule. CH-dwr-head-02-sign-not-volume **misses as a false claim** (A already called it a sign test and refused volume conversion) and **hits as a summary risk**. The revision states “median of 15 qualifying Good pairs,” unweighted, zone not locked, not a spatially weighted subbasin head, and not confirmation of 468,635 AF. |
| C-dwr-head-03 | accepted-with-revisions | The spring companion (n=11, median −42.97 ft) is in the fill and scoreboard. CH-dwr-head-03-window-dependence **misses as a false claim** and **hits as a summary risk**. The revision requires short summaries to name the locked fall window and the opposite-sign companion. |

## What this is not

Not a Bite 5 score, not \(V_W\), not η or *severed*, not a volume reconstruction, not an attribution of storage loss to pumping, and not a publication to `main`.
