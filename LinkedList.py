from Node import SLLNode as Node


class LinkedList(object):
    __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, item, position=0):
        # TODO: insert at a given position
        new_node = Node(item)
        new_node.head = self.head
        self.head = new_node

    def size(self):
        return self.size

    def remove(self, item, position=0):
        pass

    def is_empty(self):
        # TODO: Possibly replace this with __bool__()
        return False

    def __contains__(self, item):
        pass

    def __repr__(self):
        pass

    def __getitem__(self, index):
        pass

    def __iter__(self):
        # TODO: figure out what this does
        pass

    def __len__(self):
        return self.size

    def __add__(self, other):
        # TODO: find if you can use this to call self.insert()
        pass

    def __sub__(self, other):
        pass
