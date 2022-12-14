from typing import List


def search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while end - start > 1:
        midIndex = start + int((end - start) / 2)
        mid = nums[midIndex]
        if mid == target:
            return midIndex
        if target > mid:
            if (mid > nums[end]) or (target <= nums[end]):
                start = midIndex
            else:
                end = midIndex
        else:
            if (mid < nums[end]) or (target > nums[end]):
                end = midIndex
            else:
                start = midIndex
    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    else:
        return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
    print(search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
    print(search([1], 0) == -1)
    print(search([1, 3, 5], 1) == 0)
    print(search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4)
    print(search([1, 3, 5], 5) == 2)
    print(search([3, 5, 1], 1) == 2)
