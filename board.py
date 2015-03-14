__author__ = 'Amit & Abtin'

from customexceptions import NotATileException
from customexceptions import NotAValidMoveException


class Board(object):

    def __init__(self, x, y):
        """
        The board contains a board with x X y tiles. x Represents the number of rows and y represents the number
        of columns

        :param x: integer representing number of rows in the board
        :param y: integer representing number of columns in the board
        :return: object of the type board
        :rtype: Board
        """
        self.board = []
        for n in range(x):
            self.board.append([])
            for m in range(y):
                self.board[n].append(0)

    def __repr__(self):
        """
        Override of __repr__()

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
        This method checks if there is a move available for the player with the given color token.  For white players
        it checks if there are any two consecutive vertical tiles free for a move. For black players, it checks if
        there are any two horizontal tiles available and free for a move

        :param color: string "white" or "black" only
        :return: True if move is availlable, False if not
        :rtype: bool
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

    def _is_tile_occupied(self, x, y, color):
        """
        Checks to see if the given tile at x and y (row and column) for the given color is available for a more or not.
        It will also check the approprate second tile for the given color as well.  It does not return anything but if
        the tile is occupied or if the given coordinates are out of the board, it will raise "NotAValidMoveException"

        :param x: row  (integer)
        :param y: column (integer)
        :param color: string "white" or "black"
        """
        try:
            if self.board[x][y] is not 0:
                raise NotAValidMoveException("This tile is occupied, not a valid move")
            if color is 'white':
                if self.board[x+1][y] is not 0:
                    raise NotAValidMoveException("This tile is occupied, not a valid move")
            if color is 'black':
                if self.board[x][y+1] is not 0:
                    raise NotAValidMoveException("This tile is occupied, not a valid move")
        except IndexError:
            raise NotAValidMoveException("Given coordinates are out of the board")

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
        """
        if color is not 'white' and color is not 'black':
            raise NotATileException("This is not an expected tile color")

        # check if (x,y), (x+1,y), (x,y+1) is occupied
        try:
            self._is_tile_occupied(x, y, color)
            if color is 'white':
                self.board[x][y] = color[0]
                self.board[x+1][y] = color[0]
            if color is 'black':
                self.board[x][y] = color[0]
                self.board[x][y+1] = color[0]
        except Exception as e:
            raise NotAValidMoveException(e.message)