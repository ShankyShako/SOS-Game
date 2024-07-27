import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import tkinter
from tkinter import *

from Code.Simple_Game import Simple
from Code.General_Game import General
from Code.Record import Recorder

class GameBoard():
    def __init__(self, board_size, GUI):
        self.board = []
        self.button = []
        for i in range(board_size):
            self.board.append(i)
            self.board[i] = []
            for j in range(board_size):
                self.board[i].append(" ")
        self.canvas = Canvas(GUI)
        self.canvas.place(x=200 + board_size * 24, y=130)
        self.turn = 0
        self.current_turn = "Blue"
        self.sim_game = Simple(self)
        self.gen_game = General(self)
        self.curr_gamemode = self.sim_game
        self.is_point = False
        self.prompt_up = False
        self.ng_or_oc = 0
        self.prompt_sg = IntVar()
        self.blue_points = 0
        self.red_points = 0
        self.lastx = 0
        self.lasty = 0
        self.b_player = StringVar()
        self.b_player.set("H")
        self.r_player = StringVar()
        self.r_player.set("H")
        self.current_player = self.b_player
        self.isOver = False
        self.Rec = Recorder(self)
    
    def GetButtonInfo(self, button, c_t, current_turn_text, b_p, r_p, CO):
        self.computer_player = CO
        self.button = button
        self.c_t = c_t
        self.current_turn_text = current_turn_text
        self.b_p = b_p
        self.r_p = r_p
    
    def NewGame(self, GUI, button, c_t, b_p, r_p):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                    self.board[i][j] = " "
                    button[i][j].config(state = ACTIVE, text = " ", bg="white")
        self.turn = 0
        self.blue_points = 0
        self.red_points = 0
        c_t.set("Blue")
        if self.curr_gamemode == self.gen_game:
            b_p.config(text="Points: 0")
            r_p.config(text="Points: 0")
        self.current_player = self.b_player
        self.isOver = False
        self.Rec.NewRec()
        if self.current_player.get() == "C":
            self.computer_player.PlayMove(GUI, button,  c_t, self.current_turn_text, b_p, r_p)
    
    def NewSimpleGame(self, GUI, option, b_p, r_p):
        c_t = StringVar()
        option.set("Simple game")
        self.curr_gamemode = self.sim_game
        b_p.config(text="")
        r_p.config(text="")
        self.prompt_up = False
        self.ng_or_oc = 1
        self.NewGame(GUI, self.button, self.c_t, b_p, r_p)
        self.prompt.destroy()
        
        
    def Obstacles(self, GUI, option, b_p, r_p):
        self.turn = 0
        self.blue_points = 0
        self.red_points = 0
        option.set("Simple game")
        self.curr_gamemode = self.sim_game
        b_p.config(text="")
        r_p.config(text="")
        self.Rec.NewRec()
        x = StringVar()
        ct = StringVar()
        ct.set("Blue")
        x.set("X")
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                    if self.board[i][j] != " ":
                        self.board[i][j] = "X"
                        self.button[i][j].config(text="X", bg="black")
                        self.Rec.RecordAction(i, j, self.c_t, x, x, self.blue_points, self.red_points)
        self.c_t.set("Blue")
        self.isOver = False
        
        self.current_player = self.b_player
        if self.current_player.get() == "C":
            self.computer_player.PlayMove(GUI, self.button,  self.c_t, self.current_turn_text, b_p, r_p)
            
        self.ng_or_oc = 2
        self.prompt_up = False
        self.prompt.destroy()
        
    def CreatePromptWindow(self, GUI, option, b_p, r_p):
        self.prompt_up = True
        self.prompt = Toplevel(GUI)
        screen_width = self.prompt.winfo_screenwidth()  # Width of the screen
        screen_height = self.prompt.winfo_screenheight() # Height of the screen
         
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (300/2)
        y = (screen_height/2) - (150/2)
         
        self.prompt.geometry('%dx%d+%d+%d' % (300, 150, x, y))
        self.prompt.resizable(False, False)
        self.prompt.title("Simple Problem!")
        
        
        problem = Label(self.prompt, text = "Game no longer follows the simple rules!\nYou can either create a New Game,\nor replace occupied cells into obstacles.", justify = 'center')
        problem.place(x = 150, y = 5, anchor=CENTER)
        
        remember_prompt = Checkbutton(self.prompt, text='Stop Prompt Pop-up and remember answer', variable=self.prompt_sg)
        remember_prompt.place(x = 20, y = 75)
        
        ng = partial(self.NewSimpleGame, GUI, option, b_p, r_p)
        new_game = Button(self.prompt, bd = 2, height=1, width=10, text="New Game", command=ng, relief=RAISED, bg="white")
        new_game.place(x = 20, y = 125)
        
        oc = partial(self.Obstacles, GUI, option, b_p, r_p)
        obstacles_game = Button(self.prompt, bd = 2, height=1, width=10, text="Obstacles", command=oc, relief=RAISED, bg="white")
        obstacles_game.place(x = 280, y = 125, anchor=NE)
        
        
        
    def GameModeChange(self, GUI, option, b_p, r_p):
        if option.get() != self.curr_gamemode.name:
            if self.curr_gamemode.name == "Simple game":
                if self.is_point == True and self.turn < len(self.board[0]) * len(self.board) - 1:
                    self.curr_gamemode = self.gen_game
                    self.is_point = False
                    for i in range(len(self.board)):
                        for j in range(len(self.board[0])):
                                self.button[i][j].config(state = ACTIVE)
                    if self.current_turn == "Blue":
                        self.current_player = self.b_player
                        self.blue_points = self.curr_gamemode.ExtraPointCheck(GUI, self.lastx, self.lasty, self.button, self.current_turn)
                    else:
                        self.current_player = self.r_player
                        self.red_points = self.curr_gamemode.ExtraPointCheck(GUI, self.lastx, self.lasty, self.button, self.current_turn)
                    b_p.config(text="Points: " + str(self.blue_points))
                    r_p.config(text="Points: " + str(self.red_points))
                    self.isOver = False
                    
                    if self.current_player.get() == "C":
                        self.computer_player.PlayMove(GUI, self.button,  self.c_t, self.current_turn_text, b_p, r_p)
                else:
                    b_p.config(text="Points: " + str(self.blue_points))
                    r_p.config(text="Points: " + str(self.red_points))
                    self.curr_gamemode = self.gen_game
                
                
            else:
                
                if self.blue_points == 0 and self.red_points == 0:
                    self.curr_gamemode = self.sim_game
                    b_p.config(text="")
                    r_p.config(text="")
                else:
                    #prompt for new game or same game-state replaced with obstacles
                    if self.prompt_sg.get() == 0 and self.prompt_up == False:
                        self.CreatePromptWindow(GUI, option, b_p, r_p)
                    elif self.prompt_sg.get() == 1:
                        if self.ng_or_oc == 1:
                            self.NewSimpleGame(GUI, option, b_p, r_p)
                            option.set("Simple game")
                            self.curr_gamemode = self.sim_game
                        else:
                            self.Obstacles(GUI, option, b_p, r_p)
                            option.set("Simple game")
                            self.curr_gamemode = self.sim_game
                    option.set(self.curr_gamemode.name)
                
        
    def CheckPoint(self, GUI, x, y, c_t, button):
        x_bound = len(self.board) - 1
        y_bound = len(self.board[0]) - 1
        w_color = c_t.get().lower()
        if self.board[x][y] == "S":
            #check all of adjacent spaces for O's
            #leaving 200s and 50s for test
            if x+1 <= x_bound and self.board[x+1][y] == "O" and x+2 <= x_bound and self.board[x+2][y] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y].config(bg=w_color)
                button[x+2][y].config(bg=w_color)
                return True
            elif x-1 >= 0 and self.board[x-1][y] == "O" and x-2 >= 0 and self.board[x-2][y] == "S":
                button[x][y].config(bg=w_color)
                button[x-1][y].config(bg=w_color)
                button[x-2][y].config(bg=w_color)
                return True
            elif x+1 <= x_bound and y+1 <= y_bound and  self.board[x+1][y+1] == "O" and x+2 <= x_bound and y+2 <= y_bound and self.board[x+2][y+2] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y+1].config(bg=w_color)
                button[x+2][y+2].config(bg=w_color)
                return True
            elif y+1 <= y_bound and self.board[x][y+1] == "O" and y+2 <= y_bound and self.board[x][y+2] == "S":
                button[x][y].config(bg=w_color)
                button[x][y+1].config(bg=w_color)
                button[x][y+2].config(bg=w_color)
                return True
            elif y-1 >= 0 and self.board[x][y-1] == "O" and y-2 >= 0 and self.board[x][y-2] == "S":
                button[x][y].config(bg=w_color)
                button[x][y-1].config(bg=w_color)
                button[x][y-2].config(bg=w_color)
                return True
            elif x-1 >= 0 and y-1 >= 0 and self.board[x-1][y-1] == "O" and x-2 >= 0 and y-2 >= 0 and self.board[x-2][y-2] == "S":
                button[x][y].config(bg=w_color)
                button[x-1][y-1].config(bg=w_color)
                button[x-2][y-2].config(bg=w_color)
                return True
            elif x+1 <= x_bound and y-1 >= 0 and self.board[x+1][y-1] == "O" and x+2 <= x_bound and y-2 >= 0 and self.board[x+2][y-2] == "S":
                
                button[x][y].config(bg=w_color)
                button[x+1][y-1].config(bg=w_color)
                button[x+2][y-2].config(bg=w_color)
                return True
            elif x-1 >= 0 and y+1 <= y_bound and self.board[x-1][y+1] == "O" and x-2 >= 0 and y+2 <= y_bound and self.board[x-2][y+2] == "S":
                button[x][y].config(bg=w_color)
                button[x-1][y+1].config(bg=w_color)
                button[x-2][y+2].config(bg=w_color)
                return True
        elif self.board[x][y] == "O":
            #check half of all adjecent spaces for S's since no need to check other half until check is true
            if x+1 <= x_bound and self.board[x+1][y] == "S" and x-1 >= 0 and self.board[x-1][y] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y].config(bg=w_color)
                button[x-1][y].config(bg=w_color)
                return True
            elif y+1 <= y_bound and self.board[x][y+1] == "S" and y-1 >= 0 and self.board[x][y-1] == "S":
                button[x][y].config(bg=w_color)
                button[x][y+1].config(bg=w_color)
                button[x][y-1].config(bg=w_color)
                return True
            elif x+1 <= x_bound and y+1 <= y_bound and self.board[x+1][y+1] == "S" and x-1 >= 0 and y-1 >= 0 and self.board[x-1][y-1] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y+1].config(bg=w_color)
                button[x-1][y-1].config(bg=w_color)
                return True
            elif x-1 >= 0 and y+1 <= y_bound and self.board[x-1][y+1] == "S" and x+1 <= x_bound and y-1 >= 0 and self.board[x+1][y-1] == "S":
                button[x][y].config(bg=w_color)
                button[x+1][y-1].config(bg=w_color)
                button[x-1][y+1].config(bg=w_color)
                return True
        return False
    
    def GetTurn(self, x, y, b_s, r_s, GUI, button,  c_t, current_turn_text, b_p, r_p):
        if self.board[x][y] == " ":
            self.lastx = x
            self.lasty = y
            self.current_turn = c_t.get()
            if self.current_turn == "Blue":
                button[x][y].config(text=b_s.get(), bg="cyan")#color for test/distinction
                self.board[x][y] = b_s.get()
                self.is_point = self.CheckPoint(GUI, x, y, c_t, button)
                c_t.set("Red")
                self.current_player = self.r_player
            else:
                button[x][y].config(text=r_s.get(), bg="pink")
                self.board[x][y] = r_s.get()
                self.is_point = self.CheckPoint(GUI, x, y, c_t, button)
                c_t.set("Blue")  
                self.current_player = self.b_player
            
            availableMoves = 0
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                        if self.board[i][j] == " ":
                            availableMoves += 1
            
            
            
            if self.is_point == True:
                self.curr_gamemode.PointGive(self.current_turn, x, y, b_s, r_s, GUI, button, current_turn_text, b_p, r_p, c_t)
                
            self.Rec.RecordAction(x, y, self.current_turn, b_s, r_s, self.blue_points, self.red_points)
            if availableMoves == 0 or self.isOver == True:
                for i in range(len(self.board)):
                    for j in range(len(self.board[0])):
                            button[i][j].config(state = DISABLED)
                current_turn_text.config(text="Draw")
                if self.blue_points == self.red_points:
                    current_turn_text.config(text="Draw")
                elif self.blue_points > self.red_points:
                    current_turn_text.config(text="Winner is Blue by " + str(self.blue_points - self.red_points) + " points!!")
                elif self.blue_points < self.red_points:
                    current_turn_text.config(text="Winner is Red by " + str(self.red_points - self.blue_points) + " points!!")
                self.isOver = True
            else:
                self.turn += 1
                current_turn_text.config(text="Current turn: " + c_t.get())
            if self.current_player.get() == "C" and self.isOver == False:
                self.computer_player.PlayMove(GUI, button,  c_t, current_turn_text, b_p, r_p)
            


    def ResizeGame(self, GUI, brd_int):
        board_int = IntVar()
        if brd_int is None:
            board_int.set(8)
        else:
            board_int.set(brd_int)
        tempbrd = self.board
        self.board = []
        for i in range(board_int.get()):
            self.board.append(i)
            self.board[i] = []
            for j in range(board_int.get()):
                self.board[i].append(" ")
        self.turn = 0
        for i in range(min(len(tempbrd), len(self.board))-1):
            for j in range(min(len(tempbrd[0]), len(self.board[0]))-1):
                    self.board[i][j] = tempbrd[i][j]
                    if self.board[i][j] != " ":
                        self.turn += 1
        if self.current_player.get() == "C":
            self.computer_player.PlayMove(GUI, self.button,  self.c_t, self.current_turn_text, self.b_p, self.r_p)