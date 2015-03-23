import cProfile
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func

@do_cprofile
def expensive_function():
    from board import Board
    from tree import Node
    from player import Player
    from tree import minmax2
    from time import time
    b = Board(8,8)
    p1 = Player(1, 'human', 'white')
    p2 = Player(2, 'human', 'black')
    t = time()
    tree = Node(None, 2, p1, p2, b, 0)
    print "Tree Time took: ", time()-t
    t = time()
    print minmax2(tree, 2, p1, p2)
    print "Minmax Time took: ", time()-t

expensive_function()
