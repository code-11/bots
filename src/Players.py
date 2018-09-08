import pygame.draw as pydraw
import pygame.color as col
import pygame.rect as rec

from Player import *

class Players:
	data=[] #players
	color_map={}
	move_map={}

	def __init__(self):
		print("initted")
		#This is were colors and unique ids are assigned to players
		blue=col.Color(0, 0, 244, 244)
		red=col.Color(244,0,0,244)
		white=col.Color(244, 244, 244, 244)
		test= Player(13,10,blue)
		test2=Player(13,25,red)
		self.data.append(test)
		self.data.append(test2)
		self.color_map[None]=white
		self.color_map[test]=blue
		self.color_map[test2]=red

		self.move_map={Direction.UP:self.move_player_up, Direction.DOWN:self.move_player_down, Direction.LEFT:self.move_player_left, Direction.RIGHT:self.move_player_right}


	def move(self,board):
		for player in self.data:
			self.move_player(player,board)

	def move_player(self,player,board):
		move_enum=player.get_next_move()
		self.move_map[move_enum](player,board)
		board.set_claim(player.x_pos,player.y_pos,player)

	def move_player_left(self,player,board):
		new_x_pos=player.x_pos-1
		if new_x_pos >= 0 and not(self.location_occupied(new_x_pos,player.y_pos,board)):
			player.x_pos=new_x_pos

	def move_player_right(self,player,board):
		new_x_pos= player.x_pos+1
		if new_x_pos <= board.x_size()-1 and not(self.location_occupied(new_x_pos,player.y_pos,board)):
			player.x_pos=new_x_pos

	def move_player_up(self,player,board):
		new_y_pos= player.y_pos-1
		if new_y_pos >= 0 and not(self.location_occupied(player.x_pos, new_y_pos, board)):
			player.y_pos=new_y_pos

	def move_player_down(self,player,board):
		new_y_pos=player.y_pos+1
		if new_y_pos <= board.y_size()-1 and not(self.location_occupied(player.x_pos, new_y_pos, board)):
			player.y_pos=new_y_pos

	def location_occupied(self,x,y,board):
		for player in self.data:
			if player.x_pos==x and player.y_pos==y:
				return True
		return False

	def make_paint_helper(self,surf):
		for player in self.data:
			player_painter=player.make_painter()
			player_painter(surf)

	def make_painter(self):
		return self.make_paint_helper