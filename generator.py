import copy
from tree import Node
from board import Board


class Generator(object):
    def __init__(self, board):
        self.board = board
        self.board_x = len(self.board.board)
        self.board_y = len(self.board.board[0])
        pass

    def generate(self, color):
        """

        :param color:
        :return:
        """

        temp_board = copy.deepcopy(self.board)
        old_board = copy.deepcopy(temp_board.board)

        list_of_boards = []
        for n in range(self.board_x):
            for m in range(self.board_y):
                temp_board.board = copy.deepcopy(old_board)
                try:
                    temp_board.place_token(n, m, color)
                    list_of_boards.append(temp_board.board)
                except:
                    if not temp_board.move_available(color):
                        break
                    continue

        return list_of_boards

    def create_tree(self, depth=1):

        # TODO: this color needs to be given to the generator class
        color = 'white'

        # Generate the next set of boards coming from the given board
        list_of_boards = self.generate(color)
        list_of_board_objects = []

        for board in list_of_boards:
            temp_b = Board(self.board_x, self.board_y)
            temp_b.board = copy.deepcopy(board)
            list_of_board_objects.append(temp_b)


        tree = Node(self.board, list_of_board_objects)

        return tree
