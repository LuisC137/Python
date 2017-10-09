
import numpy as np

def printList(list) :
	for element in list :
		print(element)


""" Main section """
L = [1,2,3]

A = np.array([1,2,3])

print('This is L:')
printList(L)
print('This is A:')
printList(A)

# we can apend to the list
L += [5]
# But we cannot apend to the Numpy array
# A += [1]

print('We trieded to apend stuff')
print('This is L:')
printList(L)
print('This is A:')
printList(A)

# We have create a new array to
#		make an addition of the List
print('Experiment with the adition of the vectors')
L2 = []

for e in L :
	L2.append(e + e)

print('This is L:')
printList(L2)

# In an array it is simpler to sum the vectors
print('This is A:')
printList(A + A) 

# Both elements can be multiplied, but they
#		will return a different result
print('Multiply each one by two')
print('This is L')
print(L*2)
print('This is A:')
print(A*2)

# Now lets try to poower the elements
print('Now lets try to poower the elements')
L2 = [] 
for e in L :
	L2.append(e**3)
print('This is L:')
print(L2)
print('This is A:')
print(A**3)