# CH-niger-precip-01-national-average-not-a-site

**TL;DR.** 151 mm per year is a country-wide long-term average. It is not rainfall at an FMNR site, and it hides north–south gradients inside Niger.

- **Claim:** C-niger-precip-01
- **Challenge:** A correctly treats the series as a repeated long-term average rather than an interannual series. Even as a climatology, a single national number cannot stand in for the rainfall at comparable FMNR or Great Green Wall sites. Niger spans a desert-to-Sahel gradient; a spatial average can be much drier than the southern farming belt where FMNR is usually discussed. The archive’s “FMNR in Niger” language does not license this national figure as a site climate series.
- **Hit if:** The fill uses 151 mm as a site or southern-Sahel rainfall value, or as a climate covariate for an FMNR contrast.
- **Miss if:** The fill already keeps 151 mm as a country long-term average only, and does not use it as a site series.
