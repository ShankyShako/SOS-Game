import GameLogic
from GUI import CreateGame
import tkinter
from tkinter import *
from GameLogic import GameBoard

from COMPUTER import ComputerPlayer


def test_gameboardcreations():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    
    CreateGame(GUI, board_int, GL, CO)
    TESTGL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    assert TESTGL.curr_gamemode.name == "Simple game"
def test_NewGame():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)

    CreateGame(GUI, board_int, GL, CO)
    button = []
    for i in range(board_int.get()):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(board_int.get()):
            n = j
            button[i].append(j)
            button[i][j] = Button(text="TEST")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    GL.NewGame(GUI, button)
def test_GameModeChange():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)

    CreateGame(GUI, board_int, GL, CO)
    option = StringVar()
    option.set("Simple game")
    GL.GameModeChange(GUI, option, 0, 0)
    assert GL.curr_gamemode.name == "Simple game"
def test_GameModeChange2():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)

    CreateGame(GUI, board_int, GL, CO)
    option = StringVar()
    option.set("General game")
    GL.GameModeChange(GUI, option, 0, 0)
    assert GL.curr_gamemode.name == "General game"
#occupied cell move
def test_GetTurn():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
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
            button[i][j] = Button(text="")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    CreateGame(GUI, board_int, GL, CO)
    GL.board[0][0] = "S"
    GL.GetTurn(0, 0, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert c_t.get() == "Blue"

    
#out of bounds move
def test_GetTurn2():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
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
    CreateGame(GUI, board_int, GL, CO)
    GL.GetTurn(9, 9, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert c_t.get() == "Blue"
#successful move
def test_GetTurn3():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
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
    CreateGame(GUI, board_int, GL, CO)
    GL.GetTurn(0, 0, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert c_t.get() == "Red"
#red side version
def test_GetTurn4():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Red")
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
            button[i][j] = Button(text="")
            button[i][j].place(x = 200 + i * 24, y = 50 + j*26 , anchor=CENTER)
    CreateGame(GUI, board_int, GL, CO)
    GL.board[0][0] = "O"
    GL.GetTurn(0, 0, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert c_t.get() == "Red"
    
def test_GetTurn5():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    GL.turn = 1
    c_t.set("Red")
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
    CreateGame(GUI, board_int, GL, CO)
    GL.GetTurn(9, 9, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert c_t.get() == "Red"
    
def test_GetTurn6():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Red")
    GL.turn = 1
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
    CreateGame(GUI, board_int, GL, CO)
    GL.GetTurn(0, 0, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert c_t.get() == "Blue"
def test_GetTurnWin():
    GUI = Tk() 
    board_int = IntVar()
    board_int.set(8)
    GL = GameBoard(board_int.get(), GUI)
    CO = ComputerPlayer(GL)
    b = StringVar()
    r = StringVar()
    c_t = StringVar()
    b.set("S")
    r.set("S")
    c_t.set("Red")
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
    GL.board[1][1] = "O"
    GL.board[2][2] = "S"
    CreateGame(GUI, board_int, GL, CO)
    GL.GetTurn(0, 0, b, r, GUI, button, c_t, current_turn_text, 0, 0)
    assert GL.is_point == True