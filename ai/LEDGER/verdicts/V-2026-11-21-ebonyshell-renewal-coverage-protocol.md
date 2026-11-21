# V-2026-11-21-ebonyshell-renewal-coverage-protocol

**TL;DR.** The protocol is a genuine blank recipe for the already-registered
renewal-coverage ratios, not a completed measurement. No rates were
invented. Two challenges hit and were fixed: life stage and loss
components must be locked before any numbers are filled, and the 1986
episode is, by default, reported beside the numerator rather than folded
into it. A third challenge missed: the sheet never claimed to measure the
registry’s same-reach sink-impairment term, but a disclaimer was added
anyway. A fourth challenge missed against the claim, and is recorded as a
corpus note: the original worked example already assigns the severed flag
from a qualitative “effectively zero,” while the decision record says no
field η has been computed.

**Proposal:** `ai/PROPOSALS/2026-11-21-ebonyshell-renewal-coverage-protocol/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-ebonyshell-renewal-01-life-stage-lock | C-ebonyshell-renewal-01 | hit | The committed protocol said to declare life stage “with the data” and did not lock loss components. Revised. |
| CH-ebonyshell-renewal-01-spatial-vs-counterfactual | C-ebonyshell-renewal-01 | miss | The protocol did not equate above/below with \(\dot B^{imp}_{OIE}\). A disclaimer was still added. |
| CH-ebonyshell-renewal-03-episode-in-numerator | C-ebonyshell-renewal-03 | hit | Episodic reporting was required, but inclusion in \(R^{nat}_{s}\) was unspecified. Default exclusion rule added. |
| CH-ebonyshell-renewal-03-example-severed-uncomputed | C-ebonyshell-renewal-03 | miss (corpus note) | Claim 03 and §1 already refused to treat the example’s qualitative severed line as a computed ratio. The tension in the original example is recorded more explicitly and the example body is not rewritten. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-ebonyshell-renewal-01 | accepted-with-revisions | Registered elements were present; life-stage/loss lock and spatial disclaimer added. |
| C-ebonyshell-renewal-02 | accepted | No computed rates. The only permitted “0” is “if a source shows none” for managed renewal, still unfilled. Tank-model parameters are forbidden as data. |
| C-ebonyshell-renewal-03 | accepted-with-revisions | Coupled renewal, episodic 1986, and unrun fish-passage test were present; numerator rule added; corpus tension recorded. |
| C-ebonyshell-renewal-04 | accepted | Official fields remain UNFILLED-REQUIRED; not claimed as validation. |

## Mechanical checks (this box)

- Scanned the protocol for numeric tokens: section numbers, already-cited years (1913, 1986, 2023, 2026), registry “comparisons with 1,” and `L_s>0` / \(\eta=0\) definitional cases. No filled recruitment, loss, or coverage value. Reporting-sheet ratio cells are “not computed.”
- Confirmed `UNFILLED-REQUIRED` on boundaries, window, series, and source versions.
- `git show --name-only da472c3`: added the protocol and `ai/` ledger files; did not modify the registry or the worked-example body.
- `git diff c9e1277..da472c3` on `definition-decisions-2026-10-30.md` and `ohio-mississippi-mussels-worked-example.md`: empty.
- Confirmed worked example §8 “effectively zero … so the population carries the registry’s *severed* flag” and decision-record remaining work “No field ACR, \(\eta_{TM}\), or buffer has been computed.”
- Confirmed the protocol did not present \(\eta\) as a measurement of \(\dot B^{imp}_{OIE}\).

## Revisions applied in the verdict commit

- Life-stage and \(L_{s}\) component conventions must be locked before rates are filled.
- Default rule: declared episodic rates are reported alongside, not in, the \(R^{nat}_{s}\) used for \(\eta^{nat}_{TM}\) and the severed test.
- Explicit disclaimer that the above/below contrast is not the sink-impairment counterfactual.
- Stronger corpus note on the example’s uncomputed severed assignment, without editing the example body.
- README table row pointing at this protocol.
- Claim statuses and ledger updated.

## Residual / later work

- Official boundaries, window, series, and source versions still need evidence; `needs-evidence` remains the right status for any later numerical filling.
- Whether Jordan wants the worked example’s qualitative severed sentence reworded is left to him; this cycle did not change that file.
- Fish-passage construction status is still unconfirmed, as the example already said.
