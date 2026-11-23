# Absorbic Ethics Framework (AEF)

> **Status (ai/evolution, 2026-11-21, Round 10; marks extended 2026-11-23, Round 17, proposed).** Working / preserved proposal. Not current AEF or HKL authority. Current definitions are in `Release/Papers/absorbic-effort-framework.md` and `Release/HKL/hkl-lyapunov.md`. Citations below that do not match those current papers are marked **[DEAD CITE]** in place. No replacement section numbers are invented here.
> - “HKL §5.1” — current HKL has no §5.1; §5 is “Effect accounting.”
> - “the Lyapunov condition $dV/dt \le 0$” — current HKL §4 says $\dot V\le 0$ is not a universal necessary condition; §7 withdraws necessary-monotonic-drift wording.
> - Terms that type $PAE$ as $\mathbb{R}_{\ge 0}$ or write $\lambda_{PAE}\cdot PAE$ treat PAE as a number, which current AEF §2 and the 16 October record reject. No replacement formula is invented here.
> Version numbers inside this draft do not supersede Registry v0.3.1 or the reconciled core papers (`Release/Working/README.md`).


## v2 — Aligned to Δ-Self Worldline Formalization
---

# 1. Purpose

The Absorbic Ethics Framework (AEF) formalizes corrective effort required to offset destabilizing externalities within bounded, causally closed systems.

AEF operates as the applied accounting layer over a stability formalism (HKL Lyapunov basin structure). It does not define stability itself; it defines effort required to preserve it.

**Inheritance:** AEF elaborates the effort dynamics introduced in Δ-Self §13 ($\frac{d}{dt}\mathcal{E}_i = \mathcal{F}_{OIE} - \mathcal{F}_{PAE}$) and the basin maintenance inequality derived in HKL §5.1 **[DEAD CITE: current HKL has no §5.1; no replacement section is invented here]**. Specifically, AEF provides the accounting structure that determines whether the Lyapunov condition $\frac{dV}{dt} \le 0$ is satisfied **[STALE / WITHDRAWN: current HKL §4 says $\dot V\le 0$ is not a universal necessary condition; §7 withdraws necessary-monotonic-drift wording]**.

---

# 2. Section-Scoped Symbol Definitions

| Symbol           | Name                              | Meaning in this document                                               | Type / Domain         | Units / Interpretation             |
| ---------------- | --------------------------------- | ---------------------------------------------------------------------- | --------------------- | ---------------------------------- |
| $PAE$            | Principle of Absorbic Effort      | Applied corrective effort to absorb/offset destabilizing externalities | $\mathbb{R}_{\ge 0}$ | Energy-equivalent effort           | **[STALE: current AEF §2 — PAE is a principle, not a number]**
| $OIE$            | Observer-Induced Entropy          | Net destabilizing externality introduced by agentic deviation          | $\mathbb{R}_{\ge 0}$ | Perturbation magnitude             | **[STALE: current AEF §2 — OIE is a process, not a number]**
| $\Delta S_{abs}$ | Absorbed Entropy                  | Total entropy absorbed or redirected from system degradation           | $\mathbb{R}_{\ge 0}$ | Disorder-equivalent measure        |
| $ELQ$            | Ethical Legitimacy Quotient       | Ratio of applied effort to absorbed destabilization                    | $\mathbb{R}_{\ge 0}$ | Dimensionless                      | **[STALE: current AEF §6 and Registry §VI deprecate $ELQ=PAE/\Delta S_{abs}$; coverage is ACR, which is not an ethical verdict]**
| $AU$             | Absorbic Unit                     | Unit representing corrective effort normalized to absorbed entropy     | scalar                | Ethical joule analog               | **[STALE: current AEF §6 and Registry §VI — AU remains reserved and undefined; no ethical joule is established]**
| $\lambda_{PAE}$  | PAE Coupling Coefficient          | Converts applied effort into geometric distortion reduction rate       | $\mathbb{R}_{> 0}$   | Effort-to-geometry bridge          |
| $\lambda_{OIE}$  | OIE Coupling Coefficient          | Converts agentic perturbation into geometric distortion increase rate  | $\mathbb{R}_{> 0}$   | Perturbation-to-geometry bridge    |

