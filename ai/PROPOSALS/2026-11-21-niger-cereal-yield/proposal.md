# Proposal: Niger World Bank / FAO cereal-yield precursor series (Round 15)

**TL;DR.** After Round 14 showed the official precipitation indicator is a repeated climatology, this cycle retrieves official FAO/WDI cereal yield for Niger, 1961–2022: an interannual series with mean 423.82 kg/ha, minimum 257.1 kg/ha in 1984, and maximum 599.3 kg/ha in 1964. It is not rainfall, not \(V\), and not an FMNR test.

**Status:** `accepted-with-revisions`

**Round:** Session 3, Round 15.

## Parent documents

- Round 14 Niger precipitation fill and verdict
- `Release/Examples/sahel_worked_example.md` §5–§6 and `sahel_bounded_test_plan_v0.1.md`

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-niger-yield-01 | For locked 1961–2022, WDI/FAOSTAT AG.YLD.CREL.KG for Niger is numeric in all 62 years, has 61 distinct values, mean 423.82 kg/ha, min 257.1 kg/ha in 1984, max 599.3 kg/ha in 1964. | Re-running the script on the committed JSON (or a live re-fetch) yields a materially different count, mean, or min/max year. |
| C-niger-yield-02 | This is not rainfall, not \(V\), not a restored Sahel sign-change claim, not an FMNR evaluation, and not a filled comparable-location lock. The choice of this indicator after Round 14 is declared. CHIRPS was not retrieved. | The fill treats yield as rainfall or as \(V\) or as an FMNR result, restores withdrawn wording, or claims CHIRPS was retrieved. |
