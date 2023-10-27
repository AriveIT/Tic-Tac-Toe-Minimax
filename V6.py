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

    def take_turn(self, turn_verbose=True):
        maximizingPlayer = True if self.board.get_current_player() == self.board.O else False
        best_move, _ = self.minimax(self.board, 10, float("-inf"), float("inf"), maximizingPlayer)
        return self.board.take_turn(best_move, turn_verbose)


    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        pruned = False
        
        #dict_val = self.dict.get(board.hash())
        dict_val = self.get_dict_value(board, alpha, beta)
        if not dict_val == None:
            return dict_val
        
        possible_moves = board.get_possible_moves()

        if depth == 0:
            return possible_moves[0], 0

        if maximizingPlayer:

            maxEval = float("-inf")
            bestMove = possible_moves[0]

            for move in possible_moves:

                state = board.take_turn(move, self.verbose, track=False)
                #print("~~~~~ take turn ~~~~~")
                #print(board)
                #print("~~~~~~~~~~~~~~~~~~~~~~")

                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    _, eval = self.minimax(board, depth - 1, alpha, beta, False)

                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
                
                #print("-" * 15)
                #print(board)
                board.undo_turn(move)
                #print(board)
                #print("-" * 15)
                self.num_states_evaluated += 1

                # alpha beta pruning
                alpha = max(alpha, eval)
                if beta <= alpha:
                    pruned = True
                    break

            
            if pruned:
                self.add_to_dict(board, bestMove, None, alpha, float("inf"))
            else:
                self.add_to_dict(board, bestMove, maxEval, None, None)
            return bestMove, maxEval

        else:
            minEval = float("inf")
            bestMove = possible_moves[0]
            
            for move in possible_moves:

                state = board.take_turn(move, self.verbose, track=False)
                #print("~~~~~ take turn ~~~~~")
                #print(board)
                #print("~~~~~~~~~~~~~~~~~~~~~~")

                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    _, eval = self.minimax(board, depth - 1, alpha, beta, True)

                if eval < minEval:
                    minEval = eval
                    bestMove = move
                
                #print("-" * 15)
                #print(board)
                board.undo_turn(move)
                #print(board)
                #print("-" * 15)
                self.num_states_evaluated += 1
                
                # alpha beta pruning
                beta = min(beta, eval)
                if beta <= alpha:
                    pruned = True
                    break

            
            if pruned:
                self.add_to_dict(board, bestMove, None, float("-inf"), beta)
            else:
                self.add_to_dict(board, bestMove, minEval, None, None)
            return bestMove, minEval
        
    def get_eval(self, eval):
        if eval == self.board.X: eval = -1
        elif eval == self.board.O: eval = 1
        elif eval == self.board.TIE: eval = 0

        return eval
    
    def add_to_dict(self, board, bestMove, exact_val, lower_bound, upper_bound):
        id = board.hash()
        self.dict[id] = (bestMove, exact_val, lower_bound, upper_bound)
    
    def get_dict_value(self, board, alpha, beta):
        hash = board.hash()
        dict_value = self.dict.get(hash)

        # if board not stored yet, return
        if dict_value is None: return None

        bestMove, exact_val, lower, upper = dict_value
        
        # if we have exact value
        if exact_val is not None: return bestMove, exact_val

        # if we have range
        if upper <= alpha: return bestMove, upper
        if lower >= beta: return bestMove, lower




