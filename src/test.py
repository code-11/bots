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


def GetInput():

  for event in pygame.event.get():
    if event.type == QUIT:
      return True
    if event.type == KEYDOWN:
      print (event)
    if event.type == MOUSEBUTTONDOWN:
      print (event)
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

    if GetInput():  # input event can also comes from diaglog
      break
    Draw(Surface,board,players)
    clock.tick(100) # slow it to something slightly realistic
    gameframe += 1

  main_dialog.destroy()

if __name__ == '__main__': 
	b=Board()
	ps=Players()

	b.set_claim(3,10,ps.data[0])
	b.set_claim(4,10,ps.data[0])
	b.set_claim(3,9,ps.data[0])
	b.set_claim(3,8,ps.data[0])

	main(b,ps)