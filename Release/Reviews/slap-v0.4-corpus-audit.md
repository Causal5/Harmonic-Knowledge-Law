# SLAP v0.4 — Corpus and Symbol-Language Audit

## Scope and evidence base

This Symbol Language Alignment Pass audits the public GitHub Release corpus at commit [`47195b664d0d56a3cf04d0185de93015e3fb9cfd`](https://github.com/Causal5/Harmonic-Knowledge-Law/commit/47195b664d0d56a3cf04d0185de93015e3fb9cfd), together with the supplied post-release working documents:

- HKL_Lyapunov_v2.md
- Absorbic_Effort_Framework_v2.md
- buffer_temporal_dimension_cross_corpus.md
- temporal-mining-freshwater-protocol-v0.1.md
- central-valley-worked-example-v0.1.md
- SLP - need complete rework

The GitHub sources inspected include the [Master Symbol Registry v0.3](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Registry/causal-ethics-master-symbol-registry.md), [Δ-Self Worldline Formalization](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Delta-Self/delta-self-worldline-formalization.md), [Sahel worked example](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Examples/sahel_worked_example.md), [AEF v1](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Papers/absorbic-effort-framework.md), [HKL v1](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/HKL/hkl-lyapunov.md), the remaining canonical papers, release indexes, SLP harness, legacy SLP DOCX, and architecture diagram.

This is a notation, typing, inheritance, and mathematical-consistency audit. It does not independently re-run the Sahel or Central Valley empirical studies.

### Representative GitHub source anchors

| Finding | Source-controlled evidence |
|---|---|
| Registry v0.3 already separates PAE/OIE concepts from measurements | [Registry rule, line 17](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Registry/causal-ethics-master-symbol-registry.md#L17) and [definitions, lines 141–156](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Registry/causal-ethics-master-symbol-registry.md#L141-L156) |
| Canonical AEF still types PAE/OIE as scalars and defines ELQ/AU | [AEF v1, lines 17–45](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Papers/absorbic-effort-framework.md#L17-L45) |
| Canonical HKL still calls \(V^*\) the least-action envelope | [HKL v1 symbol table, lines 19–23](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/HKL/hkl-lyapunov.md#L19-L23) and [interpretation, line 68](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/HKL/hkl-lyapunov.md#L68) |
| Sahel gives \(\lambda_{PAE}\) its homomorphism meaning while retaining scalar-budget PAE | [Sahel, lines 121–143](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Examples/sahel_worked_example.md#L121-L143) |
| Sahel states validation stronger than its shown calculations support | [Sahel, lines 89–97](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Examples/sahel_worked_example.md#L89-L97) |
| Fallacy paper crosses from structural analogy into unmodeled thermodynamic identity | [Fallacy paper, lines 114–133](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Papers/fallacy-of-large-scale-absorbic-effort.md#L114-L133) |
| Harness uses fixed proxy constants, text truncation, and a user-supplied curvature threshold | [Harness core, lines 26 and 100–118](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/slp_gdelta_harness/slp_gdelta_harness/core.py#L100-L118) and [canonical-layer claim](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/slp_gdelta_harness/README.md#L1-L5) |
| Release indexes refer to stale or nonexistent paths | [Manifest, lines 22–35](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/MANIFEST.md#L22-L35), [Examples status, lines 23–29](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/Examples/README.md#L23-L29), and [Architecture, lines 22–39](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/47195b664d0d56a3cf04d0185de93015e3fb9cfd/Release/ARCHITECTURE.md#L22-L39) |

## Overall verdict

Registry v0.3 and the aligned Δ-Self Worldline are the only substantially reconciled formal pair in the current GitHub release. The rest of Release is a mixed-time corpus:

- The Sahel paper introduced the field/scalar/homomorphism insight in April 2026.
- Registry v0.3 retyped PAE and OIE in July 2026.
- Canonical AEF, HKL, Four Pillars, and the Δ-Self extension retain pre-v0.3 symbols and claims.
- The supplied HKL v2 and AEF v2 drafts are newer than the canonical v1 files, but depend on a different Δ-Self formalization than the current worldline parent.
- Buffer and Temporal Mining add necessary temporal and physical-stock structure, but contain correctable sign, boundary, unit, and namespace errors.
- SLP and FRF remain downstream reconstruction material; the current harness is a prototype, not a faithful implementation of the formal corpus.

Registry v0.4 therefore cannot be a row-addition release. It must be a type-correction and parent-synthesis release.

## Authority order used for v0.4

1. The current authorial decision: PAE is the **Principle of Absorbic Effort**, and Sahel has right of way for its homomorphic realization.
2. Δ-Self Worldline Formalization for ontic state, observer model, simulation, coordinate, ledger, and trajectory distinctions.
3. Registry v0.3 for all definitions not explicitly revised by v0.4.
4. Sahel for the macro-to-micro homomorphism requirement, after correcting its type collapses.
5. Buffer and Temporal Mining for new temporal and physical-stock objects, after mathematical correction.
6. HKL/AEF v1 and v2, Four Pillars, Continuation Filter, and Fallacy papers as migration targets rather than controlling notation.
7. SLP, FRF implementation notes, the harness, archive files, and CorePrinciples as provenance or reconstruction material only.

## PAE ruling

### Canonical concept

PAE is not a scalar, field, budget, rate, or unit. It is the structural principle that corrective absorption is not causally free: predicting, preventing, absorbing, repairing, or locally reconciling OIE-related destabilizing burden requires **traceable endogenous energy expenditure by an effort-bearing agent or regulator**.

“Endogenous” is boundary-relative. For a person it may be metabolic, cognitive, and mechanical work. For FMNR it is realized through farmers' local observation, restraint, pruning, coordination, and maintenance. For a large institution it must be decomposed into the actual metabolic, mechanical, electrical, and other physically identified energy expenditures of constituent agents and machinery. Labor-hours, computation, materials, money, political will, and nominal program allocations remain in their native units unless a defensible energy conversion is supplied; none is energy merely by being called effort.

Endogenous expenditure is necessary but not sufficient. A PAE-realizing attempt must identify an effort bearer, a boundary, an OIE-related target, a physical expenditure, and a traceable corrective orientation. It may still fail to land.

### Homomorphic realization

Sahel's durable contribution is:

> Equal nominal effort does not imply equal correction. Effort lands only to the degree that the regulator's model and action structure preserve the relevant structure of the local system being regulated.

Sahel therefore has right of way in two related but nonidentical homomorphic senses. The local coefficient \(\lambda^{hom}_{PAE,i,k,\Omega}\) represents regulator-model adequacy to a target channel. The collective operator \(\mathcal H^{PAE}_{\Omega,k}\) composes local effort realizations into a macro corrective field. The second is what makes FMNR a lawful macro realization of PAE without turning the region, budget, or institution into an independent energy-bearing agent.

The canonical homomorphism coefficient should therefore be:

\[
\lambda^{\mathrm{hom}}_{PAE,i,k,\Omega}(t)\in[0,1],
\]

indexed by regulator \(i\), correction channel \(k\), system boundary \(\Omega\), and time. It measures declared model-to-target structural adequacy for the correction at issue.

Sahel's current expression

\[
\lambda_{PAE}=\Phi(G_i,S_\Phi)
\]

requires three corrections:

1. \(G_i\) is the representational substrate under v0.3; \(m_i\) is the model. Homomorphic adequacy pertains to the model encoded in \(G_i\), not to the storage substrate by itself.
2. \(\Phi_t\) is already the history-and-interaction deformation operator. A homomorphism functional cannot also be \(\Phi\).
3. No universal information-theoretic distance between \(m_i\) and ontic \(S_\Phi\) has been defined. Each empirical use must declare the compared features, structure-preserving relation, loss function, observability bridge, and calibration.

### Attempted versus landed effort

Failed but genuine corrective effort may still instantiate PAE as an attempted expenditure. It must not be counted as successful correction. The registry needs separate objects for:

- actual endogenous corrective power/energy and any separately recorded native-unit proxies;
- homomorphism/model adequacy;
- physical actuation and conversion;
- landed burden reduction; and
- OIE or other burden created by the correction itself.

This preserves the Sahel result without saying that a poorly modeled program did no work or that its financial budget was itself PAE.

### Macro-to-micro rule

A macro claim of PAE is admissible only when it supplies a decomposition into local effort-bearing agents and a composition rule showing how their corrections land across the target field. The aggregate is a diagnostic readout of the local realizations; it is not an independent macro force.

The stronger statement in the Buffer paper—“macro-as-primary is always a category error”—should be narrowed. Macro variables can be constituted by micro-interactions without being simple additive sums; network topology, phase transitions, and coordination effects are examples. What v0.4 should prohibit is an **undecomposed macro effort claim**, not all emergent macro description.

## Critical findings

### 1. The canonical release contradicts its controlling registry

Registry v0.3 says PAE is a principle and OIE a process, with separate measured quantities. Canonical AEF v1 still assigns both to \(\mathbb R_{\ge0}\), defines \(ELQ=PAE/\Delta S_{abs}\), defines an AU, and uses \(PAE=E-C_{pae}\). Canonical HKL v1 still identifies \(V^*\) with a least-action envelope and sums raw \(w_kB_k\) without the registry's normalization map. Four Pillars and the Δ-Self extension retain legacy trajectory and state notation.

This means Release currently cannot be read as one formal system despite its canonical-directory claim.

### 2. The supplied v2 papers inherit objects absent from the current parent

HKL v2 and AEF v2 cite Δ-Self sections and equations involving:

\[
\mathcal E_i,\quad
\Delta g_i,\quad
g^{(G_i)},\quad
g^{(S_\Phi)},\quad
\frac{d\mathcal E_i}{dt}
=\mathcal F_{OIE}-\mathcal F_{PAE}.
\]

Those objects and section-level claims are not defined in the current v0.3-aligned Δ-Self Worldline. The v2 drafts therefore have phantom inheritance. They cannot be promoted by repairing symbols alone.

The direct norm

\[
\|g^{(G_i)}-g^{(S_\Phi)}\|
\]

is additionally invalid unless both metrics are represented in a declared common space, chart, gauge, and norm—and unless the ontic target is observable enough to estimate the comparison. v0.4 should replace it with a declared empirical model-mismatch diagnostic, not a presumed direct ontic distance.

### 3. Sahel's insight is sounder than its current types

Sahel correctly exposes distribution and coupling, but currently makes:

- OIE both a process and a field;
- PAE both a principle and a scalar budget;
- \(G_i\) both substrate and model;
- \(\Phi\) both deformation and homomorphism functional;
- \(\lambda_{PAE}\) both model fidelity and total effort-to-correction conversion.

v0.4 should preserve Sahel by retyping its realizations:

- OIE remains the process; its realized burden-generation rate is a field.
- PAE remains the principle; committed effort has rate and accumulation symbols.
- \(\lambda^{\mathrm{hom}}_{PAE,i,k,\Omega}\) is channel- and boundary-specific homomorphism efficiency.
- A separate actuation/conversion map handles technology, access, latency, placement, and physical conversion.
- Landed correction is the output after both maps.

### 4. Buffer uses the wrong HKL boundary

The Buffer paper defines:

\[
\tau_{buffer}=\frac{V^*-V}{\dot V}
\quad\text{for }\dot V>0
\]

and says basin exit occurs as \(V\to V^*\). Under Registry v0.3, \(V^*\) is a selected viable reference profile, while \(V_{max}\) is the viability boundary. If \(V>V^*\) and burden is rising, the published numerator is negative.

The local linear estimate must instead be:

\[
\widehat\tau^{\mathrm{lin}}_{buf,\Omega}(t)
=
\frac{V_{max,\Omega}(t)-V_\Omega(t)}
{\dot V_\Omega(t)-\dot V_{max,\Omega}(t)}
\]

when the viability margin is positive and the closing rate \(\dot V_\Omega-\dot V_{max,\Omega}\) is positive. If the boundary is locally constant, this reduces to the simpler \((V_{max}-V)/\dot V\) form. The primary definition should be first-passage time to basin exit under a declared continuation scenario. It must distinguish whole-boundary exit time from the patch field obtained by applying the same definition to declared patch sub-boundaries. A spatial average is only a diagnostic and can hide a zero-runway patch. Recovery time is a different quantity and should not be represented as a signed buffer.

### 5. Buffer reverses its gradient language and conflates two fluxes

Corrective capacity sent from a high-buffer patch to a low-buffer patch moves **down** the buffer gradient, not up it. Therefore

\[
\int J_{PAE}\cdot\nabla\tau_{buf}\,d\mu
\]

is negative for the distributive case as currently described. The sign convention is reversed.

More importantly, corrective-energy transport and burden externalization are not the same flux. v0.4 should separate:

- \(\mathbf J^E_{PAE,k}\): corrective-energy flux; and
- \(\mathbf J^B_k\): destabilizing-burden flux.

A distributive alignment functional may use

\[
\mathcal C_{buf,k,\Omega}(t)
=
-\int_\Omega
\mathbf J^E_{PAE,k,\Omega}(\xi,t)\cdot\nabla_\xi\tau^\pi_{buf,\omega_\xi}(t)
\,d\mu_\Omega(\xi),
\]

so positive values mean corrective energy is deployed toward low-buffer patches. Burden export should be measured separately through the outward boundary flux of \(\mathbf J^B_k\).

### 6. Buffer's regeneration bound is not dimensionally complete

The expression

\[
\rho_{regen}
\le
\frac{\lambda_{PAE}\kappa_{coord}j_{PAE}}
{1+\Omega_{var}}
\]

does not declare compatible units. The denominator requires a dimensionless normalized variability index. Coordination “density” requires units or normalization. A local effort budget is not automatically a burden-reduction rate. A conversion/actuation map is missing.

In addition, \(\rho_{regen}\) and \(\rho_{deplete}\) collide with the later substrate-coupling ratio \(\rho=\tau_s/\tau_d\). v0.4 should reserve \(\rho_{TM}\) for the Temporal Mining ratio and rename the rate fields.

### 7. Residence time is not regeneration time

The Central Valley example uses groundwater age data as the prospective source for \(\tau_s\). Isotopic residence-time distributions constrain provenance and turnover, but they do not directly equal stock-regeneration or recovery time. v0.4 must distinguish:

- \(\tau_{age}\): residence-time statistic;
- \(\tau_s\): substrate renewal/recovery timescale;
- \(\tau_{draw}=G/W_g\): gross draw timescale; and
- \(\tau_d^{net}=(G-G_{min})/[-\dot G]_+\): net time to a declared operational floor under a local linear scenario.

The Temporal Mining ratio should be:

\[
\rho_{TM}(\xi,t)=\frac{\tau_s(\xi,t)}{\tau_d(\xi,t)},
\]

with both timescales estimated independently and uncertainty reported. Groundwater age may inform \(\tau_s\), but cannot substitute for it without a model.

### 8. Fresh water cannot be a universal Absorbic Unit

Freshwater is a critical substrate and an excellent domain metric for hydrologic, food, cooling, energy, and civilizational-dependency studies. It is not a dimensionally universal currency for corrective burden across all channels. Converting model error, habitat loss, thermal load, labor, and water into a single water unit requires explicit valuation maps and boundary choices.

Registry v0.3 was correct to reserve AU. v0.4 should keep it undefined and treat freshwater throughput as a domain anchor, not a universal unit.

### 9. Sahel currently overstates empirical validation

The Sahel document says \(dV/dt\) “measurably flipped sign,” that the framework passed a falsification test, and that \(\lambda_{PAE}\) has its first empirical anchor. The document does not define and calculate \(V\), preregister its normalization/weights, estimate \(\lambda^{hom}_{PAE,i,k,\Omega}\), or compare held-out predictions.

The case is a strong structural illustration and hypothesis generator. On the present record it is not a completed falsification test or a measurement of \(\lambda_{PAE}\). Those claims should be downgraded until an empirical protocol is executed.

### 10. The SLP harness is not a formal implementation

The current harness:

- calculates a generic Euclidean delta from hard-coded default coherence and efficiency values;
- applies an arbitrary \(k=0.1\) correction function;
- assigns elq_geo as either 1.8 or 0.4 by branch;
- routes FRF using a user-supplied curvature_score greater than 0.75, not Forman–Ricci curvature;
- truncates text to 300 characters for SIP reduction; and
- claims canonical traceability to files or equations that no longer match the current registry.

It is an interface sketch. Its README claim that it is the “canonical externalized symbolic layer” is false under the present architecture and should be removed when SLP reconstruction begins.

### 11. Physical energy does not make PAE a thermodynamic entropy identity

The Fallacy paper invokes the Second Law and then identifies PAE with corrective entropic effort, OIE with entropic fallout, and cognition with a thermodynamic threshold. No isolated-system boundary, thermodynamic state function, heat or mass balance, entropy-production term, or units are supplied. The inference does not follow from the Second Law.

v0.4 can require real endogenous energy expenditure without making this mistake. Corrective work ordinarily dissipates energy; its success is evaluated through landed burden reduction and viability. A literal entropy claim is admissible only in a domain model with a physical entropy balance. \(\Delta S_{abs}\) therefore remains thermodynamically restricted, and AU remains undefined.

## Collision and migration table

| Current use | Collision or error | v0.4 resolution |
|---|---|---|
| \(V(t)\) for HKL burden and \(V(R)\) for Ashby variety | Same symbol, unrelated type | Keep \(V_\Omega(t)\) for HKL; use \(\mathscr V(X)\) for variety |
| \(R\) for regulator and \(R(t)\) for reachability | Object collision | Use \(\mathsf{Reg}_i\) for regulator; \(\mathcal R^{ont}\) and \(\mathcal R_i\) for reachability |
| \(\Phi_t\) deformation and \(\Phi(G_i,S_\Phi)\) homomorphism score | Operator collision | Keep \(\Phi_t\); use \(\Lambda_{hom}\) as calibration functional and \(\lambda^{hom}_{PAE,i,k,\Omega}\) as score |
| \(G_i\) as substrate and as model | Type collapse | \(G_i\) stores/encodes; \(m_i\) models |
| \(S_\Phi\) as ontic conditioned structure and agent-accessible informational manifold | Ontic/epistemic collapse | Keep it ontic; accessibility remains in \(m_i,\mathcal A_{i,acc},\mathcal R_i\) |
| PAE as principle, scalar, budget, field, and flux | Type collapse | PAE stays principle; effort rate, accumulation, density, flux, and landed correction receive separate symbols |
| OIE as process, scalar, and field | Type collapse | OIE stays process; burden-generation density/rate and accumulation receive separate symbols |
| \(\lambda_{PAE}\) as homomorphism and physical conversion | Causal mechanisms collapsed | Sahel wins \(\lambda^{hom}_{PAE,i,k,\Omega}\); physical actuation becomes \(\mathcal K^{act}\) |
| \(\rho_{regen},\rho_{deplete},\rho=\tau_s/\tau_d\), and reachability \(\rho(t)\) | Multiple unrelated meanings | Reserve \(\rho_{TM}\) for timescale ratio; rename rate fields and any reachability proxy |
| \(V^*\) as target, PCB, and basin boundary | Reference/boundary collapse | Separate \(V^*\), \(V_{PCB}\), and \(V_{max}\) |
| \(\mathcal A(t)\) includes physical constraints and knowledge | Ontic/epistemic collapse | Physical \(\mathcal A(t)\); known/executable \(\mathcal A_{i,acc}(t)\) |
| \(\Psi\), \(\Phi_t\), and \(\Psi_R\) | Redundant or untyped constraint updates | Type \(\Psi_{t\to t'}\); derive reachability from dynamics and constraints |
| \(S_{abs}\) for cellular absorption | Collides with state space and entropy notation | Use landed or accumulated correction symbols |
| \(CIR\) in the universal HKL registry | Water-domain metric presented as universal | Move to application/domain annex |
| \(\nabla S\) as entropy baseline | Field and metric undeclared | Remove or define a physical entropy field and metric in the relevant domain |
| \(\Delta I,\Delta\gamma,\gamma_{act},\gamma_{pcb},s(t),c(t)\) | Legacy Δ-Self notation | Use v0.3 worldline forms |
| \(\Delta S_{abs}\), AU, raw ELQ | Dimensional overreach | Keep restricted or deprecated |

## Per-document disposition

| Document | Status after SLAP | Required action |
|---|---|---|
| Registry v0.3 | Predecessor; structurally strong | Promote into v0.4 with new namespaces and collision log |
| Δ-Self Worldline | Formal parent | Preserve; add reachability and v0.4 inheritance patch |
| Δ-Self Extension | Rewrite required | Replace legacy symbols; separate actual from estimated reachability; remove PCB expectation formula |
| Δ-Self Concept / Δ-Self 2 | Conceptual sources | Replace \(\Delta I\); remove duplicate-file ambiguity; inherit worldline terms |
| HKL v1 | Obsolete under v0.3 | Rewrite around normalization, \(V^*\), \(V_{PCB}\), \(V_{max}\), fields, boundaries, and export terms |
| Supplied HKL v2 | Do not promote | Remove phantom Δ-Self inheritance and direct ontic metric subtraction |
| AEF v1 | Obsolete under v0.3 | Replace scalar PAE/OIE, raw ELQ, AU, and \(\Delta S_{abs}\) usage |
| Supplied AEF v2 | Do not promote wholesale | Rebuild with PAE principle, homomorphic landing, actuation map, and measured fields/rates |
| Sahel | Theoretically load-bearing example | Retype PAE/OIE; preserve \(\lambda^{hom}_{PAE,i,k,\Omega}\); rename Ashby variety; downgrade unperformed empirical claims |
| Four Pillars | Conceptually compatible | Migrate trajectory notation; split physical and epistemic actions; remove undeclared \(\nabla S\) |
| Fallacy paper | Major revision | Normalize \(V\); define or remove BMR/BRR/TWFS/GDS/ESR; distinguish local burden reduction from export; remove unmodeled thermodynamic identities |
| Continuation Filter | Formalization candidate | Add amplification, coupling, timescale, buffer, and reachability objects after v0.4 settles them |
| Buffer as Temporal Dimension | Important but mathematically unready | Correct \(V_{max}\), first-passage buffer, flux signs/types, units, \(\rho\) collision, and macro claim |
| Temporal Mining protocol | Strong application protocol | Keep physical-first rule; move symbols to a domain annex; add timescale distinctions |
| Central Valley example | Application work in progress | Preserve stock-flow inference; separate age/renewal/draw/net depletion; avoid calling 2043 a computed buffer |
| SLP/FRF PDF and DOCX | Reconstruction material | Preserve FRF purpose; do not let legacy geometry control v0.4 |
| SLP GΔ harness | Prototype | Reclassify; remove canonical claim; rebuild only after SLP boundary contracts exist |

## Repository-control defects

- Release/MANIFEST.md still points to legacy top-level paths moved to Release/archive/.
- The manifest lists Examples/sahel-worked-example.md, while the actual canonical file is Examples/sahel_worked_example.md.
- Examples/README.md says the Sahel slot is pending although the document exists.
- ARCHITECTURE.md says active material remains at top level, which is no longer true after archive migration.
- Several category READMEs link to removed top-level legacy files rather than the archive.
- The legacy SLP DOCX is presented as a release asset without a status marker stating that its claims are historical and under reconstruction.

These are not symbol errors, but they undermine source authority and should be fixed in the same release cycle as v0.4.

## Recommended migration sequence

1. Ratify Registry v0.4's PAE, OIE, homomorphism, reachability, burden, buffer, and Temporal Mining types.
2. Patch Δ-Self Worldline and fully rewrite Δ-Self Extension under those types.
3. Rewrite AEF and HKL together; neither should be promoted independently.
4. Migrate Sahel, Four Pillars, Fallacy, and Continuation Filter.
5. Create a Temporal Mining domain annex and migrate the freshwater protocol and Central Valley symbols into it.
6. Correct Release indexes, paths, and status labels.
7. Specify FRF boundary semantics and only then respecify SLP.
8. Replace or retire the current harness after the SLP contracts exist.

## Material not fully auditable in this pass

The later Sahel logistic-map/addendum notation referenced in prior project work was not present in the audited GitHub Release tree or supplied local source bytes. Its \(g_{CE}\), recurrence, logistic, and reachability-proxy symbols should not be registered from memory. They require a separate source-controlled pass before v0.4 is declared final.

The Law of WE PDF remains explicitly unreconciled and should not supply new v0.4 symbols until its metric, Lagrangian, gradient, and physics-analogy claims receive their own audit.

## Confidence

- Overall corpus/type audit: **98%**
- PAE principle versus effort-realization separation: **99%**
- Sahel right of way for \(\lambda^{\mathrm{hom}}_{PAE,i,k,\Omega}\): **98%**
- Need to separate homomorphism from physical actuation: **97%**
- Buffer boundary/sign corrections: **99%**
- Residence time versus renewal time correction: **97%**
- Exact final notation choices in the accompanying v0.4 draft: **91%**, because authorial ratification and the missing logistic addendum may still change names without changing the type structure
