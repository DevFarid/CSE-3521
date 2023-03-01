import argparse
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define numpy arrays
A = np.random.rand(3, 5)

# Return a new array of given shape and type, filled with zeros.
B = np.zeros((3, 1))\


C = np.ones((1, 3))

# return evenly spaced numbers over a specified interval.
D = np.linspace(0, 5, num=6)

# Print
print(A, end="\n\n")
print(B, end="\n\n")
print(C, end="\n\n")
print(D, end="\n\n")

# Print shapes
print(A.shape, end="\n\n")
print(B.shape, end="\n\n")
print(C.shape, end="\n\n")
print(D.shape, end="\n\n")

print(A.ndim, end="\n\n")
print(B.ndim, end="\n\n")
print(C.ndim, end="\n\n")
print(D.ndim, end="\n\n")

# Reshape
print(D.reshape(6, 1), end="\n\n") # 6-by-1 matrix (column vector)
print(D.reshape(6, 1).shape, end="\n\n")
print(D.reshape(6, 1).ndim, end="\n\n")

print(D.reshape(1, 6), end="\n\n") # 1-by-6 matrix (row vector)
print(D.reshape(1, 6).shape, end="\n\n")
print(D.reshape(1, 6).ndim, end="\n\n")

print(D.reshape(-1, 1), end="\n\n")
print(D.reshape(-1, 1).shape, end="\n\n")
print(D.reshape(-1, 1).ndim, end="\n\n")


# Extract element (note that, numpy index starts from 0)
print(A, end="\n\n")
print(A[1,1], end="\n\n")
print(A[:, 1], end="\n\n")
print(A[1, :], end="\n\n")
print(A[1, -1], end="\n\n")
print(A[1, 0:3], end="\n\n")

# matrix transpose
print(A, end="\n\n")
print(A.transpose(), end="\n\n")

# real values
print(-4)
print((-4)**0.5)
print(np.real(-4**0.5))

# matrix multiplication
print(np.matmul(A.transpose(), A), end="\n\n")
print(np.matmul(A, A.transpose()), end="\n\n")
print(np.matmul(B, C), end="\n\n")
print(np.matmul(C, B), end="\n\n")

# matrix inversion
print(np.linalg.inv(np.matmul(A, A.transpose())), end="\n\n")

# eigendecomposition
Sigma = np.matmul(A, A.transpose())
V, W = np.linalg.eig(Sigma)
print(V, end="\n\n")
print(np.argsort(V), end="\n\n")
print(np.argsort(V)[::-1], end="\n\n")
print(V[np.argsort(V)], end="\n\n")