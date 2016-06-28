class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.last = None

    def __del__(self):
        pass

    # def __str__(self):
    #     return str(self.item)
