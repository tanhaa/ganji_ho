__author__ = 'Amit & Abtin'

from customexceptions import *


class Player(object):

    def __init__(self, player_id, player_type, token_color):
        playertypes = ['human', 'computer']
        tokencolors = ['white', 'black']
        player_ids = [1, 2]

        try:
            assert player_id in player_ids
            self.id = player_id
        except:
            raise ValueError("Player ID must be an integer for 1 or 2")

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