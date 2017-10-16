"""
	Author: Luis_C-137
	Using joins exmaple
	This is just for practice purposes
	This is NOT functional code
"""
import pandas as pd

t1 = pd.read_csv('table1.csv')
t2 = pd.read_csv('table2.csv')

print(t1)
print(t2)

m = pd.merge(t1,t2,on='user_id')
print(m)
m = t1.merge(t2,on='user_id')
print(m)