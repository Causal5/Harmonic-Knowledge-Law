# Δ-Self Worldline Formalization
### Bridging State, Coordinate, Identity, and Operator-Limited Simulation

**Status:** Registry v0.3-aligned integration release candidate.

---

# Purpose

This document formalizes the bridge between:

- ontic state,
- realized state-time coordinate,
- causal trajectory,
- history-dependent identity,
- operator-relative models and simulated futures.

Its central claim is limited but consequential:

> State recurrence does not imply coordinate recurrence, because a realized event is indexed by both state and ordered time.

The document also distinguishes what a system **is doing** from what an operator **models or simulates** about it.

---

# 0. Registry Inheritance

This document inherits notation from:

[`../Registry/causal-ethics-master-symbol-registry.md`](../Registry/causal-ethics-master-symbol-registry.md)

The controlling distinctions are:

- $\mathcal{M}$: operator-independent ontic domain;
- $S$: bounded system state space;
- $x(t)\in S$: realized system state;
- $G_i(t)$: operator $i$'s representational substrate;
- $m_i(t)$: operator $i$'s epistemic model;
- $p_i(\gamma\mid m_i(t))$: operator $i$'s simulated trajectory distribution.

Realized state, epistemic model, and simulated trajectory distribution are not interchangeable.

---

# 1. Ontic Domain and Bounded State

Let:

$$
\mathcal{M}
$$

denote the operator-independent causal domain.

Let:

$$
S
$$

denote the state space of a bounded system selected for analysis. The system's realized state at time $t$ is:

$$
x(t)\in S.
$$

$S$ is not identical to $\mathcal{M}$. It is a bounded state description induced over selected degrees of freedom within the wider ontic domain.

History and interaction may deform the system's accessible structure. Let:

$$
\Phi_t:S\rightarrow S_{\Phi}(t)
$$

where $S_{\Phi}(t)$ denotes the history-conditioned accessible state structure. This is an ontic constraint structure, not an observer's belief state.

---

# 2. Realized Coordinates

Let time be an ordered domain:

$$
t\in T
$$

with:

$$
t_{n+1}>t_n.
$$

Define the $n$th realized coordinate:

$$
c_n:=(x_n,t_n)\in C,
$$

where:

$$
C=S\times T.
$$

The realized trajectory is the ordered sequence:

$$
\gamma=\{c_0,c_1,c_2,\ldots\}.
$$

A system therefore does not merely occupy states. It realizes state-time coordinates.

---

# 3. Irreversible Coordinate Theorem

## Theorem

If:

$$
t_i\ne t_j,
$$

then:

$$
(x_i,t_i)\ne(x_j,t_j),
$$

even when:

$$
x_i=x_j.
$$

Therefore:

> State recurrence does not imply coordinate recurrence.

## Proof

Let:

$$
c_i=(x_i,t_i),\qquad c_j=(x_j,t_j).
$$

Suppose:

$$
x_i=x_j
$$

but:

$$
t_i\ne t_j.
$$

By ordered-pair identity:

$$
(x_i,t_i)\ne(x_j,t_j).
$$

Thus repeated states correspond to distinct realized events.

$\square$

---

# 4. Consequences

## 4.1 Forward Recurrence

A system may evolve:

$$
x_0\rightarrow x_1\rightarrow x_2\rightarrow x_0.
$$

The realized coordinates remain:

$$
(x_0,t_0),\ (x_1,t_1),\ (x_2,t_2),\ (x_0,t_3)
$$

with:

$$
t_3>t_0.
$$

The return to $x_0$ is a forward-time recurrence, not reversal to the earlier event.

## 4.2 Non-Erasable History

Define the causal ledger through coordinate $n$:

$$
L_n=(c_0,c_1,\ldots,c_n).
$$

Then:

$$
|L_{n+1}|=|L_n|+1.
$$

Recurrence does not remove prior ledger entries.

## 4.3 Finite State Spaces

Even if $S$ is finite, the coordinate space:

$$
C=S\times T
$$

can support an arbitrarily long realized trajectory while ordered time continues.

Therefore finite state cardinality does not imply finite history.

---

# 5. Trajectory Representation

Where a continuous parameterization is appropriate, write:

$$
\gamma(t)=(x(t),t).
$$

Identity is therefore not determined by state alone. It is associated with a realized curve or ordered ledger through coordinate space.

This statement does not require that the full ontic state be observable. It requires only that realized events remain historically distinct.

---

# 6. Passive Cost Baseline

Define the Passive Cost Baseline trajectory:

$$
\gamma_{PCB}(t).
$$

It represents the trajectory predicted when the document's specified recursive-deviation terms are removed.

PCB is a **descriptive counterfactual baseline**. It is not automatically:

- the least-energy path,
- the minimum-burden path,
- the stable path,
- the ethical path,
- or the desired path.

Any correspondence between PCB and a stability reference must be argued in the relevant HKL model.

---

# 7. Δ-Self as History-Dependent Deviation

Δ-Self names the historically accumulated deviation of a realized worldline relative to a declared counterfactual baseline.

## 7.1 Linear or Chart-Local Form

Where trajectories are represented in a common vector space or valid local chart, define:

$$
\Delta_{\gamma,PCB}(t)
:=
\gamma(t)-\gamma_{PCB}(t).
$$

