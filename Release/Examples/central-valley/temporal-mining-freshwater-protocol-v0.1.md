# Temporal Mining Freshwater Study Protocol v0.1

**Status:** Working empirical protocol; not canonical theory  
**Date:** 2026-06-22  
**Primary case:** California Central Valley, with San Joaquin Valley focus  
**Replication case:** High Plains aquifer

## 1. Study Claim

This study tests one narrow structural claim:

> A water system can maintain approximately stable delivered service while
> destabilizing its future viability by drawing down a slow groundwater stock,
> accumulating irreversible compaction, and failing to build substitute supply
> and demand-reduction capacity before the stock buffer becomes unavailable.

This pattern is the proposed freshwater signature of **Temporal Mining**. It is
not, by itself, validation of Causal Ethics, HKL, Delta-Self, or AEF. It tests
whether those constructs describe a known system without hiding adverse
observations or importing the conclusion into the metric.

## 2. Case Selection

The Central Valley is the first case because one boundary contains long
groundwater and pumping histories, storage-loss estimates, subsidence records,
surface-water deliveries, drought variation, water budgets, and transition
plans. The San Joaquin Valley supplies the nested high-subsidence test. The
High Plains aquifer is the replication case so the framework is not tuned to
one California institutional history.

## 3. Units of Analysis

1. **Hydrologic unit:** basin or subbasin-year.
2. **Institutional unit:** groundwater agency or water-supplier plan-year.
3. **Built-environment unit:** permitted development or facility-year.

Do not merge these into one score until each has been analyzed in its own
physical units.

## 4. Core Time Series

| Variable | Meaning | Preferred unit |
|---|---|---|
| `G(t)` | Recoverable groundwater storage estimate | acre-feet or km3 |
| `H(t)` | Representative groundwater head | metres |
| `W_g(t)` | Gross groundwater withdrawal | volume/year |
| `R_n(t)` | Natural aquifer recharge | volume/year |
| `R_m(t)` | Managed recharge retained in basin | volume/year |
| `Q_sw(t)` | Surface-water delivery or diversion | volume/year |
| `D(t)` | Demand or delivered water service | volume/year |
| `L_s(t)` | Cumulative land subsidence | metres |
| `C_irr(t)` | Irreversible compaction or storage-capacity loss | volume |
| `E_sw(t)` | Burden transferred to connected surface water/ecosystems | declared measure |
| `S_alt(t)` | Firm substitute capacity under the test scenario | volume/year |

Keep natural recharge, managed recharge, gross pumping, net storage change,
and streamflow capture separate. Recharge is not synonymous with sustainable
yield because pumping can reduce groundwater discharge to streams, wetlands,
springs, and dependent ecosystems.

## 5. Temporal Mining Signature

Use observed or model-assimilated storage change as the primary measure:

```math
TM_G(t) = \left[-\frac{dG(t)}{dt}\right]_+
```

where `[x]_+ = max(0,x)`.

The system exhibits a buffer-financed stability interval when, over a declared
window:

```math
\left|\frac{dD}{dt}\right| \le \epsilon_D,
\qquad
\frac{dG}{dt}<0,
\qquad
\frac{dC_{irr}}{dt}>0
```

The claim is stronger when firm transition capacity is inadequate:

```math
T_{gap}(t)=\left[D_{critical}(t)-S_{alt,firm}(t)\right]_+ > 0
```

The diagnostic ratio

```math
X_R(t)=\frac{W_g(t)}{R_n(t)+R_m(t)}
```

may be reported, but cannot establish sustainability alone. It omits lateral
flows, discharge capture, storage changes, ecological requirements, water
quality, and estimation uncertainty.

## 6. HKL Operationalization

Preserve the observations first. Then construct dimensionless burdens against
declared reference ranges:

```math
B_G=N_G(G_{ref}-G),\quad B_H=N_H(H_{ref}-H),\quad
B_C=N_C(C_{irr}),\quad B_E=N_E(E_{sw}),\quad B_T=N_T(T_{gap})
```

The freshwater HKL candidate is:

```math
V_W(t)=w_GB_G+w_HB_H+w_CB_C+w_EB_E+w_TB_T
```

Requirements:

- publish every normalization, weight, boundary, and time window;
- report unaggregated components beside `V_W`;
- test several defensible weight sets;
- do not let a favorable component erase a hard physical threshold; and
- call the result **Lyapunov-style** unless positivity, boundedness, and decline
  along actual dynamics are demonstrated.

The prospective test is whether interventions that reduce `V_W` also improve
held-out storage, head, subsidence, transition-gap, and ecological outcomes.

## 7. Aquifer Age

Do not assert that all extracted water is thousands or tens of thousands of
years old. Groundwater age is a spatial distribution, varies with depth and
flow path, and is not the same variable as recharge rate or storage renewal.

Age tracers should answer bounded questions:

- What fraction of sampled water is modern, premodern, or mixed?
- Which screened depths contain slow-renewing water?
- Does pumping increasingly recruit older or poorer-quality water?
- How does residence-time distribution compare with withdrawal and usable
  storage loss?

