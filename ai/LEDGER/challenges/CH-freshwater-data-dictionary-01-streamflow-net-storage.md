# CH-freshwater-data-dictionary-01-streamflow-net-storage

**TL;DR.** The protocol says to keep net storage change and streamflow capture as separate things. The spreadsheet has sideways-flow and balance terms, but it never gives those two their own rows, so a later user could collapse them. This challenge is aimed at claim 01.

- **Claim:** C-freshwater-data-dictionary-01
- **Passage:** Protocol §4, after the core table: “Keep natural recharge, managed recharge, gross pumping, net storage change, and streamflow capture separate.” File: `Release/Examples/central-valley/temporal-mining-freshwater-protocol-v0.2.md`. Dictionary: `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`.
- **Challenge:** Claim 01 says the CSV records the separations required by §4, §6.1, and §7. The CSV has `R_n`, `R_m`, `W_g`, and `Q_net` (defined as signed lateral and connected-water exchanges not already counted in recharge or withdrawal). It has no variable named net storage change, observed \(\dot G_W\), or streamflow capture. `Q_net` and `E_sw` might be *meant* to cover streamflow capture, and \(\dot G_W\) might be meant to be computed only from the balance identity, but the protocol asks that net storage change be kept separate — including from a residual computed after the fact — and that streamflow capture be kept separate from the other flows. That mapping is not stated.
- **Hit:** The required §4 separations are incomplete if net storage change or streamflow capture has no own row and no explicit, exclusive mapping to an existing row.
- **Miss:** The challenge fails if the CSV already distinguishes an observed storage-change series from a computed balance residual, and distinguishes streamflow capture from `Q_net` / `E_sw`, in terms that match §4.
