# Pre-registration: temporal-mining signature completeness, Tulare Lake, 24 November 2026

**Locked 24 November 2026, America/New_York, before delivery or subsidence tables in the WY 2025 filing were extracted for this test.** Unpublished branch work on `ai/evolution`. Not a publication to `main`.

**Parent documents.** [Temporal Mining Freshwater Study Protocol v0.2](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/central-valley/temporal-mining-freshwater-protocol-v0.2.md) §5 on `main`; [Central Valley worked example v0.2](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/central-valley/central-valley-worked-example-v0.2.md) (net fall-to-fall storage loss; signature not claimed to have fired; C-zone storage already uses InSAR).

## What is being tested

Protocol §5 says a buffer-financed stability interval is exhibited when, over a declared window, \(|dD_W/dt|\le\epsilon_{D_W}\), \(dG_W/dt<0\), and \(dC_{irr}/dt>0\). v0.2 already reports a net storage loss over water years 2020–2025 and already says the full signature still needs a matched delivery series and an irreversible-compaction estimate that accounts for shared InSAR input. This test asks whether the public WY 2025 filing can complete that signature under a locked independence rule.

The current papers do **not** claim that the signature already fired in Tulare Lake. A failure of the conjunction is therefore not, by itself, a theory failure. The test is of **completeness**: can the signature be evaluated?

## Locked protocol

- **Window.** The six water years 2020–2025, subbasin 5-022.12, same as the v0.2 storage table.
- **Storage limb.** Use the already published v0.2 net fall-to-fall storage change (−468,635 AF). That limb is treated as \(dG_W/dt<0\) over the six-year interval (annual signs may vary). Not recomputed here.
- **Delivery limb \(D_W\).** A consistent annual surface-water delivery or delivered-service series for 5-022.12, in acre-feet, taken from a named table or section of the WY 2025 filing (PDF SHA-256 `32c080a3a4972730b94ce7d047ffcec90de16348f50abc166c55465096395be9`, already cited in v0.2). The series must cover all six water years and must be distinguished from gross groundwater extraction.
- **Compaction limb \(C_{irr}\).** An annual irreversible-compaction or permanent storage-capacity loss series for the same boundary and years that does **not** use the same InSAR input already incorporated into the C-zone storage estimate (v0.2 §“What the measurements support”). If the only compaction figure shares that InSAR input, \(C_{irr}\) cannot be locked independently.
- **Source.** The WY 2025 PDF only, in this cycle. No new source class.

## Pre-registered outcome rule

| Outcome | If |
|---|---|
| **Holds** (the signature is completable) | Both \(D_W\) and independent \(C_{irr}\) can be locked as specified. Then, and only then, evaluate the conjunction under a predeclared \(\epsilon_{D_W}=0.25\) times the WY 2020 delivery value. Report whether the interval is exhibited, without treating that as validation. |
| **Indeterminate** (not completable) | \(D_W\) or independent \(C_{irr}\) cannot be locked. Leave the signature unassigned. Extract any partial delivery or subsidence figures as observations only. |
| **Breaks** (procedure) | The fill declares the signature to have fired, or not fired, without both locked limbs, or uses the shared InSAR input as if it were an independent \(C_{irr}\) check on the same storage series. |

**Cause if indeterminate.** Scope / data limit of the public filing under the independence rule. Not a Layer 0 theory failure. Not a Bite 5 score.

**Forbidden.** Do not assign Bite 5, \(V_W\), official buffer, or A1–A8 terms.
