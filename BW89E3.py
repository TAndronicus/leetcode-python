import math
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxAv = nums[0]
        cumSum = nums[0]
        for i in range(1, len(nums)):
            cumSum += nums[i]
            maxAv = max(maxAv, math.ceil(cumSum / (i + 1)))
        return maxAv


if __name__ == '__main__':
    s = Solution()
    print(s.minimizeArrayValue([1, 3, 5, 9]) == 5)
    print(s.minimizeArrayValue([1, 3, 5]) == 3)
    print(s.minimizeArrayValue([1, 9, 5, 5]) == 5)
    print(s.minimizeArrayValue([1, 9, 6, 5]) == 6)
    print(s.minimizeArrayValue([10, 1]) == 10)
