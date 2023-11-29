from queue import Empty
import numpy as np


class TicTacToe:
    EMPTY = 0
    X = 1
    O = 2
    TIE = 3
    WIDTH = 3

    def __init__(self, starting_board = None, current_turn = O):
        self.record = {"X": 0, "O": 0, "Tie": 0}

        if starting_board is None:
            self.board_state = np.full((3,3), self.EMPTY)
        else:

            self.board_state = np.copy(starting_board)
        self.current_turn = current_turn # O goes first

    def take_turn(self, space, verbose=True, track=True):
        space = self.move_to_ind(space)

        # take turn if given space is valid
        if self.board_state[space] == self.EMPTY:
            self.board_state[space] = self.current_turn
            self.current_turn = self.change_turn()
        else:
            if verbose: print("space already occupied")

        # print board_state
        if verbose: print(self)

        # check if anyone won
        if self.is_game_over(self.X):
            if track:
                if verbose: print("X won!")
                self.record["X"] += 1
                #self.reset_board()
            return self.X
        
        elif self.is_game_over(self.O):
            if track:
                if verbose: print("O won!")
                self.record["O"] += 1
                #self.reset_board()
            return self.O
        
        elif not self.get_possible_moves():
            if track:
                if verbose: print("Tie")
                self.record["Tie"] += 1
                #self.reset_board()
            return self.TIE

    def undo_turn(self, move, output=None):
        turn = self.change_turn()
        move = self.move_to_ind(move)

        if self.board_state[move] == turn:
            self.board_state[move] = self.EMPTY
            self.current_turn = turn
        else:
            print(f"invalid undo for move {move}. Output: {output}")
            exit()

    def is_game_over(self, mark):
        return  (self.board_state[0,0] == mark and self.board_state[0,1] == mark and self.board_state[0,2] == mark) or \
                (self.board_state[1,0] == mark and self.board_state[1,1] == mark and self.board_state[1,2] == mark) or \
                (self.board_state[2,0] == mark and self.board_state[2,1] == mark and self.board_state[2,2] == mark) or \
                (self.board_state[0,0] == mark and self.board_state[1,0] == mark and self.board_state[2,0] == mark) or \
                (self.board_state[0,1] == mark and self.board_state[1,1] == mark and self.board_state[2,1] == mark) or \
                (self.board_state[0,2] == mark and self.board_state[1,2] == mark and self.board_state[2,2] == mark) or \
                (self.board_state[0,0] == mark and self.board_state[1,1] == mark and self.board_state[2,2] == mark) or \
                (self.board_state[0,2] == mark and self.board_state[1,1] == mark and self.board_state[2,0] == mark)

    def copy(self):
        return TicTacToe(self.board_state, self.current_turn)

    def reset_board(self):
        self.board_state = np.full((3,3), self.EMPTY)
        self.current_turn = self.O # O goes first

    def change_turn(self):
        return self.O if self.current_turn == self.X else self.X

    def get_current_player(self):
        return self.current_turn

    def get_possible_moves(self):
        possible_moves = []

        for i in range(self.WIDTH):
            for j in range(self.WIDTH):
                if self.board_state[i,j] == self.EMPTY:
                    possible_moves.append(i * 3 + j)

        return possible_moves

    def get_record(self):
        return self.record
    
    def move_to_ind(self, move):
        x = move // self.WIDTH
        y = move - x * self.WIDTH
        return (x,y)

    def hash(self):
        return str(self.board_state)

    def __str__(self):
        output = ""

        for i in range(self.WIDTH):
            for j in range(self.WIDTH):
                if self.board_state[i,j] == self.X: output += "X"
                elif(self.board_state[i,j] == self.O): output += "O"
                else: output += " "
                
                if not j == self.WIDTH - 1:
                    output += "|"
            output += "\n"
        
        return output
