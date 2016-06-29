#!/usr/bin/python3
from sorting import *
import numpy
from time import time


def test_builtin(nums, size):
    start_time = time()
    nums.sort()
    print("Builtin sort. %i items in %f seconds." % (size, time() - start_time))


def test_bubblesort(nums, size):
    start_time = time()
    sorted_items = bubblesort(nums)
    print("Bubble sort. %i items in %f seconds." % (size, time() - start_time))


def test_selectionsort(nums, size):
    start_time = time()
    sorted_items = selectionsort(nums)
    print("Selection sort. %i items in %f seconds." % (size, time() - start_time))


def test_insertionsort(nums, size):
    start_time = time()
    sorted_items = insertionsort(nums)
    print("Insertion sort. %i items in %f seconds." % (size, time() - start_time))


def test_mergesort(nums, size):
    start_time = time()
    sorted_items = mergesort(nums)
    print("Merge sort. %i items in %f seconds." % (size, time() - start_time))


def test_quicksort(nums, size):
    start_time = time()
    sorted_items = quicksort(nums)
    print("Quick sort. %i items in %f seconds." % (size, time() - start_time))


def test_heapsort(nums, size):
    start_time = time()
    sorted_items = heapsort(nums)
    print("Heap sort. %i items in %f seconds." % (size, time() - start_time))


def main():
    size = 5000

    test_builtin(numpy.random.randint(1000, size=size), size)
    test_bubblesort(numpy.random.randint(1000, size=size), size)
    test_selectionsort(numpy.random.randint(1000, size=size), size)
    test_insertionsort(numpy.random.randint(1000, size=size), size)
    test_mergesort(numpy.random.randint(1000, size=size), size)
    test_quicksort(numpy.random.randint(1000, size=size), size)
    test_heapsort(numpy.random.randint(1000, size=size), size)


if __name__ == '__main__':
    main()
