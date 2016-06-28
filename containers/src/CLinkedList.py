#!/usr/bin/python3
from Node import Node


class CLinkedList(object):
    """
       Implements an ordered, circularly-linked list.
    """
    def __init__(self, debug=False):
        self.debug = debug
        self._tail = None
        self._size = 0

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, val):
        self._tail = val

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val

    def insert(self, item):
        temp = Node(item)
        temp.next = None

        # Empty
        if self.tail is None:
            self.tail = temp
            temp.next = temp
            self.size += 1
            return True

        # Beginning
        if temp.item <= self.tail.next.item:
            temp.next = self.tail.next
            self.tail.next = temp
            self.size += 1
            return True
        curr = self.tail.next
        prev = self.tail.next

        # Traversal
        while curr != self.tail and curr.item <= temp.item:
            prev = curr
            curr = curr.next

        # End
        if temp.item > curr.item:
            temp.next = curr.next
            curr.next = temp
            self.tail = temp
            self.size += 1
            return True

        # Middle
        prev.next = temp
        temp.next = curr
        self.size += 1
        return True

    def remove(self, item):
        prev = self.tail.next
        curr = self.tail.next

        # Empty
        if self.tail is None:
            return False

        # Beginning
        if self.tail.next.item == item:
            # Last remaining node
            if self.tail is self.tail.next:
                self.tail = None
                self.size -= 1
                return True
            # Beginning
            temp = self.tail.next
            self.tail.next = temp.next
            del temp
            self.size -= 1
            return True

        # Traversal
        while curr is not self.tail and curr.item != item:
            prev = curr
            curr = curr.next

        # Not Found
        if curr.item != item:
            return False

        # End
        if curr is self.tail:
            prev.next = curr.next
            self.tail = prev
            del curr
            self.size -= 1
            return True

        # Middle
        prev.next = curr.next
        del curr
        self.size -= 1
        return True

    def is_empty(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self.size)

    def __len__(self):
        return self.size

    def __contains__(self, val):
        for item in self:
            if item == val:
                return True
        return False

    def __repr__(self):
        contents = []
        if self.tail is not None:
            temp = self.tail.next
            while True:
                contents.append(temp.item)
                temp = temp.next
                if temp is self.tail.next:
                    break
        return str(contents)

    def __getitem__(self, index):
        """
           Returns item at `index`. However, this is an expensive lookup, and
           should only be performed for debugging purposes. (Linked Lists were
           not designed for lookups like this)
        """
        i = 0
        item = None
        if self.tail is not None:
            temp = self.tail.next
            if index > self.size-1:
                raise IndexError("Index out of range.")
            while i <= index:
                item = temp.item
                temp = temp.next
                i += 1
                if temp is self.tail.next:
                    break

        return item
