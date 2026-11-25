#!/usr/bin/env python3
# Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 28).
# Applies the pre-registered qualification rule. Protocol: ../PREREG.md, committed
# before this search was scored.
"""Classify locked-catalog C_irr candidates for Tulare Lake 5-022.12."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
OUTPUTS = ROOT / "outputs"
POLYGON = (
    ROOT.parent
    / "2026-11-21-tulare-lake-72019"
    / "sources"
    / "b118_5-022.12_tulare_lake.geojson"
)
NWIS = SOURCES / "nwis_ca_gwex.rdb"
EXPECTED_NWIS_SHA256 = "7b5e6ba2ac4acb56326007f6ed19325be04bd1b79285c991c50fa5eaa089f394"

# WY 2025 Appendix RMS coordinates (also used as NGL station positions).
CGPS_SITES = [
    {"site_id": "CRCN", "latitude": 36.113986, "longitude": -119.568034, "source": "WY 2025 appendix"},
    {"site_id": "LEMA", "latitude": 36.292025, "longitude": -119.782390, "source": "WY 2025 appendix"},
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_rings():
    import json as _json

    geo = _json.loads(POLYGON.read_text())
    geom = geo["features"][0]["geometry"]
    rings = []
    if geom["type"] == "Polygon":
        rings.append(geom["coordinates"][0])
    elif geom["type"] == "MultiPolygon":
        for poly in geom["coordinates"]:
            rings.append(poly[0])
    else:
        raise SystemExit(f"unexpected geometry {geom['type']}")
    return rings


def in_ring(x, y, ring) -> bool:
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


def in_subbasin(x, y, rings) -> bool:
    return any(in_ring(x, y, r) for r in rings)


def parse_rdb(path: Path):
    rows = []
    header = None
    for line in path.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if header is None:
            header = parts
            continue
        if parts[0].endswith("s") and parts[0][0].isdigit():
            continue
        rows.append(dict(zip(header, parts)))
    return rows


def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    nwis_sha = sha256_file(NWIS)
    if nwis_sha != EXPECTED_NWIS_SHA256:
        raise SystemExit(f"unexpected NWIS sha256 {nwis_sha}")
    rings = load_rings()

    nwis_rows = []
    n_in = 0
    for rec in parse_rdb(NWIS):
        lon = float(rec["dec_long_va"])
        lat = float(rec["dec_lat_va"])
        inside = in_subbasin(lon, lat, rings)
        if inside:
            n_in += 1
        nwis_rows.append(
            {
                "agency_cd": rec["agency_cd"],
                "site_no": rec["site_no"],
                "station_nm": rec["station_nm"],
                "site_tp_cd": rec["site_tp_cd"],
                "latitude": f"{lat:.8f}",
                "longitude": f"{lon:.8f}",
                "in_5_022_12": "yes" if inside else "no",
            }
        )

    cgps_rows = []
    for rec in CGPS_SITES:
        inside = in_subbasin(rec["longitude"], rec["latitude"], rings)
        if not inside:
            raise SystemExit(f"expected {rec['site_id']} to fall inside 5-022.12")
        cgps_rows.append(
            {
                "site_id": rec["site_id"],
                "latitude": rec["latitude"],
                "longitude": rec["longitude"],
                "in_5_022_12": "yes",
                "source": rec["source"],
            }
        )

    # Locked product assessments. Object-class and independence judgments are
    # recorded here from the retrieved official labels; the script only checks
    # that none of the forbidden products are marked as qualifying, and that
    # coverage for NWIS extensometers matches the polygon test.
    products = [
        {
            "product_id": "dwr_tre_altamira_insar",
            "product": "DWR / TRE Altamira InSAR and the WY 2025 C-zone storage volume derived from it",
            "catalog": "DWR or SGMA subsidence products",
            "object_class": "fail",
            "independence": "fail",
            "coverage": "pass",
            "lockability": "pass",
            "qualifies": "no",
            "reason": "Surface displacement already used as the C-zone input (v0.2; WY 2025 §3.5.2, V = A Δb with Δb from subsidence; filing states subbasin subsidence data are InSAR). Independence rule forbids reusing that input as C_irr.",
        },
        {
            "product_id": "usgs_nwis_gwex",
            "product": "USGS NWIS borehole extensometers (site type GW-EX), California inventory retrieved 25 November 2026",
            "catalog": "USGS extensometer pages and data releases",
            "object_class": "pass",
            "independence": "pass",
            "coverage": "fail",
            "lockability": "pass",
            "qualifies": "no",
            "reason": "Extensometers measure aquifer-system compaction and are independent of InSAR, but 0 of 17 California GW-EX sites fall inside 5-022.12. WY 2025 still says additional high-resolution extensometer data is needed in the subbasin.",
        },
        {
            "product_id": "usgs_refurbished_sjv_extensometers",
            "product": "USGS refurbished San Joaquin Valley extensometers (Oro Loma Deep, Panoche, DWR Yard, Rasta)",
            "catalog": "USGS extensometer pages and data releases",
            "object_class": "pass",
            "independence": "pass",
            "coverage": "fail",
            "lockability": "pass",
            "qualifies": "no",
            "reason": "Named on the USGS Central Valley subsidence-data page as the four refurbished cable-type sites. All four are in the NWIS inventory and all are outside 5-022.12 (Rasta, 020S018E06D001M, is the nearest, still outside the Bulletin 118 polygon).",
        },
        {
            "product_id": "usgs_brandt_p144brey",
            "product": "Brandt, Sneed, and Boyce extensometer compaction observations, 1958–2018 (DOI 10.5066/P144BREY)",
            "catalog": "USGS extensometer pages and data releases",
            "object_class": "pass",
            "independence": "pass",
            "coverage": "fail",
            "lockability": "fail",
            "qualifies": "no",
            "reason": "The data-release landing page exists and describes borehole-extensometer compaction observations through 2018. The ScienceBase item and site table were not retrieved (HTTP 403). No 5-022.12 site can be locked from that release here. The lockable public NWIS inventory has zero sites in the polygon.",
        },
        {
            "product_id": "cgps_lema_crcn",
            "product": "CGPS stations LEMA (Lemoore) and CRCN (Corcoran)",
            "catalog": "Continuous GPS or documented spirit-leveling / borehole-compaction records",
            "object_class": "fail",
            "independence": "pass",
            "coverage": "pass",
            "lockability": "pass",
            "qualifies": "no",
            "reason": "Both stations lie inside 5-022.12. WY 2025 reports land-surface subsidence in feet, and NGL publishes daily IGS20 height series. That is an independent displacement record, not a locked C_irr volume. No retrieved official source converts these two series into storage-capacity loss for the subbasin without the shared InSAR. v0.2 already states that translating surface displacement into water released from a particular aquifer requires a model. This fill does not invent that conversion.",
        },
        {
            "product_id": "krcd_benchmark_surveys",
            "product": "KRCD / other RMS benchmark surveys reported in WY 2025",
            "catalog": "Continuous GPS or documented spirit-leveling / borehole-compaction records",
            "object_class": "fail",
            "independence": "pass",
            "coverage": "pass",
            "lockability": "pass",
            "qualifies": "no",
            "reason": "WY 2025 reports an average land-surface decrease of 0.2079 ft at benchmark RMS stations. That is survey displacement, not a locked C_irr volume, and no official independent conversion was retrieved.",
        },
        {
            "product_id": "openet_et",
            "product": "OpenET evapotranspiration",
            "catalog": "OpenET (checked only to record that it is not C_irr)",
            "object_class": "fail",
            "independence": "pass",
            "coverage": "pass",
            "lockability": "pass",
            "qualifies": "no",
            "reason": "OpenET describes itself as satellite-based evapotranspiration (evaporation plus transpiration) and consumptive use. That is not irreversible compaction or storage-capacity loss. Treating it as C_irr would be a procedure break.",
        },
    ]

    # Integrity checks against the pre-registered rule.
    for p in products:
        if p["product_id"] in {"dwr_tre_altamira_insar", "openet_et"} and p["qualifies"] == "yes":
            raise SystemExit(f"procedure break: {p['product_id']} marked as qualifying")
        flags = [p["object_class"], p["independence"], p["coverage"], p["lockability"]]
        if all(f == "pass" for f in flags) and p["qualifies"] != "yes":
            raise SystemExit(f"{p['product_id']} meets all four tests but is not marked qualifying")
        if any(f != "pass" for f in flags) and p["qualifies"] == "yes":
            raise SystemExit(f"{p['product_id']} is marked qualifying without all four tests")
    if n_in != 0:
        raise SystemExit(f"expected 0 NWIS GW-EX sites inside 5-022.12, found {n_in}")
    usgs = next(p for p in products if p["product_id"] == "usgs_nwis_gwex")
    if usgs["coverage"] != "fail":
        raise SystemExit("NWIS coverage flag does not match the polygon test")

    n_qualifying = sum(p["qualifies"] == "yes" for p in products)
    if n_qualifying == 0:
        round_outcome = "indeterminate"
        cause = "data / scope gap"
    else:
        round_outcome = "holds"
        cause = "—"

    summary = {
        "nwis_sha256": nwis_sha,
        "n_nwis_ca_gwex": len(nwis_rows),
        "n_nwis_in_5_022_12": n_in,
        "n_products": len(products),
        "n_qualifying": n_qualifying,
        "round_outcome": round_outcome,
        "cause": cause,
        "arm_07": "wait",
        "signature": "unassigned",
        "note": "Finding a qualifying product would not have developed ARM-07 or evaluated the protocol §5 conjunction. None qualified.",
    }

    write_csv(
        OUTPUTS / "nwis_extensometer_sites.csv",
        nwis_rows,
        [
            "agency_cd",
            "site_no",
            "station_nm",
            "site_tp_cd",
            "latitude",
            "longitude",
            "in_5_022_12",
        ],
    )
    write_csv(
        OUTPUTS / "cgps_sites.csv",
        cgps_rows,
        ["site_id", "latitude", "longitude", "in_5_022_12", "source"],
    )
    write_csv(
        OUTPUTS / "product_qualification.csv",
        products,
        [
            "product_id",
            "product",
            "catalog",
            "object_class",
            "independence",
            "coverage",
            "lockability",
            "qualifies",
            "reason",
        ],
    )
    (OUTPUTS / "qualification_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"nwis_ca={len(nwis_rows)} nwis_in_basin={n_in}")
    print(f"n_qualifying={n_qualifying}")
    print(f"round_outcome={round_outcome}")
    print(f"cause={cause}")


if __name__ == "__main__":
    main()
