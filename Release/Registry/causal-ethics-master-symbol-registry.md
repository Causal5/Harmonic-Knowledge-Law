# Causal Ethics — Master Symbol Registry

## Version 0.3 — State, Model, Simulation, and Entourage Integration

**Status:** Integration release candidate. This registry controls notation for all documents revised after v0.3.

---

# Registry Rules

1. One symbol → one meaning → one namespace.
2. No bare difference symbols. Every use of $\Delta$ must identify its referent.
3. Ontic realization, bounded system state, epistemic model, representational substrate, and simulated trajectory distribution are distinct objects.
4. Mathematical symbols and implementation identifiers remain separate namespaces.
5. New repeated theoretical symbols must enter this registry before cross-document use.
6. Every dimensional quantity must declare units. Quantities from different channels may be aggregated only through an explicit normalization or conversion map.
7. $PAE$ and $OIE$ name a principle and a causal process. Measured rates and accumulated quantities use separate symbols.
8. A counterfactual baseline is descriptive unless a document separately justifies it as a normative or viability target.
9. Ethical viability is evaluated through continuity, stability, burden, and effort constraints—not inside observation, projection, or bridge operators.
10. Symbols borrowed from mathematics and physics are structural analogs unless a document explicitly establishes a physical identity.

---

# Namespace I — Ontology and Bounded System State

| Symbol | Canonical Meaning | Type / Domain | Notes | Introduced In |
|---|---|---|---|---|
| $\mathcal{M}$ | Ontic manifold / operator-independent causal domain | Manifold or general state-bearing domain | Reality is not collapsed into any observer model | CI-A0 / Δ-Self |
| $S$ | Bounded system state space | State space induced over selected degrees of freedom in $\mathcal{M}$ | $S$ is not identical to $\mathcal{M}$ | Δ-Self |
| $x(t)$ | Realized system state at time $t$ | $x(t)\in S$ | Ontically realized; never redefined as an observer model | Registry v0.3 |
| $T$ | Ordered time domain | Totally ordered set or interval | $t_{n+1}>t_n$ for realized ledger entries | Δ-Self |
| $\Phi_t$ | History-and-interaction deformation operator | $S\rightarrow S_{\Phi}(t)$ | Encodes realized constraint and dependency deformation | Δ-Self extension |
| $S_{\Phi}(t)$ | History-conditioned accessible state structure | Deformed subset or structure over $S$ | Ontic constraint structure, not an agent belief state | Δ-Self extension |
| $\mathcal{A}(t)$ | Physically feasible action set | Set | Feasible under current system constraints | Δ-Self |
| $\alpha_t$ | Ontic realization operator | $(x(t),a_t)\rightarrow x(t+1)$ | Maps selected action and current state into the next realized state | Law of WE / Δ-Self |

## Ontic relation

$$
x(t)\in S,\qquad S\text{ is induced over relevant structure in }\mathcal{M}.
$$

No operator is assumed to possess complete access to $x(t)$, $S_{\Phi}(t)$, or $\mathcal{M}$.

---

# Namespace II — Observation, Representation, and Simulation

| Symbol | Canonical Meaning | Type / Domain | Notes | Introduced In |
|---|---|---|---|---|
| $i$ | Operator / agent index | Index | Required whenever a model or representation is observer-relative | Registry v0.3 |
| $\mathcal{O}_i(t)$ | Observation set available to operator $i$ | Information set | Horizon-limited and lossy | Δ-Self 2 |
| $\mu_{i,t}$ | Measurement / observation operator | $\mathcal{M}\rightarrow\mathcal{O}_i(t)$ | Does not reproduce the ontic domain in full | Δ-Self 2, revised |
| $G_i(t)$ | Operator $i$'s representational substrate | Graph, memory, or structured symbolic system | Stores and organizes observations, relations, and commitments | SLP / Δ-Self 2 |
| $m_i(t)$ | Operator $i$'s epistemic model | Model encoded through $G_i(t)$ | Model of relevant state, dependencies, and constraints; not realized state | Registry v0.3 |
| $\Gamma_i(t)$ | Candidate trajectory set represented by operator $i$ | Set of trajectories | Support is bounded by model and simulation capacity | Registry v0.3 |
| $\Sigma_i$ | Internal simulation operator | $m_i(t)\rightarrow\Delta(\Gamma_i(t))$ | Produces a normalized distribution over candidate trajectories | Registry v0.3 |
| $p_i(\gamma\mid m_i(t))$ | Simulated trajectory distribution | Probability distribution on $\Gamma_i(t)$ | Total probability remains one; support and calibration may change | Registry v0.3 |
| $\mathcal{A}_{i,acc}(t)$ | Epistemically accessible action set | $\mathcal{A}_{i,acc}(t)\subseteq\mathcal{A}(t)$ | Actions operator $i$ can identify, select, and attempt | Δ-Self 2, revised |
| $\mathcal{R}_i(t)$ | Operator-estimated reachable set | Set of candidate future states or trajectories | Must not be conflated with actual ontic reachability | Registry v0.3 |

