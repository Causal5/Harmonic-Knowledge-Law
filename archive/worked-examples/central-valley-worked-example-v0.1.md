# Central Valley Freshwater — Working Example v0.1

**Status:** Bite 2 deliverable — observed-data report without HKL, per Temporal Mining Freshwater Study Protocol v0.1, §14
**Case:** California Central Valley, San Joaquin Valley subbasin focus
**Cross-references:** Temporal Mining Freshwater Study Protocol v0.1, Buffer as Temporal Dimension, Fallacy of Large-Scale Absorbic Effort, Continuation Filter

---

## 1. Purpose

This document reconstructs observed hydrologic and infrastructural data for the Central Valley per Bite 1–2 of the Temporal Mining protocol. It does **not** compute `V_W`, assign weights, or declare an HKL stability score. Per protocol §14: "Do not begin by choosing HKL weights or collecting building anecdotes." This is the sourced data layer the framework would later score, not the score itself.

---

## 2. Observed Time Series (Sourced)

| Variable | Value | Source | Notes |
|---|---|---|---|
| `G` (storage loss, pre-development → 2019) | ~158 km³ | USGS CVHM2 (Nelson, Quinn, Traum; published Apr 2024) | Central Valley Hydrologic Model v2, integrated surface-subsurface model |
| `C_irr` (permanent/irreversible loss share) | ~15% of total storage loss | Same, USGS CVHM2 | Permanent loss attributed to subsidence-driven compaction, infrastructure-damaging |
| `T_gap` indicator — current delivery restriction | 3% reduction in State Water Project deliveries | CA DWR technical report, addendum to 2024 Delivery Capability Report, published May 2025 | Attributed to subsidence reducing canal freeboard/flow capacity |
| `T_gap` indicator — projected, no-action trajectory | up to 87% reduction in SWP deliveries by 2043 | Same DWR report | Combines subsidence trajectory + climate change; explicitly conditional on "if no action is taken" |
| Independent subsidence replication | 2006–2022 Valley-wide subsidence matched the entire cumulative 20th-century total | Lees & Knight, *Communications Earth & Environment* (2024), remote-sensing/InSAR based | Independent of USGS CVHM2 model chain — separate methodology, convergent result |

---

## 3. Qualitative Buffer-Financed Stability Signature

USGS documents four repeating episodes where the protocol's §5 signature pattern appears in the historical record:

| Period | Trigger | Observed Pattern |
|---|---|---|
| 1976–77 | Reduced surface-water availability | Pumping increase → water levels to/beyond historic lows → renewed compaction |
| 1986–92 | Same | Same |
| 2007–09 | Same | Same |
| 2012–2015 | Same | Same |

Each episode qualitatively matches: `|dD/dt| ≤ ε_D` (delivered service held approximately stable) while `dG/dt < 0` and `dC_irr/dt > 0` concurrently. This is **qualitative pattern-matching against the historical record**, not the regression test Bite 3 calls for. A formal test requires aligning annual `D(t)`, `G(t)`, and `C_irr(t)` series across these windows — not yet done here.

---

## 4. Descriptive Cross-Corpus Mapping (Non-Computational)

This section notes conceptual correspondence only. No numeric HKL/AEF/buffer quantity is computed or asserted here.

- **Continuation Filter §V (Precursor Signals):** "shrinking shock buffers" and "growing concentration of... load" are descriptively consistent with the DWR delivery-restriction trajectory (3% → 87%) and the CVHM2 storage-loss trend.
- **Fallacy of Large-Scale Absorbic Effort — Invalid Smoothing Operator:** delivered service holding roughly stable while stock depletes and permanent damage accrues is structurally the pattern the addendum describes — apparent equilibrium sustained by drawing down a buffer rather than genuine absorption.
- **Buffer formalism, §4 (`τ_buffer`):** the 2043 projection is, informally, a stated institutional estimate of *time-to-basin-exit under current trajectory* — the DWR report is effectively supplying an independent, real-world `τ_buffer` estimate for this patch, arrived at without reference to this framework. Worth treating as an external check once `τ_buffer` is formally computed from the `G(t)` series, not as confirmation on its own.
- **SGMA's Groundwater Sustainability Agencies as a natural experiment:** SGMA implements *decentralized* agencies operating under a *shared centralized* state mandate — this is a real, ongoing, checkable instance of the centralized-vs-distributed correction question the Continuation Filter and Fallacy paper pose theoretically. Different subbasins' GSAs have set different sustainable-yield determinations under the same law. That variation is itself a dataset: it should be possible to compare subbasins with more locally-responsive GSA governance against subbasins with more centralized/uniform management, and check whether `G(t)` and `C_irr(t)` trajectories differ. Not attempted here — flagged as a strong candidate for Bite 5.

