import copy

class TicTacToeMiniMax:

    def __init__(self, player, board, verbose):
        self.player = player # X or O
        self.board = board # TicTacToe board
        self.num_states_evaluated = 0
        self.verbose = verbose

    def take_turn(self, turn_verbose=True):
        maximizingPlayer = True if self.board.get_current_player() == self.board.O else False
        best_move, eval = self.minimax(self.board, 10, maximizingPlayer)
        return self.board.take_turn(best_move, turn_verbose)


    def minimax(self, board, depth, maximizingPlayer):
        possible_moves = board.get_possible_moves()

        if depth == 0:
            #print("depth == 0 reached")
            return possible_moves[0], 0
        

        if maximizingPlayer:
            maxEval = float("-inf")
            bestMove = possible_moves[0]

            for move in possible_moves:
                board_copy = copy.deepcopy(board)
                eval = board_copy.take_turn(move, self.verbose)

                # determine evaluation
                if not eval == None:
                    eval = self.get_eval(eval)
                else:
                    # continue down tree
                    _, eval = self.minimax(board_copy, depth - 1, False)

                if eval > maxEval:
                    maxEval = eval
                    bestMove = move

                self.num_states_evaluated += 1
            
            return bestMove, maxEval

        else:
            minEval = float("inf")
            bestMove = possible_moves[0]
            
            for move in possible_moves:
                board_copy = copy.deepcopy(board)
                eval = board_copy.take_turn(move, self.verbose)
                
                # determine evaluation
                if not eval == None:
                    eval = self.get_eval(eval)
                else:
                    # continue down tree
                    _, eval = self.minimax(board_copy, depth - 1, True)

                if eval < minEval:
                    minEval = eval
                    bestMove = move
                
                self.num_states_evaluated += 1

            return bestMove, minEval
        
    def get_eval(self, eval):
        if eval == self.board.X: eval = -1
        elif eval == self.board.O: eval = 1
        elif eval == self.board.TIE: eval = 0

        return eval



