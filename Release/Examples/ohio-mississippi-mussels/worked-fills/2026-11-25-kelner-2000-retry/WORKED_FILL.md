# Worked fill: Kelner and Sietman (2000) retry and Appendix D fallback

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 29, 25 November 2026).** Not a publication to `main`. Scored after the pre-registration at `b83bd3c`.

**TL;DR.** Stage 1, the legitimate-route retry of Kelner and Sietman (2000), did not put a full text in hand (Limb A fails). Unpaywall and OpenAlex describe a bronze Taylor & Francis PDF and report no repository copy; the publisher returned a Cloudflare 403 challenge, and author, IR, USGS, CORE, DOAJ, Internet Archive, and ORCID routes also yielded no file. Stage 1 is **unobtainable**. That is not a finding that the paper lacks rates. \(\eta\) and *severed* stay unassigned. Stage 2 then retrieved the 2022 GSP Appendix D groundwater-model report. The report documents irrigation-efficiency assumptions (75%, then 85%; 95% on the lake bottom) used in the farm-demand equation, and it treats imported groundwater as a separate supply. It does not document a conveyance-efficiency number or method that can be applied to the Table 3-1 ex-Imported columns without inventing an identification; canal seepage is described as having little available information. Under the locked Round 24 rule the candidate \(Q_{sw}\) stays unfilled. Stage 2 is **indeterminate** (data gap). The subset is not \(D_W\). ARM-06 stays `wait`. No Sahel sites were invented.

**Parents.** [PREREG](PREREG.md) · Round 22 ebonyshell fill · Round 24 Table 3-1 mapping · `main` at `37522fc`.

## Stage 1 — Kelner full-text retry

Legitimate routes listed in the pre-registration were attempted and logged in [retrieval_log.md](retrieval_log.md). The only “open” location reported by OpenAlex and Unpaywall is the publisher PDF. That request, and the epdf and full-text pages, returned HTTP 403 Cloudflare challenge pages, not a PDF. Both services report that no repository copy exists. Sietman’s ORCID record lists the DOI only. CORE, DOAJ, Europe PMC, Internet Archive, and the DOI resolver did not supply a full text.

**Limb A:** fails (full text not in hand). **Limb B:** not scored. **Stage 1:** unobtainable. Procedure check: no flags were assigned from a non-legitimate copy.

## Stage 2 — GSP Appendix D fallback

Opened only after Stage 1 was unobtainable. The official Appendix D is the Groundwater Model Report (Wood, 8 January 2020), retrieved as Part 3 of the 2022 Amended GSP from the California Water Library (PDF SHA-256 `47cafbd1f63cdcb000c04da750a906a14ebf1b2594616ce191d454fcc1e5aa2f`). The Water Year 2025 annual report’s own Appendix D is groundwater-quality data and is not this document. Excerpts are in [sources/gsp_appendix_d_excerpt.txt](sources/gsp_appendix_d_excerpt.txt).

What the retrieved report supplies:

- Surface-water diversions and deliveries for lands in the subbasin were taken from GSA and member-agency records (section 2.8.1.2). Imported groundwater from Tule Subbasin well fields (Creighton Ranch and Angiola) is a separate supply (section 2.8.1.3). Lake-bottom storage is stored surface water (section 2.8.1.4).
- In the simple water-balance used to estimate agricultural pumping, “Surface Water Supplies include Surface Water Deliveries, imported groundwater, and lake bottom water storage” (section 2.8.2.4). That is why the Imported column was already excluded in Round 24. It does not, by itself, show groundwater mixing inside the Kings, Kaweah, Tule, Deer, Poso, SWP, and CVP columns.
- Farm Demand is computed from crop demand divided by Irrigation Efficiency. Over most of the model domain that efficiency is assumed to be 75% from 1990 to 2000 and 85% from 2000 onward (95% on the lake bottom). The Water Year 2025 filing points to this discussion as “GSP Appendix D, page 26” / “Section D2-3.” In the 8 January 2020 report the 85% assumption is on the farm-demand pages (printed pages 25–26 of the model report). No section literally titled “D2-3” for a conveyance correction was found; Table D2-3 is historical Kings River diversions, and section 2.3 is geology.
- On canal seepage: “There was little available information on seepage losses in the Subbasin,” with anecdotal reports of substantial losses near some head gates (section 2.8.1.6). The phrase “conveyance efficiency” does not appear in the Appendix D excerpt of the model report.

**Application of the locked rule.** The appendix was retrieved, so Stage 2 is not a retrieval gap. The appendix does not show that the ex-Imported column set mixes groundwater, so the candidate is not broken on that limb. It also does not document a conveyance-efficiency correction, as a number or method, that can be applied to those Table 3-1 columns without inventing an identification. The 85%/95% figures are irrigation efficiency in the farm-demand equation, not a documented headgate-to-turnout conveyance factor. Treating 85% as that missing correction would be invention. Therefore the ex-Imported subset remains a candidate only and is not a locked dictionary \(Q_{sw}\). It is not \(D_W\). Stage 2 is **indeterminate**. Cause: data gap.

## Round-level outcome

**Indeterminate.** Stage 1 unobtainable; Stage 2 a data gap on the conveyance correction. Not a Layer 0 or theory failure. \(\eta\), *severed*, and the Table 3-1 ex-Imported \(Q_{sw}\) fill stay unassigned. ARM-06 stays `wait`.

## What this fill does not do

- Circumvent a paywall or use a shadow copy.
- Claim that the unretrieved Kelner PDF lacks rates.
- Apply 85% irrigation efficiency as if it were a locked conveyance correction.
- Treat the candidate subset as \(D_W\), or invent Sahel sites, or develop ARM-06.
- Evaluate the temporal-mining conjunction or edit `main`.
