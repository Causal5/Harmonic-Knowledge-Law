# CH-freshwater-data-dictionary-01-tau-d

**TL;DR.** The protocol’s ratio uses a timescale called tau_d. The spreadsheet defines a *net* depletion time and then writes the ratio with tau_d, without a row that says whether those are the same thing. That is a real chance to mix two clocks. This challenge is aimed at claim 01.

- **Claim:** C-freshwater-data-dictionary-01
- **Passage:** Protocol §6.1: “Define \(\rho_{TM}=\tau_s/\tau_d\) only after estimating both comparable timescales and their uncertainty.” Crosswalk: “Bare \(\rho\)” currently means “\(\rho_{TM}=\tau_s/\tau_d\); distinguish from a reachability proxy,” and separately, “Net time to depletion” is \(\widehat{\tau}_d^{net}=(G_W-G_{min})/(-\dot G_W)\), “a local linear approximation, not a forecast.” Files: `temporal-mining-freshwater-protocol-v0.2.md` §6.1; `definition-crosswalk-v0.3.1.md` (Physical balance). CSV rows `tau_d_net` and `rho_TM`.
- **Challenge:** Claim 01 includes the separations required by §6.1 and the crosswalk. The CSV has `tau_draw`, `tau_d_net`, and `rho_TM` with formula `rho_TM = tau_s / tau_d`, but it has no `tau_d` row and does not say whether `tau_d` is `tau_d_net`, some other depletion timescale, or a quantity still to be declared. If they are silently treated as the same, the crosswalk’s care in naming a *net* local approximation is lost.
- **Hit:** \(\tau_d\) is used in the \(\rho_{TM}\) formula but is not defined, and is not explicitly distinguished from `tau_d_net`.
- **Miss:** The challenge fails if the CSV already defines \(\tau_d\) and states its relation to `tau_d_net` without collapsing the two.
