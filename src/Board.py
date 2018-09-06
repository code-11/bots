import pygame.draw as pydraw
import pygame.color as col
import pygame.rect as rec
class Board:
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
				arr.append(0)
			to_return.append(arr)
		return to_return
			

	def __init__(self):
		self.data=self.zeros(Board.XLEN,Board.YLEN)

	def make_paint_helper(self,surf):
		white=col.Color(244, 244, 244, 244)
		for i,arr in enumerate(self.data):
			for j,el in enumerate(arr):
				rect=rec.Rect(i*(Board.WIDTH+Board.PADDING),j*(Board.WIDTH+Board.PADDING),Board.WIDTH,Board.WIDTH)
				pydraw.rect(surf,white,rect)

	def make_painter(self):
		return self.make_paint_helper

	def board_size(self):
		return (Board.XLEN*(Board.WIDTH+Board.PADDING),Board.YLEN*(Board.WIDTH+Board.PADDING))
