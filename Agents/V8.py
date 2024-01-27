import copy
import time
from Symmetry import Symmetry as s
import numpy as np

# with memoization + alpha beta pruning
# and symmetry
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
        
        dict_val = self.get_dict_value(board, alpha, beta)
        if not dict_val == None:
            return dict_val
        
    
        possible_moves = board.get_possible_moves()
        if len(possible_moves) > 6:
            possible_moves = s.asymmetric_moves(board.board_state, possible_moves)

        #order moves based on how good they immediately look
        #possible_moves.sort(key=self.get_move_potential_v2)
        #np.flip(possible_moves)
        #np.random.shuffle(possible_moves)


        if depth == 0:
            return possible_moves[0], 0

        if maximizingPlayer:

            maxEval = float("-inf")
            bestMove = possible_moves[0]

            for move in possible_moves:

                state = board.take_turn(move, self.verbose, track=False)

                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    _, eval = self.minimax(board, depth - 1, alpha, beta, False)

                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
                
                board.undo_turn(move)
                
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

                # determine evaluation
                if not state == None:
                    eval = self.get_eval(state)
                else:
                    # continue down tree
                    _, eval = self.minimax(board, depth - 1, alpha, beta, True)

                if eval < minEval:
                    minEval = eval
                    bestMove = move
                
                board.undo_turn(move)
                
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
    """
            Move ordering
    """
    def get_move_potential_v2(self, move):
        # middle or corner
        if move % 2 == 0: return 1

        # side
        return 0



    def get_move_potential(self, move):
        state = self.board.board_state
        player = self.board.get_current_player()
        potential = 0

        x = move % 3
        #y = move // 3

        col_sum = state[x] + state[x+3] + state[x+6]
        start_of_row = move - x
        row_sum = state[start_of_row] + state[start_of_row+1] + state[start_of_row+2]

        #print(f"player: {self.board.get_current_player()}")
        #print(f"move: {move}, column: {col_sum}, row: {row_sum}")
        #print(f"(x,y): {(x,y)}\n")

        """ Rows and Columns """
        # makes 3 in a row
        if  col_sum == 2 * player:
            return 10
        if  row_sum == 2 * player:
            return 10
        # makes 2 in a row
        if  col_sum == 1 * player:
            potential += 1
        if  row_sum == 1 * player:
            potential += 1

        """ Diagonals """
        if move % 2 == 0:
            pos_diagonal = state[0] + state[4] + state[8]
            neg_diagonal = state[2] + state[4] + state[6]

            # if pos_diagonal == 2 * player or neg_diagonal == 2 * player:
            #     return 10
            
            # makes 2 in a row
            if pos_diagonal == 1 * player:
                potential += 1
            if neg_diagonal == 1 * player:
                potential += 1


        return potential



    """
            Utility
    """  
    def get_eval(self, eval):
        if eval == self.board.X: eval = -1
        elif eval == self.board.O: eval = 1
        elif eval == self.board.TIE: eval = 0

        return eval
    """
            Transposition Table
    """
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




