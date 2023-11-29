
import numpy as np

class Symmetry:

    def __init__():
        pass
    
    def asymmetric_moves(board_state, moves):
        asymmetric_moves = [moves[0]]
        symmetric = False

        for move in moves:
            # playing in the center has no symmetries
            if move == 4:
                asymmetric_moves.append(move)
                continue

            for a_move in asymmetric_moves:
                if Symmetry.is_symmetric(board_state, move, a_move):
                    symmetric = True
                    break
                else:
                    continue

            if move not in asymmetric_moves and not symmetric:
                asymmetric_moves.append(move)
            
            symmetric = False


        return asymmetric_moves

    # assumes move > a_move
    def is_symmetric(board_state, move, a_move):
        if not Symmetry.possibly_symmetric(move, a_move):
            return False
        
        """
        note: we do not have to "play" the moves since we know, after the transformations,
        the moves would end up on the same spot
        therefore that spot wouldn't change if the 2 board states are equal or not
        note: move < a_move will never happen, since move must be visited first in order to be added to a_move
        and move is in increasing order
        """
        if (move == 8 and a_move == 6):
            temp = Symmetry.yaxis_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.positive_diagonal_reflection(temp)): 
                return True
        elif (move == 2 and a_move == 0):
            temp = Symmetry.yaxis_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.negative_diagonal_reflection(temp)):
                return True
        elif (move == 6 and a_move == 0):
            temp = Symmetry.xaxis_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.negative_diagonal_reflection(temp)):
                return True
        elif (move == 8 and a_move == 2): 
            temp = Symmetry.xaxis_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.positive_diagonal_reflection(temp)):
                return True
        elif (move == 8 and a_move == 0): 
            temp = Symmetry.positive_diagonal_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.negative_diagonal_reflection(temp)):
                return True
        elif (move == 2 and a_move == 6): 
            temp = Symmetry.negative_diagonal_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.positive_diagonal_reflection(temp)):
                return True
        elif (move == 7 and a_move == 5):
            temp = Symmetry.negative_diagonal_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.xaxis_reflection(temp)):
                return True
        elif (move == 3 and a_move == 1): 
            temp = Symmetry.negative_diagonal_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.yaxis_reflection(temp)):
                return True
        elif (move == 7 and a_move == 3): 
            temp = Symmetry.positive_diagonal_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.xaxis_reflection(temp)):
                return True
        elif (move == 5 and a_move == 1):
            temp = Symmetry.positive_diagonal_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.yaxis_reflection(temp)):
                return True
        elif (move == 5 and a_move == 3): 
            temp = Symmetry.yaxis_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.xaxis_reflection(temp)):
                return True
        elif (move == 7 and a_move == 1):
            temp = Symmetry.xaxis_reflection(board_state)
            if np.array_equal(board_state, temp) or np.array_equal(board_state, Symmetry.yaxis_reflection(temp)):
                return True

        return False

    # 2 moves can only be symmetric if both on corner or
    # both on side
    def possibly_symmetric(move1, move2):
        return move1 % 2 == move2 % 2

    """ reflections """
    def xaxis_reflection(board_state):
        return np.flip(board_state,0)

    def yaxis_reflection(board_state):
        return np.flip(board_state,1)

    # positive diagonal: y=x
    def positive_diagonal_reflection(board_state):
        return board_state.T

    #negative diagonal: y=-x
    def negative_diagonal_reflection(board_state):
        return np.rot90(np.flip(board_state, 0))