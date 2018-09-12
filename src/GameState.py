import copy
class GameState:

	board_state=None
	player_state={}

	def __init__ (self,board,players):
		self.board_state=copy.deepcopy(board.data)
		for player in players.player_map.values():
			self.player_state[player.uid]=(player.x_pos,player.y_pos)
