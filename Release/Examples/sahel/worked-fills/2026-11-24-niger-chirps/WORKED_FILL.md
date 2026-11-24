# Worked fill: CHIRPS vs WDI Niger rainfall

> **Unpublished branch work (ai/evolution, Launch Pad Session 1, Round 21, 24 November 2026).** This path does not exist in `Release/` on `main` (`56c6ab5`). It is not a publication to `main`.

**TL;DR.** A CHIRPS v2.0 national-mean annual series for Niger, 1981–2022, has mean 142.88 mm, standard deviation 24.44 mm, and CV 0.171 (range 71.94 mm in 1984 to 190.45 mm in 1994; 41 distinct values at 0.1 mm). The committed WDI series is 151 mm in every year. The pre-registered test **holds**: WDI is not an interannual rainfall series. This national mean is not a site series, does not fill Sahel step 1, and was not used to construct \(V\) or restore withdrawn claims.

**Pre-registration:** [PREREG.md](PREREG.md), written before the CHIRPS national mean was computed.

## Decision

| Item | Value |
|---|---|
| Years | 1981–2022 (n=42) |
| Cells | 40,220 CHIRPS 0.05° centers inside the Natural Earth Niger polygon, all finite each year |
| CHIRPS mean / sd / CV | 142.88 mm / 24.44 mm / 0.171 |
| Range | 71.94 mm (1984) – 190.45 mm (1994) |
| WDI 1981–2022 | 151 mm every year |
| **Outcome** | **Holds** |
| Unassigned | \(V\), \(\dot V\), withdrawn Sahel completion claims, A1–A8, Bite 5 |

## Object class

| Quantity | Object class | Reporting mode |
|---|---|---|
| CHIRPS national mean | observation (spatial mean of a gridded product) | computed on the locked protocol |
| WDI AG.LND.PRCP.MM | observation / published indicator (repeated climatology) | already computed in Round 14 |

Replay: `python3 scripts/compute_niger_chirps_national_mean.py --offline`
