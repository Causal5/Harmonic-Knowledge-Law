# Verdict: Round 21 CHIRPS vs WDI Niger rainfall

**TL;DR.** Accept with revisions. A clean `--offline` replay confirms the pre-registered test **holds**: CHIRPS v2.0 national-mean annual rainfall for Niger, 1981–2022, has CV 0.171 and ranges from 71.94 mm (1984) to 190.45 mm (1994), while WDI is 151 mm every year. The revision keeps the national mean from being read as a site series, a completed Sahel step 1, or a license to construct \(V\). Withdrawn Sahel claims stay withdrawn.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-24-niger-chirps/`

**Date:** 2026-11-24, America/New_York

## Checks run

- Re-ran `python3 scripts/compute_niger_chirps_national_mean.py --offline`. Decision: outcome `holds`, CV 0.171066…, min 71.938… mm, max 190.450… mm, 42 years.
- Confirmed PREREG.md precedes the series and forbids constructing \(V\) or restoring withdrawn claims.
- Confirmed the fill does not assign A1–A8 terms or run Sahel steps 1–6.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-chirps-01 | accepted | CH-chirps-01-rerun **misses**. Offline replay matches the committed decision statistics. |
| C-chirps-02 | accepted-with-revisions | The diagnosis holds under the locked rule. CH-chirps-02-national-not-site **misses as a false claim** and **hits as a summary risk**. The scoreboard note and fill already say this is a national mean, step 1 remains unfilled, and \(V\) was not constructed; that wording is retained as the required summary rule. |

## What this is not

Not a Sahel bounded-test result, not a site or FMNR contrast, not a \(V\) or sign-change restoration, and not a publication to `main`.
