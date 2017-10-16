"""
	Author: Luis_C-137
	Using a spherical gausian distribution exmaple
	This is just for practice purposes
	This is NOT functional code
"""
from scipy.stats import multivariate_normal as mvn
import numpy as np
import matplotlib.pyplot as plt

cov = np.array([[1,0.8],[0.8,3]])
mu = np.array([0,2])

# r = mvn.rvs(mean=mu, cov=cov,size=1000)						# We can use Scipy OR
r = np.random.multivariate_normal(mean=mu, cov=cov, size=1000) 	# Use Numpy

plt.scatter(r[:,0],r[:,1])
plt.axis('equal')
plt.show()
