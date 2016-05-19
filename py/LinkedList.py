from Node import Node


class LinkedList(object):
    """
       Implements an ordered, singularly-linked list.
    """
    def __init__(self, debug=False):
        self.debug = debug
        self._head = None
        self._size = 0

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, val):
        self._head = val

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val

    def insert(self, item):
        curr = self.head
        prev = self.head

        temp = Node(item)
        temp.next = None

        # Empty
        if self.head is None:
            if self.debug:
                print("inserting", item, "into an empty list.")
            self.head = temp
            self.size += 1
            return True

        # Beginning
        if temp.item <= self.head.item:
            if self.debug:
                print("inserting", item, "at beginning of list.")
            temp.next = self.head
            self.head = temp
            self.size += 1
            return True

        # Middle/End
        while curr is not None and curr.item <= temp.item:
            prev = curr
            curr = curr.next

        if self.debug:
            print("inserting", item, "in middle/end of list.")
        prev.next = temp
        temp.next = curr
        self.size += 1
        return True

    def remove(self, n):
        temp = self.head
        prev = self.head
        curr = self.head

        # Empty
        if self.head is None:
            if self.debug:
                print("attempting to remove", n, "from an empty list.")
            return False

        # Beginning
        if self.head.item == n:
            if self.debug:
                print("removing", n, "from beginning of list.")
            self.head = self.head.next
            del temp
            self.size -= 1
            return True

        # Middle/End
        while curr is not None and curr.item != n:
            prev = curr
            curr = curr.next

        if curr is None:
            if self.debug:
                print(n, "not found in list.")
            return False

        if self.debug:
            print("removing", n, "from middle/end of list.")
        prev.next = curr.next
        del curr
        self.size -= 1
        return True

    def is_empty(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self.size)

    def __contains__(self, val):
        for item in self:
            if item == val:
                return True
        return False

    def __getitem__(self, index):
        """
           Returns item at `index`. However, this is an expensive lookup, and
           should only be performed for debugging purposes. (Linked Lists were
           not designed for lookups like this)
        """
        i = 0
        temp = self.head
        item = None

        if index > self.size-1:
            raise IndexError("Index out of range.")
        while temp is not None and i <= index:
            item = temp.item
            temp = temp.next
            i += 1

        return item

    def __len__(self):
        return self.size

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
