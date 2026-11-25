# Verdict: Round 26 Paani service vs groundwater-condition records

**TL;DR.** Accept with revisions. Limb A holds and Limb B breaks, so the published justification **breaks** as a scope / object-class limit, not a Layer 0 failure. The revision: short summaries must keep Limb A as a hold, and must not call Table 4 a delivered-service series or call this a theory failure.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-25-paani-service-condition/`

**Date:** 2026-11-25, America/New_York

## Checks run

- Confirmed the pre-registration commit (`f719835`) precedes the scored fill.
- Reran `compute_paani_direction_pairs.py`. It reports two opposite regions (North Maharashtra, Marathwada) and two same regions.
- Confirmed the fill leaves \(D_W\), Bite 5, and \(V\) unassigned, and does not rewrite the published pages.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-paani-sc-01 | accepted | The protocol was locked before the outcome was assigned. No challenge. |
| C-paani-sc-02 | accepted-with-revisions | Break / scope / object-class is the correct round-level outcome. Both challenges **hit as a summary risk**. |

## What this is not

Not a Layer 0 or theory failure, not a denial of the Marathwada numbers, not a locked \(D_W\) fill, not a Bite 5 score, and not a publication to `main`.
