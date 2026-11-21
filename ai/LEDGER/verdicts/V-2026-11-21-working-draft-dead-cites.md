# V-2026-11-21-working-draft-dead-cites

**TL;DR.** The recovered AEF v2 and buffer drafts now carry status
banners and in-place marks for dead section numbers and for withdrawn
“necessary dV/dt ≤ 0” wording. Official papers were not rewritten, and
no replacement sections or formulas were invented. All three challenges
hit and were fixed: AEF v2’s leftover Lyapunov-condition clause, the
buffer draft’s second “requires dV/dt ≤ 0 across the buffer” sentence,
and AEF v2’s unmarked PAE-as-number presentations.

**Proposal:** `ai/PROPOSALS/2026-11-21-working-draft-dead-cites/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-working-cites-01-aef-v2-lyapunov | C-working-cites-01, C-working-cites-02 | hit | Inheritance paragraph still treated dV/dt ≤ 0 as the current Lyapunov condition. Marked stale/withdrawn. |
| CH-working-cites-02-buffer-second-sentence | C-working-cites-02 | hit | The next sentence still required dV/dt ≤ 0 across τ_buffer. Marked. |
| CH-working-cites-01-pae-as-number | C-working-cites-01 | hit | AEF v2 still typed PAE as a number. Table row and first product marked; later products share that status; no replacement formula invented. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-working-cites-01 | accepted-with-revisions | Banners held; leftover unmarked lines were marked; no invented replacements. |
| C-working-cites-02 | accepted-with-revisions | Withdrawn necessary-drift wording is marked in both remaining places; official papers untouched. |
| C-working-cites-03 | accepted | No series filled; no validation claim. |

## Mechanical checks (this box)

- [A] `ea9892e` and this cycle did not modify `Release/HKL/hkl-lyapunov.md`, `Release/Papers/absorbic-effort-framework.md`, or `Release/Examples/sahel_worked_example.md`.
- Current HKL still has no §4.1 or §5.1; current Sahel still has no §5.3; current AEF still has no §3.2 / §3.3 heading; AU remains reserved.
- No empirical series were filled.
