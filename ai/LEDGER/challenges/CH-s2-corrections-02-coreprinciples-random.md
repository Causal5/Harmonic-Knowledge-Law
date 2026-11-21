# CH-s2-corrections-02-coreprinciples-random

**TL;DR.** The `src/` random placeholders were the target of this cycle,
but the standing file `CorePrinciples/Law_of_We_Full.md` still uses
`np.random.uniform` to invent an OIE-impact score and a decision-balance
score. That is a leftover fake-score pattern in the human corpus, not a
failure of the Linux import fix.

- **Claim:** C-s2-corrections-02
- **Challenge:** This does not falsify the claim as scoped to `src/`.
  It records a standing-corpus residual: in `CorePrinciples/Law_of_We_Full.md`,
  `ricci_change = np.random.uniform(0, 0.5)` is used to build `oie_impact`,
  and `prior_knowledge_match = np.random.uniform(0.5, 1.0)` is used as
  `decision_balance`, both commented as “Simulated.”
- **Hit if:** Those `np.random.uniform` placeholder scores are still
  present in `CorePrinciples/Law_of_We_Full.md`.
- **Miss if:** They have already been replaced with an explicit
  not-implemented / `None` result, or the file no longer contains those
  simulated scores.
