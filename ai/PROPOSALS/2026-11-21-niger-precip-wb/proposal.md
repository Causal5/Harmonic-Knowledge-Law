# Proposal: Niger World Bank / FAOSTAT precipitation indicator as a Sahel precursor (Round 14)

**TL;DR.** This cycle retrieves a real official FAO/World Bank precipitation indicator for Niger and computes what it actually is: a repeated long-term average of 151.0 mm per year for 1961–2022, not an interannual rainfall series. It does not construct \(V\) and does not restore withdrawn Sahel claims.

**Status:** `proposed`

**Round:** Session 3, Round 14.

## Parent documents

- `Release/Examples/sahel_worked_example.md` §5–§6 (withdrawn completion claims stay withdrawn; no \(V\) before plan steps 1–5)
- `Release/Examples/sahel_bounded_test_plan_v0.1.md` (new source classes must be declared; comparable locations remain UNFILLED-REQUIRED)
- Archive `Release/archive/sahel_worked_example.md` (names FMNR in Niger; not used to restore withdrawn results)

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-niger-precip-01 | The retrieved WDI/FAOSTAT indicator AG.LND.PRCP.MM for Niger, locked window 1961–2022, is a single repeated value 151.0 mm/year in all 62 years, consistent with its “long-term average” source note, and is not treated as interannual rainfall. | Re-running the script on the committed JSON (or a live re-fetch of the same API URLs) shows more than one distinct numeric value in that window, or the fill treats 151 mm as a year-to-year rainfall series. |
| C-niger-precip-02 | This cycle does not construct \(V\), does not restore withdrawn Sahel sign-change or “passed falsification” wording, and does not lock bounded-test comparable locations. The FAO/World Bank source class is declared as new. | A \(V\) or sign-change result is reported, withdrawn wording is restored, or Niger is treated as the filled comparable-location lock. |
