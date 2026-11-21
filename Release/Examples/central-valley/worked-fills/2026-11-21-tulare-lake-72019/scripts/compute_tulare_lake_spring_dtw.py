#!/usr/bin/env python3
"""Spring depth-to-water change in Bulletin 118 Tulare Lake Subbasin (5-022.12).

LOCKED PROTOCOL (declared before values are aggregated):
  Spatial unit: DWR Bulletin 118 subbasin
    Basin_Subbasin_Number = 5-022.12
    Basin_Subbasin_Name = SAN JOAQUIN VALLEY - TULARE LAKE
    Source: DWR ArcGIS FeatureServer
      Geoscientific/i08_B118_CA_GroundwaterBasins
      https://gis.water.ca.gov/arcgis/rest/services/Geoscientific/i08_B118_CA_GroundwaterBasins/FeatureServer/0
    This is a declared official published unit for this fill. It is not
    a claim that 5-022.12 is "the" official Central Valley or San Joaquin
    Valley study boundary for Bite 5 / V_W.

  Parameter: USGS 72019 (depth to water level). Unit as reported
    (expected ft, depth below land surface). Other groundwater parameters
    are not substituted if 72019 is sparse.

  Windows: spring 2015 and spring 2024, each defined as
    1 March through 31 May of that calendar year, inclusive.
    This spring window is a declared convention for this fill.
    A DWR or USGS official "spring measurement" definition was not
    independently retrieved and is not cited.

  Inclusion: a monitoring location is included if and only if
    (a) its reported coordinates fall inside the official 5-022.12
        polygon (outer rings, excluding holes), and
    (b) it has at least one numeric 72019 field measurement in EACH
        spring window.
    If a well has several measurements in one window, the well-window
    value is the median of that window's numeric values.
    No well is dropped after seeing the sign of its change.

  Statistic: n qualifying wells; mean and median of
    (spring 2024 DTW minus spring 2015 DTW). A positive change means
    a greater depth to water (a lower water level) in spring 2024.
    Also count wells with positive, negative, and zero change.
    Report units and approval/qualifier counts. Do not invent missing
    values. Do not score V_W or Bite 5. Do not choose weights.

  Measurement source: USGS Water Data OGC API v0 field-measurements
    https://api.waterdata.usgs.gov/ogcapi/v0/collections/field-measurements

Usage:
  python3 compute_tulare_lake_spring_dtw.py [--offline]
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

PARAM = "72019"
SPRING_2015 = (date(2015, 3, 1), date(2015, 5, 31))
SPRING_2024 = (date(2024, 3, 1), date(2024, 5, 31))
# fetch a little extra at the end in case the API treats the end as exclusive
FETCH_START = "2015-03-01"
FETCH_END = "2024-06-01"
API = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/field-measurements/items"
UA = "HKL-ai-evolution-research/0.1 (https://github.com/Causal5/Harmonic-Knowledge-Law; Session 3)"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "outputs"
GEOJSON = SOURCES / "b118_5-022.12_tulare_lake.geojson"


def http_get(url: str, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, resp.geturl(), resp.read()


def load_rings():
    d = json.loads(GEOJSON.read_text())
    feats = d["features"]
    if len(feats) != 1:
        raise SystemExit(f"expected 1 subbasin feature, got {len(feats)}")
    props = feats[0]["properties"]
    geom = feats[0]["geometry"]
    # lists of (outer, [holes]) where each ring is list[(x,y)]
    polys = []

    def as_poly(coords):
        outer = [(p[0], p[1]) for p in coords[0]]
        holes = [[(p[0], p[1]) for p in r] for r in coords[1:]]
        return outer, holes

    if geom["type"] == "Polygon":
        polys.append(as_poly(geom["coordinates"]))
    elif geom["type"] == "MultiPolygon":
        for c in geom["coordinates"]:
            polys.append(as_poly(c))
    else:
        raise SystemExit(f"unexpected geom {geom['type']}")
    # bbox
    xs, ys = [], []
    for outer, _ in polys:
        for x, y in outer:
            xs.append(x)
            ys.append(y)
    bbox = (min(xs), min(ys), max(xs), max(ys))
    return props, polys, bbox


def point_on_or_in_ring(x, y, ring) -> bool:
    # even-odd, treating a vertex/edge hit as inside
    n = len(ring)
    if n < 4:
        return False
    # close
    if ring[0] != ring[-1]:
        ring = ring + [ring[0]]
        n = len(ring)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = ring[i]
        xj, yj = ring[j]
        # vertex / edge
        if (xi, yi) == (x, y):
            return True
        # on horizontal or general edge
        if (min(yi, yj) <= y <= max(yi, yj)) and (min(xi, xj) <= x <= max(xi, xj)):
            if yi == yj:
                if min(xi, xj) <= x <= max(xi, xj):
                    return True
            else:
                t = (y - yi) / (yj - yi) if yj != yi else 0
                if 0 <= t <= 1:
                    xe = xi + t * (xj - xi)
                    if abs(xe - x) <= 1e-12:
                        return True
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 0.0) + xi):
            inside = not inside
        j = i
    return inside


def in_subbasin(x, y, polys) -> bool:
    for outer, holes in polys:
        if point_on_or_in_ring(x, y, outer):
            if any(point_on_or_in_ring(x, y, h) for h in holes):
                continue
            return True
    return False


def in_window(d: date, window):
    a, b = window
    return a <= d <= b


def fetch_all(bbox):
    """Fetch 72019 field measurements in the subbasin bbox over the locked years."""
    items = []
    chunks = []
    # year-by-year to stay under limits
    for year in range(2015, 2025):
        # only need March-May of 2015 and 2024, but also we may paginate
        # Fetch only the two spring windows (plus a day).
        if year not in (2015, 2024):
            continue
        start = f"{year}-03-01"
        end = f"{year}-06-01"
        offset = 0
        limit = 10000
        while True:
            q = {
                "f": "json",
                "parameter_code": PARAM,
                "bbox": f"{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}",
                "datetime": f"{start}/{end}",
                "limit": str(limit),
                "offset": str(offset),
            }
            url = API + "?" + urllib.parse.urlencode(q)
            status, final, body = http_get(url)
            data = json.loads(body.decode("utf-8"))
            feats = data.get("features") or []
            chunks.append(
                {
                    "year": year,
                    "url": url,
                    "http_status": status,
                    "final_url": final,
                    "numberReturned": data.get("numberReturned"),
                    "feature_count": len(feats),
                    "api_timeStamp": data.get("timeStamp"),
                    "offset": offset,
                }
            )
            items.extend(feats)
            if len(feats) < limit:
                break
            offset += limit
            if offset > 100000:
                raise SystemExit("pagination exceeded safeguard")
    return items, chunks


def coords_of(feat):
    g = feat.get("geometry") or {}
    c = g.get("coordinates")
    if g.get("type") == "Point" and isinstance(c, (list, tuple)) and len(c) >= 2:
        return float(c[0]), float(c[1])
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    props, polys, bbox = load_rings()
    raw_path = SOURCES / "usgs_field_measurements_72019_bbox_springs_2015_2024.json"

    fetch_meta = {
        "computed_at_local": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
        "offline": bool(args.offline),
        "bbox_used_for_api": bbox,
        "subbasin": {
            "Basin_Subbasin_Number": props.get("Basin_Subbasin_Number"),
            "Basin_Subbasin_Name": props.get("Basin_Subbasin_Name"),
            "Basin_Name": props.get("Basin_Name"),
            "Area_SqMiles": props.get("Area_SqMiles"),
            "Area_Acres": props.get("Area_Acres"),
            "OBJECTID": props.get("OBJECTID"),
            "Comments": props.get("Comments"),
        },
    }

    if args.offline:
        if not raw_path.exists():
            raise SystemExit("missing committed raw measurements")
        bundle = json.loads(raw_path.read_text())
        items = bundle["features"]
        chunks = bundle.get("chunk_meta") or []
        fetch_meta["mode"] = "offline"
    else:
        items, chunks = fetch_all(bbox)
        raw_path.write_text(json.dumps({"chunk_meta": chunks, "features": items}))
        fetch_meta["mode"] = "live"
        fetch_meta["n_fetched_features"] = len(items)

    # process
    by_well = defaultdict(lambda: {"c2015": [], "c2024": [], "props": None, "xy": None, "in_poly": None})
    skipped_no_xy = 0
    skipped_out = 0
    skipped_bad_date = 0
    skipped_non_numeric = 0
    skipped_other_window = 0
    units = Counter()
    approval = Counter()
    for feat in items:
        p = feat.get("properties") or {}
        xy = coords_of(feat)
        if xy is None:
            skipped_no_xy += 1
            continue
        if not in_subbasin(xy[0], xy[1], polys):
            skipped_out += 1
            continue
        t = p.get("time")
        if not t:
            skipped_bad_date += 1
            continue
        try:
            d = date.fromisoformat(str(t)[:10])
        except ValueError:
            skipped_bad_date += 1
            continue
        raw = p.get("value")
        try:
            if raw is None or raw == "":
                raise ValueError("empty")
            val = float(raw)
        except (TypeError, ValueError):
            skipped_non_numeric += 1
            continue
        if p.get("parameter_code") not in (None, PARAM) and str(p.get("parameter_code")) != PARAM:
            # should already be filtered
            continue
        units[p.get("unit_of_measure") or ""] += 1
        approval[p.get("approval_status") or ""] += 1
        loc = p.get("monitoring_location_id") or p.get("monitoring_location_number")
        if not loc:
            continue
        rec = by_well[loc]
        rec["xy"] = xy
        rec["props"] = {
            "monitoring_location_id": loc,
            "monitoring_location_name": p.get("monitoring_location_name"),
            "agency_code": p.get("agency_code") or p.get("agency_name"),
            "site_type": p.get("site_type"),
            "hydrologic_unit_code": p.get("hydrologic_unit_code"),
            "unit_of_measure": p.get("unit_of_measure"),
        }
        rec["in_poly"] = True
        if in_window(d, SPRING_2015):
            rec["c2015"].append({"date": d.isoformat(), "value": val, "approval": p.get("approval_status"), "qualifier": p.get("qualifier")})
        elif in_window(d, SPRING_2024):
            rec["c2024"].append({"date": d.isoformat(), "value": val, "approval": p.get("approval_status"), "qualifier": p.get("qualifier")})
        else:
            skipped_other_window += 1

    qualifying = []
    only_2015 = only_2024 = neither_both_incomplete = 0
    for loc, rec in by_well.items():
        if rec["c2015"] and rec["c2024"]:
            m15 = statistics.median([x["value"] for x in rec["c2015"]])
            m24 = statistics.median([x["value"] for x in rec["c2024"]])
            delta = m24 - m15
            qualifying.append(
                {
                    "monitoring_location_id": loc,
                    "monitoring_location_name": rec["props"]["monitoring_location_name"],
                    "lon": rec["xy"][0],
                    "lat": rec["xy"][1],
                    "unit": rec["props"]["unit_of_measure"],
                    "n_spring2015": len(rec["c2015"]),
                    "n_spring2024": len(rec["c2024"]),
                    "median_dtw_spring2015": m15,
                    "median_dtw_spring2024": m24,
                    "delta_2024_minus_2015": delta,
                    "hydrologic_unit_code": rec["props"]["hydrologic_unit_code"],
                }
            )
        elif rec["c2015"] and not rec["c2024"]:
            only_2015 += 1
        elif rec["c2024"] and not rec["c2015"]:
            only_2024 += 1
        else:
            neither_both_incomplete += 1

    deltas = [q["delta_2024_minus_2015"] for q in qualifying]
    units_q = Counter(q["unit"] for q in qualifying)
    summary = {
        "protocol": {
            "subbasin_number": "5-022.12",
            "parameter_code": PARAM,
            "spring_2015": [SPRING_2015[0].isoformat(), SPRING_2015[1].isoformat()],
            "spring_2024": [SPRING_2024[0].isoformat(), SPRING_2024[1].isoformat()],
            "delta_definition": "median DTW spring 2024 minus median DTW spring 2015; positive = deeper water table in 2024",
            "purpose": "observed head-change field for a locked official subbasin; not V_W; not Bite 5; not a basin storage volume",
        },
        "fetch": fetch_meta,
        "chunk_meta": chunks if not args.offline else "see committed raw bundle",
        "counts": {
            "n_features_fetched_or_loaded": len(items),
            "skipped_no_xy": skipped_no_xy,
            "skipped_outside_polygon": skipped_out,
            "skipped_bad_date": skipped_bad_date,
            "skipped_non_numeric": skipped_non_numeric,
            "skipped_other_window_inside_poly": skipped_other_window,
            "wells_inside_poly_with_any_kept_measurement": len(by_well),
            "wells_only_spring2015": only_2015,
            "wells_only_spring2024": only_2024,
            "n_qualifying_both_windows": len(qualifying),
            "units_all_inside_poly_measurements": dict(units),
            "approval_all_inside_poly_measurements": dict(approval),
            "units_qualifying_wells": dict(units_q),
        },
        "change_2024_minus_2015": None,
    }
    if deltas:
        summary["change_2024_minus_2015"] = {
            "n": len(deltas),
            "mean": sum(deltas) / len(deltas),
            "median": statistics.median(deltas),
            "min": min(deltas),
            "max": max(deltas),
            "n_deeper_in_2024_positive": sum(1 for x in deltas if x > 0),
            "n_shallower_in_2024_negative": sum(1 for x in deltas if x < 0),
            "n_zero": sum(1 for x in deltas if x == 0),
        }

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    qpath = OUTPUTS / "tulare_lake_qualifying_wells_spring2015_2024.csv"
    fields = list(qualifying[0].keys()) if qualifying else [
        "monitoring_location_id","monitoring_location_name","lon","lat","unit",
        "n_spring2015","n_spring2024","median_dtw_spring2015","median_dtw_spring2024","delta_2024_minus_2015","hydrologic_unit_code"
    ]
    with qpath.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in sorted(qualifying, key=lambda r: r["monitoring_location_id"]):
            w.writerow(row)
    (OUTPUTS / "tulare_lake_spring_dtw_summary.json").write_text(json.dumps(summary, indent=2, default=str))

    print("SUBBASIN 5-022.12 SAN JOAQUIN VALLEY - TULARE LAKE")
    print("parameter 72019 spring 2015 vs spring 2024")
    print("fetched/loaded", len(items), "inside-poly wells with a spring measurement", len(by_well))
    print("qualifying both windows", len(qualifying), "only2015", only_2015, "only2024", only_2024)
    if deltas:
        s = summary["change_2024_minus_2015"]
        print(
            f"delta (2024-2015) mean {s['mean']:.6g} median {s['median']:.6g} "
            f"min {s['min']:.6g} max {s['max']:.6g} "
            f"deeper={s['n_deeper_in_2024_positive']} shallower={s['n_shallower_in_2024_negative']} zero={s['n_zero']}"
        )
        print("units", dict(units_q))
    else:
        print("NO QUALIFYING WELLS")
    print("outputs under", OUTPUTS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