## Epistemic-simulation relation

$$
\mathcal{M}\xrightarrow{\mu_{i,t}}\mathcal{O}_i(t)
\longrightarrow G_i(t)
\longrightarrow m_i(t)
\xrightarrow{\Sigma_i}p_i(\gamma\mid m_i(t)).
$$

This chain is epistemic. It does not imply that the operator's probability support exhausts actual reachable futures.

---

# Namespace III — Entourage Channels

The **Entourage method** names networked information and resource sharing among operators. Its epistemic and material effects must remain distinct.

| Symbol | Canonical Meaning | Type / Domain | Notes | Introduced In |
|---|---|---|---|---|
| $\mathfrak{E}^{info}_i(t)$ | Entourage informational update | Operator on $G_i(t)$ and $m_i(t)$ | May expand support, improve calibration, or reduce model error | Registry v0.3 |
| $\mathfrak{E}^{act}_i(t)$ | Entourage action-capacity update | Operator on $\mathcal{A}_{i,acc}(t)$ and $\mathcal{R}_i(t)$ | Represents shared material, labor, access, or coordination capacity | Registry v0.3 |

Informational sharing does not by itself create ontic capacity. Material coordination may alter actual reachability only through realized changes to system constraints.

---

# Namespace IV — Identity, Coordinate, and Worldline (Δ-Self)

| Symbol | Canonical Meaning | Type / Domain | Notes | Introduced In |
|---|---|---|---|---|
| $C$ | Realized coordinate space | $S\times T$ | Coordinate space for realized state-time events | Δ-Self worldline |
| $c_n$ | $n$th realized coordinate | $c_n=(x_n,t_n)\in C$ | Replaces legacy $(s_n,t_n)$ notation | Registry v0.3 |
| $\gamma$ | Realized trajectory / worldline | Ordered sequence or curve in $C$ | $\gamma=\{c_0,c_1,\ldots\}$ | Δ-Self worldline |
| $L_n$ | Causal ledger through coordinate $n$ | Ordered sequence $(c_0,\ldots,c_n)$ | History is append-only in the formalization | Δ-Self worldline |
| $\gamma_{PCB}(t)$ | Passive Cost Baseline trajectory | Counterfactual trajectory | Continuation absent specified recursive-deviation terms; not automatically optimal or ethical | Δ-Self worldline |
| $\Delta_{\gamma,PCB}(t)$ | Trajectory deviation from PCB | Difference object or displacement when defined | Use a metric distance when direct subtraction is not defined | Registry v0.3 |
| $d_{\Gamma}(\gamma,\gamma_{PCB})$ | Trajectory-space distance | $\mathbb{R}_{\ge0}$ | Preferred where trajectories do not form a vector space | Registry v0.3 |
| $\kappa_{\Delta}(t)$ | Deviation-curvature magnitude | $\mathbb{R}_{\ge0}$ | Measures structural reorientation relative to PCB | Δ-Self worldline |
| $\Delta\mathrm{Self}(t)$ | Named history-dependent identity-deviation construct | Trajectory-dependent object | Equations should resolve it through registered trajectory or curvature quantities | Δ-Self |

## Irreversible Coordinate Theorem

If $t_i\ne t_j$, then

$$
(x_i,t_i)\ne(x_j,t_j)
$$

even when $x_i=x_j$. State recurrence therefore does not imply coordinate recurrence.

---

# Namespace V — Stability and Basin Geometry (HKL)

