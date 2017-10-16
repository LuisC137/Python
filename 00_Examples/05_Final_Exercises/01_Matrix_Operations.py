"""
	Author: Luis_C-137
	Given A and v multiply them the get a v', 
	then use this v' to multiply it by A.
	Do this 15 times or more, v should be equal to v' 
	This is just for practice purposes
	This is NOT functional code
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0.3,0.6,0.1],[0.5,0.2,0.3],[0.4,0.1,0.5]])
v = np.array([1/3,1/3,1/3])
v_control = np.array([1/3,1/3,1/3])

for x in range(1,30):
	v = v*A
	plt.plot(np.abs(v - v_control))
	plt.show()

print(v)