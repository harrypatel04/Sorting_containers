#!/usr/bin/python3
from UnorderedLinkedList import UnorderedLinkedList
from LinkedList import LinkedList
from CLinkedList import CLinkedList
from DLinkedList import DLinkedList
from Queue import Queue
from Deque import Deque
from Stack import Stack


def main():
    a = Queue()

    a.enque(1)
    a.enque(2)
    a.enque(3)
    a.enque(4)

    print(a)

    a.deque()

    print(a)

    a.deque()
    print(a)


if __name__ == '__main__':
    main()
