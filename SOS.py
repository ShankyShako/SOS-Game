import sys
sys.path.append('/path/to/Code')
from Code.GUI import CreateGame
import tkinter
from tkinter import *
from Code.GameLogic import GameBoard
from Code.COMPUTER import ComputerPlayer

GUI = Tk() 
board_int = IntVar()
board_int.set(8)
GL = GameBoard(board_int.get(), GUI)
CO = ComputerPlayer(GL)
GUI.eval('tk::PlaceWindow . center')
CreateGame(GUI, board_int, GL, CO)
GUI.mainloop()