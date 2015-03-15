"""
source: http://cbio.ufs.ac.za/live_docs/nbn_tut/trees.html
Usage examples:
tree = Node("grandmother", [
    Node("daughter", [
        Node("granddaughter"),
        Node("grandson")]),
    Node("son", [
        Node("granddaughter"),
        Node("grandson")])
    ]);

print tree
'grandmother'
    'daughter'
        'granddaughter'
        'grandson'
    'son'
        'granddaughter'
        'grandson'

"""
import copy


def convert_to_alphamove(n, m):
    row_letter = chr(n+1+96)
    column_number = m+1
    move = row_letter.upper() + str(column_number)
    return move


class Node(object):
    def __init__(self, move, depth, player1, player2, board, value):
        self.move = move
        self.depth = depth
        self.player = player1
        self.player2 = player2
        self.board = board
        self.value = value
        self.children = []
        self.create_children()

    def create_children(self):

        if self.depth >= 0:
            #generate the list of boards
            list_of_boards = self.generate(self.player.get_player_color())

            list_of_moves = []
            for i in range(len(list_of_boards)):
                list_of_moves.append(list_of_boards[i]["move"])
            print list_of_moves

            for i in range(len(list_of_boards)):
                # print(list_of_boards)
                v = self.value # change it with heuristic
                sub_move = list_of_boards[i]["move"]
                sub_board = list_of_boards[i]["board"]
                print sub_move
                print sub_board
                self.children.append(Node(sub_move, self.depth-1, self.player2, self.player, sub_board, v))

    def calculate_heuristic_value(self):
        pass

    def generate(self, color):
        """

        :param color:
        :return:
        :rtype: list
        """
        # deep copy the board object.
        temp_board = copy.deepcopy(self.board)
        initial_state = copy.deepcopy(temp_board.board)
        list_of_boards = []
        for n in range(len(temp_board.board)):
            for m in range(len(temp_board.board[0])):
                temp_board.board = copy.deepcopy(initial_state)
                try:
                    temp_board.place_token(n, m, color)
                    move = convert_to_alphamove(n, m)
                    list_of_boards.append({"move": move, "board": copy.deepcopy(temp_board)})
                except:
                    if not temp_board.move_available(color):
                        break
                    continue

        return list_of_boards

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.move) + " " + repr(self.player) + " " + \
              repr(self.player2) + " " + repr(self.value) + " " + \
              + "\n" + repr(self.board) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
