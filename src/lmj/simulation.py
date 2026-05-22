"""
Top-level Simulation class that ties the whole MD engine together.

Will implement a Simulation object with roughly this interface:

    sim = Simulation(N=100, density=0.8, T=1.0, dt=0.005, seed=42)
    sim.run(n_steps=10_000, record_every=100)
    sim.plot_energy()
    sim.plot_rdf()

Internally it holds:
  - positions  (N, 2)
  - velocities (N, 2)
  - forces     (N, 2)
  - box        (L_x, L_y)
  - a trajectory list of snapshots

The run() loop calls boundary.wrap, forces.forces_numpy, and
integrator.verlet_step in sequence, collecting observables at the
requested interval.
"""