| Symbol | Canonical Meaning | Type / Domain | Notes | Introduced In |
|---|---|---|---|---|
| $\mathbf{B}(t)$ | Vector of burden channels | Product space of channel-specific quantities | Preserve channel units before normalization | HKL v2, revised |
| $B_k(t)$ | $k$th burden component | Channel-specific nonnegative quantity | Examples may include depletion, coordination, thermal, ecological, or model burden | HKL |
| $N_{\theta}$ | Declared normalization / aggregation map | $\mathbf{B}(t)\rightarrow\mathbb{R}_{\ge0}$ | Must state reference scales, weights, and uncertainty | Registry v0.3 |
| $w_k$ | Post-normalization weight | $\mathbb{R}_{\ge0}$ | Valid only after components are dimensionless or commensurate | HKL, revised |
| $V(t)$ | Lyapunov-style aggregate burden function | $\mathbb{R}_{\ge0}$ | Typically $V(t)=N_{\theta}(\mathbf{B}(t))$ | HKL |
| $V^*(t)$ | Selected viable reference burden profile | $\mathbb{R}_{\ge0}$ | Not universally identical to PCB or minimal action | HKL, revised |
| $V_{PCB}(t)$ | Burden evaluated along the PCB | $\mathbb{R}_{\ge0}$ | $V_{PCB}(t)=V\vert_{\gamma=\gamma_{PCB}}$; descriptive baseline | Registry v0.3 |
| $\Delta V(t)$ | Deviation from selected burden reference | $\mathbb{R}$ | $V(t)-V^*(t)$ | HKL |
| $V_{max}(t)$ | Viability boundary | $\mathbb{R}_{\ge0}$ | Crossing may indicate departure from the selected basin | Registry v0.3 |
| $\mathcal{B}_V(t)$ | Viable/stable basin | Subset of $S$ | Example definition: $\{x\in S:V(x,t)\le V_{max}(t)\}$ | Registry v0.3 |
| $\dot V(t)$ | Burden drift rate | Burden per unit time | Sign is interpreted only relative to the selected interval and basin | HKL |
| $CIR$ | Circular Integration Ratio | $[0,1]$ | Resource reintegration efficiency; application-specific denominator required | HKL |

A PCB may be used to construct a reference, but the correspondence must be argued rather than presumed.

---

# Namespace VI — Corrective Effort and Destabilizing Externality (AEF)

## Concept labels

| Term | Canonical Meaning | Status |
|---|---|---|
| $PAE$ | Principle of Absorbic Effort: elective corrective effort by a capable agent to absorb, prevent, or locally reconcile destabilizing burden | Principle, not a scalar |
| $OIE$ | Observer-Induced Entropy: the causal process by which agentic action generates, transfers, or amplifies destabilizing burden across dependencies | Process/category, not a scalar |

## Measured quantities

| Symbol | Canonical Meaning | Type / Units | Notes | Introduced In |
|---|---|---|---|---|
| $\dot E_{PAE,k}(t)$ | Applied corrective-effort rate in burden channel $k$ | Declared physical or normalized units per time | Must identify the corrected channel and boundary | Registry v0.3 |
| $E_{PAE,k}[t_0,t_1]$ | Accumulated corrective effort in channel $k$ | Declared physical or normalized units | Integral of $\dot E_{PAE,k}$ over the interval | Registry v0.3 |
| $\dot B_{OIE,k}(t)$ | OIE-generated burden rate in channel $k$ | Same channel units per time after conversion | Must include transferred burden where the boundary requires it | Registry v0.3 |
| $B_{OIE,k}[t_0,t_1]$ | Accumulated OIE burden in channel $k$ | Same channel units after conversion | Integral of $\dot B_{OIE,k}$ | Registry v0.3 |
| $\lambda_{PAE,k}$ | Corrective coupling coefficient | Conversion map or coefficient | Maps applied effort into reduction of normalized burden channel $k$ | AEF v2, revised |
| $\lambda_{OIE,k}$ | Destabilizing coupling coefficient | Conversion map or coefficient | Maps agentic perturbation into normalized burden channel $k$ | AEF v2, revised |
| $\mathcal{F}_{PAE,k}(t)$ | Effective corrective burden-reduction rate | Normalized burden per time | $\lambda_{PAE,k}\dot E_{PAE,k}(t)$ | AEF v2, revised |
| $\mathcal{F}_{OIE,k}(t)$ | Effective destabilizing burden-generation rate | Normalized burden per time | $\lambda_{OIE,k}\dot B_{OIE,k}(t)$ | AEF v2, revised |
| $ELQ_{geo}$ | Normalized corrective-to-destabilizing ratio | Dimensionless | Valid only when numerator and denominator are commensurate and boundary-matched | AEF v2, revised |

Where a scalar ratio is appropriate:

$$
ELQ_{geo}
=
\frac{\sum_k \mathcal{F}_{PAE,k}}
{\sum_k \mathcal{F}_{OIE,k}}.
$$

