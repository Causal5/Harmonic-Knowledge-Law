# Δ-Self Extension: Reachability & Constraint Evolution (Normalized)

---

# Symbol Glossary (Section-Specific)

| Symbol | Meaning | Type / Domain | Notes |
|------|--------|--------------|------|
| S | State space | Set | All possible system states |
| s(t) | Realized state at time t | Element of S | Actual system configuration |
| T | Time index set | Ordered set | Typically R or Z |
| c(t) | Realized coordinate | S × T | c(t) = (s(t), t) |
| γ(t) | Realized trajectory | Function T → S × T | Worldline of system |
| γ_pcb(t) | Passive Cost Baseline trajectory | Function T → S × T | Default non-recursive continuation |
| A(t) | Feasible action set | Set of transitions | Actions available under constraints and knowledge |
| R(t) | Reachable future set | Set of trajectories | All trajectories accessible from c(t) |
| Ψ | Constraint evolution operator | Mapping | Updates future possibility structure |
| S_Φ(t) | Accessible constraint structure | Subset of S | State space as deformed by history |
| Δγ(t) | Trajectory deviation | Scalar or functional | Difference from baseline trajectory |
| d_S(·,·) | State distance metric | Function S × S → R≥0 | Measures difference between states |
| κ_Δ(t) | Deviation curvature | Scalar R≥0 | Measures bending away from PCB |
| Ψ_R | Reachability update operator | Mapping | Updates reachable set specifically |

---

# 1. Realized Coordinate and Trajectory

A system evolves through coordinates:

c(t) := (s(t), t)

Trajectory:

γ(t) = c(t)

---

# 2. Reachable Future Set

Define the reachable future set:

R(t) := { γ_α(τ) | τ ≥ t, α ∈ A(t) }

---

# 3. Passive Cost Baseline (Refined)

γ_pcb(t) := E[γ_α(t)] for α ∈ A(t) under non-recursive selection

---

# 4. Trajectory Deviation

Δγ(t) := d_S(s(t), s_pcb(t))

---

# 5. Curvature of Deviation

κ_Δ(t) := || s¨(t) - s¨_pcb(t) ||

---

# 6. Constraint Evolution

S_Φ(t+Δt) = Ψ(S_Φ(t), γ([t, t+Δt]))

---

# 7. Reachability Update

R(t+Δt) = Ψ_R(R(t), γ([t, t+Δt]))

---

# 8. Trajectory-Deformed Reachability Theorem

s1(t) = s2(t) does NOT imply R1(t) = R2(t)

---

# 9. Δ-Self (Refined Definition)

Δγ(t) > 0 AND recursive modeling + persistence

---

# 10. Distinction

Non-cognitive: no recursive modeling  
Δ-Self: recursive + persistent + topology affecting

---

# Summary

Δ-Self is recursively selected deviation within a history-modified constraint topology.
