from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    rev = -1
    while (rev > - len(nums)) and (nums[rev] <= nums[rev - 1]):
        rev -= 1
    if rev == -len(nums):
        nums[:] = nums[::-1]
        return
    tmp = nums[rev - 1:]
    nums[rev - 1] = cutOutSmallestLarger(tmp, nums[rev - 1])
    nums[rev:] = sorted(tmp)


def cutOutSmallestLarger(nums: List[int], a: int) -> int:
    counter, min = None, None
    for i in range(1, len(nums)):
        if (nums[i] > a) and ((min is None) or (min > nums[i])):
            counter, min = i, nums[i]
    if counter is None:
        counter, min = nums.index(a), a
    del nums[counter]
    return min


def checker(input, expected):
    nextPermutation(input)
    print(input == expected)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(cutOutSmallestLarger(l, 3) == 4)
    print(l == [1, 2, 3, 5])
    print(cutOutSmallestLarger([1, 2, 3, 4, 5], 4) == 5)
    print(cutOutSmallestLarger([1, 2, 3, 4, 5], 1) == 2)
    print(sorted([2, 1, 3, 5, 4]) == [1, 2, 3, 4, 5])
    checker([1, 2, 5, 4, 3], [1, 3, 2, 4, 5])
    checker([1, 2, 5, 3, 4], [1, 2, 5, 4, 3])
    checker([1, 5, 4, 3, 2], [2, 1, 3, 4, 5])
    checker([1, 2], [2, 1])
    checker([1], [1])
    checker([2, 1], [1, 2])
    checker([1, 2, 3], [1, 3, 2])
    checker([3, 2, 1], [1, 2, 3])
    checker([1, 1, 5], [1, 5, 1])
    checker([2, 3, 1], [3, 1, 2])  # [1, 2, 3]
    checker([1, 1], [1, 1])
    checker([5, 1, 1], [1, 1, 5])
