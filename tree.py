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
from sys import maxsize

def convert_to_alphamove(n, m):
    row_letter = chr(n+1+96)
    column_number = m+1
    move = row_letter.upper() + str(column_number)
    return move


class Node(object):
    def __init__(self, move, depth, player1, player2, board, value):
        self.best_move = ""
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
            # generate the list of boards
            list_of_boards = self.generate(self.player.get_player_color())

            # ====Debug====
            # list_of_moves = []
            # for i in range(len(list_of_boards)):
            #     h_value = self.calculate_heuristic_value(list_of_boards[i]["board"])
            #     s = list_of_boards[i]["move"] + " (" + str(h_value) + ")"
            #     list_of_moves.append(s)
            # print self.depth
            # print list_of_moves

            for i in range(len(list_of_boards)):
                # print(list_of_boards)
                sub_move = list_of_boards[i]["move"]
                sub_board = list_of_boards[i]["board"]
                v = self.calculate_heuristic_value(sub_board)
                self.children.append(Node(sub_move, self.depth-1, self.player2, self.player, sub_board, v))

    def calculate_heuristic_value(self, board):
        if board.is_board_terminal():
            return maxsize if self.player.get_player_color() == 'white' else -maxsize
        else:
            return board.num_moves_available('white') - board.num_moves_available('black')

    def generate(self, color):
        """

        :param color:
        :return:
        :rtype: list
        """
        # deep copy the board object.
        temp_board = copy.deepcopy(self.board)
        initial_state = [row[:] for row in temp_board.board]
        list_of_boards = []
        for n in range(len(temp_board.board)):
            for m in range(len(temp_board.board[0])):
                # temp_board.board = copy.deepcopy(initial_state)
                temp_board.board = [row[:] for row in initial_state]
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
        ret = "Move: " + str(self.move)
        ret += "\nPlayer: " + str(self.player)
        ret += "\nPlayer2: " + str(self.player2)
        ret += "\nValue: " + str(self.value)
        ret += "\n" + str(self.board)
        moves = []
        for child in self.children:
            moves.append(child)

        ret += "\n" + str(moves)

        return ret


def minmax2(node, depth, player, player2):
    """
    This method will call the appropriate minmax method depending on the color of the player.
    Help source: http://www.hamedahmadi.com/gametree/
    :param node: Tree, type Node
    :param depth: how deep do we want to go? Integer, 0 = root only.
    :param player: Player whose move it is
    :param player2: The other player.
    :return: a tuple with the heuristic value at index 0 and list of moves at index 1
    """
    if player.get_player_color() == 'white':
        val = minmax_white(node, depth, player, player2)
    else:
        val = minmax_black(node, depth, player, player2)

    return val


def minmax_white(node, depth, player, player2):
    """

    :param node:
    :param depth:
    :param player:
    :param player2:
    :return:
    """
    if depth == 0 or abs(node.value) == maxsize:
        # print str(node.value) + " * " + str(player.get_player_color()) + " for white " + str(node.move)
        return (node.value, [node.move])
    max_val = (-maxsize, [node.move])
    # print "Setting max_val to " + str(max_val)
    for child in node.children:
        # print "I'm in the white loop for " + child.move
        val = minmax_black(child, depth - 1, player2, player)
        # print "Found val " + str(val) + " for " + str(player.get_player_color())
        if val[0] > max_val[0]:
            val[1].append(node.move)
            max_val = val
            # print "Changed bestValue to val above"
        # elif val[0] == max_val[0]: # this is we really have no moves that are good, pick the first one
        #     if len(max_val[1]) == 1:
        #         if max_val[1][0] is None:
        #             max_val[1].append(val[1][-1])

    # print "Returning bestValue " + str(max_val)
    return max_val


def minmax_black(node, depth, player, player2):
    """

    :param node:
    :param depth:
    :param player:
    :param player2:
    :return:
    """
    if depth == 0 or abs(node.value) == maxsize:
        # print str(node.value) + " * " + str(player.get_player_color()) + " for black " + str(node.move)
        return (node.value, [node.move])
    min_val = (maxsize, [node.move])
    # print "Setting min_val to " + str(min_val) + " " + str(len(min_val[1]))
    for child in node.children:
        # print "I'm in the black loop for " + child.move
        val = minmax_white(child, depth - 1, player2, player)
        # print "Found val " + str(val) + " for " + str(player.get_player_color())
        if val[0] < min_val[0]:
            val[1].append(node.move)
            min_val = val
            # print "Changed bestValue to val above"
        # elif val[0] == min_val[0]:
        #     # print str(min_val)
        #     if len(min_val[1]) == 1:
        #         if min_val[1][0] is None:
        #             min_val[1].append(val[1][-1])

    # print "Returning bestValue " + str(min_val)
    return min_val


def minmax(node, depth, player, player2):
    if depth == 0 or abs(node.value) == maxsize:
        print str(node.value) + " * " + str(player.id) + " for " + str(node.move)
        sign_val = 1
        if player.id is 2:
            sign_val = -1
        return (node.value * sign_val, [node.move])

    best_value = (-maxsize, None)

    for child in node.children:
        # print "I'm in the loop for " + child.move
        val = minmax(child, depth - 1, player2, player)
        # print "Found val " + str(val) + " for " + str(player.id)
        if -val[0] > best_value[0]:
            if val[1]:
                val[1].append(node.move)
            best_value = val
            # print "Changed bestValue to val above"

    # print "Returning bestValue " + str(best_value)
    return best_value