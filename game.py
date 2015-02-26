__author__ = 'Amit'

from board import Board
from customexceptions import *
from player import Player

class Game(object):

    def __init__(self, mode):
        if mode is 1:
            self.player1 = Player(


if __name__ == '__main__':
    print("Select play mode:")
    print("1. Manual")
    print("2. Automatic")

    selection = input("Please enter your selection: ")

    try:
        selection = int(selection)
    except ValueError:
        raise NotAValidSelectionException("You must enter a number as your selection")

    if selection is not 1 and selection is not 2:
        raise NotAValidSelectionException("You must select 1 or 2 as a selection")

    if selection is 2:
        raise NotImplementedError("This functionality has not been implemented yet")

    # create the players


