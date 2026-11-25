# Pre-registration: Paani / Marathwada service vs groundwater-condition records

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 26, 25 November 2026).** Not a publication to `main`. Written before this test assigned a round-level outcome.

**TL;DR.** This test asks whether the published Central Valley justification — that the Marathwada Water Cup contrast is why Tulare needs separate records for water service and groundwater condition — holds under the already-published protocol labels, using the Foundation Tables 3–4 already excerpted in Round 25. A clean descriptive decoupling of two observations can still **break** as a protocol identification if winter sown area is not a delivered-service series.

**Parents.** Central Valley v0.2 (the Marathwada paragraph) and protocol v0.2 §4 / dictionary rows for \(D_W\) and \(H_W\) or well level, as on `main` at `37522fc`. Locked source: the Round 25 excerpt of the Water Cup 2019 report, Tables 3–4 (PDF SHA-256 `1267108cb5883959ccd0c40d962d7f572c4f4dc9aae98d0b9b2bb7dc1fc2b442`). Object-class declaration is used as the adopted research-procedure worksheet, not as Registry vocabulary. No new definition is introduced. A1–A8 remain undefined.

## Locked protocol labels (not newly defined)

- \(D_W(t)\): “Demand or delivered water service.” Dictionary: used in the buffer-financed interval with a declared \(\epsilon_{D_W}\). “Delivered service is not the same as stock viability.”
- Representative groundwater condition in the protocol symbol list includes \(H_W(t)\) (representative groundwater head) and \(G_W(t)\) (recoverable storage). The Foundation series is average dug-well level change, in metres.

The published Central Valley sentence under test: “In Marathwada, Water Cup villages retained 36.17% of the previous winter’s sown area in the *rabi* season, compared with 24.90% in comparison villages. Over the same drought year their average dug-well level fell farther (0.63 versus 0.42 metres). This is why the Tulare analysis tracks service delivered and groundwater levels separately.”

## Two pre-registered limbs

**Limb A — descriptive independence (locked table).** Using only Tables 3–4 as already excerpted:

- **Holds** if at least one reported region shows the two series moving in opposite evaluative directions (more winter area with a larger well-level decline, or less winter area with a smaller well-level decline or a rise).
- **Breaks** if every region moves the two series in the same evaluative direction.
- **Indeterminate** if the locked excerpt is missing a region that the published table uses.

**Limb B — object class of the winter-area series.** Under the locked labels above, and the Foundation’s own description of rabi area as indicating “utilization of the groundwater”:

- **Holds** if the winter-area series can be assigned to \(D_W\) or to “delivered water service” without mixing it with groundwater withdrawal and without inventing a delivered-service identification the locked notes do not support.
- **Breaks** if the series is cropped area, and is described by the Foundation as a use/extraction indicator, so it cannot be \(D_W\) or a clean “water service” record under the published labels without inventing that identification. Cause, if so: **scope / object-class**, not a Layer 0 theory failure. The well-level series may still be treated as a groundwater-condition observation.
- **Indeterminate** if the locked excerpt lacks the Foundation’s own description of what rabi area measures.

## Round-level rule

The published justification (“this is why Tulare needs separate records for water service and groundwater condition”) **holds** only if Limb A holds **and** Limb B holds. If Limb A holds and Limb B breaks, the round-level outcome is **breaks** (scope / object-class): the two observations can move independently, but winter sown area is not a protocol service record. If either limb is indeterminate, the round is indeterminate. Declaring \(D_W\), \(\epsilon_{D_W}\), Bite 5, or \(V\) is a procedure break.

## What this test will not do

- Invent a mixed “cropped-area-as-service” symbol.
- Treat the Foundation’s one-year, selected-village comparison as a Tulare measurement.
- Construct \(V\), score Bite 5, or rewrite the published pages.
