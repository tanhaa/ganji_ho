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


class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
