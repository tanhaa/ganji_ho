__author__ = 'Amit & Abtin'

from board import Board
from customexceptions import *
from player import Player
from tree import Node
from tree import minmax2


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
            self.player2 = Player(2, 'human', 'black')
            self.turn = self.player1

        # TODO: Randomize the player color selection for automatic mode
        # TODO: Assign whose_turn to the white player after randomizing
        if mode is 2:
            self.player1 = Player(1, 'human', 'white')
            self.player2 = Player(2, 'computer', 'black')
            self.turn = self.player1

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
            if self.board.move_available(self.player2.get_player_color()):
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
            print ("The coordinates entered are not valid, they must be of the form A1")
            return False

        try:
            row = ord(move[0].lower()) - 96
            column = int(move[1])
        except:
            print ("There was an error parsing the move coordinates")
            return False

        # place token on the board
        try:
            self.board.place_token(row-1, column-1, self.turn.get_player_color())
        except:
            print("--Invalid token placement!--")
            return False

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

    # ========================#
    # Get Board Size          #
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
        if game.turn.get_player_type() is "human":
            print("It's human player%s's (%s) turn" % (str(game.turn.id), str(game.turn.get_player_color())))
            move = raw_input("player%s, please enter the coordinates for your token placement: "
                             "" % str(game.turn.id))
        else:
            p1 = game.turn
            p2 = game.player2 if game.turn == game.player1 else game.player1
            # print p1
            # print p2

            tree = Node(None, 1, p1, p2, game.board, 0)
            best_val = minmax2(tree, 1, p1, p2)

            if best_val[-1][-1] is None:
                move = best_val[-1][-2]
            print best_val
            print "Computer places its tokens on " + move
            # move = raw_input("player%s, please enter the coordinates for your token placement: "
            #                  "" % str(game.turn.id))

        if not game.make_move(move):
            if game.turn.get_player_type() is "computer":
                print "Computer made an error! It loses."
            else:
                print "Move error, you get only one more chance to make a correct move"
                move = raw_input("player%s, please enter the coordinates for your token placement: "
                                 "" % str(game.turn.id))
                if not game.make_move(move):
                    print "You made another error, too bad you lose!"
                    game.is_game_over = True
                    game.winner = game.player2 if game.turn == game.player1 else game.player1

    # ========================#
    # End Game                #
    # ========================#
    print(game.board)
    print("***Game Over***")
    print("%s Player%s (%s) Wins!" % (str(game.winner.get_player_type()), str(game.winner.id), game.winner.get_player_color()))
