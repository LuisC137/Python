"""
	Author: Luis_C-137
	Tic Tac Toe with AI
"""

import numpy as np

from agent import Agent
from human import Human
from Enviroment import Enviroment

def get_state_hash_and_winner(env, i=0, j=0):
		results = []

		for v in (0, env.x, env.o):
			env.board[i,j] = v
			if j == 2:
				if i == 2:
					state = env.hash_state()
					ended = env.game_over(force_recalculate=True)
					winner = env.winner

					results.append((state, winner, ended))
				else:
					results += get_state_hash_and_winner(env,i+1,0)
			else:
				results += get_state_hash_and_winner(env,i,j+1)
		return results

def initialV_x(env,state_winner_triples):
	V = np.zeros(env.num_states)
	for state, winner, ended in state_winner_triples:
		if ended:
			if winner== env.x:
				v = 1
			else:
				v = 0
		else:
			v = 0.5
		V[state] = v
	return V
		
def initialV_o(env,state_winner_triples):
	V = np.zeros(env.num_states)
	for state, winner, ended in state_winner_triples:
		if ended:
			if winner== env.o:
				v = 1
			else:
				v = 0
		else:
			v = 0.5
		V[state] = v
	return V

def update_current_player(p1,p2):
	if (current_player == p1):
		return p2
	else:
		return p1

def draw_board(draw,env):
	if draw:
		env.draw_board()

def update_state_history(p1,p2,env):
	state = env.hash_state()
	p1.update_state_history(state)
	p2.update_state_history(state)

def update_players(p1,p2,env):
	p1.update(env)
	p2.update(env)

"""
def play_game(p1,p2,env,draw_flag=False):
	# Initialize current player
	global current_player

	# Loop until the game is over
	current_player = None
	while not env.game_over():
		print("let the game begin!")
		current_player = update_current_player(p1,p2)
		draw_board(draw_flag,env)
		current_player.take_action(env)
		update_state_history(p1,p2,env)
		draw_board(True,env)
		update_players(p1,p2,env)
"""
def play_game(p1, p2, env, draw=False):
	# loops until the game is over
	current_player = None
	while not env.game_over():
		# alternate between players
		# p1 always starts first
		if current_player == p1:
			current_player = p2
		else:
			current_player = p1

		# draw the board before the user who wants to see it makes a move
		if draw:
			if draw == 1 and current_player == p1:
				env.draw_board()
			if draw == 2 and current_player == p2:
				env.draw_board()

		# current player makes a move
		current_player.take_action(env)

		# update state histories
		state = env.hash_state()
		p1.update_state_history(state)
		p2.update_state_history(state)

	if draw:
		env.draw_board()

	# do the value function update
	p1.update(env)
	p2.update(env)

def main():
	print("\n\n---------------------")
	print("Initialize AI´s")
	p1 = Agent()
	p2 = Agent()

	# Set initial V for p1 and p2
	env = Enviroment()
	state_winner_triples = get_state_hash_and_winner(env)

	Vx = initialV_x(env, state_winner_triples)
	p1.setV(Vx)
	Vo = initialV_o(env, state_winner_triples)
	p2.setV(Vo)

	# Give each player their symbol
	p1.set_symbol(env.x)
	p2.set_symbol(env.o)

	print("\n---------------------")
	print("Training agent\n")

	T = 10000
	for t in range(T):
		if t % 200 == 0:
			print(t)
		play_game(p1,p2,Enviroment())

	print("\n---------------------")
	print("Let the game begin!\n\n\n")

	human = Human()
	human.set_symbol(env.o)
	while True:
		p1.set_verbose(True)
		play_game(p1, human, Enviroment(), draw=2)
		# I made the agent player 1 because I wanted to see if it would
		# select the center as its starting move. If you want the agent
		# to go second you can switch the human and AI.
		answer = input("Play again? [Y/n]: ")
		if answer and answer.lower()[0] == 'n':
			break	
	

if __name__ == '__main__':
	main()
else:
	print("Importing module {} may not be useful".format(__name__))