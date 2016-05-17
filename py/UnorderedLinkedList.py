#!/usr/bin/python3
from LinkedList import LinkedList
from Node import Node


class UnorderedLinkedList(LinkedList):
    def insert(self, item):
        temp = Node(item)
        temp.next = None

        # Empty
        if self._head is None:
            if self.debug:
                print("inserting", item, "into an empty list.")
            self._head = temp
            self._size += 1
            return True

        # Beginning
        if self.debug:
            print("inserting", item, "at beginning.")
        temp.next = self._head
        self._head = temp
        self._size += 1
        return True

    def remove(self, n):
        temp = self._head
        prev = self._head
        curr = self._head

        # Empty
        if self._head is None:
            if self.debug:
                print("attempting to remove", n, "from an empty list.")
            return False

        # Beginning
        if self._head.item == n:
            if self.debug:
                print("removing", n, "from beginning of list.")
            self._head = self._head.next
            del temp
            self._size -= 1
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
        self._size -= 1
        return True
