# Worked fill: Table 3-1 mapping onto protocol \(Q_{sw}\) or \(D_W\)

> **Unpublished branch work (ai/evolution, Launch Pad Session 1, Round 24, 24 November 2026).** Not a publication to `main`. Not a dictionary fill.

**TL;DR.** The Total column of WY 2025 Table 3-1 cannot be assigned to \(Q_{sw}\) or to \(D_W\) under the published labels. The filing itself treats groundwater extracted outside the subbasin as a “surface water delivery,” and the table is supply accounting, not a declared delivered-service series. Outcome: **breaks**. Cause: **scope / object-class**, not a Layer 0 theory failure. No new symbol was invented. The signature, Bite 5, and \(V_W\) stay unassigned.

**Pre-registration:** [PREREG.md](PREREG.md), written before this mapping was scored.

## Object class (research-procedure worksheet, not Registry vocabulary)

| Quantity | Object class | Reporting mode | Notes |
|---|---|---|---|
| Table 3-1 Total | observation (filing-reported accounting total) | qualitative-provisional as to protocol symbols | Does **not** assign \(Q_{sw}\) or \(D_W\). |
| Imported share (this fill) | observation computed from the locked CSV | computed on the pre-locked Round 23 CSV | Share only; not a protocol symbol. |
| \(Q_{sw}(t)\) | unassigned | not-implemented | Dictionary still requires separation from groundwater withdrawal. |
| \(D_W(t)\) | unassigned | not-implemented | No declared delivered-service series and no \(\epsilon_{D_W}\) lock here. |

## Primary result (Total column)

The locked excerpt states: “For the purposes of this report, groundwater extracted outside the Tulare Lake Subbasin but utilized within the Tulare Lake Subbasin is treated as a surface water delivery for the purpose of calculating groundwater pumping within the Tulare Lake Subbasin.”

Under the v0.2 dictionary rule that \(Q_{sw}\) be kept “separate from groundwater withdrawal,” the Total column cannot be \(Q_{sw}\). The same notes describe “Surface water supply used or available for use,” with conveyance-efficiency corrections toward on-farm delivery, not a declared demand or delivered-service tolerance series with a locked \(\epsilon_{D_W}\). The Total therefore cannot be \(D_W\) without inventing that identification.

**Outcome:** **breaks**. Cause: **scope / object-class**. Layer 0 is unchanged. The protocol already required the separation; the public table does not instantiate it.

Imported share of the Total, from the committed Round 23 CSV (script rerun SHA of the shares file is in the outputs folder): 2.0% (WY 2024) to 50.4% (WY 2015). In the five Dry years the share is 18.2%–50.4%. The mix is not a rounding footnote.

## Sensitivity (not the decision)

Excluding the Imported column, the remaining river, SWP, and CVP columns are described as surface-water sources and, in the locked notes, are not the imported-groundwater mix. That subset is a *candidate* \(Q_{sw}\) only, not a locked dictionary fill: “Surface Water Delivery includes a conveyance efficiency correction to account for on-farm surface water delivery,” and GSP Appendix D is not in the locked excerpt. The subset is not \(D_W\).

## What was not done

The temporal-mining conjunction was not evaluated. Bite 5, \(V_W\), official buffer, and the freshwater dictionary remain unfilled. No mixed symbol was invented.

**Short-summary rule (Round 24 [C]).** Say the Total **breaks** as a scope / object-class limit, not a Layer 0 failure. Do not call the totals \(Q_{sw}\) or delivered service. The ex-Imported subset is a candidate only; the dictionary stays unfilled.
