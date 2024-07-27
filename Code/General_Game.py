import tkinter
from tkinter import *
from tkinter import messagebox

class General():
    def __init__ (self, GL):
        self.GameBoard = GL
        self.name = "General game"
        
    def ExtraPointCheck(self, GUI, x, y, button, current_turn):
        x_bound = len(self.GameBoard.board) - 1
        y_bound = len(self.GameBoard.board[0]) - 1
        w_color = current_turn.lower()
        
        total_points = 0
        if self.GameBoard.board[x][y] == "S":
            #check all of adjacent spaces for O's
            #leaving 200s and 50s for test
            if x+1 <= x_bound and self.GameBoard.board[x+1][y] == "O" and x+2 <= x_bound and self.GameBoard.board[x+2][y] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y].config(bg=w_color)
                button[x+2][y].config(bg=w_color)
                total_points += 1
            if x-1 >= 0 and self.GameBoard.board[x-1][y] == "O" and x-2 >= 0 and self.GameBoard.board[x-2][y] == "S":
                button[x][y].config(bg=w_color)
                button[x-1][y].config(bg=w_color)
                button[x-2][y].config(bg=w_color)
                total_points += 1
            if x+1 <= x_bound and y+1 <= y_bound and  self.GameBoard.board[x+1][y+1] == "O" and x+2 <= x_bound and y+2 <= y_bound and self.GameBoard.board[x+2][y+2] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y+1].config(bg=w_color)
                button[x+2][y+2].config(bg=w_color)
                total_points += 1
            if y+1 <= y_bound and self.GameBoard.board[x][y+1] == "O" and y+2 <= y_bound and self.GameBoard.board[x][y+2] == "S":
                button[x][y].config(bg=w_color)
                button[x][y+1].config(bg=w_color)
                button[x][y+2].config(bg=w_color)
                total_points += 1
            if y-1 >= 0 and self.GameBoard.board[x][y-1] == "O" and y-2 >= 0 and self.GameBoard.board[x][y-2] == "S":
                button[x][y].config(bg=w_color)
                button[x][y-1].config(bg=w_color)
                button[x][y-2].config(bg=w_color)
                total_points += 1
            if x-1 >= 0 and y-1 >= 0 and self.GameBoard.board[x-1][y-1] == "O" and x-2 >= 0 and y-2 >= 0 and self.GameBoard.board[x-2][y-2] == "S":
                button[x][y].config(bg=w_color)
                button[x-1][y-1].config(bg=w_color)
                button[x-2][y-2].config(bg=w_color)
                total_points += 1
            if x+1 <= x_bound and y-1 >= 0 and self.GameBoard.board[x+1][y-1] == "O" and x+2 <= x_bound and y-2 >= 0 and self.GameBoard.board[x+2][y-2] == "S":
                
                button[x][y].config(bg=w_color)
                button[x+1][y-1].config(bg=w_color)
                button[x+2][y-2].config(bg=w_color)
                total_points += 1
            if x-1 >= 0 and y+1 <= y_bound and self.GameBoard.board[x-1][y+1] == "O" and x-2 >= 0 and y+2 <= y_bound and self.GameBoard.board[x-2][y+2] == "S":
                button[x][y].config(bg=w_color)
                button[x-1][y+1].config(bg=w_color)
                button[x-2][y+2].config(bg=w_color)
                total_points += 1
        if self.GameBoard.board[x][y] == "O":
            #check half of all adjecent spaces for S's since no need to check other half until check is true
            if x+1 <= x_bound and self.GameBoard.board[x+1][y] == "S" and x-1 >= 0 and self.GameBoard.board[x-1][y] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y].config(bg=w_color)
                button[x-1][y].config(bg=w_color)
                total_points += 1
            if y+1 <= y_bound and self.GameBoard.board[x][y+1] == "S" and y-1 >= 0 and self.GameBoard.board[x][y-1] == "S":
                button[x][y].config(bg=w_color)
                button[x][y+1].config(bg=w_color)
                button[x][y-1].config(bg=w_color)
                total_points += 1
            if x+1 <= x_bound and y+1 <= y_bound and self.GameBoard.board[x+1][y+1] == "S" and x-1 >= 0 and y-1 >= 0 and self.GameBoard.board[x-1][y-1] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y+1].config(bg=w_color)
                button[x-1][y-1].config(bg=w_color)
                total_points += 1
            if x-1 >= 0 and y+1 <= y_bound and self.GameBoard.board[x-1][y+1] == "S" and x+1 <= x_bound and y-1 >= 0 and self.GameBoard.board[x+1][y-1] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y-1].config(bg=w_color)
                button[x-1][y+1].config(bg=w_color)
                total_points += 1
        return total_points
        
    def PointGive(self, current_turn, x, y, b_s, r_s, GUI, button, current_turn_text, b_p, r_p, c_t):
        total_points = self.ExtraPointCheck(GUI, x, y, self.GameBoard.button, current_turn)
        if current_turn == "Blue":
            self.GameBoard.blue_points += total_points
            b_p.config(text="Points: " + str(self.GameBoard.blue_points))
            c_t.set("Blue")
            self.GameBoard.current_player = self.GameBoard.b_player
        else:
            self.GameBoard.red_points += total_points
            r_p.config(text="Points: " + str(self.GameBoard.red_points))
            c_t.set("Red")
            self.GameBoard.current_player = self.GameBoard.r_player
        current_turn_text.config(text="Current turn: " + c_t.get() + "\n" + current_turn + " scored a point!!")
        
        
        self.is_point = False