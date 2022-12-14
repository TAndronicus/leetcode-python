from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    start, end, mid = 0, len(nums) - 1, 0
    while True:
        mid = start + int((end - start) / 2)
        if end <= start + 1:
            break
        if nums[mid] == target:
            break
        elif nums[mid] > target:
            end = mid
        else:
            start = mid
    if (mid > 0) and (nums[mid - 1] == target):
        mid -= 1
    elif (mid < len(nums) - 1) and (nums[mid + 1] == target):
        mid += 1
    elif nums[mid] != target:
        return [-1, -1]
    first, last = mid, mid
    for _ in range(mid, 0, -1):
        if nums[first - 1] != target:
            break
        first -= 1
    for _ in range(mid, len(nums) - 1):
        if nums[last + 1] != target:
            break
        last += 1
    return [first, last]


if __name__ == '__main__':
    print(searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
    print(searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
    print(searchRange([], 0) == [-1, -1])
    print(searchRange([1], 0) == [-1, -1])
    print(searchRange([1], 0) == [-1, -1])
    print(searchRange([0], 0) == [0, 0])
    print(searchRange([3, 3, 3, 3], 3) == [0, 3])
    print(searchRange([1, 3], 1) == [0, 0])
    print(searchRange([1, 3, 3], 1) == [0, 0])
    print(searchRange([1, 3, 3, 3], 1) == [0, 0])
    print(searchRange([1, 3], 3) == [1, 1])
    print(searchRange([1, 1, 3], 3) == [2, 2])
    print(searchRange([1, 1, 1, 3], 3) == [3, 3])
