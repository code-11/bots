import pygame.draw as pydraw
import pygame.color as col
import pygame.rect as rec

from Player import *

class Players:
	data=[] #players

	def __init__(self):
		print("initted")
		blue=col.Color(0, 0, 244, 244)
		test= Player(20,25,blue)
		self.data.append(test)

	def make_paint_helper(self,surf):
		for player in self.data:
			player_painter=player.make_painter()
			player_painter(surf)

	def make_painter(self):
		return self.make_paint_helper