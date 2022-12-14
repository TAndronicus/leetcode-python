from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        while len(nums) > 1 and nums[0] == nums[-1]:
            del nums[-1]
        start, end = 0, len(nums) - 1
        while end - start > 1:
            midIndex = start + int((end - start) / 2)
            mid = nums[midIndex]
            if mid == target:
                return True
            if target > mid:
                if (mid > nums[end]) or (target <= nums[end]):
                    start = midIndex
                else:
                    end = midIndex
            else:
                if (mid <= nums[end]) or (target > nums[end]):
                    end = midIndex
                else:
                    start = midIndex
        if nums[start] == target:
            return True
        elif nums[end] == target:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.search([1, 2, 3, 0, 1, 1], 1))
    print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(not s.search([2, 5, 6, 0, 0, 1, 2], 3))
    print(not s.search([1, 2, 3, 4, 5, 6], 7))
    print(not s.search([1, 2, 3, 4, 5, 6], 0))
    print(s.search([1, 2, 3, 0, 1, 1], 0))
    print(s.search([5, 0, 0, 0, 1, 1], 5))
    print(s.search([5, 0, 0, 0, 1, 1], 1))
    print(s.search([5, 0, 0, 0, 1, 1], 0))
    print(s.search([1, 2, 3, 4, 5, 6, 7, 0], 1))
    print(s.search([1, 2, 3, 4, 5, 6, 7, 0], 0))
    print(s.search([1, 2, 3, 4, 5, 6, 7, 0], 7))
    print(s.search([0, 2, 2], 0))
