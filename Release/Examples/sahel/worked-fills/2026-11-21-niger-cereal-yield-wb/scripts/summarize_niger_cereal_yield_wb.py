#!/usr/bin/env python3
"""World Bank / FAOSTAT cereal yield indicator for Niger.

LOCKED PROTOCOL (declared before values are aggregated):
  Geography: Republic of Niger (ISO 3166-1 alpha-2: NE; World Bank code NE).
    Named in the archive Sahel example as the FMNR setting. This is a
    country-scale precursor series, not a lock of comparable locations
    for the bounded test (those remain UNFILLED-REQUIRED).

  New source class (declared): World Bank World Development Indicators,
    sourced from FAOSTAT (FAO). Jordan's Session 3 direction named FAO
    and World Bank. This class is not among the current Sahel paper's
    own external URLs and is declared here so it can be challenged.

  Indicator: AG.YLD.CREL.KG
    Name: Cereal yield (kg per hectare).
    Official sourceNote: long-term average in depth (over space and time)
    of annual cereal yield in the country. If the retrieved series is a
    repeated long-term average rather than an interannual series, report
    that fact and do not treat it as year-to-year rainfall.

  Window: all official annual records with a numeric value in the
    retrieved API extract whose year is between 1961 and 2022 inclusive.
    Years present on the page but outside that window, or with null
    values, are reported as missing/out-of-window, not interpolated.

  Statistics: n years, missing years inside the window, number of
    distinct numeric values, min/max/mean if more than one distinct
    value, and the value itself if only one distinct value. No
    interpolation. No V, dV/dt, lambda_PAE, or restored sign-change
    claim. Not a test of FMNR or of the Great Green Wall.

  API: https://api.worldbank.org/v2/country/NE/indicator/AG.YLD.CREL.KG
       ?format=json&per_page=200
  Indicator metadata:
       https://api.worldbank.org/v2/indicator/AG.YLD.CREL.KG?format=json

Usage: python3 summarize_niger_precip_wb.py [--offline]
"""
from __future__ import annotations

import argparse, json, csv, sys, urllib.request
from datetime import datetime
from pathlib import Path

COUNTRY = "NE"
INDICATOR = "AG.YLD.CREL.KG"
YEAR0, YEAR1 = 1961, 2022
SERIES_URL = f"https://api.worldbank.org/v2/country/{COUNTRY}/indicator/{INDICATOR}?format=json&per_page=200"
META_URL = f"https://api.worldbank.org/v2/indicator/{INDICATOR}?format=json"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCES, OUTPUTS = ROOT / "sources", ROOT / "outputs"
UA = "HKL-ai-evolution-research/0.1 (https://github.com/Causal5/Harmonic-Knowledge-Law; Session 3)"


def http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.geturl(), r.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    OUTPUTS.mkdir(exist_ok=True)
    SOURCES.mkdir(exist_ok=True)
    series_path = SOURCES / "wb_AG.YLD.CREL.KG_NE.json"
    meta_path = SOURCES / "wb_indicator_AG.YLD.CREL.KG.json"
    meta_fetch = {"computed_at_local": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"), "offline": bool(args.offline)}
    if args.offline:
        series = json.loads(series_path.read_text())
        meta = json.loads(meta_path.read_text())
        meta_fetch["mode"] = "offline"
    else:
        st, fin, body = http_get(SERIES_URL)
        series_path.write_bytes(body)
        series = json.loads(body)
        meta_fetch["series_http"] = st
        meta_fetch["series_final_url"] = fin
        st2, fin2, body2 = http_get(META_URL)
        meta_path.write_bytes(body2)
        meta = json.loads(body2)
        meta_fetch["meta_http"] = st2
        meta_fetch["meta_final_url"] = fin2
        meta_fetch["mode"] = "live"

    page = series[0]
    rows = series[1]
    by_year = {}
    for r in rows:
        y = int(r["date"])
        by_year[y] = r.get("value")
    window_years = list(range(YEAR0, YEAR1 + 1))
    numeric = []
    missing = []
    for y in window_years:
        v = by_year.get(y)
        if v is None:
            missing.append(y)
        else:
            numeric.append((y, float(v)))
    values = [v for _, v in numeric]
    distinct = sorted(set(values))
    out_of_window = sorted(y for y in by_year if y < YEAR0 or y > YEAR1)
    # official metadata fields
    rec = meta[1][0] if isinstance(meta, list) and len(meta) > 1 else {}
    summary = {
        "protocol": {
            "country": "Niger",
            "country_code": COUNTRY,
            "indicator": INDICATOR,
            "window": [YEAR0, YEAR1],
            "purpose": "country-scale precursor agricultural-outcome series; not V; not a dV/dt sign test; not an FMNR evaluation; not a lock of bounded-test comparable locations",
        },
        "fetch": meta_fetch,
        "api_page": page,
        "indicator_metadata": {
            "id": rec.get("id"),
            "name": rec.get("name"),
            "sourceNote": rec.get("sourceNote"),
            "sourceOrganization": rec.get("sourceOrganization"),
            "source": rec.get("source"),
        },
        "counts": {
            "n_years_in_window": len(window_years),
            "n_numeric": len(numeric),
            "n_missing": len(missing),
            "missing_years": missing,
            "years_on_page_outside_window": out_of_window,
            "n_distinct_values": len(distinct),
            "distinct_values_mm_per_year": distinct,
        },
        "statistics": None,
        "interpretation_rule": (
            "If n_distinct_values == 1, this indicator is a repeated long-term average "
            "in this extract and must not be treated as an interannual rainfall series."
        ),
    }
    if len(distinct) == 1:
        summary["statistics"] = {
            "type": "repeated_constant_series",
            "value_kg_per_ha": distinct[0],
            "n_years_with_that_value": len(values),
        }
    elif values:
        summary["statistics"] = {
            "type": "interannual",
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
            "min_year": next(y for y, v in numeric if v == min(values)),
            "max_year": next(y for y, v in numeric if v == max(values)),
        }

    with (OUTPUTS / "niger_AG.YLD.CREL.KG_1961-2022.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "value_kg_per_ha", "status"])
        for y in window_years:
            v = by_year.get(y)
            w.writerow([y, "" if v is None else v, "missing" if v is None else "numeric"])
    (OUTPUTS / "niger_cereal_yield_wb_summary.json").write_text(json.dumps(summary, indent=2))
    print("INDICATOR", INDICATOR, rec.get("name"))
    print("sourceOrganization", rec.get("sourceOrganization"))
    print("window", YEAR0, YEAR1, "numeric", len(numeric), "missing", missing)
    print("n_distinct", len(distinct), "values", distinct)
    print("statistics", summary["statistics"])
    print("WDI lastupdated", page.get("lastupdated"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
