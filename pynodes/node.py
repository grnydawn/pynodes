# -*- coding: utf-8 -*-
""" Node classes
"""

class Edge(object):
    """Edgen class
    """

    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.B.edges.append(self)

    def disconnect(self):
        self.B.edges.remove(self)

class Node(object):
    """Node class
    """

    def __init__(self):
        self.edges = []

    @property
    def adj_nodes(self):
        return (e.B for e in self.edges)

    def add_edge(self, B, multiedge=False):

        if not multiedge and B in self.adj_nodes:
            return self.get_edge(B)

        self.edges.append(Edge(self, B))
        return self.edges[-1]

    def remove_edge(self, B):
        if B in self.adj_nodes:
            e = self.get_edge(B)
            self.edges.remove(e)
            e.disconnect()
        
    def get_edge(self, B):
        for e in self.edges:
            if B == e.B:
                return e

class TreeNode(Node):
    """TreeNode class
    """

    pass


class SyntaxTreeNode(TreeNode):
    """SyntaxTreeNode class
    """

    pass
