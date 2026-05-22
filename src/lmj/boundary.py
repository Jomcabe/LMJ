"""
Periodic boundary conditions (PBC) and the minimum-image convention.

Will implement:
  - wrap(positions, box)
      Folds all particle positions back into the primary cell [0, L_x) × [0, L_y).
  - minimum_image(delta, box)
      Given a raw displacement vector delta = r_i − r_j, return the shortest
      equivalent vector under PBC.  For a cubic/rectangular box this is simply
      delta − box * round(delta / box).

The minimum-image convention ensures that each pair interacts through the
nearest periodic image, making the small simulation box behave like an
infinite bulk system (up to finite-size corrections).
"""
