#!/usr/bin/python3
from UnorderedLinkedList import UnorderedLinkedList
from LinkedList import LinkedList
from Stack import Stack


def main():
    a = Stack(debug=False)

    a.push(1)
    a.push(2)
    a.push(1+7j)
    a.push('cat')

    print(a)

    print(a.peek())
    print(a)

    a.pop()
    print(a)


if __name__ == '__main__':
    main()
