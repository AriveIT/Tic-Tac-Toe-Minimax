import copy

# with memoization
class TicTacToeMiniMax:

    def __init__(self, player, board, verbose):
        self.player = player # X or O
        self.board = board # TicTacToe board
        self.num_states_evaluated = 0
        self.verbose = verbose
        self.dict = {}

    def take_turn(self, turn_verbose=True):
        maximizingPlayer = True if self.board.get_current_player() == self.board.O else False
        best_move, eval = self.minimax(self.board, 10, maximizingPlayer)
        return self.board.take_turn(best_move, turn_verbose)


    def minimax(self, board, depth, maximizingPlayer):
        
        dict_val = self.dict.get(board.hash())
        if not dict_val == None:
            return self.dict[board.hash()]
        
        possible_moves = board.get_possible_moves()

        if depth == 0:
            return possible_moves[0], 0
        
        

        if maximizingPlayer:

            maxEval = float("-inf")
            bestMove = possible_moves[0]

            for move in possible_moves:
                board_copy = copy.deepcopy(board)
                #print(board_copy)
                state = board_copy.take_turn(move, self.verbose)

                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    #dict_val = self.dict.get(self.board.hash())
                    _, eval = self.minimax(board_copy, depth - 1, False)
                    #if dict_val == None:   
                    #    _, eval = self.minimax(board_copy, depth - 1, False)
                    #else:
                    #    eval = dict_val

                if eval > maxEval:
                    maxEval = eval
                    bestMove = move

                self.num_states_evaluated += 1
            
            self.add_to_dict(board, bestMove, maxEval)
            return bestMove, maxEval

        else:
            minEval = float("inf")
            bestMove = possible_moves[0]
            
            for move in possible_moves:
                board_copy = copy.deepcopy(board)
                state = board_copy.take_turn(move, self.verbose)
                
                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    #dict_val = self.dict.get(self.board.hash())
                    _, eval = self.minimax(board_copy, depth - 1, True)
                    #if dict_val == None:
                    #    _, eval = self.minimax(board_copy, depth - 1, True)
                    #else:
                    #    eval = dict_val

                if eval < minEval:
                    minEval = eval
                    bestMove = move
                
                self.num_states_evaluated += 1
            
            self.add_to_dict(board, bestMove, minEval)
            return bestMove, minEval
        
    def get_eval(self, eval):
        if eval == self.board.X: eval = -1
        elif eval == self.board.O: eval = 1
        elif eval == self.board.TIE: eval = 0

        return eval
    
    def add_to_dict(self, board, bestMove, eval):
        id = board.hash()
        #print(id)
        #print(board)
        self.dict[id] = (bestMove, eval)



