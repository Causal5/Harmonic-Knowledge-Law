# Buffer as Temporal Dimension
## Cross-Corpus Re-Anchor

### Cross-references: Δ-Self Worldline Formalization, Δ-Self Extension, HKL Lyapunov v2, AEF v2, Fallacy of Large-Scale Absorbic Effort, Continuation Filter, Sahel Worked Example

---

# 1. Purpose

This addendum formalizes the **temporal dimension** that the corpus has been operating without. It introduces buffer ($\tau_{buffer}$), corrective flux ($J_{PAE}$), the coherence functional ($\mathcal{C}(t)$), regeneration rate ($\rho_{regen}$), depletion rate ($\rho_{deplete}$), coordination coherence density ($\kappa_{coord}$), and perturbation-field variability ($\Omega_{var}$) as cross-corpus structural objects.

The corpus to date has expressed temporal claims through instantaneous quantities — $dV/dt$, $d\mathcal{E}_i/dt$, $\mathcal{F}_{PAE} - \mathcal{F}_{OIE}$ — which are necessary but insufficient. Stability requires not only that these inequalities hold at a moment, but that they hold across the *runway* available before basin exit. The runway is buffer.

This addendum supplies the buffer formalism and threads it back through Δ-Self, HKL, AEF, the Fallacy of Large-Scale Absorbic Effort, and the Continuation Filter. The Sahel Worked Example §6 demonstrates the buffer formalism in application; this document is the structural commitment beneath it.

Buffer is corpus-wide infrastructure. It is not a Sahel-specific construct.

---

# 2. The Cellular Constitution Principle

A constitutive principle anchors what follows.

> Sublimation of dry ice does not spontaneously decouple and evaporate the entire thermal mass. Each molecule absorbs enough energy proximal to radiant heat collision and molecule bond by molecule bond the entire thermal mass of the dry ice block sublimates.

Macro stability is constituted by, not additional to, the integrated absorption of micro-cellular components. There is no thermal-mass-as-a-whole that absorbs; there is only the sum of local absorptions, each happening at a specific molecular site under specific local conditions.

This principle applies recursively. Any framework object that operates at "macro" scale must be decomposable to micro-cellular constituents. **Macro-as-primary is a category error.** Aggregate readings are diagnostic of cellular fields, not constitutive of stability.

Throughout this addendum, "patch-local" or "patch-wise" denotes the cellular level at which framework objects are constituted. Integrated quantities ($\int \tau_{buffer} \, d\mu$, etc.) are observable, reportable, and useful — but they are summaries of the cellular field, never the thing itself. Optimizing the integral while eroding the field reproduces the cellular constitution error one level up.

---

# 3. Section-Scoped Symbol Definitions

| Symbol | Name | Type | Domain | Interpretation |
|---|---|---|---|---|
| $\tau_{buffer}(x, t)$ | Buffer field | Scalar field on $S_\Phi$ | $\mathbb{R}_{\ge 0}$ (time) | Runway at patch $x$ before basin exit at current rate |
| $J_{PAE}(x, t)$ | Corrective flux | Vector field on $S_\Phi$ | $TS_\Phi$ | Directional flow of corrective effort across patches |
| $\mathcal{C}(t)$ | Coherence functional | Scalar | $\mathbb{R}$ | Distinguishes distribution from externalization |
| $\rho_{regen}(x, t)$ | Regeneration rate | Scalar field on $S_\Phi$ | $\mathbb{R}_{\ge 0}$ | Local rate of buffer regeneration |
| $\rho_{deplete}(x, t)$ | Depletion rate | Scalar field on $S_\Phi$ | $\mathbb{R}_{\ge 0}$ | Local rate of buffer depletion |
| $\kappa_{coord}(x, t)$ | Coordination coherence density | Scalar field on $S_\Phi$ | $\mathbb{R}_{\ge 0}$ | Phase-coherent regulator density at patch |
| $\Omega_{var}(x, t)$ | Perturbation-field variability | Scalar field on $S_\Phi$ | $\mathbb{R}_{\ge 0}$ | Variance burden in the disturbance field |
| $j_{PAE}(x, t)$ | Local PAE budget | Scalar field on $S_\Phi$ | $\mathbb{R}_{\ge 0}$ | Effort budget applied at patch $x$ |

All quantities are patch-wise unless explicitly integrated.

---

# 4. Buffer

## 4.1 Definition

For a patch $x$ at time $t$ with stability function $V(x, t)$ (HKL §4) and basin envelope $V^*(x)$ (HKL §7):

$$
\tau_{buffer}(x, t) = \frac{V^*(x) - V(x, t)}{\dot{V}(x, t)} \quad \text{when } \dot{V}(x, t) > 0
$$

