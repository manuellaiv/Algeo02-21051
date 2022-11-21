import numpy as np
from sympy import Matrix, Symbol

k = Symbol('k')

u = np.array([k-3, 0])
v = np.array([-8, k+1])

z = [u, v]

A = Matrix(z)
print(A.det())
