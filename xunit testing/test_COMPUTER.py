from GUI import CreateGame
from GUI import ResizeBoard
import tkinter
from tkinter import *
from GameLogic import GameBoard


from COMPUTER import ComputerPlayer

def test_CPUBlue():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    GL.b_player.set("C")
    CreateGame(GUI, board_int, GL, CO)
    
    unVacant = 0
    
    for i in range(len(GL.board)):
        for j in range(len(GL.board[0])):
                if GL.board[i][j] != " ":
                    unVacant += 1
    assert unVacant == 1

def test_CPURed():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    
    CreateGame(GUI, board_int, GL, CO)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Blue")
    button = []
    current_turn_text = Label(GUI,
                          text = "Current turn: " + c_t.get())
    for i in range(board_int.get()):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(board_int.get()):
            n = j
            button[i].append(j)
            button[i][j] = Button(text=" ")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    unVacant = 0
    GL.b_player.set("H")
    GL.r_player.set("C")
    GL.GetTurn(5, 5, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    
    for i in range(len(GL.board)):
        for j in range(len(GL.board[0])):
                if GL.board[i][j] != " ":
                    unVacant += 1
                    print(i,j)
    assert unVacant == 3
    
def test_CPULevel():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    GL.b_player.set("C")
    CreateGame(GUI, board_int, GL, CO)
    
    CO.humanity.set(.9)
    CO.ha.set(.9)
    
def test_CPUBlueRedSimple():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    
    
    CreateGame(GUI, board_int, GL, CO)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Blue")
    button = []
    current_turn_text = Label(GUI,
                          text = "Current turn: " + c_t.get())
    for i in range(board_int.get()):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(board_int.get()):
            n = j
            button[i].append(j)
            button[i][j] = Button(text=" ")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    unVacant = 0
    GL.b_player.set("C")
    GL.r_player.set("C")
    GL.NewGame(GUI, button)
    for i in range(len(GL.board)):
        for j in range(len(GL.board[0])):
                if GL.board[i][j] != " ":
                    unVacant += 1
                    print(i,j)
    assert GL.isOver == True
    
def test_CPUBlueRedGeneral():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    
    
    CreateGame(GUI, board_int, GL, CO)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Blue")
    button = []
    current_turn_text = Label(GUI,
                          text = "Current turn: " + c_t.get())
    for i in range(board_int.get()):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(board_int.get()):
            n = j
            button[i].append(j)
            button[i][j] = Button(text=" ")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    unVacant = 0
    option = StringVar()
    option.set("General game")
    GL.GameModeChange(GUI, option, 0, 0)
    GL.b_player.set("C")
    GL.r_player.set("C")
    GL.NewGame(GUI, button)
    for i in range(len(GL.board)):
        for j in range(len(GL.board[0])):
                if GL.board[i][j] != " ":
                    unVacant += 1
                    print(i,j)
    assert unVacant == len(GL.board) * len(GL.board[0])
    

def test_CPUBlueRedSimpleGeneral():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    
    
    CreateGame(GUI, board_int, GL, CO)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Blue")
    button = []
    current_turn_text = Label(GUI,
                          text = "Current turn: " + c_t.get())
    for i in range(board_int.get()):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(board_int.get()):
            n = j
            button[i].append(j)
            button[i][j] = Button(text=" ")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    unVacant = 0
    GL.b_player.set("C")
    GL.r_player.set("C")
    GL.NewGame(GUI, button)
    option = StringVar()
    option.set("General game")
    GL.GameModeChange(GUI, option, 0, 0)
    for i in range(len(GL.board)):
        for j in range(len(GL.board[0])):
                if GL.board[i][j] != " ":
                    unVacant += 1
                    print(i,j)
    assert GL.isOver == True
