__author__ = 'Amit & Abtin'

from board import Board
from customexceptions import *
from player import Player


def is_move_valid(move):
    """
    This is a sanity method to check if the move made is valid or not.  A valid move must be of the form A1 or C2. It
    must be a string of 2 characters, where the first character is a letter between A and Z and the second character
    is a number.  The first letter indicates the row on the board and the second the column on the board.
    It returns false if any of these conditions are violated.
    :param move:  A string of length 2
    :return:  True if valid, false if invalid
    :rtype : bool
    """
    if len(move) is not 2:
        return False
    if not move[0].isalpha():
        return False
    if not move[1].isdigit():
        return False
    return True


class Game(object):

    def __init__(self, mode, board_size_x, board_size_y):
        """
        This method initializes the game with the given mode, automatic or manual. If the mode is manual, it creates
        two human players, player1 is assigned white and player2 is assigned black.  If the mode is automatic, it
        creates two players, player1 is assigned white and is a human player, player2 is assigned black and is an AI
        player.  It creates a board wth the given x (rows) and y(columns) values.

        :param mode:  Integer 1 -> Manual  2-> Automatic
        :param board_size_x: Integer >= 2
        :param board_size_y: Integer >= 2
        :return: A game object
        :rtype : Game
        """
        modes = [1, 2]
        try:
            assert mode in modes
        except:
            raise NotAValidModeException("Please provide a correct mode: 1(manual) or 2(automatic)")

        if mode is 1:
            self.player1 = Player(1, 'human', 'white')
            self.player2 = Player(-1, 'human', 'black')
            self.turn = self.player1

        # TODO: Randomize the player color selection for automatic mode
        # TODO: Assign whose_turn to the white player after randomizing
        if mode is 2:
            self.player1 = Player(1, 'human', 'white')
            self.player2 = Player(-1, 'computer', 'black')

        self.board = Board(board_size_x, board_size_y)
        self.is_game_over = False
        self.winner = None

    def _post_move_processing(self):
        """
        This method is called after every move to see if there is a move available for the next player.  If no move
        is available, this method turns the boolean flag of is_game_over to True and assigns the current player as
        the winner of the game.  It will make a call to the method "move_available" in the board class.
        :rtype : None
        """
        # check if there is a move available for next player
        if self.player1 == self.turn:
            if self.board.mo(self.player2.get_player_color()):
                self.turn = self.player2
            else:
                self.is_game_over = True
                self.winner = self.player1
        else:
            if self.board.move_available(self.player1.get_player_color()):
                self.turn = self.player1
            else:
                self.is_game_over = True
                self.winner = self.player2

    def make_move(self, move):
        """

        :param move:
        :return:
        """

        if not is_move_valid(move):
            raise NotAValidMoveException("The coordinates entered are not valid, they must be of the form A1")

        try:
            row = ord(move[0].lower()) - 96
            column = int(move[1])
        except:
            raise NotAValidMoveException("There was an error parsing the move coordinates")

        # place token on the board
        try:
            self.board.place_token(row-1, column-1, self.turn.get_player_color())
        except:
            # TODO so if an invalid move is made, an exception will be raised
            # if AI makes that error, it loses
            # if human makes it, it gets another chance to play, else it loses
            # ----------------------------------------------------------------
            # For iteration 1, if an error is made, turn is simply skipped
            print("--Invalid token placement, forfeiting turn!--")
            return False
            # ----------------------------------------------------------------

        # do post move processing, set turn and check win condition
        self._post_move_processing()
        return True

if __name__ == '__main__':
    # ========================#
    # Get Play Mode           #
    # ========================#
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

    # ========================#
    # Get Play Mode           #
    # ========================#
    try:
        board_rows = int(raw_input("Please enter the desired number of rows on the board: "))
        board_columns = int(raw_input("Please enter the desired number of columns on the board: "))
    except:
        raise ValueError("AW Crap! Stop entering non-integer values for the size of the"
                         "board! you crashed the program!")

    # ========================#
    # Start Game              #
    # ========================#
    game = Game(selected_mode, board_rows, board_columns)

    # ========================#
    # Get Turns (Play game)   #
    # ========================#

    while not game.is_game_over:
        print(game.board)
        print("It's player%s's turn" % str(game.turn.id))
        move = raw_input("player%s, please enter the coordinates for your token placement: "
                         "" % str(game.turn.id))
        game.make_move(move)

    # ========================#
    # End Game                #
    # ========================#
    print(game.board)
    print("***Game Over***")
    print("Player%s Wins!" % game.winner.id)