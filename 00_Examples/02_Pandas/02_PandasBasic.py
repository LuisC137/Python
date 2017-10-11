"""
	Author: Luis_C-137
	Basic Pandas exmaple
	This is just for practice purposes
	This is NOT functional code
"""

import pandas as pd
csvRoot = ".\\..\\00_DataSets\\data_example.csv"

X = pd.read_csv(csvRoot,header = None)

type(X) # Will show use it is a DataFrame

print("Info -----------------------------")
print(X.info())
print("First Rows")
print(X.head())
print("First 10 Rows")
print(X.head(10))

#Convert the data into a matrix
M = X.as_matrix()
print(type(M))	# It returns a munpy array

print(M[0])	# Numpy matrix return the first row
print(X[0]) # Pandas return the first column wich is of type Series

# The how do I get a Row in Pandas???
X.iloc[0]
X[0]		# They are the same and they are also series

# Get many columns in Pandas
print(X[[0,2]])

# Select columns based on criteria
X[ X[0] < 5]

# We can also check the condition
X[0] < 5




