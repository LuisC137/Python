"""
	Author: Luis_C-137
	Help to find where to find usefull stuff and exmaple
	This is just for practice purposes
	This is NOT functional code
"""
from scipy.stats import multivariate_normal as mvn
import numpy as np
import matplotlib.pyplot as plt

# Check documentation for any of this functions on Scipy.org

# Load Matlab .mat
#spipy.io.loadmat(file_name)


# Load Sound .wav
# scipy.wavfile.read(filename)
# scipy.wavfile.write(filename)

# Convolution in signal processing
# Scipy has several convolution methods, it is better to check the documentation

# Filters
# Scipy also has many filters

# FFT is in Numpy!
x = np.linspace(0,100,10000)
y = np.sin(x) + np.sin(3*x) + np.sin(5*x)

plt.plot(y)
plt.show()

Y = np.fft.fft(y)

plt.plot(np.abs(Y))
plt.show()
