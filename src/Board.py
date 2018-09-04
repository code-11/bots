import pygame.draw as pydraw
import pygame.color as col
import pygame.rect as rec
class Board:
	data=[]

	@staticmethod
	def zeros(x,y):
		to_return=[]
		for i in range(y):
			arr=[]
			for j in range(x):
				arr.append(0)
			to_return.append(arr)
		return to_return
			

	def __init__(self):
		self.data=self.zeros(2,3)

	def make_paint_helper(self,surf):
		WIDTH=10
		PADDING=1
		color=col.Color(244, 0, 0, 0)
		for i,arr in enumerate(self.data):
			for j,el in enumerate(arr):
				rect=rec.Rect(i*(WIDTH+PADDING),j*(WIDTH+PADDING),WIDTH,WIDTH)
				pydraw.rect(surf,color,rect)

	def make_painter(self):
		return self.make_paint_helper
