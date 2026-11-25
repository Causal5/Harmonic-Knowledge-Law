# Worked fill: Paani / Marathwada service vs groundwater-condition records

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 26, 25 November 2026).** Not a publication to `main`. Not a rewrite of the published pages.

**TL;DR.** Tables 3–4 do show descriptive independence: in Marathwada, Water Cup villages kept more winter area while wells fell farther; in North Maharashtra the pairing is the other way around. Limb A **holds**. Winter sown area is cropped area that the Foundation itself describes as indicating “utilization of the groundwater,” so it cannot be assigned to \(D_W\) or to a clean “water service” record under the published labels. Limb B **breaks**. Under the pre-registered rule the published justification therefore **breaks**. Cause: **scope / object-class**, not a Layer 0 failure. No new symbol was invented. Bite 5, \(V\), and \(D_W\) remain unassigned.

**Pre-registration:** [PREREG.md](PREREG.md), committed at `f719835` before this fill assigned the outcome.

## Limb A — descriptive independence

| Zone | Well-level change, m (Cup / comparison) | Winter area, % of previous (Cup / comparison) | Evaluative directions |
|---|---:|---:|---|
| North Maharashtra | −0.72 / −2.17 | 25.74 / 44.99 | opposite |
| West Maharashtra | −0.53 / −0.56 | 51.37 / 31.23 | same |
| Marathwada | −0.63 / −0.42 | 36.17 / 24.90 | opposite |
| Vidarbha | +0.04 / −0.11 | 91.28 / 90.00 | same |
| All regions, as reported | −0.37 / −0.45 | 53.97 / 47.40 | same |

Two of four regions are opposite, including the Marathwada pairing used in Central Valley v0.2. The script `compute_paani_direction_pairs.py` recomputes those labels from the committed CSV. **Limb A: holds.**

## Limb B — object class

| Quantity | Object class (research-procedure worksheet, not Registry vocabulary) | Reporting mode | Notes |
|---|---|---|---|
| Table 3 well-level change | observation (Foundation-reported average dug-well level change) | qualitative-provisional as to protocol symbols | A groundwater-condition observation. Not a locked \(H_W\) or \(G_W\) fill. |
| Table 4 rabi sown area | observation (percentage of previous winter’s sown area) | qualitative-provisional as to protocol symbols | Does **not** assign \(D_W\). |
| \(D_W(t)\) | unassigned | not-implemented | No declared delivered-service series and no \(\epsilon_{D_W}\) lock here. |

The locked excerpt states that the evaluation “measures the impact on groundwater (through water levels of dugwells) and the sown area in Rabi season (which indicates utilization of the groundwater).” The Foundation then explains the Marathwada / West Maharashtra well-level pattern by “greater extraction of well water” for rabi irrigation. Under the v0.2 dictionary, \(D_W\) is demand or delivered water service, not cropped area, and not a withdrawal or utilization proxy. Assigning Table 4 to \(D_W\) or treating it as a clean “water service” record would invent that identification.

**Limb B: breaks.** Cause: **scope / object-class**. Layer 0 is unchanged. The two observations can still be kept as separate records; they are not, thereby, a protocol service series and a protocol head series.

## Round-level outcome

**Breaks** (Limb A holds, Limb B breaks). The published sentence’s numbers are correct, and the two Foundation series can move independently. The inference that this contrast supplies “water service” and “groundwater condition” records, in the protocol sense that justifies a Tulare \(D_W\) identification, does not go through.

What was not done: \(D_W\), \(\epsilon_{D_W}\), Bite 5, and \(V\) remain unassigned. The published Central Valley sentence was not rewritten.

**Short-summary rule (Round 26 [C]).** Say the published justification **breaks** as a scope / object-class limit, not a Layer 0 failure. Keep Limb A as a hold (Marathwada and North Maharashtra are opposite pairings). Do not call Table 4 a delivered-service or \(D_W\) series.
