"""
Hessian (dynamical matrix) of the potential energy at a local minimum.

Will implement:
  - hessian_numerical(positions, box, eps, sigma, h)
      Finite-difference Hessian: H_ij = (U(x+h*e_j) − 2U(x) + U(x−h*e_j)) / h²
      evaluated for every pair of Cartesian degrees of freedom.
      Returns a (2N, 2N) symmetric NumPy array.
  - hessian_analytical(positions, box, eps, sigma)
      Analytic second derivatives of the LJ pair potential.
      More accurate and faster; used for production.

The Hessian must be evaluated at a minimum (all forces ≈ 0); otherwise
imaginary frequencies (negative eigenvalues) indicate a saddle point, not
a stable crystal.
"""
