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

if __name__ == '__main__':
    print("Select play mode:")
    print("1. Manual")
    print("2. Automatic")

    selection = input("Please enter your selection: ")

    try:
        selections = [1, 2]
        assert selection in selections
    except:
        raise NotAValidSelectionException("You must enter a number (1 or 2) as your selection")

    if selection is 2:
        raise NotImplementedError("This functionality has not been implemented yet")






