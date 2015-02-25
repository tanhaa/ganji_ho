__author__ = 'Amit'

from exceptions import NotATileException
from exceptions import NotAValidMoveException
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
        # ToDo: make a better represenation with headers for rows/columsn
        return pp.pformat(self.board)

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
        if color is not 'w' and color is not 'b':
            raise NotATileException("This is not an expected tile color")

        # check if (x,y), (x+1,y), (x,y+1) is occupied
        if self.board[x][y] is not 0:
            raise NotAValidMoveException("This tile is occupied, not a valid move")
        if color is 'w' and self.board[x+1][y] is not 0:
            raise NotAValidMoveException("This tile is occupied, not a valid move")
        else:
            self.board[x][y] = color
            self.board[x+1][y] = color

        if color is 'b' and self.board[x][y+1] is not 0:
            raise NotAValidMoveException("This tile is occupied, not a valid move")
        else:
            self.board[x][y] = color
            self.board[x][y+1] = color