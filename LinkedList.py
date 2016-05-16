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

    @property
    def size(self):
        return self._size

    def insert(self, item):
        curr = self._head
        prev = self._head

        temp = Node(item)
        temp.next = None

        # Empty
        if self._head is None:
            if self.debug:
                print("inserting", item, "into an empty list.")
            self._head = temp
            self._size += 1
            return

        # Beginning
        if temp.item <= self._head.item:
            if self.debug:
                print("inserting", item, "at beginning of list.")
            temp.next = self._head
            self._head = temp
            self._size += 1
            return

        # Middle/End
        while curr is not None and curr.item <= temp.item:
            prev = curr
            curr = curr.next

        if self.debug:
            print("inserting", item, "in middle/end of list.")
        prev.next = temp
        temp.next = curr
        self._size += 1
        return

    def remove(self, n):
        temp = self._head
        prev = self._head
        curr = self._head

        # Empty
        if self._head is None:
            if self.debug:
                print("attempting to remove", n, "from an empty list.")
            return

        # Beginning
        if self._head.item == n:
            if self.debug:
                print("removing", n, "from beginning of list.")
            self._head = self._head.next
            del temp
            self._size -= 1
            return

        # Middle/End
        while curr is not None and curr.item != n:
            prev = curr
            curr = curr.next

        if curr is None:
            if self.debug:
                print(n, "not found in list.")
            return

        if self.debug:
            print("removing", n, "from middle/end of list.")
        prev.next = curr.next
        del curr
        self._size -= 1
        return

    def is_empty(self):
        return self.__bool__()

    def __bool__(self):
        return bool(self._size)

    def __contains__(self, item):
        temp = self._head
        prev = self._head
        curr = self._head

        while curr is not None and curr.item != item:
            prev = curr
            curr = curr.next

        if curr is None:
            if self.debug:
                print(item, "not found in list.")
            return False
        else:
            if self.debug:
                print(item, "found in list.")
            return True

    def __getitem__(self, index):
        """
           Returns item at `index`. However, this is an expensive lookup, and
           should only be performed for debugging purposes. (Linked Lists were
           not designed for lookups like this)
        """
        i = 0
        temp = self._head
        prev = self._head
        curr = self._head

        while curr is not None and i < index:
            prev = curr
            curr = curr.next
            i += 1

        print("Warning: __getitem__() slow. Use for debugging only")
        return curr.item

    def __len__(self):
        return self._size

    def __repr__(self):
        temp = self._head
        contents = []
        while temp is not None:
            contents.append(temp.item)
            temp = temp.next
        if self.debug:
            return "size: " + str(self._size) + " contents: " + str(contents)
        else:
            return str(contents)

    def __str__(self):
        return self.__repr__()
