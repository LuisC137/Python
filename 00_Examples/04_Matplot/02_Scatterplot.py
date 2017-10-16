"""
	Author: Luis_C-137
	Scatter chart exmaple
	This is just for practice purposes
	This is NOT functional code
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

csvRoot = ".\\..\\00_DataSets\\data_example.csv"

A = pd.read_csv(csvRoot,header=None).as_matrix()

x = A[:,0]	# The culumn ':' indeicates that all data 
y = A[:,1]	# 		of the column in going to be used

x_line = np.linspace(0,20000000,x.size)
y_function = x_line*0.5

plt.scatter(x,y)
plt.plot(x_line,y_function)
plt.show() 