**Note:** All absorbed entropy terms previously denoted as $\Delta S_{absorbed}$ or $\Delta S_{kB}$ are standardized to $\Delta S_{abs}$. If Boltzmann units are required, they must be explicitly stated as units, not separate symbols.

---

# 3. Core Relations

## 3.1 Ethical Legitimacy Quotient

$$
ELQ = \frac{PAE}{\Delta S_{abs}}
$$

**[STALE: current AEF §6 and Registry §VI deprecate $ELQ=PAE/\Delta S_{abs}$; coverage is ACR, which is not an ethical verdict. No replacement ratio is invented here.]**

Interpretation:

* $ELQ > 1$: Effort exceeds destabilization; corrective surplus.
* $ELQ = 1$: Exact stabilization parity.
* $ELQ < 1$: Destabilization exceeds corrective effort; deficit accumulates.

## 3.2 Geometric Interpretation of ELQ (Bridge to Δ-Self)

From Δ-Self §13, the rate of epistemic distortion is:

$$
\frac{d}{dt}\mathcal{E}_i = \mathcal{F}_{OIE} - \mathcal{F}_{PAE}
$$

AEF provides the bridge between effort-accounting quantities (PAE, OIE) and geometric rates ($\mathcal{F}_{PAE}$, $\mathcal{F}_{OIE}$) via coupling coefficients:

$$
\mathcal{F}_{PAE} = \lambda_{PAE} \cdot PAE

**[STALE: $\lambda_{PAE}\cdot PAE$ treats PAE as a number; current AEF §2 rejects that; no replacement formula is invented here. Later displayed products in this draft have the same status.]
$$

$$
\mathcal{F}_{OIE} = \lambda_{OIE} \cdot OIE
$$

Substituting into the Δ-Self distortion dynamics:

$$
\frac{d}{dt}\mathcal{E}_i = \lambda_{OIE} \cdot OIE - \lambda_{PAE} \cdot PAE
$$

The Lyapunov condition (HKL §5, $\frac{dV}{dt} \le 0$) is satisfied when: **[STALE / WITHDRAWN / DEAD CITE: current HKL §5 is Effect accounting; §4 says $\dot V\le 0$ is not a universal necessary condition; §7 withdraws necessary-monotonic-drift wording]**

$$
\lambda_{PAE} \cdot PAE \ge \lambda_{OIE} \cdot OIE
$$

Which gives the **geometric ELQ constraint**:

$$
ELQ_{geo} = \frac{\lambda_{PAE} \cdot PAE}{\lambda_{OIE} \cdot OIE} \ge 1
$$

When $\lambda_{PAE} = \lambda_{OIE}$ (symmetric coupling), this reduces to:

$$
PAE \ge OIE
$$

**[STALE: current AEF §6 and Registry §VI — $PAE\ge OIE$ is not a current accounting equation / conceptual shorthand only; PAE and OIE are not numbers. No replacement inequality is invented here.]**

The familiar constraint. Asymmetric coupling ($\lambda_{PAE} \ne \lambda_{OIE}$) captures systems where correction is harder or easier than destabilization — a structural property of the manifold, not an accounting artifact.

---

## 3.3 Absorbic Unit Definition

One Absorbic Unit ($AU$) represents normalized corrective effort per absorbed entropy unit. **[STALE: current AEF §6 and Registry §VI — AU remains reserved and undefined; no ethical joule is established. The displayed identity is not a current definition.]**

Conceptually:

$$
1\, AU = \frac{1\, J}{1\, \Delta S_{abs}}
$$

This is an accounting normalization, not a physical thermodynamic identity. **[STALE: same reservation; this is not a current official unit.]**

---

## 3.4 Effort Decomposition (Model-Dependent)

A model-dependent decomposition of $PAE$ may be expressed as:

$$
PAE = E - C_{pae}
$$

**[STALE: current AEF §6 lists $PAE=E-C_{pae}$ among expressions that are not current accounting equations. PAE is a principle, not a budget residual. No replacement decomposition is invented here.]**

Where:

* $E$: Total available energy or effort budget.
* $C_{pae}$: Structural inefficiencies or corrective overhead.

This decomposition is illustrative and not the definition of $PAE$ itself.

---

# 4. Structural Interpretation

In a causally closed system:

