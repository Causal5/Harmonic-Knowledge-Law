# Retrieval log — Round 29, 25 November 2026 (America/New_York)

## Stage 1 — Kelner and Sietman (2000)

DOI 10.1080/02705060.2000.9663755. No paywall was circumvented. No shadow-library copy was used.

| Route | URL or query | Result |
|---|---|---|
| OpenAlex work record | https://api.openalex.org/works/https://doi.org/10.1080/02705060.2000.9663755 | 200. `is_oa` true, status bronze. `any_repository_has_fulltext` false. Only location is the Taylor & Francis PDF. SHA-256 of the saved JSON excerpt is recorded with the file. |
| Unpaywall | https://api.unpaywall.org/v2/10.1080/02705060.2000.9663755 | 200. `has_repository_copy` false. Best location is the same T&F bronze PDF (`evidence`: deprecated). Saved as `sources/unpaywall_kelner_2000.json`. |
| Crossref | https://api.crossref.org/works/10.1080/02705060.2000.9663755 | 200. No abstract field. Link is the T&F PDF. Pages 371–377, volume 15, issue 3. |
| Semantic Scholar | DOI query, paper `c349a1a4855c3a15c4e755088c6121f023fa6e04` | 200. `isOpenAccess` true, status BRONZE, same T&F PDF URL. Abstract elided. |
| Taylor & Francis PDF / epdf / full text | https://www.tandfonline.com/doi/pdf/10.1080/02705060.2000.9663755?needAccess=true&role=button and related paths | HTTP 403, Cloudflare “Just a moment...” challenge page, not a PDF. |
| DOI resolver | https://doi.org/10.1080/02705060.2000.9663755 | HTTP 500 at retrieval time. |
| Europe PMC | DOI search | 0 hits. |
| CORE | DOI search, work 223022851 | 200. `downloadUrl` empty; `sourceFulltextUrls` empty; `fullText` “Not available for public API users.” Data provider: Crossref only. |
| Internet Archive advanced search | Kelner Sietman Ebony Shell | 0 documents. |
| DOAJ article search | doi:10.1080/02705060.2000.9663755 | 0 results. |
| ORCID for Bernard Sietman | https://orcid.org/0000-0002-5921-4391 | 200. The 2000 work is listed with the DOI only; no author-manuscript URL. |
| Google Scholar | query for the title | HTTP 403 “Sorry...” page. |
| Minnesota DNR search path | /search.html?query=Sietman Kelner ebena | HTTP 404. A later DNR field-guide PDF was not treated as this article. |
| OpenAIRE | DOI search | Metadata only; collected from Unpaywall, Crossref, and MAG. No additional repository PDF. |

Authors’ 2000 affiliation in OpenAlex/Unpaywall is Ecological Specialists, Inc., St. Peters, Missouri. No institutional-repository or agency reprint of this article was retrieved.

**Stage 1 outcome:** Limb A fails. Full text unobtainable by the locked legitimate routes in this session. Unpaywall and OpenAlex *describe* a bronze publisher PDF, but that file was not in hand (403 challenge), and both services report no repository copy. This does not prove that the paper lacks rates.

## Stage 2 — GSP Appendix D (opened after Stage 1 was unobtainable)

| Source | URL | Result |
|---|---|---|
| California Water Library, 2022 Amended GSP page | https://cawaterlibrary.net/document/tulare-lake-subbasin-groundwater-sustainability-plan-amended/ | 200. SHA-256 `d775f8b52221cbaadab9566014123754bf9589418251ebff30f263c5913efd14`. Lists six PDF parts. |
| 2022 Amended GSP Part 3 | https://cawaterlibrary.net/wp-content/uploads/2023/11/Pt-3-from-2022-Tulare-Lake-Amended-GSP-and-Addendum-4.pdf | 200, application/pdf, 24,623,078 bytes, SHA-256 `47cafbd1f63cdcb000c04da750a906a14ebf1b2594616ce191d454fcc1e5aa2f`. Contains Appendix D, Groundwater Model Report (Wood, 8 January 2020). Full PDF not committed; excerpt in `sources/gsp_appendix_d_excerpt.txt`. |
| A mistyped Part 2 URL ending Addendum-2.pdf | first guess from an incomplete citation | HTTP 404. The live Part 2 URL uses Addendum-3. |
| WY 2025 Annual Report (already held locally) | https://sgma.water.ca.gov/portal/service/gspar/document/5821 | Reused. Its own Appendix D is groundwater-quality data, not the GSP model report. The body cites GSP Appendix D, Section D2-3 and page 26, for farm-demand / efficiency calculations. |

The 2019 draft hydrologic-model PDF on southforkkings.org was also retrieved (HTTP 200, 85,890,996 bytes, SHA-256 `d110110cfbce40e39aaf3a171a2e59592e04db8b542abbba2e1177cf85b4d35b`) but was not used as the scored source, because the official 2022 GSP Appendix D in Part 3 is the document the annual report cites.
