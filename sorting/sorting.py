import itertools
import heapq


def swap(x, y):
    x, y = y, x


def heapify(seq, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and seq[child] < seq[child + 1]:
            child += 1
        if seq[root] < seq[child]:
            swap(seq[root], seq[child])
            root = child
        else:
            break


def bubblesort(seq):
    for i in range(len(seq)):
        for k in range(len(seq)-1, i, -1):
            if seq[k] < seq[k-1]:
                seq[k], seq[k-1] = seq[k-1], seq[k]
    return seq


def selectionsort(seq):
    for i, e in enumerate(seq):
        # min() can take a generator expression:
        mn = min(range(i, len(seq)), key=seq.__getitem__)
        seq[i], seq[mn] = seq[mn], e
    return seq


def insertionsort(seq):
    for i in range(1, len(seq)):
        j = i - 1
        key = seq[i]
        while (seq[j] > key) and (j >= 0):
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = key


def mergesort(seq):
    if len(seq) <= 1:
        return seq

    middle = len(seq) // 2
    left = seq[:middle]
    right = seq[middle:]

    left = mergesort(left)
    right = mergesort(right)
    return list(heapq.merge(left, right))


def quicksort(seq):
    if len(seq) < 1:
        return []
    else:
        pivot = seq[0]
        less = [x for x in seq if x < pivot]
        more = [x for x in seq[1:] if x >= pivot]
        return quicksort(less) + [pivot] + quicksort(more)


def heapsort(seq):
    for start in range((len(seq) - 2) // 2, -1, -1):
        heapify(seq, start, len(seq)-1)

    for end in range(len(seq) - 1, 0, -1):
        swap(seq[end], seq[0])
        heapify(seq, 0, end - 1)

    return seq
