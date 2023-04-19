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
                actions_set.add((i, j))
    #print("Actions:")
    #print(actions_set)
    return actions_set

def result(board, action):    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #print(action)
    if type(action) != tuple:
        raise TypeError
    i = action[0]
    j = action[1]
    #print("I:"+str(i) + " J:"+str(j))
    board_copy = copy.deepcopy(board)
    #print(board_copy)
    if board_copy[i][j] != None:
        raise Exception("Move is not legal; spot has been occupied")
    board_copy[i][j] = player(board)
    #print(board_copy)
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
            if (board[0][j]==(X)) and (board[1][j]==(X)) and (board[2][j]==(X)):
                return True
            
            if (board[0][j]==(O)) and (board[1][j]==(O)) and (board[2][j]==(O)):
                return True
            
            if (board[j][0] == X) and (board[j][1] == X) and (board[j][2] == X):
                return True
            
            if (board[j][0] == O) and (board[j][1] == O) and (board[j][2] == O):
                return True

        if (board[0][0]==X) and (board[1][1]==X) and (board[2][2]==X):
            return True
        
        if (board[0][0]==O) and (board[1][1]==O) and (board[2][2]==O):
            return True
        
        if (board[0][2]==(X)) and (board[1][1]==(X)) and (board[2][0]==(X)):
            return True
        
        if (board[0][2]==(O)) and (board[1][1]==(O)) and (board[2][0]==(O)):
            return True

        i_count+=1
    if len(actions(board)) == 0:
        return True
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

call = 0
def minimax(board):
    global call
    call += 1
    print(f"call #{call}")

    if terminal(board):
        return None
    
    
    if actions(board) == set():
        return None
    
    for action in actions(board):
        
        # init variables
        optimalx = None
        optimalx = None
        optimalx_util = -1000
        optimalo = None
        optimalo_util = 1000
        skip = False
        playerX = action
        playerO = None
        
        playerO = minimax(result(board, playerX))
        if playerO == None:
            onlyaction = None
            for action in actions(board):
                onlyaction = action
            utility_num = utility(result(board, onlyaction))
            skip = True

        else:
            playerX = minimax(result(board, playerO))
            if playerX == None:
                onlyaction = None
                for action in actions(board):
                    onlyaction = action
                utility_num = utility(result(board, onlyaction))
                skip = True
        #print(skip)
        if skip == False:
            while True:
                playerO = minimax(result(board, playerX))
                if playerO == None:
                    onlyaction = None
                    for action in actions(board):
                        onlyaction = action
                    utility_num = utility(result(board, playerX))
                    break

                playerX = minimax(result(board, playerO))
                if playerX == None:
                    onlyaction = None
                    for action in actions(board):
                        onlyaction = action
                    utility_num = utility(result(board, playerO))
                    break

        #print(utility_num)
        if player(board) == X and utility_num > optimalx_util:
            optimalx = action
            optimalx_util = utility_num
            #print(action)
        if player(board) == O and utility_num > optimalo_util:
            optimalo = action
            optimalo_util = utility_num
            #print(action)

    if player(board) == X:
        return optimalx
    if player(board) == O:
        return optimalo
    

    