Buffer is the *time to basin exit* at current burden velocity. Units: time. Bounded below by zero (basin exit imminent); unbounded above (runway extending).

When $\dot{V}(x, t) \le 0$, buffer is regenerating rather than depleting; the formula inverts to recovery time toward $V^*$. The signed quantity $\tau_{buffer}$ together with the sign of $\dot{V}$ classifies the patch's regime.

## 4.2 Buffer as Field

$\tau_{buffer}$ is a field over $S_\Phi$, not a scalar. Patch-wise variation matters: a manifold can carry high integrated buffer while specific patches sit at zero runway. The integrated quantity $\int_{S_\Phi} \tau_{buffer}(x, t) \, d\mu(x)$ is a **diagnostic readout**, not the thing being maintained.

This is the cellular constitution principle (§2) applied to the buffer field itself. Policy interventions targeting integrated buffer while eroding the cellular field commit the macro-as-primary error.

## 4.3 Buffer Dynamics

The local burden velocity decomposes into regeneration and depletion rates:

$$
\dot{V}(x, t) = \rho_{deplete}(x, t) - \rho_{regen}(x, t)
$$

When $\rho_{regen} > \rho_{deplete}$, $\tau_{buffer}$ extends. When $\rho_{regen} < \rho_{deplete}$, $\tau_{buffer}$ contracts. Basin exit occurs when $V(x, t) \to V^*(x)$ — the patch can no longer sustain perturbation within its corrective architecture.

---

# 5. Corrective Flux $J_{PAE}$

## 5.1 Definition

$J_{PAE}$ is a vector field on the manifold:

$$
J_{PAE}: S_\Phi \to TS_\Phi
$$

$J_{PAE}(x, t)$ is the directional flow of corrective effort across patch boundaries. Local patch behavior is classified by the divergence:

$$
\nabla \cdot J_{PAE}(x, t) \begin{cases} < 0 & \text{patch is a sink (absorbing)} \\ = 0 & \text{patch is neutral (pass-through)} \\ > 0 & \text{patch is a source (exporting)} \end{cases}
$$

## 5.2 Flux as Buffer Transport

$J_{PAE}$ has a clean physical interpretation: it is the directional flow of *buffer* across patches. Two regimes are structurally distinct, and they are not distinguishable from the scalar PAE budget alone.

**Distributive transport.** $J_{PAE}$ flows from patches with surplus $\tau_{buffer}$ toward patches with depleted $\tau_{buffer}$. Total integrated buffer is preserved or grows because high-$\lambda_{PAE}$ patches donate runway to neighbors who absorb it productively. The Fallacy paper's "absorbed entropy" without displacement is precisely up-gradient flux.

**Externalization.** $J_{PAE}$ flows down the buffer gradient — from low-buffer patches outward, dumping onto neighbors. The source patch's apparent buffer surplus is borrowed from neighboring runway. Total integrated buffer decreases even when scalar $V$ at the source patch appears stable. The Fallacy paper's "displaced burden" and the Continuation Filter's "exported entropy" are precisely down-gradient flux.

## 5.3 Coherence Functional

The two regimes are distinguished by the coherence functional:

$$
\mathcal{C}(t) = \int_{S_\Phi} J_{PAE}(x, t) \cdot \nabla \tau_{buffer}(x, t) \, d\mu(x)
$$

When $J_{PAE}$ flows up the buffer gradient (toward depleted patches), $\mathcal{C}(t) > 0$: distributive correction. When $J_{PAE}$ flows down the buffer gradient (away from depleted patches, dumping onto neighbors), $\mathcal{C}(t) < 0$: externalization.

**Critical:** the sign of $dV/dt$ does not distinguish these regimes. A centralized system maintaining $dV/dt \le 0$ at a focal patch by externalizing burden has $\mathcal{C}(t) < 0$ — the basin maintenance inequality is satisfied locally while the manifold is hollowing. $\mathcal{C}(t)$ is the formal object that detects this; the Fallacy paper has been describing it in prose.

---

# 6. Regeneration

## 6.1 The Three-Quantity Bound

Local regeneration is structurally bounded:

$$
\rho_{regen}(x, t) \le \frac{\lambda_{PAE}(x, t) \cdot \kappa_{coord}(x, t) \cdot j_{PAE}(x, t)}{1 + \Omega_{var}(x, t)}
$$

Three structural quantities bound regeneration, none reducible to the others:

- **$\lambda_{PAE}$** — homomorphism efficiency (Sahel §5.3): the fidelity of the regulator's internal model $G_i$ to the manifold $S_\Phi$. Conant–Ashby coefficient. Collapses when the regulator does not contain a model of what it regulates.

