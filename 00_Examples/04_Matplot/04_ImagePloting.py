"""
	Author: Luis_C-137
	Plotting images exmaple
	This is just for practice purposes
	This is NOT functional code
"""
import pandas as pd 
import matplotlib.pyplot as plt


csvRoot = ".\\train.csv"

df = pd.read_csv(csvRoot)

print(df.shape)

M = df.as_matrix()

im = M[0,1:]
im = im.reshape(28,28)
print(im.shape)

#plt.imshow(im)	# Color plot
#plt.imshow(im,cmap='gray')	# Grey scale plot
plt.imshow(255-im,cmap='gray')	# Plot the inverse grey scale
plt.title("This is number: " + str(M[0,0]))
plt.show()
