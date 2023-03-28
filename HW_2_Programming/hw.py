import numpy as np
from numpy import array
from numpy.linalg import norm


X = np.array([[20, 8, -4, 4],[-5, 2, 3, -4]])
C = np.cov(X, rowvar=False)

print("X =", X, "\n\n","C =", C)
