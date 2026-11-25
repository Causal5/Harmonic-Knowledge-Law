#!/usr/bin/env python3
"""Recompute Table 3-4 evaluative-direction pairs. Stdlib only."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSV = ROOT / "outputs" / "paani_tables_3_4_region_pairs.csv"

def main() -> None:
    opposite = []
    same = []
    with CSV.open(newline="") as f:
        for row in csv.DictReader(f):
            well_cup = float(row["well_change_cup_m"])
            well_cmp = float(row["well_change_comparison_m"])
            rabi_cup = float(row["rabi_pct_cup"])
            rabi_cmp = float(row["rabi_pct_comparison"])
            well_better = well_cup > well_cmp  # less decline or a larger rise
            rabi_higher = rabi_cup > rabi_cmp
            direction = "opposite" if well_better != rabi_higher else "same"
            if direction != row["evaluative_directions"]:
                raise SystemExit(f"direction mismatch in {row['zone']}: computed {direction}")
            if row["zone"].startswith("All"):
                continue
            (opposite if direction == "opposite" else same).append(row["zone"])
    print(f"regions_opposite={len(opposite)}:{','.join(opposite)}")
    print(f"regions_same={len(same)}:{','.join(same)}")
    print("limb_A=holds" if opposite else "limb_A=breaks")

if __name__ == "__main__":
    main()
