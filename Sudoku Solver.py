
import random, requests, bs4, os, re



testBoard = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def stringToBoard(string):
    listString = list(string)
    board = []
    for i in range(9):
        board += [listString[i*9 : (i*9)+9]]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                board[i][j] = '0'
            board[i][j] = int(board[i][j])
    return board


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('------------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end = '')
            if j == 8:
                print((board[i][j]))
            else:
                print(str(board[i][j]) + ' ', end= '')

def checkEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    else:
        return None

def checkValid(board,num,pos):
     ## Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    ## Check coloumn
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    ## Check grid

    gridX = pos[1] // 3
    gridY = pos[0] // 3

    for i in range(gridX * 3 , gridX * 3 + 3): # top row of grid (along the x axis)
        for j in range(gridY * 3, gridY * 3 + 3): # down the column of the grid (y axis)
            if board[j][i] == num:
                return False
    else:
        return True



def solve(board):
    find = checkEmpty(board)
    if not find: ## If it cant find an empty square. It must mean that it is solved.
        return True
    else:
        row, col = find ## Takes on next empty square

    for i in range(1,10): ## Runs through numbers 1-9
        if checkValid(board, i, (row, col)):
            board[row][col] = i ## If the number is valid, the number takes the spot of that square
            if solve(board):
                return True
            else:
                board[row][col] = 0 ## If the number is valid, it changes it back to a zero and runs back through the previous square with the next valid number and so on..
    return False

def getRandomPuzzle():
    url = 'http://magictour.free.fr/msk_009'
    res = requests.get(url)
    res.raise_for_status()
    puzzleFinder = re.compile(r'((\d|[.]){81})')
    puzzleList = puzzleFinder.findall(res.text)
    puzzleMatch = puzzleFinder.search(puzzleList[random.randint(0,len(puzzleList))][0]) # searches a list of tuples. The first tuple being the one we want to search. [1] position tuple is not needed
    puzzle = puzzleMatch.group()
    return puzzle

stringPuzzle = getRandomPuzzle() ## Gets a random puzzle from the internet

puzzle = stringToBoard(stringPuzzle) ## Converts it into useable data

def wholeThing(board):

    print('Here is the puzzle before it was solved...\n')
    printBoard(board)
    print('\n')
    print('Solving...\n')
    solve(board)
    print('Solved!\n')
    printBoard(board)



wholeThing(puzzle)