The denominator, system boundary, integration window, conversion maps, and uncertainty must be stated. $ELQ_{geo}\ge1$ is a local accounting condition, not by itself a complete ethical judgment.

## Restricted or deprecated quantities

| Symbol | Status | Rule |
|---|---|---|
| $\Delta S_{abs}$ | Restricted | Use only for actual entropy with declared thermodynamic units; do not use as a generic cross-domain burden scalar |
| $ELQ=PAE/\Delta S_{abs}$ | Deprecated | Dimensionless only after an explicit commensuration map; use $ELQ_{geo}$ where justified |
| $AU$ | Reserved / undefined | Do not use as a physical or accounting unit until a reproducible dimensional definition exists |

---

# Namespace VII — Formal Operators and Probability

| Symbol | Meaning | Rule |
|---|---|---|
| $\Delta_X$ | Difference in referent $X$ | Referent must be explicit |
| $\partial$ | Partial derivative | Use where differentiability assumptions are stated |
| $\nabla$ | Gradient operator | The field and metric must be identified |
| $\sum$ | Summation operator | Summands must be commensurate or explicitly normalized |
| $\Delta(\Gamma)$ | Probability simplex over trajectory set $\Gamma$ | Distinct from the difference operator by argument and context |

---

# Namespace VIII — Implementation Identifiers (Non-Theoretical)

Implementation names are not theoretical primitives. Examples:

- `oie_impact`
- `hkl_metrics`
- `V_star`
- `delta_v`
- `trajectory_support`
- `entourage_info_update`

They must appear in code blocks, schemas, or implementation appendices and must map explicitly to registered theory symbols when used analytically.

---

# Migration and Collision Log

| Legacy symbol or claim | Conflict | v0.3 resolution |
|---|---|---|
| $m(t)$ = realized ontic state | Collides with authorial use of $m_i(t)$ as epistemic model | Realized state becomes $x(t)$; epistemic model becomes indexed $m_i(t)$ |
| $s(t)$ = realized state | Collides with simulation terminology and overuses $S/s$ | Canonical realized state becomes $x(t)$; legacy $s(t)$ is deprecated |
| $S$ = ontic informational probability manifold | Conflates ontic domain, state space, and probability support | $\mathcal{M}$ is ontic domain; $S$ is bounded system state space; probabilities live on $\Delta(\Gamma_i)$ |
| $G(t)$ = internal representation | Observer index omitted | Canonical form is $G_i(t)$ |
| $\Delta I$ | Competes with worldline deviation and Δ-Self notation | Deprecated; use $\Delta_{\gamma,PCB}$, $d_{\Gamma}$, $\kappa_{\Delta}$, or $\Delta\mathrm{Self}$ as appropriate |
| $V^*$ = least-action envelope = PCB | Treats descriptive passive baseline as universal viability optimum | $V^*$ is a selected viable reference; $V_{PCB}$ is separately registered |
| $PAE$ as principle and scalar | Type ambiguity | $PAE$ remains the principle; measured quantities use $\dot E_{PAE,k}$ and $E_{PAE,k}$ |
| $OIE$ as process, field, and scalar | Type ambiguity | $OIE$ remains the causal process; measured quantities use $\dot B_{OIE,k}$ and $B_{OIE,k}$ |
| $\Delta S_{abs}$ as generic burden | Thermodynamic and dimensional overreach | Restricted to declared physical entropy quantities |
| $ELQ$ raw ratio | Unit mismatch hidden by notation | Deprecated unless explicitly commensurated; use $ELQ_{geo}$ with declared maps |
| $CI$ = Circular Integration | Collision with Causal Integrity | Circular Integration remains $CIR$ |
| Bare $\Delta$ | Ambiguous difference | Every difference must identify its referent |

---

# Pending Audit

- Propagate $x(t)$, $m_i(t)$, $G_i(t)$, and $p_i(\gamma\mid m_i(t))$ into all canonical Δ-Self files.
- Reconcile $S_{\Phi}(t)$ and metric notation across Δ-Self extensions.
- Promote HKL v2 only after replacing the universal PCB/$V^*$ identity with the conditional $V_{PCB}$ relation.
- Promote AEF v2 only after channel units and normalization maps are explicit.
- Register Temporal Mining and Continuation Filter reachability symbols during the parent-synthesis pass.
- Audit Law of WE metric, Lagrangian, and gradient notation before promotion.

---

End of Symbol Registry v0.3 — Integration Release Candidate