---

## 5. Open Item Carried Forward: Baseline Admissibility

Per prior discussion: a regulatory sustainable-yield figure (`G_ref` under SGMA) is a political/institutional determination, not a direct physical measurement, and is therefore vulnerable to being set favorably by interested parties. Before any `V_W` is computed:

- Pull SGMA subbasin-level sustainable-yield determinations from DWR's SGMA Data Viewer as **one candidate baseline**.
- Treat CVHM2's physical pre-development storage estimate as a **second, independent candidate baseline**.
- Report both. Do not collapse them into a single `G_ref` until the divergence (if any) between regulatory and physical baselines is itself reported as a finding.
- Per the added Falsification condition (protocol §10, extended): if `G_ref` tracks legislative/institutional change independent of hydrologic evidence, the baseline is inadmissible as stated and must be replaced or paired with a physically-anchored alternative.

---

## 6. Substrate Coupling Ratio (ρ = τ_s/τ_d): Real Data Path, Not Yet Computed

The original corpus already defines the needed metric — `ρ = τ_s / τ_d`, the Substrate Coupling Ratio, with the stated principle that deep aquifer pumping is temporal mining from a reservoir whose recharge occurs outside civilizational time. This section identifies the real data source for `τ_s` and flags why `ρ` must be a field, not a scalar, per the Cellular Constitution Principle (Buffer doc §2).

### 6.1 τ_s is not a single constant — it is depth- and location-resolved

Isotope age-dating of Central Valley groundwater (¹⁴C, ³H, noble gases, SF₆, CFCs) finds a mixed-age system: some sampled water is genuinely fossil (>12,000 years, pre-Holocene), some is post-1950s modern water, varying by depth and location across the basin. This is not an approximation gap to be averaged away — it is the physical structure of the resource. A shallow well and a deep well nearby can have `τ_s` differing by orders of magnitude.

**Real data source:** USGS has published a "Central Valley Aquifer Age Dating" web tool and an associated 4D model (depth of post-1950s water, `D-1950`) built from tracer data at 650 wells across the valley (Jasechko et al. methodology; USGS data releases, 2022). This is the real `τ_s(x)` source. It has not yet been pulled into this document — flagged as the next data-acquisition task, not yet executed here.

### 6.2 τ_d requires local pumping-depth records at matched well locations

To compute `ρ(x) = τ_s(x) / τ_d(x)` at a given patch, extraction depth and rate at that same location must be matched to the age-dated well. DWR/SGMA well-completion reports and CVHM2's pumping-layer data are the candidate sources. Not yet pulled or matched here.

**τ_d as inferred residual, not disclosed measurement.** Actor-level extraction data (agricultural, municipal, and increasingly data-center withdrawal) is not fully or granularly disclosed. `τ_d` therefore cannot be built from summed disclosed withdrawals.

**Correction (v0.2): the first-pass derivation here incorrectly routed through the abstract HKL/Buffer burden-rate symbols (`ρ_deplete`, `ρ_regen`) and got the sign backwards relative to Buffer doc §4.3 (`V̇ = ρ_deplete − ρ_regen`, not `ρ_deplete − ρ_regen = V̇`). It also conflated `V` (burden, increases when the system worsens) with `G` (storage, decreases when the system worsens) without the required `B_G = N_G(G_ref − G)` translation (Temporal Mining protocol §6). Corrected derivation below stays entirely in the protocol's own physical stock-flow variables (real volume/time units) until the final step, avoiding both errors:**

By water balance, using the protocol's own §4 variables:

```
dG(x,t)/dt = R_n(x,t) + R_m(x,t) − W_g(x,t)
```

`R_n` (natural recharge) and `R_m` (managed recharge) are independently estimable (§ managed + natural recharge figures, this document). `dG/dt` is independently observable (GRACE gravimetry, CVHM2 model output). Rearranged, this gives gross withdrawal as an inferred residual — in real volume/time units, no abstract burden layer involved:

```
W_g(x,t) ≈ R_n(x,t) + R_m(x,t) − dG(x,t)/dt
```

Then, following the same structural form as the Buffer document's own `τ_buffer` (§4.1: current deficit divided by current rate), the depletion timescale is:

```
τ_d(x,t) ≈ G(x,t) / W_g(x,t)
```

— time-to-exhaustion of current recoverable storage at the current inferred withdrawal rate. Only at this final step does the physical layer connect to the corpus's abstract formalism: `τ_d(x,t)` feeds directly into `ρ(x,t) = τ_s(x) / τ_d(x,t)` (§6, dimensionless) and, separately, `B_G = N_G(G_ref − G)` (protocol §6) is where `G` enters the abstract HKL burden layer, if and when that layer is computed. This keeps physical inference and abstract burden accounting from being conflated, per the namespace separation both source documents already require.

