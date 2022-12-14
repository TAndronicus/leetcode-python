from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        currentIndex, jumps = 0, 0
        while True:
            jumps += 1
            if currentIndex + nums[currentIndex] >= len(nums) - 1:
                break
            maxReachMovement, maxReach = 0, 0
            for i in range(1, nums[currentIndex] + 1):
                reach = i + nums[currentIndex + i]
                if reach > maxReach:
                    maxReachMovement, maxReach = i, reach
            currentIndex += maxReachMovement
        return jumps


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]) == 2)
    print(s.jump([2, 3, 0, 1, 4]) == 2)
    print(s.jump([0]) == 0)
