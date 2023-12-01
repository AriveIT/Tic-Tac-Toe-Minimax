
class TicTacToe:
    EMPTY = 0
    X = 1
    O = 2
    TIE = 3
    WIDTH = 3

    def __init__(self, starting_board = None, current_turn = O):
        self.record = {"X": 0, "O": 0, "Tie": 0}

        if starting_board is None:
            self.board_state = [self.EMPTY for i in range(self.WIDTH * self.WIDTH)]
        else:
            self.board_state = [x for x in starting_board]
        self.current_turn = current_turn # O goes first

    def take_turn(self, space, verbose=True, track=True):

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

        if self.board_state[move] == turn:
            self.board_state[move] = self.EMPTY
            self.current_turn = turn
        else:
            print(f"invalid undo for move {move}. Output: {output}")
            exit()

    def is_game_over(self, mark):
        return  (self.board_state[0] == mark and self.board_state[1] == mark and self.board_state[2] == mark) or \
                (self.board_state[3] == mark and self.board_state[4] == mark and self.board_state[5] == mark) or \
                (self.board_state[6] == mark and self.board_state[7] == mark and self.board_state[8] == mark) or \
                (self.board_state[0] == mark and self.board_state[3] == mark and self.board_state[6] == mark) or \
                (self.board_state[1] == mark and self.board_state[4] == mark and self.board_state[7] == mark) or \
                (self.board_state[2] == mark and self.board_state[5] == mark and self.board_state[8] == mark) or \
                (self.board_state[0] == mark and self.board_state[4] == mark and self.board_state[8] == mark) or \
                (self.board_state[2] == mark and self.board_state[4] == mark and self.board_state[6] == mark)

    def copy(self):
        return TicTacToe(self.board_state, self.current_turn)

    def reset_board(self):
        self.board_state = [self.EMPTY for i in range(self.WIDTH * self.WIDTH)]
        self.current_turn = self.O # O goes first

    def change_turn(self):
        return self.O if self.current_turn == self.X else self.X

    def get_current_player(self):
        return self.current_turn

    def get_possible_moves(self):
        return [ind for ind, _ in enumerate(self.board_state) if self.board_state[ind] == self.EMPTY]

    def get_record(self):
        return self.record
    
    def hash(self):
        return str(self.board_state)

    def __str__(self):
        output = ""

        for i in range(self.WIDTH * self.WIDTH):
            if self.board_state[i] == self.X: output += "X"
            elif(self.board_state[i] == self.O): output += "O"
            else: output += " " # str(i)

            if (i + 1) % (self.WIDTH) == 0: output += "\n"
            else: output += "|"
        
        return output
