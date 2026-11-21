# Proposal: Ebonyshell renewal-coverage protocol v0.1

**TL;DR.** The mussel example already defines renewal coverage and lists
computing it for ebonyshell above and below Keokuk as an open step, if
the data exist. This cycle writes the measurement recipe and leaves every
rate blank. It does not invent recruitment numbers, does not treat the
example’s qualitative “effectively zero” line as a computed result, and
does not claim the planned fish passage has been tested.

## Parent documents

- `Release/Registry/definition-decisions-2026-10-30.md` §3–§6 and remaining work
- `Release/Examples/ohio-mississippi-mussels/README.md`
- `Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md` §8
- Registry v0.3.2 (no silent rewrite of v0.3.1)

## Deliverable

`Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md`

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-ebonyshell-renewal-01 | The protocol declares the registered quantities \(R^{nat}_{s}\), \(R^{man}_{s}\), \(L_{s}\), \(\eta^{nat}_{TM}\), \(\eta^{tot}_{TM}\), the three exclusive statuses, the independent severed flag, and an above/below-Keokuk comparison on a common window in consistent units, without adding a new primitive or a new universal cutoff. | A required registered element is missing, a new primitive or cutoff is introduced, or the two units are not specified as a common-window comparison. |
| C-ebonyshell-renewal-02 | The protocol computes no rates or ratios and invents no empirical values; filled numeric cells remain UNFILLED-REQUIRED or “not computed.” | A numeric \(\eta\), rate, or status assignment appears as a computed result, or illustrative tank-model parameters are used as data. |
| C-ebonyshell-renewal-03 | The protocol records host-fish coupled renewal, treats the 1986 passage as episodic, and preregisters the planned fish passage as a pathway-restoration test without claiming that test has been run, and without treating the worked example’s qualitative “effectively zero / severed” wording as a computed \(\eta\). | Those requirements are omitted, the 1986 event is treated as continuous renewal, the fish-passage test is reported as completed, or the qualitative severed statement is presented as a measured ratio. |
| C-ebonyshell-renewal-04 | Official boundaries, window, series, and source versions remain unfilled; this is not empirical validation of HKL. | Those fields are filled with unevidenced values, or the protocol claims validation. |
