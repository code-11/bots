import pygame.draw as pydraw
import pygame.rect as rec

from enum import Enum

from Board import *
from RoundedRect import *

class Direction(Enum):
	UP   = 1
	DOWN = 2
	LEFT = 3
	RIGHT= 4

class Player:
	INSET_X=2
	INSET_Y=2

	SIZE_X=Board.WIDTH-2
	SIZE_Y=Board.WIDTH-2

	x_pos=None
	y_pos=None
	color=None

	def __init__(self,x_pos,y_pos,color):
		self.x_pos=x_pos
		self.y_pos=y_pos
		self.color=color

	def __str__(self):
		return "<Player x:"+self.x_pos+" y:"+self.y_pos+" col:"+self.color

	def make_paint_helper(self,surf):
		rect=rec.Rect(self.x_pos*(Board.WIDTH+Board.PADDING)+Player.INSET_X/2,self.y_pos*(Board.WIDTH+Board.PADDING)+Player.INSET_Y/2,Player.SIZE_X,Player.SIZE_Y)
		AAfilledRoundedRect(surf,rect,self.color,radius=.4)

	def make_painter(self):
		return self.make_paint_helper

	def get_next_move(self):
		return Direction.UP