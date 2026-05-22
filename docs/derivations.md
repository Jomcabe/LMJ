# LMJ Derivations and Notes

Working notes for the physics and mathematics behind each component.
Equations use reduced Lennard-Jones units throughout: ε = σ = m = k_B = 1.

---

## Lennard-Jones potential and forces

_To be filled in._

Key results to derive:
- U(r) = 4ε[(σ/r)¹² − (σ/r)⁶]
- F(r) = −dU/dr expressed in Cartesian components
- Cutoff and shift: U_shifted(r) = U(r) − U(r_cut)

---

## Lagrangian and equations of motion

_To be filled in._

Key results to derive:
- L = T − U = ½ Σ mᵢ |ṙᵢ|² − U({rᵢ})
- Euler-Lagrange equations → Newton's second law mᵢr̈ᵢ = Fᵢ
- Why the Lagrangian formulation is equivalent to Newton for conservative forces

---

## Velocity Verlet derivation

_To be filled in._

Key results to derive:
- Taylor expansion of x(t + dt) and x(t − dt)
- Adding and subtracting to get the Verlet position update
- Velocity Verlet form that gives v at the same time as x
- Why Verlet is symplectic (area-preserving in phase space) and what that implies for energy conservation

---

## Virial theorem and pressure

_To be filled in._

Key results to derive:
- Time-averaged virial: ⟨PV⟩ = Nk_BT + ½ ⟨Σᵢⱼ rᵢⱼ · Fᵢⱼ⟩
- Instantaneous pressure estimator for an MD trajectory
- Equation of state for the LJ fluid (comparison to ideal gas)

---

## Hessian and normal modes

_To be filled in._

Key results to derive:
- Hessian H_αβ = ∂²U / ∂x_α ∂x_β evaluated analytically from the LJ pair potential
- Mass-weighted dynamical matrix D = M^{-1/2} H M^{-1/2}
- Eigenvalue problem D e_k = ω_k² e_k
- Physical meaning of eigenvectors (collective displacements) and eigenvalues (squared frequencies)
- Two zero modes (Goldstone modes) from translational invariance
- Phonon density of states g(ω) and its relation to heat capacity
