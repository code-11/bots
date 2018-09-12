import pygame.draw as pydraw
import pygame.color as col
import pygame.rect as rec
class Board:
	BLANK=0

	WIDTH=10
	PADDING=1
	XLEN=50
	YLEN=60

	data=[]

	@staticmethod
	def zeros(x,y):
		to_return=[]
		for i in range(x):
			arr=[]
			for j in range(y):
				arr.append(Board.BLANK)
			to_return.append(arr)
		return to_return
			
	@staticmethod
	def brighten(color):
		r=Board.clamp_color(color.r+140)
		g=Board.clamp_color(color.g+140)
		b=Board.clamp_color(color.b+140)
		return col.Color(r,g,b,color.a) 

	@staticmethod
	def clamp_color(val):
		if val<0:
			return 0
		if val>255:
			return 255
		return val

	def __init__(self):
		self.data=self.zeros(Board.XLEN,Board.YLEN)

	def set_claim(self,x,y,player):
		self.data[x][y]=player.uid

	def x_size(self):
		return len(self.data)

	def y_size(self):
		return len(self.data[0])

	def make_paint_helper(self,surf,color_map):
		for i,arr in enumerate(self.data):
			for j,el in enumerate(arr):
				rect=rec.Rect(i*(Board.WIDTH+Board.PADDING),j*(Board.WIDTH+Board.PADDING),Board.WIDTH,Board.WIDTH)
				col=color_map[el]
				if(el!=None):
					col=Board.brighten(col)
				pydraw.rect(surf,col,rect)

	def make_painter(self):
		return self.make_paint_helper

	def board_size(self):
		return (Board.XLEN*(Board.WIDTH+Board.PADDING),Board.YLEN*(Board.WIDTH+Board.PADDING))