This subtraction is not presumed to be globally valid on an arbitrary manifold.

## 7.2 General Trajectory-Distance Form

Where direct subtraction is not defined, use a declared trajectory-space metric:

$$
d_{\Gamma}\bigl(\gamma,\gamma_{PCB}\bigr).
$$

The metric, interval, and weighting of state dimensions must be stated.

## 7.3 Curvature Form

Where both trajectories are twice differentiable within a common representation, define deviation curvature:

$$
\kappa_{\Delta}(t)
=
\left\|
\ddot\gamma(t)-\ddot\gamma_{PCB}(t)
\right\|.
$$

Interpretation:

$$
\kappa_{\Delta}(t)>0
$$

indicates local reorientation of the realized trajectory relative to the selected passive baseline.

## 7.4 Integrated Deviation

Across $[t_0,t_1]$:

$$
\|\Delta\mathrm{Self}\|_{[t_0,t_1]}
=
\int_{t_0}^{t_1}\kappa_{\Delta}(t)\,dt,
$$

provided the curvature form and its units are well-defined.

This integral records cumulative reorientation. It does not by itself establish ethical value.

---

# 8. Operator-Relative Models and Simulated Futures

Let operator $i$ receive horizon-limited observations:

$$
\mathcal{M}
\xrightarrow{\mu_{i,t}}
\mathcal{O}_i(t).
$$

The operator organizes observations in a representational substrate:

$$
G_i(t),
$$

from which the operator constructs an epistemic model:

$$
m_i(t).
$$

An internal simulation operator:

$$
\Sigma_i:m_i(t)\rightarrow\Delta(\Gamma_i(t))
$$

produces:

$$
p_i(\gamma\mid m_i(t)),
$$

a normalized probability distribution over the candidate trajectory set $\Gamma_i(t)$.

The distinction is:

$$
\text{realized trajectory }\gamma
\ne
\text{epistemic model }m_i(t)
\ne
\text{simulated distribution }p_i(\gamma\mid m_i(t)).
$$

A model may omit an actually reachable path. It may also represent a path that is not physically reachable.

---

# 9. Entourage Effects

The Entourage method permits networked operators to exchange information, resources, labor, access, and coordination.

Its two channels are distinct.

## 9.1 Informational Channel

$$
\mathfrak{E}^{info}_i(t)
$$

updates $G_i(t)$, $m_i(t)$, or the support and calibration of $p_i(\gamma\mid m_i(t))$.

This may improve awareness of candidate paths, but total probability remains normalized:

$$
\sum_{\gamma\in\Gamma_i(t)}
p_i(\gamma\mid m_i(t))=1
$$

for a discrete candidate set.

## 9.2 Action-Capacity Channel

$$
\mathfrak{E}^{act}_i(t)
$$

updates the operator's accessible action and reachable sets:

$$
\mathcal{A}_{i,acc}(t),\qquad \mathcal{R}_i(t).
$$

Shared material or coordination capacity may alter actual reachability only when it changes realized system constraints through action.

Knowing more possible paths and possessing more executable paths are therefore different effects.

---

# 10. Relationship to HKL and AEF

This document defines **what moves through realized coordinate space**.

HKL defines the selected stability basin and burden drift associated with that motion.

AEF defines the corrective effort and destabilizing burden accounting required to remain within that basin.

The relationship is:

```text
Δ-Self / worldline
    defines realized trajectory and history

HKL
    defines stability geometry and burden drift

AEF
    defines corrective and destabilizing flow accounting
```

The legacy shorthand:

$$
PAE\ge OIE
$$

is not a dimensionally complete equation. It remains only a conceptual parity statement until AEF supplies channel-matched rates, conversion maps, boundaries, and an integration window.

---

# 11. Probability and Agency

An agent may simulate multiple candidate trajectories and select an action from an accessible action set. That is an epistemic and operational claim:

$$
p_i(\gamma\mid m_i(t)),
\qquad
\mathcal{A}_{i,acc}(t)\subseteq\mathcal{A}(t).
$$

This document does **not** infer from that fact that ontic evolution must be fundamentally indeterministic. It also does not define agency merely as random deviation.

The stronger framework claim is that capable agents can:

1. represent more than one candidate continuation;
2. evaluate anticipated consequences under bounded knowledge;
3. select and realize an action;
4. incur and potentially absorb the resulting thermodynamic and dependency costs.

The causal ledger records the realized result regardless of whether the operator predicted it correctly.

---

# 12. Conceptual Interpretation

A system may return to the same state, but it cannot return to the same realized coordinate.

The present coordinate therefore contains an irreversible historical distinction even when selected state variables recur.

Δ-Self does not assert an immutable substance. It identifies identity with historically realized position and deviation along a causal worldline.

---

# 13. Summary

A system can return to what it was under a selected state description.

It cannot return to when it was.

Therefore:

- state is not coordinate;
- coordinate is not history;
- history is not an observer model;
- an observer model is not the realized worldline;
- simulated possibility is not ontic reachability;
- trajectory deviation is not automatically ethical value.

Δ-Self is the history-dependent identity construct grounded in those distinctions.

---

End of Δ-Self Worldline Formalization — Registry v0.3 Integration Candidate
