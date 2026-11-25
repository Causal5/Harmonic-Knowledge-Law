# Pre-registration: lag-justified Tulare DWR head-sign windows

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 27, 25 November 2026).** Not a publication to `main`. Written before signed differences were computed for these windows.

**TL;DR.** This test re-runs the Round 20 DWR Good-pair sign contrast for Tulare Lake 5-022.12, but only on comparison windows predeclared from the published recharge-lag findings checked in Round 25. The already-known Round 20 six-year fall hold and opposite-sign spring companion are **not** the decision. A sign flip in any determinate lag-justified window is a **break**. Sign only; no volume conversion; no Bite 5.

**Parents.** Protocol and dictionary as on `main` at `37522fc`. Published lag findings, as verified in Round 25: Izbicki et al. 2008 (Oro Grande Wash: 3 years to the water table at 117 m, then 1 year after wetting); Perzan et al. 2023 (Tulare Irrigation District orchard model: median saturated-zone recharge efficiency at 2 years). Zhou et al. 2023 (Modesto, tracer to 5 m over a days-to-weeks flood experiment) is recorded as too short to generate a multi-year fall survey window. Round 20 script, polygon, and DWR zip SHA-256 `d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d`.

## Locked windows (fall, to match the v0.2 fall storage surveys)

All windows use October–November, DWR Good quality, in-polygon 5-022.12 sites, unweighted median of paired depth-to-water differences (later minus earlier, feet). Same pairing rule as Round 20. \(n_G \ge 5\) required.

| Window | Dates | Published lag used as the predeclaration reason |
|---|---|---|
| W3 | Oct–Nov 2022 vs Oct–Nov 2025 | Oro Grande initial arrival (3 years) |
| W2 | Oct–Nov 2023 vs Oct–Nov 2025 | Tulare orchard-model median time to saturated-zone recharge (2 years) |
| W1 | Oct–Nov 2024 vs Oct–Nov 2025 | Oro Grande arrival after wetting (1 year) |

These site lags are not claimed to be Tulare Lake travel times. They are used only to predeclare comparison lengths before looking at the Tulare paired differences for those lengths. Kraemer Basin (consistent travel times on repeat tests) does not supply a new length; it is not used to pick a window.

## Pre-registered outcomes

For each locked window:

- **Holds** if \(n_G \ge 5\) and median \(\Delta\) DTW \(> 0\) (deeper later, same sign as the v0.2 fall storage loss).
- **Breaks** if \(n_G \ge 5\) and median \(\Delta\) DTW \(< 0\).
- **Indeterminate** if \(n_G < 5\) or the median is 0.

Round-level:

- **Holds** if every determinate locked window holds, and at least one window is determinate.
- **Breaks** if any determinate locked window breaks.
- **Indeterminate** if all three locked windows are indeterminate.

Cause, if the round breaks because a lag-justified fall window flips sign: **scope / window-dependence** (the sign is not stable across predeclared fall lengths), not a Layer 0 theory failure and not a volume confirmation. A window that cannot be filled is a data gap for that window only.

The Round 20 six-year fall result and the spring 2015–2024 companion may be cited only as already-published context, after the three locked windows are scored, and are not used to change those scores.

## What this test will not do

- Convert a sign to a volume, or score Bite 5 or \(V_W\).
- Treat Oro Grande, Kraemer, or Modesto travel times as Tulare Lake lags.
- Invent a well-weighting scheme or change the Good-quality and October–November pairing rule.
- Use A1–A8 as if defined.
