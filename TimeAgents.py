from TicTacToeOld import TicTacToe
from RandomAgent import RandomAgent
from V1 import TicTacToeMiniMax as v1
from V2 import TicTacToeMiniMax as v2
from V3 import TicTacToeMiniMax as v3
from V4 import TicTacToeMiniMax as v4
from V5 import TicTacToeMiniMax as v5
from V6 import TicTacToeMiniMax as v6
from V7 import TicTacToeMiniMax as v7

import math
import time
import numpy as np


def main():
    print("\nTiming...")

    board = TicTacToe()
    minimax_agent = v1(board.X, board, False)
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"v1 time: {end_time - start_time}")
    
    board = TicTacToe()
    minimax_agent = v2(board.X, board, False)
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"v2 time: {end_time - start_time}")


    board = TicTacToe()
    minimax_agent = v3(board.X, board, False)
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"v3 time: {end_time - start_time}")


    board = TicTacToe()
    minimax_agent = v4(board.X, board, False)
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"v4 time: {end_time - start_time}")


    board = TicTacToe()
    minimax_agent = v5(board.X, board, False)
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"v5 time: {end_time - start_time}")


    board = TicTacToe()
    minimax_agent = v6(board.X, board, False)
    start_time = time.perf_counter()
    minimax_agent.take_turn(False)
    end_time = time.perf_counter()
    print(f"v6 time: {end_time - start_time}")



if __name__ == "__main__":
    main()