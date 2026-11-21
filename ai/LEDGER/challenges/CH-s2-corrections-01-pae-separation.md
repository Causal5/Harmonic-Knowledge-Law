# CH-s2-corrections-01-pae-separation

**TL;DR.** The patched helper should record spending in one field and
leave the error score alone. If running it with a numeric delta and a
nonzero effort still shrinks delta, or if the two fields are missing,
the correction failed.

- **Claim:** C-s2-corrections-01
- **Challenge:** Re-run `IIFEvaluator._apply_pae(2.5, effort=10.0)` on
  this Linux box against `src/IIF_Evaluator.py` on `ai/evolution`. The
  16 October record and current AEF §2 say a costly attempt can fail;
  expenditure must not be treated as achieved correction.
- **Hit if:** The returned `delta` is reduced from 2.5, or the record
  lacks separate `expenditure` and `achieved_correction` fields.
- **Miss if:** `delta` remains 2.5, `expenditure` is 10.0, and
  `achieved_correction` is recorded separately (including as `None` /
  not implemented).
