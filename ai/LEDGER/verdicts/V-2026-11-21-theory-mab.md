# Verdict: Theory MAB registry and first assessments (Round 16)

**TL;DR.** Accept with revisions. The registry exists, assessments were written before any development, four arms are dropped, one is marked wait, and no arm was developed. Revisions: “reward signal” stays qualitative, and `wait` is not explore and is not permission to score Bite 5 or construct \(V\). Layer 0 is unchanged.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-21-theory-mab/`

**Date:** 2026-11-21, America/New_York

## Checks run

- Read `ai/THEORY_MAB.md`. Confirmed five arm records with the required fields, decisions drop/drop/drop/drop/wait, and no companion development fill in this cycle.
- Confirmed Layer 0 charter was not edited in the [A] commit.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-theory-mab-01 | accepted-with-revisions | The file is a process aid with assessments first. CH-theory-mab-01-not-a-bandit-algorithm **hits as a summary risk** (A already denied a numeric algorithm; the revision adds that “reward signal” is qualitative prose, not a score or regret bound). |
| C-theory-mab-02 | accepted-with-revisions | No arm was developed; earlier unassigned quantities stay unassigned. CH-theory-mab-02-wait-is-not-explore **hits as a summary risk** (A already said wait is not a hidden go-ahead; the revision states that wait expires only after a new assessment when the missing inputs are actually in hand). |

## What this is not

Not a Layer 0 change, not a fitted bandit, not a Bite 5 score, not \(\eta\), not a restored Sahel result. `main` was not changed.
