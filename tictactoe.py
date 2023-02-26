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
    X_count = 0
    O_count = 0
    i_count = 0
    for i in board:
        for j in board[i_count]:
            if j == X:
                X_count+=1
            elif j == O:
                O_count+=1
        i_count += 1
    if X_count == O_count:
        return X
    elif X_count > O_count:
        return X
    elif X_count < O_count:
        return O
    else:
        raise TypeError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    i_count = 0
    j_count = 0
    for i in range(3):
        for j in range(3):
            if j == EMPTY:
                actions_set.add((i_count, j_count))
            j_count += 1
        i_count += 1
    print(actions_set)
    return actions_set

def result(board, action):    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j= action[1]
    print("I:"+str(i) + " J:"+str(j))
    board_copy = copy.deepcopy(board)
    #print(board_copy)
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    i_count = 0
    for i in board:
        if i == [X, X, X]:
            return X
        elif i == [O, O, O]:
            return O
        
        for j in range(i_count):
            if board[0][j] and board[1][j] and board[2][j] == X:
                return X
            elif board[0][j] and board[1][j] and board[2][j] == O:
                return O

        if board[0][0] and board [1][1] and board[2][2] == X:
            return X
        
        if board[0][0] and board [1][1] and board[2][2] == O:
            return O

        i_count += 1
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if type(board) != list:
        raise TypeError
    i_count = 0
    for i in board:
        if i == [X, X, X]:
            return True
        elif i == [O, O, O]:
            return True
        # print(len(board[i_count]))
        for j in range(3):
            #print(j)
            #print(board[0][j])
            if (board[0][j] and board[1][j] and board[2][j]) == (X or O):
                return True

        if (board[0][0] and board [1][1] and board[2][2]) == (X or O):
            return True

        i_count+=1
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    choices = []
    for action in actions(board):
        if terminal(result(board, action)):
            if winner(action) == X:
                return (1, action)
            elif winner(action) == O:
                return (-1, action)
            else:
                return (0, action)
        else:
            choice = (minimax(result(board, action))[0], minimax(result(board, action))[1])
            choices.append(choice)
    min_list = []
    max_list = []
    min_num = 1000
    max_num = -1000
    for choice in choices:
        print(choice)
        if choice[0] < min_num:
            print("reached case 1")
            min_num = choice[0]
            min_list.clear()
            min_list.append(min_num)
            min_list.append(choice[1])
        
        if choice[0] > max_num:
            print("Reached case 2")
            max_num = choice[0]
            max_list.clear()
            max_list.append(max_num)
            max_list.append(choice[1])
    
    if player(board) == X:
        print(max_list)
        return max_list[1]
    elif player(board) == O:
        print(min_list)
        return min_list[1]
    else:
        return None
