"""
	Author: Luis_C-137
	Using a spherical gausian distribution exmaple
	This is just for practice purposes
	This is NOT functional code
"""
from scipy.stats import norm
import matplotlib.pyplot as plt


r = np.random.randn(10000,2)
r[:,1] = 5*r[:,1] + 2	# Change the deviation of the 
						# second dimention to five and the 
						# mean to two
plt.scatter(r[:,0],r[:,1])
plt.axis('equal')	# To make the axis the same size
plt.show()
