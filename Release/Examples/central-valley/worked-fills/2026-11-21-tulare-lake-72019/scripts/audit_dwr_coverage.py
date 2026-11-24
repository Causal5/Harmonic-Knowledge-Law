"""Count DWR spring depth-to-water coverage for the locked Tulare Lake polygon.

Usage: python3 audit_dwr_coverage.py periodic_gwl_bulkdatadownload.zip
The two windows are March–May 2015 and March–May 2024, in DWR local time.
Count a site once per window with any finite gse_gwe, and separately with
DWR quality Good. These are inventory counts only. No trends or scores.
"""
import csv
import io
import json
import math
import sys
import zipfile

from compute_tulare_lake_spring_dtw import in_subbasin, load_rings


def rows(bundle, filename):
    with bundle.open(filename) as raw, io.TextIOWrapper(raw, encoding="utf-8-sig", newline="") as stream:
        yield from csv.DictReader(stream)


def finite(value):
    try:
        return math.isfinite(float(value))
    except (ValueError, TypeError):
        return False


def audit(bundle):
    _, polygons, (west, south, east, north) = load_rings()
    sites = set()
    for row in rows(bundle, "stations.csv"):
        if finite(row["longitude"]) and finite(row["latitude"]):
            x, y = float(row["longitude"]), float(row["latitude"])
            if west <= x <= east and south <= y <= north and in_subbasin(x, y, polygons):
                sites.add(row["site_code"])

    windows = ("2015", "2024")
    coverage = {quality: {year: set() for year in windows} for quality in ("numeric", "good")}
    for row in rows(bundle, "measurements.csv"):
        site, date = row["site_code"], row["msmt_date"]
        year = date[:4]
        if site not in sites or year not in windows or not "03-01" <= date[5:10] <= "05-31":
            continue
        if finite(row["gse_gwe"]):
            coverage["numeric"][year].add(site)
            if row["wlm_qa_desc"].strip().lower() == "good":
                coverage["good"][year].add(site)

    return {
        quality: {"2015": len(s["2015"]), "2024": len(s["2024"]), "both": len(s["2015"] & s["2024"])}
        for quality, s in coverage.items()
    }


if __name__ == "__main__":
    with zipfile.ZipFile(sys.argv[1]) as archive:
        print(json.dumps(audit(archive), indent=2))
