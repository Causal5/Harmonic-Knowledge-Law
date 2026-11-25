# Worked fill: independent \(C_{irr}\) product search for Tulare Lake (ARM-07)

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 28, 25 November 2026).** Not a publication to `main`. Scored after the pre-registration at `12d7edf`.

**TL;DR.** Seven public products from the locked catalogs were classified under the pre-registered four-part rule. None qualifies as an independent \(C_{irr}\) series for Tulare Lake 5-022.12. USGS NWIS lists 17 California extensometer wells; zero fall inside the Bulletin 118 polygon, and the Water Year 2025 filing still says additional extensometer data are needed. CGPS stations LEMA and CRCN, and KRCD-style benchmarks, are independent land-surface displacement records inside the subbasin, but they are not a locked storage-capacity-loss volume. OpenET is evapotranspiration, not \(C_{irr}\). InSAR and the C-zone acre-foot figure derived from it fail the independence rule. The round is **indeterminate** (data / scope gap). ARM-07 stays `wait`. The temporal-mining signature stays unassigned. This fill does not develop the arm and does not evaluate the protocol §5 conjunction.

**Parents.** [PREREG](PREREG.md) · Protocol v0.2 §4 and §13 · Central Valley v0.2 · ARM-07 · Round 23 independence rule · `main` at `37522fc`.

## What was searched

The catalogs named in the pre-registration: USGS extensometer pages and data releases; DWR / SGMA subsidence products, distinguishing InSAR from CGPS and extensometers; continuous GPS and documented survey / borehole-compaction records; and OpenET, only to record that it is not \(C_{irr}\).

A classification script, [scripts/classify_tulare_cirr_products.py](scripts/classify_tulare_cirr_products.py), checks the Bulletin 118 polygon against the committed NWIS inventory and against the WY 2025 coordinates for LEMA and CRCN, then applies the locked product table. It refuses to mark OpenET or shared InSAR as qualifying. Offline replay uses only the committed extracts.

## Qualification results

| Product | Object class | Independence | Coverage | Lockability | Qualifies? |
|---|---|---|---|---|---|
| DWR / TRE Altamira InSAR, and the WY 2025 C-zone storage volume derived from it | fail (shared InSAR displacement used as volume) | fail | pass | pass | **no** |
| USGS NWIS borehole extensometers (17 California GW-EX sites) | pass | pass | fail (0 in 5-022.12) | pass | **no** |
| USGS refurbished SJV extensometers (Oro Loma Deep, Panoche, DWR Yard, Rasta) | pass | pass | fail | pass | **no** |
| Brandt, Sneed, and Boyce 1958–2018 data release (DOI 10.5066/P144BREY) | pass | pass | fail (no site table retrieved) | fail | **no** |
| CGPS stations LEMA and CRCN | fail (surface displacement, not a locked volume) | pass | pass (both inside the polygon) | pass | **no** |
| KRCD / other RMS benchmark surveys in WY 2025 | fail (survey displacement, not a locked volume) | pass | pass | pass | **no** |
| OpenET evapotranspiration | fail (ET / consumptive use) | pass | pass | pass | **no** |

Details and reasons are in [outputs/product_qualification.csv](outputs/product_qualification.csv). Site tests are in [outputs/nwis_extensometer_sites.csv](outputs/nwis_extensometer_sites.csv) and [outputs/cgps_sites.csv](outputs/cgps_sites.csv).

## Evidence that supports those flags

- **InSAR / C-zone.** v0.2 already states that C-zone storage uses surface displacement and that reusing the same InSAR as an independent check would count some evidence twice. The WY 2025 filing says the subbasin’s extensive subsidence coverage “is derived from satellite-based InSAR measurements,” and computes C-zone storage as \(V = A\Delta b\), where \(\Delta b\) is “the change in aquitard thickness due to subsidence.” That volume is therefore not independent of the v0.2 C-zone input.
- **Extensometers.** The USGS Central Valley subsidence-data page records 35 historical San Joaquin Valley extensometers, most from the 1950s–early 1980s, and four refurbished cable-type sites (Oro Loma Deep, Panoche, DWR Yard, Rasta). All four, and all 17 California GW-EX sites in the 25 November 2026 NWIS inventory, lie outside 5-022.12. The nearest refurbished site, Rasta (`020S018E06D001M`, 36.22631, −120.06517), is outside the polygon. WY 2025 still states: “Additional high-resolution extensometer data is needed to determine which clay-rich zones are most susceptible to compaction.” An El Rico GSA subsidence study “currently underway” may use “additional wells, benchmarks, and possibly extensometers”; that is not a locked public series.
- **Brandt et al. data release.** The Science Data Catalog page exists (DOI 10.5066/P144BREY) and describes borehole-extensometer compaction observations for 1958–2018. The ScienceBase item and site table returned HTTP 403, so no 5-022.12 site is named from that release here.
- **CGPS and benchmarks.** WY 2025 reports land-surface decreases of 0.433 ft at LEMA and 0.400 ft at CRCN, and an average 0.2079 ft decrease at other RMS benchmarks. Both CGPS stations fall inside the Bulletin 118 polygon. Nevada Geodetic Laboratory publishes daily IGS20 height series for both (CRCN from 27 September 2010; LEMA from 11 September 2005; last retrieved observations 28 July 2025). Those are independent displacement records. Protocol \(C_{irr}\) is a volume. v0.2 already says that translating surface displacement into water released from a particular aquifer requires a model. No retrieved official source performs that conversion for these two stations independently of the shared InSAR. This fill does not invent one.
- **OpenET.** The project’s “What is ET?” page defines evapotranspiration as evaporation plus transpiration and as a measure of consumptive use. That is not irreversible compaction or storage-capacity loss.

## Outcome

Under the pre-registration:

- **Holds** would have required at least one product to meet all four tests. None did.
- The fill does not assign a locked independent \(C_{irr}\) to OpenET or to shared InSAR, does not invent a conversion, and does not declare the signature to have fired or failed. It therefore does not take the procedure-break branch.
- The locked catalogs were searched and no product qualifies. The round is **indeterminate**. Cause: **data / scope gap**, not a Layer 0 or theory failure.

ARM-07 remains `wait`. The protocol §5 signature remains unassigned. A later public extensometer in 5-022.12, or an official conversion of an independent displacement series to storage-capacity loss that does not reuse the v0.2 InSAR, would be a new test, not a result of this one.

## What this fill does not do

- It does not develop ARM-07.
- It does not evaluate \(|dD_W/dt|\le\epsilon_{D_W}\), score Bite 5, or construct \(V\).
- It does not convert CGPS or benchmark displacements to acre-feet.
- It does not treat the C-zone −50,395 AF figure as an independent \(C_{irr}\).
- It does not invent sites, citations, or definitions. A1–A8 remain undefined.
- It does not edit `main`.
