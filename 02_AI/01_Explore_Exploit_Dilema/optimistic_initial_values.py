"""
	Author: Luis_C-137
	First example to compare optimistic initial value
"""

import numpy as np
import matplotlib.pyplot as plt

upper_limit = 5

class Bandit:
	def __init__(self,m):
		self.m = m
		self.mean = upper_limit
		self.N = 0

	def pull(self):
		return np.random.rand() + self.m

	def update(self, x):
		self.N += 1
		self.mean = (1 -1.0/self.N) * self.mean + 1.0 / self.N * x

def run_experiment(m1,m2,m3,N):
	bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

	data = np.empty(N)

	for i in range(N):
		j = np.argmax([b.mean for b in bandits])
		x = bandits[j].pull()
		bandits[j].update(x)

		# for the plot
		data[i] = x
	cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

	# plot moving average ctr
	plt.title('Optimistic initial mean value')
	plt.plot(cumulative_average,label = 'Cumulative average')
	for b in bandits:
		plt.plot(np.ones(N) * b.mean)
	plt.legend()
	plt.xscale('log')
	plt.show()


def main():
	print("\n\n---------------------")
	print("And so it begins...\n\n\n")
	run_experiment(1.0,2.0,3.0,10000)

if __name__ == '__main__':
	main()
else:
	print("Importing module {} may not be useful".format(__name__))