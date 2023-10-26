import copy
import time

# with memoization + alpha beta pruning
class TicTacToeMiniMax:

    def __init__(self, player, board, verbose):
        self.player = player # X or O
        self.board = board # TicTacToe board
        self.dict = {}

        # Debugging / Statistics
        self.num_states_evaluated = 0
        self.verbose = verbose
        self.time_spent_copying = 0

    def take_turn(self, turn_verbose=True):
        maximizingPlayer = True if self.board.get_current_player() == self.board.O else False
        best_move, eval = self.minimax(self.board, 10, float("-inf"), float("inf"), maximizingPlayer)
        return self.board.take_turn(best_move, turn_verbose)


    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        
        #dict_val = self.dict.get(board.hash())
        #if not dict_val == None:
        #    return self.dict[board.hash()]
        
        possible_moves = board.get_possible_moves()

        if depth == 0:
            return possible_moves[0], 0
        
        

        if maximizingPlayer:

            maxEval = float("-inf")
            bestMove = possible_moves[0]

            for move in possible_moves:

                start_time = time.perf_counter()
                board_copy = copy.deepcopy(board)
                end_time = time.perf_counter()
                self.time_spent_copying += end_time - start_time

                state = board_copy.take_turn(move, self.verbose)

                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    _, eval = self.minimax(board_copy, depth - 1, alpha, beta, False)

                if eval > maxEval:
                    maxEval = eval
                    bestMove = move

                # alpha beta pruning
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

                self.num_states_evaluated += 1
            
            self.add_to_dict(board, bestMove, maxEval)
            return bestMove, maxEval

        else:
            minEval = float("inf")
            bestMove = possible_moves[0]
            
            for move in possible_moves:

                start_time = time.perf_counter()
                board_copy = copy.deepcopy(board)
                end_time = time.perf_counter()
                self.time_spent_copying += end_time - start_time

                state = board_copy.take_turn(move, self.verbose)
                
                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    _, eval = self.minimax(board_copy, depth - 1, alpha, beta, True)

                if eval < minEval:
                    minEval = eval
                    bestMove = move
                
                # alpha beta pruning
                beta = min(beta, eval)
                if beta <= alpha:
                    break

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
        self.dict[id] = (bestMove, eval)



