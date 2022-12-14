from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        seeds = {}
        targets = {}
        maxVal, minTarget = 1, 1000000000
        nums.sort()
        for target in nums:
            rem = target % space
            if rem not in seeds:
                seeds[rem] = 1
                targets[rem] = target
            else:
                seeds[rem] += 1
            if seeds[rem] > maxVal or (seeds[rem] == maxVal and targets[rem] < minTarget):
                maxVal = seeds[rem]
                minTarget = targets[rem]
        return minTarget


if __name__ == '__main__':
    s = Solution()
    print(s.destroyTargets([3, 7, 8, 1, 1, 5], 2))
    print(s.destroyTargets([1, 3, 5, 2, 4, 6], 2))
    print(s.destroyTargets([6, 2, 5], 100))
    print(s.destroyTargets([2, 4, 6, 3, 5, 7, 9, 12, 15], 3))
