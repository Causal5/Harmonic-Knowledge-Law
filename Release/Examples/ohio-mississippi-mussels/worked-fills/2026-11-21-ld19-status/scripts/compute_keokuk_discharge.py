#!/usr/bin/env python3
# Unpublished branch work (ai/evolution, Round 19, 23 November 2026).
# This file does not exist in Release/ on main (270942cd107ffc92a44b4be8d7fffa0e6c22fd1d).
# It is not a publication to main. Release/ on main is the authoritative current source.
"""Keokuk / USGS 05474500 daily-mean discharge summary.

LOCKED PROTOCOL (do not change after inspecting values):
  Site: USGS 05474500, Mississippi River at Keokuk, IA
  Parameter: 00060 (discharge), statistic 00003 (daily mean)
  Unit: as reported (ft3/s / ft^3/s)
  Window: USGS water years 2016 through 2025 inclusive
          (2015-10-01 through 2025-09-30).
  Water-year definition (retrieved 2026-11-21 from
  https://water.usgs.gov/nwc/explain_data.html):
  "The term U.S.Geological Survey 'water year' in reports that deal with
  surface-water supply is defined as the 12-month period October 1, for
  any given year through September 30, of the following year. The water
  year is designated by the calendar year in which it ends and which
  includes 9 of the 12 months."

  Primary source: USGS NWIS Daily Values REST service
    https://waterservices.usgs.gov/nwis/dv/
  Comparison source: USGS Water Data OGC API v0 daily collection
    https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily

  Purpose: hydrologic context only. Not eta, not host-fish passage,
  not sink-impairment, not a fish-passage monitoring result.

Usage:
  python3 compute_keokuk_discharge.py [--offline]
  Run from any cwd. Outputs are written next to this script's
  ../outputs and raw comparison files under ../sources if fetched.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

SITE = "05474500"
SITE_ID = "USGS-05474500"
SITE_NAME = "Mississippi River at Keokuk, IA"
PARAM = "00060"
STAT = "00003"
WINDOW_START = date(2015, 10, 1)
WINDOW_END = date(2025, 9, 30)
LEGACY_URL = "https://waterservices.usgs.gov/nwis/dv/"
OGC_URL = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/items"
UA = (
    "HKL-ai-evolution-research/0.1 "
    "(https://github.com/Causal5/Harmonic-Knowledge-Law; Session 3)"
)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "outputs"


def water_year(d: date) -> int:
    return d.year + 1 if d.month >= 10 else d.year


def daterange(a: date, b: date):
    d = a
    while d <= b:
        yield d
        d += timedelta(days=1)


def http_get(url: str, timeout: int = 90) -> tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, resp.geturl(), resp.read()


def fetch_legacy_rdb() -> tuple[str, bytes]:
    q = {
        "sites": SITE,
        "parameterCd": PARAM,
        "statCd": STAT,
        "startDT": WINDOW_START.isoformat(),
        "endDT": WINDOW_END.isoformat(),
        "format": "rdb",
    }
    url = LEGACY_URL + "?" + urllib.parse.urlencode(q)
    status, final, body = http_get(url)
    if status != 200 or not body.startswith(b"#") and b"agency_cd" not in body[:2000]:
        raise SystemExit(f"legacy DV fetch failed status={status} url={final}")
    return url, body


def parse_rdb(text: str) -> tuple[dict, dict]:
    retrieved = None
    meta_lines = []
    for line in text.splitlines():
        if line.lower().startswith("# retrieved") or "retrieved:" in line.lower():
            retrieved = line
        if line.startswith("#"):
            meta_lines.append(line)
    data_lines = [ln for ln in text.splitlines() if ln and not ln.startswith("#")]
    if len(data_lines) < 3:
        raise SystemExit("RDB has no data rows")
    header = data_lines[0].split("\t")
    date_i = header.index("datetime") if "datetime" in header else 2
    val_i = next(i for i, h in enumerate(header) if "00060" in h and not h.endswith("_cd"))
    cd_i = next(i for i, h in enumerate(header) if "00060" in h and h.endswith("_cd"))
    by = {}
    for ln in data_lines[2:]:
        parts = ln.split("\t")
        d = date.fromisoformat(parts[date_i][:10])
        raw = parts[val_i].strip() if val_i < len(parts) else ""
        cd = parts[cd_i].strip() if cd_i < len(parts) else ""
        by[d] = {"raw": raw, "cd": cd}
    meta = {
        "retrieved_line": retrieved,
        "header": header,
        "value_column": header[val_i],
        "cd_column": header[cd_i],
        "n_rdb_rows": len(data_lines) - 2,
    }
    return by, meta


def fetch_ogc() -> tuple[list[dict], list[dict]]:
    rows = []
    chunk_meta = []
    for wy in range(2016, 2026):
        a = date(wy - 1, 10, 1)
        b = date(wy, 9, 30)
        q = {
            "f": "json",
            "monitoring_location_id": SITE_ID,
            "parameter_code": PARAM,
            "statistic_id": STAT,
            "datetime": f"{a.isoformat()}/{(b + timedelta(days=1)).isoformat()}",
            "limit": "10000",
        }
        url = OGC_URL + "?" + urllib.parse.urlencode(q)
        status, final, body = http_get(url, timeout=60)
        data = json.loads(body.decode("utf-8"))
        feats = data.get("features") or []
        chunk_meta.append(
            {
                "water_year": wy,
                "request_url": url,
                "http_status": status,
                "final_url": final,
                "numberReturned": data.get("numberReturned"),
                "feature_count": len(feats),
                "api_timeStamp": data.get("timeStamp"),
            }
        )
        if data.get("numberReturned") == 10000:
            raise SystemExit(f"OGC chunk WY{wy} hit limit")
        for f in feats:
            rows.append(f.get("properties") or {})
    return rows, chunk_meta


def summarize(by_day: dict, source_name: str, extra=None):
    missing = []
    non = []
    values = []  # (date, float, code)
    codes = Counter()
    n_cal = (WINDOW_END - WINDOW_START).days + 1
    for d in daterange(WINDOW_START, WINDOW_END):
        rec = by_day.get(d)
        if rec is None:
            missing.append(d)
            continue
        raw, cd = rec["raw"], rec.get("cd") or rec.get("approval_status") or ""
        codes[cd] += 1
        if raw is None or raw == "":
            non.append({"date": d.isoformat(), "raw": raw, "cd": cd})
            continue
        try:
            values.append((d, float(raw), cd))
        except ValueError:
            non.append({"date": d.isoformat(), "raw": raw, "cd": cd})
    annual = []
    for wy in range(2016, 2026):
        sub = [(d, v, cd) for d, v, cd in values if water_year(d) == wy]
        vs = [v for _, v, _ in sub]
        wy_days = sum(1 for d in daterange(WINDOW_START, WINDOW_END) if water_year(d) == wy)
        rec = {
            "water_year": wy,
            "calendar_days": wy_days,
            "n_numeric": len(sub),
            "n_missing": sum(1 for d in missing if water_year(d) == wy),
            "n_non_numeric": sum(1 for x in non if water_year(date.fromisoformat(x["date"])) == wy),
            "mean_cfs": (sum(vs) / len(vs)) if vs else None,
            "min_cfs": min(vs) if vs else None,
            "max_cfs": max(vs) if vs else None,
            "n_approved_A": sum(1 for _, _, cd in sub if str(cd).startswith("A") or str(cd) == "Approved"),
            "n_estimated": sum(
                1
                for _, _, cd in sub
                if "e" in str(cd).lower() or "ESTIMATED" in str(cd)
            ),
        }
        if vs:
            rec["min_date"] = next(d.isoformat() for d, v, _ in sub if v == rec["min_cfs"])
            rec["max_date"] = next(d.isoformat() for d, v, _ in sub if v == rec["max_cfs"])
        else:
            rec["min_date"] = rec["max_date"] = None
        annual.append(rec)
    vs_all = [v for _, v, _ in values]
    out = {
        "source": source_name,
        "counts": {
            "n_calendar_days": n_cal,
            "n_numeric": len(values),
            "n_missing": len(missing),
            "n_non_numeric": len(non),
            "codes_or_approval": dict(codes),
        },
        "period": {
            "mean_cfs": (sum(vs_all) / len(vs_all)) if vs_all else None,
            "min_cfs": min(vs_all) if vs_all else None,
            "max_cfs": max(vs_all) if vs_all else None,
            "min_date": next((d.isoformat() for d, v, _ in values if v == min(vs_all)), None)
            if vs_all
            else None,
            "max_date": next((d.isoformat() for d, v, _ in values if v == max(vs_all)), None)
            if vs_all
            else None,
        },
        "annual_water_year": annual,
        "missing_dates": [d.isoformat() for d in missing],
        "non_numeric": non,
    }
    if extra:
        out.update(extra)
    return out, values, missing


def write_annual_csv(path: Path, annual):
    fields = [
        "water_year",
        "calendar_days",
        "n_numeric",
        "n_missing",
        "n_non_numeric",
        "mean_cfs",
        "min_cfs",
        "max_cfs",
        "min_date",
        "max_date",
        "n_approved_A",
        "n_estimated",
    ]
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in annual:
            row = dict(r)
            for k in ("mean_cfs", "min_cfs", "max_cfs"):
                if row[k] is not None:
                    row[k] = f"{row[k]:.6g}"
            w.writerow(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="use committed RDB only; skip live fetches")
    args = ap.parse_args()
    SOURCES.mkdir(parents=True, exist_ok=True)
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    rdb_path = SOURCES / "nwis_dv_05474500_00060_wy2016-2025.rdb"
    fetch_meta = {
        "computed_at_local": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
        "offline": bool(args.offline),
    }
    if args.offline:
        if not rdb_path.exists():
            raise SystemExit(f"--offline but missing {rdb_path}")
        text = rdb_path.read_text(errors="replace")
        fetch_meta["legacy_mode"] = "offline_committed_rdb"
        fetch_meta["legacy_url"] = None
    else:
        url, body = fetch_legacy_rdb()
        rdb_path.write_bytes(body)
        text = body.decode("utf-8", "replace")
        fetch_meta["legacy_mode"] = "live_fetch"
        fetch_meta["legacy_url"] = url

    by, rdb_meta = parse_rdb(text)
    legacy, values, missing = summarize(
        by,
        "USGS NWIS Daily Values REST (waterservices.usgs.gov/nwis/dv)",
        extra={"rdb_meta": rdb_meta},
    )

    # daily csv from primary (legacy) source
    daily_path = OUTPUTS / "usgs_05474500_daily_mean_discharge_wy2016-2025.csv"
    with daily_path.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "date",
                "water_year",
                "value_cfs",
                "unit",
                "qualification_cd",
                "status",
                "source",
            ],
        )
        w.writeheader()
        for d in daterange(WINDOW_START, WINDOW_END):
            rec = by.get(d)
            if rec is None:
                w.writerow(
                    {
                        "date": d.isoformat(),
                        "water_year": water_year(d),
                        "value_cfs": "",
                        "unit": "ft3/s",
                        "qualification_cd": "",
                        "status": "missing",
                        "source": "nwis_dv",
                    }
                )
            else:
                status = "ok"
                try:
                    float(rec["raw"])
                except (TypeError, ValueError):
                    status = "non_numeric" if rec["raw"] != "" else "empty"
                w.writerow(
                    {
                        "date": d.isoformat(),
                        "water_year": water_year(d),
                        "value_cfs": rec["raw"],
                        "unit": "ft3/s",
                        "qualification_cd": rec["cd"],
                        "status": status,
                        "source": "nwis_dv",
                    }
                )

    write_annual_csv(
        OUTPUTS / "usgs_05474500_annual_summary_nwis_dv_wy2016-2025.csv",
        legacy["annual_water_year"],
    )

    ogc_summary = None
    comparison = None
    if not args.offline:
        try:
            ogc_rows, chunk_meta = fetch_ogc()
            ogc_by = {}
            for p in ogc_rows:
                if not p.get("time"):
                    continue
                d = date.fromisoformat(str(p["time"])[:10])
                ogc_by[d] = {
                    "raw": p.get("value"),
                    "cd": p.get("approval_status") or "",
                    "unit": p.get("unit_of_measure"),
                    "qualifier": p.get("qualifier"),
                    "time_series_id": p.get("time_series_id"),
                }
            ogc_summary, _, _ = summarize(
                ogc_by,
                "USGS Water Data OGC API v0 daily collection",
                extra={"chunk_meta": chunk_meta},
            )
            write_annual_csv(
                OUTPUTS / "usgs_05474500_annual_summary_ogc_api_wy2016-2025.csv",
                ogc_summary["annual_water_year"],
            )
            # value agreement on days present in both
            both = []
            disagree = []
            for d, v, _ in values:
                if d in ogc_by:
                    try:
                        ov = float(ogc_by[d]["raw"])
                    except (TypeError, ValueError):
                        continue
                    both.append(d)
                    if ov != v:
                        disagree.append({"date": d.isoformat(), "nwis_dv": v, "ogc": ov})
            comparison = {
                "n_legacy_numeric": legacy["counts"]["n_numeric"],
                "n_ogc_numeric": ogc_summary["counts"]["n_numeric"],
                "n_legacy_missing": legacy["counts"]["n_missing"],
                "n_ogc_missing": ogc_summary["counts"]["n_missing"],
                "n_days_present_in_both": len(both),
                "n_value_disagreements": len(disagree),
                "disagreements": disagree[:50],
                "note": (
                    "OGC API missingness is a service-coverage difference, "
                    "not evidence of hydrologic missingness, when NWIS DV has a value."
                ),
            }
        except Exception as e:
            comparison = {"error": f"{type(e).__name__}: {e}"}

    report = {
        "protocol": {
            "site": SITE_ID,
            "site_name": SITE_NAME,
            "parameter_code": PARAM,
            "statistic_id": STAT,
            "locked_window": {
                "start": WINDOW_START.isoformat(),
                "end": WINDOW_END.isoformat(),
                "definition": "USGS water years 2016-2025 inclusive",
                "water_year_source": "https://water.usgs.gov/nwc/explain_data.html",
            },
            "purpose": "hydrologic context only; not eta; not host passage; not sink-impairment",
        },
        "fetch": fetch_meta,
        "primary_nwis_dv": legacy,
        "comparison_ogc_api": ogc_summary,
        "source_comparison": comparison,
    }
    (OUTPUTS / "usgs_05474500_summary.json").write_text(json.dumps(report, indent=2))

    # stdout report for C
    p = legacy["period"]
    c = legacy["counts"]
    print("PRIMARY SOURCE: USGS NWIS Daily Values REST")
    print(
        f"window {WINDOW_START} to {WINDOW_END}: "
        f"{c['n_numeric']}/{c['n_calendar_days']} numeric days, "
        f"{c['n_missing']} missing, {c['n_non_numeric']} non-numeric"
    )
    if p["mean_cfs"] is not None:
        print(
            f"period mean {p['mean_cfs']:.6g} ft3/s; "
            f"min {p['min_cfs']:.6g} on {p['min_date']}; "
            f"max {p['max_cfs']:.6g} on {p['max_date']}"
        )
    print("water-year means (ft3/s):")
    for r in legacy["annual_water_year"]:
        mean = "NA" if r["mean_cfs"] is None else f"{r['mean_cfs']:.6g}"
        print(
            f"  WY{r['water_year']}: n={r['n_numeric']}/{r['calendar_days']} "
            f"missing={r['n_missing']} mean={mean} "
            f"min={r['min_cfs']} max={r['max_cfs']} estimated={r['n_estimated']}"
        )
    if comparison and "n_ogc_missing" in comparison:
        print(
            "OGC API comparison: "
            f"numeric {comparison['n_ogc_numeric']} "
            f"missing {comparison['n_ogc_missing']}; "
            f"days in both {comparison['n_days_present_in_both']}; "
            f"value disagreements {comparison['n_value_disagreements']}"
        )
    elif comparison:
        print("OGC API comparison:", comparison)
    print("outputs written under", OUTPUTS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
