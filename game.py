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
            self.turn = self.player1

        # TODO: Randomize the player color selection for automatic mode
        # TODO: Assign whose_turn to the white player after randomizing
        if mode is 2:
            self.player1 = Player('human', 'white')
            self.player2 = Player('computer', 'black')

        self.board = Board(board_size_x, board_size_y)
        self.is_game_over = False
        self.winner = None

    def post_move_processing(self, color):
        return self.board.move_available(color)

    def whose_turn(self):
        return ["Player1", self.player1] if self.turn is self.player1\
            else ["Player2", self.player2]

    def make_move(self, move):

        if not self.is_move_valid(move):
            raise NotAValidMoveException("The coordinates entered are not valid, they must be of the form A1")

        try:
            row = ord(move[0].lower()) - 96
            column = int(move[1])
        except:
            raise NotAValidMoveException("There was an error parsing the coordinates")

        # place token on the board
        try:
            self.board.place_token(row-1, column-1, self.whose_turn()[1].get_player_color())
        except:
            # TODO so if an invalid move is made, an exception will be raised
            # if AI makes that error, it loses
            # if human makes it, it gets another chance to play, else it loses
            pass

        # set the turn for next player
        if "1" in self.whose_turn()[0]:
            self.player2.set_next(True)
            self.player1.set_next(False)
            # TODO: check if black will have an available move next or not
        else:
            self.player1.set_next(True)
            self.player2.set_next(False)
            # TODO: check if white will have an available move next or not

    def is_move_valid(self, move):
        if len(move) is not 2:
            return False
        if not move[0].isalpha():
            return False
        if not move[1].isdigit():
            return False

        return True
        

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
        print("It's %s's turn" % game.whose_turn()[0])
        move = raw_input("%s, please enter the coordinates for your token placement: "
                         "" % game.whose_turn()[0])
        game.make_move(move)