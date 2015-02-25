__author__ = 'Amit'


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

    def place_token(self, x, y, color):
        """
        Places a token on the board at the given (x,y) coordinate with the given color

        :param x: integer representing the row of the board
        :param y: integer representing the column of the board
        :param color: a character representing the color of the token, either 'w' or 'b'
        :return: Nothing
        """
        if color!= 'w' or color!= 'b':
            raise
        self.board[x][y] = color