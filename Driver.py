from TicTacToe import TicTacToe
from RandomAgent import RandomAgent
from V6 import TicTacToeMiniMax

import math
import time

def main():
    test_minimax()
    time_minimax()
    #minimax_vs_random(False, num_games=1000)
    #player_vs_minimax()
    #player_vs_player()

# ---------------------
# Test minmax
# ---------------------
# for empty board full depth:
# v1: 549 945 states
# v2: 16 167 states
# v3: 10 116 states
# v4: 3 120 states
def test_minimax():
    print("\nTesting...")
    board = TicTacToe()
    #prep_board_state(board)
    minimax_agent = TicTacToeMiniMax(board.X, board, False)

    results = minimax_agent.minimax(board, 10, float("-inf"), float("inf"), True)
    #results = minimax_agent.take_turn(False)
    
    print(f"states evaluated: {minimax_agent.num_states_evaluated}")
    #print(results) 
    print(f"dict length: {len(minimax_agent.dict)}")

# this is wrong as it doesn't account for recursion stopping due to a win
# returns 623 530
def expected_num_states():
    sum = 0

    for i in range(1, 10):
        sum += math.factorial(9) / math.factorial(i)

    return sum

def prep_board_state(board):
    t(board, 0)
    t(board, 8)
    t(board, 2)
    t(board, 1)
    t(board, 4)
    t(board, 5)
    
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
# v3: 0.29037840000819415s
# v4: 0.08041890012100339s
def time_minimax():
    print("\nTiming...")
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)
    
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time}")

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
        #board.reset_board()
    print(board.get_record())


def player_vs_minimax():
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)

    while True:
        if not minimax_agent.take_turn(True) == None: break
        player_input = int(input())
        if not board.take_turn(player_input, True) == None: break

def player_vs_player():
    board = TicTacToe()

    while True:
        player_input = int(input())
        if not board.take_turn(player_input, True) == None: break
        player_input = int(input())
        if not board.take_turn(player_input, True) == None: break

def minimax_vs_random(verbose, num_games = 10):
    print("\nvs Random...")
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)
    random_agent = RandomAgent(board.O, board)

    for i in range(num_games):
        while True:
            if minimax_agent.take_turn(verbose) is not None: break
            if random_agent.take_turn(verbose) is not None: break


        if board.get_record()["X"] != 0: break
        minimax_agent.dict = {}
        board.reset_board()

    print(board.get_record())



# ------------------
# Test TicTacToe
# ------------------


def t(board, move):
    board.take_turn(move, False)

if __name__ == "__main__":
    main()




