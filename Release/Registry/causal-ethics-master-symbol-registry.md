# Causal Ethics — Master Symbol Registry

## Version 0.3.2 — Additive definitions from worked examples

**Status:** Current controlling definitions, 30 October 2026.

Version 0.3.2 adds sink impairment, correction type, OIE temporal class,
renewal coverage, corrective dependency, coupled renewal, and target type
(§VI.1, §VII.1, and the note in §V). It changes no v0.3.1 definition; papers
reconciled to v0.3.1 remain valid. The
[30 October decision record](definition-decisions-2026-10-30.md) gives the
reasons and the worked example that exposed each gap.

Version 0.3.1 preserved the conceptual meaning of v0.3 and reconciled its
measurement vocabulary with the current Worldline, Extension, HKL, and AEF
papers. The separate v0.4 research draft is not promoted by either revision.
The [16 October decision record](definition-decisions-2026-10-16.md) identifies
those adopted clarifications and deferred proposals.

## 0. Authority and rules

The registry controls notation. [Worldline](../Delta-Self/delta-self-worldline-formalization.md)
defines realized history and operator-relative representation;
[Extension](../Delta-Self/delta-self-extension.md) defines reachability;
[HKL](../HKL/hkl-lyapunov.md) defines burden and viability;
[AEF](../Papers/absorbic-effort-framework.md) defines effort and effect accounting.
These are complementary roles, not a derivation of one theory from another.

1. One symbol has one meaning in its declared namespace.
2. Declare the system boundary, channel, units, time interval, and claim status.
3. A principle, process, stock, rate, accumulation, field, ratio, and model are distinct objects.
4. Ontic realization, observation, model, representation, and simulation are distinct.
5. Normalize or convert unlike quantities before aggregation; publish the map.
6. A counterfactual baseline is descriptive unless a separate argument makes it a target.
7. Keep physical feasibility separate from the agent's knowledge of it.
8. Keep intended effort, expended resources, and achieved correction separate.
9. Include boundary transfers and side effects; local improvement may export burden.
10. Every difference symbol identifies its referent; direct subtraction needs a common space.
11. Borrowed physical or mathematical language is an analogy unless the relevant identity and assumptions are established.
12. Software identifiers do not define theoretical quantities.

An application may omit indices only after fixing them unambiguously.

## I. Ontology, state, and boundaries

| Symbol | Meaning | Type and restriction |
|---|---|---|
| $\mathcal M$ | Operator-independent causal domain | General state-bearing domain; a manifold only where justified |
| $\Omega$ | Declared system/accounting boundary | Includes selected dependencies and transfers |
| $S$ | Bounded system state space | Induced over selected degrees of freedom in $\mathcal M$ |
| $x(t)$ | Realized system state | $x(t)\in S$; not an observer model |
| $T$ | Ordered time domain | $t_{n+1}>t_n$ for ledger entries |
| $\Phi_t$ | History-and-interaction deformation operator | $S\rightarrow S_\Phi(t)$ |
| $S_\Phi(t)$ | History-conditioned ontic constraint structure | Structure over $S$; not a belief state |
| $\mathcal A_\Omega(t)$ | Physically feasible action set | Physical constraints at the declared boundary |
| $a_t$ | Realized action | Member of $\mathcal A_\Omega(t)$ |
| $\alpha_t$ | Realization operator in a declared dynamics model | $(x(t),a_t,S_\Phi(t))\mapsto x(t+\delta t)$; external inputs or stochastic laws must be specified when applicable |
| $\delta t$ | Declared time increment | Positive time interval |
| $i,\ k$ | Agent and burden-channel indices | Index sets must be declared |

No operator is assumed to know $\mathcal M$, $x(t)$, or $S_\Phi(t)$ completely.

## II. Observation, representation, and simulation

