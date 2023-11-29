from TicTacToe import TicTacToe
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
    print("Timing...")

    boards = [TicTacToe()] * 6
    agents = [v1(boards[0].X, boards[0], False),
              v2(boards[1].X, boards[1], False),
              v3(boards[2].X, boards[2], False),
              v4(boards[3].X, boards[3], False),
              v5(boards[4].X, boards[4], False),
              v6(boards[5].X, boards[5], False),
    ]

    for i in range(len(agents)):
        time = time_agent(agents[i])
        print(f"{type(agents[i])} time: {time}")

def time_agent(agent):
    start_time = time.perf_counter()
    agent.take_turn(False)
    end_time = time.perf_counter()
    return end_time - start_time



if __name__ == "__main__":
    main()