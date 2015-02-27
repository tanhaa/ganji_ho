__author__ = 'Amit'

from customexceptions import *


class Player(object):

    def __init__(self, player_type, token_color):
        playertypes = ['human', 'computer']
        tokencolors = ['white', 'black']
        try:
            assert player_type.lower() in playertypes
            self.player_type = player_type
        except:
            raise NotAValidPlayerTypeException("Player type must be Human or Computer")

        try:
            assert token_color.lower() in tokencolors
            self.token_color = token_color
        except:
            raise NotAValidTokenColorException("Token color must White or Black")

        if self.token_color is tokencolors[0]:
            self.turn = True
        else:
            self.turn = False

    def is_next(self):
        """
        Returns a boolean indicating if it's the current player's turn or not
        :return: boolean
        """
        return self.turn

    def set_next(self, boolean):
        """

        :return:
        """
        self.turn = boolean

    def get_player_type(self):
        """
        Returns tye type of player
        :return: string
        """
        return self.player_type

    def get_player_color(self):
        """

        :param selfself:
        :return:
        """
        return self.token_color


