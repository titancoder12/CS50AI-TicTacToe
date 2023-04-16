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
    print(actions_set)
    return actions_set

def result(board, action, caller="caller"):    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if caller != "caller":
        print(caller)
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


def minimax(board):
    choices = []

    optimalx = None
    optimalo = None

    if terminal(board):
        return None
    
    if actions(board) == set():
        return None

    for action in actions(board):

        choicesdict = {}
        choicesdict[utility(result(board, action, caller="1"))] = action
        choices.append(choicesdict)

        utilitynum = utility(result(board, action, caller="2"))

        for i in range(len(choices)):
            if terminal(result(board, action)):
                if player(board) == X:
                    
                    if utilitynum == 1:
                        return action
                
                    if choices[i].get(0) != None and optimalx != None:
                        if utility(result(board, choices[i][0], caller="3")) > utility(result(board, optimalx, caller="4")):
                            optimalx = choices[i][0]

                    if choices[i].get(-1) != None and optimalx != None:
                        if utility(result(board, choices[i][-1], caller="5")) > utility(result(board, optimalx, caller="6")):
                            optimalx = choices[i][-1]

                if player(board) == O:
                    if utilitynum == -1:
                        return action
                    
                    if choices[i].get(0) != None and optimalo != None:
                            if utility(result(board, choices[i][0], caller="7")) > utility(result(board, optimalo, caller="8")):
                                optimalo = choices[i][0]
                    
                    if choices[i].get(1) != None and optimalo != None:
                        if utility(result(board, choices[i][1], caller="9")) > utility(result(board, optimalo, caller="10")):
                            optimalo = choices[i][1]
            if (player(board) == X) and (optimalx != None):
                return minimax(result(board, optimalx))
            
            if (player(board) == O) and (optimalo != None):
                return minimax(result(board, optimalo))
            if len(actions(board)) == 1:
                return action        
        return minimax(result(board, action)) 
"""
def minimax(board):
    choices = []

    for action in actions(board):
        if terminal(result(board, action)):
            utilitynum = utility(result(board, action))
            if player(board) == X:
                if utilitynum == 1:
                    return action
            
            if player(board) == O:
                if utilitynum == -1:
                    return action
            
            choices_dict = {}
            choices_dict[utilitynum] = action

            choices.append(choices_dict)
    
        for i in range(len(choices)):
            if player(board) == X:
                if choices[i].get(1) != None:
                    return choices[i][1]
                elif choices[i].get(0) != None:
                    return choices[i][0]
                elif choices[i].get(-1) != None:
                    return choices[i][-1]
        
            if player(board) == O:
                if choices[i].get(-1) != None:
                    return choices[i][-1]
                elif choices[i].get(0) != None:
                    return choices[i][0]
                elif choices[i].get(1) != None:
                    return choices[i][1]
        print(minimax(result(board, action)))
        return minimax(result(board, action))
"""