#!/usr/bin/python3
from disjoint import DisjointSet


def main():
    elems = range(1, 100)
    d = DisjointSet(elems)
    d.union(1, 2, 5)
    print(d.findSet(1))
    print(d.findSet(2))
    print(d.findSet(5))
    print(d.findSet(3))

if __name__ == '__main__':
    main()
