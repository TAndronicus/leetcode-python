from typing import List


def countingSort(l: List[int], k: int):
    amounts = [0] * k
    for el in l:
        amounts[el] += 1
    for i in range(1, k):
        amounts[i] += amounts[i - 1]
    counter, index, res = 0, 0, [0] * len(l)
    while counter < len(l):
        if amounts[index] > counter:
            res[counter] = index
            counter += 1
        else:
            index += 1
    return res


def assertSorted(l: List[int]):
    if len(l) < 2:
        return True
    else:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True


if __name__ == '__main__':
    print(assertSorted(countingSort([0, 2, 3, 1, 1, 5, 2, 3, 1], 6)))
    print(assertSorted(countingSort([0], 1)))
    print(assertSorted(countingSort([6, 5, 4, 3, 2, 1, 0], 7)))
    print(assertSorted(countingSort([1, 1, 1, 1, 1, 1], 2)))
