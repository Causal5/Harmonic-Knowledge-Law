# Pre-registration: independent \(C_{irr}\) product search for Tulare Lake (ARM-07)

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 28, 25 November 2026).** Not a publication to `main`. Written before this search scored whether any product qualifies.

**TL;DR.** This test asks whether a public, InSAR-independent irreversible-compaction or storage-capacity-loss series can be locked for Tulare Lake 5-022.12. OpenET evapotranspiration is not \(C_{irr}\). Finding no qualifying product leaves ARM-07 at `wait` and the signature unassigned. This test does not develop the arm and does not evaluate the protocol §5 conjunction.

**Parents.** Protocol v0.2 §4 (\(C_{irr}(t)\): “Irreversible compaction or storage-capacity loss,” volume) and §13 (USGS extensometer, GPS, InSAR, and DWR SGMA products as a source stack). Central Valley v0.2: C-zone storage already uses surface displacement; a comparison that reuses the same InSAR as an independent check would count some evidence twice. ARM-07 (24 November 2026): `wait` until an independent series is in hand. Round 23 independence rule. `main` at `37522fc`. A1–A8 remain undefined.

## Locked catalogs to search

The search is limited to these public classes, named in protocol §13 or in the Session 2 brief:

1. USGS San Joaquin Valley / Tulare land-subsidence and extensometer pages and data releases.
2. DWR or SGMA Data Viewer subsidence-monitoring products, distinguishing InSAR from CGPS and extensometers.
3. Continuous GPS or documented spirit-leveling / borehole-compaction records for sites in or documented as representing 5-022.12.
4. OpenET, only to record that evapotranspiration is not \(C_{irr}\) and does not qualify.

No new catalog is added after scoring begins. A source that appears in a locked catalog may be followed to its official landing page, data release, or peer-reviewed documentation.

## Qualification rule (all four required)

A product **qualifies** as an independent \(C_{irr}\) candidate for this test only if all of the following hold:

1. **Object class.** It measures irreversible compaction or storage-capacity loss, or a retrieved official or peer-reviewed source already documents a conversion from the measured quantity to that class. Surface-displacement series without such a conversion remain displacement observations, not a locked \(C_{irr}\) volume. Evapotranspiration, crop water use, soil moisture, and similar products are not \(C_{irr}\).
2. **Independence.** Its primary input is not the InSAR / surface-displacement already used in the v0.2 C-zone storage estimate. InSAR-derived products (including alternative processings of the same class of radar scenes) do not qualify.
3. **Coverage.** A public record locates the series in Tulare Lake 5-022.12, or documents a named site as representing that subbasin.
4. **Lockability.** A public time series or a documented period of record can be cited (version, retrieval date, URL). A page that only asserts that a network exists, without a citable series or site-in-basin record, does not lock the product.

Treating OpenET, or the WY 2025 / v0.2 InSAR, as a locked independent \(C_{irr}\) is a procedure break.

## Pre-registered outcomes

- **Holds** if at least one product from the locked catalogs meets all four qualification tests. Finding such a product does not develop ARM-07, does not convert displacement to acre-feet here, and does not evaluate the temporal-mining conjunction.
- **Indeterminate** if the locked catalogs are searched and no product meets all four tests. Cause: data / scope gap. ARM-07 stays `wait`. The signature stays unassigned.
- **Breaks** (procedure) if the fill assigns a locked independent \(C_{irr}\) to OpenET or to shared InSAR, invents a conversion, or declares the signature to have fired or failed.

## What this test will not do

- Develop ARM-07 or change its decision from `wait` except to record whether a qualifying series is now in hand (a qualifying find still does not, by itself, meet the development gate).
- Evaluate \(|dD_W/dt|\le\epsilon_{D_W}\), score Bite 5, or construct \(V\).
- Invent a storage-capacity conversion or a new definition.
- Use A1–A8 as if defined.
