#!/usr/bin/env python3
# Unpublished branch work (ai/evolution, Launch Pad Session 1, Round 21, 24 November 2026).
# This file does not exist in Release/ on main (56c6ab5464672a945c7832f03e969676c86d4a2b).
# It is not a publication to main.
"""CHIRPS v2.0 national-mean annual rainfall for Niger, 1981-2022.

LOCKED PROTOCOL: see ../PREREG.md, written before the CHIRPS national
mean was computed. Does not construct V, restore withdrawn Sahel claims,
or treat the national mean as a site series.

Usage:
  python3 compute_niger_chirps_national_mean.py --nc path/to/chirps_bbox.nc
  python3 compute_niger_chirps_national_mean.py --offline
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "outputs"
GEOJSON = SOURCES / "ne_50m_niger.geojson"
WDI = (
    ROOT.parent
    / "2026-11-21-niger-precip-wb"
    / "outputs"
    / "niger_AG.LND.PRCP.MM_1961-2022.csv"
)
CV_HOLDS = 0.05
CV_BREAKS = 0.01


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_niger():
    gj = json.loads(GEOJSON.read_text())
    from shapely.geometry import shape
    return shape(gj["features"][0]["geometry"])


def mask_centers(lats, lons, geom):
    import numpy as np
    from shapely.geometry import Point

    mask = np.zeros((len(lats), len(lons)), dtype=bool)
    for i, lat in enumerate(lats):
        for j, lon in enumerate(lons):
            if geom.contains(Point(float(lon), float(lat))):
                mask[i, j] = True
    return mask


def series_from_nc(nc_path: Path, geom):
    import numpy as np
    from netCDF4 import Dataset, num2date
    from shapely.geometry import Point

    with Dataset(nc_path) as ds:
        precip = ds.variables["precip"]
        fill = getattr(precip, "_FillValue", None)
        missing = getattr(precip, "missing_value", None)
        lats = np.array(ds.variables["latitude"][:], dtype=float)
        lons = np.array(ds.variables["longitude"][:], dtype=float)
        times = ds.variables["time"]
        years = [
            int(num2date(t, times.units, only_use_cftime_datetimes=False).year)
            for t in times[:]
        ]
        data = np.array(precip[:], dtype=float)  # (time, lat, lon)
    if fill is not None:
        data = np.where(data == float(fill), np.nan, data)
    if missing is not None:
        data = np.where(data == float(missing), np.nan, data)
    mask = mask_centers(lats, lons, geom)
    n_cells = int(mask.sum())
    out = []
    for yi, year in enumerate(years):
        slab = data[yi]
        vals = slab[mask]
        finite = vals[np.isfinite(vals)]
        out.append(
            {
                "year": year,
                "chirps_national_mean_mm": float(np.mean(finite)) if len(finite) else None,
                "n_cells_used": int(len(finite)),
                "n_cells_in_polygon": n_cells,
            }
        )
    return out, n_cells


def wdi_map():
    m = {}
    with WDI.open() as f:
        for row in csv.DictReader(f):
            m[int(row["year"])] = float(row["value_mm_per_year"])
    return m


def decide(means):
    vals = [r["chirps_national_mean_mm"] for r in means if r["chirps_national_mean_mm"] is not None]
    mean = statistics.fmean(vals)
    std = statistics.stdev(vals)
    cv = std / mean if mean else math.nan
    k = len({round(v, 1) for v in vals})
    if cv > CV_HOLDS or k > 2:
        outcome, reason = "holds", "CHIRPS national mean is interannual; WDI is not"
    elif cv <= CV_BREAKS and k <= 2:
        outcome, reason = "breaks", "CHIRPS is essentially as flat as WDI"
    else:
        outcome, reason = "indeterminate", "CV in the narrow band between 0.01 and 0.05 with k<=2"
    return {
        "n_years": len(vals),
        "mean_mm": mean,
        "std_mm": std,
        "cv": cv,
        "n_distinct_0.1mm": k,
        "min_mm": min(vals),
        "max_mm": max(vals),
        "outcome": outcome,
        "reason": reason,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--nc", type=Path)
    p.add_argument("--offline", action="store_true")
    args = p.parse_args()
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    wdi = wdi_map()
    if args.offline:
        rows = list(csv.DictReader((OUTPUTS / "niger_chirps_v2_national_mean_1981-2022.csv").open()))
        means = []
        for r in rows:
            means.append(
                {
                    "year": int(r["year"]),
                    "chirps_national_mean_mm": float(r["chirps_national_mean_mm"]),
                    "n_cells_used": int(r["n_cells_used"]),
                    "n_cells_in_polygon": int(r["n_cells_in_polygon"]),
                }
            )
        existing = OUTPUTS / "niger_chirps_national_mean_summary.json"
        if existing.exists():
            nc_sha = json.loads(existing.read_text()).get("source_nc_sha256", "offline")
            if nc_sha == "offline":
                nc_sha = "207ec71e966b9eb00bfa5b3d62d76053df5d7524be678b15120aa41cc56f338e"
        else:
            nc_sha = "207ec71e966b9eb00bfa5b3d62d76053df5d7524be678b15120aa41cc56f338e"
    else:
        if not args.nc:
            raise SystemExit("--nc or --offline is required")
        geom = load_niger()
        means, _ = series_from_nc(args.nc, geom)
        nc_sha = sha256_file(args.nc)

    for r in means:
        r["wdi_mm"] = wdi.get(r["year"])
        r["difference_mm"] = (
            None
            if r["chirps_national_mean_mm"] is None or r["wdi_mm"] is None
            else r["chirps_national_mean_mm"] - r["wdi_mm"]
        )

    decision = decide(means)
    fieldnames = [
        "year",
        "chirps_national_mean_mm",
        "wdi_mm",
        "difference_mm",
        "n_cells_used",
        "n_cells_in_polygon",
    ]
    with (OUTPUTS / "niger_chirps_v2_national_mean_1981-2022.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in means:
            w.writerow({k: r[k] for k in fieldnames})

    summary = {
        "protocol": "PREREG.md",
        "product": "CHIRPS v2.0 annual, 0.05°, mm/year, 1981-2022",
        "erddap_dataset": "chirps20GlobalAnnualP05",
        "polygon": "sources/ne_50m_niger.geojson (Natural Earth Admin 0 50m, version 5.1.1, ADMIN=Niger, ISO_A3=NER)",
        "source_nc_sha256": nc_sha,
        "geojson_sha256": sha256_file(GEOJSON),
        "decision": decision,
        "assigned": "none; V, withdrawn Sahel claims, and A1-A8 remain unused",
    }
    (OUTPUTS / "niger_chirps_national_mean_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(decision, indent=2))


if __name__ == "__main__":
    main()
