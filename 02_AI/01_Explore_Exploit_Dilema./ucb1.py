"""
	Author: Luis_C-137
	UCB1 exaple
"""
import math
import numpy as np
import matplotlib.pyplot as plt

class Bandit:
	def __init__(self,m):
		self.m = m
		self.mean = 0
		self.N = 0

	def pull(self):
		return np.random.rand() + self.m

	def update(self, x):
		self.N += 1
		self.mean = (1 -1.0/self.N) * self.mean + 1.0 / self.N * x

	def getUCB1(self,n):
		return self.mean + math.sqrt(2 * math.log(n) / (self.N + 0.00000001))

def run_experiment(m1,m2,m3,N):
	bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

	data = np.empty(N)

	for i in range(N):
		j = np.argmax([b.getUCB1(i+1) for b in bandits])
		x = bandits[j].pull()
		bandits[j].update(x)

		# for the plot
		data[i] = x
	cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

	# plot moving average ctr
	plt.title('Optimistic initial mean value')
	plt.plot(cumulative_average,label = 'Cumulative average')
	for b in bandits:
		plt.plot(np.ones(N) * b.m,label = 'Mean = ' + str(b.m))
		plt.plot(np.ones(N) * b.mean,label = 'Calc mean = ' + str(b.mean))
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