# ticTacToe.py
import pprint

theBoard = {'top-L': '　', 'top-M': '　', 'top-R': '　',
            'mid-L': '　', 'mid-M': '　', 'mid-R': '　',
            'low-L': '　', 'low-M': '　', 'low-R': '　'}

def printBoard(board):
    print(board['top-L'] + '｜' + board['top-M'] + '｜' + board['top-R'])
    print(u'－＋－＋－')
    print(board['mid-L'] + '｜' + board['mid-M'] + '｜' + board['mid-R'])
    print(u'－＋－＋－')
    print(board['low-L'] + '｜' + board['low-M'] + '｜' + board['low-R'])

turn = u'×'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == u'×':
        turn = u'○'
    else:
        turn = u'×'
printBoard(theBoard)
