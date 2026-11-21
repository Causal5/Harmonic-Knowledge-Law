# CH-s2-corrections-02-residual-invented-scores

**TL;DR.** Random placeholders were removed from `src/`, but other
invented numbers are still printed as if they were scores. `_score_reasoning`
still returns a connection-count number (0.0 in the tests). Libra still
writes EGR and GDS from hardcoded flops, thermal waste, and heat-resource
lists. Those are not `np.random`, but they are still fake scores.

- **Claim:** C-s2-corrections-02
- **Challenge:** The claim, as written, is about lowercase imports,
  `np.random` placeholders, and scripts running. This challenge does not
  deny that those three checks can pass. It attacks the leftover invented
  numerics in the same experimental folder: `IIF_Evaluator._score_reasoning`
  returns `min(len(node.connections)/10, 1.0)` rather than `None`;
  `Libra_Model.update_hkl_metrics` sets EGR = `10**9 / 1000` and GDS from
  `[500000, 300000, 200000]`; `compute_entropy_score` still turns string
  length into an “entropy” score that can reject inputs. After the patch,
  `test_giln_*.py` prints `HRS: [0.0, None, ...]`, and a short Libra run
  prints `average_EGR: 1000000.0` and a floating GDS.
- **Hit if:** After the proposed `src/` patch, invented numeric scores
  remain in those helpers and appear in script output.
- **Miss if:** Those helpers already return `None` / not implemented, or
  clearly stop presenting the hardcoded values as HKL metrics.
