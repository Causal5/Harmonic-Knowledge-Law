# C-freshwater-data-dictionary-02

**TL;DR.** This claim is that the dictionary does not sneak in a new official symbol, does not rewrite an existing registry definition, uses the names already corrected in the crosswalk, and does not pick HKL weights or a cutoff. If it does any of those, the claim fails.

- **Proposal:** `ai/proposal/2026-11-21-freshwater-data-dictionary`
- **Statement:** The dictionary introduces no new registry primitive, does not change a v0.3.1 definition, follows the crosswalk’s domain-scoped names (`G_W`, `H_W`, `D_W`, `D_W,crit`, `Q_alt,firm`, `tau_draw`, `tau_age`), and does not select HKL weights, normalizations, or a `rho_TM` cutoff.
- **Falsifier:** A new primitive is treated as registered, a v0.3.1 meaning is rewritten, or weights/`V_W`/a cutoff are chosen or computed.
- **Status:** proposed
