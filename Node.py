class SLLNode(object):
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    @property
    def item(self):
        return self.item

    @property
    def next(self):
        return self.next


class CLLNode(object):
    def __init__(self, item=None, _next=None):
        self.item = item
        self.next = _next

    @property
    def item(self):
        return self.item

    @property
    def next(self):
        return self.next


class DLLNode(object):
    def __init__(self, item=None, _next=None, _prev=None):
        self.item = item
        self.next = _next
        self.prev = _prev

    @property
    def item(self):
        return self.item

    @property
    def next(self):
        return self.next

    @property
    def prev(self):
        return self.prev