- **$\kappa_{coord}$** — coordination coherence density: phase-coherent regulator density at patch $x$. Captures whether multiple local regulators arrive in synchronized register or in destructive interference. Distinct from sheer headcount.

- **$\Omega_{var}$** — perturbation-field variability: variance in the disturbance field itself (rainfall stochasticity, market shocks, conflict, pest pressure, supply instability). Independent of regulator behavior.

## 6.2 Why Three, Not Two

$\kappa_{coord}$ and $\Omega_{var}$ must be separated. Collapsing them into one term conflates regulator failure with environmental complexity, obscuring which is operative.

**$\kappa_{coord}$** captures regulator-side variability: irregular timing, intermittent coordination, stochastic methodology fidelity, duplicated effort, phase-canceling correction. These are failures of regulator coherence.

**$\Omega_{var}$** captures perturbation-side variability: variance in the disturbance field that even a perfectly-coordinated regulator cannot eliminate by being more coherent. A regulator faces a moving target.

Both reduce $\rho_{regen}$, but through different mechanisms. The framework requires the distinction because intervention design requires it: low $\rho_{regen}$ caused by low $\kappa_{coord}$ is addressed through coordination structure; low $\rho_{regen}$ caused by high $\Omega_{var}$ requires shock-buffering and variance management.

## 6.3 Patch-Locality of $\kappa_{coord}$

By the cellular constitution principle (§2), $\kappa_{coord}$ is a patch-local quantity. **Inter-patch coordination is not a primitive.** It is the integrated readout of patch-local $\kappa_{coord}$ values across adjacent patches whose regulators are in homomorphic register with overlapping $S_\Phi$ regions.

Watershed-scale synchronization is constituted by, not additional to, village-scale $\kappa_{coord}$. Writing $\kappa_{coord}$ as a patch-pair object would reproduce macro-as-primary error at the coordination layer. Coordination is something patches *have* (locally); coordination effects are something the manifold *exhibits* (as readout) when many patches have it simultaneously.

---

# 7. The Asymmetry Between Depletion and Regeneration

Recovery is structurally burdened by coordination, fidelity, and energy constraints in ways disruption need not symmetrically satisfy.

**Depletion** is bounded above by physics. Shock can destroy buffer at rates the regulator cannot match in real time; a drought, a market collapse, a cadastral imposition can deplete $\tau_{buffer}$ across many patches simultaneously without requiring regulator participation. The rate-limit on depletion is the rate at which the perturbation arrives.

**Regeneration** is bounded above by $\lambda_{PAE} \cdot \kappa_{coord}$ and damped by $\Omega_{var}$. It requires a regulator whose model is homomorphic to $S_\Phi$, enough such regulators acting coherently, sufficient stability in the disturbance field, and energy expenditure proportional to the regeneration achieved. Each factor can collapse regeneration regardless of how much PAE is nominally spent.

The asymmetry is structural: destruction does not require coherence; reconstruction does. This is not a contingent feature of bad architecture. It bounds what any regulator can do in any system, and it is the structural reason the Continuation Filter operates the way it does.

---

# 8. Spatial Integration vs Temporal Differentiation

Two distinct calculus operations on two distinct dimensions.

## 8.1 Spatial Integration Constitutes Stabilization

Local absorptions integrate across the cellular extent:

$$
S_{abs}(t) = \int_{S_\Phi} \lambda_{PAE}(x, t) \cdot \kappa_{coord}(x, t) \cdot j_{PAE}(x, t) \, d\mu(x)
$$

This is the accumulation side. Stabilization is constituted by the spatial integral of cellular absorption, weighted by homomorphism efficiency and coordination coherence at each patch. The integrand is patch-local; the integral is the manifold-level constitution.

Variability in regulator phase fragments this integral: micro-absorptions arrive but not in coherent register, so the effective integral is smaller than headcount alone would predict. This is what $\kappa_{coord} < 1$ does — it down-weights the contribution of regulators who are present but not in phase.

## 8.2 Temporal Differentiation Reveals Buffer Dynamics

Buffer is the temporal derivative reading of the same accumulation:

$$
\frac{d\tau_{buffer}(x, t)}{dt} \quad \text{governed by} \quad \rho_{regen}(x, t) - \rho_{deplete}(x, t)
$$

Spatial integration tells you what the system has accumulated; temporal differentiation tells you whether the runway is growing or collapsing. Both calculus operations are required:

