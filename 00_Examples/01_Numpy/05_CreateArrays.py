"""
	Author: Luis_C-137
	Use this file as a template
	This is just for practice purposes
	This is NOT functional code
"""

import numpy as np

np.array([1,2,3,4])

z = np.zeros(10) # This creates an array of ten ceros

ones = np.ones((10,10))	# This creates a matrix of ones
		# NOTE: It uses double parentesis

R = np.random.random((10,10))	# Generates ten by ten matrix
								#		of random numbers
# NOTE: This particular functions give us an even distribution 
#		of values between cero and one

# For a Gaussian distribution use:
Gauss = np.random.randn(10,10)
# NOTE: This does not need the double '()'

# We also have stadistic functions
print(Gauss.mean())
print(Gauss.var())

