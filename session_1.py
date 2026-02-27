# Molecular dynamics (MD) of Lennard-Jones particles in a periodic box

# MD solves classical equations of motion for a system of N particles
# m * a = F

# Interactions are encoded in a potential energy function, U(r^N)
# Time evolution is deterministic (no stochastic component)

# U(r^N) = Sum (of all pairs) [(Sum of other particles) [u(r_ij)]
# U(r) of N particles
# Sums help avoid double counting of interactions

# Forces follow from gradients of the potential:
# F_i = - Nabla_i * U(r^N) = -dU(r^N)/dx - dU(r^N)/dy - dU(r^N)/dz
# F_i is force on particle i


# Lennard-Jones (LJ) potential as a minimal interaction model:
# u_LJ(r) = 4 * epsilon [(sigma/r)^12 - (sigma/r)^6]
# epsilon: interaction strength (energy scale)
# sigma: LJ distance (distance where u = 0)

# Physical meaning:
# - r^-12 means short-range (Bohr) repulsion
# - r^-6 means van der Waals attraction

# Force from LJ potential
# F(r) = -du/dr
# For LJ, F_LJ(r) = 24 * epsilon * [2 * (sigma/r)^12 - (sigma/r)^6]*(1/r)
# Vector force between particles i and j is:
# F_ij = F(r_ij) * r^_ij
# r-> = (x, y, z)
# r^2 = x^2 + y^2 + z^2
# r = sqrt(x^2 + y^2 + z^2)

# Note: Exponential is an expensive operation


