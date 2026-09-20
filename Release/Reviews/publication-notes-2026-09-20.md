# Publication notes — 20 September 2026

The Central Valley freshwater example, Temporal Mining protocol, Buffer paper, integration drafts, Sahel addendum, earlier SLP documents, and audit material are now indexed together in the repository. Original research bodies and source variants are preserved. The [publication index](../PUBLICATION-INDEX.md) and [source manifest](../publication-sources-2026-09-20.json) define the exact coverage.

## What this checkpoint resolves

Recovered project documents previously outside the repository now have stable paths, explicit status, and content checksums. Ten recovered source copies were confirmed already present. Navigation no longer describes the existing Sahel example as missing, and legacy links point to the archive where the files actually reside.

The older audit's inability to inspect the Sahel section 9 addendum is a source-availability issue resolved here. Its substantive claims still require evaluation. The preserved project-status report predates this publication; references in it to unpublished files are historical.

## What remains open

| Workstream | Remaining work |
|---|---|
| Registry and parent hierarchy | Ratify v0.4, reconcile HKL/AEF inheritance with the current Worldline parent, and migrate downstream notation consistently |
| Central Valley | Produce a reproducible matched dataset; separate water age from renewal/recovery time and gross draw from net depletion; compute physical indicators and perform comparison/held-out tests |
| Buffer | Reconcile viability reference versus exit boundary, gradient/sign conventions, and corrective-energy versus transported-burden accounting before operational use |
| Sahel | Reconcile section 9 with the current parent papers; define and calibrate coefficients and reachability bounds; supply the referenced multipatch and simulation work |
| SLP and harness | Implement and test semantic reduction, evidence-sensitive acceptance, quarantine, traceability, and meaningful efficiency benchmarks |
| Agency arguments | Specify observable criteria, comparison systems, counterexamples, and validation boundaries before claiming a universal agency test |

The Sahel logistic proposal also needs a stability check: for the classical recurrence `x[n+1] = r*x[n]*(1-x[n])`, the nonzero fixed point has derivative `2-r`, so its local stability range is `1 < r < 3`. Increasing a mapped parameter toward 4 is therefore not, by itself, a monotonic stabilization mechanism. The addendum's proposed mapping must be tested against an explicitly stated target behavior.

These items carry forward the [corpus audit](slap-v0.4-corpus-audit.md) and [project-status review](project-status-2026-09-20.md). Publishing the material closes an availability gap; it does not mark those research tasks complete.

## Version authority

The [v0.3 registry](../Registry/causal-ethics-master-symbol-registry.md) remains the current registry; the [v0.4 document](../Registry/causal-ethics-master-symbol-registry-v0.4-draft.md) remains explicitly a research draft. The [Worldline formalization](../Delta-Self/delta-self-worldline-formalization.md) remains the current parent. An older or newly recovered manuscript is not promoted solely because it has a higher version number.
