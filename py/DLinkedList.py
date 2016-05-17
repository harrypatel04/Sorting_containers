#!/usr/bin/python3
from Node import Node


class DLinkedList(object):
    def __init__(self):
        self.debug = False
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, val):
        self._head = val

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, val):
        self._tail = val

    def insert(self, item):
        temp = Node(item)
        temp.next = None
        temp.last = None

        # Empty
        if self.head is None:
            self.head = temp
            self.tail = temp
            self.size += 1
            return True

        # Beginning
        if temp.item <= self.head.item:
            temp.next = self.head
            self.head.last = temp
            self.head = temp
            self.size += 1
            return True

        prev = self.head
        curr = self.head

        # Traversal
        while curr is not None and curr.item <= temp.item:
            prev = curr
            curr = curr.next

        # End
        if curr is None:
            prev.next = temp
            temp.last = prev
            self.tail = temp
            self.size += 1
            return True

        # Middle
        prev.next = temp
        temp.next = curr
        curr.last = temp
        temp.last = prev
        self.size += 1
        return True

    def remove(self, item):
        temp = self.head
        prev = self.head
        curr = self.head

        # Empty
        if self.head is None:
            return False

        # Beginning
        if self.head.item == item:
            # Last remaining node
            if self.head.next is None:
                # del self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return True

            # Beginning
            self.head = self.head.next
            self.head.last = None
            del temp
            self.size -= 1
            return True

        # Traversal
        while curr is not None and curr.item != item:
            prev = curr
            curr = curr.next

        # Not found
        if curr.item != item:
            return False

        # End
        if curr is None:
            prev.next = None
            self.tail = prev
            del curr
            self.size -= 1
            return True

        # Middle
        prev.next = curr.next
        curr.next.last = prev
        del curr
        self.size -= 1
        return True

    def is_empty(self):
        return self.__bool__()

    def __bool__(self):
        return self.head is None

    def __len__(self):
        return self.size

    def __contains__(self, item):
        for item in self:
            if item == val:
                return True
        return False

    def __repr__(self):
        temp = self.head
        contents = []
        while temp is not None:
            contents.append(temp.item)
            temp = temp.next
        if self.debug:
            return "size: " + str(self.size) + " contents: " + str(contents)
        else:
            return str(contents)

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, index):
        """
           Returns item at `index`. However, this is an expensive lookup, and
           should only be performed for debugging purposes. (Linked Lists were
           not designed for lookups like this)
        """
        i = 0
        temp = self.head

        if index > self.size-1:
            raise IndexError("Index out of range.")
        while temp is not None and i <= index:
            item = temp.item
            temp = temp.next
            i += 1

        return item
