import os, random

clearBoard = [' ']*10
clearBoard[0] = '%'
winningBoard = list('%XOXOXOXOX')
drawBoard = list('%OXOXXOOOX')
def clear():
    os.system( 'cls' )

def printBoard(board):
    print(board[1],'|',board[2], '|', board[3])
    print('---------')
    print(board[4], '|', board[5], '|', board[6])
    print('---------')
    print(board[7], '|', board[8], '|', board[9])



def whoGoesFirst(): ## Returns 'Player one' or 'Player two'
    if random.randint(0,1) == 0:
        return 'Player one'
    else:
        return 'Player two'

def markerChoice():
    choice = ''
    while choice.upper() not in ['X','O']:
        choice = input('Player one please choose a marker... X or O')
    if choice.upper() == 'X':
        print('You have chosen X')
        return 'X','O'
    else:
        print('You have chosen O')
        return 'O','X'

def playerAssignment():
    player1,player2 = markerChoice()


# def checkIfSpaceEmpty(board,choice):
#     if board[choice] == ' ':
#         return True
#     else:
#         return False

def checkIfFull(board):
    for i, j in enumerate(board):
        if board[i] == ' ':
            return False
    return True

def checkWin(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def placeMarker(marker,board,player):
    choice = 0
    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or board[choice] != ' ':
        choice = int(input(f'Please choose your next move, {player}'))
        if choice == 0:
            print('Please choose another location for your marker')
    board[choice] = marker

gameOn = True

player1,player2 = markerChoice()
printBoard(clearBoard)
whosGo = 'Player one'#whoGoesFirst()
print(whosGo + ' you will go first')

while gameOn == True:

    while whosGo == 'Player one':
        placeMarker(player1, clearBoard,whosGo)
        printBoard(clearBoard)
        if checkWin(clearBoard,player1) == True:
            print(f'Congratulations, {whosGo} Wins!')
            gameOn = False
            break
        if checkIfFull(clearBoard) == True:
            print('It ended in a draw!')
            gameOn = False
            break
        else:
            whosGo = 'Player two'

    while whosGo == 'Player two':
        placeMarker(player2, clearBoard, whosGo)
        printBoard(clearBoard)
        if checkWin(clearBoard,player2) == True:
            print(f'Congratulations, {whosGo} Wins!')
            gameOn = False
        if checkIfFull(clearBoard) == True:
            print('It ended in a draw!')
            gameOn = False
        else:
            whosGo = 'Player one'