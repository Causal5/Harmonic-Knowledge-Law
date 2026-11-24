# Pre-registration: Table 3-1 mapping onto protocol \(Q_{sw}\) or \(D_W\)

> **Unpublished branch work (ai/evolution, Launch Pad Session 1, Round 24, 24 November 2026).** Not a publication to `main`. Written before this test scored the mapping.

**TL;DR.** This test asks whether the already-extracted WY 2025 Table 3-1 can be assigned, under published protocol labels, to \(Q_{sw}\) or to \(D_W\). A mixed or unique-assignment failure is a **break** (scope / object-class), not a Layer 0 failure and not permission to invent a new symbol.

**Parents.** Protocol v0.2 §4 and the v0.2 data-dictionary rows for \(Q_{sw}(t)\) and \(D_W(t)\), as published on `main` at `56c6ab5`. Object-class declaration is used as the adopted research-procedure worksheet, not as Registry vocabulary. The locked source is the Round 23 excerpt and CSV of Table 3-1 (PDF SHA-256 `32c080a3a4972730b94ce7d047ffcec90de16348f50abc166c55465096395be9`).

## Locked protocol labels (not newly defined)

From protocol §4:

- \(Q_{sw}(t)\): “Surface-water delivery or diversion.”
- \(D_W(t)\): “Demand or delivered water service.”

From the v0.2 dictionary:

- \(Q_{sw}\): “Keep separate from groundwater withdrawal and from net connected-water / lateral flows \(Q_{net}\).”
- \(D_W\): “Used in the buffer-financed stability interval with a declared \(\epsilon_{D_W}\) (protocol §5). Do not treat service stability as proof of viability.” “Delivered service is not the same as stock viability.”

No new symbol or cutoff is introduced here.

## Primary series under test

The **Total** column of Table 3-1, water years 2015–2025, as already committed in the Round 23 CSV. That is the filing’s own “Surface Water Supplies” total and the series quoted as observations in Round 23. This test does not extract a new table.

## Pre-registered outcomes

- **Holds** if, under the locked labels above, the Total column can be assigned to exactly one of \(Q_{sw}\) or \(D_W\) without mixing groundwater withdrawal into the surface-water symbol, and without treating a supply-accounting series as delivered-service tolerance unless the locked notes support that identification.
- **Breaks** if the locked notes show that the Total mixes groundwater extracted outside the subbasin into a surface-water total, so it cannot be \(Q_{sw}\) under the dictionary’s separation rule, and the same series is supply accounting rather than a declared delivered-service series, so it cannot be \(D_W\) without inventing the identification. Cause, if so: **scope / object-class**, not a Layer 0 theory failure, not a definition of A1–A8, and not a data gap about the numbers themselves.
- **Indeterminate** if the locked excerpt lacks the notes needed to classify the Total.

Evaluating the temporal-mining conjunction, scoring Bite 5 or \(V_W\), filling the official dictionary, or inventing a mixed “imported-groundwater-as-surface-water” symbol is a procedure break and is not a hold.

## Sensitivity (not the decision)

After the primary outcome is recorded, report the sum of Kings, Kaweah, Tule, Deer, Poso, SWP, and CVP (excluding Imported) as a descriptive share. That subset is a candidate \(Q_{sw}\) only if the locked notes describe those columns as surface-water sources with no groundwater mixing. A clean subset is **not** a locked dictionary fill: conveyance-efficiency corrections still sit between headgate diversion and on-farm delivery, and GSP Appendix D is not in the locked excerpt. The subset is not \(D_W\) unless the notes declare it as delivered-service tolerance.

## What this test will not do

- Invent a definition, symbol, or cutoff.
- Treat object-class worksheet labels as Registry vocabulary.
- Construct \(V\), score Bite 5, or assign the temporal-mining signature.
- Restore withdrawn Sahel claims or use A1–A8 as if defined.
