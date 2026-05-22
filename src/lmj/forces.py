"""
Vectorized force computation for all N particles.

Will implement two versions for comparison and verification:
  - forces_naive(positions, box, eps, sigma)   — explicit Python double loop, O(N²)
  - forces_numpy(positions, box, eps, sigma)   — NumPy broadcast over all pairs, O(N²)

Both return an (N, 2) array of force vectors.  The numpy version is the one
used in production; the naive loop is kept as a reference for testing.
"""
