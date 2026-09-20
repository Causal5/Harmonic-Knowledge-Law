# Harmonic Knowledge Law (HKL)

## Lyapunov Basin Formalism — v2
### Aligned to Δ-Self Worldline Formalization
---

# 1. Purpose

The Harmonic Knowledge Law (HKL) defines the stability structure governing bounded, interdependent systems. It provides the basin formalism within which corrective effort (AEF) operates.

HKL does not define corrective effort. It defines deviation and stability geometry.

**Note:** "Law" is contextual to this body of work, not a structural claim of reality.

**Inheritance:** HKL elaborates the stability structure introduced in Δ-Self §§13, 17–18. Specifically, it decomposes the Lyapunov stability function $V_i = f(\mathcal{E}_i)$ into its component burden terms and defines the basin geometry within which Δ-Self trajectories evolve.

---

# 2. Section-Scoped Symbol Definitions

| Symbol        | Name                        | Meaning in this document                                  | Type / Domain         | Interpretation                       |
| ------------- | --------------------------- | --------------------------------------------------------- | --------------------- | ------------------------------------ |
| $V(t)$        | Lyapunov Stability Function | Aggregate corrective burden at time $t$                   | $\mathbb{R}_{\ge 0}$ | Basin deviation metric               |
| $V^*$         | Least-Action Envelope       | Reference equilibrium or minimal viable burden            | $\mathbb{R}_{\ge 0}$ | Stability target                     |
| $\Delta V(t)$ | Basin Deviation             | $V(t) - V^*$                                              | $\mathbb{R}$         | Signed deviation from envelope       |
| $B_k(t)$      | Burden Component            | $k$th stability burden term                               | $\mathbb{R}_{\ge 0}$ | Component destabilization            |
| $w_k$         | Weight Coefficient          | Weight assigned to burden component $k$                   | $\mathbb{R}_{\ge 0}$ | Relative contribution                |
| $CIR$         | Circular Integration Ratio  | Fraction of remediated resource successfully reintegrated | $[0,1]$              | Water-cycle efficiency metric        |
| $\mathcal{E}_i$ | Epistemic Distortion Magnitude | $\|\Delta g_i\|$ (inherited from Δ-Self §11)          | $\mathbb{R}_{\ge 0}$ | Primary burden component             |

**Note:** The previous symbol $CI$ (Circular Integration) has been renamed to $CIR$ to avoid collision with Causal Integrity (CI-A0).

---

# 3. Geometric Grounding (Inherited from Δ-Self)

HKL operates over the informational manifold structure defined in Δ-Self §§0, 8:

$$
M \to S \to S_\Phi \to G_i
$$

Where:
- $S_\Phi$ = Agent-accessible informational manifold (deformed by history and interaction)
- $G_i = \Pi_i(S_\Phi)$ = Agent internal geometric reconstruction

The basin defined by HKL is a basin in $S_\Phi$-space. Stability means the agent's trajectory $\gamma(t)$ remains within a region where epistemic distortion $\mathcal{E}_i$ is bounded.

---

# 4. Core Stability Relation

The Lyapunov-style stability function is defined as:

$$
V(t) = \sum_k w_k B_k(t)
$$

Where each $B_k(t)$ represents a distinct destabilizing burden term.

## 4.1 Primary Burden Identification

The epistemic distortion magnitude $\mathcal{E}_i$ (Δ-Self §11) is the primary burden component:

$$
B_0(t) = \mathcal{E}_i(t) = \|\Delta g_i(t)\| = \|g^{(G_i)} - g^{(S_\Phi)}\|
$$

This grounds the Δ-Self placeholder $V_i = f(\mathcal{E}_i)$ (§18) as:

$$
V_i(t) = w_0 \cdot \mathcal{E}_i(t) + \sum_{k \ge 1} w_k B_k(t)
$$

Where $B_{k \ge 1}$ represent additional burden terms (resource depletion, coordination overhead, etc.) that HKL elaborates independently.

---

# 5. Stability Condition

Define basin deviation:

$$
\Delta V(t) = V(t) - V^*
$$

Stability requires:

$$
\frac{dV}{dt} \le 0
$$

Interpretation:

* $\frac{dV}{dt} < 0$: corrective drift toward stability.
* $\frac{dV}{dt} = 0$: marginal equilibrium.
* $\frac{dV}{dt} > 0$: destabilizing divergence.

## 5.1 Distortion-Stability Bridge

From Δ-Self §13:

$$
\frac{d}{dt} \mathcal{E}_i = \mathcal{F}_{OIE} - \mathcal{F}_{PAE}
$$

Since $\mathcal{E}_i$ is the primary burden component, the Lyapunov condition $\frac{dV}{dt} \le 0$ requires (at minimum):

$$
\mathcal{F}_{PAE} \ge \mathcal{F}_{OIE} + \frac{1}{w_0} \sum_{k \ge 1} w_k \dot{B}_k(t)
$$

This is the **basin maintenance inequality**: corrective effort must exceed not only epistemic destabilization but also the drift of all other burden components. This constraint is handed to AEF for effort-level elaboration.

---

# 6. Structural Interpretation

HKL formalizes the geometry of deviation within bounded systems.

* $V(t)$ measures accumulated systemic burden, with $\mathcal{E}_i$ as the geometrically grounded primary term.
* $V^*$ represents the least-action envelope — the PCB-equivalent (Δ-Self §4) at the basin level.
* $\Delta V(t)$ quantifies deviation from the stability basin.

HKL therefore provides the state-space structure within which:

* Absorbic Effort (AEF) determines required corrective input.
* Law of WE determines macro-scale coordination constraints.
* Δ-Self trajectories evolve and are evaluated.

HKL defines *where the basin is*.
AEF defines *what it costs to remain inside it*.
Δ-Self defines *what moves through it*.

---

# 7. Least-Action Envelope and PCB Correspondence

$V^*$ corresponds to the burden profile along the Passive Cost Baseline trajectory $\gamma_{PCB}(t)$ (Δ-Self §4):

$$
V^* = V\big|_{\gamma = \gamma_{PCB}}
$$

That is: the least-action envelope is the stability burden accumulated by a system following the trajectory absent recursive deviation. Any ΔSelf ≠ 0 introduces additional burden that must be absorbed (see AEF) or the system diverges from the basin.

---

# 8. Namespace Clarification

HKL symbols belong to the **Stability / Basin Namespace**.

They must not be conflated with:

* Effort Accounting symbols ($PAE$, $OIE$, $\Delta S_{abs}$) — elaborated in AEF
* Identity/Geometry symbols ($\Delta g_i$, $g_{ij}$, $\mathcal{E}_i$) — defined in Δ-Self, inherited here as burden input
* Implementation identifiers (code-level metrics)

**Cross-namespace inheritance:** $\mathcal{E}_i$ originates in the Identity/Geometry namespace (Δ-Self §11) and enters HKL as a burden component. It retains its geometric definition; HKL does not redefine it.

---

# 9. Normalization Changes Executed in v2

* All v1 changes retained (CIR rename, $V^*$ standardization, $\Delta V(t)$ standardization, explicit glossary)
* Added §3: Geometric grounding inherited from Δ-Self manifold ontology
* Added §4.1: Explicit identification of $\mathcal{E}_i$ as primary burden component $B_0$
* Added §5.1: Distortion-stability bridge deriving basin maintenance inequality
* Added §7: PCB correspondence for least-action envelope $V^*$
* Updated §8: Cross-namespace inheritance rules for $\mathcal{E}_i$
* Added $\mathcal{E}_i$ to symbol table

---

End of HKL Normalized v2
