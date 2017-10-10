"""
	Author: Luis_C-137
	Explore matrixes
	This is just for practice purposes
	This is NOT functional code
"""

import numpy as np 

M = np.array([ [1,2], [2,1]])
L = [ [1,2], [3,4] ]

row = L[0]		# This calls the firts row
				#		of the Matrix

element = L[0][0]	# This  calls the first element
					#		of the matrix

# We can do the same with the numpy structure
element = M[0][0]
#	but we can also call it as a matrix in Matlab
element = M[0,0]

# There is a data type Matrix
M2 = np.matrix([[1,2],[3,4]])
# But the oficial documentations recomends against using them
# So we can transform it into an array

A = np.array(M2)

# This also allow us to do matrix operations as the 
#		traspose
print(A.T)
