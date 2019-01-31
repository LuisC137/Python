"""
	Author: Luis_C-137
	Human class file
"""
from __future__ import print_function, division
from builtins import range, input

import numpy as np
import matplotlib.pyplot as plt

class Human:
	def __init__(self):
		pass

	def set_symbol(self, sym):
		self.sym = sym

	def take_action(self, env):
		while True:
			# break if we make a legal move
			move = input("Enter coordinates i,j for your next move (i,j = 0..2): ")
			i, j = move.split(',')
			i = int(i)
			j = int(j)
			if env.is_empty(i,j):
				env.board[i,j] = self.sym
				break

	def update(self, env):
		pass

	def update_state_history(self, s):
		pass

