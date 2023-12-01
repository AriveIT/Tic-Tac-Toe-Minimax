import random

class RandomAgent:

    def __init__(self, player, board):
        self.player = player # X or O
        self.board = board # TicTacToe board

    def take_turn(self, verbose=True):
        possible_moves = self.board.get_possible_moves()
        space = random.choice(possible_moves)
        
        return self.board.take_turn(space, verbose)
