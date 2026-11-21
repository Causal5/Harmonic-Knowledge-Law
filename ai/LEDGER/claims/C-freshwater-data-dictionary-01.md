# C-freshwater-data-dictionary-01

**TL;DR.** This claim is only that the spreadsheet lists every core water variable already named in the protocol, with the same meaning and units, and keeps apart things the protocol says must stay apart (age versus renewal, gross pumping versus net depletion, and sideways water flows). If a listed variable is missing or contradicted, the claim fails.

- **Proposal:** `ai/proposal/2026-11-21-freshwater-data-dictionary`
- **Statement:** The CSV includes every core time-series variable from protocol §4 (`G_W`, `H_W`, `W_g`, `R_n`, `R_m`, `Q_sw`, `D_W`, `L_s`, `C_irr`, `E_sw`, `Q_alt,firm`), with the stated meaning and preferred unit, and records the separations required by §4, §6.1, §7, and `Release/Examples/central-valley/definition-crosswalk-v0.3.1.md` (including age ≠ renewal, gross draw ≠ net depletion, and declared `Q_net`).
- **Falsifier:** A §4 variable is missing or its meaning/unit contradicts the protocol, or a required separation is omitted or contradicted.
- **Status:** proposed
