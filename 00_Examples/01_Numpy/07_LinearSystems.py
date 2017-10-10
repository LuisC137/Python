"""
	Author: Luis_C-137
	Solving Linear systems
	This is just for practice purposes
	This is NOT functional code
"""

import numpy as np

A = np.array([[1,2],[3,4]])
b = np.array([1,2])

print('Solving fo x')
x = np.linalg.solve(A,b)
print(x)

