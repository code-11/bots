import pygame.draw as pydraw
import pygame.color as col
import pygame.rect as rec

from Player import *

class Players:
	data=[] #players
	color_map={}

	def __init__(self):
		print("initted")
		#This is were colors and unique ids are assigned to players
		blue=col.Color(0, 0, 244, 244)
		white=col.Color(244, 244, 244, 244)
		test= Player(20,25,blue)
		self.data.append(test)
		self.color_map[None]=white
		self.color_map[test]=blue

	def make_paint_helper(self,surf):
		for player in self.data:
			player_painter=player.make_painter()
			player_painter(surf)

	def make_painter(self):
		return self.make_paint_helper