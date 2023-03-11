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
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                X_count+=1
            elif board[i][j] == O:
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
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.update([(i, j)])
    print("Actions:")
    print(actions_set, end="\n\n")
    return actions_set

def result(board, action):    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j= action[1]
    print("I:"+str(i) + " J:"+str(j))
    board_copy = copy.deepcopy(board)
    print(player(board))
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
            if (board[0][j] == X) and (board[1][j] == X) and (board[2][j] == X):
                return X
            elif (board[0][j] == O) and (board[1][j] == O) and (board[2][j] == O):
                return O

        if ((board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X)) or ((board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X)):
            return X
        
        if (board[0][0]) == O and (board[1][1] == O) and (board[2][2] == O):
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
            if (board[0][j]==(X or O)) and (board[1][j]==(X or O)) and (board[2][j]==(X or O)):
                return True

        if (board[0][0]==(X or O)) and (board[1][1]==(X or O)) and (board[2][2]==(X or O)):
            return True
        
        if (board[0][2]==(X or O)) and (board[1][1]==(X or O)) and (board[2][0]==(X or O)):
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
    # print(board)
    if terminal(board):
        return None
    choices = []
    for action in actions(board):
        if terminal(result(board, action)):
                return action
        else:
            choice = minimax(result(board, action))
            choices.append(choice)
        print("choice:")
        print(choice)
    min_list = []
    max_list = []
    min_num = -10000
    max_num = 10000
    min_choice = []
    max_choice = []
    for choice in choices:
        utility_num = utility(result(board, choice))
        print("Choices:")
        print(choices)
        if utility_num == -1:
            print("O win")
            
        
        if utility_num == 1:
            print("X win")
            utility_num = max_num
            max_choice[1] = list(choice)[1]
            max_choice[2] = list(choice)[2]
        
        if utility_num == 0:
            print("Tie")
    
    if player(board) == X:
        print("max_list:")
        print(max_list)
        return tuple(max_choice)
    elif player(board) == O:
        print("min_list:")
        print(min_list)
        return tuple(min_choice)
        #min_list[1]
    else:
        return None

#print(result((1, 1), [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]))