import itertools


class Node(object):
    def __init__(self, data, rank):
        self.data = data
        self.rank = rank
        self.parent = self

    def __repr__(self):
        return 'data: {} rank: {} parent: {}'.format(self.data, self.rank, self.parent.data)

    @classmethod
    def node_comp_key(cls, node):
        """A comparison key for sorting by rank"""
        return node.rank


class DisjointSet(object):
    def __init__(self, elems):
        """example: `d = Disjoint((1, 2, 5))`"""
        self.nodes = {}

        if elems:
            for elem in elems:
                self.makeSet(elem)

    def __repr__(self):
        s = ''
        for key in self.nodes:
            s += self.nodes[key].__repr__() + '\n'
        return s

    def makeSet(self, data):
        self.nodes[data] = Node(data, 0)

    def union(self, *elems):
        """Union an arbitrary number (>2) of elements"""
        if len(elems) < 2:
            raise RuntimeError('Must union at least 2 elements')
        for pair in self.__pairwise(elems):
            self.__union(*pair)

    def findSet(self, data):
        temp = self.nodes[data]
        t_repr = self.__find_repr(temp)
        # Path compression
        temp.parent = t_repr
        return t_repr.data

    def __pairwise(self, seq):
        """(s0,s1), (s1,s2), (s2, s3), ..."""
        a, b = itertools.tee(seq)
        next(b, None)
        return zip(a, b)

    def __find_repr(self, node):
        temp = node
        while temp.parent is not temp:
            temp = temp.parent
        return temp

    def __union(self, first, second):
        repr1 = self.findSet(first)
        repr2 = self.findSet(second)

        if repr1 is repr2:
            return

        n1 = self.nodes[repr1]
        n2 = self.nodes[repr2]

        # if the two elements are the same (by the comparison function)
        # the first element encountered is returned, hence orderings in
        # min and max are flipped.
        smaller = min(n1, n2, key=Node.node_comp_key)
        larger = max(n2, n1, key=Node.node_comp_key)

        smaller.parent = larger
        if larger.rank == smaller.rank:
            larger.rank += 1
