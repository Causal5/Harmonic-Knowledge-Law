# Δ-Self Extension: Reachability and Constraint Evolution

## Definition reconciliation — Registry v0.3.1

**Status:** Current extension, 16 October 2026.
Inherits the [Worldline](delta-self-worldline-formalization.md) and
[registry](../Registry/causal-ethics-master-symbol-registry.md).

## 1. Realized state and conditioned constraints

The realized state is $x(t)\in S$, the coordinate is $(x(t),t)$, and the
worldline is $\gamma$. The structure $S_\Phi(t)$ records the physical
constraints and dependencies conditioned by history. It is distinct from
an agent's model $m_i(t)$ encoded through substrate $G_i(t)$.

With declared dynamics and external inputs, write

$$
x(t+\delta t)=\alpha_t(x(t),a_t,S_\Phi(t)),\qquad
S_\Phi(t')=\Psi_{t\to t'}(S_\Phi(t),\gamma|_{[t,t']}).
$$

The second expression abbreviates any required environmental inputs.
It is a modeling interface, not a universal physical evolution equation.

## 2. Three kinds of accessibility

| Object | Meaning |
|---|---|
| $\mathcal A_\Omega(t)$ | Actions feasible under the realized physical constraints |
| $\mathcal A_{i,acc}(t)$ | Feasible actions the agent can identify and attempt |
| $\mathcal R_i(t;h)$ | Agent-estimated future states or trajectories |

The accessible action set is a subset of physical feasibility by definition.
The agent's simulated candidates may nevertheless contain impossible actions
or paths; those candidates do not enter the accessible set merely by being
imagined.

Define actual reachability over horizon $h$ using admissible action sequences,
not a single present action:

$$
\mathcal R^{ont}_\Omega(t;h)=
\mathsf{Reach}_{\alpha,\Psi}
(x(t),S_\Phi(t),\mathcal A_\Omega,[t,t+h]).
$$

An application must say whether this denotes endpoint states or whole
continuations, and how disturbances, stochastic dynamics, and policies enter.
For deterministic dynamics with fully fixed inputs and policy, only one
continuation may remain. The notation does not establish indeterminism.

The viability-preserving subset $\mathcal R^{viab}_\Omega(t;h)$ contains only
continuations satisfying the declared HKL constraints throughout the horizon.
Estimated reachability $\mathcal R_i(t;h)$ may include impossible paths or omit
actual ones.

## 3. What history can change

Equal selected state observations need not imply equal reachable sets when
hidden constraints, environment, admissible controls, or dynamics differ.
For example, two reservoirs with equal present volume can have different
usable futures if their storage capacity or delivery infrastructure differs.

This is a conditional proposition about incomplete descriptions. If the
complete state, constraints, laws, permitted input sequences, and horizon
are identical, prior history alone cannot be invoked to assign different
reachable sets under the same reachability construction. Any persistent
effect of history must enter the state, constraints, or dynamics.

The old independent update symbol $\Psi_R$ is unnecessary. Recompute
reachability from updated dynamics and constraints; implementation shortcuts
must preserve that relationship.

## 4. PCB and deviation

PCB is the declared counterfactual obtained by removing specified
recursive-control terms. It is not automatically the expectation of an
unspecified action distribution. A stochastic baseline needs an explicit
distribution and a declared trajectory-comparison rule.

Use $\Delta_{\gamma,PCB}$ only where subtraction is defined; otherwise use
$d_\Gamma(\gamma,\gamma_{PCB})$. The acceleration-difference proxy
$\kappa_\Delta$ requires a common representation, metric, time scale, and
differentiability.

## 5. Agency interpretation

Recursive modeling, persistent comparison, selected action, and realized
consequences are the framework's proposed agency-related structure.
A nonzero trajectory distance alone does not distinguish cognition from
noise, imposed forcing, or non-cognitive feedback.

Information-sharing can reveal feasible futures. Material intervention can
change feasibility itself. Both can influence the realized worldline, but
their contributions must remain distinguishable.
