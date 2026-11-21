# CH-layer1-consistency-03-stale-section-citations

**TL;DR.** The audit caught the addendum still talking as if a measured
sign change were an empirical anchor. That is real, but it undersells the
problem. The same draft cites “Sahel §5.1” for an OIE integral and
“HKL §5.1” for a basin-maintenance formula, and it treats PAE as a number
in a gain function. The *current* Sahel and HKL papers do not contain those
sections or formulas. If those stale citations are in the addendum and the
audit did not record them, the challenge hits.

- **Claim:** C-layer1-consistency-03
- **Challenge:** F4 is too narrow as a characterization of the unpromoted
  addendum’s inconsistency with the current corpus. In
  `Release/Examples/sahel-logistic-addendum-section9-draft.md`:
  1. The header lists “HKL Lyapunov v2” and “AEF v2” among sources, and
     later “Authoritative chain: Worldline → Extension → Sahel (this
     addendum extends Sahel §§5–8).” Current
     `Release/HKL/hkl-lyapunov.md` §7 says the recovered v2 draft is
     historical and does not override the current definitions.
  2. The draft says “Sahel §5.1 already commits OIE to being a measure
     over \(S_\Phi\),” with \(OIE_\int = \int_{S_\Phi} OIE(x)\,d\mu(x)\).
     Current `Release/Examples/sahel_worked_example.md` has no §5.1; §5
     withdraws completion claims, and the migration table says OIE is a
     process.
  3. The draft defines a “basin-maintenance margin from HKL §5.1,”
     \(M(t) := \mathcal{F}_{PAE} - \mathcal{F}_{OIE} - \frac{1}{w_0}\sum_{k\ge 1} w_k \dot{B}_k(t)\),
     and states \(M(t)>0 \iff dV/dt < 0\). Current HKL has no §5.1;
     §5 is “Effect accounting,” and the margin in current §3–§6 is
     \(M_{V,\Omega}=V_{max,\Omega}-V_\Omega\), not that flux difference.
     The formula resembles `Release/Working/hkl-lyapunov-v2.md` §5.1, which
     is superseded.
  4. The gain function includes a term written \(\lambda_{PAE}(t)\,PAE(t)\),
     treating PAE as a number, which current AEF §2 and the 16 October
     record reject.

  These are standing-corpus issues in an in-tree (unpromoted) example
  source, not defects invented by A. They should be recorded if the audit
  is to be used as a human review aid.

- **Hit if:** Those citations or formulas are present in the addendum as
  described, and the current Sahel and HKL papers do not contain the cited
  sections, and the audit as committed does not record this stale-citation
  problem.
- **Miss if:** The cited passages are not in the addendum, or the current
  papers do contain those sections as cited, or the audit already recorded
  this issue.
