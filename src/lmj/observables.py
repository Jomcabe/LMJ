"""
Thermodynamic and structural observables.

Will implement:
  - kinetic_energy(velocities, masses) -> float
  - temperature(velocities, masses) -> float
      Via the equipartition theorem: <KE> = (N_dof / 2) k_B T.
  - potential_energy(positions, box, eps, sigma) -> float
  - total_energy(positions, velocities, box, masses, eps, sigma) -> float
  - pressure_virial(positions, forces, box, T) -> float
      Pressure from the virial theorem: P V = N k_B T + (1/2) Σ r_ij · F_ij.
  - radial_distribution(positions, box, n_bins, r_max) -> (r, g_r)
      Pair correlation function g(r); the Fourier transform gives the
      static structure factor S(q).
"""
