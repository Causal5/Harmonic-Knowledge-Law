# Freshwater and Buffer definition crosswalk — Registry v0.3.1

**Status:** Current interpretation of the preserved working sources,
16 October 2026. This document corrects definitions; it does not revalidate
the source measurements or execute the study.

Read the [current registry](../../Registry/causal-ethics-master-symbol-registry.md)
and [HKL](../../HKL/hkl-lyapunov.md) with the
[v0.2 working protocol](temporal-mining-freshwater-protocol-v0.2.md).
The original [v0.1 example](central-valley-worked-example-v0.1.md),
[v0.1 protocol](temporal-mining-freshwater-protocol-v0.1.md), and
[Buffer manuscript](../../Working/buffer-as-temporal-dimension.md) remain
unchanged source records.

## Source-to-current mapping

| Source usage | Current meaning or correction |
|---|---|
| Bare $G$ | $G_W$ for recoverable groundwater stock; $G_i$ remains representational substrate |
| $G$ in the example's storage-loss table | A change/loss relative to a historical reference, not an absolute recoverable stock |
| $H,\ D,\ D_{critical},\ S_{alt,firm}$ | Domain-scoped $H_W,\ D_W,\ D_{W,crit},\ Q_{alt,firm}$ |
| $B_G=N_G(G_{ref}-G)$ | Separate raw nonnegative burden $B_{G,W}=[G_{ref}-G_W]_+$ from normalized $\beta_{G,W}$ |
| Groundwater age used for $\tau_s$ | Age is $\tau_{age}$; infer renewal/recovery $\tau_s$ using a separate physical model |
| $G/W_g$ called time to exhaustion | $\tau_{draw}$, a gross draw timescale |
| Net time to depletion | Requires current usable stock above $G_{min}$ and net loss after recharge and other flows |
| Bare $\rho$ | $\rho_{TM}=\tau_s/\tau_d$; distinguish from a reachability proxy |
| Buffer numerator $V^*-V$ | Use the exit margin $V_{max}-V$ |
| Declining burden gives negative buffer/recovery | Recovery and first-exit time are separate positive-time questions |
| Single $J_{PAE}$ for correction and export | Use separate resource/energy transport and burden-transfer quantities |

## Physical balance

With non-overlapping flow definitions and common boundary/time support:

$$
\dot G_W=R_n+R_m-W_g+Q_{net}.
$$

$Q_{net}$ includes signed lateral and connected-water exchanges not already
counted in recharge or withdrawal. An inferred pumping residual therefore is
$\widehat W_g=\widehat R_n+\widehat R_m+\widehat Q_{net}-\widehat{\dot G}_W$.
Omitting $Q_{net}$ requires evidence that it is negligible or separately
accounted for. Preserve uncertainty and dependence among model-derived inputs.

For positive denominators and usable stock above the declared floor:

$$
\tau_{draw}=G_W/W_g,\qquad
\widehat\tau_d^{net}=(G_W-G_{min})/(-\dot G_W).
$$

The second is a local linear approximation, not a forecast under changing
recharge or pumping. A cumulative storage-loss estimate alone supplies
neither the absolute recoverable stock nor its operational floor.

## Buffer and projections

First-exit time requires a scenario and a threshold. A report projecting a
percentage loss by 2043 is not automatically an estimate of the first time
a declared service or viability threshold is crossed. Define the threshold,
trajectory, start time, and uncertainty before making that translation.

For a positive scalar viability margin closing at a positive local rate:

$$
\widehat\tau^{lin}_{buf}
=\frac{V_{max}-V}{\dot V-\dot V_{max}}.
$$

Finite observed no-exit time is censored. Declining burden at present does
not prove that future exit is impossible. A weighted mean of patch buffers
does not establish that all critical patches remain viable.

## Transport distinction

Sending resources toward a low-buffer patch is different from transferring
burden out of another patch. Toward decreasing buffer is down the buffer
gradient, so the old up-gradient wording reverses that sign.
This geometric fact alone does not determine whether the transfer is
beneficial, whether correction succeeds, or whether burden is externalized.
Measure the transported quantity and its recipient effects separately.
Buffer time is derived from dynamics and thresholds, not a generally
conserved substance flowing between patches.

## Next empirical step

Build a common-boundary data dictionary for stocks, flows, floors, service,
and compaction. Preserve the original observations and uncertainty before
selecting normalizations, weights, or a Temporal Mining timescale ratio.
