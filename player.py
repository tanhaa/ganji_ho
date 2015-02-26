__author__ = 'Amit'

from customexceptions import *


class Player(object):

    def __init__(self, player_type, color):
        try:
            assert isinstance(player_type, int)
            self.player_type = player_type
        except:
            raise NotAValidPlayerTypeException("Player type must be 1 (human) or 2 (computer)")

        if color is not 'black' and color is not 'white':
            raise NotAValidTokenColorException("Token color must be black or white")
        else:
            self.color = color

        if color is 'white':
            self.turn = True
        else:
            self.turn = False

    def is_turn(self):
        """
        Returns a boolean indicating if it's the current player's turn or not
        :return: boolean
        """
        return self.turn

    def get_player_type(self):
        """
        Returns tye type of player
        :return: string
        """

        if self.type is 1:
            return "Human"
        if self.type is 2:
            return "Computer"


