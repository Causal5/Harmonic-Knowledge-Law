# Harmonic Knowledge Law (HKL)

## Burden and viability — Registry v0.3.1

**Status:** Current definition-level specification, 16 October 2026.
“Law” identifies the research program; an application must establish its own
dynamics and evidence.

## 1. Inheritance and purpose

The [Worldline](../Delta-Self/delta-self-worldline-formalization.md)
identifies realized trajectories and observer-relative models.
The [registry](../Registry/causal-ethics-master-symbol-registry.md)
controls notation. HKL defines burden and a selected viable region;
[AEF](../Papers/absorbic-effort-framework.md) accounts for interventions and
burden flows. No missing Worldline section or universal model-error metric
is assumed.

## 2. Burden construction

For boundary $\Omega$, let $B_{k,\Omega}$ be a nonnegative raw burden in
channel $k$. Preserve its units and uncertainty. Define

$$
\beta_{k,\Omega}=N_{k,\theta}(B_{k,\Omega}),\qquad
V_\Omega=N_\theta((\beta_{k,\Omega})_k).
$$

Channel maps specify reference scales, direction, thresholds, and uncertainty.
The aggregation map acts on the normalized channels. One possible choice is

$$
V_\Omega=\sum_k w_k\beta_{k,\Omega},\qquad w_k\ge0.
$$

A weighted sum does not permit compensation for violating a separately
declared hard constraint. Retain the component vector alongside the aggregate.
Model mismatch can be a channel with an operational loss function; it is not
universally the primary burden, nor an unmeasured difference between an
internal graph metric and the total ontic geometry.

## 3. Three distinct reference objects

| Symbol | Role | Interpretation |
|---|---|---|
| $V^*_\Omega(t)$ | Selected viable reference | A target or comparison profile |
| $V_{PCB,\Omega}(t)$ | Burden along $\gamma_{PCB}$ | Descriptive counterfactual |
| $V_{max,\Omega}(t)$ | Selected viability boundary | Threshold for the specified model |

The first two may coincide in a particular justified model. They are not
identical by definition. Neither is a universal least-action envelope.

Reference deviation and boundary margin answer different questions:

$$
\Delta V_\Omega=V_\Omega-V^*_\Omega,\qquad
M_{V,\Omega}=V_{max,\Omega}-V_\Omega.
$$

Being above a preferred target does not itself mean crossing a viability boundary.

## 4. Viability, drift, and stability

Define a viable region, for example,

$$
\mathcal B_{V,\Omega}(t)=
\{x\in S:V_\Omega(x,t)\le V_{max,\Omega}(t)\}
\cap\{\text{declared hard constraints}\}.
$$

Viability over an interval means the trajectory remains in this region.
The region is not automatically a basin of attraction. An attractor,
dynamics, and attraction property require separate specification.
Along a differentiable trajectory,

$$
\dot M_{V,\Omega}=\dot V_{max,\Omega}-\dot V_\Omega.
$$

Increasing burden consumes a fixed scalar margin; it need not cause an exit.
For example, $V(t)=1+0.25\sin t$ stays below $V_{max}=2$ for all time although
$\dot V$ is positive on some intervals. Thus $\dot V\le0$ is not a universal
necessary condition for viability.

Conversely, declining burden is insufficient with a faster shrinking
boundary. Over $0\le t\le2$, let $V(t)=2-t$ and $V_{max}(t)=3-2t$.
The margin is $1-t$: it reaches zero at $t=1$ and becomes negative afterward,
despite $\dot V=-1$.

For an absolutely continuous scalar burden and fixed boundary, initial
membership plus $\dot V\le0$ almost everywhere is sufficient to preserve
the scalar inequality over the interval. It does not protect unmodeled
constraints or prove asymptotic convergence. For a moving boundary, use the
margin and a justified invariance analysis; a pointwise slope alone does not
settle stochastic, discontinuous, or unmodeled future behavior.

Use **Lyapunov-style burden function** until an application demonstrates
the required positivity, target set, dynamics, regularity, and derivative
conditions for a Lyapunov argument. A constant burden index is not by itself
evidence of equilibrium.

## 5. Effect accounting

AEF provides channel-matched achieved correction and burden-generation rates.
A favorable ACR covers only its declared OIE accounting. Exogenous
disturbances, passive recovery, delayed effects, and boundary transfers also
enter the burden dynamics.

When $V=\sum_k w_kB_k/s_k$ with fixed positive scales $s_k$ and fixed weights,
$\dot V=\sum_k(w_k/s_k)\dot B_k$. For nonlinear or time-varying maps,
differentiate the complete normalization and aggregation. A derivative of
an arbitrary index is not automatically a conserved physical flux.

## 6. Buffer

For a declared continuation scenario $\pi$:

$$
\tau^\pi_{buf,\Omega}(t)
=\inf\{s\ge0:x^\pi(t+s)\notin\mathcal B_{V,\Omega}(t+s)\}.
$$

No exit over an unlimited specified scenario gives infinity; no observed exit
before a finite horizon gives a censored lower bound. If already outside,
buffer is zero. With positive margin and positive locally constant closing rate,

$$
\widehat\tau^{lin}_{buf,\Omega}
=\frac{M_{V,\Omega}}{\dot V_\Omega-\dot V_{max,\Omega}}.
$$

This estimates a scalar-boundary exit. A hard physical threshold may fail
earlier. Recovery time to a desired target is a separate quantity.

## 7. Scope and migration

This specification replaces the current paper's universal least-action
reference, raw cross-unit sum, and necessary-monotonic-drift wording.
The recovered [v2 draft](../Working/hkl-lyapunov-v2.md) remains a historical
proposal and does not override these definitions. CIR is an application
metric with its own denominator, not a universal stability primitive.
