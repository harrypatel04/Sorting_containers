#!/usr/bin/python3
from Node import Node
from DLinkedList import DLinkedList


class Deque(DLinkedList):
    def push_front(self, item):
        temp = Node(item)
        temp.next = None
        temp.last = None

        # Empty
        if self.head is None:
            self.tail = temp
            self.head = temp
            self.size += 1
            return True

        # Front
        self.head.last = temp
        temp.next = self.head
        self.head = temp
        self.size += 1
        return True

    def pop_front(self):
        if self.is_empty():
            return False
        if self.tail is self.head:
            # Last remaining node
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            del temp
            return True

        temp = self.head
        self.head = self.head.next
        self.head.last = None
        self.size -= 1
        del temp
        return True

    def push_back(self, item):
        temp = Node(item)
        temp.next = None

        # Empty
        if self.head is None:
            self.tail = temp
            self.head = temp
            self.size += 1
            return True

        # End
        temp.last = self.tail
        self.tail.next = temp
        self.tail = temp
        self.size += 1
        return True

    def pop_back(self):
        if self.is_empty():
            return False
        if self.tail is self.head:
            # Last remaining node
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            del temp
            return True

        temp = self.tail
        self.tail = self.tail.last
        self.tail.next = None
        self.size -= 1
        del temp
        return True

    def front(self):
        return self.head.item

    def back(self):
        return self.tail.item