| Symbol | Meaning | Type and restriction |
|---|---|---|
| $\mathcal O_i(t)$ | Observations available to operator $i$ | Horizon-limited information set |
| $\mu_{i,t}$ | Observation operator | $\mathcal M\rightarrow\mathcal O_i(t)$ |
| $G_i(t)$ | Representational substrate | Graph, memory, or symbolic/physical storage structure |
| $m_i(t)$ | Epistemic model encoded through $G_i(t)$ | Model of selected state and dependencies |
| $\Gamma_i(t)$ | Represented candidate trajectories | May omit feasible paths or include infeasible paths |
| $\Sigma_i$ | Internal simulation operator | $m_i(t)\rightarrow\Delta(\Gamma_i(t))$ |
| $p_i(\gamma\mid m_i(t))$ | Simulated trajectory distribution | Normalized; not the set of actual futures |
| $\mathcal A_{i,acc}(t)$ | Actually feasible actions identifiable and attemptable by $i$ | $\mathcal A_{i,acc}(t)\subseteq\mathcal A_\Omega(t)$; excludes merely imagined impossible actions |
| $\mathcal R_i(t;h)$ | Operator-estimated reachable set over horizon $h$ | An estimate; need not be a subset of actual reachability |
| $\widehat\varepsilon^{mdl}_{i,\Omega}$ | Estimated model-mismatch diagnostic | Declared loss against observations; not direct access to ontic error |

The representation chain is
$\mathcal M\xrightarrow{\mu_{i,t}}\mathcal O_i(t)\rightarrow G_i(t)
\rightarrow m_i(t)\xrightarrow{\Sigma_i}p_i(\gamma\mid m_i(t))$.
Total simulated probability remains one when candidate support changes.

## III. Entourage

| Symbol | Meaning | Restriction |
|---|---|---|
| $\mathfrak E^{info}_i(t)$ | Information-sharing update | Updates $G_i,m_i,p_i$ |
| $\mathfrak E^{act}_i(t)$ | Material/action-capacity update | Shared labor, resources, access, or coordination |

Information can reveal an already feasible action. It changes physical capacity
only through realized changes to constraints, resources, or control.

## IV. Identity, coordinates, and reachability

