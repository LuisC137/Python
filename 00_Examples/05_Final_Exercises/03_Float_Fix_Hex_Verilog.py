"""
	Author: Luis_C-137
	(1) Transform an array of floating point to an array of
			fixed point where the int part has cero bits and the 
			decimal part has 32 bits.
	(2) Use this new column to map the HEX value to a new column
	(3) Then create an array of strings with the verilog format 
			to assign the hex value to the array
	Create a file with this Array of strings
"""

import sys
import math
import pandas as pd 
import tkinter as tk
from tkinter import filedialog

def promptForPath () :
	root = tk.Tk()
	root.withdraw()
	return filedialog.askopenfilename()

def getCSVSource () :
	if (len(sys.argv) == 1) :
		csv_path = promptForPath() 
	else :
		csv_path = sys.argv[1]
	return csv_path

def dec2hex (row) :
	return hex(int(row[1])).split('x')[-1]

def hex2verilog (row) :
	return 'H[' + str(row.name) + "] = 32'h" + format(row[1], '08x')

csv_path = getCSVSource()
floatArray = pd.read_csv(csv_path,header = None)

floatArray[1] = floatArray[0] * (2**32)
floatArray[1] = floatArray.apply(lambda row: math.floor(row[1]),axis=1)	#1

# Implementation of step #3 did not used step #2 due to format issues
floatArray[2] = floatArray.apply(dec2hex,axis=1) #2

floatArray[3] = floatArray.apply(hex2verilog,axis=1) #3

print(floatArray.head())