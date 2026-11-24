# Verdict: Round 24 Table 3-1 mapping onto protocol \(Q_{sw}\) or \(D_W\)

**TL;DR.** Accept with revisions. Table 3-1 totals cannot be assigned to \(Q_{sw}\) or \(D_W\) under published labels, so the test **breaks** as a scope / object-class limit, not a Layer 0 failure. The revision: short summaries must keep that classification, and must not present the ex-Imported subset as a locked dictionary fill.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-24-tulare-table3-1-mapping/`

**Date:** 2026-11-24, America/New_York

## Checks run

- Confirmed the pre-registration predates the mapping fill.
- Reran `compute_tulare_table3-1_shares.py`. Row sums match; imported share ranges from 0.020018 (WY 2024) to 0.504148 (WY 2015); Dry-year shares range from 0.182318 to 0.504148.
- Confirmed the fill leaves \(Q_{sw}\), \(D_W\), Bite 5, \(V_W\), and the signature unassigned, and does not invent a mixed symbol.
- Confirmed the fill already classifies the outcome as scope / object-class and calls the ex-Imported subset a candidate only.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-map-01 | accepted | The pre-registration predates the scored mapping. No challenge. |
| C-map-02 | accepted-with-revisions | Break / scope / object-class is the correct outcome. CH-map-02-not-theory-failure and CH-map-02-subset-not-fill **hit as a summary risk**; later short summaries must keep both limits. |

## What this is not

Not a Layer 0 or theory failure, not a locked \(Q_{sw}\) or \(D_W\) fill, not a temporal-mining or Bite 5 score, and not a publication to `main`.