The core result should survive without an age estimate. Measured long-run
storage decline and irreversible compaction are sufficient stock evidence.

## 8. Transition Audit

Classify projects before counting capacity:

| Status | Counting rule |
|---|---|
| Existing | Operating, metered, and available in the test year |
| Contracted | Legally secured and funded, with a delivery date |
| Planned | Designed or budgeted but not secured |
| Aspirational | Named without enforceable capacity, funding, or schedule |

Only existing capacity enters current `S_alt,firm(t)`. Contracted capacity may
enter a dated scenario. Planned and aspirational capacity cannot close the
current transition gap.

Audit the entire portfolio: demand reduction, land-use change, leakage,
recycled water, stormwater capture, managed recharge, surface supply,
drinking-water and ecosystem floors, conveyance capacity, energy, treatment,
salinity, and displaced burdens.

Catchment capture is not new water at basin scale unless the counterfactual
destination is specified. Count only the increment retained after downstream
rights, environmental flows, evaporation, treatment loss, and climate
covariance are considered.

## 9. Building and Development Audit

The building question is a transition-readiness test, not the initial basin
proof. Select a reproducible sample of recent high-water or high-energy
developments and extract from plans, permits, and operating records:

- catchment area, rainfall series, and storage capacity;
- infiltration area and retained-recharge estimate;
- potable, process, irrigation, and cooling demand;
- rainwater, stormwater, graywater, condensate, and blowdown reuse;
- cooling architecture and water source;
- drain-water and other waste-heat recovery, including temperature grade and
  an actual heat sink;
- metering, commissioning, maintenance, and drought controls; and
- verified annual water and energy offsets.

Report:

```math
F_{water}=\frac{\text{verified onsite or recycled supply}}
{\text{total facility water demand}}
```

```math
F_{critical}=\frac{\text{verified drought-reliable supply}}
{\text{critical water demand}}
```

```math
F_{heat}=\frac{\text{usefully recovered waste heat}}
{\text{technically recoverable waste heat}}
```

A feature counts only when sized, funded, commissioned, maintained, and
measured. A sustainability narrative is not capacity.

## 10. Falsification and Weakening

The Temporal Mining interpretation is weakened or rejected if:

1. climate-normalized groundwater storage is not declining;
2. service stability does not depend materially on groundwater stock;
3. subsidence and permanent loss are absent or unrelated to pumping;
4. connected-water and ecological burdens do not rise or are fully accounted;
5. firm substitution and demand reduction close the transition gap before
   thresholds are crossed; or
6. a simpler water-budget model explains and predicts the observations as well
   as or better than the HKL operationalization.

HKL receives incremental support only if `V_W` adds predictive or diagnostic
value beyond its individual hydrologic variables.

## 11. Minimum Dataset

1. Annual groundwater-storage change.
2. Groundwater levels with well metadata.
3. Pumping estimates.
4. Natural and managed-recharge estimates.
5. Surface-water deliveries and climate covariates.
6. Annual and cumulative subsidence.
7. Permanent compaction or storage loss where available.
8. Demand or delivered-service series.
9. Transition projects with capacity, status, cost, and operating date.
10. Uncertainty and provenance for every series.

Age tracers, water quality, ecosystem flows, energy intensity, land use, crop
mix, and building permits are second-stage data.

## 12. Execution Bites

### Bite 1: Data dictionary and boundary

Select Central Valley and nested San Joaquin boundaries; fix the common time
interval; define hydrologic year, units, missing-data rules, and uncertainty;
map each variable to an authoritative source before transformation.

**Deliverable:** `freshwater_data_dictionary_v0.1.csv`

### Bite 2: Stock and subsidence reconstruction

Reproduce published storage-change estimates and align head, storage, pumping,
climate, and subsidence. **Deliverable:** observed-data report without HKL.

### Bite 3: Buffer-illusion test

Compare delivered service with depletion and irreversible damage; identify
intervals satisfying the signature; test spatial and temporal sensitivity.

### Bite 4: Transition-capacity audit

Classify projects, calculate current and dated transition gaps, and test drought
covariance and displaced burdens.

### Bite 5: HKL test

Pre-register normalization, weights, thresholds, and held-out periods. Compare
`V_W` with simpler baselines and report failure as clearly as success.

### Bite 6: Cross-scale extension

Audit buildings and replicate the basin test in the High Plains aquifer.

## 13. Initial Source Stack

- USGS Central Valley groundwater, subsidence, InSAR, GPS, extensometer, and
  model products.
- California DWR SGMA Data Viewer, basin water budgets, Bulletin 118, and
  groundwater-condition updates.
- USGS High Plains water-level and storage-change reports.
- EPA WaterSense at Work guidance for onsite alternative water sources.
- U.S. Department of Energy waste-heat recovery guidance.

Government estimates remain model outputs with uncertainty. Preserve version,
retrieval date, method, resolution, and revision history.

## 14. Immediate Decision

Proceed with **Bite 1**. Do not begin by choosing HKL weights or collecting
building anecdotes. Establish a source-controlled hydrologic data dictionary
and a boundary on which stock, flow, damage, and transition claims can be
independently checked.
