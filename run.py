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

