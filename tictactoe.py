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
    elif X_count < O_count:
        return X
    elif X_count > O_count:
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
    #print("Actions:")
    #print(actions_set, end="\n\n")
    return actions_set

def result(board, action):    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j= action[1]
    #print("I:"+str(i) + " J:"+str(j))
    board_copy = copy.deepcopy(board)
    #print(player(board))
    if board_copy[i][j] != None:
        raise Exception("Move is not legal; spot has been occupied")
    board_copy[i][j] = player(board)
    #print(board)
    i = 0
    j = 0
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
        # #print(len(board[i_count]))
        for j in range(3):
            ##print(j)
            ##print(board[0][j])
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

def minimax(board, caller="notself"):
    """
    Returns the optimal action for the current player on the board.
    """
    choices = []
    # #print(board)
    #if terminal(board):
    #    return None

    # Loop over actions
    for action in actions(board):
        # Check action leads to terminal board
        # Make sure the caller is self, so as not to return the wrong value
        if terminal(result(board, action)):
            print(f"utility:{utility(result(board, action))}")
            return utility(result(board, action))
        else:
            # Recursive programming
            utility_num = minimax(result(board, action))
            print(f"utility num: {utility_num}")
            # Create dict to add to list later on
            choices_dict = {}
            # Assign utility number to action
            choices_dict[utility_num] = action
            # Add dict to list
            choices.append(choices_dict) 
        # #print out possible choices
        #print(f"\n Choices: {choices_dict} \n")

    for i in range(len(choices)):
        print(choices)
        if player(board) == X:
            if choices[i].get(1) != None:
                #print(f"ideal: {choices[i][1]}")
                return choices[i][1]
            elif choices[i].get(0) != None:
                #print(f"ideal: {choices[i][0]}")
                return choices[i][0]
            elif choices[i].get(-1) != None:
                #print(f"ideal: {choices[i][-1]}")
                return choices[i][-1]
    
        if player(board) == O:
            if choices[i].get(-1) != None:
                #print(f"ideal: {choices[i][-1]}")
                return choices[i][-1]
            elif choices[i].get(0) != None:
                #print(f"ideal: {choices[i][0]}")
                return choices[i][0]
            elif choices[i].get(1) != None:
                #print(f"ideal: {choices[i][1]}")
                return choices[i][1]
    return None