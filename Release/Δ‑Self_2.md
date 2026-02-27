# Δ‑Self 2.0 — The Thermodynamic Identity Ledger

By: Jordan LeDuc

---

# 0. Section‑Scoped Symbol Definitions (Normalization Block)

> **Scope note:** Symbols here are used as contextual analogs borrowed from formal mathematics to represent functions and constraints within this body of work.

| Symbol        | Name                            | Meaning in this document                                          | Type / Domain        | Notes                                   |
| ------------- | ------------------------------- | ----------------------------------------------------------------- | -------------------- | --------------------------------------- |
| $\Delta I(t)$ | Identity deviation (Δ‑Self)     | Thermodynamic identity deviation vector at time $t$               | Vector               | Canonical replacement for $\Delta_I(t)$ |
| $PLA$         | Passive baseline placeholder    | Passive counterfactual extremal trajectory                        | Concept              | Not a metaphysical claim                |
| $E_{PAE}$     | Absorbic effort energy          | Energy spent in applied corrective effort over a window           | $\mathbb{R}_{\ge 0}$ | Energy form of PAE                      |
| $E_{OIE}$     | Observer‑induced entropy energy | Energy‑equivalent destabilization due to state change/externality | $\mathbb{R}_{\ge 0}$ | Energy‑equivalent OIE                   |
| $\nabla S$    | Entropic‑gradient baseline      | Local gradient of entropy over state space                        | Vector field         | Passive drift reference                 |
| $\Delta t$    | Integration window              | Time window over which energies are integrated                    | Scalar interval      | Instrumentation window                  |
| $\Delta L$    | Path‑cost deviation             | Excess realized path cost vs passive baseline                     | $\mathbb{R}_{\ge 0}$ | Empirical observable of agency          |

**Normalization rules applied in v2**

* No bare $\Delta$ (all deltas must specify referent).
* Standardized unicode subscripts → explicit subscript form.

---

# 1. Definition

The Δ‑Self is the thermodynamic identity vector of a cognition‑bearing system.

It represents the minimal‑energy feasible deviation from a passive counterfactual baseline that remains causally viable under the constraint:

$$
E_{PAE} \ge E_{OIE}
$$

A Δ‑Self exists only when a system maintains persistent memory and a stable internal reference sufficient to resolve successive state changes.

---

# 2. Thermodynamic Ledger Framing

Every informational update incurs an energy cost (≥ $k_B T \ln 2$).

The forward arrow of time is the accumulation of irreversible state changes — the Entropy Ledger.

The Δ‑Self is the portion of this ledger where persistence and comparison are possible: the locally stored history against which future change is measured.

Loss of anchor or persistence ⇒ uncontrolled $\Delta I$ fluctuation ⇒ identity decoherence.

---

# 3. Operational Model (Macro‑Safe Form)

$$
\Delta I(t) = \arg\min_{\vec v}
\left(
| \vec v - \nabla S | , ; , E_{PAE} > E_{OIE}
\right)
$$

Where:

* $\nabla S$ = instantaneous entropy gradient (passive drift baseline)
* $\vec v$ = candidate deviation vector (candidate agentic adjustment)
* Constraint $E_{PAE} > E_{OIE}$ enforces causal viability

Interpretation:
The Δ‑Self selects the closest viable deviation from the entropic‑gradient baseline that remains within energy feasibility constraints.

---

# 4. PAE / OIE Coupling

Agency is measurable only if:

1. A passive baseline exists.
2. Excess effort over baseline exists ($E_{PAE}$).
3. Resulting destabilization can be bounded ($E_{OIE}$).

In short:

* $E_{PAE}$ is what the agent expends.
* $E_{OIE}$ is what propagates as destabilization.

---

# 5. Empirical Window

Let $P_A(t)$ denote excess power relative to baseline:

$$
P_A(t) = P_{total}(t) - P_{baseline}(t)
$$

Then:

$$
E_{PAE} = \int_{\Delta t} P_A(t) , dt
$$

$E_{OIE}$ is estimated from observer/environment perturbation cost over the same window.

---

# 6. Path‑Cost Observable

Agency produces detectable excess path cost relative to baseline:

$$
\Delta L > 0
$$

Meaning: the realized trajectory exhibits additional energy/action beyond passive drift.

---

End of Δ‑Self 2 Normalized v2
