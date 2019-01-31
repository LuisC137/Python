"""
	Author: Luis_C-137
	Enviroment file
"""

import numpy as np 

#Constant definition
LENGTH = 3

class Enviroment:

	def __init__(self):
		self.board = np.zeros((LENGTH,LENGTH))
		self.x = -1
		self.o = 1
		self.winner = None
		self. ended = False
		self.num_states = 3**(LENGTH*LENGTH)

	def is_empty(self,i,j):
		return self.board[i,j] == 0

	def reward(self, sym):
		if not self.game_over():
			return 0

		return 1 if self.winner == sym else 0

	def hash_cell(self,cell):
		if cell == self.o:
			v = 2
		elif cell == self.x:
			v = 1
		else:
			v = 0
		return v

	def hash_state(self):
		k = 0
		h = 0
		for row in self.board :
			for cell in row :
				v = self.hash_cell(cell)
				h += (3**k) * v
				k += 1
		return h

	def game_over(self, force_recalculate=False):
		if not force_recalculate and self.ended:
			return self.ended

		for player in (self.x, self.o):
			#Check all the rows
			for row in range(LENGTH):
				if self.board[row].sum() == player*LENGTH:
					self.winner = player
					self.ended = True
					return True
			#Check all the columns
			for col in range(LENGTH):
				if self.board[:,col].sum() == player*LENGTH:
					self.winner = player
					self.ended = True
					return True
			#Check the first diagonal
			if self.board.trace() == player * LENGTH:
					self.winner = player
					self.ended = True
					return True
			#Check the second diagonal
			if np.fliplr(self.board).trace() == player * LENGTH:
					self.winner = player
					self.ended = True
					return True
			#Check if draw
			if np.all((self.board == 0) == False):
				self.winner = None
				self.ended = True
				return True

		self.winner= None
		return False

	def is_draw(self):
	    return self.ended and self.winner is None

	def draw_board(self):
		for row in range(LENGTH):
			print("-------------")
			line = ""
			for col in range(LENGTH):
				line += "| "
				if self.board[row,col] == self.o:
					line += "O "
				elif self.board[row,col] == self.x:
					line += "X "
				else:
					line += "  "
			line += "|"
			print(line)
		print("-------------")



def main():
	#help(Enviroment)

	env = Enviroment()
	env.board[2,2] = -1
	env.board[2,1] = 1
	print(env.hash_state())
	print(env.game_over(True))
	env.draw_board()

if __name__ == '__main__':
	print("This file contains the enviroment class of the tik tak toe game, \n\tby accesing it this way it will run the help method for the class\n\tand then the test suit will be runned")
	main()
else:
	print("Importing module {}".format(__name__))