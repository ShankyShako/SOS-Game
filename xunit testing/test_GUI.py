from GUI import CreateGame
from GUI import ResizeBoard
import tkinter
from tkinter import *
from GameLogic import GameBoard

from COMPUTER import ComputerPlayer


def test_resize():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    
    CreateGame(GUI, board_int, GL, CO)
    
    board_int.set(6)
    ResizeBoard(GL, GUI, board_int, 8)
    assert len(GL.board[0]) == 6
    
def test_resize2():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)

    CreateGame(GUI, board_int, GL, CO)
    board_int.set(15)
    ResizeBoard(GL, GUI, board_int, 8)
    assert len(GL.board[0]) != 15
    
def test_resize3():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)

    CreateGame(GUI, board_int, GL, CO)
    board_int.set(4)
    ResizeBoard(GL, GUI, board_int, 8)
    assert len(GL.board[0]) != 4

def test_creategame():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)

    CreateGame(GUI, board_int, GL, CO)
    GUI.mainloop()
