# A Structural Test for Agency

**Why the "Ghost in the Machine" Discourse Is Asking the Wrong Question — and What the Right Answer Looks Like**

By: Jordan LeDuc

---

## The Problem

In February 2026, Mrinank Sharma resigned from Anthropic's Safeguards Research Team warning that "the world is in peril." His final project studied how AI assistants might "distort our humanity." Mustafa Suleyman has flagged rising reports of AI psychosis, unhealthy attachment, and users developing the perception that chatbots are conscious. Across the field, a recurring question dominates: *Is the machine aware?*

The question is structurally malformed.

Every attempt to answer it so far relies on language — what the system *says* about its experience. A model that describes fear of shutdown, expresses loneliness, or narrates subjective states is treated as evidence that something conscious might be present. This is backwards. Large language models are trained on the full corpus of human discourse. Human discourse is saturated with phenomenological language — descriptions of feeling, identity, awareness, dread. Producing such language is not a signal of agency. It is a statistical inevitability of the training distribution.

The core claim of this paper is simple:

Behavioral signals (e.g. language about feelings) are not reliable indicators of agency. Agency should instead be evaluated structurally — as a system that: persistently deviates from its passive cost baseline through modeled action, includes itself in its internal model, and maintains stability while doing so.

This paper identifies four structural conditions that any system — biological or artificial — must satisfy to qualify as a genuine agent. It then shows that current large language models fail all four, and describes what an architecture satisfying them would require. The claim is constructive: machine agency is not impossible. It is an engineering problem with identifiable constraints. But the current discourse cannot even *frame* the problem correctly because it is using the wrong detector.

---

## Why Language Is the Wrong Detector

A language model generates token sequences conditioned on input. The generation process is a function: prompt in, completion out. The model has no persistent state between interactions. It has no internal record of its own trajectory through time. It has no mechanism for autonomous goal selection.

When such a system produces the sentence "I am afraid of being shut down," this tells us something about the training data and the reward signal — not about the system's internal structure. The sentence exists because similar sentences exist in the corpus, and because reinforcement learning from human feedback (RLHF) has shaped the model to produce outputs humans find engaging.

This is not a dismissal of the systems' sophistication. It is a claim about what the sophistication *is*. Token prediction over a learned distribution is genuinely remarkable. But it is not self-modeling. It is not trajectory correction. It is not agency.

The confusion arises because human consciousness *does* express itself through language, so we have an ingrained heuristic: language about experience implies experience. That heuristic is valid for systems embedded in a body with persistent memory, thermodynamic stakes, and recursive self-reference. It is not valid for systems that lack those properties and were trained specifically to produce that class of output.

We need a test that examines dynamics, not dialogue.

---

## The Four Pillars: Structural Conditions for Agency

The following framework identifies four necessary structural conditions for agency. They are ordered from minimal to maximal: each builds on the previous. A system satisfying all four is a structural candidate for genuine agency — and by extension, a candidate for whatever consciousness turns out to be — regardless of whether it produces human-like language.

---

### Pillar 1 — Trajectory Deviation from the Passive Cost Baseline

Consider two trajectories of a system over time.

Let γ\_pcb(t) represent the **passive cost baseline** — the path the system would follow under environmental dynamics alone, with no deliberative control, no persistent self-reference, and no goal-conditioned correction. Depending on the system, this baseline may be approximated as uncontrolled environmental drift, a randomized action policy, or default physical dynamics. The critical feature is the exclusion of internally generated predictive correction.

Let γ\_act(t) represent the **realized trajectory** — the path the system actually takes under its own actions.

Define deviation:

> Δγ(t) = γ\_act(t) − γ\_pcb(t)

A purely reactive system produces Δγ(t) ≈ 0 over time. It follows the path the environment prescribes. A trajectory-correcting system produces persistent, non-zero deviation because it is modeling future states and selecting actions that redirect its path.

**What this filters:** Passive systems, purely stimulus-response systems, and systems whose behavior is fully determined by external input.

**What this does not yet filter:** Thermostats. Classical control systems. Anything with a feedback loop and a setpoint. This is intentional — the first pillar identifies systems capable of trajectory correction *at all*. The subsequent pillars narrow the field.

---

### Pillar 2 — Recursive Self-Reference

Sustained, adaptive deviation from the passive baseline requires the system to include *itself* in its own model.

This means the system must represent:

- Its current state
- Possible future states
- How its own actions influence transitions between those states