* Destabilizing externalities ($OIE$) propagate unless absorbed.
* Absorption requires applied effort ($PAE$).
* If $PAE < \Delta S_{abs}$, instability accumulates. **[STALE: compares PAE as a number to an entropy term; current AEF §2 and §6 reject that accounting.]**

AEF therefore functions as a corrective accounting constraint layered atop a stability measure (HKL, $V(t)$), operating over the trajectory geometry defined by Δ-Self.

The three-layer relationship:

* **Δ-Self** defines the trajectory, the manifold structure ($S_\Phi$, $G_i$), and the distortion dynamics.
* **HKL** defines the basin — *where* stability lives — and identifies $\mathcal{E}_i$ as the primary burden component.
* **AEF** defines the effort accounting — *what it costs* to keep $\frac{d}{dt}\mathcal{E}_i \le 0$.

AEF does not define the basin. It does not define the trajectory. It defines the cost of remaining within the basin along the trajectory.

---

# 5. Coupling Coefficients: Structural Notes

The coupling coefficients $\lambda_{PAE}$ and $\lambda_{OIE}$ are properties of the manifold geometry, not free parameters. They encode:

* **$\lambda_{PAE}$**: How efficiently corrective effort translates into distortion reduction on $S_\Phi$. Depends on the local curvature of the accessible informational manifold and the quality of the agent's reconstruction $G_i$.
* **$\lambda_{OIE}$**: How readily agentic perturbation roughens the metric. Depends on the sensitivity of $g^{(S_\Phi)}$ to observer-induced deformation.

In principle, both are derivable from the metric structures $g^{(G_i)}_{ij}$ and $g^{(S_\Phi)}_{ij}$. In practice, they serve as the accounting interface: AEF operates on (PAE, OIE) while Δ-Self operates on ($\mathcal{F}_{PAE}$, $\mathcal{F}_{OIE}$), and the $\lambda$ coefficients mediate between the two namespaces.

---

# 6. ELQ Triangle (Cross-Document Integration)

The ELQ bridges all three documents:

| Condition | AEF Reading | HKL Reading | Δ-Self Reading |
| --------- | ----------- | ----------- | -------------- |
| $ELQ_{geo} > 1$ | Corrective surplus | $\frac{dV}{dt} < 0$: converging to basin | $\frac{d}{dt}\mathcal{E}_i < 0$: distortion decreasing |
| $ELQ_{geo} = 1$ | Exact parity | $\frac{dV}{dt} = 0$: marginal equilibrium | $\frac{d}{dt}\mathcal{E}_i = 0$: distortion stable |
| $ELQ_{geo} < 1$ | Corrective deficit | $\frac{dV}{dt} > 0$: diverging from basin | $\frac{d}{dt}\mathcal{E}_i > 0$: distortion increasing |

This is a single phenomenon described in three namespaces.

---

# 7. Namespace Clarification

AEF symbols belong to the **Effort Accounting Namespace**.

They must not be conflated with:

* Stability/Basin symbols (e.g., $V(t)$, $V^*$, $\Delta V$) — elaborated in HKL
* Identity/Geometry symbols (e.g., $\Delta g_i$, $g_{ij}$, $\mathcal{E}_i$) — defined in Δ-Self

**Cross-namespace bridges:** $\lambda_{PAE}$ and $\lambda_{OIE}$ are defined here in AEF as the interface between effort-accounting and geometric namespaces. They convert AEF scalars into Δ-Self geometric rates. These are AEF-owned symbols that operate *at* the namespace boundary.

---

# 8. Normalization Changes Executed in v2

* All v1 changes retained ($\Delta S_{abs}$ standardization, symbol scoping, model-dependent clarification)
* Added inheritance statement linking AEF to Δ-Self §13 and HKL §5.1 **[DEAD CITE: current HKL has no §5.1]**
* Added §3.2: Geometric interpretation of ELQ via coupling coefficients
* Introduced $\lambda_{PAE}$ and $\lambda_{OIE}$ as bridge operators (effort → geometry)
* Derived $ELQ_{geo}$ constraint and symmetric/asymmetric coupling cases
* Added §5: Structural notes on coupling coefficients as manifold properties
* Added §6: ELQ Triangle cross-document integration table
* Updated §7: Cross-namespace bridge ownership rules
* Added both $\lambda$ symbols to glossary

---

End of Normalized AEF v2
