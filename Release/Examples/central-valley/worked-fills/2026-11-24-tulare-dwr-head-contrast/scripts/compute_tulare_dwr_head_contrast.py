#!/usr/bin/env python3
# Unpublished branch work (ai/evolution, Launch Pad Session 1, Round 20, 24 November 2026).
# This file does not exist in Release/ on main (56c6ab5464672a945c7832f03e969676c86d4a2b).
# It is not a publication to main. Release/ on main is the authoritative current source.
"""DWR depth-to-water sign test for Tulare Lake 5-022.12.

LOCKED PROTOCOL: see ../PREREG.md, written before signed differences
were computed. Decision statistic: median Good-quality paired
(Oct-Nov 2025 minus Oct-Nov 2019) depth to water, in feet, for
in-polygon sites with n_G >= 5. Does not score Bite 5, V_W, eta,
severed, or buffer.

Usage:
  python3 compute_tulare_dwr_head_contrast.py /path/to/periodic_gwl_bulkdatadownload.zip
  python3 compute_tulare_dwr_head_contrast.py --offline
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import statistics
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PRIOR = ROOT.parent / "2026-11-21-tulare-lake-72019"
sys.path.insert(0, str(PRIOR / "scripts"))
from compute_tulare_lake_spring_dtw import in_subbasin, load_rings  # noqa: E402

SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "outputs"
GEOJSON = PRIOR / "sources" / "b118_5-022.12_tulare_lake.geojson"
EXPECTED_SHA256 = "d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d"

WINDOWS = {
    "fall_2019_octnov": ("2019-10-01", "2019-11-30"),
    "fall_2025_octnov": ("2025-10-01", "2025-11-30"),
    "fall_2024_octnov": ("2024-10-01", "2024-11-30"),
    "fall_2019_sepnov": ("2019-09-01", "2019-11-30"),
    "fall_2025_sepnov": ("2025-09-01", "2025-11-30"),
    "spring_2015": ("2015-03-01", "2015-05-31"),
    "spring_2024": ("2024-03-01", "2024-05-31"),
}

CONTRASTS = {
    "primary_fall_octnov_2019_2025": ("fall_2019_octnov", "fall_2025_octnov"),
    "sensitivity_fall_sepnov_2019_2025": ("fall_2019_sepnov", "fall_2025_sepnov"),
    "sensitivity_fall_octnov_2019_2024": ("fall_2019_octnov", "fall_2024_octnov"),
    "companion_spring_2015_2024": ("spring_2015", "spring_2024"),
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def finite(value):
    try:
        return math.isfinite(float(value))
    except (ValueError, TypeError):
        return False


def in_window(date: str, start: str, end: str) -> bool:
    return len(date) >= 10 and start <= date[:10] <= end


def rows(bundle, filename):
    with bundle.open(filename) as raw, io.TextIOWrapper(
        raw, encoding="utf-8-sig", newline=""
    ) as stream:
        yield from csv.DictReader(stream)


def median(values):
    return statistics.median(values) if values else None


def contrast_stats(pairs):
    if not pairs:
        return {
            "n": 0,
            "median_delta_ft": None,
            "mean_delta_ft": None,
            "p25_delta_ft": None,
            "p75_delta_ft": None,
            "n_deeper": 0,
            "n_shallower": 0,
            "n_zero": 0,
        }
    deltas = [p["delta_ft"] for p in pairs]
    deltas_sorted = sorted(deltas)
    n = len(deltas)

    def pct(p):
        # inclusive rank, same convention as a simple nearest-rank
        i = min(n - 1, max(0, math.ceil(p / 100.0 * n) - 1))
        return deltas_sorted[i]

    return {
        "n": n,
        "median_delta_ft": median(deltas),
        "mean_delta_ft": statistics.fmean(deltas),
        "p25_delta_ft": pct(25),
        "p75_delta_ft": pct(75),
        "n_deeper": sum(d > 0 for d in deltas),
        "n_shallower": sum(d < 0 for d in deltas),
        "n_zero": sum(d == 0 for d in deltas),
    }


def decide_primary(good_stats):
    n = good_stats["n"]
    d = good_stats["median_delta_ft"]
    if n < 5 or d == 0 or d is None:
        return "indeterminate", "data insufficient" if n < 5 else "median is zero"
    if d > 0:
        return "holds", "median depth to water increased (same direction as published net storage loss)"
    return "breaks", "median depth to water decreased (opposite direction to published net storage loss)"


def load_sites(bundle, polygons, bbox):
    west, south, east, north = bbox
    sites = {}
    for row in rows(bundle, "stations.csv"):
        if not (finite(row["longitude"]) and finite(row["latitude"])):
            continue
        x, y = float(row["longitude"]), float(row["latitude"])
        if west <= x <= east and south <= y <= north and in_subbasin(x, y, polygons):
            sites[row["site_code"]] = {
                "site_code": row["site_code"],
                "longitude": x,
                "latitude": y,
                "well_use": row.get("well_use", ""),
                "well_type": row.get("well_type", ""),
                "wcr_no": row.get("wcr_no", ""),
            }
    return sites


def collect(bundle, sites):
    # site -> window -> list of {date, dtw, quality}
    acc = {site: {w: [] for w in WINDOWS} for site in sites}
    wanted_years = {"2015", "2019", "2024", "2025"}
    for row in rows(bundle, "measurements.csv"):
        site = row["site_code"]
        if site not in sites:
            continue
        date = row["msmt_date"]
        if date[:4] not in wanted_years or not finite(row["gse_gwe"]):
            continue
        rec = {
            "date": date[:10],
            "dtw_ft": float(row["gse_gwe"]),
            "quality": (row.get("wlm_qa_desc") or "").strip(),
        }
        for name, (start, end) in WINDOWS.items():
            if in_window(date, start, end):
                acc[site][name].append(rec)
    return acc


def site_window_value(records, good_only):
    vals = [
        r["dtw_ft"]
        for r in records
        if (not good_only or r["quality"].lower() == "good")
    ]
    return median(vals), len(vals)


def build_pairs(acc, sites, left, right, good_only):
    pairs = []
    for site, windows in acc.items():
        v0, n0 = site_window_value(windows[left], good_only)
        v1, n1 = site_window_value(windows[right], good_only)
        if v0 is None or v1 is None:
            continue
        pairs.append(
            {
                "site_code": site,
                "longitude": sites[site]["longitude"],
                "latitude": sites[site]["latitude"],
                "dtw_left_ft": v0,
                "dtw_right_ft": v1,
                "n_left": n0,
                "n_right": n1,
                "delta_ft": v1 - v0,
                "quality_rule": "good" if good_only else "numeric",
            }
        )
    return pairs


def write_csv(path: Path, rows_, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_)


def extract_measurements(acc, sites):
    out = []
    for site, windows in acc.items():
        seen = set()
        for name, recs in windows.items():
            for r in recs:
                key = (site, r["date"], r["dtw_ft"], r["quality"], name)
                if key in seen:
                    continue
                seen.add(key)
                out.append(
                    {
                        "site_code": site,
                        "longitude": sites[site]["longitude"],
                        "latitude": sites[site]["latitude"],
                        "window": name,
                        "date": r["date"],
                        "dtw_ft": r["dtw_ft"],
                        "quality": r["quality"],
                    }
                )
    out.sort(key=lambda r: (r["site_code"], r["window"], r["date"]))
    return out


def run(zip_path: Path, offline: bool):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    SOURCES.mkdir(parents=True, exist_ok=True)
    # Point load_rings at the prior geojson by temporarily matching its expected path.
    # load_rings reads SOURCES relative to the imported module (PRIOR/sources).
    _, polygons, bbox = load_rings()

    if offline:
        stations = list(csv.DictReader((SOURCES / "dwr_tulare_lake_stations.csv").open()))
        sites = {r["site_code"]: {
            "site_code": r["site_code"],
            "longitude": float(r["longitude"]),
            "latitude": float(r["latitude"]),
            "well_use": r.get("well_use", ""),
            "well_type": r.get("well_type", ""),
        } for r in stations}
        acc = {site: {w: [] for w in WINDOWS} for site in sites}
        with (OUTPUTS / "dwr_tulare_lake_window_measurements.csv").open() as f:
            for row in csv.DictReader(f):
                acc[row["site_code"]][row["window"]].append(
                    {
                        "date": row["date"],
                        "dtw_ft": float(row["dtw_ft"]),
                        "quality": row["quality"],
                    }
                )
        zip_sha = "offline"
    else:
        zip_sha = sha256_file(zip_path)
        if zip_sha != EXPECTED_SHA256:
            print(
                f"WARNING: zip SHA-256 {zip_sha} != locked {EXPECTED_SHA256}",
                file=sys.stderr,
            )
        with zipfile.ZipFile(zip_path) as bundle:
            sites = load_sites(bundle, polygons, bbox)
            acc = collect(bundle, sites)
        station_rows = [
            {
                "site_code": s["site_code"],
                "longitude": s["longitude"],
                "latitude": s["latitude"],
                "well_use": s["well_use"],
                "well_type": s["well_type"],
            }
            for s in sites.values()
        ]
        write_csv(
            SOURCES / "dwr_tulare_lake_stations.csv",
            station_rows,
            ["site_code", "longitude", "latitude", "well_use", "well_type"],
        )
        write_csv(
            OUTPUTS / "dwr_tulare_lake_window_measurements.csv",
            extract_measurements(acc, sites),
            ["site_code", "longitude", "latitude", "window", "date", "dtw_ft", "quality"],
        )

    summary = {
        "protocol": "PREREG.md",
        "boundary": "DWR Bulletin 118 5-022.12",
        "geojson": "../2026-11-21-tulare-lake-72019/sources/b118_5-022.12_tulare_lake.geojson",
        "source_zip_sha256": zip_sha,
        "n_in_polygon_stations": len(sites),
        "unit": "feet, depth to water (gse_gwe); positive delta = deeper water / lower head",
        "contrasts": {},
        "decision": {},
    }

    pair_fields = [
        "contrast",
        "quality_rule",
        "site_code",
        "longitude",
        "latitude",
        "dtw_left_ft",
        "dtw_right_ft",
        "n_left",
        "n_right",
        "delta_ft",
    ]
    all_pairs = []
    for cname, (left, right) in CONTRASTS.items():
        block = {"left_window": left, "right_window": right, "quality": {}}
        for good_only, label in ((True, "good"), (False, "numeric")):
            pairs = build_pairs(acc, sites, left, right, good_only)
            for p in pairs:
                row = {"contrast": cname, **p}
                all_pairs.append(row)
            stats = contrast_stats(pairs)
            block["quality"][label] = stats
        summary["contrasts"][cname] = block

    primary = summary["contrasts"]["primary_fall_octnov_2019_2025"]["quality"]["good"]
    outcome, reason = decide_primary(primary)
    summary["decision"] = {
        "test": "primary_fall_octnov_2019_2025, Good quality",
        "outcome": outcome,
        "reason": reason,
        "n_G": primary["n"],
        "median_delta_ft": primary["median_delta_ft"],
        "cause_if_breaks": (
            "scope / data-limit unless aquifer zone is locked; not a Layer 0 theory failure"
            if outcome == "breaks"
            else None
        ),
        "assigned_flags": "none; eta, severed, buffer, V_W, and Bite 5 remain unassigned",
    }

    write_csv(OUTPUTS / "dwr_tulare_lake_paired_contrasts.csv", all_pairs, pair_fields)
    (OUTPUTS / "dwr_tulare_lake_head_contrast_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    print(json.dumps(summary["decision"], indent=2))
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path", nargs="?", type=Path)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    if not args.offline and not args.zip_path:
        parser.error("zip path or --offline is required")
    run(args.zip_path, args.offline)


if __name__ == "__main__":
    main()
