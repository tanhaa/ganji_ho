__author__ = 'Amit'

from board import Board
from customexceptions import *
from player import Player


class Game(object):

    def __init__(self, mode, board_size_x, board_size_y):
        modes = [1, 2]
        try:
            assert mode in modes
        except:
            raise NotAValidModeException("Please provide a correct mode: 1(manual) or 2(automatic)")

        if mode is 1:
            self.player1 = Player('human', 'white')
            self.player2 = Player('human', 'black')

        if mode is 2:
            self.player1 = Player('human', 'white')
            self.player2 = Player('computer', 'black')

        self.board = Board(board_size_x, board_size_y)

    def is_game_over(self):
        return False

    def whose_turn(self):
        return "Player1" if self.player1.is_next() else "Player2"

if __name__ == '__main__':
    print("Select play mode:")
    print("1. Manual")
    print("2. Automatic")

    try:
        selected_mode = int(raw_input("Please enter your selection: "))
        selections = [1, 2]
        if selected_mode not in selections:
            selected_mode = int(raw_input("You must enter a number (1 or 2) as your "
                                      "selection, try again: "))
        assert selected_mode in selections
    except:
        raise NotAValidSelectionException("You crashed the program!! You must "
                                          "enter a number (1 or 2) as your selection")
    if selected_mode is 2:
        raise NotImplementedError("This functionality has not been implemented yet!")

    try:
        board_rows = int(raw_input("Please enter the desired number of rows on the board: "))
        board_columns = int(raw_input("Please enter the desired number of columns on the board: "))
    except:
        raise ValueError("AW Crap! Stop entering non-integer values for the size of the"
                         "board! you crashed the program!")

    game = Game(selected_mode, board_rows, board_columns)

    while not game.is_game_over():
        print(game.board)
        print("It's %s's turn" % game.whose_turn())
        move = raw_input("%s, please enter the coordinates for your token placement: "
                         "" % game.whose_turn())





