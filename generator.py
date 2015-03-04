import copy


class Generator(object):
    def __init__(self):
        pass

    def generate(self, color, board):

        temp_board = copy.deepcopy(board)

        board_num_rows = len(board.board)
        board_num_columns = len(board.board[0])

        old_board = copy.deepcopy(temp_board.board)

        list_of_boards = []
        for n in range(board_num_rows):
            for m in range(board_num_columns):
                temp_board.board = copy.deepcopy(old_board)
                try:
                    temp_board.place_token(n, m, color)
                    list_of_boards.append(temp_board.board)
                except:
                    if not temp_board.move_available(color):
                        break
                    continue

        return list_of_boards

