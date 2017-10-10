"""
	Author: Luis_C-137
	Examples of matrix operations
	This is just for practice purposes
	This is NOT functional code
"""

import numpy as np

# Create a matrix
A = np.array([[1,2],[3,4]])
print(A)

# Matrix inverse
Ainv = np.linalg.in(A)
print('The inverse is')
print(Ainv)

# Calculate identity matrix
identity = Ainv.dot(A) # A.dot(Ainv) would produce the same output
print('The identity is matrix is ')
print(identity)

# To get the diagonal vector
print('Get the diagonal vector')
print(np.diag(A))
# NOTE: The diag operation can also get a 1D Array and get the 2D Matrix of it

a = np.array([1,2])
b = np.array([3,4])

# Calculate the element wise product
print('element wise product')
print(a*b)

# Calculate the dot product
print('Dot prodcut')
print(a.dot(b))
print(a.inner(b))

# Calculate outer product
print('Outer product')
print(np.outer(a,b))

# Get the sum of the diagonal
print('Diagonal Sum')
print(np.diag(A).sum())
print(np.trace(A))

# Eigenvalues and Eigenvectors
X = np.random.randn(100,3)	# Gaussian distribution
print('For the Eigenvalues and Eigenvectors we will use the next matrix')
print(X)

# Calculate the covariance of a matrix
conv = np.conv(X.T)	# To calculate the covariance we have 
					#		to use the Traspose
print('We can calcualte the covariance')
print('conv')

print('Finaly we calculate the eigen vector')
aux = np.linalg.eigh(conv)	# we use eigh because it is only for 
							#		symetric and Midian matrixes
print(aux)
# We can also use eig method but it may be in a diferent order
aux = np.linalg.eig(conv)
print(aux)