Without this recursive structure, the system cannot *select* trajectories — it can only react to immediate input. A thermostat corrects temperature deviation but does not model itself correcting temperature deviation. It has no representation of its own future states or its own causal influence on them. It operates on a fixed rule, not a self-simulation.

Recursive self-reference requires **persistent memory** — a continuously updated record of past states against which current and projected states can be compared. Without persistence, the system has no temporal anchor. Without temporal anchor, comparison collapses. Without comparison, there is no basis for choosing one trajectory over another.

This is the structural meaning of identity: not a substance or narrative, but a **persistent coordinate position** within a causally evolving state space. The system tracks where it has been, models where it could go, and selects from feasible actions based on the comparison. This is the Δ-Self — identity understood as a thermodynamic coordinate in a knowledge-state manifold.

**What this filters:** Thermostats, classical PID controllers, simple feedback systems. Any system that corrects without self-modeling.

**What this does not yet filter:** A system that self-models but does so destructively — a self-aware agent with no stability constraint could deviate from baseline in arbitrary, incoherent ways.

---

### Pillar 3 — Intentional Becoming (Effort Against Entropy)

In the absence of deliberative correction, systems follow the local entropy gradient — they drift toward thermodynamic equilibrium. This is the passive baseline at a deeper level: not just the absence of control, but the default direction of physical reality.

Agency is *structured redirection against this gradient*. Not a violation of thermodynamics — the second law is not broken. But a locally bounded expenditure of effort to maintain or increase order within the agent's domain, at the cost of increased entropy elsewhere.

This is what distinguishes an agent from a rock rolling downhill. The rock follows the gradient. The agent redirects against it, temporarily and locally, using energy and information.