| Symbol | Meaning | Type and restriction |
|---|---|---|
| $C$ | Realized coordinate space | $S\times T$ |
| $c_n$ | Realized coordinate | $(x_n,t_n)\in C$ |
| $\gamma$ | Realized worldline | Ordered sequence or curve of coordinates |
| $L_n$ | Ledger through coordinate $n$ | Ordered sequence $(c_0,\ldots,c_n)$; append-only by construction |
| $\gamma_{PCB}$ | Passive Cost Baseline | Counterfactual with explicitly removed recursive-control terms |
| $\Delta_{\gamma,PCB}$ | Trajectory displacement from PCB | Valid only in a common vector space or suitable chart |
| $d_\Gamma(\gamma,\gamma_{PCB})$ | Trajectory-space distance | Declared metric, interval, weights, and units |
| $\kappa_\Delta(t)$ | Deviation-curvature proxy | Difference of trajectory accelerations in a declared common representation; not generally coordinate-invariant geometric curvature |
| $\Delta\mathrm{Self}$ | History-dependent identity-deviation construct | Resolved through registered trajectory quantities |
| $h$ | Prospective horizon | Nonnegative duration |
| $\Psi_{t\to t'}$ | Constraint-evolution operator | Updates $S_\Phi$ using realized history and declared inputs |
| $\mathsf{Reach}_{\alpha,\Psi}$ | Reachability construction | Uses dynamics, constraints, admissible action sequences, and horizon |
| $\mathcal R^{ont}_\Omega(t;h)$ | Physically reachable continuations | State or trajectory set; the chosen kind must be declared |
| $\mathcal R^{viab}_\Omega(t;h)$ | Viability-preserving reachable subset | Subset of $\mathcal R^{ont}_\Omega(t;h)$ |
| $d_S$ | State-space distance | Declared metric or pseudometric and units |

Different times give different coordinates even if states recur:
$t_i\ne t_j\Rightarrow(x_i,t_i)\ne(x_j,t_j)$.
This ordered-pair result does not itself establish thermodynamic irreversibility.
An append-only historical ledger is not a claim that every physical memory is lossless.

## V. HKL burden and viability

| Symbol | Meaning | Type and restriction |
|---|---|---|
| $\mathbf B_\Omega(t)$ | Vector of raw burden channels | Channel-specific nonnegative quantities |
| $B_{k,\Omega}(t)$ | Raw burden in channel $k$ | Native units; distinguish stocks from rates |
| $N_{k,\theta}$ | Channel normalization | Maps $B_k$ to dimensionless $\beta_k$; declares scale and direction |
| $\beta_{k,\Omega}(t)$ | Normalized burden | Dimensionless, nonnegative |
| $N_\theta$ | Aggregation of normalized channels | Declared map to a nonnegative burden index |
| $w_k$ | Post-normalization weight | Nonnegative, with sensitivity analysis |
| $V_\Omega(x,t)$ | Lyapunov-style burden function | $N_\theta((\beta_{k,\Omega})_k)$ |
| $V^*_\Omega(t)$ | Selected viable reference burden | Reference/target, not an exit boundary |
| $V_{PCB,\Omega}(t)$ | Burden along PCB | Descriptive counterfactual |
| $V_{max,\Omega}(t)$ | Declared scalar viability boundary | Application-specific threshold |
| $\Delta V_\Omega(t)$ | Deviation from the reference | $V_\Omega(t)-V^*_\Omega(t)$ |
| $M_{V,\Omega}(t)$ | Scalar viability margin | $V_{max,\Omega}(t)-V_\Omega(t)$ |
| $\mathcal B_{V,\Omega}(t)$ | Selected viable region | Example: $\{x:V_\Omega(x,t)\le V_{max,\Omega}(t)\}$, intersected with all hard constraints |
| $\dot V_\Omega(t)$ | Drift along the realized trajectory | Burden-index units/time |

For a weighted example, $V_\Omega=\sum_k w_k\beta_{k,\Omega}$.
Raw quantities with incompatible units may not be added.
Time-varying weights or reference scales contribute to $\dot V$ and must be
accounted for. No universal identity $V^*=V_{PCB}$ is assumed.

Viability means satisfying the declared constraints over the specified horizon.
It does not universally require $\dot V\le0$ at every interior point.
The margin evolves as $\dot M_V=\dot V_{max}-\dot V$.
Nonpositive drift is a useful sufficient scalar-boundary check when the
boundary is fixed, the system starts inside, and all other constraints hold.
It is not a proof of asymptotic stability. The [HKL paper](../HKL/hkl-lyapunov.md)
states the distinction and counterexamples.

**Target type (v0.3.2).** Declare each viability target as a *function target*,
met by any adequate source of the function, or a *dependency target*, met only
by a specified dependency. For a dependency target, composition and renewal
channels are hard constraints; a substitute supplying the same aggregate
service cannot offset them.

## VI. PAE, OIE, effort, and achieved effect

### Concept labels

| Term | Controlling meaning | Type |
|---|---|---|
| PAE | **Principle of Absorbic Effort:** elective corrective effort by a capable agent to absorb, prevent, or locally reconcile destabilizing burden | Principle; not a scalar or unit |
| OIE | **Observer-Induced Entropy:** the causal process by which agentic action generates, transfers, or amplifies destabilizing burden across dependencies | Process/category; not a scalar or automatically thermodynamic entropy |

PAE retains its v0.3 meaning. Physical expenditure is a property to account
for in a realized attempt; it does not replace elective corrective orientation.
“Elective” identifies agent-directed selection and does not require a
metaphysical conclusion about free will. Delegated mechanisms can implement
an agent's correction without being classified as cognitive agents themselves.

An attempt can be costly and unsuccessful. Passive recovery is recorded
separately. Effects on exogenous disturbances are not automatically
OIE compensation. OIE attribution needs evidence beyond observing a rising
burden index.

### Measured quantities

| Symbol | Meaning | Type and units |
|---|---|---|
| $\dot E_{PAE,i,k}$ | Actual corrective-effort rate | One declared resource unit/time; energy uses J/time |
| $E_{PAE,i,k}[t_0,t_1]$ | Accumulated expended effort | Integral of $\dot E_{PAE,i,k}$ |
| $\mathcal Q^{nom}_{PAE}$ | Planned or nominal corrective allocation | Native budget/capacity units; not expended effort |
| $\dot B^{land}_{PAE,k}$ | Achieved corrective burden-reduction rate | Native burden-channel units/time |
| $\dot B_{OIE,k}$ | Attributed OIE burden-addition rate | Same burden-channel units/time |
| $B_{OIE,k}[t_0,t_1]$ | Accumulated attributed OIE burden | Integral of $\dot B_{OIE,k}$ |
| $\mathcal F^{land}_{PAE,k}$ | Normalized achieved corrective rate | Declared common burden scale/time |
| $\mathcal F^+_{OIE,k}$ | Normalized OIE-generated burden rate | Same scale/time |
| $\lambda_{PAE,k}$ | Model-specific effort-to-effect coefficient | Converts one declared effort rate into a specified correction rate |
| $\lambda_{OIE,k}$ | Perturbation-to-burden conversion coefficient | Needed only when the input is not already in burden units |
| $N^{rate}_\theta$ | Rate conversion and aggregation map | Declared common scales and weights; not silently the state-normalization map |
| $\mathrm{ACR}_\Omega[t_0,t_1]$ | Absorbic Coverage Ratio | Matched achieved correction divided by attributed OIE burden |

The boundary $\Omega$ is required even when omitted from table subscripts.
Different effort channels retain their own units. Money, labor-hours, and
energy are not interchangeable without an empirical conversion; a resource
vector is preferable when no defensible common scale exists.

The shorthand $\mathcal F^{land}_{PAE,k}=\lambda_{PAE,k}\dot E_{PAE,k}$
is a calibrated model, not an identity proving successful correction.
A simple scalar coefficient may fail under latency, saturation, interference,
or changing local conditions. Separate model adequacy and physical actuation
when the application supports that decomposition. The v0.4 homomorphism
architecture remains a proposal rather than a universal conversion law.

For positive denominator and matched boundary, time window, attribution, and
conversion map:

$$
\mathrm{ACR}_\Omega[t_0,t_1]=
\frac{\int_{t_0}^{t_1}N^{rate}_\theta((\dot B^{land}_{PAE,k})_k)\,dt}
{\int_{t_0}^{t_1}N^{rate}_\theta((\dot B_{OIE,k})_k)\,dt}.
$$

The numerator counts only correction attributable to the burden channels and
targets covered by the denominator; report other correction separately.
Use a positive linear rate map for additive coverage accounting. A different
nonlinear score requires its own interpretation and cannot inherit that
accounting meaning. Define zero-denominator cases as undefined; report the
underlying quantities rather than assigning automatic success.

$\mathrm{ACR}\ge1$ records coverage within this accounting model. It does not
establish ethical legitimacy, overall viability, complete recovery, or
non-externalization. Exogenous inputs, passive recovery, transfers, existing
stocks, and hard constraints still matter.

| Legacy item | Disposition |
|---|---|
| $PAE\ge OIE$ | Conceptual shorthand only; use matched measured rates in equations |
| $ELQ=PAE/\Delta S_{abs}$ | Deprecated: principle and entropy do not form a defined dimensionless ratio |
| $ELQ_{geo}$ | Legacy coverage label; migrate to ACR only after checking actual quantities and attribution |
| $AU$ | Reserved/undefined; no “ethical joule” is established |
| $\Delta S_{abs}$ | Restricted to physical entropy with declared system, sign, and units such as J/K |
| $\mathcal F_{PAE,k},\mathcal F_{OIE,k}$ | Legacy rate labels; specify achieved effect and attributed source explicitly |

### VI.1 Passive removal, sink impairment, and correction type (v0.3.2)

| Symbol | Meaning | Type and units |
|---|---|---|
| $\dot B_{pass,k}$ | Realized passive removal (as in AEF) | Channel units/time |
| $\dot B^{cf}_{pass,k}$ | Passive removal with the impairing OIE process absent | Modeled counterfactual; method declared |
| $\dot B^{0}_{pass,k}$ | Passive removal with the impairing process present and correction absent | Modeled or pre-intervention reference |
| $\dot B^{imp}_{OIE,k}$ | Sink-impairment OIE rate | $\dot B^{cf}_{pass,k}-\dot B^{0}_{pass,k}$; classed as impairment when positive |
| $\dot B^{gen}_{OIE,k}$ | Direct OIE burden generation | The v0.3.1 $\dot B_{OIE,k}$ |
| $\dot B^{land,sub}_{PAE,k}$ | Substituting landed correction | Removal supplied directly by the intervention |
| $\dot B^{land,rest}_{PAE,k}$ | Pathway-restoring landed correction | $\dot B_{pass,k}-\dot B^{0}_{pass,k}$ when causally attributable |
| $c_{OIE}$ | OIE temporal class | *pulse*, *persistent*, or *self-propagating* |
| $h_{attr}$ | Attribution horizon for self-propagating OIE | Declared duration; at least two values reported |
| $\mathrm{ACR}^{ext}_\Omega[t_0,t_1]$ | Extended Absorbic Coverage Ratio | Attributed form: substituting plus restoring correction over generation plus impairment; the v0.3.1 ACR is unchanged |

By construction
$\dot B_{pass,k}=\dot B^{cf}_{pass,k}-\dot B^{imp}_{OIE,k}+\dot B^{land,rest}_{PAE,k}$.
The AEF burden balance may be written in a *realized* form (direct generation
$\dot B^{gen}_{OIE,k}$, substituting correction only, realized $\dot B_{pass,k}$) or
an *attributed* form (generation plus impairment, both kinds of landed
correction, counterfactual $\dot B^{cf}_{pass,k}$). The two are equal term for
term. Use one form per analysis; never subtract realized passive removal while
also adding impairment. In the realized form, pathway-restoring effects are
already inside $\dot B_{pass,k}$ and are not added to landed correction.

The v0.3.1 ACR above is unchanged. Where sink impairment is declared, also
report the extended coverage ratio, which uses the attributed rates:

$$
\mathrm{ACR}^{ext}_\Omega[t_0,t_1]=
\frac{\int_{t_0}^{t_1}N^{rate}_\theta\left(\left(\dot B^{land,sub}_{PAE,k}+\dot B^{land,rest}_{PAE,k}\right)_k\right)dt}
{\int_{t_0}^{t_1}N^{rate}_\theta\left(\left(\dot B^{gen}_{OIE,k}+\dot B^{imp}_{OIE,k}\right)_k\right)dt}.
$$

All ACR conditions apply unchanged. With no declared impairment it equals the
v0.3.1 ACR; with impairment declared, the v0.3.1 ACR covers direct generation
only and is reported alongside it.

OIE remains a process. A persistent source's burden-generation rates may form a
continuous, spatially extended rate field; the process is what is attributed and
what removal ends. For self-propagating OIE, burden after $h_{attr}$ is reported
separately as exogenous burden with provenance, and each further introduction,
escapement, or release is a new OIE event.

## VII. Buffer and Temporal Mining

These definitions support future application work; they do not promote the
original Buffer manuscript or assert completed freshwater calculations.

| Symbol | Meaning | Restriction |
|---|---|---|
| $\pi$ | Declared continuation scenario | Dynamics, policy, disturbances, and horizon |
| $\tau^\pi_{buf,\Omega}(t)$ | Time to first exit from the viable region | Scenario-dependent; time or infinity |
| $\tau^\pi_{rec,\Omega}(t)$ | Time to a separately declared recovery target | Not a negative buffer |
| $\widehat\tau^{lin}_{buf,\Omega}$ | Local linear estimate of exit time | Positive margin and closing boundary required |
| $\tau_s$ | Renewal or recovery timescale | Estimated from renewal dynamics |
| $\tau_d$ | Net depletion time to a declared floor | Scenario-dependent |
| $\tau_{age}$ | Age/residence-time statistic | Not automatically $\tau_s$ |
| $\tau_{draw}$ | Gross stock-to-withdrawal timescale | Not net time to exhaustion |
| $\rho_{TM}$ | Temporal Mining timescale ratio | $\tau_s/\tau_d$ for positive, finite comparable timescales |
| $\rho_R$ | Reserved application label for a reachability ratio | Distinct from $\rho_{TM}$; no automatic $[0,1]$ bound |

$$
\tau^\pi_{buf,\Omega}(t)=
\inf\{s\ge0:x^\pi(t+s)\notin\mathcal B_{V,\Omega}(t+s)\}.
$$

If already outside, buffer is zero. If no exit ever occurs under the specified
scenario, $\inf\varnothing=+\infty$. A finite observation or simulation horizon
with no exit is right-censored, not evidence of infinite buffer.

For positive margin and positive closing rate:

$$
\widehat\tau^{lin}_{buf,\Omega}
=\frac{V_{max,\Omega}-V_\Omega}{\dot V_\Omega-\dot V_{max,\Omega}}.
$$

This is a local linear approximation. An unmodeled hard-constraint crossing
can occur earlier. Spatial averages do not replace the most vulnerable
dependency or the whole-system first-exit calculation.

### VII.1 Renewal coverage and corrective dependency (v0.3.2)

| Symbol | Meaning | Restriction |
|---|---|---|
| $R^{nat}_{s}$ | Natural renewal rate of a stock | Same units and window as $L_s$ |
| $R^{man}_{s}$ | Managed renewal rate (managed recharge, stocking) | Same units and window |
| $L_{s}$ | Gross loss rate from the stock | Withdrawal, mortality, predation, other losses |
| $\eta^{nat}_{TM}$ | Natural renewal coverage | $R^{nat}_s/L_s$ for $L_s>0$; zero allowed |
| $\eta^{tot}_{TM}$ | Total renewal coverage | $(R^{nat}_s+R^{man}_s)/L_s$ for $L_s>0$ |
| — | Renewal status (exclusive) | *Net mining* ($\eta^{tot}_{TM}<1$), *substituted* ($\eta^{nat}_{TM}<1\le\eta^{tot}_{TM}$), or *covered* ($\eta^{nat}_{TM}\ge1$) |
| — | Severed flag (independent) | Set when $\eta^{nat}_{TM}=0$ apart from declared episodic events; occurs with *net mining* or *substituted*, never *covered* |
| $\pi_{cont},\ \pi_{stop}$ | Scenarios continuing or ending corrective expenditure | Identical except for the declared stop time |

Renewal coverage is a screen, not a viability result. With $L_s=W_g$ and
$R^{nat}_s+R^{man}_s=R_n+R_m$, $\eta^{tot}_{TM}=1/X_R$ of the freshwater protocol.
$\rho_{TM}$ is used only where both timescales are positive and finite; severed
renewal is reported through $\eta^{nat}_{TM}$. Episodic renewal is reported as an
event count and a window-averaged rate.

A system is **correctively dependent** over horizon $h$ when
$\tau^{\pi_{stop}}_{buf,\Omega}$ is finite within $h$ and shorter than
$\tau^{\pi_{cont}}_{buf,\Omega}$ by a declared margin, and the difference arises from
$\dot B^{imp}_{OIE,k}>0$ in a declared channel. The *substituted* status is a
screening indication only. Correction is *pathway-restoring* when its effect on
renewal or impairment persists after expenditure ends, and *substituting* when
it supplies renewal or removal only while expenditure continues.

**Coupled renewal.** A renewal term declares its dependence on its own stock and
on any other stocks it requires (for example, host fish), with the dependency
graph published. Density-dependent reproduction is not assumed without evidence.

## VIII. Freshwater annex

| Symbol | Meaning | Preferred units |
|---|---|---|
| $G_W,\ G_{ref},\ G_{min}$ | Recoverable stock, reference stock, operational floor | Volume |
| $W_g$ | Gross withdrawal rate | Volume/time |
| $R_n,\ R_m$ | Natural and managed recharge retained in boundary | Volume/time |
| $Q_{net}$ | Net lateral and connected-water inflow, excluding already counted recharge/withdrawal | Volume/time, signed |
| $D_W,\ D_{W,crit}$ | Delivered service and critical service requirement | Volume/time |
| $Q_{alt,firm}$ | Firm alternative supply/capacity | Volume/time |
| $C_{irr}$ | Irreversible compaction or storage-capacity loss | Declared physical measure |
| $TM_G$ | Positive net stock depletion | $[-\dot G_W]_+$ |
| $T_{gap}$ | Firm service-capacity gap | $[D_{W,crit}-Q_{alt,firm}]_+$ |
| $CIR$ | Circular Integration Ratio | Domain metric; explicit numerator and denominator required |

Physical stock-flow accounting precedes normalization:

$$
\dot G_W=R_n+R_m-W_g+Q_{net},\qquad
\tau_{draw}=\frac{G_W}{W_g},\qquad
\widehat\tau_d^{net}=\frac{G_W-G_{min}}{-\dot G_W}.
$$

The last two estimates require respectively $W_g>0$, and both
$G_W>G_{min}$ and $-\dot G_W>0$. Nonpositive current depletion does not
prove indefinite future sustainability. Age, reference, floor, stock loss,
and permanent capacity loss remain distinct.

## IX. Formal operators, FRF, and implementation

| Notation | Meaning or restriction |
|---|---|
| $\Delta_X$ | Difference in the stated referent $X$ |
| $\Delta(\Gamma)$ | Probability distributions on $\Gamma$, distinct from subtraction |
| $[z]_+$ | $\max(0,z)$ |
| $\widehat X$ | Estimate with method and uncertainty |
| $\partial,\nabla,\int,\sum$ | Require declared variables, metric/measure where applicable, and compatible units |

FRF denotes Forman–Ricci Flow in this project's proposal. Graph curvature,
contextual storage, retrieval, and admission into objective commitments are
different operations. Neither curvature nor retrieval establishes truth.
The SLP harness is a prototype; its identifiers are not theoretical primitives.
These boundary distinctions are adopted; a completed FRF admission mechanism
or compression result is not claimed.

## X. Migration and scope

Use $x(t)$ for realized state, $m_i(t)$ for model, and $G_i(t)$ for substrate.
Replace unqualified $\Delta I$, $\gamma_{act}$, and $\gamma_{pcb}$ in current
formal equations with the registered trajectory objects. Distinguish actual
from estimated reachability and reference from boundary.

The [16 October decision record](definition-decisions-2026-10-16.md) and
[publication notes](../Reviews/publication-notes-2026-10-16.md) identify which
papers are reconciled and which recovered sources retain historical wording.
The [30 October decision record](definition-decisions-2026-10-30.md) records the
additive v0.3.2 definitions, their established-concept counterparts, and the
reference tank model. Earlier files and the v0.4 draft do not override this registry.
