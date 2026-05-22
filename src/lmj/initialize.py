"""
System initialization: particle positions and velocities.

Will implement:
  - triangular_lattice(N, density)
      Place N particles on a 2D triangular (hexagonal close-packed) lattice
      at the given number density ρ = N/V.  Returns positions (N, 2) and
      box dimensions (L_x, L_y).
  - maxwell_boltzmann(N, T, mass, rng)
      Draw velocities from the Maxwell-Boltzmann distribution at temperature T:
      each component is i.i.d. Gaussian with σ² = k_B T / m.
      Removes center-of-mass drift by subtracting the mean velocity.

Units throughout: reduced LJ units where ε = σ = m = k_B = 1.
"""
