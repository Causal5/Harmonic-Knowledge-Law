# Erratum and reconciliation: main moved to 270942c (Round 19)

**TL;DR.** Jordan fixed mussel §8 item 4 on `main` (23 November 2026, 5:07 PM America/New_York): the 2023 fish-passage project named in citation [38] is at Lock and Dam 22 near Saverton, not at Keokuk. Official papers are still identical on both branches. This file records that fix, what the branch did to follow it, and which earlier branch wording is now superseded. It does not rewrite earlier verdict bodies or edit `main`.

**Status:** `accepted-with-revisions` with the Round 19 cycle.

## What changed on `main`

- Previous pin: `c9e12778aba0014732a8add3c90c5676e5785bf7`.
- Current `main`: `270942cd107ffc92a44b4be8d7fffa0e6c22fd1d` — “Correct the fish passage site in mussel example §8.”
- The only file that changed is `Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md`. Official papers, Registry v0.3.2, both October records, ARCHITECTURE, MANIFEST, Release/README, and `START_HERE.md` remain identical on `main` and this branch.

## What the branch did

- §8 item 4 on this branch now uses the published `main` sentence. The earlier branch wording of item 4 (which still located a “first of its kind” passage at Keokuk and then corrected it only in a Session 3 note) is superseded.
- The Session 3 retrieval note is shortened: it records that `main` has the correction, and keeps the unpublished LD19 / uADS / USGS 05474500 pointer.
- §8 item 3 on this branch still uses the Round 7 wording that does not assign *severed* from a qualitative story. The published `main` sentence still does. That remains a Jordan-only `main` fix (`ai/REVIEW_FOR_JORDAN.md` B1).
- Diverging and branch-only `Release/` paths now carry an “unpublished vs `main`” banner. Nothing was silently copied to `main`, and official papers were not rewritten.

## Earlier verdicts (not rewritten)

- `V-2026-11-21-keokuk-ld19-status` (Round 12) found the [38] mislocation. That finding is now reflected on `main` by Jordan’s own edit. The verdict body is preserved. The worked fill remains unpublished branch work.
- `V-2026-11-21-session2-corpus-corrections` (Round 7) and the Round 18 source-precedence erratum still correctly describe item 3. Item 4’s site typo is no longer outstanding on `main`.
