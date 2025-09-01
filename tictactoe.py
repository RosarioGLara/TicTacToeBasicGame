import random 

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board
def printboard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])
#Take player input and put it on the board.
def playerInput(board):
    inp = int(input('Enter a number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('Choose another position')
    
# check if it win or tie
def check_horizontal(board): 
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True, currentPlayer
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True, currentPlayer
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True, currentPlayer
    return False, currentPlayer

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True, currentPlayer
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True, currentPlayer
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True, currentPlayer
    return False, currentPlayer

def check_diagonal(board):
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True, currentPlayer
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True, currentPlayer
    return False, currentPlayer

def check_tie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print('it is a tie')
        gameRunning = False

def checkWin(board, gameRunning):
    if check_diagonal(board)[0] or check_horizontal(board)[0] or check_vertical(board)[0]:
        print(f"The winner is {check_diagonal(board)[1]}" )
        gameRunning = False
    return gameRunning
# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

# check for win or tie again.
def computer(board):
    while currentPlayer == 'O':
        position = random.randint(0,8)
        if board[position] == '-':
            board[position] = 'O'
            switchPlayer()
while gameRunning:
    printboard(board)
    playerInput(board)
    gameRunning = checkWin(board, gameRunning)
    check_tie(board)
    switchPlayer()
    computer(board)
    gameRunning = checkWin(board, gameRunning)
    check_tie(board)
printboard(board)



