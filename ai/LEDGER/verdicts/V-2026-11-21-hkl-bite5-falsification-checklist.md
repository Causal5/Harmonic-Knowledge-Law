# V-2026-11-21-hkl-bite5-falsification-checklist

**TL;DR.** The blank checklist is a real tightening of how Bite 5 should
be reported, and it computed no scores. All three challenges hit and
were fixed: the comparison metric must be a held-out score on the
protocol’s named outcomes; the sheet now records whether a condition
fired instead of inventing a weaken-versus-reject split; and the hard-
threshold list must be locked before HKL-4 is scored.

**Proposal:** `ai/PROPOSALS/2026-11-21-hkl-bite5-falsification-checklist/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-bite5-falsification-01-weaken-vs-reject | C-bite5-falsification-01 | hit | The proposal used a combined “Weaken / reject” column. Revised to fired / did not fire / needs-evidence, and the protocol’s unsplit wording is kept. |
| CH-bite5-falsification-01-hard-thresholds | C-bite5-falsification-01 | hit | HKL-4 had no locked threshold list. A required UNFILLED predeclaration was added. |
| CH-bite5-falsification-02-metric-class | C-bite5-falsification-02 | hit | “Any predeclared function” was too open. The metric class is now a held-out score on the named §6 outcomes; post-hoc or in-sample metrics fire HKL-2. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-bite5-falsification-01 | accepted-with-revisions | Blocks were present; reporting column and threshold lock revised. |
| C-bite5-falsification-02 | accepted-with-revisions | No scores filled; metric class tightened. |
| C-bite5-falsification-03 | accepted | Not execution; missing evidence is not a pass. Unchallenged. |

## Mechanical checks (this box)

- Every Block A and B result cell is UNFILLED. No weight, \(V_W\), or metric value is filled.
- [A] `19cc2c0` added the checklist and `ai/` ledger files; `git diff c9e1277..19cc2c0` on the v0.2 protocol and `Release/HKL/hkl-lyapunov.md` is empty.
- Confirmed the proposal column “Weaken / reject,” unconstrained “predeclared function,” and missing threshold-list lock in the pre-revision text.

## Revisions applied in the verdict commit

- Report columns changed as above.
- Held-out metric class and hard-threshold predeclaration added.
- Central Valley README table row added.
- Claim statuses and ledger updated.

## Residual / later work

- Official boundaries, window, and source versions from Round 1 still need evidence.
- The specific held-out score (how named outcomes are combined) remains UNFILLED-REQUIRED and must be locked before fitting.
- A later cycle may justify a weaken-versus-reject split; this one does not invent it.
