import random
import tkinter
from tkinter import *
from functools import partial

class ComputerPlayer():
    def __init__(self, GL):
        self.prompt_up = False
        self.board = GL.board
        self.GL = GL
        self.bp = StringVar()
        self.rp = StringVar()
        
        self.blue_choice = StringVar()
        self.red_choice = StringVar()
        self.blue_choice.set("S")
        self.red_choice.set("S")
        
        self.humanity = DoubleVar()
        self.humanity.set(.5)
        self.ha = DoubleVar()
        self.ha.set(5)
        
    def GetGUIInfo(self, GUI, button, current_turn, current_turn_text, blue_points, red_points, GL):
        self.GUI = GUI
        self.button = button
        self.current_turn = current_turn
        self.current_turn_text = current_turn_text
        self.blue_points = blue_points
        self.red_points = red_points
        self.board = GL.board
        self.GL = GL

    def GetComputerPlayer(self, GUI, blue_s_btn, blue_o_btn, red_s_btn, red_o_btn, board_int, current_turn):
        if self.prompt_up == False:
            self.prompt_up = True
            self.prompt = Toplevel(GUI)
            current_turn = current_turn.get()
            
            
            screen_width = self.prompt.winfo_screenwidth()  # Width of the screen
            screen_height = self.prompt.winfo_screenheight() # Height of the screen
             
            # Calculate Starting X and Y coordinates for Window
            x = (screen_width/2) - (300/2)
            y = (screen_height/2) - (150/2)
             
            self.prompt.geometry('%dx%d+%d+%d' % (300, 150, x, y))
            self.prompt.resizable(False, False)
            self.prompt.title("Computer Player")
            
            
            self.bp = StringVar()
            self.rp = StringVar()
            
            
            if self.GL.b_player.get() == "H":
                self.bp.set("H")
            else:
                self.bp.set("C")
            
            if self.GL.r_player.get() == "H":
                self.rp.set("H")
            else:
                self.rp.set("C")
            self.ha.set(self.humanity.get())
            
            
            blue_player = Label(self.prompt,
                                  text='Blue Player').place(x=25, 
                                                      y=0)
                                                         
            blue_human = Radiobutton(self.prompt,
                                  text='Human', variable = self.bp,
                                 value = "H").place(x=25, 
                                                      y=25)
            blue_computer = Radiobutton(self.prompt,
                                  text='Computer',variable = self.bp,
                                 value = "C").place(x=25, 
                                                      y=50)
            
            red_human_txt = Label(self.prompt,
                                  text='Human').place(x=250, 
                                                      y=25, anchor=NE)
                                                      
            red_player = Label(self.prompt,
                                  text='Red Player').place(x=265, 
                                                      y=0, anchor=NE)
                                                      
            red_computer_txt = Label(self.prompt,
                                  text='Computer').place(x=250, 
                                                      y=50, anchor=NE)
                                                           
            red_human = Radiobutton(self.prompt, variable = self.rp,
                                 value = "H").place(x=275, 
                                                      y=25, anchor=NE)
            red_computer = Radiobutton(self.prompt,variable = self.rp,
                                 value = "C").place(x=275, 
                                                      y=50, anchor=NE)
            
            humanity_txt = Label(self.prompt, text = "Humanity").place(x = 300/2, y = 80, anchor=CENTER)                                        
                                                    
            humanity_set = Entry(self.prompt, textvariable = self.ha, 
                                 width = 5, justify = 'center').place(x = 300/2, y = 100, anchor=CENTER)
            self.prompt.bind("<Destroy>", lambda event: self.ConfirmPlayers(GUI, blue_s_btn, blue_o_btn, red_s_btn, red_o_btn, board_int, current_turn))
            sub = partial(self.ConfirmPlayers, GUI, blue_s_btn, blue_o_btn, red_s_btn, red_o_btn, board_int, current_turn)
            submit_btn = Button(self.prompt, bd = 2, height=1, width=10, text="Confirm", command=sub, relief=RAISED, bg="white")
            submit_btn.place(x = 300/2, y = 130, anchor=CENTER)
    
    def ConfirmPlayers(self, GUI, blue_s_btn, blue_o_btn, red_s_btn, red_o_btn, board_int, current_turn):
        
        if self.ha.get() >= 1 and self.ha.get() <= 9:
            self.humanity.set(self.ha.get() * 0.1)
        elif self.ha.get() > 0.1 and self.ha.get() < 1:
            self.humanity.set(self.ha.get())
        elif self.ha.get() >= 10 and self.ha.get() <= 99:
            self.humanity.set(self.ha.get() * 0.01)
        
        
        
            
        if self.prompt_up == True:
            self.prompt.unbind("<Destroy>")
            
            self.prompt_up = False
            
            self.GL.b_player.set(self.bp.get())
            self.GL.r_player.set(self.rp.get())
            
            
            
            self.prompt.destroy()
            
        if self.GL.b_player.get() == "H":    
            blue_s_btn.place(x=50, 
                             y=75)
            blue_o_btn.place(x=50, 
                             y=100)
            
        elif self.GL.b_player.get() == "C":
            blue_s_btn.place_forget()
            blue_o_btn.place_forget()
            
        if self.GL.r_player.get() == "H":                                                
            red_s_btn.place(x=250 + board_int* 24, 
                                                      y=75)
            red_o_btn.place(x=250 + board_int* 24, 
                                                      y=100)
            
        elif self.GL.r_player.get() == "C":
            red_s_btn.place_forget()
            red_o_btn.place_forget()
        
        if current_turn == "Blue" and self.GL.b_player.get() == "C":
            self.PlayMove(GUI, self.button,  current_turn, self.current_turn_text, self.blue_points, self.red_points)
        elif current_turn == "Red" and self.GL.r_player.get() == "C":
            self.PlayMove(GUI, self.button,  current_turn, self.current_turn_text, self.blue_points, self.red_points) 
        

    #def TrainAgent(self, env):
        
    def GenerateActions(self):
        actions = []
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == " ":
                    for character in ["S", "O"]:
                        actions.append([x, y, character])
        return actions
    
    def CheckWin(self, actions):
        
        x_bound = len(self.board) - 1
        y_bound = len(self.board[0]) - 1
        win_conditions = []
        for i in range(len(actions)):
            
            x, y, _ = actions[i]
            if x <= x_bound and y <= y_bound and x >= 0 and y >= 0:
                #repeats of the same win con to help highten the chance of getting more points
                if x+1 <= x_bound and self.board[x+1][y] == "O" and x+2 <= x_bound and self.board[x+2][y] == "S":
                    win_conditions.append([x, y, "S"])
                if x-1 >= 0 and self.board[x-1][y] == "O" and x-2 >= 0 and self.board[x-2][y] == "S":
                    win_conditions.append([x, y, "S"])
                if x+1 <= x_bound and y+1 <= y_bound and  self.board[x+1][y+1] == "O" and x+2 <= x_bound and y+2 <= y_bound and self.board[x+2][y+2] == "S":
                    win_conditions.append([x, y, "S"])
                if y+1 <= y_bound and self.board[x][y+1] == "O" and y+2 <= y_bound and self.board[x][y+2] == "S":
                    win_conditions.append([x, y, "S"])
                if y-1 >= 0 and self.board[x][y-1] == "O" and y-2 >= 0 and self.board[x][y-2] == "S":
                    win_conditions.append([x, y, "S"])
                if x-1 >= 0 and y-1 >= 0 and self.board[x-1][y-1] == "O" and x-2 >= 0 and y-2 >= 0 and self.board[x-2][y-2] == "S":
                    win_conditions.append([x, y, "S"])
                if x+1 <= x_bound and y-1 >= 0 and self.board[x+1][y-1] == "O" and x+2 <= x_bound and y-2 >= 0 and self.board[x+2][y-2] == "S":
                    win_conditions.append([x, y, "S"])
                if x-1 >= 0 and y+1 <= y_bound and self.board[x-1][y+1] == "O" and x-2 >= 0 and y+2 <= y_bound and self.board[x-2][y+2] == "S":
                    win_conditions.append([x, y, "S"])
                if x+1 <= x_bound and self.board[x+1][y] == "S" and x-1 >= 0 and self.board[x-1][y] == "S":
                    win_conditions.append([x, y, "O"])
                if y+1 <= y_bound and self.board[x][y+1] == "S" and y-1 >= 0 and self.board[x][y-1] == "S":
                    win_conditions.append([x, y, "O"])
                if x+1 <= x_bound and y+1 <= y_bound and self.board[x+1][y+1] == "S" and x-1 >= 0 and y-1 >= 0 and self.board[x-1][y-1] == "S":
                    win_conditions.append([x, y, "O"])
                if x-1 >= 0 and y+1 <= y_bound and self.board[x-1][y+1] == "S" and x+1 <= x_bound and y-1 >= 0 and self.board[x+1][y-1] == "S":
                    win_conditions.append([x, y, "O"])
        return win_conditions
    
    
    def Decision(self, actions):
        decision = False
        tries = 0
        TRY_LIMIT = 15
        while decision == False and tries <= int(self.humanity.get() * TRY_LIMIT):
            decision = True
            tries += 1
            x, y, state = random.choice(actions)
            if self.humanity.get() >= random.random():
                
                check_surrounds = [[x+1,y+1, 0],[x+1,y, 0],[x,y+1, 0],[x-1,y-1, 0],[x-1,y, 0],[x,y-1, 0],[x+1,y-1, 0],[x-1,y+1, 0], [x+2,y+2, 0],[x+2,y, 0],[x,y+2, 0],[x-2,y-1, 0],[x-2,y, 0],[x,y-2, 0],[x+2,y-2, 0],[x-2,y+2, 0]]
                    
                self.board[x][y] = state
                check_surrounds = self.CheckWin(check_surrounds)
                self.board[x][y] = " "
                if len(check_surrounds) != 0:
                    #print("aha! " + str(tries) + " " + str(check_surrounds))
                    decision = False
            #else:
                #print("nocheck")
            
        return x, y, state

    def PlayMove(self, GUI, button,  current_turn, current_turn_text, blue_points, red_points):
        actions = self.GenerateActions()
        CHECK_MINLIMIT = .1
        if len(actions) > 0:
            if (self.humanity.get() * 1 - CHECK_MINLIMIT) + CHECK_MINLIMIT >= random.random():
                win_array = self.CheckWin(actions)
                #print("checkWin")
                if len(win_array) == 0:
                    #print("noWin")
                    x, y, state = self.Decision(actions)
                else:
                    #print("WINNERRR")
                    x, y, state = random.choice(win_array)
            else:
                #print("norm")
                x, y, state = self.Decision(actions)
                    
            
            #if current_turn == "Blue":
            self.blue_choice.set(state)
            #elif current_turn == "Red":
            self.red_choice.set(state)
            self.GL.GetTurn(x, y, self.blue_choice, self.red_choice, GUI, button,  self.current_turn, current_turn_text, blue_points, red_points)