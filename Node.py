

class SLLNode(object):
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next

    @property
    def data(self):
        return self.data

    @property
    def next(self):
        return self.next


class CLLNode(object):
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next

    @property
    def data(self):
        return self.data

    @property
    def next(self):
        return self.next


class DLLNode(object):
    def __init__(self, data=None, _next=None, _prev=None):
        self.data = data
        self.next = _next
        self.prev = _prev

    @property
    def data(self):
        return self.data

    @property
    def next(self):
        return self.next

    @property
    def prev(self):
        return self.prev
