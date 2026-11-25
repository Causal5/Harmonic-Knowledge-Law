# Verdict: Round 27 lag-justified Tulare DWR head-sign windows

**TL;DR.** Accept with revisions. W1 and W2 hold; W3 breaks (median −20.49 ft, n=36), so the round **breaks** as scope / window-dependence, not a Layer 0 failure. The revision: short summaries must name all three locked windows and must not convert the medians to a volume or treat the published site lags as Tulare travel times.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-25-tulare-lag-windows/`

**Date:** 2026-11-25, America/New_York

## Checks run

- Confirmed the pre-registration commit (`6c8ea86`) precedes the scored fill.
- Reran `compute_tulare_lag_windows.py --offline`. Results match the fill: W3 n=36, median −20.49 ft, breaks; W2 n=34, median +14.20 ft, holds; W1 n=36, median +2.72 ft, holds.
- Confirmed the fill leaves Bite 5 and \(V_W\) unassigned and does not convert a sign to acre-feet.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-lag-win-01 | accepted | The protocol was locked before signed differences were computed. Offline replay matches. |
| C-lag-win-02 | accepted-with-revisions | Break / window-dependence is the correct round-level outcome. Both challenges **hit as a summary risk**. |

## What this is not

Not a Layer 0 or theory failure, not a confirmation or refutation of the 468,635 AF figure, not an assignment of Oro Grande or orchard-model lags to Tulare wells, and not a publication to `main`.
