from typing import List


def quicksort(l: List[int]):
    quicksortI(l, 0, len(l) - 1)


def quicksortI(l: List[int], start: int, end: int):
    if end - start < 2:
        if (end - start == 1) and (l[start] > l[end]):
            swap(l, start, end)
        return
    index, last = start + 1, end
    while index <= last:
        if l[index] > l[start]:
            swap(l, index, last)
            last -= 1
        else:
            index += 1
    swap(l, start, last)
    quicksortI(l, start, last - 1)
    quicksortI(l, last + 1, end)


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
    quicksort(l)
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
