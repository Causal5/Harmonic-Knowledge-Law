# CH-layer1-consistency-01-authority-scope

**TL;DR.** The official Absorbic Effort paper already separates expenditure
from correction. The problem A found lives in experimental Python, which
the root README already calls experimental. If the audit is written so a
reader thinks the official PAE *definition* is inconsistent with itself,
the challenge hits. If the audit clearly parks the defect in `src/` and
does not demote the paper, the challenge misses.

- **Claim:** C-layer1-consistency-01
- **Challenge:** Finding F1 is a real code/definition mismatch, but “Layer 1
  / implementation consistency” can be read as if established Layer 1 PAE
  were internally broken. The current AEF paper and the 16 October record
  already reject treating expenditure as successful correction. `README.md`
  already lists `src/` as experimental implementation material. The issue
  is experimental-code drift, not a hole in the official definition.
- **Hit if:** The audit or claim presents F1 as a defect in the current
  official PAE definition, or treats `src/IIF_Evaluator.py` as a governing
  Layer 1 source.
- **Miss if:** The audit and claim clearly locate the defect in experimental
  code, and do not treat that code as governing the definition.
