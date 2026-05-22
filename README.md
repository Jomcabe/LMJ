# LMJ — Lennard-Jones Molecular Dynamics

A 2D molecular dynamics simulator built from scratch as a two-week learning project. The simulator
models ~50–500 particles in a periodic 2D box interacting via the Lennard-Jones potential
U(r) = 4ε[(σ/r)¹² − (σ/r)⁶]. The equations of motion come from the Lagrangian L = T − U and are
integrated with the velocity Verlet algorithm, a symplectic integrator that conserves a shadow
Hamiltonian and prevents energy drift over long runs. Periodic boundary conditions (minimum-image
convention) make the small system behave like bulk material. The eventual payoff is computing the
Hessian of the potential at a crystalline energy minimum and diagonalizing it — the eigenvectors are
normal modes (phonon-like collective vibrations), and the eigenvalue distribution yields a phonon
density of states for a 2D solid.

## Project goals

- Practice deriving and implementing **Lagrangian mechanics** directly in code
- Build **linear algebra intuition** through Hessian construction and eigendecomposition (normal mode analysis)
- Learn **numerical methods**: velocity Verlet symplectic integration, gradient descent / conjugate gradient minimization
- Produce **real physical results**: energy conservation curves, phase behavior (solid/liquid/gas), radial distribution functions, and a phonon density of states for a 2D triangular lattice

## Planned milestones

### Week 1 — Working MD engine
- Lennard-Jones potential and forces (naive loop, then NumPy-broadcast)
- Velocity Verlet integrator
- Periodic boundary conditions and minimum-image convention
- Lattice initialization and Maxwell-Boltzmann velocity sampling
- Energy conservation check (should hold to < 0.1 % drift over 10⁴ steps)
- Radial distribution function g(r)

### Week 2 — Thermodynamics and normal modes
- Temperature and pressure (virial theorem)
- Phase exploration at varying ρ and T (solid, liquid, gas)
- Gradient descent / conjugate gradient energy minimization
- Hessian construction at the minimum (2N × 2N matrix)
- Hessian diagonalization → normal-mode frequencies and shapes
- Phonon density of states plot

## Stack

- **Python 3.11+**
- **NumPy** — array math and broadcasting
- **SciPy** — sparse linear algebra, eigensolvers, minimization routines
- **Matplotlib** — plotting and animation
- **pytest** — unit and integration tests
- **Jupyter** — interactive notebooks for exploration and figures

## Results

_To be filled in as milestones are completed._
