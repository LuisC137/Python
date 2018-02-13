"""
	Author: Luis_C-137
	Tic Tac Toe with AI
"""

def update_current_player(p1,p2):
	if (current_player == p1):
		player = p2
	else
		player = p1
	return player

def play_game(p1,p2,env,draw_flag=False):
	# Initialize current player
	global current_player = None

	# Loop until the game is over
	while not env.game_over():
		current_player = update_current_player(p1,p2)
		draw_board(draw_flag)
		current_player.take_action(env)
		update_states_history()
		update_players()

def main():
	print("\n\n---------------------")
	print("Let the game begin!\n\n\n")
	
	play_game(p1,p2,env,True)		
	

if __name__ == '__main__':
	main()
else:
	print("Importing module {} may not be useful".format(__name__))