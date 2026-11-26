# Verdict: Session 3 claim-table rescoping

**TL;DR.** Accept with revisions. Twenty-eight simple claims were extracted, attacked, narrowed, and ruled: 2 supported, 25 supported-with-limit, 1 partial (CV-11, because the cited USGS San Joaquin Valley subsidence URL did not resolve), 0 unsupported, 0 needs-definition. All three challenges hit as wording or verification risks and were addressed in `ai/CLAIMS.md`. This is not a Layer 0 test, not a new field dataset, and not a publication to `main`.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-25-claim-table-rescoping/`

**Date:** 2026-11-25, America/New_York

## Checks run

- Confirmed the protocol and extraction (`615aa69` / `3ee21a9`) precede the attack (`eebabe7` / `2488d38`) and this verdict.
- Applied the three challenges to each extracted row and narrowed wording rather than dropping claims.
- Resolved unique extraction URLs and checked distinctive wording for Oro Grande (USGS 70199565), Kraemer (eScholarship PDF), Faunt (158 km³ / 15%), Lees and Knight (14 km³), SIR 2024-5009 (hundreds to thousands / tens of thousands of years), NPS skipjack / Keokuk 1913, Waterways Council Lock and Dam 22 near Saverton, Whitledge establishment, Poulton 2019 and 2021 consumption figures, Larson biofouling and refugia, beaver lag +55.9% / −17.5%, and Panama pasture peak runoff 1.7× forest.
- Confirmed no row uses or needs an undefined A1–A8 term, and that THEORY_MAB arms were not developed.
- Confirmed `main` remains `37522fc` and was not edited.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-claims-01 | accepted | The protocol was locked before any row was scored. |
| C-claims-02 | accepted-with-revisions | All three challenges **hit**. The master table narrows overreach (including MU-01, CV-01, SA-02, and rabi-as-service language), adds missing links and uncertainties, keeps unverified clauses visible, and records the one partial row. |

## Challenge dispositions

| Challenge | Disposition |
|---|---|
| [CH-claims-overreach](../challenges/CH-claims-overreach.md) | **Hit.** MU-01 narrowed to “may then be needed”; CV-01 attributes the six-year figures to summed annual rows; SA-02 drops the unstudied equal-budget sentence as an empirical claim; PAE-01’s PAE-effectiveness gloss is marked as a corpus comment; CV-02 keeps rabi area from being read as deliveries; PAE-03, PAE-04, and CV-12 stay inside the studied sites or regions. |
| [CH-claims-mislink-unverified](../challenges/CH-claims-mislink-unverified.md) | **Hit.** MU-05 now links and quotes the Waterways Council page for Lock and Dam 22 / Saverton. MU-03 does not leave Larson carrying the filtration point. MU-06 links Poulton 2019 and 2021 and uses their abstracts. Page-anchor, Qiaozigou-timing, abstract-only Oro Grande, and the unresolved USGS episode URL remain visible. The “thousands of years” clause was confirmed in SIR 2024-5009 and kept, narrowed to the southeastern San Joaquin Valley. No invented citations. |
| [CH-claims-missing-limit](../challenges/CH-claims-missing-limit.md) | **Hit.** CV-03 now includes 88.3 ± 17% and 32.7 ± 26.3%. CV-06 names all three windows. CV-07 and CV-08 stay object-class / completeness results. MU-02 / MU-04 do not say the Kelner paper lacks rates. Transcription limits on CV-09, CV-10, and CV-13 are stated. No `needs-definition` ruling for A1–A8; no theory arm developed. |

## What this is not

Not a Layer 0 or theory failure, not an assignment of A1–A8, \(\eta\), *severed*, \(C_{irr}\), \(Q_{sw}\), or \(D_W\), not a restoration of withdrawn Sahel wording, not a development of ARM-06 or ARM-07, and not a publication to `main`.
