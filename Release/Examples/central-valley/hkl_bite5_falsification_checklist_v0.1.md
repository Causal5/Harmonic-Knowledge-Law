# HKL Bite 5 falsification checklist v0.1

**TL;DR.** This is a predeclared score sheet for later Bite 5 work, not a
completed test. It splits two questions the protocol already asks: when
the Temporal Mining story itself is weakened, and when an HKL burden
index fails to add anything beyond a simpler water budget. It also lists
results that would look like failures but are not, according to current
HKL (for example, burden going up for a while under a still-adequate
margin). Every check is unfilled. No weights, scores, or cutoffs are
chosen here.

**Status:** proposed. Parents: `temporal-mining-freshwater-protocol-v0.2.md`
§6, §6.1, §10, and Bite 5; `Release/HKL/hkl-lyapunov.md` §3–§4, §6;
Round 1 dictionary residuals remain open.

## 1. What this is not

This is not Bite 5 execution, not a computed \(V_W\), and not empirical
validation of HKL. Official Central Valley / San Joaquin boundaries, the
hydrologic-year window, and retrieved source versions remain
UNFILLED-REQUIRED from Round 1. Those must be filled with evidence before
any check below can be scored. A blank check is reported as
`needs-evidence`, not as a pass.

No new primitive and no new universal cutoff are adopted. Protocol §10
item 6 (“a simpler water-budget model explains and predicts as well as or
better”) is left with its comparison *metric* UNFILLED-REQUIRED: the
metric family must be named after the protocol’s own held-out outcomes
and locked **before** \(V_W\) is fit. Choosing the metric after seeing
which index wins is itself a weakening of the test, not a result.

## 2. Three report columns

Each check is later marked with exactly one of:

- **Hold** — the named condition was tested and did not fire.
- **Weaken / reject** — the named condition fired, as defined in §10 or
  below.
- **Needs-evidence** — the official series or a required predeclaration
  is not yet available.

Do not mark “hold” merely because a horizon has not been reached.

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
does not replace them with a new number.

## 4. Block B — HKL operationalization (protocol §10 item 6, Bite 5, HKL §4)

HKL receives incremental support only if \(V_W\) adds predictive or
diagnostic value beyond its individual hydrologic variables and beyond a
simpler water-budget model. The following are predeclared failure or
weakening modes for that claim. None is scored here.

| ID | Predeclared condition | Result |
|---|---|---|
| HKL-1 | Normalization, weights, thresholds, viable set, and held-out periods were not locked before \(V_W\) was compared with baselines | UNFILLED |
| HKL-2 | The comparison metric (UNFILLED-REQUIRED; must be a predeclared function of the held-out outcomes already named in protocol §6: storage, head, subsidence, transition-gap, and ecological outcomes) was chosen after seeing which model won | UNFILLED |
| HKL-3 | On the locked metric and locked held-out windows, a simpler water-budget or unaggregated-component model predicts as well as or better than \(V_W\) | UNFILLED |
| HKL-4 | A favorable component of \(V_W\) was allowed to erase a declared hard physical threshold | UNFILLED |
| HKL-5 | Unaggregated components were not reported beside \(V_W\) | UNFILLED |
| HKL-6 | Several defensible weight sets were not tested, or only the best-looking set was reported | UNFILLED |

If HKL-3 fires, that is the protocol’s own weakening or rejection of
incremental HKL support. It is not a rejection of the raw hydrologic
observations.

## 5. Block C — Not-failures (do not treat these as rejects by themselves)

Current HKL §4 and protocol §6.1 already say that some patterns are *not*
automatic failures. Recording them as rejects would be a procedure error.

| ID | Pattern that is not, by itself, a failed operationalization |
|---|---|
| NF-1 | Temporary positive burden drift (\(\dot V_W>0\) on some intervals) while the trajectory remains inside the declared viable set |
| NF-2 | No exit observed before a finite horizon (right-censored buffer, not proven safety) |
| NF-3 | A constant burden index, by itself, offered as “equilibrium” |
| NF-4 | Using “Lyapunov-style burden function” without claiming a completed Lyapunov theorem |

NF-3 is a *misreading to avoid*, not a hydrologic observation. NF-2 must
not be scored as “hold” on safety.

Also do not identify \(V_W^*\) with \(V_{PCB}\) or with \(V_{max}\) by
definition (HKL §3).

## 6. Reporting rule

Bite 5 may be reported only after Blocks A and B are marked, including
`needs-evidence` where official inputs are still missing. Success and
failure must be reported in the same format. This checklist is not itself
that report.
