from typing import List


def left(n: int):
    return 2 * (n + 1) - 1


def right(n: int):
    return 2 * (n + 1)


def maxHeapify(l: List[int], index: int, heapSize: int):
    max, maxIndex = l[index], index
    if left(index) < heapSize and l[left(index)] > max:
        max, maxIndex = l[left(index)], left(index)
    if right(index) < heapSize and l[right(index)] > max:
        max, maxIndex = l[right(index)], right(index)
    if index != maxIndex:
        swap(l, index, maxIndex)
        maxHeapify(l, maxIndex, heapSize)


def buildMaxHeap(l: List[int]):
    for i in range(int(len(l) / 2), -1, -1):
        maxHeapify(l, i, len(l))


def heapsort(l: List[int]):
    if len(l) == 0:
        return
    buildMaxHeap(l)
    for i in range(len(l) - 1, 0, -1):
        swap(l, 0, i)
        maxHeapify(l, 0, i)


def swap(l: List[int], left: int, right: int):
    if left == right:
        return
    l[left], l[right] = l[right], l[left]


def assertSorted(l: List[int]):
    if len(l) < 2:
        return True
    else:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True


def sortAndAssert(l: List[int]):
    heapsort(l)
    print(l)
    return assertSorted(l)


if __name__ == '__main__':
    print(sortAndAssert([1, 2]))
    print(sortAndAssert([2, 1]))
    print(sortAndAssert([2]))
    print(sortAndAssert([]))
    print(sortAndAssert([11, 3, 2, 5, 7, 56, 2]))
    print(sortAndAssert([1, 2, 3, 4, 7, 8, 9]))
    print(sortAndAssert([9, 8, 7, 6, 5, 4, 3, 2]))
    print(sortAndAssert([2, 2, 2, 2, 2]))
