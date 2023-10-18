from queue import Empty


class TicTacToe:


    def __init__(self):
        self.EMPTY = 0
        self.X = 1
        self.O = 2
        self.TIE = 3
        self.width = 3
        self.record = {"X": 0, "O": 0, "Tie": 0}

        self.board = [self.EMPTY for i in range(self.width * self.width)]
        self.current_turn = self.O # O goes first

    def get_current_player(self):
        return self.current_turn

    def get_possible_moves(self):
        return [ind for ind, _ in enumerate(self.board) if self.board[ind] == self.EMPTY]

    def get_record(self):
        return self.record
    
    def hash(self):
        board_string = ""

        for i in self.board:
            board_string += str(i)
        
        return board_string

    def take_turn(self, space, verbose=True):

        # take turn if given space is valid
        if self.board[space] == self.EMPTY:
            self.board[space] = self.current_turn
            self.current_turn = self.O if self.current_turn == self.X else self.X
        else:
            if verbose: print("space already occupied")

        # print board
        if verbose: print(self)

        # check if anyone won
        if self.is_game_over(self.X):
            if verbose: print("X won!")
            self.record["X"] += 1
            self.reset_board()
            return self.X
        elif self.is_game_over(self.O):
            if verbose: print("O won!")
            self.record["O"] += 1
            self.reset_board()
            return self.O
        elif not self.get_possible_moves():
            if verbose: print("Tie")
            self.record["Tie"] += 1
            self.reset_board()
            return self.TIE

    def is_game_over(self, mark):
        return  (self.board[0] == mark and self.board[1] == mark and self.board[2] == mark) or \
                (self.board[3] == mark and self.board[4] == mark and self.board[5] == mark) or \
                (self.board[6] == mark and self.board[7] == mark and self.board[8] == mark) or \
                (self.board[0] == mark and self.board[3] == mark and self.board[6] == mark) or \
                (self.board[1] == mark and self.board[4] == mark and self.board[7] == mark) or \
                (self.board[2] == mark and self.board[5] == mark and self.board[8] == mark) or \
                (self.board[0] == mark and self.board[4] == mark and self.board[8] == mark) or \
                (self.board[2] == mark and self.board[4] == mark and self.board[6] == mark)
                
    def reset_board(self):
        self.board = [self.EMPTY for i in range(self.width * self.width)]
        self.current_turn = self.O # O goes first


    def __str__(self):
        output = ""

        for i in range(self.width * self.width):
            if self.board[i] == self.X: output += "X"
            elif(self.board[i] == self.O): output += "O"
            else: output += " " # str(i)

            if (i + 1) % (self.width) == 0: output += "\n"
            else: output += "|"
        
        return output
