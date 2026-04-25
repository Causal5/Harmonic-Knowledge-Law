# Causal Ethics — Master Symbol Registry

## Version 0.2 (Dual-Aspect Formalization — Δ-Self 2 Integrated)

---

# Registry Rules

1. One symbol → one meaning → one namespace.
2. No bare symbols (e.g., no standalone $\Delta$).
3. Mathematical symbols and implementation identifiers must remain separate namespaces.
4. All new symbols must be added here before publication use.
5. These are contextual symbols borrowed from 'real' math and applied as analogs/representations of function within this body of work.
6. Ontic variables: $\mathcal{M}$ and $m(t)$; informatic variables: $\mathcal{G}(t)$ and $G(t)$ must not be conflated.
7. Ethical viability is evaluated only in Stability (HKL) and Effort (AEF) namespaces, not inside bridge operators.

---

# Namespace I — Stability / Basin (HKL)

| Symbol          | Canonical Meaning                             | Type / Domain        | Notes                                  | Introduced In |
| --------------- | --------------------------------------------- | -------------------- | -------------------------------------- | ------------- |
| $V(t)$          | Lyapunov stability (burden) function          | $\mathbb{R}_{\ge 0}$ | Aggregate basin deviation              | HKL           |
| $V^*$           | Least-action envelope (reference equilibrium) | $\mathbb{R}_{\ge 0}$ | Stability target                       | HKL           |
| $\Delta V(t)$   | Basin deviation from reference                | $\mathbb{R}$         | $V(t) - V^*$                           | HKL           |
| $\frac{dV}{dt}$ | Stability drift rate                          | $\mathbb{R}$         | Sign determines convergence/divergence | HKL           |
| $B_k(t)$        | k-th destabilizing burden component           | $\mathbb{R}_{\ge 0}$ | Component term in $V(t)$               | HKL           |
| $w_k$           | Weight coefficient for burden component       | $\mathbb{R}_{\ge 0}$ | Relative contribution                  | HKL           |
| $CIR$           | Circular Integration Ratio                    | $[0,1]$              | Resource reintegration efficiency      | HKL           |

---

# Namespace II — Effort Accounting (AEF)

| Symbol           | Canonical Meaning                      | Type / Domain        | Notes                             | Introduced In |
| ---------------- | -------------------------------------- | -------------------- | --------------------------------- | ------------- |
| $PAE$            | Applied corrective effort              | $\mathbb{R}_{\ge 0}$ | Effort to offset destabilization  | AEF           |
| $OIE$            | Destabilizing externality              | $\mathbb{R}_{\ge 0}$ | Displaced system cost             | AEF / CI-A0   |
| $\Delta S_{abs}$ | Absorbed entropy / redirected disorder | $\mathbb{R}_{\ge 0}$ | Canonical absorbed entropy term   | AEF           |
| $ELQ$            | Ethical Legitimacy Quotient            | $\mathbb{R}_{\ge 0}$ | $ELQ = PAE / \Delta S_{abs}$      | AEF           |
| $AU$             | Absorbic Unit                          | scalar               | Normalized corrective effort unit | AEF           |

---

# Namespace III — Identity / Geometry (Δ-Self)

| Symbol                 | Canonical Meaning                     | Type / Domain                                      | Notes                                               | Introduced In  |
| ---------------------- | ------------------------------------- | -------------------------------------------------- | --------------------------------------------------- | -------------- |
| $\Delta I$             | Identity deviation vector             | Vector                                             | Deviation of agent trajectory                       | Δ-Self         |
| $\nabla S$             | Entropy gradient                      | Vector field                                       | Structural gradient reference                       | Δ-Self         |
| $g_{ij}$               | Metric tensor components              | Matrix                                             | Geometric structure                                 | Law of WE      |
| $\mathcal{M}$          | Ontic manifold state space            | Differentiable manifold                            | Total causal state space (inaccessible in totality) | Δ-Self 2       |
| $m(t)$                 | Realized ontic state at time $t$      | Element of $\mathcal{M}$                           | Physical state under causal evolution               | Δ-Self 2       |
| $\mathcal{G}(t)$       | Agent knowledge graph substrate       | Weighted discrete graph                            | Informatic geometric structure                      | SLP / Δ-Self 2 |
| $G(t)$                 | Agent internal representation state   | Element of $\mathcal{G}(t)$                        | Structured symbolic state                           | SLP            |
| $\mu_t$                | Measurement operator                  | $\mathcal{M} \rightarrow \mathcal{O}(t)$           | Horizon-limited, lossy observation                  | Δ-Self 2       |
| $\varepsilon_t$        | Probabilistic interpretation operator | $\mathcal{O}(t) \rightarrow \Delta(\mathcal{H})$   | Hypothesis distribution encoding (SIP layer)        | SLP            |
| $\kappa_t$             | Coarse-grain / symbol commit operator | $\Delta(\mathcal{H}) \rightarrow \mathcal{G}(t+1)$ | Equivalence-class resolution into graph             | SLP            |
| $\alpha_t$             | Ontic realization operator            | $(m(t), a_t) \rightarrow m(t+1)$                   | Physical action realization                         | Law of WE      |
| $\mathcal{A}_{acc}(t)$ | Accessible feasible action set        | Subset of $\mathcal{A}(t)$                         | Epistemically bounded admissible actions            | Δ-Self 2       |

---

## Dual-Aspect Coexistence Statement

Agents are dual-resident systems embedded in the ontic manifold $\mathcal{M}$ while operating through an internal discrete representational substrate $\mathcal{G}(t)$. Informatic updates occur through the composed mapping:

$$
\pi_t = \kappa_t \circ \varepsilon_t \circ \mu_t
$$

Ethical viability is evaluated only after ontic realization via $\alpha_t$ using Stability (HKL) and Effort (AEF) constraints.

---

# Namespace IV — Formal Math Operators

| Symbol     | Meaning             | Notes                                         |
| ---------- | ------------------- | --------------------------------------------- |
| $\Delta$   | Difference operator | Must always be subscripted (e.g., $\Delta V$) |
| $\partial$ | Partial derivative  | Used in continuous formulations               |
| $\nabla$   | Gradient operator   | Vector differential operator                  |
| $\sum$     | Summation operator  | Used in $V(t)$ construction                   |

---

# Namespace V — Implementation Identifiers (Non-Theoretical)

These identifiers exist only in implementation or simulation contexts and must not be treated as theoretical primitives.

Examples:

* `oie_impact`
* `hkl_metrics`
* `V_star`
* `delta_v`

These must always appear in code blocks or implementation appendices.

---

# Collision Log (Resolved)

| Previous Symbol       | Issue                                               | Resolution                                         |
| --------------------- | --------------------------------------------------- | -------------------------------------------------- |
| $CI$                  | Collision: Circular Integration vs Causal Integrity | Renamed Circular Integration to $CIR$              |
| $\Delta S_{absorbed}$ | Multiple absorbed entropy forms                     | Standardized to $\Delta S_{abs}$                   |
| Bare $\Delta$         | Ambiguous delta reference                           | All deltas must specify referent                   |
| $M_t$                 | Ambiguous macro/memory/state placeholder            | Removed; replaced with $m(t)$ and $\mathcal{G}(t)$ |

---

# Pending Audit

* Law of WE mathematical namespace isolation
* Lagrangian formal namespace consistency check

---

End of Symbol Registry v0.2
