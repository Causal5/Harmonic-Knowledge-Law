# Pre-registration: citation check of the published hydrological PAE pages

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 25, 25 November 2026).** Not a publication to `main`. Written before this test assigned hold, break, or indeterminate to each locked claim.

**TL;DR.** This test asks whether the papers and reports cited on the published Paani PAE page, and in the new Central Valley v0.2 passages that use them, actually exist and say what those pages claim. A contradicted or fabricated claim is a **break**. An unretrieved source with no official abstract is **indeterminate**. Page-anchor offsets and unretrieved full texts are recorded, not silently fixed in the published pages.

**Parents.** `Release/Examples/paani-water-cup-hydrological-pae.md` and `Release/Examples/central-valley/central-valley-worked-example-v0.2.md` as published on `main` at `37522fc` (byte-identical on this branch at `9edff38`). Empirical review procedure on `main`. No new definition is introduced. A1–A8 remain undefined.

## Locked claims under test

Primary claims (Jordan’s 25 November summary and the two published pages):

1. **Water Cup 2019 scale.** The 2019 competition involved 4,706 villages. The Foundation estimated that the works added 232.13 billion litres of storage capacity, described as potential capacity. Source: Water Cup 2019 report, cited at `#page=27`.
2. **Drought-year evaluation design.** The evaluation followed the 2018 competition cohort through May 2019, with 971 dug wells in 100 high-performing Water Cup villages and 655 wells in 67 geographically matched comparison villages, and with 96 of 167 villages in areas more than 40% below normal rainfall. Source: same report, Tables 1–4, cited at `#page=19`.
3. **Table numbers.** The well-level and winter-sown-area figures in the published Paani table, including the Marathwada pairing used in Central Valley v0.2 (36.17% vs 24.90% winter area; wells fell 0.63 vs 0.42 m). Source: Tables 3–4, cited at `#page=21`.
4. **Foundation explanation and limits.** The Foundation proposed irrigation demand as an explanation of the Marathwada/North Maharashtra contrast. The comparison is selected villages over one drought year; some comparison villages could have received government watershed works; data checks were pending; the tables give no metered irrigation volumes.
5. **Samruddha Gaon follow-on.** 18,649 water-level readings from 7,359 wells in 734 villages over roughly a year; a crop survey in 600 villages recorded area planted and irrigation method; the published summaries do not identify a matched continuation of the original Water Cup cohort. Source: 2021–22 annual report, cited at `#page=4`.
6. **Modesto / Zhou.** At three flooded orchard plots near Modesto, researchers sampled a bromide tracer and logged soil moisture every ten minutes, and detected the tracer down to five metres in the deepest instrumented profile. Source: Zhou and colleagues, §2.2 and Figure 6, Madera County Water PDF.
7. **Oro Grande / Izbicki.** Recharge first reached the water table 117 metres below ground after three years; once the sediments had wetted, it took one year. Source: Izbicki, Flint and Stamos, 2008, doi:10.1111/j.1745-6584.2007.00406.x.
8. **Kraemer / Clark.** Tracers connected the recharge pond to specific wells; repeat tests found consistent travel times to most wells. Source: Clark and colleagues, 2014, doi:10.3390/w6061826.

Secondary claims added in the same `main` commits (Central Valley v0.2, three models and runoff delays):

9. **Tulare orchard model (Perzan et al.).** Across 284 simulations, additional drainage below the root zone was about 88% of applied water 14 days after the last flooding; after two years, median saturated-zone recharge was 32.7% (range 0.28–87.7%). Source: https://hess.copernicus.org/articles/27/969/2023/ (Figs. 5–8).
10. **Beaver dam lag.** In a paired English catchment study, lag from peak rainfall to peak discharge increased by 56% after beavers established dams and shortened by 18% at the comparison site. Source: doi:10.1002/hyp.14735.
11. **Panama land cover.** A grazed pasture catchment had 1.7 times the peak storm runoff rate of a forested catchment. Source: doi:10.1002/2013WR013956.
12. **Contour-bund delay.** On cultivated slopes in central India, one contour-bund treatment delayed the onset of runoff by 9–72 minutes relative to cultivation up and down the slope. Source: https://indianjournals.com/article/ijsc-47-3-010.
13. **Qiaozigou.** Adjacent hill-and-gully catchments, 1988–2018; at comparable rainfall, less water and sediment per unit area passed the treated outlet, already during hillside work. Source: doi:10.3390/su12208376.
14. **Marking-system cite.** Water Cup design §§3–5 and 10 support the statement that the Foundation scored construction and monitored what followed. Source: 2019 marking-system PDF.

## Pre-registered outcomes

For each locked claim:

- **Holds** if a retrieved source (full text, or an official abstract from Crossref, Europe PMC, or the USGS Publications Warehouse) exists and states the claimed fact, allowing ordinary rounding (for example 55.9% reported as 56%) and documented unit conversion (for example Indian crore litres to billion litres) that is shown in the fill.
- **Breaks** if the retrieved source contradicts the claim (wrong number, wrong site, or the opposite finding), or if the cited work does not exist.
- **Indeterminate** if the cited source cannot be retrieved in this check and no official abstract containing the claimed fact is available.

The **round-level** outcome is:

- **Breaks** if any primary claim (1–8) breaks.
- **Holds** if every primary claim holds and no secondary claim breaks (secondary indeterminates are allowed).
- **Otherwise indeterminate.**

Page-number anchors that are off by a few PDF pages, or a closed full text whose official abstract already states the claim, are recorded as limits. They do not by themselves break a claim whose wording checks out. This test does not rewrite the published pages, invent a definition, construct \(V\), or score Bite 5.

## What this test will not do

- Treat an official abstract as a substitute when the claim is not in that abstract.
- Invent a citation, number, or quotation.
- Use A1–A8 as if defined.
- Merge the findings into a Tulare recharge volume or a Bite 5 score.
