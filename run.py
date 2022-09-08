import random

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