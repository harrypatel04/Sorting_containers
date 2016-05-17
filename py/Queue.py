#!/usr/bin/python3
from Node import Node
from Deque import Deque


class Queue(Deque):
    def enque(self, item):
        Deque.push_back(self, item)

    def deque(self):
        Deque.pop_front(self)

    def front(self):
        return self.head.item
