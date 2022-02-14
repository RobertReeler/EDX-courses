"""
Tic Tac Toe Player
"""

from ast import Raise
import math
from operator import contains
from queue import Empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moveCount = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                moveCount+=1
    if moveCount % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possibleMoves.add((row,col))
    return possibleMoves

def copyBoard(board):
    tempBoard = initial_state()
    for row in range(3):
        for col in range(3):
            tempBoard[row][col] = board[row][col]
    return tempBoard


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tempBoard = copyBoard(board)
    if tempBoard[action[0]][action[1]] == EMPTY:
        tempBoard[action[0]][action[1]] = player(tempBoard)
        return tempBoard
    raise NotImplementedError

def bX(move):
    return move % 3

def bY(move):
    return math.trunc(move/3)

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winRows = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for check in winRows:
        if board[bX(check[0])][bY(check[0])] == board[bX(check[1])][bY(check[1])] and board[bX(check[0])][bY(check[0])] == board[bX(check[2])][bY(check[2])] and not board[bX(check[0])][bY(check[0])] == EMPTY:
            return board[bX(check[0])][bY(check[0])]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board) == None:
        return True
    if not actions(board):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winningPlayer = winner(board)
    if winningPlayer == X:
        return 1
    elif winningPlayer == O:
        return -1    
    return 0

def BestStep(board):
    whosTurn = player(board)
    if terminal(board):
        return utility(board)
    if whosTurn == X:
        bestActionScore = -2
    else: 
        bestActionScore = 2
    mypossibleMoves = actions(board)
    for consideredMove in mypossibleMoves:
        actionResult = BestStep(result(board,consideredMove))
        actionComapason = betterScore(whosTurn, actionResult, bestActionScore)
        if actionComapason == 2:
            return actionResult
        elif actionComapason == 1:
            bestActionScore = actionResult
    return bestActionScore

def betterScore(whosTurn, value, currentBest):
    if whosTurn == "X" and value > currentBest:
        if value == 1:
            return 2
        else:
            return 1
    if whosTurn == "O" and value < currentBest:
        if value == -1:
            return 2
        else:
            return 1
    return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestAction = None
    whatAmI = player(board)
    if whatAmI == X:
        bestActionScore = -2
    else: 
        bestActionScore = 2
    mypossibleMoves = actions(board)
    for consideredMove in mypossibleMoves:
        #print(str(board) + " " + str(consideredMove))
        actionResult = BestStep(result(board,consideredMove))
        actionComapason = betterScore(whatAmI, actionResult, bestActionScore)
        if actionComapason == 2:
            return consideredMove
        elif actionComapason == 1:
            bestActionScore = actionResult
            bestAction = consideredMove
    return bestAction

