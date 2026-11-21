# C-layer1-consistency-01

**TL;DR.** The experimental code has a function named after Absorbic Effort
that automatically shrinks an error score when you pass in a larger
“effort” number. The official definitions say a costly attempt can fail,
so expenditure is not the same thing as a correction. If that function
does not do this, or the definitions do not say that, the claim fails.

- **Proposal:** `ai/PROPOSALS/2026-11-21-layer1-consistency-audit/`
- **Statement:** Finding F1 is present as described: `_apply_pae` in `src/IIF_Evaluator.py` reduces `delta` by a term built from the `effort` argument, which conflicts with the 16 October decision to keep expenditure separate from achieved correction.
- **Falsifier:** The cited function does not so reduce `delta`, or the 16 October record does not require that separation.
- **Status:** proposed
