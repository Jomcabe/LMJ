"""
Lennard-Jones pair potential and its gradient.

Will implement:
  - lj_potential(r, eps, sigma) -> U(r) for a single pair distance r
  - lj_gradient(r, eps, sigma)  -> dU/dr  (scalar, before chain-ruling to Cartesian)

The potential is U(r) = 4ε[(σ/r)^12 − (σ/r)^6].
The gradient (force magnitude) is F(r) = −dU/dr.
A cutoff radius r_cut (typically 2.5σ) will be applied with an optional
shift so U(r_cut) = 0 exactly.
"""
