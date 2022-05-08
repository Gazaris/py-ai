"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

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
    # Count how many moves each player has made
    x_player = 0
    o_player = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_player += 1
            elif cell == O:
                o_player += 1
    
    # Decide who's turn it is
    if o_player < x_player:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Counts all free spaces
    res = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                res.add((i, j))

    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If was given an invalid move for the given board
    if action not in actions(board):
        raise Exception("Not a valid move!")

    # Create a deep copy of the board and make a move for whichever player's move it is
    res_board = deepcopy(board)
    res_board[action[0]][action[1]] = player(board)
    return res_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking every row vertically and then horizontally
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # Checking diagonally
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board [1][1]
    
    # If no win was found return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


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

    # Get all actions scores and choose the best option
    if player(board) == X:
        best_action = (None, -10)
        for action in actions(board):
            action_res_value = min_value(result(board, action))
            if action_res_value > best_action[1]:
                best_action = (action, action_res_value)

        return best_action[0]
    else:
        best_action = (None, 10)
        for action in actions(board):
            action_res_value = max_value(result(board, action))
            if action_res_value < best_action[1]:
                best_action = (action, action_res_value)

        return best_action[0]


def max_value(board):
    """
    Returns an optimal action for the X player on the given board
    """
    if terminal(board):
        return utility(board)
    
    v = -10
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v


def min_value(board):
    """
    Returns an optimal action for the O player on the given board
    """
    if terminal(board):
        return utility(board)
    
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v
