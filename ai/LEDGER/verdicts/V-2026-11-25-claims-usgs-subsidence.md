# Verdict: USGS subsidence follow-up (CV-11 and CV-14)

**TL;DR.** Accept with revisions. The USGS San Joaquin Valley page cited on `main` has now been retrieved and confirms the episode paragraph, so CV-11 is ruled **supported-with-limit**. A new row, CV-14, is also **supported-with-limit**: roughly 9 m of subsidence from 1925 to 1977 at the approximate point of maximum subsidence (Ireland photograph), plus the national 80-percent groundwater-use sentence. Both challenges hit as wording risks and were addressed. This is not a Tulare Lake transfer, not a delivered-service finding, and not a publication to `main`.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-25-claims-usgs-subsidence/`

**Date:** 2026-11-25, America/New_York

## Checks run

- Confirmed the protocol and extraction (`4b37203` / `6eb3f18`) precede the attack (`9780a2b` / `2029e61`) and this verdict.
- Re-fetched `https://www.usgs.gov/centers/land-subsidence-in-california/science/land-subsidence-san-joaquin-valley` (200). The page is dated October 17, 2018. Immediately above “Importance of Monitoring Subsidence,” it states that reduced surface-water availability during 1976-77, 1986-92, 2007-09, and 2012-2015 caused groundwater-pumping increases, water-level declines, and renewed aquifer compaction.
- Resolved Jordan’s short link `https://share.google/NTs3sZSCGsDBph3Vf` to `https://www.usgs.gov/mission-areas/water-resources/science/land-subsidence#overview` (200). The page is *Land Subsidence*, Water Resources Mission Area, March 2, 2019. The Ireland caption and the national 80-percent sentence were confirmed. The media-details page for the photograph also returned 200 and does not print BM S661.
- Applied both challenges. No A1–A8 term was needed. THEORY_MAB arms were not developed. `main` remains `37522fc` and was not edited.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-usgs-01 | accepted | The protocol was locked before either row was scored, and the retrieval result was recorded first. |
| C-usgs-02 | accepted-with-revisions | Both challenges **hit**. CV-11 is `supported-with-limit` with the pre-registered service limit and the transfer limit kept. CV-14 is `supported-with-limit`; 9 m stays a single point, 80 percent stays national, and BM S661 is not treated as a page finding. |

## Challenge dispositions

| Challenge | Disposition |
|---|---|
| [CH-usgs-service-and-transfer](../challenges/CH-usgs-service-and-transfer.md) | **Hit.** The ruled CV-11 row and the TL;DR keep the limit that whether pumping maintained delivered water service during those episodes remains open, and they do not transfer the episodes or the Faunt / Lees and Knight volumes to Tulare Lake. |
| [CH-usgs-cv14-limits](../challenges/CH-usgs-cv14-limits.md) | **Hit.** The ruled CV-14 row keeps the point-versus-valley and national-80-percent limits, cites the canonical usgs.gov URL, and notes that BM S661 is not printed on the page. |

## What this is not

Not a Layer 0 or theory failure, not a Tulare Lake 5-022.12 result, not a finding that delivered service was maintained in the episode windows, not an assignment of A1–A8, and not a publication to `main`.
