import pygame
from pygame.locals import *
import tkinter
from Board import *
from Players import *

import sys   # for exit and arg


def Draw(surf,board,players):
  #Clear view
  surf.fill((200,200,200))

  board_painter=board.make_painter()
  board_painter(surf,players.color_map)

  players_painter=players.make_painter()
  players_painter(surf)

  pygame.display.flip()


def GetInput(board,players):

  for event in pygame.event.get():
    if event.type == QUIT:
      return True
    if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
      print (event)
      players.move(board)
    sys.stdout.flush()  # get stuff to the console
  return False


Done = False

def quit_callback():
  global Done
  Done = True

def main(board,players):

  # initialise pygame
  pygame.init()
  ScreenSize = board.board_size()
  Surface = pygame.display.set_mode(ScreenSize)

  #initialise tkinter
  root = tkinter.Tk()
  root.protocol("WM_DELETE_WINDOW", quit_callback)
  main_dialog =  tkinter.Frame(root)
  main_dialog.pack()

  # start pygame clock
  clock = pygame.time.Clock()
  gameframe = 0

  # main loop
  while not Done:
    try:
      main_dialog.update()
    except:
      print ("dialog error")

    if GetInput(board,players):  # input event can also comes from diaglog
      break
    Draw(Surface,board,players)
    clock.tick(100) # slow it to something slightly realistic
    gameframe += 1

  main_dialog.destroy()


if __name__ == '__main__': 
	# load_players()
	b=Board()
	ps=Players()
	main(b,ps)