- High spatial integral with negative temporal derivative → system burning down accumulated buffer faster than regenerating
- Positive temporal derivative with low spatial integral → system regenerating too slowly to matter
- High spatial integral *and* positive temporal derivative → genuinely stabilizing
- Low spatial integral *and* negative temporal derivative → in collapse

The corpus has been operating predominantly at the temporal-derivative layer ($dV/dt$, $d\mathcal{E}_i/dt$) without explicitly naming the spatial-integration layer. This addendum names both and supplies their relationship.

---

# 9. Cross-Corpus Re-Anchor

Buffer is corpus-wide. The following sections re-anchor each existing document to the buffer formalism without modifying the documents' core commitments.

## 9.1 Δ-Self Worldline Formalization & Δ-Self Extension

The realized trajectory $\gamma(t)$ deviates from $\gamma_{PCB}(t)$. Buffer reads as the temporal extent over which Δ-Self deviation can be sustained before the trajectory exits the basin of $S_\Phi$:

$$
\tau_{buffer}^{(\Delta)}(t) = \text{time until } \gamma(t) \notin \mathcal{R}_{stable}(t)
$$

Epistemic distortion $\mathcal{E}_i = \|g^{(G_i)} - g^{(S_\Phi)}\|$ can grow within $\tau_{buffer}^{(\Delta)}$; what the buffer measures is how long the regulator has to update $G_i$ before the divergence becomes structural. Chaos-as-$\mathcal{E}_i$ acquires temporal teeth here: chaos manifests when $\mathcal{E}_i$ grows faster than $\tau_{buffer}$ permits regulator update, regardless of whether the underlying dynamical system is classically chaotic.

## 9.2 HKL Lyapunov v2

$V(t)$ is instantaneous burden. Its temporal interpretation requires buffer:

$$
\tau_{buffer}(x, t) = \frac{V^*(x) - V(x, t)}{\dot{V}(x, t)} \quad \text{when } \dot{V}(x, t) > 0
$$

The basin maintenance inequality $dV/dt \le 0$ (HKL §5) is necessary but instantaneous. Sustained basin maintenance requires $dV/dt \le 0$ across $\tau_{buffer}$ — the system must remain in basin over its runway, not merely at any moment. HKL §4.1's primary burden component $B_0 = \mathcal{E}_i$ acquires a temporal floor: $B_0$ must remain bounded across $\tau_{buffer}$, not merely at any moment.

## 9.3 AEF v2

The geometric ELQ constraint $\lambda_{PAE} \cdot PAE \ge \lambda_{OIE} \cdot OIE$ (AEF §3.2) is instantaneous. Its time-resolved form is satisfied across $\tau_{buffer}$:

$$
\int_0^{\tau_{buffer}} [\lambda_{PAE}(t) PAE(t) - \lambda_{OIE}(t) OIE(t)] \, dt \ge 0
$$

ELQ is therefore a runway-integrated quantity in its proper temporal form. $\lambda_{PAE}$ and $\lambda_{OIE}$ in AEF are bridge coefficients to the geometric namespace; they now carry the additional structural commitment that effective regeneration is bounded by $\lambda_{PAE} \cdot \kappa_{coord} / (1 + \Omega_{var})$, which gates how much of the nominal PAE budget reaches the manifold as $\rho_{regen}$.

## 9.4 Fallacy of Large-Scale Absorbic Effort

Exported burden is now formal: $J_{PAE}$ flowing down-gradient consuming neighbor $\tau_{buffer}$, with $\mathcal{C}(t) < 0$. The "Invalid Smoothing Operator" addendum is precisely externalization detected at $\mathcal{C}(t)$ rather than $V(t)$. The Falsifiability Condition gains a temporal axis: a centralized system that maintains $dV/dt \le 0$ by externalizing has $\mathcal{C}(t) < 0$ even when scalar $V$ appears stable, and the test is whether buffer is being preserved across the manifold or borrowed from peripheral patches.

The precursor signals are buffer-erosion indicators across specific dependency classes:
- **BMR (Basin Mass Ratio)** — proxy for the ratio of available absorptive capacity to $V^*$; shock-fragility metric
- **BRR (Basin Replenishment Ratio)** — proxy for $\rho_{regen} / \rho_{deplete}$
- **TWFS (Total Water Footprint Stress)** — fresh-water-coupled $\tau_{buffer}$ collapse
- **GDS (Grid Distribution Stress)** — entropy concentration tracking $\kappa_{coord}$ erosion
- **ESR (Ecosystem Service Resilience)** — integrated $\tau_{buffer}$ across ecological dependency classes

These were referenced in prose in the Fallacy paper without formal definition. The buffer formalism supplies the structural definitions; full operational definitions remain a corpus to-do.

## 9.5 Continuation Filter

