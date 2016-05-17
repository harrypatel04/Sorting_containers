#!/usr/bin/python3
from Node import Node
from UnorderedLinkedList import UnorderedLinkedList


class Stack(UnorderedLinkedList):

    def peek(self):
        return self._head.item

    def top(self):
        return peek(self)

    def push(self, item):
        self.insert(item)

    def pop(self):
        item = self.peek()
        self.remove(item)
        return item
