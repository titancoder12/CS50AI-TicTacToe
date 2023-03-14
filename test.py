from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax

board = initial_state()
X = "X"
O = "O"
EMPTY = None
X_board = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
O_board = [[O, O, O], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
Tie_board = [[X, X, O], [O, O, X], [X, X, O]]
Random_board = [[X, EMPTY, EMPTY], [O, EMPTY, EMPTY], [X, EMPTY, EMPTY]]

# test player
print("player:\n---------------------")
print(f"{player(board)} is X")
print(f"{player(Random_board)} is O")

print("")

# test action
print("action:\n---------------------")
print(f"{actions(board)}")
print(f"{actions(X_board)}")
print(f"{actions(O_board)}")
print(f"{actions(Tie_board)}")
print(f"{actions(Random_board)}")

print("")

# test result
print("result:\n---------------------")
print(f"{result(board, (1, 1))}")
#result(X_board, (1, 1))
#result(O_board, (1, 1))
#result(Tie_board, (1, 1))
print(f"{result(Random_board, (1, 1))}")

print("")

# test winner
print("winner:\n---------------------")
print(f"{winner(board)} should be None")
print(f"{winner(X_board)} should be X")
print(f"{winner(O_board)} should be O")
print(f"{winner(Tie_board)} should be None")
print(f"{winner(Random_board)} should be None")

print("")

# test terminal
print("terminal:\n---------------------")
print(f"{terminal(board)} should be False")
print(f"{terminal(X_board)} should be True")
print(f"{terminal(O_board)} should be True")
print(f"{terminal(Tie_board)} should be True")
print(f"{terminal(Random_board)} should be False")


print("")

# test utility
print("utility:\n---------------------")
print(f"{utility(X_board)} should be 1")
print(f"{utility(O_board)} should be -1")
print(f"{utility(Tie_board)} should be 0")

print("")

# test minimax
print("minimax:\n---------------------")
print(f"{minimax(board)}")
print(f"{minimax(Tie_board)}")
print(f"{minimax(Random_board)}")