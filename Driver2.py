from TicTacToe import TicTacToe
from RandomAgent import RandomAgent
from V3 import TicTacToeMiniMax

import math
import time

def main():
    #test_minimax()
    #time_minimax()
    #minimax_vs_random()
    player_vs_minimax()

# ---------------------
# Test minmax
# ---------------------
# for empty board full depth:
# v1: 549 945 states
# v2: 16 167 states
def test_minimax():
    print("\nTesting...")
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)

    results = minimax_agent.minimax(board, 10, float("-inf"), float("inf"), True)
    
    print(minimax_agent.num_states_evaluated)
    print(results) 
    print("dict length: " + str(len(minimax_agent.dict)))

# this is wrong as it doesn't account for recursion stopping due to a win
# returns 623 530
def expected_num_states():
    sum = 0

    for i in range(1, 10):
        sum += math.factorial(9) / math.factorial(i)

    return sum

def get_almost_full_board(board):
    t(board, 0)
    t(board, 2)
    t(board, 1)
    t(board, 3)
    t(board, 4)
    t(board, 7)
    return board
# ---------------
# timing minimax
# ---------------
# v1: 8.127084970474243s
# v2: 0.26595592498779s
def time_minimax():
    print("\nTiming...")
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)
    
    start_time = time.perf_counter()
    minimax_agent.minimax(board, 10, float("-inf"), float("inf"), True)
    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time}")

    copy_time = minimax_agent.time_spent_copying
    print(f"Time copying: {copy_time}")
    print(f"proportion: {copy_time / (end_time - start_time)}")

    """
    start_time = time.perf_counter()
    minimax_agent.minimax(board, 10, float("-inf"), float("inf"), True)
    end_time = time.perf_counter()
    print(end_time - start_time)
    """

# -----------------------
# Compare models
# -----------------------
def minimax_vs_minimax():
    board = TicTacToe()
    minimax_agent1 = TicTacToeMiniMax(board.X, board, False)
    minimax_agent2 = TicTacToeMiniMax(board.X, board, False)
    
    num_games = 1
    for i in range(num_games):
        while True:
            if not minimax_agent1.take_turn(False) == None: break
            if not minimax_agent2.take_turn(False) == None: break

    print(board.get_record())


def player_vs_minimax():
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)

    while True:
        if not minimax_agent.take_turn(True) == None: break
        player_input = int(input())
        if not board.take_turn(player_input, True) == None: break


def minimax_vs_random():
    #print("\nvs Random...")
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)
    random_agent = RandomAgent(board.O, board)
    num_games = 1000
    
    
    for i in range(num_games):
        while True:
            if not minimax_agent.take_turn(True) == None: break
            if not random_agent.take_turn(True) == None: break

        if (board.get_record()["X"] != 0 or board.get_record()["Tie"] != 0): break

    print(board.get_record())



# ------------------
# Test TicTacToe
# ------------------

def t(board, move):
    board.take_turn(move, False)

if __name__ == "__main__":
    main()



