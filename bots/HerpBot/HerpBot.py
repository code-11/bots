from Player import Direction 
class HerpBot:

	last_direction=None
	steps=0

	def __init__ (self):
		self.last_direction=Direction.LEFT
		self.steps=0

	def get_next_move(self,uid,game_state):
		to_return=None
		if (self.steps<5):
			to_return=self.last_direction
			self.steps+=1
		else:
			to_return=self.last_direction.anticlockwise()
			self.last_direction=to_return
			self.steps=0

		return to_return

def provide_bot():
	return HerpBot()

