#!/usr/bin/env python3
"""Recompute Table 3-1 imported shares from the Round 23 CSV. Stdlib only."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT.parent / "2026-11-24-tulare-tm-signature" / "outputs" / "tulare_table3-1_surface_water_supplies_wy2015-2025.csv"
OUT = ROOT / "outputs" / "tulare_table3-1_imported_shares.csv"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    source_sha = sha256(CSV_PATH)
    rows_out = []
    with CSV_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            total = int(row["total_af"])
            imported = int(row["imported_af"])
            surface = (
                int(row["kings_river_af"])
                + int(row["kaweah_river_af"])
                + int(row["tule_river_af"])
                + int(row["deer_creek_af"])
                + int(row["poso_creek_af"])
                + int(row["swp_af"])
                + int(row["cvp_af"])
            )
            if surface + imported != total:
                raise SystemExit(
                    f"row sum mismatch WY{row['water_year']}: {surface}+{imported}!={total}"
                )
            share = imported / total if total else None
            rows_out.append(
                {
                    "water_year": row["water_year"],
                    "year_type": row["year_type"],
                    "surface_ex_imported_af": surface,
                    "imported_af": imported,
                    "total_af": total,
                    "imported_share": f"{share:.6f}" if share is not None else "",
                }
            )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "water_year",
                "year_type",
                "surface_ex_imported_af",
                "imported_af",
                "total_af",
                "imported_share",
            ],
        )
        w.writeheader()
        w.writerows(rows_out)
    imported_shares = [float(r["imported_share"]) for r in rows_out]
    dry_shares = [float(r["imported_share"]) for r in rows_out if r["year_type"] == "Dry"]
    print(f"source_csv={CSV_PATH}")
    print(f"source_csv_sha256={source_sha}")
    print(f"n={len(rows_out)}")
    print(f"imported_share_min={min(imported_shares):.6f}")
    print(f"imported_share_max={max(imported_shares):.6f}")
    print(f"dry_year_imported_share_min={min(dry_shares):.6f}")
    print(f"dry_year_imported_share_max={max(dry_shares):.6f}")
    print(f"wrote={OUT}")


if __name__ == "__main__":
    main()
