"""
	Author: Luis_C-137
	Histogram exmaple
	This is just for practice purposes
	This is NOT functional code
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

csvRoot = ".\\..\\00_DataSets\\data_example.csv"

R = np.random.random(10000)

#plt.hist(R)
plt.hist(R,bins=20)
plt.show()
