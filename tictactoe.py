"""
Tic Tac Toe Player
"""

import math
import copy

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
    xmoves=0
    omoves=0
    for row in board:
        xmoves+=row.count(X)
        omoves+=row.count(O)
    return X if xmoves==omoves else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]]!= EMPTY:
        raise NameError('INVALID ACTION')
    rlt=copy.deepcopy(board)

    rlt[action[0]][action[1]]=player(board)
    return rlt


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    diag1=[]
    diag2=[]
    rows=[set(row) for row in board]

    for i in range(3):
        rows.append(set([board[l][i] for l in range(3)]))
        diag1.append(board[i][i])
        diag2.append(board[i][-1-i])
    rows.append(set(diag1))
    rows.append(set(diag2))
    for row in rows:
        if row=={X} or row=={O}:
            return list(row)[0]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    else:
        return (all([EMPTY not in l for l in board]))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    rlt=winner(board)
    if rlt==X:
        return 1
    elif rlt==O:
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board."""

    if terminal(board):
        return None
    else:
            move=()
            if player(board)==X:
                max=-2
                for action in actions(board):

                    v=max_value(result(board,action))
                    if max<v:
                        max=v
                        move=action

            else:
                min=2
                for action in actions(board):
                    v=min_value(result(board,action))
                    if min>v:
                        min=v
                        move=action
            return move

def max_value(board):

    if terminal(board):
        return utility(board)
    else:
        u=-2
        for action in actions(board):
            u=max(u,min_value(result(board,action)))
        return u

def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        u=2
        for action in actions(board):
            u=min(u,max_value(result(board,action)))
        return u
