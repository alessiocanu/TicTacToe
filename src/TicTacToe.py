"""
Tic Tac Toe
"""
import PySimpleGUI as sg

board = {1: "-", 2: "-", 3: "-",
         4: "-", 5: "-", 6: "-",
         7: "-", 8: "-", 9: "-"}

gamefinished = False
correct = False


def print_board():
    """
    Function that prints the board on terminal
    """
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])


def set_player():
    """
    Function to change the symbol that needs to be used based on the player
    :return: the symbol (a single char)
    """
    if whoplays == 1:
        return "X"
    else:
        return "O"


def gameover():
    """
    Function to check if there are 3 equal symbols on the same row, column or diagonally
    :return: True or False
    """
    if board[1] == board[4] == board[7] and board[1] != "-" or board[2] == board[5] == board[8] and board[2] != "-" \
            or board[3] == board[6] == board[9] and board[3] != "-":
        return True
    else:
        if board[1] == board[2] == board[3] and board[1] != "-" or board[4] == board[5] == board[6] and board[4] != "-" \
                or board[7] == board[8] == board[9] and board[7] != "-":
            return True
        else:
            if board[1] == board[5] == board[9] and board[1] != "-" or board[3] == board[5] == board[7] and board[3] != "-":
                return True
            else:
                return False


# Layout and Window Setup
layout = [[sg.Text("", size=(30, 1), key="playturn")],
          [sg.Button("", size=(5, 2), key="1"), sg.Button("", size=(5, 2), key="2"), sg.Button("", size=(5, 2), key="3")],
          [sg.Button("", size=(5, 2), key="4"), sg.Button("", size=(5, 2), key="5"), sg.Button("", size=(5, 2), key="6")],
          [sg.Button("", size=(5, 2), key="7"), sg.Button("", size=(5, 2), key="8"), sg.Button("", size=(5, 2), key="9")],
          [sg.Text("", size=(30, 1), key="gamefinished")], [sg.Button("Sì", size=(3, 1), key="Si", visible=False),
                                                            sg.Button("No", size=(3, 1), key="No", visible=False)]]

window = sg.Window("Tic Tac Toe", layout, element_justification="center")

whoplays = 1
symbol = set_player()

while True and not gamefinished:
    event, values = window.read()

    while not correct:
        # Board events handler
        if event == "1":
            if board[1] == "-":
                window.FindElement("1").update(f"{symbol}")
                board[1] = {symbol}
                correct = True
            break
        if event == "2":
            if board[2] == "-":
                window.FindElement("2").update(f"{symbol}")
                board[2] = {symbol}
                correct = True
            break
        if event == "3":
            if board[3] == "-":
                window.FindElement("3").update(f"{symbol}")
                board[3] = {symbol}
                correct = True
            break
        if event == "4":
            if board[4] == "-":
                window.FindElement("4").update(f"{symbol}")
                board[4] = {symbol}
                correct = True
            break
        if event == "5":
            if board[5] == "-":
                window.FindElement("5").update(f"{symbol}")
                board[5] = {symbol}
                correct = True
            break
        if event == "6":
            if board[6] == "-":
                window.FindElement("6").update(f"{symbol}")
                board[6] = {symbol}
                correct = True
            break
        if event == "7":
            if board[7] == "-":
                window.FindElement("7").update(f"{symbol}")
                board[7] = {symbol}
                correct = True
            break
        if event == "8":
            if board[8] == "-":
                window.FindElement("8").update(f"{symbol}")
                board[8] = {symbol}
                correct = True
            break
        if event == "9":
            if board[9] == "-":
                window.FindElement("9").update(f"{symbol}")
                board[9] = {symbol}
                correct = True
            break
        if event == sg.WIN_CLOSED:
            break

    # If the turn was played correctly, change the player
    if event is not None:
        if whoplays == 1:
            whoplays = 2
        else:
            whoplays = 1
        symbol = set_player()
        gamefinished = gameover()
        correct = False
    else:
        break

    # If the game finishes, check for another game
    if gamefinished:
        window.FindElement("gamefinished").update("Vuoi rigiocare?", visible=True)
        window.FindElement("Si").update(visible=True)
        window.FindElement("No").update(visible=True)

        event, values = window.read()
        if event == "Si":
            gamefinished = False
            for i in board:
                board[i] = "-"
            for i in range(1, 10):
                window.FindElement(f"{i}").update("")
            window.FindElement("gamefinished").update(visible=False)
            window.FindElement("Si").update(visible=False)
            window.FindElement("No").update(visible=False)
        if event == "No":
            break

window.close()