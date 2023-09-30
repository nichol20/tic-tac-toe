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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count <= o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
                
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    new_board = copy.deepcopy(board)
    i, j = action

    if new_board[i][j] != EMPTY:
        raise Exception("Action must be on an empty field")

    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    for player in [X, O]:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return player
            if all(board[j][i] == player for j in range(3)):
                return player

    for diagonal in diagonals:
        if all(board[i][j] == X for i, j in diagonal):
            return X
        if all(board[i][j] == O for i, j in diagonal):
            return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return all(row.count(EMPTY) == 0 for row in board) or bool(winner(board))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    player_turn = player(board)
    if player_turn == X:
        return max_value(board)[1]
    if player_turn == O:
        return min_value(board)[1]

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = -math.inf
    optimal_action = None

    for action in actions(board):
        min_value_result = min_value(result(board, action))[0]
        if min_value_result > v:
            v = min_value_result
            optimal_action = action

    return v, optimal_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = math.inf
    optimal_action = None

    for action in actions(board):
        max_value_result = max_value(result(board, action))[0]
        if max_value_result < v:
            v = max_value_result
            optimal_action = action

    return v, optimal_action