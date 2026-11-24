# Worked fill: DWR head-sign test, Tulare Lake 5-022.12

> **Unpublished branch work (ai/evolution, Launch Pad Session 1, Round 20, 24 November 2026).** This path does not exist in `Release/` on `main` (`56c6ab5464672a945c7832f03e969676c86d4a2b`). It is not a publication to `main`.

**TL;DR.** Under the pre-registered fall window, 15 qualifying Good-quality DWR *pairs* inside 5-022.12 have October–November measurements in both 2019 and 2025 (a subset of 687 in-polygon station records, unweighted, aquifer zone not locked). The median depth to water of those 15 pairs increased 19.03 feet (13 deeper, 2 shallower). That is the same direction as the v0.2 net storage loss, so the pre-registered sign test **holds**. It is not a spatially weighted subbasin head and not a confirmation of 468,635 acre-feet. A companion spring 2015–2024 contrast, which was not the decision, has the opposite sign. η, *severed*, buffer, \(V_W\), and Bite 5 were not assigned.

**Pre-registration:** [PREREG.md](PREREG.md) was written before signed paired differences were computed.

## Decision (primary test)

| Item | Value |
|---|---|
| Window | 1 October–30 November 2019 vs 2025 (declared convention) |
| Quality | DWR `Good` |
| \(n_G\) | 15 (threshold was 5) |
| Median \(\Delta\) DTW | +19.03 ft (deeper water / lower head in fall 2025) |
| Deeper / shallower / zero | 13 / 2 / 0 |
| Mean \(\Delta\) DTW | +19.29 ft (descriptive only; median is the decision statistic) |
| **Outcome** | **Holds** |
| Cause | Not applicable (did not break) |
| Unassigned | η, *severed*, official buffer, \(V_W\), Bite 5 |

This is a sign test only. It does not confirm the 468,635 acre-foot figure, does not convert feet to volume, and does not attribute the change to pumping.

## Sensitivities and companion (not the decision)

| Contrast | Good \(n\) | Good median \(\Delta\) ft | Direction |
|---|---:|---:|---|
| Sep–Nov 2019 vs 2025 | 18 | +18.77 | same as primary |
| Oct–Nov 2019 vs 2024 | 13 | +9.00 | same as primary |
| Spring 1 Mar–31 May 2015 vs 2024 | 11 | −42.97 | **opposite** (shallower water in spring 2024) |

The spring companion covers a different season and a different interval (late drought into a post-2023 wet period). Under the pre-registration it cannot be promoted into the decision. It does show that the **sign of a well-network contrast in this subbasin depends on the window**. That is reported, not used to change the locked rule.

## Object-class and computed-status notes

| Quantity | Object class | Reporting mode |
|---|---|---|
| Site-window median `gse_gwe` | observation | computed on the locked protocol |
| Median paired \(\Delta\) DTW | observation (network median) | computed on the locked protocol |
| v0.2 468,635 AF storage change | agent model / estimated storage change from the agencies | already published; not recomputed here |
| *severed*, η, buffer, \(V_W\), Bite 5 | — | unassigned / not implemented |

## Reproduction

```
python3 scripts/compute_tulare_dwr_head_contrast.py --offline
```

Or pass the DWR zip with SHA-256 `d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d`.

**Verifier revision (Round 20 [C]).** Short summaries must name the locked October–November 2019–2025 window, call the statistic a median of 15 qualifying Good pairs, and mention the opposite-sign spring 2015–2024 companion.
