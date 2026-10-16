# Absorbic Effort Framework (AEF)

## Definition reconciliation — Registry v0.3.1

**Status:** Current effort-accounting specification, 16 October 2026.
“Absorbic Ethics Framework” is the earlier title of the same AEF lineage.

## 1. Purpose and inheritance

AEF accounts for corrective effort, achieved correction, generated burden,
and transfers within a declared boundary. It inherits the
[registry](../Registry/causal-ethics-master-symbol-registry.md),
[Worldline](../Delta-Self/delta-self-worldline-formalization.md), and
[HKL](../HKL/hkl-lyapunov.md) definitions. It does not inherit an
epistemic-distortion differential equation absent from the current Worldline.

The boundary may be open. Imports, exports, delayed effects, and interventions
across it must be declared rather than assumed away through “causal closure.”

## 2. Principle, process, expenditure, and effect

**PAE — Principle of Absorbic Effort:** elective corrective effort by a capable
agent to absorb, prevent, or locally reconcile destabilizing burden.

**OIE — Observer-Induced Entropy:** the causal process by which agentic action
generates, transfers, or amplifies destabilizing burden across dependencies.

PAE is a principle and OIE is a process. Neither is a number. The established
elective meaning of PAE is retained. A physical implementation consumes
resources, but expenditure alone does not establish corrective orientation,
successful correction, or cognition. A delegated mechanism can implement an
agent's corrective action without itself being classified as an agent.

For each attempt, record:

1. The agent, selected action, corrective target, boundary, and interval.
2. Planned allocation separately from actual expenditure, in native units.
3. The expected effect and the observations or comparison used to estimate it.
4. Achieved correction, latency, failures, induced burden, and transfers.

Energy can be measured in joules, labor in hours, and money in currency.
These quantities need explicit conversion models before combination.
An unmeasured expenditure is unknown, not zero. Passive recovery is not
automatically attributed to the intervention.

| Quantity | Meaning | Units |
|---|---|---|
| $\dot E_{PAE,i,k}$ | Actual corrective-effort rate | Declared resource unit/time |
| $E_{PAE,i,k}[t_0,t_1]$ | Expended effort over the interval | Integral of the rate |
| $\mathcal Q^{nom}_{PAE}$ | Nominal/planned allocation | Native units |
| $\dot B^{land}_{PAE,k}$ | Achieved burden reduction attributable to correction | Burden-channel unit/time |
| $\dot B_{OIE,k}$ | Attributed OIE burden generation | Same burden-channel unit/time |
| $\mathcal F^{land}_{PAE,k},\mathcal F^+_{OIE,k}$ | Converted effective rates | Common burden scale/time |

“Landed” means achieved effect. Prevention requires an explicit counterfactual
or other causal-identification method; the absence of damage alone is not an
estimate of how much damage was prevented.

## 3. Effort-to-effect models

A simple local model may use

$$
\mathcal F^{land}_{PAE,k}(t)
=\lambda_{PAE,k}(t)\dot E_{PAE,k}(t).
$$

The coefficient has the units required by the selected conversion. It must
be calibrated or derived within that model. It is not universally a
dimensionless efficiency and is not supplied by the definition of PAE.
Where multiple resources or agents contribute, specify the composition rule.
Do not sum overlapping corrections twice.

Model adequacy, physical actuation, access, timing, and coordination can
affect the mapping. The Sahel proposal motivates separating these effects;
it does not supply a universal homomorphism coefficient or prove that all
correction vanishes below an unmeasured variety threshold.

## 4. Matched coverage

For a fixed boundary $\Omega$, positive denominator, common time window,
and declared positive linear rate conversion $N^{rate}_\theta$:

$$
\mathrm{ACR}_\Omega[t_0,t_1]
=
\frac{\int_{t_0}^{t_1}
N^{rate}_\theta((\dot B^{land}_{PAE,k})_k)\,dt}
{\int_{t_0}^{t_1}
N^{rate}_\theta((\dot B_{OIE,k})_k)\,dt}.
$$

The numerator includes correction of the targets and channels represented
by the denominator. Correcting unrelated natural disturbances cannot be
counted as compensation for agent-generated damage. Report those effects
separately, together with the full burden balance.

ACR above, equal to, or below one means a surplus, parity, or deficit of
matched achieved correction relative to the accounted OIE burden.
Zero denominator makes the ratio undefined; retain the underlying rates.
If attribution or commensuration is unavailable, report separate channels
instead of manufacturing a scalar ratio.

Coverage is not ethical legitimacy. A favorable ratio can coexist with
pre-existing damage, an uncorrected critical channel, externalized burden,
or a failed service floor.

## 5. Burden balance and the HKL connection

For one burden stock $B_k$, a declared additive local balance is

$$
\dot B_k=
\dot B_{OIE,k}+\dot B_{exo,k}+\dot B_{in,k}
-\dot B^{land}_{PAE,k}-\dot B_{pass,k}-\dot B_{out,k}.
$$

Here the extra terms are section-local positive magnitudes for exogenous
generation, imports, passive removal, and exports, respectively, all in
channel units/time. Agent-induced side burden belongs in the OIE term.
This equation requires a measurable stock and a valid source/sink model;
it is not asserted for arbitrary psychological or social scores.

An export reduces the local stock while potentially burdening a receiver.
Record the recipient and transport losses. Separate physical burden
transport from energy or resources sent to implement correction.

For fixed linear normalizations $\beta_k=B_k/s_k$ with positive reference
scales $s_k$, and fixed nonnegative weights:

$$
V=\sum_k w_k B_k/s_k,\qquad
\dot V=\sum_k(w_k/s_k)\dot B_k.
$$

Only in a simplified model where OIE and corrective effects are the sole
terms does matched effective correction directly determine burden drift.
Nonlinear or changing normalizations require the relevant chain rule.
The measured burden dynamics, selected boundary, and hard constraints
determine viability as specified in HKL.

## 6. Restricted legacy terms

The raw expression $ELQ=PAE/\Delta S_{abs}$, the scalar inequality
$PAE\ge OIE$, and $PAE=E-C_{pae}$ are not current accounting equations.
The old “Ethical Legitimacy Quotient” name is replaced by ACR for defined,
matched coverage. It does not become an ethical verdict.

AU remains reserved and undefined. No physical “ethical joule” is established.
Entropy notation is restricted to thermodynamic entropy with declared units,
system, and sign. Corrective work can reduce a local burden while dissipating
energy; local correction does not imply decreasing total isolated-system entropy.

## 7. Research boundary

This revision supplies types, accounting requirements, and conditional
relations. It does not calculate the Sahel coefficient, validate a
consciousness test, or execute the freshwater protocol.
Earlier AEF v1 and recovered v2 wording remains in Git history and the
clearly labeled [working collection](../Working/README.md).
