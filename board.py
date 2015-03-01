__author__ = 'Amit'

from customexceptions import NotATileException
from customexceptions import NotAValidMoveException
import pprint as pp


class Board(object):

    def __init__(self, x, y):
        """
        The board contains a board with x X y tiles.

        :param x: integer representing number of rows in the board
        :param y: integer representing number of columns in the board
        :return: object of the type board
        """
        self.board = []
        for n in range(x):
            self.board.append([])
            for m in range(y):
                self.board[n].append(0)

    def __str__(self):
        """
        Override of __str__()

        :return: String representing the board
        """
        s = "    "
        for n in range(len(self.board[0])):
            s += " " + str(n+1) + " "
        s += "\n"
        for n in range(len(self.board)):
            s += chr(n+65) + "  ["
            for m in range(len(self.board[n])):
                s += " " + str(self.board[n][m]) + " "
            s += "]\n"

        return s

    def move_available(self, color):
        """

        :param color:
        :return:
        """
        if color is "white":
            # check if any rows have two consecutive vertical moves available
            for n in range(len(self.board)):
                for m in range(len(self.board[n])):
                    if self.board[n][m] == 0:
                        try:
                            if self.board[n+1][m] == 0:
                                return True
                        except:
                            continue
        if color is "black":
            # check if any column ha two consecutive horizontal moves available
            for n in range(len(self.board)):
                for m in range(len(self.board[n])):
                    if self.board[n][m] == 0:
                        try:
                            if self.board[n][m+1] == 0:
                                return True
                        except:
                            continue

        return False


    def place_token(self, x, y, color):
        """
        Places two tokens on the board at the given (x,y) coordinates for the given color.
        The x represents the row of the board (A, B, C...)
        The y represents the column of the board (1,2,3,4,5...).
        if the tokens are white, they are placed vertically (Top, Down) and the coordinates
        represent the top coordinate.
        if the tokens are black, they are placed horizontally (Left, Right) and the coordinates
        represent the left coordinate.

        :param x: integer representing the row of the board
        :param y: integer representing the column of the board
        :param color: a character representing the color of the token, either 'w' or 'b'
        :return: Nothing
        """
        if color is not 'white' and color is not 'black':
            raise NotATileException("This is not an expected tile color")

        # check if (x,y), (x+1,y), (x,y+1) is occupied
        try:
            if self.board[x][y] is not 0:
                raise NotAValidMoveException("This tile is occupied, not a valid move")

            if color is 'white':
                if self.board[x+1][y] is not 0:
                    raise NotAValidMoveException("This tile is occupied, not a valid move")

                self.board[x][y] = color[0]
                self.board[x+1][y] = color[0]

            if color is 'black':
                if self.board[x][y+1] is not 0:
                    raise NotAValidMoveException("This tile is occupied, not a valid move")
                self.board[x][y] = color[0]
                self.board[x][y+1] = color[0]

        except IndexError:
            raise NotAValidMoveException("Given coordinates are out of the board")