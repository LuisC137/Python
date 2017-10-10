"""
	Author: Luis_C-137
	Explore the dot product on Numpy
	This is just for practice purposes
	This is NOT functional code
"""

import numpy as np

a = np.array([1,2])
b = np.array([2,1])

dot = 0

for e, f in zip(a,b):
	dot+= e*f

print('This is the dot product of a + b')
print(dot)

print('This is the product of the vector a * b')
print(a * b)

print('We can also use Numpy built in method')
print(np.sum(a * b))

# We can also call it as:
np.dot(a,b)

# Or as:
a.dot(b)

# We can also calculate the magnitudnp.linalg.norm(a) * np.linalg.norm(b)

amag = np.sqrt( (a**2).sum())
print("This is the magnitud of the vector A")
print(amag)

# Which is the same as:
amag = np.linalg.norm(a)

# Now we can implement it all to calculate the angle
cosAngle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("The angle in radians is:")
print(cosAngle)