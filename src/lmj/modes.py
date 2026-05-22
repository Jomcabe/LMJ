"""
Normal-mode analysis via Hessian diagonalization.

Will implement:
  - normal_modes(hessian, masses)
      Build the mass-weighted dynamical matrix D = M^{-1/2} H M^{-1/2},
      diagonalize with numpy.linalg.eigh (real symmetric), return:
        - frequencies  (2N,)  in units of sqrt(ε/m)/σ
        - mode_vectors (2N, 2N)  columns are the orthonormal eigenvectors
      Two zero-frequency modes correspond to global translations (Goldstone
      modes); they are identified and flagged rather than discarded silently.
  - density_of_states(frequencies, n_bins)
      Histogram the squared frequencies to produce a phonon DOS g(ω).

Eigendecomposition of the 2N×2N Hessian for N~100 is fast (milliseconds);
for N~500 scipy.linalg.eigh with the 'evr' driver is preferred.
"""
