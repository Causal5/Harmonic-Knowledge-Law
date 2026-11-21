# Ebonyshell renewal-coverage protocol v0.1

**TL;DR.** This is a fill-in sheet for the already-registered renewal
coverage ratios, not a completed measurement. It says what would have to
be declared and recorded to compute natural and total renewal coverage
for ebonyshell above and below the Keokuk dam, including the severed
flag, the 1986 skipjack passage as an episode rather than a continuous
trickle, and the planned fish passage as a later test of pathway
restoration. Every rate, window, and official source version is left
unfilled. No ratio is computed here.

**Status:** proposed preregistration. Not an empirical validation, not an
HKL score, and not a new primitive. Parent definitions:
`Release/Registry/definition-decisions-2026-10-30.md` §3–§6;
`Release/Examples/ohio-mississippi-mussels/README.md` (open empirical
steps); worked example §8 (source-qualified illustration).

## 1. What is and is not being claimed

The decision record states that no field \(\eta_{TM}\) has been computed
for the mussel case, and that computing \(\eta^{nat}_{TM}\) for ebonyshell
above and below Keokuk would be the first application, if recruitment
data exist. The worked example §8 already *qualitatively* says natural
renewal coverage above Keokuk after 1913 is “effectively zero” apart from
rare passage such as 1986, and therefore carries the *severed* flag, while
net-mining versus substituted “is not measured here.” This protocol does
**not** treat that qualitative statement as a computed result. The ratios
and the flag remain to be filled from declared series, or left unfilled
if the series cannot be obtained.

Yangtze sturgeon material in the example is a cross-basin analog and is
outside this protocol’s boundary.

## 2. Comparison units

Declare two spatial units, using the same stock and the same units:

| Unit ID | Stock | Spatial extent | Official boundary source |
|---|---|---|---|
| EBONY-ABOVE-KEOKUK | Ebonyshell (declare the scientific name and life stage with the data) | Upstream of Lock and Dam 19 / Keokuk dam, exact river miles UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| EBONY-BELOW-KEOKUK | Same stock and life stage | Downstream of the dam, exact river miles UNFILLED-REQUIRED | UNFILLED-REQUIRED |

The dam is a barrier on the host-fish pathway, not automatically a wall
for every adult mussel. Do not treat skipjack herring coverage as a
substitute for ebonyshell \(\eta_{TM}\). Host access is a declared
dependency of \(R^{nat}_{s}\), per decision record §5.

## 3. Window, units, and required series

Over one common window \([t_0,t_1]\) and in the same units, record:

| Symbol | Meaning | Value in this protocol |
|---|---|---|
| \([t_0,t_1]\) | Common observation window | UNFILLED-REQUIRED |
| \(R^{nat}_{s}\) | Natural renewal rate (successful recruitment into the declared life stage) | UNFILLED-REQUIRED |
| \(R^{man}_{s}\) | Managed renewal rate (stocking or managed translocation into that life stage) | UNFILLED-REQUIRED (may be recorded as 0 if a source shows none) |
| \(L_{s}\) | Gross loss rate from that same stock (mortality, harvest, predation, other losses — not a net change) | UNFILLED-REQUIRED |

For \(L_s>0\):

\[
\eta^{nat}_{TM}=\frac{R^{nat}_{s}}{L_{s}},\qquad
\eta^{tot}_{TM}=\frac{R^{nat}_{s}+R^{man}_{s}}{L_{s}}.
\]

If \(L_s=0\) over the window, do not form the ratio; record that the
denominator is undefined and stop. No new universal cutoff is adopted.
The status table in the decision record already uses the registered
comparisons with 1; those are classification rules, not a new threshold
invented here.

\(\rho_{TM}=\tau_s/\tau_d\) is used only when both timescales are positive
and finite. If they are not, report through \(\eta\), not as an infinite
ratio.

## 4. Status, severed flag, and episodes

After the ratios are filled (and only then), assign exactly one status:

| Status | Condition |
|---|---|
| Net mining | \(\eta^{tot}_{TM}<1\) |
| Substituted | \(\eta^{nat}_{TM}<1\le\eta^{tot}_{TM}\) |
| Covered | \(\eta^{nat}_{TM}\ge 1\) |

**Severed** is an independent flag, set when \(\eta^{nat}_{TM}=0\) apart
from declared episodic events. A severed stock cannot be classified
Covered. Report the flag with the status (for example “severed,
substituted”).

The 1986 skipjack passage cited in the worked example (NPS secondary
summary; contemporaneous Bureau of Fisheries studies are named there as
the primary sources to consult) is recorded as an **event count and a
window-averaged rate**, not as continuous renewal. Additional episodes,
if documented later, are added the same way. Do not invent a continuous
upstream trickle from a single cited high-water event.

## 5. Coupled renewal, targets, and screens

Publish a dependency graph before computing \(R^{nat}_{s}\): ebonyshell
recruitment depends on the adult stock *and* on host-fish access
(skipjack herring in this case). Habitat and access conditions are
declared, not inferred from adult counts alone. The freshwater v0.2
assumption that recharge does not depend on the groundwater stock is
**not** transferred here.

Native unionid recruitment and composition are a **dependency target**:
a substitute that supplies filtration or other service cannot offset a
failed native-recruitment channel.

Substituted status is only a **screen** for possible corrective
dependency. Confirmation still needs the buffer comparison in decision
record §4, or observation after a program ends. Coverage is not
viability. Stock size, floors, and connected flows still matter.

Do not compute field ACR or buffer in this protocol. Do not assume a
reproductive Allee threshold for unionids.

## 6. Prospective pathway-restoration test (not run here)

If a fish passage at Keokuk is built and operated, the preregistered
observations are:

1. Skipjack passage counts (or a declared equivalent host-access measure)
   above the dam, with effort and detection limits stated.
2. Subsequent ebonyshell recruitment upstream, on a window long enough
   for the declared life stage, recorded separately from stocking.
3. Classification of the passage as *pathway-restoring* only if natural
   renewal rises in a way that is expected to persist after passage
   operations are attributed; stocking remains *substituting*.
4. Construction and operating status remain UNFILLED-REQUIRED. The
   worked example already notes that construction status as of October
   2026 has not been confirmed. This protocol does not update that
   status and does not invent a monitoring result.

## 7. Sources and uncertainty

Source citations already in the worked example may be reused. Official
retrieved versions, reach-specific recruitment series, mortality series,
and stocking records are UNFILLED-REQUIRED. Missingness and uncertainty
rules are UNFILLED-REQUIRED. Do not fill a rate by guessing, by copying
the tank-model figure parameters (those are illustrative, not fitted),
or by treating “effectively zero” as a measured numerator.

## 8. Reporting sheet (all values unfilled in v0.1)

| Field | EBONY-ABOVE-KEOKUK | EBONY-BELOW-KEOKUK |
|---|---|---|
| Scientific name and life stage | UNFILLED-REQUIRED | same |
| Official boundary / river miles | UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| Window \([t_0,t_1]\) | UNFILLED-REQUIRED | same window |
| \(R^{nat}_{s}\) | UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| \(R^{man}_{s}\) | UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| \(L_{s}\) | UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| \(\eta^{nat}_{TM}\) | not computed | not computed |
| \(\eta^{tot}_{TM}\) | not computed | not computed |
| Renewal status | not assigned | not assigned |
| Severed flag | not assigned | not assigned |
| Episodic events (count, window-averaged rate) | 1986 passage: rate UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| Dependency graph | UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| Source versions | UNFILLED-REQUIRED | UNFILLED-REQUIRED |
| Fish-passage monitoring result | not run | not run |
