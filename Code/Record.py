import tkinter as tk
from tkinter import *
from functools import partial
from datetime import datetime
import os
import csv
import pandas as pd

class Recorder():
    def __init__(self, GL):
        self.GL = GL
        now = datetime.now()
        path = os.getcwd()
        time = now.strftime(' %Y,%m-%d %H.%M.%S')
        self.file_name = path + '\\Highlight\\rec' + time + '.csv'
        #self.file_record = open("Highlight/" + self.file_name + ".txt", "w")
        self.file_data = [] 
        self.record_data = []
        """with open(self.file_name, 'w') as file:
            file_record = csv.writer(file)
            file_record.writerow(["x", "y", "state", "turn", "Blue Points", "Red Points"])
            file_record.writerow([str(len(self.GL.board)), str(len(self.GL.board[0])), "state", "turn", 0, 0])"""
        self.prompt_up = False
        self.isRep = False
        self.isSaved = False
        self.moves = 0
        
    
    def NewRec(self):
        self.isSaved = False
        self.record_data = []
            
    def SaveReplay(self):
        if self.isSaved == False and len(self.record_data) > 0:
            with open(self.file_name, 'w') as file:
                self.isSaved = True
                file_record = csv.writer(file)
                file_record.writerow(["x", "y", "state", "turn", "Blue Points", "Red Points"])
                file_record.writerow([str(len(self.GL.board)), str(len(self.GL.board[0])), "state", "turn", 0, 0])
                for data in self.record_data:
                    x, y, state, c_t, blue_points, red_points = data
                    file_record.writerow([x, y, state, c_t, blue_points, red_points])
                    
    def UpdateSaveReplay(self, x, y, state, c_t, blue_points, red_points):
        with open(self.file_name, 'a') as file:
            file_record = csv.writer(file)
            file_record.writerow([x, y, state, c_t, blue_points, red_points])
            
            
    def RecordAction(self, x, y, c_t, b_s, r_s, blue_points, red_points):
        if self.isRep == False:
            state = b_s.get()
            if c_t == "Blue":
                state = b_s.get()
            elif c_t == "Red":
                state = r_s.get()
            self.record_data.append([x, y, state, c_t, blue_points, red_points])
            if self.isSaved == True:
                self.UpdateSaveReplay(x, y, state, c_t, blue_points, red_points)
    def RewindAction(self):
        
        x = int(self.file_data.iloc[self.moves][0])
        y = int(self.file_data.iloc[self.moves][1])
        
        self.GL.board[x][y] = " "
        
        self.button[x][y].config(text = " ", bg="white")
        
        self.moves -= 1
        
        self.b_p.config(text="Points: " + str(self.file_data.iloc[self.moves][4]))
        self.GL.blue_points = int(self.file_data.iloc[self.moves][4])
        self.r_p.config(text="Points: " + str(self.file_data.iloc[self.moves][5]))
        self.GL.red_points = int(self.file_data.iloc[self.moves][5])
        print(self.moves, self.turns_available)
        self.do_btn.place(x = self.board_s_x/2 + 25, y = 18, anchor=W)
        self.GL.isOver = False
        if self.moves == 0:
            self.undo_btn.place_forget()
    
    def ReplayAction(self):
        self.moves += 1
        self.undo_btn.place(x = self.board_s_x/2 - 25, y = 18, anchor=E)
        print(self.moves, self.turns_available)
        if self.moves <= self.turns_available:
            x = int(self.file_data.iloc[self.moves][0])
            y = int(self.file_data.iloc[self.moves][1])
            
            c_t = self.file_data.iloc[self.moves][3]
            
            
            
            state = StringVar()
            state.set(self.file_data.iloc[self.moves][2])
            current_turn = StringVar()
            current_turn.set(c_t)
            if self.moves == self.turns_available:
                self.GL.isOver = True
                self.do_btn.place_forget()
            self.GL.GetTurn(x, y, state, state, self.GUI, self.button,  current_turn, self.current_turn_text, self.b_p, self.r_p)
            self.b_p.config(text="Points: " + str(self.file_data.iloc[self.moves][4]))
            self.r_p.config(text="Points: " + str(self.file_data.iloc[self.moves][5]))
            
        
        
        
    def ReplayGame(self, GUI, v, GUIArray):
        self.prompt.destroy()
        self.prompt_up = False
        
        self.GL.isOver = False
        path = os.getcwd()
        self.file_data = pd.read_csv(path + '\\Highlight\\' + v.get(), skipinitialspace=True)
        
        self.board_s_x = 375 + int(self.file_data.iloc[0][0])* 24
        self.board_s_y = 85 + int(self.file_data.iloc[0][0])* 26
        
        self.turns_available = len(self.file_data) - 1
        
        GUIArray[0].config(text="Points: 0")
        GUIArray[1].config(text="Points: 0")
        GUIArray[2].place_forget()
        GUIArray[3].place_forget()
        GUIArray[4].config(text=" ")
        GUIArray[5].pack_forget()
        GUIArray[6].config(text="Blue")
        GUIArray[7].place_forget()
        GUIArray[8].place_forget()
        GUIArray[9].config(text="Red")
        GUIArray[10].place_forget()
        GUIArray[11].place_forget()
        for i in range(len(self.GL.board)):
            for j in range(len(self.GL.board[0])):
                    GUIArray[13][i][j].place_forget()
                    self.GL.board[i][j] = " "
        self.GL.ResizeGame(GUI, int(self.file_data.iloc[0][0]))
        GUIArray[13] = []
        for i in range(int(self.file_data.iloc[0][0])):
            GUIArray[13].append(i)
            GUIArray[13][i] = []
            for j in range(int(self.file_data.iloc[0][1])):
                GUIArray[13][i].append(j)
                GUIArray[13][i][j] = Button(
                    GUI, bd = 2, height=1, width=2, text=" ", command=None, relief=RAISED, bg="white")
                GUIArray[13][i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
        
        
        self.moves = 0
        
        self.b_p = GUIArray[0]
        self.r_p = GUIArray[1]
        self.current_turn_text = GUIArray[11]
        self.button = GUIArray[13]
        self.GUI = GUI
        self.original_option = GUIArray[16]
        option = StringVar()
        option.set("General game")
        
        self.GL.GameModeChange(GUI, option, self.b_p, self.r_p)
        
        self.GL.b_player.set("H")
        self.GL.r_player.set("H")
        
        for i in range (len(self.file_data) - 1):
            if self.file_data.iloc[i][2] == "X":
                x = self.file_data.iloc[i][0]
                y = self.file_data.iloc[i][1]
                self.GL.board[x][y] = "X"
                GUIArray[13][x][y].config(text="X", bg="black")
                
        
        
        
        self.resizeFunc = GUIArray[15]
        
       
        
        un = partial(self.RewindAction)
        do = partial(self.ReplayAction)
        rsz = partial(self.ReplayCancel, GUI)
        org = partial(self.OpenRecPrompt, GUI, GUIArray)
        if self.isRep == False:
            self.undo_btn = Button(GUI, bd = 2, height=1, width=3, text="<<", command= un, relief=RAISED, bg="grey")
            self.do_btn = Button(GUI, bd = 2, height=1, width=3, text=">>", command= do, relief=RAISED, bg="grey")
            menubar = Menu(GUI)
            rec = Menu(menubar, tearoff = 0) 
            
            
            menubar.add_cascade(label ='Record', menu = rec)
            rec.add_command(label ='Open Replay', command = org)
            rec.add_command(label ='Stop Replay', command = rsz)
        self.isRep = True
        
        
        self.undo_btn.place_forget()
        self.do_btn.place(x = self.board_s_x/2 + 25, y = 18, anchor=W)
        GUI.config(menu=menubar)
        
        
    def ReplayCancel(self, GUI):
        self.GL.GameModeChange(GUI, self.original_option, self.b_p, self.r_p)
        for i in range(len(self.GL.board)):
            for j in range(len(self.GL.board[0])):
                    self.GL.board[i][j] = " "
        self.isRep = False
        self.GL.isOver = False
        self.resizeFunc()
        
    def OpenRecPrompt(self, GUI, GUIArray):
        if self.prompt_up == False:
            path = os.getcwd()
            self.page_num = 0
            values = list(reversed(os.listdir(path + '\\Highlight')))
            self.prompt_up = True
            self.prompt = Toplevel(GUI)
            
            screen_width = self.prompt.winfo_screenwidth()  # Width of the screen
            screen_height = self.prompt.winfo_screenheight() # Height of the screen
             
            # Calculate Starting X and Y coordinates for Window
            x = (screen_width/2) - (300/2)
            y = (screen_height/2) - (175/2)
             
            self.prompt.geometry('%dx%d+%d+%d' % (300, 175, x, y))
            self.prompt.resizable(False, False)
            self.prompt.title("Computer Player")
            
            
            v = StringVar(self.prompt, values[0])
             
            # Loop is used to create multiple Radiobuttons
            # rather than creating each button separately
            self.buttons = []
            for i in range(5):
                if i < len(values):
                    self.buttons.append(i)
                    self.buttons[i] = Radiobutton(self.prompt, text = values[i], variable = v, 
                                                   value = values[i])
                    self.buttons[i].pack(side = TOP,expand = False, fill = BOTH)
            
            
            self.prompt.bind("<Destroy>", lambda event: self.PromptClose())
            
            
            pre = partial(self.RefreshPrompt, -1, values)
            self.prev_btn = Button(self.prompt, bd = 2, height=1, width=3, text="<<", command= pre, relief=RAISED, bg="white")
            
            nex = partial(self.RefreshPrompt, +1, values)
            self.next_btn = Button(self.prompt, bd = 2, height=1, width=3, text=">>", command= nex, relief=RAISED, bg="white")
            
            
            if len(values) > 5:
                self.next_btn.place(x = 300/2 + 50, y = 155, anchor=W)
            
            rg = partial(self.ReplayGame, GUI, v, GUIArray)
            
            replay_btn = Button(self.prompt, bd = 2, height=1, width=10, text="Replay", command= rg, relief=RAISED, bg="white")
            replay_btn.place(x = 300/2, y = 155, anchor=CENTER)
    
    
    
    def RefreshPrompt(self, page_num, values):
        self.page_num += page_num
        for i in range(5):
            if i + self.page_num * 5 < len(values):
                self.buttons[i].config(text = values[i + self.page_num * 5],
                                               value = values[i + self.page_num * 5])
                self.buttons[i].pack(side = TOP,expand = False, fill = BOTH)
            else:
                self.buttons[i].place_forget()
                
        if ((self.page_num + 1) * 5) < len(values):
            self.next_btn.place(x = 300/2 + 50, y = 155, anchor=W)
        else:
            self.next_btn.place_forget()
            
        if (self.page_num - 1) * 5 >= 0:
            self.prev_btn.place(x = 300/2 - 50, y = 155, anchor=E)
        else:
            self.prev_btn.place_forget() 
            
    
    def PromptClose(self):
        self.prompt_up = False