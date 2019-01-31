"""
	Author: Luis_C-137
	Agent file
"""

import numpy as np

#Constant definition
LENGTH = 3

class Agent:

	def __init__(self, eps=0.1, alpha=0.5):
		self.eps = eps
		self.alpha = alpha
		self.verbose = False
		self.state_history = []

	def setV(self, V):
		self.V = V

	def set_symbol(self, sym):
		self.sym = sym

	def set_verbose(self, v):
		self.verbose = v

	def reset_history(self):
		self.state_history = []

	def take_random_action(self,env):
		if self.verbose:
			print("Taking a random action")

		#Find posible moves
		posible_moves = []
		for row in range(LENGTH):
			for col in range(LENGTH):
				if env.is_empty(row, col):
					posible_moves.append((row,col))
		#Select move
		idx = np.random.choice(len(posible_moves))
		next_move = posible_moves[idx]

		return next_move

	def take_greedy_action(self,env):
		pos2value ={}
		next_move = None
		best_value = -1
		for row in range(LENGTH):
			for col in range(LENGTH):
				if env.is_empty(row,col):
					env.board[row,col] = self.sym
					state = env.hash_state()
					env.board[row,col] = 0
					pos2value[(row,col)] = self.V[state]
					if self.V[state] > best_value:
						best_value = self.V[state]
						best_state = state
						next_move = (row,col)

		# if verbose, draw the board w/ the values
		if self.verbose:
			print("Taking a greedy action")
			for i in range(LENGTH):
				print("------------------")
				for j in range(LENGTH):
					if env.is_empty(i, j):
					# print the value
						print(" %.2f|" % pos2value[(i,j)], end="")
					else:
						print("  ", end="")
						if env.board[i,j] == env.x:
							print("x  |", end="")
						elif env.board[i,j] == env.o:
							print("o  |", end="")
						else:
							print("   |", end="")
				print("")
			print("------------------")
		return next_move

	def take_action(self,env):
		r = np.random.rand()
		best_state = None
		if r < self.eps:
			next_move = self.take_random_action(env)
		else:
			next_move = self.take_greedy_action(env)

		env.board[next_move[0], next_move[1]] = self.sym

	def update_state_history(self, s):
		self.state_history.append(s)

	def update(self, env):
		reward = env.reward(self.sym)
		target = reward
		for prev in reversed(self.state_history):
			value = self.V[prev] + self.alpha*(target - self.V[prev])
			self.V[prev] = value
			taget = value
		self.reset_history() 

	

