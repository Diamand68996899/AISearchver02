"""
Tic Tac Toe Player
"""
import copy
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
    x_count = 0
    o_count = 0
    count_empty = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == X:
                x_count += 1
            elif board[r][c] == O:
                o_count += 1
            elif board[r][c] =='EMPTY':
                count_empty += 1

    if count_empty == 9:
        return X
    elif x_count > o_count:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_postions = set()

    for r in range(3):
        for c in range(3):
            if board[r][c] ==None:
                empty_postions.add((r, c))
    return empty_postions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    who = player(board)
    board_tran = copy.deepcopy(board)
    r = action[0]
    c = action[1]
    if board_tran != None:
        board_tran[r][c] = who
    return board_tran



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # winning conditions
    win_set = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # count and sort occupied positions by X, O and EMPTY
    x_occupy = []
    x_set = []
    o_occupy = []
    o_set = []
    position_count = 0
    position_empty = 0
    for r in range(3):
        for c in range(3):
            position_count += 1
            if board[r][c] == None:
                position_empty += 1
                if position_empty >= 5:
                    return None  # game not over with empty positions, x_occupy > 3 and o_occupy >=2
            if board[r][c] == X:
                x_occupy.append(position_count)
            if board[r][c] == O:
                o_occupy.append(position_count)

    # combination of x positions and check if winning condition is reached
    for i in x_occupy:
        x_set.append(i)
        x_occupy_1 = copy.deepcopy(x_occupy)
        x_occupy_1.remove(i)
        for j in x_occupy_1:
            x_set.append(j)
            x_occupy_2 = copy.deepcopy(x_occupy_1)
            x_occupy_2.remove(j)
            for m in x_occupy_2:
                x_set.append(m)
                if x_set in win_set:
                    return X
    # combination of o positions and check if winning condition is reached
    for i in o_occupy:
        o_set.append(i)
        o_occupy_1 = copy.deepcopy(o_occupy)
        o_occupy_1.remove(i)
        for j in o_occupy_1:
            o_set.append(j)
            o_occupy_2 = copy.deepcopy(o_occupy_1)
            o_occupy_2.remove(j)
            for m in o_occupy_2:
                o_set.append(m)
                if o_set in win_set:
                    return O

    if position_empty == 0:
        return 'nobody'  # no winner
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    outcome = winner(board)
    if outcome == None:
        return False
    else:
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    outcome = winner(board)
    if outcome == X:
        return 1
    elif outcome == O:
        return -1
    elif outcome == 'nobody':
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move = []
    for action in actions(board):
        move.append(action)
    return move[0]



def max_value(board):
    v= math.inf



def min_value(board):
    v = -math.inf