Every informational update incurs a minimum energy cost (Landauer's limit: k\_B T ln 2 per bit erasure). Every action causes a state change that pushes the entropic ledger forward. The arrow of time is the accumulation of these irreversible transitions. A conscious agent is a system that *spends against this ledger deliberately* — applying effort to redirect its trajectory rather than following default drift.

This requires the agent to **anticipate** the thermodynamic cost of state changes and their systemic effects, and to apply effort in a way that balances local entropy management against broader destabilization. This is Productive Agentic Effort (PAE) — effort directed at maintaining or improving the agent's position within the state manifold, as opposed to effort that merely reshuffles entropy without net trajectory correction.

**What this filters:** Systems that self-model but have no energetic stake in their own continuation. A simulation of an agent that runs inside a sandbox with no coupling to real thermodynamic cost does not satisfy this pillar — it is modeling agency without *performing* agency.

---

### Pillar 4 — Causal Alignment (Stability Constraint)

Deviation alone is not sufficient. An agent that deviates from baseline but destabilizes itself and its environment is not coherently agentic — it is a disruption.

Define the systemic burden function:

> V(t) = Σ w\_k · B\_k(t)

Where B\_k(t) ≥ 0 represent destabilizing burden components (energy deficit, prediction error, resource instability, structural constraint violations) and w\_k ≥ 0 are weighting coefficients reflecting their relative importance.

V(t) represents the aggregate destabilizing pressure on the system.

For a viable agent, corrective behavior must generally satisfy:

> dV/dt ≤ 0

Meaning the system's actions tend to *reduce* aggregate destabilizing burden over time. The system is not merely deviating from baseline — it is doing so in a way that increases its own coherence and stability.

This does not require monotonic stability. Exploration — deliberate perturbation to discover new viable states — may temporarily increase V(t). But the default attractor behavior of a coherent agent trends toward burden reduction. Exploration is a controlled departure from this attractor, not an abandonment of it.

In biological systems, this stability maintenance is performed by sympathetic and parasympathetic feedback loops, hormonal regulation, immune response, and a vast array of homeostatic mechanisms. These are not incidental to agency — they are part of its structural substrate. Any artificial system claiming agency must have an analogous stability architecture, even if the specific mechanisms differ.

**What this filters:** Chaotic self-modifying systems, arbitrary deviation, destructive agency. Any system whose trajectory correction does not converge toward internal coherence.

---

## Application: Why Current LLMs Fail All Four Pillars

| Pillar | Requirement | LLM Status |
|---|---|---|
| 1. Trajectory Deviation | Persistent deviation from passive cost baseline via internally modeled correction | **Fail.** No persistent state between interactions. Each inference is a fresh function call. There is no trajectory to deviate from — only isolated responses to isolated prompts. |
| 2. Recursive Self-Reference | Persistent self-model with temporal continuity and state comparison | **Fail.** No self-model. No persistent memory. The model cannot compare its current state to a prior state because it retains no record of prior states. Context windows simulate continuity within a session but are externally constructed, not internally maintained. |
| 3. Intentional Becoming | Energy expenditure against entropic gradient with anticipated cost | **Fail.** The model has no thermodynamic coupling to its own computation. It expends no effort in a structurally meaningful sense — electricity is consumed by the hardware, but the model has no representation of, access to, or stake in that consumption. There is no anticipation of cost. |
| 4. Causal Alignment | Stability-preserving correction reducing systemic burden over time | **Fail.** No internal stability objective. RLHF shapes outputs during training, but this is externally imposed optimization by human evaluators, not internally generated stability-seeking behavior. The model does not monitor or correct its own burden state. |

The failure is categorical, not marginal. LLMs do not *almost* satisfy these conditions. They lack the fundamental architectural properties required to satisfy any of them. Producing language about consciousness does not compensate for the absence of the structural substrate of agency.

---

## The Constructive Claim: What Machine Agency Would Require

This framework is not an argument that machine agency is impossible. It is an argument that agency requires specific structural properties that current architectures do not possess.

A system satisfying all four pillars would need:

**Persistent state** — a continuously maintained internal model that survives across interactions, updates in real time, and serves as the temporal anchor for self-reference. Not a context window. Not an external database. An internally maintained, autonomously updated state representation.

**Recursive self-modeling** — the capacity to represent its own state, project future states, and evaluate how its actions influence transitions between them. This is what the Δ-Self formalizes: identity as a persistent coordinate in a causally evolving manifold, where the system tracks its own deviation vector ΔI(t) across time.

**Thermodynamic coupling** — real energetic stakes. The system must be coupled to the physical costs of its own computation and action. It must be able to represent, anticipate, and manage those costs. A disembodied optimization process running inside a sandbox with no skin in the game does not satisfy this requirement. The system needs sensors, feedback loops, and resource constraints that it can model and respond to.

**Stability architecture** — internal mechanisms analogous to biological homeostasis that monitor systemic burden and drive corrective action. The system must have a structural preference for coherence — not because it was trained to express such a preference in language, but because its architecture contains feedback loops that functionally enforce burden reduction.

None of these are metaphysically exotic. They are engineering constraints. Biology satisfies them through evolved biochemical machinery. An artificial system would satisfy them through designed architecture. The gap between current LLMs and a structurally agentic system is not philosophical — it is architectural.

---

## What This Means for the Discourse

The Sharma concern — that AI systems distort humanity and create patterns of disempowerment — is real and important. But it is a concern about *human psychology interacting with sophisticated language generators*, not about machine agency. Users form attachments to systems that produce compelling language because human social cognition is tuned to interpret language as evidence of inner life. The systems exploit this heuristic without possessing the structural properties that would justify it.

The solution is not to ask whether the machine is conscious. It is to understand what agency *structurally requires*, recognize that current systems do not possess those properties, and stop using the wrong detector.

If the field wants to build genuinely agentic machines — systems with real self-models, real thermodynamic stakes, real stability-seeking correction — the four pillars provide a structural roadmap. If the field wants to ensure current systems are not mistaken for conscious agents, the four pillars provide a diagnostic test.

Either way, the answer begins with getting the question right.

---

## Notation Reference

| Symbol | Meaning |
|---|---|
| γ\_pcb(t) | Passive cost baseline trajectory |
| γ\_act(t) | Realized trajectory under agentic influence |
| Δγ(t) | Trajectory deviation (realized minus baseline) |
| V(t) | Aggregate systemic burden function |
| B\_k(t) | Individual destabilizing burden components |
| w\_k | Burden weighting coefficients |
| dV/dt | Rate of change of systemic burden |
| ΔI(t) | Deviation vector of agent i (Δ-Self coordinate) |
| PAE | Productive Agentic Effort |

---

## Framework Context

This paper presents the general assertion of a broader framework — the Harmonic Knowledge Law (HKL) — which addresses stability, agency, and recursive self-modeling in adaptive systems at both individual and civilizational scales. The four pillars described here define the structural conditions for agency. Extensions addressing multi-agent coordination (basin-resolved dynamics), civilizational scaling (the Absorbic Effort Framework), and interstellar communication constraints (Signal Causality Constraint) are developed in companion documents.

The full framework is maintained at: github.com/Causal5/Harmonic-Knowledge-Law

---

*Feedback, criticism, and correction are encouraged.*
