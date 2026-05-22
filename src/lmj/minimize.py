"""
Energy minimization to find local potential-energy minima.

Will implement:
  - gradient_descent(positions, box, eps, sigma, step, tol)
      Simple steepest-descent minimizer; easy to implement, slow to converge
      near the minimum.  Useful for debugging the force calculation.
  - minimize_scipy(positions, box, eps, sigma)
      Wraps scipy.optimize.minimize (L-BFGS-B or CG) for production use.
      Returns the minimized positions and the final energy.

Minimized configurations are required before computing the Hessian, because
the Hessian at a non-minimum mixes real curvature with residual forces.
"""
