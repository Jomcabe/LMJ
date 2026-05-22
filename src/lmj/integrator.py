"""
Time-integration schemes for the equations of motion.

Will implement:
  - euler_step(positions, velocities, forces, masses, dt)
      Simple forward Euler; not symplectic, included only for comparison.
  - verlet_step(positions, velocities, forces_fn, masses, dt)
      Velocity Verlet (Störmer–Verlet) integrator.  Symplectic: conserves a
      shadow Hamiltonian, so total energy drifts only as O(dt²) per step
      rather than diverging.  Requires two force evaluations per step but
      allows positions and velocities to be stored at the same time point.

The Verlet derivation follows from Taylor-expanding x(t+dt) and x(t−dt)
and combining to eliminate the O(dt²) error; see docs/derivations.md.
"""
