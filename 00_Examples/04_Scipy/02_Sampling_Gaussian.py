"""
	Author: Luis_C-137
	Sampling from a Gaussian distribution exmaple
	This is just for practice purposes
	This is NOT functional code
"""
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Std deviation of 10 and mean of 5
r = 10*np.random.randn(10000) + 5

plt.hist(r,bins = 100)
plt.show()
