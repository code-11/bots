import pygame
from pygame.locals import *
import tkinter
from Board import *
from Players import *

import sys   # for exit and arg

class Game:
	players=None
	board=None
	done = False

	def __init__(self):
		self.players=Players()
		self.board=Board()

	def Draw(self,surf):
		#Clear view
		surf.fill((200,200,200))

		board_painter=self.board.make_painter()
		board_painter(surf,self.players.color_map)

		players_painter=self.players.make_painter()
		players_painter(surf)

		pygame.display.flip()

	def quit_callback(self):
		self.done = True

	def go(self):
		move_list=[]
		for i in range(3):
			move_list.append(self.players.move(self.board))
		print(move_list)

	def main(self):
		# initialise pygame
		pygame.init()
		ScreenSize = self.board.board_size()
		Surface = pygame.display.set_mode(ScreenSize)

		#initialise tkinter
		root = tkinter.Tk()
		root.protocol("WM_DELETE_WINDOW", self.quit_callback)
		main_dialog =  tkinter.Frame(root)
		main_dialog.winfo_toplevel().title("Bot Paint Arena")
		main_dialog.pack()

		player_lbl = tkinter.Label(root,text="Number Players Loaded: "+str(self.players.num_players()))
		player_lbl.pack()

		b = tkinter.Button(root, text="Move 100", command=self.go) 
		b.pack()

		# start pygame clock
		clock = pygame.time.Clock()
		gameframe = 0

	  # main loop
		while not self.done:
			try:
				main_dialog.update()
			except:
				print ("dialog error")

			self.Draw(Surface)
			clock.tick(100) # slow it to something slightly realistic
			gameframe += 1

		main_dialog.destroy()


if __name__ == '__main__': 
	# load_players()
	game=Game()
	game.main()