import sys
sys.path.insert(0, './Agents')

from TicTacToe import TicTacToe
from RandomAgent import RandomAgent
from V8 import TicTacToeMiniMax

import time

def main():
    test_minimax()
    #time_minimax()
    #minimax_vs_random(num_games=1000)

    #test_move_potential()

    # a = ['break', 'apple', 'dreadful', 'catastrophic']
    # a.sort(key=test_sort)
    # print(a)

def test_sort(s, test_var=5):
    return len(s) + test_var

def test_move_potential():
    board = TicTacToe([1, 0, -1, 1, -1, -1, 0, 0, 0])
    agent = TicTacToeMiniMax(board.X, board, False)
    moves = board.get_possible_moves()
    potentials = [agent.get_move_potential(move) for move in moves]

    print(board)
    print(moves)
    print(potentials)
# ---------------------
# Test minmax
# ---------------------
def test_minimax():
    print("\nTesting...")
    board = TicTacToe()
    minimax_agent = TicTacToeMiniMax(board.X, board, False)

    results = minimax_agent.minimax(board, 10, float("-inf"), float("inf"), True)
    
    print(f"states evaluated: {minimax_agent.num_states_evaluated}")
    print(f"dict length: {len(minimax_agent.dict)}")

# ---------------
# timing minimax
# ---------------
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

def minimax_vs_random(verbose=False, num_games=10):
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

if __name__ == "__main__":
    main()




