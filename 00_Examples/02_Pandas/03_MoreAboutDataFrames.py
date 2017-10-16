"""
	Author: Luis_C-137
	Some other funcitons of pandas like column manipulation
	and footer exclusion.
	Also using the apply funcion to generate new columns with new data
	This is just for practice purposes
	This is NOT functional code
"""

def do_something(row):
		return row['col1']/row['new']

import pandas as pd
csvRoot = ".\\..\\00_DataSets\\data_example_with_title_and_footer.csv"

df = pd.read_csv(csvRoot,engine="python",skipfooter=3)

# Check the column Names
df.columns

# Set the column names
df.columns = ["col1","col2","col3"]

# Check a column by name
df['col1']
df.col1

# To add a new column full of ones
df['ones'] = 1

print(df.head())

# What if a I want a different value?
df['new'] = df.apply(lambda row: row['col1']*row['col2'],axis=1)
df['new2'] = df.apply(do_something,axis=1)
print(df.head())




