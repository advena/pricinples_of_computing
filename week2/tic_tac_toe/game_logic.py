"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3
DRAW = 4

# Add your functions here.

def mc_trial(board_clone, player):
    """
    This is the trial game for given board and player position
    Function does not return anything only changes are made in board where you can find the status of finished game
    """

    while not board_clone.check_win():
        possible_moves = board_clone.get_empty_squares()
        row, column = possible_moves[get_next_move(possible_moves)]
        board_clone.move(row, column, player)
        player =provided.switch_player(player)

    return


def get_next_move(possible_moves):
    """
    Returns the index of next possible move according to the list of squares provided
    """

    index_of_next_move = possible_moves[random.randrange(0, len(possible_moves))]
    return possible_moves.index(index_of_next_move)


def mc_update_scores(scores, board, player):
    """
    Updates the scores with given board.
    """
    dimension = board.get_dim()
    winner = board.check_win()
    if winner == DRAW or winner == None:
        return

    for row in range(dimension):
        for column in range(dimension):
            square_status = board.square(row, column)
            if winner == PLAYERO:
                if square_status == PLAYERO:
                    scores[row][column] += MCOTHER
                elif square_status == PLAYERX:
                    scores[row][column] -= MCMATCH
            else:
                if square_status == PLAYERX:
                    scores[row][column] += MCMATCH
                elif square_status == PLAYERO:
                    scores[row][column] -= MCOTHER

    return


def get_best_move(board, scores):
    """
    Returns randomly best possible move according to the score grid of the previous game simulations
    The output is a tuple of (row, column) for the best move
    """

    possible_moves_with_scores = {}
    possible_best_moves = []
    empty_squares = board.get_empty_squares()
    dim = board.get_dim()
    for row in range(dim):
        for column in range(dim):
            current_score = scores[row][column]
            current_square = (row, column)
            if current_square in empty_squares:
                possible_moves_with_scores[current_square] = current_score

    highest_score_position = max(possible_moves_with_scores.values())

    for position in possible_moves_with_scores.keys():
        if possible_moves_with_scores[position] == highest_score_position:
            possible_best_moves.append(position)

    return possible_best_moves[random.randrange(len(possible_best_moves))]


def mc_move(board, player, trials):
    """
    Function runs the Monte Carlo simulation of number of trials, with given board and player and return the next move
    """

    scores = []
    while trials > 0:
        current_board = board.clone
        mc_trial(current_board, player)
        mc_update_scores(scores, current_board, player)
        trials -= 1


    return get_best_move(board, scores)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

if __name__ == '__main__':
    board = provided.TTTBoard(2, False, [[EMPTY, EMPTY], [EMPTY, EMPTY]])
    print mc_trial(board, 2)
    print board
    print board.check_win()
