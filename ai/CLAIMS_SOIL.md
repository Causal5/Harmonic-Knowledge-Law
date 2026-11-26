# Simple claims: industrial farming, soil loss, and humus / SOM

**TL;DR.** In retrieved specialist studies, conventionally plowed fields erode much faster than soil forms, the midwestern U.S. Corn Belt has lost a substantial share of its carbon-rich A-horizon, and agricultural land use has created a large global soil-carbon debt that is not uniform everywhere. Soil organic matter is tied to crop yield up to about 2% soil organic carbon, but its average effect on plant-available water is modest. On the long-running Broadbalk wheat experiment, grain yields can be similarly high with mineral fertilizers alone or with farmyard manure plus fertilizer, while plough-layer organic matter is much higher where manure is applied every year. That is a real service-versus-condition contrast, not a finding that fertilizer depletes organic matter relative to unfertilized cropland, and not complete decoupling: yields still rise with organic carbon up to about 2%, and complete A-horizon loss has been associated with a small yield reduction. Organized practices can raise organic carbon, sometimes quickly at first, but no-till gains are often a change in depth distribution rather than a whole-profile increase, cover-crop rates were compiled for a shallow layer, and long-term accumulation moves toward a new equilibrium and can reverse if the practice stops. No best-fit study in this table is agrochemical-manufacturer funded; conservation-NGO, foundation, and CGIAR funding are labeled where they appear.

This table is a new-domain product on `ai/evolution` (25 November 2026). It is not a publication to `main`, not a Layer 0 test, and not a developed THEORY_MAB arm. Wording was narrowed after the adversarial pass rather than dropping rows. A1–A8 stay undefined. The water-domain table remains [`ai/CLAIMS.md`](CLAIMS.md).

## Counts by ruling

| Ruling | Count | IDs |
|---|---:|---|
| supported | 0 | — |
| supported-with-limit | 9 | SOIL-01–SOIL-09 |
| partial | 0 | — |
| unsupported | 0 | — |
| needs-definition | 0 | — |
| **Total** | **9** | |

No row needed an undefined A1–A8 term. No industry-funded source is used as a best-fit study. Candidate wordings that were **not** extracted, and were not restored at C: “synthetic nitrogen fertilizer depletes SOM” (the Khan et al. 2007 reading); Dust Bowl SCS as a locked SOM-rebuild-rate study; Rodale as a best-fit long-term trial (full text not retrieved); SOM “underpins soil structure” (no extracted structure study).

---