The Filter's central claim — *amplification without proportionate distributed correction is unstable* — is buffer-language without the symbol. Amplification raises $\rho_{deplete}$; distributed correction raises $\rho_{regen}$ via high $\kappa_{coord}$ and high $\lambda_{PAE}$; "unstable" means depletion outruns regeneration sustained over civilizational $\tau_{buffer}$.

The Filter's prediction — civilizations exhibit rising corrective drift before collapse — formalizes as: $\int_{S_\Phi} \tau_{buffer} \, d\mu$ contracts faster than $\int_{S_\Phi} j_{PAE} \, d\mu$ rises. Precursor signals at sub-civilizational scale (e.g., Sahel) propagate to civilizational scale by the same cellular mechanism — every "civilizational" failure is an integrated readout of patch-level buffer collapse.

The Filter's "Cellular Requirement" (§VII) and "Parallel Stabilization vs. Interference" (§VIII) are now formally underwritten: cellular architecture maintains $\kappa_{coord}$ at cell scale, where coordination is patch-local; centralized architecture cannot manufacture $\kappa_{coord}$ because $\kappa_{coord}$ is constituted by many homomorphic local regulators in phase, and centralization removes regulators, not adds them.

---

# 10. Operational Substrate: Fresh Water as Plugin Currency

The Absorbic Unit (AEF §3.3) currently has a thermodynamic-analog definition ($1 \, AU = 1 \, J / 1 \, \Delta S_{abs}$) that is conceptually clean but operationally hard to measure across cases.

**Fresh water throughput is the candidate operational currency.** Civilization runs on fresh water. Even where water is not the *direct* substrate of a system's stability, it is the *operational* substrate: power generation, cooling, manufacturing, food, sanitation, survival. Fresh water is the natural gold standard currency for civilizational basin maintenance. It is the resource whose throughput is most directly tied to basin maintenance at every scale from household to civilization.

Fresh water available, consumed, displaced, and regenerated are directly measurable quantities. The Continuation Filter precursor signal TWFS is already water-coupled. The Sahel Worked Example is water-mediated at every step of its trajectory. The Paani Foundation Water Cup (forthcoming worked example) is water-explicit by design.

The full operationalization of AU through fresh water throughput is reserved for a dedicated addendum. Within this document, fresh water is named as the empirical anchor that makes $\rho_{regen}$, $\rho_{deplete}$, and $\tau_{buffer}$ auditable across worked examples and across the corpus.

---

# 11. Symbol Registry Updates

The following symbols enter the live ontology at the corpus root in a new namespace, **Buffer/Transport**:

| Symbol | Live? | Namespace | Defined in |
|---|---|---|---|
| $\tau_{buffer}(x, t)$ | Live | Buffer/Transport | §4 |
| $J_{PAE}(x, t)$ | Live | Buffer/Transport | §5 |
| $\mathcal{C}(t)$ | Live | Buffer/Transport | §5.3 |
| $\rho_{regen}(x, t)$ | Live | Buffer/Transport | §6 |
| $\rho_{deplete}(x, t)$ | Live | Buffer/Transport | §4.3 |
| $\kappa_{coord}(x, t)$ | Live | Buffer/Transport | §6 |
| $\Omega_{var}(x, t)$ | Live | Buffer/Transport | §6 |
| $j_{PAE}(x, t)$ | Live | Buffer/Transport (interfaces with AEF) | §3 (table) |

All quantities are patch-wise unless explicitly integrated. Integrated forms are diagnostic readouts.

Existing symbols in Δ-Self, HKL, and AEF retain their definitions. This addendum adds the temporal-axis structure rather than replacing existing geometry. The Master Symbol Registry should incorporate Buffer/Transport as a new namespace alongside Identity/Geometry, Stability/Basin, and Effort Accounting.

---

# 12. What This Addendum Does Not Do

Three explicit non-commitments:

**It does not make claims about specific operational thresholds.** Numerical values for $\lambda_{PAE}$, $\kappa_{coord}$, or $\Omega_{var}$ in any specific case must be derived from worked examples (Sahel, Paani, etc.). The structural form is supplied here; calibration is empirical.

**It does not eliminate the asymmetry it formalizes.** Naming the depletion/regeneration asymmetry does not lessen it. The asymmetry is structural to the universe and bounds any regulator. The framework's claim is that distributed cellular architectures *navigate* the asymmetry better than centralized ones — not that any architecture eliminates it.

**It does not promote any single worked example to canonical status.** Buffer is corpus-wide. The Sahel applies it. Paani will apply it. Future cases will apply it. None of these are the canonical home of buffer; the corpus root is.

---

# End of Addendum
