import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
from GameLogic import GameBoard
from SETTINGS import Settings
from COMPUTER import ComputerPlayer

##possible color catching option
#from tkinter import ttk
#print(ttk.Style().lookup('TButton', 'background'))

def ResizeBoard(GL, GUI, board_int, brd_size):
    input_size = int(board_int.get())
    if input_size >= 5 and input_size <= 12 and input_size != brd_size:
        GL.ResizeGame(GUI, board_int.get())
        brd_size = IntVar()
        brd_size.set(board_int.get())
        GUI.destroy()
        
        GUI = Tk()
        GUI.eval('tk::PlaceWindow . center')
        CO = ComputerPlayer(GL)
        CreateGame(GUI, brd_size, GL, CO)

def CreateGame(GUI, brd_int, GL, CO):
    board_int = IntVar()
    if brd_int is None:
        board_int.set(9)
    else:
        board_int.set(brd_int.get())
    
    
    
    board_s_x = 375 + board_int.get()* 24
    board_s_y = 85 + board_int.get()* 26
    # Initialize tkinter window with dimensions with adjustable size based on board            
    screen_width = GUI.winfo_screenwidth()  # Width of the screen
    screen_height = GUI.winfo_screenheight() # Height of the screen
     
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (board_s_x/2)
    y = (screen_height/2) - (board_s_y/2)
     
    GUI.geometry('%dx%d+%d+%d' % (board_s_x, board_s_y, x, y))
    GUI.resizable(False, False)
    GUI.title('SOS Game')
    v = StringVar()
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    v.set("Simple game")
    b.set("S")
    r.set("S")
    c_t.set("Blue")
    button = []
    
    b_p = Label(GUI,
                      text = "")
    #b_p.place_forget()
    
    r_p = Label(GUI,
                          text="")
    #r_p.place_forget()
    
    b_p.place(x = 50,
                                   y = 125)
    r_p.place(x = 250 + board_int.get()* 24,
                                       y = 125)
        
    gmc = partial(GL.GameModeChange, GUI, v, b_p, r_p)
    rdbtn1 = Radiobutton(GUI,
                          text='Simple game', command=gmc, variable = v,
                         value = "Simple game")
    rdbtn1.place(x=board_s_x/2-5, y=10, anchor=NE)
    
    rdbtn2 = Radiobutton(GUI,
                          text='General game', command=gmc, variable = v,
                         value = "General game")
    rdbtn2.place(x=board_s_x/2+5, y=10, anchor=NW)


    board_size_text = Label(GUI,
                          text = "Board size").place(x = board_s_x - 110,
                                                   y = 10)

    board_size = Entry(GUI, textvariable = board_int,
                                 width = 5, justify='center')

    board_size.bind('<Return>', lambda event: ResizeBoard(GL, GUI, board_size, int(brd_int.get())))
    board_size.pack(padx = (325 + board_int.get()* 25, 10),
                                             pady = 10, expand=False)

    blue_p_text = Label(GUI,
                          text = "Blue player").place(x = 50,
                                                   y = 50)
    blue_s_btn = Radiobutton(GUI,
                          text='S', variable = b,
                         value = "S")
    blue_s_btn.pack()
    blue_o_btn = Radiobutton(GUI,
                          text='O',variable = b,
                         value = "O")
                                            
    blue_o_btn.pack()

    red_p_text = Label(GUI,
                          text = "Red player").place(x = 250 + board_int.get()* 24,
                                                   y = 50)
    red_s_btn = Radiobutton(GUI,
                          text='S', variable = r,
                         value = "S")
    red_s_btn.pack()
    red_o_btn = Radiobutton(GUI,
                          text='O',variable = r,
                         value = "O")
    red_o_btn.pack()
    
    
                                                     
    current_turn_text = Label(GUI,
                          text = "Current turn: " + c_t.get())
    current_turn_text.place(x = board_s_x/2, y = board_s_y-35, anchor=CENTER)
    
    for i in range(board_int.get()):
        button.append(i)
        button[i] = []
        for j in range(board_int.get()):
            button[i].append(j)
            get_t = partial(GL.GetTurn, i, j, b, r, GUI, button, c_t, current_turn_text, b_p, r_p)
            button[i][j] = Button(
                GUI, bd = 2, height=1, width=2, text=GL.board[i][j], command=get_t, relief=RAISED, bg="white")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
            
            
    gmc = partial(GL.GameModeChange, GUI, v, b_p, r_p)
    ng = partial(GL.NewGame, GUI, button, c_t, b_p, r_p)
    co = partial(CO.GetComputerPlayer, GUI, blue_s_btn, blue_o_btn, red_s_btn, red_o_btn, board_int.get(), c_t)

    menubar = Menu(GUI)
    game = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Game', menu = game)
    game.add_command(label ='New Game', command = ng)
    game.add_command(label ='Play Computer', command = co)
    
    ##TO BE ADDED
    #game.add_command(label ='Save Game', command = None)
    #game.add_command(label ='Replay Game', command = None)
    #game.add_command(label ='Open Replay', command = None)

    #settings = Menu(menubar, tearoff = 0) 
    #menubar.add_cascade(label ='Settings', menu = settings)
    #settings.add_command(label ='Auto Record: ' + "Off", command = None)
    #settings.add_command(label ='Auto Prompt: ' + "Off", command = None)
    #settings.add_command(label ='Highlight Last Move: ' + "Off", command = None)

    #help_s = Menu(menubar, tearoff = 0) 
    #menubar.add_cascade(label ='Help', menu = help_s)
    #help_s.add_command(label ='How To Play', command = None)
    
    #self.prompt.bind("<Destroy>", lambda event: self.DeleteGUI(CO))
    
    
    CO.GetGUIInfo(GUI, button, c_t, current_turn_text, b_p, r_p, GL)
    CO.ConfirmPlayers(GUI, blue_s_btn, blue_o_btn, red_s_btn, red_o_btn, board_int.get(), c_t.get())
    GL.GetButtonInfo(button, c_t, current_turn_text, b_p, r_p, CO)
    GUI.config(menu = menubar) 