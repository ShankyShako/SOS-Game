import tkinter
from tkinter import *

from functools import partial
from tkinter import messagebox
from copy import deepcopy

class Simple():
    def __init__ (self, GL):
        self.GameBoard = GL
        self.name = "Simple game"
        
    def PointGive(self, current_turn, x, y, b_s, r_s, GUI, button, current_turn_text, b_p, r_p, c_t):
        current_turn_text.config(text="Winner is " + current_turn + "!")
        for i in range(len(self.GameBoard.board)):
            for j in range(len(self.GameBoard.board[0])):
                    self.GameBoard.button[i][j].config(state = DISABLED)
                    
        if current_turn == "Blue":
            c_t.set("Blue")
            self.GameBoard.current_player = self.GameBoard.b_player
        else:
            c_t.set("Red")
            self.GameBoard.current_player = self.GameBoard.r_player
        self.GameBoard.isOver = True
        self.GameBoard.turn += 1