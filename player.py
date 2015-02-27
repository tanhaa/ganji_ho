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