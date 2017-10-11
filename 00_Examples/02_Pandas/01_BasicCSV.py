"""
	Author: Luis_C-137
	Parsing a CSV file
	This is just for practice purposes
	This is NOT functional code
"""
import os

csvRoot = ".\\..\\00_DataSets\\data_example.csv"

X = []

import numpy as numpy
for line in open(csvRoot):
	row = line.split(',')
	sample = map(float,row)
	X.append(sample)

for x in X:
	for f in x:
		print(f)