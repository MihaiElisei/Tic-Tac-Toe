import random

print('Welcome to Tic Tac Toe!')
name = input('What is your name?\n')
print(f'Welcome {name} and good luck!')


def boardLayout(board): #prints out the board
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

#Player choose letter X or O
def playerSymbol():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to play with X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O'] #Player have X and computer O
    else:
        return ['O', 'X'] #Computer have X and player O

#Choose random who makes the first move
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else: 
        return 'player'

#returns True if the player wants to play again, otherwise it returns False.
def replay():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter

#check if there is a winner
def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or #  left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or #  middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or #  right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

#Make a list with the copy of the board 
def getBoardCopy(board):
    copyBoard = []
    for i in board:
        copyBoard.append(i)
    return copyBoard

#checks if the space on the board is still empty
def isSpaceFree(board, move):
    return board[move] == ' '

#inputs  for player moves, transformed to integers
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? Choose a empty spot!(1-9)')
        move = input()
    return int(move)

#checks if there are valid moves and append them to a list,  returns a valid move from th move list
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#function for computer moves and logic of computer moves
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #Computer Checks if the player could win on their next move, and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    #Select corners if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #Select the center if is free
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

# Return True if every space on the board has been taken. Otherwise return False.
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True  

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = playerSymbol()
    turn = whoGoesFirst()
    print('The ' + turn + ' will make the first move.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            boardLayout(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                boardLayout(theBoard)
                print('Congratulations! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    boardLayout(theBoard)
                    print('Is a tie! Please try again!')
                    break
                else:
                    turn = 'computer'
        
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                boardLayout(theBoard)
                print('You lost. Please try again!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    boardLayout(theBoard)
                    print('Is a tie! Please try again!')
                    break
                else:
                    turn = 'player'
    if not replay():
        break
