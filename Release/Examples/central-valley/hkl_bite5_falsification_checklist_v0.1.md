# HKL Bite 5 falsification checklist v0.1

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

**TL;DR.** This is a predeclared score sheet for later Bite 5 work, not a
completed test. It splits two questions the protocol already asks: when
the Temporal Mining story itself is weakened, and when an HKL burden
index fails to add anything beyond a simpler water budget. It also lists
results that would look like failures but are not, according to current
HKL (for example, burden going up for a while under a still-adequate
margin). Every check is unfilled. No weights, scores, or cutoffs are
chosen here.

**Status:** accepted-with-revisions (Round 4). Parents:
`temporal-mining-freshwater-protocol-v0.2.md` §6, §6.1, §10, and Bite 5;
`Release/HKL/hkl-lyapunov.md` §3–§4, §6; Round 1 dictionary residuals
remain open.

## 1. What this is not

This is not Bite 5 execution, not a computed \(V_W\), and not empirical
validation of HKL. Official Central Valley / San Joaquin boundaries, the
hydrologic-year window, and retrieved source versions remain
UNFILLED-REQUIRED from Round 1. Those must be filled with evidence before
any check below can be scored. A blank check is reported as
`needs-evidence`, not as a pass.

No new primitive and no new universal cutoff are adopted.

Protocol §10 says the Temporal Mining interpretation is “weakened or
rejected” if listed conditions hold. This sheet does **not** invent a
split between “weaken” and “reject.” It only records whether each
condition fired. The protocol’s unsplit wording still governs what that
firing means.

## 2. Three report columns

Each check is later marked with exactly one of:

- **Fired** — the named condition was tested and held.
- **Did not fire** — the named condition was tested and did not hold.
- **Needs-evidence** — the official series or a required predeclaration
  is not yet available.

Do not mark “did not fire” merely because a horizon has not been reached
(see NF-2). Do not use a combined “weaken / reject” mark as if those were
already two different, defined verdicts.

## 3. Block A — Temporal Mining interpretation (protocol §10 items 1–5)

These tests are about the study’s Temporal Mining reading, not about
whether \(V_W\) is a good index.

| ID | Condition already in protocol §10 | Result |
|---|---|---|
| TM-1 | Climate-normalized groundwater storage is not declining | UNFILLED |
| TM-2 | Service stability does not depend materially on groundwater stock | UNFILLED |
| TM-3 | Subsidence and permanent loss are absent or unrelated to pumping | UNFILLED |
| TM-4 | Connected-water and ecological burdens do not rise or are fully accounted | UNFILLED |
| TM-5 | Firm substitution and demand reduction close the transition gap before thresholds are crossed | UNFILLED |

“Materially” and “fully accounted” remain as in the protocol; this sheet
does not replace them with a new number. If a condition fires, report
that firing; do not relabel it as a newly defined “reject” or “weaken.”

## 4. Block B — HKL operationalization (protocol §10 item 6, Bite 5, HKL §4)

HKL receives incremental support only if \(V_W\) adds predictive or
diagnostic value beyond its individual hydrologic variables and beyond a
simpler water-budget model.

**Required predeclarations (all UNFILLED-REQUIRED; lock before any
Block B check is scored):**

- Normalization, weight sets to be tested, viable set, and held-out
  periods (already required by protocol Bite 5 and HKL-1).
- **Comparison metric class:** a *held-out score* on the outcomes already
  named in protocol §6 — storage, head, subsidence, transition-gap, and
  ecological outcomes. The specific score (for example, how those
  outcomes are combined) remains UNFILLED-REQUIRED, but it must be a
  held-out score on that named list. An in-sample score, a function that
  drops the named outcomes, or a metric changed after seeing which model
  won is recorded as HKL-2 firing. No numeric metric value is chosen here.
- **Hard-threshold list:** the declared hard physical thresholds that
  HKL-4 will use. Locked before HKL-4 is marked; not chosen after seeing
  \(V_W\).

| ID | Predeclared condition | Result |
|---|---|---|
| HKL-1 | Normalization, weights, thresholds, viable set, and held-out periods were not locked before \(V_W\) was compared with baselines | UNFILLED |
| HKL-2 | The comparison metric was in-sample, was not a held-out score on the named §6 outcomes, or was chosen or changed after seeing which model won | UNFILLED |
| HKL-3 | On the locked held-out metric and locked held-out windows, a simpler water-budget or unaggregated-component model predicts as well as or better than \(V_W\) | UNFILLED |
| HKL-4 | A favorable component of \(V_W\) was allowed to erase a threshold on the locked hard-threshold list | UNFILLED |
| HKL-5 | Unaggregated components were not reported beside \(V_W\) | UNFILLED |
| HKL-6 | Several defensible weight sets were not tested, or only the best-looking set was reported | UNFILLED |

If HKL-3 fires, that is the protocol’s own weakening or rejection of
incremental HKL support (still using the protocol’s unsplit wording). It
is not a rejection of the raw hydrologic observations.

## 5. Block C — Not-failures (do not treat these as rejects by themselves)

Current HKL §4 and protocol §6.1 already say that some patterns are *not*
automatic failures. Recording them as if a Block A or B condition had
fired would be a procedure error.

| ID | Pattern that is not, by itself, a failed operationalization |
|---|---|
| NF-1 | Temporary positive burden drift (\(\dot V_W>0\) on some intervals) while the trajectory remains inside the declared viable set |
| NF-2 | No exit observed before a finite horizon (right-censored buffer, not proven safety) |
| NF-3 | A constant burden index, by itself, offered as “equilibrium” |
| NF-4 | Using “Lyapunov-style burden function” without claiming a completed Lyapunov theorem |

NF-3 is a *misreading to avoid*, not a hydrologic observation. NF-2 must
not be scored as “did not fire” on a safety claim, and must not be scored
as proven safety.

Also do not identify \(V_W^*\) with \(V_{PCB}\) or with \(V_{max}\) by
definition (HKL §3).

## 6. Reporting rule

Bite 5 may be reported only after Blocks A and B are marked, including
`needs-evidence` where official inputs or required predeclarations are
still missing. Success and failure must be reported in the same format.
This checklist is not itself that report.
