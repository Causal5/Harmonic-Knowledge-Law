#!/usr/bin/env python3
# Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 27).
# Sign-only lag-window contrasts. Protocol: ../PREREG.md, committed before these
# signed differences were computed.
"""DWR depth-to-water sign test for predeclared lag-justified fall windows."""
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
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
R20 = ROOT.parent / "2026-11-24-tulare-dwr-head-contrast"
PRIOR = ROOT.parent / "2026-11-21-tulare-lake-72019"
sys.path.insert(0, str(PRIOR / "scripts"))
from compute_tulare_lake_spring_dtw import in_subbasin, load_rings  # noqa: E402

SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "outputs"
EXPECTED_SHA256 = "d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d"

WINDOWS = {
    "fall_2022_octnov": ("2022-10-01", "2022-11-30"),
    "fall_2023_octnov": ("2023-10-01", "2023-11-30"),
    "fall_2024_octnov": ("2024-10-01", "2024-11-30"),
    "fall_2025_octnov": ("2025-10-01", "2025-11-30"),
}
CONTRASTS = {
    "W3_fall_2022_2025": ("fall_2022_octnov", "fall_2025_octnov"),
    "W2_fall_2023_2025": ("fall_2023_octnov", "fall_2025_octnov"),
    "W1_fall_2024_2025": ("fall_2024_octnov", "fall_2025_octnov"),
}
WANTED_YEARS = {"2022", "2023", "2024", "2025"}


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
            "n_deeper": 0,
            "n_shallower": 0,
            "n_zero": 0,
        }
    deltas = [p["delta_ft"] for p in pairs]
    return {
        "n": len(deltas),
        "median_delta_ft": median(deltas),
        "mean_delta_ft": statistics.fmean(deltas),
        "n_deeper": sum(d > 0 for d in deltas),
        "n_shallower": sum(d < 0 for d in deltas),
        "n_zero": sum(d == 0 for d in deltas),
    }


def decide(stats):
    n = stats["n"]
    d = stats["median_delta_ft"]
    if n < 5 or d == 0 or d is None:
        return "indeterminate", "data insufficient" if n < 5 else "median is zero"
    if d > 0:
        return "holds", "median depth to water increased"
    return "breaks", "median depth to water decreased"


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
            }
    return sites


def collect(bundle, sites):
    acc = {site: {w: [] for w in WINDOWS} for site in sites}
    for row in rows(bundle, "measurements.csv"):
        site = row["site_code"]
        if site not in sites:
            continue
        date = row["msmt_date"]
        if date[:4] not in WANTED_YEARS or not finite(row["gse_gwe"]):
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


def site_window_value(records):
    vals = [r["dtw_ft"] for r in records if r["quality"].lower() == "good"]
    return median(vals), len(vals)


def build_pairs(acc, sites, left, right):
    pairs = []
    for site, windows in acc.items():
        v0, n0 = site_window_value(windows[left])
        v1, n1 = site_window_value(windows[right])
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
            }
        )
    return pairs


def write_csv(path: Path, rows_, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path", nargs="?", default="/tmp/hkl-data/periodic_gwl_bulkdatadownload.zip")
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    _, polygons, bbox = load_rings()

    if args.offline:
        meas_path = OUTPUTS / "dwr_lag_window_measurements.csv"
        stations = list(csv.DictReader((SOURCES / "dwr_tulare_lake_stations.csv").open()))
        sites = {
            r["site_code"]: {
                "site_code": r["site_code"],
                "longitude": float(r["longitude"]),
                "latitude": float(r["latitude"]),
            }
            for r in stations
        }
        acc = {site: {w: [] for w in WINDOWS} for site in sites}
        for row in csv.DictReader(meas_path.open()):
            rec = {
                "date": row["date"],
                "dtw_ft": float(row["dtw_ft"]),
                "quality": row["quality"],
            }
            acc[row["site_code"]][row["window"]].append(rec)
        zip_sha = "offline"
    else:
        zip_path = Path(args.zip_path)
        zip_sha = sha256_file(zip_path)
        if zip_sha != EXPECTED_SHA256:
            raise SystemExit(f"unexpected zip sha256 {zip_sha}")
        with zipfile.ZipFile(zip_path) as bundle:
            sites = load_sites(bundle, polygons, bbox)
            acc = collect(bundle, sites)
        # persist extracts for offline replay
        SOURCES.mkdir(parents=True, exist_ok=True)
        write_csv(
            SOURCES / "dwr_tulare_lake_stations.csv",
            [
                {
                    "site_code": s["site_code"],
                    "longitude": s["longitude"],
                    "latitude": s["latitude"],
                }
                for s in sites.values()
            ],
            ["site_code", "longitude", "latitude"],
        )
        meas = []
        for site, windows in acc.items():
            for name, recs in windows.items():
                for r in recs:
                    meas.append(
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
        meas.sort(key=lambda r: (r["site_code"], r["window"], r["date"]))
        write_csv(
            OUTPUTS / "dwr_lag_window_measurements.csv",
            meas,
            ["site_code", "longitude", "latitude", "window", "date", "dtw_ft", "quality"],
        )

    summary = {
        "zip_sha256": zip_sha if not args.offline else EXPECTED_SHA256,
        "n_sites": len(sites),
        "windows": {},
    }
    all_pairs = []
    outcomes = []
    for name, (left, right) in CONTRASTS.items():
        pairs = build_pairs(acc, sites, left, right)
        stats = contrast_stats(pairs)
        outcome, reason = decide(stats)
        summary["windows"][name] = {
            "left": left,
            "right": right,
            **stats,
            "outcome": outcome,
            "reason": reason,
        }
        outcomes.append(outcome)
        for p in pairs:
            row = dict(p)
            row["contrast"] = name
            all_pairs.append(row)
        print(
            f"{name}: n={stats['n']} median={stats['median_delta_ft']} "
            f"deeper={stats['n_deeper']} shallower={stats['n_shallower']} => {outcome}"
        )

    determinate = [o for o in outcomes if o != "indeterminate"]
    if not determinate:
        round_outcome = "indeterminate"
    elif any(o == "breaks" for o in determinate):
        round_outcome = "breaks"
    else:
        round_outcome = "holds"
    summary["round_outcome"] = round_outcome
    print(f"round_outcome={round_outcome}")

    write_csv(
        OUTPUTS / "dwr_lag_window_pairs.csv",
        all_pairs,
        [
            "contrast",
            "site_code",
            "longitude",
            "latitude",
            "dtw_left_ft",
            "dtw_right_ft",
            "n_left",
            "n_right",
            "delta_ft",
        ],
    )
    (OUTPUTS / "dwr_lag_window_summary.json").write_text(json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