Same epistemic status as before: this is a disciplined inference (analogous to epidemiological R_eff, inferred from observable downstream data via a stated method) with explicit uncertainty, not a measurement.

**Explicit remaining limitation:** this residual method recovers *aggregate* withdrawal only. It cannot isolate the data-center-specific marginal contribution to `W_g` from the agricultural or municipal share. Attributing composition within the residual still requires disclosure that does not currently exist. This is a distinct, unresolved open problem — not something the residual method solves by implication.

### 6.3 The data-center water draw is two mechanisms, not one, and they are not independent

Direct on-site cooling water is the first draw. The second — electricity generation to power the facility — is not merely additive; globally, indirect water consumed at power plants generating electricity for data centers has been larger than direct on-site cooling water (IEA: ~373 billion liters indirect vs. ~140 billion liters direct, 2023 figures, all data centers). Two further points sharpen this beyond simple "double-dipping":

- **Correlated failure, not independent draws.** Both draws are likely to tighten simultaneously during drought: aquifer stress peaks, hydroelectric generation (a real component of the California grid) tends to fall with low reservoir levels, and thermoelectric plants elsewhere in the grid face their own cooling-water constraints — pushing more load onto whatever generation remains available at the exact moment local water stress is also highest. This is a correlated risk structure, not two independent burden terms that happen to sum.
- **Jurisdictional mismatch.** The local draw hits the Central Valley basin directly. The grid-electricity draw may hit water resources in a different watershed entirely, depending on where the marginal generation comes from — meaning the total footprint of one facility can span basins with no shared governance, complicating any single-basin `V(x,t)` accounting. Not yet resolved here; flagged as a structural accounting gap.

### 6.4 τ_s(x) is also governed by land-surface hydrology, not infiltration area alone

Naive recharge estimates that treat "surface area exposed to water" as equivalent to "water absorbed" ignore soil composition, slope, horizontal (lateral) flow to connected streams, and land-management history. Two concrete, sourced factors relevant to this basin:

- **Loss of natural flow-retention infrastructure.** California's Department of Fish and Wildlife formally recognizes beavers as a "keystone species" and "ecosystem-restoration tool" specifically for their role in increasing groundwater recharge and extending seasonal flows, and has run an active Beaver Restoration Program (first reintroduction, Plumas County, 2023, after ~75 years of absence) explicitly for this function. The historical removal of this flow-retention mechanism across the state is a real, documented, named factor in reduced infiltration — not a rhetorical aside.
- **Modern storm infrastructure moves water off-territory rather than retaining it.** Conventional storm-drain design is built to remove water quickly rather than retain it for infiltration, concentrating discharge elsewhere. This is a real, land-use-driven modifier on `τ_s(x)` distinct from the underlying geology, and is a planning-era effect layered on top of natural variation.

**Net effect on this section:** `τ_s(x)` should be understood as jointly determined by (a) deep geologic/isotopic age structure (§6.1) and (b) land-surface retention infrastructure, historical and current (§6.4). Neither is fully captured by the USGS age-dating tool alone; (b) would require a separate topographical/land-use data layer not yet identified here.

---

## 7. What This Document Does Not Do

- Does not compute `V_W`, `B_G`, `B_H`, `B_C`, `B_E`, `B_T`, or any weight `w_k`.
- Does not compute `τ_buffer`, `ρ_regen`, `ρ_deplete`, `κ_coord`, or `Ω_var` numerically.
- Does not assert HKL, AEF, or the Continuation Filter are validated by this case. Per protocol §1: this tests whether those constructs describe a known system, not the reverse.
- Does not select a final `G_ref`. Two candidate baselines are named; neither is adopted.

---

## 8. Next Concrete Steps

1. Pull DWR SGMA Data Viewer subbasin-level sustainable-yield determinations for San Joaquin Valley subbasins, alongside CVHM2's subbasin-resolved storage estimates, to execute the baseline-divergence check in §5 before any Bite 5 HKL test is attempted.
2. Pull USGS Central Valley Aquifer Age Dating tool output for a small initial set of well locations to obtain real `τ_s(x)` values (§6.1).
3. Match those wells against DWR/SGMA pumping-depth and rate records to obtain `τ_d(x)` at the same locations, and compute the first real, non-illustrative `ρ(x)` values for this corpus (§6.2).
4. Identify a topographical/land-use data source (soil permeability, slope, storm-infrastructure coverage) to address the §6.4 gap — not yet identified.
5. Verify the primary methodology of the NASA "~4 million acre-feet/year" seepage estimate directly (does it net out lateral flow to connected streams, or treat fall-area as absorbed) before citing it as a recharge figure in any computed section.
