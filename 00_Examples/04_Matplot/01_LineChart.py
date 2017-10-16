"""
	Author: Luis_C-137
	Line chart exmaple
	This is just for practice purposes
	This is NOT functional code
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100) # Start point, end point, number of points

y = np.sin(x)

plt.plot(x,y)

plt.xlabel("Time")
plt.ylabel("Function of time")
plt.title("My first chart")

plt.show();