### SOIL-01 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | Conventionally plowed agricultural fields, taken as a global compilation, erode on average one to two orders of magnitude faster than measured soil-production rates, erosion under native vegetation, or long-term geological erosion. |
| **Best-fit study** | Montgomery, D.R. (2007), “Soil erosion and agricultural sustainability,” *PNAS* 104:13268–13272. Verified classic baseline, not the newest industrial-cropland work. |
| **What it shows** | Compiled conventional-agriculture erosion: median 1.537 mm/yr, mean 3.939 mm/yr (n=448). Soil production: median 0.017 mm/yr, mean 0.036 mm/yr (n=188). Native vegetation erosion: median 0.013 mm/yr (n=65). Conservation agriculture: median 0.082 mm/yr, mean 0.124 mm/yr (n=47). The paper argues that plow-based rates are unsustainable on upland soils, while no-till rates are much closer to production rates. |
| **Limit** | A global compilation of heterogeneous methods and sites, not a single controlled experiment and not a measurement of soil organic matter. Floodplain settings, where flooding can refresh mineral soil, are distinguished from upland thinning. “Conservation agriculture” in the table is a smaller sample than conventional agriculture. This row is not a substitute for SOIL-02 on industrial cropland. |
| **Funding / affiliation** | David R. Montgomery, Department of Earth and Space Sciences, University of Washington. The PMC text thanks Mark Nearing for data and declares no conflict of interest. No manufacturer funder is listed. **Not industry-funded.** |
| **Link** | [PNAS / DOI](https://doi.org/10.1073/pnas.0611508104) · [PMC1948917](https://pmc.ncbi.nlm.nih.gov/articles/PMC1948917/) (wording and Table 1 confirmed) |
| **Support** | PMC full text and Table 1 retrieved in this session. |

### SOIL-02 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | In the midwestern United States Corn Belt, a substantial share of cultivated land has completely lost its carbon-rich A-horizon. |
| **Best-fit study** | Thaler, E.A., Larsen, I.J. & Yu, Q. (2021), “The extent of soil loss across the US Corn Belt,” *PNAS* 118:e1922375118. Preferred newer work for a major industrial cropland region. |
| **What it shows** | Scaling from satellite and LiDAR relationships between A-horizon loss and topographic curvature across 3.9 × 10⁵ km², the authors estimate that 35 ± 11% of the cultivated area has lost A-horizon soil, and that prior soil-survey-based estimates understated this complete A-horizon loss. Convex hilltops are often denuded. The paper links the pattern to tillage-induced erosion, which is not simulated in the nationwide models it discusses, and estimates 1.4 ± 0.5 Pg of carbon removed from hillslopes, a 6 ± 2% yield reduction, and $2.8 ± $0.9 billion in annual economic losses. Much of the eroded carbon “likely remains buried in depositional areas within the fields.” |
| **Limit** | This is complete A-horizon loss, not a partial-thinning inventory, and it is one region, not all industrial cropland. The 35% figure is a scaled estimate with a ±11 percentage-point uncertainty. In-field deposition means the carbon is not necessarily lost from the field. The 6 ± 2% yield reduction is a limit on any claim that yields are fully insulated from this soil loss. |
| **Funding / affiliation** | University of Massachusetts Amherst, Department of Geosciences. Supported by NASA (80NSSC18K0747 P0004) and NSF (1653191) grants to I.J.L. The authors declare no competing interest. **Not industry-funded.** |
| **Link** | [PNAS / DOI](https://doi.org/10.1073/pnas.1922375118) · [PMC7923383](https://pmc.ncbi.nlm.nih.gov/articles/PMC7923383/) (wording confirmed) |
| **Support** | PMC full text and acknowledgments retrieved in this session. |

### SOIL-03 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | Agricultural land use has created a large global soil-organic-carbon debt, with loss concentrated in some major cropping and grazing regions, while other agricultural zones show small losses or even net gains. |
| **Best-fit study** | Sanderman, J., Hengl, T. & Fiske, G.J. (2017), “Soil carbon debt of 12,000 years of human land use,” *PNAS* 114:9575–9580. |
| **What it shows** | A machine-learning model, projected onto a no-agriculture counterfactual, estimates a global carbon debt due to agriculture of 133 Pg C in the top 2 m of soil, with the rate of loss increasing dramatically in the past 200 years. Grazing and cropland contributed nearly equally in total; percent losses were higher on cropland, but more land is grazed. Hotspots coincide with some major cropping regions and semiarid grazing regions. Some major agricultural zones showed small losses or net gains. |
| **Limit** | This is a modeled counterfactual, not a single field trial. The authors note that comparison with remnant native plots suggests the estimate may be conservative. It is a land-use debt (cropland and grazing), not a verdict on fertilizer or on “industrial farming” alone. Regional gains mean the global total must not be read as uniform loss everywhere. |
| **Funding / affiliation** | Woods Hole Research Center (Sanderman, Fiske); ISRIC – World Soil Information (Hengl). Funding was provided by The Nature Conservancy and the Doris Duke Charitable Foundation. ISRIC is a nonprofit foundation primarily funded by the Netherlands government. The authors declare no conflict of interest. **Not industry-funded.** **Conservation-NGO and foundation funding is labeled.** |
| **Link** | [PNAS / DOI](https://doi.org/10.1073/pnas.1706103114) · [PMC5594668](https://pmc.ncbi.nlm.nih.gov/articles/PMC5594668/) (wording and acknowledgments confirmed) |
| **Support** | PMC full text retrieved in this session. |

### SOIL-04 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | Increasing soil organic carbon has only a modest effect, on average, on plant-available water capacity. A 1% mass increase in soil organic carbon increases available water capacity by about 1.16 mm of water per 100 mm of soil, with a larger effect in sands and a smaller effect in clays. |
| **Best-fit study** | Minasny, B. & McBratney, A.B. (2018), “Limited effect of organic matter on soil available water capacity,” *European Journal of Soil Science* 69:39–47. Newer work used to narrow the popular “SOM underpins water holding” wording. |
| **What it shows** | A meta-analysis of 60 published studies and a large global database. A 1% mass increase in soil OC (about 10 g C kg⁻¹ mineral soil) increases water content at saturation, field capacity, wilting point, and available water capacity by, on average, 2.95, 1.61, 0.17, and 1.16 mm H₂O per 100 mm soil, respectively. The authors conclude that the plant-available-water increase with organic matter may be overestimated, and that carbon sequestration from conservation agriculture is unlikely to materially increase soil water storage. |
| **Limit** | This row supports the modest-effect wording, not the original candidate claim that SOM “underpins water holding.” It does not say SOM is irrelevant to soil physics, only that the available-water effect is small on average and texture-dependent. The publisher page was not retrieved as a full PDF in this session; the figures above are from the Crossref abstract. |
| **Funding / affiliation** | Sydney Institute of Agriculture, The University of Sydney. Crossref lists an Australian Research Council Future Fellowship as a funder. **Not industry-funded** on the retrieved metadata. |
| **Link** | [DOI](https://doi.org/10.1111/ejss.12475) (Crossref abstract wording confirmed; publisher full text not retrieved) |
| **Support** | Crossref abstract retrieved in this session. |

### SOIL-05 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | For maize and wheat, yields are on average greater at higher soil organic carbon, but the yield increase levels off at about 2% SOC. About two-thirds of the world’s cultivated maize and wheat lands are below that level. Nitrogen fertilizer is a co-varying management factor, not a complete substitute for SOC at low concentrations. |
| **Best-fit study** | Oldfield, E.E., Bradford, M.A. & Wood, S.A. (2019), “Global meta-analysis of the relationship between soil organic matter and crop yields,” *SOIL* 5:15–32. |
| **What it shows** | A mixed model of 834 observations from 90 studies, controlling for N fertilizer rate, irrigation, climate, pH, and texture. Yields of maize and wheat are on average greater with higher SOC and level off at ~2% SOC. The authors also explore whether higher SOC could reduce reliance on N fertilizer; that is a modeled potential, not a farm-scale demonstration in this paper. |
| **Limit** | A global statistical relationship, not a single long-term trial. “Levels off at ~2%” is an average, not a universal agronomic target. The paper does not by itself prove a structure or biology mechanism. It is a limit on a complete service-versus-condition decoupling story: even after accounting for N fertilizer, yield still rises with SOC up to about 2%. |
| **Funding / affiliation** | Yale School of Forestry and Environmental Studies (Oldfield, Bradford, Wood); Wood also lists The Nature Conservancy, Arlington, VA. The paper thanks the SNAPP working group on “Managing Soil Carbon.” The authors declare no conflict of interest. No manufacturer funder is listed. **Not industry-funded.** **A conservation-NGO co-affiliation is labeled.** |
| **Link** | [SOIL article / PDF](https://soil.copernicus.org/articles/5/15/2019/) (200; OA PDF wording confirmed) |
| **Support** | Official OA PDF retrieved in this session. |

### SOIL-06 — supported-with-limit (key decoupling row)

| Field | Text |
|---|---|
| **Claim** | On a long-running arable experiment, grain yields can be similarly high with mineral fertilizers alone or with farmyard manure plus fertilizer, while plough-layer soil organic matter is much higher where farmyard manure is applied annually than where only mineral fertilizers are used. |
| **Best-fit study** | Rothamsted Research, *Broadbalk Wheat Experiment* official handout (2024), reporting the long-term Broadbalk trial (started 1843), read with the SOC-accumulation limits in Poulton et al. (2018). |
| **What it shows** | The 2024 handout states that the largest yields now exceed 13 t ha⁻¹ with either fertilizers only or FYM plus extra N in spring, and that “it is possible to maintain or increase yield with manure or fertilizers alone or a combination of both.” Long-term FYM at 35 t ha⁻¹ yr⁻¹ has “more than doubled the SOM (organic C × 1.72) content of the plough layer (0–23 cm),” with larger increases in the early years; “as SOM approaches equilibrium,” much of the more recently added FYM carbon has been lost. “Mineral N fertilizer enhanced SOM a little, probably due to increased returns of organic matter in crop roots and above ground residues,” while soils with no additional inputs have remained relatively constant. This is the strongest retrieved evidence for a service (yield) versus condition (SOM) contrast on the same soil, under documented management. |
| **Limit** | One soil type at one site. The contrast is fertilizer-only versus FYM (and versus unfertilized arable), not fertilizer versus native prairie, and not a finding that fertilizer depletes SOM relative to unfertilized cropland. Structure and soil biology are not separately measured in the handout sentences used here. The yield-and-SOM sentences are from an official institutional handout, not a single journal article; Poulton et al. (2018) is the retrieved peer-reviewed complement for equilibrium and reversal. Oldfield (SOIL-05) and Thaler’s 6 ± 2% yield reduction (SOIL-02) show that yield is not fully independent of soil condition. High fertilized yields do not prove that soil condition is intact. |
| **Funding / affiliation** | Rothamsted Research. The Long-Term Experiments National Bioscience Research Infrastructure is funded by UKRI-BBSRC (award BBS/E/RH/23NB0007, 2023–2028) and supported by the Lawes Agricultural Trust. Poulton et al. (2018) were funded by BBSRC grant BBS/E/C/000J0300. **Not industry-funded.** Public UK research institute, with a historical agricultural-trust endowment. |
| **Link** | [Broadbalk 2024 handout (PDF)](https://www.era.rothamsted.ac.uk/metadata/rbk1/Broadbalk_handout_2024.pdf) (200; wording confirmed) · [Poulton et al. 2018](https://doi.org/10.1111/gcb.14066) · [Rothamsted OA PDF](https://repository.rothamsted.ac.uk/id/eprint/93/1/Poulton_et_al-2018-Global_Change_Biology.pdf) (200) |
| **Support** | Official 2024 handout and Poulton et al. 2018 OA PDF retrieved in this session. |

### SOIL-07 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | Switching from conventional tillage to no-till often increases organic-carbon concentration near the surface, which can improve some soil properties, but much of the apparent carbon gain is a change in depth distribution rather than a large increase in whole-profile stock. Where paired sites were sampled to at least 40 cm, larger stocks in the top 20 cm were counteracted by smaller quantities at 20–40 cm, with no overall increase in the comparison reported. |
| **Best-fit study** | Powlson, D.S. et al. (2014), “Limited potential of no-till agriculture for climate change mitigation,” *Nature Climate Change* 4:678–683. |
| **What it shows** | The authors argue that claims of substantial climate mitigation via no-till carbon sequestration are widely overstated. A comparison of 69 paired no-till and conventional-till data sets sampled to at least 40 cm showed no overall increase in SOC stock under no-till. Surface concentration is generally beneficial for soil properties that often, though not always, translate into improved crop growth. In many regions, soil is cultivated conventionally every few years, so any carbon benefit may then be lost. They still regard no-till as beneficial for soil quality and climate adaptation. This is a limit on “no-till rebuilds SOM / sequesters carbon,” not a finding that no-till has no agronomic value. |
| **Limit** | This is a perspective that synthesizes prior meta-analyses, not a new field trial. Erosion reduction (SOIL-01 conservation-agriculture rates) is a separate claim and is not cancelled by this stock-distribution result. Herbicide- or equipment-industry messaging that treats no-till as large-scale carbon sequestration is not supported by this paper; the paper itself is not an industry source. |
| **Funding / affiliation** | Rothamsted Research (Powlson); CIMMYT / CGIAR (Stirling, Jat, Gerard); Earth Institute, Columbia University (Palm, Sanchez); University of Nebraska-Lincoln (Cassman). Acknowledgements: parts of the work came from CIMMYT studies funded by the CGIAR Climate Change, Agriculture and Food Security (CCAFS) programme. The authors declare no competing financial interests. **Not industry-funded.** **CGIAR / international public-research funding is labeled.** |
| **Link** | [Journal DOI](https://doi.org/10.1038/nclimate2292) · author-posted PDF used for wording: [GWCT copy](https://www.gwct.org.uk/media/841523/Powlson-2014-Limited-potential-for-no-till.pdf) (200; wording and acknowledgments confirmed) |
| **Support** | Retrieved PDF (14 pp.) in this session. |

### SOIL-08 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | Replacing winter fallows with cover crops can increase soil organic carbon stocks in the sampled layer at an average rate on the order of 0.32 Mg C ha⁻¹ yr⁻¹, but a new steady state has to be modeled rather than assumed to go on rising linearly forever, and the compiled observations were for a shallow average depth. |
| **Best-fit study** | Poeplau, C. & Don, A., published journal version: “Carbon sequestration in agricultural soils via cultivation of cover crops – A meta-analysis,” *Agriculture, Ecosystems & Environment* (2015), doi:10.1016/j.agee.2014.10.024. Wording below is taken from the authors’ official 2014 EGU abstract of that meta-analysis, which was retrieved; the 2015 journal PDF was not. |
| **What it shows** | The official EGU abstract (same authors) reports a meta-analysis of 33 studies, 47 sites, and 147 plots. SOC stock change was a linear function of time since introduction, with an annual sequestration rate of 0.32 Mg C ha⁻¹ yr⁻¹. No saturation was visible in the observations, so the authors used RothC to estimate a new steady-state level; the total average SOC stock change was 16.76 Mg C ha⁻¹ for an average soil depth of 22 cm, and they estimated a potential global sequestration of 0.12 ± 0.03 Pg C yr⁻¹. |
| **Limit** | The 2015 journal article may have updated plot counts or uncertainty intervals relative to the 2014 abstract; those updates were not retrieved here. Average depth is only 22 cm, so this is not a deep-profile stock result (see SOIL-07). “No saturation visible in the observations” is not the same as no long-term equilibrium: Poulton et al. (SOIL-09) show that SOC accumulation moves toward equilibrium when practices run for many decades. Cover crops are one organized practice, not a complete reconstruction of lost A-horizon or humus stocks. |
| **Funding / affiliation** | Swedish University of Agricultural Sciences (Poeplau) and Thünen Institute of Climate-Smart Agriculture, Germany (Don, and Poeplau). Crossref lists the EU project GHG-Europe (grant 244122) as a funder of the 2015 paper. **Not industry-funded.** Public research institutes. |
| **Link** | [2015 journal DOI](https://doi.org/10.1016/j.agee.2014.10.024) (existence confirmed) · [official 2014 EGU abstract PDF](https://meetingorganizer.copernicus.org/EGU2014/EGU2014-16286.pdf) (200; wording confirmed) |
| **Support** | EGU abstract PDF and Crossref bibliographic record retrieved in this session; 2015 full text not retrieved. |

### SOIL-09 — supported-with-limit

| Field | Text |
|---|---|
| **Claim** | Organized organic additions and related management can raise soil organic carbon stocks, sometimes rapidly at first, but there are severe practical limits to sustaining a high fractional increase over large areas and many decades: accumulation moves toward a new equilibrium, rates slow, and gains can be reversed if the practice is not continued. |
| **Best-fit study** | Poulton, P., Johnston, J., Macdonald, A., White, R. & Powlson, D. (2018), “Major limitations to achieving ‘4 per 1000’ increases in soil organic carbon stock in temperate regions: Evidence from long-term experiments at Rothamsted Research, United Kingdom,” *Global Change Biology* 24:2563–2584. This is also the long-term-trial best-fit for realistic rebuild rates. |
| **What it shows** | Sixteen long-term experiments in southeast England, 114 treatment comparisons over 7–157 years, including organic additions, N fertilizers, pasture leys in arable systems, and conversion of arable land to woodland. In 65% of cases, SOC increased at more than 7‰ per year in the 0–23 cm depth (approximately equivalent to the 4‰ per year goal in the 0–40 cm depth). In the two longest-running experiments, annual FYM at 35 t ha⁻¹ gave increases of 18‰ and 43‰ per year in the first 20 years, and rates stayed above 7‰ for 40–60 years. The authors conclude there are severe limitations to achieving the “4 per 1000” goal in practical agriculture over large areas, including insufficient manure, some favorable practices already being widely adopted, and the fact that increases are reversed if the modified practice is not continued. SOC accumulation “does not increase indefinitely but moves towards an equilibrium value.” Treating soils as a major climate-mitigation contribution of that magnitude is described as unrealistic, even though any contribution can still be beneficial. This is a limit on large, lasting fractional claims, not a finding that corrective effort cannot raise SOM. |
| **Limit** | Temperate southeast United Kingdom, three soil types. High early rates come from large, sustained FYM applications that many farms cannot match. This is not a no-till carbon result. |
| **Funding / affiliation** | Rothamsted Research. Funded by BBSRC grant BBS/E/C/000J0300; the authors also thank the Lawes Agricultural Trust. **Not industry-funded.** Public UK research institute. |
| **Link** | [DOI](https://doi.org/10.1111/gcb.14066) · [Rothamsted OA PDF](https://repository.rothamsted.ac.uk/id/eprint/93/1/Poulton_et_al-2018-Global_Change_Biology.pdf) (200; wording confirmed) |
| **Support** | Author-posted OA PDF retrieved in this session. |

---

## Cross-domain note: water parallels

This note is analogical. It does not transfer water-domain protocol symbols (`D_W`, `Q_sw`, `G_W`, `C_irr`), invent soil-domain quantities, treat the parallels as a demonstrated HKL law, or develop a THEORY_MAB arm.

| Water-domain claim or result | Soil parallel | How strong |
|---|---|---|
| **Service versus condition (key).** PAE-02 / Round 26 Limb A: well-level change and winter planted area can move in opposite directions across regions. Limb B: winter planted area is not delivered water (`D_W`). CV-11: pumping can rise when surface water is short, with renewed aquifer compaction; whether delivered service was maintained remains open. | **SOIL-06**, read with **SOIL-05** and **SOIL-02**. At Broadbalk, grain yields can be similarly high with fertilizers only or with FYM plus fertilizer, while plough-layer SOM is much higher under annual FYM. Thaler associates complete A-horizon loss with only a 6 ± 2% yield reduction, which is closer to “service mostly held while condition degraded.” | **Moderate, and incomplete.** The Broadbalk contrast is coexistence of high yield with lower SOM than under manure, not opposite movement of the two series, and not fertilizer-caused SOM decline. Oldfield still finds a yield gain with SOC up to about 2%. The parallel is the strongest soil analogue to Marathwada in this table, but it is not a transfer and not complete decoupling. |
| **Substitution that is incomplete.** Imported groundwater in Table 3-1, and pumping as a substitute during surface-water shortages (CV-11), can keep a supply account looking filled while the aquifer condition changes. | **SOIL-05**: nitrogen fertilizer is a co-varying management factor, not a complete substitute for SOC at low concentrations. High fertilized yields (SOIL-06) do not prove that soil condition is intact. | **Moderate analogy.** Different mechanism (imported or pumped water versus fertilizer), same caution against a yield-only or supply-only reading. |
| **Organized corrective effort** (PAE-01): people can organize watershed works and then record wells and planting, with selection and object-class limits. | **SOIL-08** and **SOIL-09**: cover crops and organic additions can raise SOC, with shallow-depth, equilibrium, and reversal limits. **SOIL-07** limits treating no-till as whole-profile sequestration, without cancelling surface-property or erosion benefits (SOIL-01 conservation rates). | **Moderate, with hard practical limits.** Dust Bowl SCS was not used as a locked SOM-rebuild-rate study. “Practices can raise SOM” and “4 per 1000 cannot be assumed over large areas and many decades” are both supported-with-limit. |
| **Time lag and window dependence** (PAE-04 Oro Grande travel time; Round 27 lag windows). | **SOIL-09** accumulation toward a new equilibrium, and **SOIL-07** carbon that may be lost if tillage resumes; **SOIL-08** had to model a new steady state. | **Weaker.** The mechanisms differ (travel time through an unsaturated zone versus stock approaching equilibrium). The shared caution is not to treat an early rate as a permanent trajectory. |
| **Do not read a compilation or national figure as a local result** (CV-14: 9 m is one point; 80% is national). | **SOIL-01** is a global erosion compilation; **SOIL-02** is the preferred regional industrial-cropland row; **SOIL-03** is a global modeled debt with regional gains as well as losses. | **Methodological, already applied.** Same discipline, not a scientific transfer. |

---

## Industry-funded sources

None of the nine best-fit studies is agrochemical-manufacturer funded on the retrieved acknowledgments or metadata. That is a fact about this table, not a finding that industry sources were searched and failed, and not a license to treat every row as an anti-industry result.

Conservation-NGO, foundation, and CGIAR funding labeled in the rows: The Nature Conservancy and the Doris Duke Charitable Foundation (SOIL-03); Wood’s Nature Conservancy co-affiliation (SOIL-05); CGIAR CCAFS (SOIL-07).
