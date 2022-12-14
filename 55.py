from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        currentIndex = 0
        while True:
            if currentIndex + nums[currentIndex] >= len(nums) - 1:
                break
            maxReachMovement, maxReach = 0, 0
            for i in range(1, nums[currentIndex] + 1):
                reach = i + nums[currentIndex + i]
                if reach > maxReach:
                    maxReachMovement, maxReach = i, reach
            if maxReach == 0:
                return False
            currentIndex += maxReachMovement
        return True

    def canJump2(self, nums: List[int]) -> bool:
        toJump = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= toJump:
                toJump = 1
            else:
                toJump += 1
        return toJump == 1


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(not s.canJump([3, 2, 1, 0, 4]))
    print(s.canJump2([2, 3, 1, 1, 4]))
    print(not s.canJump2([3, 2, 1, 0, 4]))
